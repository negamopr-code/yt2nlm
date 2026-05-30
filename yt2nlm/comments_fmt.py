"""Render a video's comments into a structured Markdown text source.

Mirrors what the reference extension puts into NotebookLM: a tree of
author -> text -> reply threads, prefixed with the video's metadata so the
comments source is self-describing.
"""

from __future__ import annotations

from datetime import datetime, timezone

from .youtube import Comment, VideoMeta


def _fmt_date(yyyymmdd: str | None) -> str:
    if not yyyymmdd or len(yyyymmdd) != 8:
        return "?"
    return f"{yyyymmdd[:4]}-{yyyymmdd[4:6]}-{yyyymmdd[6:8]}"


def _fmt_ts(ts: int | None) -> str:
    if not ts:
        return ""
    try:
        return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")
    except (ValueError, OSError, OverflowError):
        return ""


def _comment_block(c: Comment, *, indent: int) -> str:
    pad = "    " * indent
    who = c.author + (" [автор канала]" if c.is_uploader else "")
    meta = f"👍{c.likes}"
    when = _fmt_ts(c.timestamp)
    if when:
        meta += f" · {when}"
    # Indent multi-line comment text consistently.
    body = c.text.replace("\n", "\n" + pad + "  ")
    marker = "↳ " if indent else ""
    return f"{pad}{marker}**{who}** ({meta})\n{pad}  {body}"


def render(meta: VideoMeta) -> str:
    """Return a Markdown document of the video's comments (threaded)."""
    # Build parent -> children index.
    children: dict[str, list[Comment]] = {}
    roots: list[Comment] = []
    for c in meta.comments:
        if c.parent == "root" or not c.parent:
            roots.append(c)
        else:
            children.setdefault(c.parent, []).append(c)

    lines: list[str] = []
    lines.append(f"# Комментарии: {meta.title}")
    lines.append("")
    lines.append(f"- Видео: {meta.url}")
    lines.append(f"- Канал: {meta.channel}")
    lines.append(f"- Опубликовано: {_fmt_date(meta.upload_date)}")
    if meta.view_count is not None:
        lines.append(f"- Просмотров: {meta.view_count:,}".replace(",", " "))
    if meta.comment_count is not None:
        lines.append(f"- Комментариев (по YouTube): {meta.comment_count}")
    lines.append(f"- Спарсено комментариев (с ответами): {len(meta.comments)}")
    lines.append("")
    lines.append("---")
    lines.append("")

    for c in roots:
        lines.append(_comment_block(c, indent=0))
        for reply in children.get(c.cid, []):
            lines.append(_comment_block(reply, indent=1))
        lines.append("")

    return "\n".join(lines).strip() + "\n"
