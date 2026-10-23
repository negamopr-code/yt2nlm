# Viewer-critic review: h102-very-hard-v1 (lab H102: micro-story interior inside "Stop Saying Very X")

Reviewed 2026-10-23. File: state/shorts/h102-very-hard-v1/final.mp4 (1440x2560, 30 fps, 20.7 s, Kokoro am_michael 1.05x, no music).
Unit: shorts/units/h102-very-hard-v1.json. Meta: content/youtube/h102-very-hard-v1.json.
Not judged as defects (they are the test): story lines on the cards, the loop back to the opening card, no music.

## Verdict: PARTLY
I understand the little story and I can name three phrases to use tomorrow, but the pictures say the opposite of two of the words (a cute, easy-looking path for "tough"; a happy victory pose for "brutal"), so the story does not teach what the words mean, and the required subscribe animation is missing.

## Ship blockers
1. Subscribe + bell animation MISSING. Meta records "subscribe_at": [20.0], but frames at 4 fps from 16 s to the end (and single frames at 19.0, 20.0, 20.4 s) show no subscribe pill and no bell. At 20.0 s only 0.7 s of video would remain anyway, and from 20.2 s the opening card is back. The recorded time is false. Owner: shorts-builder (render with shorts/subscribe_anim.py in the second half, e.g. on the "Brutal" beat around 12-13 s or the end card at 17 s, and write the real time to the meta).
2. "Brutal" beat teaches the wrong feeling (judgement blocker). The card line is "But she reaches the top!" and the picture is Ana with arms up in a golden sunburst, a victory picture. The word "brutal" (extremely hard, painful) arrives together with success and joy; only the last 1 s line "What a brutal climb!" carries the meaning. A B1 learner can leave thinking "brutal" = "great / amazing". Owner: scenario-writer (story line must show the pain: e.g. "The last hour nearly breaks her." / "It was a brutal climb." then the success), visuals (exhausted climber, not a triumph).

Not blockers, checked and clean: no word spelled letter by letter (whisper heard every word whole: Tough 3.78, Tricky 8.34, Brutal 12.84); 1440 short side; no magnifying glass; no watermark; POLICY: none.

## Pain -> what the video gives -> gap
- Learner evidence (no NotebookLM query spent; content/problems does not exist). On file in content/insights/audience-needs.md, verbatim: "great video but please shorten the intro!", "very helpful thanks :)", "Useful information... I'll share it to my close ones", and the recurring pattern of viewers adding their own word under Stop Saying Shorts: "Frigid too", "Melancholic too", "There is also minuscule as in a minuscule mouse.", "Enraged and pissed off also work". There is still no learner quote about overusing "very"; the pain is the brief's, not proven by quotes.
- Pain in the learner's words (assumed): "I always say 'very hard'; give me words I can say instead, quickly."
- Solved = tomorrow I say "a tough exam", "a tricky question", "a brutal week" and know which one fits.
- Gives: three good, common words, each in a natural phrase (tough climb / every step is tricky / brutal climb), inside a 3-step story that is easy to follow by ear.
- Gap: the story lines themselves ("Ana wants to climb a mountain.", "Then the path turns icy.", "But she reaches the top!") do not contain the word and do not explain it; the meaning sits only in the 1 s example line after it. The difference between the words (tricky = needs care, things can go wrong; brutal = extremely hard and painful) is carried by the story only for "tricky" (icy path). Nothing asks me to try a word myself except "Comment yours!".

## Second by second
- 0.0-1.4 "Stop saying very hard." The card appears at frame 0, the red strike draws in by 0.5 s. My phrase, I stop.
- 1.4-1.9 silence; 1.9-3.3 "Here are three better words." 3.8 s before the first word: acceptable, but this is the "intro" the top comment complains about.
- 3.8 "Tough," then 0.55 s pause, then the story line. The headline "Tough" sits alone on screen with no picture/line for about 0.6 s.
- 4.5-7.1 "Ana wants to climb a mountain. It's a tough climb." Picture: pastel path, smiling clouds, a child's head cut off at the bottom edge. Nothing looks tough; it looks like an easy walk. Picture contradicts word (fix 3).
- 7.1-8.3 1.2 s silence on a finished card. First swipe risk.
- 8.3-11.7 "Tricky, then the path turns icy. Every step is tricky." Best beat: the story makes the word clear (balancing, arms out). But it is a different drawing style and a different-looking woman, and the ice is not obvious (grey/white rocks).
- 11.7-12.8 1.2 s silence. Second swipe risk: pattern known, I know where it goes.
- 12.8-16.0 "Brutal, but she reaches the top. What a brutal climb." Third style (clay figure), third different Ana, victory picture (blocker 2).
- 16.0-17.1 1.1 s silence, then end card "Which word will you use? / Comment yours!" 17.1-19.4.
- 19.4-20.2 silence on the end card; 20.2-20.7 opening card returns (loop). The loop card has the headline without strike, same as frame 0: the seam looks matched.
- Swipe risk: moderate at 7-8 s and 11.7-12.8 s; the end card (17-20 s) is 3 s of no new content.

## Takeaway test
"Tomorrow I say 'It's a tough climb / a tough exam', 'Every step is tricky', 'What a brutal week!' instead of 'very hard'." Nameable. Not SOLVES: two of three pictures fight the word, and I never test myself.

## Retention risks
- Length 20.7 s vs 13-16 s planned. Where the extra 5 s goes: the story lines add ~1.3-1.9 s per word (about 4.5 s total), plus three ~1.2 s silent holds after each example and 1.3 s of silence before the loop. The story itself is not the problem; the fixed pauses are. Cutting the holds to ~0.5 s and the hook_gap would bring it to ~16-17 s without losing a word.
- Speech is clear and quick (1.05x, no podcast drawl); level mean RMS -17.9 dB, peak -1.4 dB. NOT checked by ear: stress/intonation.
- Three different art styles (flat pastel, watercolour sketch, clay 3D) for one heroine: the "one story" feeling of the test is weakened, which can bias the H102 result downward. Owner: visuals.
- Text: headlines and example lines are large and readable; the story line in beat 1 starts very small (Ana wants... set tiny at 4.5 s, full size about 0.5 s later) and the "Brutal" headline also pops in small first. Readable in time. Drifting "very hard" wallpaper words behind the cards: noisy but lane standard.

## Trust risks
- "Brutal" shown with joy (blocker 2). "Tough" shown with an easy cute path (fix 3).
- Card says "Ana"; voice says it so whisper wrote "Anna": same sound, no issue.
- "Tricky" is milder than "very hard" (language-editor noted it); in the icy-path context it works. "Stop saying very hard" is lane convention.
- English is natural throughout (language-editor approved, hash 3b5aba5d31472013).

## Top 3 fixes (by impact)
1. Add the subscribe + bell animation in the second half and record the real time in content/youtube/h102-very-hard-v1.json (now a false 20.0). Owner: shorts-builder.
2. Rewrite the "Brutal" story step so the hard part comes with the word (e.g. use line: "The last part nearly breaks her." sub: "It's a brutal climb.") and redraw beat 3 as exhaustion/strong wind, not victory; if the happy ending must stay, move it to the end card. Owner: scenario-writer, then language-editor, then visuals.
3. One consistent Ana in one art style across the three pictures, and a beat-1 picture that looks hard (steep, rocky, tired climber, her face visible). Then cut the post-example holds from ~1.2 s to ~0.5 s to land near 16 s. Owner: visuals; pacing: shorts-builder.
