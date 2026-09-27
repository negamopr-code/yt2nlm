#!/bin/sh
# Glottos method-research daemon — runs INSIDE awf-monitor-runner, kept alive by /app/runner/loop.sh
# (ensure_methods_daemon), so it survives crashes, reboots and session ends. Zero Claude tokens.
# Pains in SERIES (pains.json order): the first pain not yet researched is the active one; when every pain is
# researched, the oldest one is refreshed after refresh_days (new expert videos / comments pick themselves up).
# Per turn, strictly in series:  discover -> transcripts -> comments+engagement -> proof -> notebook sync
#                                -> strategy (one NLM query) -> publish (:8093 Research tab) -> heartbeat
# NotebookLM account work2 — turn-taking lock work2_account.lock for any future work2 daemon.
W=/app/state/glottos-methods
HB=/home/app/.notebooklm-mcp-cli/heartbeats
ACCTLOCK=/home/app/.notebooklm-mcp-cli/work2_account.lock
export NLM_PROFILE=work2
cd $W || exit 1
mkdir -p $HB
LOG=$W/daemon.log
say() { echo "$(date -u '+%F %H:%M') $*" >> $LOG; }
stage() { python3 -c "import common,sys;common.stage(sys.argv[1], sys.argv[2] or None)" "$1" "$2" >> $LOG 2>&1; python3 publish.py >> $LOG 2>&1; }

active_pain() { python3 - <<'PY'
import time, calendar
from common import load, PAINS
d = load(PAINS, {}); ps = d.get('pains', [])
for p in ps:
    if p.get('status') not in ('researched', 'paused'):
        print(p['id']); raise SystemExit
def ts(s):
    try: return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception: return 0
old = sorted((p for p in ps if p.get('status') == 'researched'), key=lambda p: ts(p.get('researched_at')))
if old and time.time() - ts(old[0].get('researched_at')) > d.get('refresh_days', 7) * 86400:
    print(old[0]['id'] + ' refresh')
PY
}

hb() {
  python3 - "$HB" <<'PY'
import sys, json, datetime
from common import load, pains, ledger, blocked, STAGE, NB
st = load(STAGE, {}); why = blocked()
for p in pains():
    led = ledger(p['id']); proof = load(f"/app/state/glottos-methods/{p['id']}/proof.json", {})
    c = {'videos': len(led), 'transcribed': sum(1 for v in led.values() if v['status'] == 'transcribed'),
         'pending': sum(1 for v in led.values() if v['status'] == 'pending'),
         'comments_done': sum(1 for v in led.values() if v.get('comments') == 'done'),
         'proof_comments': sum(v.get('proof_n', 0) for v in proof.get('videos', []))}
    state = 'blocked' if why else ('done' if p.get('status') == 'researched' else 'running')
    json.dump({'job': f"Glottos methods {p['id']} -> NLM", 'account': 'work2', 'state': state,
               'summary': (f'BLOCKED: {why} | ' if why else '') + f"{p['title']} — {p.get('status')}; now: {st.get('stage', '')}",
               'counts': c, 'needsUser': 'sign in work2 at http://localhost:8106/vnc.html' if why and 'signed out' in why else None,
               'kind': 'expert-pipeline', 'family': 'glottos-methods', 'channel': 'http://localhost:8093/ (Research tab)',
               'notebook': NB, 'updatedAt': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')},
              open(f"{sys.argv[1]}/glottos-methods-{p['id'].lower()}.json", 'w'), indent=1)
PY
}

acquire_account() {
  n=0
  while [ -f "$ACCTLOCK" ] && [ -n "$(find "$ACCTLOCK" -mmin -30 2>/dev/null)" ]; do
    [ "$(cat "$ACCTLOCK" 2>/dev/null)" = "glottos-methods" ] && return 0
    n=$((n+1)); [ "$n" -ge 20 ] && { say "acct: lock held >10 min, taking it"; break; }
    sleep 30
  done
  echo glottos-methods > "$ACCTLOCK"
}
release_account() { rm -f "$ACCTLOCK" 2>/dev/null; }

say "daemon start (pid $$)"
while true; do
  if [ -f $W/PAUSED ]; then stage "paused by user (remove $W/PAUSED to resume)" ""; hb; sleep 600; continue; fi
  A=$(active_pain); P=${A%% *}
  if [ -z "$P" ]; then stage "idle: every pain researched; next refresh when one is older than refresh_days" ""; hb; sleep 3600; continue; fi
  WORK=0
  # discovery: first time, or a refresh of a researched pain
  if [ "${A#* }" = "refresh" ] || [ ! -f "$W/$P/ledger.json" ]; then
    say "$P: discovery${A#$P}"
    timeout 3600 python3 discover.py "$P" >> $LOG 2>&1; WORK=1
  fi
  acquire_account
  TP=$(python3 -c "from common import ledger;print(sum(1 for v in ledger('$P').values() if v['status']=='pending'))")
  if [ "$TP" -gt 0 ]; then
    say "$P: transcripts pending $TP"
    timeout 5400 python3 harvest.py "$P" 15 >> $LOG 2>&1; WORK=1
    python3 publish.py >> $LOG 2>&1
  fi
  release_account
  CP=$(python3 -c "from common import ledger;print(sum(1 for v in ledger('$P').values() if v.get('comments')=='pending'))")
  if [ "$CP" -gt 0 ]; then
    say "$P: comments pending $CP"
    timeout 5400 python3 comments.py "$P" 20 >> $LOG 2>&1; WORK=1
  fi
  timeout 600 python3 proof.py "$P" >> $LOG 2>&1
  python3 publish.py >> $LOG 2>&1
  acquire_account
  timeout 3600 python3 sync.py "$P" >> $LOG 2>&1
  timeout 900 python3 synth.py "$P" >> $LOG 2>&1
  release_account
  if [ "$WORK" = 1 ]; then stage "between batches: next turn in 2 min" "$P"; else stage "waiting: next check in 30 min" "$P"; fi
  hb
  if [ "$WORK" = 1 ]; then sleep 120; else sleep 1800; fi
done
