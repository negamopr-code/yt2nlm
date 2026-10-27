# single source of truth for the S5 v2 polish (source = s5-v1.mp4, 24 fps, 1280x720). Critic: critic-v1.md (PARTLY).
FPS = 24
def fr(t): return int(round(t * FPS))

END = fr(358.3)  # keep frames < END; CTA/site audio ends 358.02, Gemini end card starts 358.63

FREEZES = [
    (fr(31.9), 72, 'pause 1: +3.0 s hold at 31.9 s (inside silence 31.48-32.37, after "remember." before "Done?")'),
    (fr(265.0), 72, 'pause 2: +3.0 s hold at 265.0 s (inside silence 264.88-265.43, after "in order." before "Tip")'),
]

COMPLICATION = (fr(142.83), fr(153.88) - 1)   # blank blue card -> parrot-in-the-cream picture
HOUSE = (fr(237.38), fr(260.96) - 1)          # disaster/ending card -> cover the burning house (whole card+ending)
BUBBLE = (fr(252.4), fr(260.96) - 1)          # grandmother's empty speech bubble -> "Best birthday in ninety years!"
TROUBLE2 = (fr(187.78), fr(191.67) - 1)       # recommended: second caption line under "problems and worry."
LADDER = (fr(281.38), fr(343.79) - 1)         # 15-row single-column ladder replaces NotebookLM's 8-row table

# spoken recap onsets (source s, from critic-v1.md / the autopilot ticket): row 0=hiccup ... 14=disaster
ONS = [288.08, 291.32, 295.94, 298.82, 303.54, 307.24, 310.90, 313.22, 316.54, 319.76, 322.64, 327.52, 331.74, 335.20, 338.68]
LEAD = 0.20
HL = [(i, ONS[i] - LEAD, (ONS[i + 1] if i < 14 else 343.79) - LEAD) for i in range(15)]

def added_before(k): return sum(n for f, n, _ in FREEZES if f < k)
def new_time(src_frame): return (src_frame + added_before(src_frame)) / FPS
