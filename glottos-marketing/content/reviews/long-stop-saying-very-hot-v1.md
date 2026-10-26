# Viewer-critic review: long-stop-saying-very-hot-v1 + door Short l1-hot-3-more-words-v1 (lab H58, Hot, 1 of 4)

Reviewed 2026-10-11. Files reviewed (the delivered ones, not the work copies, which differ byte-wise):
- Long: `/workspace/glottos-auto/out/long-stop-saying-very-hot-v1.mp4` - 2560x1440, 30 fps, 193.6 s (3:13), AAC 48 kHz mono.
- Short: `/workspace/glottos-auto/out/l1-hot-3-more-words-v1.mp4` - 1440x2560, 30 fps, 22.1 s, AAC 48 kHz stereo.
- Units: `shorts/units/long-stop-saying-very-hot-v1.json` (language hash 998c91d29600f45e), `shorts/units/l1-hot-3-more-words-v1.json` (0f7b04d68404e4ef).

## Verdicts

- **Long: SOLVES - with 2 render blockers** (section-2 title card runs edge to edge; the answer is ghosted behind the blank in quiz 2). Content, audio and structure meet every H58 requirement.
- **Door Short: SOLVES** as a door: three correct, usable collocations in 16 s and a clear pointer to the full lesson. No blocker.

## Pain

Evidence is thin and I say so. There is no `content/problems/` folder and no PROBLEM document or format article for the "Stop saying very X" lane. What exists:
- Corpus (`state/corpus-glottos-niche/raw`): "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- Channel comments (`content/insights/audience-needs.md`): viewers add their own word under these Shorts - "Frigid too", "Melancholic too", "There is also minuscule as in a minuscule mouse.", "Enraged and pissed off also work".
- Demand, not quotes: the old Short had 985 views; `content/insights/ab-lessons.md` says the typed phrase is "another word for hot".
No NotebookLM query was spent.

Pain in the learner's words: "I say the same words all the time" - everything is "very hot".
Solved means: tomorrow I say "It's boiling in here", "The soup is piping hot", "Careful, the water is scalding" and I know which word goes with weather and which with food, water or fire.

Pain -> what the video gives -> gap:
- Gives: 10 correct words in two groups that match real use (weather/feeling vs food/water/fire), a plain meaning, a natural sentence, "informal" marked on boiling, baking, roasting, 2 quiz questions between two real hot-words, 10 say-it-aloud sentences.
- Gap 1: only 2 of 10 words are tested. Scorching vs baking vs roasting and steaming vs piping hot are never contrasted.
- Gap 2: nothing says which words are the everyday ones. A learner leaves with ten equal words; "boiling" and "piping hot" would cover 80 % of daily use.

## H58 hard requirements

| Requirement | Result | Evidence |
|---|---|---|
| No greeting | PASS | first word at 0.00 s is "Stop" |
| Struck-out "very hot" + "boiling" on screen and spoken in 5 s | PASS | frames at 0.5 / 2 / 4 s all show `Stop saying "very hot"` struck in red and `Say "boiling" - or one of 9 other words`; spoken "very hot" 0.74-1.3 s, "Say boiling" 1.88-2.7 s |
| "another word for hot" said in first 30 s | PASS | 3.26-4.3 s |
| 10 words, each picture + meaning + example | PASS | all 10 final states checked |
| One quiz + one repeat-after-me per part | PASS | quiz 52.5-64.7 and 136.5-147.9; repeat 65.0-94.7 and 148.2-176.7 |
| Length 3-4 min | PASS | 3:13 |
| Native 1440 short side | PASS | 2560x1440 and 1440x2560 in the stream headers |
| Subscribe + bell at recorded times | PASS | long 19.0 and 127.0, Short 16.8 (see below) |
| Last chapter >= 10 s, chapters match | PASS | 2:56 -> tip card 176.9 s, cta 183.8 s, end 193.6 s = 17.6 s; 0:10 = 10.0, 1:04 = 65.0, 1:34 = 94.9, 2:28 = 148.2 |
| Spelled-out words | none | whisper small.en shows every word whole in both videos |

## Audio (whisper small.en, word timings)

Every sentence of both units is heard as written; nothing added, dropped or spelled out. "Sweltering", "Scalding", "Piping hot", "Red hot", "another word for .NET" all recognised as the intended words. Limit: I cannot listen, so intonation and rhythm are not judged. Pauses: quiz think time 3.5 s with a 3-2-1 countdown; say-it pauses 3.2-4.3 s after sentences of 1.3-2.4 s - enough. All pauses are fully silent (12 of them, no tick or bed).

## Second by second (long)

