#!/bin/sh
# Knowledge-gap enrichment applier (2026-10-28): every 60 s apply the user's approved "enrich" requests from the :8122 page.
# Zero Claude tokens, no NotebookLM calls — it only edits a pipeline's queries.json and ages its discovery stamps.
while true; do
  python3 /app/runner/enrich_apply.py >> /app/runner/enrich.log 2>&1
  sleep 60
done
