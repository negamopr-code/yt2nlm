#!/usr/bin/env python3
"""Transcribe pending videos of one pain with the house method (same as SMB/EV/P01): add the YouTube link to the
notebook -> read `source content` (zero AI quota) -> save text -> DELETE the video source ("removing link").
Most-viewed first, sequential, polite gaps.  Usage: python3 harvest.py P01 [N]
"""
import os
import sys
import time

from common import nlm, source_list, record_write, limit_kind, nlm_wait, ledger, save_ledger, pdir, stage, NB, OURS_PREFIX


def ids():
    return {s['id']: s.get('title', '') for s in source_list()}


def content(sid):
    import json
    for cmd in (('source', 'content', sid, '--json'), ('source', 'get', sid)):
        r = nlm(*cmd)
        if r.returncode == 0 and r.stdout.strip():
            try:
                j = json.loads(r.stdout)
                return (j.get('value') or {}).get('content') or j.get('content') or ''
            except Exception:
                if len(r.stdout) > 200:
                    return r.stdout
    return ''


def ours(t):
    return (t or '').lower().startswith(OURS_PREFIX)


def one(v):
    before = ids()
    r = nlm('source', 'add', NB, '--youtube', v['url'], '--wait', '--wait-timeout', '600')
    out = (r.stdout + r.stderr).lower()
    fail = 'could not add' in out or 'authentication' in out or r.returncode != 0
    record_write(not fail, f'add video {v["id"]}', r.stdout + r.stderr if fail else '')
    if fail and limit_kind(out):                     # limit / signed out: the video stays PENDING, the batch stops,
        print(f'NotebookLM {limit_kind(out)} — batch stopped, auto-retry later', flush=True)   # the worker backs off
        sys.exit(3)
    new = {}
    for _ in range(6):
        new = {k: t for k, t in ids().items() if k not in before and not ours(t)}
        if new:
            break
        time.sleep(10)
    if not new:
        v.update(status='failed', why=('add refused: ' + out[-150:]) if fail else 'no new source appeared')
        return
    stub = [k for k, t in new.items() if (t or '').strip().rstrip('/').startswith('https://')]
    text = ''
    if not stub:
        sid = next(iter(new))
        for _ in range(15):
            text = content(sid)
            if len(text) > 300:
                break
            time.sleep(20)
    for k in new:                                            # remove the link: temporary video source(s) deleted
        nlm('source', 'delete', k, '--confirm')
    if len(text) > 300:
        with open(pdir(v['pain'], 'transcripts', v['id'] + '.txt'), 'w') as f:
            f.write(f"## {v['title']} | {v['channel']} | {v['views']} views | {v['url']}\n\n{text}\n")
        v.update(status='transcribed', chars=len(text))
        v.pop('why', None)
    else:
        v.update(status='unavailable', why='URL stub (not fetchable)' if stub else 'empty transcript')


def main(pid, n):
    led = ledger(pid)
    for v in led.values():                            # genuine failures get another go after 24 h (max 3 attempts)
        if v['status'] == 'failed' and v.get('attempts', 1) < 3 and time.time() - v.get('failed_ts', 0) > 86400:
            v['status'] = 'pending'
    todo = sorted((v for v in led.values() if v['status'] in ('pending',)), key=lambda v: -v['views'])[:n]
    os.makedirs(pdir(pid, 'transcripts'), exist_ok=True)
    for i, v in enumerate(todo, 1):
        stage(f'transcripts: {i}/{len(todo)} of this batch — "{v["title"][:60]}" ({v["channel"]})', pid)
        if nlm_wait():
            print('NotebookLM waiting (limit/sign-in) — batch stopped', flush=True)
            break
        v['pain'] = pid
        try:
            one(v)
        except SystemExit:
            save_ledger(pid, led)
            raise
        except Exception as e:  # noqa: BLE001
            v.update(status='failed', why=str(e)[:200])
        if v['status'] == 'failed':
            v['attempts'] = v.get('attempts', 0) + 1
            v['failed_ts'] = time.time()
        v.pop('pain', None)
        save_ledger(pid, led)
        time.sleep(5)
    c = {}
    for v in led.values():
        c[v['status']] = c.get(v['status'], 0) + 1
    print(f'harvest {pid}:', c, flush=True)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 15)
