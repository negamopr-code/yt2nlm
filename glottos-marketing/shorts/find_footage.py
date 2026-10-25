#!/usr/bin/env python3
"""Find FREE + LEGAL video clips for a scene, across the sources in state/footage/sources.json (user 2026-10-18 / 2026-10-23:
"you will have access to unlimited library of videos where you can search the videos for each and every situtation or scene";
"having different footages can be a hypotesis"). Sources and licence rules come from the free-footage NotebookLM corpus
(skill free-legal-footage). No Claude.

  python3 shorts/find_footage.py "two people arguing" [--source pexels,pixabay,commons,archive,nasa] [--portrait] [-n 8] [--json]

Keyless: commons (Wikimedia Commons, licence read per file), archive (Internet Archive, licenseurl filter), nasa (US gov = public
domain). With a free API key in state/footage/keys.json ({"pexels": "...", "pixabay": "..."}): pexels, pixabay (modern people,
everyday situations, vertical). Only licences in ALLOWED are returned; every hit carries page, licence, attribution text.
Still check each clip by eye: recognizable people never in an offensive/sensitive context, no visible logos, no "Editorial use only".
"""
import argparse, json, os, re, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "..", "state", "footage")
UA = {"User-Agent": "glottos-footage-finder/1.0 (anotherwordfor.net; educational Shorts)"}
# CC BY-SA would force OUR video under BY-SA; NC/ND forbid a monetized edit -> never.
ALLOWED = re.compile(r"^(public domain|pd|cc0|cc-zero|cc by(?!-(nc|nd|sa))[ -]?[\d.]*|pexels license|pixabay license|us gov.*)$", re.I)


def get(url, headers=None, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={**UA, **(headers or {})}), timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429 and i < tries - 1: time.sleep(5 * (i + 1)); continue
            raise
    return {}


def keys():
    try: return json.load(open(os.path.join(STATE, "keys.json")))
    except Exception: return {}


def pexels(q, n, portrait):
    k = keys().get("pexels") or os.environ.get("PEXELS_API_KEY")
    if not k: return None
    d = get("https://api.pexels.com/videos/search?" + urllib.parse.urlencode(
        {"query": q, "per_page": n, **({"orientation": "portrait"} if portrait else {})}), {"Authorization": k})
    out = []
    for v in d.get("videos", []):
        f = max(v.get("video_files", []), key=lambda x: (x.get("width") or 0) * (x.get("height") or 0), default={})
        out.append({"source": "pexels", "title": v.get("url", "").rstrip("/").split("/")[-1], "page": v.get("url"), "file": f.get("link"),
                    "w": f.get("width"), "h": f.get("height"), "dur": v.get("duration"), "license": "Pexels License",
                    "attribution": f"Video by {v.get('user', {}).get('name')} on Pexels (credit appreciated, not required)"})
    return out


def pixabay(q, n, portrait):
    k = keys().get("pixabay") or os.environ.get("PIXABAY_API_KEY")
    if not k: return None
    d = get("https://pixabay.com/api/videos/?" + urllib.parse.urlencode({"key": k, "q": q[:100], "per_page": max(3, n), "safesearch": "true"}))
    out = []
    for v in d.get("hits", []):
        vv = v.get("videos") or {}
        f = next((vv[k] for k in ("large", "medium", "small") if (vv.get(k) or {}).get("url")), {})   # "large" is often an empty entry
        if not f: continue
        if portrait and not (f.get("height") or 0) > (f.get("width") or 0): continue
        # realistic AI-generated people need YouTube's synthetic-content disclosure -> not used (user rule: free + legal, nothing risky)
        if re.search(r"\bgenerated\b|\bai art\b|\bmidjourney\b|\bstable diffusion\b", v.get("tags") or "", re.I): continue   # 2026-10-25: Pixabay AI clips carry a truncated 'generated to(ol)' tag
        out.append({"source": "pixabay", "title": v.get("tags"), "page": v.get("pageURL"), "file": f.get("url"), "w": f.get("width"),
                    "h": f.get("height"), "dur": v.get("duration"), "license": "Pixabay License",
                    "attribution": f"Video by {v.get('user')} on Pixabay (credit appreciated, not required)"})
    return out


