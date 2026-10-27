# Viewer-critic review: pd5-furious-v1 (lab H94: conflict hook + action at frame 0, old-movie situation Short)

Reviewed 2026-10-27. File `state/shorts/pd5-furious-v1/final.mp4`: 1440x2560, 30 fps, 10.30 s, AAC 48 kHz stereo. Unit `shorts/units/pd5-furious-v1.json` (language hash 0be965431ababa22). Clip: The Battle of the Century (1927), credited under the picture. Subscribe at 5.2 s (recorded in `content/youtube/pd5-furious-v1.json`).

## Verdict: PARTLY - no ship-blocker
It's shippable and policy-clean. Frame 0 is action, the three words are correct, and the cards are synced. But it gives three labels and almost no way to use them: each word only appears in "You're X." The furious beat shows a laughing crowd throwing pies, not an angry face. There is no self-test either. A learner leaves with three new words on screen, not something they'll say tomorrow.

## Pain
There is no PROBLEM doc for this lane (as with the other pd reviews). No NotebookLM query was spent. These are verbatim corpus lines, already sourced in `content/reviews/long-another-word-for-angry-v1.md`:
- "I can understand what you say clearly , the point is that when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "when I'm in front of people I forget how to speak or I forget the words"
- "my pronunciation and conversation and vocabulary is small, Please help me with advice."
- "great video but please shorten the intro!"

The pain in their words: "I say the same words all the time". For anger, that means "angry" or "very angry" every time.
What solved looks like: tomorrow I say "I was fuming when my roommate ate my lunch" or "My boss was livid", and I know which one is stronger.

What the video gives: furious, fuming and livid, each with a 3 to 5 word meaning and a register tag, in a relatable POV situation.
The gap:
- No sentence beyond "You're furious." There's no "furious about / with", no past tense, no "I was fuming when...".
- No moment where I pick the right word.
- The "often quietly" nuance of fuming is in small text for about 1.3 s.

## What is heard (faster-whisper small.en, word timings)
0.00 Your roommate ate your lunch. / 1.98 You're not just angry. / (1.0 s pause 2.9-3.96) / 3.96 You're furious. / 5.40 You're fuming. / 6.68 You're livid. / 7.84 Would you shout or say nothing? (ends ~9.3, about 1 s to the loop seam).
Every word is heard as written. No spelled-out words. No intro or chatter.

## Second by second
- 0.0: The yellow 2-line hook "POV: your roommate ate your lunch" sits over a full street pie fight already in motion, with "3 better ways to say 'angry'" in grey. The H94 target is met: there is action and a conflict at frame 0. I stop.
- 0.0-3.9: The bottom ~40% of the screen is empty black. At 1.5 there's a cut to the lady sitting in the car, serious, and then back to the crowd.
- 2.9-3.96: A 1 s silence after "not just angry". It reads as a dramatic beat, but in a 10 s Short it's 10% of the runtime. This is the likeliest swipe point.
- 3.88-5.27: The "furious" card lands on the word (4.16). The picture is a crowd happily throwing pies. Nobody looks furious. **Picture contradicts the word.**
- 5.27-6.62: "fuming" + "very angry, often quietly". The lady gets a pie in the face and sits still. This is a great match, the best moment of the video. Subscribe + bell appear here, under the tag, and cover nothing.
- 6.62-7.79: "livid" + "even angrier than furious", over the lady covered in pie, frozen. Good match. Only 1.2 s on the card. The word is readable; the meaning is just readable.
- 7.79-10.3: The hook swaps to "Would you shout, or say nothing?" The picture holds on her as she wipes her face. The question is engagement bait. It's not a test of the words.

## Takeaway test
"I was fuming when my roommate ate my lunch." I can name it, but only because I built it myself. The video never says a sentence like that. Most B1 viewers will just leave with "you're furious".

## Retention risks
- Length is fine (10.3 s). Pacing is fine apart from the 1 s gap at 2.9 s.
- The bottom 40% is empty until 3.9 s, which is wasted space.
- Card time for livid is 1.2 s, borderline.
- Loop: "Would you shout or say nothing?" leads back into "Your roommate ate your lunch." That's coherent. The picture jumps from the close-up lady to the street crowd, which is a visible seam.

## Trust risks
- "livid = even angrier than furious": most dictionaries give livid as "extremely angry", about equal to furious. It's a mild overclaim; the language editor already softened it. Acceptable, but "as angry as furious, or more" would be safer.
- Hook vs picture: a stolen lunch at home vs a 1920s street pie war. As comedy it works. As meaning it doesn't.
- Policy: slapstick pie fight, no sexual content, no real person as the topic, and a 1927 film (US public domain) with credit. Clean. No POLICY hit.
- Brand: the "anotherwordfor.net" wordmark is shown, not the channel avatar logo. Same as the other pd Shorts, so not new here.

## Ship-blockers
None. There are no spelled-out words, the subscribe animation is present with its time recorded, the render is 1440, and there's no watermark.

## Top 3 fixes (by impact)
1. **Give one usable sentence and one micro-choice.** Replace "You're livid." with a line like "When it happened again, you were livid." Or add a 1 s card: "quietly angry = ? (fuming)". Change the CTA from "shout or say nothing?" to "Fuming or livid? Comment." Owner: scenario-writer, then language-editor.
2. **Match the furious beat to an angry face.** Use a segment where the lady (or someone hit) reacts angrily, or move the pie-in-the-face moment earlier so all three words sit on her. Cut the crowd-laughing shot from under "furious". Owner: visuals / shorts-builder (segment choice).
3. **Tighten the 1 s silence at 2.9 s to about 0.3 s** and give livid the saved time (at least 1.8 s on the card). Owner: shorts-builder (beat gap).
