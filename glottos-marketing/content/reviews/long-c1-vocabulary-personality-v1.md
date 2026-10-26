# Viewer-critic review: long-c1-vocabulary-personality-v1 (lab H30, "C1 Advanced Vocabulary: PERSONALITY (Friendly → Affable)")

Reviewed 2026-10-13. Door Short reviewed separately: `content/reviews/l1-friendly-3-c1-words-v1.md`.
- Video: `state/shorts/long-c1-vocabulary-personality-v1/final.mp4` - 2560x1440, 30 fps, 1079.7 s (17:59.7), AAC 48 kHz mono, md5 6594ceb16677018bdc3bd6b866403c5b.
- Unit: `shorts/units/long-c1-vocabulary-personality-v1.json` (language hash bf0b9b53aeed8752). Meta: `content/youtube/long-c1-vocabulary-personality-v1.json`.

## Verdict

**SOLVES the pain on content - 1 ship blocker in the render (subscribe animation hides a word label at 2:19).**
A learner who types "c1 advanced vocabulary personality" gets what they asked for from second 0: 40 words, each tied to a plain word they already say, each with a one-line difference, an example, a self-test and a say-it-aloud turn. Nothing in the words, answers or audio is wrong. The one defect is cheap to fix.

## Pain

Evidence is thin and I say so: there is no `content/problems/` folder and no PROBLEM document for this lane (it is a search-proven lab topic, gate B). Quotes below are verbatim from the learner comment corpus (`/workspace/reports/monitor-awf/archives/youtube-comments-vol1*.md`), names removed. No NotebookLM query spent.

- "Don't use your vocabulary just because you can. Use it to be precise. There's a difference between "like", "love", "adore", "admire", and "idolize" for example."
- "Hi! Could you tell me the difference between fundamental and important?"
- "It's kind of like C1 level word blended in a B1 level sentence."
- "Well, basically, he just used some really advanced words. However, nobody in real life talks like that."
- "My own guess was that even though many natives may know these words but they don't use all these advanced words in their casual daily conversations quite often as it sounds a bit unnatural."
- "C1 listening and writing and B1-B2 speaking"
- "Hi, could you help me with speaking??? I am in c1 level of English."

Pain in the learner's words: I know "friendly" and "shy"; I want the advanced words, but I do not know the difference between them and I am afraid of sounding unnatural.
Solved means: tomorrow I can say "my boss is approachable" instead of "friendly", and I know why it is not "gregarious".

Gives: 8 plain words x 5 advanced words; the difference is in the definition itself (lethargic "how you feel, not who you are"; complacent "lazy because of success"; tenacious "the positive side of stubborn"; vain "how you look" vs conceited "what you can do"); 16 in-part quiz questions whose wrong option is a sibling from the same part (this is where the difference is really tested); 40 repeat-after-me turns; 8 final questions.
Gap: (1) register is marked on only 5 of 40 words (affable, reticent, indolent, altruistic: formal; upfront: informal). Diffident, haughty, pompous, obstinate, forthright get no "you will read this more than say it" line - exactly the fear in the quotes above. (2) The final test does not test the difference: every wrong option is from another part and usually the opposite meaning (genial / haughty, timid / blunt, upfront / vain). A B1 viewer passes it without having learned anything.

## Checks asked for

