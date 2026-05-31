#!/usr/bin/env bash
# Build + (re)run the yt2nlm-web fan-out UI as its own container on host :8091.
#
# Runs from INSIDE the claude container via the mounted docker socket, so all
# paths passed to docker (build context, -v sources) must be HOST paths.
#
#   host :8091  ->  container :8091
#   profile:    /root/claude-sandbox/persistent/nlm-profile  (auth.json cookies)
#   state:      <workspace host>/state                       (channel manifests, :ro)
set -euo pipefail

NAME=yt2nlm-web
PORT=8091

# Host paths (this repo's workspace + the persistent nlm profile) — used for -v,
# which the docker DAEMON (host) resolves.
HOST_WS="/root/claude-sandbox/workspaces/need collecting from customers comments"
HOST_PROFILE="/root/claude-sandbox/persistent/nlm-profile"
# Host Claude config (holds OAuth credentials for the merge step). Mounted
# READ-ONLY at /seed; entrypoint copies just .credentials.json out of it.
HOST_CLAUDE="/root/.claude"

# Build context is read by the docker CLI (inside the claude container), so it is
# a CONTAINER path. Override with BUILD_CTX=... if running from the host instead.
CTX="${BUILD_CTX:-/workspace/web}"

echo ">> build $NAME from $CTX"
docker build -t "$NAME" "$CTX"

echo ">> (re)start $NAME on :$PORT"
docker rm -f "$NAME" >/dev/null 2>&1 || true
docker run -d --name "$NAME" --restart unless-stopped \
  -p "$PORT:$PORT" \
  -v "$HOST_PROFILE:/home/node/.notebooklm-mcp-cli" \
  -v "$HOST_WS/state:/app/state:ro" \
  -v "$HOST_CLAUDE:/seed:ro" \
  "$NAME"

echo ">> up: http://localhost:$PORT/"
docker ps --filter "name=$NAME" --format '{{.Names}}  {{.Status}}  {{.Ports}}'
