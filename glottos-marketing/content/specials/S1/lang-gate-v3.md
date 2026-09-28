# S1 language gate v3: s1-v3.mp4 (only the changes since v2)

Gate: glottos-language-editor (headless autopilot step "special S1: polish", re-gate). Date: 2026-09-28 (UTC).
Input: `content/specials/S1/s1-v3.mp4` (sha256 0787a7f3… per polish-v3.md), changelog `polish-v3.md`, previous gate `lang-gate-v2.md` (NEEDS FIX).
Scope: only the three v3 changes. Everything else was approved in lang-gate-v2 and is not re-read here.
Nothing was edited, uploaded, or sent to NotebookLM. No `lang_gate.py` stamp, because specials have no unit JSON (same convention as lang-gate-v2).

## Verdict: APPROVED

| # | Check | Evidence | Result |
|---|---|---|---|
| 1 | Drill cut / audio join | faster-whisper small.en on v3 48-60 s: "First up, content.[52.28-52.50] You're[53.60] lying down in a hammock tied between two sleepy cows." No "Say it with me", no second "content". 50 ms RMS: speech ends ~52.60, the gap 52.65-53.65 stays at −54 to −75 dB (room tone, with no click or word fragment), and "You're" starts cleanly at 53.70. The ~1.0 s pause reads as a natural beat. | PASS |
| 2 | Stress cue on the hammock scene | Frames 51.5 / 52.5 / 60 / 65.5 / 65.96 / 66.2. Exact string `con-TENT`: "con-" is white and "TENT" is yellow, on a dark rounded semi-transparent plate at x≈447-637, y≈465-513. The cue is absent at 51.5, visible at 52.5 (before the spoken word ends) through 65.5, and gone at 65.96, where the glad scene has already cut in. At 900 px zoom the text is crisp and high-contrast. There is about 20 px of clear space after the `content` caption, and the plate bottom (≈513) sits well above the "Quietly satisfied…" line (top ≈555). It does not touch the logo tile or the magnifier. The cow artwork behind the plate shows through slightly but does not reduce legibility. A hyphenated caps-stress notation is the standard learner convention. | PASS |
| 3 | Ladder Glad row | The frame at 380 s reads `Glad · happy about one thing, often relieved · everyday speech`. `diff ladder.py` v2→v3 changes only this string. Pixel diff of ladder_base + all 15 highlight PNGs v2→v3 finds one bbox (660,603)-(697,623), the tail of the word "relieved", and nothing else. The recap voice ("glad … when you're relieved about…") now matches the adjective in the cell. | PASS |

## Not checked
- No human listening. The join was judged by whisper plus the energy contour.
- The cue was checked on sampled frames only. It is a static overlay (`polish-v3-build/stress.png`), so the text does not change across the range.
- The ladder highlight timings (re-derived in polish-v3.md) are timing, not language, so this gate did not audit them. The critic owns that check.
- The optional v2 notes that were not applied (`British, informal` for Over the moon; `for a quiet, easy kind of happy` for Content) remain optional and do not block.
