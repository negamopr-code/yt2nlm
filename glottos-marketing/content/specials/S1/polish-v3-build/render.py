# v3 render: same overlay stack as v2 (delogo, ladder + karaoke rows, logo tile) plus the con-TENT cue,
# then the edit in two parts joined by an XF-frame video crossfade at the drill cut (plan.XF_CUT).
# Part A = src [0, XF_A) minus earlier cuts, with freeze 1; part B = src [XF_B, END) minus later cuts, with freeze 2.
# trim (not select) ends part A with a real EOF, so xfade never has to buffer part B.
import subprocess, sys
from plan import *
F='/workspace/glottos-auto/node_modules/ffmpeg-static/ffmpeg'
S='/workspace/glottos-marketing/content/specials/S1/s1-v1.mp4'
OUT=sys.argv[1]
ovs=[('ladder_base.png',LADDER[0],LADDER[1])]
for r,t0,t1 in HL:
    ovs.append((f'ladder_hl_{r:02d}.png',int(round(t0*FPS)),min(int(round(t1*FPS))-1,LADDER[1])))
ovs.append(('stress.png',STRESS[0],STRESS[1]))
inputs=['-i',S]
for f,_,_ in ovs: inputs+=['-i',f]
inputs+=['-i','logo.png','-i','audio_v3.wav']
g=['[0:v]delogo=x=1153:y=697:w=123:h=16[v0]']
cur='v0'
for i,(f,a,b) in enumerate(ovs,1):
    g.append(f"[{cur}][{i}:v]overlay=0:0:enable='between(n,{a},{b})'[v{i}]"); cur=f'v{i}'
L=len(ovs)+1
g.append(f"[{cur}][{L}:v]overlay=0:0,split=2[pa][pb]")
cutsA=[c for c in CUTS if c[1]<=XF_CUT[0]]; cutsB=[c for c in CUTS if c[0]>=XF_CUT[1]]
assert len(cutsA)+len(cutsB)+1==len(CUTS)
fr=[f for f,_ in FREEZES]
# part A
selA='+'.join(f'between(n,{a},{b-1})' for a,b,_ in cutsA)
chA=f"[pa]trim=end_frame={XF_A},select='not({selA})',setpts=N/{FPS}/TB"
nA=XF_A-sum(b-a for a,b,_ in cutsA); jA=0
for k in fr:
    if k<XF_CUT[0]:
        chA+=f",loop=loop={FREEZE_FRAMES}:size=1:start={k-removed_before(k)+FREEZE_FRAMES*jA}"; jA+=1; nA+=FREEZE_FRAMES
chA+=f",setpts=N/{FPS}/TB,fps={FPS}[A]"
# part B (select's n restarts at 0 after trim)
selB='+'.join(f'between(n,{a-XF_B},{b-1-XF_B})' for a,b,_ in cutsB)+f'+gte(n,{END-XF_B})'
chB=f"[pb]trim=start_frame={XF_B},select='not({selB})',setpts=N/{FPS}/TB"
nB=END-XF_B-sum(b-a for a,b,_ in cutsB); jB=0
for k in fr:
    if k>=XF_CUT[1]:
        idx=(k-XF_B)-sum(min(b,k)-a for a,b,_ in cutsB if a<k)+FREEZE_FRAMES*jB
        chB+=f",loop=loop={FREEZE_FRAMES}:size=1:start={idx}"; jB+=1; nB+=FREEZE_FRAMES
chB+=f",setpts=N/{FPS}/TB,fps={FPS}[B]"
g+= [chA, chB]
nfr=nA+nB-XF
dur=nfr/FPS
g.append(f"[A][B]xfade=transition=fade:duration={XF/FPS:.6f}:offset={(nA-XF)/FPS:.6f},setpts=N/{FPS}/TB,"
         f"fade=t=out:st={dur-0.4:.3f}:d=0.4,format=yuv420p[vout]")
cmd=[F,'-hide_banner','-y','-threads','4','-filter_complex_threads','2']+inputs+['-filter_complex',';'.join(g),
     '-map','[vout]','-map',f'{L+1}:a','-r','24','-c:v','libx264','-preset','medium','-crf','18','-threads','4',
     '-c:a','aac','-b:a','128k','-ar','44100','-ac','1','-movflags','+faststart','-shortest',OUT]
print('part A',nA,'part B',nB,'expected frames',nfr,'dur',dur,'xfade out-frames',nA-XF,'..',nA-1)
for f,a,b in ovs: print(f,a,b,round(new_time(a),2),round(new_time(b),2))
if '--dry' in sys.argv: print(';\n'.join(g)); sys.exit()
subprocess.run(cmd,check=True)
