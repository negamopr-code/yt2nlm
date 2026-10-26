# Viewer-critic review: pd2-stuck-v1 (lab H85 batch 1, old-movie situation Short)

Reviewed 2026-10-17. File `state/shorts/pd2-stuck-v1/final.mp4`: 1440x2560, 30 fps, 10.20 s, AAC 48 kHz. Unit `shorts/units/pd2-stuck-v1.json`. Clip: One Week (1920), source 529.1-531.85 + 534.0-535.75, played TWICE. Meta `content/youtube/pd2-stuck-v1.json`, subscribe_at [5.15].

## Verdict: PARTLY - 2 blockers
The close-up of a man yelling with his head poking out of the shingles is a great "stuck" image. But the 4.5 s clip simply repeats, so at 4.5 s the man bursts up through the roof again, right under "wedged in". The first frame is also an empty roof.

## Pain (learner's words)
There is no PROBLEM doc for this lane; I used the same corpus evidence as the pd1 reviews and spent no NotebookLM query:
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank."
- "great video but please shorten the intro!"
- "You have use the wrong synonym for rude"

Pain: "I say the same words all the time". Everything is "I'm stuck".
Solved means: tomorrow I say "I was wedged in between two people on the bus" or "the door won't budge an inch".
What it gives: three correct expressions with meanings and tags. Gap: no self-test, and "can't budge an inch" is shown as a headline but the picture doesn't support it (below).

## What is heard (faster-whisper small.en, word timings)
0.00 The roof repair went wrong. / 1.78 You're not just stuck. / 3.24 You're trapped. / 4.48 You're wedged in. / 5.88 You can't budge an inch. / 7.76 Ever been in a spot like this? (ends 9.32, then 0.69 s of silence to the loop). Every word is heard as written. No spelled-out words. Gaps between lines are 0.49-0.54 s. Peak -1.5 dB, clean.

## Second by second (cuts: 2.77, 4.50, 7.27)
- 0.00-0.10 BLOCKER: frame 0 is an empty roof with no person (zoomed frame checked). The head bursts through a hatch at about 0.1 s. The format promise is the funny situation AT frame 0; the extracted frame 0 shows only shingles. Cheap fix.
- 0.1-2.77 Wide shot: the man pops up through the roof, the hatch flies off, he twists and yells. Funny and moving. Under "The roof repair went wrong" it reads well.
- 2.77-4.50 Close-up: his head ringed by broken shingles, mouth wide open. "trapped" (spoken 3.40-3.74) fits perfectly.
- 4.50 The same wide clip restarts: an empty roof for a few frames (frame 4.55 checked), then he bursts up through the hatch AGAIN. BLOCKER: this plays exactly under "wedged in" (4.66-5.26). The picture shows a man shooting up out of the roof, the opposite of being stuck tight. Any viewer also sees an obvious rewind 4.5 s into a 10 s video.
- 5.15 Subscribe + bell at bottom-left (frame 5.6 checked). It clicks and the bell rings by about 8.5. It covers no text.
- 5.82-7.27 "can't budge an inch" (spoken 5.98-7.16) over the wide shot: he wriggles and moves his arms (motion index about 1.5-1.8, peak 4.6 at 7.0). It is weakly supported. The close-up (7.27-) would fit better.
- 7.27-9.0 Close-up again (also a repeat), under "Ever been in a spot like this?".
- 9.0-10.2 Picture FROZEN for 1.2 s (motion index 0.2-0.3). The clip material runs out at 9.0 s.

## Loop
It ends on the frozen close-up and loops to the empty roof, then the burst. Because the video already repeats internally, the loop seam is no worse than the inside cut, but the freeze followed by the empty roof is a visible hiccup. Audio: "Ever been in a spot like this? / The roof repair went wrong." No echo.

## Takeaway test
"The door won't budge an inch." / "I was trapped in the lift." I can name it, so PARTLY rather than DOESN'T.

## Checklist
- 1440x2560: yes. The hook is 2 lines ("POV: the roof repair went wrong") and readable. Text sizes are the same as the other pd2 Shorts. "can't budge an inch" fills the full width but fits.
- Subscribe + bell at 5.15 s (50.5%, second half), matching the meta: yes.
- No intertitle cards, no watermark: yes. Credit "One Week (1920)" only: yes.
- "public domain": not on screen and not in the title, description or tags. It is in the internal meta `format` field; remove it.
- Truth: "roof repair" is never seen. The picture shows a head through a roof, so it is plausible enough. Tags trapped = everyday, wedged in = neutral, can't budge an inch = spoken are fine.

