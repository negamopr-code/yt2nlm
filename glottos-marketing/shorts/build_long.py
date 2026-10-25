#!/usr/bin/env python3
"""Long-video builder, 16:9 (user 2026-09-30: "Stop saying VERY: 30 better words", ~8 min, Marcus double-dip).

  .nlmvenv/bin/python shorts/build_long.py shorts/units/long-stop-saying-very-v1.json [--overwrite]

Slides, not motion: every beat is a few still STATES (e.g. word -> + meaning -> + example + picture) whose durations
equal the narration clips, joined with ffmpeg (concat demuxer) - low memory (the VM has no swap), restartable, and the
look of the channels that win this format (static picture + voice). Same brand as the Shorts (black, yellow, logo).
Text on screen = the language-approved unit text, character for character (lang_gate.verify, else REFUSED).
Pictures per word: the family's Short (state/shorts/<unit>/pic-NN.png, NN = that word's beat) - "big" = the winning
Short kvCFmAhXcH8 (stop-saying-l1-very-big-v2).
Kinds: hook, section, word, quiz ('|' = think pause with a 3-2-1 countdown, then the answer; three options, card "sub" /
"note" and unit "countdown" = the quiz video of lab H72), tip/cta + "clip": <library clip id> (a muted public-domain
film clip plays in the middle of the card, T02 2026-10-17), shadow ('|' = a
"your turn" pause after each sentence, 1.4 x its length + 0.8 s), tip, cta.
Writes state/shorts/<id>/final.mp4, chapters.txt (YouTube chapters) and thumbnail.jpg.
Search-phrase videos (lab H19, 2026-10-04): the unit carries "tag" (top-left line = the search phrase), "pic_units"
{family: unit name} for families outside FAMILY_UNITS, a "label" on each section beat (tag + chapter names) and
"thumb.lines" [[text, "white"|"yellow"], ...]; without "tag" everything is the Stop-saying-very look as before."""
import json, re, subprocess, sys, wave
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
W, H = 1920, 1080                                 # DESIGN units: every coordinate and size below is written for 1920x1080 ...
K = 4 / 3                                          # ... and drawn natively at K x that (user 2026-10-05: "videos should be in 1440 quality and not in 1080")
RW, RH = int(W * K), int(H * K)                    # 2560 x 1440 = the real frame
def sc(v): return int(v * K + 0.5)
BLACK, YELLOW, WHITE, GREY, RED, GREEN, DARK = (12, 12, 12), (255, 212, 0), (255, 255, 255), (150, 150, 150), (232, 44, 32), (70, 200, 90), (40, 40, 40)
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
LOGO = ROOT / "state/brand/awf-logo-channel.jpg"
TTSPY = str(ROOT / ".ttsvenv/bin/python")
FF = str(ROOT / ".nlmvenv/lib/python3.11/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2")
FAMILY_UNITS = {"big": "l1_verybig_v2", "good": "l1-very-good-v1", "happy": "l1-very-happy-v1", "tired": "l1-very-tired-v1",
                "bad": "l1-very-bad-v1", "small": "l1-very-small-v1",
                "sad": "l1-very-sad-v1", "angry": "l1-very-angry-v1", "beautiful": "l1-very-beautiful-v1",   # Vol. 2 (user 2026-10-03)
                "scared": "l1-very-scared-v1", "important": "l1-very-important-v1", "interesting": "l1-very-interesting-v1"}
SR = 24000
CLIP_BOX = (260, 245, 1660, 900)                  # design units: where a film clip plays on a clip beat

def font(s, bold=True): return ImageFont.truetype(FB if bold else FR, sc(s))     # design size -> real pixels
def rfont(s, bold=True): return ImageFont.truetype(FB if bold else FR, s)        # unscaled (thumbnails are 1280x720 as before)
class D:
    """ImageDraw in DESIGN units on a real-size image: coordinates, radii and line widths are scaled by K on the way in,
    text widths are returned in design units - so the layout code keeps its 1920x1080 numbers and nothing is upscaled."""
    def __init__(self, img): self.d = ImageDraw.Draw(img)
    def text(self, xy, t, font=None, fill=None): self.d.text((xy[0] * K, xy[1] * K), t, font=font, fill=fill)
    def textlength(self, t, font=None): return self.d.textlength(t, font=font) / K
    def rounded_rectangle(self, box, radius=0, fill=None, outline=None, width=1):
        self.d.rounded_rectangle(tuple(v * K for v in box), sc(radius), fill=fill, outline=outline, width=max(1, sc(width)))
    def rectangle(self, box, fill=None): self.d.rectangle(tuple(v * K for v in box), fill=fill)
    def line(self, xy, fill=None, width=1): self.d.line(tuple(v * K for v in xy), fill=fill, width=max(1, sc(width)))
