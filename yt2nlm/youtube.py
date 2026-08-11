"""YouTube enumeration + comment fetching via yt-dlp (no API key needed).

Two jobs:
- list_channel_videos(): cheap, flat listing of every video on a channel/playlist.
- fetch_video(): per-video metadata + comments (with reply threads).

Throttling: YouTube rate-limits headless comment scraping, so callers should
pace fetch_video() and be ready for partial/empty comment results. yt-dlp is
configured to sort by top and cap total comments.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from yt_dlp import YoutubeDL


@dataclass
class Comment:
    cid: str
    parent: str            # "root" for top-level, else parent comment id
    author: str
    text: str
    likes: int
    timestamp: int | None
    is_uploader: bool


@dataclass
class VideoMeta:
    video_id: str
    url: str
    title: str
    channel: str
    upload_date: str | None      # YYYYMMDD
    view_count: int | None
    comment_count: int | None
    comments: list[Comment] = field(default_factory=list)


def _channel_videos_url(channel: str) -> str:
    """Normalize a channel input into a URL whose entries are its videos."""
    c = channel.strip()
    if c.startswith("http://") or c.startswith("https://"):
        # A bare channel URL lists tabs; '/videos' gives the uploads feed.
        if ("/videos" not in c and "/shorts" not in c
                and "/playlist" not in c and "list=" not in c):
            c = c.rstrip("/") + "/videos"
        return c
    if c.startswith("@"):
        return f"https://www.youtube.com/{c}/videos"
    if c.startswith("UC") and len(c) == 24:
        return f"https://www.youtube.com/channel/{c}/videos"
    # Fallback: treat as a handle.
    return f"https://www.youtube.com/@{c.lstrip('@')}/videos"


def list_channel_videos(channel: str, *, limit: int | None = None) -> list[dict]:
    """Return [{video_id, url, title}] for every video on the channel/playlist.

    Uses extract_flat so each video is NOT downloaded/probed — fast even for 500+.
    """
    url = _channel_videos_url(channel)
    opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": "in_playlist",
        "skip_download": True,
    }
    if limit:
        opts["playlistend"] = limit

    out: list[dict] = []
    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
        for entry in info.get("entries", []) or []:
            if not entry:
                continue
            vid = entry.get("id")
            if not vid:
                continue
            out.append({
                "video_id": vid,
                "url": entry.get("url") or f"https://www.youtube.com/watch?v={vid}",
                "title": entry.get("title") or vid,
            })
    return out


def fetch_video(video_url_or_id: str, *, comments_mode: str = "top",
                max_comments: int = 1000, include_replies: bool = True) -> VideoMeta:
    """Fetch one video's metadata + comments.

    comments_mode: 'top' (popular first) or 'all' (newest, capped by max_comments).
    """
    if not video_url_or_id.startswith("http"):
        video_url_or_id = f"https://www.youtube.com/watch?v={video_url_or_id}"

    sort = "top" if comments_mode == "top" else "new"
    # max_comments tuple: total, top-level, replies, replies-per-thread.
    replies_cap = "all" if include_replies else "0"
    max_tuple = [str(max_comments), "all", replies_cap, "all"]

    opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "getcomments": True,
        "extractor_args": {
            "youtube": {
                "comment_sort": [sort],
                "max_comments": max_tuple,
            }
        },
    }
    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(video_url_or_id, download=False)

    comments = []
    for c in info.get("comments") or []:
        comments.append(Comment(
            cid=c.get("id", ""),
            parent=c.get("parent", "root"),
            author=c.get("author") or "anonymous",
            text=(c.get("text") or "").strip(),
            likes=c.get("like_count") or 0,
            timestamp=c.get("timestamp"),
            is_uploader=bool(c.get("author_is_uploader")),
        ))

    return VideoMeta(
        video_id=info.get("id", ""),
        url=info.get("webpage_url") or video_url_or_id,
        title=info.get("title") or info.get("id", ""),
        channel=info.get("channel") or info.get("uploader") or "",
        upload_date=info.get("upload_date"),
        view_count=info.get("view_count"),
        comment_count=info.get("comment_count"),
        comments=comments,
    )
