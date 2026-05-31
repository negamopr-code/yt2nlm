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
        nbs = d.get("notebooks") or []
        if not nbs:
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


def main():
    srv = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"yt2nlm-web on :{PORT}  (nlm={NLM_BIN}, state={STATE_DIR})", flush=True)
    srv.serve_forever()


if __name__ == "__main__":
    main()
