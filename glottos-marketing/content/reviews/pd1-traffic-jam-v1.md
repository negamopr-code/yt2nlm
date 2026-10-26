# Viewer-critic review: pd1-traffic-jam-v1 (public-domain situation test, 1 of 4)

Reviewed 2026-10-16. File `state/shorts/pd1-traffic-jam-v1/final.mp4`: 1440x2560, 30 fps, video 11.53 s / audio 11.60 s. Unit `shorts/units/pd1-traffic-jam-v1.json` (language hash 34540849355667d9). Clip: Two Tars (1928).

## Verdict: PARTLY - 1 blocker
The hook and the words are right and usable tomorrow, but the picture contradicts the strongest word: under "gridlock" ("nothing moves at all") the clip shows its most motion of the whole video.

## Pain
No PROBLEM doc or `content/problems/` exists for this lane (same gap as earlier reviews); no NotebookLM query spent. Evidence used (verbatim, from the corpus and channel comments already logged in `content/insights/`):
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank."
- "great video but please shorten the intro!"
- viewers adding their own synonyms: "Frigid too", "Melancholic too", "Enraged and pissed off also work"
- "give me please these words word or pdf file, please"

Pain in their words: "I say the same words all the time" - every jam is just "slow traffic".
Solved means: tomorrow at work I say "Sorry, I got stuck in traffic" or "it was bumper-to-bumper", and I know "gridlock" is the news word.

Gives: three correct expressions with a short meaning and a register tag, each said in a full sentence, recap row of earlier words. Gap: no example of me using it ("I got stuck in traffic"); no test moment; gridlock not shown visually.

## What is heard (faster-whisper small.en)
0.00 Monday morning, / 1.38 the traffic isn't just slow. / 3.40 You're stuck in traffic. / 5.10 The cars are bumper(-to-)bumper, / 7.16 total gridlock. / 8.76 So which one is your Monday morning? (ends ~10.8, 0.8 s silence to loop).
"to" in bumper-to-bumper lasts 0.16 s: whisper small.en on the full mix printed "bumper bumper"; on the line alone it printed "bumper to bumper". The word is there but swallowed. No spelled-out words.

## Second by second
- 0.0 Frame 0: 2-line yellow hook "POV: Monday morning commute" + long queue of 1920s cars on a country road. It reads as a jam instantly. Expert target met (hook + moving clip at frame 0, 2 lines).
- 0.0-3.3 Bottom ~45 % of the screen is empty black; the clip is a fairly static queue (motion index 5, lowest of the video). Mild swipe risk at 2-3 s: nothing has happened yet, no word on screen until 3.3 s.
- 3.3-5.07 "stuck in traffic" card (1.75 s). The 9-word meaning "unable to move because there are too many cars" is too long to read in 1.75 s while listening.
- 5.07-7.2 "bumper-to-bumper": cut to close cars side by side. Fine match.
- 6.2-11.2 subscribe + bell, under the tag, covers nothing; the moving cursor competes with the word card for the eye.
- 7.2-11.5 "gridlock": the clip has its highest motion here (index 24-26 vs 5-8 under "stuck in traffic"), cars and people visibly moving. Contradicts "nothing moves at all". BLOCKER.
- 8.7 hook box changes to "Which one is your Monday morning?". Comment prompt, not an outro.

## Loop
Audio: "...your Monday morning?" -> "Monday morning, the traffic..." works well. Picture: hard reset visible - word stack vanishes, hook text swaps, and the clip jumps from a close-up of moving cars to the wide queue. The loop is heard, but it is seen as a restart.

## Takeaway test
"I got stuck in traffic this morning" - yes, one clear action. The card text does not give that sentence; the voice says "You're stuck in traffic", close enough.

## Retention risks
12 s for 3 words is right. First word only at 3.3 s; empty lower half before that. Card 1 meaning too long for its 1.75 s. Clip has no visible gag in the used shots (Two Tars is famous for wrecking cars; none of it is here) - the "funny, memorable" part of the format is missing in this one.

## Trust risks
Gridlock picture vs meaning (above). Tags OK (gridlock = news, per language editor). Hook "commute" with a 1920s country road is a fine joke, not a contradiction.

## Blockers vs nice-to-haves
Blocker: gridlock over the busiest footage.
Nice-to-have: louder/clearer "to" in bumper-to-bumper; shorter meaning for card 1 ("can't move, too many cars"); use the car-wreck gag shot somewhere.

## Top 3 fixes
1. Re-cut the clip so the most static, packed shot sits under "gridlock" and a crawling shot under "bumper-to-bumper" (visuals + shorts-builder).
2. Shorten the stuck-in-traffic meaning to <=6 words, or hold it 2.5 s (scenario-writer / language-editor).
3. Re-render the bumper-to-bumper line so "to" is audible (try speed 1.0 or "bumper to bumper" text) (voice).

---

## Second pass (re-render 16:49, language re-approved 16:36:40)
File now video 11.80 s / 1440x2560 / 30 fps. Segments: Two Tars 547-552 (still queue) -> 552-554.2 (cars pulling up close) -> 547-551.8 (still queue again). Subscribe 6.4 s, recorded in `content/youtube/pd1-traffic-jam-v1.json`.

**Final verdict: SOLVES - no blocker.**

- Earlier blocker FIXED: clip motion under "gridlock" (spoken 7.54) is now 4.8-5.6, which is as still as the hook shot (first pass: 24-26). The busy close-up (17-25) now sits only under "bumper to bumper" (5.10-6.42), where movement fits.
- "to" is now heard: whisper on the full mix prints "bumper@5.94 to@6.20 bumper@6.42". The card keeps the hyphen, which is correct for the adjective.
- New grey promise line "3 better ways to say 'slow'" fills the empty lower half from 0 to 3.3 s. At phone width it is readable but dim. It is good because it tells me what I will get before the first card.
- Loop: the last frame and frame 0 are both the wide still queue, so the picture seam is nearly invisible. Only the word stack and hook text reset. Audio "...your Monday morning? / Monday morning, the traffic..." works.
- Gaps between lines are at most 0.64 s, with 0.84 s of tail silence before the loop. No spelled-out words.

Nice-to-haves (not blocking): card 1 meaning is still 9 words in 1.75 s. "Gridlock" reuses the hook footage, so the same 4 s are seen twice. The Two Tars car-wrecking gag is still unused.
