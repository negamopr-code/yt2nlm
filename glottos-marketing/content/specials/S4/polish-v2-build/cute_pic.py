# Whiteboard-style panel for the empty yellow "cute" card (src 38.33-70.29): tiny mountain railway station,
# "you" in a yellow raincoat and green wellies with a camera round your neck, and the goat's head+eyes
# peeking out of your open camera bag. Full-frame RGBA overlay, transparent outside the drawing.
# Placed in the empty upper area of the card (x100-930, y125-395); text sits below y400, magnifier at x920-1060.
import math
from PIL import Image, ImageDraw, ImageFont
W,H=1280,720; S=3
FB='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
def f(p,s): return ImageFont.truetype(p,s*S)
OUT=(44,34,28,255); LW=3
def P(pts): return [(x*S,y*S) for x,y in pts]
def poly(d,pts,fill,outline=OUT,w=LW):
    d.polygon(P(pts),fill=fill); d.line(P(pts+[pts[0]]),fill=outline,width=w*S,joint='curve')
def rr(d,box,r,fill,outline=OUT,w=LW):
    d.rounded_rectangle([v*S for v in box],radius=r*S,fill=fill,outline=outline,width=w*S)
def ell(d,box,fill,outline=OUT,w=LW):
    d.ellipse(P(box)[0]+P(box)[1],fill=fill,outline=outline,width=w*S)
im=Image.new('RGBA',(W*S,H*S),(0,0,0,0)); d=ImageDraw.Draw(im)

gy=372  # ground / platform line
# ---- background mountains (behind everything) ----
poly(d,[(150,gy-6),(300,155),(430,gy-6)],(176,190,212,255))
poly(d,[(270,155),(300,140),(330,155)],(250,250,250,255))          # snow cap
poly(d,[(560,gy-6),(700,168),(840,gy-6)],(190,202,222,255))
poly(d,[(668,168),(700,150),(730,168)],(250,250,250,255))          # snow cap
# a few birds
for bx,by in [(500,120),(540,108),(470,132)]:
    d.line(P([(bx-10,by),(bx,by-7),(bx+10,by)]),fill=(90,95,110,255),width=2*S,joint='curve')

# ---- platform / ground line ----
d.line(P([(110,gy),(900,gy)]),fill=OUT,width=3*S)
for x in range(120,900,26): d.line(P([(x,gy),(x-8,gy+9)]),fill=(180,150,120,255),width=2*S)

# ---- tiny station building (left) ----
bx0,by0,bx1,by1=150,240,300,gy
rr(d,(bx0,by0,bx1,by1),4,(233,214,168,255))
poly(d,[(bx0-14,by0),((bx0+bx1)/2,by0-46),(bx1+14,by0)],(150,70,60,255))   # pitched roof
rr(d,(bx0+20,by0+18,bx0+70,by0+70),4,(214,236,240,255))                    # window
d.line(P([(bx0+45,by0+18),(bx0+45,by0+70)]),fill=OUT,width=2*S)
d.line(P([(bx0+20,by0+44),(bx0+70,by0+44)]),fill=OUT,width=2*S)
rr(d,(bx1-46,by1-70,bx1-16,by1),4,(150,104,62,255))                        # door
# sign board on two posts
d.line(P([(190,by0-46),(190,by0-70)]),fill=(120,90,60,255),width=4*S)
d.line(P([(260,by0-46),(260,by0-70)]),fill=(120,90,60,255),width=4*S)
rr(d,(178,by0-88,272,by0-58),4,(250,248,240,255))
fsg=f(FB,15); tw=d.textlength('STATION',font=fsg)
d.text(((178+272)/2*S,(by0-73)*S),'STATION',font=fsg,fill=(60,50,40,255),anchor='mm')

# ---- goat hay pile near the station (continuity prop) ----
poly(d,[(320,gy),(365,gy-30),(410,gy)],(226,196,110,255))
for lx in range(325,405,10): d.line(P([(lx,gy),(lx+6,gy-18)]),fill=(196,166,90,255),width=2*S)

# ---- the photographer ("you"): yellow raincoat, hood, camera, green wellies ----
cx=560  # character centre-x
# legs + wellies
for lx in (cx-22,cx+22):
    d.rectangle(P([(lx-9,gy-70),(lx+9,gy-14)])[0]+P([(lx-9,gy-70),(lx+9,gy-14)])[1],fill=(60,90,120,255),outline=OUT,width=3*S)
    poly(d,[(lx-12,gy-2),(lx+9,gy-2),(lx+9,gy+12),(lx+26,gy+16),(lx+26,gy+22),(lx-12,gy+22)],(70,150,90,255))
