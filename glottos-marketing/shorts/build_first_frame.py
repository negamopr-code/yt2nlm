#!/usr/bin/env python3
"""Stop Saying lane — "first frame" Shorts builder (user 2026-10-11: "I do not see in your new produced videos any changes";
both expert corpora, consult Q5: the Shorts are swiped because frame 0 is a dark, static page of text, the first better word
comes at second 4-5, the voice is calm and every Short opens the same).

  .nlmvenv/bin/python shorts/build_first_frame.py shorts/units/<unit>.json

What is different from build_stop_saying.py, each point from the consult:
  - frame 0 is a PICTURE of the situation filling the whole screen (shorts/scene_from_nlm.py), moving from the first frame
    (a quick push-in, then a slow one); a new picture with every word = something changes every 1.5-2 s
  - the banned phrase stands struck out in frame 0, the first better word is on screen AND spoken at 0.0 (no lead-in sentence)
  - high contrast: black word on a yellow box (Marcus's "ugly banner"), the example white on black
  - only TWO text blocks in frame 0 (review round 1, both corpora: four were clutter): the struck-out phrase and the word;
    a progress bar of N segments + the number on the word box = the visible count; the open loop is a blue badge that
    comes with a LATER word, not in frame 0
  - a sound under the voice: pop on every text box, whoosh on every new picture, a quiet loop (sound_bed)
  - no logo bar; a small logo tile comes in after `logo_from` seconds (brand rule 09-27 kept, clutter in the first seconds gone)
  - no closing question: the last beat ("loop") shows picture 1 again and its sentence runs into the first word
  - unit "numbers": false (lab H71, textbook vs real): no red number on the word box - the boxes are an opinion, not a list
  - unit "ladder": true (lab H68, levels): no banned phrase; a staircase of N steps stands at the top from frame 0, one more
    step lights up with every word, and the word box carries the card's "level" ("LEVEL 1") in the red pill instead of the number
  - unit "quiz": true (lab H69, fill in the blank): beats {kind "quiz", card {sentence with "___", a, b, c}, answer "b"} - the
    sentence with the gap and a full bar stand from frame 0; the three choices pop in as the voice reads them while the bar
    runs down with a tick;
    {kind "answer", same card with the gap filled, mark "word"} - the right box turns green; {kind "example", card {tag?,
    sentence}, mark "w1 w2"} - one more line; {kind "loop"} - frame 0 again under the loop line
unit: {id, look? ("dark" = the word box white on dark instead of black on yellow), sub_maxw? (narrower example box, clear of the logo tile), voice "kokoro:<v>", speed, trim_silence, logo_from, beats: [{kind "word", card {headline, sub?, tag?; first beat also
       wrong (the banned phrase) and teaser}, speech "Word! Example." (or "Tag: headline!"), picture "state/..png"}, ...,
       {kind "loop", card {headline}, speech}]}
Text on screen = the language-approved unit text, character for character. Kokoro runs in its own process (no swap on the VM)."""
import json, math, re, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
from moviepy import AudioFileClip, ColorClip, CompositeAudioClip, CompositeVideoClip, ImageClip
sys.path.insert(0, str(Path(__file__).parent))
from build_stop_saying import ROOT, W, H, K, RW, RH, px, font, arr, logo_tile, speak, trim_silence, BLACK, YELLOW, WHITE, RED

def cover(path, cut_bottom=0.04, shift=0):
    """picture -> exactly RW x RH (cover fit); the bottom strip with the NotebookLM mark is cut off first. shift (design
    units) moves the picture DOWN so the word box does not cover its subject; the gap above is filled from its top rows"""
    im = Image.open(path).convert("RGB"); im = im.crop((0, 0, im.width, int(im.height * (1 - cut_bottom))))
    k = max(RW / im.width, RH / im.height); im = im.resize((math.ceil(im.width * k), math.ceil(im.height * k)), Image.LANCZOS)
    x, y = (im.width - RW) // 2, (im.height - RH) // 2; im = im.crop((x, y, x + RW, y + RH))
    if shift:
        d = px(shift); o = Image.new("RGB", (RW, RH)); o.paste(im.crop((0, 0, RW, 6)).resize((RW, d), Image.BILINEAR), (0, 0)); o.paste(im, (0, d)); im = o
    return im

