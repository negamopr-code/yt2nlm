#!/usr/bin/env python3
"""Stop Saying lane — Shorts builder (traffic test, user 2026-09-30).

  .nlmvenv/bin/python shorts/build_stop_saying.py shorts/units/l1_verybig_v2.json

User asks (2026-09-30): anotherwordfor.net background with flying synonyms + the logo guy instead of a blank one;
yellow text on black (Marcus); a longer pause between the word and its example "to digest"; zoom effects; pictures
reused from an earlier NotebookLM video with the text removed (shorts/detext.py), placed below the word.
Deterministic and Claude-free: the text on screen is the language-approved unit text, character for character;
nothing is drawn by an image model. No captions (every spoken word is already on the card). No subscribe/bell
overlay (kept as a separate layer; TikTok/IG versions must not carry YouTube's).
Memory (VM has no swap): Kokoro and the OCR run in their own processes (.ttsvenv) and exit before the render."""
import json, random, re, subprocess, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
from moviepy import VideoFileClip, AudioFileClip, ColorClip, CompositeAudioClip, CompositeVideoClip, ImageClip

ROOT = Path(__file__).resolve().parent.parent
W, H = 1080, 1920                                  # DESIGN units: every coordinate and size in main() is written for 1080x1920 ...
K = 4 / 3                                           # ... and every image is made natively at K x that (user 2026-10-05: "videos should be in 1440 quality and not in 1080")
RW, RH = int(W * K), int(H * K)                     # 1440 x 2560 = the real frame
def px(v): return int(v * K + 0.5)
BLACK, YELLOW, WHITE, GREY, RED = (12, 12, 12), (255, 212, 0), (255, 255, 255), (150, 150, 150), (232, 44, 32)
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
LOGO = ROOT / "state/brand/awf-logo-channel.jpg"
TTSPY = "/workspace/glottos-marketing/.ttsvenv/bin/python"
FF = "/workspace/glottos-marketing/.nlmvenv/lib/python3.11/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
SAFE_BOTTOM = 1520                    # YouTube Shorts title/buttons cover the bottom ~400 px
# 09-30 bug: this "very big" list flew behind EVERY Short (giant/bulky behind "exhausted") -> fallback only;
# main() passes the unit's own words (bg_words)
SYNONYMS = ["large", "huge", "vast", "giant", "massive", "enormous", "immense", "jumbo", "bulky", "hefty", "towering",
            "mammoth", "colossal", "gigantic", "whopping", "ginormous", "tremendous", "monumental", "titanic", "hulking"]

def font(s): return ImageFont.truetype(FB, px(s))     # design size -> real pixels
def arr(im): return np.asarray(im)

def logo_tile(S):
    S = px(S)                                                    # S comes in design units
    lg = Image.open(LOGO).convert("RGB").resize((S, S), Image.LANCZOS)
    m = Image.new("L", (S, S), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, S - 1, S - 1), S // 7, fill=255)
    t = Image.new("RGBA", (S, S), (0, 0, 0, 0)); t.paste(lg, (0, 0), m); return t

