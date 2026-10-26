# Viewer-critic review: long-stop-saying-very-happy-v1 + door Short l1-happy-3-more-words-v1 (lab H58, Happy, 3 of 4)

Reviewed 2026-10-11. Frame: `content/reviews/long-stop-saying-very-small-v1.md`.
- Long: `state/shorts/long-stop-saying-very-happy-v1/final.mp4` - 2560x1440, 30 fps, 211.5 s (3:31.5), AAC 48 kHz mono. md5 b0d6c4de1ee1d8149b940471f0d2a79e.
- Short: `state/shorts/l1-happy-3-more-words-v1/final.mp4` - 1440x2560, 30 fps, 21.6 s, AAC 48 kHz stereo. md5 9fa42c936dee842677dad7ceafd2699e.
- Units: `shorts/units/long-stop-saying-very-happy-v1.json` (language hash 4639f85a4859d94d), `shorts/units/l1-happy-3-more-words-v1.json` (e385aeb081e47e96).

## Verdicts

- **Long: SOLVES - no render blocker.** Every H58 promise holds; the hook gives the answer in 2.6 s and says the search phrase by 4.5 s.
- **Door Short: SOLVES - no render blocker.** The Small sibling's blocker is fixed here: the struck phrase is on frame 0.
- **Hand-over blocker without a render (both videos):** there is no `content/youtube/long-stop-saying-very-happy-v1.json` and no `content/youtube/l1-happy-3-more-words-v1.json`, so `subscribe_at` is recorded only in the two `sub.subscribe.json` files. By the 2026-10-05 rule the videos are not finished until the times are in the metas. The files are also not yet in `/workspace/glottos-auto/out/`.

## Pain

Same thin evidence as the Hot and Small reviews, no new source: no `content/problems/` folder, no PROBLEM document for this lane. Corpus quote (`state/corpus-glottos-niche/raw`): "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?" No Happy-specific learner quote was found; I did not invent one. Demand: the old Short xcmxz9i1rno, 941 views. No NotebookLM query spent.

Pain in the learner's words: "I say the same words all the time" - everything is "very happy".
Solved means: tomorrow I say "I'm thrilled with my new job", "We're delighted to see you", "a joyful day".

Gives: 10 correct words in two groups, plain meaning, natural example with the right preposition (thrilled with, delighted to, overjoyed at), 2 quiz questions, 10 say-it-aloud sentences.
Gap: Happy is harder than Small or Hot, because all ten words name one feeling. The video never says which are everyday (thrilled, delighted) and which are formal or written (elated, jubilant, euphoric), and never puts them in order of strength. Overjoyed / ecstatic / elated / euphoric stay near-identical for the viewer. Only 2 of 10 words are tested.

## H58 promises

| Promise | Result | Evidence |
|---|---|---|
| No greeting | PASS | first word "Stop" at 0.00 s |
| "very happy" struck from second 0 (long) | PASS | frames 0.0 / 0.5 / 1.0 / 2.0 / 3.0 / 5.0 s identical: `Stop saying "very happy"` with the red strike, `Say "thrilled" - or one of 9 other words` |
| "thrilled" on screen and spoken in 5 s | PASS | on screen from 0.0 s; spoken 2.12-2.58 s |
| "another word for happy" in the first seconds | PASS | spoken 3.34-4.50 s ("Need another word for happy?"); "Here are ten" 4.94-5.54 s |
| 10 words, each picture + meaning + example | PASS | all 10 final states read |
| Quiz + repeat per part | PASS | quiz 54.9-68.7 and 148.6-160.2; repeat 68.7-101.3 and 160.2-194.9 |
| Pronunciation (recogniser) | PASS | see Audio |
| Spelled-out words | none | every word whole in both videos |
| Native >= 1440 short side | PASS | 2560x1440 and 1440x2560 in the stream headers |
| Part title cards inside margins | PASS | `People and times: "very happy"` runs x=194 to 2385 of 2560 (175 px = 6.8 % right margin); part 1 is shorter |
| Quiz cards: no giveaway behind the blank | PASS | both quiz cards have a plain background; blank on screen, 3-2-1 countdown, then the answer in green and the wrong option struck |
| Subscribe + bell | PASS | see below |
| Magnifying glass | none | no magnifying glass in any picture |
| Short: struck phrase from the first frame | PASS | frames 0.0 / 0.1 / 0.5 s all carry the red strike (x 98-1341 of 1440) over the yellow "very happy" |
| Short: three words all in the long video, closing card points to the lesson | PASS | Joyful / Jubilant / Blissful with the same emoji; "Want 10 words for happy? Watch the full lesson on this channel." |

## First 5 seconds of the long video (measured)

| Time | Heard | Seen |
|---|---|---|
| 0.00-1.44 | "Stop saying very happy." | `Stop saying "very happy"` (struck), `Say "thrilled" - or one of 9 other words`, six picture tiles |
| 1.88-2.58 | "Say thrilled." | same slide |
| 3.12-4.50 | "Need another word for happy?" | same slide |
| 4.94-5.54 | "Here are ten" | same slide (it stays to 10.4 s) |

