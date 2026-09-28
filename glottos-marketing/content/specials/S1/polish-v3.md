# S1 polish v3: changelog (s1-v2 build + lang-gate-v2 fix → s1-v3.mp4)

Step "special S1: polish" (headless autopilot, polish round 1 continued as for M1 v3), 2026-09-28. The render ran at 06:44Z. The tick that started it died before QA. This tick (10:53Z) did the QA and promoted the file.
Output `content/specials/S1/s1-v3.mp4`: 1280x720, 24 fps, H.264 CRF 18, AAC mono, **415.83 s**, 9980 frames (= plan). sha256 `0787a7f36640e3e6da2cd08885731680aa8f2da73cdc91084a2f7325e69ca370`.
Build: `polish-v3-build/` (plan.py, audio.py, ladder.py, stress.py, render.py, render.log, qa/). Source is still s1-v1.mp4, with all v2 edits kept.

## Changes vs v2
1. **Drill cut** (lang-gate-v2 NEEDS FIX): src 62.250-64.167 (frames 1494-1540), "Say it with me, CON-tent." removed. It is at v3 new ~52.9 s, with a 4-frame video crossfade over the hammock zoom and 8 ms audio fades. Everything after it moves −1.92 s.
2. **Stress cue** `con-TENT` ("con-" white, "TENT" yellow) on a dark rounded plate to the right of the NotebookLM `content` caption, v3 new 52.0-65.9 s (hammock scene). It stays above the "Quietly satisfied…" line.
3. **Ladder, Glad row:** `happy about one thing, often relief` → `happy about one thing, often relieved` (lang-gate-v2 optional edit). The other rows are unchanged.
4. The ladder is now new 344.92-408.12, with highlight timings re-derived from plan.py (row starts: content 351.25, glad 354.12, … ecstatic 403.75).

## QA (this tick)
- whisper small.en across the join: "First up, content. | You're lying down in a hammock tied between two sleepy cows." (content 52.28, You're 53.62). No clipped word.
- Ladder voice vs highlight (word start / row lit): content 351.36/351.25, glad 354.40/354.12, pleased 359.24/359.12, chuffed 363.60/363.54, cheerful 367.50/367.54, upbeat 370.36/370.25, joyful 374.00/373.75, delighted 378.08/377.33 (lit on "Then we step up to"), thrilled 382.10/381.92, over the moon 386.76/386.62, cloud nine 388.36/388.25, overjoyed 392.04/392.04, elated 395.46/396.04, jubilant 399.62/399.54, ecstatic 405.02/403.75 (on "And right at the top").
- Contact sheet `polish-v3-build/qa/sheet.jpg` (0.5, both pause holds, 50.8-60 around the cue and the join, 66 glad, 345/350/380/405 ladder, 413.5 CTA, 415.6 fade). The logo tile is on every frame, with no Gemini watermark and no end card. The cue is legible and does not overlap anything.
- Not done: a human listen, and the critic on v3 (next step).

Still open (non-blocking, from v2): no art for cheerful/thrilled, low-contrast NotebookLM captions, "literally" ×6.
