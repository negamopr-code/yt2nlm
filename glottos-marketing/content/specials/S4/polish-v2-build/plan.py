# single source of truth for the S4 v2 polish (source = s4-v1.mp4, 24 fps, 1280x720). Critic: critic-v1.md (PARTLY).
FPS=24
def fr(t): return int(round(t*FPS))
END=fr(407.3)    # keep frames < END; CTA audio ends 407.04, Gemini end card starts 407.67
FREEZES=[(fr(30.10),72,'pause 1: +3.0 s hold after "remember." (30.10 s; inside existing 2.88 s silence -> 5.88 s total)'),
         (fr(298.15),72,'pause 2: +3.0 s hold after "in order." (298.15 s; was 0.78 s -> now 3.0 s)')]
CUTEPIC=(fr(38.33),fr(70.29)-1)     # whiteboard panel on the empty yellow "cute" card
ENDCARD=(fr(280.67),fr(294.46)-1)   # patch "The happy couple takes it home." -> gate wording
REVEAL=(fr(309.0),fr(317.67)-1)     # extras chips on the "fifteen, not ten" reveal card
LADDER=(fr(317.67),fr(392.67)-1)    # 15-row single-column ladder replaces NotebookLM's 8-row table
CTA=(fr(393.0),fr(397.2)-1)         # "Comment your two scores: list vs story" on "Which score was higher?"
# voice recap onsets (source s) from the autopilot ticket / critic-v1: row 0=cute ... 14=breathtaking
ONS=[320.86,325.28,330.92,335.52,340.28,344.86,348.96,353.54,358.24,363.48,368.68,373.90,377.98,383.68,387.02]
LEAD=0.10
HL=[(i,ONS[i]-LEAD,(ONS[i+1] if i<14 else 392.67)-LEAD) for i in range(15)]
def added_before(k): return sum(n for f,n,_ in FREEZES if f<k)
def new_time(src_frame): return (src_frame+added_before(src_frame))/FPS
