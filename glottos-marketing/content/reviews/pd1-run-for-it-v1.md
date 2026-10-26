# Viewer-critic review: pd1-run-for-it-v1 (public-domain situation test, 3 of 4)

Reviewed 2026-10-16. File `state/shorts/pd1-run-for-it-v1/final.mp4`: 1440x2560, 30 fps, video 11.47 s / audio 11.50 s. Unit `shorts/units/pd1-run-for-it-v1.json` (language hash 09bfdc437ecc6efa). Clip: Cops (1922).

## Verdict: PARTLY - 1 blocker
Best hook of the four (boss = a hundred cops is a real laugh), but 1.4 s of dead air right after it, and the three words sit on one undifferentiated crowd shot, so the picture never shows what makes bolt different from flee or run for it.

## Pain
Same evidence as the other pd1 reviews (no PROBLEM doc for this lane; no NotebookLM query spent):
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank."
- "great video but please shorten the intro!"
- "Enraged and pissed off also work" (viewers add their own words)

Pain in their words: "I say the same words all the time" - I only know "run away".
Solved means: tomorrow I can say "I bolted out of the meeting" and know "flee" is for news/books.

Gives: three correct words with meaning + register tag (flee = written, honestly marked). Gap: nothing shows HOW they differ (sudden start = bolt; escape danger = flee); no example of real use beyond "You bolt." / "You flee."; no self-test.

## What is heard (faster-whisper small.en)
0.00 Your boss says, got a minute. (whisper printed a full stop: the quoted question is read flat) / [1.66-3.07 silence, 1.41 s] / 2.92 You don't just leave, / 4.28 you run for it. / 5.72 You bolt, / 6.92 you flee. / 8.18 Which one do you do when your boss says, got a minute? (ends ~10.7, 0.8 s silence to loop). No spelled-out words.

## Second by second
- 0.0 Frame 0: 2-line hook "When your boss says: "Got a minute?"" + Keaton running down an empty street toward the crowd. Expert target met.
- 1.66-3.07 BLOCKER: 1.4 s with no voice, no new text, lower half empty. Caused by the forced `"at": 3.0` on beat 2. This is exactly where a scroller decides; nothing pulls me forward.
- 3.0-5.65 "run for it" card. During it Keaton leaves the frame and the crowd of police charges at the camera; the person who "runs for it" is not on screen, the chasers are. Confusing: who is "you"?
- 5.65-6.85 "bolt" card for 1.2 s - shortest card of all four videos.
- 6.85-11.5 "flee". Subscribe + bell 6.2-11.2, covers nothing, cursor moves under bolt/flee.
- 8.0 hook box becomes 1 line "Which one do you do?".
- 10.0 hard cut to a blurred close crowd (motion index jumps 8 -> 24).

## Word-picture match
run for it: weak (escapee off screen while the word is shown). bolt: no sudden start visible - same crowd shot continues. flee: generic crowd running, OK. The best "bolt" moment (Keaton turning and taking off) is at 0-2.5 s, under the hook, before any word.

## Loop
Audio: "...says, got a minute? / Your boss says, got a minute." - same phrase twice, works as a joke. Picture: hard visible restart - blurred close crowd -> wide empty street, word stack vanishes, hook grows from 1 to 2 lines.

## Takeaway test
"I bolted." is nameable but not taught in a usable sentence; PARTLY at most anyway.

## Retention risks
Dead air 1.66-3.07. Bolt card 1.2 s. Flat reading of "got a minute" weakens the joke.

## Trust risks
"You flee." as spoken reply about a boss with a "written" tag is honest but sounds odd in speech; acceptable because the tag says so.

## Blockers vs nice-to-haves
Blocker: 1.4 s dead air after the hook.
Nice-to-have: re-time picture so Keaton's take-off is under "bolt"; question intonation on "Got a minute?"; hold bolt >=1.8 s.

## Top 3 fixes
1. Remove the forced `"at": 3.0` (or fill the gap with the boss line text/voice) so speech flows from 0 to 3 s with <=0.5 s gaps (scenario-writer + shorts-builder).
2. Re-cut: Keaton turning and running under "run for it"/"bolt", the charging crowd under "flee" or the hook (visuals + shorts-builder).
3. Re-voice "Got a minute?" with question intonation (e.g. its own sentence) (voice).

---

## Second pass (re-render 16:43, language re-approved 16:36:40)
File now video 10.70 s, Cops 1017-1031. Subscribe 5.4 s, recorded in `content/youtube/pd1-run-for-it-v1.json`.

**Final verdict: SOLVES - no blocker. Weakest of the four.**

- Earlier blocker FIXED: the longest gap between lines is now 0.65 s (first pass: 1.41 s at 1.66-3.07). Transcript: 0.00 Your boss says, got a minute. / 2.24 You don't just leave, / 3.50 you run for it. / 4.90 You bolt, / 6.08 you flee. / 7.34 Which one do you do when your boss says, got a minute? The last line ends at about 9.9, with 0.82 s of silence before the loop. No spelled-out words.
- "Bolt" now matches very well. At 5.2-5.6 Keaton jumps up off the ground and sprints at the camera with the whole police force behind him, which is a sudden start.
- "Run for it" is still only partly matched. Zoomed frames at 2.2-4.8 show Keaton standing and facing the crowd, then falling flat at 3.8-4.8, which is exactly when "you run for it" is said (3.50-4.12). The real running is under the hook (0-1.9 s). A viewer gets the threat, but the picture under the word is a man falling, not escaping.
- The grey promise line "3 better ways to say 'leave'" disagrees with the title "Another Word for Run Away". "Bolt" and "flee" are closer to "run away" than to "leave".
- Loop: the picture still jumps hard from the full charging crowd (last frame) to the empty street with one small runner (frame 0). The audio loop works.
- "got a minute." is still read flat (whisper prints a full stop at 1.42).

Nice-to-haves: shift the in-point about 1.5 s so the fall lands under the hook and the take-off under "run for it"/"bolt". Align the promise line with the title ("run away" in both). Re-voice "Got a minute?" with question intonation.
