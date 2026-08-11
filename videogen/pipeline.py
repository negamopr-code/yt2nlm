"""Batch orchestration: queued -> scripted -> tts -> rendered, resume-safe,
with monitor-style progress heartbeats."""

from __future__ import annotations

import json
import os
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

from . import brand as brand_mod
from . import render, script as script_mod, topics, tts
from .config import (REPORTS, item_dir, load_config, load_state, new_id,
                     now_utc, save_state)

SIZES = {"shorts": (1080, 1920), "long": (1920, 1080)}

_PROG: dict = {}
_PROG_LOCK = threading.Lock()


def _prog_write() -> None:
    _PROG["run"]["updated_at"] = datetime.now(timezone.utc).isoformat()
    p = REPORTS / "progress.json"
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(_PROG["run"], ensure_ascii=False))
    os.replace(tmp, p)


def progress(phase: str, detail: str = "", cur=None, total=None, **extra):
    if not _PROG:
        return
    with _PROG_LOCK:
        run = _PROG["run"]
        if (phase, detail) != (run.get("phase"), run.get("detail")):
            run["step_changed_at"] = datetime.now(timezone.utc).isoformat()
        run.update({"phase": phase, "detail": detail[:200], "cur": cur,
                    "total": total, **extra})
        _prog_write()


def progress_init(command: str) -> None:
    global _PROG
    REPORTS.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat()
    _PROG = {"run": {"command": command, "status": "running", "phase": "starting",
                     "detail": "", "cur": None, "total": None,
                     "started_at": now, "step_changed_at": now,
                     "pid": os.getpid()}}
    _prog_write()

    def beat():
        while True:
            time.sleep(30)
            with _PROG_LOCK:
                if not _PROG or _PROG["run"]["status"] != "running":
                    return
                _prog_write()
    threading.Thread(target=beat, daemon=True).start()


def progress_end(status: str, detail: str = "") -> None:
    if not _PROG:
        return
    with _PROG_LOCK:
        _PROG["run"].update({"status": status, "phase": status,
                             "detail": detail[:250]})
        _prog_write()


def _stage_script(item: dict, cfg: dict, state: dict) -> None:
    topic = {"target": item["target"], "source": item["topic_source"]}
    s = script_mod.generate(topic, cfg, item["format"])
    d = item_dir(item["id"])
    (d / "script.json").write_text(json.dumps(s, ensure_ascii=False, indent=1))
    (d / "meta.json").write_text(json.dumps(
        {"title": s["title"], "description": s["description"],
         "tags": s["tags"], "categoryId": "27", "privacyStatus": "private"},
        ensure_ascii=False, indent=1))
    item["status"] = "scripted"
    save_state(state)


def _stage_tts(item: dict, cfg: dict, state: dict) -> None:
    d = item_dir(item["id"])
    s = json.loads((d / "script.json").read_text())
    voice = cfg["voice"] or "en-US-ChristopherNeural"
    durs = tts.synth_slides(s["slides"], voice, cfg["voice_rate"], d / "audio")
    (d / "audio" / "durations.json").write_text(json.dumps(durs))
    item["status"] = "tts"
    item["voice"] = voice
    save_state(state)


def _stage_render(item: dict, cfg: dict, state: dict) -> None:
    d = item_dir(item["id"])
    s = json.loads((d / "script.json").read_text())
    durs = json.loads((d / "audio" / "durations.json").read_text())
    b = brand_mod.load_brand()
    size = SIZES[item["format"]]
    slides_dir = d / "slides"
    slides_dir.mkdir(exist_ok=True)
    pngs = []
    for i, sl in enumerate(s["slides"]):
        png = slides_dir / f"s{i:02d}.png"
        if not png.exists():
            render.draw_slide(sl, b, size).save(png)
        pngs.append(png)
        progress("slides", f"{item['id']} slide {i + 1}/{len(s['slides'])}",
                 i + 1, len(s["slides"]))
    wavs = [d / "audio" / f"slide{i:02d}.wav" for i in range(len(s["slides"]))]
    work = d / "work"
    work.mkdir(exist_ok=True)
    progress("assemble", item["id"])
    offsets = render.assemble(pngs, durs, wavs, d / "final.mp4", size,
                              cfg["music"], work)
    full_durs = [max(x + render.LEAD + render.TAIL, render.MIN_SLIDE)
                 for x in durs]
    render.make_srt(s["slides"], offsets, full_durs, d / "sub.srt")
    render.make_thumbnail(s, b, d / "thumb.jpg")
    item["status"] = "rendered"
    save_state(state)


STAGES = [("queued", _stage_script), ("scripted", _stage_tts),
          ("tts", _stage_render)]


def advance(item: dict, cfg: dict, state: dict) -> None:
    """Run remaining stages for one item (resume at current status)."""
    while item["status"] != "rendered":
        for status, fn in STAGES:
            if item["status"] == status:
                progress({"queued": "script", "scripted": "tts",
                          "tts": "render"}[status], item["id"])
                fn(item, cfg, state)
                break
        else:
            break


def make(n: int, fmt: str, topic_word: str | None = None) -> list[str]:
    cfg = load_config()
    state = load_state()
    progress_init(f"make {n} {fmt}")
    try:
        # resume any unfinished items first (monitor doctrine)
        pending = [it for it in state["items"].values()
                   if it["status"] not in ("rendered", "failed", "uploaded")]
        for it in pending:
            print(f"resuming {it['id']} at {it['status']}")
            advance(it, cfg, state)

        made = []
        queue = topics.uncovered(topics.build_queue(cfg, state), state, fmt,
                                 cfg["recover_legacy"])
        if topic_word:
            queue = [{"target": topic_word,
                      "source": {"kind": "manual", "text": "", "batch": ""}}]
        nlm_budget = cfg["max_nlm_queries_per_run"]
        for t in queue:
            if len(made) >= n or nlm_budget <= 0:
                break
            item_id = new_id(state, fmt)
            item = {"id": item_id, "target": t["target"], "format": fmt,
                    "status": "queued", "topic_source": t["source"],
                    "dir": str(item_dir(item_id)), "error": "",
                    "youtube_id": None, "created_at": now_utc(),
                    "approved_at": None}
            state["items"][item_id] = item
            save_state(state)
            try:
                nlm_budget -= 2          # generate may retry once
                advance(item, cfg, state)
                state["covered"].setdefault(t["target"], {})[fmt] = item_id
                made.append(item_id)
            except Exception as exc:
                item["status"] = "failed"
                item["error"] = str(exc)[:300]
                print(f"  {item_id} FAILED: {exc}")
            save_state(state)
        progress_end("done", f"{len(made)} video(s) rendered")
        return made
    except Exception as exc:
        progress_end("error", str(exc)[:250])
        raise
