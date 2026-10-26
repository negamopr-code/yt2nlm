# Viewer-critic review: l3-im-sorry-v1 (Say It Like a Native, EP 10, lab H12)

Reviewed 2026-10-04. Video: `state/shorts/l3-im-sorry-v1/final.mp4` (28.94 s, 1080x1920, 30 fps, words only, voice kokoro am_michael 1.05).
Unit: `shorts/units/l3-im-sorry-v1.json`. YouTube text: `content/youtube/l3-im-sorry-v1.json`.
Compared against the winner: `state/shorts/l3-i-dont-know-v1/final.mp4` (26.97 s) and `shorts/units/l3-i-dont-know-v1.json`.

## Verdict: SOLVES (narrowly, for the lane's pain)

I say "I'm sorry" for everything; in 29 s I get five correct alternatives, each with a label telling me when to use it, read clearly, with nothing wrong on screen or in the voice. Tomorrow I can say "My bad" to a friend and "That was my fault" at work. It does not help me remember them (no recall moment), one of the five still contains the word I was told not to say, and "Don't say I'm sorry" is an overclaim; all of that is the template the test holds constant.

## Ship blockers: 0

- No word is spelled letter by letter: no "X -Y -Z" pattern in the whisper output of the final video or of any of the 13 voice clips.
- No "just" in the hook, heard or on screen.
- No mispronounced or swallowed answer found (see "Answers as heard"). Caveat: measured, not heard. I have no ears.

## Pain

Evidence is thin, same as for `l3-thank-you-v2`: there is no PROBLEM NN document, article or format file for this lane. The one verbatim corpus line for the pain:

- "I can understand what you say clearly , the point is that when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"

The rest is search demand from `/workspace/glottos-auto/out/lab/lab.json`, hypothesis H12 (YouTube autocomplete): "say this instead of sorry", "instead of saying sorry i'm late". No NotebookLM query was spent.

Pain in the learner's words: "I say the same words all the time."
Solved would mean: tomorrow, when I make a mistake or bump into someone, I say something other than "I'm sorry", it fits the situation, and it is correct.

Pain -> what the video gives -> gap:
- Gives: My bad (very casual), Sorry about that (everyday), I apologise (formal), That was my fault (when you take the blame), Pardon me (polite, when you bump into someone). All natural English, all labels true.
- Gap 1: "memorize ... and use them": no recall moment, no situation shown. I read five cards and scroll.
- Gap 2: "Sorry about that." is "sorry" again. Two seconds after "Don't say I'm sorry" was struck out in red, the second answer says sorry. It is good English, but it is the weakest item for this hook.
- Gap 3: the typed query is "instead of saying sorry i'm late". None of the five is the thing natives say there ("Thanks for waiting", "Sorry to keep you waiting"). The video answers "sorry" in general, not the situation people search for.
- Gap 4: "Don't say I'm sorry" is false as advice. "I'm sorry" is always correct, and for bad news ("I'm sorry for your loss") none of the five can replace it. Held constant by the test.

## Template check against the winner: PASS (same hook card, strike, voice, pace, layout)

| Item | l3-i-dont-know-v1 (winner) | l3-im-sorry-v1 |
|---|---|---|
| Voice / speed / pause | kokoro am_michael, 1.05, 1.0 | same |
| Hook card | `Don't say` white, phrase yellow in quotes, red strike, `Say this instead` | same |
| "Don't say" alone | 0.0-0.1 s | 0.0-0.1 s |
| Phrase fully on | 0.4 s | 0.4 s |
| Red strike drawn | 1.5 s | 1.5 s |
| "Say this instead" on | 1.9 s | 1.9 s |
| Hook voice | 0.09-1.11, 1.91-2.90 | 0.07-1.20, 1.89-2.88 |
| First answer card | 3.7 s | 3.7 s |
| Headline end -> label voice | 1.26 / 1.33 / 1.31 / 1.30 / 1.36 s | 1.31 / 1.49 / 1.20 / 1.36 / 1.27 s |
| CTA voice / tail | 23.71-25.19, tail 1.79 s | 25.68-27.16, tail 1.80 s |
| Mean / peak level | -27.7 dB / -6.4 dB | -27.6 dB / -6.5 dB |
| Text bounds | x 64-1004, lowest y 1040 | x 80-996, lowest y 1040 |
| Background brightness (headline band, mean luma) | 17.1 | 17.1 |
| Counter, header, chip | 1/5..5/5, logo, "SAY IT LIKE A NATIVE - EP 2" | same, "EP 10" |

