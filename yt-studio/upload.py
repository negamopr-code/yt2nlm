#!/usr/bin/env python3
"""Upload a finished Short to the @anotherword8913 channel as a PRIVATE draft via YouTube Studio
(user rule 2026-09-27: the user alone publishes or deletes in Studio; never set public/unlisted here).

  docker exec yt-studio /home/app/yt-profile/.venv/bin/python /opt/yt/upload.py <video-id> <meta.json> [--dry-run]
    video-id  = file name in /videos without .mp4 (e.g. words-that-stick-ep01-v4-podcast)
    meta.json = file name in /meta (content/youtube/, language-gated): title, description, tags, made_for_kids

  ... upload.py --finish <youtube-id> <meta.json>   re-run only the finish+verify pass on an existing draft

After the upload a FINISH pass opens the draft's edit page: sets playlist (meta "playlist", created PRIVATE if
missing), video language and category when they're not right yet, saves, re-reads every field and prints
VERIFY: {json}. Never touches visibility.

Drives the signed-in Chromium over CDP :9222 (Playwright connect_over_cdp). Ledger of uploads:
/home/app/yt-profile/uploads.json (refuses to upload the same video twice unless --again)."""
import json, re, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

LEDGER = Path("/home/app/yt-profile/uploads.json")

def yt_id(link):
    m = re.search(r"(?:youtu\.be/|/shorts/|[?&]v=|/video/)([A-Za-z0-9_-]{11})", link or "")
    return m.group(1) if m else None

def _pick(page, field, want):
    """open a Studio select (language/category) and choose the item whose text is exactly `want`"""
    field.locator("ytcp-dropdown-trigger, ytcp-text-dropdown-trigger, #trigger").first.click(); time.sleep(1.5)
    page.locator("tp-yt-paper-item:visible").filter(has_text=re.compile(rf"^\s*{re.escape(want)}\s*$")).first.click(); time.sleep(1)

def set_playlist(page, name):
    """tick playlist `name` in the Playlists picker; create it (PRIVATE, user rule: nothing goes public) if missing"""
    page.locator("ytcp-video-metadata-playlists").first.locator("ytcp-dropdown-trigger, ytcp-text-dropdown-trigger, #trigger").first.click(); time.sleep(2)
    dlg = page.locator("ytcp-playlist-dialog").first
    labels = lambda: [t.strip() for t in dlg.locator("#items ytcp-ve").all_inner_texts()]
    created = False
    if name not in labels():
        dlg.locator("ytcp-button:visible", has_text="New playlist").first.click(); time.sleep(1)
        page.locator("tp-yt-paper-listbox:visible tp-yt-paper-item, ytcp-text-menu:visible tp-yt-paper-item").filter(has_text="New playlist").first.click(); time.sleep(2)
        cd = page.locator("ytcp-playlist-creation-dialog").last
        cd.locator("#textbox").first.click(); page.keyboard.insert_text(name)
        cd.locator("ytcp-dropdown-trigger, ytcp-text-dropdown-trigger").filter(has_text="Public").first.click(); time.sleep(1)
        page.locator("tp-yt-paper-item:visible").filter(has_text=re.compile(r"^\s*Private\s*$")).first.click(); time.sleep(1)
        cd.locator("ytcp-button", has_text="Create").last.click(); time.sleep(5); created = True
    i = labels().index(name)
    box = dlg.locator("#items ytcp-ve").nth(i)
    if box.locator("#checkbox").first.get_attribute("aria-checked") != "true": box.locator("ytcp-checkbox-lit").first.click(); time.sleep(1)
    dlg.locator("ytcp-button:visible", has_text="Done").last.click(); time.sleep(1.5)
    return "created PRIVATE + added" if created else "added"

def read_fields(page):
    t = lambda sel: (page.locator(sel).first.inner_text() if page.locator(sel).count() else "").replace("\n", " | ")
    return {"title": t("#title-textarea #textbox"), "language": t('ytcp-form-language-input:has-text("Video language")'),
            "category": t("#category"), "playlists": t("ytcp-video-metadata-playlists"), "audience": t("#audience")[:80]}

