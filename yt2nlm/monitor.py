"""Market monitor: ONE rotating NotebookLM notebook accumulating market
feedback on a topic, with per-batch novelty digests and a local
engagement-weighted theme ledger.

Rotation doctrine (from patent-workbench's mega-screen): the notebook keeps a
handful of permanent sources (Frame + per-platform Archive docs); every batch
source is temporary — uploaded, novelty-queried, merged into its platform
archive, then DELETED. A 3350-video channel fits through the 50-source cap.

Resume-first: every run first finishes whatever the previous run left behind
(`collected` -> upload, `uploaded` -> query, `digested` -> merge), so quota
pauses (RESOURCE_EXHAUSTED -> exit 75) and Ctrl-C never lose work.
"""

from __future__ import annotations

import json
import os
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

from . import batch_fmt, discovery, ledger, nlm
from .state import STATE_DIR
from .youtube import fetch_video, list_channel_videos

REPORTS_DIR = Path(__file__).resolve().parent.parent / "reports"

CONFIG_DEFAULTS = {
    "channels": [], "subreddits": [], "apps": [], "urls": [],
    "searches": [],
    "search": {"per_query": 15, "max_probe": 40, "min_comments": 200},
    "per_channel_videos": 5,
    "channel_backfill_per_run": 15,   # deep lane: full-history walk, one channel/run
    "auto_promote_channels": {"min_videos": 2},
    "max_comments_per_video": 500,
    "max_videos_per_run": 25,
    "include_shorts": True,
    "recheck_days": 90,
    "max_recheck": 15,
    "archive_roll_words": 400_000,
    "pace": 2.0,
    "score_weights": ledger.DEFAULT_WEIGHTS,
    "novelty_prompt": "",           # override of the built-in template
    "reddit": {"listing": "top", "time": "week", "max_posts": 5,
               "max_comments": 200},
    "app_reviews": {"per_app": 40},
    "competitors": ["thesaurus.com", "WordHippo", "Power Thesaurus",
                    "QuillBot", "Merriam-Webster", "wordreference"],
    "trend_keywords": [],
    "transcripts": {"enabled": True, "backfill_per_run": 10},
    "site": "anotherwordfor.net (English synonyms / vocabulary site)",
}

NOVELTY_PROMPT = """You are checking a new batch of market feedback (YouTube/Reddit/app-review comments) for novelty.
The source titled "{batch_title}" is the NEW batch. All other sources are
the ACCUMULATED knowledge; the source starting with "Frame" defines the
topics we track.

Known themes so far (id — label):
{theme_list}

Section 1 — NEW. List ONLY points from "{batch_title}" that are not already
present in the other sources and do not match any known theme above. One
bullet per point: start with a category tag (need|works|idea|complaint) and
a sentiment tag [pos|neg|mixed], then a short paraphrase, then a short quote
preserving its 👍N count, and end the bullet with
[videos: <Video ID(s) from the batch section headers>].

Section 2 — REPEATED. For each point in "{batch_title}" that matches a known
theme, one line: "REPEATED: <theme id> — <5-word confirmation> [videos: <Video ID(s)>]".

Section 3 — QUESTIONS. Literal questions users ask in "{batch_title}"
(content/SEO ideas), one line each:
"QUESTION: <the question, lightly cleaned> [videos: <Video ID(s)>]".

Section 4 — COMPETITORS. For each mention in "{batch_title}" of a tool such
as {competitors}, one line:
"COMPETITOR: <name> — <praise|complaint> — <short point> [videos: <Video ID(s)>]".

End with: "COVERED: <n> repeated, <m> new."
"""

PROPOSALS_PROMPT = """You are a product strategist for {site}.
Ground yourself ONLY in this notebook's sources (accumulated market feedback:
comments, transcripts, reviews; the Frame source defines our angle).

Our current top themes ranked by audience weight (views/comments/engagement):
{theme_table}

Produce a concrete, prioritized proposal list for {site}:
1. FEATURES — what to build, each tied to the theme id(s) it serves.
2. CONTENT/SEO — pages or content formats to create, with the user questions
   they answer.
3. POSITIONING — what to say differently from competitors users complain about.
Be specific and grounded; cite theme ids like (T012). Max ~600 words.
"""

QUERY_SAFE_TOTAL = 5000            # NotebookLM rejects longer questions


class QuotaExhausted(RuntimeError):
    pass


def _quota_guard(exc: Exception) -> None:
    msg = str(exc)
    if "RESOURCE_EXHAUSTED" in msg or "quota" in msg.lower():
        raise QuotaExhausted(msg) from exc


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


# --------------------------------------------------------------------------- #
# Live progress (patent-workbench style): every step heartbeats into
# reports/<key>/progress.json; the /monitor dashboard polls it.
# --------------------------------------------------------------------------- #
_PROG: dict = {}
_PROG_LOCK = threading.Lock()


def progress_init(cfg: dict, command: str) -> None:
    global _PROG
    now = datetime.now(timezone.utc).isoformat()
    _PROG = {"path": report_dir(cfg) / "progress.json",
             "run": {"command": command, "status": "running",
                     "started_at": now, "step_changed_at": now,
                     "pid": os.getpid(), "phase": "starting", "detail": "",
                     "cur": None, "total": None, "batch_id": ""}}
    _progress_write()
    # Heartbeat thread: long blocking steps (a 5-min Gemini query, a heavy
    # yt-dlp fetch) must not read as "process died" — updated_at is stamped
    # every 30 s while the process lives; step_changed_at moves only when the
    # actual step changes, so a genuine stall is still visible.
    threading.Thread(target=_heartbeat, daemon=True).start()


def _heartbeat() -> None:
    while True:
        time.sleep(30)
        with _PROG_LOCK:
            if not _PROG or _PROG["run"]["status"] != "running":
                return
            _progress_write_locked()


