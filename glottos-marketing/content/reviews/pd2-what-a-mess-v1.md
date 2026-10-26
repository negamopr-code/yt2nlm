# Viewer-critic review: pd2-what-a-mess-v1 (lab H85 batch 1, old-movie situation Short)

Reviewed 2026-10-17. File `state/shorts/pd2-what-a-mess-v1/final.mp4`: 1440x2560, 30 fps, 10.30 s, AAC 48 kHz. Unit `shorts/units/pd2-what-a-mess-v1.json`. Clip: The Battle of the Century (1927), source 903-907 + 907.5-913.6. Meta `content/youtube/pd2-what-a-mess-v1.json`, subscribe_at [5.2].

## Verdict: PARTLY - 2 blockers
The street pie fight is the right picture for chaos. But frame 0 is a different scene (a mailman at a mailbox), and the biggest word, "pandemonium", plays over one woman in a car quietly taking a pie. That is the opposite of "total chaos, with noise and shouting".

## Pain (learner's words)
There is no PROBLEM doc for this lane; I used the same corpus evidence as the pd1 reviews and spent no NotebookLM query:
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank."
- "great video but please shorten the intro!"
- "You have use the wrong synonym for rude"

Pain: "I say the same words all the time". Everything messy is "a mess".
Solved means: tomorrow I say "the meeting turned into chaos" or "it was mayhem at the station".
What it gives: three correct words with meanings and register tags. Gaps: (a) the picture mismatch above; (b) "a mess" mostly means untidy ("my room is a mess"). These three words cover only the "situation out of control" sense. A learner who goes on to say "my desk is pandemonium" has been misled (see trust risks).

## What is heard (faster-whisper small.en, word timings)
0.00 Things got out of hand. / 1.70 It isn't just a mess. / 3.26 It's chaos. / 4.64 It's mayhem. / 6.00 It's pandemonium. / 7.68 Ever seen things get this out of hand? (ends 9.46, then 0.71 s of silence to the loop). Every word is heard as written. No spelled-out words. Gaps between lines are 0.48-0.67 s. Peak -1.5 dB, clean.

## Second by second (cuts from scene detection: 0.27, 2.17, 3.67, 5.57)
- 0.00-0.27 BLOCKER: frame 0 is a mailman pulling pie out of a mailbox (a cut-in from the film), under "POV: things got out of hand". There is no fight and no crowd. That is 8 frames, enough to register as "what is this?". It is also the frame a feed preview grabs.
- 0.27-2.17 The street pie fight, a crowd throwing pies (motion index 8-10). This is what frame 0 should be.
- 2.17-3.67 Cut to a calm, well-dressed woman sitting in a car. Nothing is happening (motion index about 3). The "chaos" card appears at 3.19 over her, and the crowd returns at 3.67, just as "chaos" ends (3.42-3.74). Borderline.
- 3.67-5.57 The crowd again, under "mayhem" (spoken 4.80-5.10). Good match.
- 5.2 Subscribe + bell at bottom-left (frame 5.7 checked). It clicks and the bell rings by about 8.5. It covers no text.
- 5.57-10.3 The woman in the car again. The pie hits her face at about 6.3, exactly as "pandemonium" is said (6.26-6.70). BLOCKER: one person, a single pie, no crowd and no shouting, under the word whose card says "total chaos, with noise and shouting". The gag is funny, but it teaches the wrong picture for the hardest word.
- 7.61 The hook box becomes 2 lines: "Ever seen things get this out of hand?" Readable.
- No end freeze (the clip covers the full length).

## Loop
It ends on the pie-faced woman and loops to the mailman (frame 0). Neither shot is the fight. With frame 0 fixed to the crowd, the loop would be fine. Audio: "...this out of hand? / Things got out of hand." That says "out of hand" twice across the seam. It is a mild echo, acceptable.

## Takeaway test
"The meeting turned into chaos." I can still name it, so PARTLY rather than DOESN'T.

## Checklist
- 1440x2560: yes. Text sizes are the same as the other pd2 Shorts (headline about 130 px, meaning about 64 px, tag about 44 px, credit about 36 px). Readable.
- Subscribe + bell at 5.2 s (50.5%, second half), matching the meta: yes.
- No intertitle cards, no watermark: yes. Credit = film name only: yes.
- "public domain": not on screen and not in the title, description or tags. It is in the internal meta `format` field; remove it.

## Retention risks
The wrong first frame. The calm car-woman shot at 2.17-3.67 sits where the energy should build. The empty black bottom band (about 30%).

