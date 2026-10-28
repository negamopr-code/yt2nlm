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
# :8093 Videos tab status + Send-to-YouTube queue (user 09-30): own process, single instance (flock inside), no Claude
python3 $D/yt_sendq.py >> $D/yt_sendq.log 2>&1 &

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
# studio copy, upload, publish_log, monitor) runs on Sonnet.
# 2026-10-23 (user: "You spend way too much token in a short period of time"): the lab steps were missing from this map and fell to
# the Opus default - lab produce + analyze = $69 of $85 in 7 days. Now every lab step runs on Sonnet and the default is Sonnet; the
# English is still written/judged by Opus because these agents pin `model: opus` in their role files: language-editor, scenario-writer,
# longvideo-writer, article-writer, viewer-critic, comment-responder, format-strategist, lab-strategist (new hypotheses in analyze).
model_for() {
  case "${1##*: }" in
    scenario|script|decide|gate_text|gate_recording|yt_meta_gate|critic|reply_drafts) echo claude-opus-5-5 ;;
    *) echo claude-sonnet-5-5 ;;
  esac
}

while true; do
  rm -f $D/.worked $D/.failed
  (
    flock -n 9 || { echo "$(date -u +%FT%TZ) busy (lock held)" >> $LOG; exit 0; }
    sh /workspace/yt-studio/post_approved.sh 2>&1 | sed "s/^/$(date -u +%FT%TZ) replies: /" >> $LOG
    # Send controller WITHOUT Claude (user 2026-10-05): every pass check the whole "Send to YouTube" path, repair what is known,
    # report the rest to out/yt/send-watch.json (red banner on :8093). Prints only when something changed.
    python3 $D/send_watch.py 2>&1 | tail -1 | grep . | sed "s/^/$(date -u +%FT%TZ) send-watch: /" >> $LOG
    python3 $D/replies_due.py 2>&1 | grep . | sed "s/^/$(date -u +%FT%TZ) replies: /" >> $LOG      # unanswered viewer comments -> reply drafts due (no Claude)
    python3 $D/lab_board.py >/dev/null 2>&1 || echo "$(date -u +%FT%TZ) lab-board: FAILED" >> $LOG      # Lab tab scoreboard (lanes, CTR, Marcus answers), no Claude
    python3 $D/video_review.py >/dev/null 2>&1 || echo "$(date -u +%FT%TZ) video-review: FAILED" >> $LOG   # :8093 Video review table, one row per video since 09-28 + daily history (user 2026-10-17), no Claude
    if [ ! -f $D/.last_like ] || [ -n "$(find $D/.last_like -mmin +60)" ]; then          # hourly: like new comments (no-like list respected)
      docker exec yt-studio /home/app/yt-profile/.venv/bin/python /opt/yt/like.py 2>&1 | head -1 | sed "s/^/$(date -u +%FT%TZ) likes: /" >> $LOG
      touch $D/.last_like
    fi
    # GAP SWEEP WITHOUT Claude (user 2026-10-28: "you need to identify such gaps yourself by looking what is missing"): hourly, what
    # SHOULD exist and is missing (long/short stock, unapproved renders, failed/unsent sends, stalled tests, loops, daily jobs, NLM sign-ins).
    if [ ! -f $D/.last_gaps ] || [ -n "$(find $D/.last_gaps -mmin +60)" ]; then
      touch $D/.last_gaps
      ( python3 $D/gap_sweep.py 2>&1 | grep -v "^no gaps" | sed "s/^/$(date -u +%FT%TZ) gaps: /" >> $LOG ) &
    fi
    # Schedule watchdog WITHOUT Claude (user 2026-10-03): Shorts exactly 6 h apart, long videos 24 h apart; re-spaces the row
    # whenever a video was deleted, moved or added. Truth = YouTube Studio (every scheduled time is read back). Hourly.
    if [ ! -f $D/.last_keeper ] || [ -n "$(find $D/.last_keeper -mmin +60)" ]; then
      touch $D/.last_keeper
      sh /workspace/yt-studio/keeper.sh 2>&1 | tail -1 | sed "s/^/$(date -u +%FT%TZ) schedule: /" >> $LOG
    fi
    # Channel snapshot WITHOUT Claude (user 2026-09-29: "performance tab is not really reflecting actual views" - the only
    # snapshot was 2 days old: collection ran once a day inside a Claude tick and found Studio signed out). Every hour (2026-10-03: a newly public long video must be linked from its Shorts quickly) while
    # signed in; while signed out re-probe every 10 min so the first snapshot lands right after the user signs in.
    # analytics/status.json tells the :8093 Performance tab whether its numbers are current.
    if [ ! -f $D/.last_snap ] || [ -n "$(find $D/.last_snap -mmin +60)" ]; then
      if docker exec -u app -w /opt/yt yt-studio /home/app/yt-profile/.venv/bin/python /opt/yt/signed_in.py >/dev/null 2>&1; then
        SI=true; touch $D/.last_snap
        sh /workspace/yt-studio/snapshot.sh 2>&1 | tail -2 | sed "s/^/$(date -u +%FT%TZ) snapshot: /" >> $LOG
      else
        SI=false; touch -d "@$(( $(date +%s) - 10200 ))" $D/.last_snap                    # retry in ~10 min
        echo "$(date -u +%FT%TZ) snapshot: skipped, yt-studio NOT SIGNED IN" >> $LOG
      fi
      printf '{"checked_at":"%s","signed_in":%s}\n' "$(date -u +%FT%TZ)" $SI > /workspace/glottos-auto/out/analytics/status.json
    fi
    # Per-video deep analytics once a day (user 2026-10-02 Marcus deep-dive): stayed vs swiped, avg view duration, traffic
    # sources, search terms, geography for every public video of the last 14 days -> :8093 analytics/deep.json. No Claude.
    if [ "${SI:-}" != false ] && { [ ! -f $D/.last_deep ] || [ -n "$(find $D/.last_deep -mmin +1440)" ]; }; then
      touch $D/.last_deep
      sh /workspace/yt-studio/deep.sh 2>&1 | tail -1 | sed "s/^/$(date -u +%FT%TZ) deep: /" >> $LOG
    fi
    # Whole catalogue once a week (user 2026-10-05: "we have statistics, we need to use it"): thumbnail impressions, click-through rate,
    # sources and search terms of EVERY public long video (the 2019-21 library = 83 % of all views). Started detached: it takes
    # tick.lock itself in turns of 20 videos, so it begins when this pass ends and lets the send queue in between.
    if [ "${SI:-}" != false ] && ! pgrep -f deep_long.sh >/dev/null && { [ ! -f $D/.last_deep_long ] || [ -n "$(find $D/.last_deep_long -mmin +10080)" ]; }; then
      touch $D/.last_deep_long
      ( exec 9>&-; nohup sh /workspace/yt-studio/deep_long.sh >> $D/deep_long.log 2>&1 & )
    fi
    # End-screen boost WITHOUT Claude (user 2026-10-04; Marcus: "put it at the end screen of your old videos"): old ranking long
    # videos -> the new long video on the same word. Every 6 h, at most 2 videos a run.
    if [ "${SI:-}" != false ] && { [ ! -f $D/.last_endscreen ] || [ -n "$(find $D/.last_endscreen -mmin +360)" ]; }; then
      touch $D/.last_endscreen
      python3 $D/auto_endscreen.py 2>&1 | tail -1 | sed "s/^/$(date -u +%FT%TZ) endscreen: /" >> $LOG
    fi
    # uploads without Claude (user 2026-09-28): also while Claude is paused by its usage limit
    if python3 $D/auto_upload.py >> $LOG 2>&1; then touch $D/.worked; exit 0; fi
    # NotebookLM waiting/retries WITHOUT Claude (user 2026-09-29: "as cheap as possible from token perspective"):
    # starts/polls/downloads the nlm_job a tick left behind; due.py skips items that still have one.
    python3 $D/nlm_jobs.py 2>&1 | sed "s/^/$(date -u +%FT%TZ) nlm_jobs: /" >> $LOG
    # Lab numbers + rule verdicts, then the small brief every lab tick reads instead of the 0.8 MB lab.json (user 2026-10-23, tokens).
    # Inside the lock = no tick is editing lab.json now. No Claude.
    python3 $D/lab_verdicts.py 2>&1 | sed "s/^/$(date -u +%FT%TZ) lab-verdicts: /" >> $LOG
    python3 $D/lab_pareto.py >/dev/null 2>&1 || echo "$(date -u +%FT%TZ) lab-pareto: FAILED" >> $LOG     # 80/20 over all videos (user 2026-10-23)
    python3 $D/lab_search_targets.py >/dev/null 2>&1 || echo "$(date -u +%FT%TZ) lab-search: FAILED" >> $LOG   # Ahrefs keywords x our catalogue (user 2026-10-23)
    python3 $D/lab_params.py >/dev/null 2>&1 || echo "$(date -u +%FT%TZ) lab-params: FAILED" >> $LOG     # TRIZ parameter ledger + expert dossier (user 2026-10-23)
    python3 $D/lab_brief.py >/dev/null 2>&1 || echo "$(date -u +%FT%TZ) lab-brief: FAILED" >> $LOG
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
      # 2026-10-16: lean-home credentials MUST be a symlink to the live file - a failed token refresh (DNS outage 10-14) made the CLI
      # write a standalone copy there, which went stale when the main credentials rotated: every tick "OAuth session expired" for 2 days
      [ -L $LEAN/.claude/.credentials.json ] || { mv -f $LEAN/.claude/.credentials.json $LEAN/.claude/.credentials.json.stale-$(date +%s) 2>/dev/null; ln -s /home/node/.claude/.credentials.json $LEAN/.claude/.credentials.json; echo "$(date -u +%FT%TZ) lean-home credentials were a copy, not a link - re-linked" >> $LOG; }
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
  # catalogue A/B tests (user 2026-10-06): start the next tests in priority order until YouTube's daily limit; no Claude, takes the lock per video itself
  # tab "ahrefs traffic info" -> rolling PDF + Google Sheet table in NotebookLM (user 2026-10-06), no Claude; one step per pass, own lock
  /workspace/.venv/bin/python /workspace/glottos-autopilot/ahrefs_sync.py >> $LOG 2>&1 &
  # our whole test record -> the youtube-traffic expert notebook as ONE labelled source (user 2026-10-23: "experts ... do not necessarily
  # know the whole tests you did already"); max every 12 h, only when changed; waits for the drawnformula account lock; no Claude, no chat quota
  ( flock -n $D/.dossier.lock python3 $D/expert_dossier_sync.py 2>&1 | grep . | sed "s/^/$(date -u +%FT%TZ) dossier: /" >> $LOG ) &
  # Google Trends once per UTC day (user 2026-10-17), no Claude -> glottos-auto/out/lab/trends.json
  sh /workspace/glottos-autopilot/trends_daily.sh >> $LOG 2>&1 &
  ( cd /workspace/glottos-marketing && /workspace/.venv/bin/python /workspace/glottos-auto/out/abtests/catalog/nlm/worker.py --once >> /workspace/glottos-auto/out/abtests/catalog/nlm/worker.log 2>&1   # NLM-drawn thumbnails: one step per pass
    python3 /workspace/glottos-auto/out/abtests/catalog/daily.py 2>&1 | sed "s/^/$(date -u +%FT%TZ) abtests: /" >> $LOG ) &
  if [ -f $D/.worked ]; then sleep 30; else sleep 600; fi   # more work may be due right away; else wait (limits, failures)
done
