# Viewer-critic review: long-stop-saying-very-short-v1 + door Short l1-short-3-more-words-v1 (lab H58, Short, 4 of 4)

Reviewed 2026-10-12. Frame: `content/reviews/long-stop-saying-very-happy-v1.md`.
- Long: `state/shorts/long-stop-saying-very-short-v1/final.mp4` - 2560x1440, 30 fps, 192.5 s (3:12.5; states sum 192.39 s), AAC 48 kHz mono. md5 cc11247e5b95608feb7fcb0c851f90e0.
- Short: `state/shorts/l1-short-3-more-words-v1/final.mp4` - 1440x2560, 30 fps, 22.5 s, AAC 48 kHz stereo. md5 d16ed54a6e5a6218dab66975fa98bbb2.
- Units: `shorts/units/long-stop-saying-very-short-v1.json` (language hash 57e3932c08ddaa8b), `shorts/units/l1-short-3-more-words-v1.json` (74a233814a224712).
- Metas: `content/youtube/long-stop-saying-very-short-v1.json`, `content/youtube/l1-short-3-more-words-v1.json`.

## Verdicts

- **Long: SOLVES - no render blocker.** Every H58 promise holds on the frames and in the timed transcript; "Say brief" is heard at 1.82-2.44 s and is on screen from frame 0.
- **Door Short: PARTLY - no render blocker by the mandatory gates.** It works as a door (struck phrase on frame 0, three words of the long video, closing card points to the lesson). It is only PARTLY for the learner because "Terse" is offered as a word "to use" with no meaning: the one thing that matters about terse (it sounds unfriendly) is carried only by an unamused emoji. "Short-lived sunshine" is also not a phrase anyone needs tomorrow. One of three words is directly usable (a succinct answer).
- **Hand-over:** both metas exist with the full launch kit. Open step: neither `final.mp4` is in `/workspace/glottos-auto/out/` yet (only the thumbnail is).

## Pain

Same thin evidence as the three siblings; no `content/problems/` folder and no PROBLEM document for this lane. The only verbatim corpus quote found (`state/corpus-glottos-niche/raw`, checked again today): "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?" A search of the corpus for "instead of very", "better word", "synonym", "simple words" found nothing more. I did not invent quotes. Demand evidence: the old Short EfeTrtoUE9I, 929 views (figure from the unit note, not re-measured). No NotebookLM query spent.

Pain in the learner's words: "I say the same words all the time" - every short thing is "very short".
Solved means: tomorrow I say "We had a brief phone call", "Let's take a quick break", "Keep your email concise".

Gives: 10 correct words in two clear groups, plain meanings, natural examples, 2 quiz questions, 10 say-it-aloud sentences. Unlike the Happy video, the words really differ and the glosses say how (fleeting = then gone; short-lived = less than you hoped; terse = unfriendly; snappy = catches attention).
Gap: "very short" in the learner's mouth is just as often a short person, short hair, a short distance. The video covers only time and texts. It says so at 4.8 s and on both part cards, but the title, the thumbnails and "Say brief" do not. A learner can leave with "a brief man" or "brief hair". Only 2 of 10 words are tested.

## H58 promises

