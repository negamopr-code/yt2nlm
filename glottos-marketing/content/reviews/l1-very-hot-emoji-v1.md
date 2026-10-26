# Viewer-critic review: l1-very-hot-emoji-v1 (Stop Saying, EP 15, lab H11 emoji arm)

Reviewed 2026-10-04. Video: `state/shorts/l1-very-hot-emoji-v1/final.mp4` (29.23 s, 1080x1920, 30 fps).
Unit: `shorts/units/l1-very-hot-emoji-v1.json` (language-approved, hash a6e01c21f8b4063c). Pictures: `state/shorts/l1-very-hot-emoji-v1/pictures.json`.

## Verdict: PARTLY

Five correct, clearly spoken, readable replacements for "very hot" in 29 s with no technical defect, but nothing makes me recall a word, two of the five emoji pairs do not show the example I am reading, and the video never tells me which word is for weather and which is for how I feel.

## Ship-blockers: 0

- Spelled-out word check: none. Whole-file and per-beat transcripts contain no letter-by-letter word.
- No text cut off, no overlap, no watermark, logo is the channel avatar.

## Pain

Evidence is thin, same as for EP 13. There is no PROBLEM NN document for this lane. One verbatim corpus line states the pain (found in `state/corpus-glottos-niche/raw`, 2 files):

- "I can understand what you say clearly , the point is that when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"

I found no other verbatim line about "very + adjective" and I am not inventing any. No NotebookLM query was spent.

Pain in the learner's words: "I say the same words all the time".
Solved would mean: tomorrow, when it is hot, I say or write "It's boiling in here" / "I'm roasting in this sweater" instead of "very hot", and I still remember it.

Pain -> what the video gives -> gap:
- Gives: 5 words, each said twice (alone, then in a phrase), one phrase on screen, one emoji pair.
- Gap 1: no recall moment. I never have to produce a word. The CTA is the only nudge.
- Gap 2: the examples are fragments ("boiling in this small room", "baking outside today"). The language note says "(I am) boiling", "(it is) baking", but the viewer does not see that. A B1 learner cannot tell whether I am boiling, the room is boiling, or it is boiling. That is exactly what they need in order to say it tomorrow.
- Gap 3: no register hint. Boiling/baking/roasting are informal speech; scorching/sweltering are weather words. Not wrong, just not given.

## What is heard (faster-whisper small.en, word timings; silencedetect for beat edges)

| t (s) | heard | note |
|---|---|---|
| 0.00-1.27 | Stop saying very hot. | clear |
| 2.07-3.54 | Here are five better words. | clear |
| 4.34-4.84 | Boiling. | clear |
| 6.15-7.40 | Boiling in this small room. | clear in the full file. The isolated clip `b02-1.wav` transcribes as "viling" - recogniser artefact on a 1.3 s clip, the full-file pass hears "Boiling". Not an audio fault. |
| 8.57-9.21 | Scorching. | clear |
| 10.54-11.76 | A scorching summer day. | clear |
| 12.92-13.63 | Sweltering. | clear |
| 14.88-16.43 | The sweltering heat of the city. | clear |
| 17.56-18.14 | Baking. | clear |
| 19.40-20.71 | Baking outside today. | clear |
| 21.84-22.48 | Roasting. | clear |
| 23.70-24.89 | Roasting in this sweater. | clear |
| 26.04-27.47 | Which one will you use today? | clear |
| 27.47-29.23 | silence, CTA card held | 1.8 s |

All 13 clips match the approved text word for word. Level: mean -26.9 dB, peak -3.7 dB. Mean is low because 16 of 29 s is silence, the speech itself is not quiet.

## What is seen (16 frames at 360 px + 10 top-half frames at 400 px)

- 0.0-1.3 s: "Stop saying "very hot"" on from frame 1, chip "STOP SAYING - EP 15". Hook is there in the first second. PASS.
- ~1.5-2.0 s: red strike through "very hot"; "5 better words" visible from about 2.0 to about 3.7 s. Readable (better than EP 13, where it flashed for 0.4 s).
- 3.9 s: "Boiling 1/5" on screen; spoken at 4.34 s. The first better word arrives about 1.5-2 s later than in EP 13 (2.5 s). This is the price of speaking "Here are five better words."
- Each word beat: headline alone about 1.5 s, then phrase + emoji card about 2.3 s (e.g. 6.1-8.5 s). Phrase lines are two short lines at most; readable in time.
- Card changes about 0.25 s before the word is spoken. Not noticeable.
- Background: ghost copies of the five words drift behind everything. A large ghost "scorching" sits directly under the "Boiling" headline at 4.4-5.9 s, and a yellow ghost "scorchin" touches the bottom of "a scorching summer day" at 11.2 s. Text stays legible, but all five answers are visible from second 0, so there is no reveal.
- Bottom half of the frame (y > ~950 of 1920) is empty in every beat.
- CTA 26.0-29.2 s: "Which one will you use today?" + "Write it in the comments." Clean, readable.

