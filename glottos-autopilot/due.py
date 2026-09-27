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
NLM_STEPS = {"audio", "visuals"}
LAST_NLM = max(STEPS.index(x) for x in NLM_STEPS)
def owes_nlm(e):
    st = e.get("step")
    if st in ("done", "stopped"): return False
    return st not in STEPS or STEPS.index(st) <= LAST_NLM          # ask_user/unknown counts as still owing
gate = None                                                         # earliest episode that still owes NLM work
for n, e in sorted(s["episodes"].items(), key=lambda x: int(x[0])):
    wait = f"NLM steps run in series: waiting for episode {gate}" if gate and e.get("step") in NLM_STEPS else None
    if e.get("nlm_wait") != wait:
        if wait: e["nlm_wait"] = wait
        else: e.pop("nlm_wait", None)
        changed = True
    if gate is None and owes_nlm(e): gate = n
    if wait or e.get("step") in ("done", "stopped", "ask_user"): continue
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
    if wait or st in ("done", "stopped", "ask_user"): continue
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
