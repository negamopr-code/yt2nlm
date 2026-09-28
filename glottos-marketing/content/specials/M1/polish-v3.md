# M1 polish v3: changelog (m1-v2.mp4 → m1-v3.mp4)

Step "special M1: polish" (headless autopilot), 2026-09-28, after language gate v2 (`lang-gate-v2.md`: NEEDS FIX, 2 on-screen items). Nothing uploaded, NotebookLM not touched, glottos-auto/out not touched.

Output `content/specials/M1/m1-v3.mp4`: 1280x720, 24 fps, H.264 CRF 18, AAC 44.1 kHz mono, **332.21 s**, 7973 frames (same as v2). sha256 `afc3d2e70b430446afd19c5fabc3f5943c4b99f5f4545ed2b2e7dc1cb7eb0acb`.
v1 and v2 are untouched (v2 sha256 still 617a1bbe…6584).

How: the v2 pipeline was re-run from m1-v1.mp4 (one ffmpeg render, -threads 4), with the same `plan.py` (cuts, freezes), the same `audio_v2.wav` (the file v2 was muxed from) and all v2 overlays, plus 5 new overlays. Build dir: `content/specials/M1/polish-v3-build/` (`render.py` lists the new overlays under "# v3"; new scripts `q3card.py`, `q2patch.py`, `egpatch.py` read single source frames `s_3000.png`, `s_4500.png`, `s_5800.png`, `s_6400.png` = m1-v1 frames 3000/4500/5800/6400, extracted with `select=eq(n\,N)`; the slides are static inside their ranges, checked by frame diff and phase correlation).

## Changes vs v2

| # | What | src frames | new time | How |
|---|---|---|---|---|
| 1 | Quote 3 card body re-lettered | 4390-4767 | 165.75-181.46 | Glyph reuse from the same card (original lettering, no substitute font): line 1 and "was a game" shifted right to make room for straight apostrophes (drawn, stem width of the card's "l"); "for me." built from the card's own f, o, r (from "myself"/"over"), m, e (from "made") and the original period. Yellow highlights on "sentence", "game", "changer" unchanged. "A learner wrote:" tag unchanged |
| 2a | Quote 2 slide: gibberish ribbon text removed | 2954-3085 | 109.79-115.25 | Text-only mask (dark small components inside a band along the lettering, long ribbon outline curves kept) + Telea inpaint; the letter tails peeking out under the card's pink shadow (x 540-812, rows 608-613) refilled with the ribbon colour. Ribbon is now empty, outline intact |
| 2b | Quote 2 slide: both "Cognizaant" labels blanked | 2954-3085 | 109.79-115.25 | Deskewed-rectangle masks (-24° and -38°) + inpaint. Chose blanking over repainting: at 1x the handwriting is ~15 px and not cleanly readable letter by letter ("zaat"/"saant"), so a repaint risked a new misspelling |
| 3 | (optional, done) faint "e.g/ meaning & meaning" background art blanked | chart 5634-6118, timeline 6119-6710, Q3 card background 4390-4767 (left of card) | 217.58-237.75, 237.79-262.29, 165.75-181.46 | Faint strokes only (slide text, axis, numbers excluded), replaced with the local paper tone |

## Exact on-screen strings (new or changed in v3)

1. Quote 3 card body: `'Repeat the sentence I made myself over and over' was a game changer for me.`
   Line breaks as on screen: `'Repeat the sentence I` / `made myself over and` / `over' was a game` / `changer for me.` (highlights: **sentence**, **game**, **changer**). Preceded by the pink decorative quote mark of the card and the tag `A learner wrote:`.
2. Quote 2 slide: the ribbon text `Töring toe the worab and ceadwe will be wed to welsh…` removed (empty ribbon); both `Cognizaant` labels removed (no replacement text). `Ephemeral` kept.
3. Chart, timeline and Q3 background: faint `e.g/ meaning & meaning` removed (no replacement text).

No other on-screen text changed. Audio unchanged.

## QA on m1-v3.mp4

- Duration 332.21 s, 7973 video frames (same as v2).
- Audio: decoded PCM of v2 and v3 is byte-identical (`cmp`, 29,300,736 bytes s16le mono 44.1 kHz).
- Full-res frames looked at: 110, 112, 114 (Quote 2: ribbon empty, both notebook labels blank, "Ephemeral" intact, card text and tag intact), 166, 170, 178 (Quote 3: new body as above, highlights in place, tag present). Boundary frames 109.80, 115.23, 165.76, 181.42 match the patched stills (mean abs diff 1.0-1.6, codec noise), so the fixes cover the whole slide time.
- Spot checks 11, 190, 225, 250, 300, 331 s: channel logo bottom-right on all, no "Gemini Notebook" watermark (corner crops at 11, 112, 170, 190, 225, 331), `STEP 2: LEARN WHEN TO USE IT` banner at 190, chart title at 225, clean Day 1/3/7 timeline at 250, quiz "very busy" slide at 300, CTA at 331. v2 vs v3 frame diff at 11, 190, 225, 250, 300, 331 is 0.00-0.06 (identical apart from the e.g. patch).

## Open / not done

- No re-gate yet: per `lang-gate-v2.md` the language editor should re-gate the frames at about 112 s and 170 s.
- The left notebook's grey underline under the blanked label is slightly broken/softened by the inpaint (visible only when zoomed). A thin band right of the card, just below its pink shadow (x 540-812, 6 px), is refilled with a flat ribbon tone and is a little smoother than its surroundings when zoomed.
- The apostrophes are drawn (not from the original font); they are slightly heavier than the text stem when zoomed 2x.
- Human viewing/listening not done. Remaining v1/v2 open items (see `polish-v2.md`) are unchanged.
