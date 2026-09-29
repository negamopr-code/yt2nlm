#!/usr/bin/env python3
"""Is a Claude step due? No Claude needed to decide (the autopilot's cheap pre-check).
Exit 0 + print the reason when a step should run now; exit 1 when everything is running, waiting (NLM limit)
or done. A `running` flag left by a crashed tick is cleared (the loop only calls this while holding the tick lock)."""
import json, sys
from datetime import datetime, timezone, timedelta
P = "/workspace/glottos-marketing/state/autopilot.json"
now = datetime.now(timezone.utc)
def t(s):
    try: return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception: return None
s = json.load(open(P)); changed = False
for n, e in sorted(s["episodes"].items(), key=lambda x: int(x[0])):
    if e.get("running"):                                           # we hold the lock, so nobody is running it
        e["stale_running"] = e.pop("running"); changed = True
ch = s.get("channel", {})                                          # channel care first: quick, and users wait on it
if ch.get("reply_drafts_due"):
    if changed: json.dump(s, open(P, "w"), indent=2)
    print("channel: reply_drafts"); sys.exit(0)
lm0 = t(ch.get("last_monitor") or "")
if lm0 is None or now - lm0 > timedelta(hours=24):
    if changed: json.dump(s, open(P, "w"), indent=2)
    print("channel: monitor"); sys.exit(0)
# NotebookLM-limited steps run strictly in EPISODE ORDER (user 2026-09-27: "everything which rate limited by nlm
# goes in series, not in parallel ... first complete episode 2 instead of trying to generate pictures or audio for
# episode 4"). An episode may run an NLM step only when every earlier episode is past ALL of its NLM steps; a
# rate-limited earlier episode makes later ones WAIT instead of handing them the quota. Non-NLM steps of later
# episodes (scenario, gate_text, ...) may still run meanwhile, one at a time.
STEPS = ["scenario", "gate_text", "audio", "gate_recording", "visuals", "render", "critic", "studio",
         "yt_meta_gate", "upload", "publish_log"]
# pipeline "video" (user 2026-09-29, Ep3 pilot: "yes you can experiment on episode 3 and if doesnt work, change it"):
# ONE NotebookLM video overview replaces audio + gate_recording + visuals + render; then polish into 9:16 like the specials.
VIDEO_STEPS = ["scenario", "gate_text", "nlm_video", "critic", "polish", "critic", "studio", "yt_meta_gate", "upload",
               "publish_log"]
NLM_STEPS = {"audio", "visuals", "nlm_video"}
def owes_nlm(e):
    st = e.get("step")
    if st in ("done", "stopped"): return False
    steps = VIDEO_STEPS if e.get("pipeline") == "video" else STEPS
    last = max(steps.index(x) for x in NLM_STEPS if x in steps)
    return st not in steps or steps.index(st) <= last               # ask_user/unknown counts as still owing
# Parked uploads resume BY THEMSELVES once YouTube Studio is signed in again (user 2026-09-28: "it should probe
# time and time again if account is signed in"). An item at ask_user with resume_step=upload is re-checked on every
# loop (10 min) with yt-studio/signed_in.py, which reads cookie metadata only: no Claude, no Google request.
import subprocess
def yt_signed_in():
    try:
        return subprocess.run(["docker", "exec", "yt-studio", "/home/app/yt-profile/.venv/bin/python", "/opt/yt/signed_in.py"],
                              capture_output=True, timeout=60).returncode == 0
    except Exception:
        return False
_parked = [e for e in list(s["episodes"].values()) + list(s.get("specials", {}).values())
           if e.get("step") == "ask_user" and e.get("resume_step") == "upload"]
if _parked and yt_signed_in():
    for e in _parked:
        e["step"] = "upload"; e.pop("resume_step", None)
        e["note"] = f"auto-resumed {now.strftime('%Y-%m-%dT%H:%M:%SZ')}: YouTube Studio signed in again (signed_in.py) — was: " + str(e.get("note", ""))[:300]
    changed = True
