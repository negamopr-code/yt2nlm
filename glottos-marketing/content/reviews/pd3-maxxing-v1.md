# Viewer-critic review: pd3-maxxing-v1 (lab H86 batch 2, old movie x Gen Z slang)
Reviewed 2026-10-22. `state/shorts/pd3-maxxing-v1/final.mp4`: 1440x2560, 30 fps, 12.80 s. Clip: The Electric House (1922). Segments [553.0,557.0] [557.5,560.0] [568.0,572.5] [574.0,577.0] (14.0 s of footage for T = 12.76; it is trimmed, with no freeze). Source shot changes: 567.83 | 573.04 | 580.71. subscribe_at [7.2] in final.subscribe.json, but NOT recorded: content/youtube/pd3-maxxing-v1.json does not exist.

## Verdict: SOLVES (for this format) - ship after the meta file is created. The picture shows a toy train bringing dinner while the voice says it, the cuts are clean, and the loop is seamless
## Pain (verbatim from the learner corpus, no NotebookLM query)
- "Defo... accent or slang words just make the things more difficult."
- "Is crashing out actually real? I get that it's used online but is it actually spoken?"
- "how do you build your on your vocab if not studying slang and idioms?"
Pain: "I see slang in comments and I don't get it." Solved means I see "sleepmaxxing" or "comfort-maxxing" and know "-maxxing" = making that one thing as good as possible.

## Heard (faster-whisper small.en)
0.00 He built a toy train that brings dinner to the table. / 3.72 Maxing means making one thing as good as it can be. / 6.82 A train that serves the food, that's comfort maxing. / 10.62 What are you maxing right now? (ends 12.1). Whisper spells it "maxing", which is the same sound, so the pronunciation is fine. No spelled-out words.

## Second by second
- 0.00-6.5 Frame 0: "POV: you automate your whole dinner" over the wide dining-room shot. The train comes down a chute from the wall and runs around an oval track on the table, carrying plates. It's small in the frame, but it moves and is readable on a phone. Good hook match. There is a 0.5 s skip at 4.0 (557.0 to 557.5, same shot). It's barely visible because the train just jumps forward a little. Acceptable.
- 6.5-11.0 Keaton close-up at the table, the track at his elbow, taking food and eating. "A train that serves the food? That's comfort-maxxing". Match.
- 11.0-12.8 Back to the wide shot under "What are you maxxing right now?".
- Every cut was checked frame by frame: no stray frames, no flash, no intertitle, no freeze.
- Card: "-maxxing / making one thing as good as it can be / Gen Z slang" fits one line. "comfort-maxxing / making life as comfortable as it can be / example". It's readable.
- Subscribe + bell: appears at about 7.25, red to about 8.7, then SUBSCRIBED + bell to about 12.2, under the "example" tag. It covers no text.
- Loop: wide goes to the same wide shot, with the audio ending at 12.1. It's seamless.

## HARD RULE
Clean. A family dinner, nothing about looks (no looksmaxxing), nothing sexual, no mockery. Safe for a 13-year-old. No POLICY hit.

## Takeaway test
I can read "sleepmaxxing" or "comfort-maxxing" and understand the pattern. I can make my own ("study-maxxing"). Yes, this is the most reusable word of the batch. No self-test beat (format-wide).

## Fixes
1. shorts-builder/publisher (blocker for "finished"): create content/youtube/pd3-maxxing-v1.json with "subscribe_at": [7.2].
2. visuals (optional nit): to remove the 4.0 skip, use [553.0,560.0] as one piece instead of the two segments, and re-time it so the close-up still starts on "A train that serves the food" (about 6.8).
3. none for scenario/voice.

---
# Pass 2 (2026-10-22, re-render 17:51)
Segments [553.0,560.0] [568.0,572.5] [574.0,577.0]. 1440x2560, 12.80 s. Meta content/youtube/pd3-maxxing-v1.json has subscribe_at [7.2], the same as final.subscribe.json.
## Verdict: SOLVES (for this format) - ship
- The wide shot now runs as one piece 0-7.0: the 4.0 skip is gone, and the train comes down the chute and around the table under beats 1-2.
- Cut 7.03 to the Keaton close-up, right on "A train that serves the food?" (speech from 6.82). Cut 11.53 back to the wide shot. Both are clean frame by frame, with no stray frames and no freeze.
- Subscribe appears at 7.2, under the "example" tag, and covers no text. Loop: wide shot to wide shot (same set-up), seamless.
- Transcript unchanged, no spelled-out word. No POLICY hit.
