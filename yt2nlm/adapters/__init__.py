"""Source adapters: each turns a platform (YouTube channel, subreddit, …) into
a stream of "units" (a video/post) that each yield one or more NotebookLM
source specs. The pipeline + notebook matrix are platform-agnostic and consume
any adapter.
"""

from .base import SourceSpec, Unit  # noqa: F401
