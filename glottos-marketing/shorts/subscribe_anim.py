#!/usr/bin/env python3
"""Subscribe + bell call-to-action overlay (user 2026-09-29: "add the animation for subscribing and hitting the bell").

  python3 shorts/subscribe_anim.py <in.mp4> <out.mp4> --at 42.6,426.4 [--corner bl|bc] [--frames-only DIR]

5-second animation, lower-left (the channel logo tile and YouTube's own branding watermark live bottom-right):
red SUBSCRIBE pill + bell slide in -> a cursor clicks SUBSCRIBE (turns grey "SUBSCRIBED ✓") -> cursor clicks the
bell (it rings) -> slides out. Silent: the audio track is copied untouched.
YouTube's own overlays must stay clear (user 2026-09-29): it sits ABOVE the player-controls/progress-bar zone
(bottom 13 %), never in the right-hand watermark corner, and never inside the END-SCREEN window (last 20 s) —
the script refuses a placement that overlaps it. Size scales with the video height
(designed at 720p), so it is equally crisp on a 1440p master. Place it at natural breaks, never during a test
or in the first 15 s hook, and at the closing CTA."""
import math, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont

FF = "/workspace/glottos-marketing/.nlmvenv/lib/python3.11/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FPS, DUR = 24, 5.0
RED, GREY, WHITE, DARK = (230, 33, 23, 255), (96, 96, 96, 255), (255, 255, 255, 255), (32, 32, 32, 255)

def ease(x): x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3

def bell(d, cx, cy, r, ang, fill, outline):
    """bell glyph centred at (cx,cy), radius r, rotated by ang degrees around its top"""
    pts = []
    for i in range(0, 181, 10):                                   # dome
        a = math.radians(180 + i); pts.append((cx + 0.55 * r * math.cos(a), cy - 0.25 * r + 0.55 * r * math.sin(a)))
    pts += [(cx + 0.62 * r, cy + 0.35 * r), (cx + 0.85 * r, cy + 0.55 * r), (cx - 0.85 * r, cy + 0.55 * r), (cx - 0.62 * r, cy + 0.35 * r)]
    px, py = cx, cy - 0.85 * r; t = math.radians(ang)
    rot = lambda p: (px + (p[0] - px) * math.cos(t) - (p[1] - py) * math.sin(t), py + (p[0] - px) * math.sin(t) + (p[1] - py) * math.cos(t))
    d.polygon([rot(p) for p in pts], fill=fill, outline=outline, width=max(2, int(r * 0.12)))
    kx, ky = rot((cx, cy + 0.72 * r)); k = 0.16 * r
    d.ellipse([kx - k, ky - k, kx + k, ky + k], fill=outline)
    tx, ty = rot((cx, cy - 0.82 * r)); d.ellipse([tx - k * 0.8, ty - k * 0.8, tx + k * 0.8, ty + k * 0.8], fill=outline)

def cursor(d, x, y, s, press):
    k = s * (0.9 if press else 1.0)
    pts = [(0, 0), (0, 17), (4.5, 13), (7.5, 20), (10, 19), (7, 12), (13, 12)]
    d.polygon([(x + p[0] * k, y + p[1] * k) for p in pts], fill=WHITE, outline=(0, 0, 0, 255), width=max(1, int(s * 0.9)))

