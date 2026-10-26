# Viewer-critic review: long-stop-saying-very-small-v1 + door Short l1-small-3-more-words-v1 (lab H58, Small, 2 of 4)

Reviewed 2026-10-11. Template: `content/reviews/long-stop-saying-very-hot-v1.md`.
- Long: `state/shorts/long-stop-saying-very-small-v1/final.mp4` - 2560x1440, 30 fps, 205.7 s (3:25.7), AAC 48 kHz mono. Byte-identical (md5) to `/workspace/glottos-auto/out/long-stop-saying-very-small-v1.mp4`.
- Short: `state/shorts/l1-small-3-more-words-v1/final.mp4` - 1440x2560, 30 fps, 22.3 s, AAC 48 kHz stereo. Byte-identical to `/workspace/glottos-auto/out/l1-small-3-more-words-v1.mp4`.
- Units: `shorts/units/long-stop-saying-very-small-v1.json` (language hash f2eea7d95815f7b6), `shorts/units/l1-small-3-more-words-v1.json` (b91c211c5c48406c).

## Verdicts

- **Long: SOLVES - no render blocker.** Both Hot-video defects are gone (part-2 card has margins, quiz cards have no background words). One hand-over blocker in the meta, not in the render: the first chapter is 9 s long.
- **Door Short: PARTLY - 1 render blocker.** The content is right (three correct collocations, pointer to the lesson), but the hook promise fails: the first frame shows only "Stop saying", and the strike arrives at 1.65 s, after the voice has already finished saying "very small".

## Pain

Same thin evidence as the Hot review, no new source: no `content/problems/` folder, no PROBLEM document for this lane. Corpus quote: "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?" Channel comment under the Small Short: "There is also minuscule as in a minuscule mouse." Demand: the old Short IerZGsgD2Wk, 983 views. No NotebookLM query spent.

Pain in the learner's words: "I say the same words all the time" - everything is "very small".
Solved means: tomorrow I say "a tiny apartment", "a slight headache", "a slim chance", and I know which words are for things and which for amounts and chances.

Gives: 10 correct words in two groups that match real use, plain meaning, natural sentence, "the most common word" marked on tiny (the Hot video lacked this), 2 quiz questions, 10 say-it-aloud sentences.
Gap: only 2 of 10 words tested; minuscule / tiny and minimal / negligible / slight are never contrasted. Meager and negligible are formal words and nothing says so.

## H58 promises

| Promise | Result | Evidence |
|---|---|---|
| No greeting | PASS | first word "Stop" at 0.00 s |
| "very small" struck from second 0 (long) | PASS | frames 0.0 / 0.5 / 1.0 / 2.0 s identical: `Stop saying "very small"` with the red strike, `Say "tiny" - or one of 9 other words` |
| "tiny" spoken and visible in 5 s | PASS | visible from 0.0 s; spoken "very small" 0.66-1.3 s, "Say tiny" 1.96-2.6 s; "ten better words" 3.56 s |
| 10 words, each picture + meaning + example | PASS | all 10 final states checked |
| Quiz + repeat per part | PASS | quiz 54.5-68.3 and 144.6-157.5; repeat 68.4-101.7 and 157.5-189.0 |
| Pronunciation (recogniser) | PASS | minuscule x5 (long 20.96, 25.76, 76.86; Short 5.24, 6.60), miniature x4 (38.00, 44.12, 59.40, 90.86), negligible x6 (129.02, 134.88, 148.30, 153.20, 155.50, 178.24), meager x4 (137.40, 142.16; printed "meagre" at 149.10 and 184.36 - same word, British spelling) all printed as the intended word |
| Spelled-out words | none | every word whole in both videos |
| Native >= 1440 short side | PASS | 2560x1440 and 1440x2560 in the stream headers |
| Part title cards inside margins | PASS | part 1 headline ends x=2378, part 2 `Amounts and chances: "very small"` runs x=160 to 2406 of 2560 (154 px = 6 % right margin; Hot had 17 px) |
| Quiz cards: no word behind the blank | PASS | both quiz cards have a plain background, no ghost words at all |
| Subscribe + bell | PASS | see below |
| Magnifying glass | none | the microscope emoji is not a magnifying glass |
| Short: struck phrase from the first frame | **FAIL** | see blocker |
| Short: three words all in the long video, closing card points to the lesson | PASS | Minuscule / Compact / Slim, same pictures; "Want 10 words for small? Watch the full lesson on this channel." |

