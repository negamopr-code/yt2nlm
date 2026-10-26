# Viewer-critic: Words That Stick Ep4 "This is why you freeze mid-sentence", e4-v1.mp4

Reviewed 2026-10-26 by glottos-viewer-critic.
- Video: `content/episodes/E4/e4-v1.mp4`. 1440x2560 (meets the 1440 minimum), 30 fps, 75.24 s, AAC stereo. Unit: `shorts/units/ep04_v1.json`. Subscribe JSON: `content/episodes/E4/e4-v1.subscribe.json` (58.0 s, 5 s, bottom-left).
- Heard audio: faster-whisper small.en with word timings, run on the FINAL mp4 audio, plus silencedetect (-40 dB, 0.6 s).
- Frames: about 50 frames (hook 0.1/0.8/1.5, every beat, every scene cut found by ffmpeg scene detection at 2.3, 7.1, 11.4, 17.8, 22.8, 28.6, 33.0, 38.6, 39.7, 44.7, 48.5, 55.4, 57.7, 61.0, 63.4, 68.9, plus the whole subscribe window 58-63).
- Pain evidence: NotebookLM source "PROBLEM 01 — synthesis" (60678678-9960-4836-88cd-453de0b673e8), read with `source content` (free). No query was used. Also read: article §5, `content/articles/p01-ep04-format.md`, `p01-ep04-audio-script.md`, `p01-ep04-visuals.md`.

## Verdict: PARTLY. The voice teaches the right thing, but for 11 seconds the picture shows the wrong word.
The lesson you hear is good. The two quizzes have real pauses, there is a clear action for tomorrow, and the teaser is spoken. But the panels are shifted by one. While the voice says "livid", the screen shows only a strip with the word "swamped". The livid picture then appears under "Let me look into that", and the meeting picture never appears at all. In an episode about choosing the RIGHT word for the setting, showing the wrong word on screen is a trust blocker. There are also literal asterisks on the second card, and the meta has no `subscribe_at`.

**ship_blockers: 3.** No spelled-out word. POLICY: none.

## 1. Pain (learner's words) → given → gap
Verbatim quotes from the PROBLEM 01 synthesis, §3 "Learners' own words":
- "my mind goes blank"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank"
- "when I try to speak I forgot every sentence in my mind !! My mind became blank ..."
- "I mostly avoid communicating in a crowd because I dont remember the words. dont know how to make phrases."
- "My mind become block out and forget what to say and sometimes im sweating And nervous kills me"
- "i felt such frozen/dumb/humiliation/shame"
- "I can write paragraphs in English without any difficulty but as soon as i speak my mind just shuts down"
- Gap row (tool reality, not a learner quote): thesaurus sites list synonyms "without register tags, example sentences, or 'avoid when' guardrails", "leading learners to use formal words in casual settings or make embarrassing mistakes".

Honest note: no verbatim learner quote in the corpus says "I freeze because I'm not sure the word is too formal". The register cause is the article's claim (§5) plus the gap row. The episode attaches it to the real "freeze / blank" pain. That is a fair bridge, but it is a hypothesis.

**Pain in one sentence (learner voice):** "When I speak, I freeze and the words are gone, and I'm scared I'll say something wrong."
**"Solved" means:** tomorrow, I write next to each new word whether it fits friends, work or both. And I know that "give me a hand" is for friends, while "assist" sounds stiff with friends.

| Pain | Given | Gap |
|---|---|---|
| Freezing mid-sentence | Hook 0-2.3 with the doubt bubbles "Too formal? Too rude? Too dramatic?" | Good. It names the freeze in second 1. |
| Not knowing where a word fits | Swamped / livid / "let me look into that" with avoid-when lines (voice only), plus 5 ways to say help from casual to formal | The avoid-when lines and the register of help/support/aid are never on screen (no tag cards, no chips). Worse, the livid and look-into-that pictures are wrong (see blocker 1). |
| "What do I do?" | "Tomorrow: tag each new word · friends · work · both" | Clear. PASS. |

