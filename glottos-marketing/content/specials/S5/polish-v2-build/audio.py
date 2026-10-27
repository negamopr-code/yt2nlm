# Build audio_v2.wav: the untouched s5-v1 audio (no splicing) with 3.0 s of true silence inserted at each
# freeze-frame hold, so the audio stays in sync with the two new video freezes. Same technique as S3/S4
# polish-v2-build/audio.py.
import numpy as np, subprocess, wave
from plan import *
F = '/workspace/glottos-auto/node_modules/ffmpeg-static/ffmpeg'
S = '/workspace/glottos-marketing/content/specials/S5/s5-v1.mp4'
SR = 44100
raw = subprocess.run([F, '-v', 'error', '-i', S, '-vn', '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
a = np.frombuffer(raw, np.float32).copy(); print('samples', len(a), len(a) / SR)
def s(t): return int(round(t * SR))
def fade(x, n):
    x = x.copy(); n = min(n, len(x) // 2)
    r = np.linspace(0, 1, n, dtype=np.float32); x[:n] *= r; x[-n:] *= r[::-1]; return x
pts = [0] + [f + 1 for f, _, _ in FREEZES] + [END]; out = []
for i in range(len(pts) - 1):
    out.append(fade(a[s(pts[i] / FPS):s(pts[i + 1] / FPS)], int(0.008 * SR)))
    if i < len(FREEZES): out.append(np.zeros(s(FREEZES[i][1] / FPS), np.float32))
y = np.concatenate(out)
n = int(0.35 * SR); y[-n:] *= np.linspace(1, 0, n, dtype=np.float32)
print('out dur', len(y) / SR)
pcm = (np.clip(y, -1, 1) * 32767).astype(np.int16)
with wave.open('audio_v2.wav', 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
