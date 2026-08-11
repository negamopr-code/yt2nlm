"""Rendering: PIL slide PNGs + ffmpeg assembly (zoompan, xfade, adelay+amix
speech timeline, lavfi-synthesized ducked music bed) — glottos techniques,
pure python + the in-repo static ffmpeg. No moviepy."""

from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from .config import FFMPEG

LEAD = 0.4          # audio lead-in per slide (s)
TAIL = 0.6
MIN_SLIDE = 2.5
XFADE = 0.4


def _c(hexs: str) -> tuple:
    return tuple(int(hexs.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))


def _font(path: str, size: int):
    return ImageFont.truetype(path, size)


def _wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def _text_block(draw, text, font, x, y, max_w, fill, align="center",
                cx=None, line_gap=1.18):
    lines = _wrap(draw, text, font, max_w)
    h = font.size * line_gap
    for i, ln in enumerate(lines):
        if align == "center":
            lw = draw.textlength(ln, font=font)
            draw.text(((cx or x) - lw / 2, y + i * h), ln, font=font, fill=fill)
        else:
            draw.text((x, y + i * h), ln, font=font, fill=fill)
    return y + len(lines) * h


def draw_slide(slide: dict, brand: dict, size: tuple[int, int]) -> Image.Image:
    """Render one slide at 2x then downscale (crisp text)."""
    W, H = size[0] * 2, size[1] * 2
    vertical = H > W
    img = Image.new("RGB", (W, H), _c(brand["bg"]))
    d = ImageDraw.Draw(img)
    accent, text_c = _c(brand["accent"]), _c(brand["text"])
    muted, card = _c(brand["muted"]), _c(brand["card"])
    head = brand["font_head"]
    body = brand["font_body"]
    cx = W // 2
    kind = slide["kind"]
    disp = slide["display"]
    margin = int(W * 0.09)
    maxw = W - 2 * margin

    # top brand strip
    d.rectangle([0, 0, W, int(H * 0.012)], fill=accent)
    d.text((margin, int(H * 0.03)), "ANOTHER WORD",
           font=_font(head, int(W * 0.030)), fill=accent)

    if kind in ("hook", "intro", "outro"):
        f = _font(head, int(W * (0.075 if vertical else 0.055)))
        y = H * (0.40 if kind != "outro" else 0.36)
        _text_block(d, disp["text"].replace("\n", " "), f, margin, y, maxw,
                    text_c, cx=cx)
        if kind == "outro":
            f2 = _font(head, int(W * 0.05))
            d.rounded_rectangle([W * 0.14, H * 0.55, W * 0.86, H * 0.64],
                                radius=28, fill=accent)
            t = brand["watermark"]
            lw = d.textlength(t, font=f2)
            d.text((cx - lw / 2, H * 0.57), t, font=f2, fill=_c(brand["bg"]))
    elif kind in ("word", "example"):
        y = H * (0.24 if vertical else 0.16)
        f_word = _font(head, int(W * (0.11 if vertical else 0.075)))
        lw = d.textlength(disp["word"], font=f_word)
        d.text((cx - lw / 2, y), disp["word"], font=f_word, fill=text_c)
        y += f_word.size * 1.35
        if kind == "word":
            reg = disp["register"]
            pill_c = _c(brand["register"].get(reg, brand["accent"]))
            f_pill = _font(head, int(W * 0.032))
            pw = d.textlength(reg.upper(), font=f_pill) + W * 0.04
            d.rounded_rectangle([cx - pw / 2, y, cx + pw / 2, y + f_pill.size * 1.9],
                                radius=24, fill=pill_c)
            d.text((cx - pw / 2 + W * 0.02, y + f_pill.size * 0.4), reg.upper(),
                   font=f_pill, fill=(255, 255, 255))
            y += f_pill.size * 2.6
            # intensity bar: 5 segments
            seg_w, seg_h, gap = W * 0.075, H * 0.012, W * 0.012
            total = 5 * seg_w + 4 * gap
            x0 = cx - total / 2
            for i in range(5):
                fill = accent if i < disp["intensity"] else card
                d.rounded_rectangle([x0 + i * (seg_w + gap), y,
                                     x0 + i * (seg_w + gap) + seg_w, y + seg_h],
                                    radius=8, fill=fill)
            y += seg_h + H * 0.02
            if disp.get("nuance"):
                f_n = _font(body, int(W * 0.036))
                y = _text_block(d, disp["nuance"], f_n, margin, y, maxw,
                                muted, cx=cx) + H * 0.03
        # example card
        f_ex = _font(body, int(W * 0.042))
        lines = _wrap(d, f"“{disp['example']}”", f_ex, maxw - W * 0.06)
        card_h = len(lines) * f_ex.size * 1.25 + H * 0.045
        d.rounded_rectangle([margin, y, W - margin, y + card_h], radius=30,
                            fill=card)
        yy = y + H * 0.022
        for ln in lines:
            lw = d.textlength(ln, font=f_ex)
            d.text((cx - lw / 2, yy), ln, font=f_ex, fill=text_c)
            yy += f_ex.size * 1.25
    elif kind in ("quiz_q", "quiz_reveal"):
        f_t = _font(head, int(W * 0.05))
        qy = 0.22 if vertical else 0.14
        d.text((margin, H * qy), "QUICK QUIZ", font=f_t, fill=accent)
        f_q = _font(body, int(W * 0.045))
        y = _text_block(d, disp["question"], f_q, margin, H * (qy + 0.08), maxw,
                        text_c, cx=cx) + H * 0.04
        f_o = _font(head, int(W * 0.042))
        for i, opt in enumerate(disp["options"]):
            selected = kind == "quiz_reveal" and i == disp.get("answer")
            oy = y + i * H * 0.085
            d.rounded_rectangle([margin, oy, W - margin, oy + H * 0.065],
                                radius=26,
                                fill=accent if selected else card)
            d.text((margin + W * 0.03, oy + H * 0.016),
                   f"{chr(65 + i)}.  {opt}", font=f_o,
                   fill=(255, 255, 255) if selected else text_c)
        if kind == "quiz_reveal" and disp.get("explain"):
            _text_block(d, disp["explain"], _font(body, int(W * 0.035)),
                        margin, y + 3 * H * 0.085 + H * 0.03, maxw, muted, cx=cx)

    # watermark (every slide except outro, which has the big CTA)
    if kind != "outro":
        f_wm = _font(body, int(W * 0.028))
        wm = brand["watermark"]
        lw = d.textlength(wm, font=f_wm)
        d.text((W - margin - lw, H - int(H * 0.045)), wm, font=f_wm,
               fill=muted)

    return img.resize(size, Image.LANCZOS)


