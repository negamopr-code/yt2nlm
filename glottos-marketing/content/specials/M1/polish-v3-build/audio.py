import numpy as np, subprocess, wave
from plan import *
F='/workspace/glottos-auto/node_modules/ffmpeg-static/ffmpeg'
S='/workspace/glottos-marketing/content/specials/M1/m1-v1.mp4'
SR=44100
raw=subprocess.run([F,'-v','error','-i',S,'-vn','-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True,check=True).stdout
a=np.frombuffer(raw,np.float32).copy(); print('samples',len(a),len(a)/SR)
def s(t): return int(round(t*SR))
def fade(x,n=int(0.01*SR)):
    x=x.copy(); n=min(n,len(x)//2)
    r=np.linspace(0,1,n,dtype=np.float32); x[:n]*=r; x[-n:]*=r[::-1]; return x
# 1) swap the mispronounced "very dizzy" for "very busy" from the challenge list
clip=fade(a[s(SWAP['src'][0]):s(SWAP['src'][1])],int(0.006*SR))
c0,c1=SWAP['dst_clear']
seg=a[s(c0):s(c1)]; n=int(0.01*SR)
a[s(c0):s(c1)]=0
a[s(c0)-n:s(c0)]*=np.linspace(1,0,n,dtype=np.float32)
a[s(c1):s(c1)+n]*=np.linspace(0,1,n,dtype=np.float32)
p=s(SWAP['dst_at']); a[p:p+len(clip)]+=clip
# 2) keep-segments (source frame ranges) with freezes inserted
bounds=[0]
keep=[]; cur=0
for x0,x1,_ in CUTS: keep.append((cur,x0)); cur=x1
keep.append((cur,END))
out=[]
for k0,k1 in keep:
    # split at freeze points
    pts=[k0]+[f+1 for f,_ in FREEZES if k0<=f<k1]+[k1]
    for i in range(len(pts)-1):
        x=a[s(pts[i]/FPS):s(pts[i+1]/FPS)]
        out.append(fade(x,int(0.008*SR)))
        if i<len(pts)-2: out.append(np.zeros(s(FREEZE_FRAMES/FPS),np.float32))
y=np.concatenate(out)
# 3) final fade-out after the CTA (last 0.35 s)
n=int(0.35*SR); y[-n:]*=np.linspace(1,0,n,dtype=np.float32)
print('out dur',len(y)/SR)
pcm=(np.clip(y,-1,1)*32767).astype(np.int16)
with wave.open('audio_v2.wav','wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