## Audio (whisper small.en, word timings)

Every sentence of both units is heard as written, nothing added or dropped. Quiz think time 3.5 s with 3-2-1 on screen; say-it pauses 3.2-4.5 s. Limit: I cannot listen. "miniature" in "a miniature train" takes 0.32 s (44.12-44.44), so it is the short two-syllable form; recognised, but stress and vowel quality of minuscule / negligible / meager are not judged by ear.

## Second by second (long)

- 0.0-9.3 Hook. Answer in 2.6 s. Then the same slide stays to 9.3 s; six unlabelled tiles for ten words. Dead picture 4-9 s, low swipe risk because the answer is already given.
- 9.3-12.8 Part 1 card, five labelled tiles. Clean.
- 12.8-54.5 Five words, about 8 s each: headline -> meaning + picture -> example.
- 20.7-25.7 Subscribe + bell, lower-left, starts with the Minuscule headline (better than Hot, where it landed on the first example). Covers nothing.
- 54.5-68.3 Quiz 1 (microscopic / miniature). Fair, one right answer. Very easy: the question contains "microscope".
- 68.4-101.7 Repeat after me. 33 s without a picture; the passive viewer leaves here.
- 101.7-106.4 Part 2 card. Margins fine. Faint ghost words "negligible" / "slight" sit right under the struck phrase; readable, not a defect.
- 106.4-144.6 Five words. Subscribe + bell 121.1-126.1 from the Minimal headline, covers nothing.
- 144.6-157.5 Quiz 2 (negligible / meager). Fair. Blank on its own line, clean background.
- 157.5-189.0 Repeat after me.
- 189.0-195.9 Tip: anotherwordfor.net. 195.9-205.7 CTA. Speech ends about 202.6 s; 3 s silent tail.

## Pictures, word by word

| Word | Picture | Fit |
|---|---|---|
| Tiny | pinching hand + house | good; house, not apartment, but "tiny home" reads at once |
| Minuscule | salt shaker + spoon | good, matches the sentence |
| Microscopic | microscope + microbe | good |
| Miniature | teddy bear + steam locomotive | acceptable; the locomotive is a normal train, only the teddy says "toy" |
| Compact | red car + P sign | good |
| Slight | pained face + pill | weak: the face shows strong pain, the word means "not serious" |
| Slim | slot machine showing 777 + four-leaf clover | **misleads**: 777 is the jackpot and the clover is luck - the picture says "we win", the sentence says the chance is very small |
| Minimal | tornado + undamaged house | acceptable; works only with the sentence |
| Negligible | price tag + level scales | acceptable; level scales = no real difference |
| Meager | gold coin + full purse | weak: a big gold coin and a fat purse read as money, not "not enough" |

No watermark, no stray text in the pictures.

## Text and layout

No cut-off anywhere. Widest text: hook sub-line to x=2448 (112 px margin). Wraps are clean; one orphan ("Add a minuscule amount of / salt."). Ghost words run through headline-only states ("Tiny" over "microscopic", countdown clean). Low contrast, not blocking.

## Subscribe + bell

- Long 20.7 s: 20.7-25.7, lower-left (x 56-555, y to 1225 of 1440), on the Minuscule card. Not in a quiz, not on a title card, not in the first 15 s. Example line appears at 25.3 s, 0.4 s before the animation ends, well above it.
- Long 121.1 s: 121.1-126.1, Minimal card. Not in a quiz; 84 s before the end.
- Short 16.9 s: on the closing card, under the text, covers nothing.
- Recorded in both metas and both `.subscribe.json` files, same values.

## Chapters

0:09 = 9.3 s, 1:08 = 68.4, 1:41 = 101.7, 2:37 = 157.5, 3:15 = 195.9: all match the slides. **But "0:00 Intro" lasts 9 s.** YouTube needs every chapter to be at least 10 s or it shows no chapters at all. The Hot video had 0:10. Fix without a render: write `0:10 Small things` (the part-1 card is on screen until 12.8 s) in `chapters.txt` and in the description. Last chapter 3:15 to 3:25.7 = 10.7 s, passes with 0.7 s to spare.