def word_tile(seed, n, alpha, sizes, words=SYNONYMS):
    """one H-tall transparent tile of scattered synonyms (+ a few faint logo tiles), seamless when stacked twice"""
    rnd = random.Random(seed); t = Image.new("RGBA", (RW, RH), (0, 0, 0, 0)); d = ImageDraw.Draw(t)
    for i in range(n):
        wd = rnd.choice(words); f = font(rnd.randint(*sizes)); c = YELLOW if rnd.random() < 0.45 else WHITE
        x, y = rnd.randint(-80, W - 120), rnd.randint(0, H - 60)
        for dy in (0, -H, H):                                   # wrap so the tile loops without a seam
            d.text((x * K, (y + dy) * K), wd, font=f, fill=c + (rnd.randint(*alpha),))
    for i in range(3):
        S = rnd.randint(110, 170); lt = logo_tile(S); lt.putalpha(Image.eval(lt.getchannel("A"), lambda a: a * 30 // 255))
        t.alpha_composite(lt, (px(rnd.randint(0, W - S)), px(rnd.randint(320, H - S))))
    return t

def scrolling(tile, speed, dur):
    two = Image.new("RGBA", (RW, 2 * RH), (0, 0, 0, 0)); two.paste(tile, (0, 0)); two.paste(tile, (0, RH))
    return ImageClip(arr(two)).with_duration(dur).with_position(lambda t: (0, -((t * speed * K) % RH)))

def top_bar(series, ep):
    from build_long import D                                     # ImageDraw in design units on a real-size image (same K = 4/3)
    img = Image.new("RGBA", (RW, px(300)), BLACK + (235,)); d = D(img)
    S = 190; d.rounded_rectangle((80, 56, 84 + S + 4, 60 + S + 4), 30, fill=WHITE); img.alpha_composite(logo_tile(S), (px(84), px(60)))
    x = 84 + S + 36; d.text((x, 92), "anotherwordfor.net", font=font(44), fill=YELLOW)
    pill = f"{series.upper()}  ·  EP {ep}" if ep is not None else series.upper(); f = font(30); w = d.textlength(pill, font=f)   # v3 (Marcus 10-02): no episode number, every Short stands alone
    d.rounded_rectangle((x, 170, x + w + 52, 228), 29, fill=YELLOW); d.text((x + 26, 182), pill, font=f, fill=BLACK)
    return img

def text_img(text, size, color, maxw=W - 140, strike=False, one_line=False):
    """size and maxw in design units; the returned image is in real pixels (text drawn once, at its final size)"""
    d0 = ImageDraw.Draw(Image.new("RGB", (1, 1))); words, lines, cur = text.split(), [], ""
    tl = lambda t, ff: d0.textlength(t, font=ff) / K              # width in design units
    while one_line and size > 60 and tl(text, font(size)) > maxw: size -= 6   # a struck phrase must be ONE line or the strike misses half of it
    while size > 40 and max(tl(w_, font(size)) for w_ in words) > maxw: size -= 6   # long single words (Meticulous at 170 px) must fit
    f = font(size)
    for w_ in words:
        t = (cur + " " + w_).strip()
        if tl(t, f) <= maxw: cur = t
        else: lines.append(cur); cur = w_
    lines.append(cur); lh = px(size * 1.22); wmax = int(max(d0.textlength(l, font=f) for l in lines)) + px(20)
    img = Image.new("RGBA", (wmax, lh * len(lines) + px(20)), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    for i, l in enumerate(lines): d.text(((wmax - d.textlength(l, font=f)) / 2, px(10) + i * lh), l, font=f, fill=color,
                                         stroke_width=px(max(3, size // 18)), stroke_fill=BLACK)   # stays readable over the flying words
    return img

def strike_img(w, h):
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0)); ImageDraw.Draw(img).line((px(6), h * 0.62, w - px(6), h * 0.40), fill=RED + (255,), width=max(px(10), h // 9))   # w, h are real pixels (the struck image's own size)
    return img

def pop(im, y, start, dur, grow=0.0, pop_s=0.28, x=None):
    """ImageClip centred on x (default: screen centre) at top y; pops from 80 % to 100 % in pop_s, then grows slowly"""
    c = ImageClip(arr(im)).with_start(start).with_duration(dur)
    def sc(t): return (0.8 + 0.2 * min(1, t / pop_s) ** 0.5) * (1 + grow * max(0, t - pop_s) / max(dur, 1))
    cx = (W / 2 if x is None else x) * K; y = y * K               # x, y come in design units; the image is real pixels
    return (c.resized(sc).with_position(lambda t: (cx - im.width * sc(t) / 2, y + im.height * (1 - sc(t)) / 2)))

def speak(jobs, out):
    json.dump(jobs, open(out / "kokoro_jobs.json", "w"))
    subprocess.run([TTSPY, str(Path(__file__).parent / "kokoro_tts.py"), str(out / "kokoro_jobs.json")], check=True)
    # 10-03 (H21 "Since."): Kokoro adds a voiced tail to some bare words ("sins-uh"); a checked clip of the same voice,
    # saved as override-<beat>-<part>.wav in the unit's folder, replaces that one clip
    return {j["key"]: AudioFileClip(str(o) if (o := out / f"override-{j['key']}.wav").exists() else j["out"]) for j in jobs}

def trim_silence(path, keep):
    """fast pace (lab H61): Kokoro leaves 0.05-0.4 s of silence at both ends of a clip; cut it down to `keep` seconds, the voice itself untouched"""
    import wave
    with wave.open(str(path)) as w: par, raw = w.getparams(), w.readframes(w.getnframes())
    a = np.frombuffer(raw, dtype=np.int16).reshape(-1, par.nchannels); lv = np.abs(a).max(axis=1); hit = np.nonzero(lv > max(200, lv.max() * 0.02))[0]
    if not len(hit): return
    k = int(keep * par.framerate); a = a[max(0, hit[0] - k):hit[-1] + k + 1]
    with wave.open(str(path), "wb") as w: w.setparams(par); w.writeframes(a.tobytes())

def picture(u, b, i, out, maxw=760, maxh=760):
    p = out / f"pic-{i:02d}.png"
    if b.get("picture_file"): p = ROOT / b["picture_file"]         # cleaned by pictures_from_nlm.py already
    if not p.exists():                                          # frame -> text removed + auto-crop (own process)
        raw = out / f"frame-{i:02d}.png"
        subprocess.run([FF, "-y", "-loglevel", "error", "-ss", str(b["picture_t"]), "-i", str(ROOT / u["picture_source"]),
                        "-frames:v", "1", str(raw)], check=True)
        extra = ["--box", b["picture_box"]] if b.get("picture_box") else ["--crop"]
        subprocess.run([TTSPY, str(Path(__file__).parent / "detext.py"), str(raw), str(p)] + extra, check=True)
    bd = px(8)                                                  # maxw, maxh in design units; the picture is resized once, straight to real pixels
    im = Image.open(p).convert("RGBA"); k = min(maxw * K / im.width, maxh * K / im.height); im = im.resize((int(im.width * k), int(im.height * k)), Image.LANCZOS)
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), px(36), fill=255)
    fr = Image.new("RGBA", (im.width + 2 * bd, im.height + 2 * bd), YELLOW + (255,))
    fm = Image.new("L", fr.size, 0); ImageDraw.Draw(fm).rounded_rectangle((0, 0, fr.width - 1, fr.height - 1), px(44), fill=255); fr.putalpha(fm)
    fr.paste(im, (bd, bd), m); return fr

def footage(f, start, dur, y, maxh, w=940):
    """silent stock clip centre-cropped to w x h (design units) inside the same yellow frame as the pictures; loops if shorter than dur"""
    from moviepy import vfx
    bd = px(8); W2, H2 = px(w), px(min(maxh, w * 1.15)); W2 -= W2 % 2; H2 -= H2 % 2
    # RAM cap (user 2026-10-25 "yes, cap the render RAM"): Pixabay clips are 4K; moviepy decoded every one at full size (one ffmpeg
    # reader of 1-1.5 GB each, VM at 0.4 GB free with swap 0). One ffmpeg pass (2 threads) scales + crops the clip to the exact
    # frame first (cached next to the source); moviepy then reads ~1250x1440 frames.
    src = ROOT / f["file"]; cy = f.get("cy", 0.5); ss = f.get("ss", 0)
    fit = src.with_name(f"{src.stem}.fit{W2}x{H2}-{ss}-{cy}.mp4")
    if not fit.exists() or fit.stat().st_mtime < src.stat().st_mtime:
        vf = (f"scale={W2}:{H2}:force_original_aspect_ratio=increase,"
              f"crop={W2}:{H2}:(iw-{W2})/2:'min(max(ih*{cy}-{H2}/2,0),ih-{H2})',fps=30,format=yuv420p")
        subprocess.run([FF, "-y", "-loglevel", "error", "-ss", str(ss), "-i", str(src), "-t", f"{dur + 0.5:.2f}", "-an", "-vf", vf,
                        "-c:v", "libx264", "-crf", "16", "-preset", "veryfast", "-threads", "2", str(fit) + ".tmp.mp4"], check=True)
        os.replace(str(fit) + ".tmp.mp4", fit)
    c = VideoFileClip(str(fit), audio=False)
    if c.duration < dur: c = c.with_effects([vfx.Loop(duration=dur)])
    c = c.subclipped(0, dur)
    fr = Image.new("RGBA", (W2 + 2 * bd, H2 + 2 * bd), YELLOW + (255,))
    x = (RW - fr.width) / 2
    return [ImageClip(arr(fr)).with_start(start).with_duration(dur).with_position((x, y * K)), c.with_start(start).with_position((x + bd, y * K + bd))]


def main(path):
    sys.path.insert(0, str(Path(__file__).parent)); import lang_gate
    u = json.load(open(path)); ok, _ = lang_gate.verify(u)
    if not ok and "--skip-language-gate" not in sys.argv:
        sys.exit(f"REFUSED: {path} has no valid English-language approval (run glottos-language-editor + lang_gate.py approve)")
    out = ROOT / "state/shorts" / u["id"]; out.mkdir(parents=True, exist_ok=True)
    if (out / "final.mp4").exists() and "--overwrite" not in sys.argv: sys.exit(f"REFUSED: {u['id']} already rendered (new id)")
    voice, speed, P = u["voice"].split(":", 1)[1], u.get("speed", 1.05), u.get("pause_after_word", 1.0)
    jobs = []                                                   # speech split so the pauses are real silence
    for i, b in enumerate(u["beats"], 1):
        s = b["speech"]
        m = re.search(r"[:.!?]\s" if b["kind"] in ("word", "pair") else r"[:.!?,]\s", s) if b["kind"] in ("word", "hook", "pair") else None   # hook splits at its comma too: the sub line appears as it is spoken
        if m: a, c = s[:m.start() + 1], s[m.end():]; parts = [a[:-1] + "." if a.endswith(":") else a, c[:1].upper() + c[1:] if b["kind"] == "hook" else c]
        else: parts = [s]
        for k, t in enumerate(parts): jobs.append({"key": (i, k), "text": t, "voice": voice, "speed": b.get("speed_first", speed) if k == 0 else speed,   # pronunciation card (lab H41): the word slow first, then at normal speed
                                                   "out": str(out / f"b{i:02d}-{k}.wav")})
    for j in jobs: j["key"] = f"{j['key'][0]}-{j['key'][1]}"
    if u.get("trim_silence"):                                   # fast pace (lab H61): the clips are made, trimmed, then loaded
        speak(jobs, out)
        for j in jobs: trim_silence(j["out"], u["trim_silence"])
        au = {j["key"]: AudioFileClip(str(o) if (o := out / f"override-{j['key']}.wav").exists() else j["out"]) for j in jobs}
    else: au = speak(jobs, out)
    TAIL, HG, HT, CT = u.get("tail_after_example", 0.9), u.get("hook_gap", 0.35), u.get("hook_tail", 0.5), u.get("cta_tail", 1.6)   # fast pace (lab H61): the waits of the lane, each one settable
    pj = out / "pictures.json"                                  # from pictures_from_nlm.py (unit file untouched)
    if pj.exists():
        for k, r in json.load(open(pj)).items(): u["beats"][int(k) - 1]["picture_file"] = r["file"]
    layers, audios, t0, nword = [], [], 0.0, sum(b["kind"] == "word" for b in u["beats"])
    # two-column table (lab H42, "columns": [left title, right title]): the titles stand from the first frame, each "pair" beat
    # adds a row, a "tip" beat a line under the table; everything stays until the closing card. (image, y, start, x) in design units
    table, t_end, XL, XR, ROW0, ROWH = [], None, 250, 700, 450, 170   # both columns stay left of x 930: the Shorts buttons cover the right edge (critic 10-07)
    npair = sum(b["kind"] == "pair" for b in u["beats"])
    if u.get("columns"): table += [(text_img(c, 54, GREY, maxw=470), 335, 0.0, x) for c, x in zip(u["columns"], (XL, XR))]
    for i, b in enumerate(u["beats"], 1):
        hl = b["card"].get("headline", ""); sub = b["card"].get("sub", "")
        if b["kind"] == "hook":
            a1, a2 = au[f"{i}-0"], au.get(f"{i}-1"); g = HG
            cd = b.get("countdown", 0); tick = 0.8              # either/or hook (lab H40): the viewer gets "2", "1" to decide before the answer
            dur = a1.duration + g + (a2.duration if a2 else 0) + (0.3 + cd * tick if cd else HT)
            ps = hl.split("*"); before, hot, after = ps[0].strip(), (ps[1] if len(ps) > 1 else ""), (ps[2].strip() if len(ps) > 2 else "")
            if after and not re.search(r"\w", after): hot, after = hot + after, ""     # trailing comma stays with the hot part
            y = 440
            lp = 0.01 if u.get("loop_back") else 0.28              # loop ending (lab H60): the opening stands at full size in frame 1, equal to the last frame
            if before: p1 = text_img(before, 110, WHITE); layers.append(pop(p1, y, t0, dur, pop_s=lp)); y += p1.height / K + 5
            if hot:
                hs = 0.0 if u.get("strike_from_start") else 0.15     # v3: the struck phrase is in frame 1 too
                h2 = text_img(hot, 150, YELLOW, one_line=b.get("strike", True)); layers.append(pop(h2, y, t0 + hs, dur - hs, pop_s=lp))
                if b.get("strike", True):                   # the banned phrase is crossed out once it has been said
                    st = strike_img(h2.width, h2.height)
                    s0 = 0.0 if u.get("strike_from_start") else a1.duration   # v3: crossed out in the FIRST frame (Marcus: red X pattern interrupt)
                    layers.append(ImageClip(arr(st)).with_start(t0 + s0).with_duration(dur - s0).with_position(((RW - st.width) / 2, y * K)))
                y += h2.height / K + 5
            if after: p3 = text_img(after, 110, WHITE); layers.append(pop(p3, y, t0 + 0.15, dur - 0.15)); y += p3.height / K + 5
            si = text_img(sub, 76, WHITE); layers.append(pop(si, y + 40, t0 + a1.duration + g, dur - a1.duration - g))
            for k in range(cd): layers.append(pop(text_img(str(cd - k), 230, YELLOW), y + 70 + si.height / K, dur + t0 - (cd - k) * tick, tick, pop_s=0.15))
            audios += [a1.with_start(t0)] + ([a2.with_start(t0 + a1.duration + g)] if a2 else [])
        elif b["kind"] == "word":
            n = sum(x["kind"] == "word" for x in u["beats"][:i]); aw, ae = au[f"{i}-0"], au[f"{i}-1"]
            te = aw.duration + P; dur = te + ae.duration + TAIL; yh = 410
            if b["card"].get("wrong"):                          # either/or (lab H40): the wrong choice, small and struck out, instead of the counter
                ws = b.get("wrong_size", 64); yh += (ws - 64) * 1.5   # first-second opening (lab H59): no hook beat, the banned phrase big and struck out over the FIRST better word
                wi = text_img(b["card"]["wrong"], ws, GREY if ws == 64 else WHITE, one_line=True); st = strike_img(wi.width, wi.height)
                layers.append(pop(wi, 330, t0, dur, pop_s=0.01)); layers.append(ImageClip(arr(st)).with_start(t0).with_duration(dur).with_position(((RW - st.width) / 2, 330 * K)))
            elif u.get("counter", True): layers.append(pop(text_img(f"{n} / {nword}", 46, GREY), 350, t0, dur, pop_s=0.01))
            hi = text_img(hl, 170 if len(hl) <= 11 else 120, YELLOW); layers.append(pop(hi, yh, t0, dur, grow=0.04))
            si = text_img(sub, 72 if len(sub) <= 28 else 60, WHITE); ys = yh + hi.height / K + 10
            layers.append(pop(si, ys, t0 + te, dur - te)); yp = ys + si.height / K + 25
            if b.get("footage"):                                # lab H103 arm (b): real stock footage in the picture slot (cropped to the same frame)
                layers += footage(b["footage"], t0 + te, dur - te, yp, SAFE_BOTTOM - yp - 20)
            elif b.get("picture_t") is not None or b.get("picture_file"):
                pic = picture(u, b, i, out, 940, SAFE_BOTTOM - yp - 20); layers.append(pop(pic, yp, t0 + te, dur - te, grow=0.06, pop_s=0.35))
            audios += [aw.with_start(t0), ae.with_start(t0 + te)]
        elif b["kind"] == "pair":                               # one row: the everyday word, then its formal twin as it is spoken
            al, ar = au[f"{i}-0"], au[f"{i}-1"]; g = 0.3; dur = al.duration + g + ar.duration + 0.4
            r = sum(x["kind"] == "pair" for x in u["beats"][:i]) - 1; y = ROW0 + r * ROWH
            if r == 0:                                          # the line between the columns comes with the first row (the hook text sits there before)
                ln = Image.new("RGBA", (px(4), px(npair * ROWH)), GREY + (160,)); table.append((ln, ROW0 - 10, t0, (XL + XR) / 2))
            table += [(text_img(b["card"]["left"], 84, WHITE, maxw=480), y, t0, XL), (text_img(b["card"]["right"], 84, YELLOW, maxw=480), y, t0 + al.duration + g, XR)]
            audios += [al.with_start(t0), ar.with_start(t0 + al.duration + g)]
        elif b["kind"] == "tip":                                # one line under the finished table
            a1 = au[f"{i}-0"]; dur = a1.duration + 0.9
            table.append((text_img(hl, 60, WHITE, maxw=860), ROW0 + npair * ROWH + 30, t0, (XL + XR) / 2)); audios.append(a1.with_start(t0))
        else:                                                   # cta
            if t_end is None: t_end = t0
            a1 = au[f"{i}-0"]; dur = a1.duration + CT
            ci = text_img(hl, 104, WHITE); layers.append(pop(ci, 560, t0, dur, grow=0.03))
            layers.append(pop(text_img(sub, 76, YELLOW), 560 + ci.height / K + 40, t0 + min(0.5, dur / 4), dur - min(0.5, dur / 4)))
            audios.append(a1.with_start(t0))
        print(f"beat {i} ({b['kind']}): {dur:.1f}s", flush=True); t0 += dur
    lb = u.get("loop_back", 0)                                  # loop ending (lab H60): no closing card - the last frames show the opening again (the struck-out phrase), so the replay starts without a break
    if lb and u["beats"][0]["kind"] == "hook":
        ps = u["beats"][0]["card"]["headline"].split("*"); y = 440
        if ps[0].strip(): p1 = text_img(ps[0].strip(), 110, WHITE); layers.append(pop(p1, y, t0, lb, pop_s=0.01)); y += p1.height / K + 5
        if len(ps) > 1:
            h2 = text_img(ps[1], 150, YELLOW, one_line=True); st = strike_img(h2.width, h2.height); layers.append(pop(h2, y, t0, lb, pop_s=0.01))
            layers.append(ImageClip(arr(st)).with_start(t0).with_duration(lb).with_position(((RW - st.width) / 2, y * K)))
        print(f"loop back: {lb:.1f}s", flush=True); t0 += lb
    total = t0
    layers += [pop(im, y, st, (t_end or total) - st, pop_s=0.2, x=x) for im, y, st, x in table]
    bg_words = [x["card"]["headline"].lower() for x in u["beats"] if x["kind"] == "word"] + [x["card"]["left"] for x in u["beats"] if x["kind"] == "pair"] or SYNONYMS
    bg = [ColorClip((RW, RH), color=BLACK).with_duration(total),
          scrolling(word_tile(u["id"] + "a", 20, (10, 20), (54, 90), bg_words), 38, total),        # far layer: small, slow
          scrolling(word_tile(u["id"] + "b", 8, (16, 28), (100, 150), bg_words), 75, total),      # near layer: big, faster
          ImageClip(arr(top_bar(u["series"], u["episode"]))).with_duration(total).with_position((0, 0))]
    final = CompositeVideoClip(bg + layers, size=(RW, RH)).with_duration(total).with_audio(CompositeAudioClip(audios).with_duration(total))
    dst = out / "final.mp4"
    final.write_videofile(str(dst), fps=30, codec="libx264", audio_codec="aac", audio_bitrate="160k", preset="medium",
                          ffmpeg_params=["-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart"], logger=None, threads=2)
    print(f"FINAL {dst} {total:.1f}s", flush=True)

if __name__ == "__main__": main(sys.argv[1])
