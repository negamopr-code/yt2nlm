"""CLI:
    python -m yt2nlm youtube '@handle'  [--max-videos N] [--ingest ...] ...
    python -m yt2nlm reddit  python      [--max-posts N] [--listing top] ...
    python -m yt2nlm reddit  'https://reddit.com/r/.../comments/.../'
    python -m yt2nlm videos  --from-file cands.json --title 'Niche name' [...]
    python -m yt2nlm videos  VIDEO_ID_OR_URL ...   --title 'Niche name'
"""

from __future__ import annotations

import argparse
import json
import re
import sys

from . import pipeline


def _slug(s: str) -> str:
    s = re.sub(r"[^\w]+", "-", s.lower(), flags=re.UNICODE).strip("-")
    return s or "curated"


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

    vd = sub.add_parser("videos",
                        help="Курируемый список видео (из файла или аргументов)")
    vd.add_argument("ids", nargs="*",
                    help="video id/URL (если без --from-file)")
    vd.add_argument("--from-file",
                    help="JSON-список [{video_id,title,url}] (вывод find_videos.py)")
    vd.add_argument("--title", required=True,
                    help="Базовое имя ноутбук-группы (матрица добавит _part N)")
    vd.add_argument("--key", default=None,
                    help="Ключ манифеста state/<key>.json (по умолчанию слаг из --title)")
    vd.add_argument("--ingest", choices=["video+comments", "comments", "video"],
                    default="video+comments")
    vd.add_argument("--comments-mode", choices=["top", "all"], default="top")
    vd.add_argument("--max-comments", type=int, default=1000)
    vd.add_argument("--no-replies", action="store_true")
    vd.add_argument("--max-videos", type=int, default=None,
                    help="Взять только первые N из списка")
    _add_common(vd)

    ur = sub.add_parser("urls",
                        help="Курируемый список веб-страниц (URL-источники)")
    ur.add_argument("urls", nargs="*", help="URL (если без --from-file)")
    ur.add_argument("--from-file",
                    help="JSON-список [{url,title}] или [url, ...]")
    ur.add_argument("--title", required=True,
                    help="Базовое имя ноутбук-группы")
    ur.add_argument("--key", default=None,
                    help="Ключ манифеста (по умолчанию слаг из --title)")
    ur.add_argument("--max-urls", type=int, default=None)
    _add_common(ur)

    mo = sub.add_parser("monitor",
                        help="Рыночный монитор: одна ротируемая NotebookLM-тетрадь "
                             "+ novelty-дайджест + scoreboard")
    mo.add_argument("config", help="путь к state/<key>.config.json")
    mo.add_argument("--init", action="store_true",
                    help="создать ноутбук + Frame-источник")
    mo.add_argument("--dry-run", action="store_true",
                    help="перечислить цели и посчитать новые комменты, ничего не писать")
    mo.add_argument("--no-query", action="store_true",
                    help="только собрать и загрузить батч, без novelty-запроса")
    mo.add_argument("--max-videos", type=int, default=None)
    mo.add_argument("--backfill-transcripts", type=int, default=None,
                    metavar="N", help="только собрать N транскриптов "
                    "(ротация через ноутбук, бесплатно)")
    mo.add_argument("--proposals", action="store_true",
                    help="сгенерировать PROPOSALS.md из топ-тем (1 Gemini-запрос)")
    mo.add_argument("--trends", action="store_true",
                    help="подтянуть Google Trends для ключевых тем (pytrends)")

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

    if args.cmd == "monitor":
        from . import monitor
        return monitor.cmd(args)

    if args.cmd == "youtube":
        from .adapters.youtube import YouTubeAdapter
        adapter = YouTubeAdapter(
            args.channel, ingest=args.ingest, comments_mode=args.comments_mode,
            max_comments=args.max_comments, include_replies=not args.no_replies)
        max_units = args.max_videos
    elif args.cmd == "videos":
        from .adapters.curated import CuratedYouTubeAdapter
        if args.from_file:
            with open(args.from_file, encoding="utf-8") as fh:
                videos = json.load(fh)
        else:
            videos = [{"video_id": x.rsplit("/", 1)[-1].split("v=")[-1][:11],
                       "url": x if x.startswith("http") else None,
                       "title": x} for x in args.ids]
        if not videos:
            p.error("videos: нужен --from-file или список id/URL")
        adapter = CuratedYouTubeAdapter(
            videos, title=args.title, key=args.key or _slug(args.title),
            ingest=args.ingest, comments_mode=args.comments_mode,
            max_comments=args.max_comments, include_replies=not args.no_replies)
        max_units = args.max_videos
    elif args.cmd == "urls":
        from .adapters.urls import UrlAdapter
        if args.from_file:
            with open(args.from_file, encoding="utf-8") as fh:
                items = json.load(fh)
        else:
            items = list(args.urls)
        if not items:
            p.error("urls: нужен --from-file или список URL")
        adapter = UrlAdapter(items, title=args.title,
                             key=args.key or _slug(args.title))
        max_units = args.max_urls
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
