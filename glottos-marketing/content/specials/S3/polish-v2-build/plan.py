# single source of truth for the S3 v2 polish (source = s3-v1.mp4, 24 fps, 1280x720). Critic: critic-v1.md (PARTLY).
FPS=24
def fr(t): return int(round(t*FPS))
END=fr(433.0)   # keep frames < END; CTA audio ends 432.64, Gemini end card starts 433.29
FREEZES=[(fr(34.70),72,'pause 1: +3.0 s hold after "remember." (34.70 s; silence 34.72-37.12 -> 5.4 s)'),
         (fr(327.05),72,'pause 2: +3.0 s hold after "in order." (327.05 s; silence 327.02-328.40 -> 4.4 s)')]
BULKY=(fr(96.46),fr(116.30)-1)     # picture on the yellow bulky card
HEFTY=(fr(116.30),fr(132.63)-1)    # picture on the yellow hefty card
WHOP=(fr(212.10),fr(226.38)-1)     # word + meaning on the whopping card (truck scene)
TOWER=(fr(245.00),fr(265.38)-1)    # corrected towering caption
INORD=(fr(325.90),fr(339.54)-1)    # "In order." on pause card 2 (kept in the freeze)
EXTRAS=(fr(344.30),fr(351.17)-1)   # the 5 extras named on the reveal card
LADDER=(fr(351.17),fr(419.50)-1)   # 15-row ladder replaces NotebookLM's paired table
CTA1=(fr(420.90),fr(423.80)-1)     # "Comment your two scores"
CTA2=(fr(423.90),fr(428.20)-1)     # "Tonight: one silly story ..."
CTA3=(fr(428.30),END-1)            # "Look up: another word for big"
# voice onsets (source s) from critic-v1 (whisper small.en): row 0=large ... 14=ginormous
ONS=[359.50,363.14,368.30,371.36,376.30,381.54,385.34,389.30,392.78,396.14,400.36,404.64,407.86,411.98,416.14]
LEAD=0.10
HL=[(i,ONS[i]-LEAD,(ONS[i+1] if i<14 else 419.50)-LEAD) for i in range(15)]
def added_before(k): return sum(n for f,n,_ in FREEZES if f<k)
def new_time(src_frame): return (src_frame+added_before(src_frame))/FPS
