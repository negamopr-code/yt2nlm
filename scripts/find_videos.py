#!/usr/bin/env python3
"""Find popular YouTube videos in a niche, filtered by comment count.

Two phases (both via yt-dlp, no API key):
  1. flat search each query → cheap candidate list (id, title, channel, views).
  2. probe each candidate (metadata only, NO comment download) for comment_count
     and view_count, then keep those with >= --min-comments.

Output: a JSON list (--out) + a printed table, sorted by comment_count desc.
Feed the JSON to `yt2nlm videos --from-file` to ingest the survivors.

    python scripts/find_videos.py "how to learn a language" "comprehensible input" \
        --min-comments 1000 --per-query 20 --max-probe 60 --out state/_candidates.json
"""
from __future__ import annotations

import argparse
import json
import sys
import time

from yt_dlp import YoutubeDL


def flat_search(query: str, n: int) -> list[dict]:
    opts = {"quiet": True, "no_warnings": True,
            "extract_flat": "in_playlist", "skip_download": True}
    out = []
    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f"ytsearch{n}:{query}", download=False)
        for e in info.get("entries", []) or []:
            if not e or not e.get("id"):
                continue
            out.append({
                "video_id": e["id"],
                "title": e.get("title") or e["id"],
                "channel": e.get("channel") or e.get("uploader") or "",
                "view_count": e.get("view_count"),
                "url": e.get("url") or f"https://www.youtube.com/watch?v={e['id']}",
            })
    return out


def probe(video_id: str) -> dict:
    """Metadata only — comment_count without downloading comments."""
    opts = {"quiet": True, "no_warnings": True, "skip_download": True}
    with YoutubeDL(opts) as ydl:
        i = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}",
                             download=False)
    return {
        "video_id": i.get("id"),
        "title": i.get("title"),
        "channel": i.get("channel") or i.get("uploader") or "",
        "view_count": i.get("view_count"),
        "comment_count": i.get("comment_count"),
        "like_count": i.get("like_count"),
        "upload_date": i.get("upload_date"),
        "duration": i.get("duration"),
        "url": i.get("webpage_url") or f"https://www.youtube.com/watch?v={video_id}",
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("queries", nargs="+", help="search queries (niche terms)")
    ap.add_argument("--min-comments", type=int, default=1000)
    ap.add_argument("--min-views", type=int, default=0)
    ap.add_argument("--per-query", type=int, default=20)
    ap.add_argument("--max-probe", type=int, default=60,
                    help="cap on how many candidates to probe (by search views)")
    ap.add_argument("--pace", type=float, default=0.8)
    ap.add_argument("--out", default="")
    args = ap.parse_args(argv)

    # 1) gather candidates
    cands: dict[str, dict] = {}
    for q in args.queries:
        try:
            for e in flat_search(q, args.per_query):
                cands.setdefault(e["video_id"], e)
        except Exception as exc:  # one bad query shouldn't kill the run
            print(f"  ! search failed for {q!r}: {exc}", file=sys.stderr)
    print(f"candidates: {len(cands)} unique across {len(args.queries)} queries",
          file=sys.stderr)

    ordered = sorted(cands.values(),
                     key=lambda c: c.get("view_count") or 0, reverse=True)
    ordered = ordered[: args.max_probe]

    # 2) probe for comment_count
    keep = []
    for n, c in enumerate(ordered, 1):
        try:
            m = probe(c["video_id"])
        except Exception as exc:
            print(f"  [{n}/{len(ordered)}] probe failed {c['video_id']}: {exc}",
                  file=sys.stderr)
            continue
        cc = m.get("comment_count") or 0
        vc = m.get("view_count") or 0
        ok = cc >= args.min_comments and vc >= args.min_views
        flag = "KEEP" if ok else "skip"
        print(f"  [{n}/{len(ordered)}] {flag} cc={cc:>7} vc={vc:>10} "
              f"{(m.get('channel') or '')[:22]:22} {(m.get('title') or '')[:48]}",
              file=sys.stderr)
        if ok:
            keep.append(m)
        time.sleep(args.pace)

    keep.sort(key=lambda m: m.get("comment_count") or 0, reverse=True)

    print(f"\n=== {len(keep)} videos with >= {args.min_comments} comments ===")
    for m in keep:
        print(f"{(m.get('comment_count') or 0):>7} cmts | "
              f"{(m.get('view_count') or 0):>10} views | "
              f"{(m.get('channel') or '')[:24]:24} | {m.get('title')}")

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(keep, fh, ensure_ascii=False, indent=2)
        print(f"\nwrote {len(keep)} -> {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