| Promise | Result | Evidence |
|---|---|---|
| No greeting | PASS | first word "Stop" at 0.00 s |
| "very short" struck from second 0 (long) | PASS | frames 0.0 / 0.5 / 2.0 / 5.0 / 8.5 s identical: `Stop saying "very short"` with the red strike, `Say "brief" - or one of 9 other words` |
| "brief" on screen and spoken in 5 s | PASS | on screen from 0.0 s; spoken 2.08-2.44 s |
| 10 words in 2 parts | PASS | part 1 card 9.07-12.51 (Brief, Quick, Fleeting, Momentary, Short-lived); part 2 card 91.66-96.00 (Concise, Succinct, Terse, Snappy, Pithy); all 10 final states read |
| One quiz + one Repeat per part | PASS | quiz 49.88-62.72 and 133.68-145.22; repeat 62.72-91.66 and 145.22-175.80 |
| 3-4 minutes | PASS | 3:12.5 |
| Pronunciation (recogniser) | PASS | see Audio |
| Spelled-out words | none | every word whole in both videos |
| Native >= 1440 short side | PASS | 2560x1440 and 1440x2560 in the stream headers |
| Text cut off / at the frame edge | PASS | widest line, part 2 card `Texts and answers: "very short"`: x 174-2393 of 2560 (6.8 % / 6.5 % margins). Pithy card: text ends x 1240, picture starts x 1346. Short frame 0: strike x 112-1327 of 1440 |
| Quiz cards: no giveaway | PASS | plain background, blank, 3-2-1, then the answer in green and the wrong option struck |
| Subscribe + bell | PASS | see below |
| Magnifying glass | none | no magnifying glass in any picture or thumbnail |
| Chapters = screen | PASS | see Chapters |
| Thumbnails | PASS | see Thumbnails |
| Launch kit in the meta | PASS | `subscribe_at` [19.5, 111.4] = `sub.subscribe.json`; `ab_thumbs` 3 files exist, 1280x720 each; `endscreen` (watch_next aXghTlqKcHQ, pointed_from 2 ids, playlist); `door_shorts` [EfeTrtoUE9I, l1-short-3-more-words-v1]. Short meta: `subscribe_at` [17.0] = its `sub.subscribe.json`, `related_video_local` set |
| Short: struck phrase from the first frame | PASS | frames 0.0 / 0.1 / 0.5 s carry the red strike over the yellow "very short" |
| Short: three words all in the long video | PASS | Short-lived / Succinct / Terse with the same emoji pairs |

## First 5 seconds of the long video (measured)

| Time | Heard | Seen |
|---|---|---|
| 0.00-1.46 | "Stop saying very short." | `Stop saying "very short"` (struck), `Say "brief" - or one of 9 other words`, six picture tiles |
| 1.82-2.44 | "Say brief." | same slide |
| 3.16-4.38 | "Here are ten better words," | same slide |
| 4.84-8.26 | "five for a short time and five for short texts and answers." | same slide (stays to 9.07 s) |

The search phrase "another word for short" is not spoken in the hook (the Happy video had it at 3.3 s). Not an H58 promise for this title form; noted only.

## Audio (whisper small.en, word timings)

