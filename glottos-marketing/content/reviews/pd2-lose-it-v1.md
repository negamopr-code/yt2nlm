# Viewer-critic review: pd2-lose-it-v1 (lab H85, old-movie situation Short)

Reviewed 2026-10-17. `state/shorts/pd2-lose-it-v1/final.mp4`: 1440x2560, 30 fps, 11.60 s, AAC 48 kHz. Unit `shorts/units/pd2-lose-it-v1.json` (language hash df299cd04f57d630). Clip: Two Tars (1928), segments 872.7-874.0, 876.7-878.25, 881.5-888.3 (9.74 s of footage for T = 11.53 s). `final.subscribe.json` subscribe_at [5.85].

## Verdict: PARTLY - 3 blockers, do not ship
The words and the voice are right. But the picture does not show anger where it has to. Under "lose it" a man is grinning. From 6.6 s to the end, the screen shows a man whose whole face is covered in black goo, eyes closed, not moving. From 9.85 s that image is a frozen still, and it is also the loop frame.

## Pain (corpus quotes reused from the batch-1 evidence; no PROBLEM doc for this lane, no NotebookLM query spent)
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank."
- "great video but please shorten the intro!"
Pain: "I say the same words all the time", and it is always "angry".
Solved means: tomorrow I say "I lost it" or "he flew off the handle".
What it gives: 3 correct expressions with a short meaning and a register tag.
Gap: the picture never shows a person losing control while the word is said, and there is no self-test.

## Heard (faster-whisper small.en)
0.00 Someone just cut you off in traffic. / 2.42 You're not just angry. / 4.22 You lost it. / 5.74 You flew off the handle. / 7.48 You saw red. / 8.98 Ever lost it in traffic like this? (ends about 10.9). No spelled-out words, no intro, no dead air beyond the planned 0.6 s gaps.

## Final timeline vs source shots (source cuts 872.63 | 874.05 intertitle "Back up, you!" | 876.63 | 877.30 | 878.30 intertitle "Who's gonna make me?" | 881.46 | 882.26 | 884.88 | splat at about 885.1 | 888.38)
- 0.0-1.9 A man in a white hat and sunglasses stands by his car and shouts a little. Frame 0 = POV hook + this man. OK, but it is the calmest shot in the clip; it is not an impactful frame 0.
- 1.9-2.9 A fat man in a cap shouts at the camera from his car. This is the best "angry" image, and it is wasted at 1.9 s.
- 2.9-3.7 The fat man and a boy in the car.
- 3.7-6.3 The white-hat man crouches at a bucket, scoops mud, and GRINS (4.4-5.3). DEFECT: the "lose it / suddenly lose control and shout" card (4.33-5.68) sits over a smiling man. A learner reads "lose control" and sees someone enjoying himself.
- 5.7-6.3 The throw (blurred). It is under "fly off the handle". OK.
- 6.3-6.6 The fat man shouts, then is hit.
- 6.6-11.53 BLOCKER: the fat man's face is fully covered in black goo, eyes shut, motionless. It sits under "fly off the handle" (end), "see red" (7.45-8.6) and the closing question. It shows a victim, not anger, so "see red / get so angry you can't think straight" has no matching picture. POLICY (doubt = block): a white actor's face smeared completely black, held for 5 s and on the loop frame, reads as blackface at phone size (see the 240 px contact sheet). It is unsafe for comments and brand trust.
- 9.85-11.53 BLOCKER: FROZEN tail of 1.7 s (motion 0.0-0.6). The footage runs out at 9.74 s, and the builder holds the last frame.
- Intertitles: none seen. Every frame at the two segment boundaries (1.20-1.50, 2.75-3.05) was checked; the margins of 0.05 s before the 874.05 and 878.30 intertitles hold.

## Subscribe, cards, loop
- Subscribe + bell at 5.85 s, bottom left under the tag. It is red SUBSCRIBE at 6.0-7.0, SUBSCRIBED by 7.5, and the bell rings at about 9. It covers no text. 5.85/11.53 = 51%, so it is in the second half. OK.
- Cards: readable, and none are clipped ("fly off the handle" fits). The hook wraps with "traffic" alone on line 2 (minor). The closing hook "Ever lost it in traffic like this?" fits on one line.
- Loop: the frozen goo face jumps to the white-hat man. The seam is visible because of the freeze. The audio loops cleanly.
- `content/youtube/pd2-lose-it-v1.json` does not exist yet, so subscribe_at is not recorded (publisher / shorts-builder).

