# Viewer-critic review: pd2-surprised-v1 (lab H85 batch 1, old-movie situation Short)

Reviewed 2026-10-17. File `state/shorts/pd2-surprised-v1/final.mp4`: 1440x2560, 30 fps, 10.60 s, AAC 48 kHz. Unit `shorts/units/pd2-surprised-v1.json` (language hash f5fca60932855e13). Clip: The Battle of the Century (1927), source 652.3-654.8 + 655-662. Meta `content/youtube/pd2-surprised-v1.json`, subscribe_at [5.6].

## Verdict: SOLVES - no blocker
A man gets a pie in the face in the first half-second, and then his stunned, pie-covered face sits under all three words. "Caught off guard / taken aback / blindsided" all fit what I just saw, and each card gives the meaning and register.

## Pain (learner's words)
There is no PROBLEM doc for this lane, so I used the same corpus evidence as the pd1 reviews and spent no NotebookLM query:
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank."
- "great video but please shorten the intro!"
- "You have use the wrong synonym for rude" (learners notice a wrong synonym and say so)

Pain: "I say the same words all the time". Every surprise comes out as "I was so surprised".
Solved means: tomorrow I say "the question caught me off guard" or "I was a bit taken aback".
What the video gives: three correct expressions in full sentences, each with a meaning and a tag, plus one memorable image. Gap: there is no self-test, and there are no example contexts beyond "You're ...".

## What is heard (faster-whisper small.en, word timings)
0.00 It came out of nowhere. / 1.64 You're not just surprised. / 3.54 You're caught off guard. / 5.16 You're taken aback. / 6.78 You've been blindsided. / 8.56 Ever had a day like this? (speech ends 9.86, then 0.64 s of silence to the loop). Every word is heard as written. No spelled-out words. Gaps between lines are 0.54-0.63 s, with no dead air. Peak -1.5 dB, mean -18 dB, clean.

## Second by second
- 0.0 Frame 0: yellow hook "POV: it came out of nowhere". The wide shot already shows the pie raised beside Hardy's face, and it lands by about 0.4 s. The hook and the motion are there at once. The figures are small in the wide shot, but the pie flash reads.
- 0.0-3.4 Grey promise "3 better ways to say 'surprised'" fills the lower area. About 30% of the screen at the bottom stays black for the whole video.
- 2.43 Cut to a close-up of the pie-covered face. This one shot then runs to the end (8.2 s).
- 3.41 "caught off guard" card appears as it is spoken (3.62). Picture: a stunned man. Match.
- 5.08 "taken aback" (spoken 5.30). Picture: the same stunned stillness. Match.
- 5.6 Subscribe + bell slides in under the tag at bottom-left (frame 5.7 checked). It clicks SUBSCRIBED and the bell rings by about 7.4. It covers no text.
- 6.68 "blindsided" (spoken 7.08). Picture: the man who was just hit by something he never expected. Match, though the hit itself was 6 s earlier.
- 8.49 The hook box swaps to "Ever had a day like this?".
- 9.5-10.6 The picture is FROZEN (motion index 0.3 vs about 1.0 for the live close-up). The clip runs out at 9.5 s and the last frame is held for 1.1 s.

## Word-picture match
All three words fit. The close-up holds for a long time with little motion (index about 1), which is fine for "taken aback" but gives the eye nothing new for 8 s.

## Loop
The end is the pie-faced close-up, and the loop goes back to the wide shot before the pie. That reads as a replay of the gag, which is good. Audio: "Ever had a day like this? / It came out of nowhere." No echo.

## Takeaway test
"Your question caught me off guard." I can use it tomorrow.

## Checklist
- 1440x2560: yes. Text at 1440: headline about 130 px, meaning about 64 px, tag about 44 px, credit about 36 px. All readable; the credit is small but only a credit.
- Subscribe + bell at 5.6 s (53%, second half), matching the meta: yes.
- No intertitle cards, no watermark: yes. Credit = "The Battle of the Century (1927)" only: yes.
- "public domain": not on screen and not in the title, description or tags. It does appear in the internal `format` field of the meta ("silent public-domain 1920s comedy clip"). The uploaders don't read that field, but the rule says "anywhere".
- Facts/tags: everyday / neutral / informal are defensible. "Taken aback" leans slightly formal or written; "neutral" is acceptable.

## Retention risks
The 1.1 s freeze before the loop. The single 8 s close-up. The empty black bottom band. The small figures in the 0-2.4 s wide shot.

## Trust risks
None of substance.

## Top 3 fixes (none blocking)
1. Remove the 1.1 s end freeze: extend the second segment to about 663.1 so the clip covers the full 10.6 s (shorts-builder).
2. Delete "public-domain" from the meta `format` string (shorts-builder / publisher).
3. Optionally punch in on the wide shot (crop around Hardy) so the pie hit is bigger at frame 0 (visuals / shorts-builder).

## Pass 2 (2026-10-17, after re-cut)
Re-checked file `state/shorts/pd2-surprised-v1/final.mp4`, built at 17:23. It is 1440x2560, 30 fps, 10.60 s, AAC 48 kHz stereo, peak -1.5 dB and mean -18.0 dB. Segments are 652.3-654.7 + 654.8-662.8.

### Verdict: SOLVES - no blocker
- Frozen tail: gone. Frame-to-frame difference on the picture area stays at 0.5-3 right to the last frame (in pass 1 it was 0.3 for 1.1 s). freezedetect finds only the stunned stillness at 2.77-4.07, which is the actor standing still, not a held frame. There is one small jump inside the shot at 9.53 (his head moves up between two frames). That is in the 1927 print, it does not read as a cut, and it is not a defect of ours.
- Frame 0: the wide shot at the pie shop with the hook "POV: it came out of nowhere". It is unchanged and correct. The cut at 2.43 is clean (frames 69-76 checked, with no flash frame).
- Picture vs word: unchanged and matching. The stunned pie-covered close-up is under caught off guard (3.62), taken aback (5.30) and blindsided (7.08).
- Audio (faster-whisper small.en): "It came out of nowhere. / You're not just surprised. / You're caught off guard. / You're taken aback. / You've been blindsided. / Ever had a day like this?" Every word is heard as written. No spelled-out words.
- Subscribe + bell: slides in at 5.6 s and reads SUBSCRIBED with the bell rung by about 7.3. It covers no text. This matches `subscribe_at` [5.6] in the meta and `final.subscribe.json`.
- No intertitle and no watermark. The credit shows the film name only.
- Loop: the last frame is the pie-faced close-up, and it jumps back to the wide shot before the hit, so it reads as a replay.
- Meta `content/youtube/pd2-surprised-v1.json`: "public-domain" is gone from `format` ("silent 1920s comedy clip"). Line 1 now reads "Another word for surprised? When something comes out of nowhere, you're not just surprised." The keyword comes first, it is tied to the hook, and the English is natural. The bullets match the cards and the title is fine.
- Left over (not blocking): the black band at the bottom (about 30%), the long single close-up, and the small figures in the 0-2.4 s wide shot. Same as pass 1.