## 2. Heard transcript (final video, small.en)
0.00 This is why you freeze mid-sentence. / 2.60 It's not that you forgot the vocabulary word. You're just not sure if it fits the setting. / 7.26 Is this word too formal? Is it rude or is it too dramatic? / 11.64 Saying you are swamped is fine at work, but not when you only have one or two small tasks. / 18.20 And being livid? That's too dramatic for someone who is just slightly annoyed. / 23.10 Let me look into that suits emails and meetings, but it feels weird in chats with friends. / 28.28 Let's check out five ways to say help, going from casual to formal. / 33.36 Friends moving a sofa. Can you give me a hand? Formal or casual? / [silence 36.73-38.69, 1.96 s] / 39.02 Casual. / 39.76 A neighbor [captioned neighbour] carrying your heavy shopping. Help. That's fine anywhere. / 45.10 The IT team fixing your laptop? That's support. / 48.68 A hotel receptionist. How may I assist you? Formal or casual? / [silence 53.55-55.42, 1.87 s] / 55.38 Formal. It sounds super stiff with friends. / 58.16 "Lori's" [= Lorries, captioned Lorries] bringing food after a flood. That's aid. / 61.26 Learn the setting, not just the meaning. / 63.72 Tomorrow, next to each new word, write where it fits. Like friends, work, or both. / 69.14 Just look up another word for help on anotherwordfor.net. / 73.22 Next, the 15-minute routine. (end 74.6, file 75.24)
- Spelled-out words: NONE. The "mid -sentence" and "15 -minute" hyphen tokens are normal compound words.
- No podcast markers, studies, numbers outside the allowed ones, or banned CTA verbs. The CTA is truthful (help page = word list).
- "super stiff": "super" is on the visuals §3 filler list. Minor. The language editor kept it.
- "Lori's" with a US accent: the caption says "Lorries", so a B1 viewer can read it. Minor.
- Teaser to Ep5 (the 15-minute routine): heard at 73.2-74.5 and printed in the CTA card sub-line. PASS (only small grey text, no own card).

## 3. Second by second (scroller view)
- 0.0-2.3 HOOK: the title "Why You Freeze Mid-Sentence" and a picture with three doubt bubbles, voice from 0.0. Strong, my problem, I stop. Good.
- **2.3-7.0: card "You didn't forget it." / "You're not sure it \*fits\*."** The asterisks are printed literally (the markdown emphasis was not rendered). It looks broken in the 3rd second, while trust is being decided. BLOCKER 2.
- 7.1-11.4: the hook picture again with the "Too formal?" caption. Fine.
- 11.4-17.8: the swamped picture (desk + piles), matches. Good.
- **17.8-22.8: voice "And being livid? That's too dramatic for someone who is just slightly annoyed." Screen: an empty white strip that says only "swamped".** The picture tells me livid = swamped. BLOCKER 1.
- **22.8-28.6: voice "Let me look into that suits emails and meetings". Screen: the angry woman at the door (the livid picture).** I'd read this as "let me look into that = angry". The meeting picture (panel 4 of the main sheet) is never shown. Same blocker.
- 28.6-33.0: card "5 ways to say help · casual → formal". Clear.
- 33.0-38.6 QUIZ 1: the question card "Can you give me a hand?", a small grey "Formal or casual?", and a countdown badge in the 2 s silence. A real self-test. The q_sub is small (about 1/3 the headline size). Readable, but it should be bigger.
- 38.6-39.7: the sofa picture with "give me a hand" + caption "Casual.". The reveal works. The answer is only in the caption, with no "casual" chip.
- 39.7-44.7 help, 44.7-48.5 support: the pictures match the voice. The caption "Help?" has a question mark, but the voice says "Help." Trivial.
- 48.5-55.4 QUIZ 2: the "How may I assist you?" card, a 1.9 s pause, then "Formal." with the receptionist picture. Works.
- 57.7-61.0 aid: picture with "aid", matches.
- 58.0-63.0 SUBSCRIBE + bell: visible bottom-left, below the caption box. It clicks to SUBSCRIBED and the bell turns yellow at about 61. It does NOT cover the rule card or the captions. PASS on screen.
- 61.0-63.4: rule card "The rule: learn the setting / not just the meaning. Screenshot this." The sub-line is small grey text. Captions are missing for about 61.0-62.7 while the voice says "Learn the setting, not just the" ("meaning." appears at 63). Minor, because the card carries the text.
- 63.4-68.9: "Tomorrow: tag each new word · friends · work · both". Clear action.
- 68.9-75.2: CTA "Look up another word for help · anotherwordfor.net · Next: the 15-minute routine". No dead air at the end (0.6 s).
- Layout: the pictures are small 16:9 bands in the upper third, and the lower half is empty on every beat. On a phone the pictures are small. It is the same template as Ep3, so this is acceptable but not great.

