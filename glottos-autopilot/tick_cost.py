#!/usr/bin/env python3
"""Per-tick token/cost logging (user 2026-09-29: "record usage per tick, so we can see what each step really costs").
loop.sh runs each tick with --output-format json; this prints the tick's result text (as before) plus one "cost:" line
to the log and appends a row to costs.jsonl. usage/total_cost_usd cover the whole tick (subagents included, per the CLI
result); cost is the API-price equivalent, a relative measure of how much of the subscription limit a step eats.
  python3 tick_cost.py <out-file> <due> <model> <rc> <start-epoch>
  python3 tick_cost.py --summary [days]      -> cost per step kind"""
import json, sys, time, collections
F = "/workspace/glottos-autopilot/costs.jsonl"
if sys.argv[1] == "--summary":
    days = float(sys.argv[2]) if len(sys.argv) > 2 else 7; cut = time.time() - days * 86400
    agg = collections.defaultdict(lambda: [0, 0.0, 0])
    for l in open(F):
        r = json.loads(l)
        if r["ts"] < cut: continue
        k = r["due"].split(": ")[-1]; a = agg[k]; a[0] += 1; a[1] += r.get("cost_usd") or 0; a[2] += r.get("tokens_in", 0)
    tot = sum(a[1] for a in agg.values()) or 1
    print(f"last {days:g} days: step, ticks, cost-equiv USD, share, avg input tokens")
    for k, (n, c, ti) in sorted(agg.items(), key=lambda x: -x[1][1]):
        print(f"  {k:16} {n:4} {c:8.2f} {100*c/tot:5.1f}%  {ti//max(n,1):>9,}")
    sys.exit(0)
out, due, model, rc, start = sys.argv[1:6]
raw = open(out, errors="replace").read()
try:
    d = json.loads(raw[raw.index("{"):])
except Exception:
    print(raw); print(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} cost: unknown (no JSON result)"); sys.exit(0)
print(d.get("result") or raw[-2000:])
u = d.get("usage") or {}
tin = sum(u.get(k, 0) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"))
row = {"ts": int(time.time()), "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "due": due, "model": model,
       "rc": int(rc), "secs": int(time.time()) - int(start), "turns": d.get("num_turns"), "cost_usd": d.get("total_cost_usd"),
       "tokens_in": tin, "tokens_out": u.get("output_tokens", 0),
       "by_model": {m: {k: v for k, v in x.items() if k in ("inputTokens", "outputTokens", "cacheReadInputTokens",
                        "cacheCreationInputTokens", "costUSD")} for m, x in (d.get("modelUsage") or {}).items()}}
open(F, "a").write(json.dumps(row) + "\n")
print(f"{row['at']} cost: ${row['cost_usd'] or 0:.2f} equiv · {row['turns']} turns · {row['secs']}s · in {tin:,} / out {row['tokens_out']:,} tokens"
      + (" · " + ", ".join(f"{m.split('-2')[0]} ${x.get('costUSD', 0):.2f}" for m, x in row["by_model"].items()) if row["by_model"] else ""))
