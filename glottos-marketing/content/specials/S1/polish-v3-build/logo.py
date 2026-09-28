# channel logo tile (same as M1): 46 px rounded square, thin grey border, bottom-right x1222-1270 y660-708
from PIL import Image, ImageDraw
W,H=1280,720
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
