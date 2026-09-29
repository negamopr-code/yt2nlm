"""Is the yt-studio browser REALLY signed in to Google? Exit 0 = yes, 2 = no, 3 = could not tell.

Asks Google itself: ListAccounts through the browser's own cookie jar over CDP (the call Chromium makes for its
account menu). Each account row carries a session-valid flag at index 5; a signed-out account is still listed
(the account chooser remembers it) with that flag 0. A cookie-presence check is NOT enough: on 2026-09-28 the DB
held SID/1PSID while Google showed the account chooser.
Used by the glottos autopilot (due.py, resumes a parked upload by itself) and the :8110 slot manager banner.
Prints no cookie values; the email is shown only as its domain."""
import json, re, sys
from playwright.sync_api import sync_playwright
try:
    with sync_playwright() as p:
        br = p.chromium.connect_over_cdp("http://127.0.0.1:9222", timeout=15000)
        r = br.contexts[0].request.post("https://accounts.google.com/ListAccounts?gpsia=1&source=ChromiumBrowser&json=standard",
                                        headers={"Origin": "https://www.google.com"}, timeout=20000)
        body = r.text()
except Exception as e:
    print(f"UNKNOWN: {type(e).__name__}"); sys.exit(3)
if r.status != 200:
    print(f"UNKNOWN: HTTP {r.status}"); sys.exit(3)
try:
    rows = json.loads(body)[1]
except Exception:
    print("UNKNOWN: unparsable ListAccounts"); sys.exit(3)
live = [a for a in rows if len(a) > 5 and a[5] == 1]
if live:
    print(f"SIGNED_IN ({len(live)} live of {len(rows)})"); sys.exit(0)
print(f"SIGNED_OUT ({len(rows)} remembered account(s), none with a live session)"); sys.exit(2)
