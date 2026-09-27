#!/usr/bin/env python3
"""Comments + full engagement metadata for one pain's videos (yt-dlp, zero NotebookLM / Claude).
Top-sorted, capped (the proof lives in the top comments; a 5k-comment video doesn't need all of them).
Writes <pain>/comments/<id>.jsonl (raw, local only — commenter names never leave this dir) and fills the ledger row
with likes / comment count / subscribers / upload date -> engagement metrics.
Usage: python3 comments.py P01 [N]
"""
import json
import os
import random
import sys
import time

from common import ledger, save_ledger, pdir, stage, engagement

CAP = ['1500', '1500', '200', '5']      # max comments, max parents, max replies, max replies per thread


def fetch(vid):
    from yt_dlp import YoutubeDL
    opts = {'quiet': True, 'no_warnings': True, 'skip_download': True, 'getcomments': True,
            'extractor_args': {'youtube': {'comment_sort': ['top'], 'max_comments': CAP}}}
    with YoutubeDL(opts) as y:
        return y.extract_info(f'https://www.youtube.com/watch?v={vid}', download=False)


def main(pid, n):
    led = ledger(pid)
    todo = sorted((v for v in led.values() if v.get('comments') == 'pending'), key=lambda v: -v['views'])[:n]
    os.makedirs(pdir(pid, 'comments'), exist_ok=True)
    strikes = 0
    for i, v in enumerate(todo, 1):
        stage(f'comments + engagement: {i}/{len(todo)} of this batch — "{v["title"][:60]}"', pid)
        try:
            info = fetch(v['id'])
        except Exception as e:  # noqa: BLE001
            msg = str(e).splitlines()[0][:200]
            v['comment_attempts'] = v.get('comment_attempts', 0) + 1
            v['comments'] = 'failed' if v['comment_attempts'] >= 3 else 'pending'
            v['comments_why'] = msg
            save_ledger(pid, led)
            if '429' in msg or 'Too Many' in msg or 'Sign in' in msg:
                strikes += 1
                time.sleep(min(1800, 300 * strikes))
            continue
        strikes = 0
        cs = info.get('comments') or []
        with open(pdir(pid, 'comments', v['id'] + '.jsonl'), 'w') as f:
            for c in cs:
                f.write(json.dumps({'id': c.get('id'), 'parent': c.get('parent', 'root'), 'author': c.get('author'),
                                    'text': (c.get('text') or '').strip(), 'likes': c.get('like_count') or 0,
                                    'ts': c.get('timestamp'), 'uploader': bool(c.get('author_is_uploader'))},
                                   ensure_ascii=False) + '\n')
        v.update(comments='done', n_comments=len(cs), views=info.get('view_count') or v['views'],
                 likes=info.get('like_count') or 0, yt_comments=info.get('comment_count') or 0,
                 subscribers=info.get('channel_follower_count') or 0, upload_date=info.get('upload_date'),
                 duration=info.get('duration') or v.get('duration'), channel=info.get('channel') or v['channel'],
                 language=info.get('language'), tags=(info.get('tags') or [])[:15],
                 fetched_at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
        v['is_short'] = bool(v['duration']) and v['duration'] <= 60
        v.update(engagement(v))
        v.pop('comments_why', None)
        save_ledger(pid, led)
        time.sleep(random.uniform(3, 7))
    done = sum(1 for v in led.values() if v.get('comments') == 'done')
    print(f'comments {pid}: {done}/{len(led)} videos done', flush=True)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 20)
