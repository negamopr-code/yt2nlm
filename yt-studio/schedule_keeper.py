#!/usr/bin/env python3
"""Schedule keeper — the permanent watchdog over the publishing schedule (user 2026-10-03: "you need to make sure at every
given point of time that schedule is respected with 6 hours interval for shorts (next one should go live 6 hours later after
the latest video published) and that all further videos are scheduled with this interval, and for long videos 24 hours. But
when videos are deleted or modified this order can be disturbed and therefore you need to have watchdog permanently
looking to it").

  python /opt/yt/schedule_keeper.py [--dry-run]     -> KEEPER: {json} + REPORT: {json} (keeper.sh stores the report for :8093)

Truth = YouTube Studio, not our ledger: lists every video (stats.videos), opens each SCHEDULED one and reads its date +
time back, then builds the plan per kind (Shorts 6 h, long videos 24 h), keeping the current order:
  first slot  = latest published video of that kind + interval (not before now + 1 h, whole hour). A first video that
                already sits at or after that point, less than one interval later, is left alone.
  next slots  = previous slot + interval, exactly (so a deleted or moved video closes / opens the row behind it).
A video going live within 45 min is never touched. Changes are made with schedule.py <id> <explicit UTC time> (read back
there). Afterwards the ledger's "last"/"last_long" = the end of each row, so the next "Send to YouTube" lands right after.
Run only while holding glottos-autopilot/tick.lock. Never publishes now, never unschedules, never deletes."""
import json, subprocess, sys, time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from playwright.sync_api import sync_playwright
sys.path.insert(0, "/opt/yt")
from stats import videos, CH
from schedule import read_back, LEDGER, chain

DRY = "--dry-run" in sys.argv
def _policy():                                                # out/lab/schedule-policy.json: Marcus-driven cadence (user 2026-10-03); /videos = glottos-auto/out
    try: return json.load(open("/videos/lab/schedule-policy.json"))
    except Exception: return {}
_P = _policy()
GAP = {"short": timedelta(hours=float(_P.get("short_gap_hours", 6))), "long": timedelta(hours=float(_P.get("long_gap_hours", 24)))}
SOON = timedelta(minutes=45); UTC = timezone.utc
# PINS (user 2026-10-09: "every time that long video is launched to piggyback the shorts success"): a door Short belongs to the day of its long
# video, not to the next free place in the row. schedule-policy.json "pins": {"<youtube id>": "2026-10-14T16:00:00+00:00"} holds a video at that
# time; it is taken OUT of its row (the row closes behind it) and "next free" ignores it. A pin in the past is ignored.
def _pins():
    out = {}
    for k, v in (_P.get("pins") or {}).items():
        try: out[k] = datetime.fromisoformat(v).astimezone(timezone.utc)
        except Exception: pass
    return out
PINS = _pins()
iso = lambda t: t.strftime("%Y-%m-%dT%H:%M:%S+00:00")
def ceil_hour(t): return (t + timedelta(minutes=59, seconds=59)).replace(minute=0, second=0, microsecond=0)
def day(s):
    try: return datetime.strptime(s.strip(), "%b %d, %Y").replace(tzinfo=UTC)
    except Exception: return None

