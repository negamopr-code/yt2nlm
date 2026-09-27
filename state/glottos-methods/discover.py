#!/usr/bin/env python3
"""Find the videos (and the EXPERTS) that teach how to overcome one pain. Zero NotebookLM, zero Claude.

1. yt-dlp YouTube search for every query in pains.json (flat, cheap).
2. Keep on-topic videos (topic_regex on the title) with real reach (MIN_VIEWS).
3. Experts = channels with >=2 on-topic hits or >= EXPERT_VIEWS summed; the top EXPERTS_MAX of them get their own
   channel listed and every on-topic video there is added too ("find out all experts on youtube").
4. Seed with an earlier study's videos (pain.reuse_dir) — already-transcribed ones are copied, not re-fetched.
Ledger rows: status pending|transcribed|unavailable|failed, comments pending|done|failed.

Usage: python3 discover.py P01
"""
import json
import os
import re
import shutil
import sys
import time

from common import load, save, pain, pains, save_pains, pdir, ledger, save_ledger, stage, now_iso

MIN_VIEWS = 20_000
MIN_DURATION = 20            # seconds; Shorts are kept (we publish Shorts), tagged is_short
EXPERT_VIEWS = 300_000
EXPERTS_MAX = 8
PER_QUERY = 40
MAX_VIDEOS = 90              # per pain (existing rows are always kept)
EXPERT_CHANNEL_SCAN = 400    # newest N uploads listed per expert channel
REFRESH_NEW = 15             # new videos admitted per refresh once the pain is at MAX_VIDEOS


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
            print(f'  yt-dlp {url[:60]}: {msg[:160]}', flush=True)
            if '429' in msg or 'Too Many' in msg:
                time.sleep(120 * (attempt + 1))
            else:
                return {}
    return {}


def row(e, found_by):
    vid = e.get('id')
    return {'id': vid, 'title': e.get('title') or '', 'channel': e.get('channel') or e.get('uploader') or '',
            'channel_id': e.get('channel_id') or '', 'views': e.get('view_count') or 0,
            'duration': e.get('duration') or 0, 'is_short': bool(e.get('duration')) and e['duration'] <= 60,
            'url': f'https://www.youtube.com/watch?v={vid}', 'found_by': found_by,
            'status': 'pending', 'comments': 'pending'}


def ok(e, rx, lang=None):
    return (e and e.get('id') and len(e['id']) == 11 and rx.search(e.get('title') or '')
            and (lang is None or lang.search(e.get('title') or ''))
            and (e.get('view_count') or 0) >= MIN_VIEWS and (e.get('duration') or 0) >= MIN_DURATION)


def main(pid):
    p = pain(pid)
    rx = re.compile(p['topic_regex'], re.I)
    lang = re.compile(p.get('language_regex') or '.', re.I)        # expert uploads: must also be about language
    os.makedirs(pdir(pid, 'transcripts'), exist_ok=True)
    cand = {}
    for i, q in enumerate(p['queries'], 1):
        stage(f'discovery: YouTube search {i}/{len(p["queries"])} "{q}"', pid)
        info = ydl(f'ytsearch{PER_QUERY}:{q}')
        for e in info.get('entries') or []:
            if ok(e, rx) and e['id'] not in cand:
                cand[e['id']] = row(e, f'search: {q}')
        time.sleep(4)
    # experts: channels that keep showing up / carry the reach
    by_ch = {}
    for r in cand.values():
        if r['channel_id']:
            c = by_ch.setdefault(r['channel_id'], {'channel': r['channel'], 'hits': 0, 'views': 0})
            c['hits'] += 1
            c['views'] += r['views']
    experts = sorted((dict(channel_id=k, **v) for k, v in by_ch.items() if v['hits'] >= 2 or v['views'] >= EXPERT_VIEWS),
                     key=lambda c: -c['views'])[:EXPERTS_MAX]
    for i, c in enumerate(experts, 1):
        stage(f'discovery: expert channel {i}/{len(experts)} {c["channel"]} — listing on-topic uploads', pid)
        for tab in ('videos', 'shorts'):
            info = ydl(f'https://www.youtube.com/channel/{c["channel_id"]}/{tab}', {'playlistend': EXPERT_CHANNEL_SCAN})
            n = 0
            for e in info.get('entries') or []:
                e.setdefault('channel', c['channel'])
                e.setdefault('channel_id', c['channel_id'])
                if tab == 'shorts' and not e.get('duration'):
                    e['duration'] = 59           # the shorts tab has no durations in flat mode
                if ok(e, rx, lang) and e['id'] not in cand:
                    cand[e['id']] = row(e, f'expert: {c["channel"]}')
                    n += 1
            c[f'added_{tab}'] = n
            time.sleep(4)
    # seed from an earlier study of the same pain (its transcripts are reused, zero NLM)
    reuse = p.get('reuse_dir')
    if reuse and os.path.isdir(reuse):
        old = load(os.path.join(reuse, 'videos.json'), {})
        for vid, m in old.items():
            if vid not in cand and m.get('title'):
                cand[vid] = {**row({'id': vid, 'title': m['title'], 'channel': m.get('channel'),
                                    'view_count': m.get('views') or m.get('search_views') or 0,
                                    'duration': m.get('duration_s') or 0}, 'earlier study (PROBLEM 01)')}
    led = ledger(pid)
    fresh = sorted((r for k, r in cand.items() if k not in led), key=lambda r: -r['views'])
    room = max(0, MAX_VIDEOS - len(led)) or (REFRESH_NEW if led else 0)   # refresh: best new uploads still get in
    for r in fresh[:room]:
        led[r['id']] = r
    # reuse transcripts already on disk
    reused = 0
    if reuse:
        for vid, r in led.items():
            src = os.path.join(reuse, 'transcripts', vid + '.txt')
            dst = pdir(pid, 'transcripts', vid + '.txt')
            if r['status'] == 'pending' and os.path.exists(src) and os.path.getsize(src) > 300:
                body = open(src).read()
                with open(dst, 'w') as f:
                    f.write(f"## {r['title']} | {r['channel']} | {r['views']} views | {r['url']}\n\n{body}\n")
                r.update(status='transcribed', chars=len(body), via='reused from earlier study')
                reused += 1
    save_ledger(pid, led)
    ps = pains()
    for x in ps:
        if x['id'] == pid:
            x['discovered_at'] = now_iso()
            x['experts'] = experts
            x['status'] = 'active'
    save_pains(ps)
    print(f'discover {pid}: candidates {len(cand)}, added {min(room, len(fresh))}, ledger {len(led)}, '
          f'experts {len(experts)}, reused transcripts {reused}', flush=True)


if __name__ == '__main__':
    main(sys.argv[1])
