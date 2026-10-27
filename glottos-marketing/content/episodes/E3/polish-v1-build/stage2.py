# stage 2: 9:16 1440x2560 composite (design units 1080x1920 x K=4/3): brand top bar, centered picture, cards, DAY chips, word-synced captions.
import sys, json
sys.path.insert(0, '/workspace/glottos-marketing/shorts')
from PIL import Image, ImageDraw, ImageFont
import subprocess
from plan import *
import build_short_v2 as B
K = 4/3
def S(v): return int(round(v*K))
BG, INK, MUTED, ACCENT, HOT = B.BG, B.INK, B.MUTED, B.ACCENT, B.HOT
FB, FR_ = B.FB, B.FR
def ft(p, s): return ImageFont.truetype(p, S(s))
W, H = 1440, 2560
PIC_Y = S(400); PIC_W, PIC_H = 1440, 810          # 16:9 picture at native width
bar = B.top_bar('Words That Stick', 3).resize((S(1080), S(300)), Image.LANCZOS)
base = Image.new('RGB', (W, H), BG); base.paste(bar.convert('RGB'), (0, 0)); base.save('base.png')

def wrapx(d, text, f, maxw):
    out, cur = [], ''
    for w_ in text.split():
        t = (cur + ' ' + w_).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: out.append(cur); cur = w_
    return out + [cur]
def centered(d, y, text, f, fill, W_=PIC_W):
    w = d.textlength(text, font=f); d.text(((W_ - w) / 2, y), text, font=f, fill=fill)
def card(name, draw):
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0)); c = Image.new('RGB', (PIC_W, PIC_H), BG); d = ImageDraw.Draw(c)
    draw(d, c); img.paste(c, (0, PIC_Y)); img.save(name)
