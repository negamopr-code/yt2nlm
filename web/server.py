#!/usr/bin/env python3
"""yt2nlm ask — combine NotebookLM notebooks and fan one question across them.

Design contract (matches the user's requirement of "free"):
- The question is forwarded VERBATIM to each selected notebook via
  `nlm notebook query <id> <question> --json`. The answer is computed by
  Gemini on Google's side → ZERO Anthropic tokens. Claude is NOT in the
  runtime loop; this server just shells out to `nlm` and renders the answers.
- Calls are SERIALIZED with a minimum gap (anti RESOURCE_EXHAUSTED), same
  discipline as yt2nlm/nlm.py.
- Output is per-notebook and verbatim — no LLM-side merge (mode "A").

No third-party deps: pure stdlib http.server, so it runs on a bare
`python:slim` image with only `notebooklm-mcp-cli` installed for the `nlm` CLI.
"""
from __future__ import annotations

import glob
import json
import os
import subprocess
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

NLM_BIN = os.environ.get("NLM_BIN", "nlm")
STATE_DIR = os.environ.get(
    "YT2NLM_STATE",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "state"),
)
REPORTS_DIR = os.environ.get(
    "YT2NLM_REPORTS",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "reports"),
)
PORT = int(os.environ.get("PORT", "8091"))
MIN_GAP = float(os.environ.get("NLM_MIN_GAP", "1.5"))
QUERY_TIMEOUT = float(os.environ.get("NLM_QUERY_TIMEOUT", "150"))

# Optional merge step: stitch the per-notebook answers into one via the
# `claude` CLI headless (-p), billed to whatever auth is in CLAUDE_CONFIG_DIR
# (OAuth subscription or ANTHROPIC_API_KEY). Pure text-in/text-out, no tools.
CLAUDE_BIN = os.environ.get("CLAUDE_BIN", "claude")
CLAUDE_MERGE_MODEL = os.environ.get("CLAUDE_MERGE_MODEL", "claude-haiku-4-5")
MERGE_TIMEOUT = float(os.environ.get("MERGE_TIMEOUT", "180"))

_last_call = 0.0


def _gap() -> None:
    global _last_call
    g = MIN_GAP - (time.monotonic() - _last_call)
    if g > 0:
        time.sleep(g)


def _json_after_brace(s: str, brace: str):
    i = s.find(brace)
    if i < 0:
        raise ValueError("no JSON in output")
    return json.loads(s[i:])


def list_notebooks() -> list[dict]:
    """All notebooks in the account (id, title, source_count)."""
    try:
        out = subprocess.run(
            [NLM_BIN, "notebook", "list"],
            capture_output=True, text=True, timeout=60,
        )
        data = _json_after_brace(out.stdout, "[")
        return [n for n in data if n.get("id")]
    except Exception:
        return []


def load_channels() -> list[dict]:
    """Channel groups straight from yt2nlm manifests (state/<channel>.json)."""
    chans = []
    for path in sorted(glob.glob(os.path.join(STATE_DIR, "*.json"))):
        try:
            with open(path, encoding="utf-8") as fh:
                d = json.load(fh)
        except Exception:
            continue
        # Skip anything that isn't a yt2nlm manifest (e.g. a candidates list
        # someone dropped in state/) — a non-dict here used to 500 /api/groups.
        if not isinstance(d, dict):
            continue
        nbs = d.get("notebooks") or []
        if not isinstance(nbs, list) or not nbs:
            continue
        chans.append({
            "channel": d.get("channel") or os.path.basename(path),
            "ingest": d.get("ingest", ""),
            "notebooks": [
                {"id": n["id"], "title": n.get("title", n["id"]),
                 "count": n.get("count")}
                for n in nbs if n.get("id")
            ],
        })
    return chans


def query_one(nb_id: str, question: str) -> dict:
    """Forward the question VERBATIM to one notebook. Returns answer or error."""
    global _last_call
    _gap()
    try:
        proc = subprocess.run(
            [NLM_BIN, "notebook", "query", nb_id, question,
             "--json", "--timeout", str(int(QUERY_TIMEOUT))],
            capture_output=True, text=True, timeout=QUERY_TIMEOUT + 30,
        )
    except subprocess.TimeoutExpired:
        _last_call = time.monotonic()
        return {"error": "timeout"}
    finally:
        _last_call = time.monotonic()

    if proc.returncode != 0:
        return {"error": (proc.stderr or proc.stdout).strip()[:400] or "nlm failed"}
    try:
        val = _json_after_brace(proc.stdout, "{").get("value", {})
    except Exception as exc:
        return {"error": f"parse: {exc}"}
    return {
        "answer": val.get("answer", ""),
        "sources_used": val.get("sources_used", []),
    }


def merge_answers(question: str, results: list[dict]) -> dict:
    """Stitch per-notebook answers into one via `claude -p` (no tools).

    Returns {"merged": text} or {"error": ...}. Degrades gracefully: if claude
    is missing or fails, the caller still returns the verbatim per-notebook
    answers — the merge is purely additive.
    """
    good = [r for r in results
            if not r.get("error") and (r.get("answer") or "").strip()]
    if len(good) < 2:
        return {"error": "need >=2 non-empty answers to merge"}

    blocks = "\n\n".join(
        f"[Ноутбук: {r['title']}]\n{r['answer'].strip()}" for r in good
    )
    prompt = (
        "Ты — редактор. Ниже ответы из РАЗНЫХ ноутбуков NotebookLM на ОДИН "
        "вопрос (каждый ноутбук видит только свою часть материалов). Сведи их "
        "в ОДИН связный ответ на русском: объедини общее, убери дубли, явно "
        "отметь расхождения между ноутбуками. Не выдумывай ничего сверх "
        "приведённого. Без преамбулы и без упоминания, что это склейка.\n\n"
        f"ВОПРОС: {question}\n\n{blocks}"
    )
    try:
        proc = subprocess.run(
            [CLAUDE_BIN, "-p", "--model", CLAUDE_MERGE_MODEL],
            input=prompt, capture_output=True, text=True, timeout=MERGE_TIMEOUT,
        )
    except FileNotFoundError:
        return {"error": "claude CLI not found in container"}
    except subprocess.TimeoutExpired:
        return {"error": "merge timeout"}
    if proc.returncode != 0:
        return {"error": (proc.stderr or proc.stdout).strip()[:400] or "claude failed"}
    return {"merged": proc.stdout.strip(), "merged_from": len(good)}


