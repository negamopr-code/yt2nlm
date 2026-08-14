#!/usr/bin/env bash
# Build + (re)run the videogen review-queue container on host :8108.
# ⚠ Before redeploying: check reports/videogen/progress.json — a render job
# mid-run dies with the container (it resumes, but wastes work).
set -euo pipefail

NAME=awf-videogen
PORT=8108
HOST_WS="/root/claude-sandbox/workspaces/need collecting from customers comments"
HOST_PROFILE="/root/claude-sandbox/persistent/nlm-profile"
CTX="${BUILD_CTX:-/workspace/videogen}"

# generic probe: ANY listener on the port = taken (project rule)
if python3 -c "import socket; socket.create_connection(('127.0.0.1', $PORT), 1)" 2>/dev/null; then
  # a listener answered from inside this container's netns — could be the host
  # port-forward of an existing owner; check it's not our own previous instance
  if ! docker ps --format '{{.Names}}' | grep -q "^$NAME$"; then
    echo "!! port $PORT already has a listener and it is not $NAME — pick another port"; exit 1
  fi
fi

echo ">> build $NAME from $CTX"
docker build -t "$NAME" "$CTX"

echo ">> (re)start $NAME on :$PORT"
docker rm -f "$NAME" >/dev/null 2>&1 || true
docker run -d --name "$NAME" --restart unless-stopped \
  -p "$PORT:$PORT" \
  -v "$HOST_WS:/app" \
  -v "$HOST_PROFILE:/home/app/.notebooklm-mcp-cli" \
  "$NAME"

echo ">> up: http://localhost:$PORT/"
docker ps --filter "name=$NAME" --format '{{.Names}}  {{.Status}}  {{.Ports}}'