def _progress_write_locked() -> None:
    _PROG["run"]["updated_at"] = datetime.now(timezone.utc).isoformat()
    tmp = _PROG["path"].with_suffix(".json.tmp")
    tmp.write_text(json.dumps(_PROG["run"], ensure_ascii=False))
    os.replace(tmp, _PROG["path"])


def _progress_write() -> None:
    if not _PROG:
        return
    with _PROG_LOCK:
        _progress_write_locked()


def progress(phase: str, detail: str = "", cur: int | None = None,
             total: int | None = None, **extra) -> None:
    if not _PROG:
        return
    with _PROG_LOCK:
        run = _PROG["run"]
        if (phase, detail[:200], cur) != (run["phase"], run["detail"],
                                          run["cur"]):
            run["step_changed_at"] = datetime.now(timezone.utc).isoformat()
        run.update({"phase": phase, "detail": detail[:200],
                    "cur": cur, "total": total, **extra})
        _progress_write_locked()


def progress_end(status: str, detail: str = "") -> None:
    if not _PROG:
        return
    with _PROG_LOCK:
        _PROG["run"].update({"status": status, "phase": status,
                             "detail": detail[:300], "cur": None,
                             "total": None})
        _progress_write_locked()


# --------------------------------------------------------------------------- #
# Config / state
# --------------------------------------------------------------------------- #
def load_config(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        cfg = json.load(fh)
    merged = dict(CONFIG_DEFAULTS)
    for k, v in cfg.items():
        if isinstance(v, dict) and isinstance(merged.get(k), dict):
            merged[k] = {**merged[k], **v}
        else:
            merged[k] = v
    if not merged.get("key"):
        raise RuntimeError(f"config {path} has no 'key'")
    return merged


def state_path(cfg: dict) -> Path:
    return STATE_DIR / f"{cfg['key']}.json"


def load_state(cfg: dict) -> dict:
    p = state_path(cfg)
    if p.exists():
        st = json.loads(p.read_text())
    else:
        st = {"key": cfg["key"], "notebook_id": "", "notebook_title": "",
              "frame_source_id": "", "archives": {}, "videos": {},
              "urls": {}, "batches": [], "updated_at": ""}
    st.setdefault("channels_auto", [])
    st.setdefault("backfill_cursor", 0)
    return st


# --------------------------------------------------------------------------- #
# Run lock: the always-on runner container and manual/agent runs share the
# bind-mounted state dir. PIDs don't cross container namespaces, so liveness
# = the progress.json heartbeat, not /proc.
# --------------------------------------------------------------------------- #
def acquire_lock(cfg: dict) -> Path:
    lock = STATE_DIR / f".{cfg['key']}.lock"
    if lock.exists():
        hb_age = 1e9
        prog = report_dir(cfg) / "progress.json"
        try:
            data = json.loads(prog.read_text())
            hb = datetime.fromisoformat(data["updated_at"])
            hb_age = (datetime.now(timezone.utc) - hb).total_seconds()
            running = data.get("status") == "running"
        except Exception:
            running = False
        if running and hb_age < 600:
            raise RuntimeError(
                f"another monitor run is ACTIVE (heartbeat {int(hb_age)}s ago) "
                f"— refusing to run concurrently. Lock: {lock}")
        lock.unlink()                  # stale — previous run died
    lock.write_text(str(os.getpid()))
    return lock


def release_lock(cfg: dict) -> None:
    (STATE_DIR / f".{cfg['key']}.lock").unlink(missing_ok=True)


def save_state(cfg: dict, state: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = datetime.now(timezone.utc).isoformat()
    p = state_path(cfg)
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2))
    os.replace(tmp, p)


def report_dir(cfg: dict) -> Path:
    d = REPORTS_DIR / cfg["key"]
    d.mkdir(parents=True, exist_ok=True)
    return d


# --------------------------------------------------------------------------- #
# init
# --------------------------------------------------------------------------- #
FRAME_TEMPLATE = """# Frame — {title}

(DRAFT — refine together with the user before heavy collection.)

Topic: the market around English vocabulary / synonyms / word-choice tools,
to guide what anotherwordfor.net should build, write, and propose.

We track, per batch of market feedback:
1. NEEDS — what users say they lack: example sentences, context, nuance
   between near-synonyms, register/formality, collocations, pronunciation,
   offline/mobile access, speed, no ads.
2. WHAT WORKS — tools/methods users praise and why (comprehensible input,
   spaced repetition, specific sites/apps).
3. IDEAS — feature requests, "I wish there was..." statements.
4. COMPLAINTS — what users hate about existing tools (thesaurus.com,
   WordHippo, Power Thesaurus, QuillBot, dictionaries, AI chatbots).
5. SIGNALS — monetization, traffic sources, search phrases people use.
"""


def cmd_init(cfg: dict, state: dict) -> None:
    if state.get("notebook_id"):
        print(f"already initialized: notebook {state['notebook_id']} "
              f"({state.get('notebook_title')})")
        return
    frame_path = report_dir(cfg) / "FRAME.md"
    if not frame_path.exists():
        frame_path.write_text(
            FRAME_TEMPLATE.format(title=cfg.get("notebook_title", cfg["key"])))
        print(f"wrote frame template -> {frame_path} (edit it, then re-run --init "
              f"or continue: the source can be refreshed later)")
    title = cfg.get("notebook_title") or f"Monitor — {cfg['key']}"
    nb = nlm.create_notebook(title)
    state["notebook_id"], state["notebook_title"] = nb["id"], title
    save_state(cfg, state)
    sid = nlm.add_text(nb["id"], frame_path.read_text(),
                       f"Frame — {title}")
    state["frame_source_id"] = sid or ""
    save_state(cfg, state)
    print(f"notebook created: {nb['id']} «{title}», frame source {sid}")


