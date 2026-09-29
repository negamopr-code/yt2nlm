#!/usr/bin/env python3
"""Like every comment on @anotherword8913 as the channel (user 2026-09-27: "you can like all comments by default").
EXCEPT the keys in /videos/replies/no-like.json (spam, crude jokes, abuse: set by the comment responder).
Never un-likes: it only clicks a button whose aria-label is exactly "Like" (a liked one says "Unlike").
  docker exec yt-studio /home/app/yt-profile/.venv/bin/python /opt/yt/like.py [--dry-run]"""
import hashlib, json, sys, time
from playwright.sync_api import sync_playwright
sys.path.insert(0, "/opt/yt"); from stats import parse_thread   # same comment keys as the snapshot
CH = "UCk2_0e63RhB_NOrjHa73L0Q"; dry = "--dry-run" in sys.argv
try: skip = set(json.load(open("/videos/replies/no-like.json")).get("keys", []))
except Exception: skip = set()
liked, seen = [], set()
with sync_playwright() as p:
    pg = p.chromium.connect_over_cdp("http://127.0.0.1:9222").contexts[0].new_page(); pg.set_default_timeout(15000)
    try:
        pg.goto(f"https://studio.youtube.com/channel/{CH}/comments/inbox"); time.sleep(6)
        if "accounts.google.com" in pg.url: sys.exit("NOT SIGNED IN")
        chip = pg.locator("ytcp-chip").filter(has_text="Response status").first           # all comments, this page load only
        if chip.count(): chip.locator("#delete-icon, ytcp-icon-button, tp-yt-iron-icon").last.click(); time.sleep(4)
        idle = 0
        for _ in range(300):
            before = len(seen)
            for t in pg.locator("ytcp-comment-thread").all():
                try:
                    c = parse_thread(t)
                    if not c or c["key"] in seen: continue
                    seen.add(c["key"])
                    if c["key"] in skip: continue
                    b = t.locator("ytcp-comment#comment #like-button ytcp-icon-button").first
                    if b.get_attribute("aria-label") == "Like":
                        if not dry: b.click(); time.sleep(1.2)
                        liked.append(f'{c["author"]}: {c["text"][:40]}')
                except Exception: pass
            idle = idle + 1 if len(seen) == before else 0
            if idle >= 4: break
            th = pg.locator("ytcp-comment-thread")
            if th.count(): th.last.hover()
            pg.mouse.wheel(0, 1200); time.sleep(1.5)
    finally:
        pg.close()
print(("WOULD LIKE" if dry else "LIKED"), len(liked), "of", len(seen), "comments;", len(skip), "on the no-like list")
for x in liked: print("  +", x)
