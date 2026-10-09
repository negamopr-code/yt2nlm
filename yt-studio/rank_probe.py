#!/usr/bin/env python3
"""Ranking probe (user 2026-10-09: "you take an easy keywords ... look what from those is ranking on google as a first result, then analyse if
those are small channel and then you have a chance to rank their also"). READ-ONLY, no Claude, no account: a SEPARATE throwaway headless Chromium
(never the yt-studio channel browser) reads, per keyword, Google page 1 and YouTube's top results and says who ranks and how beatable they are
(Marcus: a YouTube video on Google page 1 = Google wants video; beatable = small channel / few views / old; green light = three or fewer of the
top 10 carry the exact phrase).
  python /opt/yt/rank_probe.py "another word for important" ["..."]      -> RANK: {json} per keyword
  python /opt/yt/rank_probe.py --check <our-video-id> "<phrase>"          -> where OUR video stands for the phrase (Google + YouTube)
Output is printed; the caller stores it (glottos-auto/out/lab/rank-probe.json)."""
import json, re, sys, time, urllib.parse
from playwright.sync_api import sync_playwright
OUR = "UCk2_0e63RhB_NOrjHa73L0Q"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
args = sys.argv[1:]; check = None
if args[:1] == ["--check"]: check = args[1]; args = args[2:]
if not args: sys.exit(__doc__)
def num(t):
    m = re.search(r"([\d.,]+)\s*([KMB]?)", t or "")
    if not m: return None
    return int(float(m.group(1).replace(",", "")) * {"": 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2)])
def norm(s): return re.sub(r"[^a-z0-9 ]", " ", (s or "").lower()).split()
def has_phrase(title, kw): return " ".join(norm(kw)) in " ".join(norm(title))
G_JS = """() => { const out = []; const seen = new Set();
  for (const h of document.querySelectorAll('a h3')) { const a = h.closest('a'); if (!a || !a.href || seen.has(a.href)) continue; seen.add(a.href);
    let box = a.parentElement, cite = null; for (let i = 0; i < 6 && box && !cite; i++) { cite = box.querySelector('cite'); box = box.parentElement; }
    let blk = a.parentElement; for (let i = 0; i < 5 && blk && (blk.innerText || '').length < 60; i++) blk = blk.parentElement;
    const txt = ((blk && blk.innerText) || '').replace(/\s+/g, ' ').slice(0, 260);
    out.push({url: a.href, title: h.innerText, site: cite ? cite.innerText.replace(/\s+/g, ' ') : '', text: txt}); }
  const vids = [...new Set([...document.querySelectorAll('a[href*="youtube.com/watch"]')].map(a => a.href))];
  return {organic: out.slice(0, 12), video_links: vids.slice(0, 12), stats: (document.querySelector('#result-stats') || {}).innerText || '',
          blocked: /unusual traffic|not a robot/i.test(document.body.innerText)} }"""
def yt_results(pg, q):
    pg.goto("https://www.youtube.com/results?hl=en&gl=US&search_query=" + urllib.parse.quote(q)); pg.wait_for_load_state("domcontentloaded"); time.sleep(4)
    try: pg.mouse.wheel(0, 6000); time.sleep(2.5)
    except Exception: pass
    if "consent." in pg.url:
        for sel in ('button[aria-label*="Reject"]', 'button:has-text("Reject all")', 'button:has-text("Accept all")'):
            try: pg.click(sel, timeout=4000); break
            except Exception: pass
        time.sleep(5)
    d = pg.evaluate("() => window.ytInitialData || null") or {}; out = []
    def walk(o):
        if isinstance(o, dict):
            v = o.get("videoRenderer")
            if v and v.get("videoId"):
                ow = (v.get("ownerText", {}).get("runs") or [{}])[0]
                out.append({"id": v["videoId"], "title": "".join(r.get("text", "") for r in v.get("title", {}).get("runs", [])),
                            "views": num(v.get("viewCountText", {}).get("simpleText", "")), "age": v.get("publishedTimeText", {}).get("simpleText", ""),
                            "channel": ow.get("text", ""), "channel_id": ow.get("navigationEndpoint", {}).get("browseEndpoint", {}).get("browseId", ""),
                            "length": v.get("lengthText", {}).get("simpleText", "")})
            for x in o.values(): walk(x)
        elif isinstance(o, list):
            for x in o: walk(x)
    walk(d); return out[:10]
SUBS = {}
def subs(pg, cid):
    if not cid: return None
    if cid in SUBS: return SUBS[cid]
    try:
        pg.goto(f"https://www.youtube.com/channel/{cid}?hl=en&gl=US"); pg.wait_for_load_state("domcontentloaded"); time.sleep(2.5)
        t = pg.evaluate("() => JSON.stringify(window.ytInitialData || {})") + pg.content(); m = re.search(r'([\d.,]+\s?[KMB]?) subscribers?', t)
        SUBS[cid] = num(m.group(1)) if m else None
    except Exception: SUBS[cid] = None
    return SUBS[cid]
def video_owner(pg, vid):
    try:
        pg.goto(f"https://www.youtube.com/watch?v={vid}&hl=en&gl=US"); pg.wait_for_load_state("domcontentloaded"); time.sleep(2.5)
        p = pg.evaluate("() => window.ytInitialPlayerResponse || null") or {}; vd = p.get("videoDetails", {}); mf = p.get("microformat", {}).get("playerMicroformatRenderer", {})
        return {"id": vid, "title": vd.get("title", ""), "views": int(vd.get("viewCount") or 0), "channel": vd.get("author", ""), "channel_id": vd.get("channelId", ""),
                "published": (mf.get("publishDate") or "")[:10]}
    except Exception as e: return {"id": vid, "error": str(e)[:120]}