# --------------------------------------------------------------------------- #
# enumeration + collection
# --------------------------------------------------------------------------- #
def _age_days(iso: str) -> float:
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        return 1e9
    return (datetime.now(timezone.utc) - dt).total_seconds() / 86400


def enumerate_targets(cfg: dict, state: dict) -> list[dict]:
    """Ordered list of {video_id, url, why} to fetch this run."""
    targets: dict[str, dict] = {}

    def put(vid: str, url: str, why: str) -> None:
        if vid and vid not in targets:
            targets[vid] = {"video_id": vid, "url": url, "why": why}

    # 1) channels (uploads + shorts): config channels + auto-promoted ones
    all_channels = list(dict.fromkeys(cfg["channels"] + state["channels_auto"]))
    for ci, ch in enumerate(all_channels, 1):
        progress("channels", ch, ci, len(all_channels))
        feeds = [ch]
        if cfg["include_shorts"]:
            base = ch if ch.startswith("http") else \
                f"https://www.youtube.com/@{ch.lstrip('@')}"
            feeds.append(base.rstrip("/") + "/shorts")
        for feed in feeds:
            try:
                for v in list_channel_videos(feed, limit=cfg["per_channel_videos"]):
                    put(v["video_id"], v["url"], f"channel:{ch}")
            except Exception as exc:
                print(f"  ! channel listing failed for {feed}: {exc}",
                      file=sys.stderr)

    # 1b) DEEP BACKFILL: walk ONE channel's FULL upload history per run
    # (rotating cursor) so entire 3000-video channels get ingested over time.
    deep = cfg["channel_backfill_per_run"]
    if deep and all_channels:
        ch = all_channels[state["backfill_cursor"] % len(all_channels)]
        progress("deep-backfill", f"full history of {ch}")
        try:
            full = list_channel_videos(ch)          # flat listing, no limit
            unknown = [v for v in full
                       if v["video_id"] not in state["videos"]
                       and v["video_id"] not in targets]
            for v in unknown[:deep]:
                put(v["video_id"], v["url"], f"deep:{ch}")
            print(f"  deep-backfill {ch}: {len(full)} videos total, "
                  f"{len(unknown)} not yet collected, taking {min(deep, len(unknown))}")
            if len(unknown) <= deep:                # channel exhausted → next
                state["backfill_cursor"] += 1
        except Exception as exc:
            print(f"  ! deep-backfill failed for {ch}: {exc}", file=sys.stderr)
            state["backfill_cursor"] += 1

    # 2) whole-YouTube searches (probe unknown candidates for comment volume)
    s = cfg["search"]
    cands: dict[str, dict] = {}
    for qi, q in enumerate(cfg["searches"], 1):
        progress("search", f"«{q}»", qi, len(cfg["searches"]))
        try:
            for e in discovery.flat_search(q, s["per_query"]):
                cands.setdefault(e["video_id"], e)
        except Exception as exc:
            print(f"  ! search failed for {q!r}: {exc}", file=sys.stderr)
    fresh = [c for c in cands.values()
             if c["video_id"] not in state["videos"] and c["video_id"] not in targets]
    fresh.sort(key=lambda c: c.get("view_count") or 0, reverse=True)
    probe_list = fresh[: s["max_probe"]]
    for pi, c in enumerate(probe_list, 1):
        progress("probe", (c.get("title") or c["video_id"])[:80],
                 pi, len(probe_list))
        try:
            m = discovery.probe(c["video_id"])
        except Exception as exc:
            print(f"  ! probe failed {c['video_id']}: {exc}", file=sys.stderr)
            continue
        if (m.get("comment_count") or 0) >= s["min_comments"]:
            put(m["video_id"], m["url"], "search")
            # Probe counts are the TRUE totals; a capped comment fetch later
            # reports only the downloaded count — keep the probe as floor.
            targets[m["video_id"]]["probe"] = {
                "view_count": m.get("view_count"),
                "comment_count": m.get("comment_count")}
        time.sleep(0.8)
    # known search finds are re-checked via the re-check lane below

    # 3) re-check known videos for NEW comments (oldest checked first)
    known = [(vid, rec) for vid, rec in state["videos"].items()
             if vid not in targets
             and _age_days(rec.get("first_seen", "")) <= cfg["recheck_days"]]
    known.sort(key=lambda kv: kv[1].get("last_checked", ""))
    for vid, rec in known[: cfg["max_recheck"]]:
        put(vid, rec.get("url") or f"https://www.youtube.com/watch?v={vid}",
            "recheck")

    return list(targets.values())


