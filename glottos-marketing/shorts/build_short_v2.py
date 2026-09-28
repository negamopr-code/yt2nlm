#!/usr/bin/env python3
"""Words That Stick — Shorts builder v2: NotebookLM infographic panels + branded cards,
assembled with moviepy, word-synced burned-in captions from edge-tts word boundaries.

  .nlmvenv/bin/python shorts/build_short_v2.py shorts/units/ep01_v2.json

unit: {id, series, episode, voice, rate, infographic: "state/nlm-raw/x.png",
       beats: [{panel: "title+1"|1|2|3, speech} | {card: {headline, sub?}, speech}]}
Rules (user 2026-09-27): the article is the scenario; NotebookLM watermark removed (the
"Gemini Notebook" mark sits in the bottom margin below the last panel → cropped away);
the real anotherwordfor.net logo on every frame; faceless.
"""
import asyncio, json, re, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy import (AudioFileClip, ColorClip, CompositeVideoClip, ImageClip, concatenate_videoclips)

ROOT = Path(__file__).resolve().parent.parent
W, H = 1080, 1920
BG, INK, MUTED, ACCENT, HOT = (250, 247, 242), (31, 26, 23), (107, 98, 91), (112, 82, 70), (228, 87, 46)
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
LOGO = ROOT / "state/brand/awf-logo-channel.jpg"
SAFE_BOTTOM = 400          # YouTube Shorts title/buttons overlay
CONTENT_TOP, CONTENT_BOTTOM = 320, 1100
CAPTION_Y = 1150

def font(p, s): return ImageFont.truetype(p, s)

