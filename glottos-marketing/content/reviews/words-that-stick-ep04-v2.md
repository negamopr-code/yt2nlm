# Viewer-critic: Words That Stick Ep4 v2 "This is why you freeze mid-sentence", e4-v2.mp4

Reviewed 2026-10-26 by glottos-viewer-critic (re-review after the v1 PARTLY, `content/reviews/words-that-stick-ep04-v1.md`).
- Video: `content/episodes/E4/e4-v2.mp4`. 1440x2560, 30 fps, 75.24 s, AAC stereo. Unit: `shorts/units/ep04_v2.json`. Subscribe JSON: `content/episodes/E4/e4-v2.subscribe.json` = `{"subscribe_at": [58.0], "seconds": 5.0, "corner": "bl"}`.
- Heard audio: faster-whisper small.en (int8, cpu_threads=4, word timings) on the FINAL v2 mp4, plus silencedetect (-40 dB, 0.6 s).
- Frames: 44 frames at 360 px (hook 0.1/0.8/1.5, every beat, the whole subscribe window 58-63), plus extra frames on both sides of every switch point (2.2/2.4, 17.7/17.9, 22.7/22.9, 28.5/28.7), plus a full-res crop of the 2.3-7.0 card sub-line. Scene cuts (ffmpeg scene>0.06): 2.2, 2.33, 7.07, 11.4, 17.8, 22.8, 28.6, 38.63, 39.73, 42.87, 44.73, 48.53, 55.37, 57.7, 61.0, 72.63.
- Pain evidence: reused from the v1 review (PROBLEM 01 synthesis, read via free `source content`). No NotebookLM query was used.

## Verdict: SOLVES (for the "not sure it fits" slice of the freeze pain). One record is still missing before it can ship.
The v1 picture/voice mismatch is gone. Every picture now shows the word you hear at that moment. The second card is clean. The video teaches one rule, tests it twice with real pauses, and ends with a concrete action for tomorrow. One thing still blocks shipping: `content/youtube/ep04.json` (read at review time) has no `"subscribe_at"`, and its `video_ids_local` still says `words-that-stick-ep04-v1`. The launcher says it is adding these. Ship only after both are written.

**ship_blockers: 1** (meta: subscribe_at [58.0] + video_ids_local -> ep04-v2, not yet in ep04.json at review time). No spelled-out word. POLICY: none.

## v1 blocker check
| v1 blocker | v2 evidence | Status |
|---|---|---|
| 1. Panels off by one (17.8-28.6) | Cut at 17.8 to the door/angry-woman picture. Voice "And being livid?" starts at 18.20, so the picture leads the word by 0.4 s. The picture holds through "slightly annoyed." (22.32). Cut at 22.8 to the meeting-table picture. Voice "Let me look into that" starts at 23.10. The picture holds through "chats with friends." (28.00). Cut at 28.6 to "5 ways to say help". The swamped picture holds from 11.4 to 17.8, and the voice word "swamped" is at 12.32. No label-only strip appears anywhere. | FIXED |
| 2. Literal *fits* asterisks (2.3-7.0) | The full-res crop reads "You're not sure it fits." with no asterisks. | FIXED |
| 3. subscribe_at missing | The animation is on screen 58.0-63: red SUBSCRIBE, then the click to SUBSCRIBED, then the bell turns yellow at about 60-61. It sits bottom-left under the picture and covers neither the captions nor the rule card. `e4-v2.subscribe.json` has 58.0. **But `content/youtube/ep04.json` has no `subscribe_at` key yet, and `video_ids_local` = v1.** | OPEN (launcher is adding it) |

## 1. Pain (learner's words) → given → gap
Verbatim quotes (PROBLEM 01 synthesis, §3): "my mind goes blank"; "I can understand 100% of the video, but when I try to speak, my mind goes blank"; "I mostly avoid communicating in a crowd because I dont remember the words. dont know how to make phrases."; "I can write paragraphs in English without any difficulty but as soon as i speak my mind just shuts down"; "i felt such frozen/dumb/humiliation/shame".
**Pain:** "When I speak, I freeze and the words are gone, and I'm scared I'll say something wrong." **Solved =** tomorrow I tag each new word friends / work / both, and I know "give me a hand" is for friends while "assist" sounds stiff with friends.
- Given: the hook names the freeze in second 1. Three register examples follow (swamped, livid, let me look into that), then 5 help words from casual to formal with two self-tests, the rule, the action and the CTA.
- Gap (unchanged from v1, not a blocker): the corpus has no learner quote that blames the freeze on register doubt. That cause is the article's hypothesis. For a viewer whose blank comes from nerves ("nervous kills me"), this episode is a partial answer. The avoid-when lines and the help/support/aid register are voice and caption only. Nothing stays on screen to screenshot (no chips).