- 0.0-10.0 Hook. Strong first 4 s: my problem, the answer, the search phrase. Then the same static slide stays 10 s while the voice lists the plan. Six unlabelled emoji tiles for ten words. Swipe risk is low because the answer is already given, but 5-10 s is dead picture.
- 10.0-13.4 Part 1 card. Clear, 5 labelled tiles.
- 13.4-52.3 Five words, about 7.5 s each. Headline -> meaning + picture -> example. Readable, never rushed.
- 19.0-24.0 Subscribe + bell pops in directly under the first example sentence, 0.2 s after that sentence appears. It covers nothing, but it pulls the eye at the first teaching moment.
- 52.5-64.7 Quiz 1 (sweltering / scorching). Fair, one right answer. Good.
- 65.0-94.7 Repeat after me. LISTEN / YOUR TURN: SAY IT pills are clear. 30 s without a picture; this is where a passive viewer leaves, an active one stays.
- 94.9-99.3 Part 2 card - BLOCKER 1.
- 99.6-136.3 Five words. Subscribe + bell 127.0-132.0 over Red-hot example and the Blazing headline, covers nothing.
- 136.5-147.9 Quiz 2 - BLOCKER 2.
- 148.2-176.7 Repeat after me.
- 176.9-183.6 Tip: anotherwordfor.net. 183.8-193.6 CTA "Which word will you use next time? Write it in the comments." 3.1 s silent tail, fine for the end screen.

## Pictures (emoji cards), word by word

| Word | Picture | Fit |
|---|---|---|
| Boiling | hot sweating face + sofa and lamp | good: a person too hot in a room, matches the example |
| Scorching | sun + beach umbrella | good |
| Sweltering | thermometer + city at dusk | acceptable; the city is at sunset, not in heat, but thermometer + city = "the city was sweltering" |
| Baking | sun + desert with cactus | good, shows "hot and dry" |
| Roasting | sad sweating face + coat | acceptable; the sentence says "sweater", the picture is a coat |
| Piping hot | pot of soup with steam + hot-springs sign | good |
| Steaming | teapot + cup with steam | good |
| Scalding | blue drinking-water tap sign + warning triangle | weak: the blue sign means "drinking water" and blue reads as cold; only the triangle says danger. Understandable with the sentence, not on its own |
| Red-hot | flame + crossed hammer and pick | weak: no metal, nothing glows red; it is "fire + tools" |
| Blazing | flame + log | good |

No magnifying glass anywhere. No watermark. No stray text inside the pictures.

## Text and layout

- Hook, part-1 card, all 10 word cards, both quiz answers, all repeat states, tip, cta: no cut-off, wrapping is clean ("It's boiling in this small / room." and "She handed me a steaming cup / of tea." break naturally).
- Section cards, `Hot weather: "very hot"` with the quoted part struck: reads clearly on card 1 - white label, yellow struck phrase, the five words underneath. It works because the hook showed the same struck phrase 10 s earlier.
- **BLOCKER 1 - part-2 card (94.9-99.3 s):** `Food, water, fire: "very hot"` is drawn from x=40 to x=2543 of 2560. Left margin 1.6 %, right margin 0.7 %; the red strike line ends 17 px from the frame edge. Nothing is cut, but it has no margin, it is the only card like this, and on a TV with overscan or a rounded phone corner the closing quote goes. Fix: fit-to-width with the same side margin as card 1, or a shorter label. Owner: shorts-builder (or scenario-writer for a shorter label, then language-editor).
- **BLOCKER 2 - quiz 2 (136.5-144.2 s):** a background ghost word "scalding" sits directly behind the blank, so the line reads `Hot enough to burn your skin: ____lding`. It is faint, but it is the correct answer, at the exact place of the blank, on the test card. Fix: no ghost words behind the question/blank zone on quiz cards (or none on quiz cards at all). Owner: shorts-builder.
- Ghost words in general: on headline-only states a ghost word runs through the headline ("Boiling" over "sweltering"), and the countdown digits sit on "piping hot". Low contrast, not a blocker, but it is the source of blocker 2.

## Subscribe + bell

- Long 19.0 s: visible 19.0-24.0 bottom-left, on the Boiling word card then the Scorching card. Not on a quiz or title card, covers no text. Sits about 80 px (at 2560) under the example line.
- Long 127.0 s: visible 127.0-132.0, Red-hot card then Blazing. Not on a quiz or title card, covers nothing.
- Short 16.8 s: visible on the closing card, bottom-left, lower edge at 77 % of the height, above the Shorts title zone. Covers nothing.
- Recorded in both metas (`subscribe_at` [19.0, 127.0] and [16.8]) and in the `.subscribe.json` files.
- Note against the written rule: the rule says "at chapter starts". 19.0 and 127.0 are both mid-chapter (chapters start at 10.0 and 94.9). Avoiding the title cards is the better choice for the viewer, but the rule text and the practice now disagree.