def collect(cfg: dict, state: dict, targets: list[dict], *,
            max_videos: int | None, dry_run: bool = False):
    """Fetch targets, dedupe by cid, return batch sections."""
    cap = max_videos or cfg["max_videos_per_run"]
    sections = []
    n_new_total = 0
    for n, t in enumerate(targets[:cap], 1):
        vid = t["video_id"]
        rec = state["videos"].get(vid)
        progress("collect", f"{t['why']}: {(rec or {}).get('title', vid)[:70]}",
                 n, min(cap, len(targets)), new_comments=n_new_total)
        mode = "all" if rec else "top"      # re-checks: newest first
        try:
            meta = fetch_video(t["url"], comments_mode=mode,
                               max_comments=cfg["max_comments_per_video"])
        except Exception as exc:
            print(f"  [{n}] fetch failed {vid}: {exc}", file=sys.stderr)
            continue
        seen = set(rec["seen_cids"]) if rec else set()
        new = [c for c in meta.comments if c.cid and c.cid not in seen]
        roots = {c.cid: c for c in meta.comments
                 if (c.parent == "root" or not c.parent)}
        print(f"  [{n}/{min(cap, len(targets))}] {t['why']:18} "
              f"{len(new):4} new / {len(meta.comments):4} fetched  "
              f"{(meta.title or vid)[:60]}")
        if dry_run:
            n_new_total += len(new)
            time.sleep(cfg["pace"])
            continue
        if rec is None:
            rec = {"channel": meta.channel, "title": meta.title, "url": meta.url,
                   "channel_handle": meta.channel_handle,
                   "first_seen": now_utc(), "seen_cids": [],
                   "transcript_done": False, "is_short": "/shorts/" in t["url"]}
            state["videos"][vid] = rec
        elif meta.channel_handle and not rec.get("channel_handle"):
            rec["channel_handle"] = meta.channel_handle
        # fetch_video caps comments, and yt-dlp then reports the DOWNLOADED
        # count as comment_count — probe (metadata-only) for the TRUE total,
        # which drives the relevance/engagement weighting.
        probe_info = t.get("probe")
        if probe_info is None:
            try:
                probe_info = discovery.probe(vid)
            except Exception:
                probe_info = {}
        meta.view_count = (meta.view_count or probe_info.get("view_count")
                           or rec.get("view_count"))
        meta.comment_count = max(meta.comment_count or 0,
                                 probe_info.get("comment_count") or 0,
                                 rec.get("comment_count") or 0) or None
        rec.update({"view_count": meta.view_count,
                    "comment_count": meta.comment_count,
                    "last_checked": now_utc()})
        if new:
            rec["seen_cids"] = list(seen | {c.cid for c in new})
            sections.append((meta, new, roots))
            n_new_total += len(new)
        time.sleep(cfg["pace"])
    if not dry_run:
        auto_promote_channels(cfg, state)
    return sections, n_new_total


def auto_promote_channels(cfg: dict, state: dict) -> None:
    """Self-widening net: a channel that surfaced >= min_videos times via
    search/deep lanes gets its whole feed monitored from now on."""
    ap = cfg["auto_promote_channels"]
    if not ap:
        return
    known = {c.lstrip("@").lower()
             for c in cfg["channels"] + state["channels_auto"]}
    by_handle: dict[str, int] = {}
    for vid, rec in state["videos"].items():
        if vid.startswith(("r-", "app-")):
            continue
        h = rec.get("channel_handle")
        if h:
            by_handle[h] = by_handle.get(h, 0) + 1
    for handle, n in sorted(by_handle.items(), key=lambda kv: -kv[1]):
        if n >= ap.get("min_videos", 2) and handle.lstrip("@").lower() not in known:
            state["channels_auto"].append(handle)
            known.add(handle.lstrip("@").lower())
            print(f"  auto-promoted channel {handle} ({n} videos collected)")


# --------------------------------------------------------------------------- #
# batch lifecycle
# --------------------------------------------------------------------------- #
def _new_batch_id(state: dict) -> str:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    n = sum(1 for b in state["batches"] if b["id"].startswith(today))
    return f"{today}{chr(ord('a') + n)}"


def _batch_title(batch: dict) -> str:
    return (f"Batch {batch['id']} — {batch['n_comments']} new comments / "
            f"{batch['n_videos']} videos")


def upload_batch(cfg: dict, state: dict, batch: dict) -> None:
    progress("upload", _batch_title(batch), batch_id=batch["id"])
    text = Path(batch["md_path"]).read_text()
    sid = nlm.add_text(state["notebook_id"], text, _batch_title(batch))
    if not sid:
        raise nlm.NlmError("batch source id not captured after add")
    batch["source_id"] = sid
    batch["status"] = "uploaded"
    save_state(cfg, state)
    print(f"uploaded batch {batch['id']} as source {sid}")


def wait_ready(source_id: str, *, tries: int = 30, gap: float = 20.0) -> bool:
    """presence != readiness: poll raw content until non-empty."""
    for i in range(tries):
        if nlm.source_content(source_id):
            return True
        progress("ingest-wait", f"source {source_id[:8]}… not ready yet",
                 i + 1, tries)
        time.sleep(gap)
    return False


def _looks_like_answer(answer: str) -> bool:
    if len(answer) < 80:
        return False
    return "COVERED:" in answer or "\n-" in answer or "\n*" in answer \
        or "REPEATED:" in answer


def query_batch(cfg: dict, state: dict, batch: dict) -> None:
    if not wait_ready(batch["source_id"]):
        raise nlm.NlmError(f"batch source {batch['source_id']} never became ready")
    led = ledger.load(report_dir(cfg))
    template = cfg["novelty_prompt"] or NOVELTY_PROMPT
    comp = ", ".join(cfg["competitors"])

    def build(limit):
        tl = ledger.theme_list_for_prompt(led, limit=limit)
        return template.format(batch_title=_batch_title(batch),
                               theme_list=tl or "(none yet — first batch)",
                               competitors=comp)
    q = build(40)
    if len(q) > QUERY_SAFE_TOTAL:      # shrink the theme list, never overflow
        q = build(25)
    answer = None
    for attempt in (1, 2):
        progress("novelty-query", f"attempt {attempt} (Gemini, may take minutes)",
                 attempt, 2, batch_id=batch["id"])
        try:
            r = nlm.query(state["notebook_id"], q)
        except nlm.NlmError as exc:
            _quota_guard(exc)
            print(f"  query attempt {attempt} failed: {exc}", file=sys.stderr)
            continue
        if _looks_like_answer(r["answer"]):
            answer = r["answer"]
            break
        print(f"  attempt {attempt}: non-answer ({len(r['answer'])} chars) — "
              f"NOT persisting", file=sys.stderr)
    if answer is None:
        raise nlm.NlmError("no valid novelty answer; batch stays 'uploaded' "
                           "(next run retries the query)")

    digest_path = report_dir(cfg) / f"digest-{batch['id']}.md"
    digest_path.write_text(f"# Digest — {_batch_title(batch)}\n"
                           f"Collected {batch.get('collected_at', '?')}, "
                           f"digested {now_utc()}\n\n{answer}\n")
    batch["digest_path"] = str(digest_path)

    batch_videos = set(batch.get("video_ids", []))
    parsed = ledger.parse_digest(answer, batch["id"], batch_videos)
    ledger.apply(led, parsed, batch["id"])
    ledger.recompute_scores(led, state, cfg["score_weights"])
    ledger.save(report_dir(cfg), led)
    ledger.render_ledger_md(report_dir(cfg), led)
    ledger.render_scoreboard_md(report_dir(cfg), led)
    ledger.render_questions_md(report_dir(cfg), led)
    ledger.render_competitors_md(report_dir(cfg), led)

    batch["status"] = "digested"
    save_state(cfg, state)
    print(f"digested batch {batch['id']}: {len(parsed['new'])} new points, "
          f"{len(parsed['repeats'])} repeats, {len(parsed['questions'])} "
          f"questions, {len(parsed['competitors'])} competitor mentions -> "
          f"{digest_path.name}, SCOREBOARD.md updated")


