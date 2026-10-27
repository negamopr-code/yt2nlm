# Viewer-critic review: h97-furthermore-v1 (H97 "Other Ways to Say Furthermore")

Reviewed 2026-10-27, file `state/shorts/h97-furthermore-v1/final.mp4` (28.9 s, 1440x2560, 30 fps, AAC 48 kHz), unit `shorts/units/h97-furthermore-v1.json` (language approval cc608cf1988f4c07).
How I checked: 16 frames (hook at 0.1/0.8/1.5/2.8 s, then 1-2 per beat) plus a full-size crop at 20 s; faster-whisper small.en transcript of final.mp4 with word timings; separate transcript of b01-0.wav (hook).
Not checked: listening by ear (I only have the transcript); loudness and gate_av numbers.

## Verdict: PARTLY
The content works: 5 correct replacements, each in a full sentence with the comma, and the word is said in second 1. But the Short is 28.9 s, against the proven 14-19 s form (the lab's 24-s form already LOST). It has no subscribe/bell animation and no `subscribe_at` meta. Two of the five "essay-ready" words are weak in a formal essay.

## Pain (learner's own words, from the corpus in reports/monitor-awf)
- "Could you please give us information about linking words?"
- "Could you please conduct lessons on these linking words?"
- "Are these transition words used in writing or speaking?"
- "Can someone put the linking word \" along with \" in a sentence in an essay for example"
- "for beginners i'd say avoid \"firstly secondly thirdly\" in your essays. ... link it to the second and third ones with \"additionally\", \"moreover\", or \"furthermore\"."
- "But my favorite transition words are however, therefore, and as well as."
- "I saw in some youtube videos that conjunctive adverbs usually need semicolon. I'm not sure about the remaining transition words."

In their words, the pain is: "I keep writing 'furthermore' in my essay. Give me other linking words I can use in writing, in a real essay sentence."
Solved would mean: tomorrow, in the essay, the second "furthermore" becomes "Moreover," or "Equally important," with the right comma, and the learner trusts that it fits a formal essay.

## What the video gives them, and the gap
- Gives: 5 alternatives, each with a full example sentence that shows "Word, + clause". The number counter (1/5 ... 5/5) and a clear CTA are there.
- Gap 1: the card says "essay-ready", but "What's more" (a contraction) and "Not only that" (spoken style) are the two that many essay teachers mark down. The learner asked "writing or speaking?", and the video never answers.
- Gap 2: the examples sound like adverts ("the app works offline", "the course is free"), not essay sentences. The learner from the corpus asked for "a sentence in an essay".
- Gap 3: the red strike-through on "furthermore" next to the "STOP SAYING" badge suggests that furthermore is wrong. It is not wrong. It is only repeated. This is a mild trust risk for a learner who was told to use it.

## Second by second (heard / seen)
- 0.0-0.8: the card shows "Other ways to say" and the voice starts at once. "furthermore" appears around 0.8 s and is heard at 1.04 s. OK, this is my search phrase, so I stop.
- 1.9-2.2 and 2.6-3.9: "Here are five." Then a 1.3 s gap before "Moreover" (3.92). The strike lands about 2.8 s. This is the first swipe risk: nothing new for about 1.3 s.
- 3.9-7.4: "Moreover, the plan is cheap. Moreover, it is fast." The headline is read alone, and then the example starts with the same word.
- 8.5-11.8 "Equally important. Equally important, the course is free." 12.9-16.2 "Not only that, not only that, ..." 17.6-20.4 "What's more, what's more, ..." 21.5-24.0 "Beyond that, beyond that, ..." Every word is said twice back to back, and there is a 1.1-1.4 s silence between beats. "Not only that, not only that" sounds like a stutter. I'd swipe around 13-17 s once the pattern is clear: I've seen the list and don't need to wait.
- 25.7-27.0: "Which one will you use today?" The card stays to 28.9 s with "Write it in the comments." This is about 1.9 s of a still card at the end.
- The picture matches the voice in every beat, and the text is readable (big yellow headline, white example; the ghost words behind it are busy but don't hide anything; checked at full size, 20 s).
- Self-test: none. The CTA asks to choose a word, not to try it.
- Whisper heard "other ways to SAVE furthermore" in the final mix, but "say" in the raw b01-0.wav. The mix or music may slightly blur "say". Listen once by ear.

## Takeaway test
Yes, one action can be named: "Replace your second 'furthermore' with 'Moreover,' or 'Equally important,'". The verdict is not capped by the takeaway. It is capped by length, the missing subscribe layer and the overclaim.

## Retention risks
- Length 28.9 s for 5 words. Lab decision: the 24-s 3-word form LOST (H83), and the proven form is 14-19 s for 5 words (H91). The fat is: every word said twice (about 5 x 1.0 s), 1.1-1.4 s gaps between beats (about 6 s), and a 1.9 s still card at the end.
- The repetition makes it sound robotic (voice am_michael 1.15x, which is otherwise clear).

## Trust risks
- "5 essay-ready words" is an overclaim for "What's more" and "Not only that".
- The strike-through suggests "furthermore" is wrong.
- Spelled-out words: none (checked in the transcript). POLICY: none found. Logo = official channel avatar (checked against state/brand/awf-logo-channel.jpg). No watermark seen.

## Ship blockers
1. No subscribe + bell animation in final.mp4, and no `content/youtube/h97-furthermore-v1.json` with `"subscribe_at"` (user rule 2026-10-05: not finished without both). Owner: shorts-builder (shorts/subscribe_anim.py, once in the second half), then publisher meta.
2. Runtime 28.9 s against the 14-19 s target the lab asked for. Owner: shorts-builder + scenario-writer (see fix 1).

## Top 3 fixes (by impact)
1. **Cut to about 17 s** (scenario-writer + shorts-builder). Say each word once: speech = only the example ("Moreover, the plan is cheap and fast."), with the headline on screen. Gaps between beats ≤0.4 s. End the CTA card about 0.5 s after the last word. Remove the gap after "Here are five" (or drop "Here are five" and keep "5 essay-ready words" only on the card).
2. **Make "essay-ready" true** (scenario-writer, then language-editor re-approval). Swap "Not only that" and "What's more" for formal connectors (e.g. "Further," / "In the same way,"; In addition/Additionally are kept out on purpose), or keep them and change the sub to "5 linking words" with a small "spoken" tag on the two informal ones. Rewrite the examples as essay sentences (e.g. "Moreover, online study saves travel time.").
3. **Add the subscribe/bell layer and meta** (shorts-builder): run subscribe_anim.py in the second half (about 10-12 s after the cut) and write subscribe_at into the meta. Optional (visuals): drop the red strike on "furthermore" or turn it into "(too often)", so the word doesn't look wrong.
