# Viewer-critic: lab batch H70 "a scene with two voices" (2026-10-12)

Videos: `state/shorts/l9-scene-i-dont-know-v1/final.mp4` (9.2 s), `state/shorts/l9-scene-no-problem-v1/final.mp4` (9.8 s), `state/shorts/l9-scene-im-busy-v1/final.mp4` (10.2 s). All 1440x2560, 30 fps. Builder `shorts/build_scene.py`.

## Verdicts
| video | verdict | why |
|---|---|---|
| i-dont-know | PARTLY | Two phrases I can use tomorrow, each with a reason; the third (a 7-word idiom) is on screen 1.6 s with no meaning given. |
| no-problem | PARTLY | Nobody says "thank you", so I am never told these are replies to thanks; strip says DON'T SAY, the voice says "with customers, don't just say". |
| im-busy | PARTLY, and BLOCKED | Best picture of the three, but the blue badge covers the speaker's mouth and chin for both of her lines. |

## Pain
- Pain as given by the producer: learners keep using the same basic phrase and want natural alternatives they can really use, with when to use them.
- Verbatim learner quotes: NOT FOUND. I searched `content/insights/audience-needs.md`, `content/insights/pain-demand-2026-09-30.md` and `reports/monitor-awf/archives/youtube-comments-vol*.md`; there is no `content/problems/` folder and no PROBLEM document for this lane. No NotebookLM query was made. So the pain is the producer's wording, not checked against learner words; no quotes are invented here.
- "Solved" would mean: tomorrow, in the same situation, I say a different phrase and I know it fits the person I am talking to.

## (a) RENDER BLOCKERS
1. **im-busy, beats 2 and 3 (about 1.8-3.75 s and 4.6-6.65 s): the blue badge "#3: the one for friends" lies across the mum's mouth and chin** while she is the speaker. Checked at 1.8, 2.6, 3.6, 4.9, 5.6, 6.5 s: mouth hidden in every frame after the badge pops. Cause: B is zoomed 1.9 with face_y 0.58, which puts her mouth at the badge line (badge_y 1330). Owner: shorts-builder (unit `badge_y` or the B focus).
2. **i-dont-know, beats 2 and 3 (about 1.6-3.2 s and 3.9-5.6 s): the badge's left end lies on the boy's cheek and the logo tile covers his chin**; the badge also covers the teacher's raised fingertip. Smaller than 1 (he is the listener and half out of frame), but it is text on a face. Owner: shorts-builder (same `badge_y` move; the logo tile sits at the same height).

No blocker in no-problem: badge sits between the two faces over the cup (its right end just reaches the customer's chin line, not on the face).

Checked and clean in all three: 1440 short side; no spelled-out word (whisper small.en, word timings); no watermark in the rendered frames (the three source pictures carry a "Gemini Notebook" mark bottom right; it is cropped out in every frame sampled, bottom strip checked at 5 times per video); no magnifying glass; no written text in the pictures; the picture shows the right speaker for every line and each bubble pointer aims at the speaker; no box outside the frame ("It's no trouble." is about 36 px from the right edge, at the top, clear of the Shorts button column); badge spans 20-80% of the width at 69% height, clear of the right-hand buttons; all text readable at phone size.

## (b) Notes that do not block
- **Mascot is not the same boy.** Classroom: small skin-colour nose. Cafe and bedroom: big pink clown nose and rosy cheeks. Three videos in one batch, two different faces. Owner: visuals.
- **no-problem never says what it answers.** No "thank you" is heard or shown; "Not at all." alone is unclear to a B1 learner, and "No problem" also answers "sorry" and requests. Owner: scenario-writer.
- **no-problem, mixed message:** strip "DON'T SAY No problem" stays all video; the voice says "With customers, don't just say"; then "Or with friends: You bet!" in a customer scene. Owner: scenario-writer / language-editor.
- **Third phrase gets the least time.** i-dont-know: "Your guess is as good as mine!" on screen 6.5-8.1 s, the hardest line, no note. Same for "I've got a lot on my plate!" (7.6-9.1 s). First-pass readers will not finish it; the format relies on the loop.
- **"Let me think." is not another way to say "I don't know"**; it is a stall. The note "It buys you time." is honest, but the strip promises a replacement.
- **i-dont-know and no-problem, B's lines:** the boy's face is as big on screen as B's (hers half outside, accepted), so the woman's voice plays over a frame where the clearest face is the boy's. In no-problem his mouth is open in a grin; it can read as the boy speaking in a woman's voice. im-busy does this right (mum centred, alone).
- **No moment where I test myself** and no closing action; by design in this lane.
- Notes under phrase 1 are on screen about 1.25 s ("It sounds softer."): readable, three words.
- The static picture means the boy says the casual line with the same embarrassed/stressed face he had in beat 1.

## i-dont-know, second by second (frames at 0.03, 0.5, 1.0, 1.6, 2.7, 3.4, 4.0, 5.2, 5.7, 6.3, 7.3, 8.0, 8.3, 9.0)
- 0.00-0.92 boy, shrug, "I don't know." heard at 0.00. Only the strip and the bar. Stops me: it is my phrase, no intro.
- 0.92-3.24 cut to teacher. "Say, I'm not sure." 1.12; yellow box 1 already on. "It sounds softer." heard 2.06, note on at about 2.0. Badge pops about 1.6.
- 3.24-5.61 "Or, let me think." 3.26 (in fact 3.60 for the phrase); "It buys you time." 4.38.
- 5.61-8.14 cut to boy. "Or with friends" 5.66, red label; "Your guess is as good as mine" 6.56, box 3 on at about 6.5.
- 8.14-9.2 teacher, "So don't just say" 8.20, white bubble; loops into "I don't know."
- Swipe risk: none in 9 s; the risk is the opposite, the idiom passes before it is read.

Heard, other two (whisper): no-problem 0.00 "No problem." / 1.20 "Say, not at all, it's polite and formal." / 3.64 "Or it's no trouble, it's friendly but polite." / 6.38 "Or with friends, you bet." / 8.12 "With customers, don't just say." im-busy 0.00 "I'm busy." / 1.18 "Say I'm tied up right now." / 2.52 "It means not now." / 3.78 "Or I have my hands full." / 5.32 "It sounds less rude." / 6.70 "Or with friends." / 7.62 "I've got a lot on my plate." / 9.18 "So don't just say."

## Takeaway test
- i-dont-know: say "I'm not sure" instead of "I don't know". Clear.
- im-busy: say "I'm tied up right now". Clear.
- no-problem: say "Not at all" ... to what? Not clear without the thanks.

## Top 3 fixes
1. shorts-builder: move the badge (and logo tile) off the faces in im-busy and i-dont-know; re-check every B frame.
2. scenario-writer: no-problem needs the trigger ("Thank you!") seen or heard, and one message about "No problem" (wrong, or only too casual for customers).
3. visuals: one mascot face across the batch; and frame B fully in the cafe and classroom pictures in the next production so the speaker's face is the main face during her lines.

## Not checked
- Not listened to by ear (transcript only): voice quality, music and effect levels, how the loop join sounds in a player.
- No real Shorts interface overlay was laid on the frames; zones judged by position.
- Only i-dont-know was timed beat by beat against frames; the other two were checked on 10 frames each plus the transcript.
- Titles/descriptions in `content/youtube/l9-scene-*.json` not reviewed.
