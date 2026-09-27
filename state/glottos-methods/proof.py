#!/usr/bin/env python3
"""Which methods do commenters CONFIRM work, and which videos are watched with engagement? Local, zero quota.

Per comment: PROOF = first-person testimonial ("I tried this and it worked", "since I started ... I remember"),
COUNTER = "didn't work for me" / "still forget". Author names are never copied out of comments/*.jsonl.
Per video: proof count/likes/rate + engagement (engagement %, views per subscriber, views per day) ->
works_score 0-100 = mean percentile (within the pain) of engagement %, views/sub, proof per 1k comments, proof likes.
Per method (pains.json taxonomy): videos teaching it (transcript keyword hits), proof comments (comment keywords,
else the video's main method), counter comments, reach.
Formats: Shorts vs long-form, and title patterns -> what gets watched ("adapt to what we do").
Writes <pain>/proof.json and <pain>/proof_doc.md (the "Proof comments + engagement" notebook source).
Usage: python3 proof.py P01
"""
import json
import os
import re
import statistics
import sys

from common import pain, ledger, pdir, save, stage, now_iso, engagement, load, OUR_ANALYTICS

POS = [re.compile(p) for p in (
    r"\b(it|this|that|these|this method|this technique|this tip|this trick|this system)('s| is| has| really| actually| definitely| totally| does| did)? ?(works?|worked|working|helped|helps)\b",
    r"\b(works?|worked|working) (for|on) me\b",
    r"\b(helped|helps|has helped|really helped) me\b",
    r"\bi('ve| have)? ?(been )?(tried|trying|using|used|doing|did|applied|applying|started|practic\w*) (this|it|that|these|anki|spaced|active recall|the method|the technique|your method)\b",
    r"\bgame ?changer\b",
    r"\bchanged (my|the way i)\b",
    r"\bnow i (can|remember|know|understand|speak|actually)\b",
    r"\bi (can )?finally (remember|speak|understand|retain)\b",
    r"\bi remember(ed)? (all|every|them|more|most|so much)\b",
    r"\bsince i (started|began)\b",
    r"\bpassed (my|the) \w* ?(exam|test|ielts|toefl|jlpt|hsk|dele|delf|n\d)\b",
    r"\bmy (vocabulary|vocab|english|spanish|french|german|japanese|korean|retention|memory|recall) (has )?(really )?(improved|grew|exploded|increased|skyrocketed)\b",
    r"\bcan confirm\b",
)]
FIRST = re.compile(r"\b(i|i'm|im|i've|ive|my|me)\b")
COUNTER = re.compile(r"\b(doesn'?t|didn'?t|does not|did not|never) (really )?(work|help)|\bnot working\b|\bwaste of time\b|\bstill forget\b|\bdoesn'?t stick\b")
# wishes / conditionals read like proof but mean the opposite ("i wished i could say it worked for me", 3.3k likes)
WISH = re.compile(r"\bwish(ed)? (i|it|this) (could|would|had|did|worked)|\bif only\b|\bwanted (it|this) to work\b|\bhope (it|this) works\b|\bwill (it|this) work\b")


def classify(text):
    t = text.lower()
    if len(t) < 12 or not FIRST.search(t):
        return None
    if WISH.search(t):
        return None                                   # neither proof nor counter
    if COUNTER.search(t):
        return 'counter'
    if t.rstrip().endswith('?') and len(t) < 90:
        return None
    return 'proof' if any(p.search(t) for p in POS) else None


def methods_in(text, tax):
    t = text.lower()
    return [m for m, kws in tax.items() if any(k in t for k in kws)]


def pct_rank(vals, x):
    vals = [v for v in vals if v is not None]
    if x is None or not vals:
        return None
    return 100 * sum(1 for v in vals if v <= x) / len(vals)


def med(xs):
    xs = [x for x in xs if x is not None]
    return round(statistics.median(xs), 2) if xs else None


