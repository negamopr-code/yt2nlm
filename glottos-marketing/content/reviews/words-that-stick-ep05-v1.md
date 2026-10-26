# Viewer-critic review: words-that-stick-ep05-v1 (Words That Stick #5 "The 15-minute routine")

- Video: `content/episodes/E5/e5-v1.mp4` (1440x2560, 30 fps, 62.8 s). Unit: `shorts/units/ep05_v1.json`. Script: `content/articles/p01-ep05-audio-script.md`. Format: `content/articles/p01-ep05-format.md`. Article §6 of `content/articles/p01-why-you-forget-new-words.md`.
- Pain source: NotebookLM source 60678678 "PROBLEM 01 — synthesis" (read with `source content`, free; no query used).
- Checked: 25 frames (0.2/0.8/1.4 s hook, every beat midpoint, the quiz pause and reveal, the subscribe window, the end card) plus 720-px crops of the three routine panels; the source infographic `state/nlm-raw/ep05-infographic.png`; a faster-whisper small.en transcript of the final mp4 with word timings; silencedetect (-45 dB, 0.7 s); `content/youtube/ep05.json` for `subscribe_at`.
- Not checked: loudness/mix by ear, a real phone with the YouTube UI overlay, the site page content (the unit says HTTP 200 on 2026-10-26).

## Verdict: PARTLY
The three steps of the routine are there and a viewer could try them tomorrow. But the hook isn't my problem, the "Speak" panel has lost its label, the hook card shows literal asterisks, and the recall picture is full of fake words. A third of the video is "never give up" synonyms that are never linked to the routine, and the voice ends on an abstract line instead of the action.

## Ship-blockers (4)
1. **Literal asterisks, 0.0–6.3 s.** The hook card sub reads `The routine that makes words *stick*`, with the asterisks visible on the very first frame. (Unit beat 0 `sub`. The emphasis markup is not rendered in `sub`, only in `headline`.) Owner: shorts-builder (render the emphasis in `sub`) or scenario-writer (remove the asterisks).
2. **The "Speak" panel is cropped, 17.1–23.0 s.** The panel 3 crop shows only the sofa picture. The label `10-15 min · Speak / Say two new sentences out loud with each word.` is in the source PNG but is cut off below the crop. So the third step of the routine has no text on screen, and someone scrolling with the sound off doesn't get step 3. Owner: visuals (fix the panel 3 split so it includes the label strip, without the "Gemini Notebook" watermark at the bottom right).
3. **Fake words in the Recall picture, 12.2–17.0 s.** The notebook in panel 2 shows "boncord", "texas", "un-valized", "protyze", "pomion" and "defin defin defin". On a vocabulary channel, non-words shown during "test your recall" hurt trust. Owner: visuals (regenerate or blur the word list, or crop to the hand and the label only).
4. **Subscribe animation is not recorded, and it lands on the only test moment.** `content/youtube/ep05.json` has no `"subscribe_at": [46.5]`, so by the house rule the video is not finished. Also, the 46.5–51.5 s animation sits exactly on the 1.5 s "your turn" pause (46.46–48.03 s silence) and the obstinate reveal: the countdown "2" and the SUBSCRIBE button compete for the learner's single self-test. Owner: shorts-builder (move it to about 53 s, over the "Tomorrow" card, and record it in the meta).

Spelled-out words: none (the transcript has no letter-by-letter tokens). POLICY: none found. The donkey is pulled on a rope by a cartoon farmer, which is harmless. No watermark or wrong logo in any frame. The logo is the channel avatar.

## Pain → what the video gives → gap
Learner quotes (verbatim, synthesis §3):
- "I can understand 100% of the video, but when I try to speak, my mind goes blank"
- "I mostly avoid communicating in a crowd because I dont remember the words. dont know how to make phrases."
- "confidence on talking I forgetting everything as soon as I start talking 😢!"
- "when I start to talk in English I stock up for what i saying hahaha evry words starting forget"
- "when I try to speak I forgot every sentence in my mind !! My mind became blank ..."
- "I can write paragraphs in English without any difficulty but as soon as i speak my mind just shuts down"
- "if I try to open my mouth for speak english, its blank. I don't have any idea what i said next"
- Gap table: Anki "feels like a chore; cards teach words in isolation". Streak myth: "5-min app streak = fluency".

**The pain in one sentence:** "I learn words, but when I start to talk they're gone and I don't know how to make phrases."
**What "solved" means tomorrow:** I take 3 new words, write one sentence about my life with each, cover them and say them back, then say sentences out loud. I do it once a day, for 15 minutes.

| Pain | Video gives | Gap |
|---|---|---|
| "evry words starting forget" | 3 blocks: anchor (8–12 s), recall (12–17 s), speak (17–23 s) | Good and quick. But the recall step ("Cover the word and guess it out loud") never says what I look at while the word is covered. The panel's "Cover the *stronger* word" assumes a very X → stronger-word list that this episode never shows (the "very angry → livid" example was cut). |
| "dont know how to make phrases" | "writing a real-life sentence for each one" | Said once, in 4 s. No example sentence is heard or shown. |
| "my mind goes blank" when I speak | "Say sentences out loud like you're just chatting with a friend" | Fine. But the link to the blank mind appears only as a grey teaser line on the end card. |
| App fatigue | "No streaks. No flashcards." (27.8–32.4 s) | Good, but only for viewers who already use apps. It's the hook too, which narrows who stops. |
| Something to do | Card "Tomorrow: 3 words, 15 minutes" (52.7–56.7 s) | Text only. The voice says something else at that moment ("mastering a language isn't about protecting an app streak"). |

