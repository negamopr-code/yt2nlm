"""Topic queue: mined viewer questions + wordlist, scored by audience weight.

Sources (part-1 monitor, read-only):
- reports/monitor-awf/ledger.json  "questions" (structured) + "themes" (scores)
- config wordlist ("another word for X" targets)
Covered-ledger prevents remaking a topic in the same format; the 103 legacy
channel videos count as covered for format "legacy".
"""

from __future__ import annotations

import json
import re
import subprocess
import sys

from .config import WORKSPACE, norm_word

MONITOR_LEDGER = WORKSPACE / "reports" / "monitor-awf" / "ledger.json"

_QUOTED = re.compile(r"[\"'«]([A-Za-z][A-Za-z \-]{1,25})[\"'»]")
_SYN_FOR = re.compile(r"(?:synonym|another word|other words?)s?\s+for\s+"
                      r"['\"]?([A-Za-z][A-Za-z\-]{1,20})", re.IGNORECASE)
_DIFF = re.compile(r"difference between\s+['\"]?([A-Za-z\-]{2,20})['\"]?\s+and\s+"
                   r"['\"]?([A-Za-z\-]{2,20})", re.IGNORECASE)
_STOP = {"the", "a", "an", "and", "or", "of", "in", "on", "to", "it", "is",
         "this", "that", "you", "your", "very much", "english"}


def _load_ledger() -> dict:
    try:
        return json.loads(MONITOR_LEDGER.read_text())
    except OSError:
        return {"questions": [], "themes": []}


def extract_targets(text: str) -> list[str]:
    """Candidate target words from a mined viewer question."""
    out = []
    for m in _SYN_FOR.finditer(text):
        out.append(m.group(1))
    for m in _DIFF.finditer(text):
        out += [m.group(1), m.group(2)]
    for m in _QUOTED.finditer(text):
        w = m.group(1)
        if len(w.split()) <= 2:
            out.append(w)
    return [norm_word(w) for w in out
            if norm_word(w) and norm_word(w) not in _STOP]


def theme_boosts(ledger: dict) -> dict[str, float]:
    """Max theme score for themes whose label mentions a candidate word."""
    boosts: dict[str, float] = {}
    for t in ledger.get("themes", []):
        score = t.get("metrics", {}).get("score", 0)
        for w in extract_targets(t.get("label", "")):
            boosts[w] = max(boosts.get(w, 0), score)
    return boosts


def build_queue(cfg: dict, state: dict) -> list[dict]:
    """Ordered topic list: {target, score, source:{kind,text,batch}}."""
    ledger = _load_ledger()
    boosts = theme_boosts(ledger)
    seen: dict[str, dict] = {}

    questions = ledger.get("questions", [])
    n_q = max(len(questions), 1)
    for i, q in enumerate(questions):
        recency = (i + 1) / n_q          # later questions = fresher batches
        for w in extract_targets(q.get("text", "")):
            t = seen.setdefault(w, {"target": w, "score": 0.0,
                                    "source": {"kind": "question",
                                               "text": q.get("text", "")[:300],
                                               "batch": q.get("batch", "")}})
            t["score"] += 3.0 * recency

    for rank, w in enumerate(cfg.get("wordlist") or []):
        w = norm_word(w)
        t = seen.setdefault(w, {"target": w, "score": 0.0,
                                "source": {"kind": "wordlist", "text": "", "batch": ""}})
        t["score"] += 2.0 + (len(cfg["wordlist"]) - rank) * 0.05

    for w, t in seen.items():
        t["score"] += boosts.get(w, 0) / 10.0

    return sorted(seen.values(), key=lambda t: -t["score"])


def uncovered(queue: list[dict], state: dict, fmt: str,
              recover_legacy: bool) -> list[dict]:
    out = []
    for t in queue:
        cov = state["covered"].get(t["target"], {})
        if fmt in cov:
            continue                       # already made in this NEW format
        if cov.get("legacy") and not recover_legacy:
            continue
        out.append(t)
    return out


def seed_covered_from_channel(cfg: dict, state: dict) -> int:
    """Mark the existing channel's 'Another Word For X' videos as legacy-covered."""
    url = f"https://www.youtube.com/channel/{cfg['channel_id']}/videos"
    sys.path.insert(0, str(WORKSPACE))
    from yt2nlm.youtube import list_channel_videos
    n = 0
    for v in list_channel_videos(url):
        m = re.search(r"another word for\s+(.+?)(?:\s*[\[\(\-—].*)?$",
                      v.get("title", ""), re.IGNORECASE)
        w = norm_word(m.group(1)) if m else ""
        if not m:
            m2 = re.search(r"synonyms for\s+([A-Za-z\-]+)", v.get("title", ""),
                           re.IGNORECASE)
            w = norm_word(m2.group(1)) if m2 else ""
        if w:
            state["covered"].setdefault(w, {})["legacy"] = True
            n += 1
    return n
