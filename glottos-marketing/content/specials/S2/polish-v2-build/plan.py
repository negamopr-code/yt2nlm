# single source of truth for the S2 v2 polish (source = s2-v1.mp4, 24 fps, 1280x720). Critic: critic-v1.md (PARTLY).
FPS=24
END=10675   # keep frames < END (444.79 s); CTA audio ends 444.30, Gemini end card starts 444.96
FREEZES=[(797,72,'pause 1: 3.0 s hold after "remember." (33.2 s, pause card; silence 33.20-34.23 -> ~4 s)'),
         (7863,60,'pause 2: 2.5 s hold after the tip (327.6 s; silence 327.51-330.14 -> ~5 s)'),
         (10394,72,'comment CTA: 3.0 s hold on the score card after "List versus story." (433.08 s)')]
BLUE=(1015,1384)     # "One story. 15 pictures." card over the early Blue card (42.29-57.7 s); the word Blue is voiced at 57.86
LADDER=(8332,10350)  # full 15-row ladder replaces NotebookLM's 8-row table (347.17-431.29 s)
CTA=(10360,10407)    # comment-CTA text on the score card (431.67-433.67 s) + the 3 s hold
# voice onsets (source s) from critic-v1 (whisper small.en): row 0=blue ... 14=inconsolable
ONS=[357.36,361.24,365.80,371.04,376.28,381.18,385.40,390.54,396.48,401.66,405.96,411.26,417.02,422.06,427.46]
LEAD=0.10
HL=[(i,ONS[i]-LEAD,(ONS[i+1] if i<14 else 431.29)-LEAD) for i in range(15)]
def added_before(k):
    return sum(n for f,n,_ in FREEZES if f<k)
def new_time(src_frame):
    return (src_frame+added_before(src_frame))/FPS
