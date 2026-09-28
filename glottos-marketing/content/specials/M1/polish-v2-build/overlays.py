from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
W,H=1280,720
PINK=(250,152,248,255); INK=(32,33,36,255)
FR='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
FB='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
def tag(x,y,text,out,size=26):
    S=3
    f=ImageFont.truetype(FR,size*S)
    tw=f.getbbox(text); w=tw[2]-tw[0]; h=size*S
    padx,pady=16*S,9*S
    bw=w+2*padx; bh=h+2*pady
    big=Image.new('RGBA',(W*S,H*S),(0,0,0,0)); d=ImageDraw.Draw(big)
    X,Y=x*S,y*S
    d.rounded_rectangle((X+5*S,Y+5*S,X+bw+5*S,Y+bh+5*S),radius=12*S,fill=PINK)
    d.rounded_rectangle((X,Y,X+bw,Y+bh),radius=12*S,fill=(255,255,255,255),outline=INK,width=2*S)
    d.text((X+padx-tw[0],Y+pady-tw[1]+ (h-(tw[3]-tw[1]))//2),text,font=f,fill=INK)
    im=big.resize((W,H),Image.LANCZOS); im.save(out)
    print(out,'box',x,y,x+bw//S+5,y+bh//S+5)
# card top-left corners: Q1 (262,208) Q2 (275,132) Q3 (157,86); tag sits 8 px above the card
for (cx,cy),o in [((262,208),'t_q1.png'),((275,132),'t_q2.png'),((157,86),'t_q3.png')]:
    h=26+18+4
    tag(cx+6,cy-h-10,'A learner wrote:',o)
# chart label
def label(out):
    S=3; text='One week later: % of a text remembered'
    f=ImageFont.truetype(FB,24*S)
    big=Image.new('RGBA',(W*S,H*S),(0,0,0,0)); d=ImageDraw.Draw(big)
    bb=f.getbbox(text); x,y=140*S,62*S
    d.rounded_rectangle((x-12*S,y-8*S+bb[1],x+bb[2]+12*S,y+bb[3]+8*S),radius=10*S,fill=(255,255,255,235))
    d.text((x,y),text,font=f,fill=INK)
    big.resize((W,H),Image.LANCZOS).save(out)
label('l_chart.png')
# logo: rounded square with thin border
def logo(out,size=46,margin_r=10,margin_b=12):
    S=4; L=Image.open('/workspace/glottos-marketing/state/brand/awf-logo-channel.jpg').convert('RGBA').resize((size*S,size*S),Image.LANCZOS)
    m=Image.new('L',(size*S,size*S),0); ImageDraw.Draw(m).rounded_rectangle((0,0,size*S-1,size*S-1),radius=9*S,fill=255)
    L.putalpha(m)
    big=Image.new('RGBA',((size+2)*S,(size+2)*S),(0,0,0,0)); d=ImageDraw.Draw(big)
    d.rounded_rectangle((0,0,(size+2)*S-1,(size+2)*S-1),radius=10*S,fill=(150,150,150,255))
    big.alpha_composite(L,(S,S))
    sm=big.resize((size+2,size+2),Image.LANCZOS)
    im=Image.new('RGBA',(W,H),(0,0,0,0)); x=W-margin_r-(size+2); y=H-margin_b-(size+2)
    im.alpha_composite(sm,(x,y)); im.save(out); print('logo box',x,y,x+size+2,y+size+2)
logo('logo.png')
