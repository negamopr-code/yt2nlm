# (1) blue_card.png: "One story. 15 pictures." card held over the early Blue card (src 42.29-57.7 s), paper-grid look of the pause cards.
# (2) cta.png: comment call to action over the score card (src 431.67-433.67 s + the 3 s hold). RGBA.
from PIL import Image, ImageDraw, ImageFont
W,H=1280,720; S=2
FB='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
FR='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
FI='/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf'
def f(p,s): return ImageFont.truetype(p,s*S)
PAPER=(248,247,243); GRID=(226,228,232); INK=(32,33,36); GREY=(110,112,118); HL=(255,226,110)
im=Image.new('RGB',(W*S,H*S),PAPER); d=ImageDraw.Draw(im)
for x in range(0,W,40): d.line((x*S,0,x*S,H*S),fill=GRID,width=S)
for y in range(0,H,40): d.line((0,y*S,W*S,y*S),fill=GRID,width=S)
A='One story.'; B='15 words.'; C='Now watch the story.'
fa,fc=f(FB,84),f(FI,34)
d.text((W//2*S,270*S),A,font=fa,fill=INK,anchor='mm')
wb=d.textlength(B,font=fa)
d.rounded_rectangle((W//2*S-wb/2-14*S,338*S,W//2*S+wb/2+14*S,432*S),radius=14*S,fill=HL)
d.text((W//2*S,385*S),B,font=fa,fill=INK,anchor='mm')
d.text((W//2*S,500*S),C,font=fc,fill=GREY,anchor='mm')
im.resize((W,H),Image.LANCZOS).save('blue_card.png')
# CTA
im=Image.new('RGBA',(W*S,H*S),(0,0,0,0)); d=ImageDraw.Draw(im)
l1='Which score was higher?'; l2='Comment your two scores: list vs story.'
f1,f2=f(FB,58),f(FB,38)
w1,w2=d.textlength(l1,font=f1),d.textlength(l2,font=f2)
pw=max(w1,w2)+80*S; x0=W*S//2-pw/2; x1=W*S//2+pw/2; y0,y1=200*S,420*S
assert x0>60*S and x1<1220*S
d.rounded_rectangle((x0,y0,x1,y1),radius=22*S,fill=(24,30,38,232))
d.text((W*S//2,285*S),l1,font=f1,fill=(255,255,255,255),anchor='mm')
d.text((W*S//2,358*S),l2,font=f2,fill=(255,226,110,255),anchor='mm')
im.resize((W,H),Image.LANCZOS).save('cta.png'); print('ok')