## Thumbnails (all 1280x720)

- `new-yellow.jpg`: "INSTEAD OF / VERY HOT (struck) / SAY BOILING" in a hand-drawn red ring. Spelling right. All words are in the video ("instead of very hot" is spoken at 185 s). The ring ends 12 px above the bottom edge and 25 px from the sides; not cut. YouTube's duration badge will sit on the ring's lower right, not on the text.
- `new-pairs.jpg`: three struck "VERY HOT" -> BOILING / SCALDING / BLAZING, band "10 BETTER WORDS". Spelling right, all words in the video. "SCALDING" and "BLAZING" end about 25 px from the right edge: tight, not cut.
- `a-current.jpg`: "VERY HOT? SAY BOILING", pill "10 BETTER WORDS", hot face. Clean.

## Door Short (22.1 s)

- 0.0-4.0 Hook: card `Stop saying "very hot"`, voice "Need another word for hot? Here are three more." The strike and "3 more words" are on by 3.6 s. It is my problem in the first second.
- 4.3-7.8 Piping hot / piping hot soup (soup pot + hot-springs sign). 8.8-11.8 Scalding / scalding water (tap sign + warning). 12.9-16.0 Blazing / a blazing fire (flame + log). Word first, then collocation and picture, about 1.2 s later.
- 16.6-22.1 "Want 10 words for hot? Watch the full lesson on this channel." + subscribe animation.
- Shorts UI zones: everything taught is above 79 % of the height. The picture panel runs to 95 % of the width between 51 % and 79 % of the height, so the like/comment buttons will sit on the panel's white right margin and may touch the edge of the right-hand emoji. No word is under a button.
- Background: this Short's ghost layer (words plus faded logo tiles, some words in dim yellow) is much busier than the long video's. On the closing card a dim yellow "piping hot" sits just above the white headline. Not a blocker; it is the look of the Short that had the wave.

## Takeaway test

Long: "Next time it is hot I say 'It's boiling in here'; for food 'piping hot'; for water 'scalding'." Named without effort - passes.
Short: "piping hot soup, scalding water, a blazing fire" - passes.

## Retention risks

- 10 s static hook slide after a 4 s answer.
- Two 30 s speaking blocks with no picture and silent gaps; about 60 s of 193 s is practice. Good for the learner who speaks, a leaving point for the one who does not.
- Subscribe animation at 19 s competes with the first example.

## Trust risks

- No wrong facts, no unnatural English found. Glosses are accurate ("scorching" = strong sun, "baking" = hot and dry, "scalding" = burns skin).
- Scalding and Red-hot pictures do not show their word (above).
- Thumbnail pairs put SCALDING and BLAZING as general swaps for "very hot"; the video itself limits them to water and fire. Acceptable for a thumbnail.

## BLOCKERS (fix before the user sees it)

1. Long, 94.9-99.3 s: part-2 title card headline edge to edge (x 40-2543 of 2560). shorts-builder.
2. Long, 136.5-144.2 s: ghost word "scalding" behind the quiz blank shows "____lding". shorts-builder.
Both are one re-render of the long video; afterwards re-run subscribe_anim.py and keep `subscribe_at` in the meta equal to what it prints.

## Non-blocking notes

1. Red-hot picture (flame + hammer and pick) and Scalding picture (blue drinking-water sign) are weak; Scalding is also in the Short and the hook strip. visuals.
2. Roasting: coat in the picture, "sweater" in the sentence. visuals.
3. Hook slide is static for 10 s; reveal the two groups at 5 s or cut to the part-1 card earlier. shorts-builder.
4. Subscribe at 19.0 lands with the first example; 2-3 s later (after the example is read) would cost nothing. shorts-builder.
5. Rule text says subscribe "at chapter starts"; practice here is mid-chapter. Decide which one is the rule.
6. Add one line naming the everyday words (boiling, piping hot) and a second quiz question per part. scenario-writer, then language-editor.
7. Short: picture panel's right edge is under the Shorts button column; busy ghost background. shorts-builder.
8. `new-pairs.jpg`: SCALDING / BLAZING sit 25 px from the right edge.

## Top 3 fixes by impact

1. Part-2 card margins + ghost words off the quiz cards (shorts-builder) - the two blockers.
2. Replace the Red-hot and Scalding pictures (visuals).
3. Shorten the static hook and move the first subscribe animation off the first example (shorts-builder).

## Not checked

- I did not listen: pronunciation is judged only by whisper recognising the intended words.
- Loudness not re-measured (gate_av.py result taken as given: -15.5 and -14.4 LUFS).
- The Shorts UI overlay was judged from zone percentages, not on a phone.
- Title, description and tags were read but not ranked against search results.
