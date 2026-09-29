# S3 hook fix (user 2026-09-29): NotebookLM voice spelled "B-I-G" because the script said "BIG".
# Replace the spelled letters with the SAME voice's own "big." from "Large means big." (68.74-69.24),
# keeping total length identical so every overlay/freeze stays in sync.
import wave, numpy as np, os
D='/workspace/glottos-marketing/content/specials/S3/polish-v2-build/'
w=wave.open(D+'audio_v2.wav'); SR=w.getframerate(); N=w.getnframes()
a=np.frombuffer(w.readframes(N),np.int16).astype(np.float32)/32768
s=lambda t:int(round(t*SR))
def rms(x): return np.sqrt((x**2).mean())
def fade(x,n):
    x=x.copy(); r=np.linspace(0,1,n,dtype=np.float32); x[:n]*=r; x[-n:]*=r[::-1]; return x
LEAD=0.30
head=fade(a[0:s(1.44)],s(0.005))
donor=a[s(68.74):s(69.24)]
# loudness: match voiced RMS of the removed letters
ref=a[s(1.50):s(2.62)]; ref=ref[np.abs(ref)>0.01]; dv=donor[np.abs(donor)>0.01]
g=rms(ref)/rms(dv); print('gain dB',20*np.log10(g))
donor=fade(donor*g,s(0.008))
new=np.concatenate([np.zeros(s(LEAD),np.float32),head,np.zeros(s(0.08),np.float32),donor])
tail_start=s(3.10)                      # still silence; "How" starts ~3.18
assert len(new)<tail_start, len(new)/SR
new=np.concatenate([new,np.zeros(tail_start-len(new),np.float32),a[tail_start:]])
assert len(new)==len(a)
print('big ends at',(s(LEAD)+len(head)+s(0.08)+len(donor))/SR,'pause to 3.18')
os.replace(D+'audio_v2.wav',D+'audio_v2.spelled-BIG.bak.wav') if not os.path.exists(D+'audio_v2.spelled-BIG.bak.wav') else None
pcm=(np.clip(new,-1,1)*32767).astype(np.int16)
o=wave.open(D+'audio_v3.wav','wb'); o.setnchannels(1); o.setsampwidth(2); o.setframerate(SR); o.writeframes(pcm.tobytes()); o.close()
