# Quote 2 slide (source frames 2954-3085, static): blank the gibberish ribbon text and both "Cognizaant" labels.
import cv2, numpy as np
from PIL import Image
img=cv2.imread('../s_3000.png'); g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
H,W=g.shape
med=cv2.medianBlur(g,21)
diff=med.astype(int)-g.astype(int)          # darker than surroundings
dark=(diff>12).astype(np.uint8)
# ---- ribbon text: polyline along the lettering, thick band
path=np.array([(172,612),(200,630),(222,652),(250,660),(300,668),(340,672),(380,666),(420,660),(450,652),
               (480,640),(510,628),(545,618),(590,612)],np.int32)
region=np.zeros((H,W),np.uint8)
cv2.polylines(region,[path],False,255,thickness=34)
cv2.rectangle(region,(596,605),(800,624),255,-1)      # letter tails right of the card's shadow
pink=((img[...,2]>200)&(img[...,1]<190)&(img[...,0]>200)).astype(np.uint8)
pink=cv2.dilate(pink,np.ones((5,5),np.uint8))
# long curves (ribbon outlines) must survive: drop big components
n,lab,st,_=cv2.connectedComponentsWithStats(dark*((region>0)|True).astype(np.uint8),8)
keep=np.zeros_like(dark)
for i in range(1,n):
    x,y,w,h,a=st[i]
    if w>110 or h>80: continue          # outline curves / big art
    keep[lab==i]=1
mR=(keep>0)&(region>0)&(pink==0)
# ---- labels: deskewed rectangles mapped back
def rotrect(cx,cy,ang,x0,x1,y0,y1,w=110,h=40):
    M=cv2.getRotationMatrix2D((cx,cy),ang,1.0); M[0,2]+=w/2-cx; M[1,2]+=h/2-cy
    Mi=cv2.invertAffineTransform(M)
    pts=np.array([[x0,y0],[x1,y0],[x1,y1],[x0,y1]],np.float32)
    return (pts@Mi[:,:2].T+Mi[:,2]).astype(np.int32)
lab_reg=np.zeros((H,W),np.uint8)
for r in [rotrect(128,360,-24,12,91,7,26.5), rotrect(128,360,-24,29,39,25,33),
          rotrect(232,320,-38,18,93,6,24), rotrect(232,320,-38,35,47,22,28)]:
    cv2.fillPoly(lab_reg,[r],255)
cv2.circle(lab_reg,(202,323),6,255,-1)
mL=(diff>8)&(lab_reg>0)
mask=(mR|mL).astype(np.uint8)*255
mask=cv2.dilate(mask,np.ones((3,3),np.uint8))
mask[(pink>0)]=0
inp=cv2.inpaint(img,mask,6,cv2.INPAINT_TELEA)
a=np.clip(cv2.GaussianBlur(cv2.dilate(mask,np.ones((3,3),np.uint8)).astype(np.float32),(0,0),1.2),0,255).astype(np.uint8)
a[pink>0]=0
Image.fromarray(np.dstack([cv2.cvtColor(inp,cv2.COLOR_BGR2RGB),a]),'RGBA').save('p_q2.png')
al=a[...,None]/255.0; prev=(inp*al+img*(1-al)).astype(np.uint8); cv2.imwrite('p_q2_prev.png',prev)
dbg=img.copy(); dbg[mask>0]=(0,0,255); dbg[(region>0)&(mask==0)]=(dbg[(region>0)&(mask==0)]*0.7+np.array([255,200,0])*0.3).astype(np.uint8)
cv2.imwrite('p_q2_dbg.png',dbg)
for nm,(x0,y0,x1,y1) in {'zq_rib':(100,580,900,700),'zq_lab':(60,280,290,400)}.items():
    cv2.imwrite(nm+'.png',cv2.resize(np.vstack([img[y0:y1,x0:x1],dbg[y0:y1,x0:x1],prev[y0:y1,x0:x1]]),None,fx=1.5,fy=1.5))
# ---- strip right of the card: letter tails peeking out below the pink shadow (rows 608-613, x 540-812)
fin=prev.copy()
L=lambda p: 0.299*p[...,2]+0.587*p[...,1]+0.114*p[...,0]
clean_cols=[660,700,820]
delta={y:np.mean([img[y,x].astype(float)-img[615,x].astype(float) for x in clean_cols],axis=0) for y in range(608,614)}
ref=prev[615].astype(float); okc=L(prev[615:616].astype(float))[0]>200
tmpl=np.zeros((W,3))
for x in range(W):
    lo,hi=max(0,x-40),min(W,x+41); cols=np.arange(lo,hi)[okc[lo:hi]]
    tmpl[x]=np.median(ref[cols],axis=0) if len(cols) else ref[x]
sm=np.zeros((H,W),np.uint8)
for x in range(540,813):
    for y in range(608,614):
        t=np.clip(img[614,x].astype(float)+delta[y],0,255)
        sm[y,x]=1
sm=cv2.dilate(sm,np.ones((3,3),np.uint8)); sm[:608]=0; sm[614:]=0
for x in range(540,813):
    for y in range(608,614):
        if sm[y,x]: fin[y,x]=np.clip(tmpl[x]+delta[y],0,255).astype(np.uint8)
d=np.abs(fin.astype(int)-img.astype(int)).max(2)>2
A=(cv2.dilate(d.astype(np.uint8),np.ones((3,3),np.uint8))*255)
Image.fromarray(np.dstack([cv2.cvtColor(fin,cv2.COLOR_BGR2RGB),A]),'RGBA').save('p_q2.png')
cv2.imwrite('p_q2_prev.png',fin)
cv2.imwrite('zq_strip.png',cv2.resize(np.vstack([img[595:630,500:880],fin[595:630,500:880]]),None,fx=3,fy=3))
cv2.imwrite('zq_rib.png',cv2.resize(np.vstack([img[580:700,100:900],fin[580:700,100:900]]),None,fx=1.5,fy=1.5))