# --------------------------------------------------------------------------- #
# merge & rotate (archives)
# --------------------------------------------------------------------------- #
def _archive(state: dict, platform: str) -> dict:
    return state["archives"].setdefault(
        platform, {"vol": 1, "source_id": "", "words": 0, "path": ""})


def _archive_path(cfg: dict, platform: str, vol: int) -> Path:
    d = report_dir(cfg) / "archives"
    d.mkdir(parents=True, exist_ok=True)
    return d / f"{platform}-vol{vol}.md"


def merge_into_archive(cfg: dict, state: dict, platform: str,
                       text: str, *, delete_after: list[str] = ()) -> None:
    """Append text to the platform archive, re-upload it, verify, THEN delete
    the superseded sources (old archive version + the merged batch source)."""
    arc = _archive(state, platform)
    progress("merge-archive", f"{platform} vol.{arc['vol']}")
    words = len(text.split())
    if arc["words"] and arc["words"] + words > cfg["archive_roll_words"]:
        arc["vol"] += 1
        arc["words"] = 0
        old_sid = ""                 # previous vol stays in the notebook
    else:
        old_sid = arc["source_id"]

    path = _archive_path(cfg, platform, arc["vol"])
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(text.rstrip() + "\n\n")
    arc["path"] = str(path)
    arc["words"] += words
    save_state(cfg, state)

    title = f"Archive {platform} vol.{arc['vol']} — {state.get('notebook_title', cfg['key'])}"
    sid = nlm.add_text(state["notebook_id"], path.read_text(), title)
    if not sid:
        raise nlm.NlmError(f"archive {platform} re-upload: id not captured")
    if not wait_ready(sid):
        raise nlm.NlmError(f"archive {platform} source {sid} never became ready")
    arc["source_id"] = sid
    save_state(cfg, state)

    doomed = [s for s in [old_sid, *delete_after] if s]
    if doomed:
        gone = nlm.delete_sources(state["notebook_id"], doomed)
        missed = set(doomed) - set(gone)
        if missed:
            print(f"  ! could not confirm deletion of {missed}", file=sys.stderr)
    print(f"archive {platform} vol.{arc['vol']} now {arc['words']} words "
          f"(source {sid}); rotated out {len(doomed)} source(s)")


def merge_batch(cfg: dict, state: dict, batch: dict) -> None:
    text = Path(batch["md_path"]).read_text()
    merge_into_archive(cfg, state, "youtube-comments", text,
                       delete_after=[batch.get("source_id", "")])
    # Gemini's own conclusions accumulate in the notebook too: the digest
    # joins a growing "digests" archive source, so future novelty queries can
    # ground on past verdicts, not only on raw material.
    dp = batch.get("digest_path", "")
    if dp and Path(dp).exists():
        merge_into_archive(cfg, state, "digests", Path(dp).read_text())
    batch["status"] = "merged"
    save_state(cfg, state)


# --------------------------------------------------------------------------- #
# Transcript harvesting (free via NotebookLM: temp source -> content -> delete)
# --------------------------------------------------------------------------- #
def _pending_path(cfg: dict, platform: str) -> Path:
    d = report_dir(cfg) / "archives"
    d.mkdir(parents=True, exist_ok=True)
    return d / f"pending-{platform}.md"


def _flush_pending(cfg: dict, state: dict, platform: str) -> None:
    p = _pending_path(cfg, platform)
    if p.exists() and p.stat().st_size > 0:
        merge_into_archive(cfg, state, platform, p.read_text())
        p.write_text("")


def harvest_transcripts(cfg: dict, state: dict, *, limit: int) -> None:
    """Rotate videos through the notebook to extract transcripts for free:
    temp native YouTube source -> `source content` (zero quota) -> append to
    the local pending file -> delete the temp source. One archive re-upload
    per run, not per video. Crash-safe: pending file is flushed first."""
    _flush_pending(cfg, state, "youtube-transcripts")
    todo = [(vid, rec) for vid, rec in state["videos"].items()
            if not rec.get("transcript_done") and not vid.startswith(("r-", "app-"))]
    if not todo or limit <= 0:
        return
    pending = _pending_path(cfg, "youtube-transcripts")
    done = 0
    for ti, (vid, rec) in enumerate(todo[:limit], 1):
        progress("transcripts", rec.get("title", vid)[:70],
                 ti, min(limit, len(todo)))
        url = rec.get("url") or f"https://www.youtube.com/watch?v={vid}"
        try:
            sid = nlm.add_youtube(state["notebook_id"], url)
        except nlm.NlmError as exc:
            _quota_guard(exc)
            if "could not add" in str(exc).lower():
                rec["transcript_done"] = "unavailable"   # no subtitles — final
                save_state(cfg, state)
                print(f"  transcript {vid}: unavailable (no subtitles)")
                continue
            print(f"  transcript {vid}: add failed: {exc}", file=sys.stderr)
            continue
        if not sid:
            print(f"  transcript {vid}: source id not captured", file=sys.stderr)
            continue
        text = ""
        if wait_ready(sid, tries=15):
            text = nlm.source_content(sid)
        nlm.delete_sources(state["notebook_id"], [sid])
        if not text:
            rec["transcript_done"] = "unavailable"
            save_state(cfg, state)
            print(f"  transcript {vid}: no content after ingest")
            continue
        views = rec.get("view_count")
        head = (f"## {rec.get('title', vid)} — {rec.get('channel', '?')} — {vid}"
                f" — {views:,} views".replace(",", " ") if views else
                f"## {rec.get('title', vid)} — {rec.get('channel', '?')} — {vid}")
        with open(pending, "a", encoding="utf-8") as fh:
            fh.write(f"{head}\n\n{text.strip()}\n\n")
        rec["transcript_done"] = True
        save_state(cfg, state)
        done += 1
        print(f"  transcript {vid}: {len(text)} chars harvested")
    if done:
        _flush_pending(cfg, state, "youtube-transcripts")
    print(f"transcripts: {done} harvested, "
          f"{sum(1 for _, r in todo if not r.get('transcript_done'))} remaining")


