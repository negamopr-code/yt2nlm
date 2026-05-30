"""CLI:
    python -m yt2nlm youtube '@handle'  [--max-videos N] [--ingest ...] ...
    python -m yt2nlm reddit  python      [--max-posts N] [--listing top] ...
    python -m yt2nlm reddit  'https://reddit.com/r/.../comments/.../'
"""

from __future__ import annotations

import argparse
import sys

from . import pipeline


def _add_common(p: argparse.ArgumentParser) -> None:
    p.add_argument("--limit", type=int, default=50,
                   help="Источников на ноутбук (free=50, plus=300)")
    p.add_argument("--pace", type=float, default=2.0,
                   help="Пауза между единицами, сек (анти-троттлинг)")
    p.add_argument("--dry-run", action="store_true",
                   help="Только перечислить и посчитать, без записи в NotebookLM")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="yt2nlm",
        description="Сбор комментариев (YouTube/Reddit) в NotebookLM с матрицей ноутбуков.")
    sub = p.add_subparsers(dest="cmd", required=True)

    yt = sub.add_parser("youtube", help="Видео канала + комментарии")
    yt.add_argument("channel", help="@handle, URL канала, UC… id или URL плейлиста")
    yt.add_argument("--ingest", choices=["video+comments", "comments", "video"],
                    default="video+comments")
    yt.add_argument("--comments-mode", choices=["top", "all"], default="top")
    yt.add_argument("--max-comments", type=int, default=1000)
    yt.add_argument("--no-replies", action="store_true")
    yt.add_argument("--max-videos", type=int, default=None,
                    help="Взять только первые N видео (последние по дате)")
    _add_common(yt)

    rd = sub.add_parser("reddit", help="Посты сабреддита + комментарии (praw)")
    rd.add_argument("source", help="сабреддит (python / r/python) или URL поста")
    rd.add_argument("--listing", choices=["top", "hot", "new", "rising"],
                    default="top")
    rd.add_argument("--time", dest="time_filter",
                    choices=["hour", "day", "week", "month", "year", "all"],
                    default="year", help="окно для --listing top")
    rd.add_argument("--max-posts", type=int, default=None)
    rd.add_argument("--max-comments", type=int, default=500,
                    help="Потолок комментов на пост")
    rd.add_argument("--comment-sort", choices=["top", "best", "new", "controversial"],
                    default="top")
    _add_common(rd)

    args = p.parse_args(argv)

    if args.cmd == "youtube":
        from .adapters.youtube import YouTubeAdapter
        adapter = YouTubeAdapter(
            args.channel, ingest=args.ingest, comments_mode=args.comments_mode,
            max_comments=args.max_comments, include_replies=not args.no_replies)
        max_units = args.max_videos
    else:
        from .adapters.reddit import RedditAdapter
        adapter = RedditAdapter(
            args.source, listing=args.listing, time_filter=args.time_filter,
            max_comments=args.max_comments, comment_sort=args.comment_sort)
        max_units = args.max_posts

    pipeline.run(adapter, limit=args.limit, max_units=max_units,
                 pace_seconds=args.pace, dry_run=args.dry_run)
    return 0


def _safe_main(argv: list[str] | None = None) -> int:
    try:
        return main(argv)
    except RuntimeError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\nпрервано (прогресс сохранён в manifest).", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(_safe_main())