| Check | Result | Evidence |
|---|---|---|
| First advanced word on screen and spoken within 5 s | PASS | "affable" is on the card at frame 0 (sub line); heard at about 1.7-2.5 s ("Don't just say friendly, say affable.") |
| "C1 advanced vocabulary" said within 30 s | PASS | 2.98-6.32 s "This is C1 Advanced Vocabulary for Personality." |
| Render at least 1440 short side | PASS | 2560x1440 |
| Subscribe + bell at 139.3 s | VISIBLE, **but covers card text** | frames 139.5-144.3: the button sits on the label "Diffident" (fully hidden) and cuts the "I" of "Introverted". The card is on screen 138.8-144.9, so "Diffident" is readable for about 1 s in total. |
| Subscribe + bell at 948.0 s | PASS | frames 948.2-953.0 on the "Final test" title card, bottom-left, nothing under it |
| Last 20 s free for the end screen | PARTLY | No animation there. But the window from 1059.7 s holds live content: final-test question 8 runs until 1070.1 (countdown and answer reveal), the closing card is only 1070.1-1079.7 (9.5 s) and the voice speaks until 1076.3. See remark 1. |
| Music / ticks never cover the voice | PASS by measurement | whisper small.en heard 2002 of 2002 unit words in order (5 near-homophone substitutions, below); bed mean -39.7 dB against narration peaks -0.3 dB |
| No dead silence | PASS | silencedetect: no stretch quieter than -35 dB for 1.5 s anywhere in 18 min; longest gap between spoken words under 6 s |
| Spelled-out word | PASS | none in the transcript |
| Launch kit in meta | PASS | subscribe_at [139.3, 948.0] = `sub.subscribe.json`; 3 ab_thumbs files exist under `/workspace/glottos-auto/out/abtests/catalog/long-c1-vocabulary-personality-v1/`; thumbnail jpg exists; endscreen and door_shorts present |
| Wrong quiz answer | none | all 24 answer frames looked at (16 in-part + 8 final): green pill = correct word every time |
| Spoken sentence differs from card | none | word-level diff of the full transcript against the unit speech: identical except "principled" heard as "principal" (11:18) and "haughty" heard as "hardy/hearty" (below) |
| Text cut off / overlapping | none cut off | all 40 word cards (final state), 8 section cards, 16 repeat frames, closing card looked at. Crowding only: part 8 labels "Considerate Compassionate" almost touch and read as one phrase (13:54). |
| Picture fits word | 39 of 40 fine | weak one: Idle = sofa + books (reads as "reading at home", not "not wanting to work"). Good ones: vain (mirror + nail polish), pompous (top hat + monocle), complacent (medal + sleeping face), gregarious (party). |

## Ship blocker (1)

1. **2:19 (139.3-144.3 s) - subscribe animation covers the label "Diffident" and the first letter of "Introverted" on the "Instead of shy" card.** Owner: shorts-builder. Fix: re-run `shorts/subscribe_anim.py` on `final-before-anim.mp4` with the first time moved to a chapter start whose bottom-left is empty, e.g. "Speaking practice: shy" at 3:40 (the "Now say them out loud with me" card, about 220.5 s) - text there is centred in the upper half. Then copy the printed SUBSCRIBE_AT into the meta `subscribe_at`. Do not use `--corner bc` on a section card: it would cover "Timid".

## Second-by-second notes

- 0:00-0:13 I stop: my word (friendly), the better word (affable), "C1", and "40 words" in 10 s. No greeting, no channel talk. But one still card for 13.6 s is long; the promise is complete by 0:10.
- 0:13-0:20 Part card with all five words as a preview. Good map.
- 0:20-1:10 Five word cards, about 10 s each: word, then meaning, then example with the word in yellow. Text appears as it is spoken; readable in time. Cards use only the upper 55 % of the frame; the lower 45 % is black with faint drifting words. On a phone the meaning line is small for the space available.
- 1:10-1:42 Two tests. I do test myself: 3-2-1 countdown, green answer, the wrong option struck out, and a one-line reason on the fill-the-gap one ("She is important, but easy to talk to"). This is the best part of the format.
- 1:42-2:18 Repeat after me, 5 sentences, LISTEN then YOUR TURN: SAY IT, about 3 s each turn. Works; the pause is not silent (measured, not listened to).
- 2:18 The subscribe button pops over the first word of the next part (blocker).
- From 2:18 on, the same 2-minute block seven more times, same voice, same order, same card. **Swipe risk is highest at 4:11 and 6:06** (start of parts 3 and 4): by then I know the pattern and nothing new is promised. Chapters help a searcher jump; a passive viewer leaves.
- 12:48-13:50 "Haughty" (see trust risks).
- 15:47-17:50 Final test. Too easy (opposites as options), 15 s per question with no explanation. A viewer who came this far deserves a real test.
- 17:50-17:59 "Which word describes you? Write it in the comments." Clear, answerable, 3.4 s of music after the last word.

