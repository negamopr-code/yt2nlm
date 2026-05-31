#!/bin/sh
# Seed the merge-step credentials from a READ-ONLY mount of the host's Claude
# config, then start the server. Copying (not mounting) credentials keeps the
# container's `claude` from writing back into the host config dir — no races
# on the operator's live .claude.json; the container refreshes its own copy.
#
# Mount the host config read-only at /seed (see web/deploy.sh). If absent, the
# merge step just falls back to ANTHROPIC_API_KEY (if set) or reports an error;
# the verbatim fan-out always works regardless.
if [ -f /seed/.credentials.json ]; then
  cp /seed/.credentials.json "$CLAUDE_CONFIG_DIR/.credentials.json" 2>/dev/null \
    && echo "entrypoint: seeded claude credentials" \
    || echo "entrypoint: WARN could not seed credentials (merge may be unavailable)"
else
  echo "entrypoint: no /seed credentials; merge uses ANTHROPIC_API_KEY if set"
fi

exec python3 /app/web/server.py
