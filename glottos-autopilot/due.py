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
# PAUSE (user 2026-09-30: "let us finished current video production in progress and then pause for a while"):
# glottos-autopilot/pause.json {"hold_episodes": [...], "hold_specials": [...]} -> held items never get a Claude tick,
# and while the file exists the Claude channel steps (monitor, reply drafts) stop too. Mechanical no-Claude work
# (approved replies, likes, snapshots, uploads) keeps running. Resume = delete pause.json.
import os
PAUSE = "/workspace/glottos-autopilot/pause.json"
try: _pz = json.load(open(PAUSE)) if os.path.exists(PAUSE) else None
except Exception: _pz = {}
HOLD_E = set(map(str, (_pz or {}).get("hold_episodes", []))); HOLD_S = set(map(str, (_pz or {}).get("hold_specials", [])))
PAUSED = bool(_pz and _pz.get("hold_channel"))      # user 2026-10-03: "comments I still do not see" -> the production pause no longer stops comment care (monitor + reply drafts); set hold_channel:true to stop those too
for n, e in sorted(s["episodes"].items(), key=lambda x: int(x[0])):
    if e.get("running"):                                           # we hold the lock, so nobody is running it
        e["stale_running"] = e.pop("running"); changed = True
# Send controller (user 2026-10-05): send_watch.py could not repair a "Send to YouTube" problem for 2 runs -> ONE tick for the agent
# glottos-send-controller (it sets agent_done_for when finished, so the same problem never gets a second tick).
try:
    _sw = json.load(open("/workspace/glottos-auto/out/yt/send-watch.json"))
    if _sw.get("needs_agent") and sorted(_sw.get("agent_done_for") or []) != sorted(_sw.get("problems") or []):
        if changed: json.dump(s, open(P, "w"), indent=2)
        print("send: repair"); sys.exit(0)
except Exception: pass
# Sends first (user 2026-10-07: "I approved all videos, but they are not going"): while a "Send to YouTube" click is waiting or being
# sent, no Claude tick starts - a tick holds the browser lock until it ends (lab: analyze = 55 min). Only jobs touched in the last
# 3 h count, so a job that hangs cannot stop the autopilot (the send controller above deals with it).
try:
    if any(_j.get("status") in ("queued", "uploading", "scheduling") and now - (t(_j.get("updated") or "") or now) < timedelta(hours=3)
           for _j in json.load(open("/workspace/glottos-auto/out/yt/jobs.json")).values()):
        if changed: json.dump(s, open(P, "w"), indent=2)
        sys.exit(1)
except Exception: pass
ch = s.get("channel", {})                                          # channel care first: quick, and users wait on it
if ch.get("reply_drafts_due") and not PAUSED:
    if changed: json.dump(s, open(P, "w"), indent=2)
    print("channel: reply_drafts"); sys.exit(0)
lm0 = t(ch.get("last_monitor") or "")
if not PAUSED and (lm0 is None or now - lm0 > timedelta(hours=24)):
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
    if n in HOLD_E: continue                                       # paused: no tick, no NLM gating
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
    if k in HOLD_S: continue
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
if not PAUSED and (lm is None or now - lm > timedelta(hours=24)):
    if changed: json.dump(s, open(P, "w"), indent=2)
    print("channel: monitor"); sys.exit(0)
if ch.get("reply_drafts_due") and not PAUSED:
    print("channel: reply_drafts"); sys.exit(0)
if changed: json.dump(s, open(P, "w"), indent=2)

# LAB — permanent hypothesis testing (user 2026-10-03: "test of hypotesis should be permanent, non stop process"). Runbook
# section "Lab". analyze every 12 h; produce whenever a hypothesis is "proposed" and fewer than max_unsent approved videos
# wait - NO cap since 2026-10-03 (see below). Stop: "paused": true.
try:
    LABF = "/workspace/glottos-auto/out/lab/lab.json"; lab = json.load(open(LABF))
