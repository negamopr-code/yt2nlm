"""videogen configuration + state (atomic saves, monitor-style)."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
STATE_DIR = WORKSPACE / "state"
REPORTS = WORKSPACE / "reports" / "videogen"
FFMPEG = os.environ.get(
    "FFMPEG", str(WORKSPACE / "glottos-auto/node_modules/ffmpeg-static/ffmpeg"))

os.environ.setdefault("NLTK_DATA", str(STATE_DIR / "nltk_data"))

DEFAULTS = {
    "channel_id": "UCk2_0e63RhB_NOrjHa73L0Q",
    "site": "anotherwordfor.net",
    "voice": "",                       # set after the user picks a sample
    "voice_rate": "+0%",
    "n_min": 5, "n_max": 8,
    "examples_per_synonym": {"shorts": 1, "long": 2},
    "wordnet_strictness": "flag",      # flag | drop for 'unrelated'
    "max_nlm_queries_per_run": 10,
    "recover_legacy": True,
    "music": {"enabled": True, "duck": True, "volume": 0.14},
    "wordlist": [],
    "uploads_per_day": 6,
}


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def load_config() -> dict:
    p = STATE_DIR / "videogen.config.json"
    cfg = dict(DEFAULTS)
    if p.exists():
        for k, v in json.loads(p.read_text()).items():
            if isinstance(v, dict) and isinstance(cfg.get(k), dict):
                cfg[k] = {**cfg[k], **v}
            else:
                cfg[k] = v
    return cfg


def load_state() -> dict:
    p = STATE_DIR / "videogen.json"
    if p.exists():
        return json.loads(p.read_text())
    return {"key": "videogen", "seq": 0, "covered": {}, "items": {},
            "uploads": {"date": "", "count": 0}, "updated_at": ""}


def save_state(state: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = datetime.now(timezone.utc).isoformat()
    p = STATE_DIR / "videogen.json"
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2))
    os.replace(tmp, p)


def new_id(state: dict, fmt: str) -> str:
    state["seq"] += 1
    return f"vg-{state['seq']:04d}-{'s' if fmt == 'shorts' else 'l'}"


def item_dir(item_id: str) -> Path:
    d = REPORTS / item_id
    d.mkdir(parents=True, exist_ok=True)
    return d


def norm_word(w: str) -> str:
    return w.strip().strip('"\'.,!?').lower()
