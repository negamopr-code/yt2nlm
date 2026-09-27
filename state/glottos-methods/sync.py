#!/usr/bin/env python3
"""Put one pain's corpus into the ONE notebook as few big documents (user rule: videos are never kept as sources —
transcripts go into a single living document; the video links were already deleted by harvest.py).
  "Methods transcripts — P01 vol N"      verbatim transcripts, rolled at ROLL chars
  "Proof comments + engagement — P01"    proof_doc.md from proof.py
Replace-by-title only when the content changed: add the new version first, then delete the old source id.
Usage: python3 sync.py P01
"""
import hashlib
import os
import sys
import tempfile

from common import nlm, source_list, record_write, ledger, pdir, load, save, stage, NB

ROLL = 1_500_000


def put(title, body, state):
    h = hashlib.sha1(body.encode()).hexdigest()
    have = {s.get('title'): s['id'] for s in source_list()}
    if state.get(title, {}).get('hash') == h and title in have:
        return 'unchanged'
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False) as f:
        f.write(body)
        tmp = f.name
    old = [s['id'] for s in source_list() if s.get('title') == title]
    r = nlm('source', 'add', NB, '--file', tmp, '--title', title, '--wait', '--wait-timeout', '900')
    os.unlink(tmp)
    out = r.stdout + r.stderr
    ok = 'ready' in out.lower() or 'Added source' in r.stdout          # same success test as the EV sync
    record_write(ok, f'add {title}', '' if ok else out)
    if not ok:
        return 'FAILED: ' + out[-160:]
    for sid in old:
        nlm('source', 'delete', sid, '--confirm')
    state[title] = {'hash': h, 'chars': len(body)}
    return f'synced ({len(body):,} chars)'


def main(pid):
    led = ledger(pid)
    sp = pdir(pid, 'sync_state.json')
    state = load(sp, {})
    order = sorted((v for v in led.values() if v['status'] == 'transcribed'), key=lambda v: -v['views'])
    vols, cur, size = [], [], 0
    for v in order:
        p = pdir(pid, 'transcripts', v['id'] + '.txt')
        if not os.path.exists(p):
            continue
        t = open(p).read()
        if cur and size + len(t) > ROLL:
            vols.append(cur)
            cur, size = [], 0
        cur.append(t)
        size += len(t)
    if cur:
        vols.append(cur)
    for n, vol in enumerate(vols, 1):
        title = f'Methods transcripts — {pid} vol {n}'
        stage(f'notebook sync: {title} ({len(vol)} transcripts)', pid)
        body = f'# {title}\n\nVerbatim transcripts of expert YouTube videos on pain {pid}, most-viewed first.\n\n' + '\n\n'.join(vol)
        print(title, put(title, body, state), flush=True)
        save(sp, state)
    doc = pdir(pid, 'proof_doc.md')
    if os.path.exists(doc):
        title = f'Proof comments + engagement — {pid}'
        stage(f'notebook sync: {title}', pid)
        print(title, put(title, open(doc).read()[:ROLL], state), flush=True)
        save(sp, state)


if __name__ == '__main__':
    main(sys.argv[1])
