# Viewer-critic review: h106-very-weak-v1 (lab H106: the wk40-41 winning "Stop saying very X" build, re-made on "very weak")

Reviewed 2026-10-26. File: state/shorts/h106-very-weak-v1/final-sub.mp4 (1440x2560, 30 fps, 25.2 s, Kokoro am_michael 1.05x, mean -19.8 dB / max -1.4 dB).
Handed-over copy /workspace/glottos-auto/out/h106-very-weak-v1.mp4 = final-sub.mp4 (same md5 836c23cb..., same size 9135843). final.mp4 differs (see blocker 1).
Unit: shorts/units/h106-very-weak-v1.json (language_approval present). Meta: content/youtube/h106-very-weak-v1.json.
Not judged as defects (they are the test): build, ending loop, no closing question, NotebookLM drawn pictures.

## Verdict: PARTLY - and NOT SHIPPABLE as handed over
As a lesson: five real words, each with a correct, common collocation, heard twice. But they are not five ways to say "very weak": each one belongs to a different thing (frail = old/ill people, flimsy = objects and excuses, limp = handshake/body, feeble = attempts/voices, powerless = no control), and nothing tells me that, so I can't safely pick one tomorrow.
As a file: the handed-over copy shows a POLICY problem in the Limp picture (below).

Ship blockers: 1 (POLICY, Limp picture in final-sub.mp4 / the out/ copy).

## Ship blockers
1. POLICY: Limp beat, ~17.8-20.0 s (picture on screen with "a limp handshake"). Behind the handshake, the NotebookLM drawing has a row of pale, unclothed-looking figures twisted around each other in pairs. At phone size they can read as naked bodies entangled. Doubt = block. Someone already saw this: pic-05.orig.png -> pic-05.png (05:40) blurs that strip, and final.mp4 (05:46) was re-rendered with the blur, BUT final.mp4 has NO subscribe/bell (checked frame 17.5 s: no button), and the handed-over final-sub.mp4 / out/h106-very-weak-v1.mp4 (05:39) is the OLD render with the figures still visible.
   Fix: shorts-builder re-runs shorts/subscribe_anim.py on the cleaned final.mp4 (subscribe_at 15.0), then re-hands the file to glottos-auto/out/. Better: visuals redraws Limp without the figure strip (the blur leaves a visible pink smudge above the hands); a limp hand + a strong hand, nothing else.

## Pain -> gives -> gap
- Pain: assumed from the brief ("I say 'very weak' about everything"). content/problems/ does not exist; no verbatim learner quote on file about overusing "very" (same as the H59/H60/H106-slow reviews). No NotebookLM query spent.
- Solved = tomorrow I say "a flimsy excuse" or "a feeble attempt" instead of "a very weak excuse/attempt".
- Gives: 5 words + 1 collocation each, picture per word.
- Gap: no "use it for..." cue. A learner who copies "a frail excuse" or "a limp attempt" or "I'm feeling powerless" meaning "I'm tired/weak" gets it wrong. "Powerless" is not "very weak" (it means no control); it is the odd one out and it is the last word I hear.

## Hard gates
- Resolution 1440x2560: PASS.
- Subscribe + bell: PASS in final-sub.mp4. final-sub.subscribe.json and meta "subscribe_at": [15.0]; red SUBSCRIBE at ~15-16 s, SUBSCRIBED + yellow bell ~17-19 s, below the Flimsy/Limp pictures, covers nothing. 15.0 of 25.2 s = second half. (FAIL in final.mp4: no animation.)
- Spelled-out word: NONE.
- Watermark / garbled text: none seen (no NotebookLM mark, embedded picture text matches the cards; "A flimsy excuse." reads fine on screen). The blur smudge in the final.mp4 Limp picture is visible but not text.
- Magnifying glass (rule 2026-10-05): DEFECT, not counted as blocker. Frail (~9.9-12 s), Flimsy (~13.7-16 s), Limp (~17.8-20 s), Powerless (~22-25 s): a small lens sits at the card edge showing empty blue glass, enlarges nothing. Feeble's lens is fine (shows a matchstick flame, the "attempt" in close-up). Back to visuals.
- POLICY: Limp picture, see blocker 1. Feeble picture: a child kneeling at a forest fire, blowing at it. Illustrates "useless attempt", not shown as fun; not blocked, but a child next to a wildfire is not ideal for a 13+ audience either - see fix 3.

