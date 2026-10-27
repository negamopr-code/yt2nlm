# Viewer-critic review: h112-very-wet-v1 (lab H112, Stop Saying "very wet": soaked / drenched / soggy)

Reviewed 2026-10-27. File: /workspace/glottos-marketing/state/shorts/h112-very-wet-v1/final.mp4 (md5 4d7dc823..., 1440x2560, 30 fps, 16.50 s, kokoro am_michael 1.05, no music). Unit: shorts/units/h112-very-wet-v1.json (language approval hash 11d04380763f9882).
Checked: faster-whisper small.en transcript with word timings, ffmpeg silencedetect (-40 dB, 0.3 s), 23 frames from 0 to 16.4 s (hook at 0/0.1/0.5/1.0/1.5 s, every beat). Not checked: listening by ear, the thumbnail, YouTube rendering.
Pain evidence: I spent no NotebookLM query. content/problems/ does not exist, and there is no learner quote about overusing "very" on file (the same gap as the H102-H109 reviews). The verbatim lines on file (content/insights/audience-needs.md) only show that viewers like these Shorts and add their own words: "Frigid too", "Melancholic too", "There is also minuscule as in a minuscule mouse.", "great video but please shorten the intro!". Pain (the brief's, NOT verbatim): "I always say 'very wet'; give me better words." Solved means that tomorrow I say "My shoes are soaked" or "We got drenched", and I know that "soggy" is for food or soft things.

## Verdict: PARTLY
The three words and sentences are correct and usable, and the pictures match the words. But this is the same template as H108 with the same faults: about 8 s of the 16.5 s is silence, the nuance is never stated (soggy is not "very wet"), there is no self-test, and the subscribe/bell animation is missing.

## Ship blockers
1. MISSING SUBSCRIBE + BELL (user rule 2026-10-05). No subscribe pill or bell appears in any sampled frame from 8 to 16 s. There is no final-sub.subscribe.json in the state folder (h108 has one), and there is no content/youtube/h112-very-wet-v1.json, so there is no "subscribe_at" either. Not finished. Owner: shorts-builder (run shorts/subscribe_anim.py once in the second half, about 9-10 s, and write the meta with subscribe_at).
- No spelled-out word: "Soaked" 4.58, "Drenched" 8.24, "Soggy" 12.12 are each heard as whole words.
- POLICY: none. Wet shoes, rain, cereal. Nothing sexual, no real people, safe for 13+.
- No magnifying glass, no NotebookLM/Gemini watermark seen. The logo is the channel avatar (top-left, "anotherwordfor.net / STOP SAYING").

## Pain -> gives -> gap
- Gives: soaked (My shoes are soaked), drenched (We got drenched in the rain), soggy (The cereal got soggy). Each word is spoken, on the card and in a matching picture.
- Gap 1: "Soggy" is NOT a stronger "wet". It means wet AND soft, and it is unpleasant (food, ground, paper). If I hear "3 better words for very wet", I will say "my shirt is soggy" or "the weather is soggy". The video never says "for food".
- Gap 2: soaked vs drenched is not explained (they are almost the same; drenched is usually from rain or water poured on you). That is acceptable at B1, but one 1-second line would add trust.
- Gap 3: there is no moment where I test myself.

## Second by second (heard / seen)
- 0.00-1.38 "Stop saying very wet." Frame 0 shows "Stop saying" plus "very wet" struck in red. It is my problem, clear, and the voice matches the screen. The "3 better words" sub is NOT on screen at 0-1.5 s; it shows at about 2.5 s.
- 1.34-2.03 0.69 s silent.
- 2.06-3.56 "Here are three better words." The screen is static. This is filler, and the card already says it.
- 3.58-4.37 0.79 s silent, headline-only screen (swipe point 1, about 3.5-4.5 s, 3 s of no new information).
- 4.58 "Soaked." / 5.01-5.77 silent. At 5.5 the screen is the headline only, no sentence and no picture. 5.66-6.80 "My shoes are soaked."; the shoe picture lands at about 6.5.
- 6.88-8.00 1.12 s silent (swipe point 2).
- 8.24 "Drenched." / 8.60-9.41 silent / 9.18-10.70 "We got drenched in the rain." The picture shows a man under a rain cloud, which matches.
- 10.79-11.86 1.07 s silent (swipe point 3).
- 12.12 "Soggy." / 12.47-13.29 silent; at 12.5 there is no picture. 13.22-14.62 "The cereal got soggy." The cereal bowl matches.
- 14.60-16.50 1.91 s silent tail. The loop frame (16.4) is the hook card, which matches frame 0. Fine for the loop, but it is 2 s of nothing.
- Pictures: each one again carries its own text. "Soaked - My shoes are soaked." is printed ON the shoes. "Drenched - We got drenched in the rain." runs across the man's body. "Soggy - The cereal got soggy." sits at the top and "Soggy" is on the bowl rim. That is a duplicate of the sub line, tiny on a phone, and the text over the man and the shoes hides the picture.
- The background word-wall (soaked/drenched/soggy, faint and large) is clutter behind the headline. It is readable, but it is noisy.

## Takeaway test
I can say "My shoes are soaked" and "We got drenched in the rain" tomorrow. That is a real action, so the verdict is not DOESN'T. But the video can teach a wrong use of "soggy" (for clothes or weather), and there is no self-test.

## Retention risks
- Silence: about 8.0 s of 16.5 s (0.69+0.79+0.76+1.12+0.80+1.07+0.82+1.91). The content fits in about 10-11 s.
- Every word is said twice (alone, then in the sentence), with a hold in between, and the picture arrives about 1.5-2 s after the word. So the first half of each beat is a bare headline.
- "Here are three better words" is 1.5 s that repeat the card.
- As a lab arm (ONE change = the word), this is a fair comparison with H106/H108 only if those had the same holds. Absolute retention will be low again.

## Trust risks
- Soggy is listed as a "better word" for "very wet". That is an overclaim about meaning (see Gap 1). It is the one real trust risk.
- The red strike says "very wet is wrong", but "very wet" is fine English. This is mild, and it is the series format.
- The English in the sentences is natural and correct.

## Top 3 fixes (by impact)
1. shorts-builder: add the subscribe/bell animation in the second half (about 9-10 s) and write content/youtube/h112-very-wet-v1.json with "subscribe_at". Cut the holds to 0.3-0.4 s and the tail to 0.5 s (target about 11 s). Show the sentence and the picture on the same frame as the headline. Put "3 better words" on frame 0.
2. scenario-writer (then the language-editor gate): fix soggy. Either make the sub "Soggy = wet and soft (food)" / "The cereal got soggy - yuck." or swap in "dripping (wet)" ("I'm dripping wet."). Optionally end with a 1 s self-test: "Your clothes after the rain? ___".
3. visuals: pictures with no embedded sentence. The text across the man and the shoes covers the picture and repeats the sub in tiny print.
