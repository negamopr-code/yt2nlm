# Viewer-critic review: pd2-broken-v1 (lab H85 batch 2, old-movie situation Short)

Reviewed 2026-10-17. File `state/shorts/pd2-broken-v1/final.mp4`: 1440x2560, 30 fps, 10.30 s, AAC 48 kHz stereo, peak -1.4 dB, mean -18.4 dB. Unit `shorts/units/pd2-broken-v1.json` (language hash 18cfcd2631a0ae63). Clip: Big Business (1929), source 870.7-873.3 + 873.45-876.4 + 876.5-882.05 (the video ends at about 881.25 in the last segment). `final.subscribe.json` subscribe_at [5.3].

## Verdict: PARTLY - 1 blocker
The car blowing up and the smoking wreck are the perfect picture for "beyond repair". But the two main words, "wrecked" and "totaled", play over a calm policeman sitting in an undamaged car writing a ticket. That is the same mistake as what-a-mess pass 1.

## Pain (learner's words)
I reused the batch-1 corpus evidence and spent no NotebookLM query:
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank."
- "great video but please shorten the intro!"
- "You have use the wrong synonym for rude"

Pain: "I say the same words all the time". Everything damaged is "broken".
Solved means: tomorrow I say "my phone is beyond repair" or "the car was totaled".
What it gives: three correct words with meanings and register tags. Gap: the picture contradicts two of the three words (below), and there is no self-test.

## What is heard (faster-whisper small.en, word timings)
0.00 You borrowed your friend's car. / 2.08 It's not just broken. (ends 3.06) / 3.80 It's wrecked. / 4.96 It's totaled. / 6.28 It's beyond repair. / 7.96 Ever "return to" car like this? (ends 9.52, then 0.78 s of silence to the loop). Whisper heard "returned a" as "return to". That is ordinary blurring of "-ed a" in fast speech, not a spelled-out word, but check it by ear. Gaps are 0.68-0.80 s.

## Second by second (cuts at 0.90 in the film, then 2.60 and 5.55 at the segment joins; the joins are clean, with no flash frames)
- 0.0 Frame 0: the yellow hook "POV: you borrowed your friend's car" over a wide, dark shot of the Model T in front of a house. The car is small and dark, and a man is half out of frame at the left. Weak motion.
- 0.9 Cut to the explosion: a white cloud swallows the car. This is the strongest moment, and it comes under "...your friend's car". Good.
- 2.60-5.55 BLOCKER: cut to a medium shot of the policeman in his own intact car, looking around and then writing in a notebook (motion index low). Under this shot: "broken" (2.70-3.06), the "wrecked / badly damaged, smashed" card (3.75, spoken 4.00-4.24) and the "totaled / too damaged to be worth fixing" card (4.92, spoken 5.18-5.48). What I see is a clean car and a calm man. The word is "smashed".
- 5.3 Subscribe + bell slides in at bottom-left (frames 5.5 and 6.0 checked). SUBSCRIBED by about 7, the bell rings by about 8.5. It covers no text.
- 5.55 Cut to the smoking wreck: the car is flattened in pieces, with a man walking through the smoke. "beyond repair / so damaged it can't be fixed" (spoken 6.48-7.28) is a perfect match.
- 7.87 The hook box swaps to "Ever returned a car like this?" (1 line). Good punchline over the wreck.
- 10.3 End. No frozen tail.

## Loop
It ends on the wreck and loops to the intact car before the blast. That reads as a replay. Audio: "...a car like this? / You borrowed your friend's car." Fine.

## Takeaway test
"My laptop is beyond repair." I can name one, so PARTLY rather than DOESN'T.

## Checklist
- 1440x2560: yes. Text is the same as in batch 1 and readable.
- Subscribe + bell at 5.3 s (51%): yes, visible, and it covers nothing.
- No intertitle and no watermark. The credit shows "Big Business (1929)" only. Film defect: a one-frame white scratch at about source 882.0. It is outside the current cut, but watch for it if segment 3 is extended.
- Meta: `content/youtube/pd2-broken-v1.json` DOES NOT EXIST yet. `"subscribe_at": [5.3]` must be recorded there.

