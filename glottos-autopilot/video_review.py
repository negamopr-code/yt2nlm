#!/usr/bin/env python3
"""Daily video review table WITHOUT Claude (user 2026-10-17, verbatim: "Do this exercise for all videos on the channel which were
uploaded starting 28/09/2026. You should have a table (probably you have it) which an agent should fill each and every day on what
is going on and discuss with the loop of experts").
Every loop pass: one row per public video published on/after SINCE, from the channel snapshot (analytics/latest.json), the per-video
Studio numbers (analytics/deep.json), the hypothesis ledger (lab/lab.json) and the thumbnail-test ledger (abtests/catalog/tests.json).
  - history: lab/video-review-history.jsonl gets ONE line per video per UTC day (views, impressions, CTR, stayed) -> day-by-day trend
  - symptom: a mechanical first diagnosis per row (not shown / shown not clicked / swiped / no feed trial / working ...)
  - experts: the newest entry the daily `lab: video_review` step wrote for that video in lab/video-review-notes.json
    (diagnosis + what the youtube-traffic corpus and Marcus said + the action + when to look again)
Writes lab/video-review.json, rendered on :8093 tab "Video review"."""
import json, os, re, time
from datetime import datetime, timezone, timedelta
OUT = "/workspace/glottos-auto/out"; A = f"{OUT}/analytics"; LAB = f"{OUT}/lab"
SINCE = datetime(2026, 9, 28, tzinfo=timezone.utc)
HIST, NOTES = f"{LAB}/video-review-history.jsonl", f"{LAB}/video-review-notes.json"
def jload(p, d):
    try: return json.load(open(p))
    except Exception: return d
def num(s):
    if s is None: return None
    m = re.fullmatch(r"([\d.,']+)\s*([KM]?)", str(s).strip())
    if not m: return None
    v = m[1].replace("'", "")
    v = v.replace(",", ".") if m[2] and re.fullmatch(r"\d+,\d{1,2}", v) else v.replace(",", "")
    return float(v) * {"": 1, "K": 1e3, "M": 1e6}[m[2]]
pc = lambda s: float(s.rstrip("%").replace(",", ".")) if s and re.fullmatch(r"[\d.,]+%", s) else None
def secs(s):
    m = re.fullmatch(r"(?:(\d+):)?(\d+):(\d+)", s or "")
    return (int(m[1] or 0) * 3600 + int(m[2]) * 60 + int(m[3])) if m else None
def pdate(s):
    try: return datetime.strptime(s, "%b %d, %Y").replace(tzinfo=timezone.utc)
    except Exception: return None

def symptom(r):
    """First, mechanical diagnosis. The expert step may overrule it (its own 'diagnosis')."""
    age = r["age_days"]
    if age is not None and age < 2: return "too_new", "public under 48 h - not judged yet"
    if r["read_at"] is None: return "no_data", "Studio numbers not read yet"
    if r["type"] == "upload":
        imp, ctr, av = r["impressions"] or 0, r["ctr"], secs(r["avg_view"])
        if imp < 100: return "not_shown", f"long video: YouTube showed the thumbnail only {imp:.0f} times in {age:.0f} days - the problem is BEFORE the click"
        if ctr is not None and ctr < 2: return "not_clicked", f"shown {imp:.0f} times but only {ctr}% clicked - packaging (title/thumbnail) does not win the click"
        if av is not None and av < 60: return "not_watched", f"clicked ({ctr}%) but average view {r['avg_view']} - the opening does not hold"
        return "working", f"shown {imp:.0f}, {ctr}% clicked, average view {r['avg_view']}"
    v, st = r["views"] or 0, r["stayed"]
    if v < 50: return "no_feed_trial", f"Short: {v} views - YouTube barely tried it in the Shorts feed"
    if st is not None and st < 30: return "swiped", f"Short: {v} views but only {st}% stayed - swiped in the first second"
    if v >= 300: return "wave", f"Short: {v} views, {st}% stayed - got a feed wave"
    return "small_wave", f"Short: {v} views, {st}% stayed - a small test group, no second wave"

now = datetime.now(timezone.utc); today = now.strftime("%Y-%m-%d")
snap, deep = jload(f"{A}/latest.json", {}), jload(f"{A}/deep.json", {})
lab, tests, notes = jload(f"{LAB}/lab.json", {}), jload(f"{OUT}/abtests/catalog/tests.json", {}), jload(NOTES, {})
hyp = {}
for h in lab.get("hypotheses", []):
    for v in h.get("videos") or []:
        for yid in re.split(r"[,\s]+", str((v.get("youtube") if isinstance(v, dict) else v) or "")):
            if yid: hyp.setdefault(yid, []).append({"id": h["id"], "status": h.get("status"), "verdict": h.get("verdict"), "statement": (h.get("statement") or "")[:240]})
