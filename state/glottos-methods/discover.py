#!/usr/bin/env python3
"""One DISCOVERY ROUND for one pain: find more videos (and EXPERTS) that teach how to overcome it. Zero NLM/Claude.

No fixed cap (user 2026-09-27: "you do not need to stop at 90 videos, you continue to scan the market as long as you
need"). The worker calls a new round whenever the pain is caught up (no transcript/comment work pending):
  1. searches every query not searched yet (pains.json queries + auto queries), PER_QUERY results each;
  2. AUTO QUERIES: on-topic tags of the best-scoring videos become new searches (the market tells us its words);
  3. experts = channels with >=2 on-topic videos or >= EXPERT_VIEWS summed (whole ledger); the top EXPERTS_MAX get
     their uploads + Shorts listed, every on-topic one is added;
  4. round log in pains.json; SATURATED when SATURATION_ROUNDS rounds in a row add < SATURATION_NEW videos —
     then the worker only re-runs a round every refresh_days (new uploads, new experts).
On-topic = title matches topic_regex (+ language_regex for expert uploads), views >= MIN_VIEWS, >= MIN_DURATION s.
Ledger rows: status pending|transcribed|unavailable|failed, comments pending|done|failed.
Usage: python3 discover.py P01
"""
import os
import re
import sys
import time

from common import load, pain, pains, save_pains, pdir, ledger, save_ledger, stage, now_iso

MIN_VIEWS = 20_000
MIN_DURATION = 20            # seconds; Shorts are kept (we publish Shorts), tagged is_short
EXPERT_VIEWS = 300_000
EXPERTS_MAX = 20
PER_QUERY = 60
EXPERT_CHANNEL_SCAN = 400    # newest N uploads listed per expert channel
AUTO_QUERIES_PER_ROUND = 6
SATURATION_NEW = 5
SATURATION_ROUNDS = 2
SAFETY_CAP = 1500            # per pain; only a runaway guard, not a target


def ydl(url, extra=None):
    import yt_dlp
    opts = {'quiet': True, 'no_warnings': True, 'extract_flat': 'in_playlist', 'skip_download': True}
    opts.update(extra or {})
    for attempt in range(3):
        try:
            with yt_dlp.YoutubeDL(opts) as y:
                return y.extract_info(url, download=False) or {}
        except Exception as e:  # noqa: BLE001
            msg = str(e)
            if 'does not have a' not in msg:
                print(f'  yt-dlp {url[:60]}: {msg[:160]}', flush=True)
            if '429' in msg or 'Too Many' in msg:
                time.sleep(120 * (attempt + 1))
            else:
                return {}
    return {}


def row(e, found_by, rnd):
    vid = e.get('id')
    return {'id': vid, 'title': e.get('title') or '', 'channel': e.get('channel') or e.get('uploader') or '',
            'channel_id': e.get('channel_id') or '', 'views': e.get('view_count') or 0,
            'duration': e.get('duration') or 0, 'is_short': bool(e.get('duration')) and e['duration'] <= 60,
            'url': f'https://www.youtube.com/watch?v={vid}', 'found_by': found_by, 'round': rnd,
            'status': 'pending', 'comments': 'pending'}


def ok(e, rx, lang=None):
    return (e and e.get('id') and len(e['id']) == 11 and rx.search(e.get('title') or '')
            and (lang is None or lang.search(e.get('title') or ''))
            and (e.get('view_count') or 0) >= MIN_VIEWS and (e.get('duration') or 0) >= MIN_DURATION)


def auto_queries(p, led, rx):
    """On-topic tags of the best videos we have (works_score, else views) that we haven't searched yet."""
    proof = load(pdir(p['id'], 'proof.json'), {})
    score = {v['id']: v.get('works_score', 0) for v in proof.get('videos', [])}
    done = {q.lower() for q in p.get('queries', []) + p.get('queries_auto', [])}
    seen, out = set(), []
    for v in sorted(led.values(), key=lambda v: (-score.get(v['id'], -1), -v['views'])):
        for t in v.get('tags') or []:
            t = ' '.join(t.lower().split())
            if 8 <= len(t) <= 60 and rx.search(t) and t not in done and t not in seen:
                seen.add(t)
                out.append(t)
        if len(out) >= AUTO_QUERIES_PER_ROUND:
            break
    return out[:AUTO_QUERIES_PER_ROUND]


