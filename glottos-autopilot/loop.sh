#!/bin/sh
# glottos-autopilot (user 2026-09-27: produce and upload all episodes unattended, like the Zoe scanner).
# Every 10 min, holding ONE lock (strictly serial):
#   1. post replies the user approved on :8093 (mechanical, no Claude)
#   2. due.py (no Claude): is an episode/channel step due?  -> only then run ONE headless Claude tick.
D=/workspace/glottos-autopilot; LOG=$D/log.txt; LOCK=$D/tick.lock
cd /workspace/glottos-marketing
[ -f "$HOME/.claude.json" ] || cp "$(ls -t $HOME/.claude/backups/.claude.json.backup.* 2>/dev/null | head -1)" "$HOME/.claude.json" 2>/dev/null   # lives outside the mounts
echo "$(date -u +%FT%TZ) autopilot loop start (pid $$)" >> $LOG
while true; do
  rm -f $D/.worked
  (
    flock -n 9 || { echo "$(date -u +%FT%TZ) busy (lock held)" >> $LOG; exit 0; }
    sh /workspace/yt-studio/post_approved.sh 2>&1 | sed "s/^/$(date -u +%FT%TZ) replies: /" >> $LOG
    if [ ! -f $D/.last_like ] || [ -n "$(find $D/.last_like -mmin +60)" ]; then          # hourly: like new comments (no-like list respected)
      docker exec yt-studio /home/app/yt-profile/.venv/bin/python /opt/yt/like.py 2>&1 | head -1 | sed "s/^/$(date -u +%FT%TZ) likes: /" >> $LOG
      touch $D/.last_like
    fi
    if DUE=$(python3 $D/due.py); then
      echo "$(date -u +%FT%TZ) tick: $DUE" >> $LOG
      PROMPT=$(sed "s|{{DUE}}|$DUE|" $D/tick-prompt.md)
      timeout 3h claude -p "$PROMPT" --permission-mode bypassPermissions >> $LOG 2>&1
      echo "$(date -u +%FT%TZ) tick end (exit $?)" >> $LOG
      touch $D/.worked
    fi
  ) 9>$LOCK
  if [ -f $D/.worked ]; then sleep 30; else sleep 600; fi   # more work may be due right away; else wait for limits
done
