# Viewer-critic review: h103-very-surprised-v1 (lab H103 arm b: "Did you know" hook + real Pixabay stock footage)

Reviewed 2026-10-25. File: state/shorts/h103-very-surprised-v1/final.mp4 (same md5 d4fa0733... as /workspace/glottos-auto/out/h103-very-surprised-v1.mp4). It is 1440x2560, 30 fps, 21.1 s, Kokoro am_michael at 1.05, no music. Meta: content/youtube/h103-very-surprised-v1.json, with `"subscribe_at": []`.
Pain evidence: I spent no NotebookLM query. There is no learner quote about "very surprised" on file (grep of content/ and docs/ finds only the 100-synonyms meta). This is the same gap as the sibling reviews, so I quote none. Pain (from the brief): "I always say 'very surprised'; give me better words." Solved means that tomorrow I can say "I was astonished / amazed / stunned" and pick the right one: good surprise (amazed), huge surprise (astonished), or shock that leaves me unable to react, often bad news (stunned).

## Verdict: PARTLY. Do not ship until the meta is fixed.
The three words are correct and clearly spoken, and the astonished and stunned faces are strong. But the meta does not record the subscribe time (a "not finished" rule), the "amazed" clip shows a smiling woman with no gift, and each picture lands 0.5-1.1 s after its word is spoken. The video never says how the three words differ, so tomorrow I will use them as free swaps for "very surprised".

## Ship blockers
1. **subscribe_at is not recorded.** The animation IS in the video: the red SUBSCRIBE pill and bell show from 12.5 s, turn into "SUBSCRIBED ✓" at about 14.5 s, and are gone by about 17 s. That is in the second half, so the placement is OK. state/shorts/h103-very-surprised-v1/final.subscribe.json says `[12.5]`, but content/youtube/h103-very-surprised-v1.json has `"subscribe_at": []`. Owner: shorts-builder. Copy `[12.5]` into the meta.
2. (Trust, to confirm, not a hard block) **A black circled "E" logo** sits on the wall at the left of the footage panel in both the astonished and stunned beats (pixabay 45119). It looks like a sticker on the wall, not an overlay, and it is not a NotebookLM or Gemini mark. But on a faceless brand channel it reads as somebody else's logo. Owner: visuals. Crop the clip about 15% from the left or pick a different clip.

Checked and OK:
- Nothing is spelled out. Whisper heard Astonished 4.48, Amazed 8.86 and Stunned 13.08 as whole words, and every sentence was transcribed verbatim.
- No magnifying glass. No NotebookLM watermark. Logo = the official channel avatar.
- POLICY: none. Both women are fully clothed (a long-sleeved blouse and a T-shirt), with neutral reactions and nothing suggestive. They are stock models, not named people.
- The language is correct (approved by the language editor, hash 026ad3dcaa623f0e).
- Hook: "very surprised" is NOT on screen at frame 0 (0.1 s shows only "Did you know there are better words than"). It appears by 0.5 s, so this is a minor issue.

## Footage vs words
| Beat | Spoken | Footage | Match |
|---|---|---|---|
| Astonished 4.48-7.70 | "She opens the box. She is astonished." | A woman against a wall, hands on her face, mouth open, eyes wide (45119) | YES for the emotion. There is no box, but the reaction is a textbook "astonished". This is the best beat. |
| Amazed 8.86-11.70 | "She sees the gift. She is amazed." | A blonde woman smiling at a blank picture frame, holding glasses (48019) | WEAK. She looks pleased or interested, not amazed. There is no gift. A blank frame is ambiguous. |
| Stunned 13.08-15.56 | "She hears the news. She is stunned." | The SAME woman and wall as astonished (45119 again, a later segment), with a worried, frozen look and her hands at her mouth | OK for the emotion (a shocked freeze). But a repeat of the astonished person makes the two words look like the same thing, which is the exact confusion a learner has. |

Compared with the drawn arm: the real faces sell astonished and stunned better than drawings. The amazed clip is the weakest picture in the set. The reuse of one clip for two words is a lab-arm weakness, because the footage pool was too thin.

## Second by second
- 0.0-0.5: The text "very surprised" is not yet visible. It is spoken at 1.80-2.64. A scroller who has the sound off sees a generic "Did you know..." for half a second.
- 2.64-3.32: a 0.7 s gap, then "Here are three" with the strike on "very surprised". OK.
- 4.48-5.5: "Astonished" is spoken over an empty card. The footage pops in at about 5.5 s (1.0 s late).
- 7.70-8.86: a **1.16 s silent hold**, which is a swipe point.
- 8.86-10.0: "Amazed" is said over an empty card. The picture lands at about 10.0 s (1.1 s late).
- 11.70-13.08: a **1.38 s silent hold**, the longest mid-video gap and the most likely mid-video swipe. The subscribe pill appears here (12.5) over an empty card.
- 13.08-13.5: "Stunned" plus an empty card. The picture lands about 0.4 s late. The subscribe pill overlaps the bottom-left of the clip until about 17 s and does not cover her face.
- 5.58-6.52, 9.80-10.68, 13.60-14.62: the story line ("She opens the box", etc.) is spoken but never shown. The screen shows only the payoff line, so text and voice disagree for about 1 s per beat.
- 15.56-16.66: a 1.1 s silent hold.
- 18.64-21.1: a **2.46 s silent tail** on "Comment yours!". This is the biggest swipe risk and it hurts the loop. The loop card (21.0) is already struck, so it does not match frame 0.

## Takeaway test
I can say "I was astonished / amazed / stunned" tomorrow instead of "very surprised". That passes, but only barely. The video gives no rule for which word to choose. "Amazed" usually means good and impressive, "stunned" means so shocked you can't move (often bad news), and "astonished" means extremely surprised. The examples hint at this (box / gift / news), but the weak amazed clip and the repeated astonished/stunned woman blur it. There is no self-test moment ("Bad news: amazed or stunned?"), only a "comment yours" CTA.

## Retention / trust risks
- 21.1 s for 3 words. Without the silences (about 6 s total of holds and tail) it would be about 15 s.
- The text is easy to read (big yellow headline, white subline, counter 1/3-3/3).
- The background word texture is busy but stays decoration. The headline is never obscured.
- The "E" wall logo is a possible third-party brand on screen (see blocker 2).
- No overclaimed facts, and the English is natural.

## Top 3 fixes (by impact)
1. **shorts-builder:** write `"subscribe_at": [12.5]` into the meta (this is the blocker). Cut the 1.1-1.4 s holds to about 0.4 s and the 2.5 s tail to about 0.5 s. Put the footage on screen AT the spoken word, not 0.4-1.1 s later. Show "very surprised" at frame 0.
2. **visuals/footage:** replace the amazed clip with someone visibly wowed, ideally by a gift or a view. Use a different person or clip for stunned so it does not look like a repeat of astonished. Crop away the "E" wall logo.
3. **scenario-writer:** give each word its 3-word nuance on screen (amazed = good wow; stunned = shocked, can't move; astonished = huge surprise). Replace "Comment yours!" with a one-line self-test ("Bad news: amazed or stunned?") so the viewer leaves knowing which word to pick.