def put(img, fr, x, y, boxw, boxh):
    """paste picture `fr` (real pixels) centred in the DESIGN box (x, y, boxw, boxh)"""
    img.paste(fr, (int((x + (boxw - fr.width / K) / 2) * K), int((y + (boxh - fr.height / K) / 2) * K)), fr)

# ---------- pictures ----------
def pkey(w):   # one normalisation for storing AND looking up a word's picture (2026-10-18: "You've got this" was stored as "youve got this")
    return re.sub(r"[^a-z -]", "", w.lower()).strip()
def family_pictures(extra=None):
    pics = {}
    for fam, uname in {**FAMILY_UNITS, **(extra or {})}.items():
        u = json.load(open(ROOT / f"shorts/units/{uname}.json"))
        for i, b in enumerate(u["beats"], 1):
            if b.get("kind", "word" if 1 < i < len(u["beats"]) else "") != "word": continue
            p = ROOT / f"state/shorts/{u['id']}/pic-{i:02d}.png"
            if p.exists(): pics[(fam, pkey(b["card"]["headline"]))] = p
    return pics

def framed(p, maxw, maxh):
    """maxw, maxh in design units; the returned picture is in real pixels (resized once, straight from the source)"""
    b = sc(7)
    im = Image.open(p).convert("RGBA"); k = min(maxw * K / im.width, maxh * K / im.height)
    im = im.resize((int(im.width * k), int(im.height * k)), Image.LANCZOS)
    m = Image.new("L", im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), sc(28), fill=255)
    fr = Image.new("RGBA", (im.width + 2 * b, im.height + 2 * b), (0, 0, 0, 0))
    ImageDraw.Draw(fr).rounded_rectangle((0, 0, fr.width - 1, fr.height - 1), sc(34), fill=YELLOW + (255,))
    fr.paste(im, (b, b), m); return fr

# ---------- text ----------
def wrap(text, f, maxw):
    d0 = ImageDraw.Draw(Image.new("RGB", (1, 1))); lines, cur = [], ""
    for w_ in text.split():
        t = (cur + " " + w_).strip()
        if d0.textlength(t, font=f) <= maxw or not cur: cur = t
        else: lines.append(cur); cur = w_
    return lines + [cur]

def draw_text(img, text, xy, size, color, maxw, align="left", bold=True, hl=None, hl_color=YELLOW, spacing=1.22):
    """wrapped text; hl = phrase whose words are drawn in hl_color (the target word inside an example)"""
    d = D(img); f = font(size, bold); x0, y = xy; lh = int(size * spacing)
    hlw = [re.sub(r"[^a-z']", "", w_.lower()) for w_ in (hl or "").split()]
    toks = text.split(); marks = [False] * len(toks)
    for i in range(len(toks) - len(hlw) + 1):
        if hlw and [re.sub(r"[^a-z']", "", t.lower()) for t in toks[i:i + len(hlw)]] == hlw:
            for k in range(i, i + len(hlw)): marks[k] = True
    lines, cur = [], []
    for t, m in zip(toks, marks):
        cand = " ".join(x for x, _ in cur + [(t, m)])
        if cur and d.textlength(cand, font=f) > maxw: lines.append(cur); cur = [(t, m)]
        else: cur.append((t, m))
    lines.append(cur)
    for ln in lines:
        wline = d.textlength(" ".join(t for t, _ in ln), font=f)
        x = x0 + (maxw - wline) / 2 if align == "center" else x0
        for t, m in ln:
            d.text((x, y), t, font=f, fill=hl_color if m else color); x += d.textlength(t + " ", font=f)
        y += lh
    return y

def strike(img, x0, y0, x1, y1, width=14):
    D(img).line((x0, y0 + (y1 - y0) * 0.62, x1, y0 + (y1 - y0) * 0.38), fill=RED, width=width)

def pill(img, text, cx, y, size, fg, bg, dim=False, struck=False):
    d = D(img); f = font(size); w = d.textlength(text, font=f); pad = size * 0.7
    box = (cx - w / 2 - pad, y, cx + w / 2 + pad, y + size * 1.7)
    d.rounded_rectangle(box, size * 0.8, fill=bg if not dim else (28, 28, 28), outline=None)
    d.text((cx - w / 2, y + size * 0.3), text, font=f, fill=fg if not dim else (90, 90, 90))
    if struck: strike(img, box[0] + 10, box[1], box[2] - 10, box[3], 8)