## Takeaway test
"I lost it when he cut me off." I can name it, so the verdict is PARTLY, not DOESN'T. No self-test moment.

## Fix (segments, unit `segments`; frames checked in the source)
The wheel-ripping rage shot 965.30-970.13 (a man tears a wheel off a car and hurls it) is the real "lose it / flew off the handle" picture in this film.
Proposed `segments`:
1. [877.35, 878.25] fat man shouting (frame 0 = an angry face + the POV hook)
2. [872.7, 874.0] white-hat man shouts back
3. [882.3, 884.4] mud scooping (under "You're not just angry"; it ends before the splat)
4. [965.35, 970.1] wheel ripped off and thrown (covers lose it, fly off the handle, start of see red)
5. [962.5, 963.6] the overturned car
6. [958.2, 959.7] the wrecked car (total about 11.7 s, at least T 11.53, so no freeze)
Visuals must re-check frames for each segment before the render (especially 958-960 and 962-964, which I saw only as single frames).

## Top 3 fixes
1. Replace segment 3 (881.5-888.3) so the goo-face shot (884.88-888.38) is gone entirely. This fixes the POLICY doubt, the "see red" mismatch and the loop frame. Owner: visuals (unit segments), then shorts-builder re-render.
2. Footage at least T: no frozen tail. Total segment length must be at least 11.6 s. Owner: visuals / shorts-builder (the builder should refuse to freeze more than 0.2 s).
3. Put an angry face at frame 0 and keep the grinning mud scooper out of the "lose it" card. Owner: visuals.
Then re-run subscribe_anim, record subscribe_at in content/youtube/pd2-lose-it-v1.json, and re-review.

---
# Pass 2 (2026-10-17, re-render 23:13)
Segments: [877.35,878.25] [872.7,874.0] [958.2,962.4] [963.7,965.25] [965.35,970.1], so 12.7 s of footage for T = 11.53. 1440x2560, 11.60 s.

## Verdict: SOLVES (for this format) - ship
All 3 pass-1 blockers are fixed. The goo-face shot and the grinning mud scooper are gone. No frame in the video is blackface-like (every frame was checked at 4 fps). There is no freeze: the lowest motion is above 1.5 everywhere, and the last frame shows two men still grappling. No intertitle appears. The transcript is identical to pass 1, and no word is spelled out.

## Picture under each card
- 0.0 Frame 0: the fat man shouts straight at the camera from his car, under the POV hook. This is a strong, on-topic stop frame.
- 0.9-2.2 The white-hat man shouts back.
- 2.2-3.2 A man runs at a car and it is shoved over onto its side. This is the most dramatic moment, and it lands under "You're not just angry". Good.
- 4.33-5.68 "lose it": the overturned wreck, with a man flung on top of it, arms flailing. It reads as chaos and destruction. Acceptable match. The man is small in the frame, but the wrecked car carries the meaning.
- 5.68-7.15 "fly off the handle": a man climbs on the wreck (5.7-6.4), then 6.4-7.95 the second wreck shot, where two men walk away from the car (6.8). That part is calm, a weak 0.7 s. It is not a blocker because the overturned car stays in frame.
- 7.45-8.6 "see red": from 7.95, two men square up and shove each other by the wreck (7.6 face-off, 8.3 punches). Match.
- 8.9-11.53 Closing "Ever lost it in traffic like this?": the fight goes on, and one man wrestles another. There is motion to the end.

## Subscribe, cards, loop, meta
- Subscribe + bell at 5.85 s: red SUBSCRIBE from about 6.0, SUBSCRIBED by about 7.5, the bell lit about 9-10, and it fades by about 10.5. It covers no text.
- Cards are all readable and none are clipped. The hook still wraps with "traffic" alone on line 2 (cosmetic).
- Loop: from the wrestling men to the shouting fat man, a hard cut with no freeze. The audio loops cleanly.
- `content/youtube/pd2-lose-it-v1.json` has `"subscribe_at": [5.85]`. The title, description and tags are clean and match the cards.

## Remaining nits (optional, none block)
1. 6.4-7.15: the calm walk-away under the end of "fly off the handle". Trimming [963.7,965.25] to start about 964.5, and extending [965.35,...] to 970.13 or adding 0.8 s elsewhere, would put the fight earlier. Owner: visuals.
2. There is still no self-test beat (applies to the whole format; owner: scenario-writer).