def _read_report(key: str, name: str) -> str:
    """Read a file from reports/<key>/ ('' when absent)."""
    path = os.path.join(REPORTS_DIR, os.path.basename(key),
                        os.path.basename(name))
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return ""


def load_monitors() -> list[dict]:
    """Monitor states (state/monitor-*.json with a `batches` field) merged
    with their reports/<key>/ ledger + rendered markdown. Read-only nutshell
    of everything the monitor went through."""
    out = []
    for path in sorted(glob.glob(os.path.join(STATE_DIR, "*.json"))):
        if path.endswith(".config.json"):
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                st = json.load(fh)
        except Exception:
            continue
        if not isinstance(st, dict) or "batches" not in st or "videos" not in st:
            continue
        key = st.get("key") or os.path.splitext(os.path.basename(path))[0]
        ledger = {}
        try:
            ledger = json.loads(_read_report(key, "ledger.json") or "{}")
        except Exception:
            pass
        videos = []
        for vid, rec in (st.get("videos") or {}).items():
            videos.append({
                "video_id": vid, "title": rec.get("title", ""),
                "channel": rec.get("channel", ""), "url": rec.get("url", ""),
                "view_count": rec.get("view_count"),
                "comment_count": rec.get("comment_count"),
                "collected": len(rec.get("seen_cids") or []),
                "engagement": (round(1000 * (rec.get("comment_count") or 0)
                                     / rec["view_count"], 2)
                               if rec.get("view_count") else None),
                "first_seen": rec.get("first_seen", ""),
                "last_checked": rec.get("last_checked", ""),
                "transcript_done": rec.get("transcript_done", False),
                "is_short": rec.get("is_short", False),
            })
        videos.sort(key=lambda v: v.get("view_count") or 0, reverse=True)
        coverage = {}
        for v in videos:
            c = coverage.setdefault(v["channel"] or "?", {
                "videos": 0, "comments_collected": 0, "transcribed": 0})
            c["videos"] += 1
            c["comments_collected"] += v["collected"]
            c["transcribed"] += 1 if v["transcript_done"] is True else 0
        batches = st.get("batches") or []
        latest_digest = ""
        for b in reversed(batches):
            if b.get("digest_path"):
                latest_digest = _read_report(
                    key, os.path.basename(b["digest_path"]))
                if latest_digest:
                    break
        trends = {}
        try:
            trends = json.loads(_read_report(key, "trends.json") or "{}")
        except Exception:
            pass
        prog = {}
        try:
            prog = json.loads(_read_report(key, "progress.json") or "{}")
        except Exception:
            pass
        out.append({
            "key": key,
            "notebook_id": st.get("notebook_id", ""),
            "notebook_title": st.get("notebook_title", ""),
            "updated_at": st.get("updated_at", ""),
            "archives": st.get("archives") or {},
            "urls": st.get("urls") or {},
            "batches": batches,
            "videos": videos,
            "coverage": coverage,
            "progress": prog,
            "themes": ledger.get("themes") or [],
            "questions": ledger.get("questions") or [],
            "competitors": ledger.get("competitors") or [],
            "trends": trends,
            "ledger_md": _read_report(key, "LEDGER.md"),
            "proposals_md": _read_report(key, "PROPOSALS.md"),
            "latest_digest_md": latest_digest,
        })
    return out


# --------------------------------------------------------------------------- #
# PDF snapshot — the complete current corpus as one document, built from the
# files AS THEY ARE at request time (the archives keep growing; every download
# is the very latest version).
# --------------------------------------------------------------------------- #
_PDF_FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
_PDF_FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
_PDF_REPL = {"👍": "+", "👎": "-", "★": "*", "↳": "->", "‰": " per-mille",
             "⏳": "", "✅": "[ok]", "⚠": "[!]", "▲": "^", "▼": "v", "·": "-"}


def _pdf_text(s: str) -> str:
    for a, b in _PDF_REPL.items():
        s = s.replace(a, b)
    s = s.replace("\t", "  ")
    # DejaVu covers the BMP well; drop astral-plane glyphs (emoji), control
    # chars and zero-width marks (fpdf2 cannot measure them).
    return "".join(
        ch for ch in s
        if ord(ch) <= 0xFFFF and (ch == "\n" or ord(ch) >= 32)
        and ch not in "​‌‍‎‏﻿  ")


