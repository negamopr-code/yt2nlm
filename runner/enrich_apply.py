#!/usr/bin/env python3
"""Apply the user's knowledge-gap decisions (user 2026-10-28, from the :8122 Rezvyakov ask page: "ask user either to enrichment of
existing nlms without spending tokens or to create a new space").

Request files: /home/app/.notebooklm-mcp-cli/enrich-requests/<id>.json (shared NLM bind store; written by rezv-ask POST /api/enrich).
  action "enrich", status "approved" → find the expert pipeline whose daemon names that notebook id (/app/state/*/), add the search
  phrases to its queries.json, and make its next turn re-run discovery (videos.json + web_discover.stamp aged past 24 h). The daemon
  then harvests as usual — no Claude tokens. Status → "applied: <pipeline> (+N phrases), re-discovery on its next turn".
  No pipeline for that notebook → status explains that a one-time Claude setup is needed.
  action "new" → left untouched (waits for a Claude session to clone a pipeline + notebook).
Run by runner/enrich_daemon.sh every 60 s. Zero Claude tokens.
"""
import glob, json, os, time

REQS = "/home/app/.notebooklm-mcp-cli/enrich-requests"
STATE = "/app/state"


def pipeline_dir(nb):
    """The state dir with a queries.json whose daemon script / config names the notebook."""
    for d in sorted(glob.glob(f"{STATE}/*/")):
        if not os.path.exists(os.path.join(d, "queries.json")):
            continue
        for f in glob.glob(os.path.join(d, "*.sh")) + glob.glob(os.path.join(d, "*.py")):
            try:
                if nb in open(f, errors="ignore").read():
                    return d.rstrip("/")
            except OSError:
                pass
    return None


def apply(r):
    d = pipeline_dir(r["notebook"])
    if not d:
        return ("no token-free pipeline feeds this notebook yet — a one-time Claude setup is needed "
                "(ask Claude: 'build the usual drill for notebook " + r["notebook"] + "')")
    qf = os.path.join(d, "queries.json")
    q = json.load(open(qf))
    have = {x.lower() for x in q.get("queries", [])}
    new = [x for x in r["queries"] if x.lower() not in have]
    q["queries"] = q.get("queries", []) + new
    q.setdefault("_enrich_log", []).append({"at": r["at"], "request": r["id"], "topic": r["topic"], "added": new})
    tmp = qf + ".tmp"
    json.dump(q, open(tmp, "w"), ensure_ascii=False, indent=1)
    os.replace(tmp, qf)
    old = time.time() - 2 * 86400
    for f in ("videos.json", "web_discover.stamp"):
        p = os.path.join(d, f)
        if os.path.exists(p):
            os.utime(p, (old, old))
    note = ""
    if q.get("title_must"):
        note = f"; note: new videos must still match its title filter ({', '.join(q['title_must'][:4])}…)"
    return f"applied: pipeline {os.path.basename(d)} (+{len(new)} search phrases), re-discovery on its next turn{note}"


def main():
    for f in sorted(glob.glob(f"{REQS}/*.json")):
        try:
            r = json.load(open(f))
        except (OSError, ValueError):
            continue
        if r.get("action") != "enrich" or r.get("status") != "approved":
            continue
        try:
            r["status"] = apply(r)
        except Exception as e:  # noqa: BLE001
            r["status"] = f"failed: {type(e).__name__}: {e}"[:300]
        r["done_at"] = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())
        tmp = f + ".tmp"
        json.dump(r, open(tmp, "w"), ensure_ascii=False, indent=1)
        os.replace(tmp, f)
        print(r["done_at"], r["id"], r["status"], flush=True)


if __name__ == "__main__":
    main()
