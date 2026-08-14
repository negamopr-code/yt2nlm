# awf-videogen — review queue + renderer + YouTube upload for "Another Word".
# Deps-only image (runner pattern); code bind-mounted rw at /app.
FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
        fonts-dejavu-core fonts-liberation ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
        edge-tts nltk pillow numpy yt-dlp \
        google-api-python-client google-auth-oauthlib \
        notebooklm-mcp-cli==0.6.10

RUN python -m nltk.downloader -d /usr/local/share/nltk_data wordnet omw-1.4

RUN useradd -m -u 1000 app
ENV HOME=/home/app NLM_BIN=/usr/local/bin/nlm \
    NLTK_DATA=/usr/local/share/nltk_data \
    FFMPEG=/app/glottos-auto/node_modules/ffmpeg-static/ffmpeg \
    PORT=8108 PYTHONUNBUFFERED=1
WORKDIR /app
USER app
ENTRYPOINT ["python", "-m", "videogen", "serve"]
