# Viewer-critic review: l1-very-quiet-rp-v2 (step 7b, 2026-10-14)

Video: `state/shorts/l1-very-quiet-rp-v2/final.mp4` (= `/workspace/glottos-auto/out/l1-very-quiet-rp-v2.mp4`, same md5), 1440x2560, 27.8 s, kokoro am_michael 1.05, no music.
Frames: `state/shorts/l1-very-quiet-rp-v2/critic/f0.png f0.5.png f1.png f2.png f3.png` + beat midpoints f5.9, f9.6, f13.2, f17.1, f21.0, end f23.5/f25/f26.5, loop f27.5.

## Verdict: PARTLY
These are the best usage lines of the three ("no sound at all", "quiet on purpose", "calm places, often in nature"), and they really separate the words. They are still only printed, never spoken. Two pictures fight the words (Soft-spoken shows a grandmother with a toddler, not a teacher; Tranquil is an abstract geometric mountain where the "lake" is a reflection band). Nothing invites me to repeat.

## Pain (learner words) -> what the video gives -> gap
Verbatim learner evidence (NotebookLM learner-comment sources vol. 1-4 + `content/insights/audience-needs.md`):
- "Very very thanks 😊"
- "very very nice more more video make you"
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them"
- "Can u help me how and when to use literally and basically"
- "It's great because it also gives you the context it can be used in and synonyms of the word"
- "but why?" (channel comment under a synonym Short)
- "Frigid too" / "Melancholic too" (viewers add their own word)

Pain: "I say 'very' plus the same adjective every time and don't know which stronger word fits which situation." Solved = tomorrow I say "the library was silent" or "she's soft-spoken" and I know that "hushed" is for voices, not places.

Gives: 5 well-chosen, clearly different words, each with a usage pill and a collocation ("in a hushed voice" is a real chunk). Gap: the differences live in the silent pill. The ear only gets "Hushed: in a hushed voice."

## Required checks
- 2(a) Promise without answer in the first 2 s: **YES.** 0-4.0 s shows only "Stop saying 'very quiet'" (strike at about 0.5-1 s) and "5 better words" (pops in at 2 s). The first answer, "Silent", is heard at 4.32 s and shown at 4.02 s.
- 2(b) Dead look repeated: **NO.** No clay mascot (editorial classroom, anime library, marker sunrise, kawaii grandma, flat geometric mountain), no answer in frame 0, no idiom badge.
- Spelled-out word: **none** ("Soft-spoken" read as two words, fine).
- Repeat gap after each example (whisper): classroom 6.60 -> 8.14 (1.5 s), voice 10.04 -> 11.48 (1.4 s), morning 13.70 -> 15.20 (1.5 s), teacher 18.04 -> 19.42 (1.4 s), lake 21.56 -> 22.86 (1.3 s). **OK (>= 1 s)**, but there's no "say it" cue.
- Closing heard: "Which word will you use?" 22.86-24.04 and "Comment your own word for very quiet" 24.62-26.48. **YES.** Loops to the hook at 27.3 s.
- Text lines: **FAIL on 1 of 5 beats.** Tranquil has headline + 2-line pill ("calm places, often in / nature") + example = 4 lines. The others have 3. The Soft-spoken headline is long but fits.
- Legibility: OK. The pill is about half the headline size.
- UI zones: the brand top bar is fine. The subscribe+bell sits bottom-left at about y 74% from 22.7 s, OK but tight. The card's right edge sits under the like/comment rail (the right-hand trees on Tranquil).
- Picture vs words: the silent classroom matches. "Hushed" (girls whispering with a finger on the lips) is the best picture of the batch. Peaceful shows a sunrise (the steaming cup is cropped away), OK. **Soft-spoken teacher shows a grandmother and a toddler**, so a viewer may store "soft-spoken = grandma". **Tranquil lake is a geometric mountain**; the lake is only the mirrored lower half, hard to read in 3.6 s.
- NotebookLM/Gemini mark: present bottom-right in the source PNGs, cropped out of the card. **None visible.**
- subscribe_at [22.7] recorded in `content/youtube/l1-very-quiet-rp-v2.json`. OK.

## Second-by-second (where I'd swipe)
- 0-1.5 "Stop saying very quiet": text-only. "Very quiet" is a plausible learner phrase, but a weaker hook than an emotion or feeling.
- 1.5-2.1 gap, then 2.1-3.5 "Here are five better words": this is the swipe-risk window, a black screen with no movement but the strike.
- 4.0-22.8 five beats, 3.4-4.2 s each. Good pace.
- 15.0-19.2 Soft-spoken: the longest beat (4.18 s). The picture mismatch costs trust, not retention.
- 22.8-27.3 close plus subscribe.

## Takeaway test
"Say 'silent' when there is no sound at all, and 'in a hushed voice' when someone speaks quietly on purpose." Nameable.

## Retention risks
27.8 s, about 2 s longer than the winners. The 4 s text-only hook (same as the winners). The pill reading load.

## Trust risks
- Soft-spoken picture contradicts "teacher".
- "Silent" is not a stronger "very quiet" for people ("he is very quiet" is not "he is silent"); the pill "no sound at all" covers it. OK.
- Tranquil picture: no visible lake.

## Ship-blockers
None (no spelled word, no watermark, subscribe present and recorded, 1440).

## Top 3 fixes (by impact)
1. **scenario-writer + voice:** speak the 3-4 word usage line ("Hushed, quiet on purpose: in a hushed voice"). The pills are already good, so make them heard.
2. **visuals:** redo Soft-spoken (a teacher talking gently to a class) and Tranquil (a clearly visible still lake, not abstract geometry).
3. **shorts-builder:** keep cards at 3 lines max (Tranquil pill wraps; widen the pill or shorten it to "calm, often in nature") and add a short "say it" cue in the 1.3-1.5 s repeat gap.
