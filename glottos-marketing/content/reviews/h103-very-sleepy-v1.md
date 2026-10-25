# Viewer-critic review: h103-very-sleepy-v1 (lab H103 arm b: "Did you know" hook + real Pixabay stock footage)

Reviewed 2026-10-25. File: state/shorts/h103-very-sleepy-v1/final.mp4 (same md5 19eb49a8... as /workspace/glottos-auto/out/h103-very-sleepy-v1.mp4). It is 1440x2560, 30 fps, 21.5 s, Kokoro am_michael at 1.05, no music. Meta: content/youtube/h103-very-sleepy-v1.json, with "subscribe_at": [12.5].
Pain evidence: I spent no NotebookLM query. There is no learner quote about "very" on file (the same gap as the pretty/tasty reviews), so I quote none. Pain (from the brief): "I always say 'very sleepy'; give me better words." Solved means that tomorrow I can say "I feel drowsy / I'm exhausted / I feel groggy" in the right situation.

## Verdict: PARTLY. Do not ship as is.
The words are correct, the drowsy and groggy footage fits, and I can use the words tomorrow. But the subscribe animation is missing, even though the meta claims it is at 12.5 s, and the "exhausted" footage shows a relaxed woman on her phone, not someone who is worn out.

## Ship blockers
1. **The subscribe and bell animation is MISSING.** I scanned every frame at 4 fps for the red pill. The only red is the strike line (2.75-4.0 s and 21.0 s), and there is no bell. The sibling h103-very-pretty-v1 has the pill at 14 s. The sleepy meta still says `"subscribe_at": [12.5]`, which is a false record. Owner: shorts-builder. Run shorts/subscribe_anim.py in the second half, re-render, and re-record the time.
2. (Arm validity, not a hard blocker) The **"exhausted" footage contradicts the words.** The voice says "She worked all day. She is exhausted." The picture (pixabay 233390) shows a calm, slightly smiling woman texting in warm lamp light. There is no tiredness. Owner: visuals/footage. Pick a clip of someone slumped at a desk or dropping onto a sofa.

Checked and OK:
- Nothing is spelled out. Whisper heard drowsy 4.26, exhausted 8.32, groggy 12.98 as whole words. "Ana" is heard as "Anna", which is fine.
- No watermark on the footage. No magnifying glass.
- POLICY: none. In "exhausted" the woman wears an everyday camisole, and in "groggy" the woman is clothed in bed. Neither is suggestive.
- The language is correct (approved by the language editor).

## Footage vs words
| Beat | Spoken | Footage | Match |
|---|---|---|---|
| Drowsy 3.9-7.6 | "Ana yawns at night. She feels drowsy." | A woman yawns, hand over her mouth, dark background (44647) | YES. The yawn is exactly what is said. Clearest beat. |
| Exhausted 8.3-11.8 | "She worked all day. She is exhausted." | A relaxed woman texting in warm light (233390) | NO. It shows no exhaustion and no work. It reads as "evening on the phone". |
| Groggy 13.0-16.1 | "She wakes up slowly. She feels groggy." | A woman in bed, eyes half open, rubbing her head (151295) | YES, mostly. It reads as half-awake. |

Compared with the drawn arm: the real faces make drowsy and groggy feel more real and emotional. When the footage is wrong (exhausted), it is more convincing in the wrong direction than a drawing would be.

## Second by second
- 0.0: frame 0 shows only "Did you know there are better words than". "very sleepy" draws in by about 0.7 s, so the problem is not on screen in the first frame.
- 2.5-3.2: a 0.6 s gap, then "Here are three". The strike on "very sleepy" is fine.
- 3.9-4.3: the "Drowsy" headline shows with no picture. The picture lands by about 4.5 s. The same lag happens at 8.3-9.5 (Exhausted) and 13.0-13.4 (Groggy), so the word is spoken over an empty card.
- 5.2-6.2, 9.6-10.5, 13.8-14.7: the story line is spoken, but the screen shows the payoff line. "Ana yawns at night" etc. never appear on screen, so the text and the voice disagree (the same as pretty).
- 7.55-8.44, 11.88-12.80, 16.14-17.05: about 0.9 s silent holds. That is better than pretty (1.0-1.5 s), but these are still swipe points.
- 19.35-21.5: a 2.15 s silent tail on "Comment yours!". This is the most likely swipe-away and it hurts the loop. The loop card (21.0) comes back already struck, so it does not match frame 0.

## Takeaway test
I can say "I feel drowsy" (before sleep), "I'm exhausted" (after hard work) and "I feel groggy" (just woke up) tomorrow. The examples carry the nuance, but it is never stated, and the wrong exhausted clip weakens that nuance. There is no moment where I test myself ("which word: you just woke up?"), only a "comment yours" CTA.

## Retention / trust risks
- 21.5 s for 3 words. Without the silences it would be about 16 s. The arm comparison with the drawn arm is fair only if the length and holds match.
- The text is easy to read (big yellow headline, white subline).
- The texture words in the background ("exhaust..." cut off at the edge) are busy but readable as decoration.

## Top 3 fixes
1. shorts-builder: add the subscribe animation (second half, about 12-15 s) and make the meta true. Cut the holds to 0.4 s and the tail to 0.5 s. Show "very sleepy" at frame 0.
2. visuals/footage: replace the "exhausted" clip with visibly tired-after-work footage. Get the footage on screen at the moment the word is spoken, not 0.4-1.2 s later.
3. scenario-writer/shorts-builder: show the story line on screen while it is spoken (or drop it), and end with a 1-line self-test ("Just woke up: drowsy or groggy?") instead of a silent CTA.