## Door Short (22.3 s)

- 0.00 s: card shows only "Stop saying". "very small" (yellow, not struck) fades in by about 0.3 s. **The strike appears at 1.65 s**; the voice said "very small" at 0.66-1.3 s. "3 more words" by 2.2 s.
- For comparison: the Short that had the wave (`/workspace/glottos-auto/out/l1-very-small-v3.mp4`) has the phrase and the red strike on frame 0. The door Short is weaker than the proven one exactly in the first second.
- 5.2-8.5 Minuscule / a minuscule amount (salt + spoon). 9.3-11.9 Compact / a compact car. 12.7-15.9 Slim / a slim chance (the misleading 777 + clover).
- 16.9-22.3 closing card + subscribe.
- Right edge: picture panel runs x=82 to 1355 of 1440 (94 % of the width), y 40-68 % of the height. The right-hand emoji ends at about 84-86 % of the width, so the Shorts button column touches the edge of the P sign / clover. No word is under a button.
- Background: busy ghost layer (words + faded logo tiles, some in dim yellow) as in the Hot door Short.

## Takeaway test

Long: "a tiny apartment, a slight headache, a slim chance" - named without effort. Passes.
Short: "a minuscule amount, a compact car, a slim chance" - passes.

## Retention risks

- Long: static hook slide 4-9 s; two 32 s speaking blocks without pictures (about 65 of 206 s is practice).
- Short: the first second does not show the problem phrase struck.

## Trust risks

- No wrong facts, no unnatural English. Glosses accurate.
- Slim picture contradicts the word (long 114.8-121.1 s, part-2 strip, hook strip, Short 12.7-15.9 s).
- Whisper prints "meagre" twice; the card says "Meager". Same sound, no issue.

## RENDER BLOCKERS (must fix before hand-over)

1. **Short, 0.00-1.65 s:** the first frame shows only "Stop saying"; the phrase fades in by about 0.3 s and the red strike only appears at 1.65 s. H58 promises the struck phrase from the first frame, and the wave Short had it on frame 0. Fix: draw `Stop saying "very small"` with the strike from frame 0 (no build-up animation on the hook). Owner: shorts-builder. One re-render of the Short, then re-run `subscribe_anim.py` and keep `subscribe_at` equal to what it prints.

Hand-over blocker without a render (meta):
2. **Long, chapters:** "0:00 Intro" is 9 s; YouTube drops all chapters under 10 s. Change `0:09 Small things` to `0:10 Small things` in `state/shorts/long-stop-saying-very-small-v1/chapters.txt` and in the description of `content/youtube/long-stop-saying-very-small-v1.json`. Owner: shorts-builder / publisher.

The long video itself has no render blocker.

## NOT BLOCKING

1. Slim picture (777 jackpot + clover) says "lucky", not "small chance"; it is in the long video three times and in the Short. visuals.
2. Slight (face in strong pain) and Meager (gold coin + full purse) pictures are weak. visuals.
3. Miniature: the locomotive is a normal train; only the teddy bear says toy. visuals.
4. Hook slide static 4-9 s, six unlabelled tiles. shorts-builder.
5. Quiz 1 gives the answer away ("microscope" -> microscopic); miniature / compact would test more. scenario-writer, then language-editor.
6. Meager and negligible are formal; one word of register on the card would help. scenario-writer, then language-editor.
7. Ghost words under the struck phrase on the part-2 card and through headlines. shorts-builder.
8. Short: picture panel's right edge is under the Shorts button column; busy background. shorts-builder.
9. Last chapter is 10.7 s; any trim of the tail breaks the chapters.

## Top 3 fixes by impact

1. Short hook: struck phrase on frame 0 (shorts-builder).
2. Chapters: 0:10 instead of 0:09 (meta).
3. Replace the Slim picture (visuals).

## Not checked

- I did not listen: pronunciation is judged only by the recogniser printing the intended words.
- Loudness and silences not re-measured (gate_av.py taken as given).
- Thumbnails and the three A/B thumbnails were not opened.
- Shorts buttons judged from zone percentages, not on a phone.
- The hook-frame comparison with the Hot door Short: it has the same late strike (no red at 1.7 s, red by 2.5 s); my Hot review noted "on by 3.6 s" and did not block it. It should be held to the same rule.
