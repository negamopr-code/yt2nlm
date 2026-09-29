#!/bin/sh
# Run the READ-ONLY channel snapshot, then copy it next to the :8093 studio (glottos-auto/out/analytics).
# Run from any container with the docker socket:  sh "/workspace/yt-studio/snapshot.sh"  (inside glottos-marketing) or via docker exec.
set -eu
docker exec yt-studio /home/app/yt-profile/.venv/bin/python /opt/yt/stats.py
F=$(docker exec yt-studio sh -c 'ls -t /home/app/yt-profile/analytics/snapshot-*.json | head -1')
docker exec yt-studio cat "$F" | docker exec -i glottos-marketing sh -c "mkdir -p /workspace/glottos-auto/out/analytics && cat > /workspace/glottos-auto/out/analytics/$(basename "$F") && cp /workspace/glottos-auto/out/analytics/$(basename "$F") /workspace/glottos-auto/out/analytics/latest.json"
echo "copied $(basename "$F") -> :8093/analytics/"