def finish(ctx, yid, meta):
    page = ctx.new_page(); page.set_default_timeout(30000); did = []
    try:
        def load():
            page.goto(f"https://studio.youtube.com/video/{yid}/edit"); page.wait_for_load_state("domcontentloaded"); time.sleep(7)
            if page.locator("#toggle-button").count(): page.locator("#toggle-button").first.click(); time.sleep(2)   # Show more
        load(); f = read_fields(page)
        lang = {"en": "English"}.get(meta.get("language"), "")
        for key, want, sel in (("language", lang, 'ytcp-form-language-input:has-text("Video language")'), ("category", meta.get("category", ""), "#category")):
            if want and want not in f[key]:
                try: _pick(page, page.locator(sel).first, want); did.append(f"{key}={want}")
                except Exception as e: page.keyboard.press("Escape"); did.append(f"{key} FAILED ({type(e).__name__})")
        pl = meta.get("playlist")
        if pl and pl not in f["playlists"]:
            try: did.append(f"playlist {set_playlist(page, pl)}")
            except Exception as e: page.keyboard.press("Escape"); did.append(f"playlist FAILED ({type(e).__name__})")
        if any("FAILED" not in d for d in did):
            page.locator("ytcp-button#save").first.click(); time.sleep(6)
            page.screenshot(path="/home/app/yt-profile/last-finish-saved.png"); load(); f = read_fields(page)
        ok = {"title": meta["title"][:100].strip() == f["title"].strip(),
              "language": (not lang) or lang in f["language"], "category": (not meta.get("category")) or meta["category"] in f["category"],
              "playlist": (not pl) or pl in f["playlists"], "not_for_kids": "not made for kids" in f["audience"].lower()}
        # Studio Content list: the row must say Private. A dialog that closed early leaves "Draft" (M1 2026-09-28)
        page.goto("https://studio.youtube.com/channel/UC/videos/upload"); time.sleep(8)
        f["studio_row"] = page.evaluate("""id => { const r = [...document.querySelectorAll("ytcp-video-row")].find(r => r.querySelector(`a[href*="/video/${id}/"]`));
            return r ? r.innerText.split("\\n").filter(x => x.trim()).slice(-7).join(" | ") : "row not found (still a Draft?)"; }""", yid)
        cells = [c.strip() for c in f["studio_row"].split(" | ")]; ok["studio_private"] = "Private" in cells and "Edit draft" not in cells
        return {"id": yid, "did": did, "ok": ok, "all_ok": all(ok.values()), "read": f}
    finally:
        page.close()