def collect_articles(cfg: dict, state: dict) -> None:
    """Articles/blogs via the same rotation trick: native URL source ->
    content read-back -> archive -> delete. No scraper needed."""
    _flush_pending(cfg, state, "articles")
    new_urls = [u for u in cfg["urls"] if u not in state["urls"]]
    if not new_urls:
        return
    pending = _pending_path(cfg, "articles")
    for ui, url in enumerate(new_urls, 1):
        progress("articles", url[:90], ui, len(new_urls))
        try:
            sid = nlm.add_url(state["notebook_id"], url)
        except nlm.NlmError as exc:
            _quota_guard(exc)
            print(f"  article {url}: add failed: {exc}", file=sys.stderr)
            continue
        text = ""
        if sid and wait_ready(sid, tries=15):
            text = nlm.source_content(sid)
        if sid:
            nlm.delete_sources(state["notebook_id"], [sid])
        if not text:
            print(f"  article {url}: no content extracted", file=sys.stderr)
            continue
        title = text.strip().splitlines()[0][:120] if text.strip() else url
        with open(pending, "a", encoding="utf-8") as fh:
            fh.write(f"## {title}\n- URL: {url}\n\n{text.strip()}\n\n")
        state["urls"][url] = {"title": title, "kind": "article",
                              "added_at": now_utc()}
        save_state(cfg, state)
        print(f"  article harvested: {title[:60]} ({len(text)} chars)")
    _flush_pending(cfg, state, "articles")


# --------------------------------------------------------------------------- #
# Reddit + app-store reviews (rendered into the same batch, uniform records)
# --------------------------------------------------------------------------- #
def collect_reddit(cfg: dict, state: dict) -> tuple[list[str], int, list[str]]:
    """Returns (extra markdown sections, n new comments, item ids).
    Posts live in state['videos'] under 'r-<postid>' keys (channel=r/<sub>,
    comment_count=num_comments) so scoring/dashboard treat them uniformly."""
    subs = cfg["subreddits"]
    if not subs:
        return [], 0, []
    if not (os.environ.get("REDDIT_CLIENT_ID")
            and os.environ.get("REDDIT_CLIENT_SECRET")):
        print("  reddit: skipped (set REDDIT_CLIENT_ID/SECRET — see "
              "yt2nlm/adapters/reddit.py)", file=sys.stderr)
        return [], 0, []
    try:
        import praw
    except ImportError:
        print("  reddit: praw not installed — scripts/restore.sh",
              file=sys.stderr)
        return [], 0, []
    rcfg = cfg["reddit"]
    reddit = praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        user_agent=os.environ.get("REDDIT_USER_AGENT",
                                  "yt2nlm:monitor:0.1"),
        check_for_async=False)
    sections, total, ids = [], 0, []
    for si, sub in enumerate(subs, 1):
        progress("reddit", f"r/{sub}", si, len(subs))
        try:
            listing = getattr(reddit.subreddit(sub.lstrip("r/")), rcfg["listing"])
            kwargs = {"limit": rcfg["max_posts"]}
            if rcfg["listing"] == "top":
                kwargs["time_filter"] = rcfg["time"]
            posts = list(listing(**kwargs))
        except Exception as exc:
            print(f"  reddit r/{sub}: listing failed: {exc}", file=sys.stderr)
            continue
        for s in posts:
            key = f"r-{s.id}"
            rec = state["videos"].setdefault(key, {
                "channel": f"r/{s.subreddit}", "title": s.title,
                "url": f"https://www.reddit.com{s.permalink}",
                "first_seen": now_utc(), "seen_cids": [],
                "transcript_done": "n/a", "is_short": False})
            try:
                s.comments.replace_more(limit=0)
                flat = s.comments.list()[: rcfg["max_comments"]]
            except Exception as exc:
                print(f"  reddit {s.id}: comments failed: {exc}",
                      file=sys.stderr)
                continue
            seen = set(rec["seen_cids"])
            new = [c for c in flat if c.id not in seen]
            rec.update({"comment_count": s.num_comments,
                        "view_count": None,
                        "last_checked": now_utc()})
            if not new:
                continue
            rec["seen_cids"] = list(seen | {c.id for c in new})
            lines = [f"## [Reddit] {s.title} — r/{s.subreddit}",
                     f"- Post: https://www.reddit.com{s.permalink}",
                     f"- Video ID: {key}",
                     f"- score {s.score} · comments total {s.num_comments} · "
                     f"new in this batch: {len(new)}", ""]
            if s.selftext:
                lines += [s.selftext.strip()[:1500], ""]
            for c in new:
                author = str(c.author) if c.author else "[deleted]"
                lines.append(f"**{author}** (👍{c.score}) — "
                             f"https://www.reddit.com{c.permalink}")
                lines.append(f"  {(c.body or '').strip()}")
                lines.append("")
            sections.append("\n".join(lines))
            total += len(new)
            ids.append(key)
    return sections, total, ids