# ---------- base frame ----------
TEX = {}
def texture(img):
    """Faint texture of the card's own words, placed AFTER the card is drawn (2026-10-25, critic on both H104 videos: words printed
    over each other and behind the headline read as a render glitch). A word goes only where its padded box is still pure black on
    the finished card and away from the other texture words; each word once, max 9. Positions are fixed per tag, so the stages of
    one card keep them (a word can vanish when content grows over it, it never jumps)."""
    from PIL import ImageChops
    import random
    tag, words = img.info["bg"]; key = (tag, tuple(words))
    if key not in TEX:
        r = random.Random(tag); d0 = D(img); cand = []; words_u = list(dict.fromkeys(words))
        for _ in range(400):
            wd, sz = r.choice(words_u), r.choice((46, 64, 90)); tw = d0.textlength(wd, font=font(sz)); th = sz * 1.2
            if tw > W - 60: continue
            x, y = r.randint(20, int(W - 20 - tw)), r.randint(170, int(H - 40 - th)); cand.append((wd, sz, x, y, tw, th))
        TEX[key] = cand
    out = img.copy(); d = D(out); boxes = []; used = set()
    for wd, sz, x, y, tw, th in TEX[key]:
        if len(boxes) >= 9: break
        if wd in used: continue
        b = (x - 40, y - 40, x + tw + 40, y + th + 40)
        if any(b[0] < o[2] and o[0] < b[2] and b[1] < o[3] and o[1] < b[3] for o in boxes): continue
        rb = tuple(int(max(0, v * K)) for v in b); reg = img.crop(rb)
        if ImageChops.difference(reg, Image.new("RGB", reg.size, BLACK)).getbbox(): continue   # something is drawn there
        boxes.append(b); used.add(wd); d.text((x, y), wd, font=font(sz), fill=(24, 24, 21))
    return out

LOGO_IM = None
def base(tag, bg_words=()):
    global LOGO_IM
    img = Image.new("RGB", (RW, RH), BLACK); d = D(img)
    if bg_words: img.info["bg"] = (tag, list(bg_words))          # faint texture of the family's own words: drawn by texture() at add()
    if LOGO_IM is None:
        LOGO_IM = Image.open(LOGO).convert("RGB").resize((sc(96), sc(96)), Image.LANCZOS)
    m = Image.new("L", LOGO_IM.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, LOGO_IM.width - 1, LOGO_IM.height - 1), sc(18), fill=255)
    img.paste(LOGO_IM, (sc(60), sc(40)), m)
    d.text((176, 50), "anotherwordfor.net", font=font(38), fill=YELLOW)
    if tag: d.text((178, 98), tag, font=font(26), fill=GREY)
    return img

# ---------- audio ----------
def speak(jobs, out):
    sig = lambda j: f"{j['voice']}|{j['speed']}|{j['text']}"         # the cache is per TEXT: a clip made for another text under the same beat number is spoken again
    todo = [j for j in jobs if not Path(j["out"]).exists() or not Path(j["out"] + ".txt").exists() or Path(j["out"] + ".txt").read_text() != sig(j)]   # (critic 2026-10-13, lab H72: a removed beat left every clip one question behind)
    for j in todo: Path(j["out"]).unlink(missing_ok=True)
    if todo:
        json.dump(todo, open(out / "kokoro_jobs.json", "w"))
        subprocess.run([TTSPY, str(Path(__file__).parent / "kokoro_tts.py"), str(out / "kokoro_jobs.json")], check=True)
    for j in todo: Path(j["out"] + ".txt").write_text(sig(j))
    res = {}
    for j in jobs:
        with wave.open(j["out"]) as w_:
            assert w_.getframerate() == SR and w_.getnchannels() == 1 and w_.getsampwidth() == 2, j["out"]
            res[j["key"]] = w_.readframes(w_.getnframes())
    return res

def silence(sec): return b"\x00\x00" * int(SR * sec)

def split_word(speech, example):
    """'Huge. It means extremely big. We grew ...' -> [word, meaning part, example]"""
    i = speech.index(". ") + 1; j = speech.rindex(example)
    return [speech[:i].strip(), speech[i:j].strip(), speech[j:].strip()]

