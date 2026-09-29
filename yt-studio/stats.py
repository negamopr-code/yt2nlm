#!/usr/bin/env python3
"""READ-ONLY channel snapshot for @anotherword8913 (user 2026-09-27: monitor traction, momentum and what viewers need).
  docker exec yt-studio /home/app/yt-profile/.venv/bin/python /opt/yt/stats.py
Reads YouTube Studio in the signed-in Chromium (CDP :9222): every video (Shorts + long) with visibility, date,
views, comments, plus every comment thread from the comments inbox. Writes /videos/analytics/snapshot-<UTC>.json
and latest.json into the profile volume; snapshot.sh copies them to glottos-auto/out/analytics (served on :8093). Clicks nothing but navigation and paging, posts nothing."""
import hashlib, json, re, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

CH = "UCk2_0e63RhB_NOrjHa73L0Q"; OUT = Path("/home/app/yt-profile/analytics"); OUT.mkdir(parents=True, exist_ok=True)
num = lambda s: int(re.sub(r"[^\d]", "", s) or 0)

def cell(r, name):
    c = r.locator(f"div.tablecell-{name}").first
    return c.inner_text().strip() if c.count() else ""

def videos(pg, tab):
    pg.goto(f"https://studio.youtube.com/channel/{CH}/videos/{tab}"); time.sleep(6); out = []
    for _ in range(20):                                                            # pages of 30
        for r in pg.locator("ytcp-video-row").all():
            a = r.locator("a[href*='/video/']").first; href = a.get_attribute("href") if a.count() else ""
            m = re.search(r"/video/([\w-]{11})", href or "")
            lines = [x for x in cell(r, "video").split("\n") if x.strip()]
            title = next((x for x in lines if not re.fullmatch(r"[\d:]+", x.strip())), "")
            out.append({"id": m.group(1) if m else None, "type": tab, "title": title.strip(),
                        "visibility": cell(r, "visibility").split("\n")[0], "date": cell(r, "date").split("\n")[0],
                        "views": num(cell(r, "views")), "comments": num(cell(r, "comments"))})
        nxt = pg.locator("#navigate-after")
        if not nxt.count() or nxt.get_attribute("aria-disabled") == "true": break
        nxt.click(); time.sleep(4)
    return out

def parse_thread(t):
    """Top-level comment of a thread, read from its own elements (not text lines)."""
    d = t.evaluate("""e => { const c = e.querySelector('ytcp-comment#comment') || e; const q = s => c.querySelector(s);
        const tx = s => (q(s) && q(s).textContent || '').trim(); const a = q('ytcp-comment-video-thumbnail a#body');
        return {author: tx('.author-text'), when: tx('.published-time-text'), text: tx('#content-text'),
                replies: tx('#show-replies-button'), likes: tx('#vote-count'), video: tx('#video-title'),
                href: a ? a.getAttribute('href') : ''}; }""")
    if not d["author"]: return None
    m = re.search(r"(?:v=|/video/|shorts/)([\w-]{11})", d["href"] or "")
    key = hashlib.sha1(f"{d['author']}|{d['video']}|{d['text']}".encode()).hexdigest()[:12]
    return {"key": key, "author": d["author"], "when": d["when"], "text": d["text"], "video": d["video"],
            "video_id": m.group(1) if m else None, "replies": num(d["replies"]), "likes": num(d["likes"])}

def threads(pg):
    """The inbox list is VIRTUALIZED (~10 thread elements recycled while scrolling): collect while scrolling."""
    got, idle = {}, 0
    for _ in range(300):
        before = len(got)
        for t in pg.locator("ytcp-comment-thread").all():
            try:
                c = parse_thread(t)
                if c: got.setdefault(c["key"], c)
            except Exception: pass                                                # element recycled mid-read
        idle = idle + 1 if len(got) == before else 0
        if idle >= 4: break
        th = pg.locator("ytcp-comment-thread")
        if th.count(): th.last.hover()
        pg.mouse.wheel(0, 1200); time.sleep(1.5)
    return list(got.values())

def comments(pg):
    """Pass 1: Studio's default inbox view (Response status: Unresponded) -> which threads still need an answer.
    Pass 2: that filter chip removed for this page load only (a reload restores the user's default) -> ALL threads."""
    pg.goto(f"https://studio.youtube.com/channel/{CH}/comments/inbox"); time.sleep(6)
    open_keys = {c["key"] for c in threads(pg)}
    chip = pg.locator("ytcp-chip").filter(has_text="Response status").first
    if chip.count(): chip.locator("#delete-icon, ytcp-icon-button, tp-yt-iron-icon").last.click(); time.sleep(4)
    allc = threads(pg)
    for c in allc: c["unresponded"] = c["key"] in open_keys
    return allc

def main():
    with sync_playwright() as p:
        ctx = p.chromium.connect_over_cdp("http://127.0.0.1:9222").contexts[0]; pg = ctx.new_page(); pg.set_default_timeout(30000)
        try:
            pg.goto(f"https://studio.youtube.com/channel/{CH}"); time.sleep(4)
            if "accounts.google.com" in pg.url: sys.exit("NOT SIGNED IN: sign in as the channel account at http://localhost:8115/vnc.html")
            snap = {"at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "channel": CH,
                    "videos": videos(pg, "short") + videos(pg, "upload"), "comments": comments(pg)}
        finally:
            pg.close()
    prev = sorted(OUT.glob("snapshot-*.json"))                                      # momentum vs the previous snapshot
    if prev:
        old = json.loads(prev[-1].read_text()); ov = {(v["id"] or v["title"]): v for v in old["videos"]}
        for v in snap["videos"]:
            o = ov.get(v["id"] or v["title"])
            if o: v.update(views_prev=o["views"], comments_prev=o["comments"], prev_at=old["at"])
    f = OUT / f"snapshot-{snap['at'].replace(':', '')}.json"
    f.write_text(json.dumps(snap, indent=1, ensure_ascii=False)); (OUT / "latest.json").write_text(f.read_text())
    print(f"{f.name}: {len(snap['videos'])} videos, {sum(v['views'] for v in snap['videos'])} views, {len(snap['comments'])} comment threads")

if __name__ == "__main__": main()
