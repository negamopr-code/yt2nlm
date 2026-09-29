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

# ---- account pool (user 2026-09-29: "you do not fully use all nlm accounts for video and pictures generation ... you are
# using 2 from 4, and wait for rate limits, but there are other which are not solicitated"). A rate limit on one account
# no longer means "wait 2 h": the job's sources are copied to the next free account's Glottos notebook and the same
# generation starts there. Limits are tracked per account AND per kind (video/audio/infographic quotas are separate).
A = "/workspace/glottos-marketing/state/nlm-accounts.json"
ACC_DEFAULT = {"pool": ["drawnformula", "work2", "work4", "default"],
               "notebooks": {"drawnformula": "8306c0a9-1418-41e2-a988-1c0459eafc89",   # Glottos — go-to-market
                             "work2": "968fad6b-b3b8-4b37-8d11-4d3ff8664330",          # Glottos — Production (work2)
                             "work4": "9b6f4036-2b0d-4be4-905c-4e3525c983c1",          # Glottos — Production (work4)
                             "default": "28470494-9583-4a5e-9aed-183c5e497658"},       # Glottos — Production (default)
               "limited": {}}

def acc_load():
    try: a = json.load(open(A))
    except Exception: a = {}
    for k, v in ACC_DEFAULT.items(): a.setdefault(k, v)
    return a

def limited_until(acc, prof, kind):
    u = t(acc["limited"].get(prof, {}).get(kind, ""))
    return u if u and u > now else None

def source_ids(job):
    m = re.search(r"--source-ids[ =]+[\"']?([\w,-]+)", job["create_cmd"])
    return m.group(1).split(",") if m else None

def list_sources(prof, nb):
    rc, out = sh(f"{NLM} source list {nb} --json --profile {prof}", prof, 120)
    try: return {x["id"] for x in json.loads(out[out.index("["):]) if x.get("id")}
    except Exception: return None

def migrate(name, job, acc, to):
    """Copy the job's sources to account `to` and rewrite create_cmd for it. Returns True when ready."""
    sids = source_ids(job); nb = acc["notebooks"].get(to)
    if not sids or not nb:
        print(f"{name}: can't move to {to} (no --source-ids in create_cmd or no notebook)"); return False
    new_ids = []
    for sid in sids:
        tmp = f"/tmp/nlmsrc-{sid[:8]}.txt"
        rc, out = sh(f"{NLM} source content {sid} -o {tmp} --profile {job['profile']}", job["profile"], 180)
        if rc != 0: print(f"{name}: read source {sid[:8]} on {job['profile']} failed: {out.strip()[-160:]}"); return False
        before = list_sources(to, nb)
        rc, out = sh(f"{NLM} source add {nb} --file {tmp} --title 'autopilot copy {sid[:8]} ({name})' --wait --profile {to}", to, 700)
        after = list_sources(to, nb) or set()
        added = list(after - (before or set()))
        if rc != 0 or len(added) != 1:
            print(f"{name}: copy source {sid[:8]} -> {to} failed rc={rc}: {out.strip()[-160:]}"); return False
        new_ids.append(added[0]); job.setdefault("copied", []).append({"profile": to, "notebook": nb, "source": added[0]})
    cmd = job["create_cmd"]; job.setdefault("origin", {"profile": job["profile"], "notebook": job["notebook"], "create_cmd": cmd})
    for old, new in zip(sids, new_ids): cmd = cmd.replace(old, new)
    cmd = cmd.replace(job["notebook"], nb)
    cmd = re.sub(r"NLM_PROFILE=\S+", f"NLM_PROFILE={to}", cmd)
    cmd = re.sub(r"(--profile|-p)([ =])\S+", rf"\g<1>\g<2>{to}", cmd)
    job.update(create_cmd=cmd, profile=to, notebook=nb)
    print(f"{name}: moved {job['kind']} job to {to} (sources copied: {', '.join(i[:8] for i in new_ids)})"); return True

def cleanup(job):
    for c in job.get("copied", []):
        sh(f"{NLM} source delete {c['source']} --confirm --profile {c['profile']}", c["profile"], 120)

def main():
    s = json.load(open(P)); changed = False; acc = acc_load()
    items = [(f"episode {k}", e) for k, e in s["episodes"].items()] + [(f"special {k}", e) for k, e in s.get("specials", {}).items()]
    for name, e in items:
        job = e.get("nlm_job")
        if not job: continue
        b = t(e.get("blocked_until") or "")
        if not job.get("artifact_id"):
            if b and b > now: continue
            kind = job["kind"]
            order = [job["profile"]] + [p for p in acc["pool"] if p != job["profile"]]
            free = [p for p in order if not limited_until(acc, p, kind)]
            if not free:
                e["blocked_until"] = iso(min(limited_until(acc, p, kind) for p in order))
                print(f"{name}: nlm {kind} limited on ALL accounts ({', '.join(order)}) -> retry {e['blocked_until']} (no Claude)")
                changed = True; continue
            for prof in free:
                if prof != job["profile"] and not migrate(name, job, acc, prof): continue
                before = status(job)
                if before is None: print(f"{name}: nlm status unreadable on {prof} (auth?) - next account"); continue
                rc, out = sh(job["create_cmd"], job["profile"])
                after = status(job) or {}
                new = [i for i, a in after.items() if i not in before and a.get("type", kind).startswith(kind[:5])]
                if new:
                    job["artifact_id"] = new[0]; job["started_at"] = iso(now); e.pop("blocked_until", None)
                    print(f"{name}: nlm {kind} started {new[0]} ({prof})"); break
                if LIMIT.search(out):
                    acc["limited"].setdefault(prof, {})[kind] = iso(now + timedelta(hours=2))
                    job["limited_count"] = job.get("limited_count", 0) + 1
                    print(f"{name}: nlm {kind} rate-limited on {prof} -> trying the next account"); continue
                e["nlm_error"] = f"{iso(now)} create failed on {prof} rc={rc}: {out.strip()[-400:]}"; cleanup(job); e.pop("nlm_job")
                print(f"{name}: nlm create FAILED on {prof} -> back to Claude"); break
            else:
                ls = [limited_until(acc, p, kind) for p in order if limited_until(acc, p, kind)]
                e["blocked_until"] = iso(min(ls) if ls else now + timedelta(minutes=30))
                print(f"{name}: nlm {kind} not started on any account -> retry {e['blocked_until']} (no Claude)")
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
            e["nlm_done"] = done; cleanup(job); e.pop("nlm_job")
            e["note"] = f"{iso(now)} nlm_jobs.py: {job['kind']} downloaded -> {job['out']} (no Claude). Continue the step from this file. | " + str(e.get("note", ""))[:600]
            print(f"{name}: nlm {job['kind']} downloaded -> {job['out']}"); changed = True
        elif state in ("failed", "error", "missing") or now - started > timedelta(minutes=90):
            e["nlm_error"] = f"{iso(now)} artifact {job['artifact_id']} status={state} after {int((now-started).total_seconds()//60)} min"
            cleanup(job); e.pop("nlm_job"); changed = True
            print(f"{name}: nlm artifact {state} -> back to Claude")
    if changed:
        json.dump(s, open(P, "w"), indent=2)
        json.dump(acc, open(A, "w"), indent=2)

if __name__ == "__main__": main()
