#!/usr/bin/env python3
"""Add the verified dummy-load patent set to NotebookLM notebook 25_349_2026.

Reads state/patents_25_349_2026.json (produced by the verification pass),
dedups against sources already in the notebook, and adds each remaining patent
as a source (patentimages PDF when available, else the Google Patents page).
Serialized via yt2nlm.nlm (anti RESOURCE_EXHAUSTED) with --wait so we can detect
ghost sources (add returns None ⇒ ingestion likely failed)."""
from __future__ import annotations

import json
import os
import re
import sys

sys.path.insert(0, "/workspace")
os.environ.setdefault("NLM_BIN", "/home/node/patent-wiki-analyzer/.venv/bin/nlm")
from yt2nlm import nlm  # noqa: E402

NB = "56a131d5-52fd-4255-868b-ddf1490ea1fe"  # 25_349_2026
ITEMS = json.load(open("/workspace/state/patents_25_349_2026.json", encoding="utf-8"))


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def main() -> int:
    existing = nlm.list_sources(NB)
    blob = norm(" ".join((s.get("title") or "") + " " + (s.get("url") or "")
                         for s in existing))
    print(f"notebook 25_349_2026: {len(existing)} existing source(s)")

    results = []
    for it in ITEMS:
        num = it["number"]
        if not it.get("real"):
            print(f"  SKIP  {num}: not verified real")
            results.append({**it, "added": False, "reason": "not real"})
            continue
        if norm(num) in blob:
            print(f"  DUP   {num}: already in notebook")
            results.append({**it, "added": False, "reason": "dup"})
            continue
        title = f"{num} — {it.get('title') or it.get('label') or ''}"[:120]
        try:
            sid = nlm.add_url(NB, it["url"], title=title, wait=True, timeout=600)
        except Exception as exc:  # noqa: BLE001
            print(f"  ERR   {num}: {exc}")
            results.append({**it, "added": False, "reason": f"err {exc}"[:120]})
            continue
        ok = bool(sid)
        print(f"  {'ADD ' if ok else 'GHOST'} {num} [{it['kind']}] -> {sid}")
        results.append({**it, "added": ok, "source_id": sid,
                        "reason": "" if ok else "ghost (no source id)"})

    json.dump(results, open("/workspace/state/patents_25_349_2026_added.json", "w"),
              ensure_ascii=False, indent=2)
    added = sum(1 for r in results if r.get("added"))
    ghosts = [r["number"] for r in results if r.get("reason", "").startswith("ghost")]
    print(f"\n=== done: added {added}, dup/skip {len(results)-added}, "
          f"ghosts {len(ghosts)} {ghosts} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
