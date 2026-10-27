# On-screen text overlays for S3 v2 (all RGBA, full frame 1280x720). Every string here needs the language-editor gate.
from PIL import Image, ImageDraw, ImageFont
W,H=1280,720; S=3
FB='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
FR='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
def f(p,s): return ImageFont.truetype(p,s*S)
def canvas(): 
    im=Image.new('RGBA',(W*S,H*S),(0,0,0,0)); return im,ImageDraw.Draw(im)
def save(im,name): im.resize((W,H),Image.LANCZOS).save(name)
INK=(26,26,26,255)
# 1) whopping: word + meaning on the yellow card, top-left free area (truck scene)
im,d=canvas()
d.text((100*S,132*S),'whopping',font=f(FB,66),fill=INK)
fm=f(FR,29)
for i,l in enumerate(['Very big. Informal, often','right before a number.']):
    d.text((102*S,222*S+i*38*S),l,font=fm,fill=INK)
assert 102*S+max(d.textlength(l,font=fm) for l in ['Very big. Informal, often','right before a number.'])<425*S
save(im,'whop.png')
# 2) towering: patch the old caption (yellow, sampled per row on the right of the text) and write the corrected one
src=Image.open('qa/full_260.png').convert('RGB')
im,d=canvas()
x0,x1,y0,y1=268,884,418,512
for y in range(y0,y1):
    c=src.getpixel((950,y)); d.rectangle((x0*S,y*S,x1*S,(y+1)*S),fill=c+(255,))
fm=f(FR,33)
for i,l in enumerate(['Very tall. A bit literary,','only before a noun.']):
    d.text((277*S,426*S+i*44*S),l,font=fm,fill=(26,26,26,255))
save(im,'tower.png')
# 3) pause card 2: "In order." highlighted like the other key words
im,d=canvas()
fp=f(FR,60); t='In order.'
w=d.textlength(t,font=fp)
d.rounded_rectangle((572*S,498*S,572*S+w+34*S,578*S),radius=18*S,fill=(206,218,250,255))
d.text((589*S,538*S),t,font=fp,fill=(20,20,20,255),anchor='lm')
save(im,'inorder.png')
# 4) reveal: name the five extras
im,d=canvas()
fl=f(FB,26); fc=f(FB,27)
words=['bulky','hefty','whopping','towering','mammoth']
label='The extras:'
gap=12*S; ws=[d.textlength(w_,font=fc)+30*S for w_ in words]
tot=d.textlength(label,font=fl)+24*S+sum(ws)+gap*(len(ws)-1)
x=(W*S-tot)/2-20*S; y=545*S
d.text((x,y),label,font=fl,fill=(60,50,40,255),anchor='lm'); x+=d.textlength(label,font=fl)+24*S
for w_,wd in zip(words,ws):
    d.rounded_rectangle((x,y-26*S,x+wd,y+26*S),radius=14*S,fill=(232,120,30,255))
    d.text((x+wd/2,y),w_,font=fc,fill=(255,255,255,255),anchor='mm'); x+=wd+gap
assert x-gap<1120*S and (W*S-tot)/2-20*S>150*S
save(im,'extras.png')
# 5) CTA plates on the top band of the closing card (also covers the untaught Gargantuan/Colossal/Titanic tags)
def plate(name,l1,l2=None,c2=(255,226,110,255)):
    im,d=canvas()
    f1=f(FB,46); f2=f(FB,32)
    w=max(d.textlength(l1,font=f1),d.textlength(l2,font=f2) if l2 else 0)+90*S
    xa,xb=W*S/2-w/2,W*S/2+w/2; ya,yb=22*S,(120 if l2 else 100)*S
    assert xa>60*S and xb<1220*S
    d.rounded_rectangle((xa,ya,xb,yb),radius=20*S,fill=(24,30,38,236))
    d.text((W*S/2,(52 if l2 else 62)*S),l1,font=f1,fill=(255,255,255,255),anchor='mm')
    if l2: d.text((W*S/2,96*S),l2,font=f2,fill=c2,anchor='mm')
    save(im,name)
plate('cta1.png','Comment your two scores:','list vs story')
plate('cta2.png','Tonight: one silly story,','one picture for each word')
plate('cta3.png','Look up: another word for big')
print('ok')
