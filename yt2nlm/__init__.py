"""yt2nlm — load a YouTube channel's videos + comments into NotebookLM,
auto-splitting across multiple notebooks (the "notebook matrix" pattern).

Replicates the workflow from the reference video (Z2UzUq94tAk): for each video
two sources are created — the video itself (transcript, via NotebookLM's native
YouTube ingest) and its comments (a structured text source) — and both land in
the SAME notebook so NotebookLM can cross-reference them. When a notebook hits
the per-notebook source limit (free tier = 50) a `_part N` notebook is created
and filling continues there.

Port of the proven splitting/loader pattern from patent-wiki-analyzer
(`src/lib/pipeline.ts`, `src/lib/notebooklm/loader.ts`).
"""

__all__ = ["nlm", "youtube", "comments_fmt", "matrix", "pipeline"]
