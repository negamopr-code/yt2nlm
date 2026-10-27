# Two hand-drawn-style panels for the empty yellow cards: bulky (sofa-sized plant-food box, lamppost) and hefty (receipt rolling out of the door).
# PIL, 3x supersampled, dark ink outlines. Full-frame RGBA overlays; drawing sits in x100-900, y128-425 of the 1280x720 frame.
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
def new(): 
    im=Image.new('RGBA',(W*S,H*S),(0,0,0,0)); return im,ImageDraw.Draw(im)
def save(im,n): im.resize((W,H),Image.LANCZOS).save(n)
def star(d,cx,cy,r1,r2,n,fill):
    pts=[]
    for i in range(2*n):
        r=r1 if i%2==0 else r2; a=math.pi*i/n-math.pi/2
        pts.append((cx+r*math.cos(a),cy+r*math.sin(a)))
    poly(d,pts,fill)
def boot(d,x,y,flip=1):  # green welly, sole line at y
    poly(d,[(x-11*flip,y-24),(x+7*flip,y-24),(x+7*flip,y-10),(x+24*flip,y-6),(x+24*flip,y),(x-11*flip,y)],(60,140,80,255),w=3)
# ---------------- bulky ----------------
im,d=new(); ox,oy=0,0
gy=430   # ground line (frame coords)
d.line(P([(110,gy),(890,gy)]),fill=OUT,width=3*S)
# lamppost (right)
rr(d,(730,190,750,gy),3,(74,78,90,255)); rr(d,(716,gy-16,764,gy),3,(74,78,90,255))
poly(d,[(722,190),(758,190),(768,168),(712,168)],(74,78,90,255)); 
d.ellipse(P([(720,136),(760,166)])[0]+P([(720,136),(760,166)])[1],fill=(255,251,214,255),outline=OUT,width=3*S)
# the box: sofa-sized, odd shape (a lopped corner + a second smaller box strapped on top)
poly(d,[(150,190),(470,178),(560,214),(566,376),(150,384)],(205,152,92,255))
poly(d,[(470,178),(560,214),(566,376),(470,372)],(184,132,76,255))            # shaded side
poly(d,[(300,150),(410,144),(424,180),(300,188)],(214,166,108,255))          # smaller box on top
d.line(P([(150,262),(470,254)]),fill=(150,104,58,255),width=10*S)              # tape
d.line(P([(320,190),(326,388)]),fill=(150,104,58,255),width=10*S)
rr(d,(214,286,404,352),6,(250,248,240,255))
d.text((309*S,308*S),'PLANT FOOD',font=f(FB,24),fill=(40,90,50,255),anchor='mm')
d.text((309*S,336*S),'( extra large )',font=f(FB,15),fill=(90,90,90,255),anchor='mm')
# person behind the box: raincoat hem, legs, wellies, hands on the sides
poly(d,[(196,384),(500,376),(506,392),(190,398)],(226,140,20,255),w=3)
for lx in (250,430):
    d.rectangle(P([(lx-9,396),(lx+9,gy-22)])[0]+P([(lx-9,396),(lx+9,gy-22)])[1],fill=(52,72,116,255),outline=OUT,width=3*S)
    boot(d,lx,gy)
for hx in (138,578):
    rr(d,(hx-14,262,hx+14,312),12,(226,140,20,255)); d.ellipse(P([(hx-13,300),(hx+13,326)])[0]+P([(hx-13,300),(hx+13,326)])[1],fill=(240,200,160,255),outline=OUT,width=3*S)
# BONK: box corner meets lamppost
star(d,660,262,62,38,9,(255,255,255,255))
d.text((660*S,262*S),'BONK!',font=f(FB,25),fill=(200,40,30,255),anchor='mm')
for a in (-0.5,0,0.5):
    x0=600+40*math.sin(a); d.line(P([(586,300+a*70),(560,300+a*70)]),fill=OUT,width=3*S)
save(im,'bulky.png')
# ---------------- hefty ----------------
im,d=new()
gy=395
d.line(P([(110,gy),(890,gy)]),fill=OUT,width=3*S)
# open door on the right, daylight outside
rr(d,(760,150,880,gy),4,(196,228,246,255)); 
poly(d,[(760,150),(716,164),(716,gy),(760,gy)],(150,104,62,255))
d.line(P([(760,150),(880,150),(880,gy)]),fill=OUT,width=4*S)
# counter + till
rr(d,(114,300,330,gy),4,(150,104,62,255)); rr(d,(140,238,290,300),8,(84,94,110,255))
rr(d,(156,248,240,276),4,(200,235,210,255)); 
for i in range(3):
    for j in range(2): d.rectangle(P([(252+i*11,252+j*11),(260+i*11,260+j*11)])[0]+P([(252+i*11,252+j*11),(260+i*11,260+j*11)])[1],fill=(230,230,230,255))
# receipt ribbon: over the counter edge, down to the floor and out of the door
pts=[(300,268),(334,296),(352,346),(392,386),(470,392),(580,394),(700,392),(800,394),(872,396)]
def cr(pts,n=14):
    out=[]
    for i in range(len(pts)-1):
        p0=pts[max(i-1,0)];p1=pts[i];p2=pts[i+1];p3=pts[min(i+2,len(pts)-1)]
        for k in range(n):
            t=k/n
            out.append(tuple(0.5*((2*p1[c])+(-p0[c]+p2[c])*t+(2*p0[c]-5*p1[c]+4*p2[c]-p3[c])*t*t+(-p0[c]+3*p1[c]-3*p2[c]+p3[c])*t**3) for c in (0,1)))
    out.append(pts[-1]); return out
C=cr(pts)
quads=[]
for i in range(len(C)-1):
    (x0,y0),(x1,y1)=C[i],C[i+1]; dx,dy=x1-x0,y1-y0; L=math.hypot(dx,dy) or 1
    nx,ny=-dy/L,dx/L
    if x0>420: nx,ny=0,1     # lying flat on the floor
    w0=w1=(34 if x0<420 else 22)
    quads.append([(x0+nx*w0/2,y0+ny*w0/2),(x1+nx*w1/2,y1+ny*w1/2),(x1-nx*w1/2,y1-ny*w1/2),(x0-nx*w0/2,y0-ny*w0/2)])
for q in quads: d.polygon(P(q),fill=(252,252,250,255))
for q in quads:
    d.line(P([q[0],q[1]]),fill=OUT,width=2*S); d.line(P([q[2],q[3]]),fill=OUT,width=2*S)
for i in range(0,len(C)-1,3):
    x0,y0=C[i]
    if x0>420: d.line(P([(x0-6,y0-1),(x0+6,y0-1)]),fill=(150,150,150,255),width=2*S)
# the slip standing out of the till, with the total circled
poly(d,[(190,132),(352,132),(352,268),(190,268)],(252,252,250,255))
for k in range(4): d.line(P([(208,152+k*18),(208+80+(k%2)*30,152+k*18)]),fill=(150,150,150,255),width=3*S)
d.text((204*S,240*S),'TOTAL',font=f(FB,14),fill=(90,90,90,255),anchor='lm')
d.text((304*S,240*S),'1,240',font=f(FB,28),fill=(30,30,30,255),anchor='mm')
d.ellipse(P([(252,214),(356,266)])[0]+P([(252,214),(356,266)])[1],outline=(210,40,30,255),width=4*S)
rr(d,(140,258,290,300),8,(84,94,110,255))    # till front over the slip's foot
save(im,'hefty.png')
print('ok')
