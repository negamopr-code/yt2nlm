# Ep3 video pilot polish v1: single source of truth. Source = ../e3-v1.mp4 (24 fps 1280x720). Critic: content/reviews/words-that-stick-ep03-v1.md
import json
FPS = 24
def fr(t): return int(round(t * FPS))
SRC = '/workspace/glottos-marketing/content/episodes/E3/e3-v1.mp4'
F = '/workspace/glottos-auto/node_modules/ffmpeg-static/ffmpeg'
CUT1 = (fr(2.85), fr(4.30))          # "The secret?" (banned) cut out
QUIZ_SKIP = (fr(22.45), fr(23.40))   # 0.95 s silence dropped, replaced by a 2.0 s freeze of the question frame
FREEZE_AT, FREEZE_N = fr(22.40), 48
END = fr(78.60)                      # Gemini end card cut
SILENT = (43.90, 44.63)              # "Think of it like this" -> silence (card shown)
def T(f):                            # source frame -> output frame
    if f < CUT1[0]: return f
    if f < CUT1[1]: return CUT1[0]
    if f < QUIZ_SKIP[0]: return f - (CUT1[1] - CUT1[0])
    if f < QUIZ_SKIP[1]: return QUIZ_SKIP[0] - (CUT1[1] - CUT1[0])
    return f - (CUT1[1] - CUT1[0]) - (QUIZ_SKIP[1] - QUIZ_SKIP[0]) + FREEZE_N
def Ts(t): return T(fr(t)) / FPS     # source seconds -> output seconds
OUT_FRAMES = T(END)
