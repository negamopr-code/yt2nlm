# S5 v2 render: delogo + complication picture/house patch/bubble text/trouble caption/ladder overlays + logo
# tile, trim at END, two freeze-frame holds, audio_v2.wav (same content, silence added at the two holds).
# Same technique as S3/S4 polish-v2-build/render.py.
import subprocess, sys
from plan import *
F = '/workspace/glottos-auto/node_modules/ffmpeg-static/ffmpeg'
S = '/workspace/glottos-marketing/content/specials/S5/s5-v1.mp4'
OUT = sys.argv[1]
ovs = [('complication.png',) + COMPLICATION, ('house_patch.png',) + HOUSE, ('bubble.png',) + BUBBLE,
       ('trouble2.png',) + TROUBLE2, ('ladder_base.png',) + LADDER]
for r, t0, t1 in HL:
    ovs.append((f'ladder_hl_{r:02d}.png', fr(t0), min(fr(t1) - 1, LADDER[1])))
inputs = ['-i', S]
for f_, _, _ in ovs: inputs += ['-i', f_]
inputs += ['-i', 'logo.png', '-i', 'audio_v2.wav']
g = ['[0:v]delogo=x=1145:y=690:w=134:h=27[v0]']
cur = 'v0'
for i, (f_, a, b) in enumerate(ovs, 1):
    g.append(f"[{cur}][{i}:v]overlay=0:0:enable='between(n,{a},{b})'[v{i}]"); cur = f'v{i}'
L = len(ovs) + 1
ch = f"[{cur}][{L}:v]overlay=0:0,trim=end_frame={END},setpts=N/{FPS}/TB"
added = 0
for k, n, _ in FREEZES:
    ch += f",loop=loop={n}:size=1:start={k + added}"; added += n
nfr = END + added; dur = nfr / FPS
ch += f",setpts=N/{FPS}/TB,fps={FPS},fade=t=out:st={dur - 0.4:.3f}:d=0.4,format=yuv420p[vout]"
g.append(ch)
cmd = [F, '-hide_banner', '-y', '-threads', '4', '-filter_complex_threads', '2'] + inputs + ['-filter_complex', ';'.join(g),
       '-map', '[vout]', '-map', f'{L + 1}:a', '-r', '24', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-threads', '4',
       '-c:a', 'aac', '-b:a', '128k', '-ar', '44100', '-ac', '1', '-movflags', '+faststart', '-shortest', OUT]
print('expected frames', nfr, 'dur', dur)
for f_, a, b in ovs: print(f_, a, b, round(new_time(a), 2), round(new_time(b), 2))
if '--dry' in sys.argv: print(';\n'.join(g)); sys.exit()
subprocess.run(cmd, check=True)
