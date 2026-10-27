# Full-frame 15-row single-column ladder (replaces NotebookLM's 8-row table, src 281.38-343.79).
# Text: content/specials/S5/script.md Beat 5, verbatim gated recap wording. Row 0=hiccup ... row 14=disaster.
from PIL import Image, ImageDraw, ImageFont
W, H = 1280, 720; S = 2
FR = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
FB = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
FI = '/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf'
PAPER = (248, 247, 243); GRID = (226, 228, 232); INK = (32, 33, 36); GREY = (110, 112, 118)
CARD = (255, 255, 255); LINE = (222, 224, 228); HL = (255, 226, 110); RAIL = (150, 120, 90); EXTRA = (232, 120, 30)
# word, meaning (verbatim script.md Beat 5 line, word-for-word), extra?
ROWS = [
    ('Hiccup', 'a small problem or a short delay.', 1),
    ('Snag', 'a problem, often small, hidden or unexpected. Informal.', 0),
    ('Hitch', 'a problem that causes a short delay.', 0),
    ('Glitch', 'a small fault that stops something working. Often machines and computers.', 1),
    ('Issue', 'a problem or worry. Often used at work.', 0),
    ('Difficulty', 'a problem. "I have difficulty doing it."', 0),
    ('Obstacle', 'something in your way.', 0),
    ('Complication', 'something that makes a situation more difficult.', 1),
    ('Setback', 'a problem that delays your progress.', 0),
    ('Headache', 'something that causes a lot of worry.', 0),
    ('Trouble', 'problems and worry. "In trouble": someone is angry with you.', 0),
    ('Dilemma', 'a very difficult choice, often between two things.', 0),
    ('Predicament', 'a difficult situation that is hard to get out of.', 1),
    ('Crisis', 'a time of great danger or difficulty.', 1),
    ('Disaster', 'a very bad situation or a complete failure. Also a flood or a fire.', 0),
]
TITLE = 'The ladder: small problem → very serious problem'
NOTE = 'The order is a guide, not a rule.'
HEAD = ('word', 'meaning')
FOOT = 'Read downward: small problem, then very serious problem.'
FOOT2 = '= one of the 5 sneaky extras'
X0, X1 = 60, 1220
CW = (X0 + 24, 300)
Y0 = 96; RH = 39.6
def f(p, s): return ImageFont.truetype(p, s * S)
def draw(hl=None):
    im = Image.new('RGB', (W * S, H * S), PAPER); d = ImageDraw.Draw(im)
    for x in range(0, W, 40): d.line((x * S, 0, x * S, H * S), fill=GRID, width=S)
    for y in range(0, H, 40): d.line((0, y * S, W * S, y * S), fill=GRID, width=S)
    ft = f(FB, 27); d.text((X0 * S, 14 * S), TITLE, font=ft, fill=INK)
    fn = f(FI, 18); d.text((X0 * S, 43 * S), NOTE, font=fn, fill=GREY)
    y1 = Y0 + 15 * RH + 6
    d.rounded_rectangle((X0 * S, 65 * S, X1 * S, y1 * S), radius=14 * S, fill=CARD, outline=LINE, width=2 * S)
    fh = f(FB, 16)
    for x, t in zip(CW, HEAD): d.text((x * S, 72 * S), t.upper(), font=fh, fill=GREY)
    fw, fm = f(FB, 19), f(FR, 17)
    for i, (w, m, ex) in enumerate(ROWS):
        y = Y0 + i * RH
        if hl == i: d.rounded_rectangle(((X0 + 6) * S, (y + 2) * S, (X1 - 6) * S, (y + RH - 2) * S), radius=8 * S, fill=HL)
        if i > 0: d.line(((X0 + 14) * S, y * S, (X1 - 14) * S, y * S), fill=LINE, width=S)
        cy = (y + RH / 2) * S
        if ex: d.ellipse(((X0 + 14) * S, cy - 6 * S, (X0 + 26) * S, cy + 6 * S), fill=EXTRA)
        d.text((CW[0] * S, cy), w, font=fw, fill=INK, anchor='lm')
        d.text((CW[1] * S, cy), m, font=fm, fill=INK, anchor='lm')
        assert CW[0] * S + d.textlength(w, font=fw) < (CW[1] - 10) * S, w
        assert CW[1] * S + d.textlength(m, font=fm) < (X1 - 10) * S, m
    lx, rx = 24, 44; top, bot = Y0 + 2, Y0 + 15 * RH - 2
    d.line((lx * S, top * S, lx * S, bot * S), fill=RAIL, width=4 * S); d.line((rx * S, top * S, rx * S, bot * S), fill=RAIL, width=4 * S)
    for i in range(15):
        y = Y0 + i * RH + RH / 2; d.line((lx * S, y * S, rx * S, y * S), fill=RAIL, width=3 * S)
        if hl == i: d.ellipse(((lx + rx) // 2 * S - 8 * S, y * S - 8 * S, (lx + rx) // 2 * S + 8 * S, y * S + 8 * S), fill=HL, outline=RAIL, width=2 * S)
    d.polygon([((lx + rx) // 2 * S, (bot + 26) * S), ((lx - 6) * S, (bot + 9) * S), ((rx + 6) * S, (bot + 9) * S)], fill=RAIL)
    fs = f(FI, 17); d.text((X0 * S, 700 * S), FOOT, font=fs, fill=GREY, anchor='lm')
    fw2 = d.textlength(FOOT, font=fs)
    ex0 = X0 * S + fw2 + 28 * S
    d.ellipse((ex0, 700 * S - 6 * S, ex0 + 12 * S, 700 * S + 6 * S), fill=EXTRA)
    d.text((ex0 + 18 * S, 700 * S), FOOT2, font=fs, fill=GREY, anchor='lm')
    assert ex0 + 18 * S + d.textlength(FOOT2, font=fs) < X1 * S
    return im.resize((W, H), Image.LANCZOS)
draw().save('ladder_base.png')
for i in range(15): draw(i).save(f'ladder_hl_{i:02d}.png')
print('ok')
