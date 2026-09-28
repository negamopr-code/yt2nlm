# M1 language gate v3: m1-v3.mp4 (re-gate of the 2 items from lang-gate-v2.md)

Gate: glottos-language-editor (headless autopilot step "special M1: polish", re-gate). Date: 2026-09-28 (UTC).
Input: content/specials/M1/m1-v3.mp4, changelog polish-v3.md, previous gate lang-gate-v2.md.
Method: full-resolution frames from m1-v3.mp4 (ffmpeg -ss ... -frames:v 1) at 110, 112, 115.2 (Quote 2), 166, 170, 176, 181.4 (Quote 3), 225 (chart), 250 (timeline), plus 2x zoomed crops of the Quote 3 body, the Quote 2 notebooks and the Quote 2 ribbon. Audio not re-checked (the changelog reports decoded PCM byte-identical to v2). No stamp via shorts/lang_gate.py (M1 has no unit JSON); the verdict is recorded here. Nothing was edited, uploaded or sent to NotebookLM.

## Verdict: APPROVED

| # | Item (time) | Result | Fix | Confidence |
|---|---|---|---|---|
| 1 | Quote 3 card, 165.75-181.46 | Body reads exactly `'Repeat the sentence I` / `made myself over and` / `over' was a game` / `changer for me.` Grammatical (the quoted imperative is now the subject, inside inner quotes), matches what the voice says apart from the omitted opener, which is acceptable for a card. "A learner wrote:" tag present. Spelling correct; no glyph glitches at 2x ("for me." built from copied letters is indistinguishable from the original font; spacing even). Highlights on sentence / game / changer intact. Same at 166, 170, 176, 181.4 (whole range covered). Straight apostrophes are slightly heavier than the stem, but only visible when zoomed and not a language issue. The pink decorative double mark before the single quote is card decoration, acceptable. | none | high |
| 2 | Quote 2 slide, 109.79-115.25 | Ribbon under the card is empty (outline intact, no letter remnants, no new strokes). Both "Cognizaant" labels gone; only "Ephemeral" (correct) and illegible sketch-scribble remain on the notebooks. No new legible garbage. Card text and tag unchanged. Checked at 110, 112, 115.2. | none | high |
| 3 | Chart ~225 / timeline ~250 | "e.g." art gone, no garbled remnants. Faint low-contrast background words "meaning / meaning", "Garden", "blossom", "perfume", "memory album", "Comprehension", "network of associations" remain; all are real, correctly spelled words, same status as accepted in lang-gate-v2.md. Foreground text (chart title, axes, Day 1/3/7 lines) unchanged and correct. | none (optional: fade the stacked "meaning meaning" too in a future pass) | high |

Everything approved in lang-gate-v2.md stays approved (audio byte-identical, no other on-screen text changed per polish-v3.md).

## Not checked
- Sampled frames only, not every frame (the changelog's boundary-frame diffs support that patched slides are static across their ranges).
- No human viewing/listening. Known v1 art items listed in lang-gate-v2.md "Not checked" remain as accepted there.
