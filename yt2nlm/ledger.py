"""Theme ledger: machine-readable record of every novelty digest, plus the
engagement-weighted scoring that ranks themes by audience weight.

Merge-never-wipe: entries are append-only; metrics/scores are DERIVED data
recomputed in full on every run from entries + the monitor state's per-video
view/comment counts (the patent-workbench "re-rank from stored coverage
without re-reading" pattern) — changing weights re-ranks everything for free.
"""

from __future__ import annotations

import json
import math
import re
import statistics
import sys
from pathlib import Path

DEFAULT_WEIGHTS = {"m": 1, "b": 1, "ch": 2, "l": 2, "v": 3, "c": 2, "e": 2}

_VIDEOS_TAG = re.compile(r"\[videos?:\s*([A-Za-z0-9_\-, ]+)\]")
_LIKES = re.compile(r"👍\s?(\d+)")
_CATEGORY = re.compile(r"^[\W`]{0,8}(need|works|idea|complaint)s?[`)\]]*\s*[:—–\-.]?\s*",
                       re.IGNORECASE)
# Keywords may arrive decorated (**QUESTION**:, `REPEATED`: …) — allow md noise.
_DECOR = r"[*`_]*\s*:\s*"
_REPEATED = re.compile(r"REPEATED" + _DECOR + r"\**\s*(T\d+)\s*\**\s*[—–\-]\s*(.+)",
                       re.IGNORECASE)
_QUESTION = re.compile(r"QUESTION" + _DECOR + r"(.+)", re.IGNORECASE)
_COMPETITOR = re.compile(
    r"COMPETITOR" + _DECOR + r"\**\s*(.+?)\s*\**\s*[—–\-]\s*\**`?\s*"
    r"(praise|complaint|mixed)\s*`?\**\s*[—–\-]\s*(.+)", re.IGNORECASE)
_SENTIMENT = re.compile(r"\[\s*(pos|neg|mixed)\s*\]", re.IGNORECASE)
_BULLET = re.compile(r"^\s*[-*•]\s+(.+)")


def load(dirpath: Path) -> dict:
    p = dirpath / "ledger.json"
    if p.exists():
        led = json.loads(p.read_text())
    else:
        led = {"next_theme_seq": 1, "themes": []}
    led.setdefault("questions", [])
    led.setdefault("competitors", [])
    return led


def save(dirpath: Path, led: dict) -> None:
    p = dirpath / "ledger.json"
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(led, ensure_ascii=False, indent=2))
    tmp.replace(p)


def theme_list_for_prompt(led: dict, *, limit: int = 40) -> str:
    themes = sorted(led["themes"],
                    key=lambda t: t.get("metrics", {}).get("score", 0),
                    reverse=True)[:limit]
    return "\n".join(f"{t['id']} — {t['label']}" for t in themes)


# --------------------------------------------------------------------------- #
# Parsing
# --------------------------------------------------------------------------- #
def _extract_videos(text: str, allowed: set[str]) -> tuple[list[str], str]:
    """Pull [videos: ...] ids out of a line; ids not in the batch are dropped."""
    ids: list[str] = []
    for mtag in _VIDEOS_TAG.finditer(text):
        for raw in mtag.group(1).split(","):
            vid = raw.strip()
            if not vid:
                continue
            if allowed and vid not in allowed:
                print(f"  ledger: unknown video id {vid!r} in digest — dropped",
                      file=sys.stderr)
                continue
            ids.append(vid)
    clean = _VIDEOS_TAG.sub("", text).strip()
    return ids, clean


