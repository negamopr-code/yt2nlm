import cv2, numpy as np
from PIL import Image
def patch(frame, rects, out, thr=12, dil=3, rot=None, k=31, full=False):
    img=cv2.imread(frame)  # BGR
    g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    med=cv2.medianBlur(g,k)
    region=np.zeros(g.shape,np.uint8)
    for r in rects:
        if len(r)==4:
            x0,y0,x1,y1=r; region[y0:y1,x0:x1]=255
        else:  # rotated rect ((cx,cy),(w,h),angle)
            box=cv2.boxPoints(r).astype(np.int32); cv2.fillPoly(region,[box],255)
    if full:
        mask=region.copy()
    else:
        diff=np.abs(g.astype(int)-med.astype(int))
        mask=((diff>thr)&(region>0)).astype(np.uint8)*255
        mask=cv2.dilate(mask,np.ones((dil*2+1,dil*2+1),np.uint8))
        mask&=cv2.dilate(region,np.ones((7,7),np.uint8))
    inp=cv2.inpaint(img,mask,7,cv2.INPAINT_TELEA)
    a=cv2.GaussianBlur(cv2.dilate(mask,np.ones((5,5),np.uint8)).astype(np.float32),(0,0),2.0)
    a=np.clip(a,0,255).astype(np.uint8)
    rgba=np.dstack([cv2.cvtColor(inp,cv2.COLOR_BGR2RGB),a])
    Image.fromarray(rgba,'RGBA').save(out)
    prev=img.copy(); 
    al=a[...,None]/255.0; prev=(inp*al+img*(1-al)).astype(np.uint8)
    cv2.imwrite(out.replace('.png','_prev.png'),prev)
    return mask.sum()//255

print(patch('fr_07.png',[(836,484,932,536)],'p_livid.png',thr=25))
print(patch('fr_09.png',[((979,113),(150,26),-33.5),(540,645,740,682)],'p_exh.png',thr=10))
print(patch('fr_09.png',[(228,235,436,262),(544,235,718,262),(866,235,1034,262)],'p_tired_steps.png',thr=25))
print(patch('fr_11.png',[(982,200,1194,228),(960,451,1174,484),(946,594,1102,630)],'p_imp_steps.png',thr=25))
print(patch('fr_05.png',[(738,338,992,364),(900,566,1180,610)],'p_chart.png',thr=5,dil=4))
print(patch('fr_06.png',[(900,566,1180,610)],'p_timeline.png',thr=5,dil=4))

# refined exhausted: exclude dark outline pixels (hair/face lines) from mask
def patch_ex(frame,out):
    img=cv2.imread(frame); g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); med=cv2.medianBlur(g,31)
    region=np.zeros(g.shape,np.uint8)
    box=cv2.boxPoints(((979,113),(146,24),-33.5)).astype(np.int32); cv2.fillPoly(region,[box],255)
    region2=np.zeros_like(region); region2[645:682,540:740]=255
    diff=np.abs(g.astype(int)-med.astype(int))
    m1=((diff>10)&(region>0)).astype(np.uint8)*255
    m1=cv2.dilate(m1,np.ones((5,5),np.uint8))&region
    dark=cv2.dilate(((g<125)).astype(np.uint8)*255,np.ones((5,5),np.uint8))
    # exclude dark outlines only where they belong to big dark components (hair/face), not text
    m1[(dark>0)&(g<125)]=0
    m1[:, :922]=0  # stay off the left boy's cheek
    m2=((diff>10)&(region2>0)).astype(np.uint8)*255
    m2=cv2.dilate(m2,np.ones((7,7),np.uint8))&cv2.dilate(region2,np.ones((7,7),np.uint8))
    mask=m1|m2
    inp=cv2.inpaint(img,mask,7,cv2.INPAINT_TELEA)
    a=np.clip(cv2.GaussianBlur(cv2.dilate(mask,np.ones((3,3),np.uint8)).astype(np.float32),(0,0),1.5),0,255).astype(np.uint8)
    Image.fromarray(np.dstack([cv2.cvtColor(inp,cv2.COLOR_BGR2RGB),a]),'RGBA').save(out)
    al=a[...,None]/255.0; cv2.imwrite(out.replace('.png','_prev.png'),(inp*al+img*(1-al)).astype(np.uint8))
patch_ex('fr_09.png','p_exh.png')