def sound_bed(events, total, music, path, sr=44100):
    """the track under the voice (consult round 1, traffic corpus: a silent pop-in is half the stimulation, and a synthetic
    voice with no music and no effects sounds more synthetic): a soft pop on every text box, a short whoosh on every new
    picture, and a quiet upbeat loop made here from sines and noise (nothing licensed). The loop's tempo is set so the video
    is a whole number of bars, so the replay does not jump."""
    import wave
    n = int(total * sr); x = np.zeros(n); rnd = np.random.default_rng(7)
    def add(t, y, g):
        i = int(t * sr); y = y[:max(0, n - i)]; x[i:i + len(y)] += g * y
    tt = lambda d: np.arange(int(d * sr)) / sr
    def pop():
        t = tt(0.07); return np.sin(2 * np.pi * (520 * t + 2600 * t * t)) * np.exp(-t / 0.018)
    def whoosh():
        t = tt(0.22); w = rnd.standard_normal(len(t)); w = np.convolve(w, np.ones(24) / 24, "same") - np.convolve(w, np.ones(200) / 200, "same")
        return w * np.sin(np.pi * t / 0.22) ** 2 * 3
    def ding():
        t = tt(0.45); return (np.sin(2 * np.pi * 880 * t) + 0.6 * np.sin(2 * np.pi * 1318.5 * np.maximum(t - 0.09, 0)) * (t > 0.09)) * np.exp(-t / 0.14)
    def tick():
        t = tt(0.03); return np.sin(2 * np.pi * 1900 * t) * np.exp(-t / 0.006)
    snd = {"pop": (pop, 0.16), "ding": (ding, 0.12), "tick": (tick, 0.10), "whoosh": (whoosh, 0.12)}
    for t, kind in events: add(t, snd[kind][0](), snd[kind][1])
    if music:
        bars = max(1, round(total * 118 / 60 / 4)); beat = total / (bars * 4)                    # about 118 bpm, whole bars
        def kick():
            t = tt(0.16); return np.sin(2 * np.pi * (48 * t + 60 * 0.045 * (1 - np.exp(-t / 0.045)))) * np.exp(-t / 0.07)
        def hat():
            t = tt(0.04); w = rnd.standard_normal(len(t)); return (w - np.convolve(w, np.ones(8) / 8, "same")) * np.exp(-t / 0.012)
        def pluck(f):
            t = tt(0.32); return (np.sin(2 * np.pi * f * t) + 0.35 * np.sin(4 * np.pi * f * t) + 0.12 * np.sin(6 * np.pi * f * t)) * np.exp(-t / 0.11)
        C = [261.63, 329.63, 392.0, 523.25, 392.0, 329.63, 440.0, 392.0]; F = [349.23, 440.0, 523.25, 698.46, 523.25, 440.0, 587.33, 523.25]
        for bi in range(bars * 4):
            add(bi * beat, kick(), music * 1.1); add((bi + 0.5) * beat, hat(), music * 0.35)
            seq = C if (bi // 4) % 2 == 0 else F
            for h in (0, 1): add((bi + h / 2) * beat, pluck(seq[(bi % 4) * 2 + h]), music * 0.55)
            if bi % 4 == 0: add(bi * beat, pluck((130.81 if seq is C else 174.61)) , music * 0.8)
    x = np.clip(x, -1, 1)
    with wave.open(str(path), "wb") as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((x * 32767).astype(np.int16).tobytes())
    return path

def kenburns(im, start, dur, punch=0.07, drift=0.09):
    """full-frame picture that moves from its first frame: a quick push-in (0.3 s), then a slow one"""
    def sc(t): return 1 + punch * (1 - math.exp(-t / 0.12)) + drift * t / max(dur, 1)
    return (ImageClip(arr(im)).with_start(start).with_duration(dur).resized(sc)
            .with_position(lambda t: ((RW - RW * sc(t)) / 2, (RH - RH * sc(t)) * 0.45)))

def box(text, size, fg, bg, maxw=W - 110, pad=(44, 22), radius=34, strike=False, alpha=255):
    """text on a filled rounded box; size, maxw, pad in design units -> real-pixel image"""
    d0 = ImageDraw.Draw(Image.new("RGB", (1, 1))); tl = lambda t, f: d0.textlength(t, font=f) / K
    while size > 44 and max(tl(w_, font(size)) for w_ in text.split()) > maxw - 2 * pad[0]: size -= 6
    f = font(size); lines, cur = [], ""
    for w_ in text.split():
        t = (cur + " " + w_).strip()
        if tl(t, f) <= maxw - 2 * pad[0]: cur = t
        else: lines.append(cur); cur = w_
    lines.append(cur); lh = px(size * 1.2); tw = int(max(d0.textlength(l, font=f) for l in lines))
    wb, hb = tw + 2 * px(pad[0]), lh * len(lines) + 2 * px(pad[1])
    img = Image.new("RGBA", (wb, hb), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, wb - 1, hb - 1), px(radius), fill=bg + (alpha,))
    for i, l in enumerate(lines):
        x = (wb - d.textlength(l, font=f)) / 2; y = px(pad[1]) + i * lh - px(size * 0.06); d.text((x, y), l, font=f, fill=fg)
        if strike: d.line((x - px(10), y + lh * 0.66, x + d.textlength(l, font=f) + px(10), y + lh * 0.46), fill=RED + (255,), width=max(px(10), lh // 8))
    return img

def put(im, y, start, dur, pop_s=0.18, x=None, from_scale=0.6):
    """centred on x (design units) at top y; pops in from 60 % (pop_s <= 0.02 = simply there, for frame 0)"""
    c = ImageClip(arr(im)).with_start(start).with_duration(dur)
    if pop_s <= 0.02: return c.with_position(((W / 2 if x is None else x) * K - im.width / 2, y * K))
    def sc(t): return from_scale + (1 - from_scale) * min(1, t / pop_s) ** 0.5
    cx = (W / 2 if x is None else x) * K
    return c.resized(sc).with_position(lambda t: (cx - im.width * sc(t) / 2, y * K + im.height * (1 - sc(t)) / 2))

BLUE = (24, 104, 232)
def ban_box(lead, wrong):
    """one black box: the lead ("DON'T SAY") in white, the banned phrase struck out in red"""
    d0 = ImageDraw.Draw(Image.new("RGB", (1, 1))); pw, ph = px(36), px(18); size = 70
    while True:                                                 # a long phrase ("very expensive") gets a smaller font, so the box keeps its margin
        f = font(size); sp = d0.textlength(" ", font=f)
        wl, ww = (d0.textlength(lead, font=f) + sp if lead else 0), d0.textlength(wrong, font=f)
        if wl + ww + 2 * pw <= px(W - 100) or size <= 44: break
        size -= 2
    lh = px(size * 1.2)
    img = Image.new("RGBA", (int(wl + ww) + 2 * pw, lh + 2 * ph), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, img.width - 1, img.height - 1), px(30), fill=BLACK + (240,)); y = ph - px(4)
    if lead: d.text((pw, y), lead, font=f, fill=WHITE)
    d.text((pw + wl, y), wrong, font=f, fill=YELLOW)
    d.line((pw + wl - px(8), y + lh * 0.66, pw + wl + ww + px(8), y + lh * 0.46), fill=RED + (255,), width=px(11))
    return img

def ladder(n, k):
    """a staircase of N numbered steps rising to the right, the first k lit yellow (the levels ladder, lab H68)"""
    hh = px(176); img = Image.new("RGBA", (RW, hh), (0, 0, 0, 0)); d = ImageDraw.Draw(img); m, g = px(60), px(12); w = (RW - 2 * m - (n - 1) * g) / n; f = font(44)
    for i in range(n):
        x = m + i * (w + g); top = hh - px(60 + 112 * i / max(n - 1, 1)); lit = i < k
        d.rounded_rectangle((x - px(4), top - px(4), x + w + px(4), hh - 1), px(14), fill=BLACK + (255,))
        d.rounded_rectangle((x, top, x + w, hh - px(4) - 1), px(10), fill=(YELLOW if lit else (120, 120, 120)) + (255,))
        t = str(i + 1); d.text((x + w / 2 - d.textlength(t, font=f) / 2, hh - px(58)), t, font=f, fill=BLACK if lit else (60, 60, 60))
    return img

def word_box(text, k, look="yellow", level=None, number=True):
    """the better word: black on yellow, as big as the width allows, its number in a red disc on the corner
    (unit "look": "dark" = white on a dark strip, the channel's old colours - lab H65; nothing else changes)"""
    fg, bg = (WHITE, BLACK) if look == "dark" else (BLACK, YELLOW)
    b = box(text, 196 if len(text) <= 9 else 132 if len(text) <= 16 or not level else 100, fg, bg, maxw=W - 90, pad=(54, 20), radius=44); r = px(46)
    if level:                                                   # the ladder: "LEVEL 3" in a red pill on the corner instead of the number
        pl = box(level, 58, WHITE, RED, pad=(30, 10), radius=30); wd = max(b.width + r, pl.width)
        img = Image.new("RGBA", (wd, b.height + pl.height - px(14)), (0, 0, 0, 0)); img.alpha_composite(b, ((wd - b.width) // 2, pl.height - px(14))); img.alpha_composite(pl, ((wd - b.width) // 2 - min(r, (wd - b.width) // 2), 0)); return img
    if not number: return b                                     # unit "numbers": false (lab H71): the boxes are an opinion and its answer, not a counted list
    img = Image.new("RGBA", (b.width + r, b.height + r), (0, 0, 0, 0)); img.alpha_composite(b, (r, r)); d = ImageDraw.Draw(img)
    d.ellipse((0, 0, 2 * r, 2 * r), fill=RED + (255,), outline=WHITE + (255,), width=px(5)); f = font(56); t = str(k)
    d.text((r - d.textlength(t, font=f) / 2, r - px(35)), t, font=f, fill=WHITE); return img

def progress(n, k):
    """N segments, the first k filled yellow"""
    img = Image.new("RGBA", (RW, px(26)), (0, 0, 0, 0)); d = ImageDraw.Draw(img); m, g = px(60), px(14); w = (RW - 2 * m - (n - 1) * g) / n
    for i in range(n):
        x = m + i * (w + g); d.rounded_rectangle((x - px(3), 0, x + w + px(3), px(26) - 1), px(13), fill=BLACK + (255,))
        d.rounded_rectangle((x, px(4), x + w, px(22) - 1), px(9), fill=(YELLOW if i < k else (120, 120, 120)) + (255,))
    return img

GREEN, GREY = (22, 150, 70), (150, 150, 150)
def sent_box(text, mark=(), size=84, maxw=W - 90, pad=(48, 24)):
    """the quiz sentence, black on yellow: "___" is drawn as a thick gap line, a word in `mark` green and underlined"""
    d0 = ImageDraw.Draw(Image.new("RGB", (1, 1))); f = font(size); sp = d0.textlength(" ", font=f); gw = px(size * 2.6)
    wd = lambda t: gw + d0.textlength(t.replace("___", ""), font=f) if "___" in t else d0.textlength(t, font=f)
    lines, cur, cw = [], [], 0
    for t in text.split():
        if cur and cw + sp + wd(t) > px(maxw - 2 * pad[0]): lines.append(cur); cur, cw = [], 0
        cw += (sp if cur else 0) + wd(t); cur.append(t)
    lines.append(cur); lh = px(size * 1.24); tw = max(sum(wd(t) for t in l) + sp * (len(l) - 1) for l in lines)
    img = Image.new("RGBA", (int(tw) + 2 * px(pad[0]), lh * len(lines) + 2 * px(pad[1])), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, img.width - 1, img.height - 1), px(40), fill=YELLOW + (255,))
    for i, l in enumerate(lines):
        x = (img.width - sum(wd(t) for t in l) - sp * (len(l) - 1)) / 2; y = px(pad[1]) + i * lh - px(size * 0.04)
        for t in l:
            if "___" in t:
                d.rounded_rectangle((x, y + lh * 0.80, x + gw, y + lh * 0.80 + px(10)), px(5), fill=BLACK + (255,)); d.text((x + gw, y), t.replace("___", ""), font=f, fill=BLACK)
            else:
                hit = re.sub(r"\W", "", t).lower() in mark; d.text((x, y), t, font=f, fill=GREEN if hit else BLACK)
                if hit: ww = d0.textlength(re.sub(r"[.,!?]+$", "", t), font=f); d.rounded_rectangle((x, y + lh * 0.88, x + ww, y + lh * 0.88 + px(8)), px(4), fill=GREEN + (255,))
            x += wd(t) + sp
    return img

def opt_box(letter, text, state="plain", wb=660, hb=116):
    """one choice: the letter in a disc, the word; plain = white, right = green, dim = grey and half see-through"""
    bg, fg, al = {"plain": (WHITE, BLACK, 250), "right": (GREEN, WHITE, 255), "dim": (GREY, (70, 70, 70), 150)}[state]
    img = Image.new("RGBA", (px(wb), px(hb)), (0, 0, 0, 0)); d = ImageDraw.Draw(img); r = px(hb / 2 - 14)
    d.rounded_rectangle((0, 0, img.width - 1, img.height - 1), px(36), fill=bg + (al,), outline=BLACK + (al,), width=px(5))
    cx, cy = px(22) + r, img.height // 2; d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(WHITE if state == "right" else BLACK) + (al,))
    fl = font(56); d.text((cx - d.textlength(letter, font=fl) / 2, cy - px(36)), letter, font=fl, fill=GREEN if state == "right" else WHITE)
    f = font(72); d.text((cx + r + px(28), cy - px(47)), text, font=f, fill=fg + (255,)); return img

def quiz(u, out, au):
    """lab H69: the timeline of a fill-in-the-blank Short (see the module text)"""
    G = u.get("gap", 0.2); SY, OW, OS = 130, 660, 132
    pics = {b["picture"]: cover(ROOT / b["picture"], shift=b.get("picture_shift", 0)) for b in u["beats"] if b.get("picture")}
    q = u["beats"][0]; layers, audios, ev, t0 = [], [], [], 0.0
    def choices(card, y, start, dur, right=None, pop=False, step=0.0):
        for j, k in enumerate("abc"):                            # step > 0: each choice pops in as the voice reads it (review round 1: frame 0 = picture, sentence, bar)
            st = "plain" if right is None else "right" if k == right else "dim"; d = j * step
            layers.append(put(opt_box(k.upper(), card[k], st), y + j * OS, start + d, dur - d, pop_s=0.16 if step or (pop and st == "right") else 0.01, from_scale=0.8))
            if step: ev.append((start + d, "pop"))
        return y + 3 * OS
    def track(y, start, dur):
        im = Image.new("RGBA", (px(OW), px(26)), (0, 0, 0, 0)); ImageDraw.Draw(im).rounded_rectangle((0, 0, im.width - 1, im.height - 1), px(13), fill=BLACK + (255,))
        layers.append(put(im, y, start, dur, pop_s=0.01))
    def fill(y, start, dur, run=None):
        bw, bh = px(OW - 12), px(14); c = ColorClip((bw, bh), color=YELLOW).with_start(start).with_duration(dur)
        if run: c = c.resized(lambda t: (max(2, int(bw * (1 - min(1, t / run)))), bh))
        layers.append(c.with_position(((W - OW) / 2 * K + px(6), y * K + px(6))))
    for i, b in enumerate(u["beats"], 1):
        kind, card = b["kind"], b["card"]; a0, a1 = au[f"{i}-0"], au.get(f"{i}-1")
        if kind == "quiz":                                       # frame 0: picture, sentence with the gap, three choices, the bar full; it runs down while the choices are read
            te = a0.duration + G; cd = max(u.get("countdown", 3.0), a1.duration + 0.4); dur = te + cd
            layers.append(kenburns(pics[b["picture"]], t0, dur)); ev.append((t0, "whoosh"))
            sb = sent_box(card["sentence"]); layers.append(put(sb, SY, t0, dur, pop_s=0.01)); y = choices(card, SY + sb.height / K + 22, t0 + te, cd, step=a1.duration * 0.36)
            track(y + 6, t0, dur); fill(y + 6, t0, te); fill(y + 6, t0 + te, cd, run=cd); ev += [(t0 + te + x * 0.5, "tick") for x in range(int(cd / 0.5) + 1)]   # a tick under the running bar
            audios += [a0.with_start(t0), a1.with_start(t0 + te)]
        elif kind == "answer":                                   # the right box turns green as the word is said, the sentence is whole
            dur = a0.duration + b.get("tail", 0.5); layers.append(kenburns(pics[b["picture"]], t0, dur)); ev += [(t0, "whoosh"), (t0, "ding")]
            sb = sent_box(card["sentence"], b.get("mark", "").split()); layers.append(put(sb, SY, t0, dur, pop_s=0.01)); choices(card, SY + sb.height / K + 22, t0, dur, right=b["answer"], pop=True)
            audios.append(a0.with_start(t0))
        elif kind == "example":                                  # one more line, the two look-alike words marked
            dur = a0.duration + b.get("tail", 0.6); layers.append(kenburns(pics[b["picture"]], t0, dur)); ev += [(t0, "whoosh"), (t0, "pop")]; y = SY
            if card.get("tag"): tg = box(card["tag"], 60, WHITE, RED, pad=(30, 12), radius=30); layers.append(put(tg, y, t0, dur, pop_s=0.16)); y += tg.height / K + 14
            layers.append(put(sent_box(card["sentence"], b.get("mark", "").split()), y, t0, dur, pop_s=0.16)); audios.append(a0.with_start(t0))
        else:                                                    # loop: frame 0 again (so the replay does not jump), the loop line under the bar
            dur = a0.duration + u.get("loop_tail", 0.1); layers.append(kenburns(pics[q["picture"]], t0, dur, punch=0.0, drift=0.0))
            sb = sent_box(q["card"]["sentence"]); layers.append(put(sb, SY, t0, dur, pop_s=0.01)); y = choices(q["card"], SY + sb.height / K + 22, t0, dur)
            track(y + 6, t0, dur); fill(y + 6, t0, dur)
            layers.append(put(box(card["headline"], 84, WHITE, BLACK, pad=(40, 22), alpha=235), y + 60, t0, dur, pop_s=0.16)); ev.append((t0, "pop")); audios.append(a0.with_start(t0))
        print(f"beat {i} ({kind}): {dur:.2f}s  starts {t0:.2f}", flush=True); t0 += dur
    return layers, audios, ev, t0

# ---- lab repair 2026-10-14 (user go-ahead): unit "promise": true -------------------------------------------------------
# WHY (measured 10-14): the 7 H62/H63 Shorts of this builder got 0/7 Shorts-feed groups vs 44/56 for the old builder.
# Viewer critic + both corpora: the answer stood in frame 0 (no open loop), 10-15 s needed >100 % retention, no gap to
# repeat, the same clay boy in every picture, and a "#N: the idiom natives use" badge on words that are not idioms.
# This mode goes back to the winners' opening (l1-very-fast-h60, l1-very-nice-h59, stop-saying-l1-very-big-v2) and adds
# what the critics asked for. Old units do not set "promise" and render exactly as before.
#   frame 0-2 s = the promise: "Stop saying" / "very X" (the strike runs across it as it is said) / "N better words";
#                 the first answer word is not before ~2.5 s (beat 1 kind "hook", speech "Stop saying very x. Here are ...")
#   word beats   = word + one usage line ("use": when/why) + a picture (a different scene and style per word, no mascot),
#                  then the example; "pause_after_word" and "tail_after_example" leave time to repeat (default 0.8 / 1.0 s)
#   idiom        = a word beat's card "idiom": true shows the red "idiom" tag AND the idiom text together; the tag and any
#                  "badge" are drawn ONLY on such a beat (the H62 bug stamped "#4: the idiom natives use" on plain words)
#   end beat     = kind "end": card {headline, sub, sub2} = the question + "Comment your own word" line, then
#                  "loop_back" seconds of frame 0 again so the replay starts without a jump
#   sound        = the winners' voice (unit voice, e.g. kokoro:am_michael at 1.05), "music" 0 (no bed), soft pops only
#   text         = at most 3 lines of about 5 words on screen at once, large (word 170, example 72, usage 58)
def promise_main(u, out):
    from build_stop_saying import text_img, strike_img, word_tile, scrolling, top_bar, SAFE_BOTTOM
    voice, speed = u["voice"].split(":", 1)[1], u.get("speed", 1.05); jobs = []
    for i, b in enumerate(u["beats"], 1):
        s = b["speech"]; m = re.search(r"[:.!?]\s", s) if b["kind"] in ("hook", "word", "end") else None
        if m: a, c = s[:m.start() + 1], s[m.end():]; parts = [a[:-1] + "." if a.endswith(":") else a, c[:1].upper() + c[1:] if b["kind"] != "word" else c]
        else: parts = [s]
        if b["kind"] == "word" and u.get("speak_use") and len(parts) == 2:   # round 2 (10-14, critic): "Word: usage. Example." -> word / usage / example, three clips
            m2 = re.search(r"[.!?]\s", parts[1])
            if m2: parts = [parts[0], parts[1][:m2.start() + 1], parts[1][m2.end():]]
        for k, t in enumerate(parts): jobs.append({"key": f"{i}-{k}", "text": t, "voice": voice, "speed": speed, "out": str(out / f"b{i:02d}-{k}.wav")})
    if u.get("trim_silence"):
        speak(jobs, out)
        for j in jobs: trim_silence(j["out"], u["trim_silence"])
        au = {j["key"]: AudioFileClip(str(o) if (o := out / f"override-{j['key']}.wav").exists() else j["out"]) for j in jobs}
    else: au = speak(jobs, out)
    P, TL, HG = u.get("pause_after_word", 0.8), u.get("tail_after_example", 1.0), u.get("hook_gap", 0.3)
    # H102 critic 2026-10-23: 20.7 s instead of 13-16 s, ~4.9 s of it silent holds (1.2 s after every example = swipe points at 7 s
    # and 12 s). Units copy these numbers from older units, so the builder caps them; "slow_pauses": true in a unit keeps its own.
    if not u.get("slow_pauses"):
        P, TL, HG = min(P, 0.2), min(TL, 0.35), min(HG, 0.2)
        for k, c in (("hook_tail", 0.2), ("end_tail", 0.3), ("use_gap", 0.1), ("loop_back", 0.5)):
            if u.get(k) is not None: u[k] = min(u[k], c)
        print(f"pauses capped (H102 critic): after word {P}, after example {TL}, hook gap {HG}", flush=True)
    words = [b for b in u["beats"] if b["kind"] == "word"]; n = len(words); hook = u["beats"][0]
    wrong = re.search(r'\*"?([^*"]+)"?\*', hook["card"]["headline"]); wrong = wrong[1] if wrong else hook["card"]["headline"]
    layers, audios, ev, t0 = [], [], [], 0.0
    def card_pic(path, maxw=820, maxh=560, cut_bottom=0.05):
        im = Image.open(ROOT / path).convert("RGB"); im = im.crop((0, 0, im.width, int(im.height * (1 - cut_bottom))))   # NotebookLM mark sits in the bottom strip
        k = max(px(maxw) / im.width, px(maxh) / im.height); im = im.resize((math.ceil(im.width * k), math.ceil(im.height * k)), Image.LANCZOS)
        x, y = (im.width - px(maxw)) // 2, int((im.height - px(maxh)) * 0.4); im = im.crop((x, y, x + px(maxw), y + px(maxh))).convert("RGBA")
        bd = px(8); m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), px(36), fill=255)
        fr = Image.new("RGBA", (im.width + 2 * bd, im.height + 2 * bd), (0, 0, 0, 0)); ImageDraw.Draw(fr).rounded_rectangle((0, 0, fr.width - 1, fr.height - 1), px(44), fill=YELLOW + (255,))
        fr.paste(im, (bd, bd), m); return fr
    HY = 440                                                            # the promise block, as in the winners
    p1 = text_img(hook["card"]["headline"].split("*")[0].strip(), 110, WHITE); h2 = text_img(f'"{wrong}"', 150, YELLOW, one_line=True)
    y2 = HY + p1.height / K + 5; y3 = y2 + h2.height / K + 30; st = strike_img(h2.width, h2.height)
    def frame0(start, dur):                                             # "Stop saying" / "very x" (no strike yet) - frame 0 and the loop back
        return [put(p1, HY, start, dur, pop_s=0.01), put(h2, y2, start, dur, pop_s=0.01)]
    for i, b in enumerate(u["beats"], 1):
        if b["kind"] == "hook":
            a1, a2 = au[f"{i}-0"], au.get(f"{i}-1"); dur = a1.duration + HG + (a2.duration if a2 else 0) + u.get("hook_tail", 0.35)
            layers += frame0(t0, dur)
            s0, s1 = u.get("strike_at", (0.45, 0.95)); steps = 8         # the red line runs across "very x" while it is said
            for k in range(1, steps + 1):
                w_ = max(2, int(st.width * k / steps)); ts = t0 + s0 + (s1 - s0) * (k - 1) / steps
                layers.append(ImageClip(arr(st.crop((0, 0, w_, st.height)))).with_start(ts).with_duration((s1 - s0) / steps if k < steps else dur - (ts - t0)).with_position(((RW - st.width) / 2, y2 * K)))
            sub_at = a1.duration + HG; layers.append(put(text_img(hook["card"]["sub"], 84, WHITE), y3, t0 + sub_at, dur - sub_at, pop_s=0.16)); ev.append((t0 + sub_at, "pop"))
            audios += [a1.with_start(t0)] + ([a2.with_start(t0 + a1.duration + HG)] if a2 else [])
        elif b["kind"] == "word":
            k = words.index(b) + 1; aw, ae = au[f"{i}-0"], au.get(f"{i}-1"); te = aw.duration + P
            au_use = au.get(f"{i}-2") and ae                          # speak_use: clip 1 = the usage line, clip 2 = the example
            if au_use: tu = aw.duration + u.get("use_gap", 0.15); ae = au[f"{i}-2"]; te = tu + au_use.duration + P
            dur = te + (ae.duration if ae else 0) + b.get("tail", TL); c = b["card"]; idiom = bool(c.get("idiom"))
            layers.append(ImageClip(arr(progress(n, k))).with_start(t0).with_duration(dur).with_position((0, px(330))))
            y = 385
            if idiom:                                                   # the tag only on a real idiom, and the idiom text with it from the first frame of the beat
                tg = box("idiom", 52, WHITE, RED, pad=(28, 10), radius=28); layers.append(put(tg, y, t0, dur, pop_s=0.16)); y += tg.height / K + 8
            hl = c["headline"]; hi = text_img(hl, 170 if len(hl) <= 11 else 120 if len(hl) <= 18 else 92, YELLOW); layers.append(put(hi, y, t0, dur, pop_s=0.16)); ev.append((t0, "pop"))
            y += hi.height / K + 4
            if c.get("use"):
                us = 58
                if u.get("speak_use"):                                  # round 2: the usage line stays ONE line (max 3 lines on screen): smaller font, never a wrap
                    d0 = ImageDraw.Draw(Image.new("RGB", (1, 1)))
                    while us > 44 and d0.textlength(c["use"], font=font(us)) / K > W - 160 - 68: us -= 2
                ua = (tu if au_use else 0.25); ui = box(c["use"], us, WHITE, (40, 40, 40), maxw=W - 160, pad=(34, 14), radius=30, alpha=230); layers.append(put(ui, y, t0 + ua, dur - ua, pop_s=0.16)); y += ui.height / K + 22
            if idiom and c.get("badge"): layers.append(put(box(c["badge"], 46, WHITE, BLUE, pad=(30, 14), radius=30), y, t0, dur, pop_s=0.16)); y += 70
            sy = u.get("example_y", 1390)
            if b.get("picture"):
                pic = card_pic(b["picture"], maxw=900, maxh=min(680, sy - 24 - y)); layers.append(put(pic, y, t0 + 0.1, dur - 0.1, pop_s=0.25, from_scale=0.85))
            if c.get("sub"): si = text_img(c["sub"], 72 if len(c["sub"]) <= 26 else 62, WHITE, one_line=bool(u.get("speak_use"))); layers.append(put(si, sy, t0 + te, dur - te, pop_s=0.16)); ev.append((t0 + te, "pop"))
            audios += [aw.with_start(t0)] + ([ae.with_start(t0 + te)] if ae else []) + ([au_use.with_start(t0 + tu)] if au_use else [])
        else:                                                           # end: the question, "Comment your own word ...", then frame 0 again; one line each = 3 lines
            a1, a2 = au[f"{i}-0"], au.get(f"{i}-1"); g = 0.25; dur = a1.duration + g + (a2.duration if a2 else 0) + u.get("end_tail", 0.6)
            c = b["card"]; q = text_img(c["headline"], 66, WHITE, maxw=1010); layers.append(put(q, 520, t0, dur, pop_s=0.16)); ev.append((t0, "pop"))
            yy = 520 + q.height / K + 40
            for j, key in enumerate(("sub", "sub2")):
                if c.get(key): si = text_img(c[key], 66, YELLOW, maxw=1010); at = a1.duration + g; layers.append(put(si, yy, t0 + at, dur - at, pop_s=0.16)); yy += si.height / K + 6
            ev.append((t0 + a1.duration + g, "pop"))
            audios += [a1.with_start(t0)] + ([a2.with_start(t0 + a1.duration + g)] if a2 else [])
        print(f"beat {i} ({b['kind']}): {dur:.2f}s  starts {t0:.2f}", flush=True); t0 += dur
    lb = u.get("loop_back", 0.6)
    if lb: layers += frame0(t0, lb); print(f"loop back: {lb:.1f}s", flush=True); t0 += lb
    bgw = [wrong] * 3                                                   # the flying background words = the banned phrase only (the winners flew the answers - no give-away here)
    bg = [scrolling(word_tile(u["id"] + "a", 12, (8, 14), (54, 80), bgw), 38, t0),          # one faint layer only (smoke test 10-14: two layers were clutter behind the text)
          ImageClip(arr(top_bar(u.get("series", "Stop Saying"), None))).with_duration(t0).with_position((0, 0))]
    finish(u, out, bg + layers, audios, ev, t0)
