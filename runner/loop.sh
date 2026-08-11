#!/bin/sh
# Continuous market-monitor loop. One cycle = one `yt2nlm monitor` run
# (collect → novelty → rotate → transcripts backfill). Exit codes:
#   0  → normal cycle, sleep INTERVAL (default 6 h)
#   75 → NotebookLM quota exhausted, back off QUOTA_SLEEP (default 4 h)
#   *  → error, short retry after ERROR_SLEEP (default 30 min)
# The run itself is lock-guarded and resume-first, so overlaps with manual
# runs are refused by the CLI, and every crash resumes cleanly.
CONFIG="${CONFIG:-state/monitor-awf.config.json}"
INTERVAL="${INTERVAL:-21600}"
QUOTA_SLEEP="${QUOTA_SLEEP:-14400}"
ERROR_SLEEP="${ERROR_SLEEP:-1800}"
MAX_CYCLE="${MAX_CYCLE:-10800}"   # watchdog: a cycle hung past 3 h gets killed
                                  # (resume-first: the next one continues)

cd /app || exit 1
echo "awf-monitor-runner: config=$CONFIG interval=${INTERVAL}s max_cycle=${MAX_CYCLE}s"

while true; do
  echo "=== cycle start $(date -u +%FT%TZ) ==="
  timeout -k 30 "$MAX_CYCLE" python -m yt2nlm monitor "$CONFIG"
  rc=$?
  case "$rc" in
    0)   echo "=== cycle ok, sleeping ${INTERVAL}s ==="; sleep "$INTERVAL" ;;
    75)  echo "=== quota pause, sleeping ${QUOTA_SLEEP}s ==="; sleep "$QUOTA_SLEEP" ;;
    124|137) echo "=== WATCHDOG: cycle exceeded ${MAX_CYCLE}s, killed; resuming in ${ERROR_SLEEP}s ==="; sleep "$ERROR_SLEEP" ;;
    *)   echo "=== cycle failed rc=$rc, retry in ${ERROR_SLEEP}s ==="; sleep "$ERROR_SLEEP" ;;
  esac
done
