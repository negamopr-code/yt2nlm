# Watercolour-style panel for the empty "complication" card (src 142.83-153.88): the parrot flying out from
# under your hat and landing in the cream on top of the birthday cake, feathers everywhere, an "Uh-oh!" bubble
# (script.md Beat 3 #8). Full-frame RGBA overlay, transparent outside the drawing; sits on the card's own solid
# blue background (same composition as every other story card in this video: colour art directly on flat blue),
# in the empty upper area above the word/meaning text (safe box x120-950, y110-445 in the 1280x720 frame,
# confirmed against qa/f_148.png: card x~98-1000, word 'complication' starts at y~460).
import math
from PIL import Image, ImageDraw, ImageFont
W, H = 1280, 720; S = 3
FB = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
def f(p, s): return ImageFont.truetype(p, s * S)
OUT = (20, 20, 24, 255); LW = 3
def P(pts): return [(x * S, y * S) for x, y in pts]
def poly(d, pts, fill, outline=OUT, w=LW):
    d.polygon(P(pts), fill=fill); d.line(P(pts + [pts[0]]), fill=outline, width=w * S, joint='curve')
def ell(d, box, fill, outline=OUT, w=LW):
    d.ellipse(P(box)[0] + P(box)[1], fill=fill, outline=outline, width=w * S)
