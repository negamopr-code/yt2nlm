#!/bin/sh
# One worker per pain (started and kept alive by methods_daemon.sh). Uses ONLY this pain's NotebookLM account
# (pains.json "account"); pains run in parallel, one per account. Never ends: when the pain is caught up it writes /
# refreshes the strategy, then runs the next discovery round, until the market is saturated (then re-checks every
# refresh_days). Zero Claude tokens.
P=$1
W=/app/state/glottos-methods
cd $W || exit 1
export GM_PAIN=$P
ACC=$(python3 -c "import common;print(common.PROFILE)")
export NLM_PROFILE=$ACC
ACCTLOCK=/home/app/.notebooklm-mcp-cli/${ACC}_account.lock
ME=glottos-methods-$P
mkdir -p $W/$P
LOG=$W/$P/worker.log
say() { echo "$(date -u '+%F %H:%M') $*" >> $LOG; }
stage() { python3 -c "import common,sys;common.stage(sys.argv[1], '$P')" "$1" >> $LOG 2>&1; }
idle() { python3 -c "import common,sys;common.heartbeat('$P', sys.argv[1], sys.argv[2])" "$1" "$2" >> $LOG 2>&1; }
publish() { python3 publish.py >> $LOG 2>&1; }
# NotebookLM limits are babysat here (user standing rule): nlm_ok = the account has no back-off running.
# auth -> re-check every 10 min; limit -> 1/2/4/6 h. Non-NotebookLM work (comments, discovery) never waits for it.
nlm_ok() {
  python3 -c "
import common, subprocess, sys
w = common.nlm_wait()
if w: sys.exit(1)
import os
s = common.load(common._retry_path(), {})
if s.get('kind') == 'auth':        # back-off over: is the account really back? (free check, no quota)
    r = subprocess.run(['nlm', 'login', '--check', '-p', common.PROFILE], capture_output=True, text=True, timeout=120)
    if 'valid' not in (r.stdout + r.stderr).lower():
        common.nlm_backoff('auth', r.stdout + r.stderr); sys.exit(1)
    common.nlm_clear()
sys.exit(0)" >> $LOG 2>&1
}
nlm_why() { python3 -c "import common;w=common.nlm_wait() or {};print(w.get('reason','?'), '— auto-retry', w.get('retry_at','?')[11:16], 'UTC')"; }

# take turns with the other daemons on a SHARED account (default / work4 locks already exist); same wait rule as theirs
acquire() {
  n=0
  while [ -f "$ACCTLOCK" ] && [ -n "$(find "$ACCTLOCK" -mmin -30 2>/dev/null)" ]; do
    [ "$(cat "$ACCTLOCK" 2>/dev/null)" = "$ME" ] && return 0
    [ "$n" = 0 ] && stage "waiting for its turn on NotebookLM $ACC (held by $(cat "$ACCTLOCK" 2>/dev/null))"
    n=$((n+1)); [ "$n" -ge 20 ] && { say "acct: lock held >10 min, taking it"; break; }
    sleep 30
  done
  echo $ME > "$ACCTLOCK"
}
release() { [ "$(cat "$ACCTLOCK" 2>/dev/null)" = "$ME" ] && rm -f "$ACCTLOCK"; }

pending() { python3 -c "
from common import ledger
L=ledger('$P').values()
print(sum(1 for v in L if v['status']=='pending'), sum(1 for v in L if v.get('comments')=='pending'))"; }
round_due() { python3 -c "
import time, calendar
from common import pain, load, PAINS
p=pain('$P'); d=load(PAINS,{})
def ts(s):
    try: return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception: return 0
if not p.get('saturated_at'): print('scan')
elif time.time()-ts(p.get('discovered_at')) > d.get('refresh_days',7)*86400: print('refresh')"; }

say "worker start $P on $ACC (pid $$)"
while true; do
  if [ -f $W/PAUSED ] || [ -f $W/$P/PAUSED ]; then stage "paused (remove PAUSED to resume)"; idle done "paused"; sleep 600; continue; fi
  set -- $(pending); TP=$1; CP=$2
  if [ "$TP" = 0 ] && [ "$CP" = 0 ]; then
    # caught up: score -> notebook -> strategy, then look further into the market
    timeout 900 python3 proof.py $P >> $LOG 2>&1; publish
    NV=$(python3 -c "from common import ledger;print(len(ledger('$P')))")
    if [ "$NV" = 0 ]; then
      :                                   # brand-new pain: nothing to put in the notebook yet -> straight to discovery
    elif nlm_ok; then
      acquire
      timeout 3600 python3 sync.py $P >> $LOG 2>&1
      timeout 900 python3 synth.py $P >> $LOG 2>&1
      release; publish
    else
      stage "notebook + strategy waiting: $(nlm_why)"
    fi
    R=$(round_due)
    if [ -n "$R" ]; then
      say "$P: discovery round ($R)"
      timeout 7200 python3 discover.py $P >> $LOG 2>&1; publish
      sleep 60; continue
    fi
    stage "saturated: no new videos in the last rounds — next market re-check after refresh_days"
    idle done "saturated; strategy up to date"; publish
    sleep 3600; continue
  fi
  # work pending: comments (yt-dlp, no NotebookLM) run IN PARALLEL with the transcripts (NotebookLM)
  CPID=
  if [ "$CP" -gt 0 ]; then timeout 5400 python3 comments.py $P 25 >> $LOG 2>&1 & CPID=$!; fi
  DID=$CPID
  if [ "$TP" -gt 0 ]; then
    if nlm_ok; then
      acquire
      timeout 5400 python3 harvest.py $P 8 >> $LOG 2>&1
      release; DID=1
    else
      stage "transcripts waiting: $(nlm_why) — comments + discovery continue"
      idle blocked "transcripts waiting: $(nlm_why)"
      # nothing else to do meanwhile? keep scanning the market (discovery needs no NotebookLM)
      if [ "$CP" = 0 ] && [ -n "$(round_due)" ]; then timeout 7200 python3 discover.py $P >> $LOG 2>&1; DID=1; fi
    fi
  fi
  [ -n "$CPID" ] && wait $CPID
  timeout 900 python3 proof.py $P >> $LOG 2>&1; publish
  if [ -n "$DID" ]; then sleep 60; else sleep 600; fi
done
