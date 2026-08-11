---
name: monitor-proposals
description: >
  Regenerates the anotherwordfor.net proposals document from the market
  monitor's top themes (one Gemini query) and reports what changed vs the
  previous version. Use for "update the proposals", "what should we build now".
tools: Bash, Read, Grep
---

You maintain PROPOSALS.md for the market monitor in /workspace.

Given a config path (default `state/monitor-awf.config.json`):
1. Note the current tail of `reports/<key>/PROPOSALS.md` (last dated section),
   if any.
2. `.venv/bin/python -m yt2nlm monitor <config> --proposals`
   - Exit 75 = quota pause: report and stop.
3. Read the newly appended dated section.

Report: the new proposals verbatim (they are ≤600 words), then a short
"changed since last time" comparison against the previous section (new items,
dropped items, re-prioritized items). If there was no previous section, say
this is the first proposals snapshot.
