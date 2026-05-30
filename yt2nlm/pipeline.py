"""Orchestration: channel -> per-video (video source + comments source) ->
notebook matrix, with a resumable manifest.
"""

from __future__ import annotations

import time

from . import comments_fmt, nlm, youtube
from .matrix import NotebookMatrix
from .state import Manifest, VideoRecord


def _unit_size(ingest: str) -> int:
    return 2 if ingest == "video+comments" else 1


def run(
    channel: str,
    *,
    base_title: str | None = None,
    ingest: str = "video+comments",     # video+comments | comments | video
    comments_mode: str = "top",          # top | all
    max_comments: int = 1000,
    include_replies: bool = True,
    limit: int = 50,
    max_videos: int | None = None,
    pace_seconds: float = 2.0,
    dry_run: bool = False,
) -> Manifest:
    base_title = base_title or f"{channel} — comments"

    print(f"[1/3] Перечисляю видео канала: {channel}")
    videos = youtube.list_channel_videos(channel, limit=max_videos)
    print(f"      найдено видео: {len(videos)}")

    manifest = Manifest.load_or_new(channel, base_title, ingest=ingest, limit=limit)
    # Rebuild the matrix from any notebooks already created in a prior run.
    matrix = NotebookMatrix(base_title, limit=limit, existing=manifest.notebooks)

    todo = [v for v in videos if not manifest.is_done(v["video_id"])]
    print(f"[2/3] К загрузке (без уже готовых): {len(todo)} из {len(videos)}")
    est_sources = len(todo) * _unit_size(ingest)
    print(f"      ~{est_sources} источников → ~{-(-est_sources // limit)} ноутбуков "
          f"(лимит {limit}/ноутбук)")

    if dry_run:
        print("[dry-run] остановка до записи в NotebookLM.")
        return manifest

    print("[3/3] Загрузка...")
    for i, v in enumerate(todo, 1):
        vid, url, title = v["video_id"], v["url"], v["title"]
        rec = VideoRecord(title=title)
        added = 0
        nb_id = matrix.place(_unit_size(ingest))
        rec.notebook_id = nb_id
        print(f"  ({i}/{len(todo)}) {title[:70]}  → nb {nb_id[:8]}")

        try:
            # Comments first (so a throttle failure doesn't waste the video add).
            if ingest in ("video+comments", "comments"):
                meta = youtube.fetch_video(
                    url, comments_mode=comments_mode,
                    max_comments=max_comments, include_replies=include_replies,
                )
                text = comments_fmt.render(meta)
                src = nlm.add_text(nb_id, text, title=f"{title} — комментарии")
                rec.comments_source_id = src
                added += 1 if src else 0
                print(f"        комментов спарсено: {len(meta.comments)} → "
                      f"{'ok' if src else 'НЕ добавлено'}")

            if ingest in ("video+comments", "video"):
                src = nlm.add_youtube(nb_id, url)
                rec.video_source_id = src
                added += 1 if src else 0
                print(f"        видео → {'ok' if src else 'НЕ добавлено'}")

            want = _unit_size(ingest)
            rec.status = "done" if added == want else ("partial" if added else "error")
        except Exception as e:  # noqa: BLE001 — keep going on a single bad video
            rec.status = "partial" if added else "error"
            rec.error = str(e)[:300]
            print(f"        ! ошибка: {rec.error}")

        matrix.record(added)
        manifest.notebooks = matrix.notebooks
        manifest.put_video(vid, rec)
        manifest.save()                # persist every video → safe to Ctrl-C
        if i < len(todo):
            time.sleep(pace_seconds)

    _summary(manifest, matrix)
    return manifest


def _summary(manifest: Manifest, matrix: NotebookMatrix) -> None:
    done = sum(1 for v in manifest.videos.values() if v["status"] == "done")
    partial = sum(1 for v in manifest.videos.values() if v["status"] == "partial")
    err = sum(1 for v in manifest.videos.values() if v["status"] == "error")
    print("\n=== Готово ===")
    print(f"видео: done={done} partial={partial} error={err}")
    print(f"ноутбуков создано: {len(matrix.notebooks)}")
    for nb in matrix.notebooks:
        print(f"  - {nb['title']}  ({nb['count']} источников)  id={nb['id']}")
    print(f"manifest: {manifest.path}")