## 2. Heard transcript (v2 final; audio is identical to v1)
0.00 This is why you freeze mid-sentence. / 2.60 It's not that you forgot the vocabulary word. You're just not sure if it fits the setting. / 7.26 Is this word too formal? Is it rude or is it too dramatic? / 11.64 Saying you are swamped is fine at work, but not when you only have one or two small tasks. / 18.20 And being livid? That's too dramatic for someone who is just slightly annoyed. / 23.10 Let me look into that suits emails and meetings, but it feels weird in chats with friends. / 28.28 Let's check out five ways to say help, going from casual to formal. / 33.36 Friends moving a sofa. Can you give me a hand? Formal or casual? / [silence 36.73-38.69] / 39.02 Casual. / 39.76 A neighbor carrying your heavy shopping. Help. That's fine anywhere. / 45.10 The IT team fixing your laptop? That's support. / 48.68 A hotel receptionist. How may I assist you? Formal or casual? / [silence 53.55-55.41] / 55.38 Formal. It sounds super stiff with friends. / 58.16 "Lori's" (= Lorries, captioned "Lorries") bringing food after a flood. That's aid. / 61.26 Learn the setting, not just the meaning. / 63.72 Tomorrow, next to each new word, write where it fits. Like friends, work, or both. / 69.14 Just look up another word for help on anotherwordfor.net. / 73.22 Next, the 15-minute routine. (voice ends 74.52, tail silence 0.63 s)
- Spelled-out words: NONE ("mid -sentence", "15 -minute" and "anotherwordfor .net" are whisper token splits of normal words).

## 3. Second by second (scroller view)
- 0.0-2.3 hook: the title plus the "Too formal? / Too rude? / Too dramatic?" bubbles, voice from 0.0. My problem, I stop.
- 2.3-7.0 card "You didn't forget it." / "You're not sure it fits.": clean now. Small things: "it." wraps alone onto line 2, and the sub-line is small grey text.
- 7.1-11.4 hook picture again: fine.
- 11.4-17.8 swamped, 17.8-22.8 livid (door), 22.8-28.6 meeting: all match the voice. This was the v1 swipe zone and it now reads correctly.
- 28.6-33.0 "5 ways to say help · casual → formal": clear.
- 33.0-38.6 quiz 1: the card, then the "2" countdown badge in the 1.96 s silence. A real self-test. The reveal at 38.6 is the sofa picture labelled "give me a hand" with the caption "Casual.".
- 39.7-44.7 help, 44.7-48.5 support: match. The caption "Help?" vs the voice "Help." is trivial.
- 48.5-55.4 quiz 2 "How may I assist you?": the countdown badge in the 1.86 s silence, then the reveal with the assist picture and "Formal.".
- 57.7-61.0 aid (lorries in a flood): matches. The subscribe animation runs 58.0-63.
- 61.0-63.4 rule card, 63.4-68.9 "Tomorrow: tag each new word · friends · work · both", 68.9-75.2 CTA "Look up another word for help · anotherwordfor.net · Next: the 15-minute routine".
- Possible swipe points (soft): about 7.1-11.4 (the same hook picture a second time) and the small 16:9 bands with an empty lower half. This is the series template, not a blocker.

## 4. Takeaway test
"Tomorrow, next to each new word, write where it fits: friends, work, or both." Heard at 63.7-68.4 and shown on a card. PASS.

## 5. Retention risks
75 s for 10 points; the pacing is natural; the quiz pauses are real. The lower half of the screen is empty on every beat. The register is not on screen as chips, so a muted viewer gets only the captions. The q_sub "Formal or casual?" and the rule sub-line are small grey text. The rule line has no caption at about 61.0-62.7 (the card carries the text).

## 6. Trust risks
None blocking. The register claims match the checked script. "super stiff" is fine spoken English. US "Lori's" is captioned "Lorries". POLICY: none (clean illustrations, no real people, no innuendo, safe for 13+).

## 7. Ship-blockers (1)
1. `content/youtube/ep04.json`: add `"subscribe_at": [58.0]` and point `video_ids_local` to `words-that-stick-ep04-v2` (at review time it still lists v1, so the publisher could pick the wrong file). Owner: shorts-builder (the launcher says it is doing this now).

## 8. Top 3 fixes by impact (future episodes / optional v3)
1. visuals + shorts-builder: bake the register chips into the panels ("fine at work · not for 1-2 small tasks", "too dramatic for slightly annoyed", "emails & meetings · not with friends", "fine anywhere", "common at work", "news, not everyday chat"). Then the lesson works muted and can be screenshotted. The language-editor gates the chips.
2. shorts-builder: make q_sub and card sub-lines bigger (at least about 60% of headline size), and caption the rule line at 61.0-62.7.
3. scenario-writer: in the hook, tie the register cause to the learner's own words ("my mind goes blank"), or say plainly that this is ONE reason you freeze. Do not imply it is THE reason.
