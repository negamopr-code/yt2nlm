"""YouTube adapter — wraps the existing youtube + comments_fmt modules.

Replicates the reference workflow: per video, two sources — the video itself
(native YouTube ingest) and its threaded comments as text.
"""

from __future__ import annotations

from .. import comments_fmt
from .. import youtube as yt
from .base import SourceSpec, Unit


class YouTubeAdapter:
    name = "youtube"

    def __init__(self, channel: str, *, ingest: str = "video+comments",
                 comments_mode: str = "top", max_comments: int = 1000,
                 include_replies: bool = True):
        self.channel = channel
        self.ingest = ingest               # video+comments | comments | video
        self.comments_mode = comments_mode
        self.max_comments = max_comments
        self.include_replies = include_replies

    @property
    def source_key(self) -> str:
        return self.channel

    def base_title(self) -> str:
        return f"{self.channel} — comments"

    def enumerate_units(self, limit: int | None) -> list[Unit]:
        vids = yt.list_channel_videos(self.channel, limit=limit)
        return [Unit(uid=v["video_id"], title=v["title"], payload=v) for v in vids]

    def fetch_unit(self, unit: Unit) -> list[SourceSpec]:
        v = unit.payload
        specs: list[SourceSpec] = []
        if self.ingest in ("video+comments", "comments"):
            meta = yt.fetch_video(
                v["url"], comments_mode=self.comments_mode,
                max_comments=self.max_comments, include_replies=self.include_replies,
            )
            specs.append(SourceSpec(
                kind="text",
                title=f"{unit.title} — комментарии",
                text=comments_fmt.render(meta),
            ))
        if self.ingest in ("video+comments", "video"):
            specs.append(SourceSpec(kind="youtube", title=unit.title, url=v["url"]))
        return specs