def hook_word_check(u, out):
    """"Another word for X" videos (2026-10-25, critic on h104-and): a short function word said bare at 0:00 ("Another word for
    and?") was heard as "end". The narration of the first beat is transcribed (faster-whisper small.en, the critic's own ear) and
    the render is REFUSED unless X is heard in the first 6 s. Fix = say X inside a phrase ("..., as in: tea and coffee").
    --skip-hook-word bypasses (only with the user's OK)."""
    m = re.match(r"another word for (.+)$", str(u.get("tag") or ""), re.I)
    if not m or "--skip-hook-word" in sys.argv: return
    x = m.group(1).strip().lower()
    sp0 = str(u["beats"][0].get("speech") or "")
    if len(x) <= 4 and not re.search(r"\bas in\b", sp0, re.I):   # deterministic part: whisper heard the bare "and" once as "end", once as "and"
        sys.exit(f"REFUSED: short hook word '{x}' must be said inside an example in beat 1 ('Another word for {x}, as in: ...'), "
                 f"found {sp0[:60]!r} (longvideo-writer checklist 13a)")
    clips = sorted((out).glob("b01-*.wav"))
    if not clips: return
    from faster_whisper import WhisperModel
    segs, _ = WhisperModel("small.en", device="cpu", compute_type="int8").transcribe(str(clips[0]), word_timestamps=True)
    words = [(w.word.strip(" .,?!:;\"'").lower(), w.start) for sg in segs for w in (sg.words or [])]
    heard = " ".join(w for w, t0 in words if t0 <= 6.0)
    # X counts only where the viewer needs it: right after "another word for", or inside the "as in: ..." example after it
    # (X also turns up elsewhere in a hook list - "in addition and moreover" - which proves nothing about the topic word).
    xr = re.escape(x)
    if re.search(r"another word for " + xr + r"( |$)", heard) or re.search(r"as in (\S+ ){0,5}?" + xr + r"( |$)", heard):
        print(f"hook word OK: '{x}' heard in the first 6 s ({heard!r})"); return
    sys.exit(f"REFUSED: hook word '{x}' is not heard in the first 6 s of beat 1 (whisper: {heard!r}). Say it inside a phrase, "
             f"e.g. 'Another word for {x}, as in: ...' (longvideo-writer checklist 13a), re-approve the language, render again.")