## Retention risks
- 2.6-5.55: 3 s of a calm close-up right after the explosion. The energy drops exactly where it should build.
- Frame 0 is dark and small (the car in shadow).
- The black band at the bottom (about 30%).

## Trust risks
- The cop's undamaged car under "wrecked / smashed" and "totaled": the picture contradicts the card.
- "totaled" is mostly said about vehicles. The meaning "too damaged to be worth fixing" doesn't say that, so a learner may stretch it ("my shirt is totaled"). Minor; "a car or other vehicle" in the meaning would protect it (language-editor).

## BLOCKING fix (shorts-builder; footage checked in `state/examples/viral/library/hd/src/big-business-1929.webm`)
Drop the policeman segment (873.45-876.4). Source shot cuts are at 868.05, 870.67, 873.42, 876.42 and 883.51. Re-cut as:
- segments `[868.1, 873.3]` + `[876.5, 881.7]` (5.2 + 5.2 = 10.4 s, which covers T 10.28-10.30 without a freeze and stops before the 882.0 scratch).
- What the viewer then sees: 0-2.57 men smashing the car (real motion at frame 0, under "You borrowed your friend's car"). 2.57-5.2 the car and then the explosion at about 3.8, landing on "wrecked" (4.00). 5.2 cut to the smoking wreck, just as "totaled" (5.18) starts. Then "beyond repair" and the closing question over the wreck.
- Re-check after the render: frames at 2.5-2.7 and 5.1-5.3 for flash frames, the frame at 0, no freeze at the end, and subscribe at 5.3.
- If you'd rather keep the intact car as frame 0, use `[869.9, 873.3]` + `[876.5, 883.4]` instead. That includes the one-frame scratch at about 882.0 (output about 8.9), so I prefer the first option.

## Other fixes (not blocking)
2. Create `content/youtube/pd2-broken-v1.json` with `"subscribe_at": [5.3]` (re-read it from `final.subscribe.json` after the re-cut). No "public domain" in any field (publisher / shorts-builder).
3. Check by ear "returned a" at 8.16-8.70. Optionally make the totaled meaning "a car too damaged to be worth fixing" (voice / language-editor).

## Pass 2 (2026-10-17, re-cut [868.1, 873.3] + [876.5, 881.7])
**Verdict: SOLVES - no blocker.** The policeman is gone. Now every damage word plays over damage.
- File: 1440x2560, 30 fps, 10.30 s. Scene cuts in the picture band are at 2.60 and 5.27 only. There are no flash frames: I checked frames at 2.5, 2.6, 2.7, 5.1, 5.23, 5.27 and 5.3. freezedetect finds no frozen stretch, and the frame at 10.2 is the live wreck with the closing question.
- 0.0-2.6: men smashing the car. There is real motion at frame 0 under "You borrowed your friend's car". This fixes the dark, static frame 0 from pass 1.
- 2.6: cut to the intact car. The explosion is up at 3.8, and "wrecked" is spoken at 4.00 into the white cloud. Match.
- "totaled" is spoken at 5.16 over the smoke tail. The cut at 5.27 goes to the smoking wreck, which matches. "beyond repair" (6.48) and "Ever returned a car like this?" (7.96) play over the wreck.
- Subscribe: red SUBSCRIBE + bell visible at 5.3, bottom-left, and it covers no text. The meta `content/youtube/pd2-broken-v1.json` now has `subscribe_at [5.3]`. "public domain" appears only in the internal `language_approval` note, not in any published field.
- Audio is unchanged. Whisper still hears "return to car" at 8.16-8.70. That is the blurred "-ed a", NOT a spelled-out word, so it is not a blocker. Optional: a human check by ear.
- Still not done (format, not blocking): there is no self-test moment.