Every sentence of both units is heard as written. Recognised as the intended word:
- brief 2.08, 12.88, 16.86, 65.86; quick 19.70, 23.86, 71.26 (and "or quick" 54.6-55.3, see below)
- fleeting 31.36, 76.24; headword at 26.60 - see below
- momentary 34.26, 38.80, 81.50
- short-lived 41.82, 47.60, 54.16, 58.38, 60.70, 87.36 (Short 4.50, 5.84)
- concise 96.12, 101.48, 148.58
- succinct 104.12, 108.64, 137.80, 153.56 (Short 8.60, 10.76)
- terse 111.40, 116.14, 137.32, 141.80, 142.98, 159.18 (Short 12.82, 14.88)
- snappy 118.68, 124.10, 164.32
- pithy 126.96, 131.18, 170.42
- "another word for dot net" 180.08-181.46, printed "another word for .NET" (the recogniser's way of writing "dot net").

Two things I re-ran:
- **Fleeting headword, 26.60 s.** The full-file pass printed "Fleeing."; three other passes on the same audio (the beat clip `b05-0.wav`, a 7 s cut of the final and a 1.3 s cut of the final) printed "Fleeting". The same word in the two sentences is "fleeting" both times. I read it as a soft American t in the single word, not a wrong word. Worth one listen by ear; not a blocker.
- **"or quick?" in quiz 1.** The full-file pass dropped it; a 15 s cut of the final has "short-lived or quick" at 54.2-55.3 s. It is in the audio.

Limits: the recogniser cannot tell "short-LIVD" from "short-LYVD" (both are accepted; the unit note says the voice says LIVD), nor stress in "succinct" / "concise". Quiz think time 3.0 s with 3-2-1; say-it pauses 3.2-3.4 s. Speech ends 189.08 s, 3.3 s silent tail. Loudness: long mean -17.2 dB / peak -1.4 dB, Short mean -19.4 dB / peak -1.4 dB (the Short is 2 dB quieter on average). No silence of 3.6 s or more.

## Second by second (long)

- 0.0-9.07 Hook. Answer at 2.4 s, plan of the video by 8.3 s. One static slide for 9 s with six unlabelled tiles for ten words, in mixed order (brief, concise, quick, succinct, fleeting, terse).
- 9.07-12.51 Part 1 card, five labelled tiles. Clean.
- 12.51-49.88 Five words, about 7.5 s each: headline -> meaning + picture -> example.
- 19.5-24.5 Subscribe + bell, lower left, starts with the Quick headline. Covers nothing.
- 49.88-62.72 Quiz 1 (short-lived / quick). One right answer, but it asks the card that left the screen 0.0 s earlier, with the same words, and the wrong option is not even close. Too easy.
- 62.72-91.66 Repeat after me. 29 s without a picture; the passive viewer leaves here.
- 91.66-96.00 Part 2 card. Margins fine.
- 96.00-133.68 Five words. Subscribe + bell 111.4-116.4 from the Terse headline.
- 133.68-145.22 Quiz 2 (terse / succinct). Fair: the card was 20 s earlier and the two words are real neighbours.
- 145.22-175.80 Repeat after me.
- 175.80-182.69 Tip: anotherwordfor.net. 182.69-192.5 CTA.

## Pictures, word by word (Noto Color Emoji pairs)

| Word | Picture | Fit |
|---|---|---|
| Brief | stopwatch U+23F1 + telephone receiver U+1F4DE | good, it is "a brief phone call" |
| Quick | high voltage U+26A1 + hot drink U+2615 | good, "a quick break" |
| Fleeting | dashing away U+1F4A8 + slightly smiling face U+1F642 | acceptable. The smile is a full, steady smile and it comes second, so it reads "wind, then a smile". Swap the order to U+1F642 then U+1F4A8 (a smile, then gone) - the gloss is "then gone" |
| Momentary | shushing face U+1F92B + hourglass with flowing sand U+23F3 | weak, the weakest of the ten. The hourglass is the sign for "wait, this takes time"; the meaning is "a second or two". Proposed: U+1F92B + index pointing up U+261D U+FE0F ("one moment"); the stopwatch is taken by Brief |
| Short-lived | sun U+2600 + cloud with rain U+1F327 | good, the best of the set: the order tells the sentence |
| Concise | envelope U+2709 + OK hand U+1F44C | weak: it says "a good email", nothing says short or "no extra words". Proposed: U+2709 U+FE0F + scissors U+2702 U+FE0F (cut the extra words) |
| Succinct | speech balloon U+1F4AC + direct hit U+1F3AF | good, "to the point" |
| Terse | mobile phone U+1F4F1 + unamused face U+1F612 | good, it shows the unfriendly feeling of the reply |
| Snappy | sparkles U+2728 + newspaper U+1F4F0 | acceptable: the newspaper stands for a headline, the sparkles for "catches your attention" |
| Pithy | memo U+1F4DD + light bulb U+1F4A1 | weak: the memo is a full page of lines, the sentence is "one pithy sentence" and the meaning is "short". Proposed: pinching hand U+1F90F + light bulb U+1F4A1 (small size, big idea) |

No picture contradicts its word, so none is a render blocker. No watermark, no stray text, no magnifying glass. Compared with Happy this set is better: only two yellow faces in ten and each pair is tied to its example.

## Text and layout

No cut-off and no overlap on any of the 10 word cards. Two-line wraps are clean; "She gave me a fleeting / smile." and "There was a momentary / silence." leave a one-word last line. The "Short-lived" headline is set visibly smaller than the other nine (smaller than the longer "Momentary"), in the long video only. Ghost words sit behind text in several places: a dim "terse" directly behind the start of "He sent a terse reply." on the Repeat card, "momentary" behind the Brief and Quick meaning lines. Low contrast, readable.

## Subscribe + bell

- Long 19.5 s: 19.5-24.5 on the Quick card, lower left (pill about x 56-555, y 1074-1197 of 1440). Seen red "SUBSCRIBE" + bell at 19.6 and 21.0 s, grey "SUBSCRIBED" + yellow bell at 23.6 and 24.4 s. The example line "Let's take a quick break." (from 23.11 s) is about 250 px above it. Not in a quiz, not on a title card, after the first 15 s.
- Long 111.4 s: 111.4-116.4 on the Terse card. Red at 111.5 s, grey at 113.0, 115.9 and 116.3 s. The example "He sent a terse reply." (from 115.47 s) sits above it with clear space. 76 s before the end.
- Short 17.0 s: 17.0-22.0 on the closing card, lower left under the text (about 76 % of the height). Fading in at 17.1 s, red at 18.5 s, grey "SUBSCRIBED" at 20.0 and 21.5 s, gone at 22.2 s. Second half of the Short, covers nothing.
- Recorded in both `sub.subscribe.json` files and in both metas, same values.

## Chapters (description of the long video)

| Line | On screen at that second | Result |
|---|---|---|
| 0:00 Intro | hook slide 0-9.07 | ok |
| 0:10 A short time | part 1 card 9.07-12.51, on screen at 10.0 s (frame checked) | ok |
| 1:02 Speaking practice: a short time | Repeat card starts 62.72 | ok (second floored; 0.7 s of the quiz answer first) |
| 1:31 Short texts and answers | part 2 card starts 91.66 | ok |
| 2:25 Speaking practice: short texts and answers | Repeat card starts 145.22 | ok |
| 3:02 Your turn | CTA card starts 182.69 ("Which word will you use next time?") | ok |

All six match. Every chapter is at least 10 s by its timestamps; the last one is 3:02 to 3:12.5 = 10.5 s, so any trim of the tail breaks the chapters. `chapters.txt` says 0:09 for part 1, the meta says 0:10: the meta is the right one for YouTube. The tip slide (175.8-182.7) sits inside the second "Speaking practice" chapter, as in the siblings.

## Thumbnails

All four files are 1280x720. Spelling checked letter by letter.
- `new-yellow.jpg`: INSTEAD OF / VERY SHORT (struck) / SAY BRIEF in a hand-drawn oval. Text x 61-1187, strike x 52-1197. Nothing cut. The oval's lower edge is at y 713 of 720 (7 px from the bottom); it ends at x 1045, left of the duration badge. Words are all in the video ("instead of very short" is spoken at 184 s).
- `new-pairs.jpg`: three rows VERY SHORT (struck) -> BRIEF / CONCISE / TERSE, bar "10 BETTER WORDS". CONCISE ends at x 1250 of 1280: 30 px, equal to the 30 px left margin of the red circles. Tight but not cut. All three words are in the video. **Trust point:** TERSE stands under a green tick as a "better word"; the video itself teaches that terse "sounds unfriendly".
- `a-current.jpg` (= `thumbnail.jpg` to the eye; the bytes differ, a re-save): VERY SHORT? / SAY / BRIEF, pill 10 BETTER WORDS, a stopwatch. Nothing cut; the stopwatch crown ends at x 1237. The same thumbnail is at `/workspace/glottos-auto/out/long-stop-saying-very-short-v1-thumbnail.jpg` (byte-identical to `thumbnail.jpg`).

## Door Short (22.5 s)

- 0.00 s: `Stop saying "very short"` with the red strike on the first frame. Voice: "Stop saying very short." 0.00-1.38, "Here are three more words." 2.08-3.48. "3 more words" on screen by 3 s.
- 4.50-7.48 Short-lived / short-lived sunshine (sun + rain cloud). 8.60-11.82 Succinct / a succinct answer (speech balloon + target). 12.82-15.74 Terse / a terse reply (phone + unamused face). Each headword appears alone first, then the phrase with the picture.
- 16.56-20.62 "Want ten words for short? Watch the full lesson on this channel." Closing card + subscribe 17.0-22.0.
- Words and phrases are large and readable. "Short-lived", the widest headline, runs about x 107-1333 of 1440 (7.4 % margins). Picture panel about 40-66 % of the height; nothing under the Shorts buttons except the edge of the right-hand emoji; the title zone below 80 % is free.
- First new word at 4.50 s; the hook takes a fifth of the Short.
- Background: busy ghost layer (dim yellow words + faded logo tiles). A dim "short-lived" sits right behind the phrase "short-lived sunshine" and behind the headline. Readable, but it is noise.
- Meaning is never given. For Succinct the picture is enough. For Terse it is not: the title promises "3 More Words to Use" instead of "very short", and a learner can thank a colleague for a "terse reply".

## Takeaway test

Long: "We had a brief phone call", "Let's take a quick break", "Keep your email concise" - named without effort. Passes.
Short: "a succinct answer" - passes with one phrase. "A terse reply" is usable only if the learner already knows it is a complaint; "short-lived sunshine" is not for tomorrow.

## Retention risks

- Long: static hook slide for 9 s; two speaking blocks of 29 s and 31 s without pictures (60 of 192 s is practice).
- Long: quiz 1 is no test (see above); the viewer who wanted to check himself gets nothing until 2:14.
- Short: 4.5 s before the first word; three words in 11 s with no meaning.

## Trust risks

- No wrong facts and no unnatural English in either video. Glosses accurate.
- "Say brief" (hook, title form, all three thumbnails) with no limit to time and texts: "very short" for height or length is not covered and "brief" is wrong there.
- Terse as a "better word": green tick on `new-pairs.jpg`, and no meaning in the Short.
- The description says "practise" (British verb spelling); the unit was approved as American spelling. Cosmetic.

## A. RENDER BLOCKERS (must be fixed and rendered again)

None for the long video. None for the Short.

## B. Hand-over blockers (no render)

1. `final.mp4` of both videos is not in `/workspace/glottos-auto/out/` (no `long-stop-saying-very-short-v1.mp4`, no `l1-short-3-more-words-v1.mp4`, no `.subscribe.json` beside them; the siblings have them). Only the thumbnail is there. Open step, not a defect. Owner: shorts-builder / publisher.

Nothing else: both metas carry `subscribe_at`, the long meta carries `ab_thumbs` (3 files exist), `endscreen`, `door_shorts`, chapters match.

## C. Not blocking

1. Short: Terse has no meaning; add "(unfriendly)" to the phrase line or swap Terse for Concise ("a concise email"). This is the reason the Short is PARTLY. It needs a new render of the Short, so it is the lab's decision. scenario-writer, then language-editor, then shorts-builder.
2. `new-pairs.jpg`: TERSE under a green tick. Replace with QUICK or SNAPPY (both shorter than CONCISE, so the margin holds). Thumbnail only, before the test starts. visuals.
3. Momentary picture: hourglass says "long wait" (long 35.3-41.7 s, part 1 strip). visuals.
4. Pithy picture: a full page for "one sentence"; Concise picture: nothing says short. visuals.
5. Fleeting picture: swap the order (smile, then puff). visuals.
6. Quiz 1 asks the card just shown, against a far option. "fleeting / momentary" or "brief / short-lived" would test something. scenario-writer, then language-editor.
7. "Say brief" has no limit: one line on the hook or in the description ("for time and for texts - not for people or things") would stop "a brief man". scenario-writer, then language-editor.
8. Hook slide static for 9 s, six unlabelled tiles in mixed order. shorts-builder.
9. "Short-lived" headline smaller than the other nine in the long video. shorts-builder.
10. Ghost words directly behind text (Repeat card part 2, Brief/Quick meaning lines, Short). shorts-builder.
11. `new-yellow.jpg`: the oval is 7 px from the bottom edge; `new-pairs.jpg`: CONCISE 30 px from the right edge. visuals.
12. Last chapter is 10.5 s; do not trim the tail.
13. Fleeting headword at 26.6 s: one listen by ear (one of four recogniser passes printed "Fleeing"). voice.
14. The Short is 2 dB quieter on average than the long video. shorts-builder.
15. Description: "practise" against American spelling in the unit. language-editor.

## Top 3 fixes by impact

1. Give Terse its meaning in the Short, or swap it for Concise (scenario-writer -> language-editor -> shorts-builder), and take TERSE off the green-tick thumbnail (visuals).
2. Replace the Momentary, Pithy and Concise pictures (visuals) - at the next render, not for this one alone.
3. Make quiz 1 a real choice between two neighbours (scenario-writer, then language-editor).

## Not checked

- I did not listen: pronunciation is judged only by the recogniser printing the intended words; vowel in "short-lived" and word stress are not judged.
- The end-screen and door video ids (aXghTlqKcHQ, l28THsee6TI, EfeTrtoUE9I) were not opened on YouTube; the 929 views figure is taken from the unit note.
- Shorts buttons and title zone judged from zone percentages, not on a phone.
- Long video: every one of the 67 states was read on a 640 px frame; hook, both part cards, Quick, Terse, Pithy, tip and CTA also at 960 px or by pixel measurement. The other cards were not opened at full size.
- Thumbnails were read at 1280x720 and measured; not viewed at the small size YouTube shows on a phone.
- No learner quote specific to "short" exists in the corpus; the pain rests on one general quote and the old Short's views.
