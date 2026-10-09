#!/usr/bin/env python3
"""Read or set the box "Publish to subscriptions feed and notify subscribers" of a video that is NOT public yet
(lab H50, 2026-10-09: does a long video offered to strangers first get more impressions than one offered to our
2019-21 subscribers first).
  python /opt/yt/notify.py <youtube-id>            -> NOTIFY: {json}  (read only: clicks "Show more", nothing else)
  python /opt/yt/notify.py <youtube-id> --off      -> unticks the box, Save, reloads and reads it back
  python /opt/yt/notify.py <youtube-id> --on       -> ticks it again
Touches nothing else: not the title, thumbnail, date or visibility. YouTube ignores the box once a video is public.
Run it only while holding glottos-autopilot/tick.lock (one user of this browser at a time)."""
import json, sys, time
from playwright.sync_api import sync_playwright

BOX = "#notify-subscribers"
LABEL = "Publish to subscriptions feed and notify subscribers"

def load(page, yid):
    page.goto(f"https://studio.youtube.com/video/{yid}/edit"); page.wait_for_load_state("domcontentloaded")
    page.locator("#title-textarea #textbox").first.wait_for(); time.sleep(8)
    title = page.locator("#title-textarea #textbox").first.inner_text().strip()
    tg = page.locator("#toggle-button").first                               # "Show more"
    if page.locator(BOX).count() == 0 or not page.locator(BOX).first.is_visible():
        tg.scroll_into_view_if_needed(); tg.click(); time.sleep(3)
    box = page.locator(BOX).first; box.scroll_into_view_if_needed(); time.sleep(1)
    return title, box

def state(box):
    """True = ticked, False = unticked, None = cannot tell."""
    for el in (box, box.locator("#checkbox").first, box.locator("[role=checkbox]").first):
        try:
            if el.count() == 0: continue
            a = el.get_attribute("aria-checked")
            if a in ("true", "false"): return a == "true"
            if el.get_attribute("checked") is not None: return True
        except Exception: pass
    return None

def main(yid, want):
    with sync_playwright() as p:
        ctx = p.chromium.connect_over_cdp("http://127.0.0.1:9222").contexts[0]; page = ctx.new_page(); page.set_default_timeout(30000)
        try:
            title, box = load(page, yid)
            text = box.inner_text().strip().replace("\n", " ")
            before = state(box)
            r = {"id": yid, "title": title, "label": text, "before": before,
                 "disabled": box.get_attribute("disabled") is not None or box.get_attribute("aria-disabled") == "true"}
            if LABEL.lower() not in text.lower(): r["result"] = "FAILED: the box does not carry the expected label"
            elif before is None:
                r["result"] = "FAILED: cannot read the box"; r["html"] = box.evaluate("e => e.outerHTML")[:1500]
            elif want is None: r["result"] = "read"
            elif before == want: r["result"] = "already done"; r["after"] = before
            elif r["disabled"]: r["result"] = "FAILED: the box is disabled (video already public?)"
            else:
                box.locator("#checkbox-container, #checkbox").first.click(); time.sleep(2)
                if state(box) != want: r["result"] = "FAILED: the click did not change the box"
                else:
                    sv = page.locator("ytcp-button#save").first
                    if not sv.is_enabled(): r["result"] = "FAILED: Save not enabled after the click"
                    else:
                        sv.click(); time.sleep(8)
                        title2, box = load(page, yid); r["after"] = state(box); r["title_after"] = title2
                        r["result"] = "OK" if r["after"] == want and title2 == title else "CHECK FAILED"
            page.screenshot(path=f"/home/app/yt-profile/last-notify-{yid}.png")
        finally:
            page.close()
    print("NOTIFY:", json.dumps(r, ensure_ascii=False))
    sys.exit(0 if r["result"] in ("read", "OK", "already done") else 1)

if __name__ == "__main__":
    main(sys.argv[1], False if "--off" in sys.argv else True if "--on" in sys.argv else None)
