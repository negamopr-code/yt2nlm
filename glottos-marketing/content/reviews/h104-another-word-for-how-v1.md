# Viewer-critic review: h104-another-word-for-how-v1 (H104 "Another Word for How")

Video: /workspace/glottos-auto/out/h104-another-word-for-how-v1.mp4 (4:26.3, 2560x1440, = state/.../final-hd1440.mp4). Reviewed 2026-10-25.
Checked: full faster-whisper small.en transcript with word timings and gaps, 25 frames (hook, every beat type, quizzes, subscribe spots, CTA), unit, meta, chapters.txt, sub.subscribe.json. Not checked: listening by ear, thumbnail, rank probe. No PROBLEM doc exists for this lab unit (content/problems absent); grep of the comment archives for "the way how / instead of how / in what way" found no quotes. Pain taken from H104: a searcher typed "another word for how" and wants usable alternatives with when-to-use, fast. No learner quotes invented. No NotebookLM query used.

## Verdict: PARTLY
Good, fast search answer that fixes 3 of 4 sister-video gaps, but its very first teaching card marks a correct sentence as wrong, and the meta is missing subscribe_at (not finished by rule).

## Sister-video issues
- Ambiguous first word: FIXED ("Another word for how, as in: how did you do that?" heard cleanly 0:00).
- No "cannot swap" beat: FIXED (0:27-0:42 "How are you? How old are you? Keep how there.").
- "Blank" run-on: FIXED (whisper hears "blank" all 4 times; 3 s think gaps at 1:40, 1:52, 3:31, 3:42).
- Crowded hook frame: REPEATS. 0:00-0:13 ghost words overlap each other ("by what means" over "the manner in which"), title + sub in the top 40 %; same ghost clutter on word cards and shadow card.

## Second-by-second
- 0:14-0:27 Before/after: "This report shows how prices rose and how much families suffered. ✗". That sentence is correct English. A B1 viewer learns "how" in a report is an error. TRUST BLOCKER.
- 0:43-1:33 Questions part: clear, meaning + register + example. "How was the film like? ✗" (1:27) is the best real-mistake moment.
- 1:59 / 3:07 subscribe anim at chapter starts: OK (3:07 overlaps the "way how" card, minor).
- 3:07-3:20 "the way how" payoff closes the hook loop: strong.
- 4:00 CTA voice "with the way, and no how after it" is heard as "know how"; card does not show the rule.
- 4:06-4:26 20 s static hold for end screen: OK only if end screen attached.
- No spelled-out word. POLICY: clean.

## Takeaway test
Write "I love the way you talk", never "the way how"; say "What was X like?", not "How was X like?". Clear action: yes.

## Top 3 fixes
1. scenario-writer + language-editor: replace the before/after "before" with a really wrong or weak sentence (e.g. "the way how prices rose") or relabel it "plain → formal" without ✗; re-render the 0:14 beat (shorts-builder). Also editor gate missed it.
2. shorts-builder: copy subscribe_at [119.0, 187.0] into content/youtube/h104-another-word-for-how-v1.json.
3. visuals/shorts-builder: thin or remove ghost-word background on hook/word cards; scenario-writer: CTA speech "with the way, without how after it" + put "(no 'how')" on the card.