# ---------- infographic: panels + watermark removal ----------
def band_panels(path, nolabel=False):
    """Split at the top of each coloured header bar: title = above the first bar, panel n = bar n .. bar n+1."""
    im = Image.open(path).convert("RGB"); a = np.asarray(im).astype(int)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    warm = ((r > 190) & (r - b > 50) & (g > 60)).mean(axis=1) > 0.6    # yellow/orange/red header rows
    tops, prev = [], False
    for y, w in enumerate(warm):
        if w and not prev: tops.append(y)
        prev = w
    light = (a.min(axis=2) > 225); blank = light.mean(axis=1) > 0.985
    def bottom(y0, y1):                                   # last content row before y1 (drops gaps + watermark strip)
        ys = [y for y in range(y0, y1) if not blank[y]]
        while len(ys) > 1 and ys[-1] - ys[-2] > 30: ys.pop()
        return ys[-1] + 1
    def trim(t, bt):
        cols = ~(light[t:bt].mean(axis=0) > 0.985); xs = np.where(cols)[0]
        return im.crop((max(0, xs[0] - 8), max(0, t - 2), min(im.width, xs[-1] + 8), min(im.height, bt + 2)))
    ends = [t - 6 for t in tops[1:]] + [len(blank) - int(0.02 * len(blank))]   # bottom 2% = watermark line
    def bar_end(t):                                        # first row below the coloured header bar
        y = t
        while y < len(warm) and warm[y]: y += 1
        return y + 1
    # nolabel: drop the header bars (their labels, e.g. "Mild", can be wrong; language editor 2026-09-27)
    starts = [bar_end(t) if nolabel else t for t in tops]
    out = {"title": trim(0, tops[0] - 4)}
    for n, (t, e) in enumerate(zip(starts, ends), 1): out[n] = trim(t, bottom(t, e))
    if nolabel:
        ti, b1 = out["title"], out[1]; cw = max(ti.width, b1.width)
        comb = Image.new("RGB", (cw, ti.height + 16 + b1.height), (255, 255, 255))
        comb.paste(ti, ((cw - ti.width) // 2, 0)); comb.paste(b1, ((cw - b1.width) // 2, ti.height + 16)); out["title+1"] = comb
    else: out["title+1"] = trim(0, bottom(tops[0], ends[0]))
    return out, len(tops)

def grid_panels(path):
    """2-D sheets (coloured cards side by side on white): white rows/columns are gutters; a card's real top/bottom
    is where its fill spans (almost) its full width, which drops a title that overlaps the cards."""
    im = Image.open(path).convert("RGB"); a = np.asarray(im).astype(int); ink = ~(a.min(axis=2) > 235)
    def runs(mask, minlen):
        out, st = [], None
        for i, m in enumerate(list(mask) + [False]):
            if m and st is None: st = i
            if not m and st is not None:
                if i - st >= minlen: out.append((st, i))
                st = None
        return out
    boxes = []
    for y0, y1 in runs(ink.mean(axis=1) > 0.30, 150):              # row bands
        for x0, x1 in runs(ink[y0:y1].mean(axis=0) > 0.5, 150):     # cards in the band
            full = runs(ink[y0:y1, x0:x1].mean(axis=1) > 0.9, 5)
            if full: boxes.append((y0 + full[0][0], x0, y0 + full[-1][1], x1))
    boxes.sort(key=lambda b: (b[0] // 200, b[1]))
    out = {n: im.crop((x0, y0, x1, y1)) for n, (y0, x0, y1, x1) in enumerate(boxes, 1)}
    return out, len(boxes)

def panels(path):
    im = Image.open(path).convert("RGB"); a = np.asarray(im).astype(int)
    light = (a.min(axis=2) > 225)                          # near-white pixels
    blank = light.mean(axis=1) > 0.985                     # background-only rows
    segs, st = [], None
    for y, b in enumerate(blank):
        if not b and st is None: st = y
        if b and st is not None:
            if y - st > 60: segs.append((st, y))           # ignore thin rows (watermark text ~20px)
            st = None
    if st is not None and len(blank) - st > 60: segs.append((st, len(blank)))
    def trim(box):
        t, b = box; cols = ~(light[t:b].mean(axis=0) > 0.985); xs = np.where(cols)[0]
        return im.crop((max(0, xs[0] - 8), max(0, t - 8), min(im.width, xs[-1] + 8), min(im.height, b + 8)))
    title, body = segs[0], segs[1:]                        # first segment = headline
    out = {"title": trim(title)}
    for n, box in enumerate(body, 1): out[n] = trim(box)
    out["title+1"] = trim((title[0], body[0][1]))
    return out, len(body)

# ---------- branded chrome ----------
def top_bar(series, ep):
    img = Image.new("RGBA", (W, 300), BG + (255,)); d = ImageDraw.Draw(img)
    # official logo = the @anotherword8913 YouTube channel avatar (user 2026-09-27), on a white rounded tile
    S = 190; logo = Image.open(LOGO).convert("RGB").resize((S, S), Image.LANCZOS)
    mask = Image.new("L", (S, S), 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, S - 1, S - 1), 28, fill=255)
    d.rounded_rectangle((80, 56, 84 + S + 4, 60 + S + 4), 30, fill=(255, 255, 255), outline=(225, 218, 205), width=2)
    img.paste(logo, (84, 60), mask)
    x = 84 + S + 36
    d.text((x, 92), "anotherwordfor.net", font=font(FB, 44), fill=ACCENT)
    pill = f"{series.upper()}  ·  EP {ep}"; f = font(FB, 30); w = d.textlength(pill, font=f)
    d.rounded_rectangle((x, 170, x + w + 52, 228), 29, fill=ACCENT); d.text((x + 26, 182), pill, font=f, fill=(255, 255, 255))
    return img

def wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t.replace("*", ""), font=f) <= maxw: cur = t
        else: lines.append(cur); cur = w_
    return lines + [cur]

def card(headline, sub=None):
    img = Image.new("RGBA", (W, CONTENT_BOTTOM - CONTENT_TOP), BG + (0,)); d = ImageDraw.Draw(img)
    f = font(FB, 84)
    n_h = len(wrap(d, headline, f, W - 84 - 150)); n_s = len(wrap(d, sub, font(FR, 46), W - 84 - 150)) if sub else 0
    y = max(20, (img.height - (100 * n_h + (30 + 62 * n_s if sub else 0))) // 2)
    hot = False                                            # *one or more words* = highlighted, may span lines
    for line in wrap(d, headline, f, W - 84 - 150):
        x = 84
        for w_ in line.split(" "):
            opens, closes = w_.startswith("*"), w_.rstrip(".,!?:;").endswith("*")
            t = w_.replace("*", "") + " "
            d.text((x, y), t, font=f, fill=HOT if (hot or opens) else INK); x += d.textlength(t, font=f)
            if opens: hot = True
            if closes: hot = False
        y += 100
    if sub:
        y += 30
        for line in wrap(d, sub, font(FR, 46), W - 84 - 150): d.text((84, y), line, font=font(FR, 46), fill=MUTED); y += 62
    return img

def caption_img(text):
    f = font(FB, 58); d0 = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    lines = wrap(d0, text, f, W - 84 - 150 - 40); h = 40 + 72 * len(lines)
    wmax = max(d0.textlength(l, font=f) for l in lines) + 48
    img = Image.new("RGBA", (int(wmax), h), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, wmax, h), 26, fill=(31, 26, 23, 225))
    for i, l in enumerate(lines): d.text((24, 18 + 72 * i), l, font=f, fill=(255, 255, 255))
    return img

# ---------- voice with word timings ----------
async def tts(text, voice, rate, mp3):
    import edge_tts
    words = []
    c = edge_tts.Communicate(text, voice, rate=rate, boundary="WordBoundary")
    with open(mp3, "wb") as fh:
        async for ch in c.stream():
            if ch["type"] == "audio": fh.write(ch["data"])
            elif ch["type"] == "WordBoundary": words.append((ch["offset"] / 1e7, (ch["offset"] + ch["duration"]) / 1e7, ch["text"]))
    return words

def chunks(words, speech, n=3, split=None):   # split: time at which a caption must break (quiz reveal)
    toks = re.findall(r"[\w'’-]+[.,!?:;]*", speech); ends, j = [], 0
    for w in words:                                        # align TTS words to script tokens
        key = re.sub(r"\W", "", w[2].lower())
        while j < len(toks) and re.sub(r"\W", "", toks[j].lower()) != key: j += 1
        ends.append(j < len(toks) and bool(re.search(r"[.!?:;,]$", toks[j]))); j += 1
    out, g = [], []
    for w, e in zip(words, ends):
        if g and split is not None and g[0][0] < split <= w[0]:   # never let one caption straddle the quiz pause
            out.append((g[0][0], g[-1][1], " ".join(x[2] for x in g))); g = []
        g.append(w)
        if e or len(g) == n: out.append((g[0][0], g[-1][1], " ".join(x[2] for x in g))); g = []
    if g: out.append((g[0][0], g[-1][1], " ".join(x[2] for x in g)))
    return out

# ---------- podcast mode: a finished voice track (e.g. NotebookLM Audio Overview) drives the timing ----------
def podcast_track(u, out):
    """unit.audio = {file, words (faster-whisper [start,end,word]), cuts [[t0,t1]], inserts [[t, secs]], fixes {heard: written}}.
    Times are on the ORIGINAL recording. cuts remove audio (language gate / podcast markers); inserts add silence
    at t (quiz answer pauses: the answer word that starts at t is heard only after the silence).
    Returns (mp3 path, words on the EDITED timeline, shift(t) original -> edited)."""
    import subprocess
    a = u["audio"]; words = json.load(open(ROOT / a["words"])); cuts = sorted(a.get("cuts", [])); ins = sorted(a.get("inserts", []))
    def keep(t): return not any(c0 <= t < c1 for c0, c1 in cuts)
    def shift(t):
        return (t - sum(min(c1, t) - c0 for c0, c1 in cuts if t > c0)
                  + sum(d for p, d in ins if p <= t))
    fx = a.get("fixes", {})
    def snap(t):   # recogniser onsets run 60-80 ms early: a word starting just before a quiz pause belongs after it
        return next((p for p, _ in ins if p - 0.15 <= t < p), t)
    words = [[shift(snap(w0)), shift(max(w1, snap(w0))), fx.get(w, w)] for w0, w1, w in words if keep((w0 + w1) / 2) and fx.get(w, w)]
    F = "/workspace/glottos-auto/node_modules/ffmpeg-static/ffmpeg"; SR = 44100
    raw = subprocess.run([F, "-v", "error", "-i", str(ROOT / a["file"]), "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32).reshape(-1, 2)
    events = sorted([(c0, "cut", c1) for c0, c1 in cuts] + [(p, "ins", d) for p, d in ins])
    parts, pos = [], 0.0
    for t, kind, v in events:
        if t > pos: parts.append(x[int(pos * SR):int(t * SR)]); pos = t
        if kind == "cut": pos = max(pos, v)
        else: parts.append(np.zeros((int(v * SR), 2), np.float32))
    parts.append(x[int(pos * SR):])
    y = np.concatenate(parts)
    mp3 = out / "voice.mp3"
    subprocess.run([F, "-y", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-b:a", "160k", str(mp3)],
                   input=y.tobytes(), check=True)
    return mp3, words, shift

def podcast_speech(u):
    """Fill beat.speech from the transcript so the language gate reviews exactly what the host says."""
    out = ROOT / "state/shorts" / u["id"]; out.mkdir(parents=True, exist_ok=True)
    _, words, shift = podcast_track(u, out); starts = [shift(b["from"]) for b in u["beats"]] + [1e9]
    for b, t0, t1 in zip(u["beats"], starts, starts[1:]):
        b["speech"] = " ".join(w for w0, _, w in words if t0 <= w0 < t1)
    return u

def main(unit_path):
    sys.path.insert(0, str(Path(__file__).parent)); import lang_gate
    u = json.load(open(unit_path)); ok, _ = lang_gate.verify(u)
    if not ok and "--skip-language-gate" not in sys.argv:
        sys.exit(f"REFUSED: {unit_path} has no valid English-language approval. Run the glottos-language-editor "
                 f"agent (shorts/lang_gate.py text/approve) first. The approval is void after ANY text edit.")
    u = json.load(open(unit_path)); out = ROOT / "state/shorts" / u["id"]; out.mkdir(parents=True, exist_ok=True)
    if (out / "final.mp4").exists() and "--overwrite" not in sys.argv:   # user 2026-09-27: never delete/overwrite versions
        sys.exit(f"REFUSED: {u['id']} already rendered. Give the unit a NEW id (never overwrite a version).")
    pans, npan = panels(ROOT / u["infographic"]) if u.get("infographic") else ({}, 0)
    for key, path in u.get("extra_infographics", {}).items():  # extra sheets -> beats use "panel": "<key>:<n>"
        p2, _ = {"bands": band_panels, "bands-nolabel": lambda p: band_panels(p, True), "grid": grid_panels}.get(u.get("split", {}).get(key), panels)(ROOT / path); pans.update({f"{key}:{k}": v for k, v in p2.items()})
    for k, im in pans.items(): im.save(out / f"panel-{str(k).replace(':', '-')}.png")
    bar = ImageClip(np.asarray(top_bar(u["series"], u["episode"]))).with_position((0, 0))
    beats = []
    # voice: the choice saved on the :8093 Voices tab wins over the unit's default (edge-tts voices only)
    VOICE = u.get("voice", "en-US-ChristopherNeural")
    try:
        ch = json.load(open("/workspace/glottos-auto/out/voices/choice.json")).get("voice") or ""
        if ch.startswith("en-") and not u.get("voice_locked"): VOICE = ch
    except Exception: pass
    print("voice:", VOICE)
    if "audio" in u:
        vmp3, pwords, shift = podcast_track(u, out); vaudio = AudioFileClip(str(vmp3)); print("voice: podcast", u["audio"]["file"])
        starts = [shift(b["from"]) for b in u["beats"]] + [vaudio.duration + 0.4]
    for i, b in enumerate(u["beats"], 1):
        if "audio" in u:
            t0, t1 = starts[i - 1], starts[i]; dur = t1 - t0
            audio = vaudio.subclipped(t0, min(t1, vaudio.duration))
            words = [[w0 - t0, w1 - t0, w] for w0, w1, w in pwords if t0 <= w0 < t1]
        else:
            mp3 = out / f"b{i:02d}.mp3"
            words = asyncio.run(tts(b["speech"], VOICE, u.get("rate", "+8%"), mp3))
            audio = AudioFileClip(str(mp3)); dur = audio.duration + 0.35
        layers = [ColorClip((W, H), color=BG).with_duration(dur), bar.with_duration(dur)]
        if "panel" in b:
            im = pans[b["panel"]]; maxw, maxh = W - 80, CONTENT_BOTTOM - CONTENT_TOP
            s = min(maxw / im.width, maxh / im.height); im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
            clip = (ImageClip(np.asarray(im)).with_duration(dur)
                    .resized(lambda t: 1 + 0.035 * t / max(dur, 1))                 # slow push-in
                    .with_position(lambda t, w=im.width, h=im.height: (40 + (maxw - w * (1 + 0.035 * t / max(dur, 1))) / 2,
                                                                         CONTENT_TOP + (maxh - h * (1 + 0.035 * t / max(dur, 1))) / 2)))
            layers.append(clip)
        elif "quiz" in b:
            q = b["quiz"]; rv = min(dur, max(0.5, shift(q["reveal_at"]) - t0)) if "audio" in u else dur / 2
            pause = q.get("pause", 1.5)
            front = card(q["q"], q.get("q_sub"))
            layers.append(ImageClip(np.asarray(front)).with_duration(rv).with_position((0, CONTENT_TOP)))
            for k in range(int(round(pause))):                      # countdown digits during the silence
                num = Image.new("RGBA", (160, 160), (0, 0, 0, 0)); dn = ImageDraw.Draw(num)
                dn.ellipse((0, 0, 159, 159), fill=HOT + (255,)); txt = str(int(round(pause)) - k); fnt = font(FB, 90)
                dn.text((80 - dn.textlength(txt, font=fnt) / 2, 22), txt, font=fnt, fill=(255, 255, 255))
                layers.append(ImageClip(np.asarray(num)).with_start(max(0, rv - pause + k)).with_duration(min(1.0, pause - k))
                              .with_position(((W - 160) // 2, CONTENT_BOTTOM - 180)))
            if "reveal_panel" in q:
                im = pans[q["reveal_panel"]]; maxw, maxh = W - 80, CONTENT_BOTTOM - CONTENT_TOP
                sc = min(maxw / im.width, maxh / im.height); im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)
                back = ImageClip(np.asarray(im)).with_position((40 + (maxw - im.width) / 2, CONTENT_TOP + (maxh - im.height) / 2))
            else:
                back = ImageClip(np.asarray(card(q["a"], q.get("a_sub")))).with_position((0, CONTENT_TOP))
            layers.append(back.with_start(rv).with_duration(max(0.1, dur - rv)))
            words = [w for w in words if w[0] < rv - pause - 0.05 or w[0] >= rv - 0.05]   # nothing spoken in the pause anyway
            split = rv - 0.05
        else:
            layers.append(ImageClip(np.asarray(card(b["card"]["headline"], b["card"].get("sub")))).with_duration(dur).with_position((0, CONTENT_TOP)))
        cks = chunks(words, b["speech"], split=split if "quiz" in b else None)
        for k, (t0, t1, txt) in enumerate(cks):
            ci = caption_img(txt); nxt = cks[k + 1][0] if k + 1 < len(cks) else dur
            end = min(max(t1 + 0.08, t0 + 0.25), nxt, dur)       # never overlap the next caption
            layers.append(ImageClip(np.asarray(ci)).with_start(t0).with_duration(max(0.05, end - t0))
                          .with_position(((W - 66 - ci.width) // 2, CAPTION_Y)))
        beats.append(CompositeVideoClip(layers, size=(W, H)).with_duration(dur).with_audio(audio))
        print(f"beat {i}: {dur:.1f}s, {len(words)} words", flush=True)
    final = concatenate_videoclips(beats, method="compose")
    dst = out / "final.mp4"
    final.write_videofile(str(dst), fps=30, codec="libx264", audio_codec="aac", audio_bitrate="160k",
                          preset="medium", ffmpeg_params=["-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart"], logger=None)
    print(f"FINAL {dst} {final.duration:.1f}s", flush=True)

if __name__ == "__main__":
    if sys.argv[1] == "--prep":                            # podcast units: write transcript text into beat.speech
        u = podcast_speech(json.load(open(sys.argv[2]))); json.dump(u, open(sys.argv[2], "w"), indent=2, ensure_ascii=False)
        for b in u["beats"]: print(f"{b['from']:6.1f} | {b['speech']}")
    else: main(sys.argv[1])