def _run_ff(args: list[str]) -> None:
    subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", *args],
                   check=True)


def assemble(slide_pngs: list[Path], wav_durs: list[float], wavs: list[Path],
             out_mp4: Path, size: tuple[int, int], music: dict,
             work: Path) -> list[float]:
    """Per-slide clips -> xfade chain -> speech timeline + music bed -> mux.
    Returns slide start offsets (for the .srt)."""
    W, Hh = size
    durs = [max(d + LEAD + TAIL, MIN_SLIDE) for d in wav_durs]
    clips = []
    for i, (png, dur) in enumerate(zip(slide_pngs, durs)):
        clip = work / f"c{i:02d}.mp4"
        frames = int(dur * 30)
        _run_ff(["-loop", "1", "-framerate", "30", "-i", str(png), "-t", f"{dur:.3f}",
                 "-vf", (f"scale={W * 4}:-2,zoompan=z='1+0.0003*on':"
                         f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
                         f"d={frames}:s={W}x{Hh}:fps=30,format=yuv420p"),
                 "-c:v", "libx264", "-crf", "20", "-preset", "veryfast",
                 str(clip)])
        clips.append(clip)

    # xfade chain: slide k starts at offsets[k]
    offsets = [0.0]
    for i in range(1, len(durs)):
        offsets.append(offsets[i - 1] + durs[i - 1] - XFADE)
    video = work / "video.mp4"
    if len(clips) == 1:
        video = clips[0]
    else:
        fc, cur = [], "[0:v]"
        for i in range(1, len(clips)):
            nxt = f"[v{i:02d}]"
            fc.append(f"{cur}[{i}:v]xfade=transition=fade:duration={XFADE}:"
                      f"offset={offsets[i]:.3f}{nxt}")
            cur = nxt
        _run_ff([*sum([["-i", str(c)] for c in clips], []),
                 "-filter_complex", ";".join(fc), "-map", cur,
                 "-c:v", "libx264", "-crf", "20", "-preset", "veryfast",
                 "-pix_fmt", "yuv420p", str(video)])

    # audio: speech at slide offsets (+LEAD), synthesized ducked bed
    total = offsets[-1] + durs[-1]
    fc, mix_in = [], []
    for i, wav in enumerate(wavs):
        ms = int((offsets[i] + LEAD) * 1000)
        fc.append(f"[{i}:a]aformat=channel_layouts=stereo:sample_rates=44100,"
                  f"adelay={ms}|{ms}[n{i}]")
        mix_in.append(f"[n{i}]")
    fc.append(f"{''.join(mix_in)}amix=inputs={len(wavs)}:normalize=0:"
              f"dropout_transition=0[speech]")
    audio_args = sum([["-i", str(w)] for w in wavs], [])
    out_audio = work / "audio.wav"
    if music.get("enabled", True):
        bed = ("aevalsrc=exprs=0.09*sin(2*PI*220*t)"
               "+0.05*sin(2*PI*277.18*t)*(0.6+0.4*sin(2*PI*0.2*t))"
               "+0.04*sin(2*PI*329.63*t)*(0.6+0.4*sin(2*PI*0.13*t)):s=44100")
        audio_args += ["-f", "lavfi", "-t", f"{total:.2f}", "-i", bed]
        b = len(wavs)
        if music.get("duck", True):
            fc.append("[speech]asplit=2[sp1][sp2]")
            fc.append(f"[{b}:a]aformat=channel_layouts=stereo,"
                      f"lowpass=f=2200,volume={music.get('volume', 0.14)}[bedv]")
            fc.append("[bedv][sp1]sidechaincompress=threshold=0.04:ratio=8:"
                      "attack=30:release=600[duck]")
            fc.append("[duck][sp2]amix=inputs=2:normalize=0,"
                      "alimiter=limit=0.95[mix]")
        else:
            fc.append(f"[{b}:a]volume={music.get('volume', 0.12)}[bedv]")
            fc.append("[speech][bedv]amix=inputs=2:normalize=0,"
                      "alimiter=limit=0.95[mix]")
        _run_ff([*audio_args, "-filter_complex", ";".join(fc),
                 "-map", "[mix]", "-t", f"{total:.2f}", str(out_audio)])
    else:
        _run_ff([*audio_args, "-filter_complex", ";".join(fc),
                 "-map", "[speech]", "-t", f"{total:.2f}", str(out_audio)])

    _run_ff(["-i", str(video), "-i", str(out_audio), "-c:v", "copy",
             "-c:a", "aac", "-b:a", "160k", "-shortest", str(out_mp4)])
    return offsets


