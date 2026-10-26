# Viewer-critic review: lab H71 "THE NARRATOR HAS AN OPINION" (Textbook English vs Real English), 2 Shorts

Date: 2026-10-13. Reviewer: viewer-critic (B1-B2 learner's point of view). Read-only: nothing rendered, changed or uploaded.

Videos:
- `state/shorts/l11-textbook-how-do-you-do-v1/final.mp4` (1440x2560, 30 fps, 10.80 s)
- `state/shorts/l11-textbook-cats-and-dogs-v1/final.mp4` (1440x2560, 30 fps, 11.80 s)

## Verdicts

| Video | Verdict | Why in one sentence |
|---|---|---|
| l11-textbook-how-do-you-do-v1 | **PARTLY** | Clean, true and watchable, and I get one usable swap, but the main swap ("Nice to meet you") is something every B1 learner already says, so little changes tomorrow. |
| l11-textbook-cats-and-dogs-v1 | **SOLVES** | I learned this idiom at school, the video tells me it is dated and hands me two phrases I did not have ("It's pouring", "It's really coming down") that I can say the next time it rains. |

**SHIP BLOCKERS: none in either video.** Nothing is wrong, unreadable, misheard or misleading. No word is spelled letter by letter.

## 1. The pain (learner corpus, verbatim, no names)

There is no `content/problems/` document for this lab lane (the folder does not exist), so quotes were pulled directly from the comment corpus `/workspace/reports/monitor-awf/archives/youtube-comments-vol*.md`. No NotebookLM query was spent.

- "It really highlights how natural communication and confidence matter so much more than trying to sound like a textbook."
- "it makes us dive into Americain cultur and sound more native as we dont get to learn them from schools or textbooks"
- "The goal is not specifically to sound like a native speaker, but rather to learn words or expressions that one might hear in real life."
- "The problem is when I try to speak I end up not saying the right words and or when I do the grammar is wrong to the point where it's unnatural and doesn't sound right."
- "Don't ever use "how's it hangin?" That's extremely outdated, and anyone you say it to is going to laugh at you"
- "no one says that anymore. [...] People will think your from the 80/90 when that expression died."
- "It works, but it doesn't sound natural."
- (about Japanese, same pain in another language) "I have heard Textbooks are not the best because they often teach unnatural and robotic sounding Japanese which is unlike what Native speakers use in their day to day lives."

Pain in the learner's words: "School and textbooks gave me phrases that real people don't say, and I am afraid of sounding dated or being laughed at."
"Solved" means: for one concrete phrase I learned, I now know it is dated and I have the phrase people really use, ready to say tomorrow.

## 2. What is seen and heard

Both renders are 1440 on the short side (pass). Audio mean -17.5 dB, peak -1.2/-1.4 dB, music well under the voice.

### how-do-you-do (10.80 s)

Heard (faster-whisper small.en, word timings, video played twice in a row to test the loop):

| Time | Heard | On screen |
|---|---|---|
| 0.00-0.60 | "How do you do?" | From frame 0: black bar "TEXTBOOK: ~~How do you do?~~", yellow "Hardly anyone says that!", blue badge "Next: what people really say". Old man in a top hat, boy scratching his head. |
| 0.82-2.26 | "Hardly anyone says that anymore." | same |
| 2.77 cut; 2.80-4.10 | "It sounds a hundred years old." | "It sounds 100 years old!" + badge. Boy coughing dust from a cobwebbed book, spider. |
| 4.55 cut; 4.58-5.08 | "People say," | red tag "REAL ENGLISH", handshake in an office |
| 5.30-6.20 | "nice to meet you," | yellow "Nice to meet you!" appears 5.40, stays to 6.62 (1.2 s) |
| 6.62 cut; 6.54-7.24 | "or more casually," | red tag "MORE CASUAL", fist bump at a skate park |
| 7.66-8.48 | "hey good to meet you." | yellow "Hey, good to meet you!" 7.63-9.45 (1.8 s) |
| 9.45 cut; 9.42-10.50 | "So if your textbook says," | black "So if your textbook says..." over picture 1 |
| loop 10.84 | "how do you do? Hardly anyone says that anymore." | back to frame 0 |

Heard text = unit text, word for word. Whisper joined the junction into one sentence: "So if your textbook says, how do you do?" - the loop works by ear (about 0.3 s between "says" and "How").

### cats-and-dogs (11.80 s)

| Time | Heard | On screen |
|---|---|---|
| 0.00-1.46 | "It's raining cats and dogs," | From frame 0: "TEXTBOOK: ~~raining cats and dogs~~", yellow "Hardly anyone says that!", blue badge. Boy under a red umbrella, cats and dogs falling. |
| 1.74-3.16 | "hardly anyone says that anymore." | same |
| 3.68 cut; 3.72-5.22 | "It mostly lives on in textbooks." | "It lives on in textbooks!" + badge. Bored boy over a cobwebbed book. |
| 5.85 cut; 5.86-6.40 | "People say," | red tag "REAL ENGLISH", soaked, cross boy in the rain |
| 6.58-7.16 | "it's pouring," | yellow "It's pouring!" appears 6.70, stays to 7.75 (1.05 s) |
| 7.75 cut; 7.64-8.16 | "or just," | red tag "OR JUST", boy pointing at a rainy window |
| 8.46-9.52 | "it's really coming down." | yellow "It's really coming down!" 8.50-10.45 (1.95 s) |
| 10.45 cut; 10.40-11.50 | "So if your textbook says," | black "So if your textbook says..." over picture 1 |
| loop 11.72 | "it's raining cats and dogs, hardly anyone says that anymore." | back to frame 0 |

Heard text = unit text, word for word. Loop junction heard as one sentence.

### Checklist

| Check | how-do-you-do | cats-and-dogs |
|---|---|---|
| Render >= 1440 short side | pass (1440x2560) | pass (1440x2560) |
| Hook in the first 1-2 s, no intro, no dead air | pass: phrase + verdict on screen at frame 0, voice at 0.00 | pass |
| Text boxes cover no face | pass | pass (the yellow box covers falling cats at the top of picture 1, not the boy) |
| Every phrase readable in time | pass; "Nice to meet you!" 1.2 s is tight but spoken and familiar | pass; "It's pouring!" 1.05 s is the tightest card in the batch (see notes) |
| Heard = unit text | pass | pass |
| Spelled-out word | none | none |
| Claim true to the unit | pass: voice "Hardly anyone says that anymore", card "Hardly anyone says that!"; never "nobody" | pass: same; voice "mostly lives on in textbooks" |
| Loop junction | pass by ear; picture 1 returns at the same position, only the box changes | pass, same |
| Stray text / watermark in pictures | none found (books are blank, only cobwebs); only the official channel logo, small, left edge, from 2.0 s | none found |
| Magnifying glass | none in any picture | none |
| Picture matches the words | pass on all 4 beats | pass on all 4 beats; the cats-and-dogs picture is the best hook image of the two |
| Self-test moment | none (by format) | none (by format) |
| Subscribe + bell animation | absent ON PURPOSE (user's open question of 2026-10-11 in `/workspace/glottos-auto/out/analytics/ask-user.md`); no `subscribe_at` in the YouTube JSON for the same reason. Noted, not a blocker. | same |

Not checked: the loop was not pixel-measured (first/last frame compared by eye only); the video was not viewed on a real phone; YouTube's own UI overlay (title, buttons on the right, the channel row at the bottom) was not simulated; the fact claims were judged against the dictionary labels quoted in the language-editor notes, not re-researched.

## 3. Pain -> what the video gives -> gap

**how-do-you-do.** Gives: "How do you do?" is dated; say "Nice to meet you" or, casually, "Hey, good to meet you". Gap: "Nice to meet you" is page 1 of every beginner course. A B1-B2 learner already says it and almost never says "How do you do?", so for most of the audience this confirms what they do instead of changing it. The only new thing is the casual line. Also missing: what to do when someone says "How do you do?" TO me (the real moment of panic with this phrase); the description mentions formal use, the video does not.

**cats-and-dogs.** Gives: the famous school idiom is dated; say "It's pouring" or "It's really coming down". Gap: small. Both swaps are short, natural and probably new at B1. This is the one that matches the pain exactly ("we dont get to learn them from schools or textbooks").

## 4. Second-by-second: where I would swipe

how-do-you-do
- 0.0-2.8: I stay. I know this phrase from school and the narrator is rude about it; the old man in a top hat makes the point without reading.
- 2.8-4.5: I stay; funny picture, the blue badge promises the answer.
- 4.6-6.6: **swipe risk.** The answer is "Nice to meet you". I knew that. The promise "what people really say" pays out with something I already have. A learner who feels cheated leaves here.
- 6.6-9.4: the casual line is the real value, but it comes after the disappointment.
- 9.4-10.8: no reason to leave before the loop; no reason to watch the loop twice either.

cats-and-dogs
- 0.0-3.7: I stay. Strong picture, a phrase every learner knows, and an opinion that surprises me (I thought it was a cool idiom).
- 3.7-5.8: I stay; 2.1 s on one line is the slowest stretch of the video but still short.
- 5.9-7.7: payoff, new phrase. It is gone after 1.05 s; I would let the loop run again to catch it (good for the retention test, slightly bad for learning).
- 7.7-10.4: second new phrase, enough time.
- no swipe point found.

## 5. Takeaway test

- how-do-you-do: "When I meet someone informally, say 'Hey, good to meet you'." Nameable, but small; the main swap is already known.
- cats-and-dogs: "Next time it rains hard, say 'It's pouring' instead of 'It's raining cats and dogs'." Clear and new.

## 6. Retention risks

- Length vs content is right in both: 4 facts in 11 s, no filler, no intro, no closing question.
- Voice at speed 1.15 is fast for B1 but every spoken line is also on screen; the two "why" lines at 1.0 are comfortable.
- how-do-you-do pays the "Next: what people really say" promise with a phrase the viewer already knows (4.6-6.6 s). This is the biggest retention risk of the batch and it is in the content, not the build.
- The payoff cards are the shortest cards in both videos (1.2 s and 1.05 s), while the opinion card gets 2.8-3.7 s. The thing worth remembering gets the least screen time.
- The 0.85-1.0 s of red tag alone before each phrase is fine as a beat of suspense.

## 7. Trust risks

- "Hardly anyone says that anymore" about "raining cats and dogs" is the strong end of what dictionaries say ("old-fashioned"). Native speakers will write "I say this all the time". The voice says "hardly anyone" and "mostly", the description adds "Native speakers still understand the idiom; it just sounds old-fashioned", so it is defensible; expect the comments and answer them.
- The card "It lives on in textbooks!" drops the "mostly" that the voice keeps. With the sound off the claim is a little harder than the unit's speech. Small.
- "How do you do?" is still correct in very formal introductions; only the description says so. A learner who watches without reading the description may think it is wrong, not just dated. Small, and the title wording ("Still Saying") already avoids "stop".
- English on every card and in every line is natural. No picture contradicts the words.

## 8. Non-blocking notes (with unit-JSON fixes)

1. **cats-and-dogs, 6.70-7.75: "It's pouring!" is on screen 1.05 s.** Readable (two words, spoken at the same moment), so not a blocker, but it is the payoff and the shortest card. Fix: beat 3 add `"tail": 0.4` (video becomes about 12.2 s).
2. **how-do-you-do, 5.40-6.62: "Nice to meet you!" is on screen 1.2 s.** Same point. Fix: beat 3 add `"tail": 0.3`.
3. **Both, the top bar, whole video: the red strike line runs through the middle of small yellow letters** ("raining cats and dogs" is about 45 px high at 1440). Legible on a still frame and the phrase is spoken at 0.0 s, so not a blocker; with the sound off on a small phone it is the hardest text in the video. Fix is in the build, not the unit (`shorts/build_first_frame.py`: thinner or semi-transparent strike line, or a larger `wrong` font); new production only.
4. **cats-and-dogs, beat 2 card (3.68-5.85): "It lives on in textbooks!" without "mostly".** Fix: `card.headline` -> "It mostly lives on in textbooks!" if it fits `sub_maxw` 820 on three lines; needs the language-editor's gate again because it changes approved text. Optional.
5. **how-do-you-do, beats 3 and 4: the second person is cut by the right frame edge** (half a face at 4.55-6.62, a sliver of a face at 6.62-9.45). The main character and the handshake / fist bump read clearly; cosmetic. `picture_shift` is vertical and cannot fix it; visuals, new production only.
6. **cats-and-dogs, picture 1: plain brown band behind the text boxes** (already known to the lab). From the viewer's side it looks like a deliberate backdrop; the yellow box hides a few falling cats, the boy's face is clear. No action.
7. **cats-and-dogs, beat 4 (7.75-10.45): the channel logo sits right at the boy's pointing fingertip**, so he seems to point at the logo. Harmless, slightly odd.
8. **No subscribe + bell animation and no `subscribe_at`** in either `content/youtube/*.json`: on purpose, pending the user's answer. If the user says the rule applies to 10-second loops too, both videos are unfinished by that rule.
9. **Progress bar has 4 segments for 5 beats** (all four are full during the loop line). Nobody will notice.

## 9. Top 3 fixes by impact

1. **scenario-writer (next units of the lane, not a re-render of this one):** choose textbook phrases where the "real" phrase is NEW to a B1-B2 learner. cats-and-dogs passes this test, how-do-you-do does not ("Nice to meet you" is already known). For how-do-you-do the honest result may simply be lower retention at 4.6-6.6 s; read the H71 result per video, not as a pair, or the weak payoff of one will blur the test of the format.
2. **shorts-builder:** give the payoff cards more time: `"tail": 0.4` on beat 3 of cats-and-dogs, `"tail": 0.3` on beat 3 of how-do-you-do. Cheap, and it moves screen time from the opinion to the thing worth remembering.
3. **shorts-builder (build_first_frame.py, new production):** make the struck-out textbook phrase easier to read with the sound off (strike line thinner or semi-transparent, or larger `wrong` text).

## Files

- Videos: `/workspace/glottos-marketing/state/shorts/l11-textbook-how-do-you-do-v1/final.mp4`, `/workspace/glottos-marketing/state/shorts/l11-textbook-cats-and-dogs-v1/final.mp4`
- Units: `/workspace/glottos-marketing/shorts/units/l11-textbook-how-do-you-do-v1.json`, `/workspace/glottos-marketing/shorts/units/l11-textbook-cats-and-dogs-v1.json`
- YouTube text: `/workspace/glottos-marketing/content/youtube/l11-textbook-how-do-you-do-v1.json`, `/workspace/glottos-marketing/content/youtube/l11-textbook-cats-and-dogs-v1.json`
- Review frames and looped audio (temporary): `/tmp/h71/`