## Emoji pairs: help or mislead?

| word | pair | verdict |
|---|---|---|
| Boiling | 1f975 hot face + 1f3e0 house | Hot face is right (a person feels hot). House is weak for "small room" but not wrong. KEEP, optional swap house -> 1f6cb (couch and lamp) or 1f6aa (door). |
| Scorching | 2600 sun + 1f3d6 beach umbrella | Reads "nice beach day", which is pleasant, not very hot. Weak but harmless: the phrase says "summer day". KEEP. Optional: 1f321 thermometer + 2600 if Sweltering gives the thermometer up. |
| Sweltering | 1f321 thermometer + 1f306 city at dusk | Matches "heat of the city" exactly. Best of the five. The humid, oppressive sense is not shown, no emoji does that without 1f975. KEEP. |
| Baking | 1f31e smiling sun face + 1f335 cactus | The smiling sun says "lovely day"; the cactus says "desert". "Baking outside today" is a complaint. Mildly misleading in tone. SWAP the sun face: 2600 + 1f3dc (desert), or 1f975 + 2600 if hot face is freed from Boiling. Low priority. |
| Roasting | 1f525 fire + 1f9e5 coat | The one to swap. Fire next to a garment reads "the coat is burning", and with the word "roasting" a learner can land on the cooking/fire meaning. The text says sweater, the picture is a coat (Unicode has no sweater emoji). SWAP to 1f975 (hot face) + 1f9e5 (coat), or 1f613 (downcast face with sweat) + 1f9e5 if hot face stays on Boiling. Optionally 1f9e3 (scarf) instead of the coat. |

Summary: one pair worth swapping before publishing (Roasting), one optional (Baking). None is a blocker. Note for H11: a swap changes this arm only, so it does not break the comparison, but do it before the twin is built, not after publishing.

## Second-by-second swipe risk

- 0.0-1.3 s: I stop. "very hot" is my phrase.
- 1.3-4.3 s: 3 s with no new word ("Here are five better words" + two 0.8 s gaps). First swipe point.
- 4.8-6.15 s and every beat after: 1.2-1.3 s of silence after the word, then about 1.1-1.2 s after the phrase. 13 gaps, about 16 s of silence in 29 s. No music, no sound effect. By word 3 (13 s) the rhythm is fully predictable; second swipe point.
- 17.6-21.8 s (Baking): the smiling sun and a cactus; the weakest picture, nothing new in the pattern.
- 26.0-29.2 s: CTA, then 1.8 s of silent hold. Fine for a loop.

## Takeaway test

One action: next time I want to say "very hot", say "boiling" (or "roasting in this sweater"). I can name it, so PARTLY, not DOESN'T. I cannot say with confidence "I'm boiling" vs "it's boiling", because the video showed me neither.

## Retention risks

- 55% of the runtime is silence with a static card. The pause is meant for repeating, but nothing on screen says "say it".
- First better word at 4.3 s instead of 2.5 s.
- Identical beat shape five times, no change at any point.
- All answers visible in the background from the first frame.

## Trust risks

- None on facts: all five mean very hot, phrases are natural.
- Fragments without a subject (see Gap 2).
- "sweater" in text, coat in picture.
- "Boiling" and "baking" and "roasting" all have a literal cooking meaning; the fire emoji is the only place where the picture pushes toward the wrong one.

## Top 3 fixes

1. visuals: swap Roasting to 1f975 + 1f9e5 (or 1f613 + 1f9e5), and Baking's 1f31e to 2600 + 1f3dc. Then Boiling takes 1f613/1f975 + 1f6cb so no face repeats.
2. scenario-writer (next episode, keep the H11 pair identical): full sentences that show who is hot - "I'm boiling in this small room", "It's baking outside today", "I'm roasting in this sweater".
3. shorts-builder: cut the post-word pause from 1.0 s to about 0.6 s and drop or shorten the ghost-word backdrop behind the headline; optionally a one-card recap of the five words before the CTA so the question "which one" can be answered without rewatching.

## Checked / not checked

- Checked: whole-file transcript and all 13 per-beat clips; silences; 26 frames; unit text vs audio; emoji code points vs meaning.
- Not checked: the H11 whiteboard twin (not built); playback on a real phone; pain evidence beyond one corpus grep; no NotebookLM query.
