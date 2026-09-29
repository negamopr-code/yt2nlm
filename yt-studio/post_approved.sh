#!/bin/sh
# Post every reply the USER approved on :8093 (Replies tab), one at a time, then mark it posted.
# Never touches drafts or rejected items: reply.py refuses anything whose status isn't "approved".
set -u
KEYS=$(docker exec glottos-files python -c "import json;q=json.load(open('/srv/replies/queue.json'));print(' '.join(x.get('type','reply')+':'+x['key'] for x in q['items'] if x.get('status')=='approved'))" 2>/dev/null)
[ -z "$KEYS" ] && { echo "no approved replies waiting"; exit 0; }
for tk in $KEYS; do
  t=${tk%%:*}; k=${tk#*:}; tool=reply.py; [ "$t" = spam ] && tool=spam.py        # spam: user confirmed -> Remove
  if docker exec yt-studio /home/app/yt-profile/.venv/bin/python /opt/yt/$tool "$k"; then
    docker exec glottos-files python -c "import urllib.request as u,json;print(u.urlopen(u.Request('http://127.0.0.1:8000/api/replies/posted',json.dumps({'key':'$k'}).encode(),{'Content-Type':'application/json'})).read().decode())"
  else echo "FAILED $k (left approved; retried next tick)"; fi
done
