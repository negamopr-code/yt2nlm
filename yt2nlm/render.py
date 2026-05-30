"""Generic threaded-comment renderer (platform-agnostic).

Used by adapters that produce arbitrarily-nested comment trees (e.g. Reddit).
YouTube keeps its own 2-level renderer in comments_fmt.py.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GComment:
    author: str
    text: str
    score: int | None
    when: str            # preformatted "YYYY-MM-DD" or ""
    is_op: bool
    depth: int           # 0 = top-level, 1+ = nested replies


def render_thread(*, title: str, header: list[str], comments: list[GComment]) -> str:
    """Render a post/thread header + nested comments into Markdown."""
    lines: list[str] = [f"# {title}", ""]
    lines += [f"- {h}" for h in header]
    lines += ["", "---", ""]

    for c in comments:
        pad = "    " * c.depth
        who = c.author + (" [OP]" if c.is_op else "")
        meta = ""
        if c.score is not None:
            meta += f"▲{c.score}"
        if c.when:
            meta += (" · " if meta else "") + c.when
        meta = f" ({meta})" if meta else ""
        marker = "↳ " if c.depth else ""
        body = c.text.replace("\n", "\n" + pad + "  ")
        lines.append(f"{pad}{marker}**{who}**{meta}")
        lines.append(f"{pad}  {body}")
        if c.depth == 0:
            lines.append("")

    return "\n".join(lines).strip() + "\n"
