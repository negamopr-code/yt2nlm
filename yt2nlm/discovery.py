"""Whole-YouTube topic discovery via yt-dlp search (no API key).

Lifted from scripts/find_videos.py so the monitor can search the entire
platform for a topic, then probe candidates for comment/view counts before
spending any collection effort on them.
"""

from __future__ import annotations

from yt_dlp import YoutubeDL


def flat_search(query: str, n: int) -> list[dict]:
    """Cheap candidate list for a search query: id, title, channel, views."""
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
    """Metadata only — comment_count/view_count without downloading comments."""
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
