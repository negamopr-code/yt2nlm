import subprocess, sys
from plan import *
F='/workspace/glottos-auto/node_modules/ffmpeg-static/ffmpeg'
S='/workspace/glottos-marketing/content/specials/S1/s1-v1.mp4'
OUT=sys.argv[1]
ovs=[('ladder_base.png',LADDER[0],LADDER[1])]
for r,t0,t1 in HL:
    ovs.append((f'ladder_hl_{r:02d}.png',int(round(t0*FPS)),min(int(round(t1*FPS))-1,LADDER[1])))
inputs=['-i',S]
for f,_,_ in ovs: inputs+=['-i',f]
inputs+=['-i','logo.png','-i','audio_v2.wav']
g=['[0:v]delogo=x=1153:y=697:w=123:h=16[v0]']
cur='v0'
for i,(f,a,b) in enumerate(ovs,1):
    g.append(f"[{cur}][{i}:v]overlay=0:0:enable='between(n,{a},{b})'[v{i}]"); cur=f'v{i}'
L=len(ovs)+1
g.append(f"[{cur}][{L}:v]overlay=0:0[vl]"); cur='vl'
sel='+'.join(f'between(n,{a},{b-1})' for a,b,_ in CUTS)+f'+gte(n,{END})'
chain=f"[{cur}]select='not({sel})',setpts=N/{FPS}/TB"
for j,(k,_) in enumerate(FREEZES):
    idx=k-removed_before(k)+FREEZE_FRAMES*j
    chain+=f",loop=loop={FREEZE_FRAMES}:size=1:start={idx}"
nfr=END-sum(b-a for a,b,_ in CUTS)+FREEZE_FRAMES*len(FREEZES)
dur=nfr/FPS
chain+=f",setpts=N/{FPS}/TB,fade=t=out:st={dur-0.4:.3f}:d=0.4,format=yuv420p[vout]"
g.append(chain)
cmd=[F,'-hide_banner','-y','-threads','4','-filter_complex_threads','2']+inputs+['-filter_complex',';'.join(g),
     '-map','[vout]','-map',f'{L+1}:a','-r','24','-c:v','libx264','-preset','medium','-crf','18','-threads','4',
     '-c:a','aac','-b:a','128k','-ar','44100','-ac','1','-movflags','+faststart','-shortest',OUT]
print('expected frames',nfr,'dur',dur)
for f,a,b in ovs: print(f,a,b,round(new_time(a),2),round(new_time(b),2))
subprocess.run(cmd,check=True)