def chip(d, cx, y, text, f, fill, fg=(255,255,255), padx=40, h=None):
    w = d.textlength(text, font=f); hh = h or S(84)
    d.rounded_rectangle((cx - w/2 - padx, y, cx + w/2 + padx, y + hh), hh//2, fill=fill); d.text((cx - w/2, y + hh*0.16), text, font=f, fill=fg)

def hook(d, c):
    f = ft(FB, 78); lines = ['Review new words on', 'these 3 days only']
    for i, l in enumerate(lines): centered(d, S(70) + i*S(98), l, f, INK)
    xs = [PIC_W*0.2, PIC_W*0.5, PIC_W*0.8]
    for x, n in zip(xs, ['1', '3', '7']):
        d.rounded_rectangle((x - S(120), S(300), x + S(120), S(520)), S(30), fill=(255,255,255), outline=ACCENT, width=S(5))
        w = d.textlength('DAY', font=ft(FB, 40)); d.text((x - w/2, S(325)), 'DAY', font=ft(FB, 40), fill=MUTED)
        w = d.textlength(n, font=ft(FB, 150)); d.text((x - w/2, S(365)), n, font=ft(FB, 150), fill=HOT)
card('c_hook.png', hook)
def five(d, c):
    centered(d, S(130), '5 ways to say', ft(FB, 80), MUTED); centered(d, S(240), 'STRONG', ft(FB, 170), HOT)
    for i in range(5): d.ellipse((PIC_W/2 - S(150) + i*S(75), S(480), PIC_W/2 - S(150) + i*S(75) + S(36), S(516)), fill=ACCENT)
card('c_five.png', five)
logo = Image.open(B.LOGO).convert('RGB')
def cta(d, c):
    L = S(260); lg = logo.resize((L, L), Image.LANCZOS); m = Image.new('L', (L, L), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, L-1, L-1), S(40), fill=255)
    c.paste(lg, ((PIC_W - L)//2, S(50)), m)
    centered(d, S(340), 'anotherwordfor.net', ft(FB, 76), ACCENT)
    centered(d, S(450), 'another word for', ft(FR_, 56), INK); centered(d, S(520), 'STRONG', ft(FB, 70), HOT)
card('c_cta.png', cta)
def teaser(d, c):
    chip(d, PIC_W/2, S(80), 'NEXT', ft(FB, 54), ACCENT)
    f = ft(FB, 88)
    for i, l in enumerate(['Why you freeze', 'mid-sentence']): centered(d, S(250) + i*S(112), l, f, INK)
card('c_teaser.png', teaser)

def label(name, text):          # DAY chip under the picture
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    chip(d, W/2, PIC_Y + PIC_H + S(30), text, ft(FB, 60), ACCENT, padx=S(46), h=S(100)); img.save(name)
for n in ('DAY 1', 'DAY 3', 'DAY 7', 'DAY 1 · 3 · 7'): label('l_' + n.replace(' · ', '_').replace(' ', '') + '.png', n)

def caption(name, text):
    f = ft(FB, 62); d0 = ImageDraw.Draw(Image.new('RGB', (1, 1))); lines = wrapx(d0, text, f, S(900))
    h = S(34) + S(76)*len(lines); wm = int(max(d0.textlength(l, font=f) for l in lines) + S(56))
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    x0 = (W - wm)//2; y0 = S(1135)
    d.rounded_rectangle((x0, y0, x0 + wm, y0 + h), S(28), fill=(31, 26, 23, 232))
    for i, l in enumerate(lines): centered(d, y0 + S(15) + S(76)*i, l, f, (255,255,255))
    img.save(name)

words = [x for s in json.load(open('../e3-v1.transcript.json'))['segments'] for x in s['words']]
def ws(i): return max(words[i]['s'], words[i]['e'] - 0.55)
def we(i): return words[i]['e']
CH = [  # (text, first idx, last idx, optional start override)
 ('Review new words', 0, 2), ('on these 3 days only.', 3, 7),
 ('A word sticks best', 11, 13, 4.49), ('when you recall it', 14, 17), ('just before you forget it.', 18, 22),
 ('So, day 1:', 23, 25), ('see the word again', 26, 29), ('in its sentence.', 30, 32),
 ('Then, day 3:', 33, 35), ('cover it up and recall it', 36, 41), ('before you look.', 42, 44),
 ('Think about this:', 45, 47, 16.97), ('You know her face,', 48, 51), ('but not her name.', 52, 55), ('Recognise or recall?', 56, 58),
 ('Well, you recognise the face.', 59, 63, 23.40), ("You just can't recall the name.", 64, 69),
 ('Finally, day 7:', 70, 72), ('use it in a new sentence', 73, 78), ('of your own, out loud.', 79, 83),
 ('Why do this?', 84, 86), ('Each review resets the forgetting curve', 87, 92), ('and it falls more slowly each time.', 93, 99),
 ('After day 7,', 100, 102), ('a word you used yourself', 103, 107), ('is much harder to forget.', 108, 112), ("The memory's strong.", 113, 115),
 ('A good handshake is firm.', 121, 125), ('A ladder that stays steady', 126, 130), ('when you climb it is sturdy.', 131, 136),
 ('Hiking boots that last', 137, 140), ('for years are durable.', 141, 144), ('A huge old oak tree is mighty.', 145, 151),
 ("And a weightlifter's arms are muscular.", 152, 158), ('So remember: days 1, 3 and 7.', 159, 165), ('Not every day, and not just once.', 166, 172),
 ('Try it tomorrow.', 173, 175), ("See today's new words again", 176, 180), ('in their sentences.', 181, 183),
 ('Look up another word for strong', 184, 189), ('on anotherwordfor.net.', 190, 194)]
caps = []
for k, c in enumerate(CH):
    t0 = c[3] if len(c) > 3 else ws(c[1]); t1 = we(c[2])
    if k + 1 < len(CH): nxt = CH[k+1]; t1 = min(t1, (nxt[3] if len(nxt) > 3 else ws(nxt[1])) - 0.02)
    caps.append([c[0], t0, t1])
for c in caps:
    if c[0] == 'Recognise or recall?': c[2] = 22.45 + 2.0 - 0.95 + 0.0 + 0.95      # held through the 2 s quiz pause (source time stand-in, mapped below)
ovs = []   # (png, out_start_s, out_end_s)
for i, (t, a, b) in enumerate(caps):
    caption(f'cap_{i:02d}.png', t)
    oa = Ts(a); ob = Ts(b)
    if t == 'Recognise or recall?': ob = Ts(23.40)       # visible until the answer starts
    ovs.append((f'cap_{i:02d}.png', oa, ob))
ovs += [('c_hook.png', 0, Ts(4.50)), ('c_five.png', Ts(43.55), Ts(44.80)), ('c_cta.png', Ts(71.70), Ts(76.10)), ('c_teaser.png', Ts(76.10), OUT_FRAMES/FPS),
        ('l_DAY1.png', Ts(8.93), Ts(12.30)), ('l_DAY3.png', Ts(12.30), Ts(16.20)), ('l_DAY7.png', Ts(27.40), Ts(32.00)), ('l_DAY1_3_7.png', Ts(61.50), Ts(66.40))]
OFF = {}
for p in {o[0] for o in ovs}:
    im = Image.open(p); bb = im.getchannel('A').getbbox(); im.crop(bb).save(p); OFF[p] = (bb[0], bb[1])
json.dump(ovs, open('overlays.json', 'w'), indent=0)
dur = OUT_FRAMES / FPS
if '--dry' in sys.argv: sys.exit()
import numpy as np
baseimg = Image.open('base.png').convert('RGB')
ov = [(Image.open(p).convert('RGBA'), OFF[p], a, b) for p, a, b in ovs]
rd = subprocess.Popen([F, '-v', 'error', '-i', 's1_video.mp4', '-vf', f'scale={PIC_W}:{PIC_H}:flags=lanczos', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
wr = subprocess.Popen([F, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', '24', '-i', '-', '-i', 's1_audio.wav',
    '-vf', f'fade=t=out:st={dur-0.35:.3f}:d=0.35,format=yuv420p', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-c:a', 'aac', '-b:a', '160k', '-ar', '44100', '-ac', '1',
    '-movflags', '+faststart', '-shortest', 's2.mp4'], stdin=subprocess.PIPE)
n = 0
while True:
    buf = rd.stdout.read(PIC_W * PIC_H * 3)
    if len(buf) < PIC_W * PIC_H * 3: break
    t = n / FPS; im = baseimg.copy(); im.paste(Image.frombuffer('RGB', (PIC_W, PIC_H), buf, 'raw', 'RGB', 0, 1), (0, PIC_Y))
    for o, (x, y), a, b in ov:
        if a <= t < b: im.paste(o, (x, y), o)
    wr.stdin.write(im.tobytes()); n += 1
wr.stdin.close(); wr.wait(); print('frames', n)
