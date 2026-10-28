#!/usr/bin/env python3
"""Lab numbers + rule verdicts WITHOUT Claude (user 2026-10-23: "You spend way too much token in a short period of time").

Every loop pass, inside tick.lock and before due.py (so no Claude tick is editing lab.json at the same time):
  1. For every hypothesis that is `waiting_send` / `live`: fill each video's `youtube`, `public_at`, `views`, `engaged_pct` (= stayed %),
     `impressions`, `ctr`, `avg_view` from yt/status.json + analytics/latest.json + analytics/deep.json.
  2. A hypothesis with a machine rule `win_rule` gets its verdict here, no Claude:
       "win_rule": {"at_hours": 48, "need": "any" | "all" | "majority", "all_of": [{"metric": "views", "min": 500},
                    {"metric": "stayed_pct", "min": 40}]}
     metrics: views, stayed_pct, ctr_pct, impressions, avg_view_s. Readable = every sent video public >= at_hours AND has the numbers.
     A video "wins" when it meets every condition; the hypothesis wins per `need` (default "any"), "lose" when none wins, "mixed" otherwise.
     Sets status "verdict", verdict, verdict_at, result (numbers only), appends one dated line to lessons + content/insights/ab-lessons.md.
     `next` / `changed` stay for the next `lab: analyze` to write (it gets them in lab-brief.json -> "auto_verdicts_to_explain").
  3. Readable hypotheses WITHOUT a win_rule -> out/lab/verdicts-due.json; `lab: analyze` judges those against their `test` text.
Prints one line only when something changed.
"""
import json, os, re, sys, time, datetime as dt

OUT = "/workspace/glottos-auto/out/"
LABF = OUT + "lab/lab.json"
DUEF = OUT + "lab/verdicts-due.json"
ABL = "/workspace/glottos-marketing/content/insights/ab-lessons.md"
now = dt.datetime.now(dt.timezone.utc)


def load(p, d=None):
    try:
        return json.load(open(p))
    except Exception:
        return d


def pct(x):
    if x is None: return None
    try: return float(str(x).replace("%", "").replace(",", "").strip())
    except ValueError: return None


def num(x):
    if x is None: return None
    try: return int(float(str(x).replace(",", "").strip()))
    except ValueError: return None


def secs(x):
    if not x: return None
    try:
        p = [int(v) for v in str(x).split(":")]
        return p[0] * 60 + p[1] if len(p) == 2 else p[0] * 3600 + p[1] * 60 + p[2]
    except ValueError: return None


def ts(s):
    if not s: return None
    try:
        t = dt.datetime.fromisoformat(str(s).replace("Z", "+00:00"))
        return t if t.tzinfo else t.replace(tzinfo=dt.timezone.utc)
    except ValueError: return None


lab = load(LABF)
if not lab: sys.exit(0)
st = load(OUT + "yt/status.json", {}) or {}
latest = load(OUT + "analytics/latest.json", {}) or {}
deep = load(OUT + "analytics/deep.json", {}) or {}

by_vid = {}                     # local file id -> its live YouTube records (the -hd1440 master counts for its base vid)
for v in st.get("videos", []):
    y = v.get("youtube")
    if y and y.get("state") != "deleted":
        by_vid.setdefault(v["vid"].replace("-hd1440", ""), []).append(y)
views = {v["id"]: v for v in latest.get("videos", [])}

