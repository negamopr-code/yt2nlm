"""Adapter contract shared by all platforms."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass
class SourceSpec:
    """One NotebookLM source to create for a unit."""
    kind: str                      # "youtube" | "text" | "url"
    title: str
    url: str | None = None
    text: str | None = None


@dataclass
class Unit:
    """A container of comments on a platform (a video, a post, …)."""
    uid: str                       # stable id for dedup/manifest
    title: str
    payload: Any = field(default=None, repr=False)   # adapter-private object


class SourceAdapter(Protocol):
    name: str                      # e.g. "youtube" | "reddit"

    @property
    def source_key(self) -> str:
        """Stable key for the manifest filename (channel handle / subreddit)."""
        ...

    def base_title(self) -> str:
        """Base notebook title (the matrix appends `_part N`)."""
        ...

    def enumerate_units(self, limit: int | None) -> list[Unit]:
        ...

    def fetch_unit(self, unit: Unit) -> list[SourceSpec]:
        """Fetch a unit's content -> the source(s) to add for it."""
        ...
