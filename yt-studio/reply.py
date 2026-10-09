#!/usr/bin/env python3
"""Post ONE user-approved reply to a comment on @anotherword8913 (user 2026-09-27: "you prepare them and I decide
if they go live"). Never posts anything the user hasn't approved on the :8093 Replies tab.
  docker exec yt-studio /home/app/yt-profile/.venv/bin/python /opt/yt/reply.py <key> [--dry-run]
Reads /videos/replies/queue.json (glottos-auto/out/replies, edited on :8093). The item must have status "approved".
Posts item["final"] (the user's edited text) or item["draft"]. Finds the thread in the Studio comments inbox by
author + comment text. --dry-run types the reply, then cancels. Ledger: /home/app/yt-profile/replies-posted.json."""
import json, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

CH = "UCk2_0e63RhB_NOrjHa73L0Q"; LEDGER = Path("/home/app/yt-profile/replies-posted.json")
key = sys.argv[1]; dry = "--dry-run" in sys.argv
q = json.load(open("/videos/replies/queue.json")); item = next((x for x in q["items"] if x["key"] == key), None)
if not item: sys.exit(f"no queue item {key}")
if item.get("type") == "spam": sys.exit(f"REFUSED: {key} is a spam suggestion, not a reply")
if not dry and item.get("status") != "approved": sys.exit(f"REFUSED: {key} is '{item.get('status')}', not approved by the user")
text = (item.get("final") or item.get("draft") or "").strip()
if not text: sys.exit("empty reply")
ledger = json.loads(LEDGER.read_text()) if LEDGER.exists() else {}
if key in ledger and not dry: print(f"already posted: {ledger[key]}"); sys.exit(0)   # lets post_approved.sh mark it posted, never posts twice
with sync_playwright() as p:
    pg = p.chromium.connect_over_cdp("http://127.0.0.1:9222").contexts[0].new_page(); pg.set_default_timeout(30000)
    try:
        # 2026-10-09: the inbox opens with "Response status: Unresponded", and Studio counts a comment we liked or hearted as responded
        # (like.py does that hourly) - so an approved reply to such a comment failed "thread not found" on every pass for 3 days. The chip
        # no longer has a delete icon either. The filter lives in the URL: open the comments of THIS video with the sort filter only
        # (few threads, nothing hidden), then the whole inbox the same way as a second try. Scrolling = hover + wheel (the list is virtualized).
        import urllib.parse
        vid = item.get("video_id")
        if not vid:
            try: vid = next((c.get("video_id") for c in json.load(open("/videos/analytics/latest.json"))["comments"] if c.get("key") == key), None)
            except Exception: vid = None
        FILT = urllib.parse.quote(json.dumps([{"isDisabled": False, "isPinned": True, "name": "SORT_BY", "value": "SORT_BY_MOST_RELEVANT"}], separators=(",", ":")))
        snippet = item["text"][:40]; th = None
        for url in ([f"https://studio.youtube.com/video/{vid}/comments/inbox?filter={FILT}"] if vid else []) + [f"https://studio.youtube.com/channel/{CH}/comments/inbox?filter={FILT}"]:
            pg.goto(url); time.sleep(7)
            if "accounts.google.com" in pg.url: sys.exit("NOT SIGNED IN")
            for _ in range(60):
                cand = pg.locator("ytcp-comment-thread").filter(has_text=item["author"]).filter(has_text=snippet)
                if cand.count(): th = cand.first; break
                last = pg.locator("ytcp-comment-thread")
                if not last.count(): time.sleep(2); break
                last.last.hover(); pg.mouse.wheel(0, 1200); time.sleep(1.5)
            if th is not None: break
        if th is None: sys.exit(f"thread not found: {item['author']} / {snippet}")
        th.scroll_into_view_if_needed(); time.sleep(1)
        th.locator("#reply-button, ytcp-button:has-text('Reply')").first.click(); time.sleep(1.5)
        cb = th.locator("ytcp-commentbox").first                              # the open reply box (textarea + Cancel/Reply)
        box = cb.locator("textarea").first; box.click(); box.fill(text); time.sleep(1)
        pg.screenshot(path="/home/app/yt-profile/last-reply.png")
        if dry:
            cb.locator("ytcp-button").filter(has_text="Cancel").first.click(); print("DRY RUN: typed and cancelled for", key); sys.exit(0)
        cb.locator("ytcp-button").filter(has_text="Reply").last.click(); time.sleep(4)
        pg.screenshot(path="/home/app/yt-profile/last-reply-posted.png")
        ledger[key] = {"at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "author": item["author"], "reply": text}
        LEDGER.write_text(json.dumps(ledger, indent=2, ensure_ascii=False)); print("POSTED reply for", key)
    finally:
        pg.close()
