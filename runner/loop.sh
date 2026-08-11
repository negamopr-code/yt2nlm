#!/bin/sh
# Continuous market-monitor loop. One cycle = one `yt2nlm monitor` run
# (collect → novelty → rotate → transcripts backfill). Exit codes:
#   0  → normal cycle, sleep INTERVAL (default 6 h)
#   75 → NotebookLM quota exhausted, back off QUOTA_SLEEP (default 4 h)
#   *  → error, short retry after ERROR_SLEEP (default 30 min)
# The run itself is lock-guarded and resume-first, so overlaps with manual
# runs are refused by the CLI, and every crash resumes cleanly.
# User doctrine (2026-08-11): run CONTINUOUSLY — cycle follows cycle with only
# a short breather; the ONLY real stop is NLM quota exhaustion (rc 75).
CONFIG="${CONFIG:-state/monitor-awf.config.json}"
INTERVAL="${INTERVAL:-60}"
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
    0)
      # adaptive breather: an EMPTY cycle (no batch) means the well is
      # momentarily dry — don't hammer YouTube enumeration every minute
      if grep -q '"batch_id": ""' reports/monitor-awf/progress.json 2>/dev/null; then
        echo "=== cycle ok (empty), sleeping ${EMPTY_INTERVAL:-900}s ==="
        sleep "${EMPTY_INTERVAL:-900}"
      else
        echo "=== cycle ok, sleeping ${INTERVAL}s ==="
        sleep "$INTERVAL"
      fi ;;
    75)  echo "=== quota pause, sleeping ${QUOTA_SLEEP}s ==="; sleep "$QUOTA_SLEEP" ;;
    124|137) echo "=== WATCHDOG: cycle exceeded ${MAX_CYCLE}s, killed; resuming in ${ERROR_SLEEP}s ==="; sleep "$ERROR_SLEEP" ;;
    *)   echo "=== cycle failed rc=$rc, retry in ${ERROR_SLEEP}s ==="; sleep "$ERROR_SLEEP" ;;
  esac
done