def make_thumbnail(script: dict, brand: dict, out: Path) -> None:
    img = Image.new("RGB", (2560, 1440), _c(brand["bg"]))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 2560, 34], fill=_c(brand["accent"]))
    f1 = _font(brand["font_head"], 150)
    f2 = _font(brand["font_head"], 300)
    d.text((140, 260), "Another Word for", font=f1, fill=_c(brand["muted"]))
    d.text((140, 480), script["target"].upper(), font=f2,
           fill=_c(brand["text"]))
    alts = " · ".join(y["word"] for y in script["synonyms"][:3])
    f3 = _font(brand["font_body"], 110)
    d.text((140, 940), alts, font=f3, fill=_c(brand["accent"]))
    f4 = _font(brand["font_body"], 80)
    d.text((140, 1250), brand["watermark"], font=f4, fill=_c(brand["muted"]))
    img.resize((1280, 720), Image.LANCZOS).save(out, "JPEG", quality=90)


def _srt_ts(t: float) -> str:
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int((s % 1) * 1000):03d}"


def make_srt(slides: list[dict], offsets: list[float], durs: list[float],
             out: Path) -> None:
    lines = []
    for i, sl in enumerate(slides):
        start = offsets[i] + LEAD
        end = offsets[i] + durs[i] - 0.2
        lines += [str(i + 1), f"{_srt_ts(start)} --> {_srt_ts(end)}",
                  sl["speech"], ""]
    out.write_text("\n".join(lines))
