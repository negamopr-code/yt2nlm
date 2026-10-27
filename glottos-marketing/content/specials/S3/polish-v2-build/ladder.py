# Full-frame 15-row BIG ladder (replaces NotebookLM's paired 2-column table, src 351.17-419.50). Text: content/specials/S3/script.md Beat 3 + Beat 5.
# Top = large (big) ... bottom = ginormous (extremely big), same order the voice reads. 5 extras marked with an orange dot.
from PIL import Image, ImageDraw, ImageFont
W,H=1280,720; S=2
FR='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
FB='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
FI='/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf'
PAPER=(248,247,243); GRID=(226,228,232); INK=(32,33,36); GREY=(110,112,118)
ACC=(22,92,200); CARD=(255,255,255); LINE=(222,224,228); HL=(255,226,110); RAIL=(150,120,90); EXTRA=(232,120,30)
ROWS=[ # word, meaning, when to use it, extra?
 ('Large','big','sizes and amounts: "a large coffee"',0),
 ('Considerable','large in amount','fairly formal: time, money, effort',0),
 ('Bulky','big and difficult to carry or move','"a bulky box"',1),
 ('Hefty','big and heavy','with money, a bit informal: "a hefty bill"',1),
 ('Jumbo','larger than usual','informal: products, "a jumbo pack"',0),
 ('Huge','extremely big','very common in speech',0),
 ('Giant','much bigger than others of its kind','only before a noun',0),
 ('Enormous','extremely big','a neutral word: fine anywhere',0),
 ('Massive','very big, heavy and solid','like a rock',0),
 ('Whopping','very big','informal: often before a number',1),
 ('Vast','extremely big','areas, spaces, amounts',0),
 ('Towering','very tall','a bit literary: "towering trees"',1),
 ('Mammoth','extremely big','"a mammoth task"',1),
 ('Immense','extremely big or great','also for feelings: "immense relief"',0),
 ('Ginormous','extremely big','informal and playful: with friends',0),
]
TITLE='The BIG ladder'; NOTE='The order is a guide, not a rule.'
HEAD=('word','meaning','when to use it')
FOOT='Read it from the top down: from big to extremely big.'
FOOT2='= one of the 5 sneaky extras'
X0,X1=112,1204
CW=(X0+38, 402, 800)
Y0=100; RH=38
def f(p,s): return ImageFont.truetype(p,s*S)
def draw(hl=None):
    im=Image.new('RGB',(W*S,H*S),PAPER); d=ImageDraw.Draw(im)
    for x in range(0,W,40): d.line((x*S,0,x*S,H*S),fill=GRID,width=S)
    for y in range(0,H,40): d.line((0,y*S,W*S,y*S),fill=GRID,width=S)
    ft=f(FB,34); d.text((X0*S,18*S),TITLE,font=ft,fill=INK)
    tw=d.textlength(TITLE,font=ft)
    fn=f(FI,20); d.text((X0*S+tw+18*S,32*S),NOTE,font=fn,fill=GREY)
    d.rounded_rectangle((X0*S,66*S,X1*S,(Y0+15*RH+6)*S),radius=14*S,fill=CARD,outline=LINE,width=2*S)
    fh=f(FB,18)
    for x,t in zip(CW,HEAD): d.text((x*S,74*S),t.upper(),font=fh,fill=GREY)
    fw,fm,fg=f(FB,23),f(FR,19),f(FR,18)
    for i,(w,m,g,ex) in enumerate(ROWS):
        y=Y0+i*RH
        if hl==i: d.rounded_rectangle(((X0+6)*S,(y+2)*S,(X1-6)*S,(y+RH-2)*S),radius=8*S,fill=HL)
        if i>0: d.line(((X0+14)*S,y*S,(X1-14)*S,y*S),fill=LINE,width=S)
        cy=(y+RH/2)*S
        if ex: d.ellipse(((X0+16)*S,cy-7*S,(X0+30)*S,cy+7*S),fill=EXTRA)
        d.text((CW[0]*S,cy),w,font=fw,fill=INK,anchor='lm')
        d.text((CW[1]*S,cy),m,font=fm,fill=INK,anchor='lm')
        d.text((CW[2]*S,cy),g,font=fg,fill=ACC,anchor='lm')
        assert CW[0]*S+d.textlength(w,font=fw)<(CW[1]-14)*S, w
        assert CW[1]*S+d.textlength(m,font=fm)<(CW[2]-14)*S, m
        assert CW[2]*S+d.textlength(g,font=fg)<(X1-14)*S, g
    lx,rx=46,82; top,bot=Y0+2,Y0+15*RH-2
    d.line((lx*S,top*S,lx*S,bot*S),fill=RAIL,width=4*S); d.line((rx*S,top*S,rx*S,bot*S),fill=RAIL,width=4*S)
    for i in range(15):
        y=Y0+i*RH+RH//2; d.line((lx*S,y*S,rx*S,y*S),fill=RAIL,width=3*S)
        if hl==i: d.ellipse(((lx+rx)//2*S-9*S,y*S-9*S,(lx+rx)//2*S+9*S,y*S+9*S),fill=HL,outline=RAIL,width=2*S)
    d.polygon([((lx+rx)//2*S,(bot+30)*S),((lx-8)*S,(bot+10)*S),((rx+8)*S,(bot+10)*S)],fill=RAIL)
    fs=f(FI,19); d.text((X0*S,697*S),FOOT,font=fs,fill=GREY,anchor='lm')
    fw2=d.textlength(FOOT,font=fs)
    ex0=X0*S+fw2+34*S
    d.ellipse((ex0,697*S-7*S,ex0+14*S,697*S+7*S),fill=EXTRA)
    d.text((ex0+22*S,697*S),FOOT2,font=fs,fill=GREY,anchor='lm')
    assert ex0+22*S+d.textlength(FOOT2,font=fs)<1200*S
    return im.resize((W,H),Image.LANCZOS)
draw().save('ladder_base.png')
for i in range(15): draw(i).save(f'ladder_hl_{i:02d}.png')
print('ok')
