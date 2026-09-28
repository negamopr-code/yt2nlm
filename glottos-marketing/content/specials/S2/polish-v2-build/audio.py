import numpy as np, subprocess, wave
from plan import *
F='/workspace/glottos-auto/node_modules/ffmpeg-static/ffmpeg'
S='/workspace/glottos-marketing/content/specials/S2/s2-v1.mp4'
SR=44100
raw=subprocess.run([F,'-v','error','-i',S,'-vn','-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True,check=True).stdout
a=np.frombuffer(raw,np.float32).copy(); print('samples',len(a),len(a)/SR)
def s(t): return int(round(t*SR))
def quiet(t,w=0.04):
    """time of the lowest 5 ms-window energy within +-w of t (a cut point inside a word gap)"""
    lo,hi=s(t-w),s(t+w); x=a[lo:hi]; n=s(0.005)
    e=np.array([np.sum(x[i:i+n]**2) for i in range(0,len(x)-n,s(0.001))]); return (lo+int(np.argmin(e))*s(0.001)+n//2)/SR
# --- slip fix: "someone or SOMEONE you love is gone" (419.9-421.24) -> "something" from 271.86-272.24, same narrator ---
# replace second 'someone' [420.34,420.56] with 'something' [271.86,272.24]; length grows, so remove the same amount
# from the silence after 'gone.' (421.24 -> 422.14) to keep every later timing identical.
d0,d1=quiet(420.34),quiet(420.56)
c0,c1=quiet(271.86),quiet(272.24)
print('slip: dst',d0,d1,'src',c0,c1)
X=s(0.010)
new=a[s(c0):s(c1)].copy()
def xf(left,right,n):
    r=np.linspace(0,1,n,dtype=np.float32); return np.concatenate([left[:-n],left[-n:]*(1-r)+right[:n]*r,right[n:]])
grow=len(new)-(s(d1)-s(d0))
z0=s(421.55)   # inside the silence after 'gone.'
seg=np.concatenate([a[:s(d0)],new,a[s(d1):z0],a[z0+grow:]])
assert len(seg)==len(a), (len(seg),len(a))
# short fades at the two joins
def fade_join(y,pos,n=X):
    r=np.linspace(0,1,n,dtype=np.float32); y[pos-n:pos]*=r[::-1]*0+np.linspace(1,0.0,n,dtype=np.float32)  # fade-out before the join
    y[pos:pos+n]*=np.linspace(0,1,n,dtype=np.float32)
fade_join(seg,s(d0)); fade_join(seg,s(d0)+len(new))
a=seg
print('silence trimmed at 421.55:',grow/SR,'s; check rms there',float(np.sqrt(np.mean(a[z0-2000:z0+2000]**2))))
# --- pause holds ---
def fade(x,n):
    x=x.copy(); n=min(n,len(x)//2)
    r=np.linspace(0,1,n,dtype=np.float32); x[:n]*=r; x[-n:]*=r[::-1]; return x
pts=[0]+[f+1 for f,_,_ in FREEZES]+[END]; out=[]
for i in range(len(pts)-1):
    out.append(fade(a[s(pts[i]/FPS):s(pts[i+1]/FPS)],int(0.008*SR)))
    if i<len(FREEZES): out.append(np.zeros(s(FREEZES[i][1]/FPS),np.float32))
y=np.concatenate(out)
n=int(0.35*SR); y[-n:]*=np.linspace(1,0,n,dtype=np.float32)
print('out dur',len(y)/SR)
pcm=(np.clip(y,-1,1)*32767).astype(np.int16)
with wave.open('audio_v2.wav','wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
