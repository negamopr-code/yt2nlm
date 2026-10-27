# Viewer-critic review: h95-experience-v1 (lab H95 "Shorts as search answers"), 2026-10-27

**Verdict: PARTLY.** The first spoken words are exactly what the learner typed and three answers come within 13 s, so it does answer the search. But all three words are for work or CV "experience" and the video never says so. There is no example sentence. "Expertise" is not the same as experience. And the H95 test change ("answers on the hook card at frame 0") is NOT in the render: the answers appear at about 2.2 s.

Ship blockers: 1 (lab validity, see below). POLICY: clean (no hit).

Technical: 1440x2560, 30 fps, 23.9 s. Logo is the channel avatar. No watermark. No magnifying glass. Nothing spelled letter by letter. Subscribe and bell: fading in after 16.6 s, "SUBSCRIBE" with cursor at about 17.5 s, "SUBSCRIBED" by 19.5 s, bottom-left, does not cover the cards. `subscribe_at: [16.6]` is in content/youtube/h95-experience-v1.json and matches final.subscribe.json.

## Pain (learner's words) -> what the video gives -> gap
There is no PROBLEM document for this lab word. The pain is the search intent "another word for experience". Corpus comments show how learners really use the word (verbatim, from reports/monitor-awf/archives/youtube-comments-vol*.md):
- "I hope to get a great experience with you"
- "make the learning experience enjoyable and effective"
- "Your video makes me feel it's just an enjoyable experience for English learners"
- "Your teaching experience is so awesome"
- "we have more experience and found further vocabulary"
- "it was by far the most challenging experience"
- "thanks For sharing your knowledge and experience"

The pain in one sentence: "I use 'experience' for everything (a great experience, my experience, more experience) and I want a different word that fits my sentence."
"Solved" would mean that tomorrow they can swap experience in a CV line or a thank-you comment and the result is still correct English.

What the video gives: Background (your work history), Expertise (great skill in one area), Know-how (skill you learned by doing).

Gaps:
1. Only one sense is covered. Most corpus uses are the EVENT/FEELING sense ("a great experience", "learning experience", "challenging experience"). None of the three words fits those. Nothing on screen says "for your CV / at work", so a searcher with the event sense learns nothing they can use and may misuse what they learned.
2. There is no frame for the words. Learners will write "I have 5 years of background in sales" or "I hope to get a great expertise with you". Both are wrong. The video needs one line like "My background is in sales" / "years of experience -> my background is in".
3. "3 better words" overclaims. These are not better replacements. Expertise means skill level, not time spent doing something. Calling it "better" invites the swap error.

## Second by second (whisper small.en, word timings)
- 0.00: the first frame shows only "Another word for". "experience" (yellow) is visible from about 0.3 s. The answer line "Background. Expertise. Know-how." is NOT on screen at 0.03, 0.4, 1.0 or 2.0 s. It appears between 2.0 and 2.4 s. So the frame-0 promise of the H95 test is not met.
- 0.00-1.56 "Another word for experience." It is the exact search phrase and the first sound, so a searcher stops. Good.
- 1.76-2.27 silence 0.5 s, then 2.40-3.84 "Here are three better words." That is a 2.3 s filler line in a 24 s Short. A searcher has already seen the answers on the card by 2.4 s, so this is a mild swipe point.
- 3.8-4.6 silence 0.8 s (transition).
- 4.6 "Background." 5.4-6.6 silence 1.3 s (self-test gap, same as the control). 6.50-7.58 "Your work history." The sub-label shows with the voice (not on screen at 6.0 s). Picture and voice in sync.
- 8.96 "Expertise." 9.7-10.9 silence 1.2 s. 11.04-12.32 "Great skill in one area."
- 13.54 "Know-how." 14.1-15.3 silence 1.2 s. 15.50-16.60 "Skill you learned by doing." Whisper hears "learn" both in the full file and in the clip on its own, while the card says "learned". The -ed is swallowed before "by". Small mismatch between ear and eye. Low risk.
- 16.6-17.8 silence 1.1 s while the subscribe button fades in.
- 17.72-22.08 CTA "Want more words for experience? Find them on anotherwordfor dot net." Whisper writes "anatherwordfor", which is the TTS vowel. The card spells it correctly.
- 22.16-23.90 1.7 s of silent tail on the CTA card.
- Swipe risk: four gaps of about 1.1-1.3 s (5.4, 9.7, 14.1, 16.6) plus 1.7 s at the end. That is about 6.5 s of silence in 23.9 s (27%). The gaps after the words are a deliberate self-test and the same as the control, so they are not a variable here. The gap at 16.6 (no test in it) and the tail are dead air.

## Takeaway test
The best case: "On my CV I write 'My background is in sales' / 'I have know-how in X'". The video doesn't show these sentences. A B1 viewer can only do this if they already know the patterns. Many will build "years of background", which is wrong. So the takeaway is weak. That caps the verdict at PARTLY.

## Retention risks
- Length fits the content (24 s, 3 words). The cards are large, high contrast, on one or two lines, and on screen for 3-4 s. Easy to read. The background word cloud is dim and does not compete with the cards.
- The filler line "Here are three better words" at 2.4-3.8 s repeats what the card already shows.
- 27% silence (see above). The tail after 22.1 s is dead air.

