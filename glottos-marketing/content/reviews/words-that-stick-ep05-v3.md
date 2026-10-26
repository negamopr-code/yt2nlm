# Viewer-critic review: words-that-stick-ep05-v3 (Words That Stick #5 "The 15-minute routine")

- Video: `content/episodes/E5/e5-v3.mp4` (1440x2560, 30 fps, 63.30 s). Unit: `shorts/units/ep05_v3.json`. Subscribe: `content/episodes/E5/e5-v3.subscribe.json` = `[52.0]`, 5 s, bottom-left.
- Change vs v2 (unit diff checked): only the quiz pause, 3.0 -> 2.0 s (two fields), plus the id and a note. No text change.
- Previous reviews: `content/reviews/words-that-stick-ep05-v2.md` (SOLVES, narrowly) and `-v1.md` (pain quotes, PROBLEM 01). Pain evidence not re-read: the content is unchanged.
- Checked: 32 frames (hook 0.3/1.2/5 s, 3-block card, all 3 panels, the text cards at 26/30/33, every synonym at 34.5/36/39.6/40.3/43, the quiz at 45/45.8/46.1/46.3/46.5/47.5/48.4, the reveal at 49/51/52.2, subscribe/end at 53/54/56/58/60/62.5), faster-whisper small.en transcript with word timings of the final mp4, silencedetect (-45 dB, 0.7 s).
- Not checked: loudness by ear, a real phone with the YouTube UI, the site page.

## Verdict: SOLVES (narrowly, unchanged from v2)
Same content as v2, which already solved the pain: the routine (anchor / recall / speak, 3 words, 15 min) is on screen and the action card "Tomorrow: 3 words, 15 minutes" holds for the last 10 s. The shorter pause still gives a real self-test.

## Ship-blockers (video): 0
- Spelled-out words: none in the transcript.
- POLICY: none (cartoon animals and people, no real people, channel-avatar logo, no watermark).
- Every quiz "blank": n/a (no "blank" in this quiz).

## Pre-publish blocker (metadata, not the video): 1
- `content/youtube/ep05.json` still has `"subscribe_at": [53.0]` (and gate notes that describe e5-v2.mp4, 64.2 s). The v3 animation is at **52.0 s**. The :8093 card would show the wrong time. Owner: shorts-builder (or publisher) must set `subscribe_at: [52.0]` and point the meta at e5-v3.mp4 before upload. A 1-line fix; the critic does not edit it.

## Quiz pause (the only change)
- Heard: "And a donkey that literally won't move?" ends at 46.00 s. Silence 46.46 -> 48.53 s (**2.07 s**, gate limit 3 s: passes). "Obstinate." at 48.62.
- Seen: question card "A donkey that won't move / Your turn: the good kind or the bad kind?". The countdown badge shows "2" at 46.5 and "1" at 47.5 and 48.4 (no "3" anymore, which is correct for 2 s). No badge at 46.1-46.3, so it appears about 0.4 s into the silence. That's fine.
- As a learner: 2 s is enough for a good-or-bad choice (it's a binary question, not a word recall). It feels quicker but not rushed. The "Your turn" sub is small grey text. If I don't read it, I only get the cue from the voice's question. That's the same as in v2.
- Subscribe vs quiz: the animation starts at 52.0 (frame 52.2 shows SUBSCRIBE + bell). The pause ended at 48.53 and the answer ends at 52.76, so it overlaps only "It's just being stubborn". It sits bottom-left below the caption and the donkey picture, and covers no text. It changes to SUBSCRIBED + yellow bell over the Tomorrow card (54-56 s) without touching the headline or sub, and it's gone by 58 s. It is in the second half and not on the quiz. OK.

## Second by second (v3 times; identical to v2 up to 46 s, then -1 s)
| Time | Heard | Seen | Note |
|---|---|---|---|
| 0.0-4.6 | "Ditch the endless digital streaks for a simple analog habit..." | "You learn words. Then they're gone." | The card stops me. The voice is app talk with hard words. This is the main swipe risk at 1-2 s for sound-on viewers (unchanged). |
| 5.0-7.8 | "Using just three words a day. The three block method." | 3-block card | OK |
| 8.3-22.6 | anchor / recall / speak lines | 3 panels with time + label | Good sync. "Cover the stronger word" (card) vs "Cover the word" (voice). Small "ow" fragment on the panel-2 edge. |
| 23.4-32.1 | "Why just three words... depth, not breadth... no flashcards... once a day" | 2 text cards | About 9 s with no picture: a swipe risk. |
| 32.6-43.4 | "Picture these scenes" + 4 synonyms | bridge card, then 4 picture cards | Each word is printed before it's spoken (for example, "tenacious" is shown at 39.6, spoken at 40.68), so I can't guess first. Captions "the rain?" / "a toy?" end with "?" to match the scripted questioning voice. They read a bit oddly but aren't wrong. Pictures are small, and the lower 40 % of the frame is empty. |
| 44.2-48.5 | donkey question + 2.07 s silence | quiz card + 2 -> 1 | A real self-test. |
| 48.6-52.8 | "Obstinate... the bad kind of never giving up. It's just being stubborn." | donkey + "obstinate"; SUBSCRIBE from 52.0 | The best language moment. |
| 53.4-62.4 | "Ultimately... isn't about protecting an app streak... anchoring, recalling, and speaking real words in the real world." | "Tomorrow: 3 words, 15 minutes" -> "Save this routine." -> "Next: why your mind goes blank" | The action is on screen. The voice is abstract. A 0.7 s silent tail at the end. |

## Takeaway test
"Tomorrow: pick 3 words (e.g. 3 of the never-give-up words), write one sentence about my life with each, cover and say them, then say two sentences out loud with each. 15 minutes." I can do this from the screen alone.

## Retention risks
- The hook voice doesn't match the pain card.
- 23-32 s has only text cards.
- Small synonym pictures.
- At 63 s the length is fine; 1 s shorter helps slightly.
- Captions are readable and in sync.

## Trust risks
- "Cover the stronger word" on screen has no "stronger word" list behind it.
- The "ow" crop fragment is cosmetic.
- The English is natural, and the senses of all 5 words are correct.

## Top 3 fixes (next episode, none blocking v3)
1. shorts-builder/publisher: update `content/youtube/ep05.json` to `subscribe_at: [52.0]` and the v3 file before upload. This is required.
2. scenario-writer: put the pain in the first voice line (or open on "Using just three words a day"), and drop "ditch/streaks/analog" from second 1.
3. visuals + shorts-builder: add a picture to the 23-32 s cards, scale the synonym pictures into the empty lower frame, show each word after it's spoken so viewers can guess, change the Recall label to "Cover the word", and remove the "ow" fragment.