def collect_app_reviews(cfg: dict, state: dict) -> tuple[list[str], int, list[str]]:
    """Google Play reviews of competitor apps. Config `apps`: package names
    ('com.duolingo') or {'id':..., 'name':...}. Records under 'app-<pkg>'."""
    apps = cfg["apps"]
    if not apps:
        return [], 0, []
    try:
        from google_play_scraper import Sort, app as gp_app, reviews as gp_reviews
    except ImportError:
        print("  app reviews: google-play-scraper not installed",
              file=sys.stderr)
        return [], 0, []
    sections, total, ids = [], 0, []
    for ai, entry in enumerate(apps, 1):
        pkg = entry["id"] if isinstance(entry, dict) else entry
        name = entry.get("name", pkg) if isinstance(entry, dict) else pkg
        progress("app-reviews", name, ai, len(apps))
        key = f"app-{pkg}"
        try:
            meta = gp_app(pkg)
            revs, _ = gp_reviews(pkg, sort=Sort.NEWEST,
                                 count=cfg["app_reviews"]["per_app"])
        except Exception as exc:
            print(f"  app {pkg}: fetch failed: {exc}", file=sys.stderr)
            continue
        rec = state["videos"].setdefault(key, {
            "channel": f"app:{name}", "title": f"{meta.get('title', name)} "
            f"(Google Play reviews)",
            "url": f"https://play.google.com/store/apps/details?id={pkg}",
            "first_seen": now_utc(), "seen_cids": [],
            "transcript_done": "n/a", "is_short": False})
        seen = set(rec["seen_cids"])
        new = [r for r in revs if r["reviewId"] not in seen]
        rec.update({"comment_count": meta.get("reviews"),
                    "view_count": meta.get("installs") and
                    int(str(meta["installs"]).strip("+,").replace(",", "")
                        .replace("+", "") or 0),
                    "last_checked": now_utc()})
        if not new:
            continue
        rec["seen_cids"] = list(seen | {r["reviewId"] for r in new})
        lines = [f"## [App reviews] {meta.get('title', name)} — Google Play",
                 f"- App: https://play.google.com/store/apps/details?id={pkg}",
                 f"- Video ID: {key}",
                 f"- installs {meta.get('installs')} · rating "
                 f"{meta.get('score')} · reviews total {meta.get('reviews')} · "
                 f"new in this batch: {len(new)}", ""]
        for r in new:
            lines.append(f"**{r.get('userName', 'user')}** "
                         f"(★{r.get('score')} · 👍{r.get('thumbsUpCount', 0)})")
            lines.append(f"  {(r.get('content') or '').strip()}")
            lines.append("")
        sections.append("\n".join(lines))
        total += len(new)
        ids.append(key)
    return sections, total, ids


# --------------------------------------------------------------------------- #
# Proposals + Google Trends
# --------------------------------------------------------------------------- #
def cmd_proposals(cfg: dict, state: dict) -> None:
    led = ledger.load(report_dir(cfg))
    themes = sorted(led["themes"],
                    key=lambda t: t.get("metrics", {}).get("score", 0),
                    reverse=True)[:15]
    if not themes:
        raise RuntimeError("no themes yet — run the monitor first")
    rows = [f"{t['id']} [{t['category']}] score {t['metrics'].get('score', 0)} "
            f"(views {t['metrics'].get('views_sum', 0):,}, comments "
            f"{t['metrics'].get('comments_sum', 0):,}) — {t['label']}"
            for t in themes]
    q = PROPOSALS_PROMPT.format(site=cfg["site"], theme_table="\n".join(rows))
    if len(q) > QUERY_SAFE_TOTAL:
        q = PROPOSALS_PROMPT.format(site=cfg["site"],
                                    theme_table="\n".join(rows[:8]))
    r = nlm.query(state["notebook_id"], q, timeout=600)
    p = report_dir(cfg) / "PROPOSALS.md"
    stamp = f"\n\n---\n\n# Proposals — {now_utc()}\n\n{r['answer']}\n"
    with open(p, "a", encoding="utf-8") as fh:
        fh.write(stamp)
    print(f"proposals appended -> {p}")


def cmd_trends(cfg: dict, state: dict) -> None:
    """Best-effort Google Trends pull (unofficial API — may 429/break)."""
    led = ledger.load(report_dir(cfg))
    kws = list(cfg["trend_keywords"])
    if not kws:
        themes = sorted(led["themes"],
                        key=lambda t: t.get("metrics", {}).get("score", 0),
                        reverse=True)[:8]
        kws = [" ".join(t["label"].split()[:4]) for t in themes if t["label"]]
    if not kws:
        print("trends: no keywords (set trend_keywords in config)")
        return
    try:
        from pytrends.request import TrendReq
        pt = TrendReq(hl="en-US", tz=0)
        out = {}
        for i in range(0, len(kws), 5):
            chunk = kws[i:i + 5]
            pt.build_payload(chunk, timeframe="today 12-m")
            df = pt.interest_over_time()
            for kw in chunk:
                if kw in df:
                    out[kw] = {"dates": [d.strftime("%Y-%m-%d")
                                         for d in df.index],
                               "values": [int(v) for v in df[kw]]}
            time.sleep(2)
    except Exception as exc:
        print(f"trends: pytrends failed ({exc}) — dashboard falls back to "
              f"trends.google.com links", file=sys.stderr)
        return
    p = report_dir(cfg) / "trends.json"
    p.write_text(json.dumps({"pulled_at": now_utc(), "series": out},
                            ensure_ascii=False))
    print(f"trends: {len(out)} keyword series -> {p}")