- `b01-1.wav` ("Say this instead.") and `b07-0.wav` (CTA) are byte-identical to the winner's (md5).
- Unit diff: only `id`, `episode`, `lane`, hook phrase, the five answers and labels, `language_approval`.
- The only measurable difference is length: 28.94 s vs 26.97 s (+1.97 s), all of it from longer labels ("when you take the blame", "polite, when you bump into someone" vs "informal", "at work").
- Background word cloud is a different random layout (seeded by unit id in `shorts/build_stop_saying.py`), built only from this unit's five answers. Expected for a new phrase.

## Hook: PASS

- Card: `Don't say` / `"I'm sorry"` (yellow), struck at 1.5 s, `Say this instead` at 1.9 s.
- Heard: "Don't(0.00) say(0.28) I'm(0.46) sorry(0.74-1.12), say(1.92) this(2.08) instead(2.32-2.84)". Exactly "Don't say I'm sorry. Say this instead." No "just".
- 2.88-3.70 s: 0.8 s of silence on the hook card (winner: the same).
- As a scroller: I stop. It is my phrase, crossed out in red within 1.5 s.

## Answers as heard: PASS

Heard (faster-whisper small.en, final video): "Don't say I'm sorry, say this instead, my bad, very casual, sorry about that. Every day, I apologize, formal, that was my fault. When you take the blame, pardon me, polite when you bump into someone, which one will you try today?"

