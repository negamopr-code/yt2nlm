import subprocess, sys
from plan import *
F='/workspace/glottos-auto/node_modules/ffmpeg-static/ffmpeg'
S='/workspace/glottos-marketing/content/specials/M1/m1-v1.mp4'
OUT=sys.argv[1]
ovs=[('ov_banner.png',4768,5327),('t_q1.png',378,575),('t_q2.png',2954,3178),('t_q3.png',4390,4767),
     ('p_chart.png',5634,6118),('l_chart.png',5634,6118),('p_timeline.png',6119,6710),
     ('p_livid.png',7469,7577),
     # v3 (language gate v2 fixes)
     ('t_q3body.png',4390,4767),('p_q3_eg.png',4390,4767),('p_q2.png',2954,3085),
     ('p_chart_eg.png',5634,6118),('p_timeline_eg.png',6119,6710),('p_exh.png',7674,7716),('p_tired_steps.png',7674,7751),('p_imp_steps.png',7818,7881)]
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
print(' '.join(cmd)[:3000])
subprocess.run(cmd,check=True)
