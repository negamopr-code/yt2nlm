#!/usr/bin/env python3
"""glottos-files (:8093): static files from /srv + two tiny JSON endpoints.
GET  /api/files -> mp4/mp3 list for the Videos tab
GET  /api/research -> glottos-methods snapshot (Research tab: confirmed methods, engagement, pipeline stage)
GET  /api/voice -> current voice choice      POST /api/voice {"voice": "..."} -> saves /srv/voices/choice.json
The Shorts builder (glottos-marketing/shorts/build_short_v2.py) reads choice.json when a unit has no fixed voice.
Replies (user 2026-09-27: "you prepare them and I decide if they go live"). This server is the ONLY writer of
/srv/replies/queue.json:
GET  /api/replies                      -> queue
POST /api/replies/add   {items:[...]}  -> comment-responder drafts (status "draft"; an existing key is left untouched)
POST /api/replies       {key, action: approve|reject|reopen, final?} -> the user's decision (browser)
POST /api/replies/posted {key}         -> reply.py posted it (status "posted")"""
import json, os, threading, time
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial

ROOT = "/srv"; CHOICE = os.path.join(ROOT, "voices", "choice.json")
QUEUE = os.path.join(ROOT, "replies", "queue.json"); QLOCK = threading.Lock()

def qload():
    try: return json.load(open(QUEUE))
    except Exception: return {"items": []}

def qsave(q):
    os.makedirs(os.path.dirname(QUEUE), exist_ok=True); tmp = QUEUE + ".tmp"
    json.dump(q, open(tmp, "w"), indent=1, ensure_ascii=False); os.replace(tmp, QUEUE)

class H(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache"); super().end_headers()
    def _json(self, obj, code=200):
        b = json.dumps(obj).encode(); self.send_response(code)
        self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(b)))
        self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        if self.path == "/api/files":
            out = []
            for dp, _, fs in os.walk(ROOT):
                for f in fs:
                    if f.endswith((".mp4", ".webm")):
                        p = os.path.join(dp, f); out.append({"path": os.path.relpath(p, ROOT), "mtime": os.path.getmtime(p), "size": os.path.getsize(p)})
            return self._json(sorted(out, key=lambda x: -x["mtime"]))
        if self.path == "/api/pipeline":                                  # Pipeline tab: autopilot state + log tail (read-only mounts)
            try: st = json.load(open("/state/autopilot.json"))
            except Exception as e: st = {"error": str(e)}
            try:
                lines = open("/autopilot/log.txt", errors="replace").read().splitlines()
                ticks = [l for l in lines if " tick: " in l or " tick end " in l or "loop start" in l]
                running = bool(ticks) and " tick: " in ticks[-1]
                return self._json({"state": st, "ticks": ticks[-12:], "running": running, "now": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
            except Exception as e:
                return self._json({"state": st, "ticks": [], "running": False, "log_error": str(e)})
        if self.path == "/api/research":                                  # Research tab: glottos-methods pipeline snapshot
            try: return self._json(json.load(open("/state/methods/research.json")))
            except Exception as e: return self._json({"error": f"no research snapshot yet ({e})", "pains": []})
        if self.path == "/api/replies":
            with QLOCK: return self._json(qload())
        if self.path == "/api/voice":
            try: return self._json(json.load(open(CHOICE)))
            except Exception: return self._json({"voice": None})
        return super().do_GET()
    def do_POST(self):
        if self.path.startswith("/api/replies"): return self.replies()
        if self.path != "/api/voice": return self._json({"error": "not found"}, 404)
        try:
            d = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
            v = str(d.get("voice", ""))[:80]
            if not v: raise ValueError("voice missing")
            os.makedirs(os.path.dirname(CHOICE), exist_ok=True)
            tmp = CHOICE + ".tmp"; json.dump({"voice": v, "at": time.strftime("%Y-%m-%dT%H:%M:%S")}, open(tmp, "w")); os.replace(tmp, CHOICE)
            return self._json({"ok": True, "voice": v})
        except Exception as e:
            return self._json({"error": str(e)}, 400)

    def replies(self):
        try:
            d = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}"); now = time.strftime("%Y-%m-%dT%H:%M:%S")
            with QLOCK:
                q = qload(); by = {x["key"]: x for x in q["items"]}
                if self.path == "/api/replies/add":
                    n = 0
                    for it in d.get("items", []):
                        if it.get("key") and it["key"] not in by and (it.get("draft") or it.get("type") == "spam"):
                            it = dict(it, status="draft", drafted_at=now); q["items"].append(it); by[it["key"]] = it; n += 1
                    qsave(q); return self._json({"ok": True, "added": n})
                it = by.get(d.get("key"))
                if not it: return self._json({"error": "unknown key"}, 404)
                if self.path == "/api/replies/posted":
                    if it.get("status") != "approved": return self._json({"error": "not approved"}, 409)
                    it.update(status="posted", posted_at=now)
                else:
                    if it.get("status") == "posted": return self._json({"error": "already posted"}, 409)
                    a = d.get("action")
                    if a not in ("approve", "reject", "reopen"): return self._json({"error": "bad action"}, 400)
                    if "final" in d: it["final"] = str(d["final"])[:5000].strip()
                    it.update(status={"approve": "approved", "reject": "rejected", "reopen": "draft"}[a], decided_at=now)
                qsave(q); return self._json({"ok": True, "item": it})
        except Exception as e:
            return self._json({"error": str(e)}, 400)

ThreadingHTTPServer(("0.0.0.0", 8000), partial(H, directory=ROOT)).serve_forever()
