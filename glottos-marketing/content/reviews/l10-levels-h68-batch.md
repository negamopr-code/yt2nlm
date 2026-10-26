# Viewer-critic review: lab H68 "LEVELS LADDER" batch (Happy, Good, Excited)

Reviewed 2026-10-12 (23:20-23:35 UTC). Files, all 1440x2560, 30 fps, voice kokoro am_fenrir 1.15x:
- state/shorts/l10-levels-happy-v1/final.mp4 (14.8 s), unit shorts/units/l10-levels-happy-v1.json, meta content/youtube/l10-levels-happy-v1.json
- state/shorts/l10-levels-good-v1/final.mp4 (13.8 s), unit shorts/units/l10-levels-good-v1.json, meta content/youtube/l10-levels-good-v1.json
- state/shorts/l10-levels-excited-v1/final.mp4 (15.5 s), the RE-RENDER (file of 23:29, state/shorts/h68/render-exc.log ends with EXC_DONE), unit shorts/units/l10-levels-excited-v1.json, meta content/youtube/l10-levels-excited-v1.json

## Verdicts
| Video | Verdict | Ship blockers |
|---|---|---|
| Happy | PARTLY | 3 |
| Good | PARTLY | 2 |
| Excited | PARTLY | 2 |

One sentence each:
- Happy: a clear ladder with three words I can use tomorrow and a strong idiom picture, but the example of Level 2 sits on the boy's open mouth, "We were" is heard as "You were", and the closing "So" is not heard as "So".
- Good: the ladder works, but two of the three "stronger words" are words I already know (great, excellent), the first example is heard as "Pizza is good" (no "The"), and the closing "So" is not heard as "So".
- Excited: the Level 4 fix is in and correct, the words are all heard correctly, but the Level 5 picture (the payoff) shows a boy lying flat among pillows, not bouncing off walls, and the closing "So" is not heard as "So".

None can be SOLVES even with the blockers fixed: I never try a word myself, each word has one example, and the meaning of the idiom is never said.

## Pain -> what the video gives -> gap
- Pain (from the task brief): "I always say happy / good / excited. Give me stronger, more natural words I can really use, with an example. I forget flat lists."
- Learner evidence: NO verbatim learner quote for this pain is on file. content/problems does not exist; content/insights/audience-needs.md has only format feedback ("very helpful thanks :)", "Useful information... I'll share it to my close ones") and viewers adding their own synonym under the Stop Saying Very X Shorts ("Frigid too", "Melancholic too", "There is also minuscule as in a minuscule mouse."); content/insights/pain-demand-2026-09-30.md has the theme as a number (332 pain comments) with no quotes; ../state/glottos-methods/pains.json searched, nothing verbatim. No NotebookLM query spent. The pain is taken from the brief, not proven here by quotes.
- Solved would mean: tomorrow I say "I'm delighted with..." or "I was ecstatic when..." in a real sentence, I know which one is stronger, and I know what "over the moon" means and when it is OK to say it.
- Gives: 4 new items per video in a clear order of strength, each heard twice (bare word, then in a sentence), each with a picture; the ladder is a memory hook a flat list does not have. The loop makes a second viewing likely, and a second viewing is where the words stay.
- Gap: (1) no moment where I produce anything; (2) the idiom is never explained, I must guess it from its place on the ladder; (3) register is not marked: "pumped" is slang, "exhilarated" is bookish, "over the moon" is mainly British, the video shows them as one line of "stronger"; (4) Good: Levels 2 and 3 are A1-A2 words, the real gain is "outstanding" plus the idiom.

## What is heard (faster-whisper small.en, word timings, final.mp4; cross-checked with base.en, with final-quiet.mp4 and with the single voice clips b0N-M.wav)
Happy: 0.00 Level one, happy. | 1.24 I'm happy today. | 2.46 Level two, delighted. | 3.62 I'm delighted with my gift. | 5.20 Level three, overjoyed. | 6.60 **You** were overjoyed at the news. | 8.34 Level four, ecstatic. | 9.66 I was ecstatic when we won. | 11.28 Level five, I'm over the moon. (ends 12.48) | 13.88 **Who** don't stop at? (ends 14.64)
Good: 0.00 Level one good, | 1.46 **[The missing]** pizza is good. | 2.44 Level two great, | 3.48 this song is great. | 4.74 Level three excellent, | 6.00 your work is excellent. | 7.32 Level four outstanding, | 8.70 the view is outstanding. | 10.10 Level five it's out of this world. (ends 11.52) | 12.76 **Who** don't stop at? (ends 13.62)
Excited: 0.00 Level one, excited. | 1.42 I'm excited about the trip. | 2.98 Level two, thrilled. | 4.06 I'm thrilled to be here. | 5.40 Level three, exhilarated. | 6.86 I felt exhilarated after the ride. | 8.82 Level four, pumped. | 10.00 I'm pumped for the game. | 11.36 Level five, I'm bouncing off the walls. (ends 13.06) | 14.32 **Who** don't stop at? (ends 15.26)