# Uploads are done WITHOUT Claude by auto_upload.py (user 2026-09-28: "yes do both"), run by loop.sh before this.
# A Claude upload tick only gets an item after 2 failed auto attempts (to debug it).
def auto_owned(e): return e.get("step") == "upload" and e.get("upload_auto_fail", 0) < 2
# Uploads jump the queue (user 2026-09-28: "why it takes so long to upload videos?"): finished videos waited behind
# episode NLM ticks (~23 min each, possibly several), because any due episode step always won over specials. An
# upload is short, needs no NotebookLM, and is what the user is waiting for, so any due upload runs first.
for kind, items in (("episode", sorted(s["episodes"].items(), key=lambda x: int(x[0]))),
                    ("special", sorted(s.get("specials", {}).items()))):
    for k, e in items:
        b = t(e.get("blocked_until") or "")
        if e.get("step") == "upload" and not (b and b > now) and not auto_owned(e):
            if changed: json.dump(s, open(P, "w"), indent=2)
            print(f"{kind} {k}: upload"); sys.exit(0)
gate = None                                                         # earliest episode that still owes NLM work
for n, e in sorted(s["episodes"].items(), key=lambda x: int(x[0])):
    wait = f"NLM steps run in series: waiting for episode {gate}" if gate and e.get("step") in NLM_STEPS else None
    if e.get("nlm_wait") != wait:
        if wait: e["nlm_wait"] = wait
        else: e.pop("nlm_wait", None)
        changed = True
    if gate is None and owes_nlm(e): gate = n
    # nlm_job = a NotebookLM generation nlm_jobs.py is waiting on / retrying WITHOUT Claude (user 2026-09-29: cheap tokens)
    if wait or e.get("step") in ("done", "stopped", "ask_user") or auto_owned(e) or e.get("nlm_job"): continue
    b = t(e.get("blocked_until") or "")
    if b and b > now: continue
    if changed: json.dump(s, open(P, "w"), indent=2)
    print(f"episode {n}: {e.get('step')}"); sys.exit(0)
# Specials (user 2026-09-27): one-off pieces outside the episode chain, e.g. M1 = the P01 mid-length video on
# NotebookLM work2 (a different account, so the drawnformula NLM series rule doesn't apply to it).
# wait_strategy is checked HERE, without Claude: due only once the method-research daemon has researched the pain.
import os
# NotebookLM video generation for specials runs in SERIES too (M1, then S1, S2, ...): a special may start nlm_video
# only when every earlier special is past it. Scripts / language gates of later specials may still run meanwhile.
SP_BEFORE_VIDEO = ("wait_strategy", "decide", "script", "gate_text", "nlm_video")
sp_gate = None
for k, sp in sorted(s.get("specials", {}).items()):
    st = sp.get("step")
    wait = f"NLM video in series: waiting for {sp_gate}" if sp_gate and st == "nlm_video" else None
    if sp.get("nlm_wait") != wait:
        if wait: sp["nlm_wait"] = wait
        else: sp.pop("nlm_wait", None)
        changed = True
    if sp_gate is None and st in SP_BEFORE_VIDEO: sp_gate = k
    if wait or st in ("done", "stopped", "ask_user") or auto_owned(sp) or sp.get("nlm_job"): continue
    if st == "wait_strategy":
        pid = sp.get("pain", "P01")
        try: pn = {x["id"]: x for x in json.load(open("/workspace/state/glottos-methods/pains.json"))["pains"]}.get(pid, {})
        except Exception: pn = {}
        if pn.get("status") != "researched" or not os.path.exists(f"/workspace/state/glottos-methods/{pid}/strategy.md"):
            continue
        sp["step"] = "script" if sp.get("format_decision") else "decide"      # the user may already have decided the format
        sp["note"] = f"strategy for {pid} ready {pn.get('researched_at')}" + (f"; format: {sp['format_decision'][:60]}" if sp.get("format_decision") else ""); changed = True
    b = t(sp.get("blocked_until") or "")
    if b and b > now: continue
    if changed: json.dump(s, open(P, "w"), indent=2)
    print(f"special {k}: {sp['step']}"); sys.exit(0)
ch = s.get("channel", {}); lm = t(ch.get("last_monitor") or "")
if lm is None or now - lm > timedelta(hours=24):
    if changed: json.dump(s, open(P, "w"), indent=2)
    print("channel: monitor"); sys.exit(0)
if ch.get("reply_drafts_due"):
    print("channel: reply_drafts"); sys.exit(0)
if changed: json.dump(s, open(P, "w"), indent=2)
sys.exit(1)