## Audio (faster-whisper small.en, word timings)
0.00 Stop saying very weak | 2.06 Here are five better words (ends 3.5) | ~4.3 Feeble (whisper: "FIBO", p 0.36; with a prompt: "Feeble") / 5.70 a feeble attempt | 8.00 Frail / 9.90 frail health | 12.00 Flimsy / 13.66 a flimsy excuse | 16.00 Limp (whisper: "limpa") / 17.76 a limp handshake | 20.00 Powerless / 22.00 feeling powerless (ends ~23.3) | ~2 s silence, loop card.
- Isolated "Feeble" is clipped/unclear (whisper misses it; the phrase "a feeble attempt" is clear at p 0.99). Minor: the card shows the word.
- Isolated "Limp" has a little trailing vowel ("limpa"). Minor.
- No spelled-out letters anywhere.

## Pictures
- Feeble, "a feeble attempt": child blowing at a huge forest fire, lens showing a match flame. Gets "weak attempt against something big". Good idea, risky subject (child + wildfire).
- Frail, "frail health": very old woman wrapped in a blanket, eyes closed. Clear. Best picture.
- Flimsy, "a flimsy excuse": man in a storm with a broken paper umbrella. Shows a flimsy OBJECT while I hear "excuse" - picture and words don't match; a learner learns "flimsy = umbrella breaks", not the excuse use.
- Limp, "a limp handshake": handshake, wilted plant, worm, broken column, chain - plus the figure strip (blocker). Busy; the handshake itself does not look limp.
- Powerless, "feeling powerless": tiny man in front of a huge wall with roots. Works.

## Second by second
- 0.0-1.4: struck-out "very weak" from frame 1. My phrase, I stay.
- 1.4-4.3: "Here are five better words" over an empty lower screen; first word only at ~4.3 s. Main swipe risk (lane-wide, part of the copied build).
- 4.3-23.3: one word every ~4 s, word alone, phrase + picture ~1.5 s later. Readable; pictures are on screen only ~2.5 s each, enough for the image, not for its small embedded text (duplicated on the card anyway).
- 15-20: subscribe/bell under Flimsy/Limp. Fine.
- 23.3-25.2: last card held, silence, loop to the opening card. OK.

## Takeaway test
"Next time someone gives a bad reason, say 'that's a flimsy excuse'; a bad try is 'a feeble attempt'." Nameable, so PARTLY not DOESN'T. No self-test moment.

## Retention / trust risks
- 4.3 s before the first word (lane-wide).
- No usage cue: five words for five different nouns, presented as swaps for one phrase.
- Flimsy picture contradicts the phrase (object vs excuse).
- "Powerless" as a "very weak" synonym is a stretch; a careful learner may stop trusting the list.

## Top 3 fixes
1. BLOCKER: hand over a file without the Limp figure strip AND with subscribe+bell (subscribe_anim.py on the cleaned final.mp4, or redraw Limp first). Owner: shorts-builder (+ visuals for the redraw).
2. Usage cue on each card (e.g. "Frail - for people", "Flimsy - for things, excuses", "Limp - handshake, body"); or swap "Powerless" for "weak-willed"/"faint" ("a faint voice"). Owner: scenario-writer (+ language-editor).
3. Redraw: Flimsy showing an excuse (someone with an obviously fake note, "the dog ate my homework"), Limp as just a floppy hand in a firm hand, Feeble without a child at a wildfire (e.g. someone pushing a stuck car alone); and make the lenses zoom or remove them. Owner: visuals.
