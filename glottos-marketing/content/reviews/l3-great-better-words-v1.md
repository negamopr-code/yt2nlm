# Viewer-critic review: l3-great-better-words-v1 (lab H83 batch 3), 2026-10-17

**Verdict: SOLVES (narrow search intent).** A learner who types "another word for great" gets three words in 22.9 s: Excellent, Outstanding, Superb. Each is a safe swap for "great" in its usual meaning ("very good"), so the viewer can use one tomorrow without any further explanation. This is the cleanest word set in the H83 batches so far.

Technical checks: PASS. 1440x2560, 30 fps, 22.9 s, AAC 48 kHz. Every label is on one line ("extremely good", "far above average", "of top quality"). "Outstanding." is the longest headline and is shrunk to fit, with clear margins. Speech matches the cards word for word. Subscribe and bell are visible from 17.4 s (the CTA "Want" starts at 17.40); the click happens at about 18.9 s and "SUBSCRIBED" plus the ringing bell show at about 20.5 s, bottom-left above the UI zone. There is no magnifying glass, no garbled text and no word spelled letter by letter.

## Pain -> what the video gives -> gap
- Pain (corpus, verbatim): "my students always use good, bad and important as the holy trinity of adjectives in their essays, even though I always provide them a nice variety to choose from" / "when I want to use some of those, I am not very sure if that adjective actually exists in English language" / "great video but please shorten the intro!"
- In the learner's words: I keep saying "great", and I want a few real words I can use right away. "Solved" = in tomorrow's email or essay I write "excellent" or "outstanding" instead of "great".
- Given: Excellent (extremely good), Outstanding (far above average), Superb (of top quality). The hook comes in 0 s with no intro, which fixes the corpus complaint about intros.
- Gap: there is no example sentence. "Great" in other senses ("a great deal", "a great distance", "great!" as a reaction) is not covered, and nothing says that "superb" sounds a little formal or British. These are small gaps for a 23 s Short.

## Second by second (whisper small.en)
- 0.00-1.48 "Need another word for great?" The card is up at 0.3 s. It is the search phrase, so it stops the scroll.
- 2.2-3.7 "Here are three better words." The strike-through on "Great" is visible at about 3.0 s.
- 4.66 "Excellent." then a 1.5 s gap for the self-test, then 6.52 "Extremely good."
- 8.80 "Outstanding." then a 1.6 s gap, then 11.02 "Far above average."
- 13.34 "Superb." then a 1.2 s gap, then 15.18 "Of top quality."
- 17.40-21.12 CTA plus subscribe, then 1.8 s of tail.
- Swipe risk: only the planned silences after each word. These match the control, so they are not a variable in this test.

## Takeaway test
"Next time, write 'excellent work' or 'an outstanding result' instead of 'great'." A viewer can do this.

## Retention / trust risks
- The length fits the content. Text is large and each word stays on screen for about 4 s.
- No overclaims. The glosses are accurate and in plain English.
- Not finished per the subscribe rule: content/youtube/l3-great-better-words-v1.json has NO "subscribe_at" (and no language_approval block, which the change/ensure metas have). Required value: [17.4].

## Top 3 fixes (by impact)
1. shorts-builder/publisher: add "subscribe_at": [17.4] (and the language_approval block) to content/youtube/l3-great-better-words-v1.json before sending. Do the same for different [17.4], help [16.2] and show [16.2].
2. scenario-writer (next version, not this A/B): one 2-word usage line per word, e.g. "excellent work", "an outstanding result", "a superb meal".
3. language-editor (optional): note that "superb" is slightly formal/British. Not needed for this test.

## Siblings (visual checks only)
- l3-different-better-words-v1: PASS. 1440x2560, 23.0 s. Labels on one line. The hook "Different" fits. Speech = cards. Subscribe visible at 17.4 ("Want" 17.30). Content note: "Diverse" only replaces "different" for groups ("different/diverse backgrounds"), and the label "of many kinds" is honest about that.
- l3-help-better-words-v1: PASS. 1440x2560, 21.6 s. Labels on one line. Speech = cards. Subscribe at 16.2 ("Want" 16.24). The CTA headline fits on 2 lines.
- l3-show-better-words-v1: PASS. 1440x2560, 21.7 s. Labels on one line. Speech = cards. Subscribe at 16.2 ("Want" 16.30). Content note: "Prove" changes the meaning (the label says so).
- All 4: subscribe_at is missing from the content/youtube meta json (only in final.subscribe.json).
