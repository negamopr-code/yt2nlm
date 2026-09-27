#!/bin/sh
# Glottos method-research SUPERVISOR — runs inside awf-monitor-runner, kept alive by /app/runner/loop.sh
# (ensure_methods_daemon). Every minute: one pain_worker.sh per pain that has a NotebookLM account (pains run in
# PARALLEL, one per account — user 2026-09-27); a pain without an account waits as "queued". Zero Claude tokens.
W=/app/state/glottos-methods
cd $W || exit 1
LOG=$W/daemon.log
say() { echo "$(date -u '+%F %H:%M') $*" >> $LOG; }
say "supervisor start (pid $$)"
while true; do
  for P in $(python3 -c "from common import pains;print(' '.join(p['id'] for p in pains() if p.get('account') and p.get('status')!='paused'))"); do
    alive=
    for d in /proc/[0-9]*; do
      case "$(tr '\0' ' ' < "$d/cmdline" 2>/dev/null)" in
        *"pain_worker.sh $P "*) alive=1; break ;;
      esac
    done
    if [ -z "$alive" ]; then
      mkdir -p $W/$P
      say "starting worker $P"
      nohup sh $W/pain_worker.sh $P >> $W/$P/worker-boot.log 2>&1 &
    fi
  done
  for P in $(python3 -c "from common import pains;print(' '.join(p['id'] for p in pains() if not p.get('account')))"); do
    python3 -c "import common;common.stage('queued: waiting for a free NotebookLM account (sign one in at :8106, then add it in pains.json)', '$P')" >> $LOG 2>&1
  done
  python3 publish.py >> $LOG 2>&1
  sleep 60
done
