#!/usr/bin/env python3
"""Remove ONE comment the USER confirmed as spam on :8093 (Replies tab, type "spam", status "approved").
User 2026-09-27: "if you detect spam you prepare it and I will make it spam". Uses Studio's comment menu → Remove.
  docker exec yt-studio /home/app/yt-profile/.venv/bin/python /opt/yt/spam.py <key>"""
import json, sys, time
from playwright.sync_api import sync_playwright
CH = "UCk2_0e63RhB_NOrjHa73L0Q"; key = sys.argv[1]
q = json.load(open("/videos/replies/queue.json")); it = next((x for x in q["items"] if x["key"] == key), None)
if not it or it.get("type") != "spam": sys.exit(f"no spam item {key}")
if it.get("status") != "approved": sys.exit(f"REFUSED: {key} not confirmed by the user")
with sync_playwright() as p:
    pg = p.chromium.connect_over_cdp("http://127.0.0.1:9222").contexts[0].new_page(); pg.set_default_timeout(15000)
    try:
        pg.goto(f"https://studio.youtube.com/channel/{CH}/comments/inbox"); time.sleep(6)
        chip = pg.locator("ytcp-chip").filter(has_text="Response status").first
        if chip.count(): chip.locator("#delete-icon, ytcp-icon-button, tp-yt-iron-icon").last.click(); time.sleep(4)
        th = None
        for _ in range(60):
            c = pg.locator("ytcp-comment-thread").filter(has_text=it["author"]).filter(has_text=it["text"][:30])
            if c.count(): th = c.first; break
            pg.mouse.wheel(0, 1200); time.sleep(1.5)
        if th is None: print("already gone (not found):", key); sys.exit(0)
        th.locator("ytcp-comment#comment #action-menu-button").first.click(); time.sleep(1.5)
        pg.locator("tp-yt-paper-item:visible").filter(has_text="Remove").first.click(); time.sleep(2)
        dlg = pg.locator("ytcp-confirmation-dialog:visible, tp-yt-paper-dialog:visible")
        if dlg.count(): dlg.first.locator("ytcp-button").filter(has_text="Remove").last.click(); time.sleep(2)
        print("REMOVED as spam:", it["author"], "|", it["text"][:40])
    finally:
        pg.close()
