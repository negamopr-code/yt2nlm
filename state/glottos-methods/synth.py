#!/usr/bin/env python3
"""Turn one pain's evidence into the strategy for the next piece of content — ONE NotebookLM query (daily at most).
Input to the notebook: transcripts + "Proof comments + engagement" (already synced) + our own channel's numbers.
Output: <pain>/strategy.md, uploaded as "Strategy — P01" (replace-by-title), and published on the :8093 Research tab.
Gate: every video transcribed-or-given-up and comments done, and the evidence changed since the last strategy
(or 20 h passed). Marks the pain 'researched' -> the daemon moves on to the next pain (series).
Usage: python3 synth.py P01 [--force]
"""
import hashlib
import json
import os
import sys
import time

from common import nlm, pain, pains, save_pains, ledger, pdir, load, save, stage, now_iso, record_write, NB
from sync import put

Q = """You are the content strategist for "Words That Stick", a faceless YouTube Shorts series (English vocabulary,
learners ~B1) on the channel @anotherword8913. Pain being solved: "{title}".

Use ONLY the sources "Methods transcripts — {pid}" (what the experts teach) and "Proof comments + engagement — {pid}"
(first-person comments saying a method worked or didn't, plus each video's engagement numbers).

Answer in Markdown with these sections:
1. METHODS THAT ARE CONFIRMED — rank the methods by comment-confirmed evidence (proof comments and their likes,
   counter-evidence), name the expert videos that teach each one best, and quote 2 short learner comments per method
   (verbatim, no names). Separate "confirmed by learners" from "only claimed by the expert".
2. WHAT IS WATCHED WITH ENGAGEMENT — which formats, lengths, title patterns and hooks get the highest engagement %,
   views per subscriber and proof per 1k comments. Be concrete (numbers from the source).
3. HOW WE COMPARE — our own Words That Stick numbers so far: {ours}. What should we change to match what works?
4. STRATEGY FOR THE NEXT PIECE OF CONTENT — the next 3 episodes/pieces: for each give method, the exact promise/hook,
   format (Short / carousel / podcast ...), title idea, the proof quote to feature, and what NOT to claim.
5. GAPS — methods learners ask for or complain about that no expert covers well.
Do not invent numbers; if a figure is not in the sources, say so."""


def mark_researched(pid):
    ps = pains()
    for x in ps:
        if x['id'] == pid:
            x['status'] = 'researched'
            x['researched_at'] = now_iso()
    save_pains(ps)


def main(pid, force=False):
    p = pain(pid)
    led = ledger(pid)
    pending_t = sum(1 for v in led.values() if v['status'] == 'pending')
    pending_c = sum(1 for v in led.values() if v.get('comments') == 'pending')
    if (pending_t or pending_c) and not force:
        print(f'synth {pid}: waiting (transcripts pending {pending_t}, comments pending {pending_c})')
        return 1
    doc = pdir(pid, 'proof_doc.md')
    if not os.path.exists(doc):
        print(f'synth {pid}: no proof_doc yet')
        return 1
    h = hashlib.sha1(open(doc).read().encode()).hexdigest()
    st = load(pdir(pid, 'synth_state.json'), {})
    if not force and st.get('hash') == h and os.path.exists(pdir(pid, 'strategy.md')):
        print(f'synth {pid}: evidence unchanged since {st.get("at")}')
        mark_researched(pid)
        return 0
    if not force and st.get('ts') and time.time() - st['ts'] < 20 * 3600:
        print(f'synth {pid}: last strategy <20 h ago')
        mark_researched(pid)
        return 0
    proof = load(pdir(pid, 'proof.json'), {})
    ours = [{'title': x['title'], 'views': x.get('views'), 'comments': x.get('comments'), 'date': x.get('date')}
            for x in (proof.get('ours') or {}).get('videos', [])]
    stage('strategy: asking NotebookLM (one query) for confirmed methods + next-content strategy', pid)
    r = nlm('notebook', 'query', '--json', '-t', '600', NB, Q.format(title=p['title'], pid=pid, ours=json.dumps(ours) or 'none yet'), timeout=660)
    try:
        ans = (json.loads(r.stdout).get('value') or {}).get('answer') or ''
    except Exception:
        ans = ''
    if not ans:
        record_write(False, 'strategy query', (r.stdout + r.stderr)[-300:])
        print(f'synth {pid}: query failed: {(r.stdout + r.stderr)[-300:]}')
        return 2
    record_write(True, 'strategy query')
    body = f'# Strategy — {pid}: {p["title"]}\n\n_Generated {now_iso()} from {len(led)} expert videos._\n\n{ans}\n'
    with open(pdir(pid, 'strategy.md'), 'w') as f:
        f.write(body)
    sst = load(pdir(pid, 'sync_state.json'), {})
    print('strategy upload:', put(f'Strategy — {pid}', body, sst))
    save(pdir(pid, 'sync_state.json'), sst)
    save(pdir(pid, 'synth_state.json'), {'hash': h, 'at': now_iso(), 'ts': time.time()})
    mark_researched(pid)
    print(f'synth {pid}: strategy written ({len(ans)} chars), pain marked researched')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], '--force' in sys.argv))
