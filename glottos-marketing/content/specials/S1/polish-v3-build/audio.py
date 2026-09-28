import numpy as np, subprocess, wave
from plan import *
F='/workspace/glottos-auto/node_modules/ffmpeg-static/ffmpeg'
S='/workspace/glottos-marketing/content/specials/S1/s1-v1.mp4'
SR=44100
raw=subprocess.run([F,'-v','error','-i',S,'-vn','-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True,check=True).stdout
a=np.frombuffer(raw,np.float32).copy(); print('samples',len(a),len(a)/SR)
def s(t): return int(round(t*SR))
def fade(x,n):
    x=x.copy(); n=min(n,len(x)//2)
    r=np.linspace(0,1,n,dtype=np.float32); x[:n]*=r; x[-n:]*=r[::-1]; return x
keep=[]; cur=0
for x0,x1,_ in CUTS: keep.append((cur,x0)); cur=x1
keep.append((cur,END))
out=[]
for k0,k1 in keep:
    pts=[k0]+[f+1 for f,_ in FREEZES if k0<=f<k1]+[k1]
    for i in range(len(pts)-1):
        out.append(fade(a[s(pts[i]/FPS):s(pts[i+1]/FPS)],int(0.008*SR)))   # 8 ms fades at every join
        if i<len(pts)-2: out.append(np.zeros(s(FREEZE_FRAMES/FPS),np.float32))
y=np.concatenate(out)
n=int(0.35*SR); y[-n:]*=np.linspace(1,0,n,dtype=np.float32)   # fade after the last word
print('out dur',len(y)/SR)
pcm=(np.clip(y,-1,1)*32767).astype(np.int16)
with wave.open('audio_v3.wav','wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