## 4. Takeaway test
"Tomorrow, next to each new word, write where it fits: friends, work, or both." It is heard at 63.7-68.4 and shown on a card. PASS. Second takeaway: give me a hand = casual, assist = stiff with friends (tested in two quizzes).

## 5. Retention risks
- 75 s for 10 points is fine. Pacing is natural, and the quiz pauses are real (1.96 s / 1.87 s).
- 17.8-28.6 is the swipe zone: the picture doesn't match the word, and the "swamped" strip on a blank background looks like a render bug.
- The register information (avoid-when lines, the chips for help/support/aid) is voice-only. A muted scroller (many are) gets no register lesson for swamped/livid/look-into-that at all. The captions carry it word by word, but nothing stays on screen to screenshot.

## 6. Trust risks
- Wrong word on screen 17.8-28.6 (blocker 1). In a "pick the right word" lesson, this is the worst kind of error.
- Literal "\*fits\*" (blocker 2).
- Facts: register claims match the dictionary-checked script (assist formal, give me a hand casual/informal, aid news/formal). No overclaims. Note: the spoken "It sounds super stiff with friends" is fine English.
- POLICY: none (clean pictures, no real people, no innuendo).

## 7. Ship-blockers (3)
1. **17.8-28.6 panel mapping is off by one.** Beat "panel 3" renders the swamped label strip, and beat "panel 4" renders the livid picture. Fix: the livid beat (17.8-22.8) must show the livid picture (door/landlord). The "let me look into that" beat (22.8-28.6) must show the meeting-table picture. Check the main-sheet split (`state/nlm-raw/ep04-infographic.png`: title+1, 2, 3, 4) so that no label-only strip becomes a panel. Re-render. Owner: shorts-builder (panel split/mapping); visuals if the sheet needs manual panels like the syn sheet.
2. **2.3-7.0 literal asterisks "You're not sure it \*fits\*."** The card `sub` field doesn't render `*…*` emphasis (the headline does, see "help" in orange). Fix: remove the asterisks from the sub, or make sub render emphasis. Owner: shorts-builder.
3. **`content/youtube/ep04.json` has no `"subscribe_at"`.** Add `"subscribe_at": [58.0]` (or the new time after the re-render) under the 2026-10-05 rule. Owner: shorts-builder.

## 8. Top 3 fixes by impact
1. shorts-builder (+visuals): fix the off-by-one panels so that livid shows the livid picture and "let me look into that" shows the meeting picture. Re-render at 1440x2560, then re-check 17.8-28.6 frame by frame.
2. shorts-builder: remove the literal asterisks on the "You didn't forget it." card, and record `subscribe_at` in ep04.json.
3. shorts-builder/visuals (retention, not a blocker): put the register on screen as a big chip under each picture: swamped "fine at work · not for 1-2 small tasks", livid "too dramatic for slightly annoyed", let me look into that "emails & meetings · not with friends", help "fine anywhere", support "common at work", aid "news, not everyday chat". Also make "Formal or casual?" and the rule sub-line bigger, and caption the rule line at 61.0-62.7. Then the language-editor re-gates the chips.
