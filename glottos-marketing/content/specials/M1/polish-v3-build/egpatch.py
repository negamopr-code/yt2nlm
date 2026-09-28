# blank the faint background art text "e.g/ meaning & meaning" (x 84-192, y 406-448) on the chart, timeline and quote-3 slides
import cv2, numpy as np
from PIL import Image
def eg(frame,out,x0=84,x1=193,y0=405,y1=449):
    img=cv2.imread(frame); g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY).astype(int)
    paper=cv2.dilate(img,np.ones((11,11),np.uint8))           # max filter: removes thin strokes
    paper=cv2.GaussianBlur(paper,(0,0),3)
    pg=cv2.cvtColor(paper,cv2.COLOR_BGR2GRAY).astype(int)
    strong=(g<160).astype(np.uint8)                              # real content (slide text, axis, numbers)
    strong=cv2.dilate(strong,np.ones((5,5),np.uint8))
    reg=np.zeros(g.shape,np.uint8); reg[y0:y1,x0:x1]=1
    m=((pg-g)>3)&(reg>0)&(strong==0)
    m=cv2.dilate(m.astype(np.uint8),np.ones((3,3),np.uint8))&reg&(1-strong)
    bgm=(reg>0)&(m==0)&(strong==0)
    off=np.median((paper.astype(int)-img.astype(int))[bgm],axis=0)
    paper=np.clip(paper.astype(int)-off,0,255).astype(np.uint8)
    fin=img.copy(); fin[m>0]=paper[m>0]
    d=np.abs(fin.astype(int)-img.astype(int)).max(2)>0
    a=(d*255).astype(np.uint8)
    Image.fromarray(np.dstack([cv2.cvtColor(fin,cv2.COLOR_BGR2RGB),a]),'RGBA').save(out)
    cv2.imwrite(out.replace('.png','_z.png'),cv2.resize(np.vstack([img[395:455,70:210],fin[395:455,70:210]]),None,fx=4,fy=4,interpolation=cv2.INTER_CUBIC))
    return fin
eg('../s_5800.png','p_chart_eg.png')
eg('../s_6400.png','p_timeline_eg.png')
eg('../s_4500.png','p_q3_eg.png',x1=157)
