# Full-frame ladder overlay (replaces NotebookLM's wrong pair table, src 353.08-416.33).
# Text source of truth: content/specials/S1/script.md, Beat 5. Top = ecstatic, bottom = content.
# Writes ladder_base.png (no highlight) and ladder_hl_XX.png (row XX highlighted while the voice reads it).
from PIL import Image, ImageDraw, ImageFont
W,H=1280,720; S=2
FR='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
FB='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
FI='/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf'
PAPER=(248,247,243); GRID=(226,228,232); INK=(32,33,36); GREY=(110,112,118)
ACC=(22,92,200); CARD=(255,255,255); LINE=(222,224,228); HL=(255,226,110); RAIL=(150,120,90)
ROWS=[  # top to bottom
 ('Ecstatic','so happy you can hardly contain it','the top of the ladder'),
 ('Jubilant','very happy and celebrating a win','mostly written: news and books'),
 ('Elated','extremely happy after a success','more common in writing'),
 ('On cloud nine','extremely happy, as if floating','informal'),
 ('Overjoyed','extremely happy about news or an event','neutral'),
 ('Over the moon','extremely happy, usually about good news','informal'),
 ('Thrilled','very happy and excited','great in everyday speech'),
 ('Delighted','very pleased','polite and safe in emails'),
 ('Joyful','full of joy','songs, celebrations; more common in writing'),
 ('Upbeat','positive and hopeful','for moods, people and music'),
 ('Cheerful','happy in a way people can see','for people, voices, even rooms'),
 ('Chuffed','pleased, often with yourself','British, informal: with friends'),
 ('Pleased','satisfied with a result','neutral, fine at work'),
 ('Glad','happy about one thing, often relief','everyday speech'),
 ('Content','calm and satisfied','a quiet, easy kind of happy'),
]
TITLE='The HAPPY ladder'; NOTE='The order is a guide, not a law.'
HEAD=('word','meaning','when to use it')
FOOT='Read it from the bottom up: from a little bit happy to extremely happy.'
X0,X1=112,1204            # card
CW=(X0+22, 350, 792)      # column x: word, meaning, register
Y0=100; RH=38             # first row top, row height -> last row bottom = 670
def f(p,s): return ImageFont.truetype(p,s*S)
def draw(hl=None):
    im=Image.new('RGB',(W*S,H*S),PAPER); d=ImageDraw.Draw(im)
    for x in range(0,W,40): d.line((x*S,0,x*S,H*S),fill=GRID,width=S)
    for y in range(0,H,40): d.line((0,y*S,W*S,y*S),fill=GRID,width=S)
    # title
    ft=f(FB,34); d.text((X0*S,18*S),TITLE,font=ft,fill=INK)
    tw=d.textlength(TITLE,font=ft)
    fn=f(FI,20); d.text((X0*S+tw+18*S,32*S),NOTE,font=fn,fill=GREY)
    # card
    d.rounded_rectangle((X0*S,66*S,X1*S,(Y0+15*RH+6)*S),radius=14*S,fill=CARD,outline=LINE,width=2*S)
    fh=f(FB,18)
    for x,t in zip(CW,HEAD): d.text((x*S,74*S),t.upper(),font=fh,fill=GREY)
    fw,fm,fg=f(FB,24),f(FR,21),f(FR,19)
    for i,(w,m,g) in enumerate(ROWS):
        y=Y0+i*RH
        if hl==i: d.rounded_rectangle(((X0+6)*S,(y+2)*S,(X1-6)*S,(y+RH-2)*S),radius=8*S,fill=HL)
        if i>0: d.line(((X0+14)*S,y*S,(X1-14)*S,y*S),fill=LINE,width=S)
        cy=(y+RH/2)*S
        d.text((CW[0]*S,cy),w,font=fw,fill=INK,anchor='lm')
        d.text((CW[1]*S,cy),m,font=fm,fill=INK,anchor='lm')
        d.text((CW[2]*S,cy),g,font=fg,fill=ACC,anchor='lm')
        # width checks
        assert CW[0]*S+d.textlength(w,font=fw)<(CW[1]-14)*S, w
        assert CW[1]*S+d.textlength(m,font=fm)<(CW[2]-14)*S, m
        assert CW[2]*S+d.textlength(g,font=fg)<(X1-14)*S, g
    # ladder rail on the left: two rails, one rung per row, arrow up
    lx,rx=46,82; top,bot=Y0+2,Y0+15*RH-2
    d.line((lx*S,top*S,lx*S,bot*S),fill=RAIL,width=4*S); d.line((rx*S,top*S,rx*S,bot*S),fill=RAIL,width=4*S)
    for i in range(15):
        y=Y0+i*RH+RH//2; d.line((lx*S,y*S,rx*S,y*S),fill=RAIL,width=3*S)
        if hl==i: d.ellipse(((lx+rx)//2*S-9*S,y*S-9*S,(lx+rx)//2*S+9*S,y*S+9*S),fill=HL,outline=RAIL,width=2*S)
    d.polygon([((lx+rx)//2*S,(top-30)*S),((lx-8)*S,(top-10)*S),((rx+8)*S,(top-10)*S)],fill=RAIL)
    # reading direction, under the card
    fs=f(FI,19); d.text((X0*S,697*S),FOOT,font=fs,fill=GREY,anchor='lm')
    assert X0*S+d.textlength(FOOT,font=fs)<1200*S
    im2=im.resize((W,H),Image.LANCZOS)
    return im2
base=draw(); base.save('ladder_base.png')
for i in range(15): draw(i).save(f'ladder_hl_{i:02d}.png')
print('ok')
