"""Shared helpers for the Glottos method-research pipeline (glottos-methods).

User 2026-09-27: "go out and look for youtube videos which are helping to understand how this and that pain can be
overcome and you collect all methods where comments litterally confirming that this method is working and based on
it you define the strategy for the next piece of content ... find out all experts on youtubes and treat those video
with the method as we did, transcribing, removing link" + "measure the engagement of what is working meaning what is
watched with engagement and try to adapt to what we do".

Runs inside awf-monitor-runner. NotebookLM account work2 (the episodes own drawnformula), ONE notebook for all pains.
Pains are researched strictly in SERIES (pains.json order); per pain everything lives in <W>/<PAIN_ID>/.
"""
import json
import os
import subprocess
import time

W = os.path.dirname(os.path.abspath(__file__))
NB = '35d9f7ee-e282-48f5-a937-29b42d4668ac'      # "Glottos — Methods that work (expert YouTube corpus)", work2
PROFILE = 'work2'
PAINS = os.path.join(W, 'pains.json')
STAGE = os.path.join(W, 'stage.json')
WSTAT = os.path.join(W, 'nlm_write_status.json')
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


def record_write(ok, what, err=''):
    """Consecutive NLM write failures -> honest 'blocked' heartbeat (lesson from the EV pipeline, 2026-09-27)."""
    s = load(WSTAT, {})
    s['last'] = {'ok': ok, 'what': what, 'at': now_iso(), 'err': (err or '')[-300:]}
    s['consecutive_fail'] = 0 if ok else s.get('consecutive_fail', 0) + 1
    if ok:
        s['last_ok_at'] = now_iso()
    save(WSTAT, s)


def blocked():
    s = load(WSTAT, {})
    if s.get('consecutive_fail', 0) < 3:
        return None
    low = (s.get('last') or {}).get('err', '').lower()
    if 'authentication' in low or 'nlm login' in low:
        return 'work2 signed out'
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
    """What the pipeline is doing right now (shown live on the :8093 Research tab)."""
    save(STAGE, {'stage': text, 'pain': pid, 'at': now_iso()})
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
