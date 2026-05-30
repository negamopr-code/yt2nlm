"""Run manifest: tracks which video went into which notebook + source ids,
so a re-run resumes instead of duplicating, and so the notebook matrix can be
rebuilt to keep filling the last `_part N`.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

STATE_DIR = Path(__file__).resolve().parent.parent / "state"


def slugify(s: str) -> str:
    s = re.sub(r"[^\w\-]+", "-", s.strip().lower()).strip("-")
    return s or "channel"


@dataclass
class VideoRecord:
    title: str = ""
    notebook_id: str = ""
    video_source_id: str | None = None
    comments_source_id: str | None = None
    status: str = "pending"        # pending | done | partial | error
    error: str = ""


@dataclass
class Manifest:
    channel: str
    base_title: str
    ingest: str = "video+comments"
    limit: int = 50
    notebooks: list[dict] = field(default_factory=list)
    videos: dict[str, dict] = field(default_factory=dict)
    updated_at: str = ""

    @property
    def path(self) -> Path:
        return STATE_DIR / f"{slugify(self.channel)}.json"

    @classmethod
    def load_or_new(cls, channel: str, base_title: str, *,
                    ingest: str, limit: int) -> "Manifest":
        p = STATE_DIR / f"{slugify(channel)}.json"
        if p.exists():
            data = json.loads(p.read_text())
            return cls(**data)
        return cls(channel=channel, base_title=base_title, ingest=ingest, limit=limit)

    def save(self) -> None:
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        self.updated_at = datetime.now(timezone.utc).isoformat()
        self.path.write_text(json.dumps(asdict(self), ensure_ascii=False, indent=2))

    def is_done(self, video_id: str) -> bool:
        return self.videos.get(video_id, {}).get("status") == "done"

    def put_video(self, video_id: str, rec: VideoRecord) -> None:
        self.videos[video_id] = asdict(rec)