im = Image.new('RGBA', (W * S, H * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)

cake_bottom = 445
# ---- table ----
d.line(P([(300, cake_bottom), (840, cake_bottom)]), fill=OUT, width=3 * S)
# ---- 3-tier birthday cake (white fondant, pastel drips), no candles yet (they come later, at "crisis") ----
tiers = [  # (x0,y0,x1,y1, drip colour)
    (380, cake_bottom - 50, 760, cake_bottom, (255, 205, 210, 255)),
    (415, cake_bottom - 95, 725, cake_bottom - 45, (200, 230, 255, 255)),
    (450, cake_bottom - 135, 690, cake_bottom - 90, (255, 235, 170, 255)),
]
for x0, y0, x1, y1, drip in tiers:
    d.rounded_rectangle((x0 * S, y0 * S, x1 * S, y1 * S), radius=8 * S, fill=(255, 255, 255, 255), outline=OUT, width=LW * S)
    for lx in range(x0 + 14, x1 - 10, 28):
        dh = 12 + (lx * 7) % 14
        poly(d, [(lx, y0), (lx + 12, y0), (lx + 6, y0 + dh)], drip)
    for dx in range(x0 + 26, x1 - 20, 36):
        ell(d, [(dx, (y0 + y1) / 2 - 5), (dx + 10, (y0 + y1) / 2 + 5)], (255, 255, 255, 0), outline=(120, 120, 126, 255), w=2)

# ---- the cream splash where the parrot lands (right on top of the top tier) ----
splash_cx, splash_cy = 570, tiers[2][1] - 4
ell(d, [(splash_cx - 90, splash_cy - 24), (splash_cx + 90, splash_cy + 26)], (255, 255, 255, 255), outline=OUT, w=LW)
for ang in range(0, 360, 30):
    rx = splash_cx + 92 * math.cos(math.radians(ang)) * 0.9
    ry = splash_cy + 22 * math.sin(math.radians(ang)) * 0.9
    ell(d, [(rx - 7, ry - 7), (rx + 7, ry + 7)], (255, 255, 255, 255), outline=OUT, w=2)

# ---- feathers flying everywhere (simple green ovals with a shaft line), all inside the safe box ----
feather_spots = [(220, 200), (260, 320), (200, 400), (860, 190), (900, 300), (870, 400),
                  (620, 150), (400, 150), (180, 280), (820, 420), (330, 420), (700, 420)]
for i, (fx, fy) in enumerate(feather_spots):
    ang = (i * 37) % 180 - 90
    im2 = Image.new('RGBA', (36 * S, 18 * S), (0, 0, 0, 0)); d2 = ImageDraw.Draw(im2)
    d2.ellipse((0, 0, 36 * S, 18 * S), fill=(90, 200, 120, 255), outline=OUT, width=2 * S)
    d2.line((0, 9 * S, 36 * S, 9 * S), fill=OUT, width=1 * S)
    im2 = im2.rotate(ang, expand=True)
    im.alpha_composite(im2, (fx * S - im2.width // 2, fy * S - im2.height // 2))

# ---- the green parrot, upside down, wings wide open, diving head-first into the cream ----
px, py = splash_cx - 10, splash_cy - 68  # parrot body centre, just above the splash
poly(d, [(px - 18, py - 6), (px - 108, py - 56), (px - 98, py - 14), (px - 26, py + 20)], (60, 170, 90, 255))
poly(d, [(px + 18, py - 6), (px + 108, py - 56), (px + 98, py - 14), (px + 26, py + 20)], (60, 170, 90, 255))
d.line(P([(px - 108, py - 56), (px - 54, py - 30)]), fill=OUT, width=2 * S)
d.line(P([(px + 108, py - 56), (px + 54, py - 30)]), fill=OUT, width=2 * S)
poly(d, [(px - 10, py - 40), (px, py - 80), (px + 10, py - 40)], (230, 90, 90, 255))  # tail feathers, pointing up
ell(d, [(px - 26, py - 18), (px + 26, py + 38)], (70, 190, 110, 255))                  # body
ell(d, [(px - 17, py + 26), (px + 17, py + 60)], (80, 205, 120, 255))                  # head, leading the dive
poly(d, [(px - 5, py + 54), (px + 5, py + 54), (px, py + 70)], (240, 170, 40, 255))    # beak
d.ellipse(P([(px - 7, py + 34), (px - 2, py + 39)])[0] + P([(px - 7, py + 34), (px - 2, py + 39)])[1], fill=OUT)  # eye
d.line(P([(px - 7, py - 18), (px - 14, py - 34)]), fill=(240, 170, 40, 255), width=3 * S)   # feet up
d.line(P([(px + 7, py - 18), (px + 14, py - 34)]), fill=(240, 170, 40, 255), width=3 * S)
for k in range(3):  # motion lines behind the parrot
    yy = py - 66 + k * 18
    d.line(P([(px - 4 - k * 10, yy), (px - 4 - k * 10, yy - 24)]), fill=(255, 255, 255, 180), width=3 * S)

# ---- "Uh-oh!" speech bubble, to the upper right of the parrot ----
bx0, by0, bx1, by1 = px + 70, py - 96, px + 250, py - 42
d.rounded_rectangle((bx0 * S, by0 * S, bx1 * S, by1 * S), radius=16 * S, fill=(255, 255, 255, 255), outline=OUT, width=LW * S)
poly(d, [(bx0 + 28, by1), (bx0 + 12, by1 + 20), (bx0 + 46, by1)], (255, 255, 255, 255))
d.line(P([(bx0 + 28, by1), (bx0 + 12, by1 + 20)]), fill=OUT, width=LW * S)
d.line(P([(bx0 + 46, by1), (bx0 + 12, by1 + 20)]), fill=OUT, width=LW * S)
ftxt = f(FB, 24)
d.text(((bx0 + bx1) / 2 * S, (by0 + by1) / 2 * S), 'Uh-oh!', font=ftxt, fill=(30, 30, 34, 255), anchor='mm')
assert bx0 > 120 and bx1 < 950 and by0 > 110, ('bubble out of safe box', bx0, by0, bx1, by1)
assert min(x for x, y in feather_spots) > 120 and max(x for x, y in feather_spots) < 950
assert min(y for x, y in feather_spots) > 110 and max(y for x, y in feather_spots) < 445

out = im.resize((W, H), Image.LANCZOS)
out.save('complication.png')
print('ok, bubble box', bx0, by0, bx1, by1, 'parrot top', py - 80)