Answers to the voice questions:
- "Level 1:" etc. is read as "level one ... level five" in all 15 places. No word is spelled letter by letter anywhere.
- "ecstatic", "exhilarated" (both times), "pumped" (both times), "thrilled", "delighted", "outstanding": recognised by both models, in the mix and in the single clips.
- "overjoyed": recognised in the mix (0.95) and in the sentence (1.00), but the bare-word clip state/shorts/l10-levels-happy-v1/b03-0.wav alone is heard as "over Jyde" (small.en) and "over jide" (base.en). Not a blocker on this evidence; a human should listen once at 5.96 s.
- "So don't stop at": the clip b06-0.wav alone is heard correctly as "So don't stop at" by both models. In all three FINAL mixes it is heard as "Who don't stop at?", also when the last second is cut out and transcribed alone, and across the loop join ("who / You don't stop at level one happy"). See blocker A.
- NOT checked: I cannot listen. Two speech models agreeing is evidence of what is audible, not proof of how it sounds to a person. Stress and intonation are not checked at all.

## SHIP BLOCKERS

### A. All three videos: the closing "So" is not heard as "So" (Happy 13.88 s, Good 12.76 s, Excited 14.32 s)
What is wrong: the voice clip is clean, but in the mix the first word is recognised as "Who" (small.en, base.en, final.mp4 and final-quiet.mp4, all three videos) or "You" (base.en across the loop). shorts/build_first_frame.py line 195 fires a "whoosh" at exactly the start of the loop beat, on top of the /s/. "Who don't stop at Level 1" is wrong English at the one place built to carry the rewatch, and it is the last thing I hear.
Fix (shorts-builder): no whoosh on the loop beat, or start the whoosh 0.2 s before the beat, or start the voice 0.15 s into the beat. Then transcribe the final mix again; ship only when it prints "So don't stop at" in all three.

### B. Happy, 3.6-5.13 s (beat 2, Level 2 "Delighted"): the example box covers the boy's mouth
What is wrong: the black box "I'm delighted with my gift." lies across the lower half of his wide-open mouth (only the upper teeth show), his chin, his hand, and the robot's body, which is the gift. It is the same defect that was just fixed in Excited Level 4.
Fix (shorts-builder, unit shorts/units/l10-levels-happy-v1.json, beat 2): add a per-beat "sub_y" (it is the BOTTOM edge of the box in 1080x1920 units, as in Excited beat 4). There is no room above the face, so go down: about "sub_y": 1590 puts the top of the box near 1380, under the chin (my numbers are read off a frame, check the frame at 4.0 s). If that sits too low for the Shorts caption zone, lift the picture with "picture_shift" instead. The robot's head and chest must stay visible.

### C. Happy, 6.60 s (beat 3): "We were overjoyed" is heard as "You were overjoyed"
What is wrong: both models hear "You were" in the final mix AND in the single clip state/shorts/l10-levels-happy-v1/b03-1.wav, while the screen says "We were overjoyed at the news." "We were" is spoken in about 0.2 s at 1.15x.
Fix (voice): make that one clip again (same voice; a slower speed for this clip only is the simple way) until the clip alone is transcribed as "We were overjoyed at the news"; keep the beat length. If a person listens and clearly hears "We", this blocker can be closed without a new clip, but say who listened.

