#!/bin/sh
# Per-video Studio analytics (stayed vs swiped, avg view duration, traffic sources, search terms, geography) for every
# public video of the last 14 days, then copy deep/summary.json next to the :8093 studio as analytics/deep.json.
# 2026-10-25: capped at 60 min - it runs under tick.lock, a hang would block every production tick (user: loop must run by itself).
# Run from a container with the docker socket, under glottos-autopilot/tick.lock (loop.sh step 1a', daily).
set -eu
timeout 60m docker exec yt-studio /home/app/yt-profile/.venv/bin/python /opt/yt/video_analytics.py --recent ${1:-14} || { docker exec yt-studio pkill -f video_analytics.py; echo "deep: stopped after 60 min or failed"; exit 1; }
docker exec yt-studio cat /home/app/yt-profile/analytics/deep/summary.json | docker exec -i glottos-marketing sh -c "cat > /workspace/glottos-auto/out/analytics/deep.json"
echo "copied deep.json -> :8093/analytics/"
