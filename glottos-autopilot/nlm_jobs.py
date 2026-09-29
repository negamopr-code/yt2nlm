#!/usr/bin/env python3
"""NotebookLM waiting WITHOUT Claude (user 2026-09-29: "we need rather do them as cheap as possible from token
perspective"). Before this, a Claude tick started `nlm ... create`, launched a background poll, said "I'll wait" and
exited, which killed the poll; the next tick re-read the runbook and polled again (S5 nlm_video: 4+ ticks, ep02
visuals: one tick per rate-limit retry).

Contract with the Claude step (docs/autopilot.md "NotebookLM jobs"): instead of polling, the tick writes
  item["nlm_job"] = {"profile": "work2", "notebook": "<nb id>", "kind": "video|audio|infographic",
                     "create_cmd": "<full shell command that starts the generation, run from glottos-marketing>",
                     "out": "<path relative to glottos-marketing>", "artifact_id": "<id if already started, else null>"}
and ends the tick. This script, run by loop.sh on every pass (holding the tick lock):
  * no artifact_id and not blocked  -> runs create_cmd; a new artifact (studio status diff) = started;
                                       "rate limit"/quota/code 8 -> blocked_until = now + 2 h (retried here, no Claude)
  * artifact generating             -> nothing (checked again next pass); > 90 min -> failed
  * artifact completed              -> download to `out` (the Claude step checks duration/QA), item["nlm_done"] = {...},
                                       nlm_job removed -> due.py hands the step back to Claude to CONTINUE from the file
  * artifact failed / create error  -> nlm_job removed, item["nlm_error"] set -> Claude decides (due again)
due.py treats an item with nlm_job as "waiting" (not due). Prints one line per action for the loop log."""
import json, re, subprocess, time
from datetime import datetime, timezone, timedelta
P = "/workspace/glottos-marketing/state/autopilot.json"; W = "/workspace/glottos-marketing"
NLM = W + "/.nlmvenv/bin/nlm"
now = datetime.now(timezone.utc); iso = lambda d: d.strftime("%Y-%m-%dT%H:%M:%SZ")
LIMIT = re.compile(r"rate.?limit|quota|try again later|code 8|RESOURCE_EXHAUSTED|too many", re.I)

def t(s):
    try: return datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except Exception: return None

def sh(cmd, prof, timeout=600):
    r = subprocess.run(cmd, shell=True, cwd=W, capture_output=True, text=True, timeout=timeout,
                       env={"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": "/home/node", "NLM_PROFILE": prof})
    return r.returncode, (r.stdout or "") + (r.stderr or "")

def status(job):
    rc, out = sh(f"{NLM} studio status {job['notebook']} --json --profile {job['profile']}", job["profile"], 120)
    try: return {a["id"]: a for a in json.loads(out[out.index("["):])}
    except Exception: return None

def main():
    s = json.load(open(P)); changed = False
    items = [(f"episode {k}", e) for k, e in s["episodes"].items()] + [(f"special {k}", e) for k, e in s.get("specials", {}).items()]
    for name, e in items:
        job = e.get("nlm_job")
        if not job: continue
        b = t(e.get("blocked_until") or "")
        if not job.get("artifact_id"):
            if b and b > now: continue
            before = status(job)
            if before is None: print(f"{name}: nlm status unreadable (auth?) - leaving job"); continue
            rc, out = sh(job["create_cmd"], job["profile"])
            after = status(job) or {}
            new = [i for i, a in after.items() if i not in before and a.get("type", job["kind"]).startswith(job["kind"][:5])]
            if new:
                job["artifact_id"] = new[0]; job["started_at"] = iso(now); e.pop("blocked_until", None)
                print(f"{name}: nlm {job['kind']} started {new[0]} ({job['profile']})")
            elif LIMIT.search(out):
                e["blocked_until"] = iso(now + timedelta(hours=2)); job["limited_count"] = job.get("limited_count", 0) + 1
                print(f"{name}: nlm {job['kind']} rate-limited on {job['profile']} -> retry {e['blocked_until']} (no Claude)")
            else:
                e["nlm_error"] = f"{iso(now)} create failed rc={rc}: {out.strip()[-400:]}"; e.pop("nlm_job")
                print(f"{name}: nlm create FAILED -> back to Claude")
            changed = True; continue
        st = status(job)
        if st is None: continue
        a = st.get(job["artifact_id"])
        state = (a or {}).get("status", "missing")
        started = t(job.get("started_at") or "") or now
        if state == "completed":
            rc, out = sh(f"{NLM} download {job['kind']} {job['notebook']} --id {job['artifact_id']} -o {job['out']} --no-progress",
                         job["profile"], 900)
            if rc != 0:
                print(f"{name}: download failed rc={rc}, retry next pass: {out.strip()[-200:]}"); continue
            done = {"out": job["out"], "artifact_id": job["artifact_id"], "profile": job["profile"], "at": iso(now)}
            e["nlm_done"] = done; e.pop("nlm_job")
            e["note"] = f"{iso(now)} nlm_jobs.py: {job['kind']} downloaded -> {job['out']} (no Claude). Continue the step from this file. | " + str(e.get("note", ""))[:600]
            print(f"{name}: nlm {job['kind']} downloaded -> {job['out']}"); changed = True
        elif state in ("failed", "error", "missing") or now - started > timedelta(minutes=90):
            e["nlm_error"] = f"{iso(now)} artifact {job['artifact_id']} status={state} after {int((now-started).total_seconds()//60)} min"
            e.pop("nlm_job"); changed = True
            print(f"{name}: nlm artifact {state} -> back to Claude")
    if changed: json.dump(s, open(P, "w"), indent=2)

if __name__ == "__main__": main()