### D. Good, 1.2-1.46 s (beat 1): the word "The" is missing from "The pizza is good"
What is wrong: both models hear "Pizza is good" in the final mix and in the single clip state/shorts/l10-levels-good-v1/b01-1.wav. Measured: the first 140 ms of that clip are at 0-4 % of the clip's peak (about 30 dB under the voice), then "pi-" starts. For comparison, "The" in "The view is outstanding" (b04-1.wav) is at 5-6 % and is heard. The screen says "The pizza is good." Dropping the article is exactly the mistake many learners make; the video must not model it, and it is inside the first two seconds.
Fix (voice): make b01-1.wav again until "The" is recognised in the clip alone and its level is in the range of b04-1; keep the beat length.

### E. Excited, 11.29-14.49 s (beat 5, Level 5): the picture does not show "bouncing off the walls"
What is wrong: state/shorts/l10-levels-excited-v1/scene-5.png is a top-down view of the boy lying spread out on a pale surface between four pillows, with a few curved lines. There is no wall and nobody is in the air. It reads as "he fell on the bed" or "he is lying on the floor", close to the opposite of the idiom. The prompt in state/shorts/h68/scenes.json asked for "bounces through the air between the walls like a rubber ball ... zig-zag path from wall to wall"; the picture did not deliver it. This is the payoff frame, held 3.2 s, and the idiom is never explained in words, so the picture is the only explanation I get. Happy (jumping over a moon) and Good (astronaut, Earth behind) are literal and work; this one does not.
Fix (visuals): new scene-5: side view of a room, two walls and the floor clearly visible, the boy in mid-air, feet off the floor, a zig-zag line from wall to wall. Then shorts-builder renders again. Note the raw picture carries a "Gemini Notebook" mark bottom right; it is cropped out of the current video (checked), check again after the new picture.

## Checked and passed
- Resolution: 1440x2560 on all three (stream header).
- Ladder in the first second: yes. Frame 0.00-0.03 s already has the five-step staircase with step 1 yellow, the red "LEVEL 1" pill, the word in the yellow box and the blue badge "Level 5: the idiom natives use". I understand "five levels, the idiom comes last" without sound. Weak point: the grey numbers 2-5 on grey steps are low contrast, but the shape says "stairs".
- One more step lights with each level; all five are yellow on Level 5 and on the loop beat.
- Excited Level 4 fix: confirmed. "I'm pumped for the game!" now sits above the head (it touches the top of the hair), eyes and mouth are fully clear, 10.0-11.29 s.
- Nothing is cut by the frame edge. No box overlaps the logo tile (bottom left, present from 2.0 s); nearest approach is about 40 px (Happy and Good beat 1, Excited beat 1). No box overlaps another box.
- No garbled writing inside any picture, no magnifying glass, no NotebookLM/Gemini mark in the bottom-right corner of any beat (7 crops per video).
- Reading time: the example box comes up together with the spoken sentence and stays 0.9-1.7 s; with the voice saying the same words that is enough. The longest, "We were overjoyed at the news." (three lines), has about 1.6 s.
- Level 5 as payoff: Happy yes, Good yes (picture and sentence are the idiom, voice ends 1.3-1.4 s before the cut, so there is time to read it again). Excited no, see E.
- Title and description against the video: five levels, Level 5 is an idiom, bullets equal to the screen text word for word in all three. Nothing promised that is not delivered. "advanced english vocabulary" is still a tag on Happy and Excited; fair for ecstatic and exhilarated.
- Pictures against words, other beats: all fit (kite walk, robot gift, hug with confetti, trophy; pizza, headphones, drawing with gold star, sunset view; airport window with suitcase, funfair, ride car, stadium).

## Known and on purpose (not counted)
- No subscribe + bell animation and no "subscribe_at" in the meta: held equal to batch H63, question open with the user. By the standing rule (2026-10-05) these videos are "not finished" until the user decides.
- No closing question.
- "Level 1-5" is our own ladder, not CEFR; the description says so. On screen nothing says so; a learner who knows A1-C2 may still read "Level 5" as an official level.

## Second by second (Happy; the other two have the same rhythm)
- 0.0-1.2: stairs, "LEVEL 1 Happy", badge. It is my word and I see there are four more. I stay.
- 1.2-2.4: "I'm happy today." Fast but easy.
- 2.4-5.1: Delighted. New word, clear picture, then the box lands on his mouth (blocker B).
- 5.1-8.2: Overjoyed. Good picture. "We/You were" doubt (blocker C).
- 8.2-11.2: Ecstatic. Good. By now the pattern is known; the badge "Level 5: the idiom natives use" is what keeps me.
- 11.2-13.9: all steps yellow, "I'm over the moon!", boy over a moon. Payoff works. 1.4 s of music only after the voice: fine here, it lets me read.
- 13.9-14.8: picture 1 again, "So don't stop at…", into the replay. The idea is good; the first word is not clear (blocker A).
Swipe risk: low in 0-2 s; small at Level 3-4 where nothing new happens in the form; none at Level 5.

