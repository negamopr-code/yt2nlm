# Viewer-critic review: l3-but-better-words-v1 (lab H83 batch 2), 2026-10-17

**Verdict: PARTLY.** It is a clean 22 s Short that answers the search "another word for but" with three words and a label for each, but only "However" gives a learner something to do tomorrow. "Yet" ("for a surprise") is too vague to use, and the video never shows a sentence or the punctuation "however" needs.

Technical checks: PASS. 1440x2560, 30 fps, 21.9 s. All word cards fit on one line above the bottom UI zone. Speech matches the cards. Subscribe and bell are fully visible at 16.6 s (fade-in about 16.5 s, "SUBSCRIBED" at about 17.6 s, at about 74% of the height, bottom-left). No magnifying glass, no stray text, nothing spelled letter by letter.

## Pain -> what the video gives -> gap
- Pain: a learner types "another word for but" and wants three replacements they can use, each with when to use it. Corpus evidence of the real error: "it does mean the same thing, however it sounds really funny and unnatural to say" (comma splice with however).
- Given: Yet (for a surprise), However (for formal writing), Except (to leave one out).
- Gap: there is no example sentence. The video doesn't show "; however," or "However," at the start of a sentence, so the comma-splice error stays. "Except" changes the meaning (exception, not contrast), and its label is honest but a learner can't put it in for "but" in most sentences.

## Second by second (whisper small.en)
- 0.0-4.3 hook "Don't just say "But"", struck through at about 2.5 s, "3 better words". Strong stop: it is the search phrase. Whisper writes "butt", which is the same sound, so no issue.
- 4.5 "Yet." then 1.2 s of silence, then "for a surprise" (5.8-6.9). The pause is the self-test gap, as in the control.
- 8.3 "However." then 1.4 s of silence, then "for formal writing" (10.1-11.1).
- 12.9 "Except." (base.en hears "Accept", small.en hears "Except" when the clip is played alone) then about 1.5 s of silence, then "to leave one out" (14.4-15.0). Light risk: accept/except is a classic learner confusion. The card spells it right.
- 16.4-20.1 CTA "Want more words for but? Watch the full lesson on this channel." Then 1.8 s of tail.
- Swipe risk: the silences after each word (about 1.2-1.5 s) at 4.5-5.8, 8.6-10.1 and 13.0-14.4. They are by design (the same as the control), so they are not changed in an A/B test.

## Takeaway test
"In a formal email, start the sentence with However, instead of but." A viewer can do this, but only if they already know the punctuation. Nothing for Yet or Except.

## Retention / trust risks
- Length fits the content (22 s, 3 words). Text is large and on screen for 3-4 s each.
- Confound for H83: this is NOT the control "beat for beat". The control (Amazing) has no sub-labels under the words, an "EP 18" badge, and the CTA "Want 10 words for amazing?". This copy adds labels, has no EP badge and uses "Want more words". That is 3 or more changed variables, not one.
- `subscribe_at` [16.6] is only in state/shorts/l3-but-better-words-v1/final.subscribe.json. No content/youtube/*.json mentions this id yet, so the :8093 card can't show it.

## Top 3 fixes (by impact)
1. scenario-writer: record the label/badge/CTA differences from the control in the H83 lane note (or accept them as the new control). Otherwise the result can't be put down to the word.
2. scenario-writer + language-editor (next version, not this test): Yet label -> "but surprising" / show "simple yet strong"; However card sub -> "However, ... (new sentence)".
3. publisher/shorts-builder: put "subscribe_at": [16.6] into the video's content/youtube meta json when it is created.