# ---------- main ----------
def main(path):
    sys.path.insert(0, str(Path(__file__).parent)); import lang_gate
    u = json.load(open(path)); ok, _ = lang_gate.verify(u)
    if not ok and "--skip-language-gate" not in sys.argv:
        sys.exit(f"REFUSED: {path} has no valid English-language approval (run glottos-language-editor + lang_gate.py approve)")
    out = ROOT / "state/shorts" / u["id"]; out.mkdir(parents=True, exist_ok=True); (out / "frames").mkdir(exist_ok=True)
    if (out / "final.mp4").exists() and "--overwrite" not in sys.argv: sys.exit(f"REFUSED: {u['id']} already rendered (new id)")
    voice, speed = u["voice"].split(":", 1)[1], u.get("speed", 1.0)
    pics = family_pictures(u.get("pic_units")); beats = u["beats"]
    TAG = u.get("tag", 'Stop saying "very"'); search = "tag" in u
    label = {b["family"]: b.get("label", f"very {b['family']}") for b in beats if b["kind"] == "section"}
    fams = [b["family"] for b in beats if b["kind"] == "section"]
    words_of = {f: [b["card"]["headline"] for b in beats if b.get("family") == f and b["kind"] == "word"] for f in fams}
    missing = [(b["family"], b["card"]["headline"]) for b in beats if b["kind"] == "word" and (b["family"], pkey(b["card"]["headline"])) not in pics]
    if missing and "--allow-missing-pictures" not in sys.argv: sys.exit(f"REFUSED: no picture for {missing}")

    # 1. narration clips (one Kokoro process, cached per text)
    parts = {}
    for i, b in enumerate(beats, 1):
        s = b["speech"]
        if b["kind"] == "word": ps = split_word(s, b["card"]["example"])
        elif b["kind"] in ("quiz", "shadow"): ps = [x.strip() for x in s.split("|")]
        else: ps = [s]
        parts[i] = ps
    # "Blank" pause (2026-10-25, critic on both H104 videos: Kokoro ran "blank" into the next word -> "blankets very expensive"):
    # a part that says "blank" is spoken as separate clips cut right after each "blank", joined with BLANK_PAUSE seconds of silence.
    BLANK_PAUSE = 0.45
    jobs, joins = [], {}
    for i, ps in parts.items():
        for k, t_ in enumerate(ps):
            segs = [x for x in re.split(r"(?<=\bblank[.,!?])\s+|(?<=\bblank)\s+", t_, flags=re.I) if x.strip()] if parts and re.search(r"\bblank\b", t_, re.I) else [t_]
            if len(segs) == 1:
                jobs.append({"key": f"{i}-{k}", "text": t_, "voice": voice, "speed": speed, "out": str(out / f"b{i:02d}-{k}.wav")}); continue
            joins[f"{i}-{k}"] = [f"{i}-{k}~{m}" for m in range(len(segs))]
            jobs += [{"key": f"{i}-{k}~{m}", "text": x, "voice": voice, "speed": speed, "out": str(out / f"b{i:02d}-{k}~{m}.wav")} for m, x in enumerate(segs)]
    au = speak(jobs, out)
    for key, subs in joins.items():
        au[key] = silence(BLANK_PAUSE).join(au.pop(x) for x in subs)
    hook_word_check(u, out)


    # 2. states (image, seconds) + audio timeline
    states, audio, chapters, t = [], [], [], 0.0
    clips = []                                                     # (start s, seconds, file) of film-clip beats
    ev = []                                                        # sound-bed events (unit "bed", lab H30): (seconds, "pop" | "tick" | "ding")
    def add(img, sec, pcm=b"", snd=None, ticks=False):
        nonlocal t
        if snd: ev.append((t, snd))
        if ticks: ev.extend((t + k, "tick") for k in range(int(max(sec, len(pcm) / 2 / SR))))
        if img.info.get("bg"): img = texture(img)
        n = len(states); p = out / "frames" / f"s{n:04d}.png"; img.save(p)
        body = pcm + silence(max(0.0, sec - len(pcm) / 2 / SR))
        states.append((p, len(body) / 2 / SR)); audio.append(body); t += len(body) / 2 / SR
    dur = lambda k: len(au[k]) / 2 / SR
    part_no = 0
    for i, b in enumerate(beats, 1):
        c, kind, fam = b["card"], b["kind"], b.get("family")
        bgw = [w_.lower() for w_ in words_of.get(fam, [])]
        tag = f"{TAG}  ·  part {part_no} of {len(fams)}: {label[fam]}" if fam else TAG
        if kind == "hook":
            chapters.append((t, "Intro"))
            img = base("", [w_.lower() for f in fams for w_ in words_of[f]])
            d = D(img); y = 190
            f1 = font(96); w1 = d.textlength(c["headline"], font=f1)
            d.text(((W - w1) / 2, y), c["headline"], font=f1, fill=YELLOW)
            if not search:
                vx = (W - w1) / 2 + d.textlength('Stop saying "', font=f1); vw = d.textlength(u.get("hook_strike", "very"), font=f1)   # one-word videos (lab H58): the whole phrase "very hot" is struck out
                strike(img, vx - 8, y + 10, vx + vw + 8, y + 110, 16)
            draw_text(img, c["sub"], (0, 330), 64, WHITE, W, align="center")
            thumbs = [pics.get((f, pkey(words_of[f][0]))) for f in fams]
            if search or len(fams) < 6: thumbs = [pics.get((f, pkey(w_))) for k in range(5) for f in fams for w_ in words_of[f][k:k + 1]][:6]
            tw = 270; x = (W - (tw * 6 + 24 * 5)) / 2
            for p in thumbs:
                if p: put(img, framed(p, tw, 250), x, 520, tw, 250)
                x += tw + 24
            add(img, dur(f"{i}-0") + 0.6, au[f"{i}-0"])
        elif kind == "section":
            part_no += 1; chapters.append((t, b.get("chapter", f"Stop saying \"very {fam}\"")))
            tag = f"{TAG}  ·  part {part_no} of {len(fams)}"
            img = base(tag, bgw); d = D(img)
            draw_text(img, c["sub"], (0, 200), 44, GREY, W, align="center")
            fs = 120; txt = c["headline"]
            while d.textlength(txt, font=font(fs)) > W - 240 and fs > 60: fs -= 4      # a long part title keeps its side margins (critic 2026-10-11)
            f1 = font(fs); w1 = d.textlength(txt, font=f1); x0 = (W - w1) / 2
            d.text((x0, 290), txt, font=f1, fill=YELLOW if search else WHITE)
            if not search:
                q = txt.index('"'); sx = x0 + d.textlength(txt[:q], font=f1); ex = x0 + w1
                d.text((sx, 290), txt[q:], font=f1, fill=YELLOW); strike(img, sx - 6, 300, ex + 6, 420, 16)
            x = (W - (300 * 5 + 20 * 4)) / 2
            for w_ in words_of[fam]:
                p = pics.get((fam, pkey(w_)))
                if p: put(img, framed(p, 300, 280), x, 560, 300, 280)
                draw_text(img, w_, (x, 860), 40, YELLOW, 300, align="center"); x += 320
            add(img, dur(f"{i}-0") + 0.8, au[f"{i}-0"])
        elif kind == "word":
            n = words_of[fam].index(c["headline"]) + 1; p = pics.get((fam, pkey(c["headline"])))
            def word_state(stage):
                img = base(tag, bgw); d = D(img)
                d.text((100, 190), f"{n} / 5", font=font(40), fill=GREY)
                hs = 132 if len(c["headline"]) <= 10 else 104
                while max(d.textlength(w_, font=font(hs)) for w_ in c["headline"].split()) > 860 and hs > 60: hs -= 4   # a long single word stays left of the picture (lab H30: "Condescending")
                y = draw_text(img, c["headline"], (100, 250), hs, YELLOW, 860)
                if stage >= 1: y = draw_text(img, "= " + c["meaning"], (100, y + 20), 54, WHITE, 860)
                if stage >= 2:
                    draw_text(img, c["example"], (100, y + 60), 58, WHITE, 860, bold=False, hl=c["headline"])
                if stage >= 1 and p:
                    put(img, framed(p, 820, 640), 1000, 230, 840, 660)
                return img
            add(word_state(0), dur(f"{i}-0") + 0.25, au[f"{i}-0"])
            add(word_state(1), dur(f"{i}-1") + 0.25, au[f"{i}-1"], snd="pop")
            add(word_state(2), dur(f"{i}-2") + 1.4, au[f"{i}-2"], snd="pop")
        elif kind == "quiz":
            opts = [x.strip() for x in c["options"].split("/")]; right = next(o for o in opts if c["answer"].lower().find(o.lower()) >= 0 and c["question"].replace("___", o) == c["answer"])
            if b.get("chapter"): chapters.append((t, b["chapter"]))          # a quiz video (lab H72) opens its chapters on question cards
            def quiz_state(count=None, answer=False):
                img = base(tag); y0 = 200 if "sub" not in c else 170   # no ghost words on a test card: one sat behind the blank and gave the answer away (critic 2026-10-11)
                draw_text(img, c["headline"], (0, y0), 76 if "sub" not in c else 60, YELLOW, W, align="center")
                if "sub" in c: draw_text(img, c["sub"], (0, 262), 54, GREY, W, align="center")   # the task line of a quiz video (lab H72)
                if answer: y = draw_text(img, c["answer"], (160, 360 if "sub" not in c else 380), 76, WHITE, W - 320, align="center", hl=right, hl_color=GREEN)
                else: y = draw_text(img, c["question"].replace("___", "_____"), (160, 360 if "sub" not in c else 380), 76, WHITE, W - 320, align="center")
                py = max(y + 70, 620)
                if len(opts) == 2:
                    for k, o in enumerate(opts):
                        ok_ = o == right
                        pill(img, o, W / 2 + (-330 if k == 0 else 330), py, 64, BLACK if not answer or ok_ else WHITE,
                             (GREEN if answer and ok_ else WHITE), dim=answer and not ok_, struck=answer and not ok_)
                else:                                                  # three choices with letters (lab H72), laid out by their real widths
                    lab = [f"{'ABC'[k]}   {o}" for k, o in enumerate(opts)]; size = 58; dd = D(img)
                    while sum(dd.textlength(x, font=font(size)) + size * 1.4 for x in lab) + 50 * (len(lab) - 1) > W - 160: size -= 2
                    ws = [dd.textlength(x, font=font(size)) + size * 1.4 for x in lab]; x = (W - sum(ws) - 50 * (len(lab) - 1)) / 2
                    for k, o in enumerate(opts):
                        ok_ = o == right
                        pill(img, lab[k], x + ws[k] / 2, py, size, BLACK if not answer or ok_ else WHITE,
                             (GREEN if answer and ok_ else WHITE), dim=answer and not ok_, struck=answer and not ok_)
                        x += ws[k] + 50
                if b.get("emoji"):                                     # a picture on every question card (lab H72, traffic corpus: no 8 minutes of text only)
                    from emoji_pics import emoji
                    _e = b["emoji"]; _e = _e if all(ch in "0123456789abcdef_" for ch in _e.lower()) else "_".join(f"{ord(ch):x}" for ch in _e if ord(ch) != 0xfe0f)   # hex code or the emoji itself (T02 2026-10-18)
                    e = emoji(_e).resize((sc(210), sc(210)), Image.LANCZOS); img.paste(e, (sc(1600), sc(120)), e)
                if count: draw_text(img, str(count), (0, 860), 110, GREY, W, align="center")
                if answer and c.get("note"): draw_text(img, c["note"], (160, py + 170), 54, YELLOW, W - 320, align="center", hl=right, hl_color=GREEN)
                return img
            add(quiz_state(), dur(f"{i}-0") + 0.3, au[f"{i}-0"])
            for cnt in range(u.get("countdown", 3), 0, -1): add(quiz_state(cnt), 1.0, ticks=True)
            add(quiz_state(answer=True), dur(f"{i}-1") + 1.2, au[f"{i}-1"], snd="ding")
        elif kind == "shadow":
            sents = c["sentences"].split("\n"); chapters.append((t, f"Speaking practice: {label[fam]}"))
            def shadow_state(k, turn):
                img = base(tag, bgw); draw_text(img, c["headline"], (0, 190), 76, YELLOW, W, align="center")
                if k is None:
                    draw_text(img, parts[i][0], (160, 420), 70, WHITE, W - 320, align="center"); return img
                draw_text(img, sents[k], (160, 400), 88, WHITE, W - 320, align="center", hl=words_of[fam][k])
                pill(img, "YOUR TURN: SAY IT" if turn else "LISTEN", W / 2, 760, 56, BLACK, GREEN if turn else WHITE)
                draw_text(img, f"{k + 1} / {len(sents)}", (0, 920), 40, GREY, W, align="center")
                return img
            add(shadow_state(None, False), dur(f"{i}-0") + 0.5, au[f"{i}-0"])
            for k in range(len(sents)):
                add(shadow_state(k, False), dur(f"{i}-{k + 1}") + 0.2, au[f"{i}-{k + 1}"])
                tp = u.get("turn_pause", [1.4, 0.8])               # the "your turn" pause = factor x the sentence + seconds
                add(shadow_state(k, True), dur(f"{i}-{k + 1}") * tp[0] + tp[1], ticks=bool(u.get("bed")))
        elif kind in ("tip", "cta"):
            if kind == "cta": chapters.append((t, "Your turn"))
            elif b.get("chapter"): chapters.append((t, b["chapter"]))          # a tip card may open a chapter (lab H30: "Final test")
            img = base("", bgw); d = D(img)
            sec = dur(f"{i}-0") + b.get("hold", 1.0 if kind == "tip" else 3.0)   # "hold" = seconds the card stays after the voice (subscribe animation, end screen)
            if b.get("clip"):                                      # film clip beat (T02, 2026-10-17): headline on top, sub at the bottom, the muted
                d.rectangle(CLIP_BOX, fill=BLACK)                  # public-domain clip plays in CLIP_BOX (overlay pass after the stills render)
                draw_text(img, c["headline"], (100, 140), 72, WHITE, W - 200, align="center")   # below the brand bar (it reaches ~y 135)
                draw_text(img, c["sub"], (100, CLIP_BOX[3] + 30), 44, YELLOW, W - 200, align="center")
                clips.append((t, sec, ROOT / "state/examples/viral/library/clips" / (b["clip"] + ".mp4")))
            else:
                y = draw_text(img, c["headline"], (100, 330), 104, WHITE, W - 200, align="center")
                draw_text(img, c["sub"], (100, y + 40), 80 if kind == "tip" else 64, YELLOW, W - 200, align="center")
            add(img, sec, au[f"{i}-0"])
        print(f"beat {i} ({kind}) -> t={t:.1f}s", flush=True)

    # 3. assemble: stills (concat demuxer) + one wav
    with wave.open(str(out / "narration.wav"), "wb") as w_:
        w_.setnchannels(1); w_.setsampwidth(2); w_.setframerate(SR); w_.writeframes(b"".join(audio))
    with open(out / "states.txt", "w") as f:
        for p, sec in states: f.write(f"file '{p}'\nduration {sec:.4f}\n")
        f.write(f"file '{states[-1][0]}'\n")
    dst = out / "final.mp4"
    if u.get("bed"):                                               # lab H30 (both expert sources: no dead silence in the pauses): ticks in the
        from build_first_frame import sound_bed                    # countdowns and "your turn" pauses, a pop per card, a quiet loop under the voice
        sound_bed(ev, t, u["bed"].get("music", 0), out / "bed.wav", sr=SR)
        subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(out / "narration.wav"), "-i", str(out / "bed.wav"), "-filter_complex",
                        "amix=inputs=2:normalize=0", str(out / "narration-bed.wav")], check=True)
    subprocess.run([FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(out / "states.txt"), "-i", str(out / ("narration-bed.wav" if u.get("bed") else "narration.wav")),
                    "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-tune", "stillimage",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", "-threads", "2", str(dst)], check=True)
    if clips:                                                      # overlay pass: each muted clip, scaled into CLIP_BOX, looped over its beat window
        missing_c = [str(f) for _, _, f in clips if not f.exists()]
        if missing_c: sys.exit(f"REFUSED: clip file missing {missing_c}")
        bw, bh = sc(CLIP_BOX[2] - CLIP_BOX[0]), sc(CLIP_BOX[3] - CLIP_BOX[1]); ins, fl, last = [], [], "0:v"
        for k, (a, sec, f) in enumerate(clips, 1):
            ins += ["-stream_loop", "-1", "-t", f"{sec:.3f}", "-i", str(f)]
            fl.append(f"[{k}:v]scale={bw}:{bh}:force_original_aspect_ratio=decrease,setpts=PTS-STARTPTS+{a:.3f}/TB[c{k}]")
            fl.append(f"[{last}][c{k}]overlay=x=(W-w)/2:y={sc(CLIP_BOX[1])}+({bh}-h)/2:enable='between(t,{a:.3f},{a + sec:.3f})':eof_action=pass[v{k}]")
            last = f"v{k}"
        tmp = out / "final-clips.mp4"
        subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(dst), *ins, "-filter_complex", ";".join(fl), "-map", f"[{last}]", "-map", "0:a",
                        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart",
                        "-threads", "2", str(tmp)], check=True)
        tmp.replace(dst); print(f"clips: {len(clips)} overlaid", flush=True)
    ch = "\n".join(f"{int(s // 60)}:{int(s % 60):02d} {name}" for s, name in chapters)
    (out / "chapters.txt").write_text(ch + "\n")
    thumbnail(u, pics, out)
    print(f"FINAL {dst} {t:.1f}s ({t / 60:.1f} min)\n{ch}", flush=True)

