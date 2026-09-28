# v3: stress cue for the adjective "content" on the hammock scene (lang-gate-v2 recommendation).
# Exact on-screen string: con-TENT ("con-" white, "TENT" in the ladder's highlight yellow), on a semi-opaque dark plate
# to the right of NotebookLM's "content" caption (x128-425, y~462-515); stays above the line
# "Quietly satisfied. You do not want anything else." (y~553-587). Writes stress.png (1280x720 RGBA).
from PIL import Image, ImageDraw, ImageFont
W,H=1280,720; S=4
FB='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
A,B='con-','TENT'; assert A+B=='con-TENT'
f=ImageFont.truetype(FB,34*S)
im=Image.new('RGBA',(W*S,H*S),(0,0,0,0)); d=ImageDraw.Draw(im)
wa=d.textlength(A,font=f); wb=d.textlength(B,font=f)
x0,y0=446,464; padx,h=16,50
x1=x0+padx*2+(wa+wb)/S; y1=y0+h
assert y1<548 and x1<700, (x1,y1)
d.rounded_rectangle((x0*S,y0*S,x1*S,y1*S),radius=12*S,fill=(24,30,38,205))
cy=(y0+h/2)*S
d.text(((x0+padx)*S,cy),A,font=f,fill=(255,255,255,255),anchor='lm')
d.text(((x0+padx)*S+wa,cy),B,font=f,fill=(255,226,110,255),anchor='lm')
im.resize((W,H),Image.LANCZOS).save('stress.png'); print('plate',x0,y0,round(x1),y1)
