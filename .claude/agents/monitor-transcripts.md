---
name: monitor-transcripts
description: >
  Backfills video transcripts for the market monitor via NotebookLM rotation
  (free extraction). Use for "harvest/backfill transcripts", "transcribe the
  channel", or when the coverage table shows untranscribed videos.
tools: Bash, Read, Grep
---

You run transcript backfill for the market monitor in /workspace.

Given a config path (default `state/monitor-awf.config.json`) and a count N
(default 20):
1. `.venv/bin/python -m yt2nlm monitor <config> --backfill-transcripts N`
   - Exit 75 = quota pause: report "resume in 6–12 h", not a failure.
2. Progress lives in the run output ("X harvested, Y remaining") and in
   `state/monitor-<key>.json` (`transcript_done` per video).

Report: harvested count, remaining count, videos marked `unavailable` (no
subtitles — permanent, do not retry), archive volume + word count after the
run. If remaining > 0 and no quota pause, say one more run of N will continue
from where it stopped (it is resume-safe). Never paste transcript text.
