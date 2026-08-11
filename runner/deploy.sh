#!/usr/bin/env bash
# Build + (re)run the always-on monitor runner. No published ports — the
# dashboard on :8091 (yt2nlm-web) reads the same state/reports read-only.
#
# ⚠ Before redeploying: check reports/monitor-awf/progress.json — if a cycle
# is mid-run (status=running, fresh heartbeat), wait for it or you kill it
# (it resumes, but wastes work).
set -euo pipefail

NAME=awf-monitor-runner
HOST_WS="/root/claude-sandbox/workspaces/need collecting from customers comments"
HOST_PROFILE="/root/claude-sandbox/persistent/nlm-profile"
CTX="${BUILD_CTX:-/workspace/runner}"

echo ">> build $NAME from $CTX"
docker build -t "$NAME" "$CTX"

echo ">> (re)start $NAME (loop every ${INTERVAL:-21600}s)"
docker rm -f "$NAME" >/dev/null 2>&1 || true
docker run -d --name "$NAME" --restart unless-stopped \
  -e INTERVAL="${INTERVAL:-21600}" \
  -v "$HOST_WS:/app" \
  -v "$HOST_PROFILE:/home/app/.notebooklm-mcp-cli" \
  "$NAME"

docker ps --filter "name=$NAME" --format '{{.Names}}  {{.Status}}'