## Audio (whisper small.en, word timings)

Every sentence of both units is heard as written. Recognised as the intended word every time:
- thrilled 2.12, 15.18, 19.70, 71.64; delighted 22.94, 26.14, 60.36, 77.06
- overjoyed 29.40, 34.20, 82.14; ecstatic 37.46, 42.54, 88.14
- elated 45.86, 51.20, 59.82, 64.32, 65.48, 94.38
- joyful 105.94, 111.54, 163.86; radiant 114.18, 118.80, 169.38
- jubilant 121.82, 127.36, 152.30, 174.72 (Short 7.98, 9.68)
- blissful 131.04, 135.32, 151.60, 156.28, 157.60, 181.46 (Short 12.22, 14.24)
- euphoric 138.20, 144.70, 187.46
- "another word for dot net" 199.14-200.52, printed by the recogniser as "another word for .NET" (its own way of writing "dot net").

Small things: "happy people and happy times" is printed "in happy times" at 8.64 s and again in part 2 - a reduced "and", normal in fast speech, not an error. Quiz think time about 3.5 s with 3-2-1; say-it pauses 3.4-4.3 s. Speech ends 208.2 s, 3.3 s silent tail. Limit: I cannot listen; stress and vowel quality are not judged by ear.

## Second by second (long)

- 0.0-10.4 Hook. Answer at 2.6 s, search phrase at 4.5 s. The same slide then stays to 10.4 s with six unlabelled tiles for ten words. Dead picture 5-10 s.
- 10.4-15.0 Part 1 card, five labelled tiles. Clean.
- 15.0-54.9 Five words, about 8 s each: headline -> meaning + picture -> example.
- 22.7-27.7 Subscribe + bell, lower left, starts with the Delighted headline. Covers nothing.
- 54.9-68.7 Quiz 1 (elated / delighted). One right answer, but it asks the card that left the screen 0.0 s earlier, with the same words. Too easy.
- 68.7-101.3 Repeat after me. 33 s without a picture; the passive viewer leaves here.
- 101.3-105.8 Part 2 card. Margins fine. Ghost words "blissful" / "joyful" sit under the struck phrase and "ant" beside the Joyful label; readable.
- 105.8-148.6 Five words. Subscribe + bell 113.9-118.9 from the Radiant headline.
- 148.6-160.2 Quiz 2 (blissful / jubilant). Fair.
- 160.2-194.9 Repeat after me.
- 194.9-201.8 Tip: anotherwordfor.net. 201.8-211.5 CTA.

## Pictures, word by word

| Word | Picture | Fit |
|---|---|---|
| Thrilled | star-struck face + briefcase | good, matches "my new job" |
| Delighted | smiling face + hugging face | good; the hug says "to see you" |
| Overjoyed | partying face + newspaper | good, "at the news" |
| Ecstatic | raised hands + football | good |
| Elated | beaming face + graduation cap | good |
| Joyful | wedding chapel + party popper | good |
| Radiant | grinning face + sparkles | acceptable; the fourth yellow face of the set, the sparkles carry it |
| Jubilant | one man dancing + trophy | weak: the sentence is "Jubilant crowds filled the streets" and the picture shows one disco dancer. Proposed: confetti ball U+1F38A + trophy U+1F3C6 (partying face U+1F973 is already Overjoyed), or woman dancing U+1F483 + man dancing U+1F57A if "more than one person" matters more than "a win" |
| Blissful | relieved face + beach with umbrella | good, the best of the set |
| Euphoric | chequered flag + sports medal | weak: no person and no feeling, it shows a race, not how she felt. Proposed: woman running U+1F3C3 U+200D U+2640 U+FE0F + chequered flag U+1F3C1 (she crosses the line; the medal goes) |

General: four of ten pictures are a yellow smiling face (star eyes, blush, grin, beam). At tile size on the hook strip they look the same. The pictures cannot show the difference between the words; only the second emoji does. No watermark, no stray text.

## Text and layout

No cut-off and no overlap on any of the 10 word cards; meaning, example and picture all readable. Two-line wraps are clean ("Jubilant crowds filled the / streets.", "She gave us a radiant / smile." leaves a one-word last line). Ghost words run directly behind the headlines in the headline-only states: "Delighted" is followed by a faint "ted", "Thrilled" by a faint "elated". Low contrast, not blocking.

## Subscribe + bell

- Long 22.7 s: 22.7-27.7, red pill x 56-555, y 1074-1197 of 1440, on the Delighted card. Seen red at 23.3 s, grey "SUBSCRIBED" with yellow bell at 26.6 s, fading at 27.5 s. The example line (y 754-828) is 250 px above it. Not in a quiz, not on a title card, not in the first 15 s.
- Long 113.9 s: 113.9-118.9, same place, Radiant card. Seen red at 114.5 s, grey at 118.4 s. The two-line example ends at y 993, the pill starts at y 1079: 86 px free. The tightest spot of the video, still clear. 92 s before the end.
- Short 16.4 s: 16.4-21.4 on the closing card, lower left under the text (about 73-76 % of the height), covers nothing.
- Recorded in both `sub.subscribe.json` files. NOT recorded in any `content/youtube/*.json` (the files do not exist yet).

