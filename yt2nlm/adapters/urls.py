"""Curated-URL adapter — ingest a list of web pages as NotebookLM URL sources.

Used for marketing-data pages that aren't YouTube/Reddit: competitor reviews
(Trustpilot), churn analyses, Quora threads, public forum/Reddit threads, etc.
NotebookLM fetches each URL server-side; one URL = one source. Reuses the
matrix/resume/manifest like the other adapters.
"""

from __future__ import annotations

from .base import SourceSpec, Unit


class UrlAdapter:
    name = "url"

    def __init__(self, items: list, *, title: str, key: str):
        # items: list of {"url": ..., "title"?: ...} or plain URL strings.
        self._items = items
        self._title = title
        self._key = key

    @property
    def source_key(self) -> str:
        return self._key

    def base_title(self) -> str:
        return self._title

    def enumerate_units(self, limit: int | None) -> list[Unit]:
        items = self._items[:limit] if limit else self._items
        units = []
        for it in items:
            if isinstance(it, dict):
                url = it.get("url")
                title = it.get("title") or url
            else:
                url = it
                title = it
            if not url:
                continue
            units.append(Unit(uid=url, title=title,
                              payload={"url": url, "title": title}))
        return units

    def fetch_unit(self, unit: Unit) -> list[SourceSpec]:
        p = unit.payload
        return [SourceSpec(kind="url", url=p["url"], title=p["title"][:100])]
