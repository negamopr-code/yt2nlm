# Full-frame 15-row single-column ladder (replaces NotebookLM's 8-row two-column table, src 317.67-392.67).
# Text: content/specials/S4/script.md Beat 5, verbatim (language-gated recap wording). Top=cute ... bottom=breathtaking.
from PIL import Image, ImageDraw, ImageFont
W,H=1280,720; S=2
FR='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
FB='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
FI='/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf'
PAPER=(248,247,243); GRID=(226,228,232); INK=(32,33,36); GREY=(110,112,118)
ACC=(22,92,200); CARD=(255,255,255); LINE=(222,224,228); HL=(255,226,110); RAIL=(150,120,90); EXTRA=(232,120,30)
ROWS=[ # word, meaning, when to use it, extra?
 ('Cute','nice to look at','babies, small animals, small things',0),
 ('Pretty','attractive, but not as strong as beautiful','girls, women, small things',0),
 ('Picturesque','pretty, often in an old-fashioned way','places and views',1),
 ('Lovely','beautiful and very pleasant','very common in British English',0),
 ('Attractive','pleasant to look at','neutral: people and things',0),
 ('Good-looking','attractive','an everyday word for men and women',0),
 ('Handsome','good-looking','usually for men; also "a handsome horse."',0),
 ('Elegant','attractive and stylish','people, clothes, places',0),
 ('Graceful','moving in a smooth, beautiful way','dancers, swans, cats',1),
 ('Exquisite','very beautiful and delicate','small things made with great care',0),
 ('Striking','very attractive, often in an unusual way','you notice it at once',1),
 ('Radiant','glowing with happiness or health','faces and smiles',1),
 ('Gorgeous','very beautiful','a bit informal, very common when you speak',0),
 ('Stunning','extremely beautiful','people, clothes, views',0),
 ('Breathtaking','so beautiful that it takes your breath away','often for views',1),
]
TITLE='The ladder: nice to look at → extremely beautiful'; NOTE='The order is a guide, not a rule.'
HEAD=('word','meaning','when to use it')
FOOT='Read downward: nice to look at, then extremely beautiful.'
FOOT2='= one of the 5 sneaky extras'
X0,X1=90,1214
CW=(X0+30, 330, 700)
Y0=98; RH=38.2
def f(p,s): return ImageFont.truetype(p,s*S)
def draw(hl=None):
    im=Image.new('RGB',(W*S,H*S),PAPER); d=ImageDraw.Draw(im)
    for x in range(0,W,40): d.line((x*S,0,x*S,H*S),fill=GRID,width=S)
    for y in range(0,H,40): d.line((0,y*S,W*S,y*S),fill=GRID,width=S)
    ft=f(FB,27); d.text((X0*S,16*S),TITLE,font=ft,fill=INK)
    fn=f(FI,18); d.text((X0*S,44*S),NOTE,font=fn,fill=GREY)
    y1=Y0+15*RH+6
    d.rounded_rectangle((X0*S,66*S,X1*S,y1*S),radius=14*S,fill=CARD,outline=LINE,width=2*S)
    fh=f(FB,16)
    for x,t in zip(CW,HEAD): d.text((x*S,73*S),t.upper(),font=fh,fill=GREY)
    fw,fm,fg=f(FB,18),f(FR,15),f(FR,14)
    for i,(w,m,g,ex) in enumerate(ROWS):
        y=Y0+i*RH
        if hl==i: d.rounded_rectangle(((X0+6)*S,(y+2)*S,(X1-6)*S,(y+RH-2)*S),radius=8*S,fill=HL)
        if i>0: d.line(((X0+14)*S,y*S,(X1-14)*S,y*S),fill=LINE,width=S)
        cy=(y+RH/2)*S
        if ex: d.ellipse(((X0+14)*S,cy-6*S,(X0+26)*S,cy+6*S),fill=EXTRA)
        d.text((CW[0]*S,cy),w,font=fw,fill=INK,anchor='lm')
        d.text((CW[1]*S,cy),m,font=fm,fill=INK,anchor='lm')
        d.text((CW[2]*S,cy),g,font=fg,fill=ACC,anchor='lm')
        assert CW[0]*S+d.textlength(w,font=fw)<(CW[1]-10)*S, w
        assert CW[1]*S+d.textlength(m,font=fm)<(CW[2]-10)*S, m
        assert CW[2]*S+d.textlength(g,font=fg)<(X1-10)*S, g
    lx,rx=42,68; top,bot=Y0+2,Y0+15*RH-2
    d.line((lx*S,top*S,lx*S,bot*S),fill=RAIL,width=4*S); d.line((rx*S,top*S,rx*S,bot*S),fill=RAIL,width=4*S)
    for i in range(15):
        y=Y0+i*RH+RH/2; d.line((lx*S,y*S,rx*S,y*S),fill=RAIL,width=3*S)
        if hl==i: d.ellipse(((lx+rx)//2*S-8*S,y*S-8*S,(lx+rx)//2*S+8*S,y*S+8*S),fill=HL,outline=RAIL,width=2*S)
    d.polygon([((lx+rx)//2*S,(bot+26)*S),((lx-6)*S,(bot+9)*S),((rx+6)*S,(bot+9)*S)],fill=RAIL)
    fs=f(FI,17); d.text((X0*S,700*S),FOOT,font=fs,fill=GREY,anchor='lm')
    fw2=d.textlength(FOOT,font=fs)
    ex0=X0*S+fw2+28*S
    d.ellipse((ex0,700*S-6*S,ex0+12*S,700*S+6*S),fill=EXTRA)
    d.text((ex0+18*S,700*S),FOOT2,font=fs,fill=GREY,anchor='lm')
    assert ex0+18*S+d.textlength(FOOT2,font=fs)<1214*S
    return im.resize((W,H),Image.LANCZOS)
draw().save('ladder_base.png')
for i in range(15): draw(i).save(f'ladder_hl_{i:02d}.png')
print('ok')
