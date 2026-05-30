#!/usr/bin/env bash
# Idempotent bootstrap for the yt2nlm project (container rootfs is ephemeral;
# /workspace persists via bind mount, so the venv lives here and survives).
set -euo pipefail
cd "$(dirname "$0")/.."

PY=python3
VENV=.venv

if [ ! -x "$VENV/bin/python" ]; then
  echo "[restore] creating venv"
  "$PY" -m venv "$VENV"
fi
echo "[restore] installing deps"
"$VENV/bin/pip" install --quiet --upgrade pip
"$VENV/bin/pip" install --quiet -r requirements.txt

# nlm (notebooklm-mcp-cli): we reuse the already-authenticated copy from the
# patent-wiki venv by default (NLM_BIN). Auth profile lives in
# ~/.notebooklm-mcp-cli (bind-mounted), shared across nlm installs.
NLM_BIN="${NLM_BIN:-/home/node/patent-wiki-analyzer/.venv/bin/nlm}"
if [ -x "$NLM_BIN" ]; then
  echo "[restore] nlm: $NLM_BIN ($("$NLM_BIN" --version 2>/dev/null | head -1))"
else
  echo "[restore] WARNING: nlm not found at $NLM_BIN."
  echo "          Install with: $VENV/bin/pip install notebooklm-mcp-cli"
  echo "          then: $VENV/bin/nlm login   (set NLM_BIN to it)"
fi

# AndyShaman/add_to_NotebookLM — Chrome extension for parsing comments in-browser
# (host side). Cloned here so it's available under the bind-mounted /workspace for
# chrome://extensions → Load unpacked.
EXT=extensions/add_to_NotebookLM
if [ -d "$EXT/.git" ]; then
  echo "[restore] extension present: $EXT ($(git -C "$EXT" describe --tags --always 2>/dev/null || echo cloned))"
else
  echo "[restore] cloning add_to_NotebookLM extension"
  git clone --depth 1 https://github.com/AndyShaman/add_to_NotebookLM.git "$EXT" || \
    echo "[restore] WARNING: extension clone failed (network?)"
fi

echo "[restore] done. Examples:"
echo "  $VENV/bin/python -m yt2nlm youtube '@SomeChannel' --max-videos 2 --dry-run"
echo "  REDDIT_CLIENT_ID=.. REDDIT_CLIENT_SECRET=.. \\"
echo "    $VENV/bin/python -m yt2nlm reddit personalfinance --max-posts 20 --dry-run"
echo "  (Reddit creds: create a 'script' app at https://www.reddit.com/prefs/apps)"
