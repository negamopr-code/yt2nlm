#!/usr/bin/env python3
"""Send controller WITHOUT Claude (user 2026-10-05: "you need to have an agent which is controlling that everything goes right when
buttone 'send to youtube' is pushed"). Runs every loop pass (loop.sh) and after it the :8093 Videos tab shows a red banner if
something is wrong. It checks the whole path click -> queue -> 1440 master -> upload -> schedule -> thumbnail -> channel:
  1. the queue process (yt_sendq.py) is alive: yt/status.json refreshed in the last 5 min; if not, it is started again
  2. no job hangs: "uploading" > 60 min (> 4 h while it makes a 1440 master), "scheduling" > 15 min, "queued" > 3 h with nothing running
     -> repaired where the truth is known: video already in the schedule chain = done; uploaded but not scheduled = schedule.py now
  3. the queue log has no new "yt_sendq error" lines
  4. every job finished in the last 72 h really is on the channel as Scheduled/Public (channel snapshot), and went up at >= 1440.
     "Not on the channel" needs two complete snapshots in a row (channel_truth.py); a half-read snapshot is reported as
     "cannot read the channel", never as missing videos
  5. failed jobs of the last 72 h are listed until the user sends them again
Report: glottos-auto/out/yt/send-watch.json {at, ok, problems[], repaired[]}. When a problem stays for 2 runs and cannot be repaired
here, `needs_agent` is set: due.py then gives ONE Claude tick to the agent glottos-send-controller (diagnose + fix the code).
Call under tick.lock only for repairs that use the browser (this script takes the lock itself, non-blocking)."""
import fcntl, json, os, re, subprocess, sys, time
from datetime import datetime, timezone, timedelta
D = "/workspace/glottos-autopilot"; OUT = "/workspace/glottos-auto/out"; Y = f"{OUT}/yt"
JOBS, STATUS, REPORT, LOG, SNAP = f"{Y}/jobs.json", f"{Y}/status.json", f"{Y}/send-watch.json", f"{D}/yt_sendq.log", f"{OUT}/analytics/latest.json"
RULE_1440_FROM = "2026-10-05T08:00:00Z"
now = datetime.now(timezone.utc); iso = lambda d: d.strftime("%Y-%m-%dT%H:%M:%SZ")
def t(s):
    try: return datetime.fromisoformat((s or "").replace("Z", "+00:00")).astimezone(timezone.utc) if "+" in (s or "") or (s or "").endswith("Z") else datetime.fromisoformat(s).replace(tzinfo=timezone.utc)
    except Exception: return None
def jload(p, d):
    try: return json.load(open(p))
    except Exception: return d
def jsave(p, o): json.dump(o, open(p + ".tmp", "w"), indent=1, ensure_ascii=False); os.replace(p + ".tmp", p)
def yt(path, d):
    try: return json.loads(subprocess.run(["docker", "exec", "yt-studio", "cat", path], capture_output=True, text=True, timeout=60).stdout)
    except Exception: return d
yid = lambda l: (re.search(r"(?:youtu\.be/|/shorts/|[?&]v=|/video/)([A-Za-z0-9_-]{11})", l or "") or [None, None])[1]
age = lambda s: (now - t(s)).total_seconds() / 60 if t(s) else 1e9
prev = jload(REPORT, {}); problems, repaired = [], []
# 1. queue process alive
st = jload(STATUS, {})
# alive = the process exists. (Its status.json can be minutes old while it waits for tick.lock behind a Claude tick - that is normal.)
running = subprocess.run(["pgrep", "-f", "yt_sendq.py"], capture_output=True, text=True).stdout.strip()
if not running:
    subprocess.Popen(f"python3 -W ignore {D}/yt_sendq.py >> {LOG} 2>&1", shell=True, start_new_session=True)
    repaired.append("send queue process was not running - started it again")
elif age(st.get("at")) > 240 and min([int(x) for x in subprocess.run(["ps", "-o", "etimes=", "-p", ",".join(running.split())], capture_output=True, text=True).stdout.split()] or [1e9]) > 300:
    # (2026-10-11: after a night with the machine off the first pass ran 6 s after start, before the queue wrote its first status -
    #  "not refreshed for 10.9 h" was the downtime. A queue process younger than 5 min gets the time to write it.)
    problems.append(f"send queue is running but its status has not refreshed for {round(age(st.get('at')) / 60, 1)} h")