def parse_digest(answer: str, batch_id: str, batch_videos: set[str]) -> dict:
    """Split a novelty answer into new points, repeats, questions and
    competitor mentions."""
    new, repeats, questions, competitors = [], [], [], []
    in_new = True                       # sections 2-4 never feed NEW bullets
    for raw in answer.splitlines():
        line = raw.strip()
        if not line:
            continue
        rep = _REPEATED.search(line)
        if rep:
            vids, text = _extract_videos(rep.group(2), batch_videos)
            repeats.append({"theme_id": rep.group(1).upper(), "text": text,
                            "videos": vids,
                            "likes_sum": sum(int(x) for x in _LIKES.findall(line))})
            in_new = False
            continue
        qm = _QUESTION.search(line)
        if qm:
            vids, text = _extract_videos(qm.group(1), batch_videos)
            if len(text) > 8:
                questions.append({"text": text, "videos": vids})
            in_new = False
            continue
        cm = _COMPETITOR.search(line)
        if cm:
            vids, text = _extract_videos(cm.group(3), batch_videos)
            competitors.append({"name": cm.group(1).strip("*` "),
                                "kind": cm.group(2).lower(),
                                "text": text, "videos": vids})
            in_new = False
            continue
        sec = re.match(r"^#+\s*|^\*{0,2}Section\s*(\d)", line, re.IGNORECASE)
        if re.search(r"Section\s*(\d)", line, re.IGNORECASE):
            in_new = bool(re.search(r"Section\s*1", line, re.IGNORECASE))
            continue
        if line.upper().startswith("COVERED:"):
            in_new = False
            continue
        if sec and line.startswith("#"):
            continue
        b = _BULLET.match(raw)
        if not b or not in_new:
            continue
        text = b.group(1).strip()
        cat_m = _CATEGORY.match(text)
        category = (cat_m.group(1).lower() if cat_m else "other")
        if cat_m:
            text = text[cat_m.end():].lstrip("`*_ :—–-").strip() or text
        sent_m = _SENTIMENT.search(text)
        sentiment = sent_m.group(1).lower() if sent_m else ""
        text = _SENTIMENT.sub("", text).lstrip("`*_ :—–-").strip()
        vids, text = _extract_videos(text, batch_videos)
        if len(text) < 15:            # headers / noise, not a point
            continue
        new.append({"category": category, "sentiment": sentiment,
                    "text": text, "videos": vids,
                    "likes_sum": sum(int(x) for x in _LIKES.findall(raw))})
    return {"new": new, "repeats": repeats, "questions": questions,
            "competitors": competitors, "batch_id": batch_id}


def _label(text: str) -> str:
    plain = re.sub(r"[*_\"«»]", "", text).lstrip("`: —–-")
    plain = plain.split(" — ")[0].split(". ")[0]
    words = plain.split()
    return " ".join(words[:10])[:90]


def apply(led: dict, parsed: dict, batch_id: str) -> None:
    by_id = {t["id"]: t for t in led["themes"]}
    misc = None
    for r in parsed["repeats"]:
        theme = by_id.get(r["theme_id"])
        if theme is None:
            print(f"  ledger: repeat for unknown theme {r['theme_id']} -> misc",
                  file=sys.stderr)
            if misc is None:
                misc = by_id.get("T0") or {"id": "T0", "label": "misc (unmatched repeats)",
                                           "category": "other", "sentiment": "",
                                           "created_batch": batch_id, "entries": [],
                                           "metrics": {}}
                if misc["id"] not in by_id:
                    led["themes"].append(misc)
                    by_id["T0"] = misc
            theme = misc
        theme["entries"].append({"batch": batch_id, "kind": "repeat",
                                 "text": r["text"], "videos": r["videos"],
                                 "likes_sum": r["likes_sum"]})
    for n in parsed["new"]:
        tid = f"T{led['next_theme_seq']:03d}"
        led["next_theme_seq"] += 1
        led["themes"].append({
            "id": tid, "label": _label(n["text"]), "category": n["category"],
            "sentiment": n.get("sentiment", ""),
            "created_batch": batch_id,
            "entries": [{"batch": batch_id, "kind": "new", "text": n["text"],
                         "videos": n["videos"], "likes_sum": n["likes_sum"]}],
            "metrics": {},
        })
    for q in parsed.get("questions", []):
        led["questions"].append({**q, "batch": batch_id})
    for c in parsed.get("competitors", []):
        led["competitors"].append({**c, "batch": batch_id})