## Retention risks
The visible repeat at 4.5 s is the biggest swipe moment. The 1.2 s end freeze. The empty black bottom band (about 30%).

## Trust risks
The picture contradicts "wedged in" (he is breaking OUT at that moment).

## Top 3 fixes, by impact
1. Stop repeating the clip. Use one continuous pass: wide 529.2-531.85 (starting at 529.2 or later so frame 0 already shows the head), then the close-up for "trapped", "wedged in" AND "can't budge an inch" (the close-up is where he is visibly stuck). Take any extra seconds from more One Week footage around 532-540 rather than looping the same burst. This fixes frame 0, the rewind and the "wedged in" contradiction (visuals, then shorts-builder).
2. Cover the whole 10.2 s with live footage so there is no 1.2 s freeze (shorts-builder).
3. Remove "public-domain" from the meta `format` string (shorts-builder / publisher).

## Pass 3 (2026-10-17): NEW footage, The Battle of the Century (1927) 885.0-896.0, words trapped / wedged in / stuck fast
File `state/shorts/pd2-stuck-v1/final.mp4`: 1440x2560, 30 fps, 10.80 s, AAC 48 kHz, mean -18.3 dB, peak -1.3 dB. Unit `shorts/units/pd2-stuck-v1.json` (language hash 0d981b3cb72bccf7). `final.subscribe.json` subscribe_at [5.45].

### Verdict: PARTLY - 1 blocker in the video, plus a stale meta
The new clip fixes the loop problem. It is one continuous shot (the source shot runs 884.88-896.00 and the clip ends at about 895.7, so no frames from other shots get in), and a man sitting in a bin at frame 0 is an instant "that's my problem" image. But the third card says "stuck fast: stuck so firmly you can't move" while the man walks briskly across the pavement with the bin on him. The picture contradicts the meaning at the moment it is said, and "stuck fast" only re-uses "stuck", so it is the weakest of the three words.

### Pain (learner's words, corpus evidence reused from batch 1; no NotebookLM query)
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank."
- "great video but please shorten the intro!"
Solved means: tomorrow I say "I was wedged in between two people on the bus" instead of "I was stuck".

### What is heard (faster-whisper small.en, word timings)
0.00 You fell into a bin and can't get out. / 2.40 You're not just stuck. / 4.06 You're trapped. / 5.46 You're wedged in. / 6.86 You're stuck fast. / 8.42 Ever been in a spot like this? (ends about 10.0, then silence to 10.8). Every word is heard as written. No spelled-out words. Gaps are about 0.6 s.

### Second by second (no cuts, no frozen stretch: frame-difference motion stays at 2.8-5.6 the whole time)
- 0.0 Frame 0: a dustbin with a man's legs sticking up out of it, in front of "Max's Barber Shop". From 0.3 to 1.0 he sits in the bin with his arms and legs flailing. This matches the hook "POV: you fell into a bin and can't get out" exactly. RISK: the figure is small (the bin is about 1/6 of the band width), so at phone size it takes a beat to read.
- 1.2-3.5 He bends over and the bin tips onto his upper body. The promise card is "3 better ways to say 'stuck'".
- 3.5 trapped / unable to get out / everyday (spoken 4.36). The bin covers him to the waist and only his legs show. Good match.
- 5.0 wedged in / stuck tight in a narrow space / neutral (spoken 5.62). He is inside the bin up to the hips. This is an acceptable match.
- 5.45 Subscribe + bell slides in at the bottom left, under the tag. It is red SUBSCRIBE at about 5.5-6.0, SUBSCRIBED by about 6.5, and the bell rings at about 8. It covers no text. 5.45/10.8 = 50%, so it is in the second half.
- 6.5 BLOCKER: stuck fast / stuck so firmly you can't move / neutral (spoken 7.02). On screen he is WALKING quickly to the right under the bin (frames 6.5-8.0). "You can't move" is visibly false at that moment.
- 8.3 The hook box swaps to "Ever been in a spot like this?". He staggers toward the shop door.
- 10.8 End: the bin man is at the doorway. The video is still live, with no frozen tail.

### Loop
It ends with the bin man at the door on the right and loops to the bin by the window on the left with him sitting in it. There is a position jump, but it reads as a replay, not a rewind. Audio: "...a spot like this? / You fell into a bin..." with no echo.

### Takeaway test
"I was wedged in between two people on the bus." / "I was trapped in the lift for an hour." I can use both tomorrow.