def main():
    now = datetime.now(UTC); c = chain()
    led = {}
    for it in c["items"]: led[it["id"]] = datetime.fromisoformat(it["at"])           # last entry per id wins
    with sync_playwright() as p:
        pg = p.chromium.connect_over_cdp("http://127.0.0.1:9222").contexts[0].new_page(); pg.set_default_timeout(30000)
        try:
            pg.goto(f"https://studio.youtube.com/channel/{CH}"); time.sleep(4)
            if "accounts.google.com" in pg.url: sys.exit("NOT SIGNED IN")
            vs = [dict(v, kind="short") for v in videos(pg, "short")] + [dict(v, kind="long") for v in videos(pg, "upload")]
            vs = [v for v in vs if v["id"]]
            for v in vs:
                if v["visibility"] != "Scheduled": continue
                pg.goto(f"https://studio.youtube.com/video/{v['id']}/edit"); pg.wait_for_load_state("domcontentloaded"); time.sleep(7)
                d, tm = read_back(pg)
                try: v["at"] = datetime.strptime(f"{d} {tm.upper()}", "%b %d, %Y %I:%M %p").replace(tzinfo=UTC)
                except Exception: v["at"] = None; v["unread"] = f"{d!r} {tm!r}"
        finally:
            pg.close()
    unread = [v["id"] for v in vs if v["visibility"] == "Scheduled" and not v.get("at")]
    if unread: sys.exit(f"KEEPER STOPPED: could not read the schedule of {unread} — nothing changed")
    plan, ends = [], {}
    for kind, gap in GAP.items():
        pub = [v for v in vs if v["kind"] == kind and v["visibility"] == "Public"]
        known = [led[v["id"]] for v in pub if v["id"] in led and led[v["id"]] <= now]
        days = [d for d in (day(v["date"]) for v in pub) if d and d <= now]
        anchor = max(known + ([max(days)] if days else [])) if (known or days) else None    # ledger time, else the publish day
        earliest = ceil_hour(now + timedelta(hours=1))
        t = max(anchor + gap, earliest) if anchor else earliest
        pinned = [v for v in vs if v["kind"] == kind and v["visibility"] == "Scheduled" and v["id"] in PINS and PINS[v["id"]] - now >= SOON]
        row = sorted((v for v in vs if v["kind"] == kind and v["visibility"] == "Scheduled" and v not in pinned), key=lambda v: v["at"])
        for v in pinned:
            cur = v["at"]; want = cur if cur - now < SOON else PINS[v["id"]]
            plan.append({"id": v["id"], "kind": kind, "title": v["title"], "now_at": iso(cur), "want": iso(want), "move": want != cur, "pinned": True})
        for n, v in enumerate(row):
            cur = v["at"]
            if cur - now < SOON: want = cur                                           # about to go live: hands off
            elif n == 0 and t <= cur < t + gap: want = cur                            # first in the row, inside its window
            else: want = max(t, earliest)
            plan.append({"id": v["id"], "kind": kind, "title": v["title"], "now_at": iso(cur), "want": iso(want), "move": want != cur})
            t = want + gap
        ends[kind] = (t - gap) if row else (anchor or now - gap)
        plan.append({"kind": kind, "anchor": iso(anchor) if anchor else None, "row": len(row), "next_free": iso(max(ends[kind] + gap, earliest))})
    moves = [x for x in plan if x.get("move")]; done = []
    if not DRY:
        for x in moves:
            r = subprocess.run([sys.executable, "/opt/yt/schedule.py", x["id"], x["want"][:16]], capture_output=True, text=True, timeout=600)
            x["ok"] = "SCHEDULED:" in r.stdout; x["out"] = (r.stdout + r.stderr).strip()[-200:]; done.append(x)
        c = chain()                                                                  # ledger follows Studio: exact times + row ends
        cur_at = {x["id"]: x["want"] if x.get("ok") else x["now_at"] for x in plan if x.get("id")}
        ids = {v["id"] for v in vs}
        c["items"] = [it for it in c["items"] if it["id"] in ids and it["id"] not in cur_at] + \
                     [{"id": i, "at": a, "by": "schedule_keeper.py", "kind": next(x["kind"] for x in plan if x.get("id") == i)} for i, a in cur_at.items()]
        c["last"] = iso(ends["short"]); c["last_long"] = iso(ends["long"])
        LEDGER.write_text(json.dumps(c, indent=2))
    rep = {"at": iso(now), "dry_run": DRY, "scheduled": sum(1 for x in plan if x.get("id")), "moves": len(moves),
           "failed": [x["id"] for x in done if not x["ok"]], "plan": plan}
    print("REPORT:", json.dumps(rep, ensure_ascii=False))                           # /videos is read-only here: keeper.sh stores it as glottos-auto/out/yt/schedule-plan.json
    print("KEEPER:", json.dumps({k: rep[k] for k in ("scheduled", "moves", "failed", "dry_run")}),
          "; ".join(f"{x['id']} {x['now_at'][5:16]} -> {x['want'][5:16]}" for x in moves))
    sys.exit(1 if rep["failed"] else 0)

if __name__ == "__main__": main()
