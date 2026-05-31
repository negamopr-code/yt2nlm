"""Curated-list YouTube adapter — ingest an explicit set of videos (across
channels), not a whole channel. Reuses the YouTube per-video logic (video +
threaded comments); only enumeration differs: the unit list is supplied
directly (e.g. from scripts/find_videos.py output) instead of scraped from a
channel feed.
"""

from __future__ import annotations

from .base import Unit
from .youtube import YouTubeAdapter


class CuratedYouTubeAdapter(YouTubeAdapter):
    name = "youtube"

    def __init__(self, videos: list[dict], *, title: str, key: str,
                 ingest: str = "video+comments", comments_mode: str = "top",
                 max_comments: int = 1000, include_replies: bool = True):
        super().__init__(key, ingest=ingest, comments_mode=comments_mode,
                         max_comments=max_comments, include_replies=include_replies)
        self._videos = videos
        self._title = title
        self._key = key

    @property
    def source_key(self) -> str:
        return self._key

    def base_title(self) -> str:
        return self._title

    def enumerate_units(self, limit: int | None) -> list[Unit]:
        vids = self._videos[:limit] if limit else self._videos
        units = []
        for v in vids:
            vid = v.get("video_id") or v.get("id")
            if not vid:
                continue
            url = v.get("url") or f"https://www.youtube.com/watch?v={vid}"
            units.append(Unit(
                uid=vid,
                title=v.get("title") or vid,
                payload={"url": url, "video_id": vid},
            ))
        return units