### Checklist
- 1440x2560: yes. The hook wraps to 2 lines and is readable. Credit "The Battle of the Century (1927)" is under the picture. No intertitle, no modern intro, no watermark, no magnifying glass.
- Subscribe at 5.45 s: visible and covers nothing.
- META STALE: `content/youtube/pd2-stuck-v1.json` still describes the OLD video. It has `subscribe_at [5.15]` (the video is now 5.45), "Can't budge an inch" in the description (the video now says "stuck fast") and "Clip: One Week (1920)" (it is now The Battle of the Century, 1927). It also has "old-movie..." in `format` (that is fine). Publishing with this meta would put the wrong word and the wrong film credit in front of the viewer. Owner: shorts-builder / publisher.

### Retention risks
The small figure at frame 0. The empty black bottom band (about 30%), the same as all pd2 Shorts.

### Trust risks
- "stuck fast = you can't move" over a man walking (above).
- "stuck fast" is a weak alternative to "stuck" because it contains the same word. A learner asked for a different word.
- "bin" is UK and consistent with the channel. Fine.

### Top 3 fixes, by impact
1. Make the third word match the picture (scenario-writer + language-editor, then voice and shorts-builder). Option A: replace "stuck fast" with a word the walking-blind picture shows, such as "boxed in" (meaning: trapped in a small space, can't get out; tag everyday). Option B: keep "stuck fast" but make the bin the subject: speech "It's stuck fast." and sub "so firmly stuck it won't come off". That is true on screen (the bin stays on him while he walks). Do not keep "you can't move".
2. Rewrite `content/youtube/pd2-stuck-v1.json` for the new video: subscribe_at [5.45] (or the new value after the re-render), the three current words, and "Clip: The Battle of the Century (1927)" (shorts-builder / publisher).
3. Optional: a gentle push-in (100% to 115% over 0-3.5 s) on the bin so that the man in the bin reads at phone size from frame 0 (visuals / shorts-builder).

---

## Pass 2 (2026-10-17, re-render 11.0 s, beat 4 = "You can't break free.")

**Verdict: SOLVES.** The only blocker from Pass 3 (the third word contradicted the picture) is gone. "can't break free" is said over a man who keeps walking with the bin still stuck on him, and that is exactly what the phrase means. Ready to ship as rendered. Meta not judged (it is being rewritten).

What I checked: frame-difference over the picture band for all 328 frames, a contact sheet every 0.4 s, zoomed strips at the two motion peaks, and a faster-whisper transcript (small.en, word timings) of `state/shorts/pd2-stuck-v1/final.mp4`.

- **Cuts / stray frames:** none. It is one shot from start to end. The only two peaks in frame difference (4.10 s and 9.23 s) are the man jerking forward under the bin inside the same shot (zoomed frames 120-125 and 274-279). There is no foreign frame.
- **Heard vs picture:**
  - 0.00 "You fell into a bin and can't get out": the man sits in the bin, flailing. Match.
  - 2.82 "stuck" / 4.36 "trapped": the bin is over his upper body. Match.
  - 5.62 "wedged in": he is in the bin to the hips. Match.
  - 6.84-7.6 "You can't break free": he staggers along, bin still on him. Match, and no longer false.
  - 8.62 "Ever been in a spot like this?": he is heading for the shop door.
  - No spelled-out words. Every word is heard as written.
- **Tail / loop:** live footage to the last frame (diff about 3 per frame up to 10.9 s), so there is no freeze. The loop goes from the man at the door to the bin by the window, which reads as a replay.
- **Cards inside the frame:**
  - "can't break free" / "can't escape, however hard you try" / everyday fits on one line each, with a wide margin.
  - The history line "trapped · wedged in" and the promise "3 better ways to say 'stuck'" fit.
  - The hook wraps to 2 lines inside the yellow box.
- **Subscribe:** red SUBSCRIBE is visible at 5.6 s (sheet frame 168), changes to SUBSCRIBED by about 6.5, the bell rings at about 8.6, and it fades by 10.9. It covers no text. 5.6/11.0 = 51%, so it falls in the second half.
- **Takeaway test:** tomorrow I can say "I was trapped in the lift" / "I was wedged in between two people on the bus" / "I tried, but I couldn't break free."
- **Remaining non-blockers (optional):**
  - The figure is small at frame 0 (a push-in, owned by visuals / shorts-builder).
  - The black bottom band is empty, as on all pd2 Shorts.