# history: what each video had on each earlier day (last reading of that day)
hist = {}
try:
    for l in open(HIST):
        try: x = json.loads(l); hist.setdefault(x["id"], {})[x["d"]] = x
        except Exception: pass
except FileNotFoundError: pass

rows, new_hist = [], []
for v in snap.get("videos", []):
    pub = pdate(v.get("date") or "")
    if v.get("visibility") != "Public" or not v.get("id") or not pub or pub < SINCE: continue
    d = deep.get(v["id"], {}); src = d.get("traffic_sources") or []
    r = {"id": v["id"], "title": v["title"], "type": v["type"], "published": pub.strftime("%Y-%m-%d"),
         "age_days": round((now - pub).total_seconds() / 86400, 1), "views": v.get("views"),
         "impressions": num(d.get("impressions")), "ctr": pc(d.get("impressions_ctr")), "stayed": pc(d.get("stayed")),
         "avg_view": d.get("avg_view_duration"), "sources": [f"{a} {b}" for a, b in src[:3]],
         "search_terms": [t[0] for t in (d.get("search_terms") or [])][:5], "read_at": d.get("scraped_at"),
         "hypotheses": hyp.get(v["id"], [])}
    t = tests.get(v["id"])
    r["abtest"] = ({"state": t.get("state"), "since": (t.get("at") or "")[:10], "variants": [x.get("name") for x in t.get("variants") or []]} if t else None)
    h = hist.get(v["id"], {})
    prev = [h[k] for k in sorted(h) if k < today]
    p1 = prev[-1] if prev else None; p7 = next((h[k] for k in sorted(h) if k >= (now - timedelta(days=7)).strftime("%Y-%m-%d")), None)
    r["views_1d"] = (r["views"] - p1["views"]) if p1 and r["views"] is not None and p1.get("views") is not None else None
    r["impr_1d"] = (r["impressions"] - p1["impressions"]) if p1 and r["impressions"] is not None and p1.get("impressions") is not None else None
    r["views_7d"] = (r["views"] - p7["views"]) if p7 and p7["d"] < today and r["views"] is not None and p7.get("views") is not None else None
    r["trend"] = [{"d": k, "views": h[k].get("views"), "impressions": h[k].get("impressions")} for k in sorted(h)][-14:]
    r["symptom"], r["symptom_why"] = symptom(r)
    n = (notes.get("videos") or {}).get(v["id"]) or []
    r["experts"] = n[-1] if n else None
    r["experts_count"] = len(n)
    rows.append(r)
    new_hist.append({"d": today, "id": v["id"], "at": now.strftime("%Y-%m-%dT%H:%MZ"), "views": r["views"], "impressions": r["impressions"],
                     "ctr": r["ctr"], "stayed": r["stayed"], "read_at": r["read_at"]})

# history: keep only the LAST reading per (video, day) -> rewrite today's lines
old = []
try: old = [l for l in open(HIST) if l.strip() and json.loads(l).get("d") != today]
except FileNotFoundError: pass
with open(HIST + ".tmp", "w") as f:
    f.writelines(old); f.writelines(json.dumps(x) + "\n" for x in new_hist)
os.replace(HIST + ".tmp", HIST)

ORDER = ["not_shown", "no_feed_trial", "not_clicked", "swiped", "not_watched", "small_wave", "no_data", "too_new", "wave", "working"]
rows.sort(key=lambda r: (ORDER.index(r["symptom"]), r["published"]))
groups = {}
for r in rows: groups.setdefault(r["symptom"], []).append(r["id"])
last_rev = notes.get("last_review")
out = {"at": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "since": SINCE.strftime("%Y-%m-%d"), "snapshot_at": snap.get("at"),
       "deep_read_latest": max((r["read_at"] or "" for r in rows), default=None), "videos": len(rows),
       "groups": {k: len(groups[k]) for k in ORDER if k in groups}, "group_ids": groups,
       "last_review": last_rev, "discussions": (notes.get("discussions") or [])[-12:], "rows": rows}
json.dump(out, open(f"{LAB}/video-review.json.tmp", "w"), indent=1, ensure_ascii=False)
os.replace(f"{LAB}/video-review.json.tmp", f"{LAB}/video-review.json")
print(f"video-review: {len(rows)} videos since {out['since']} · " + " ".join(f"{k}={v}" for k, v in out["groups"].items()))