| # | Card on (s) | Voice headline (s) | Label on / voice (s) | Whisper, final | Whisper, clip alone |
|---|---|---|---|---|---|
| hook | 0.0 | 0.07-1.20 | 1.9 / 1.89-2.88 | Don't say I'm sorry (I'm 0.78) | same (0.76) |
| 1 | 3.7 | 3.70-4.34 | 5.6 / 5.65-6.60 | my bad (my 0.26, bad 1.00) | My bad. (0.78 / 0.88) |
| 2 | 7.7 | 7.71-8.68 | 10.1 / 10.17-10.77 | sorry about that (0.97-1.00) | same |
| 3 | 11.9 | 12.02-13.10 | 14.3 / 14.30-14.84 | I apologize (0.98) | same (0.96) |
| 4 | 16.0 | 16.06-17.11 | 18.4 / 18.47-19.60 | that was my fault (0.99-1.00) | same |
| 5 | 20.8 | 20.81-21.55 | 22.8 / 22.82-24.53 | pardon me (0.99 / 1.00) | Pardon me. (0.82 / 0.98) |
| CTA | 25.6 | 25.68-27.16 | 26.1 (silent) | which one will you try today? | same |

- "my" in "My bad" has low confidence in the final (0.26) but 0.78 on the clip, and the word is transcribed correctly both times. A short unstressed word after silence; not a defect on this evidence.
- "pardon" got a zero-length time stamp in the final (21.12-21.12); the energy run is a normal 0.74 s and the clip alone is clean. Whisper timing artifact.
- "everyday" is transcribed "Every day": same sounds.
- A human should still play `b02-0.wav` (0.96 s) and `b06-0.wav` (1.00 s) once.

## Legibility / cut-off / picture-voice sync: PASS

- Every card matches the unit letter for letter (18 frames on contact sheets, one close-up at 23.7 s): "My bad." / "Sorry about that." / "I apologise." / "That was my fault." / "Pardon me." with their labels; CTA "Which one will you try today?" / "Write it in the comments."
- Foreground text x 80-996 of 1080; lowest text y = 1040 of 1920. Nothing near the Shorts UI zone, nothing cut off.
- Each headline appears with its voice (within 0.1 s); each label appears as it is spoken.
- Labels stay on 2.0-2.8 s. The longest, "polite, when you bump into someone" (two lines, smaller type than the other labels), is on for 2.8 s: readable.
- Background words pass behind the headlines (dim "i apolog", "pardon r", "my bad"). Headlines and labels stay clearly readable; only the small grey counter gets muddy. The cloud shows all five answers from second 0.
- Not checked: a real phone with the real Shorts UI.

## Second-by-second swipe risks

- 0.0-1.5: my phrase, struck out. I stay.
- 2.9-3.7: 0.8 s nothing new.
- 3.7-7.7: "My bad." Strong first item, new to many B1 learners. 1.3 s silence (4.34-5.65) before "very casual".
- 7.7-11.9: "Sorry about that." I was just told not to say sorry. First real swipe risk: it feels like a cheat, and 1.5 s of silence follows (8.68-10.17).
- 11.9-16.0: "I apologise." I know this one from school. Second weak item in a row; swipe risk.
- 16.0-20.8: "That was my fault." Useful, clear label.
- 20.8-25.6: "Pardon me." Fine; longest label, read in full.
- 25.6-28.94: CTA; speech ends 27.16, then 1.8 s silent tail.

## Takeaway test

One action: next time I make a small mistake with a friend, say "My bad"; at work, when it really was me, say "That was my fault." Nameable and correct, hence SOLVES.

## Retention risks

- Speech totals about 13.0 s of 28.94 s; about 16 s is silence on a static card. Same ratio as the winner; held constant.
- 2 s longer than the winner with the same amount of new information.
- Items 2 and 3 are the two a learner already knows; the middle of the video sags.
- Seven identical beats, no picture, no self-test.

## Trust risks

- "Don't say I'm sorry": overclaim (template).
- "Sorry about that" under a "don't say sorry" hook: a sharp commenter will point it out.
- "Pardon me" is correct for bumping into someone but sounds formal or old-fashioned to many speakers; "Excuse me" is the usual word. The label does not say so. The language-editor passed it as dictionary-checked.
- American voice, card spelled "apologise": invisible to the ear, harmless.
- No wrong fact, no unnatural English, picture never contradicts the voice.

## Top 3 fixes (by impact; none blocks this upload)

1. scenario-writer (next version, not this test): replace "Sorry about that." with an answer that does not contain "sorry" and serves the typed query "instead of saying sorry i'm late", e.g. "Thanks for waiting." (when you are late). Put it second.
2. scenario-writer / language-editor (next version): swap "Pardon me." for "Excuse me." or label it "polite, a little formal".
3. shorts-builder (template, after H12 is read): cut the headline-to-label silence from ~1.3 s to ~0.7 s and the tail to ~1.0 s (saves about 4 s) and spend 2 s on a recall card before the CTA ("You step on someone's foot. You say: ___ me.").

## Other three, light check

Contact sheet of 18 frames each (hook at 0.1 / 0.6 / 1.2 / 1.6 / 2.4 / 3.3 s, each answer with and without its label, CTA twice) plus faster-whisper small.en on the final video and on every voice clip.

- `state/shorts/l3-i-think-v1/final.mp4` (28.14 s): **PASS.** Hook heard "Don't say, I think. Say this instead." (no "just"; "I" short, p=0.19, word present). Cards match the unit: I guess. / I believe. / I reckon. / In my opinion. / It seems to me. "I reckon" is recognised (final 0.99, clip 0.83; 11.77-12.44 s, not clipped). Strike at 1.3 s because the phrase is shorter. Note for the learner: "I guess." / "I believe." / "I reckon." are shown as finished sentences though they are openers; not a defect, same as "I think".
- `state/shorts/l3-how-are-you-v1/final.mp4` (27.53 s): **PASS.** Hook heard "Don't say how are you. Say this instead." (no "just"; "how" low confidence 0.34, word present). Cards match: How's it going? / How are you doing? / What's up? / How have you been? / How's everything? Whisper printed a stray "day." (p=0.28) after "today?" at 25.68 s: the CTA clip is byte-identical to the other videos' and the speech run is the usual 1.48 s, so it is a recognition artifact, not a sound. Two cosmetic notes: the background cloud is the busiest of the four (large dim "how are you doing?" directly under the struck "How are you?"), still readable; "How are you doing?" is barely a new phrase.
- `state/shorts/l3-youre-welcome-v1/final.mp4` (26.53 s): **PASS.** Hook heard "Don't say you're welcome. Say this instead." (no "just"). Cards match: No problem. / My pleasure. / Anytime. / Don't mention it. / Happy to help. All recognised ("Anytime" 0.86 final, 0.56 on the clip alone, correct both times).

None of the three has a word spelled letter by letter. All three: text x within 84-988 of 1080, lowest text y 1040, level -27.6 to -27.7 dB mean, strike and "Say this instead" timing as in the winner.

## What was and was not checked

- Checked: unit against the winner's unit; md5 of the shared hook and CTA clips; faster-whisper small.en word timings on five final videos and on all 13 voice clips of each of the four new videos; speech-energy runs; card, label and strike times from 10 fps frames of all five videos; text bounds and background brightness on those frames; 18 frames per video on contact sheets plus two close-ups; YouTube text file against the unit.
- Not checked: anything by ear (pronunciation and stress are inferred from recognition); LUFS; a real phone with the Shorts UI; NotebookLM (no query spent); the builders' own gate logs.
- Nothing was edited, rendered or uploaded. Scratch files only under `/tmp/h12/` (my files: `tr.py`, `tr.json`, `an.py`, `b.py`, `mysheet.py`, `vc_*.png`, the five `*.wav` and the `f0001.png`-style frames; older files there belong to an earlier step and were left alone).
