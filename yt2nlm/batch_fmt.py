"""Render one monitor batch (new comments across many videos) as Markdown.

One batch = ONE NotebookLM source. The header of every video section carries
the numbers the scoring needs (views, total comments, engagement) and an
explicit `Video ID:` line so the novelty answer can tag points with
`[videos: <id>]` and the parser can trace them back.
"""

from __future__ import annotations

from .comments_fmt import _fmt_date, _fmt_ts
from .youtube import Comment, VideoMeta


def _permalink(video_id: str, cid: str) -> str:
    return f"https://www.youtube.com/watch?v={video_id}&lc={cid}"


def _comment_block(c: Comment, video_id: str, *, indent: int) -> str:
    pad = "    " * indent
    who = c.author + (" [channel author]" if c.is_uploader else "")
    meta = f"👍{c.likes}"
    when = _fmt_ts(c.timestamp)
    if when:
        meta += f" · {when}"
    body = c.text.replace("\n", "\n" + pad + "  ")
    marker = "↳ " if indent else ""
    link = _permalink(video_id, c.cid) if c.cid else ""
    return f"{pad}{marker}**{who}** ({meta}) — {link}\n{pad}  {body}"


def _stub_block(c: Comment, *, note: str) -> str:
    """One-line stub of an already-seen root so an unseen reply keeps context."""
    first_line = c.text.split("\n", 1)[0]
    return f"**{c.author}** ({note}): {first_line[:160]}"


def engagement_per_1k(meta: VideoMeta) -> float | None:
    if not meta.view_count or meta.comment_count is None:
        return None
    return round(1000 * meta.comment_count / max(meta.view_count, 1), 2)


def render_video_section(meta: VideoMeta, new_comments: list[Comment],
                         seen_roots: dict[str, Comment]) -> str:
    """One video's section. new_comments = only comments unseen so far;
    seen_roots maps cid -> Comment for roots that are NOT in this batch but
    have an unseen reply (rendered as one-line stubs for thread integrity)."""
    children: dict[str, list[Comment]] = {}
    roots: list[Comment] = []
    new_ids = {c.cid for c in new_comments}
    for c in new_comments:
        if c.parent == "root" or not c.parent:
            roots.append(c)
        else:
            children.setdefault(c.parent, []).append(c)

    lines: list[str] = []
    lines.append(f"## {meta.title} — {meta.channel}")
    lines.append(f"- Video: {meta.url}")
    lines.append(f"- Video ID: {meta.video_id}")
    stat = []
    if meta.view_count is not None:
        stat.append(f"Views: {meta.view_count:,}".replace(",", " "))
    if meta.comment_count is not None:
        stat.append(f"comments total: {meta.comment_count}")
    eng = engagement_per_1k(meta)
    if eng is not None:
        stat.append(f"engagement: {eng} comments/1k views")
    if stat:
        lines.append("- " + " · ".join(stat))
    lines.append(f"- published {_fmt_date(meta.upload_date)} · "
                 f"new comments in this batch: {len(new_comments)}")
    lines.append("")

    for c in roots:
        lines.append(_comment_block(c, meta.video_id, indent=0))
        for reply in children.get(c.cid, []):
            lines.append(_comment_block(reply, meta.video_id, indent=1))
        lines.append("")

    # Orphaned replies: parent root was seen in an earlier batch.
    orphan_parents = [p for p in children if p not in {r.cid for r in roots}]
    for p in orphan_parents:
        root = seen_roots.get(p)
        if root is not None and root.cid not in new_ids:
            lines.append(_stub_block(root, note="earlier comment, for context"))
        for reply in children[p]:
            lines.append(_comment_block(reply, meta.video_id, indent=1))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_batch(batch_id: str, topic: str, collected_utc: str,
                 sections: list[tuple[VideoMeta, list[Comment], dict]],
                 extra_sections: list[str] | None = None) -> str:
    """Assemble the full batch document.

    sections: (VideoMeta, new_comments, seen_roots) per video.
    extra_sections: pre-rendered blocks from other platforms (Reddit etc.).
    """
    n_comments = sum(len(cs) for _, cs, _ in sections)
    channels = {m.channel for m, _, _ in sections if m.channel}
    head: list[str] = []
    head.append(f"# Batch {batch_id} — {n_comments} new comments / "
                f"{len(sections)} videos / {len(channels)} channels")
    head.append(f"- Collected: {collected_utc}")
    head.append(f"- Topic: {topic}")
    if sections:
        head.append("- Videos in this batch:")
        for m, cs, _ in sections:
            views = f"{m.view_count:,}".replace(",", " ") if m.view_count else "?"
            head.append(f"  - {m.title} — {m.channel} — {len(cs)} new comments — "
                        f"{views} views")
    head.append("")
    head.append("---")
    head.append("")

    body = [render_video_section(m, cs, seen) for m, cs, seen in sections]
    body += extra_sections or []
    return "\n".join(head) + "\n" + "\n".join(body)