def commons(q, n, portrait):
    d = get("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
        "action": "query", "format": "json", "generator": "search", "gsrnamespace": 6, "gsrlimit": n * 3,
        "gsrsearch": f"{q} filetype:video", "prop": "imageinfo", "iiprop": "url|size|extmetadata"}))
    out = []
    for p in (d.get("query", {}).get("pages") or {}).values():
        ii = (p.get("imageinfo") or [{}])[0]; md = ii.get("extmetadata") or {}
        lic = re.sub("<[^>]+>", "", (md.get("LicenseShortName") or {}).get("value", "")).strip()
        if not ALLOWED.match(lic): continue
        if portrait and (ii.get("width") or 0) > (ii.get("height") or 0): continue
        art = re.sub("<[^>]+>", "", (md.get("Artist") or {}).get("value", "")).strip()[:120]
        out.append({"source": "commons", "title": p.get("title"), "page": ii.get("descriptionurl"), "file": ii.get("url"), "w": ii.get("width"),
                    "h": ii.get("height"), "dur": md.get("Duration", {}).get("value") if isinstance(md.get("Duration"), dict) else None,
                    "license": lic, "attribution": f"{p.get('title', '').replace('File:', '')} — {art or 'Wikimedia Commons'} ({lic})"})
        if len(out) >= n: break
    return out


def archive(q, n, portrait):
    # only items whose licenseurl PROVES it: public-domain mark/dedication or plain CC BY (Prelinger items without one are skipped)
    d = get("https://archive.org/advancedsearch.php?" + urllib.parse.urlencode(
        {"q": f"({q}) AND mediatype:movies AND (licenseurl:*publicdomain* OR licenseurl:*by*)",
         "fl[]": ["identifier", "title", "licenseurl", "year"], "rows": n * 3, "output": "json"}, doseq=True))
    out = []
    for x in d.get("response", {}).get("docs", []):
        lu = x.get("licenseurl") or ""
        if "publicdomain" in lu: lic = "Public domain"
        elif re.search(r"creativecommons\.org/licenses/by/", lu): lic = "CC BY"
        else: continue
        out.append({"source": "archive", "title": x.get("title"), "page": f"https://archive.org/details/{x['identifier']}", "file": None,
                    "year": x.get("year"), "license": lic, "license_url": lu,
                    "attribution": f"{x.get('title')} ({x.get('year') or 'n.d.'}), Internet Archive"})
        if len(out) >= n: break
    return out


def nasa(q, n, portrait):
    d = get("https://images-api.nasa.gov/search?" + urllib.parse.urlencode({"q": q, "media_type": "video", "page_size": n}))
    out = []
    for it in d.get("collection", {}).get("items", [])[:n]:
        m = (it.get("data") or [{}])[0]
        out.append({"source": "nasa", "title": m.get("title"), "page": f"https://images.nasa.gov/details/{m.get('nasa_id')}", "file": it.get("href"),
                    "license": "Public domain (US gov work)", "attribution": f"NASA ({m.get('center', '')}) — no NASA logo, no implied endorsement"})
    return out


# Real incidents with identifiable private people (bodycam, arrests, crashes, court) are legal as US-gov public domain but are never
# used to teach English: flagged, not returned unless --include-real.
REAL = re.compile(r"bodycam|body cam|dashcam|arrest|deputy|police|sheriff|officer|court|suspect|crash|shooting|ticket|man rams|woman rams", re.I)

BACKENDS = {"pexels": pexels, "pixabay": pixabay, "commons": commons, "archive": archive, "nasa": nasa}

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("query"); ap.add_argument("--source", default="pexels,pixabay,commons,archive")
    ap.add_argument("-n", type=int, default=6); ap.add_argument("--portrait", action="store_true"); ap.add_argument("--json", action="store_true")
    ap.add_argument("--include-real", action="store_true")
    a = ap.parse_args()
    res, notes = [], []
    for s in a.source.split(","):
        s = s.strip()
        try:
            r = BACKENDS[s](a.query, a.n, a.portrait)
        except KeyError:
            notes.append(f"{s}: unknown source"); continue
        except Exception as e:
            notes.append(f"{s}: error {e}"); continue
        if r is None: notes.append(f"{s}: no API key in state/footage/keys.json - skipped (manual search: see sources.json)")
        else:
            for h in r:
                if REAL.search(str(h.get("title"))):
                    if not a.include_real: notes.append(f"skipped real-incident footage: {h['title'][:70]}"); continue
                    h["warning"] = "real incident, identifiable private people - do not use"
                res.append(h)
    if a.json: print(json.dumps({"query": a.query, "hits": res, "notes": notes}, ensure_ascii=False, indent=1))
    else:
        for h in res: print(f"[{h['source']}] {h['license']:<24} {str(h.get('w') or '')}x{str(h.get('h') or '')} {h['title']}\n    {h['page']}")
        for nn in notes: print("note:", nn)
