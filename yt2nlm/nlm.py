"""Thin wrapper around the `nlm` CLI (notebooklm-mcp-cli).

Design notes (ported from patent-wiki-analyzer `loader.ts`):
- All `nlm` calls are SERIALIZED with a minimum gap between them. NotebookLM's
  backend returns RESOURCE_EXHAUSTED when hammered; the gap keeps us under that.
- Calls use subprocess with an argv LIST (no shell), so there is no quoting hell
  and large `--text` payloads are passed safely (no shell ARG parsing).
- Source IDs are obtained by diffing `source list` before/after an add, which is
  more robust than scraping the human-readable "Source ID:" line.
"""

from __future__ import annotations

import json
import os
import subprocess
import tempfile
import time

# nlm binary: default to the already-installed, already-authenticated copy in the
# patent-wiki venv (auth profile lives in ~/.notebooklm-mcp-cli, shared anyway).
NLM_BIN = os.environ.get(
    "NLM_BIN", "/home/node/patent-wiki-analyzer/.venv/bin/nlm"
)
NLM_PROFILE = os.environ.get("NLM_PROFILE", "")

# Minimum seconds between any two nlm calls (anti RESOURCE_EXHAUSTED).
MIN_CALL_GAP = float(os.environ.get("NLM_MIN_GAP", "1.5"))

_last_call_ts = 0.0


class NlmError(RuntimeError):
    pass


def _run(args: list[str], timeout: float = 180.0) -> str:
    """Run `nlm <args>` serialized with a min gap. Returns stdout (stripped)."""
    global _last_call_ts
    gap = MIN_CALL_GAP - (time.monotonic() - _last_call_ts)
    if gap > 0:
        time.sleep(gap)

    cmd = [NLM_BIN, *args]
    if NLM_PROFILE:
        cmd += ["--profile", NLM_PROFILE]
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    finally:
        _last_call_ts = time.monotonic()

    if proc.returncode != 0:
        raise NlmError(
            f"nlm {' '.join(args[:3])} failed (rc={proc.returncode}): "
            f"{(proc.stderr or proc.stdout).strip()[:500]}"
        )
    return proc.stdout.strip()


def _run_json(args: list[str], timeout: float = 180.0):
    out = _run(args, timeout)
    # nlm sometimes prints a banner line before JSON; grab from first [ or {.
    for i, ch in enumerate(out):
        if ch in "[{":
            out = out[i:]
            break
    return json.loads(out)


# --------------------------------------------------------------------------- #
# Notebooks
# --------------------------------------------------------------------------- #
def list_notebooks() -> list[dict]:
    data = _run_json(["notebook", "list"])
    return [n for n in data if n.get("id")]


def create_notebook(title: str) -> dict:
    """Create a notebook and return its {id, title, source_count}."""
    _run(["notebook", "create", title], timeout=120)
    # Find it back in the list (newest matching title).
    matches = [n for n in list_notebooks() if n.get("title") == title]
    if not matches:
        raise NlmError(f'Notebook "{title}" created but not found in list')
    # Newest first if updated_at present.
    matches.sort(key=lambda n: n.get("updated_at", ""), reverse=True)
    return matches[0]


def notebook_source_count(nb_id: str) -> int:
    return len(list_sources(nb_id))


# --------------------------------------------------------------------------- #
# Sources
# --------------------------------------------------------------------------- #
def list_sources(nb_id: str) -> list[dict]:
    try:
        data = _run_json(["source", "list", nb_id])
    except (NlmError, json.JSONDecodeError):
        return []
    return [s for s in data if s.get("id")]


def _add_and_capture(nb_id: str, add_args: list[str], timeout: float) -> str | None:
    """Run a `source add ...` then diff the source list to get the new id."""
    before = {s["id"] for s in list_sources(nb_id)}
    _run(["source", "add", nb_id, *add_args], timeout=timeout)
    after = list_sources(nb_id)
    new = [s for s in after if s["id"] not in before]
    return new[0]["id"] if new else None


def add_youtube(nb_id: str, url: str, *, wait: bool = True,
                timeout: float = 600.0) -> str | None:
    """Add a YouTube video as a source. Returns its source id (or None)."""
    args = ["--youtube", url]
    if wait:
        args += ["--wait", "--wait-timeout", str(int(timeout))]
    return _add_and_capture(nb_id, args, timeout=timeout + 30)


def add_text(nb_id: str, text: str, title: str, *, wait: bool = True,
             timeout: float = 600.0) -> str | None:
    """Add a text blob as a source (used for the comments dump).

    Passes the text via a temp .md FILE (`--file`), not `--text` on argv:
    large comment dumps (1000+ comments) blow past ARG_MAX and fail with
    E2BIG ("Argument list too long"). A file upload has no such limit.
    """
    safe = "".join(c if (c.isalnum() or c in " -_.") else "_"
                   for c in title)[:80].strip() or "comments"
    with tempfile.TemporaryDirectory() as td:
        path = os.path.join(td, f"{safe}.md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(f"# {title}\n\n{text}")
        args = ["--file", path, "--title", title]
        if wait:
            args += ["--wait", "--wait-timeout", str(int(timeout))]
        return _add_and_capture(nb_id, args, timeout=timeout + 30)


def add_url(nb_id: str, url: str, *, title: str | None = None, wait: bool = True,
            timeout: float = 600.0) -> str | None:
    """Add a web URL as a source (NotebookLM fetches the page)."""
    args = ["--url", url]
    if title:
        args += ["--title", title]
    if wait:
        args += ["--wait", "--wait-timeout", str(int(timeout))]
    return _add_and_capture(nb_id, args, timeout=timeout + 30)


def add_spec(nb_id: str, kind: str, *, url: str | None = None,
             text: str | None = None, title: str = "") -> str | None:
    """Dispatch a SourceSpec to the right add_* call."""
    if kind == "youtube":
        return add_youtube(nb_id, url)
    if kind == "url":
        return add_url(nb_id, url, title=title)
    if kind == "text":
        return add_text(nb_id, text or "", title)
    raise ValueError(f"unknown source kind: {kind}")