def build_pdf(m: dict) -> bytes:
    from fpdf import FPDF

    pdf = FPDF(format="A4")
    pdf.set_auto_page_break(True, margin=14)
    pdf.add_font("dv", "", _PDF_FONT)
    pdf.add_font("dv", "B", _PDF_FONT_BOLD)

    def h1(t):
        pdf.add_page()
        pdf.set_font("dv", "B", 16)
        pdf.multi_cell(0, 8, _pdf_text(t), new_x="LMARGIN", new_y="NEXT")
        pdf.ln(2)

    def h2(t):
        pdf.ln(3)
        pdf.set_font("dv", "B", 12)
        pdf.multi_cell(0, 6, _pdf_text(t), new_x="LMARGIN", new_y="NEXT")
        pdf.ln(1)

    def p(t, size=9):
        pdf.set_font("dv", "", size)
        for para in t.split("\n"):
            clean = _pdf_text(para)
            try:
                pdf.multi_cell(0, 4.6, clean, new_x="LMARGIN", new_y="NEXT")
            except Exception:
                # last resort: a paragraph fpdf2 cannot lay out is degraded
                # to ASCII rather than failing the whole document
                pdf.set_x(pdf.l_margin)
                pdf.multi_cell(0, 4.6, clean.encode("ascii", "replace").decode(),
                               new_x="LMARGIN", new_y="NEXT")

    now = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())
    videos = m.get("videos") or []
    n_com = sum(v.get("collected") or 0 for v in videos)
    arch = m.get("archives") or {}

    # Cover
    pdf.add_page()
    pdf.set_font("dv", "B", 22)
    pdf.ln(40)
    pdf.multi_cell(0, 12, _pdf_text(m.get("notebook_title") or m["key"]), new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("dv", "", 12)
    pdf.multi_cell(0, 8, new_x="LMARGIN", new_y="NEXT", text=_pdf_text(
        f"Market-monitor corpus snapshot — generated {now}\n\n"
        f"Batches: {len(m.get('batches') or [])}   Items tracked: {len(videos)}   "
        f"Comments collected: {n_com:,}\n"
        f"Themes: {len(m.get('themes') or [])}   Questions: "
        f"{len(m.get('questions') or [])}   Competitor mentions: "
        f"{len(m.get('competitors') or [])}\n"
        + "\n".join(f"Archive {k}: vol.{a.get('vol')} — {a.get('words', 0):,} words"
                    for k, a in arch.items())
        + "\n\nThis document is regenerated on every download and always "
          "reflects the current state of the continuously growing corpus."))

    # Scoreboard
    h1("1. Scoreboard — themes ranked by audience weight")
    themes = sorted(m.get("themes") or [],
                    key=lambda t: t.get("metrics", {}).get("score", 0),
                    reverse=True)
    for i, t in enumerate(themes, 1):
        x = t.get("metrics", {})
        h2(f"{i}. [{t['id']}] {t.get('label', '')}  "
           f"(score {x.get('score', 0)}, {t.get('category', '')})")
        p(f"trend {x.get('trend', '-')} | mentions {x.get('n_mentions', 0)} | "
          f"batches {x.get('n_batches', 0)} | channels {len(x.get('channels', []))} | "
          f"likes {x.get('likes_sum', 0)} | views {x.get('views_sum', 0):,} | "
          f"comments {x.get('comments_sum', 0):,} | engagement "
          f"{x.get('engagement', 0)} per 1k views")
        for e in t.get("entries", []):
            p(f"  - ({e.get('batch')}, {e.get('kind')}) {e.get('text', '')}")

    # Coverage + batches
    h1("2. Coverage and batches")
    h2("Coverage by channel")
    for ch, c in (m.get("coverage") or {}).items():
        p(f"{ch}: {c['videos']} videos seen, {c['comments_collected']:,} comments "
          f"collected, {c['transcribed']} transcribed")
    h2("Batches")
    for b in m.get("batches") or []:
        p(f"{b.get('id')}  [{b.get('status')}]  {b.get('n_comments', 0):,} new "
          f"comments / {b.get('n_videos', 0)} items  ({b.get('collected_at', '')})")
    h2("Items (videos / posts / apps)")
    for v in videos:
        p(f"{v.get('title', '')} — {v.get('channel', '')} — views "
          f"{v.get('view_count') or '?'} — comments {v.get('comment_count') or '?'}"
          f" — collected {v.get('collected')}"
          f"{' — transcribed' if v.get('transcript_done') is True else ''}")

    # Questions / competitors / proposals / ledger
    h1("3. Questions users ask (content/SEO ideas)")
    for q in m.get("questions") or []:
        p(f"- ({q.get('batch', '')}) {q.get('text', '')}")
    h1("4. Competitor mentions")
    by = {}
    for c in m.get("competitors") or []:
        by.setdefault(c.get("name", "?"), []).append(c)
    for name, ms in sorted(by.items(), key=lambda kv: -len(kv[1])):
        h2(f"{name} ({len(ms)} mentions)")
        for c in ms:
            p(f"- [{c.get('kind')}] ({c.get('batch', '')}) {c.get('text', '')}")
    if m.get("proposals_md"):
        h1("5. Proposals for the site")
        p(m["proposals_md"])
    if m.get("ledger_md"):
        h1("6. Ledger — chronological novelty digests")
        p(m["ledger_md"])

    # Appendices: the full growing archives, as of right now
    letter = "A"
    for pname, title in (("digests", "Gemini digests"),
                         ("youtube-comments", "All collected comments"),
                         ("youtube-transcripts", "All video transcripts"),
                         ("reddit", "Reddit"), ("app-reviews", "App reviews"),
                         ("articles", "Articles")):
        parts = sorted(glob.glob(os.path.join(
            REPORTS_DIR, m["key"], "archives", f"{pname}-vol*.md")))
        if not parts:
            continue
        h1(f"Appendix {letter}. {title} (full archive)")
        for part in parts:
            try:
                with open(part, encoding="utf-8") as fh:
                    p(fh.read(), size=8)
            except OSError:
                pass
        letter = chr(ord(letter) + 1)

    return bytes(pdf.output())


# --------------------------------------------------------------------------- #
# HTTP
# --------------------------------------------------------------------------- #
class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # quieter logs
        pass

    def _send(self, code: int, body: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json(self, code: int, obj) -> None:
        self._send(code, json.dumps(obj).encode("utf-8"),
                   "application/json; charset=utf-8")

    def do_GET(self):
        if self.path == "/" or self.path.startswith("/?"):
            self._send(200, PAGE.encode("utf-8"), "text/html; charset=utf-8")
        elif self.path == "/monitor" or self.path.startswith("/monitor?"):
            self._send(200, MONITOR_PAGE.encode("utf-8"),
                       "text/html; charset=utf-8")
        elif self.path == "/api/monitor":
            self._json(200, {"monitors": load_monitors()})
        elif self.path.startswith("/api/monitor/pdf"):
            from urllib.parse import parse_qs, urlparse
            key = (parse_qs(urlparse(self.path).query).get("key") or [""])[0]
            mons = load_monitors()
            m = next((x for x in mons if x["key"] == key), mons[0] if mons else None)
            if not m:
                self._json(404, {"error": "no monitor state"})
                return
            try:
                blob = build_pdf(m)
            except Exception as exc:
                self._json(500, {"error": f"pdf build failed: {exc}"})
                return
            stamp = time.strftime("%Y%m%d-%H%M", time.gmtime())
            self.send_response(200)
            self.send_header("Content-Type", "application/pdf")
            self.send_header("Content-Disposition",
                             f'attachment; filename="{m["key"]}-corpus-{stamp}.pdf"')
            self.send_header("Content-Length", str(len(blob)))
            self.end_headers()
            self.wfile.write(blob)
        elif self.path == "/api/groups":
            self._json(200, {
                "channels": load_channels(),
                "all_notebooks": [
                    {"id": n["id"], "title": n.get("title", n["id"]),
                     "count": n.get("source_count")}
                    for n in list_notebooks()
                ],
            })
        else:
            self._send(404, b"not found", "text/plain")

    def do_POST(self):
        if self.path != "/api/ask":
            self._send(404, b"not found", "text/plain")
            return
        try:
            n = int(self.headers.get("Content-Length", 0))
            req = json.loads(self.rfile.read(n) or b"{}")
        except Exception:
            self._json(400, {"error": "bad request"})
            return
        question = (req.get("question") or "").strip()
        ids = [i for i in (req.get("notebooks") or []) if i]
        want_merge = bool(req.get("merge"))
        if not question or not ids:
            self._json(400, {"error": "question and notebooks required"})
            return

        titles = {}
        for c in load_channels():
            for nb in c["notebooks"]:
                titles[nb["id"]] = nb["title"]
        for nb in list_notebooks():
            titles.setdefault(nb["id"], nb.get("title", nb["id"]))

        results = []
        for nb_id in ids:
            r = query_one(nb_id, question)
            r["id"] = nb_id
            r["title"] = titles.get(nb_id, nb_id)
            results.append(r)

        resp = {"question": question, "results": results}
        if want_merge:
            resp["merge"] = merge_answers(question, results)
        self._json(200, resp)


PAGE = r"""<!doctype html>
<html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>yt2nlm · ask across notebooks</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
 :root{--bg:#0f1419;--card:#1a2029;--line:#2a3340;--fg:#e6edf3;--mut:#8b98a5;--acc:#4493f8}
 *{box-sizing:border-box}
 body{margin:0;font:15px/1.55 system-ui,Segoe UI,Roboto,sans-serif;background:var(--bg);color:var(--fg)}
 header{padding:18px 24px;border-bottom:1px solid var(--line)}
 header h1{margin:0;font-size:18px}
 header p{margin:4px 0 0;color:var(--mut);font-size:13px}
 .wrap{display:grid;grid-template-columns:340px 1fr;gap:0;height:calc(100vh - 64px)}
 .side{border-right:1px solid var(--line);overflow:auto;padding:16px}
 .main{overflow:auto;padding:20px 24px}
 .grp{margin-bottom:14px;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 12px}
 .grp h3{margin:0 0 6px;font-size:13px;color:var(--acc);display:flex;align-items:center;gap:6px;cursor:pointer}
 .grp h3 .meta{color:var(--mut);font-weight:400;font-size:11px}
 label.nb{display:flex;gap:8px;align-items:flex-start;padding:3px 0;font-size:13px;cursor:pointer}
 label.nb span.t{flex:1}
 label.nb span.c{color:var(--mut);font-size:11px}
 .ask{position:sticky;top:0;background:var(--bg);padding-bottom:12px;margin-bottom:8px;z-index:2}
 textarea{width:100%;min-height:70px;background:var(--card);color:var(--fg);border:1px solid var(--line);border-radius:8px;padding:10px;font:inherit;resize:vertical}
 .row{display:flex;gap:10px;align-items:center;margin-top:8px}
 button{background:var(--acc);color:#fff;border:0;border-radius:7px;padding:9px 18px;font:inherit;font-weight:600;cursor:pointer}
 button:disabled{opacity:.5;cursor:default}
 .sel{color:var(--mut);font-size:13px}
 .res{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:14px 16px;margin-bottom:14px}
 .res h4{margin:0 0 8px;font-size:14px}
 .res .src{color:var(--mut);font-size:12px;margin-top:8px;border-top:1px solid var(--line);padding-top:8px}
 .res .ans{font-size:14px}
 .res .ans h1,.res .ans h2,.res .ans h3{font-size:15px;margin:12px 0 6px}
 .res.err{border-color:#a33}
 .err b{color:#f77}
 .hint{color:var(--mut);font-size:13px}
 a{color:var(--acc)}
 .pill{display:inline-block;background:var(--line);border-radius:10px;padding:1px 8px;font-size:11px;color:var(--mut)}
</style></head>
<body>
<header>
 <h1>yt2nlm · вопрос сразу во все ноутбуки</h1>
 <p>Вопрос уходит в каждый выбранный ноутбук <b>дословно</b>. Отвечает NotebookLM (Gemini) — ответы по полным материалам: транскрипты видео + комменты. Никакой пересборки и 0 токенов модели.</p>
</header>
<div class="wrap">
 <div class="side">
  <div class="row" style="margin:0 0 12px"><button id="reload" style="background:var(--line)">↻ обновить список</button></div>
  <div id="groups" class="hint">загрузка…</div>
 </div>
 <div class="main">
  <div class="ask">
   <textarea id="q" placeholder="Например: какие главные тезисы и обещания повторяются от видео к видео? где аудитория в комментах расходится с тем, что заявлено в видео?"></textarea>
   <div class="row">
    <button id="go" disabled>Спросить</button>
    <label class="sel" style="display:flex;gap:6px;align-items:center;cursor:pointer">
     <input type="checkbox" id="merge"> свести в один ответ <span class="pill">Haiku · копейки</span>
    </label>
    <span class="sel" id="selinfo">ноутбуков выбрано: 0</span>
   </div>
  </div>
  <div id="out" class="hint">Выбери ноутбуки слева, задай вопрос — каждый ответит отдельно.</div>
 </div>
</div>
<script>
let GROUPS={channels:[],all_notebooks:[]};
const sel=new Set();
const $=s=>document.querySelector(s);

function selInfo(){ $('#selinfo').textContent='ноутбуков выбрано: '+sel.size;
  $('#go').disabled = sel.size===0 || !$('#q').value.trim(); }

function nbRow(nb){
  const id='cb_'+nb.id;
  const cnt = nb.count!=null? `<span class="c">${nb.count}</span>`:'';
  return `<label class="nb"><input type="checkbox" data-id="${nb.id}" ${sel.has(nb.id)?'checked':''}>
    <span class="t">${esc(nb.title)}</span>${cnt}</label>`;
}
function esc(s){return (s||'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}

function render(){
  let h='';
  for(const c of GROUPS.channels){
    const ids=c.notebooks.map(n=>n.id);
    h+=`<div class="grp"><h3 data-pick="${ids.join(',')}">▾ ${esc(c.channel)}
        <span class="meta">${c.notebooks.length} нб · клик = выбрать все</span></h3>`;
    h+=c.notebooks.map(nbRow).join('');
    h+='</div>';
  }
  // notebooks not covered by any channel manifest
  const known=new Set(GROUPS.channels.flatMap(c=>c.notebooks.map(n=>n.id)));
  const orphan=GROUPS.all_notebooks.filter(n=>!known.has(n.id));
  if(orphan.length){
    h+=`<div class="grp"><h3 data-pick="${orphan.map(n=>n.id).join(',')}">▾ прочие ноутбуки
        <span class="meta">${orphan.length} нб</span></h3>`;
    h+=orphan.map(nbRow).join('')+'</div>';
  }
  $('#groups').innerHTML = h || '<span class="hint">ноутбуков не найдено</span>';
}

function load(){
  $('#groups').textContent='загрузка…';
  fetch('/api/groups').then(r=>r.json()).then(g=>{GROUPS=g;render();selInfo();})
    .catch(()=>{$('#groups').innerHTML='<span class="err"><b>не удалось загрузить список</b></span>';});
}

document.addEventListener('change',e=>{
  if(e.target.matches('input[data-id]')){
    const id=e.target.dataset.id;
    e.target.checked?sel.add(id):sel.delete(id); selInfo();
  }
});
document.addEventListener('click',e=>{
  const h=e.target.closest('h3[data-pick]');
  if(h){ const ids=h.dataset.pick.split(',').filter(Boolean);
    const allOn=ids.every(i=>sel.has(i));
    ids.forEach(i=>allOn?sel.delete(i):sel.add(i));
    render(); selInfo(); }
});
$('#q').addEventListener('input',selInfo);
$('#reload').addEventListener('click',load);

$('#go').addEventListener('click',()=>{
  const question=$('#q').value.trim();
  const notebooks=[...sel];
  if(!question||!notebooks.length) return;
  const merge=$('#merge').checked;
  $('#go').disabled=true;
  $('#out').innerHTML=`<div class="hint">опрашиваю ${notebooks.length} ноутбук(ов) последовательно…${merge?' затем склейка через Haiku…':''} (по ~10–40с на каждый)</div>`;
  fetch('/api/ask',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({question,notebooks,merge})})
   .then(r=>r.json()).then(d=>{
     if(d.error){$('#out').innerHTML=`<div class="res err"><b>${esc(d.error)}</b></div>`;selInfo();return;}
     let h=`<div class="hint" style="margin-bottom:12px">вопрос: <i>${esc(d.question)}</i> · ${d.results.length} ответ(ов)</div>`;
     if(d.merge){
       if(d.merge.merged){
         h+=`<div class="res" style="border-color:var(--acc);border-width:2px">
              <h4>🧩 Сводный ответ <span class="pill">склейка ${d.merge.merged_from} ноутбуков · Haiku</span></h4>
              <div class="ans">${marked.parse(d.merge.merged)}</div></div>
             <div class="hint" style="margin:4px 0 12px">ниже — исходные ответы по каждому ноутбуку (verbatim):</div>`;
       }else if(d.merge.error){
         h+=`<div class="res err"><h4>🧩 Склейка не выполнена</h4><div class="err"><b>${esc(d.merge.error)}</b> — ответы ниже без склейки.</div></div>`;
       }
     }
     for(const r of d.results){
       if(r.error){
         h+=`<div class="res err"><h4>${esc(r.title)}</h4><div class="err"><b>ошибка:</b> ${esc(r.error)}</div></div>`;
       }else{
         const src=(r.sources_used&&r.sources_used.length)?`<div class="src">источников использовано: ${r.sources_used.length}</div>`:'';
         h+=`<div class="res"><h4>${esc(r.title)}</h4><div class="ans">${marked.parse(r.answer||'(пусто)')}</div>${src}</div>`;
       }
     }
     $('#out').innerHTML=h; selInfo();
   })
   .catch(err=>{$('#out').innerHTML=`<div class="res err"><b>сбой запроса: ${esc(String(err))}</b></div>`;selInfo();});
});

load();
</script>
</body></html>"""


MONITOR_PAGE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>market monitor · nutshell</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
 :root{--bg:#0f1419;--card:#1a2029;--line:#2a3340;--fg:#e6edf3;--mut:#8b98a5;--acc:#4493f8;--ok:#3fb950;--warn:#d29922}
 *{box-sizing:border-box}
 body{margin:0;font:14px/1.5 system-ui,Segoe UI,Roboto,sans-serif;background:var(--bg);color:var(--fg)}
 header{padding:16px 24px;border-bottom:1px solid var(--line);display:flex;gap:16px;align-items:baseline;flex-wrap:wrap}
 header h1{margin:0;font-size:17px}
 header .mut{color:var(--mut);font-size:13px}
 header a{color:var(--acc);font-size:13px}
 .wrap{padding:18px 24px;max-width:1300px}
 .cards{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:16px}
 .stat{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 16px;min-width:110px}
 .stat b{display:block;font-size:20px}
 .stat span{color:var(--mut);font-size:12px}
 section{margin-bottom:22px}
 h2{font-size:15px;margin:0 0 8px;color:var(--acc)}
 .tblwrap{overflow-x:auto;background:var(--card);border:1px solid var(--line);border-radius:8px}
 table{border-collapse:collapse;width:100%;font-size:13px}
 th,td{padding:6px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
 th{color:var(--mut);font-weight:600;white-space:nowrap;cursor:pointer;user-select:none}
 tr:last-child td{border-bottom:0}
 td.num,th.num{text-align:right;white-space:nowrap}
 .cat{display:inline-block;border-radius:9px;padding:0 8px;font-size:11px;background:var(--line)}
 .cat.need{background:#1f4429;color:#7ee2a0}.cat.complaint{background:#4a1f24;color:#f5989d}
 .cat.idea{background:#1f3a4a;color:#8fd0f5}.cat.works{background:#43401f;color:#e2d67e}
 .md{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px 16px;font-size:13px}
 .md h1,.md h2,.md h3{font-size:14px;margin:10px 0 6px;color:var(--fg)}
 .badge{display:inline-block;border-radius:9px;padding:0 8px;font-size:11px;background:var(--line);color:var(--mut)}
 .badge.merged,.badge.digested{background:#1f4429;color:#7ee2a0}
 .badge.collected,.badge.uploaded{background:#43401f;color:#e2d67e}
 .badge.empty{background:var(--line)}
 details summary{cursor:pointer;color:var(--acc);margin-bottom:8px}
 a{color:var(--acc);text-decoration:none}
 .hint{color:var(--mut)}
 .tabs{display:flex;gap:8px;margin-bottom:14px}
 .tabs button{background:var(--card);border:1px solid var(--line);color:var(--fg);border-radius:7px;padding:6px 14px;cursor:pointer}
 .tabs button.on{border-color:var(--acc);color:var(--acc)}
</style></head>
<body>
<header>
 <h1>🕵️ market monitor — in a nutshell</h1>
 <span class="mut">everything we went through: videos · articles · batches · themes</span>
 <a href="/">→ ask the notebooks</a>
</header>
<div class="wrap" id="app"><span class="hint">loading…</span></div>
<script>
const $=s=>document.querySelector(s);
const esc=s=>(s==null?'':String(s)).replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
const fmt=n=>n==null?'—':Number(n).toLocaleString('en-US');
let DATA=null, CUR=0, SORT={key:'view_count',dir:-1};

function stat(label,val){return `<div class="stat"><b>${val}</b><span>${label}</span></div>`}

const PHASES=['search','probe','channels','collect','upload','ingest-wait','novelty-query','merge-archive','reddit','app-reviews','articles','transcripts'];
function progressCard(m){
  const p=m.progress||{};
  if(!p.phase) return '';
  const age=(Date.now()-Date.parse(p.updated_at||0))/1000;
  const stepAge=(Date.now()-Date.parse(p.step_changed_at||p.updated_at||0))/1000;
  const running=p.status==='running';
  // heartbeat thread stamps every 30 s → >180 s of silence = process is dead;
  // a long-running SAME step (big Gemini query) is only a "slow" hint.
  const stale=running && age>180;
  const slow=running && !stale && stepAge>1800;
  const col= p.status==='done'?'var(--ok)': p.status==='error'?'#f77':
             p.status==='quota-paused'?'var(--warn)': stale?'#f77': slow?'var(--warn)':'var(--acc)';
  const pct=(p.cur&&p.total)?Math.round(100*p.cur/p.total):null;
  const bar=pct!=null?`<div style="background:var(--line);border-radius:4px;height:8px;margin:6px 0">
      <div style="background:${col};height:8px;border-radius:4px;width:${pct}%"></div></div>`:'';
  const chips=PHASES.map(ph=>`<span class="badge" style="${ph===p.phase?`background:${col};color:#08131f;font-weight:600`:''}">${ph}</span>`).join(' ');
  const status= stale?`⚠ stale — no heartbeat for ${Math.round(age)}s (process died; the runner's watchdog will restart the cycle)`
    : slow?`⏳ running · ${p.phase} — same step for ${Math.round(stepAge/60)} min (long external call; watchdog kills at 3 h)`
    : running?`⏳ running · ${p.phase}${p.cur?` ${p.cur}/${p.total}`:''} · heartbeat ${Math.round(age)}s ago`
    : p.status==='quota-paused'?'⏸ quota-paused — auto-resumes (runner backs off 4 h)'
    : p.status==='error'?'❌ error': p.status==='interrupted'?'⏹ interrupted (resume-safe)':'✅ done';
  return `<section><h2>⚙️ Run progress <span class="hint" style="font-weight:400">(${esc(p.command||'run')}, started ${esc((p.started_at||'').slice(0,16))})</span></h2>
   <div class="md" style="border-left:3px solid ${col}">
    <div><b style="color:${col}">${status}</b></div>
    ${bar}
    <div class="hint">${esc(p.detail||'')}${p.batch_id?` · batch ${esc(p.batch_id)}`:''}${p.new_comments!=null?` · ${p.new_comments} new comments so far`:''}</div>
    <div style="margin-top:8px">${chips}</div>
   </div></section>`;
}

function scoreboard(m){
  const ths=[...(m.themes||[])].sort((a,b)=>(b.metrics?.score||0)-(a.metrics?.score||0));
  if(!ths.length) return '<span class="hint">no themes yet — run the monitor</span>';
  let rows=ths.map((t,i)=>{const x=t.metrics||{};
    const kw=encodeURIComponent((t.label||'').split(' ').slice(0,4).join(' '));
    return `<tr>
    <td class="num">${i+1}</td><td>${t.id}</td><td>${esc(t.label)}${t.sentiment?` <span class="badge">${esc(t.sentiment)}</span>`:''}</td>
    <td><span class="cat ${t.category}">${t.category}</span></td>
    <td>${esc(x.trend||'·')}</td>
    <td class="num"><b>${x.score??0}</b></td><td class="num">${x.n_mentions??0}</td>
    <td class="num">${x.n_batches??0}</td><td class="num">${(x.channels||[]).length}</td>
    <td class="num">${fmt(x.likes_sum)}</td><td class="num">${fmt(x.views_sum)}</td>
    <td class="num">${fmt(x.comments_sum)}</td><td class="num">${x.engagement??0}</td>
    <td><a href="https://trends.google.com/trends/explore?q=${kw}" target="_blank" title="Google Trends">📈</a></td></tr>`}).join('');
  return `<div class="tblwrap"><table><thead><tr><th class="num">#</th><th>id</th><th>theme</th><th>cat</th>
   <th>trend</th>
   <th class="num">score</th><th class="num">mentions</th><th class="num">batches</th><th class="num">channels</th>
   <th class="num">Σ👍</th><th class="num">Σviews</th><th class="num">Σcomments</th><th class="num">eng ‰</th><th>GT</th></tr></thead>
   <tbody>${rows}</tbody></table></div>`;
}

function coverage(m){
  const e=Object.entries(m.coverage||{});
  if(!e.length) return '';
  const rows=e.map(([ch,c])=>`<tr><td>${esc(ch)}</td><td class="num">${c.videos}</td>
    <td class="num">${fmt(c.comments_collected)}</td><td class="num">${c.transcribed}</td></tr>`).join('');
  return `<section><h2>Coverage by channel</h2><div class="tblwrap"><table>
   <thead><tr><th>channel</th><th class="num">videos seen</th><th class="num">comments collected</th>
   <th class="num">transcribed</th></tr></thead><tbody>${rows}</tbody></table></div></section>`;
}

function batches(m){
  const bs=[...(m.batches||[])].reverse();
  if(!bs.length) return '<span class="hint">no batches yet</span>';
  const rows=bs.map(b=>`<tr><td>${esc(b.id)}</td>
    <td><span class="badge ${esc(b.status)}">${esc(b.status)}</span></td>
    <td class="num">${fmt(b.n_comments)}</td><td class="num">${fmt(b.n_videos)}</td>
    <td>${esc(b.collected_at||'')}</td></tr>`).join('');
  return `<div class="tblwrap"><table><thead><tr><th>batch</th><th>status</th>
   <th class="num">new comments</th><th class="num">videos</th><th>collected</th></tr></thead>
   <tbody>${rows}</tbody></table></div>`;
}

function videos(m){
  let vs=[...(m.videos||[])];
  const k=SORT.key;
  vs.sort((a,b)=>{const x=a[k]??-1,y=b[k]??-1;
    return (typeof x==='string'? String(x).localeCompare(String(y)) : x-y)*SORT.dir;});
  if(!vs.length) return '<span class="hint">no videos yet</span>';
  const th=(key,label,num)=>`<th class="${num?'num':''}" data-sort="${key}">${label}${SORT.key===key?(SORT.dir<0?' ↓':' ↑'):''}</th>`;
  const rows=vs.map(v=>`<tr>
    <td><a href="${esc(v.url)}" target="_blank">${esc(v.title||v.video_id)}</a>${v.is_short?' <span class="badge">short</span>':''}</td>
    <td>${esc(v.channel)}</td><td class="num">${fmt(v.view_count)}</td>
    <td class="num">${fmt(v.comment_count)}</td><td class="num">${fmt(v.collected)}</td>
    <td class="num">${v.engagement??'—'}</td>
    <td>${v.transcript_done===true?'✅':(v.transcript_done==='unavailable'?'∅':'')}</td>
    <td>${esc((v.first_seen||'').slice(0,10))}</td><td>${esc((v.last_checked||'').slice(0,10))}</td></tr>`).join('');
  return `<div class="tblwrap"><table><thead><tr>
   ${th('title','video')}${th('channel','channel')}${th('view_count','views',1)}
   ${th('comment_count','comments',1)}${th('collected','collected',1)}${th('engagement','eng ‰',1)}
   ${th('transcript_done','tx')}${th('first_seen','first seen')}${th('last_checked','last checked')}
   </tr></thead><tbody>${rows}</tbody></table></div>`;
}

function spark(series){
  if(!series||!series.values||!series.values.length) return '';
  const vs=series.values, W=160, H=28, mx=Math.max(...vs,1);
  const pts=vs.map((v,i)=>`${(i/(vs.length-1)*W).toFixed(1)},${(H-2-v/mx*(H-4)).toFixed(1)}`).join(' ');
  return `<svg width="${W}" height="${H}"><polyline points="${pts}" fill="none" stroke="var(--acc)" stroke-width="1.5"/></svg>`;
}

function trendsSec(m){
  const e=Object.entries(m.trends?.series||{});
  if(!e.length) return '';
  const rows=e.map(([kw,s])=>`<tr><td>${esc(kw)}</td><td>${spark(s)}</td>
    <td class="num">${s.values?s.values[s.values.length-1]:'—'}</td>
    <td><a href="https://trends.google.com/trends/explore?q=${encodeURIComponent(kw)}" target="_blank">open</a></td></tr>`).join('');
  return `<section><h2>📈 Google Trends (12 m)</h2><div class="tblwrap"><table>
   <thead><tr><th>keyword</th><th>interest</th><th class="num">now</th><th></th></tr></thead>
   <tbody>${rows}</tbody></table></div>
   <div class="hint">pulled ${esc(m.trends.pulled_at||'')} · general-trend vs niche-artefact check</div></section>`;
}

function questionsSec(m){
  const qs=m.questions||[];
  if(!qs.length) return '';
  const rows=qs.slice().reverse().map(q=>`<li>${esc(q.text)} <span class="hint">(${esc(q.batch||'')})</span></li>`).join('');
  return `<section><details><summary>❓ Questions users ask (${qs.length}) — content/SEO ideas</summary>
   <div class="md"><ul>${rows}</ul></div></details></section>`;
}

function competitorsSec(m){
  const cs=m.competitors||[];
  if(!cs.length) return '';
  const by={};
  cs.forEach(c=>{(by[c.name]=by[c.name]||[]).push(c)});
  const rows=Object.entries(by).sort((a,b)=>b[1].length-a[1].length).map(([n,ms])=>{
    const p=ms.filter(x=>x.kind==='praise').length, c=ms.filter(x=>x.kind==='complaint').length;
    const det=ms.map(x=>`<li><b>${esc(x.kind)}</b> ${esc(x.text)} <span class="hint">(${esc(x.batch||'')})</span></li>`).join('');
    return `<h3>${esc(n)} — ${ms.length} mentions (👍${p} / 👎${c})</h3><ul>${det}</ul>`;}).join('');
  return `<section><details><summary>⚔️ Competitor mentions (${cs.length})</summary>
   <div class="md">${rows}</div></details></section>`;
}

function urls(m){
  const e=Object.entries(m.urls||{});
  if(!e.length) return '';
  const rows=e.map(([u,r])=>`<tr><td><a href="${esc(u)}" target="_blank">${esc(r.title||u)}</a></td>
    <td>${esc(r.kind||'article')}</td><td>${esc(r.added_at||'')}</td></tr>`).join('');
  return `<section><h2>Articles / blogs</h2><div class="tblwrap"><table>
   <thead><tr><th>url</th><th>kind</th><th>added</th></tr></thead><tbody>${rows}</tbody></table></div></section>`;
}

function render(){
  const ms=DATA.monitors;
  if(!ms.length){$('#app').innerHTML='<span class="hint">no monitor state found — run <code>python -m yt2nlm monitor … --init</code></span>';return;}
  CUR=Math.min(CUR,ms.length-1);
  const m=ms[CUR];
  const nVid=(m.videos||[]).length, nCom=(m.videos||[]).reduce((s,v)=>s+(v.collected||0),0);
  const arch=Object.entries(m.archives||{}).map(([p,a])=>`${p} vol.${a.vol} (${fmt(a.words)} words)`).join(' · ')||'—';
  let h='';
  if(ms.length>1) h+='<div class="tabs">'+ms.map((x,i)=>`<button class="${i===CUR?'on':''}" data-tab="${i}">${esc(x.key)}</button>`).join('')+'</div>';
  h+=`<div class="cards">${stat('notebook',esc(m.notebook_title||'—'))}
      ${stat('batches',(m.batches||[]).length)}${stat('videos seen',nVid)}
      ${stat('comments collected',fmt(nCom))}${stat('themes',(m.themes||[]).length)}
      <a class="stat" style="text-decoration:none;display:flex;flex-direction:column;justify-content:center"
         href="/api/monitor/pdf?key=${encodeURIComponent(m.key)}"
         title="Builds the document from the corpus AS IT IS right now — every download is the latest version. Large corpus: may take up to a minute.">
        <b>⬇ PDF</b><span>current corpus snapshot</span></a></div>
   <div class="hint" style="margin:-8px 0 16px">archives: ${arch} · updated ${esc((m.updated_at||'').slice(0,16))}</div>
   ${progressCard(m)}
   <section><h2>🏆 Scoreboard — themes by audience weight</h2>${scoreboard(m)}</section>
   ${coverage(m)}
   ${trendsSec(m)}
   <section><h2>Batches</h2>${batches(m)}</section>
   <section><h2>Videos / posts / apps we went through</h2>${videos(m)}</section>
   ${urls(m)}
   ${questionsSec(m)}
   ${competitorsSec(m)}
   <section><details><summary>💡 Proposals for the site</summary><div class="md">${m.proposals_md?marked.parse(m.proposals_md):'<span class=hint>none yet — run <code>monitor … --proposals</code></span>'}</div></details></section>
   <section><details><summary>📄 Latest digest</summary><div class="md">${m.latest_digest_md?marked.parse(m.latest_digest_md):'<span class=hint>none yet</span>'}</div></details></section>
   <section><details><summary>📚 Full ledger</summary><div class="md">${m.ledger_md?marked.parse(m.ledger_md):'<span class=hint>none yet</span>'}</div></details></section>`;
  $('#app').innerHTML=h;
}

document.addEventListener('click',e=>{
  const t=e.target.closest('[data-tab]'); if(t){CUR=+t.dataset.tab;render();return;}
  const s=e.target.closest('th[data-sort]');
  if(s){const k=s.dataset.sort;SORT= SORT.key===k?{key:k,dir:-SORT.dir}:{key:k,dir:-1};render();}
});

let OPEN=new Set();
function snapshotOpen(){OPEN=new Set([...document.querySelectorAll('details[open] summary')].map(s=>s.textContent.slice(0,20)))}
function restoreOpen(){document.querySelectorAll('details').forEach(d=>{const k=d.querySelector('summary')?.textContent.slice(0,20);if(OPEN.has(k))d.open=true;})}

function refresh(first){
  fetch('/api/monitor').then(r=>r.json()).then(d=>{
    snapshotOpen(); DATA=d; render(); restoreOpen();
  }).catch(err=>{if(first)$('#app').innerHTML='<span class="hint">failed to load: '+esc(String(err))+'</span>'});
}
refresh(true);
setInterval(()=>refresh(false),10000);   // heartbeat is a local file — cheap
</script>
</body></html>"""


def main():
    srv = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"yt2nlm-web on :{PORT}  (nlm={NLM_BIN}, state={STATE_DIR})", flush=True)
    srv.serve_forever()


if __name__ == "__main__":
    main()
