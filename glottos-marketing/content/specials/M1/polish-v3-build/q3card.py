# Quote 3 card: re-letter body to
#   'Repeat the sentence I made myself over and over' was a game changer for me.
# using glyphs cut from the same card (original Google-Sans-like lettering), plus drawn straight apostrophes.
import cv2, numpy as np
from PIL import Image, ImageDraw
src=cv2.imread('../s_4500.png')          # source frame 4500 (card static 4390-4767)
c=src.copy()
W=255
INK=(25,25,26)  # BGR
# 1) line 1: shift "Repeat the sentence I" (+ yellow box) right by 11 px, leave room for the opening '
dx1=11; y0,y1=212,292
c[y0:y1,285+dx1:880+dx1]=src[y0:y1,285:880]; c[y0:y1,285:285+dx1]=W
# 2) line 3: shift "was a game" (+ yellow box) right by 10 px, closing ' goes after "over"
dx3=10; y0,y1=358,434
c[y0:y1,410+dx3:745+dx3]=src[y0:y1,410:745]; c[y0:y1,410:410+dx3]=W
# 3) line 4: drop the old period, append " for me."
c[474:494,523:537]=W
dy=488-342   # line-2 baseline -> line-4 baseline
def put(x0,x1,xdst,ys=(296,360),dyy=dy,from_=src):
    g=from_[ys[0]:ys[1],x0:x1+1]; yd=ys[0]+dyy
    reg=c[yd:yd+g.shape[0],xdst:xdst+g.shape[1]]
    c[yd:yd+g.shape[0],xdst:xdst+g.shape[1]]=np.minimum(reg,g)
    return xdst+(x1-x0)
x=538
x=put(597,615,x)+2       # f (from "myself")
x=put(630,659,x)+5       # o (from "over")
x=put(724,740,x)+18      # r (from "over")
x=put(296,338,x)+6       # m (from "made")
x=put(407,434,x)+4       # e (from "made")
put(524,532,x,ys=(476,492),dyy=0)   # period (original, same line)
end4=x+8
# 4) straight apostrophes, drawn at 4x, stem width like "l" (6 px), cap-top aligned
S=4
def apostrophe(img,xl,baseline):
    top=baseline-40; h=14
    big=Image.new('L',(40*S,40*S),0); d=ImageDraw.Draw(big)
    # slightly tapered rounded stroke
    wt,wb=6.4,4.8; cx=20*S
    d.polygon([(cx-wt/2*S,2*S),(cx+wt/2*S,2*S),(cx+wb/2*S,(2+h)*S),(cx-wb/2*S,(2+h)*S)],fill=255)
    d.ellipse((cx-wt/2*S,(2-0.2)*S-wt/2*S*0.6,cx+wt/2*S,(2+wt*0.6)*S),fill=255)
    d.ellipse((cx-wb/2*S,(2+h)*S-wb/2*S,cx+wb/2*S,(2+h)*S+wb/2*S),fill=255)
    a=np.asarray(big.resize((40,40),Image.LANCZOS)).astype(np.float32)/255
    ox=int(round(xl+3.2))-20; oy=top-2
    reg=img[oy:oy+40,ox:ox+40].astype(np.float32)
    img[oy:oy+40,ox:ox+40]=(reg*(1-a[...,None])+np.array(INK,np.float32)*a[...,None]).astype(np.uint8)
apostrophe(c,296,269)     # opening, line 1
apostrophe(c,408,415)     # closing, after "over" on line 3
ov=np.zeros((720,1280,4),np.uint8)
ov[...,:3]=cv2.cvtColor(c,cv2.COLOR_BGR2RGB)
ov[212:510,285:900,3]=255
Image.fromarray(ov,'RGBA').save('t_q3body.png')
cv2.imwrite('q3body_prev.png',c)
print('line4 ends at x',end4)
