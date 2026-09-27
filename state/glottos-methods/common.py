"""Shared helpers for the Glottos method-research pipeline (glottos-methods).

User 2026-09-27: "go out and look for youtube videos which are helping to understand how this and that pain can be
overcome and you collect all methods where comments litterally confirming that this method is working and based on
it you define the strategy for the next piece of content ... find out all experts on youtubes and treat those video
with the method as we did, transcribing, removing link" + "measure the engagement of what is working meaning what is
watched with engagement and try to adapt to what we do".

User 2026-09-27 (2): "you do not need to stop at 90 videos, you continue to scan the market as long as you need ...
make a sub tab for this specific pain ... launch this research in another nlm account which is free and the same for
next pain as long as you have free nlm account".

Runs inside awf-monitor-runner. EACH PAIN has its own NotebookLM account + notebook (pains.json "account",
"notebook") and its own worker process (pain_worker.sh <ID>, kept alive by methods_daemon.sh); pains run in
PARALLEL, one per account. A pain without an account waits ("queued"). Per pain everything lives in <W>/<PAIN_ID>/.
Scripts learn their pain from argv; the worker also exports GM_PAIN so nlm() uses that pain's account.
"""
import json
import os
import subprocess
import time

W = os.path.dirname(os.path.abspath(__file__))
PAINS = os.path.join(W, 'pains.json')


def _pain_cfg(pid):
    try:
        with open(PAINS) as f:
            return next((p for p in json.load(f)['pains'] if p['id'] == pid), {})
    except Exception:
        return {}


PAIN = os.environ.get('GM_PAIN') or 'P01'
_CFG = _pain_cfg(PAIN)
PROFILE = _CFG.get('account') or 'work2'
NB = _CFG.get('notebook') or '35d9f7ee-e282-48f5-a937-29b42d4668ac'    # P01: "Glottos — Methods that work", work2
STAGE = os.path.join(W, f'stage-{PAIN}.json')
WSTAT = os.path.join(W, f'nlm_write_status-{PROFILE}.json')
OUR_ANALYTICS = '/app/glottos-auto/out/analytics/latest.json'      # performance monitor snapshot of @anotherword8913
PUBLISH = '/app/glottos-marketing/state/methods/research.json'     # read by glottos-files (:8093 Research tab)
OURS_PREFIX = ('methods transcripts', 'proof comments', 'strategy', 'engagement')   # our own documents in the notebook
GAP = 1.6
_last = [0.0]


def nlm(*args, timeout=900):
    wait = GAP - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    r = subprocess.run(['nlm', *args, '-p', PROFILE], capture_output=True, text=True, timeout=timeout)
    _last[0] = time.time()
    return r


def limit_kind(text):
    """'auth' | 'limit' | None for one NotebookLM CLI output."""
    low = (text or '').lower()
    if 'authentication' in low or 'nlm login' in low or 'signed out' in low:
        return 'auth'
    if any(k in low for k in ('quota', 'rate limit', 'rate-limit', 'resource exhausted', 'too many', '429',
                              'daily limit', 'limit reached', 'try again later')):
        return 'limit'
    return None


def record_write(ok, what, err=''):
    """Every NotebookLM write outcome. Consecutive failures -> honest 'blocked' heartbeat (EV lesson 2026-09-27);
    an auth/limit failure (or 3 unexplained in a row) -> nlm_backoff(): the account's NotebookLM work waits and
    retries BY ITSELF (user standing rule: babysit limits automatically, never wait for the user to notice)."""
    s = load(WSTAT, {})
    s['last'] = {'ok': ok, 'what': what, 'at': now_iso(), 'err': (err or '')[-300:]}
    s['consecutive_fail'] = 0 if ok else s.get('consecutive_fail', 0) + 1
    if ok:
        s['last_ok_at'] = now_iso()
    save(WSTAT, s)
    if ok:
        nlm_clear()
    else:
        k = limit_kind(err)
        if k or s['consecutive_fail'] >= 3:
            nlm_backoff(k or 'unexplained', err)


def _retry_path(profile=None):
    return os.path.join(W, f'nlm_retry-{profile or PROFILE}.json')


def nlm_wait(profile=None):
    """None when NotebookLM work may run on this account now, else {'reason', 'retry_at', ...}. Shared by every
    worker on the same account."""
    s = load(_retry_path(profile), {})
    return s if s.get('retry_ts', 0) > time.time() else None