except Exception: lab = None
if lab and not lab.get("paused"):
    bu = t(lab.get("blocked_until") or "")
    la, lp = t(lab.get("last_analyze") or ""), t(lab.get("last_produce") or "")
    try: nh = sum(1 for l in open("/workspace/glottos-auto/out/lab/hints.jsonl") if l.strip())
    except Exception: nh = 0
    na = 0   # tab "ahrefs traffic info": pictures go to NotebookLM by ahrefs_sync.py without Claude (user 2026-10-06, later the same day); an upload does NOT make an analyze due
    # DAILY VIDEO REVIEW (user 2026-10-17, verbatim: "You should have a table ... which an agent should fill each and every day on what is
    # going on and discuss with the loop of experts"): once per UTC day, after the day's Studio read, agent glottos-video-reviewer.
    try: _vn = json.load(open("/workspace/glottos-auto/out/lab/video-review-notes.json"))
    except Exception: _vn = {}
    _lr = t(_vn.get("last_review") or ""); _vb = t(_vn.get("blocked_until") or "")
    if ((_lr is None or _lr.date() < now.date()) and now.hour >= 6 or _vn.get("apply_due")) and not (_vb and _vb > now):
        print("lab: video_review"); sys.exit(0)
    if la is None or now - la > timedelta(hours=12) or nh > lab.get("hints_read", 0) or na or not any(h.get("status") == "proposed" for h in lab.get("hypotheses", [])):      # a new hint from the user = analyse now
        print("lab: analyze"); sys.exit(0)
    try:
        st = json.load(open("/workspace/glottos-auto/out/yt/status.json")); live = lambda v: v["youtube"] and v["youtube"]["state"] != "deleted"
        unsent = sum(1 for v in st["videos"] if not live(v) and v["meta"] and v["meta"]["approved"]
                     and not any(x["vid"] == v["vid"] + "-hd1440" and live(x) for x in st["videos"]))
    except Exception: unsent = 0
    todo = any(h.get("status") == "proposed" for h in lab.get("hypotheses", []))
    # user 2026-10-17: "make 10 shorts for the moment and then stop" -> lab.json "produce_only": [ids]: produce ONLY those (kept "proposed"/
    # "producing" until their batch_target is made); when none of them is left to make, production pauses again by itself.
    _po = lab.get("produce_only")
    if _po:
        todo = any(h.get("id") in _po and h.get("status") in ("proposed", "producing") for h in lab.get("hypotheses", []))
        if not todo and not lab.get("produce_paused"):
            lab["produce_paused"] = True; lab.pop("produce_only", None)
            lab["produce_paused_note"] = f"{now:%Y-%m-%dT%H:%MZ} paused again by due.py: the ordered batch ({', '.join(_po)}) is made. | " + (lab.get("produce_paused_note") or "")
            json.dump(lab, open(LABF + ".tmp", "w"), indent=1, ensure_ascii=False); os.replace(LABF + ".tmp", LABF)
    # user 2026-10-03: "there should be no cap! we should test as much as we possibly can till the moment we find the right format
    # for the right audience!" -> no limit on waiting videos and no pause between production steps; only a NotebookLM rate limit waits.
    # user 2026-10-04: "after the current videos which you have in production are done, you can pause production till I tell
    # you to continue" -> lab.json "produce_paused": true stops NEW video production only; analysis of results (analyze, every
    # 12 h / on a hint), packaging changes, sending, the schedule keeper and channel care keep running. Resume = set it to false.
    # PRODUCTION QUOTA (user 2026-10-23, verbatim: "you should produce not more than 2 shorts and 1 long video per day and each of those
    # three should be produced only per session of 5 hours window. meaning 1 short in on window, 2nd in second window and so on. It does
    # not prevent you though to launch nlm activities of generating pictures for videos and so on.") -> ONE video per produce tick, at
    # least 5 h after the previous one, at most 2 Shorts + 1 long per UTC day. Ledger out/lab/production-quota.json "made": due.py adds
    # the slot when it starts the tick, the tick fills vid (or failed:true -> not counted for the day, the 5 h still apply).
    QF = "/workspace/glottos-auto/out/lab/production-quota.json"
    try: pq = json.load(open(QF))
    except Exception: pq = {"made": []}
    made = [m for m in pq.get("made", []) if t(m.get("at") or "")]
    last = max((t(m["at"]) for m in made), default=None)
    day = [m for m in made if t(m["at"]).date() == now.date() and not m.get("failed")]
    cap = {"short": 2, "long": 1}
    # USER EXCEPTIONS (user 2026-10-25: "make exceptionaly another long video in glottos"): production-quota.json "extra":
    # [{"date": "YYYY-MM-DD", "kind": "long", "by": "user ...", "used": null}] = one more video of that kind on that UTC day, and that
    # one video may skip the 5 h gap. Only the user adds these; due.py marks the entry used when it hands out the slot.
    # an extra counts for its UTC "date", or - when it has "until" (ISO UTC) - for the current UTC day while until is ahead
    # (a batch ordered at 17Z may run past midnight). A used "until" extra counts for the day it was used on.
    live = lambda e: e.get("date") == now.strftime("%Y-%m-%d") or (e.get("until") and t(e["until"]) and t(e["until"]) > now and not e.get("used")) \
        or (e.get("until") and e.get("used") and e["used"][:10] == now.strftime("%Y-%m-%d"))
    extra = [e for e in pq.get("extra", []) if live(e) and not e.get("used")]
    for e in pq.get("extra", []):
        if live(e) and e.get("kind") in cap: cap[e["kind"]] += 1
    left = {k: c - sum(1 for m in day if m.get("kind") == k) for k, c in cap.items()}
    kind = lambda h: "long" if str(h.get("format") or "").lower().startswith("long") else "edit" if "no production" in str(h.get("format") or "").lower() else "short"
    cand = [h for h in lab.get("hypotheses", []) if h.get("status") in (("proposed", "producing") if _po else ("proposed",)) and (not _po or h.get("id") in _po)]
    order = {x: i for i, x in enumerate(_po or lab.get("produce_order") or [])}
    # STOCK FIRST (user 2026-10-25, verbatim: "agent should take care what needs to be produced first long or short video dependenly on
    # in which type we a running out of stock"): runway = hours until the LAST scheduled video of that kind goes public (keeper plan
    # out/yt/schedule-plan.json, hourly; videos still in the send queue count as one more slot), in slots of the policy gap. The kind with
    # the shorter runway goes first; inside a kind the produce_only / produce_order stays.
    def _runway():
        try: plan = json.load(open("/workspace/glottos-auto/out/yt/schedule-plan.json")).get("plan", [])
        except Exception: plan = []
        try: pol = json.load(open("/workspace/glottos-auto/out/lab/schedule-policy.json"))
        except Exception: pol = {}
        gap = {"short": float(pol.get("short_gap_hours") or 12), "long": float(pol.get("long_gap_hours") or 24)}
        r = {}
        for k in gap:
            ends = [t(x["now_at"]) for x in plan if x.get("kind") == k and x.get("now_at") and t(x["now_at"])]
            hrs = max([(e - now).total_seconds() / 3600 for e in ends] + [0])
            r[k] = hrs / gap[k]
        try:
            jobs = json.load(open("/workspace/glottos-auto/out/yt/jobs.json"))
            for j in (jobs.values() if isinstance(jobs, dict) else jobs):
                if j.get("status") in ("queued", "uploading", "scheduling"):
                    k = "long" if "long" in str(j.get("kind") or j.get("vid") or "").lower() else "short"
                    r[k] = r.get(k, 0) + 1
        except Exception: pass
        return r
    runway = _runway()
    cand.sort(key=lambda h: (runway.get(kind(h), 0) if kind(h) != "edit" else -1, order.get(h.get("id"), 999)))
    gap_ok = last is None or now - last >= timedelta(hours=5)
    # USER OVERRIDE (user 2026-10-25, verbatim: "follow the results of the analysis and produce videos accordignly, you can
    # exceptionally skip the rules of quantity of videos per window with automatic resume when tokens are back"):
    # production-quota.json "override": {"until": ISO, "by": ...} -> no 5 h gap, no daily caps; still ONE video per tick, only the
    # analysis' produce_only hypotheses, stock-first order, every gate. Claude limit -> the loop waits for the reset and resumes.
    ov = pq.get("override") or {}
    if ov.get("until") and t(ov["until"]) and t(ov["until"]) > now:
        gap_ok = True; left = {k: 99 for k in left}
    xk = {e.get("kind") for e in extra}
    pick = next((h for h in cand if kind(h) == "edit" or ((gap_ok or kind(h) in xk) and left[kind(h)] > 0)), None)
    if todo and pick and not lab.get("produce_paused") and not (bu and bu > now):
        k = kind(pick)
        if k != "edit":
            pq.setdefault("made", []).append({"at": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "kind": k, "hyp": pick["id"], "vid": None})
            ex = next((e for e in extra if e.get("kind") == k), None)
            if ex and (not gap_ok or sum(1 for m in day if m.get("kind") == k) >= cap[k] - 1):
                ex["used"] = now.strftime("%Y-%m-%dT%H:%M:%SZ"); pq["made"][-1]["note"] = "user exception: " + str(ex.get("by") or "")
            json.dump(pq, open(QF + ".tmp", "w"), indent=1); os.replace(QF + ".tmp", QF)
        print("lab: produce ONE %s of %s" % (k, pick.get("id"))); sys.exit(0)
sys.exit(1)