# --------------------------------------------------------------------------- #
# Scoring
# --------------------------------------------------------------------------- #
def recompute_scores(led: dict, state: dict, weights: dict) -> None:
    w = {**DEFAULT_WEIGHTS, **(weights or {})}
    videos = state.get("videos", {})
    all_batches = sorted({e["batch"] for t in led["themes"]
                          for e in t["entries"]})
    recent_window = set(all_batches[-3:])
    for t in led["themes"]:
        vids, channels, likes = set(), set(), 0
        batches = set()
        for e in t["entries"]:
            batches.add(e["batch"])
            likes += e.get("likes_sum", 0)
            for vid in e.get("videos", []):
                vids.add(vid)
                ch = videos.get(vid, {}).get("channel")
                if ch:
                    channels.add(ch)
        views_sum = sum(videos.get(v, {}).get("view_count") or 0 for v in vids)
        comments_sum = sum(videos.get(v, {}).get("comment_count") or 0
                           for v in vids)
        engagements = [1000 * (videos.get(v, {}).get("comment_count") or 0)
                       / max(videos.get(v, {}).get("view_count") or 0, 1)
                       for v in vids
                       if videos.get(v, {}).get("view_count")]
        engagement = round(statistics.median(engagements), 2) if engagements else 0.0
        score = (w["m"] * len(t["entries"])
                 + w["b"] * len(batches)
                 + w["ch"] * len(channels)
                 + w["l"] * math.log10(1 + likes)
                 + w["v"] * math.log10(1 + views_sum)
                 + w["c"] * math.log10(1 + comments_sum)
                 + w["e"] * engagement)
        recent = sum(1 for e in t["entries"] if e["batch"] in recent_window)
        if t.get("created_batch") in recent_window:
            trend = "new"
        elif recent >= 2:
            trend = "▲"
        elif recent == 0:
            trend = "▼"
        else:
            trend = "·"
        t["metrics"] = {
            "n_mentions": len(t["entries"]), "n_batches": len(batches),
            "videos": sorted(vids), "channels": sorted(channels),
            "views_sum": views_sum, "comments_sum": comments_sum,
            "likes_sum": likes, "engagement": engagement,
            "recent_mentions": recent, "trend": trend,
            "score": round(score, 2),
        }


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #
def render_ledger_md(dirpath: Path, led: dict) -> None:
    lines = ["# Ledger — chronological novelty digests", ""]
    by_batch: dict[str, list] = {}
    for t in led["themes"]:
        for e in t["entries"]:
            by_batch.setdefault(e["batch"], []).append((t, e))
    for batch in sorted(by_batch):
        lines.append(f"## {batch}")
        for t, e in by_batch[batch]:
            mark = "NEW" if e["kind"] == "new" else "repeat"
            lines.append(f"- **{t['id']}** ({t['category']}, {mark}) {e['text']}"
                         + (f" _[{', '.join(e['videos'])}]_" if e["videos"] else ""))
        lines.append("")
    (dirpath / "LEDGER.md").write_text("\n".join(lines))


def render_scoreboard_md(dirpath: Path, led: dict) -> None:
    themes = sorted(led["themes"],
                    key=lambda t: t.get("metrics", {}).get("score", 0),
                    reverse=True)
    lines = [
        "# Scoreboard — themes ranked by audience weight",
        "",
        "| # | id | theme | cat | trend | score | mentions | batches | channels "
        "| Σ👍 | Σviews | Σcomments | engagement‰ |",
        "|---|----|-------|-----|-------|-------|----------|---------|----------"
        "|-----|--------|-----------|-------------|",
    ]
    for i, t in enumerate(themes, 1):
        m = t.get("metrics", {})
        lines.append(
            f"| {i} | {t['id']} | {t['label']} | {t['category']} "
            f"| {m.get('trend', '·')} "
            f"| {m.get('score', 0)} | {m.get('n_mentions', 0)} "
            f"| {m.get('n_batches', 0)} | {len(m.get('channels', []))} "
            f"| {m.get('likes_sum', 0)} | {m.get('views_sum', 0):,} "
            f"| {m.get('comments_sum', 0):,} | {m.get('engagement', 0)} |")
    (dirpath / "SCOREBOARD.md").write_text("\n".join(lines) + "\n")


def render_questions_md(dirpath: Path, led: dict) -> None:
    lines = ["# Questions users ask — content/SEO ideas", ""]
    for q in led.get("questions", []):
        vids = f" _[{', '.join(q['videos'])}]_" if q.get("videos") else ""
        lines.append(f"- ({q.get('batch', '?')}) {q['text']}{vids}")
    (dirpath / "QUESTIONS.md").write_text("\n".join(lines) + "\n")


def render_competitors_md(dirpath: Path, led: dict) -> None:
    by_name: dict[str, list] = {}
    for c in led.get("competitors", []):
        by_name.setdefault(c["name"], []).append(c)
    lines = ["# Competitor mentions", ""]
    for name in sorted(by_name, key=lambda n: -len(by_name[n])):
        ms = by_name[name]
        praise = sum(1 for m in ms if m["kind"] == "praise")
        compl = sum(1 for m in ms if m["kind"] == "complaint")
        lines.append(f"## {name} — {len(ms)} mentions "
                     f"(👍{praise} praise / 👎{compl} complaints)")
        for m in ms:
            vids = f" _[{', '.join(m['videos'])}]_" if m.get("videos") else ""
            lines.append(f"- **{m['kind']}** ({m.get('batch', '?')}) "
                         f"{m['text']}{vids}")
        lines.append("")
    (dirpath / "COMPETITORS.md").write_text("\n".join(lines) + "\n")