## Trust risks
- "Better words" + "Expertise" = experience is a meaning shift that isn't labelled as one. A learner who knows the difference ("experience = time doing it, expertise = how good you are") will doubt the channel.
- The sense is not labelled. The title and tags promise general synonyms ("synonyms for experience"), but the content only covers the CV sense. Not misleading enough to break the rules, but it disappoints anyone who searched with the event sense.
- "learned" heard as "learn" (16.0 s). Minor.
- No factual errors in the glosses themselves (the language-editor fixes hold).

## Ship blockers
1. **Lab H95 variable missing (frame 0).** The unit's lane note says the one change vs the control is "the first answers sit on the hook card at frame 0". In final.mp4 the answer line appears at about 2.2 s, and at frame 0 even "experience" is not visible yet. If this ships as H95, the test measures the exact-phrase speech only and the search-share result can't be credited to answers-at-frame-0. Fix: put the sub line (and the yellow keyword) on screen from frame 0, with no entrance animation on the hook card (shorts-builder). Or rewrite the lane note to say the variable is only the spoken phrase (scenario-writer). Note for the "Another word for X" checklist: the exact phrase is heard at 0.00-1.56 s, OK. Checklist items (b), (c) and (d) are for long videos and do not apply to this 3-word Short (no quiz, no "blank").

## Top 3 fixes (by impact)
1. **shorts-builder:** render the hook card complete at frame 0 (headline + "Background. Expertise. Know-how."), so that H95 is what it says. Also cut the 1.7 s tail and the 1.1 s gap at 16.6 s (the subscribe animation can run over the CTA voice).
2. **scenario-writer + language-editor:** label the sense and give each word a frame. Hook sub: "At work / on your CV". Sub-labels, for example: "Background: 'My background is in sales.'", "Expertise: how good you are", "Know-how: practical skill". Change "3 better words" to "3 words for your CV". A second Short can cover the event sense (a great experience -> "a great time", "an adventure", "it was fun").
3. **scenario-writer:** replace the filler "Here are three better words." with the first answer, or with "For your CV:". That saves about 2 s and matches the card the searcher already sees. **voice:** re-take "learned" so the -ed is heard (or the card says "skill you get by doing").

Checked: the unit json, the meta json, final.subscribe.json, 24 frames (hook 0.03/0.4/1.0/2.0/2.4/3.0, every beat, subscribe 15.5-19.5, tail 21.5-23.8), the full whisper transcript plus 2 clips transcribed on their own, silencedetect (-40 dB, 0.5 s), and corpus comments.
Not checked: there is no PROBLEM document and no article for this lab word, and no NotebookLM query was made. I did not compare frame by frame with the l3-but-better-words-v1 render. Whether search traffic comes is a day-7 Studio metric.

## Re-check (2026-10-27, re-render v2)
**Verdict: PARTLY (unchanged).** Ship blockers: 0. The frame-0 blocker is fixed. The content gaps (no CV/work label, no example frame, "better words", "expertise" is not the same as experience) are still in the video because the text was not changed. They are logged as follow-ups for the next H95 words, so they do not block this lab cell. POLICY: clean.

- **Frame 0 (blocker 1): FIXED.** Frames at 0.000, 0.5, 1.5 and 2.4 s all show the full hook card: "Another word for" + yellow "experience" + "Background. Expertise. Know-how." At frame 0 the card is slightly smaller (it scales up by 0.5 s), but every word can be read. H95 now tests what its lane note says.
- **Technical:** 1440x2560, 30 fps, 22.80 s (was 23.9). Logo is the channel avatar. No watermark. Nothing spelled letter by letter.
- **Tail:** the voice ends at 22.08 s and the silence after it is 0.66 s (was 1.7 s). OK.
- **Subscribe:** final.subscribe.json `[15.5]` matches content/youtube/h95-experience-v1.json `"subscribe_at": [15.5]`. At 15.5 s the screen is still clear. By 16.5 s the red SUBSCRIBE button and cursor are on screen. At 18.0 s it shows SUBSCRIBED + bell, and it is gone by 22.5 s. It sits bottom-left and covers no card. It now fills the 16.63-17.77 s gap (1.15 s with no voice), so that gap is no longer dead picture.
- **Transcript (whisper small.en)** is the same as v1, shifted: "Another word for experience" 0.00-1.56; filler "Here are three better words" 2.40-3.84; Background 5.10; Expertise 8.96; Know-how 13.54; "Skill you learn by doing" 15.50 (the -ed is still not heard, but the card says "learned"); CTA 17.72-22.08 ("anatherwordfor" TTS vowel, spelled correctly on the card).
- Still open (not blockers): fixes 2 and 3 from the first review (scenario-writer/language-editor: sense label + example frame + drop "better"; voice: "learned").

Checked: ffprobe; 12 frames (0, 0.033, 0.5, 1.5, 2.4, 6.5, 11, 15.5, 16.5, 18, 20, 22.5); full whisper transcript with word timings; silencedetect (-40 dB, 0.5 s); subscribe json vs meta json. Not checked: I did not watch the whole video frame by frame; search traffic is a day-7 Studio metric.
