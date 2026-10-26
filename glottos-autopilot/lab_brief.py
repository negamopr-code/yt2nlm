#!/usr/bin/env python3
"""lab-brief.json = the SMALL view of lab.json that every lab tick reads first (user 2026-10-23: "You spend way too much token").

lab.json is ~0.8 MB (100 hypotheses with their whole history); a tick that reads it re-sends ~100k tokens on every turn. This brief
(no Claude, every loop pass) holds what a step needs: state flags, unread hints, the hypotheses to produce next IN FULL, every other open
hypothesis in one short row, the last verdicts and lessons, the newest ideas entry, the top of the scoreboard, verdicts due, footage sources.
Full text of anything: `python3 - <<'PY'` with json.load and print ONLY the keys needed. Never cat / Read lab.json whole.
"""
import json, os, datetime as dt

OUT = "/workspace/glottos-auto/out/lab/"
now = dt.datetime.now(dt.timezone.utc)


def load(p, d=None):
    try: return json.load(open(p))
    except Exception: return d


def cut(s, n=280):
    s = s if isinstance(s, str) else json.dumps(s, ensure_ascii=False)
    return s if len(s) <= n else s[:n] + " …[lab.json]"


lab = load(OUT + "lab.json")
if not lab: raise SystemExit(0)
hyps = lab.get("hypotheses", [])
try: hints = [json.loads(l) for l in open(OUT + "hints.jsonl") if l.strip()]
except Exception: hints = []
po = lab.get("produce_only")
if po: nxt = [h for h in hyps if h.get("id") in po and h.get("status") in ("proposed", "producing")]
else: nxt = [h for h in hyps if h.get("status") in ("producing", "proposed")][:1]
nxt_ids = {h["id"] for h in nxt}


def row(h):
    r = {"id": h["id"], "status": h.get("status"), "statement": cut(h.get("statement"), 200), "test": cut(h.get("test"), 200),
         "next": cut(h.get("next"), 160)}
    if h.get("win_rule"): r["win_rule"] = h["win_rule"]
    vids = [v if isinstance(v, dict) else {"vid": v} for v in h.get("videos", [])]   # ticks also log bare unit/YouTube ids (H104, H105)
    vs = [{k: v.get(k) for k in ("vid", "youtube", "public_at", "views", "engaged_pct", "ctr") if v.get(k) is not None} for v in vids]
    if vs: r["videos"] = vs
    return r


board = load(OUT + "board.json", {}) or {}
ff = load("/workspace/glottos-marketing/state/footage/sources.json", {}) or {}
brief = {
    "at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "how_to_use": "Read this instead of lab.json. Edit lab.json only with a small python json load/modify/save of the keys you change "
                  "(write .tmp then os.replace, indent=1, ensure_ascii=False). Full text of a hypothesis: print just that one.",
    "state": {k: lab.get(k) for k in ("cycle", "last_analyze", "last_produce", "paused", "produce_paused", "produce_only", "blocked_until",
                                      "hints_read") if k in lab},
    "hints_total": len(hints),
    "hints_unread": hints[lab.get("hints_read", 0):],
    "produce_next_FULL": nxt,
    "open": [row(h) for h in hyps if h.get("status") != "verdict" and h["id"] not in nxt_ids],
    "recent_verdicts": [{"id": h["id"], "verdict": h.get("verdict"), "result": cut(h.get("result"), 220), "auto": h.get("auto_verdict", False)}
                        for h in [x for x in hyps if x.get("status") == "verdict"][-15:]],
    "auto_verdicts_to_explain": lab.get("auto_verdicts_to_explain", []),
    "verdicts_due": (load(OUT + "verdicts-due.json", {}) or {}).get("due", []),
    "lessons_last": lab.get("lessons", [])[-12:],
    "ideas_newest": (lab.get("ideas") or [None])[0],
    "production_rules": lab.get("production_rules"),
    "board_top_ctr": (board.get("top_ctr") or [])[:8],
    "board_lanes": [{k: l.get(k) for k in ("lane", "n", "views_median", "views_best", "best_title", "best_id", "stayed_avg", "ctr")}
                    for l in (board.get("lanes") or [])[:12]],
    "pareto_80_20": load(OUT + "pareto.json"),   # lab_pareto.py: which 20 % of effort gave 80 % of views (user 2026-10-23)
    # TRIZ exchange (user 2026-10-23): ledger -> dossier (also a source in the traffic notebook) -> matrix built WITH the experts
    "triz": {"dossier": "/workspace/glottos-auto/out/lab/triz/dossier.md", "params": "/workspace/glottos-auto/out/lab/triz/params.json",
             "matrix": "/workspace/glottos-auto/out/lab/triz/matrix.json",
             "contradictions": [{k: c.get(k) for k in ("id", "improve", "worsens", "resolution_round1")} for c in
                                (load("/workspace/glottos-auto/out/lab/triz/matrix.json", {}) or {}).get("contradictions", [])],
             "rounds": len((load("/workspace/glottos-auto/out/lab/triz/matrix.json", {}) or {}).get("rounds", []))},
    # every long video targets ONE keyword from the top of this list (user 2026-10-23)
    "search_targets_top": [{k: t.get(k) for k in ("keyword", "difficulty", "volume", "gap", "best_old_impressions", "best_old_ctr")}
                           for t in ((load(OUT + "search-targets.json", {}) or {}).get("targets") or [])
                           if (t.get("volume_n") or 0) >= 1000 and t.get("gap") != "new made"][:12],
    "expert_bar": lab.get("expert_bar"),
    "secret_sauce": lab.get("secret_sauce"),
    # user 2026-10-23: every new video names its hypothesis, aligned with BOTH experts -> produce refuses these until analyze fixes them
    "proposed_missing_fields": [{"id": h["id"], "missing": [k for k in ("variable", "experts", "win_rule") if not h.get(k)]}
                                for h in hyps if h.get("status") in ("proposed", "producing")
                                and any(not h.get(k) for k in ("variable", "experts", "win_rule"))],
    "footage_sources": {"file": "/workspace/glottos-marketing/state/footage/sources.json",
                        "finder": "python3 /workspace/glottos-marketing/shorts/find_footage.py \"<scene words>\" [--source …] [--json]",
                        "sources": [s.get("id") for s in ff.get("sources", [])]},
}
tmp = OUT + "lab-brief.json.tmp"
json.dump(brief, open(tmp, "w"), indent=1, ensure_ascii=False); os.replace(tmp, OUT + "lab-brief.json")