# --------------------------------------------------------------------------- #
# run
# --------------------------------------------------------------------------- #
def resume_pending(cfg: dict, state: dict, *, no_query: bool) -> None:
    for batch in state["batches"]:
        if batch["status"] == "collected":
            print(f"resuming batch {batch['id']}: upload")
            upload_batch(cfg, state, batch)
        if batch["status"] == "uploaded" and not no_query:
            print(f"resuming batch {batch['id']}: novelty query")
            query_batch(cfg, state, batch)
        if batch["status"] == "digested":
            print(f"resuming batch {batch['id']}: merge into archive")
            merge_batch(cfg, state, batch)


def cmd_run(cfg: dict, *, dry_run: bool = False, no_query: bool = False,
            max_videos: int | None = None) -> None:
    state = load_state(cfg)
    if not state.get("notebook_id"):
        raise RuntimeError("not initialized — run with --init first")

    if not dry_run:
        resume_pending(cfg, state, no_query=no_query)

    if not any(cfg[k] for k in ("channels", "searches", "subreddits", "apps")):
        raise RuntimeError(
            f"config has no channels/searches/subreddits/apps — add channel "
            f"handles to {cfg['key']}.config.json (channels: [\"@handle\", ...])")

    print("enumerating targets...")
    targets = enumerate_targets(cfg, state)
    print(f"{len(targets)} target videos "
          f"({sum(1 for t in targets if t['why'] == 'recheck')} re-checks)")

    sections, n_new = collect(cfg, state, targets,
                              max_videos=max_videos, dry_run=dry_run)
    if dry_run:
        print(f"dry-run: {n_new} new comments across {len(targets)} targets "
              f"(nothing written)")
        return

    extra_md, extra_ids = [], []
    for fn in (collect_reddit, collect_app_reviews):
        md, n, ids = fn(cfg, state)
        extra_md += md
        n_new += n
        extra_ids += ids
    if extra_md:
        save_state(cfg, state)

    if not sections and not extra_md:
        state["batches"].append({"id": _new_batch_id(state), "status": "empty",
                                 "n_comments": 0, "n_videos": 0,
                                 "collected_at": now_utc()})
        save_state(cfg, state)
        print("no new comments anywhere — empty batch recorded, no upload, "
              "no query")
        return

    batch_id = _new_batch_id(state)
    md = batch_fmt.render_batch(
        batch_id, cfg.get("notebook_title", cfg["key"]), now_utc(),
        sections, extra_sections=extra_md)
    md_path = report_dir(cfg) / f"batch-{batch_id}.md"
    md_path.write_text(md)
    batch = {"id": batch_id, "status": "collected",
             "n_comments": n_new, "n_videos": len(sections) + len(extra_ids),
             "video_ids": [m.video_id for m, _, _ in sections] + extra_ids,
             "collected_at": now_utc(),
             "md_path": str(md_path), "source_id": "", "digest_path": ""}
    state["batches"].append(batch)
    save_state(cfg, state)     # cids marked seen + md on disk in one step
    print(f"batch {batch_id}: {n_new} new comments / {batch['n_videos']} items "
          f"-> {md_path.name}")

    upload_batch(cfg, state, batch)
    if not no_query:
        query_batch(cfg, state, batch)
        merge_batch(cfg, state, batch)

    collect_articles(cfg, state)
    t = cfg["transcripts"]
    if t.get("enabled"):
        harvest_transcripts(cfg, state, limit=int(t.get("backfill_per_run", 0)))


def cmd(args) -> int:
    cfg = load_config(args.config)
    lock_taken = False

    def lock() -> None:
        nonlocal lock_taken
        acquire_lock(cfg)
        lock_taken = True

    try:
        if args.init:
            state = load_state(cfg)
            cmd_init(cfg, state)
            return 0
        if getattr(args, "proposals", False):
            lock()
            progress_init(cfg, "proposals")
            cmd_proposals(cfg, load_state(cfg))
            progress_end("done", "PROPOSALS.md updated")
            return 0
        if getattr(args, "trends", False):
            cmd_trends(cfg, load_state(cfg))
            return 0
        if getattr(args, "backfill_transcripts", None) is not None:
            state = load_state(cfg)
            if not state.get("notebook_id"):
                raise RuntimeError("not initialized — run with --init first")
            lock()
            progress_init(cfg, "backfill-transcripts")
            harvest_transcripts(cfg, state, limit=args.backfill_transcripts)
            progress_end("done", "transcript backfill finished")
            return 0
        if not args.dry_run:
            lock()
            progress_init(cfg, "run")
        cmd_run(cfg, dry_run=args.dry_run, no_query=args.no_query,
                max_videos=args.max_videos)
        progress_end("done", "cycle finished")
        return 0
    except QuotaExhausted as exc:
        progress_end("quota-paused",
                     "NotebookLM quota exhausted — re-run in 6-12 h, "
                     "resume is automatic")
        print(f"\nNotebookLM quota exhausted: {str(exc)[:200]}\n"
              f"State saved — re-run the same command in 6-12 h; "
              f"it resumes automatically.", file=sys.stderr)
        return 75                      # EX_TEMPFAIL
    except nlm.NlmError as exc:
        try:
            _quota_guard(exc)
        except QuotaExhausted:
            progress_end("quota-paused",
                         "NotebookLM quota exhausted — re-run in 6-12 h")
            print(f"\nNotebookLM quota exhausted: {str(exc)[:200]}\n"
                  f"State saved — re-run in 6-12 h.", file=sys.stderr)
            return 75
        progress_end("error", str(exc)[:250])
        raise
    except KeyboardInterrupt:
        progress_end("interrupted", "Ctrl-C — state saved, next run resumes")
        raise
    except Exception as exc:
        progress_end("error", str(exc)[:250])
        raise
    finally:
        if lock_taken:
            release_lock(cfg)
