#!/usr/bin/env python3
"""Claude-free uploads (user 2026-09-28: "yes do both" — uploads keep going through Claude usage pauses and cost no
Claude tokens). Called by loop.sh on every loop, inside the tick lock, BEFORE the Claude limit check.

Picks the first episode/special at step=upload (not blocked, fewer than 2 failed auto attempts) and runs
yt-studio/upload.py with its language-gated content/youtube/<epNN|m1>.json: PRIVATE draft + title/description/tags/
kids, then the finish pass (playlist, language, category) and a VERIFY read-back. Afterwards checks from OUTSIDE that
the video is not publicly viewable (YouTube oEmbed must NOT answer 200).
  success   -> youtube=<link>, step=publish_log (a normal Claude tick writes the journal later)
  signed out-> ask_user + resume_step=upload (due.py resumes it by itself after the next sign-in)
  failure   -> upload_auto_fail += 1; after 2 the item is left to a Claude upload tick (due.py) to debug
Exit 0 = did something (uploaded / parked / failed), 1 = nothing to do."""
import json, re, subprocess, sys, urllib.request, urllib.error
from datetime import datetime, timezone
P = "/workspace/glottos-marketing/state/autopilot.json"
META = "/workspace/glottos-marketing/content/youtube"
ASK = "/workspace/glottos-auto/out/analytics/ask-user.md"
JOURNAL = "/workspace/glottos-marketing/docs/nlm-mirror/discussion-journal.md"
PY = ["docker", "exec", "-u", "app", "yt-studio", "/home/app/yt-profile/.venv/bin/python"]
now = datetime.now(timezone.utc); stamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")

def t(x):
    try: return datetime.fromisoformat(x.replace("Z", "+00:00"))
    except Exception: return None

def ask_user(title, body):                                  # newest on top, same format the Claude ticks use
    try: old = open(ASK).read()
    except Exception: old = ""
    open(ASK, "w").write(f"## {stamp} — {title}\n{body}\n\n" + old)

def journal(line):
    with open(JOURNAL, "a") as f: f.write(f"autopilot {stamp} (auto_upload, no Claude): {line}\n")


# HD master (user 2026-09-28: "the quality of video is not HD, but SD ... at least HD"; only for videos NOT yet on
# YouTube). NotebookLM videos are 1280x720 at ~0.5-0.8 Mbit/s and YouTube serves a 720p upload at a low bitrate, so
# every upload goes up as a 1440p master (short side 1440, lanczos + light unsharp, x264 CRF 16): crisper lines,
# and YouTube streams 1440p uploads with VP9 at every quality. The source file stays untouched.
import os
FF = "/workspace/glottos-marketing/.nlmvenv/lib/python3.11/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
OUT = "/workspace/glottos-auto/out"

def probe(path):
    err = subprocess.run([FF, "-hide_banner", "-i", path], capture_output=True, text=True).stderr
    wh = re.search(r"Video: .*?(\d{3,5})x(\d{3,5})", err); du = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err)
    return (int(wh.group(1)), int(wh.group(2))) if wh else None, (int(du.group(1)) * 3600 + int(du.group(2)) * 60 + float(du.group(3))) if du else None

def hd_master(vid):
    src = f"{OUT}/{vid}.mp4"; (w, h), dur = probe(src)
    if min(w, h) >= 1440: return vid, f"source already {w}x{h}"
    hd = f"{vid}-hd1440"; dst = f"{OUT}/{hd}.mp4"
    if not (os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src)):
        tmp = dst[:-4] + ".part.mp4"
        r = subprocess.run([FF, "-v", "error", "-y", "-i", src, "-vf",
                            "scale=w='if(gt(iw,ih),-2,1440)':h='if(gt(iw,ih),1440,-2)':flags=lanczos,unsharp=5:5:0.6:5:5:0.0",
                            "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-profile:v", "high", "-pix_fmt", "yuv420p",
                            "-threads", "4", "-c:a", "copy", "-movflags", "+faststart", tmp], capture_output=True, text=True, timeout=7200)
        if r.returncode: raise RuntimeError("hd encode failed: " + r.stderr[-300:])
        os.replace(tmp, dst)
    (w2, h2), dur2 = probe(dst)
    if min(w2, h2) != 1440 or dur is None or dur2 is None or abs(dur2 - dur) > 0.5:
        raise RuntimeError(f"hd master check failed: {w2}x{h2}, {dur2}s vs source {dur}s")
    return hd, f"{w}x{h} -> {w2}x{h2} master"

s = json.load(open(P))
todo = [("episode", k, e, f"ep{int(k):02d}.json") for k, e in sorted(s["episodes"].items(), key=lambda x: int(x[0]))] + \
       [("special", k, e, f"{k.lower()}.json") for k, e in sorted(s.get("specials", {}).items())]
pick = None
for kind, k, e, meta_name in todo:
    b = t(e.get("blocked_until") or "")
    if e.get("step") == "upload" and not (b and b > now) and e.get("upload_auto_fail", 0) < 2:
        pick = (kind, k, e, meta_name); break
