"""Review queue + 1-click upload on :8108 (stdlib http.server).

Everything the user needs in one page: item cards with seekable <video>
preview (Range serving), editable metadata, WordNet flags, render trigger,
OAuth connect, Approve -> YouTube upload (private)."""

from __future__ import annotations

import json
import mimetypes
import os
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

from . import upload as up
from .config import REPORTS, load_config, load_state, save_state

PORT = int(os.environ.get("PORT", "8108"))
_flows: dict = {}          # oauth state -> flow (single-user, in-memory)
_render_lock = threading.Lock()


def _progress() -> dict:
    try:
        return json.loads((REPORTS / "progress.json").read_text())
    except OSError:
        return {}


def _spawn_render(n: int, fmt: str) -> bool:
    if not _render_lock.acquire(blocking=False):
        return False

    def go():
        try:
            subprocess.run([sys.executable, "-m", "videogen", "make", str(n),
                            "--format", fmt], cwd=str(REPORTS.parent.parent))
        finally:
            _render_lock.release()
    threading.Thread(target=go, daemon=True).start()
    return True


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        if isinstance(body, (dict, list)):
            body = json.dumps(body, ensure_ascii=False).encode()
        elif isinstance(body, str):
            body = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    # ------------------------------------------------------------------ GET
    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/":
            self._send(200, PAGE, "text/html; charset=utf-8")
        elif u.path == "/api/queue":
            state = load_state()
            items = sorted(state["items"].values(),
                           key=lambda i: i["id"], reverse=True)
            for it in items:
                meta_p = Path(it["dir"]) / "meta.json"
                it["meta"] = (json.loads(meta_p.read_text())
                              if meta_p.exists() else {})
                script_p = Path(it["dir"]) / "script.json"
                if script_p.exists():
                    s = json.loads(script_p.read_text())
                    it["flags"] = [y["word"] for y in s.get("synonyms", [])
                                   if y.get("wordnet") not in ("verified", None)
                                   and y.get("wordnet") != "related"]
                    it["synonyms"] = [(y["word"], y.get("wordnet", ""))
                                      for y in s.get("synonyms", [])]
            self._send(200, {"items": items, "progress": _progress(),
                             "oauth": up.TOKEN_PATH.exists(),
                             "client": up.client_config() is not None,
                             "uploads": load_state()["uploads"]})
        elif u.path == "/api/oauth/start":
            if up.client_config() is None:
                self._send(400, {"error": "put your Desktop OAuth client json "
                                          "into state/videogen.oauth-client.json "
                                          "first (GCP → YouTube Data API v3)"})
                return
            host = self.headers.get("Host", f"localhost:{PORT}")
            url, flow = up.auth_url(f"http://{host}/oauth2cb")
            _flows["flow"] = flow
            self._send(200, {"url": url})
        elif u.path == "/oauth2cb":
            code = (parse_qs(u.query).get("code") or [""])[0]
            flow = _flows.pop("flow", None)
            if not code or flow is None:
                self._send(400, "OAuth callback without code/flow — retry "
                                "Connect YouTube", "text/plain")
                return
            try:
                up.finish_auth(flow, code)
                self._send(200, "<h2>YouTube connected ✓</h2>"
                                "<a href='/'>back to the queue</a>",
                           "text/html")
            except Exception as exc:
                self._send(500, f"token exchange failed: {exc}", "text/plain")
        elif u.path.startswith("/media/"):
            self._media(unquote(u.path[len("/media/"):]))
        else:
            self._send(404, {"error": "not found"})

    def _media(self, rel: str):
        base = os.path.realpath(REPORTS)
        path = os.path.realpath(os.path.join(base, rel))
        if not path.startswith(base) or not os.path.isfile(path):
            self._send(404, {"error": "not found"})
            return
        size = os.path.getsize(path)
        ctype = mimetypes.guess_type(path)[0] or "application/octet-stream"
        rng = self.headers.get("Range")
        start, end = 0, size - 1
        if rng and rng.startswith("bytes="):
            try:
                a, b = rng[6:].split("-", 1)
                start = int(a) if a else max(0, size - int(b))
                if a and b:
                    end = min(int(b), size - 1)
            except ValueError:
                pass
        length = end - start + 1
        self.send_response(206 if rng else 200)
        self.send_header("Content-Type", ctype)
        self.send_header("Accept-Ranges", "bytes")
        if rng:
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Content-Length", str(length))
        self.end_headers()
        with open(path, "rb") as fh:
            fh.seek(start)
            left = length
            while left > 0:
                chunk = fh.read(min(65536, left))
                if not chunk:
                    break
                try:
                    self.wfile.write(chunk)
                except BrokenPipeError:
                    return
                left -= len(chunk)

    # ----------------------------------------------------------------- POST
    def do_POST(self):
        u = urlparse(self.path)
        try:
            n = int(self.headers.get("Content-Length") or 0)
            req = json.loads(self.rfile.read(n) or b"{}")
        except Exception:
            self._send(400, {"error": "bad json"})
            return
        if u.path == "/api/render":
            ok = _spawn_render(int(req.get("n", 1)),
                               req.get("format", "shorts"))
            self._send(200 if ok else 409,
                       {"ok": ok} if ok else {"error": "a render job is "
                                                       "already running"})
            return
        parts = u.path.strip("/").split("/")
        if len(parts) == 3 and parts[0] == "api":
            action, item_id = parts[1], parts[2]
            state = load_state()
            it = state["items"].get(item_id)
            if not it:
                self._send(404, {"error": "unknown item"})
                return
            d = Path(it["dir"])
            if action == "meta":
                meta_p = d / "meta.json"
                meta = json.loads(meta_p.read_text())
                for k in ("title", "description", "tags", "privacyStatus"):
                    if k in req:
                        meta[k] = req[k]
                meta_p.write_text(json.dumps(meta, ensure_ascii=False,
                                             indent=1))
                self._send(200, {"ok": True})
            elif action == "reject":
                it["status"] = "rejected"
                save_state(state)
                self._send(200, {"ok": True})
            elif action == "approve":
                cfg = load_config()
                if not up.quota_ok(state, cfg["uploads_per_day"]):
                    self._send(429, {"error": "daily upload quota (6) reached"})
                    return
                meta = json.loads((d / "meta.json").read_text())
                try:
                    vid = up.upload(d, meta)
                except Exception as exc:
                    self._send(500, {"error": str(exc)[:300]})
                    return
                it["status"] = "uploaded"
                it["youtube_id"] = vid
                up.count_upload(state)
                save_state(state)
                self._send(200, {"ok": True, "youtube_id": vid,
                                 "url": f"https://studio.youtube.com/video/{vid}/edit"})
            else:
                self._send(404, {"error": "unknown action"})
        else:
            self._send(404, {"error": "not found"})