with sync_playwright() as p:
    # Google answers a headless browser with "unusual traffic" after one or two searches (seen 2026-10-09); a headed Chromium with its OWN
    # persistent throwaway profile (/tmp/rank-probe-profile - not the channel profile) on a private display is read like a person's browser.
    import os
    headed = bool(os.environ.get("DISPLAY"))
    cx = p.chromium.launch_persistent_context("/tmp/rank-probe-profile", executable_path="/usr/bin/chromium", headless=not headed,
            args=["--no-sandbox", "--disable-dev-shm-usage", "--disable-blink-features=AutomationControlled", "--window-position=3000,3000"],
            viewport={"width": 1400, "height": 1000}, locale="en-US"); br = cx
    cx.add_cookies([{"name": "SOCS", "value": "CAI", "domain": d, "path": "/"} for d in (".youtube.com", ".google.com")]); pg = cx.new_page()
    cx.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"); pg.set_default_timeout(30000)
    try:
        for kw in args:
            out = {"keyword": kw, "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
            try:
                pg.goto("https://www.google.com/search?hl=en&gl=us&num=10&q=" + urllib.parse.quote(kw)); pg.wait_for_load_state("domcontentloaded"); time.sleep(3)
                if "consent.google" in pg.url or pg.locator('button:has-text("Reject all")').count():
                    try: pg.click('button:has-text("Reject all")', timeout=5000); time.sleep(4)
                    except Exception: pass
                g = pg.evaluate(G_JS)
                out["google_blocked"] = bool(g["blocked"]) or "/sorry/" in pg.url
                org = [{"pos": i + 1, "site": (o.get("site") or o["url"])[:70], "title": o["title"][:90],
                        "youtube": bool(re.search(r"youtube", o.get("site", "") + o["url"] + o.get("text", ""), re.I))} for i, o in enumerate(g["organic"][:10])]
                out["google_first"] = org[0] if org else None; out["google_organic"] = org
                ids = []
                for u in [o["url"] for o in g["organic"]] + g["video_links"]:
                    m = re.search(r"youtube\.com/watch\?v=([\w-]{11})", u)
                    if m and m.group(1) not in ids: ids.append(m.group(1))
                gv = [video_owner(pg, i) for i in ids[:5]]
                # Google wraps its links, so a video row is recognised by the word YouTube beside it and resolved by searching its title on YouTube
                for o in org:
                    if o["youtube"] and len(gv) < 5:
                        r = [v for v in yt_results(pg, o["title"].rstrip(". ")) if " ".join(norm(o["title"])[:5]) in " ".join(norm(v["title"]))]
                        if r and r[0]["id"] not in [x.get("id") for x in gv]: r[0]["google_pos"] = o["pos"]; gv.append(r[0])
                        elif not r: gv.append({"google_pos": o["pos"], "title": o["title"], "unresolved": True})
                out["google_videos"] = gv
            except Exception as e: out["google_error"] = str(e)[:160]
            try:
                y = yt_results(pg, kw); out["youtube_top"] = y
                out["youtube_exact_title_in_top10"] = sum(1 for v in y if has_phrase(v["title"], kw))
                out["our_position_youtube"] = next((i + 1 for i, v in enumerate(y) if v["channel_id"] == OUR), None)
                if check: out["check_position_youtube"] = next((i + 1 for i, v in enumerate(y) if v["id"] == check), None)
            except Exception as e: out["youtube_error"] = str(e)[:160]
            for v in (out.get("google_videos") or []) + (out.get("youtube_top") or [])[:5]:
                if v.get("channel_id"): v["subscribers"] = subs(pg, v["channel_id"])
            gv = [v for v in out.get("google_videos") or [] if not v.get("error")]
            out["first_video_google_pos"] = min([v["google_pos"] for v in gv if v.get("google_pos")] or [0]) or None
            out["video_on_google_page1"] = bool(gv)
            if check: out["check_on_google_page1"] = any(v["id"] == check for v in gv)
            out["our_video_on_google"] = any(v.get("channel_id") == OUR for v in gv)
            # Marcus: beatable = a small channel, OR a video with few views however big its channel ("3,000 views in 6 years ... pretty low")
            small = [v for v in gv if v.get("channel_id") and v.get("channel_id") != OUR and ((v.get("subscribers") or 10**9) < 20000 or (v.get("views") if v.get("views") is not None else 10**9) < 5000)]
            ys = [v for v in (out.get("youtube_top") or [])[:5] if v.get("channel_id") != OUR and (v.get("subscribers") or 10**9) < 20000]
            out["beatable_video_on_google"] = [f'{v["channel"]} ({v.get("subscribers")} subs, {v.get("views")} views, {v.get("age") or v.get("published")}, Google pos {v.get("google_pos")})' for v in small]
            out["small_channel_in_youtube_top5"] = [f'{v["channel"]} ({v.get("subscribers")} subs, {v.get("views")} views, {v.get("age")})' for v in ys]
            out["green_light"] = bool(not out.get("google_blocked") and out["video_on_google_page1"] and (small or out["our_video_on_google"]) and out.get("youtube_exact_title_in_top10", 99) <= 3)
            print("RANK:", json.dumps(out, ensure_ascii=False), flush=True); time.sleep(25)
    finally: br.close()
