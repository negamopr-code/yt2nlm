# Viewer-critic review: pd1-cramped-v1 (public-domain situation test, 2 of 4)

Reviewed 2026-10-16. File `state/shorts/pd1-cramped-v1/final.mp4`: 1440x2560, 30 fps, video 11.90 s / audio 12.01 s. Unit `shorts/units/pd1-cramped-v1.json` (language hash 727bb5cb31a594f0). Clip: Berth Marks (1929).

## Verdict: SOLVES - no blocker
The best of the four: one continuous shot of Laurel and Hardy squashed into a tiny bunk, and every word (cramped, a tight squeeze, packed like sardines) is visibly true on screen while it is said.

## Pain
Same evidence as the other pd1 reviews (no PROBLEM doc for this lane; no NotebookLM query spent):
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank."
- "great video but please shorten the intro!"
- "Frigid too" / "There is also minuscule as in a minuscule mouse." (viewers add their own words)

Pain in their words: "I say the same words all the time" - every small space is "very small".
Solved means: tomorrow I say "the hotel room was cramped" or "it's a tight squeeze in the car".

Gives: three correct expressions with meaning + tag, each in a full sentence, and a picture that makes all three obvious. Gap: no self-test; "packed like sardines" for two people is a slight stretch (sardines = many), but the image sells it.

## What is heard (faster-whisper small.en)
0.00 You booked the cheapest room. / 2.00 The room isn't just small, / 3.46 it's cramped. / 4.68 It's a tight squeeze. / 6.42 You're packed like sardines. / 8.32 Ever slept like this because you booked the cheapest room? (ends ~11.4, 0.57 s silence to loop). All words heard as written. No spelled-out words.

## Second by second
- 0.0 Frame 0: 2-line hook "POV: you booked the cheapest room" + the two men already fighting for space in the bunk. Expert target met.
- 0.0-3.6 Lower ~45 % of the screen empty black until the first card. The clip is funny enough to hold me here.
- 3.6-4.65 "cramped" card appears on the spoken word (3.62). Good sync.
- 4.65-6.32 "a tight squeeze" (1.7 s), meaning 3 words - readable.
- 6.32-11.9 "packed like sardines" (idiom tag). Subscribe + bell 6.6-11.6 under the tag, covers nothing.
- 8.3 hook box becomes 1 line "Ever slept like this?".

## Word-picture match
cramped: yes (bunk too small for two). tight squeeze: yes (they twist to fit). packed like sardines: yes (pressed side by side). Small mismatch: the hook says "room" and the picture is a train sleeping berth, dark top band. Few viewers will care.

## Loop
Picture: near-seamless - same shot, same framing at the seam; only the word stack disappears and the hook text swaps back. Audio: "...because you booked the cheapest room. / You booked the cheapest room." - the same sentence twice in a row. It loops, but it sounds like an echo; a viewer who notices may feel the repeat.

## Takeaway test
"My hotel room was cramped." Clear, usable tomorrow.

## Retention risks
Footage is dark (low contrast on a phone in daylight). Empty lower half 0-3.6 s. Subscribe cursor moves under the idiom while I am reading it.

## Trust risks
None of substance. Tags match the language editor's Longman checks.

## Blockers vs nice-to-haves
Blocker: none.
Nice-to-have: lift the clip brightness/contrast; end line without repeating the hook verbatim (e.g. "Ever slept like this?" only, so the loop lands on "You booked the cheapest room" fresh).

## Top 3 fixes
1. Shorten the closing line to "Ever slept like this?" so the loop does not say the same sentence twice (scenario-writer, then language-editor).
2. Brighten the clip (curves/contrast) for phone viewing (visuals / shorts-builder).
3. Put something in the empty lower half for 0-3.6 s (e.g. the hook word "small" struck out, or a larger clip crop) (shorts-builder).

---

## Second pass (re-render 16:49, language re-approved 16:36:40)
File now video 10.20 s. Closing line is "Ever slept like this?". Subscribe 5.2 s (51 % of the length, just inside the second half), recorded in `content/youtube/pd1-cramped-v1.json`.

**Final verdict: SOLVES - no blocker.**

- Transcript: 0.00 You booked the cheapest room. / 1.98 The room isn't just small, / 3.46 it's cramped. / 4.66 It's a tight squeeze. / 6.40 You're packed like sardines. / 8.26 Ever slept like this? Speech ends at 9.54, with 0.67 s of silence before the loop. Every line is heard as written; no spelled-out words.
- The earlier echo is FIXED: the loop now runs "Ever slept like this? / You booked the cheapest room." with no repeated sentence. The picture seam is still the same continuous bunk shot.
- Grey promise line "3 better ways to say 'small'" shows from 0 to 3.6 s. It fills the empty half and is readable.
- Word-picture match unchanged and strong for all three words.

Nice-to-haves: the footage is still dark (low contrast on a phone). The subscribe button is still fading out in the last 0.3 s, so it vanishes abruptly at the loop point. Room vs train berth is a minor mismatch.