def nlm_backoff(kind, err=''):
    """auth: re-check every 10 min (the keeper re-signs; we resume the moment it works).
    limit / unexplained: 1 h, 2 h, 4 h, then every 6 h until a write succeeds."""
    s = load(_retry_path(), {})
    n = s.get('n', 0) + 1
    delay = 600 if kind == 'auth' else min(6 * 3600, 3600 * 2 ** (n - 1))
    reason = {'auth': f'{PROFILE} signed out', 'limit': f'NotebookLM limit on {PROFILE}'}.get(kind, f'NotebookLM writes failing on {PROFILE}')
    save(_retry_path(), {'n': n, 'kind': kind, 'reason': reason, 'err': (err or '')[-200:], 'since': s.get('since') or now_iso(),
                         'retry_ts': time.time() + delay,
                         'retry_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(time.time() + delay))})


def nlm_clear():
    try:
        os.remove(_retry_path())
    except FileNotFoundError:
        pass


def blocked(profile=None):
    w = nlm_wait(profile)
    if w:
        return f"{w['reason']} — auto-retry {w['retry_at'][11:16]} UTC (attempt {w['n']})"
    s = load(os.path.join(W, f'nlm_write_status-{profile}.json') if profile else WSTAT, {})
    if s.get('consecutive_fail', 0) < 3:
        return None
    low = (s.get('last') or {}).get('err', '').lower()
    if 'authentication' in low or 'nlm login' in low:
        return f'{profile or PROFILE} signed out'
    if 'quota' in low or 'rate limit' in low or 'resource exhausted' in low:
        return 'NLM quota exhausted'
    return f"{s['consecutive_fail']} NLM writes failed in a row: {(s.get('last') or {}).get('err', '')[-120:]}"


def now_iso():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def load(path, default):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return default


def save(path, obj):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(obj, f, indent=1, ensure_ascii=False)
    os.replace(tmp, path)


def pains():
    return load(PAINS, {'pains': []})['pains']


def save_pains(ps):
    d = load(PAINS, {})
    d['pains'] = ps
    save(PAINS, d)


def pain(pid):
    return next(p for p in pains() if p['id'] == pid)


def pdir(pid, *parts):
    return os.path.join(W, pid, *parts)


def ledger(pid):
    return load(pdir(pid, 'ledger.json'), {})


def save_ledger(pid, led):
    save(pdir(pid, 'ledger.json'), led)


def stage(text, pid=None):
    """What this pain's worker is doing right now (shown live on its :8093 Research sub-tab)."""
    save(os.path.join(W, f'stage-{pid or PAIN}.json'), {'stage': text, 'pain': pid or PAIN, 'at': now_iso()})
    heartbeat(pid or PAIN, 'running', text)
    print(f'{now_iso()} stage: {text}', flush=True)


def source_list():
    r = nlm('source', 'list', NB)
    try:
        return json.loads(r.stdout)
    except Exception:
        return []


def engagement(v):
    """Engagement metrics from full yt-dlp metadata (filled by comments.py)."""
    views = v.get('views') or 0
    likes, ncom, subs = v.get('likes') or 0, v.get('yt_comments') or 0, v.get('subscribers') or 0
    out = {}
    if views:
        out['engagement_pct'] = round(100 * (likes + ncom) / views, 2)
        out['like_pct'] = round(100 * likes / views, 2)
    if views and subs:
        out['views_per_sub'] = round(views / subs, 2)
    ud = v.get('upload_date')
    if views and ud and len(ud) == 8:
        try:
            age = max(1, (time.time() - time.mktime(time.strptime(ud, '%Y%m%d'))) / 86400)
            out['views_per_day'] = round(views / age, 1)
            out['age_days'] = int(age)
        except Exception:
            pass
    return out


HB_DIR = '/home/app/.notebooklm-mcp-cli/heartbeats'


def heartbeat(pid, state, now_text=''):
    """Slot Manager (:8110) card for this pain — written at every stage, so its account shows as busy live."""
    try:
        p = pain(pid)
        led = ledger(pid)
        proof = load(pdir(pid, 'proof.json'), {})
        why = blocked(p.get('account'))
        c = {'videos': len(led), 'transcribed': sum(1 for v in led.values() if v['status'] == 'transcribed'),
             'pending': sum(1 for v in led.values() if v['status'] == 'pending'),
             'comments_done': sum(1 for v in led.values() if v.get('comments') == 'done'),
             'proof_comments': sum(v.get('proof_n', 0) for v in proof.get('videos', [])),
             'rounds': len(p.get('rounds', []))}
        save(os.path.join(HB_DIR, f'glottos-methods-{pid.lower()}.json'), {
            'job': f'Glottos methods {pid} -> NLM', 'account': p.get('account'), 'state': 'blocked' if why else state,
            'summary': (f'BLOCKED: {why} | ' if why else '') + f"{p['title']} — {now_text}",
            'counts': c, 'needsUser': f"sign in {p.get('account')} at http://localhost:8106/vnc.html" if why and 'signed out' in why else None,
            'kind': 'expert-pipeline', 'family': 'glottos-methods', 'channel': 'http://localhost:8093/ (Research tab)',
            'notebook': p.get('notebook'), 'updatedAt': now_iso()})
    except Exception as e:  # noqa: BLE001
        print('heartbeat failed:', e, flush=True)