## Takeaway test

One action: next time I describe my boss, my sister or a rude passenger I pick one of the five and know why - "approachable" (important but easy to talk to), not "gregarious" (loves groups). Named without effort, so the verdict is not capped.

## Retention risks

- 18:00 of one template repeated 8 times with one synthetic voice. Disclosed; it matters. The pattern video has a human teacher talking for 27 min. Expect a steep drop after part 2. The length being under 20 min does not matter to a learner; the sameness does.
- Hook card static for 13.6 s.
- Repeat blocks re-read the same five sentences already heard twice (card, sometimes quiz). Third hearing in 2 minutes.
- Voice speed 1.0, fine. Text legibility fine at 1440; small on a phone because half the frame is empty.

## Trust risks

- **"Haughty" is heard as "hardy" / "hearty" by the speech model in 4 of 5 places** (12:48.5 headword, 12:54.9 example, 13:12.8 quiz option, 13:50.4 repeat sentence "She gave the waiter a hearty look"; only 15:59.6 came out as "haughty"). It is probably the American voice's soft t, which is legitimate, but this is a word the viewer is told to repeat after the voice. A human must listen at 12:48 before publishing. I did not listen by ear; this is a speech-model finding only.
- British spelling on the cards (neighbour), American voice. Small.
- No overclaim found. Definitions and examples are natural (language gate already passed); "idle student who never does his homework" and "an indolent worker waits to be told what to do" are a little textbook but correct.
- "C1" label: taken on trust from the language gate; I did not re-check levels. Introverted, timid, blunt, frank, vain, selfless are words many B2 learners know - a viewer may say "these are not C1".

## Non-blocking remarks for the channel owner

1. End screen: set it to the last 9 s only (closing card, from 17:50.5) and put the elements in the lower half - the closing text sits in the middle of the frame at about 45-52 % height. A 20 s end screen would sit on final-test question 8 during its countdown and answer. Better next time: hold the closing card 20 s.
2. Listen to "haughty" at 12:48.
3. Final test: use sibling words as wrong options (genial / gregarious, timid / reticent, upfront / principled). Owner: scenario-writer, next episode or a v2.
4. Add a register line to the bookish words (diffident, obstinate, haughty, pompous, forthright): "you read it more than you say it". Owner: scenario-writer + language-editor.
5. Part 8 section card: labels "Considerate Compassionate" nearly touch. Owner: visuals/shorts-builder (smaller label font when a label is 13 letters).
6. Idle picture (sofa + books) is weak. Owner: visuals.
7. The rendered file is not yet in `/workspace/glottos-auto/out/` (earlier long videos had a byte-identical copy there at review time). Check before the send step.

## Top 3 fixes by impact

1. shorts-builder: move the first subscribe animation off the "Instead of shy" card (blocker above) and update `subscribe_at`.
2. voice (human ear first): confirm or re-voice "haughty" in beats 61, 63, 64.
3. scenario-writer: final test with same-family distractors; vary the block from part 4 on (e.g. swap the repeat block for "which of the five would you use for your boss?") to break the sameness.

## What was checked and what was not

- Checked by frame: 0-145 s densely (37 frames, intro + all of part 1 + the 2:19 animation); 946-962 s (12 frames, second animation); the final state of all 40 word cards; question and answer frame of all 24 quiz beats; all 8 section cards; 2 repeat frames per part; final-test title; closing card.
- Checked by speech model: the whole 18 minutes, faster-whisper small.en with word timings, diffed word by word against the unit.
- Checked by measurement: resolution, duration, silence, levels of narration and bed.
- NOT checked: nobody listened by ear (pronunciation, tick loudness against the voice, how the pop/ding feels); intermediate states of word cards (word only, word + meaning) outside part 1; countdown frames outside part 1 and final question 1; the 3 A/B thumbnails were only checked to exist, not looked at; CEFR levels of the 40 words; YouTube-side metadata limits.
