# Viewer-critic review: pd2-ruined-v1 (lab H85, old-movie situation Short)

Reviewed 2026-10-17. File `state/shorts/pd2-ruined-v1/final.mp4`: 1440x2560, 30 fps, 10.80 s, AAC 48 kHz stereo, mean -18.1 dB, peak -1.5 dB. Unit `shorts/units/pd2-ruined-v1.json` (language hash e9595933ca7c068f). Clip: One Week (1920), source 1080.0-1092.0, one segment (the build uses about 1080.0-1090.7). `final.subscribe.json` subscribe_at [5.45].

## Verdict: SOLVES - no blocker
The storm-wrecked house (roof caved in, walls twisted, porch hanging off) fills the picture from frame 0 and stays in frame under every word. "Falling apart", "in ruins" and "uninhabitable" are each visibly true on screen when they are said. The footage is live to the last frame and has no cuts.

## Pain (learner's words; there is no PROBLEM doc for this lane, so I reused the batch-1 corpus evidence and spent no NotebookLM query)
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank."
- "great video but please shorten the intro!"
- "You have use the wrong synonym for rude"
Pain: "I say the same words all the time". Everything broken is "ruined".
Solved means: tomorrow I say "my old car is falling apart" or "after the fire the flat was uninhabitable".
What it gives: three correct expressions, each with a meaning and a register tag (everyday, neutral, formal), so the register ladder is clear. Gap: there is no self-test, and "uninhabitable" is the only one for which a B1 learner may need to hear the stress twice.

## What is heard (faster-whisper small.en, word timings)
0.00 You built the house yourself. / 1.86 It's not just ruined. / 3.80 It's falling apart. / 5.46 It's in ruins. / 7.18 It's uninhabitable. / 8.90 Would you still live there? (ends about 10.2, then silence to the loop at 10.8). Every word is heard as written, and "uninhabitable" is clear. No spelled-out words. Gaps are about 0.6 s, with no long dead air.

## Second by second (source shot is continuous from 1077.2 to 1092.2; frame-difference motion is 2.1-8.2 throughout, so there is no frozen stretch)
- 0.0 Frame 0: the yellow hook "POV: you built the house yourself" over the wrecked house, with the couple standing small in front of the porch. The house reads instantly at phone size. Motion at frame 0 comes from the couple only, and they are small (about 70 px tall).
- 0.0-3.7 Grey promise "3 better ways to say 'ruined'". The couple walk toward the camera and look at the house.
- 3.7 falling apart / breaking into pieces / everyday (spoken 4.00). The roof is caved in and the walls are buckled. Match.
- 5.4 in ruins / badly damaged, destroyed / neutral (spoken 5.74). Match: the house is clearly destroyed as a home, though it is still standing (see trust risks).
- 5.45 Subscribe + bell slides in at the bottom left, under the tag. It is red SUBSCRIBE at about 5.5-6.5, SUBSCRIBED by about 7, and the bell rings at about 8.5. It covers no text. 5.45/10.8 = 50%, so it is in the second half.
- 7.0 uninhabitable / not safe or fit to live in / formal (spoken 7.30). The couple struggle with each other in front of the porch (one tumbles at about 7.5). Match: nobody could live in it.
- 8.8 The hook box swaps to "Would you still live there?" (1 line). It is a real question the viewer can answer.
- 10.8 End: the couple are by the porch, and the footage is still moving.

## Loop
It ends with the couple at the porch and loops to them standing in front of it. The jump is small and the house is identical, so it reads as seamless. Audio: "...still live there? / You built the house yourself." with no echo.

## Takeaway test
"My old laptop is falling apart." / "After the flood the flat was uninhabitable." I can use both tomorrow, and the tags tell me which one to use at work.

## Checklist
- 1440x2560: yes. Headline about 130 px, meaning about 64 px, tag about 44 px, credit "One Week (1920)" about 36 px. All readable, nothing covered.
- No intertitle (the clip sits inside the shot; there is a held still at 1092.2, but the clip ends before it). No modern intro, no watermark, no magnifying glass.
- Subscribe + bell at 5.45 s: yes.
- Meta: `content/youtube/pd2-ruined-v1.json` DOES NOT EXIST yet. The video is not finished until it records `"subscribe_at": [5.45]` (shorts-builder / publisher). Keep "public domain" out of the viewer-facing fields.

## Retention risks
- The figures are small, so frame-0 motion is weak. The wreck carries the hook, the same as crooked pass 1.
- SAME HOUSE, SAME FILM as pd2-crooked-v1 (One Week, 1920). Different moments (built lopsided vs storm-wrecked), but in a feed a returning viewer sees "that house again". Do not publish the two Shorts on adjacent days (publisher).
- The empty black bottom band (about 30%), the same as all pd2 Shorts.

## Trust risks
- "in ruins" is slightly strong for a building that is still standing, but dictionaries allow "badly damaged" and the sub says exactly that. Acceptable.
- The hook "you built the house yourself" is true to the film. The language-editor already fixed "renovated".

## Top 3 fixes (none blocking)
1. Create `content/youtube/pd2-ruined-v1.json` with `"subscribe_at": [5.45]` and the three words with their tags in the description (shorts-builder / publisher).
2. Schedule it at least several days away from pd2-crooked-v1 (publisher).
3. Optional: a slow push-in on the couple and the porch (100% to about 115% over 0-3.7 s), so the human reaction reads at phone size (visuals / shorts-builder).
