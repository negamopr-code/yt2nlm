# Viewer-critic review: l1-friendly-3-c1-words-v1 (door Short of the H30 long video)

Reviewed 2026-10-13. Long video review: `content/reviews/long-c1-vocabulary-personality-v1.md`.
- Video: `state/shorts/l1-friendly-3-c1-words-v1/final.mp4` - 1440x2560, 30 fps, 23.9 s, AAC 48 kHz stereo, md5 23f4bed20579af88ded39f45d1cff978.
- Unit: `shorts/units/l1-friendly-3-c1-words-v1.json` (language hash c6eaa449b7a97763). Meta: `content/youtube/l1-friendly-3-c1-words-v1.json`.

## Verdict

**PARTLY - 0 ship blockers.** It does its door job (three correct words, clean pointer to the lesson) but on its own it gives three words with no meaning and no difference between them, which is the pain itself.

## Pain

Same evidence as the long review (no PROBLEM document; corpus quotes, names removed): "Use it to be precise. There's a difference between "like", "love", "adore", "admire", and "idolize" for example." / "nobody in real life talks like that." / "It's kind of like C1 level word blended in a B1 level sentence."
Pain: I only say "friendly"; I want better words and to know which one fits.
Solved means: tomorrow I say "an affable host" and know it is not the same as "gregarious".

Gives: affable / gregarious / genial, each with a two-word phrase and the long video's picture.
Gap: no meaning at all. The pictures carry it only for gregarious (party face + balloon). Affable (smile + handshake) and genial (old man + waving hand) both just read "friendly". A viewer leaves with three labels for the same thing.

## What is heard (faster-whisper small.en) and seen

| Time | Heard | Seen |
|---|---|---|
| 0.0-1.1 | "Don't just say friendly." | frame 0: "Don't just say "friendly"", friendly already struck in red; pill "C1 ADVANCED VOCABULARY" at top. The headline is still zooming in at frame 0. |
| 1.9-3.6 | "Here are three advanced words." | "3 advanced words (C1)" appears at about 2.0 s |
| 4.6-7.4 | "Affable, an affable host" | "Affable" alone (frame at 5.0 s); phrase + picture by the frame at 7.0 s |
| 8.4-11.8 | "Gregarious, my gregarious sister" | same pattern |
| 12.8-16.1 | "Genial, our genial neighbour" | same pattern |
| 17.2-22.1 | "Want 40 advanced words to describe people? Watch the full lesson on this channel." | closing card; subscribe + bell 17.6-22.6 bottom-left, below the text |

All three words heard and shown, in the same order as the description. Card says "Want 40 words", voice says "40 advanced words" - fine. No spelled-out word. Nothing cut off.

## Checks asked for

- First frame: the problem is complete at frame 0 (struck "friendly" + the C1 pill). The payoff "3 advanced words (C1)" is not there until about 2 s, in sync with the voice. Acceptable, not ideal: a muted scroller sees only what not to say for 2 s.
- Subscribe + bell at 17.6 s: visible on frames 17.8-21.5, in the empty space under the closing text, hides nothing. Recorded in meta `subscribe_at: [17.6]` and `sub.subscribe.json`. In the second half as required.
- Render 1440x2560: passes.
- Pictures: same emoji cards as the long video; they fit, with the limit named above.

## Second-by-second swipe risk

- 0-2 s: stop is plausible ("friendly" is my word, struck out).
- 5.1-6.4, 9.4-10.6, 13.7-15.0: **after each headword there is 1.2-1.3 s of true silence** (below -45 dB, no music bed in the Short) with only the bare word on screen and no cue such as "say it". With the pauses between cards (3.6-4.4, 7.5-8.6, 11.9-13.1, 16.2-17.3) that is seven silent gaps, about 8 s of 24 s. This is where a scroller leaves; it feels like the video stalled.
- 17.2 s: closing card. No link is possible in a Short; "on this channel" depends on the Related video being set.
- Background: the faint yellow words and logo tiles are brighter here than in the long video and sit directly behind the headline ("gregario" behind the struck "friendly" at frame 0). They also show all three answers before they are taught.

## Takeaway test

One action: say "an affable host" / "my gregarious sister" / "our genial neighbour". Nameable, but only as a copied phrase - I could not say when to pick which. Hence PARTLY.

## Trust risks

None found. Collocations are natural. British "neighbour", American voice.

## Non-blocking remarks for the channel owner

1. The silences after each headword: fill them (the long video's bed + tick) or shorten `pause_after_word` to about 0.4 s. Owner: shorts-builder.
2. Add three or four words of meaning under each phrase ("calm and easy to talk to" / "loves groups" / "warm and cheerful"). That would turn PARTLY into SOLVES without making it longer if remark 1 is done. Owner: scenario-writer, then language-editor.
3. Show "3 advanced words (C1)" from frame 0. Owner: shorts-builder.
4. Dim the background words behind the hook headline. Owner: visuals/shorts-builder.
5. The rendered file is not yet in `/workspace/glottos-auto/out/`. Check before the send step.

## Top 3 fixes by impact

1. scenario-writer: a few words of meaning per word.
2. shorts-builder: remove the dead air after headwords.
3. shorts-builder: full promise on frame 0.

## What was checked and what was not

- Checked: 20 frames across the 23.9 s (0, 0.5, 1.5, 2.0, 2.4, 3 ... 23.7), the whole audio by faster-whisper small.en, silence and level measurement, resolution, meta fields.
- NOT checked: nobody listened by ear; the exact frame at which each phrase and picture appears was read from frames about 1 s apart, not frame by frame.
