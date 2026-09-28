# S2 v2 render: delogo + blue card + ladder (base + karaoke rows) + CTA text + logo tile, trim at END, three freeze-frame holds.
import subprocess, sys
from plan import *
F='/workspace/glottos-auto/node_modules/ffmpeg-static/ffmpeg'
S='/workspace/glottos-marketing/content/specials/S2/s2-v1.mp4'
OUT=sys.argv[1]
ovs=[('blue_card.png',BLUE[0],BLUE[1]),('ladder_base.png',LADDER[0],LADDER[1])]
for r,t0,t1 in HL:
    ovs.append((f'ladder_hl_{r:02d}.png',int(round(t0*FPS)),min(int(round(t1*FPS))-1,LADDER[1])))
ovs.append(('cta.png',CTA[0],CTA[1]))
inputs=['-i',S]
for f,_,_ in ovs: inputs+=['-i',f]
inputs+=['-i','logo.png','-i','audio_v2.wav']
g=['[0:v]delogo=x=1153:y=695:w=125:h=20[v0]']
cur='v0'
for i,(f,a,b) in enumerate(ovs,1):
    g.append(f"[{cur}][{i}:v]overlay=0:0:enable='between(n,{a},{b})'[v{i}]"); cur=f'v{i}'
L=len(ovs)+1
ch=f"[{cur}][{L}:v]overlay=0:0,trim=end_frame={END},setpts=N/{FPS}/TB"
added=0
for k,n,_ in FREEZES:
    ch+=f",loop=loop={n}:size=1:start={k+added}"; added+=n
nfr=END+added; dur=nfr/FPS
ch+=f",setpts=N/{FPS}/TB,fps={FPS},fade=t=out:st={dur-0.4:.3f}:d=0.4,format=yuv420p[vout]"
g.append(ch)
cmd=[F,'-hide_banner','-y','-threads','4','-filter_complex_threads','2']+inputs+['-filter_complex',';'.join(g),
     '-map','[vout]','-map',f'{L+1}:a','-r','24','-c:v','libx264','-preset','medium','-crf','18','-threads','4',
     '-c:a','aac','-b:a','128k','-ar','44100','-ac','1','-movflags','+faststart','-shortest',OUT]
print('expected frames',nfr,'dur',dur)
for f,a,b in ovs: print(f,a,b,round(new_time(a),2),round(new_time(b),2))
if '--dry' in sys.argv: print(';\n'.join(g)); sys.exit()
subprocess.run(cmd,check=True)
