# Viewer-critic review: h98-revenge-part2-v1 (lab H98, Part 2 of "Stop Saying I Want Revenge" 2ozeoc1cv4Y)

Reviewed 2026-10-27. File `state/shorts/h98-revenge-part2-v1/final.mp4`: 1440x2560, 30 fps, 13.40 s, AAC 48 kHz. Unit `shorts/units/h98-revenge-part2-v1.json` (language hash 136ba682199b09d4). Clip: Big Business (1929), segments 904-906.8, 909-911.8, 912-914.8, 916-918.4. `final.subscribe.json` subscribe_at [7.0], corner bl.

## Verdict: PARTLY - 3 blockers, do not ship yet
The three expressions are correct and useful, the voice is clean, and "hit back" over a man swinging at a window is a great match. But it repeats Part 1's clipped promise line, the bell covers the "idiom" tag for about 2.5 s, and the spoken hook doesn't say what the neighbour DID. The metadata file that has to record subscribe_at does not exist.

## Pain (learner's words; no PROBLEM doc for this lane, same corpus evidence as pd2-get-even-v1; no NotebookLM query spent)
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank."
- "great video but please shorten the intro!"
- Viewers keep adding their own synonyms under "Stop Saying ..." Shorts ("Frigid too", "Melancholic too", "minuscule").
Pain: "I say the same words all the time". I always say "revenge".
Solved means: tomorrow I can say "I'll get back at him", "they hit back" or "she had the last laugh" without freezing.
What it gives: three correct phrases, each with a short meaning and a register tag. Gap: no self-test, and no example sentence beyond "You want to ...".

## What is heard (faster-whisper small.en, word timings)
0.00 Part 2. / 0.96 Your neighbor is back and now he's angry. / 3.50 You don't just want revenge. / 5.46 You want to get back at him. / 7.34 You want to hit back. / 8.92 You want to have the last laugh. / 11.08 Would you hit back or walk away? (ends 12.64). Every word is heard as written. NO spelled-out words ("neighbor" is just whisper's spelling). Gaps are about 0.6-1.0 s, with no dead air.

## Shot map of the final (frame-difference cuts)
0.0-2.2: Hardy in front of the house, crowd behind (dark, wide). 2.2-4.4: a man swings at the house window while a policeman watches. 4.4-5.6: the car wreck and the crowd in the street (a different shot, but the same feud). 5.6-13.4: house window smash, then from about 10.4 the man stays crouched in almost the same pose (low motion).

## Second by second
- 0.0-1.0 The yellow hook "Part 2: the neighbour strikes back" is over motion from frame 0. The spoken "Part two" takes 1 s before the situation starts. A viewer who missed Part 1 gets no context, and Part 2 viewers already know it.
- 0.0-4.9 BLOCKER: the promise "3 more ways to say 'get revenge'" is wider than the frame. The "3" is cut on the left and the closing quote on the right (checked at full size at 1.0 s), the same bug pd2-get-even-v1 had.
- 1.0-3.0 LOGIC: the voice says "now he's angry. You don't just want revenge." Him being angry is no reason for ME to want revenge. Only the card ("strikes back") says he did something. A B1 listener who reads less than they hear gets lost here.
- 4.4-5.6 A cut to the car-wreck street shot under "revenge" and the gap. It belongs to the same fight, so it reads OK, but it is a jump.
- 5.5-7.0 get back at someone / do something bad to someone who hurt you / everyday, over window smashing. Match. Minor: "you" sits alone on line 2.
- 7.0 Subscribe + bell at the bottom left: red SUBSCRIBE 7.0-8.6, click, SUBSCRIBED, bell rings, gone by about 12. It is visible, and 7.0/13.4 = 52%, so it is in the second half. OK.
- 7.3-8.6 hit back / answer an attack with an attack / everyday, over a man swinging at the window with a policeman beside him. Strong match.
- 8.9-10.7 have the last laugh / win in the end, after others laughed at you / idiom. BLOCKER: the bell icon sits on the yellow "idiom" tag from about 9.0 to about 11.5, so only "id" is visible. The picture is also weak: a man crouched in rubble, with nobody winning or laughing.
- 10.4-13.4 The man stays crouched almost still under the closing question, a near-freeze for about 3 s. That is where a viewer swipes.
- 11.0-12.6 "Would you hit back, or walk away?" is a good comment prompt. It is not a test.

## Loop
The tail (man crouched by the house) jumps to the dark wide crowd shot at 0.0, a visible seam. Audio: "...walk away? / Part two." with no echo.

## Takeaway test
"I'll get back at him for this." / "In the end, she had the last laugh." I can name an action, so PARTLY rather than DOESN'T. There is no moment where I test myself.

## Checklist
- 1440x2560: yes. Credit "Big Business (1929)" is shown. No watermark, no intertitle, no magnifying glass.
- Subscribe + bell at 7.0: present (overlap noted above).
- `content/youtube/h98-revenge-part2-v1.json` DOES NOT EXIST, so `"subscribe_at": [7.0]` is not recorded. Not finished.
- POLICY: none. 1929 slapstick property damage, nobody hurt, nothing sexual, safe for 13+.

## Retention risks
The 1 s spoken "Part two" intro. The near-still last 3 s. The about 30% empty black band at the bottom. At 13.4 s it is longer than Part 1 (12.3 s) with the same amount of content.

## Trust risks
The clipped promise looks broken. "he's angry" -> "you want revenge" doesn't follow. The definitions are correct (Cambridge-aligned, per the language-editor). The English is natural.

## Top 3 fixes (by impact)
1. shorts-builder: auto-fit the promise width (shrink the font or wrap it so it fits about 1300 px). Move the subscribe/bell lower, or put it at 5.5-7.5 so it clears the "idiom" tag. Write `content/youtube/h98-revenge-part2-v1.json` with `"subscribe_at"` from the re-render.
2. scenario-writer + language-editor: change the hook so the wrong is said out loud, e.g. "Part two: your neighbour is back, and he broke your window." Or drop "Part two" from the speech and keep it on the card only.
3. visuals / shorts-builder: replace the last segment (916-918.4, crouched near-still) with a high-motion shot for "have the last laugh" and the closing line, ideally someone grinning or the opponent losing, and make the last frame match frame 0 for the loop.
