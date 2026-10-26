# Viewer-critic review: h106-very-slow-v1 (lab H106: the wk40-41 winning "Stop saying very X" build, re-made on "very slow")

Reviewed 2026-10-26. File: state/shorts/h106-very-slow-v1/final-sub.mp4 (1440x2560, 30 fps, 26.3 s, Kokoro am_michael 1.05x, mean -19.7 dB / max -1.5 dB).
Unit: shorts/units/h106-very-slow-v1.json (language_approval present). Meta: content/youtube/h106-very-slow-v1.json.
Not judged as defects (they are the test): build, ending loop, no closing question, NotebookLM drawn pictures.

## Verdict: PARTLY
Clean, fast, correct: five real words for "very slow", each heard twice with a natural phrase. But the five are not interchangeable (leisurely = slow and pleasant; sluggish/plodding/glacial = slow and annoying) and nothing tells me which is which, and I never try one myself.

Ship blockers: 0. (Same PARTLY as the lane's earlier reviews, e.g. l1-very-easy-h60-v1; fine to ship as the lab test.)

## Pain -> gives -> gap
- Pain: assumed from the brief ("I say 'very slow' about everything"). content/problems/ does not exist; no verbatim learner quote on file about overusing "very" (same as the H59/H60 reviews). No NotebookLM query spent.
- Solved = tomorrow I say "the traffic was snail-paced" or "a sluggish start" instead of "very slow".
- Gives: 5 words + 1 collocation each, picture per word.
- Gap: no tone cue. A learner who copies "a leisurely meeting" meaning "an annoyingly slow meeting" gets it wrong. "Glacial" is C1 and rare in speech for B1-B2.

## Hard gates
- Resolution 1440x2560: PASS.
- Subscribe + bell: PASS. final-sub.subscribe.json and meta "subscribe_at": [15.0]; red SUBSCRIBE at ~15-16 s, SUBSCRIBED + yellow bell 17-19 s, under the leisurely/snail-paced pictures, covers nothing. 15.0 of 26.3 s = second half.
- Spelled-out word: NONE.
- Magnifying glass / watermark / garbled text: none seen.
- POLICY: nothing found.

## Audio (faster-whisper small.en, word timings)
0.00 Stop saying very slow | 2.08 Here are five better words (ends 3.6) | 4.60 Sluggish / 6.34 a sluggish start | 8.36 "Plotting" / 10.42 "a plotting film" | 12.52 Leisurely / 14.62 a leisurely stroll | 17.08 Snail-"paste" / 19.26 snail-"paste" traffic | 21.22 Glacial / 23.60 at a glacial pace (ends ~24.3) | ~2 s silence, loop card.
- "Plodding" heard as "plotting" twice (American flap d). On screen the word is right, so readers are fine; listeners may learn "plotting". Minor, not a blocker.
- "Snail-paste": correct, "paced" IS pronounced /peist/. Not a defect.

## Pictures
- Sluggish, "a sluggish start": a man lying in bed looking ill, a tiny snail in the corner. Reads "sick in bed" more than "slow start". Weak. Caption "Experiencing a sluggish start" is stiff English.
- Plodding, "a plodding film": bored man in a cinema, sleepy emoji. Good.
- Leisurely, "a leisurely stroll": man walking in a park. Good, and shows the positive tone (the only hint of it).
- Snail-paced, "snail-paced traffic": traffic jam, "Stuck in snail-paced traffic." Good.
- Glacial, "at a glacial pace": ice cube + small glacier in corners, mostly empty card. Shows ice, not slowness; a learner may think "glacial = cold". Weakest, and it is the last picture before the loop.

## Second by second
- 0.0-1.4: struck-out "very slow" from frame 1. My phrase, I stay.
- 1.4-4.6: "Here are five better words" and an empty lower screen; first real word only at 4.6 s. Main swipe risk.
- 4.6-24.3: one word every ~4.2 s, headline first, picture ~1-1.5 s later. Readable, steady; no dead air inside beats.
- 24.3-26.3: last card held, silence, loop to the opening card. OK.

## Takeaway test
"Next time traffic or a film is slow, say snail-paced traffic / a plodding film." Nameable, so PARTLY not DOESN'T. No self-test moment.

## Retention / trust risks
- 4.6 s before the first word (lane-wide, part of the copied build).
- Leisurely mixed in with negative words without a cue = a quiet trust risk for learners who use it wrongly.
- Glacial picture can mislead (cold, not slow).

## Top 3 fixes (for a v2 / next word in this lane, not to break the H106 test)
1. Tone cue on the card: small "(relaxed, nice)" under Leisurely, "(annoying)" under Sluggish/Plodding/Glacial; or swap Leisurely for a negative word (e.g. "slow-moving"). Owner: scenario-writer (+ language-editor).
2. Redraw Glacial (glacier sliding / a clock with a snail of ice, "moving at a glacial pace" shown as slowness) and Sluggish (person dragging themselves out of bed in the morning, not ill); rewrite caption to "Off to a sluggish start." Owner: visuals.
3. Make "plodding" heard as plodding: phoneme hint / slower stress on the d in Kokoro, check it with whisper. Owner: voice.