## Second by second (final-video times)
| Time | Heard | Seen | Viewer reaction |
|---|---|---|---|
| 0.0–6.2 | "Ditch the endless digital streaks for a simple analogue habit that makes vocabulary stick. Using just three words a day." | Text card "15 minutes a day. No app." + "*stick*" with literal asterisks | The voice opens on apps, not on my pain (forgetting, blanking). "Ditch", "streaks" and "analogue" are three hard words in the first 2 s for a B1 listener. A learner without an app streak thinks "not me". **Swipe risk 0–2 s.** There's no picture, just a text card on cream. |
| 6.3–7.9 | "The three block method." | Card "The 3-block method / anchor · recall · speak" | OK, quick. |
| 7.9–12.2 | "0 to 5, anchor your words by writing a real-life sentence for each one." | Panel 1, man writing, "0-5 min · Anchor" | Good sync. "0 to 5" without "minutes" is unclear for a second (the "minutes" word was cut). |
| 12.2–17.0 | "Then minutes 5 to 10, test your recall. Cover the word and guess it out loud." | Panel 2, hand on a notebook of fake words | Guess from what? Unclear. The fake words are visible if you look. |
| 17.1–23.0 | "Finally minutes 10 to 15, speak. Say sentences out loud like you're just chatting with a friend." | Panel 3, sofa picture only, **no label** | Sound-off viewers lose step 3. |
| 23.0–27.7 | "Why just three words? Well, because true retention is about depth, not breadth." | Card "3 new words a day / Depth, not breadth." | "Retention" and "depth, not breadth" sound like a slogan. A B1 listener won't parse "breadth". **Swipe risk.** |
| 27.7–32.4 | "There are no flashcards to manage and no streaks to protect. Just do this once a day." | Card "No streaks. No flashcards. / Just once a day." | Repeats the hook. 10 s of text cards in a row (23–32 s), with no picture. **Highest swipe point around 25–30 s.** |
| 32.4–33.6 | "Picture these scenes." | Card "5 ways to say never give up" | A topic change with no bridge (the "Just keep going" line was cut). Why are we doing synonyms in a routine video? |
| 33.6–44.0 | runner/keep going, girl+bike/determined, dog+toy/tenacious, waves/relentless | One picture card each, word printed | Nice pictures, good sync. But they're small (about 20 % of the frame height, lower 40 % of the screen empty), and the word is shown before it's spoken, so there's no guessing. Tenacious and relentless are C1 words. |
| 44.0–48.0 | "And a donkey that literally won't move?" + 1.5 s silence | "A donkey that won't move / Your turn: the good kind or the bad kind?" + countdown, **plus the SUBSCRIBE animation** from 46.5 | The only self-test, and it's 1.5 s with a subscribe button popping up on it. |
| 48.0–52.6 | "Obstinate. Obstinate is the bad kind of never giving up. It's just being stubborn." | Donkey card "obstinate" | The best language moment: a clear register point. |
| 52.7–56.7 | "Ultimately, mastering a language isn't about protecting an app streak." | Card "Tomorrow: 3 words, 15 minutes / Save this routine." | The voice and the card say different things. The action is text only, for 4 s. |
| 56.7–62.8 | "It's about deliberately anchoring, recalling, and speaking real words in the real world." | End card, URL + "Next: why your mind goes blank" in small grey type | Abstract wrap-up. No spoken CTA and no spoken teaser. The teaser is the most "my problem" line in the video, and it's grey 30-px text at the very end. |

## Takeaway test
Action I can name: "Tomorrow, pick 3 words, write one real-life sentence each, cover them and say them, then chat them out loud. 15 minutes, once a day." I can name it, but only by putting the panels and the card together. It is never said in one sentence, and the recall step is fuzzy.

## Retention risks
- Length (62.8 s) is right for the content, but about 20 s (32–52 s) is a synonym set with no tie to the routine.
- Text cards back to back from 23 to 33 s with no picture. The hook card has no picture either.
- The lower 40 % of every frame is empty. Panels and synonym cards are small on a phone.
- Captions are one short line, readable, and in sync. The 0.9x podcast voice is clear, and whisper made no errors.
- The hook doesn't name the learner's pain.

## Trust risks
- Fake words in the Recall picture (ship-blocker #3).
- "Depth, not breadth" and "true retention" sound like a slogan, not a fact. That's acceptable but empty.
- "Dog holding a toy" (voice) vs. a dog pulling a rope (picture): close enough.
- The panel says "Cover the stronger word", but nothing in the episode defines "stronger word". That's a small contradiction with the voice ("Cover the word").
- English: natural. "Literally" in the donkey line is used in its literal sense, which is fine.

## Top 3 fixes (by impact)
1. **visuals + shorts-builder:** fix the blockers. Re-crop panel 3 with its "10-15 min · Speak" label. Replace or blur the fake-word notebook in panel 2. Render or remove the `*stick*` asterisks. Move the subscribe animation off the quiz pause (to about 53 s) and write `"subscribe_at"` into `content/youtube/ep05.json`.
2. **scenario-writer:** bridge the synonym spin to the routine with a card at 32.4 s, e.g. "Try the routine with 3 of these", so the five words become tomorrow's 3 words. Widen the donkey pause to 3.0 s (the script asked for 3.0 s) so the "your turn" is a real test.
3. **scenario-writer + shorts-builder:** put the pain on the first frame. Make the hook card the learner's problem ("You learn words. Then they're gone." / "15 minutes a day fixes it") instead of "No app", and keep "Tomorrow: 3 words, 15 minutes" on screen for the full closing 10 s with the teaser at headline size. If an approved voice line can't be cut in, keep the voice and fix it on screen only.
