# yt2nlm-web — fan-out question UI across NotebookLM notebooks (+ optional merge).
#
# Two runtimes inside:
#   - python3  → the stdlib HTTP server + the `nlm` CLI (notebooklm-mcp-cli),
#                which queries NotebookLM over saved cookies (no browser).
#   - node + `claude` CLI → optional "merge" step: stitches the per-notebook
#                answers into one via `claude -p` headless (text-in/text-out, no
#                tools). Auth comes from CLAUDE_CONFIG_DIR at runtime (an OAuth
#                subscription token seeded by entrypoint, or ANTHROPIC_API_KEY).
FROM node:22-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 python3-venv ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# nlm in an isolated venv (PEP668-safe), exposed via NLM_BIN.
RUN python3 -m venv /opt/nlmvenv \
    && /opt/nlmvenv/bin/pip install --no-cache-dir notebooklm-mcp-cli==0.6.10

# claude CLI for the merge step.
RUN npm install -g @anthropic-ai/claude-code@2.1.158

ENV HOME=/home/node
ENV CLAUDE_CONFIG_DIR=/home/node/.claude
ENV NLM_BIN=/opt/nlmvenv/bin/nlm
ENV CLAUDE_BIN=claude
ENV CLAUDE_MERGE_MODEL=claude-haiku-4-5
ENV PORT=8091
ENV YT2NLM_STATE=/app/state

# /home/node is the `node` user's home (uid 1000); make config dir writable.
RUN mkdir -p /home/node/.claude && chown -R node:node /home/node

WORKDIR /app
COPY server.py /app/web/server.py
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

USER node
EXPOSE 8091
ENTRYPOINT ["/app/entrypoint.sh"]