def thumbnail(u, pics, out):
    """Marcus: face + max 4 big words, yellow on black, a red X; the face = the drawn 'overjoyed' woman (happy family)"""
    img = Image.new("RGB", (1280, 720), BLACK); d = ImageDraw.Draw(img)
    th = u.get("thumb", {})                                     # Vol. 2+ (2026-10-03): the unit names its own face + pill text
    _f = th.get("face", ["happy", "overjoyed"]); face = pics.get((_f[0], pkey(_f[1]))); bx = th.get("box", [0.0, 0.02, 0.40, 1.0])
    if face:
        im = Image.open(face).convert("RGB"); w, h = im.size
        box = (int(w * bx[0]), int(h * bx[1]), int(w * bx[2]), int(h * bx[3]))       # the face only, not the card
        crop = im.crop(box); k = 720 / crop.height; crop = crop.resize((int(crop.width * k), 720), Image.LANCZOS)
        if th.get("lines") and crop.width > 560:               # search-phrase thumbnail: the words keep the left 700 px
            off = int((crop.width - 560) * th.get("cx", 0.5)); crop = crop.crop((off, 0, off + 560, 720))
        img.paste(crop, (1280 - crop.width, 0))
    if th.get("lines"):                                         # search-phrase videos: the thumbnail says the title's key words
        y = 60
        for txt, col in th["lines"]:
            size = 150
            while d.textlength(txt, font=rfont(size)) > 620: size -= 6
            d.text((60, y), txt, font=rfont(size), fill=YELLOW if col == "yellow" else WHITE); y += int(size * 1.12)
        pill = th.get("pill", "10 WORDS"); fp = rfont(58); pw = d.textlength(pill, font=fp)
        d.rounded_rectangle((60, 600, 60 + pw + 48, 690), 20, fill=YELLOW); d.text((84, 612), pill, font=fp, fill=BLACK)
        img.save(out / "thumbnail.jpg", quality=92); return
    d.text((60, 70), "STOP", font=rfont(130), fill=WHITE)
    d.text((60, 210), "SAYING", font=rfont(130), fill=WHITE)
    fv = rfont(190); d.text((50, 350), '"VERY"', font=fv, fill=YELLOW); vw = d.textlength('"VERY"', font=fv)
    d.line((60, 560, 50 + vw, 400), fill=RED, width=22); d.line((60, 400, 50 + vw, 560), fill=RED, width=22)
    pill = th.get("pill", "30 BETTER WORDS"); fp = rfont(58); pw = d.textlength(pill, font=fp)
    d.rounded_rectangle((60, 600, 60 + pw + 48, 690), 20, fill=YELLOW); d.text((84, 612), pill, font=fp, fill=BLACK)
    img.save(out / "thumbnail.jpg", quality=92)

if __name__ == "__main__": main(sys.argv[1])
