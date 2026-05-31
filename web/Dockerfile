# yt2nlm-web — fan-out question UI across NotebookLM notebooks.
# Pure-stdlib server; the only dependency is the `nlm` CLI (notebooklm-mcp-cli),
# which uses httpx+websocket over saved cookies (no browser needed at query time).
FROM python:3.12-slim

RUN pip install --no-cache-dir notebooklm-mcp-cli==0.6.10

# nlm reads its profile from $HOME/.notebooklm-mcp-cli — mirror the dev path so the
# existing auth.json (mounted at runtime) is found unchanged.
ENV HOME=/home/node
ENV NLM_BIN=nlm
ENV PORT=8091
ENV YT2NLM_STATE=/app/state

WORKDIR /app
COPY server.py /app/web/server.py

EXPOSE 8091
CMD ["python", "/app/web/server.py"]
