# Viewer-critic review: pd2-crooked-v1 (lab H85 batch 2, old-movie situation Short)

Reviewed 2026-10-17. File `state/shorts/pd2-crooked-v1/final.mp4`: 1440x2560, 30 fps, 10.10 s, AAC 48 kHz stereo, peak -1.4 dB, mean -18.2 dB. Unit `shorts/units/pd2-crooked-v1.json` (language hash f521e422f71d1be8). Clip: One Week (1920), source 542.05-553.6, one segment. `final.subscribe.json` subscribe_at [5.06].

## Verdict: SOLVES - no blocker (with a retention risk)
The crooked house is the whole picture from frame 0, and it really is lopsided, wonky and askew, so all three words are shown, not just said. The weak point is motion: it is one static wide shot, and for the first 6 s only a tiny figure moves.

## Pain (learner's words)
There is no PROBLEM doc for this lane. I reused the corpus evidence from the batch-1 reviews and spent no NotebookLM query:
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank."
- "great video but please shorten the intro!"
- "You have use the wrong synonym for rude"

Pain: "I say the same words all the time". Anything not straight is just "crooked".
Solved means: tomorrow I say "the picture on the wall is a bit askew" or "this table is wonky".
What it gives: three correct words, each with a meaning and a register tag, over a picture that is the meaning. Gap: there is no self-test, and the only example frame is "It's ...".

## What is heard (faster-whisper small.en, word timings)
0.00 You built your own house. / 1.70 It's not just crooked. (ends 2.58) / 3.60 It's lopsided. / 5.10 It's wonky. / 6.52 It's askew. / 7.80 Ever built something like this? (ends 9.34, then 0.76 s of silence to the loop). Every word is heard as written. No spelled-out words. The gap after "crooked" is 1.02 s, which is the longest pause in batch 2. Other gaps are 0.54-0.66 s.

## Second by second (one shot: no cuts in the picture area, and freezedetect finds no frozen stretch)
- 0.0 Frame 0: the yellow hook "POV: you built your own house" over the famous crooked house, which fills the picture band. The tilted window, the sloping porch roof and the leaning walls all read at phone size. The "my problem" stop works because of the house, not because of action: Buster is a figure about 60 px tall at the bottom left, walking. There is nothing else in motion.
- 0.0-3.5 Grey promise "3 better ways to say 'crooked'". RISK: 3.5 s with no visible event and a 1 s pause at 2.6-3.6. This is the most likely moment for a scroller to swipe.
- 3.5 "lopsided / higher or bigger on one side / everyday" (spoken 3.90). Picture: one side of the house is clearly higher. Match.
- 5.0-5.1 "wonky / crooked or a bit shaky / informal, UK" (spoken 5.40). Subscribe + bell slides in at bottom-left under the tag, clicks to SUBSCRIBED at about 6.5 and rings by about 8. It covers no text. Visible at the recorded 5.06 s (50%, second half).
- 6.3-6.5 "askew / not straight, at an angle / neutral" (spoken 6.72). The man lifts a ladder (about 6.0-7.5) and stands it against the house. This is the first real motion, and it is small.
- 7.6 The hook box swaps to "Ever built something like this?" (2 lines). Readable. The man is at the foot of the ladder.
- 10.1 End. No frozen tail. The man is still moving.

## Word-picture match
All three fit, and better than any other pd2 Short so far: the object on screen is literally the word. "Wonky" (a bit shaky) also fits a hand-built house.

## Loop
It ends with the ladder against the house and loops to the house with no ladder and the man walking in. There is a small jump in the ladder, but it reads as a replay. Audio: "...something like this? / You built your own house." No echo.

## Takeaway test
"The picture on the wall is a bit askew." / "This chair is wonky." I can use both tomorrow.

## Checklist
- 1440x2560: yes. Text sizes are the same as in batch 1 (headline about 130 px, meaning about 64 px, tag about 44 px, credit about 36 px). Readable.
- Subscribe + bell at 5.06 s: yes, visible, and it covers nothing.
- No intertitle (the shot runs 541.92-562.21 in the source, so the clip is inside one shot). No watermark. The credit shows "One Week (1920)" only.
- Meta: `content/youtube/pd2-crooked-v1.json` DOES NOT EXIST yet. The rule says the video is not finished until `"subscribe_at": [5.06]` is recorded in the meta (publisher / shorts-builder).

## Retention risks
- Frame-0 motion: almost none. This is the known risk, and it is real. The house carries the hook, but the eye has nothing to follow until the ladder at about 6 s.
- The 1.02 s pause at 2.58-3.60 over a still picture.
- The black band at the bottom (about 30%) is empty, same as batch 1.

## Trust risks
- "wonky / crooked or a bit shaky": the meaning uses "crooked", the word we are replacing. That is acceptable, because wonky does mean that.
- Tags: lopsided = everyday, wonky = informal UK, askew = neutral. All are defensible (as checked by the language-editor).
- "crooked" also means dishonest. The hook (a house) fixes the sense, so there is no risk.

## Top 3 fixes (none blocking)
1. Add motion at the start. EITHER (a) a slow push-in on the house (for example from the full band to about 115% over the first 3.5 s) (visuals / shorts-builder), OR (b) slide the window later in the same shot, to 547.5-557.6 (the same shot, ending before the 562.21 cut). Then the ladder goes up at about 1-2 s and he climbs toward the roof under the three words. Check the frames for the climb before you commit (visuals, then shorts-builder).
2. Tighten the pause after "crooked" from 1.0 s to about 0.6 s (voice / shorts-builder). The total length can shrink by 0.4 s.
3. Create `content/youtube/pd2-crooked-v1.json` with `"subscribe_at": [5.06]` (publisher / shorts-builder). Keep "public domain" out of every field, including `format`.

## Pass 2 (2026-10-17, window 547.0-557.6, 1.0 s pause kept)
**Verdict: SOLVES - no blocker.** Fix 1(b) works: the house now has a moving event from the start.
- File: 1440x2560, 30 fps, 10.10 s. It is one shot, with no cuts. freezedetect finds no frozen stretch, and the frame at 9.9 is live (he is climbing the ladder).
- 0.0-1.5: the man walks along the porch. By 2.0-2.5 he lifts the ladder diagonally across the frame, and by 3.5 it stands against the house. So the 1.0 s pause after "crooked" (2.58-3.60) now sits over the ladder going up, not over a still picture. Keeping the pause is acceptable.
- lopsided (3.88), wonky (5.40), askew (6.74): the crooked house stays fully in frame under all three. The climb at about 9.5 plays under "Ever built something like this?".
- Subscribe: fading in at 5.0, red SUBSCRIBE at 5.1, SUBSCRIBED by 6, bell by 8. It covers no text, and 5.06 s is in the second half. The meta `content/youtube/pd2-crooked-v1.json` has `subscribe_at [5.06]`. "public domain" appears only in the internal `language_approval` note.
- Audio is unchanged. Every word is heard as written, with no spelled-out words.
- Remaining risk (not blocking): the man is still small (about 60 px), and there is no self-test.