jobs = jload(JOBS, {}); chain = None; ledger = None; changed = False
active = [j for j in jobs.values() if j["status"] in ("uploading", "scheduling")]
def schedule_now(j, i):
    kind = next((v["kind"] for v in st.get("videos", []) if v["vid"] == j["vid"]), "short")
    with open(f"{D}/tick.lock", "a") as lk:
        held_by_loop = False
        try: held_by_loop = os.path.realpath("/proc/self/fd/9") == f"{D}/tick.lock"   # called from loop.sh: the pass already holds the lock on fd 9
        except OSError: pass
        if not held_by_loop:
            try: fcntl.flock(lk, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError: return None                                        # browser busy: next pass
        o = subprocess.run(["docker", "exec", "-u", "app", "yt-studio", "/home/app/yt-profile/.venv/bin/python", "/opt/yt/schedule.py", i, "next-long" if kind == "long" else "next"],
                           capture_output=True, text=True, timeout=600)
    m = re.search(r"^SCHEDULED: (\{.*\})$", o.stdout + o.stderr, re.M)
    return "scheduled " + " ".join(json.loads(m[1])["want"]) if m else False
# 2026-10-18: [u]/[p] brackets - the old pattern matched this check's own sh -c line, so busy was ALWAYS true and 2a/2b never ran
# 2a. a job left at "uploading" by a restart: nothing is encoding or uploading, and there is no upload on record -> back into the queue (once)
busy = subprocess.run("pgrep -f 'yt-studio.*[u]pload.py|\\.hd/.*[p]art.mp4' >/dev/null || docker exec yt-studio pgrep -f '[u]pload.py' >/dev/null", shell=True).returncode == 0
if not busy:
    led0 = None
    for j in jobs.values():
        if j["status"] == "uploading" and age(j.get("updated")) > 5 and not j.get("youtube") and not j.get("requeued"):
            if led0 is None: led0 = yt("/home/app/yt-profile/uploads.json", {})
            if j["vid"] in led0: continue                                      # uploaded after all: handled below
            j.update(status="queued", requeued=iso(now), note="back in the queue (the send was interrupted before the upload)", updated=iso(now)); changed = True
            repaired.append(f"{j['vid']}: the send was interrupted before the upload - put back into the queue")
# 2b. leftover Studio tabs: a failed or interrupted upload leaves its tab open; five of them made signed_in.py time out on 2026-10-05
# and the loop then believed the browser was signed out (no snapshots for 30 min). Nothing is using the browser -> keep one tab.
if not busy and os.path.realpath("/proc/self/fd/9") == f"{D}/tick.lock":            # only inside a loop pass (we hold the browser lock)
    try:
        r = subprocess.run(["docker", "exec", "-u", "app", "yt-studio", "timeout", "40", "/home/app/yt-profile/.venv/bin/python", "-c",
            "import json,urllib.request as u\nt=[x for x in json.load(u.urlopen('http://127.0.0.1:9222/json',timeout=10)) if x.get('type')=='page']\n"
            "[u.urlopen('http://127.0.0.1:9222/json/close/'+x['id'],timeout=10).read() for x in t[1:]]\nprint(len(t)-1)"], capture_output=True, text=True, timeout=60)
        n = int((r.stdout.strip() or "0").splitlines()[-1])
        if n >= 2: repaired.append(f"closed {n} leftover YouTube Studio tabs")
    except Exception: pass
# 2. hanging jobs
for j in jobs.values():
    s, a = j["status"], age(j.get("updated")); limit = {"uploading": 240 if "1440 master" in (j.get("note") or "") else 60, "scheduling": 15}.get(s)
    if s == "queued" and a > 20 and not active: problems.append(f"{j['vid']}: waiting in the queue for {round(a)} min and nothing is being sent"); continue   # 2026-10-07: was 3 h - eight clicks waited an hour behind a Claude tick and this said nothing
    if not limit or a <= limit: continue
    if chain is None: chain = {i["id"]: i["at"] for i in yt("/home/app/yt-profile/schedule-chain.json", {}).get("items", [])}; ledger = yt("/home/app/yt-profile/uploads.json", {})
    i = yid(j.get("youtube")) or yid((ledger.get(j["vid"]) or {}).get("link"))
    if i and i in chain:
        j.update(status="done", youtube=j.get("youtube") or ledger[j["vid"]]["link"], note=f"scheduled {chain[i][:16].replace('T', ' ')} UTC (state repaired by the send controller)", updated=iso(now)); changed = True
        repaired.append(f"{j['vid']}: was stuck at '{s}', is in fact scheduled {chain[i][:16].replace('T', ' ')} UTC - marked done")
    elif i:
        r = schedule_now(j, i)
        if r: j.update(status="done", youtube=j.get("youtube") or ledger[j["vid"]]["link"], note=r + " (scheduled by the send controller)", updated=iso(now)); changed = True; repaired.append(f"{j['vid']}: uploaded but never scheduled - {r}")
        elif r is False: problems.append(f"{j['vid']}: uploaded ({i}) but scheduling fails - it sits in Studio as a private draft")
    else: problems.append(f"{j['vid']}: stuck at '{s}' for {round(a)} min and there is no upload on record")
# 2c. sends that failed because Docker / yt-studio was away, found after the restart (2026-10-11 22:39Z: the machine went down in the
# middle of 7 sends; user 2026-10-12: "make sure this doesn't happen again after a reboot"). Not uploaded -> back into the queue;
# uploaded but not scheduled -> scheduled here. At most 3 tries per job, then it stays "failed" and is reported as before.
# 2026-10-18: "_cdp: Timeout ... connect_over_cdp" = the yt-studio browser hung before any upload started (3 Shorts sat as failed)
INFRA = re.compile(r"Cannot connect to the Docker daemon|error during connect|No such container|is not running|is restarting|_cdp: Timeout|connect_over_cdp|TimeoutError: (Locator|Page)\.", re.I)   # 2026-10-28: a Studio page that did not load in 60 s (h112) = retry too
try: docker_ok = subprocess.run(["docker", "exec", "yt-studio", "true"], capture_output=True, timeout=30).returncode == 0
except Exception: docker_ok = False
for j in (jobs.values() if docker_ok else []):
    note = j.get("note") or ""
    if j["status"] != "failed" or age(j.get("updated")) > 72 * 60 or j.get("auto_retry", 0) >= 3: continue
    if "but scheduling failed" in note and yid(j.get("youtube")):
        if chain is None: chain = {i["id"]: i["at"] for i in yt("/home/app/yt-profile/schedule-chain.json", {}).get("items", [])}; ledger = yt("/home/app/yt-profile/uploads.json", {})
        i = yid(j["youtube"])
        if i in chain:
            j.update(status="done", note=f"scheduled {chain[i][:16].replace('T', ' ')} UTC (state repaired by the send controller)", updated=iso(now)); changed = True
            repaired.append(f"{j['vid']}: was 'failed', is in fact scheduled {chain[i][:16].replace('T', ' ')} UTC - marked done")
            continue
        r = schedule_now(j, i)
        if r: j.update(status="done", note=r + " (scheduled by the send controller after an interrupted send)", updated=iso(now)); changed = True; repaired.append(f"{j['vid']}: uploaded but not scheduled - {r}")
        elif r is False: j["auto_retry"] = j.get("auto_retry", 0) + 1; changed = True     # None = browser busy: next pass, not a try
    elif note.startswith("upload failed:") and INFRA.search(note):
        why = "the YouTube browser was hung" if re.search(r"_cdp|connect_over_cdp", note) else "Docker was down"
        j.update(status="queued", interrupted=True, auto_retry=j.get("auto_retry", 0) + 1, note=f"back in the queue ({why} when it was sent)", updated=iso(now)); changed = True
        repaired.append(f"{j['vid']}: the send failed because {why} - put back into the queue")
if changed: jsave(JOBS, jobs)
# 2c. hung browser (2026-10-18: Chrome answered /json/version but every Playwright connect_over_cdp timed out for 4 h - uploads, schedule
# keeper and snapshot all stalled, the snapshot even reported "NOT SIGNED IN"). Test a real connect; two hung passes in a row and nothing
# uploading -> restart yt-studio (the profile and its sign-in survive a container restart, verified 10-18).
if docker_ok and not busy:
    _hp = f"{D}/.cdp_hang"
    try:
        _r = subprocess.run(["docker", "exec", "-u", "app", "yt-studio", "timeout", "75", "/home/app/yt-profile/.venv/bin/python", "-c",
                             "from playwright.sync_api import sync_playwright\nwith sync_playwright() as p: p.chromium.connect_over_cdp('http://127.0.0.1:9222', timeout=60000); print('CDP_OK')"],
                            capture_output=True, text=True, timeout=100)
        _ok = "CDP_OK" in _r.stdout
    except Exception:
        _ok = False
    if _ok:
        if os.path.exists(_hp): os.remove(_hp)
    else:
        _n = int(open(_hp).read() or 0) + 1 if os.path.exists(_hp) else 1
        open(_hp, "w").write(str(_n))
        if _n >= 2:
            subprocess.run(["docker", "restart", "yt-studio"], capture_output=True, timeout=180); os.remove(_hp)
            repaired.append("the YouTube browser was hung (Playwright could not connect twice in a row) - restarted yt-studio")
        else:
            problems.append("the YouTube browser does not answer Playwright (1st time) - restarted automatically if it is still hung next pass")
# 3. errors in the queue log (last 60 min)
try: lines = open(LOG).read().splitlines()[-400:]
except Exception: lines = []
# only crashes of the code that is running NOW: a line older than the last change of yt_sendq.py (= already fixed and restarted) or
# older than 60 min is history, not a problem (user 2026-10-05 saw the banner "again crashed" for a crash fixed 20 min earlier)
code_at = datetime.fromtimestamp(os.path.getmtime(f"{D}/yt_sendq.py"), timezone.utc)
errs = [l for l in lines if " yt_sendq error:" in l and age(l[:20]) < 60 and t(l[:20]) and t(l[:20]) > code_at]
if errs: problems.append(f"send queue crashed {len(errs)}x in the last hour: {errs[-1][21:200]}")
# 4. + 5. finished and failed jobs of the last 72 h against the channel
# A video counts as missing only when channel_truth says so: absent in the last TWO complete snapshots. One read proves nothing
# (2026-10-05 16:11Z: the Shorts tab came back empty once and 16 scheduled Shorts were reported here as "not on the channel").
from channel_truth import Channel
ch = Channel(); snap = ch.latest; sv = ch.videos; vids = {v["vid"]: v for v in st.get("videos", [])}
if ch.unreadable(): problems.append(f"cannot read the channel: {ch.unreadable()} - sent videos are NOT checked until the next good snapshot (nothing is known to be missing)")
elif age(snap.get("at")) > 300 and jload(f"{OUT}/analytics/status.json", {}).get("signed_in") and time.time() - os.stat("/proc/1").st_ctime > 45 * 60:   # 2026-10-06: after a night with the computer off the first pass reported "the Studio read itself fails" 2 min before the first snapshot of the day
    problems.append(f"cannot read the channel: the last complete snapshot is {round(age(snap.get('at')) / 60, 1)} h old (signed in, so the Studio read itself fails)")
for j in jobs.values():
    if age(j.get("updated")) > 72 * 60: continue
    if j["status"] == "failed": problems.append(f"{j['vid']}: NOT sent - {(j.get('note') or '')[:160]}"); continue
    if j["status"] != "done": continue
    i = yid(j.get("youtube")); v = sv.get(i)
    if i and snap.get("at") and t(snap["at"]) and t(j.get("updated")) and t(snap["at"]) > t(j["updated"]) + timedelta(minutes=5):
        if not v:
            if ch.gone(i, j.get("updated")): problems.append(f"{j['vid']}: marked sent, but {i} is not on the channel in two reads in a row (deleted, or the upload did not finish)")
        elif v.get("visibility") not in ("Scheduled", "Public"): problems.append(f"{j['vid']}: on the channel as {v.get('visibility')}, not scheduled")
    f = vids.get(j["vid"])
    if f and min(f["w"], f["h"]) < 1440 and (j.get("clicked") or "") > RULE_1440_FROM and "->" not in (j.get("note") or "") and "1440" not in (j.get("note") or ""):
        problems.append(f"{j['vid']}: went up at {f['w']}x{f['h']}, under the 1440 rule")
same = sorted(problems) == sorted(prev.get("problems", []))
rep = {"at": iso(now), "ok": not problems, "problems": problems, "repaired": (prev.get("repaired", []) + [f"{iso(now)[:16]} {r}" for r in repaired])[-20:],
       "runs_with_same_problems": prev.get("runs_with_same_problems", 0) + 1 if (problems and same) else (1 if problems else 0)}
rep["needs_agent"] = bool(problems) and rep["runs_with_same_problems"] >= 2 and any(("crashed" in p or "stuck" in p or "scheduling fails" in p or "under the 1440 rule" in p or "not on the channel" in p or "cannot read the channel" in p) for p in problems)
rep["agent_done_for"] = prev.get("agent_done_for") if same else None
jsave(REPORT, rep)
if repaired or (problems and not same): print("; ".join([f"REPAIRED {r}" for r in repaired] + [f"PROBLEM {p}" for p in problems])[:600])
# Cleanup of sent videos (user 2026-10-18: "no videos should be stored in our local memory or container if we already have sent video
# to youtube"): hourly, detached, no Claude - cleanup_sent.py archives the status record, then deletes the local video/audio files.
_stamp = f"{D}/.last_cleanup"
if not os.path.exists(_stamp) or time.time() - os.path.getmtime(_stamp) > 3600:
    open(_stamp, "w").close()
    subprocess.Popen(f"python3 {D}/cleanup_sent.py --apply 2>&1 | tail -1 | grep -v \" 0 sent\" | sed \"s/^/$(date -u +%FT%TZ) /\" >> {D}/log.txt",
                     shell=True, start_new_session=True)
