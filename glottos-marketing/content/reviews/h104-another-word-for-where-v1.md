# Viewer-critic review: h104-another-word-for-where-v1 (H104 "Another Word for Where", video 3 of 3)

Video: /workspace/glottos-marketing/state/shorts/h104-another-word-for-where-v1/final.mp4 (4:36.0, 2560x1440, 30 fps, mono AAC). Reviewed 2026-10-26.
What I checked: the full faster-whisper small.en transcript with word timings, about 40 frames (hook at 0.5/1.5 s, every beat, the quiz think and answer states, both subscribe spots, the CTA, the end hold), the unit, the meta, chapters.txt, final_sub.subscribe.json and thumbnail.jpg.
What I did not check: listening by ear (only the transcript), the rank probe (not run yet, per the meta), and the end screen on YouTube. There is no PROBLEM doc for this lab unit. I took the pain from H104: a searcher typed "another word for where" and wants usable alternatives with when to use each one, fast. No learner quotes exist for it, so none are invented here. No NotebookLM query was used.

## Verdict: SOLVES (video). One pre-send blocker on the thumbnail.
It answers the search in second 1, gives 10 alternatives with register and an example, and every ✗ marks a real mistake. A learner can fix "where I grew up in" and "do you know where is" the next day. The thumbnail picture (a woman crying or laughing on the phone, with a "Congratulations" paper) has nothing to do with "where", so fix it before sending.

## Checklist 13 ("another word for X")
- (a) "Another word for where, as in: where do you live?" is heard clearly at 0:00-0:03 (whisper gets it exactly). The five answer words are on the hook card at 0:00. PASS
- (b) "Where must stay": 0:33-0:45, "Where are you? Where is my phone? ... keep where." PASS. One small point: at 0:33 "not every where" is heard as "not everywhere" (whisper writes "everywhere"), which means something else. The card does not show that line.
- (c) Before/after: 0:13-0:32, labelled "Plain" and "Report style" with NO ✗, and both sentences are correct. This fixes the trust blocker from the h104-how review. Real-mistake ✗ cards are at 1:35 ("Do you know where is the station? ✗", a real word-order error) and 3:13 ("the town where I grew up in ✗", a real error). The crossed-out options in the quizzes ("which" alone at 3:42, "How do I get to" at 2:01, "the location of" at 3:55) are all really wrong in those blanks. PASS
- (d) "blank" is heard 4 of 4 times (1:41, 1:53, 3:36, 3:48). "blanket" never appears. Think gaps are about 3.5 s. PASS

## Sister-video gaps (h104-how)
- ✗ on a correct sentence: FIXED (see c).
- subscribe_at missing in the meta: FIXED, [123.0, 191.0] matches final_sub.subscribe.json.
- CTA rule not on the card: FIXED. The card says "one sentence with in which (no where)" and the speech says "without where" clearly at 4:08.
- Ghost-word clutter: REDUCED. The background words are darker, and the hook and word cards are readable at 360 px. Still some noise behind the cards at 0:47 and 2:24.

## Second-by-second
- 0:00-0:13 Hook: my problem in 1 s, the answer is on screen, and there is an open loop ("the little word learners add at the end"). I would not swipe.
- 0:13-0:32 Before/after with a crime report: 19 s of long sentences, the slowest stretch. A searcher who wants a quick list may swipe here. Risk: medium.
- 0:47-1:33 Question words: each one takes about 8-12 s, has its meaning, register and an example, and the example appears when it is spoken. Good pace.
- 1:35 Indirect-question mistake: a strong moment.
- 1:38-2:04 Two quizzes with a countdown, a green answer and a note: I test myself here.
- 2:03-2:08 Subscribe animation over "Say it now": OK. Shadowing at 2:05-2:20 has gaps of about 3 s.
- 2:24-3:11 Sentence words: "If possible = where possible" (3:07) is the weakest item. It replaces a fixed phrase, not "where" itself, and a learner can't use it the way they use the others. "That ... in" at 2:38 is heard as "That within".
- 3:11-3:16 The second subscribe animation sits over the key payoff card ("where I grew up in ✗"). It is bottom-left and covers no text, but it pulls the eye away from the best moment.
- 3:13-3:25 The loop from the hook is closed: "Where, or in at the end, never both." This is the strongest takeaway.
- 4:16-4:36 A 20 s static hold for the end screen: fine only if the end screen is attached.
- No word is spelled out. POLICY: clean (speech, cards, title, description, tags, thumbnail).

## Takeaway test
Say "the town where I grew up" or "the town I grew up in", never both. Say "Do you know where the station is?" and "Which way is the station?". Both are clear actions for tomorrow. PASS

## Retention risks
- Length 4:36 (speech ends at 4:16) for 10 items: OK. The before/after at 0:13 is long and comes too early for a searcher in a hurry.
- Pace: speed 1.0 with am_michael, no dead air. Text stays up long enough to read.
- Repetition: low.

## Trust risks
- "If possible" as "another word for where" overclaims a little. "The location of" and "How do I get to" are rewordings, not swaps, but they are honest about it in the speech.
- "Not every where" is heard as "not everywhere" (0:33).
- The thumbnail picture does not match the video. A viewer who clicks a crying woman on the phone gets a black text-only video, which risks a "misleading thumbnail" mismatch and a fast exit. The meta send_note is also out of date ("not rendered, no language approval yet").

## Top 3 fixes (by impact)
1. visuals + shorts-builder: replace thumbnail.jpg with a picture that matches the topic (a map, a signpost, or text only "NOT JUST WHERE" + "10 WORDS"), or no picture. Do this before sending. It is a pre-send blocker.
2. scenario-writer + language-editor (next where-type unit; for this one, only if re-voiced): swap "If possible" for a real where swap (e.g. "whereabouts" as a noun, "the place where/that", or "somewhere/anywhere"). Re-voice 0:33 as "Not every 'where' can be swapped" with a pause, or show the line on the card. Cut the before/after to under 12 s.
3. shorts-builder: move the second subscribe animation off the 3:11 payoff card (e.g. to the 2:24 "Part 2" chapter start, which keeps the chapter-start rule), update subscribe_at, and update the meta send_note. Run rank_probe.py before sending.