def main(pid):
    p = pain(pid)
    rx = re.compile(p['topic_regex'], re.I)
    lang = re.compile(p.get('language_regex') or '.', re.I)       # expert uploads: must also be about language
    os.makedirs(pdir(pid, 'transcripts'), exist_ok=True)
    led = ledger(pid)
    rounds = p.get('rounds', [])
    rnd = len(rounds) + 1
    refresh = bool(p.get('saturated_at'))
    searched = set(p.get('searched', []))
    if rnd == 1 and led:                        # corpus from before rounds existed: its queries were all searched
        searched |= set(p.get('queries', []))
    autoq = auto_queries(p, led, rx)
    queries = [q for q in dict.fromkeys(p.get('queries', []) + p.get('queries_auto', []) + autoq) if refresh or q not in searched]
    cand = {}
    for i, q in enumerate(queries, 1):
        stage(f'discovery round {rnd}: YouTube search {i}/{len(queries)} "{q}"', pid)
        for e in (ydl(f'ytsearch{PER_QUERY}:{q}').get('entries') or []):
            if ok(e, rx) and e['id'] not in led and e['id'] not in cand:
                cand[e['id']] = row(e, f'search: {q}', rnd)
        searched.add(q)
        time.sleep(4)
    # experts over the WHOLE corpus (ledger + this round)
    by_ch = {}
    for r in list(led.values()) + list(cand.values()):
        if r.get('channel_id'):
            c = by_ch.setdefault(r['channel_id'], {'channel': r['channel'], 'hits': 0, 'views': 0})
            c['hits'] += 1
            c['views'] += r['views'] or 0
    experts = sorted((dict(channel_id=k, **v) for k, v in by_ch.items() if v['hits'] >= 2 or v['views'] >= EXPERT_VIEWS),
                     key=lambda c: -c['views'])[:EXPERTS_MAX]
    listed = set(p.get('experts_listed', []) or ([e['channel_id'] for e in p.get('experts', [])] if rnd == 1 and led else []))
    for i, c in enumerate(experts, 1):
        if c['channel_id'] in listed and not refresh:
            continue
        stage(f'discovery round {rnd}: expert {i}/{len(experts)} {c["channel"]} — on-topic uploads', pid)
        for tab in ('videos', 'shorts'):
            info = ydl(f'https://www.youtube.com/channel/{c["channel_id"]}/{tab}', {'playlistend': EXPERT_CHANNEL_SCAN})
            for e in info.get('entries') or []:
                e.setdefault('channel', c['channel'])
                e.setdefault('channel_id', c['channel_id'])
                if tab == 'shorts' and not e.get('duration'):
                    e['duration'] = 59           # the shorts tab has no durations in flat mode
                if ok(e, rx, lang) and e['id'] not in led and e['id'] not in cand:
                    cand[e['id']] = row(e, f'expert: {c["channel"]}', rnd)
            time.sleep(4)
        listed.add(c['channel_id'])
    # seed from an earlier study of the same pain (its transcripts are reused, zero NLM)
    reuse = p.get('reuse_dir')
    if reuse and os.path.isdir(reuse):
        for vid, m in load(os.path.join(reuse, 'videos.json'), {}).items():
            if vid not in cand and vid not in led and m.get('title'):
                cand[vid] = row({'id': vid, 'title': m['title'], 'channel': m.get('channel'),
                                 'view_count': m.get('views') or m.get('search_views') or 0,
                                 'duration': m.get('duration_s') or 0}, 'earlier study (PROBLEM 01)', rnd)
    fresh = sorted(cand.values(), key=lambda r: -r['views'])[:max(0, SAFETY_CAP - len(led))]
    for r in fresh:
        led[r['id']] = r
    reused = 0
    if reuse:
        for vid, r in led.items():
            src = os.path.join(reuse, 'transcripts', vid + '.txt')
            if r['status'] == 'pending' and os.path.exists(src) and os.path.getsize(src) > 300:
                body = open(src).read()
                with open(pdir(pid, 'transcripts', vid + '.txt'), 'w') as f:
                    f.write(f"## {r['title']} | {r['channel']} | {r['views']} views | {r['url']}\n\n{body}\n")
                r.update(status='transcribed', chars=len(body), via='reused from earlier study')
                reused += 1
    save_ledger(pid, led)
    ps = pains()
    for x in ps:
        if x['id'] != pid:
            continue
        x['rounds'] = rounds + [{'round': rnd, 'at': now_iso(), 'queries': len(queries), 'auto_queries': autoq,
                                 'new_videos': len(fresh), 'experts': len(experts), 'total': len(led)}]
        x['queries_auto'] = x.get('queries_auto', []) + [q for q in autoq if q not in x.get('queries_auto', [])]
        x['searched'] = sorted(searched)
        x['experts_listed'] = sorted(listed)
        x['experts'] = experts
        x['discovered_at'] = now_iso()
        last = x['rounds'][-SATURATION_ROUNDS:]
        if len(last) == SATURATION_ROUNDS and all(r['new_videos'] < SATURATION_NEW for r in last):
            x.setdefault('saturated_at', now_iso())
        elif len(fresh) >= SATURATION_NEW:
            x.pop('saturated_at', None)
    save_pains(ps)
    print(f'discover {pid} round {rnd}: {len(queries)} queries ({len(autoq)} auto), experts {len(experts)}, '
          f'new {len(fresh)}, ledger {len(led)}, reused transcripts {reused}', flush=True)


if __name__ == '__main__':
    main(sys.argv[1])
