# Viewer-critic review: lab H69 "FILL IN THE BLANK, ANSWER HELD BACK" (Which Word Fits?), 2 Shorts

Date: 2026-10-13. Reviewer: viewer-critic (A2-B2 learner's point of view). Read-only: nothing rendered, changed or uploaded.

Videos:
- `state/shorts/l12-quiz-excited-v1/final.mp4` (1440x2560, 30 fps, 10.80 s) - with the rule line
- `state/shorts/l12-quiz-experience-v1/final.mp4` (1440x2560, 30 fps, 8.40 s) - ends on the answer

## Verdicts

| Video | Verdict | Why in one sentence |
|---|---|---|
| l12-quiz-excited-v1 | **SOLVES** | It tests me on a mistake learners in our own corpus make every day ("I'm so exciting"), shows the right word, and the last card gives me a pair I can copy tomorrow: the trip is exciting, I am excited. |
| l12-quiz-experience-v1 | **PARTLY** | I get one correct, useful sentence for a CV or interview, but the quiz is too easy to feel like a test, nothing says what "experiment" means, and the corpus has no learner who mixes these two words. |

**SHIP BLOCKERS: 1** (experience: the channel logo sits on the main character's face for 3 seconds). 0 in excited.
No word is spelled letter by letter in either video. Both renders are 1440 on the short side.

## 1. The pain (learner corpus, verbatim, no names)

There is no `content/problems/` document for this lab lane (the folder does not exist), so quotes come straight from `/workspace/reports/monitor-awf/archives/youtube-comments-vol*.md`. No NotebookLM query was spent.

excited / exciting - the mistake is live in the comments, and learners ask about it:
- "i am so exciting to write this comment for you."
- "I was so exciting about that lesson"
- "I'm so exciting to  learn it."
- "Complete the series bro , I am exciting  to see the rest"
- "I'm exciting when I watch your video. I feel excited. right?"
- "I did feel a lot of excited because I was understanding the more than I believed"
- "Thank you so much for this interesting lesson! I all the time confused [ bored and boring]!!!"
- "finally finally I understand the difference between ed and ing adjectives"
- "i m boring means u r bored.. so who is you in this sentense? I am or u r?? Who get bored??"

experience / experiment - **no quote found.** About 120 comments use "experience" about work or study and use the word correctly; none uses "experiment" in its place and none asks about the pair. The nearest real mistakes are about the pattern, not the word: "I've already got one-year experience of listening", "with many years experience". So this pain is assumed (it is a known false friend for some first languages), not shown by our learners.

Pain in the learner's words: "I write 'I'm so exciting' and I don't know why it is wrong - who is bored, who is boring?"
"Solved" means: tomorrow I write "I'm excited about ..." for my feeling and "it is exciting" for the thing, without stopping to think.

## 2. What is seen and heard

Heard with `state/shorts/h68/hear.py` (small.en and base.en) plus small.en word timings on the audio played twice in a row. Frames taken with moviepy at 0.0, 0.5, 1.0, 1.5, 1.9, 2.5, 3.2, 4.0, 4.5, 4.9, 5.3, 6.0, 7.5 and the end; the moments the choice boxes appear were measured frame by frame. Audio mean -18.1 dB, peak -1.3 / -1.4 dB; the 1.5 s without voice is not silent (ticks, about -33 dB).

### excited (10.80 s)

| Time | Heard | On screen |
|---|---|---|
| 0.00-1.84 | "I'm so blank about my trip to Japan." | From frame 0: yellow box "I'm so _____ about my trip to Japan!", full yellow bar. Boy jumping in an airport, passport in his hand, red suitcase, plane. No choices yet. |
| 2.32-3.58 | "Exciting, excited, or excite?" | A appears 2.13, B 2.67, C 3.17; bar runs down from about 1.9; logo tile from 2.0 |
| 3.58-5.13 | ticks only | all three choices on screen (1.96 s with all three visible) |
| 5.13 cut; 5.16-7.64 | "Excited! I'm so excited about my trip to Japan." | new picture (boy in a plane seat, snowy mountain in the window); box B green, A and C grey; sentence whole with "excited" green and underlined |
| 8.27 cut; 8.38-10.04 | "The trip is exciting. I am excited." | new picture (boy, red gate, cherry blossom); red tag REMEMBER + yellow box with the same words, both key words green |
| loop 10.84 | "I'm so blank about my trip to Japan." | back to frame 0 |

### experience (8.40 s)

| Time | Heard | On screen |
|---|---|---|
| 0.00-1.70 | "I have five years of blank in sales." | From frame 0: yellow box "I have five years of _____ in sales.", full bar. Boy in a jacket and tie pointing at himself, an interviewer with a sheet of paper. No choices yet. |
| 2.10-3.78 | "Experiment, experience, or expedition?" | A appears 2.03, B 2.77, C 3.47; bar runs down; logo tile from 2.0 **on the boy's cheek** |
| 3.78-5.03 | ticks only | all three choices on screen (1.56 s with all three visible) |
| 5.03 cut; about 5.1-7.6 | "Experience! I have five years of experience in sales." | new picture (boy hands a paper bag to a customer, cash register); B green, A and C grey; sentence whole, "experience" green and underlined |
| 7.6-8.4 | tail | same |
| loop 8.40 | "I have five years of blank in sales." | back to frame 0 |

Heard text = unit text in both, word for word (whisper printed "Trip is exciting" without "The" on the looped pass and garbled the second pass of experience; the single pass of each file is clean, so this is the recogniser, not the voice).

### Checklist

| Check | excited | experience |
|---|---|---|
| Render >= 1440 short side | pass (1440x2560) | pass (1440x2560) |
| Question understood with the sound off at frame 0 | pass: a sentence with a thick gap, a matching picture | pass |
| Choices on screen at frame 0 | no - they come at 2.1-3.2 s (by design after expert round 2) | no - 2.0-3.5 s |
| Time to choose with all three visible | 1.96 s - enough for three short forms of one word | 1.56 s - tight for three long look-alike words |
| Answer clear with the sound off | pass: green box + green word in the sentence | pass |
| Exactly one right answer | pass ("excited"; the other two are impossible in the gap) | pass ("experience") |
| Heard = unit text | pass | pass |
| Spelled-out word | none | none |
| Text over a face / cut by the frame | none | **logo tile on the boy's cheek and ear 2.0-5.03 s**; the interviewer is half a face at the right edge; the push-in cuts the boy's left ear off by 4.9 s |
| Text in the Shorts UI zones | none: all text is in the top 40 % (y 170-1000 of 2560), nothing near the bottom 20 % or the right-hand buttons | same |
| Garbled text inside pictures | none (passport shows a globe and a stamp, no letters; the interviewer's sheet is blank; register keys are blank) | none |
| Magnifying glass | none | none |
| Picture matches the words | pass on all 3 beats | pass (interview, then selling) |
| Self-test moment | yes, 2.1-5.1 s | yes, 2.0-5.0 s |
| Loop seam | hard cut gate -> airport, 0.8 s of music between "excited." and "I'm so"; clean | hard cut shop -> interview, same; clean |
| Subscribe + bell animation | absent ON PURPOSE (user's open question of 2026-10-11 in `/workspace/glottos-auto/out/analytics/ask-user.md`); no `subscribe_at` in the YouTube JSON. Noted, not counted as a blocker. | same |

Not checked: the video on a real phone; YouTube's own overlay was not simulated (safe zones judged by position only); the tick and pop sounds were confirmed by level, not judged by ear; music was not judged; the loop was compared by eye and by the looped audio, not pixel-measured.

## 3. The quiz from the learner's side

**Sound off, frame 0.** I see a sentence with a hole and a happy boy with a passport. I understand "a word is missing" at once. I do not yet know it is a quiz with choices: for 2 seconds there is nothing to choose from and no label ("Which word fits?" is only in the title). I can already guess, which is fine. This costs little in excited, where the picture gives the answer away as a feeling; in experience the interview picture tells me the situation too.

**Time to choose.** The bar runs about 3.2 s, but half of it is spent showing the choices one by one. With all three on screen I have 2.0 s (excited) and 1.6 s (experience). For exciting / excited / excite that is enough. For experiment / experience / expedition, three long words that start the same, 1.6 s is short for A2; C is on screen for the shortest time. The loop gives a second look, but by then I know the answer.

**The answer.** Very clear: green box, grey losers, the word green and underlined inside the full sentence, said aloud twice. The sentence box grows from two lines to three at the reveal, so the three choice boxes jump down about 130 px - a small jolt, not a problem.

**Hearing "blank".** With the screen in front of me it is clear, because the gap is right there. But the commas in the unit did not make a pause: "so" ends at 0.40, "blank" runs 0.40-0.68, "about" starts at 0.68. By ear alone it is the fluent sentence "I'm so blank about my trip to Japan", and "blank" is a real adjective, so an A2 listener who is not reading could take it for the sentence. The same in the second video ("five years of blank in sales", no pause). Nobody watches a quiz Short without looking, so this is a note, not a blocker. The language-editor's note said this was not checked by ear; it now is: no pause.

## 4. Pain -> what the video gives -> gap

**excited.** Gives: the test on exactly the sentence learners write wrongly ("I'm so exciting ..."), the answer, and the contrast pair "The trip is exciting. I am excited." with a picture for it. Gap: the pair is an example, not a rule; I have to work out myself that it also means bored / boring, interested / interesting. For a 10-second Short that is the right size.

**experience.** Gives: the correct sentence "I have five years of experience in sales", seen and heard twice. Gap: (1) nothing tells me what "experiment" or "expedition" mean, so a learner who really mixes the words learns "B" and not why; (2) at B1 nobody is in doubt - "expedition" is a joke option and "experience" is known - so it is a quiz I pass without thinking, pleasant but not teaching; (3) the corpus does not show this confusion at all. What it does give is the pattern "years of experience in", which our commenters do get wrong ("many years experience").

## 5. Second-by-second: where I would swipe

excited
- 0.0-1.9: I stay. It is my sentence, the gap pulls. With the sound off there is a small "and now what?" until the choices come.
- 1.9-5.1: I stay and choose. The ticks keep it alive. This is the best part.
- 5.1-8.3: I stay to see if I was right. 3.1 s on the answer is a little long once I have seen the green box (the sentence is read in full a second time).
- 8.3-10.8: **small swipe risk** for those who were right - they have their reward and the REMEMBER card is "more school". For those who were wrong it is the most useful 2.5 s of the video.

experience
- 0.0-2.0: I stay.
- 2.0-5.0: I stay, but I know the answer the moment B appears (2.8 s); the remaining 2.2 s is waiting, not thinking. **Swipe risk for B1 and above at about 3.5 s:** "too easy".
- 5.0-8.4: confirmation; nothing new. No reason to watch the loop a second time.

## 6. Takeaway test

- excited: "When I talk about my feeling I write 'I'm excited about ...'; the thing is 'exciting'." Clear, and it corrects a mistake I really make.
- experience: "In my CV or interview: 'I have five years of experience in sales.'" Nameable and useful, but only for someone who did not already know it.

## 7. Retention risks

- Length vs content is right in both; no intro, no dead air, no closing question.
- Voice 1.15x is fast for A2, but every word is on screen.
- Choices are not in frame 0, so the first 2 seconds of a silent viewer are a sentence and a bar that does not move.
- experience is too easy for the B1-B2 part of the audience; easy quizzes can still get comments ("B!") but they do not hold a second loop.
- excited: the answer beat repeats the whole sentence (3.1 s); the rule card that carries the learning gets 2.5 s.
- **The test itself is blurred:** the two videos differ in the rule line AND in the word, the topic, the difficulty and the title. If excited keeps more viewers, it may be the word, not the rule line. Read H69 per video; a clean answer to "does a line after the answer help" needs the same quiz cut both ways.

## 8. Trust risks

- English is natural and correct on every card and in every line; one answer only in each quiz.
- experience: the hero is a small boy in a tie with "five years of experience in sales" - reads as a cartoon joke, harmless.
- experience: the tag "experience or experiment" promises the difference; the video only gives the answer. Small (tags are not shown).
- The unit `lane` text still says "three choices from frame 0, a silent 3-second bar"; the render has the choices from 2.0 s and ticks. Internal note only, the viewer never sees it.

## 9. Fixes

### Must fix before the user sees it (1)

1. **experience, 2.0-5.03 s: the logo tile is on the boy's cheek and ear.** The hero's face is the thing I look at while I choose, and a brand sticker sits on it for the whole thinking time. Owner: shorts-builder. Cheapest fix: `"logo_from": 5.1` in `shorts/units/l12-quiz-experience-v1.json` (on the answer picture the tile lies on the cash register, clear of any face), or a `picture_shift` on beat 1 that moves the face clear of the tile; re-render. In `build_first_frame.py` for new production: do not place the tile where a face is.

### Should fix if a re-render happens anyway (not blockers)

2. **excited, 8.27-10.8 s: the stretched bottom strip of the last picture is visible** - vertical streaks across the lowest 5-6 % of the frame (y > about 2420); the boy's legs end in two brown posts and the suitcase bottom is smeared. In the Shorts feed the channel row and title cover it, so no viewer will swipe for it; on the review card and in a paused frame it looks like a rendering fault. Owner: visuals (extend the ground properly or regenerate the picture with room under the boy), or shorts-builder (shift less).
3. **experience: give the choice 0.4-0.5 s more with all three boxes visible** (1.56 s now against 1.96 s in excited). Owner: shorts-builder (longer countdown after the last choice).

### Notes for the next batch

4. **scenario-writer: choose pairs the corpus really confuses and keep all three choices plausible.** excited / exciting is the model (same family: bored / boring, interested / interesting, "I'm boring"). experience / experiment / expedition has no evidence behind it and one option nobody would pick.
5. **scenario-writer + lab: test the rule line cleanly** - the same quiz with and without the line, not two different quizzes.
6. **voice: make the gap audible.** "blank" is spoken with no pause on either side and sounds like a word of the sentence. A real pause before and after, or a soft tone in place of the word, would be clearer for A2 ears. Needs the language-editor only if the text changes.
7. **shorts-builder: a tiny "Which word fits?" tag at frame 0** (or the first choice already visible) would tell a silent viewer in the first second that choices are coming. This goes against the expert round-2 advice to keep frame 0 to one text block, so treat it as a variant to test, not a correction.
8. **shorts-builder: keep the sentence box the same height at the reveal** (wrap the question on the same lines as the answer) so the choice boxes do not jump.
9. **experience picture 1: the interviewer is half a face at the right edge and the push-in cuts the boy's ear at the left.** Cosmetic; visuals, new production.
10. **Subscribe + bell animation and `subscribe_at` are absent on purpose**, pending the user's answer. If the user says the rule covers 10-second loops, both videos are unfinished by that rule.

## Files

- Videos: `/workspace/glottos-marketing/state/shorts/l12-quiz-excited-v1/final.mp4`, `/workspace/glottos-marketing/state/shorts/l12-quiz-experience-v1/final.mp4`
- Units: `/workspace/glottos-marketing/shorts/units/l12-quiz-excited-v1.json`, `/workspace/glottos-marketing/shorts/units/l12-quiz-experience-v1.json`
- YouTube text: `/workspace/glottos-marketing/content/youtube/l12-quiz-excited-v1.json`, `/workspace/glottos-marketing/content/youtube/l12-quiz-experience-v1.json`
- Review frames, contact sheets and looped audio (temporary): `/tmp/h69/`
