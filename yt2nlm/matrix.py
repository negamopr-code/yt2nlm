"""Notebook matrix: distribute sources across notebooks, creating `_part N`
notebooks when the per-notebook source limit is reached.

Ported from patent-wiki-analyzer's split loop (`src/lib/pipeline.ts`) with one
deliberate change for this use case: placement is done per VIDEO-UNIT (a video +
its comments = up to 2 sources) and a unit is never split across notebooks, so
NotebookLM can always cross-reference a video with its own comments.
"""

from __future__ import annotations

import re

from . import nlm

FREE_TIER_SOURCE_LIMIT = 50

# Matches "Title_part 3" or legacy "Title (part 3)".
_PART_RE = re.compile(r"^(.*?)(?:\s*\(part\s+(\d+)\)|_part\s+(\d+))\s*$", re.IGNORECASE)


def base_and_part(title: str) -> tuple[str, int]:
    m = _PART_RE.match(title)
    if not m:
        return title, 1
    base = m.group(1).strip()
    part = int(m.group(2) or m.group(3))
    return base, part


def next_part_title(title: str) -> str:
    base, part = base_and_part(title)
    return f"{base}_part {part + 1}"


class NotebookMatrix:
    """Stateful placement engine over one or more notebooks."""

    def __init__(self, base_title: str, *, limit: int = FREE_TIER_SOURCE_LIMIT,
                 existing: list[dict] | None = None):
        self.base_title = base_title
        self.limit = limit
        # notebooks: list of {"id","title","count"} in fill order.
        self.notebooks: list[dict] = []
        if existing:
            for nb in existing:
                self.notebooks.append({
                    "id": nb["id"],
                    "title": nb.get("title", ""),
                    "count": int(nb.get("source_count", nb.get("count", 0))),
                })

    @property
    def notebook_ids(self) -> list[str]:
        return [nb["id"] for nb in self.notebooks]

    def _current(self) -> dict | None:
        return self.notebooks[-1] if self.notebooks else None

    def place(self, unit_size: int) -> str:
        """Return the id of a notebook with room for `unit_size` sources,
        creating the first/next `_part N` notebook if needed. Does NOT itself
        add sources — call this, then add, then call `record()`.
        """
        cur = self._current()
        if cur is None:
            created = nlm.create_notebook(self.base_title)
            cur = {"id": created["id"], "title": created["title"], "count": 0}
            self.notebooks.append(cur)
        elif cur["count"] + unit_size > self.limit:
            title = next_part_title(cur["title"] or self.base_title)
            created = nlm.create_notebook(title)
            cur = {"id": created["id"], "title": created["title"], "count": 0}
            self.notebooks.append(cur)
        return cur["id"]

    def record(self, added: int) -> None:
        """Account for sources actually added to the current notebook."""
        cur = self._current()
        if cur is not None:
            cur["count"] += added