# raincoat body (a deeper mustard so it still reads against the pure yellow background)
poly(d,[(cx-64,gy-64),(cx+64,gy-64),(cx+78,gy-4),(cx-78,gy-4)],(214,168,26,255))
d.line(P([(cx-30,gy-64),(cx-24,gy-4)]),fill=(180,138,16,255),width=2*S)   # coat fold
d.line(P([(cx+30,gy-64),(cx+24,gy-4)]),fill=(180,138,16,255),width=2*S)
for bx in (cx-2,cx-2,cx-2):
    pass
for k,by in enumerate(range(gy-56,gy-16,14)):
    d.ellipse(P([(cx-4,by-4),(cx+4,by+4)])[0]+P([(cx-4,by-4),(cx+4,by+4)])[1],fill=(150,110,10,255))
# arms
poly(d,[(cx-64,gy-58),(cx-96,gy-30),(cx-88,gy-16),(cx-58,gy-40)],(214,168,26,255))
poly(d,[(cx+64,gy-58),(cx+96,gy-30),(cx+88,gy-16),(cx+58,gy-40)],(214,168,26,255))
# hood + head
ell(d,[(cx-30,gy-118),(cx+30,gy-64)],(214,168,26,255))
ell(d,[(cx-19,gy-108),(cx+19,gy-72)],(250,214,178,255))
d.ellipse(P([(cx-9,gy-96),(cx-3,gy-90)])[0]+P([(cx-9,gy-96),(cx-3,gy-90)])[1],fill=OUT)
d.ellipse(P([(cx+3,gy-96),(cx+9,gy-90)])[0]+P([(cx+3,gy-96),(cx+9,gy-90)])[1],fill=OUT)
d.line(P([(cx-6,gy-80),(cx+6,gy-80)]),fill=OUT,width=2*S,joint='curve')
# camera round the neck: strap + camera box resting on the coat
d.line(P([(cx-26,gy-96),(cx-6,gy-40),(cx+6,gy-40),(cx+26,gy-96)]),fill=(90,66,40,255),width=3*S)
rr(d,(cx-32,gy-52,cx+32,gy-16),4,(58,58,64,255))
ell(d,[(cx-14,gy-46,),(cx+14,gy-22)],(150,190,210,255))
ell(d,[(cx-8,gy-40),(cx+8,gy-28)],(90,140,170,255))
rr(d,(cx-8,gy-58,cx+8,gy-50),2,(58,58,64,255))

# ---- open camera bag at your hip, goat peeking out ----
bagx,bagy=cx+96,gy-26
poly(d,[(bagx-48,bagy-14),(bagx+48,bagy-22),(bagx+54,bagy+34),(bagx-42,bagy+38)],(96,68,42,255))
poly(d,[(bagx-48,bagy-14),(bagx-16,bagy-46),(bagx+38,bagy-36),(bagx+48,bagy-22)],(126,90,54,255))  # open flap
d.line(P([(bagx-48,bagy-14),(bagx-16,bagy-46)]),fill=OUT,width=2*S)
d.line(P([(bagx+38,bagy-36),(bagx+48,bagy-22)]),fill=OUT,width=2*S)
# goat head + big eyes peeking out of the bag opening
poly(d,[(bagx-16,bagy-58),(bagx-6,bagy-80),(bagx+2,bagy-56)],(206,190,156,255))   # left ear/horn
poly(d,[(bagx+0,bagy-60),(bagx+10,bagy-82),(bagx+18,bagy-56)],(206,190,156,255))  # right ear/horn
ell(d,[(bagx-28,bagy-62),(bagx+30,bagy-4)],(248,241,222,255))
d.ellipse(P([(bagx-19,bagy-44),(bagx-3,bagy-28)])[0]+P([(bagx-19,bagy-44),(bagx-3,bagy-28)])[1],fill=(255,255,255,255),outline=OUT,width=2*S)
d.ellipse(P([(bagx+3,bagy-44),(bagx+19,bagy-28)])[0]+P([(bagx+3,bagy-44),(bagx+19,bagy-28)])[1],fill=(255,255,255,255),outline=OUT,width=2*S)
d.ellipse(P([(bagx-14,bagy-38),(bagx-9,bagy-33)])[0]+P([(bagx-14,bagy-38),(bagx-9,bagy-33)])[1],fill=OUT)
d.ellipse(P([(bagx+8,bagy-38),(bagx+13,bagy-33)])[0]+P([(bagx+8,bagy-38),(bagx+13,bagy-33)])[1],fill=OUT)
ell(d,[(bagx-6,bagy-18),(bagx+6,bagy-10)],(226,196,166,255))                      # nose
d.arc(P([(bagx-8,bagy-16),(bagx+8,bagy-2)])[0]+P([(bagx-8,bagy-16),(bagx+8,bagy-2)])[1],20,160,fill=OUT,width=2*S)  # smile

out=im.resize((W,H),Image.LANCZOS)
out.save('cute.png')
print('ok, bbox used approx x150-900 y95-372')
