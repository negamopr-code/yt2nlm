#!/bin/sh
# glottos-autopilot (user 2026-09-27: produce and upload all episodes unattended, like the Zoe scanner).
# Every 10 min, holding ONE lock (strictly serial):
#   1. post replies the user approved on :8093 (mechanical, no Claude)
#   1a. channel snapshot every 3 h (no Claude) -> :8093 Performance
#   1b. nlm_jobs.py (no Claude): wait for / retry / download NotebookLM generations
#   1c. auto_upload.py (no Claude): upload a finished video as a PRIVATE draft + verify
#   2. due.py (no Claude): is an episode/channel step due?  -> only then run ONE headless Claude tick.
# Claude usage limit (2026-09-27: 20:00-22:30 UTC the loop retried every 30 s, ~300 empty ticks): the reset time in
# "You've hit your session limit · resets 10:30pm (UTC)" is parsed into .claude_limit_until and Claude ticks are
# skipped until then (replies/likes keep running). Any other failed tick backs off 10 min; 30 s only after success.
D=/workspace/glottos-autopilot; LOG=$D/log.txt; LOCK=$D/tick.lock; LIMIT=$D/.claude_limit_until
LEAN=/home/node/.claude/lean-home   # see the tick below
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

# Model per step (user 2026-09-28: "then do it" — cheaper model for routine work). Opus 5.5 only where quality is
# judged or English is written: scripts/scenarios, format decision, every English gate (text, recording, YouTube
# metadata), the viewer critic, reply drafts. Everything mechanical (NLM audio/visuals/video, render, polish cuts,
# studio copy, upload, publish_log, monitor) runs on Sonnet 5. Unknown/new steps default to Opus so nothing new
# is silently downgraded. Subagents inherit the tick's model (no glottos-* agent pins one).
model_for() {
  case "${1##*: }" in
    scenario|script|decide|gate_text|gate_recording|yt_meta_gate|critic|reply_drafts) echo claude-opus-5-5 ;;
    audio|visuals|nlm_video|render|polish|studio|upload|publish_log|monitor) echo claude-sonnet-5 ;;
    *) echo claude-opus-5-5 ;;
  esac
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
    # Channel snapshot WITHOUT Claude (user 2026-09-29: "performance tab is not really reflecting actual views" - the only
    # snapshot was 2 days old: collection ran once a day inside a Claude tick and found Studio signed out). Every 3 h while
    # signed in; while signed out re-probe every 10 min so the first snapshot lands right after the user signs in.
    # analytics/status.json tells the :8093 Performance tab whether its numbers are current.
    if [ ! -f $D/.last_snap ] || [ -n "$(find $D/.last_snap -mmin +180)" ]; then
      if docker exec -u app -w /opt/yt yt-studio /home/app/yt-profile/.venv/bin/python /opt/yt/signed_in.py >/dev/null 2>&1; then
        SI=true; touch $D/.last_snap
        sh /workspace/yt-studio/snapshot.sh 2>&1 | tail -2 | sed "s/^/$(date -u +%FT%TZ) snapshot: /" >> $LOG
      else
        SI=false; touch -d "@$(( $(date +%s) - 10200 ))" $D/.last_snap                    # retry in ~10 min
        echo "$(date -u +%FT%TZ) snapshot: skipped, yt-studio NOT SIGNED IN" >> $LOG
      fi
      printf '{"checked_at":"%s","signed_in":%s}\n' "$(date -u +%FT%TZ)" $SI > /workspace/glottos-auto/out/analytics/status.json
    fi
    # uploads without Claude (user 2026-09-28): also while Claude is paused by its usage limit
    if python3 $D/auto_upload.py >> $LOG 2>&1; then touch $D/.worked; exit 0; fi
    # NotebookLM waiting/retries WITHOUT Claude (user 2026-09-29: "as cheap as possible from token perspective"):
    # starts/polls/downloads the nlm_job a tick left behind; due.py skips items that still have one.
    python3 $D/nlm_jobs.py 2>&1 | sed "s/^/$(date -u +%FT%TZ) nlm_jobs: /" >> $LOG
    if [ -f $LIMIT ] && [ "$(date +%s)" -lt "$(cat $LIMIT)" ]; then exit 0; fi       # Claude limit: no tick until reset
    if DUE=$(python3 $D/due.py); then
      echo "$(date -u +%FT%TZ) tick: $DUE" >> $LOG
      PROMPT=$(sed "s|{{DUE}}|$DUE|" $D/tick-prompt.md)
      OUT=$(mktemp)
      MODEL=$(model_for "$DUE")
      echo "$(date -u +%FT%TZ) model: $MODEL" >> $LOG
      # Lean context (user 2026-09-29): HOME=lean-home has ONLY credentials + glottos-* agents + the 2 skills they use, so
      # no global CLAUDE.md / auto-memory / SessionStart hook / 40 unrelated skills+agents (measured 36.5k -> 22.9k input
      # tokens per call). --output-format json -> tick_cost.py logs tokens + cost per tick to costs.jsonl.
      START=$(date +%s)
      HOME=$LEAN timeout 3h claude -p "$PROMPT" --model "$MODEL" --permission-mode bypassPermissions --output-format json > $OUT 2>&1; RC=$?
      python3 $D/tick_cost.py $OUT "$DUE" "$MODEL" $RC $START >> $LOG 2>&1 || cat $OUT >> $LOG
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