PAGE = r"""<!doctype html>
<html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Another Word · video queue</title>
<style>
 :root{--bg:#0f1419;--card:#1a2029;--line:#2a3340;--fg:#e6edf3;--mut:#8b98a5;--acc:#4493f8;--ok:#3fb950;--warn:#d29922}
 *{box-sizing:border-box} body{margin:0;font:14px/1.5 system-ui;background:var(--bg);color:var(--fg)}
 header{padding:14px 22px;border-bottom:1px solid var(--line);display:flex;gap:14px;align-items:center;flex-wrap:wrap}
 h1{margin:0;font-size:16px} .mut{color:var(--mut);font-size:12px}
 button{background:var(--acc);color:#fff;border:0;border-radius:7px;padding:7px 14px;font:inherit;font-weight:600;cursor:pointer}
 button.sec{background:var(--line)} button.ok{background:var(--ok)} button.warn{background:#8a3b3b}
 button:disabled{opacity:.5;cursor:default}
 .wrap{padding:18px 22px;display:grid;grid-template-columns:repeat(auto-fill,minmax(430px,1fr));gap:16px}
 .card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px}
 video{width:100%;max-height:420px;background:#000;border-radius:8px}
 input,textarea{width:100%;background:var(--bg);color:var(--fg);border:1px solid var(--line);border-radius:6px;padding:6px;font:inherit;margin:3px 0}
 textarea{min-height:70px}
 .badge{display:inline-block;border-radius:9px;padding:0 8px;font-size:11px;background:var(--line);color:var(--mut)}
 .badge.rendered{background:#1f4429;color:#7ee2a0}.badge.uploaded{background:#143a5e;color:#7cc0ff}
 .badge.failed,.badge.rejected{background:#4a1f24;color:#f5989d}
 .flag{color:#f5b942;font-size:12px}
 #prog{font-size:12px;color:var(--mut)}
 .row{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-top:8px}
</style></head><body>
<header>
 <h1>🎬 Another Word — review queue</h1>
 <button onclick="render('shorts')">＋ make Short</button>
 <button onclick="render('long')">＋ make long-form</button>
 <button class="sec" id="oauthBtn" onclick="oauth()">connect YouTube</button>
 <span id="prog"></span>
</header>
<div class="wrap" id="q"><span class="mut">loading…</span></div>
<script>
const $=s=>document.querySelector(s);
const esc=s=>(s==null?'':String(s)).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
let D=null;
function load(){fetch('/api/queue').then(r=>r.json()).then(d=>{D=d;draw();});}
function draw(){
  const p=D.progress||{};
  $('#prog').textContent = p.status==='running' ? `⏳ ${p.phase} ${p.detail||''}` :
    `uploads today: ${D.uploads?.count||0}/6 · ${D.oauth?'YouTube ✓':(D.client?'YouTube not connected':'no OAuth client configured')}`;
  $('#oauthBtn').style.display = D.oauth ? 'none':'inline-block';
  const items=(D.items||[]).filter(i=>i.status!=='rejected');
  $('#q').innerHTML = items.map(card).join('') || '<span class="mut">queue is empty — hit “make Short”</span>';
}
function card(it){
  const m=it.meta||{};
  const flags=(it.flags||[]).length?`<div class="flag">⚠ WordNet-flagged: ${it.flags.join(', ')}</div>`:'';
  const canUp = it.status==='rendered' && D.oauth;
  const vid = it.status==='rendered'||it.status==='uploaded' ?
    `<video controls preload="metadata" src="/media/${it.id}/final.mp4" poster="/media/${it.id}/thumb.jpg"></video>`:'';
  const yt = it.youtube_id?`<a class="badge uploaded" target="_blank" href="https://studio.youtube.com/video/${it.youtube_id}/edit">Studio ↗</a>`:'';
  return `<div class="card">
   <div class="row"><b>${it.id}</b> <span class="badge ${esc(it.status)}">${esc(it.status)}</span>
     <span class="mut">${esc(it.target)} · ${esc(it.format)}</span> ${yt}</div>
   ${vid}${flags}
   <input value="${esc(m.title||'')}" id="t_${it.id}" placeholder="title">
   <textarea id="d_${it.id}" placeholder="description">${esc(m.description||'')}</textarea>
   <input value="${esc((m.tags||[]).join(', '))}" id="g_${it.id}" placeholder="tags, comma separated">
   <div class="row">
    <button class="sec" onclick="saveMeta('${it.id}')">save meta</button>
    ${canUp?`<button class="ok" onclick="approve('${it.id}')">✓ approve → upload (private)</button>`:''}
    ${it.status!=='uploaded'?`<button class="warn" onclick="reject('${it.id}')">✗ reject</button>`:''}
    ${it.error?`<span class="flag">error: ${esc(it.error)}</span>`:''}
   </div></div>`;
}
function api(p,body){return fetch(p,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body||{})}).then(r=>r.json());}
function render(f){api('/api/render',{n:1,format:f}).then(d=>{if(d.error)alert(d.error);load();});}
function saveMeta(id){api('/api/meta/'+id,{title:$('#t_'+id).value,description:$('#d_'+id).value,
  tags:$('#g_'+id).value.split(',').map(s=>s.trim()).filter(Boolean)}).then(()=>load());}
function approve(id){if(!confirm('Upload to YouTube as PRIVATE?'))return;
  api('/api/approve/'+id).then(d=>{d.error?alert(d.error):window.open(d.url,'_blank');load();});}
function reject(id){api('/api/reject/'+id).then(()=>load());}
function oauth(){fetch('/api/oauth/start').then(r=>r.json()).then(d=>{d.error?alert(d.error):location.href=d.url;});}
load(); setInterval(load, 8000);
</script></body></html>"""


def main():
    srv = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"videogen review queue on :{PORT}", flush=True)
    srv.serve_forever()