## Takeaway test
Happy: "Tomorrow, when I get good news, I say 'I'm delighted' or 'I'm over the moon' instead of 'I'm very happy'." Nameable.
Good: "I say 'The view is outstanding' and 'It's out of this world'." Nameable, but only two new items.
Excited: "I say 'I'm thrilled to be here' and 'I'm pumped for the game'." Nameable. I would not dare to use "bouncing off the walls": I do not know what it means from this picture.

## Retention risks
- Speech speed. The sentences run at about 300 words a minute in bursts ("We were overjoyed at the news" in 1.1 s, "I'm pumped for the game" in 0.8 s). For B1 that is at the limit; the text on screen saves it. This is also the likely cause of blockers C and D.
- No self-test and no pause where I can say the word.
- The idiom is only shown, never glossed. One line on the Level 5 card ("= extremely happy") would turn a guess into knowledge.

## Trust risks
- Excited: the order is not a real order of strength. "Exhilarated" (Level 3) is not weaker than "pumped" (Level 4); "pumped" is informal American, "exhilarated" is written style. "Bouncing off the walls" means too full of energy to keep still, often said about children; it is not simply "very excited about something". A viewer who knows English may comment on this.
- Happy: "over the moon" is mainly British informal; "the idiom natives use" is true but not for every native.
- Good: "great" and "excellent" as Levels 2-3 may feel thin against the title; the tag fix by the language editor ("stronger words for good") was right.

## Nice-to-have fixes (not blockers)
1. Excited beat 1 (1.45-2.89 s): the box "I'm excited about the trip." plus the logo tile hide almost the whole plane, and the box touches the chin. The suitcase still says "trip" and the plane is visible for the first 1.4 s, so not a blocker; a "sub_y" about 150 units lower would free the plane. (shorts-builder)
2. Good beat 2 (3.5-4.65 s): the right end of the box overlaps the left edge of the music player; Good beat 3: the box covers the top quarter of the drawing and touches the chin. Lower both a little. (shorts-builder)
3. Happy beat 1: the blue badge lies on the top of the boy's hair, and the word box covers most of the kite. Face is clear; cosmetic. (shorts-builder)
4. Add a short gloss on the Level 5 card ("= extremely happy / extremely good / too excited to sit still"). (scenario-writer, language-editor)
5. Good Level 5: nothing in the picture is being praised; a slice of pizza in the astronaut's glove would tie "It" back to Level 1. (visuals)
6. Step numbers 2-5: lighter digits on the grey steps. (shorts-builder)
7. Have a person listen once to "Overjoyed!" at 5.96 s in Happy. (voice)

## Top 3 fixes by impact
1. Loop "So" masked by the whoosh, all three videos: shorts-builder (blocker A).
2. The two swallowed first words, "We" (Happy 6.60 s) and "The" (Good 1.2 s): voice (blockers C, D). Add a standing check: transcribe every clip alone and compare word for word with the unit's speech before the build.
3. Excited Level 5 picture and Happy Level 2 box on the mouth: visuals and shorts-builder (blockers E, B).

## What was checked and what was not
- Checked: 18 frames per video (start, middle, end of each of the 6 beats) at 540 px wide, plus zooms at 720-900 px of Happy beat 2, Good beats 2-3, Excited beats 1, 4, 5, the first 1.6 s of Happy in six frames, the bottom-right corner of every beat; stream headers; word-timed transcripts with two models on the final mix, on final-quiet.mp4 (Happy, Good) and on single voice clips; level envelope of the clips in question; units and YouTube meta read in full.
- Not checked: listening by ear; the videos inside the real Shorts player on a phone (caption zone, right-hand buttons); every frame between my samples; final-quiet.mp4 of Excited; learner quotes (none on file); NotebookLM (not queried).
- Nothing was rendered, changed, deleted or uploaded. The only file written is this one.
