# single source of truth for the S1 v3 edit (v2 + drill cut 1494-1540 + con-TENT cue + Glad wording) (source = s1-v1.mp4, frame indices at 24 fps)
# boundaries from faster-whisper small.en/medium.en word timings + silencedetect -40 dB (see polish-v2.md)
FPS=24
CUTS=[(270,406,'filler: "First up is the playlist [plain list?]. I want you to just read and listen to this stark baseline test." (11.250-16.917)'),
      (984,1032,'filler: "Right, let\'s dive into the trick." (41.000-43.000)'),
      (1102,1212,'stage direction read aloud: "We\'re gonna build one continuous whiteboard drawing that grows from left to right." (45.917-50.500)'),
      (1494,1540,'wrong-stress drill (lang-gate-v2 NEEDS FIX): "Say it with me, CON-tent." (62.250-64.167; v2 new 53.00-54.92)'),
      (9992,10052,'dangling question: "So what does this all mean for your memory?" (416.333-418.833)')]
END=10236   # keep frames < END (426.500 s); CTA audio ends 425.89, Gemini end card starts 426.58
FREEZES=[(816,'pause 1, after "remember." (34.000 s, pause card)'),
         (7736,'pause 2, after "in order." (322.333 s, pause card)')]
FREEZE_FRAMES=72  # 3.0 s extra each
LADDER=(8474,9991)  # ladder table on screen from 353.083 s (scene change) to the cut at 416.333
# row highlight while the voice reads that word (source seconds; row index 0=Ecstatic ... 14=Content)
HL=[(14,359.40,362.30),(13,362.30,367.30),(12,367.30,371.70),(11,371.70,375.70),(10,375.70,378.40),
    (9,378.40,381.90),(8,381.90,385.50),(7,385.50,390.10),(6,390.10,393.50),(5,394.80,396.40),
    (3,396.40,400.20),(4,400.20,404.20),(2,404.20,407.70),(1,407.70,411.90),(0,411.90,416.34)]
def removed_before(k):
    return sum(min(b,k)-a for a,b,_ in CUTS if a<k)
def new_time(src_frame):
    """output time (s) of the start of source frame src_frame"""
    extra=sum(FREEZE_FRAMES for f,_ in FREEZES if f<src_frame)
    return (src_frame-removed_before(src_frame)+extra)/FPS
# v3: video crossfade at the drill cut instead of a hard cut (hammock slow zoom). XF frames of overlap,
# centred on the audio join: video part A ends at src XF_A (exclusive), part B starts at src XF_B.
XF=4
XF_CUT=(1494,1540)
XF_A=XF_CUT[0]+XF//2   # 1496
XF_B=XF_CUT[1]-XF//2   # 1538
# v3: stress cue con-TENT on the hammock scene, from just before "First up, content." (61.42) to the scene change (77.125 = frame 1851)
STRESS=(1470,1850)
