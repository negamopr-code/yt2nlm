#!/usr/bin/env python3
"""Compact snapshot for the :8093 Research tab -> glottos-marketing/state/methods/research.json (glottos-files reads it
at /state/methods/research.json). No commenter names, quotes only. Cheap; the daemon calls it after every step."""
import os

from common import pains, ledger, pdir, load, save, now_iso, blocked, STAGE, PUBLISH, W, NB, PROFILE, engagement

KEEP = ('id', 'title', 'channel', 'url', 'views', 'likes', 'yt_comments', 'engagement_pct', 'views_per_sub',
        'views_per_day', 'is_short', 'duration', 'works_score', 'taught', 'proof_n', 'proof_likes', 'counter_n',
        'proof_per_1k', 'status', 'comments', 'found_by')


def main():
    out_pains = []
    for p in pains():
        pid = p['id']
        led = ledger(pid)
        proof = load(pdir(pid, 'proof.json'), {})
        scored = {v['id']: v for v in proof.get('videos', [])}
        vids = []
        for v in led.values():
            s = scored.get(v['id'])
            base = {**v, **(engagement(v) if v.get('comments') == 'done' else {}), **(s or {})}   # likes unknown until comments.py ran
            row = {k: base.get(k) for k in KEEP}
            row['quotes'] = [{'text': q['text'][:300], 'likes': q['likes']} for q in (s or {}).get('proofs', [])[:3]]
            row['counter_quotes'] = [{'text': q['text'][:200], 'likes': q['likes']} for q in (s or {}).get('counters', [])[:1]]
            vids.append(row)
        vids.sort(key=lambda r: (-(r['works_score'] or -1), -(r['views'] or 0)))
        c = lambda f: sum(1 for v in led.values() if f(v))
        strat = pdir(pid, 'strategy.md')
        out_pains.append({
            'id': pid, 'title': p['title'], 'status': p.get('status'), 'discovered_at': p.get('discovered_at'),
            'researched_at': p.get('researched_at'), 'experts': p.get('experts', []),
            'counts': {'videos': len(led), 'transcribed': c(lambda v: v['status'] == 'transcribed'),
                       'transcripts_pending': c(lambda v: v['status'] == 'pending'),
                       'unavailable': c(lambda v: v['status'] in ('unavailable', 'failed')),
                       'comments_done': c(lambda v: v.get('comments') == 'done'),
                       'comments_pending': c(lambda v: v.get('comments') == 'pending'),
                       'proof': sum(v.get('proof_n', 0) for v in proof.get('videos', [])),
                       'counter': sum(v.get('counter_n', 0) for v in proof.get('videos', [])),
                       'shorts': c(lambda v: v.get('is_short'))},
            'methods': proof.get('methods', []), 'formats': proof.get('formats', {}),
            'title_patterns': proof.get('title_patterns', {}), 'ours': proof.get('ours', {}),
            'proof_at': proof.get('at'), 'videos': vids,
            'strategy_md': open(strat).read() if os.path.exists(strat) else None,
            'strategy_at': load(pdir(pid, 'synth_state.json'), {}).get('at')})
    log = os.path.join(W, 'daemon.log')
    tail = open(log, errors='replace').read().splitlines()[-40:] if os.path.exists(log) else []
    save(PUBLISH, {'at': now_iso(), 'notebook': NB, 'account': PROFILE, 'stage': load(STAGE, {}),
                   'blocked': blocked(), 'log': tail, 'pains': out_pains})


if __name__ == '__main__':
    main()
