# awf-monitor-runner — always-on loop for the market monitor.
# The CODE is bind-mounted at /app (the workspace), so `git pull`/edits take
# effect on the next cycle without a rebuild. This image only carries deps.
FROM python:3.12-slim

RUN pip install --no-cache-dir \
        yt-dlp \
        notebooklm-mcp-cli==0.6.10 \
        google-play-scraper \
        pytrends

# uid 1000 = node in the dev container = owner of the bind-mounted workspace.
RUN useradd -m -u 1000 app
ENV HOME=/home/app
ENV NLM_BIN=/usr/local/bin/nlm
ENV PYTHONUNBUFFERED=1

WORKDIR /app
USER app
ENTRYPOINT ["/bin/sh", "/app/runner/loop.sh"]
