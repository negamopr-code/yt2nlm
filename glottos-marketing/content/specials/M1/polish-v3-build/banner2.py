from PIL import Image, ImageDraw
import numpy as np, math
src=Image.open('g_210.png').convert('RGB')
box=(841,67,861,105); bg=(238,234,228)
S=4
big=Image.new('RGBA',(1280*S,720*S),(0,0,0,0))
d=ImageDraw.Draw(big)
# path for handwritten "2"
pts=[]
# upper arc: centre (851.5,78), radius ~6, from angle 200deg to 20deg (clockwise over top)
cx,cy,r=851.5,78.5,6.2
for a in np.linspace(math.radians(205),math.radians(370),20):
    pts.append((cx+r*math.cos(a), cy+r*math.sin(a)))
# down-left diagonal to bottom-left
x0,y0=pts[-1]
for t in np.linspace(0,1,12)[1:]:
    # slight curve
    x=x0+(845.5-x0)*t - 1.5*math.sin(math.pi*t); y=y0+(100.5-y0)*t
    pts.append((x,y))
# base
pts.append((850.5,100.2)); pts.append((859.5,99.2))
w=4.6
sp=[(x*S,y*S) for x,y in pts]
d.line(sp,fill=(28,28,28,255),width=int(w*S),joint='curve')
for p in (sp[0],sp[-1]):
    d.ellipse((p[0]-w*S/2,p[1]-w*S/2,p[0]+w*S/2,p[1]+w*S/2),fill=(28,28,28,255))
glyph=big.resize((1280,720),Image.LANCZOS)
ov=Image.new('RGBA',(1280,720),(0,0,0,0))
dd=ImageDraw.Draw(ov); dd.rectangle(box,fill=bg+(255,))
ov.alpha_composite(glyph)
ov.save('ov_banner.png')
out=src.convert('RGBA'); out.alpha_composite(ov)
out.crop((760,50,960,140)).resize((800,360),Image.LANCZOS).save('banner_prev.png')
out.convert('RGB').crop((680,20,1260,260)).save('banner_prev_wide.png')
