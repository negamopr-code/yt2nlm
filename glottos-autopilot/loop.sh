#!/bin/sh
# glottos-autopilot (user 2026-09-27: produce and upload all episodes unattended, like the Zoe scanner).
# Every 10 min, holding ONE lock (strictly serial):
#   1. post replies the user approved on :8093 (mechanical, no Claude)
#   2. due.py (no Claude): is an episode/channel step due?  -> only then run ONE headless Claude tick.
# Claude usage limit (2026-09-27: 20:00-22:30 UTC the loop retried every 30 s, ~300 empty ticks): the reset time in
# "You've hit your session limit · resets 10:30pm (UTC)" is parsed into .claude_limit_until and Claude ticks are
# skipped until then (replies/likes keep running). Any other failed tick backs off 10 min; 30 s only after success.
D=/workspace/glottos-autopilot; LOG=$D/log.txt; LOCK=$D/tick.lock; LIMIT=$D/.claude_limit_until
cd /workspace/glottos-marketing
[ -f "$HOME/.claude.json" ] || cp "$(ls -t $HOME/.claude/backups/.claude.json.backup.* 2>/dev/null | head -1)" "$HOME/.claude.json" 2>/dev/null   # lives outside the mounts
echo "$(date -u +%FT%TZ) autopilot loop start (pid $$)" >> $LOG

limit_until() {   # epoch of the reset named in the tick output, else now + 30 min
  python3 - "$1" <<'PY'
import re, sys, time, calendar, datetime as dt
t = open(sys.argv[1], errors='replace').read()
now = dt.datetime.now(dt.timezone.utc)
m = re.search(r'resets\s+(?:(\w{3,9})\s+(\d{1,2}),?\s+)?(\d{1,2})(?::(\d{2}))?\s*(am|pm)', t, re.I)
if m:
    h = int(m.group(3)) % 12 + (12 if m.group(5).lower() == 'pm' else 0)
    mi = int(m.group(4) or 0)
    if m.group(1):
        try:
            mon = dt.datetime.strptime(m.group(1)[:3], '%b').month
            cand = now.replace(month=mon, day=int(m.group(2)), hour=h, minute=mi, second=0, microsecond=0)
        except Exception:
            cand = now + dt.timedelta(minutes=30)
    else:
        cand = now.replace(hour=h, minute=mi, second=0, microsecond=0)
        if cand <= now:
            cand += dt.timedelta(days=1)
else:
    cand = now + dt.timedelta(minutes=30)
print(int(cand.timestamp()) + 60)
PY
}

while true; do
  rm -f $D/.worked $D/.failed
  (
    flock -n 9 || { echo "$(date -u +%FT%TZ) busy (lock held)" >> $LOG; exit 0; }
    sh /workspace/yt-studio/post_approved.sh 2>&1 | sed "s/^/$(date -u +%FT%TZ) replies: /" >> $LOG
    if [ ! -f $D/.last_like ] || [ -n "$(find $D/.last_like -mmin +60)" ]; then          # hourly: like new comments (no-like list respected)
      docker exec yt-studio /home/app/yt-profile/.venv/bin/python /opt/yt/like.py 2>&1 | head -1 | sed "s/^/$(date -u +%FT%TZ) likes: /" >> $LOG
      touch $D/.last_like
    fi
    if [ -f $LIMIT ] && [ "$(date +%s)" -lt "$(cat $LIMIT)" ]; then exit 0; fi       # Claude limit: no tick until reset
    if DUE=$(python3 $D/due.py); then
      echo "$(date -u +%FT%TZ) tick: $DUE" >> $LOG
      PROMPT=$(sed "s|{{DUE}}|$DUE|" $D/tick-prompt.md)
      OUT=$(mktemp)
      timeout 3h claude -p "$PROMPT" --permission-mode bypassPermissions > $OUT 2>&1; RC=$?
      cat $OUT >> $LOG
      echo "$(date -u +%FT%TZ) tick end (exit $RC)" >> $LOG
      if grep -qiE "hit your (session|usage|weekly) limit|usage limit reached|limit (will )?reset" $OUT; then
        U=$(limit_until $OUT); echo $U > $LIMIT
        echo "$(date -u +%FT%TZ) Claude usage limit — no ticks until $(date -u -d @$U +%FT%TZ 2>/dev/null || echo $U)" >> $LOG
      elif [ "$RC" = 0 ]; then touch $D/.worked
      else touch $D/.failed; fi
      rm -f $OUT
    fi
  ) 9>$LOCK
  if [ -f $D/.worked ]; then sleep 30; else sleep 600; fi   # more work may be due right away; else wait (limits, failures)
done
