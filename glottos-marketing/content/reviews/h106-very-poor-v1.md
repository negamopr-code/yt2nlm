# Viewer-critic review: h106-very-poor-v1 (lab H106 arm 3: the wk40-41 winning "Stop saying very X" build, re-made on "very poor")

Reviewed 2026-10-26. File: state/shorts/h106-very-poor-v1/final.mp4 (1440x2560, 30 fps, 25.8 s, Kokoro am_michael 1.05x, mean -19.7 dB / max -1.3 dB).
final.mp4 = final-sub.mp4 (same md5 9fcbff07..., 11035311 bytes) - the handed file has the subscribe animation (unlike h106-very-weak-v1).
Not yet in /workspace/glottos-auto/out/ (no h106-very-poor-v1.mp4 there at review time).
Unit: shorts/units/h106-very-poor-v1.json (language_approval a6a01e9c8a301ee0). Meta: content/youtube/h106-very-poor-v1.json.
Not judged as defects (they are the test): the build itself, loop ending, no closing question, NotebookLM drawn pictures.

## Verdict: PARTLY
Five real words, each with a correct collocation, a clear picture and a clean, respectful treatment of poverty. But nothing tells me WHERE each word fits (impoverished = places, destitute = formal/nothing at all, broke = informal/me right now, needy = people who need help), and the video only covers the money sense of "very poor" - the "very poor quality / very poor results" I actually write at work is not touched, so a learner can produce "impoverished results".

Ship blockers: 0 hard blockers. One "ear check before publish" item (Penniless pronunciation, below). POLICY: none.

## Pain -> gives -> gap
- Pain: assumed from the lane brief ("I say 'very X' for everything, I want better words"). content/problems/ does not exist; the NotebookLM source list has only PROBLEM 01 (memorizing words); no verbatim learner quote on file about overusing "very" (same gap as the H59/H60/H106-slow/weak reviews). No NotebookLM query spent. No quotes invented.
- Solved = tomorrow I write "an impoverished region" or say "I'm broke this month" instead of "very poor".
- Gives: 5 words x 1 collocation, each heard twice, one picture each.
- Gap 1: no register/usage cue. "Broke" (informal, temporary, about yourself) and "destitute" (formal, extreme) are presented as equal swaps.
- Gap 2: "very poor" has a second, very common learner meaning: bad quality ("very poor service", "my English is very poor"). Not mentioned; all five words are wrong there. A one-line "(money only - for quality say 'dreadful'/'substandard')" would close it.
- Gap 3: "needy" also means emotionally clingy ("he's so needy"); "a needy family" disambiguates only partly.

## Hard gates
- Resolution 1440x2560: PASS.
- Subscribe + bell: PASS. final-sub.subscribe.json and meta "subscribe_at": [15.0]; red SUBSCRIBE ~15-16 s, SUBSCRIBED + yellow bell ~17-19 s, under the Penniless/Broke pictures, covers nothing. 15.0/25.8 s = second half.
- Spelled-out word: NONE.
- NotebookLM/Gemini watermark: none visible. Each picture has a faint white pill smudge at its bottom-right corner (watermark removal area), barely visible at phone size (e.g. 15.5 s, under the Penniless picture). Minor.
- POLICY / sensitivity: PASS, nothing blocked. Poverty is shown with sympathy, no mockery, no named people, nothing sexual:
  - Impoverished: wide arid landscape, crumbling mud-brick houses, tiny faceless figures. Neutral, but it is the stock "poor country = dry village" image - mild stereotype risk, not a block.
  - Destitute: older man in ragged clothes sitting on a step, holding a bag, coin at his feet. Sad, dignified.
  - Penniless: student with empty wallet, instant noodles, book stacks. Light, relatable.
  - Broke: woman at a checkout, card DECLINED. Relatable, neutral.
  - Needy: family with children at a COMMUNITY FOOD PANTRY, smiling volunteer. Respectful.