## Chapters

0:10 = 10.4 s, 1:08 = 68.7, 1:41 = 101.3, 2:40 = 160.2, 3:21 = 201.8: all match the slides. "0:00 Intro" is 10 s, passes. Last chapter 3:21 to 3:31.5 = 10.5 s, passes with 0.5 s to spare.

## Door Short (21.6 s)

- 0.00 s: `Stop saying "very happy"` with the red strike on the first frame. Voice: "Need another word for happy?" 0.00-1.48, "Here are three more." 2.24-3.44. "3 more words" on screen by 3 s.
- 4.24-6.96 Joyful / a joyful day (chapel + party popper). 7.98-10.98 Jubilant / jubilant crowds (dancer + trophy). 12.22-15.00 Blissful / a blissful week (relieved face + beach).
- 15.74-19.82 "Want ten words for happy? Watch the full lesson on this channel." Closing card + subscribe to 21.4 s.
- Words and collocations are large and readable. Picture panel: x 90-1348 of 1440, y 36-68 % of the height; the right-hand emoji ends at about 87-91 % of the width, so the top of the Shorts button column touches the trophy handle / umbrella edge. No word is under a button. Bottom title zone (below about 80 %) is free: the panel ends at 68 %, the subscribe pill at 76 %.
- First new word at 4.24 s. The hook takes 4.2 s, a fifth of the Short.
- Background: busy ghost layer (words in dim yellow + faded logo tiles); on frame 0 a dim-yellow "bliss / jubila" sits right behind "very happy". Readable, but it is noise in the first second.
- The picture says "Stop saying very happy", the voice says "Need another word for happy?" - two different sentences at once. Both are true; not a defect.

## Takeaway test

Long: "I'm thrilled with my new job", "We're delighted to see you", "a joyful day" - named without effort. Passes.
Short: "a joyful day, jubilant crowds, a blissful week" - passes.

## Retention risks

- Long: static hook slide 5-10 s; two 33 s speaking blocks without pictures (about 67 of 211 s is practice).
- Long: ten words for one feeling at the same pace; by word 7 it feels like repetition because nothing separates them.
- Short: none beyond the 4.2 s before the first word.

## Trust risks

- No wrong facts, no unnatural English. Glosses accurate.
- Register is not marked: a learner who says "I'm jubilant" or "I'm elated" in a meeting will sound bookish. The examples themselves are safe ("Jubilant crowds", "He was elated after passing the exam").
- Jubilant picture shows one person for "crowds".

## RENDER BLOCKERS (must fix before hand-over)

None for the long video. None for the Short.

Hand-over blocker without a render (meta):
1. **Both videos:** create `content/youtube/long-stop-saying-very-happy-v1.json` with `"subscribe_at": [22.7, 113.9]` and `content/youtube/l1-happy-3-more-words-v1.json` with `"subscribe_at": [16.4]` (values = the two `sub.subscribe.json` files), chapters as in `chapters.txt`. Owner: shorts-builder / publisher.

## NOT BLOCKING

1. Jubilant picture: one dancer for "crowds" (long 122.7-130.8 s, part-2 strip, hook strip, Short 9.7-11.9 s). visuals.
2. Euphoric picture: flag + medal, no person, no feeling. visuals.
3. Four near-identical yellow faces (Thrilled, Delighted, Elated, Radiant). visuals.
4. No register or strength marking on ten near-synonyms; "most common" could go on Thrilled, "formal" on Elated / Jubilant / Euphoric. scenario-writer, then language-editor.
5. Quiz 1 asks the word whose card was on screen a moment before, in the same words. Thrilled / overjoyed or delighted / ecstatic would test more. scenario-writer, then language-editor.
6. Hook slide static 5-10 s, six unlabelled tiles for ten words. shorts-builder.
7. Ghost words directly behind headlines and under the struck phrase on the part-2 card. shorts-builder.
8. Short: right-hand emoji under the edge of the Shorts button column; busy background on frame 0. shorts-builder.
9. Last chapter is 10.5 s; any trim of the tail breaks the chapters.

## Top 3 fixes by impact

1. Write the two metas with `subscribe_at` and chapters (shorts-builder / publisher) - without them the videos are not finished.
2. Mark register and the most common word on the cards (scenario-writer, then language-editor) - this is what decides whether the learner uses the right one tomorrow.
3. Replace the Jubilant and Euphoric pictures (visuals).

## Not checked

- I did not listen: pronunciation is judged only by the recogniser printing the intended words.
- Loudness and silences not re-measured.
- `thumbnail.jpg` and any A/B thumbnails were not opened.
- Shorts buttons and title zone judged from zone percentages, not on a phone.
- Word cards were read on 640 px frames of every state plus full-size frames of the hook, both part cards, quiz 1, Thrilled, Delighted, Joyful, Radiant and the CTA; the other cards were not opened at full size.