## Trust risks
- "pandemonium" over a lone woman: the picture contradicts the meaning card.
- Register tags: "chaos" is tagged neutral and "mayhem" everyday. In real frequency "chaos" is the everyday one and "mayhem" is more journalistic. A learner who checks a dictionary will see the tags reversed. Suggest chaos = everyday, mayhem = neutral (language-editor to confirm).
- Sense gap: the title "Stop Saying 'What a Mess'" invites the untidy sense. Viewers do call out wrong synonyms ("You have use the wrong synonym for rude"). A sub or speech hint such as "when a situation is a mess" would protect it.

## Top 3 fixes, by impact
1. Re-cut the picture so the crowd fight sits under the hook AND under all three words (chaos 3.4, mayhem 4.8, pandemonium 6.3). Start segment 1 at 903.3, not 903.0, so frame 0 is the fight. Move the woman's pie hit to the closing line (7.6+) or drop it. If there isn't enough crowd footage, take more of the street fight from elsewhere in the film (visuals, then shorts-builder).
2. Swap the register tags chaos/mayhem, and add the "situation" sense to the title, hook or sub so "a mess" = untidy isn't implied (language-editor, then scenario-writer).
3. Remove "public-domain" from the meta `format` string (shorts-builder / publisher).

## Pass 2 (2026-10-17, after re-cut)
Re-checked file `state/shorts/pd2-what-a-mess-v1/final.mp4`, built at 17:30. It is 1440x2560, 30 fps, 10.30 s, AAC 48 kHz stereo, peak -1.5 dB. Segments are 903.3-905.15 / 917.0-920.4 / 906.7-909.0 / 909.6-913.9 (the last one is cut off by the end of the video at about 912.3).

### Verdict: SOLVES on content - 1 ship-blocker (a 2-frame flash)
Both pass-1 blockers are fixed. Frame 0 is now the street pie fight: a crowd in mid-throw under "POV: things got out of hand". The crowd stays on screen under the hook, chaos (3.42), mayhem (4.80) and pandemonium (6.26). The picture finally shows what "total chaos, with noise and shouting" means.

### SHIP-BLOCKER: woman-in-car flash at 1.83-1.90
Frames 55-56 (1.833 and 1.867 s) are 2 frames of the calm woman in the car, between the two crowd shots. Segment 1 ends at 905.15, but the film cuts to the woman at about 905.08. In a 10 s loop that plays over and over it looks like a flicker or a glitch. Scene detection catches it as two cuts (1.83 and 1.90). Fix: end segment 1 at 905.05 or earlier and keep the total length the same (for example, start segment 2 at 916.9 or let segment 4 run 0.1 s longer). Then re-check frames 50-60. Owner: shorts-builder.

### Other checks
- Picture vs word: the crowd is under the hook (0-1.83), "It isn't just a mess" (1.70), chaos and mayhem (1.90-7.63 across the 917 and 906.7 segments) and pandemonium (6.00-6.70). The cut to the woman comes at 7.63, just before the closing line (7.68). The pie hits her face at about 7.9 during "Ever seen things get this out of hand?", which works as a funny punchline to the question. Minor: the last word card ("pandemonium / total chaos, with noise and shouting") stays on screen over the lone woman for the closing 2.7 s. The yellow box has already changed to the closing question, so this is acceptable. Not a blocker.
- Audio (faster-whisper small.en): "Things got out of hand. / It isn't just a mess. / It's chaos. / It's mayhem. / It's pandemonium. / Ever seen things get this out of hand?" Every word is heard as written. No spelled-out words. Gaps are 0.5-0.7 s.
- Subscribe + bell: in at 5.2 s, it clicks to SUBSCRIBED at about 6.4 and the bell rings at about 8.0. It covers no text. This matches `subscribe_at` [5.2] in the meta and `final.subscribe.json`.
- No intertitle (the clip ends at about 912.3, before the 913.96 card). No watermark. The credit shows the film name only. No frozen tail: motion stays at 1.4-3.7 to the last frame.
- Loop: it ends on the pie-faced woman and returns to the crowd fight. The cut back works. The audio echo "...out of hand? / Things got out of hand." is unchanged and mild.
- Tags on screen: chaos = everyday, mayhem = neutral, pandemonium = big word. This matches the corrected unit (language-editor hash c283c0699e794753).
- Meta `content/youtube/pd2-what-a-mess-v1.json`: "public-domain" is gone from `format`. Line 1 reads "Another word for a mess? When things get out of hand, it isn't just a mess." That makes the out-of-control sense clear and covers my pass-1 worry about the "untidy" sense. The bullets match the cards.
- Left over (not blocking): the black band at the bottom (about 30%).
