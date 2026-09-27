#!/bin/sh
# (Re)create the glottos marketing-strategy chat at http://localhost:8097/
# Headless `claude -p` agent (server.mjs) — needs the host Claude login (/root/.claude).
# 2026-09-27: + NotebookLM access — the shared host cookie store (kept signed in and
# renewed by nlm-keeper + nlm-slot-manager) and profile drawnformula, which holds the
# "Glottos — go-to-market" notebook 8306c0a9-1418-41e2-a988-1c0459eafc89.
# nlm CLI lives in glottos-marketing/.nlmvenv (gitignored; recreate with
#   python3 -m venv .nlmvenv && .nlmvenv/bin/pip install notebooklm-mcp-cli==0.7.2).
set -eu
WS='/root/claude-sandbox/workspaces/need collecting from customers comments'
docker rm -f glottos-marketing 2>/dev/null || true
docker run -d --name glottos-marketing --restart unless-stopped \
  -p 8097:8097 --user node -w /workspace/glottos-marketing \
  -v /root/.claude:/home/node/.claude \
  -v "$WS":/workspace \
  -v /root/claude-sandbox/persistent/nlm-profile:/home/node/.notebooklm-mcp-cli \
  -e CLAUDE_CWD=/workspace/glottos-marketing -e PORT=8097 \
  -e NLM_PROFILE=drawnformula \
  -e GLOTTOS_NLM_NOTEBOOK=8306c0a9-1418-41e2-a988-1c0459eafc89 \
  --entrypoint node claude-sandbox-claude /workspace/glottos-marketing/server.mjs
echo "→ http://localhost:8097/"
