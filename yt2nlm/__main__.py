"""CLI entry point:  python -m yt2nlm <channel> [options]"""

from __future__ import annotations

import argparse
import sys

from . import pipeline


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="yt2nlm",
        description="Загрузить видео канала YouTube + комментарии в NotebookLM "
                    "с авто-разбивкой по нескольким ноутбукам (матрица).",
    )
    p.add_argument("channel",
                   help="@handle, channel URL, UC… id, или URL плейлиста")
    p.add_argument("--title", dest="base_title", default=None,
                   help="Базовое имя ноутбука (default: '<channel> — comments')")
    p.add_argument("--ingest", choices=["video+comments", "comments", "video"],
                   default="video+comments",
                   help="Что грузить на видео (default: video+comments, как в видео)")
    p.add_argument("--comments-mode", choices=["top", "all"], default="top",
                   help="top — популярные первыми; all — все (до --max-comments)")
    p.add_argument("--max-comments", type=int, default=1000,
                   help="Потолок комментов на видео (default 1000)")
    p.add_argument("--no-replies", action="store_true",
                   help="Не грузить ответы на комментарии")
    p.add_argument("--limit", type=int, default=50,
                   help="Источников на ноутбук (free=50, plus=300)")
    p.add_argument("--max-videos", type=int, default=None,
                   help="Взять только первые N видео канала (для теста)")
    p.add_argument("--pace", type=float, default=2.0,
                   help="Пауза между видео, сек (анти-троттлинг)")
    p.add_argument("--dry-run", action="store_true",
                   help="Только перечислить и посчитать, без записи в NotebookLM")

    args = p.parse_args(argv)

    pipeline.run(
        args.channel,
        base_title=args.base_title,
        ingest=args.ingest,
        comments_mode=args.comments_mode,
        max_comments=args.max_comments,
        include_replies=not args.no_replies,
        limit=args.limit,
        max_videos=args.max_videos,
        pace_seconds=args.pace,
        dry_run=args.dry_run,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