if not pick: sys.exit(1)
kind, k, e, meta_name = pick; name = f"{kind} {k}"
meta = json.load(open(f"{META}/{meta_name}"))
vid = (meta.get("video_ids_local") or [None])[-1]
print(f"auto_upload: {name}: {vid} + {meta_name}")

def save(): json.dump(s, open(P, "w"), indent=2)

if not vid:
    e["upload_auto_fail"] = 2; e["note"] = f"{stamp}: auto_upload: {meta_name} has no video_ids_local; left to a Claude upload tick"
    save(); print("  no video id -> Claude tick"); sys.exit(0)

si = subprocess.run(PY + ["/opt/yt/signed_in.py"], capture_output=True, text=True, timeout=90)
if si.returncode == 2:
    e["step"] = "ask_user"; e["resume_step"] = "upload"
    e["note"] = f"{stamp}: STOPPED — YouTube Studio is signed out (signed_in.py). Nothing uploaded. Resumes by itself after sign-in at http://localhost:8115/vnc.html"
    save(); ask_user(f"YouTube is signed out: {name} upload is waiting (needs you)",
                     f"Sign in as @anotherword8913 at http://localhost:8115/vnc.html. The upload of `{vid}` then starts by itself within 10 min.")
    print("  signed out -> ask_user"); sys.exit(0)

hd_note = "HD master skipped (hd_master=false)"
if e.get("hd_master", True):
    try: vid, hd_note = hd_master(vid); print("  hd:", hd_note)
    except Exception as x:
        n = e.get("upload_auto_fail", 0) + 1; e["upload_auto_fail"] = n
        e["note"] = f"{stamp}: auto_upload attempt {n}: HD master FAILED, nothing uploaded: {str(x)[:250]}"
        save(); journal(f"{name} HD master failed ({str(x)[:160]})"); sys.exit(0)
try:
    r = subprocess.run(PY + ["/opt/yt/upload.py", vid, meta_name], capture_output=True, text=True, timeout=2400)
    out = (r.stdout or "") + (r.stderr or "")
except subprocess.TimeoutExpired as x:
    out = f"TIMEOUT after 40 min: {x.stdout or ''}"
print("  " + out.strip().replace("\n", "\n  ")[-2500:])
m = re.search(r"UPLOADED \(private draft\): (\S+)", out) or re.search(r"already uploaded: .*?'link': '([^']+)'", out)
if not m:
    n = e.get("upload_auto_fail", 0) + 1; e["upload_auto_fail"] = n
    tail = out.strip().splitlines()[-1][:300] if out.strip() else "no output"
    e["note"] = f"{stamp}: auto_upload attempt {n} FAILED: {tail}" + (" — handed to a Claude upload tick" if n >= 2 else " — retrying next loop")
    save(); journal(f"{name} upload attempt {n} failed ({tail[:160]})"); sys.exit(0)

link = m.group(1)
vm = re.search(r"^VERIFY: (\{.*\})$", out, re.M)
verify = json.loads(vm.group(1)) if vm else {"all_ok": False, "error": "no VERIFY line"}
yid = verify.get("id") or (re.search(r"(?:youtu\.be/|/shorts/|v=)([A-Za-z0-9_-]{11})", link) or [None, None])[1]
try:
    code = urllib.request.urlopen(f"https://www.youtube.com/oembed?format=json&url=https://www.youtube.com/watch?v={yid}", timeout=20).status
except urllib.error.HTTPError as x: code = x.code
except Exception: code = None
private_ok = code in (401, 403, 404)                       # 200 = anyone can watch it = NOT private

e["youtube"] = link; e["step"] = "publish_log"; e.pop("upload_auto_fail", None)
bad = [f for f, v in (verify.get("ok") or {}).items() if not v] + ([verify["error"]] if verify.get("error") else [])
e["note"] = (f"{stamp}: uploaded PRIVATE draft {link} (auto_upload, no Claude; {hd_note}); finish: {', '.join(verify.get('did') or []) or 'nothing to change'}; "
             f"verify: {'ALL OK' if verify.get('all_ok') else 'CHECK ' + ', '.join(bad)}; outside view: {'private ✓' if private_ok else f'oEmbed {code} ✗'}")
save()
journal(f"{name} '{meta['title']}' uploaded as PRIVATE draft {link}; {e['note'].split('; ', 1)[1]}")
if not private_ok:
    ask_user(f"⚠ {name} may be VIEWABLE by anyone — check Studio now",
             f"`{link}` answered YouTube oEmbed with {code} right after upload (a private video must not answer 200). Open it in Studio and set it to Private.")
elif bad:
    ask_user(f"{name} is uploaded (private) — one field needs a look in Studio (no answer needed)",
             f"`{link}`: {', '.join(bad)} didn't verify. Studio → Edit draft to fix. Everything else was set.")
else:
    ask_user(f"{name} is uploaded as a PRIVATE draft, ready for you to publish (no answer needed)",
             f"**{meta['title']}** — {link}. Title, description, tags, not-for-kids, language, category"
             + (f", playlist *{meta['playlist']}*" if meta.get("playlist") else "") + " set and verified. Publishing is your click in Studio.")
print(f"  done: {e['note']}")
sys.exit(0)