def main():
    if sys.argv[1] == "--finish":
        meta = json.load(open(Path("/meta") / sys.argv[3]))
        with sync_playwright() as p:
            print("VERIFY:", json.dumps(finish(p.chromium.connect_over_cdp("http://127.0.0.1:9222").contexts[0], sys.argv[2], meta)))
        return
    vid, meta_name = sys.argv[1], sys.argv[2]; dry = "--dry-run" in sys.argv
    video = Path("/videos") / f"{vid}.mp4"; meta = json.load(open(Path("/meta") / meta_name))
    assert video.exists(), f"missing {video}"
    assert meta.get("privacy", "private") == "private", "this uploader only makes PRIVATE drafts"
    ledger = json.loads(LEDGER.read_text()) if LEDGER.exists() else {}
    if vid in ledger and "--again" not in sys.argv: sys.exit(f"already uploaded: {ledger[vid]}")
    with sync_playwright() as p:
        br = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        ctx = br.contexts[0]; page = ctx.new_page(); page.set_default_timeout(60000)
        page.goto("https://studio.youtube.com/"); page.wait_for_load_state("domcontentloaded"); time.sleep(3)
        if "accounts.google.com" in page.url: sys.exit("NOT SIGNED IN: sign in as the channel account at http://localhost:8115/vnc.html")
        # 2026-09-28: a failed run leaves a DRAFT (attaching the file creates it). Resume that draft instead of uploading
        # a duplicate: Content -> row with this exact title + "Edit draft" reopens the upload dialog at Details.
        page.goto("https://studio.youtube.com/channel/UC/videos/upload"); time.sleep(8)
        done_id = page.evaluate("""t => { const r = [...document.querySelectorAll("ytcp-video-row")].find(r =>
            r.innerText.split("\\n").some(x => x.trim() === t) && r.querySelector('a[href*="/video/"]'));
            if (!r) return null; const m = r.querySelector('a[href*="/video/"]').getAttribute("href").match(/video\\/([A-Za-z0-9_-]{11})/); return m && m[1]; }""", meta["title"][:100].strip())
        if done_id and "--again" not in sys.argv:                             # already a real video: never upload twice (--again = deliberate new version, e.g. fixed audio)
            link = f"https://www.youtube.com/watch?v={done_id}"; print("already in Studio (matched by exact title):", link)
            ledger[vid] = {"link": link, "title": meta["title"], "at": time.strftime("%Y-%m-%dT%H:%M:%S"), "privacy": "private", "note": "matched by title"}
            LEDGER.write_text(json.dumps(ledger, indent=2)); print("UPLOADED (private draft):", link); page.close()
            print("VERIFY:", json.dumps(finish(ctx, done_id, meta))); return
        row = page.locator("ytcp-video-row").filter(has_text=meta["title"][:100]).filter(has_text="Edit draft")
        resumed = row.count() > 0
        if resumed:
            print("resuming existing draft:", meta["title"][:100]); row.first.locator("ytcp-button, button", has_text="Edit draft").first.click()
        else:
            page.goto("https://studio.youtube.com/"); page.wait_for_load_state("domcontentloaded"); time.sleep(4)   # upload icon lives on the dashboard
            if page.locator("#upload-icon").count(): page.click("#upload-icon")      # 2026-09 Studio: direct "Upload videos" icon
            else: page.click("#create-icon"); page.click("#text-item-0")             # older Studio: Create -> Upload videos
            if video.stat().st_size < 45 * 2**20: page.locator("input[type=file]").set_input_files(str(video))
            else:   # 2026-09-29: Playwright refuses >50 MB over CDP; the browser shares this filesystem -> hand it the PATH
                cdp = page.context.new_cdp_session(page); doc = cdp.send("DOM.getDocument", {"depth": -1, "pierce": True})
                nid = cdp.send("DOM.querySelector", {"nodeId": doc["root"]["nodeId"], "selector": "input[type=file]"})["nodeId"]
                cdp.send("DOM.setFileInputFiles", {"files": [str(video)], "nodeId": nid})
        title = page.locator("#title-textarea #textbox"); title.wait_for(); time.sleep(2)
        if not (resumed and title.inner_text().strip() == meta["title"][:100].strip()):    # a resumed draft keeps what was typed
            title.click(); page.keyboard.press("Control+A"); page.keyboard.type(meta["title"][:100])
            desc = page.locator("#description-textarea #textbox"); desc.click()
            page.keyboard.press("Control+A"); page.keyboard.press("Delete")
            for i, line in enumerate(meta["description"].split("\n")):         # typed line by line: Enter = newline
                if i: page.keyboard.press("Shift+Enter")
                if line: page.keyboard.insert_text(line)
            page.locator("#toggle-button").click()                             # "Show more" -> tags
            tags = page.locator('input[aria-label="Tags"]'); tags.click()
            tags.fill(",".join(meta.get("tags", [])) + ",")
        kids = "VIDEO_MADE_FOR_KIDS_MFK" if meta.get("made_for_kids") else "VIDEO_MADE_FOR_KIDS_NOT_MFK"
        page.locator(f'tp-yt-paper-radio-button[name="{kids}"]').click()
        # language/category/playlist are set by finish() on the edit page AFTER saving. Setting them here pressed Escape
        # on a timeout, which CLOSED the whole upload dialog (M1 and S1 on 2026-09-28).
        page.screenshot(path="/home/app/yt-profile/last-upload-details.png", full_page=True)
        dlg = page.locator("ytcp-uploads-dialog").first
        link = dlg.locator('a[href*="youtu.be/"], a[href*="/watch?v="], a[href*="/shorts/"]').first.get_attribute("href")
        assert yt_id(link), f"no video link inside the upload dialog: {link}"
        for _ in range(3): page.click("#next-button"); time.sleep(1.5)       # Details -> Elements -> Checks -> Visibility
        page.locator('tp-yt-paper-radio-button[name="PRIVATE"]').click()
        page.screenshot(path="/home/app/yt-profile/last-upload.png")
        if dry:
            print("DRY RUN: stopped before Save; dialog left open. link would be", link); return
        lab = ""
        for _ in range(120):                                                   # wait until the file is fully uploaded before saving/closing
            lab = (page.locator(".progress-label, ytcp-video-upload-progress").first.inner_text() or "").lower()
            if "complete" in lab or "processing" in lab or "checks" in lab: break
            time.sleep(5)
        print("progress:", lab.strip()[:80])
        page.click("#done-button"); time.sleep(6)
        page.screenshot(path="/home/app/yt-profile/last-upload-saved.png")
        ledger[vid] = {"link": link, "title": meta["title"], "at": time.strftime("%Y-%m-%dT%H:%M:%S"), "privacy": "private"}
        LEDGER.write_text(json.dumps(ledger, indent=2))
        print("UPLOADED (private draft):", link); page.close()
        yid = yt_id(link)
        try: print("VERIFY:", json.dumps(finish(ctx, yid, meta)))
        except Exception as e: print("VERIFY:", json.dumps({"id": yid, "all_ok": False, "error": f"{type(e).__name__}: {e}"[:300]}))

if __name__ == "__main__":
    try: main()
    except Exception:                                                          # leave the dialog open for a human; show where it stopped
        try:
            with sync_playwright() as p:
                p.chromium.connect_over_cdp("http://127.0.0.1:9222").contexts[0].pages[-1].screenshot(path="/home/app/yt-profile/last-upload-error.png")
        except Exception: pass
        raise
