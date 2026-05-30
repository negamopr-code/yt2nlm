"""Reddit adapter — read-only via praw (official API).

A "unit" is a submission (post); it yields ONE text source = the post body +
its threaded comments. Reddit is the easiest headless target: official API,
ToS-friendly, no browser. Needs a free script app's client id/secret:

    https://www.reddit.com/prefs/apps  (type: "script")
    export REDDIT_CLIENT_ID=...  REDDIT_CLIENT_SECRET=...
    # optional: REDDIT_USER_AGENT="yt2nlm:comments:0.1 (by /u/you)"

Source can be a subreddit ("python" / "r/python") or a submission URL.
"""

from __future__ import annotations

import os
import re
from datetime import datetime, timezone

from ..render import GComment, render_thread
from .base import SourceSpec, Unit

_SUB_RE = re.compile(r"^(?:/?r/)?([A-Za-z0-9_]+)$")


def _client():
    try:
        import praw
    except ImportError as e:  # pragma: no cover
        raise RuntimeError("praw not installed — run scripts/restore.sh") from e
    cid = os.environ.get("REDDIT_CLIENT_ID")
    csec = os.environ.get("REDDIT_CLIENT_SECRET")
    if not cid or not csec:
        raise RuntimeError(
            "Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET (create a 'script' app "
            "at https://www.reddit.com/prefs/apps)."
        )
    ua = os.environ.get("REDDIT_USER_AGENT", "yt2nlm:comments-collector:0.1")
    return __import__("praw").Reddit(
        client_id=cid, client_secret=csec, user_agent=ua, check_for_async=False,
    )


def _fmt_date(epoch: float | None) -> str:
    if not epoch:
        return ""
    try:
        return datetime.fromtimestamp(epoch, tz=timezone.utc).strftime("%Y-%m-%d")
    except (ValueError, OSError, OverflowError):
        return ""


class RedditAdapter:
    name = "reddit"

    def __init__(self, source: str, *, listing: str = "top",
                 time_filter: str = "year", max_comments: int = 500,
                 comment_sort: str = "top", replace_more: int = 0):
        self.source = source.strip()
        self.listing = listing             # top | hot | new | rising
        self.time_filter = time_filter      # for listing=top: hour|day|week|month|year|all
        self.max_comments = max_comments
        self.comment_sort = comment_sort
        self.replace_more = replace_more    # 0 = only already-loaded comments (fast)
        self.reddit = _client()

        m = _SUB_RE.match(self.source)
        self.subreddit = m.group(1) if m else None     # None => treat as URL

    @property
    def source_key(self) -> str:
        return f"r-{self.subreddit}" if self.subreddit else "reddit-post"

    def base_title(self) -> str:
        return f"r/{self.subreddit} — comments" if self.subreddit else "Reddit post — comments"

    def enumerate_units(self, limit: int | None) -> list[Unit]:
        if not self.subreddit:
            s = self.reddit.submission(url=self.source)
            return [Unit(uid=s.id, title=s.title, payload=s)]

        sub = self.reddit.subreddit(self.subreddit)
        fn = {"top": sub.top, "hot": sub.hot, "new": sub.new,
              "rising": sub.rising}[self.listing]
        kwargs: dict = {"limit": limit}
        if self.listing == "top":
            kwargs["time_filter"] = self.time_filter
        return [Unit(uid=s.id, title=s.title, payload=s) for s in fn(**kwargs)]

    def fetch_unit(self, unit: Unit) -> list[SourceSpec]:
        s = unit.payload
        s.comment_sort = self.comment_sort
        s.comments.replace_more(limit=self.replace_more)

        flat: list[GComment] = []

        def walk(c, depth: int) -> None:
            if len(flat) >= self.max_comments:
                return
            flat.append(GComment(
                author=str(c.author) if c.author else "[deleted]",
                text=(c.body or "").strip(),
                score=c.score,
                when=_fmt_date(getattr(c, "created_utc", None)),
                is_op=bool(getattr(c, "is_submitter", False)),
                depth=depth,
            ))
            for r in c.replies:
                walk(r, depth + 1)

        for top in s.comments:
            if len(flat) >= self.max_comments:
                break
            walk(top, 0)

        header = [
            f"Reddit: https://www.reddit.com{s.permalink}",
            f"Сабреддит: r/{s.subreddit}",
            f"Автор поста: u/{s.author if s.author else '[deleted]'}",
            f"Score: {s.score} · Комментариев (по Reddit): {s.num_comments}",
            f"Опубликовано: {_fmt_date(getattr(s, 'created_utc', None))}",
            f"Спарсено комментариев: {len(flat)}",
        ]
        title = f"r/{s.subreddit}: {unit.title}"
        post_body = (s.selftext or "").strip()
        body_title = unit.title + (f"\n\n{post_body}" if post_body else "")
        text = render_thread(title=body_title, header=header, comments=flat)
        return [SourceSpec(kind="text", title=title[:120], text=text)]
