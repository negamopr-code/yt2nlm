# On-screen text overlays for S4 v2 (all RGBA, full frame 1280x720). Every string here needs the language-editor gate.
from PIL import Image, ImageDraw, ImageFont
import numpy as np
W,H=1280,720; S=3
FB='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
FR='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
def f(p,s): return ImageFont.truetype(p,s*S)
def canvas():
    im=Image.new('RGBA',(W*S,H*S),(0,0,0,0)); return im,ImageDraw.Draw(im)
def save(im,name): im.resize((W,H),Image.LANCZOS).save(name)
INK=(26,26,26,255); HLBOX=(206,218,250,255)

# 1) Ending card: patch "The happy couple takes it home." -> the gate wording ("The bride and groom take the goat home."),
#    keep "The best photo of the day is the goat!" unchanged. Reconstruct the grid-paper background under the text
#    (sampled per row from clean columns of the same frame, x1030-1270, which are clear at this y-range) and redraw
#    all three lines in the same place, font and size as the original card.
src=Image.open('qa/f_291.png').convert('RGB')
im,d=canvas()
def paint_patch(px0,px1,py0,py1):
    patch=np.zeros((py1-py0,px1-px0,3),dtype=np.uint8)
    clean=np.array(src)[py0:py1,1030:1270]
    for row in range(patch.shape[0]):
        patch[row,:]=clean[row].mean(axis=0).astype(np.uint8)
    big=Image.fromarray(patch).resize(((px1-px0)*S,(py1-py0)*S),Image.BILINEAR).convert('RGBA')
    im.paste(big,(px0*S,py0*S))
patch_x0,patch_x1=185,1015
patch_y0,patch_y1=242,476
paint_patch(patch_x0,patch_x1,patch_y0,patch_y1)
paint_patch(235,1015,476,500)  # mop up the old highlight tail below the last line, staying clear of the goat (x<225)
fe=f(FR,62); fem=ImageFont.truetype(FR,62)  # fem = unscaled, for measuring in frame units
lines=[('The best photo of the day is',[]),
       ('the goat! The bride and',[('goat!',HLBOX)]),
       ('groom take the goat home.',[('home.',HLBOX)])]
x0,y0,lh=201,250,86
for i,(line,hls) in enumerate(lines):
    y=y0+i*lh
    for word,color in hls:
        idx=line.find(word); pre=line[:idx]
        wx=x0+d.textlength(pre,font=fem)
        ww=d.textlength(word,font=fem)
        d.rounded_rectangle(((wx-4)*S,(y+2)*S,(wx+ww+4)*S,(y+58)*S),radius=10*S,fill=color)
    d.text((x0*S,y*S),line,font=fe,fill=INK,anchor='la')
save(im,'ending.png')

# 2) Reveal card: the 5 extras as chips, in the clear band under the speech-bubble box.
im,d=canvas()
fl=f(FB,24); fc=f(FB,25)
words=['picturesque','graceful','striking','radiant','breathtaking']
gap=14*S; ws=[d.textlength(w_,font=fc)+30*S for w_ in words]
tot=sum(ws)+gap*(len(ws)-1)
x=(W*S-tot)/2; y=620*S
for w_,wd in zip(words,ws):
    d.rounded_rectangle((x,y-25*S,x+wd,y+25*S),radius=14*S,fill=(232,120,30,255))
    d.text((x+wd/2,y),w_,font=fc,fill=(255,255,255,255),anchor='mm'); x+=wd+gap
assert x-gap<1220*S and (W*S-tot)/2>60*S
save(im,'extras.png')

# 3) CTA plate on the top band of the "Which score was higher?" card.
def plate(name,l1,l2=None,c2=(255,226,110,255)):
    im,d=canvas()
    f1=f(FB,40); f2=f(FB,30)
    w=max(d.textlength(l1,font=f1),d.textlength(l2,font=f2) if l2 else 0)+80*S
    xa,xb=W*S/2-w/2,W*S/2+w/2; ya,yb=12*S,(104 if l2 else 86)*S
    assert xa>60*S and xb<1220*S
    d.rounded_rectangle((xa,ya,xb,yb),radius=18*S,fill=(24,30,38,236))
    d.text((W*S/2,(44 if l2 else 50)*S),l1,font=f1,fill=(255,255,255,255),anchor='mm')
    if l2: d.text((W*S/2,84*S),l2,font=f2,fill=c2,anchor='mm')
    save(im,name)
plate('cta.png','Comment your two scores:','list vs story')
print('ok')
