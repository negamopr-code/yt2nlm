# single source of truth for the edit (source frame indices at 24 fps)
FPS=24
CUTS=[(163,295,'filler: "This frustrating cycle ... reassure yourself right now."'),
      (456,576,'filler: "That exact quote perfectly captures ... traditional cramming."'),
      (2501,2568,'filler: "And this brilliantly illustrates why it works."'),
      (3086,3179,'filler: "That physical power of writing it down is incredibly effective."'),
      (6707,6826,'overclaim: "You can put it all together into a highly effective 15-minute daily routine."')]
END=8264   # keep frames < END (344.333 s); Gemini end card starts at frame 8270 (344.583 s)
FREEZES=[(7566,'angry'),(7637,'busy'),(7709,'tired'),(7783,'happy'),(7849,'important')]
FREEZE_FRAMES=48  # 2.0 s extra
SWAP=dict(dst_clear=(317.10,317.97), dst_at=317.14, src=(36.90,37.46))
def removed_before(k):
    return sum(min(b,k)-a for a,b,_ in CUTS if a<k)
def new_time(src_frame):
    """output time (s) of the start of source frame src_frame"""
    extra=sum(FREEZE_FRAMES for f,_ in FREEZES if f<src_frame)
    return (src_frame-removed_before(src_frame)+extra)/FPS
