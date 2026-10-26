# Ep5 YouTube metadata gate: re-check for words-that-stick-ep05-v3

Gate: glottos-language-editor, yt_meta_gate. Stamp: 2026-10-26T14:51:08Z (in ep05.json "language_approval", video "words-that-stick-ep05-v3").
Verdict: APPROVED, no edits.

Upload file: content/episodes/E5/e5-v3.mp4 (63.3 s). sha256 37c722ae2112ec34b147b026740e4cbb439728e4ca8e7b33e69d2e45ff1aef2d, the same as /workspace/glottos-auto/out/words-that-stick-ep05-v3.mp4. The only change from v2 is a 2.0 s quiz pause (critic: content/reviews/words-that-stick-ep05-v3.md, SOLVES).

Cheap re-check (as instructed, not a full redo):
- I made a fresh faster-whisper small.en transcript of v3. The spoken text matches v2 word for word: hook, anchor/recall/speak, "depth, not breadth", the 5 synonyms, "Obstinate is the bad kind of never giving up. It's just being stubborn", and the outro. No spelled-out words.
- PyAV frames at 1, 46.5, 49, 52.2, 55, 60 and 62.5 s:
  - Hook card "You learn words. Then they're gone. A 15-minute routine fixes it."
  - Quiz card "A donkey that won't move / Your turn: the good kind or the bad kind?"
  - Donkey picture with "obstinate"
  - SUBSCRIBE + bell at 52.2, SUBSCRIBED at 55
  - "Tomorrow: 3 words, 15 minutes / Save this routine"
  - Teaser "Next: why your mind goes blank" (60 and 62.5)
- The title, description and tags all still match what is heard and shown. The v2 table below still holds.
- Link https://anotherwordfor.net/never-give-up-synonym/ returns HTTP 200 (curl -k -L, 2026-10-26).
- subscribe_at [52.0] matches e5-v3.subscribe.json and is not in the description. video_ids_local = ["words-that-stick-ep05-v3"]. The critic's pre-publish blocker (53.0) is resolved.
- POLICY: none.

Not checked: the video at full frame rate (frames were sampled), the other frames between 1 and 46 s (unchanged from v2 per the critic's unit diff). No NotebookLM query was used.

---
(Previous gate on v2, kept for reference)

# Ep5 YouTube metadata gate (content/youtube/ep05.json vs words-that-stick-ep05-v2)

Gate: glottos-language-editor, step "episode 5: yt_meta_gate". Stamp: 2026-10-26T09:59:21Z (in ep05.json "language_approval").
Verdict: APPROVED, no edits.

Upload file: content/episodes/E5/e5-v2.mp4 (64.2 s, 1440x2560). sha256 be0c0531ffacae8d92e16b77ad01b34535c2f8c4d263af6f72ba438c4eb18e4f, the same as /workspace/glottos-auto/out/words-that-stick-ep05-v2.mp4.

Sources:
- My own faster-whisper small.en transcript (int8, one full pass, .nlmvenv). Working files are in /tmp/ep05m, outside the repo.
- PyAV frames at 1, 6, 10, 14, 19, 25, 30, 35, 38, 40, 43, 46, 49, 51, 54, 57, 60 and 63 s.
- Critic report content/reviews/words-that-stick-ep05-v2.md (SOLVES; 0 blockers; note: the hook voice still says "Ditch the endless digital streaks").

## Heard and seen (summary)
- Voice hook: "Ditch the endless digital streaks for a simple analog habit that makes vocabulary stick. Using just three words a day..." Title card: "You learn words. Then they're gone. A 15-minute routine fixes it."
- Routine cards: "0-5 min · Anchor: Write one sentence about your own life with each new word"; "5-10 min · Recall: Cover the stronger word. Say it before you look"; "10-15 min · Speak: Say two new sentences out loud with each word". Voice matches.
- "3 new words a day / Depth, not breadth"; "No streaks. No flashcards. Just once a day."
- Pictures: runner in rain / keep going; girl on a bike (helmet, pads) / determined; dog pulling a rope toy / tenacious; waves on rocks / relentless; donkey that won't move / obstinate ("the bad kind of never giving up. It's just being stubborn"). Quiz card "Your turn: the good kind or the bad kind?" with a pause.
- End cards: "Tomorrow: 3 words, 15 minutes", "Save this routine", "Next: why your mind goes blank". Subscribe animation at 53-58 s. Voice ends at 63.7 s ("...in the real world"). The link is not said or shown (the description is where it belongs).

## Checks
| Item | Result |
|---|---|
| Title (66 chars) | Natural; matches the "15-minute routine" title card and the "no app" message. Not misleading. PASS |
| "15 minutes a day. No app. Three new words is plenty." | Matches the video. "Three words is plenty" (an amount, so singular) is natural. PASS |
| Anchor / recall / speak bullets | Match the cards and voice. The "very angry" -> "livid" recall example is not in the video, but it is a correct example (livid = extremely angry) that only explains the step. PASS |
| "Your turn: ... swamped" | Not in the video (the unit dropped it; the video's quiz is good kind/bad kind). It does not claim to be from the video, so it is fine as extra practice. Example sentence is natural. PASS |
| "No streaks to protect, no decks to manage. Just keep going." | Matches the voice and the card. PASS |
| 5 "never give up" words + pictures | All 5 match the audio and frames; senses correct (obstinate = negative, stubborn). PASS |
| "Try it tomorrow: pick three new words and set a timer for 15 minutes." | Matches the "Tomorrow: 3 words, 15 minutes" card. PASS |
| Teaser | "Next: why your mind goes blank" on the end card. PASS |
| Link | https://anotherwordfor.net/never-give-up-synonym/ gives HTTP 200 with curl -k -L. PASS |
| Tags | Natural, relevant, no misleading tags. PASS |
| Policy | Girl on a bike = cartoon child with helmet, nothing suggestive. No sexual or unsafe content, no real people, no misleading claims, made_for_kids false. POLICY: none. PASS |
| subscribe_at | [53.0] present in JSON (matches e5-v2.subscribe.json), absent from the description. video_ids_local = words-that-stick-ep05-v2. PASS |

## Not checked
- Video not watched at full frame rate; frames sampled.
- No NotebookLM query used (none needed). lang_gate.py approve n/a (metadata only, no beats).