changed, auto, due = [], [], []
for h in lab.get("hypotheses", []):
    if h.get("status") not in ("waiting_send", "live"): continue
    h["videos"] = [v if isinstance(v, dict) else {"vid": v} for v in h.get("videos", [])]   # ticks also log bare unit ids (H104)
    for v in h.get("videos", []):
        cand = by_vid.get(v.get("vid", "")) or []
        # deterministic: keep the YouTube id already recorded; else the public one; else the first (status.json order varies)
        y = (next((c for c in cand if c.get("id") == v.get("youtube")), None) or next((c for c in cand if c.get("state") == "public"), None)
             or (cand[0] if cand else None) or ({"id": v["youtube"]} if v.get("youtube") else None))
        if not y: continue
        new = {"youtube": y["id"]}
        if y.get("state") == "public" and ts(y.get("at")): new["public_at"] = ts(y["at"]).astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
        lv, dv = views.get(y["id"]), deep.get(y["id"]) or {}
        if lv: new["views"], new["visibility"] = lv.get("views"), lv.get("visibility")
        if dv.get("stayed"): new["engaged_pct"] = pct(dv["stayed"])
        if dv.get("impressions") is not None: new["impressions"] = num(dv["impressions"])
        if dv.get("impressions_ctr") is not None: new["ctr"] = pct(dv["impressions_ctr"])
        if dv.get("avg_view_duration"): new["avg_view"] = dv["avg_view_duration"]
        new = {k: x for k, x in new.items() if x is not None}
        if any(v.get(k) != x for k, x in new.items()):
            v.update(new); changed.append(h["id"])
    # 2026-10-28 gap sweep: nothing promoted waiting_send -> live, so H87/H102/H103 sat public for days without a verdict. Every video
    # on YouTube (public or scheduled) = the send is done -> live; the verdict then waits for at_hours after public_at as before.
    if h.get("status") == "waiting_send" and h.get("videos") and all(v.get("youtube") for v in h["videos"])             and all((views.get(v["youtube"]) or {}).get("visibility") in ("Public", "Scheduled") or v.get("public_at") for v in h["videos"]):
        h["status"] = "live"; h["live_since"] = now.strftime("%Y-%m-%dT%H:%MZ"); changed.append(h["id"])
    if h.get("status") != "live": continue
    sent = [v for v in h.get("videos", []) if v.get("youtube") and v.get("public_at")]
    if not sent: continue
    rule = h.get("win_rule")
    at_h = (rule or {}).get("at_hours", 48)
    ages = [(now - ts(v["public_at"])).total_seconds() / 3600 for v in sent if ts(v["public_at"])]
    if not ages or min(ages) < at_h: continue
    if not isinstance(rule, dict) or not rule.get("all_of"):
        due.append({"id": h["id"], "test": h.get("test"), "videos": [{k: v.get(k) for k in ("vid", "youtube", "public_at", "views", "engaged_pct",
                    "impressions", "ctr", "avg_view")} for v in sent]})
        continue
    get = {"views": lambda v: num(v.get("views")), "stayed_pct": lambda v: pct(v.get("engaged_pct")), "ctr_pct": lambda v: pct(v.get("ctr")),
           "impressions": lambda v: num(v.get("impressions")), "avg_view_s": lambda v: secs(v.get("avg_view"))}
    try:
        vals = [[get[c["metric"]](v) for c in rule["all_of"]] for v in sent]
    except KeyError as e:
        due.append({"id": h["id"], "test": h.get("test"), "rule_error": f"unknown metric {e}"}); continue
    if any(x is None for row in vals for x in row):
        continue                                    # numbers not read yet (deep.json is daily) -> next pass
    wins = [all(x >= c["min"] for x, c in zip(row, rule["all_of"])) for row in vals]
    need, nw = rule.get("need", "any"), sum(wins)
    ok = {"any": nw >= 1, "all": nw == len(wins), "majority": nw * 2 > len(wins)}.get(need, nw >= 1)
    verdict = "win" if ok else ("lose" if nw == 0 else "mixed")
    cond = " and ".join(f"{c['metric']} >= {c['min']}" for c in rule["all_of"])
    nums = "; ".join(f"{v.get('vid')}: " + ", ".join(f"{c['metric']} {x}" for x, c in zip(row, rule["all_of"])) for v, row in zip(sent, vals))
    h.update({"status": "verdict", "verdict": verdict, "verdict_at": now.strftime("%Y-%m-%dT%H:%MZ"), "auto_verdict": True,
              "result": f"auto verdict {now:%Y-%m-%d} at {at_h} h (rule: {cond}, need {need}): {nw}/{len(wins)} videos met it. {nums}"})
    line = f"{now:%Y-%m-%d} (auto, lab_verdicts.py): {h['id']} {verdict.upper()} - {nw}/{len(wins)} met {cond} at {at_h} h. {nums}"
    lab.setdefault("lessons", []).append(line)
    try:
        with open(ABL, "a") as f: f.write(f"\n- {line}\n")
    except OSError: pass
    auto.append(h["id"]); changed.append(h["id"])

if changed:
    lab.setdefault("auto_verdicts_to_explain", [])
    lab["auto_verdicts_to_explain"] = sorted(set(lab["auto_verdicts_to_explain"]) | set(auto))
    json.dump(lab, open(LABF + ".tmp", "w"), indent=1, ensure_ascii=False); os.replace(LABF + ".tmp", LABF)
old = load(DUEF, {}) or {}
if [d["id"] for d in old.get("due", [])] != [d["id"] for d in due]:
    print(f"verdicts due for analyze: {', '.join(d['id'] for d in due) or 'none'}")
json.dump({"at": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "due": due}, open(DUEF + ".tmp", "w"), indent=1, ensure_ascii=False); os.replace(DUEF + ".tmp", DUEF)
if auto: print(f"auto verdicts: {', '.join(auto)}")
elif changed: print(f"numbers refreshed: {len(set(changed))} hypotheses")