TITLE_PATTERNS = {
    'number in title': r'\d',
    '"how to"': r'\bhow to\b',
    'question': r'\?',
    'negative / stop / never': r"\b(stop|never|don'?t|mistake|wrong|forget)\b",
    '"you / your"': r'\b(you|your)\b',
    'fast / easy / hack': r'\b(fast|quick|easy|easily|hack|trick|secret|cheat)\b',
    'personal ("I", "my")': r"\b(i|my|i'm|how i)\b",
}


def main(pid):
    p = pain(pid)
    tax = p['methods']
    led = ledger(pid)
    stage('proof: scoring comments, engagement and methods (local)', pid)
    vids = []
    for v in led.values():
        if v.get('comments') != 'done':
            continue
        v = {**v, **engagement(v)}
        tpath = pdir(pid, 'transcripts', v['id'] + '.txt')
        tr = open(tpath).read().lower() if os.path.exists(tpath) else ''
        hits = {m: sum(tr.count(k) for k in kws) for m, kws in tax.items()}
        taught = [m for m, h in sorted(hits.items(), key=lambda x: -x[1]) if h >= 3][:2]
        if not taught:
            taught = methods_in(v['title'], tax)[:1]
        proofs, counters, scanned = [], [], 0
        cpath = pdir(pid, 'comments', v['id'] + '.jsonl')
        if os.path.exists(cpath):
            for line in open(cpath):
                c = json.loads(line)
                if c.get('uploader'):
                    continue
                scanned += 1
                k = classify(c['text'])
                if not k:
                    continue
                ms = methods_in(c['text'], tax) or taught[:1]
                item = {'text': c['text'][:400], 'likes': c.get('likes') or 0, 'methods': ms}
                (proofs if k == 'proof' else counters).append(item)
        proofs.sort(key=lambda x: -x['likes'])
        counters.sort(key=lambda x: -x['likes'])
        v.update(taught=taught, method_hits=hits, scanned=scanned, proof_n=len(proofs),
                 proof_likes=sum(x['likes'] for x in proofs), counter_n=len(counters),
                 proof_per_1k=round(1000 * len(proofs) / scanned, 1) if scanned else 0,
                 proofs=proofs[:25], counters=counters[:5], transcribed=v.get('status') == 'transcribed')
        vids.append(v)
    cols = {k: [v.get(k) for v in vids] for k in ('engagement_pct', 'views_per_sub', 'proof_per_1k', 'proof_likes')}
    for v in vids:
        rs = [pct_rank(cols[k], v.get(k)) for k in cols]
        rs = [r for r in rs if r is not None]
        v['works_score'] = round(sum(rs) / len(rs)) if rs else 0
    vids.sort(key=lambda v: -v['works_score'])
    # methods
    meth = {}
    for m in tax:
        teach = [v for v in vids if m in v['taught']]
        pr = [(x, v) for v in vids for x in v['proofs'] if m in x['methods']]
        co = [(x, v) for v in vids for x in v['counters'] if m in x['methods']]
        meth[m] = {'method': m, 'videos': len(teach), 'views': sum(v['views'] for v in teach),
                   'median_engagement_pct': med([v.get('engagement_pct') for v in teach]),
                   'median_views_per_sub': med([v.get('views_per_sub') for v in teach]),
                   'proof_n': sum(1 for v in vids for x in v['proofs'] if m in x['methods']),
                   'proof_likes': sum(x['likes'] for x, _ in pr), 'counter_n': len(co),
                   'quotes': [{'text': x['text'][:280], 'likes': x['likes'], 'video': v['title'][:80]}
                              for x, v in sorted(pr, key=lambda t: -t[0]['likes'])[:6]],
                   'top_videos': [{'id': v['id'], 'title': v['title'], 'works_score': v['works_score']} for v in teach[:5]]}
    methods = sorted(meth.values(), key=lambda m: (-m['proof_n'], -m['proof_likes']))
    for m in methods:
        m['confirm_rate'] = round(m['proof_n'] / (m['proof_n'] + m['counter_n']), 2) if m['proof_n'] + m['counter_n'] else None
    # formats: what is watched with engagement
    def bucket(sel):
        return {'videos': len(sel), 'median_views': med([v['views'] for v in sel]),
                'median_views_per_day': med([v.get('views_per_day') for v in sel]),
                'median_views_per_sub': med([v.get('views_per_sub') for v in sel]),
                'median_engagement_pct': med([v.get('engagement_pct') for v in sel]),
                'median_proof_per_1k': med([v['proof_per_1k'] for v in sel])}
    formats = {'Shorts (<=60 s)': bucket([v for v in vids if v.get('is_short')]),
               'Mid (1-8 min)': bucket([v for v in vids if not v.get('is_short') and (v.get('duration') or 0) <= 480]),
               'Long (>8 min)': bucket([v for v in vids if (v.get('duration') or 0) > 480])}
    titles = {}
    for name, rx in TITLE_PATTERNS.items():
        r = re.compile(rx, re.I)
        yes = [v for v in vids if r.search(v['title'])]
        no = [v for v in vids if not r.search(v['title'])]
        titles[name] = {'with': bucket(yes), 'without': bucket(no)}
    ours = load(OUR_ANALYTICS, {})
    out = {'pain': pid, 'title': p['title'], 'at': now_iso(), 'videos': vids, 'methods': methods,
           'formats': formats, 'title_patterns': titles,
           'ours': {'at': ours.get('at'), 'videos': [x for x in ours.get('videos', []) if 'Words That Stick' in (x.get('title') or '')]}}
    save(pdir(pid, 'proof.json'), out)
    # notebook document (no commenter names)
    L = [f'# Proof comments + engagement — {pid}: {p["title"]}', '',
         f'Generated {now_iso()} by the glottos-methods pipeline. PROOF = first-person comment saying the method worked '
         f'for them; COUNTER = says it did not. Numbers are counted locally from the top comments of each video.', '',
         '## Methods ranked by comment-confirmed proof', '']
    for m in methods:
        L.append(f"- {m['method']}: {m['proof_n']} proof comments ({m['proof_likes']} likes), {m['counter_n']} counter; "
                 f"taught in {m['videos']} videos ({m['views']:,} views), median engagement {m['median_engagement_pct']}%")
    L += ['', '## What is watched with engagement (format)', '']
    for k, b in formats.items():
        L.append(f'- {k}: {b}')
    L += ['', '## Title patterns (median views per subscriber with vs without)', '']
    for k, b in titles.items():
        L.append(f"- {k}: with {b['with']['median_views_per_sub']} ({b['with']['videos']} videos) vs without "
                 f"{b['without']['median_views_per_sub']} ({b['without']['videos']})")
    L += ['', '## Videos (best "works score" first)', '']
    for v in vids:
        L.append(f"### {v['title']} — {v['channel']}")
        L.append(f"views {v['views']:,} | likes {v.get('likes', 0):,} | engagement {v.get('engagement_pct')}% | "
                 f"views/sub {v.get('views_per_sub')} | views/day {v.get('views_per_day')} | "
                 f"{'Short' if v.get('is_short') else str(v.get('duration')) + ' s'} | works score {v['works_score']} | "
                 f"teaches: {', '.join(v['taught']) or '?'} | proof {v['proof_n']} ({v['proof_per_1k']}/1k comments), counter {v['counter_n']}")
        for x in v['proofs'][:12]:
            L.append(f"  - PROOF ({x['likes']} likes): {x['text']}")
        for x in v['counters'][:3]:
            L.append(f"  - COUNTER ({x['likes']} likes): {x['text']}")
        L.append('')
    with open(pdir(pid, 'proof_doc.md'), 'w') as f:
        f.write('\n'.join(L))
    print(f'proof {pid}: {len(vids)} videos scored, proof comments {sum(v["proof_n"] for v in vids)}, '
          f'counter {sum(v["counter_n"] for v in vids)}; top method: {methods[0]["method"] if methods else "-"}', flush=True)


if __name__ == '__main__':
    main(sys.argv[1])