# ---------------------------------------------------------------------------------------------------------------------------

def main(path):
    import lang_gate
    u = json.load(open(path)); ok, _ = lang_gate.verify(u)
    if not ok and "--skip-language-gate" not in sys.argv: sys.exit(f"REFUSED: {path} has no valid English-language approval")
    out = ROOT / "state/shorts" / u["id"]; out.mkdir(parents=True, exist_ok=True)
    if (out / "final.mp4").exists() and "--overwrite" not in sys.argv: sys.exit(f"REFUSED: {u['id']} already rendered (new id)")
    if u.get("promise"): return promise_main(u, out)                   # lab repair 2026-10-14 (see promise_main)
    voice, speed = u["voice"].split(":", 1)[1], u.get("speed", 1.15); jobs = []
    for i, b in enumerate(u["beats"], 1):
        m = re.search(r"[.!?]\s" if u.get("ladder") else r"[:.!?]\s", b["speech"]) if b["kind"] in ("word", "quiz") and not b.get("one_clip") else None
        parts = [b["speech"][:m.start() + 1], b["speech"][m.end():]] if m else [b["speech"]]
        for k, t in enumerate(parts): jobs.append({"key": f"{i}-{k}", "text": t, "voice": b.get("voice", voice), "speed": b.get("speed", speed), "out": str(out / f"b{i:02d}-{k}.wav"), "trim": b.get("trim_silence", u.get("trim_silence", 0.03))})
    speak(jobs, out)
    for j in jobs: trim_silence(j["out"], j["trim"])                # a beat's own "trim_silence" keeps a quiet first word ("The ...") the cut would eat
    au = {j["key"]: AudioFileClip(j["out"]) for j in jobs}
    if u.get("quiz"): return finish(u, out, *quiz(u, out, au))
    G, TAIL = u.get("gap", 0.2), u.get("tail", 0.35)
    words = [b for b in u["beats"] if b["kind"] == "word"]; n = len(words)
    pics = {b["picture"]: cover(ROOT / b["picture"], shift=b.get("picture_shift", 0)) for b in words}
    c0 = u["beats"][0]["card"]                                    # the banned phrase lives in the first card, so the language gate covers it
    lad = u.get("ladder"); bar = ladder if lad else progress; BY = 96 if lad else 120
    ban = None if lad else ban_box(c0.get("wrong_lead", ""), c0["wrong"]); YW, YS = (290 if lad else 180 + ban.height / K), 1500
    layers, audios, ev, t0 = [], [], [], 0.0
    for i, b in enumerate(u["beats"], 1):
        first = t0 == 0.0
        if b["kind"] == "word":
            k = words.index(b) + 1; aw, ae = au[f"{i}-0"], au.get(f"{i}-1"); te = aw.duration + G
            dur = (te + ae.duration if ae else aw.duration) + b.get("tail", TAIL)   # a beat's own "tail" holds the payoff longer (H68: Level 5)
            layers.append(kenburns(pics[b["picture"]], t0, dur)); ev.append((t0, "whoosh"))
            layers.append(ImageClip(arr(bar(n, k))).with_start(t0).with_duration(dur).with_position((0, px(BY))))
            own = b["card"].get("tag"); hl = b["card"]["headline"]; ht = te if own else 0.0      # a beat's own tag (red) is SPOKEN first; its headline comes when it is said
            if u.get("idiom_fix") and own: ht = 0.0                  # lab repair 10-14 (opt-in): the idiom beat shows the idiom text from its first frame, not the tag alone
            wi = word_box(hl, k, u.get("look", "yellow"), b["card"].get("level"), u.get("numbers", True)); layers.append(put(wi, YW, t0 + ht, dur - ht, pop_s=0.01 if first else 0.16)); yb = YW + wi.height / K + 14
            if not first: ev.append((t0 + ht, "pop"))
            if own: layers.append(put(box(own, 60, WHITE, RED, pad=(30, 12), radius=30), YW + 40, t0, ht, pop_s=0.16))
            if b["card"].get("badge") and not (u.get("idiom_fix") and "idiom" in b["card"]["badge"].lower() and not own):   # repair 10-14 (opt-in): no idiom badge on a plain word
                bt = b.get("badge_at", 0.0) * dur; layers.append(put(box(b["card"]["badge"], 46, WHITE, BLUE, pad=(30, 14), radius=30), yb, t0 + bt, dur - bt, pop_s=0.01 if first and not bt else 0.16)); ev.append((t0 + bt, "pop"))
            if b["card"].get("sub"):
                si = box(b["card"]["sub"], 70, WHITE, BLACK, maxw=u.get("sub_maxw", W - 110), pad=(40, 22), alpha=235); layers.append(put(si, b.get("sub_y", YS) - si.height / K, t0 + te, dur - te, pop_s=0.16))   # a beat's own "sub_y" lifts the example off a face; ev.append((t0 + te, "pop"))
            audios += [aw.with_start(t0)] + ([ae.with_start(t0 + te)] if ae else [])
        else:                                                    # loop: picture 1 again, its sentence runs into the first words
            a1 = au[f"{i}-0"]; dur = a1.duration + u.get("loop_tail", 0.1); w0 = words[0]
            layers.append(kenburns(pics[w0["picture"]], t0, dur, punch=0.0, drift=0.0))
            if not lad and u.get("loop_whoosh", True): ev.append((t0, "whoosh"))             # ladder (H68): the whoosh lay on the "S" of "So don't stop at" - heard as "Who don't"
            layers.append(ImageClip(arr(bar(n, n))).with_start(t0).with_duration(dur).with_position((0, px(BY))))
            layers.append(put(box(b["card"]["headline"], 84 if lad else 96, WHITE, BLACK, pad=(40, 22), alpha=235), YW + 20, t0, dur, pop_s=0.16))
            audios.append(a1.with_start(t0))
        print(f"beat {i} ({b['kind']}): {dur:.2f}s  starts {t0:.2f}", flush=True); t0 += dur
    if ban: layers.append(put(ban, 168, 0, t0, pop_s=0.01))                                          # the struck-out phrase: on from frame 0 to the end
    finish(u, out, layers, audios, ev, t0)

def finish(u, out, layers, audios, ev, total):
    """logo tile, the sound under the voice, the file"""
    lf = u.get("logo_from", 2.0); lt = logo_tile(92)                       # promise mode (repair 10-14): no tile, the logo is in the winners' top bar
    if lf < total and not u.get("promise"): layers.append(ImageClip(arr(lt)).with_start(lf).with_duration(total - lf).with_position((px(24), px(1436))))
    if u.get("sfx", True) or u.get("music"):
        audios.append(AudioFileClip(str(sound_bed(ev if u.get("sfx", True) else [], total, u.get("music", 0), out / "bed.wav"))).with_start(0))
    final = CompositeVideoClip([ColorClip((RW, RH), color=BLACK).with_duration(total)] + layers, size=(RW, RH)).with_duration(total).with_audio(CompositeAudioClip(audios).with_duration(total))
    dst = out / "final.mp4"
    final.write_videofile(str(dst), fps=30, codec="libx264", audio_codec="aac", audio_bitrate="160k", preset="medium",
                          ffmpeg_params=["-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart"], logger=None, threads=2)
    print(f"FINAL {dst} {total:.1f}s", flush=True)

if __name__ == "__main__": main(sys.argv[1])
