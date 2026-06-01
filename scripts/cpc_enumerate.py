#!/usr/bin/env python3
"""Exhaustive-ish CPC enumeration for the 'conditionally-activated artificial load
governed by charging current' concept. Waits out the Google Patents query-API
rate-limit, then enumerates the precise CPC classes + concept intersections,
scores every hit, and flags anything that could beat the current top-2
(WO2016033258A1, US9425629B2/US9812893B2).

Runs headless/background. Writes results to state/cpc_enum_results.json.
"""
from __future__ import annotations
import urllib.request, urllib.parse, json, time, re, sys

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
      "Accept": "application/json"}

def xhr(query: str, num: int = 100, page: int = 0):
    inner = urllib.parse.urlencode({"q": query, "num": num, "page": page})
    url = f"https://patents.google.com/xhr/query?url={urllib.parse.quote(inner)}&exp="
    req = urllib.request.Request(url, headers=UA)
    raw = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
    return json.loads(raw)

def parse(d):
    out = []
    res = d.get("results", {})
    total = res.get("total_num_results")
    for cl in res.get("cluster", []):
        for r in cl.get("result", []):
            p = r.get("patent", {})
            num = p.get("publication_number")
            if not num:
                continue
            strip = lambda s: re.sub(r"</?b>", "", s or "").strip()
            out.append({"number": num, "title": strip(p.get("title")),
                        "snippet": strip(p.get("snippet")),
                        "assignee": p.get("assignee"), "year": p.get("priority_date")})
    return total, out

def wait_for_api(max_wait=2400):
    """Poll until the query API answers (recovers from 503). Returns True/False."""
    waited, delay = 0, 60
    while waited < max_wait:
        try:
            xhr("H02J7/00712", num=10, page=0)
            print(f"[poll] API recovered after {waited}s", flush=True)
            return True
        except Exception as e:
            print(f"[poll] still blocked ({e}); sleep {delay}s (waited {waited}s)", flush=True)
            time.sleep(delay)
            waited += delay
            delay = min(int(delay * 1.4), 180)
    return False

def enumerate_query(query, max_pages=6):
    """Pull up to max_pages*100 results for a query (paginated)."""
    items, total = [], None
    for pg in range(max_pages):
        for attempt in range(4):
            try:
                d = xhr(query, num=100, page=pg)
                break
            except Exception as e:
                time.sleep(20 * (attempt + 1))
        else:
            break
        t, batch = parse(d)
        total = total or t
        if not batch:
            break
        items.extend(batch)
        time.sleep(2.0)
        if len(batch) < 100:
            break
    return total, items

HAVE = {"KR20240016842","US20250192591","WO2024025164","KR100426643","US20250183861",
        "US11522381","US7622897","US12133040","US20230379613","US9425629","US20160359357",
        "US12113373","US20220200362","WO2016033258","JPS59185160","US20170179755",
        "US20260074571","US10439441","US20170098963","US20070024261","US9812893",
        "WO2009140222","US20140152117"}
b = lambda n: re.sub(r"[A-Z]\d?$", "", n)

WEIGHTS = [(r"dummy load",5),(r"ballast",4),(r"minimum load",4),(r"artificial load",4),
           (r"pseudo load|bleeder",3),(r"variable load",2),(r"state.?of.?charge|\bSOC\b",2),
           (r"full.?bridge|half.?bridge",2),(r"end.?of.?charge|fully charged",2),
           (r"light load|no.?load",2),(r"constant.?voltage|\bCV\b|CC.?to.?CV",1),
           (r"rectifier",1),(r"earbud|earphone|cradle|charging case|hearing aid",2),
           (r"wireless",0.5)]
def score(it):
    txt = f"{it['title']} {it['snippet']}".lower()
    return sum(w for pat,w in WEIGHTS if re.search(pat, txt))

def main():
    if not wait_for_api():
        json.dump({"status": "API_STILL_BLOCKED"}, open("/workspace/state/cpc_enum_results.json","w"))
        print("=== GAVE UP: Google Patents query API still blocked ===", flush=True)
        return 1
    QUERIES = [
        "H02J7/00712",                       # CPC: charging with dummy/variable load
        "H02J7/0049 dummy load",             # CPC: load management during charging
        "H02J7/00712 dummy load",
        "H02J7/00712 minimum load",
        "H02J50/80 dummy load",              # wireless power, comms/load
        "dummy load rectifier full bridge half bridge wireless charging",
        "artificial load state of charge wireless charging rectifier stability",
        "minimum load wireless power receiver constant voltage end of charge",
    ]
    pool, class_totals = {}, {}
    for q in QUERIES:
        try:
            total, items = enumerate_query(q, max_pages=6 if q.startswith("H02J7/00712") else 2)
        except Exception as e:
            print(f"[q] {q!r} failed: {e}", flush=True); continue
        class_totals[q] = {"total": total, "pulled": len(items)}
        print(f"[q] {q!r}: total={total} pulled={len(items)}", flush=True)
        for it in items:
            if b(it["number"]) in HAVE:
                continue
            cur = pool.get(it["number"])
            if not cur:
                it["sc"] = score(it); pool[it["number"]] = it
        time.sleep(2.0)
    ranked = sorted(pool.values(), key=lambda x: x["sc"], reverse=True)
    out = {"status": "OK", "class_totals": class_totals,
           "n_new_candidates": len(ranked), "top": ranked[:30]}
    json.dump(out, open("/workspace/state/cpc_enum_results.json","w"), ensure_ascii=False, indent=2)
    print(f"\n=== DONE: {len(ranked)} new candidates; top by concept-score: ===", flush=True)
    for it in ranked[:20]:
        print(f"  sc={it['sc']:>4} {it['number']:16} {it['title'][:58]}", flush=True)
    return 0

if __name__ == "__main__":
    sys.exit(main())
