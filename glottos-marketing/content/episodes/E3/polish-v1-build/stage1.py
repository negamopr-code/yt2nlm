# stage 1: 16:9 cleanup on the source timeline: delogo, arm->check and tree-climber patches, cuts, quiz freeze, silent audio gap.
import numpy as np, subprocess, wave
from PIL import Image, ImageDraw
from plan import *
SR = 44100
frame = subprocess.run([F,'-v','error','-ss','40','-i',SRC,'-frames:v','1','-f','image2pipe','-vcodec','png','-'],capture_output=True,check=True).stdout
import io; im = Image.open(io.BytesIO(frame)).convert('RGB'); paper = im.getpixel((300,150)); print('paper', paper)
# arm patch (37.9-43.5): blank + green check; tree-climber patch (47.3-50.9): blank
def patch(box, draw=None):
    p = Image.new('RGBA',(1280,720),(0,0,0,0)); d = ImageDraw.Draw(p)
    d.rounded_rectangle(box, 18, fill=paper+(255,))
    if draw: draw(d)
    return p
def check(d):
    d.ellipse((60,100,170,210), fill=(46,160,90,255)); d.line([(85,155),(108,180),(148,128)], fill=(255,255,255,255), width=14, joint='curve')
patch((40,80,200,240), check).save('p_arm.png')
patch((1000,465,1280,720)).save('p_tree.png')
ovs = [('p_arm.png', 37.9, 43.5), ('p_tree.png', 47.3, 50.9)]
g = ['[0:v]delogo=x=1145:y=690:w=134:h=27[v0]']; cur = 'v0'
for i,(f_,a,b) in enumerate(ovs,1):
    g.append(f"[{cur}][{i}:v]overlay=0:0:enable='between(t,{a},{b})'[v{i}]"); cur = f'v{i}'
g.append(f"[{cur}]split=3[a][b][d]")
g.append(f"[a]trim=start_frame=0:end_frame={CUT1[0]},setpts=PTS-STARTPTS[s0]")
g.append(f"[b]trim=start_frame={CUT1[1]}:end_frame={QUIZ_SKIP[0]},setpts=PTS-STARTPTS[s1]")
g.append(f"[{1+len(ovs)}:v]scale=1280:720,setsar=1,fps={FPS},trim=end_frame={FREEZE_N},setpts=PTS-STARTPTS[s2]")
g.append(f"[d]trim=start_frame={QUIZ_SKIP[1]}:end_frame={END},setpts=PTS-STARTPTS[s3]")
g.append(f"[s0][s1][s2][s3]concat=n=4:v=1:a=0,fps={FPS},format=yuv420p[vout]")
cmd = [F,'-hide_banner','-y','-i',SRC] + sum([['-i',o[0]] for o in ovs],[]) + ['-loop','1','-framerate','24','-t','2.5','-i','freeze.png','-filter_complex',';'.join(g),'-map','[vout]','-c:v','libx264','-preset','medium','-crf','12','-an','s1_video.mp4']
subprocess.run(cmd, check=True)
# audio
raw = subprocess.run([F,'-v','error','-i',SRC,'-vn','-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True,check=True).stdout
a = np.frombuffer(raw,np.float32).copy()
def s(f): return int(round(f/FPS*SR))
def fade(x,n=int(0.008*SR)):
    x=x.copy(); n=min(n,len(x)//2); r=np.linspace(0,1,n,dtype=np.float32); x[:n]*=r; x[-n:]*=r[::-1]; return x
a0,a1=int(SILENT[0]*SR),int(SILENT[1]*SR); a[a0:a1]=0
parts=[a[s(0):s(CUT1[0])], a[s(CUT1[1]):s(QUIZ_SKIP[0])], np.zeros(int(FREEZE_N/FPS*SR),np.float32), a[s(QUIZ_SKIP[1]):s(END)]]
y=np.concatenate([fade(p) if len(p)>int(0.02*SR) else p for p in parts]); n=int(0.35*SR); y[-n:]*=np.linspace(1,0,n,dtype=np.float32)
print('audio', len(y)/SR, 'video frames expected', OUT_FRAMES, OUT_FRAMES/FPS)
with wave.open('s1_audio.wav','wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(y,-1,1)*32767).astype(np.int16).tobytes())