- Magnifying glass (rule 2026-10-05): DEFECT in 4 of 5 pictures -> back to visuals. Impoverished (~6-8 s), Destitute (~9.6-12 s), Penniless (~14-16 s), Broke (~18.3-20 s): the lens is plain blue/green glass, enlarges nothing. Needy (~22-25 s) is correct: the lens shows the family's faces and the patched coat enlarged.
- Garbled picture text (smudges): Penniless top-right book spines ("Advanced Eaxy...", "Mcrie Callers"); Needy volunteer's apron ("COMMUNITY 3HOP TNTRY", while the table sign is spelled right) and a cereal box. Tiny at phone size, not blockers; the apron one is the one a sharp viewer may notice.

## Audio (faster-whisper small.en, word timings)
0.00 Stop saying very poor | 2.02 Here are five better words (ends 3.46) | 4.36 Impoverished / 6.44 an impoverished country | 7.62 Destitute / 9.56 left destitute | 11.98 Penniless (heard "Panelist") / 14.00 a penniless student (heard "a panelist student") | 16.04 Broke / 18.26 flat broke | 19.88 Needy (heard "Nady") / 22.00 a needy family (ends 23.66) | ~2.1 s silence, loop card.
- Penniless: whisper writes "panelist(s)" 6 times out of 6 (small.en and base.en, with and without a vocabulary prompt, final mix and raw b04-0.wav/b04-1.wav). The clip ends on a plain /s/ (no separate /t/ burst in the energy profile), so it is probably the vowel/stress, not an added t. Can't confirm by ear here -> a human listen is needed; if it sounds like "PAN-uh-list", re-voice. A target word taught by ear must be pronounced cleanly.
- Needy (isolated, 19.88): clipped, whisper "Nady"/"Neaty". The phrase "a needy family" is clear (p 0.99). Minor.
- No spelled-out letters anywhere.

## Second by second
- 0.0-1.4: struck-out "very poor" from frame 1 over the floating-word background. My phrase, I stop.
- 1.4-4.3: "Here are five better words", lower screen empty; first word only at 4.36 s. Main swipe risk (lane-wide, part of the copied winning build).
- 4.3-23.7: one word every ~3.8 s, word alone then phrase + picture ~1.6 s later. Readable; card text big and yellow. Pictures ~2.3 s each: enough for the scene, not for the small embedded text (duplicated on the card anyway).
- The faint floating words in the background ("penniless", "broke", "destitute") are a little busy behind the cards but don't hurt legibility.
- 23.7-25.8: last card held, silence, loop to opening card. OK.

## Picture / word match
All five match what I hear at that moment: country landscape on "an impoverished country", man on the street on "left destitute" (it shows destitute, not the "left" = after a loss, fine), student + empty wallet on "a penniless student", declined card on "flat broke", family at a food bank on "a needy family". Best match of the H106 arms so far.

## Takeaway test
"When I run out of money, say 'I'm flat broke'; in writing about a country, say 'an impoverished country'." Nameable -> PARTLY, not DOESN'T. No self-test moment.

## Retention / trust risks
- 4.3 s before the first word (lane-wide).
- No register cue: informal "broke" next to formal "destitute"/"impoverished".
- Quality sense of "very poor" missing - the most frequent learner use in writing.
- Penniless possibly mispronounced (to confirm by ear).
- Empty lenses in 4/5 pictures look like a template sticker.

## Top 3 fixes (by impact)
1. Ear-check "Penniless" at 11.98 s and 14.0 s; if it is "PAN-uh-list", regenerate b04-0/b04-1 (e.g. respell for Kokoro, or the same voice's clean take) keeping the beat lengths, re-mux. Owner: voice (+ shorts-builder for the re-mux).
2. Add a 2-3 word usage tag on each card ("Impoverished - places", "Destitute - formal", "Broke - informal", "Needy - people who need help") and one line in the description: "Only for money. 'Very poor quality'? Say 'dreadful' or 'substandard'." Owner: scenario-writer (+ language-editor).
3. Make the lens really zoom in Impoverished, Destitute, Penniless, Broke (or remove it), and while redrawing fix the Needy apron text and give Impoverished a less stock scene (e.g. a run-down town street with closed shops). Owner: visuals.
