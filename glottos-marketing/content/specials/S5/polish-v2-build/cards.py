# On-screen text/patch overlays for S5 v2 (all RGBA, full frame 1280x720). Every string here needs the
# language-editor gate.
from PIL import Image, ImageDraw, ImageFont
import math
W, H = 1280, 720; S = 3
FB = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
FR = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
def f(p, s): return ImageFont.truetype(p, s * S)
def canvas():
    im = Image.new('RGBA', (W * S, H * S), (0, 0, 0, 0)); return im, ImageDraw.Draw(im)
def save(im, name): im.resize((W, H), Image.LANCZOS).save(name)
INK = (26, 26, 26, 255); WHITE = (255, 255, 255, 255)

# 1) House patch: cover the burning house + its flame/smoke at the left of the disaster/ending card (focus.txt
#    bans drawing fire). Box confirmed on qa/house_fine2.png: flames/house occupy about x25-220, y150-345; the
#    sprinkler spray column starts about x280+, so the patch (x0-235, y0-360) stays clear of it with margin. The
#    patch is anchored to the frame's own top-left corner (x0,y0) so two of its four edges need no blending at
#    all; the paper colour/grid are sampled from clean paper in this same frame (qa/f_250.png (10,10)/(5,60) =
#    ~(244,242,238)) and the remaining (right/bottom) edges are feathered so the patch blends into the paper
#    rather than showing a hard box seam. No new "wet guests"/sprinkler added (a plain patch was cleaner and
#    lower-risk than a hand-drawn sprinkler that might look inconsistent with the rest of this scene's art).
from PIL import ImageFilter
PX0, PY0, PX1, PY1 = 0, 0, 235, 360
FEATHER = 26
patch_im = Image.new('RGBA', (W * S, H * S), (0, 0, 0, 0))
pd = ImageDraw.Draw(patch_im)
PAPER = (244, 242, 238, 255); GRID = (227, 227, 223, 255)
pd.rectangle((PX0 * S, PY0 * S, PX1 * S, PY1 * S), fill=PAPER)
for gx in range(0, PX1 + 33, 33):
    pd.line((gx * S, PY0 * S, gx * S, PY1 * S), fill=GRID, width=1)
for gy in range(0, PY1 + 33, 33):
    pd.line((PX0 * S, gy * S, PX1 * S, gy * S), fill=GRID, width=1)
mask = patch_im.split()[3].filter(ImageFilter.GaussianBlur(FEATHER))
patch_im.putalpha(mask)
# re-flatten the two frame-edge sides back to fully opaque (only the inner right/bottom edges should fade)
pd2 = ImageDraw.Draw(patch_im)
pd2.rectangle((0, 0, (PX0 + FEATHER) * S, PY1 * S), fill=PAPER)
pd2.rectangle((0, 0, PX1 * S, (PY0 + FEATHER) * S), fill=PAPER)
for gx in range(0, PX0 + FEATHER + 33, 33):
    pd2.line((gx * S, PY0 * S, gx * S, PY1 * S), fill=GRID, width=1)
for gy in range(0, PY0 + FEATHER + 33, 33):
    pd2.line((PX0 * S, gy * S, PX1 * S, gy * S), fill=GRID, width=1)
im, d = canvas()
im.alpha_composite(patch_im)
assert PX1 < 270, 'house patch must stay clear of the spray column at x~280+'
save(im, 'house_patch.png')

# 2) Grandmother's speech bubble: "Best birthday in ninety years!" (spoken verbatim at 255.40s), wrapped to two
#    lines inside the empty bubble. Bubble interior confirmed on qa/f_250.png: oval roughly x715-945, y500-615
#    (tail points down-right toward grandmother, not used for text).
im, d = canvas()
fL = f(FB, 20)
lines = ['Best birthday', 'in ninety years!']
cx, y0, lh = 815, 550, 34
for i, line in enumerate(lines):
    y = y0 + i * lh
    d.text((cx * S, y * S), line, font=fL, fill=INK, anchor='mm')
    w = d.textlength(line, font=fL)
    assert cx * S - w / 2 > 735 * S and cx * S + w / 2 < 895 * S, (line, w)
assert y0 - 12 > 508 and y0 + lh + 14 < 636
save(im, 'bubble.png')

# 3) Trouble card: second caption line under "problems and worry.", reusing the exact phrase already used (and
#    gate-approved) in the ladder row for trouble (script.md Beat 5): '"In trouble": someone is angry with you.'
im, d = canvas()
fT = f(FB, 26)
tx, ty = 130, 605
line = '"In trouble": someone is angry with you.'
d.text((tx * S, ty * S), line, font=fT, fill=WHITE, anchor='lm')
w = d.textlength(line, font=fT)
assert tx * S + w < 970 * S and ty < 645, (line, w, ty)
save(im, 'trouble2.png')
print('ok')
