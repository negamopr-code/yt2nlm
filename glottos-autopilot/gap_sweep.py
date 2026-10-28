#!/usr/bin/env python3
"""GAP SWEEP (user 2026-10-28, verbatim: "you need to identify such gaps yourself by looking what is missing").
Hourly, no Claude. Checks what SHOULD exist and doesn't - not only what failed. Every gap = one log line "gaps: ..." and
out/lab/gaps.json (read by sessions and by the analyze brief). Born from the gaps of 10-27/28 that nobody saw:
long row empty for a day, sent tests never judged, a made video never offered for Send, a send that lost its file,
analyze firing every minute, NLM accounts dead for hours."""
import json, os, re, subprocess, datetime as dt, glob
OUT = "/workspace/glottos-auto/out"; MK = "/workspace/glottos-marketing"; LOG = "/workspace/glottos-autopilot/log.txt"
now = dt.datetime.now(dt.timezone.utc)
def t(s):
    try: return dt.datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except Exception: return None
def j(p, d=None):
    try: return json.load(open(p))
    except Exception: return d
gaps = []
def gap(kind, msg): gaps.append({"kind": kind, "msg": msg})

# 1. stock: long row (user 2026-10-28: one long every day) and Shorts row
plan = (j(f"{OUT}/yt/schedule-plan.json", {}) or {}).get("plan", [])
pol = j(f"{OUT}/lab/schedule-policy.json", {}) or {}
for k, gap_h, need in (("long", float(pol.get("long_gap_hours") or 24), 2), ("short", float(pol.get("short_gap_hours") or 12), 4)):
    ends = [t(x["now_at"]) for x in plan if x.get("kind") == k and x.get("now_at") and t(x["now_at"])]
    slots = max([(e - now).total_seconds() / 3600 for e in ends] + [0]) / gap_h
    if slots < need: gap("stock", f"{k} row: only {slots:.1f} slots scheduled ahead (need >= {need})")

# 2. made but never offered: rendered mp4 in out/, not on YouTube, YouTube text not approved, older than 2 h
st = (j(f"{OUT}/yt/status.json", {}) or {}).get("videos", [])
live = lambda v: (v.get("youtube") or {}).get("state") not in (None, "deleted")
for v in st:
    if live(v) or v.get("archived") or not v.get("meta"): continue
    if not (v["meta"] or {}).get("approved") and now.timestamp() - (v.get("mtime") or now.timestamp()) > 7200:
        gap("unapproved", f"{v['vid']}: rendered but its YouTube text is not language-approved -> never offered for Send")

# 3. sends: failed jobs of the last 7 days; approved videos waiting > 24 h
jobs = j(f"{OUT}/yt/jobs.json", {}) or {}
for x in (jobs.values() if isinstance(jobs, dict) else jobs):
    u = t(x.get("updated"))
    if x.get("status") == "failed" and u and now - u < dt.timedelta(days=7):
        gap("send", f"{x['vid']}: send failed ({str(x.get('note'))[:90]})")
for v in st:
    if not live(v) and not v.get("archived") and (v.get("meta") or {}).get("approved") and not v.get("job") \
            and now.timestamp() - (v.get("mtime") or now.timestamp()) > 86400:
        gap("unsent", f"{v['vid']}: approved and waiting in Not sent yet for > 24 h")

# 4. lab: tests stuck, analyze/produce loops, verdicts
lab = j(f"{OUT}/lab/lab.json", {}) or {}
po = lab.get("produce_only") or []
for h in lab.get("hypotheses", []):
    if h.get("status") == "producing" and po and h["id"] not in po:
        gap("lab", f"{h['id']} is 'producing' but not in produce_only -> the scheduler will never make the rest")
    if h.get("resume_note") and h.get("status") in ("waiting_send", "live", "verdict", "closed"):
        gap("lab", f"{h['id']}: stale resume_note on a {h['status']} test (a later tick may redo work)")
try:
    lines = [l for l in open(LOG, errors="ignore").readlines()[-400:] if " tick: " in l and t(l[:20]) and now - t(l[:20]) < dt.timedelta(hours=1)]
    names = [l.split(" tick: ", 1)[1].strip() for l in lines]
    for n in set(names):
        if names.count(n) >= 4: gap("loop", f"'{n}' ran {names.count(n)} times in the last hour")
except Exception: pass
if lab.get("produce_paused") and po: gap("lab", "produce_paused is true while produce_only has work")

# 5. daily jobs that must have happened
vr = j(f"{OUT}/lab/video-review-notes.json", {}) or {}
lr = t(vr.get("last_review"))
if now.hour >= 9 and (lr is None or lr.date() < now.date()): gap("daily", f"video review not done today (last {vr.get('last_review')})")
la = t(lab.get("last_analyze"))
if la is None or now - la > dt.timedelta(hours=14): gap("daily", f"lab analyze older than 14 h ({lab.get('last_analyze')})")

# 6. NotebookLM accounts used by the expert consults / pictures (free login --check)
N = f"{MK}/.nlmvenv/bin/nlm"
for p in ("default", "work2", "drawnformula", "work4"):
    try:
        r = subprocess.run([N, "login", "--check", "--profile", p], capture_output=True, text=True, timeout=90)
        if "valid" not in (r.stdout + r.stderr): gap("nlm", f"NotebookLM profile '{p}' signed out")
    except Exception as e: gap("nlm", f"NotebookLM profile '{p}' check failed: {e}")

# 7. quota override about to end while its batch is unfinished
ov = (j(f"{OUT}/lab/production-quota.json", {}) or {}).get("override") or {}
ou = t(ov.get("until"))
if ou and now < ou < now + dt.timedelta(hours=2) and po: gap("quota", f"override ends {ov['until']} with produce_only still {po[:5]}")

prev = {g["msg"] for g in (j(f"{OUT}/lab/gaps.json", {}) or {}).get("gaps", [])}
json.dump({"at": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "gaps": gaps}, open(f"{OUT}/lab/gaps.json.tmp", "w"), indent=1)
os.replace(f"{OUT}/lab/gaps.json.tmp", f"{OUT}/lab/gaps.json")
for g in gaps: print(("NEW " if g["msg"] not in prev else "") + f"[{g['kind']}] {g['msg']}")
if not gaps: print("no gaps")