def frame(t, S):
    """RGBA frame at time t; S = scale (1.0 at 720p)"""
    W, H = int(430 * S), int(120 * S); im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    appear, leave = ease(t / 0.4), ease((t - (DUR - 0.45)) / 0.45)
    dy = (1 - appear) * 60 * S + leave * 60 * S; alpha = appear * (1 - leave)
    subscribed, rung = t >= 1.65, t >= 3.0
    press_sub = 1.5 <= t < 1.7; press_bell = 2.85 <= t < 3.05
    bx, by, bw, bh = 10 * S, 30 * S + dy, 250 * S, 62 * S           # pill
    sc = 0.95 if press_sub else 1.0
    cxp, cyp = bx + bw / 2, by + bh / 2; w2, h2 = bw * sc / 2, bh * sc / 2
    d.rounded_rectangle([cxp - w2 + 3 * S, cyp - h2 + 4 * S, cxp + w2 + 3 * S, cyp + h2 + 4 * S], radius=h2, fill=(0, 0, 0, 90))
    d.rounded_rectangle([cxp - w2, cyp - h2, cxp + w2, cyp + h2], radius=h2, fill=GREY if subscribed else RED)
    f = ImageFont.truetype(FONT, int((24 if subscribed else 27) * S))
    txt = "SUBSCRIBED ✓" if subscribed else "SUBSCRIBE"
    tw = d.textlength(txt, font=f); d.text((cxp - tw / 2, cyp), txt, font=f, fill=WHITE, anchor="lm")
    gx, gy, gr = bx + bw + 58 * S, cyp, 31 * S * (0.93 if press_bell else 1.0)  # bell button
    d.ellipse([gx - gr + 3 * S, gy - gr + 4 * S, gx + gr + 3 * S, gy + gr + 4 * S], fill=(0, 0, 0, 90))
    d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=WHITE, outline=DARK, width=int(3 * S))
    ang = 0.0
    if rung and t < 4.2: ang = 24 * math.sin((t - 3.0) * 26) * math.exp(-(t - 3.0) * 2.2)
    bell(d, gx, gy, 20 * S, ang, (255, 196, 0, 255) if rung else WHITE, DARK)
    if rung and t < 4.0:                                             # ring waves
        k = (t - 3.0) * 1.0
        for side in (-1, 1):
            for n in range(2):
                rr = (26 + 9 * n + 8 * k) * S
                d.arc([gx - rr, gy - rr, gx + rr, gy + rr], 300 if side > 0 else 210, 330 if side > 0 else 240,
                      fill=(255, 196, 0, int(255 * max(0, 1 - k))), width=int(3 * S))
    # cursor path: enter from right -> SUBSCRIBE (1.5) -> bell (2.85) -> drift away
    keys = [(0.5, (W - 5 * S, H + 10 * S)), (1.35, (cxp + 40 * S, cyp + 6 * S)), (1.75, (cxp + 40 * S, cyp + 6 * S)),
            (2.7, (gx + 4 * S, gy + 6 * S)), (3.3, (gx + 4 * S, gy + 6 * S)), (4.2, (W, H + 20 * S))]
    if keys[0][0] <= t <= keys[-1][0]:
        for (t0, p0), (t1, p1) in zip(keys, keys[1:]):
            if t0 <= t <= t1:
                u = ease((t - t0) / (t1 - t0)); cursor(d, p0[0] + (p1[0] - p0[0]) * u, p0[1] + (p1[1] - p0[1]) * u, 1.6 * S, press_sub or press_bell)
    if alpha < 1:
        a = im.getchannel("A").point(lambda v: int(v * alpha)); im.putalpha(a)
    return im

def probe(path):
    import re
    err = subprocess.run([FF, "-hide_banner", "-i", path], capture_output=True, text=True).stderr
    m = re.search(r"Video: .*?(\d{3,5})x(\d{3,5})", err); du = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err)
    return int(m.group(1)), int(m.group(2)), int(du.group(1)) * 3600 + int(du.group(2)) * 60 + float(du.group(3))

def main():
    a = sys.argv[1:]; src, out = a[0], a[1]
    at = [float(x) for x in a[a.index("--at") + 1].split(",")]
    corner = a[a.index("--corner") + 1] if "--corner" in a else "bl"
    W, H, dur = probe(src); S = H / 720
    for t in at:
        if t + DUR > dur - 20: sys.exit(f"--at {t}: overlaps YouTube's end-screen window (last 20 s of {dur:.2f}s)")
        if t < 15: sys.exit(f"--at {t}: inside the first-15-s hook")
    tmp = a[a.index("--frames-only") + 1] if "--frames-only" in a else tempfile.mkdtemp(prefix="subanim-")
    os.makedirs(tmp, exist_ok=True)
    for i in range(int(DUR * FPS)): frame(i / FPS, S).save(f"{tmp}/{i:03d}.png")
    if "--frames-only" in a: print("frames ->", tmp); return
    fw, fh = Image.open(f"{tmp}/000.png").size; m = int(18 * S)
    x = {"bl": m, "bc": (W - fw) // 2}[corner]; y = H - fh - int(0.13 * H)     # above the controls bar
    cmd = [FF, "-v", "error", "-y", "-i", src]
    for t in at: cmd += ["-framerate", str(FPS), "-itsoffset", f"{t:.3f}", "-i", f"{tmp}/%03d.png"]
    chain, last = [], "0:v"
    for n in range(len(at)):
        chain.append(f"[{last}][{n + 1}:v]overlay={x}:{y}:eof_action=pass:format=auto[v{n}]"); last = f"v{n}"
    enc = ["-c:v", "libx264", "-preset", "medium", "-crf", "16" if H >= 1440 else "18", "-profile:v", "high", "-pix_fmt", "yuv420p"]
    cmd += ["-filter_complex", ";".join(chain), "-map", f"[{last}]", "-map", "0:a", *enc, "-c:a", "copy", "-movflags", "+faststart", "-threads", "4", out]
    subprocess.run(cmd, check=True)
    W2, H2, d2 = probe(out)
    if (W2, H2) != (W, H) or abs(d2 - dur) > 0.1: sys.exit(f"check failed: {W2}x{H2} {d2}s vs {W}x{H} {dur}s")
    print(f"OK {out}: {W2}x{H2}, {d2:.2f}s, subscribe+bell at {at} ({corner})")

if __name__ == "__main__":
    main()
