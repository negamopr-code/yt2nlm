# Viewer-critic review: l1-very-weird-rp-v1 (step 7b, 2026-10-14)

Video: `state/shorts/l1-very-weird-rp-v1/final.mp4` (= `/workspace/glottos-auto/out/l1-very-weird-rp-v1.mp4`, same md5), 1440x2560, 27.1 s, kokoro am_michael 1.05, no music.
Frames: `state/shorts/l1-very-weird-rp-v1/critic/f0.png f0.5.png f1.png f2.png f3.png` + beat midpoints f5.7, f9.2, f12.8, f16.7, f20.4, end f23/f24.5/f26, loop f26.8.

## Verdict: PARTLY
This is the strongest of the three on meaning, because the words really differ (creepy = scary, peculiar = unpleasant, surreal = dreamlike), and the creepy house and smelly fridge pictures carry that difference without reading. But the differences are printed, not spoken. The Bizarre pill says "**very** strange" in a video called "Stop saying very". "Odd" is weaker than "very weird", so it doesn't keep the "better word" promise. Three of the five cards run to 4 lines.

## Pain (learner words) -> what the video gives -> gap
Verbatim learner evidence (NotebookLM learner-comment sources vol. 1-4 + `content/insights/audience-needs.md`):
- "Very very thanks 😊"
- "very very nice more more video make you"
- "You are an amazing teacher: explain clearly, very profesionally, very very sympathic"
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them"
- "Can u help me how and when to use literally and basically"
- "It's great because it also gives you the context it can be used in and synonyms of the word"
- "but why?" (channel comment under a synonym Short)
- "Enraged and pissed off also work" (viewers add their own word)

Pain: "I say 'very weird' for everything strange and don't know which word fits which kind of strange." Solved = tomorrow I say "a peculiar smell" or "a creepy old house" and don't call a funny hat "creepy".

## Required checks
- 2(a) Promise without answer in the first 2 s: **YES.** 0-3.9 s shows only "Stop saying 'very weird'" (strike at about 0.5-1 s) and "5 better words" from about 2 s. The first answer, "Bizarre", is heard at 4.12 s and shown at 3.93 s. The background floats only "very weird".
- 2(b) Dead look repeated: **NO.** No clay mascot (anime bus stop, kawaii cat, sketch fridge, ink house, flat surreal), no answer in frame 0, no idiom badge.
- Spelled-out word: **none.**
- Repeat gap after each example (whisper): hat 6.26 -> 7.80 (1.5 s), noise 9.74 -> 10.92 (1.2 s), smell 13.48 -> 15.04 (1.6 s), house 17.38 -> 18.78 (1.4 s), scene 20.98 -> 22.30 (1.3 s). **OK**, but there's no "say it" cue. The subscribe animation starts at 22.0 s, inside the Surreal repeat gap.
- Closing heard: "Which word will you use?" 22.30-23.54 and "Comment your own word for very weird" 24.12-25.94. **YES.** Loops to the hook at 26.6 s.
- Text lines: **FAIL on 3 of 5 beats.** Bizarre ("very strange, hard to / believe"), Odd ("unusual, not what you / expect") and Peculiar ("strange, sometimes / unpleasant") each have headline + 2-line pill + example = 4 lines.
- Legibility: OK, with the same small-pill caveat.
- UI zones: the brand top bar is fine. The subscribe+bell sits bottom-left at about y 74%, OK but tight. The card's right edge sits under the like/comment rail.
- Picture vs words: the bizarre hat (a goldfish on a businessman's head, bystanders shocked) matches. **Odd noise = a cute cat staring at a fridge**: the "noise" is three faint squiggles and the question marks were cropped off, so it doesn't read as "noise". Peculiar smell (stink lines from a fridge, a man holding his nose) is excellent. Creepy house (moon, crow) is excellent. Surreal scene (melting clocks, flying whales) matches.
- NotebookLM/Gemini mark: present in the source PNGs, cropped out of the card. **None visible.**
- subscribe_at [22.0] recorded in `content/youtube/l1-very-weird-rp-v1.json`. OK.

## Second-by-second (where I'd swipe)
- 0-1.5 "Stop saying very weird": "weird" is a very common learner word, so this is the best hook phrase of the three.
- 1.5-3.5 "Here are five better words": text-only, the swipe-risk window.
- 3.9-22.3 five beats of 3.4-3.9 s. The creepy house at about 15 s is the visual peak.
- 22.0-26.6 close plus subscribe (it starts 0.3 s before the end card, over the Surreal repeat gap).

## Takeaway test
"For a bad strange smell say 'peculiar'; for strange-and-scary say 'creepy'." Nameable and genuinely useful.

## Retention risks
27.1 s, about 1 s longer than the winners. The hook is 3.9 s of text only. Three beats have 4 lines.

## Trust risks
- The Bizarre pill "**very** strange, hard to believe" uses "very" inside a "Stop saying very" video, so expect a mocking comment. Use "extremely strange" or "so strange it's hard to believe".
- "Odd" is milder than "very weird", so as a "better word for very weird" it's a downgrade. Fine as a word, wrong for the promise.
- "Creepy" changes the meaning (adds fear). The pill says so, but the voice doesn't, so a viewer may use "creepy" for any weird thing.

## Ship-blockers
None (no spelled word, no watermark, subscribe present and recorded, 1440).

## Top 3 fixes (by impact)
1. **scenario-writer + voice:** speak the short usage line, especially for Creepy ("strange and scary") and Peculiar ("strange and unpleasant"). That is exactly the "but why?" the viewers asked.
2. **language-editor:** remove "very" from the Bizarre pill and swap "Odd" for a word that is actually stronger than "very weird" (e.g. "outlandish" or "freaky", editor's call), or relabel it honestly.
3. **shorts-builder + visuals:** cap cards at 3 lines (Bizarre/Odd/Peculiar pills wrap; widen the pill box or cut to 3 words), add a "say it" cue in the repeat gap, start the subscribe animation after the end card begins (>= 22.3 s), and replace the Odd picture with one where the noise is visible.
