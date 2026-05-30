"""Orchestration: any SourceAdapter -> notebook matrix, with a resumable manifest.

Platform-agnostic: the adapter enumerates units and fetches each unit's source
specs; this loop places them into the notebook matrix (auto-splitting at the
per-notebook limit) and records progress after every unit.
"""

from __future__ import annotations

import time

from . import nlm
from .adapters.base import SourceAdapter
from .matrix import NotebookMatrix
from .state import ItemRecord, Manifest


def run(
    adapter: SourceAdapter,
    *,
    limit: int = 50,
    max_units: int | None = None,
    pace_seconds: float = 2.0,
    dry_run: bool = False,
) -> Manifest:
    base_title = adapter.base_title()

    print(f"[1/3] [{adapter.name}] перечисляю единицы: {adapter.source_key}")
    units = adapter.enumerate_units(max_units)
    print(f"      найдено: {len(units)}")

    manifest = Manifest.load_or_new(
        adapter.source_key, base_title, ingest=adapter.name, limit=limit)
    matrix = NotebookMatrix(base_title, limit=limit, existing=manifest.notebooks)

    todo = [u for u in units if not manifest.is_done(u.uid)]
    print(f"[2/3] К загрузке (без готовых): {len(todo)} из {len(units)}")

    if dry_run:
        # Cheap estimate assuming 1-2 sources/unit; exact size known only on fetch.
        print(f"      оценка: ~{len(todo)}–{len(todo) * 2} источников "
              f"→ ~{-(-len(todo) // limit)}–{-(-(len(todo) * 2) // limit)} ноутбуков "
              f"(лимит {limit})")
        print("[dry-run] остановка до записи в NotebookLM.")
        return manifest

    print("[3/3] Загрузка...")
    for i, u in enumerate(todo, 1):
        rec = ItemRecord(title=u.title)
        try:
            specs = adapter.fetch_unit(u)               # network-heavy
        except Exception as e:  # noqa: BLE001
            rec.status = "error"
            rec.error = f"fetch: {str(e)[:280]}"
            print(f"  ({i}/{len(todo)}) {u.title[:60]} — ! fetch error: {rec.error}")
            manifest.put_item(u.uid, rec)
            manifest.save()
            continue

        nb_id = matrix.place(len(specs))
        rec.notebook_id = nb_id
        print(f"  ({i}/{len(todo)}) {u.title[:64]}  → nb {nb_id[:8]} "
              f"({len(specs)} ист.)")

        added = 0
        for spec in specs:
            try:
                sid = nlm.add_spec(nb_id, spec.kind, url=spec.url,
                                   text=spec.text, title=spec.title)
            except Exception as e:  # noqa: BLE001
                sid = None
                rec.error = (rec.error + f" | {spec.kind}: {str(e)[:120]}").strip(" |")
            if sid:
                rec.source_ids.append(sid)
                added += 1
            print(f"        {spec.kind} → {'ok' if sid else 'НЕ добавлено'}")

        rec.status = ("done" if added == len(specs)
                      else "partial" if added else "error")
        matrix.record(added)
        manifest.notebooks = matrix.notebooks
        manifest.put_item(u.uid, rec)
        manifest.save()                                  # safe to Ctrl-C
        if i < len(todo):
            time.sleep(pace_seconds)

    _summary(manifest, matrix)
    return manifest


def _summary(manifest: Manifest, matrix: NotebookMatrix) -> None:
    vals = manifest.videos.values()
    done = sum(1 for v in vals if v["status"] == "done")
    partial = sum(1 for v in vals if v["status"] == "partial")
    err = sum(1 for v in vals if v["status"] == "error")
    print("\n=== Готово ===")
    print(f"единиц: done={done} partial={partial} error={err}")
    print(f"ноутбуков: {len(matrix.notebooks)}")
    for nb in matrix.notebooks:
        print(f"  - {nb['title']}  ({nb['count']} источников)  id={nb['id']}")
    print(f"manifest: {manifest.path}")
