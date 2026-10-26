# Viewer-critic review: l3-thank-you-v2 (Say It Like a Native, EP 3, lab H14)

Reviewed 2026-10-04. Video: `state/shorts/l3-thank-you-v2/final.mp4` (28.85 s, 1080x1920, 30 fps, words only, voice kokoro am_michael 1.05).
Unit: `shorts/units/l3-thank-you-v2.json`. YouTube text: `content/youtube/l3-thank-you-v2.json`.
Compared against: `state/shorts/l3-thank-you-v1/final.mp4` (29.09 s) and `shorts/units/l3-thank-you-v1.json`.

## Verdict: SOLVES (narrowly, for the lane's pain)

I overuse "thank you"; in 29 s I get five natural replacements, each with a label that tells me when to use it, read clearly, with nothing wrong on screen or in the voice. Tomorrow I can say "I owe you one" after a favour. It does not help me remember them (no recall moment) and "Don't say thank you" is an overclaim, but both are part of the template the test holds constant.

## Ship blockers: 0

- No word is spelled letter by letter (whisper output has no "X -Y -Z" pattern anywhere).
- No mispronounced answer found (see Check 2). Caveat: measured, not heard. I have no ears.

## Pain

Evidence is thin and I say so. I found no PROBLEM NN document, article or format file for this lane (`content/problems/` is empty or absent), and the learner corpus has no line about replacing "thank you". The one verbatim corpus line for the neighbouring pain (present in `state/corpus-glottos-niche/raw/78640fa0-…json` and `7a34608a-…json`):

- "I can understand what you say clearly , the point is that when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"

The rest of the basis is search demand from `/workspace/glottos-auto/out/lab/lab.json` ("other ways to say thank you" is a typed query; the search results are long videos, not Shorts). No NotebookLM query was spent.

Pain in the learner's words: "I say the same words all the time."
Solved would mean: tomorrow I thank someone with a different phrase that fits the situation, and it is correct.

Pain -> what the video gives -> gap:
- Gives: Thanks a lot (everyday), I really appreciate it (warm and sincere), Cheers! (casual, British), You're a lifesaver! (when someone really helps you), I owe you one (after a favour). All natural, labels true.
- Gap 1: "memorize ... and use them": no recall moment, no situation shown. I read five cards and scroll.
- Gap 2: "Thanks a lot" is barely a new phrase, and with flat intonation it is the standard sarcastic one. Not flagged.
- Gap 3: "Don't say thank you" is false as advice ("thank you" is always correct). v1's "just" was the honest wording; removing it is the test, so accepted, but a literal-minded learner is told something wrong.

## Check 1: hook - PASS

- Card: `Don't say` (white) / `"Thank you"` (yellow, in quotes), red strike through the phrase, then `Say this instead`. No "just" anywhere on screen in any of 288 sampled frames (10 fps) I looked at by contact sheet and close-up.
- Timing: "Don't say" alone at 0.0-0.1 s, phrase on by 0.2 s, strike drawn at 1.3 s (v1: 1.6 s), "Say this instead" on at 1.7 s.
- Voice (whisper small.en, final video): "Don't(0.00) say(0.28) thank(0.46) you(0.74-1.24), say(1.66) this(1.92) instead(2.16-2.62)". No "just". On the clip `b01-0.wav` alone: "Don't say thank you." Speech energy 0.05-1.06 s and 1.73-2.71 s.
- 2.71-3.5 s: 0.8 s of silence on the hook card.
- As a scroller: I stop. My phrase, crossed out, in the first 1.3 s.

## Check 2: answers as heard - PASS

Heard (final video): "Don't say thank you, say this instead, thanks a lot, every day, I really appreciate it, warm and sincere, cheers, casual British, you're a life saver, when someone really helps you, I owe you one, after a favor, which one will you try today?"

| # | Card on (s) | Voice headline (s) | Label on / voice (s) | Whisper, final | Whisper, clip alone |
|---|---|---|---|---|---|
| hook | 0.0 | 0.05-1.06 | 1.7 / 1.73-2.71 | Don't say thank you (thank p=0.72) | same (thank p=0.47) |
| 1 | 3.5 | 3.58-4.29 | 5.7 / 5.77-6.37 | thanks a lot (thanks p=0.46) | Thanks a lot. (0.87) |
| 2 | 7.5 | 7.63-8.85 | 10.1 / 10.12-11.17 | I really appreciate it (0.99) | same |
| 3 | 12.3 | 12.29-12.86 | 14.1 / 14.09-15.14 | cheers (0.82) | Cheers! (0.97) |
| 4 | 16.2 | 16.27-17.22 | 18.6 / 18.62-20.08 | you're a life saver (life 0.35, saver 0.98) | You're a lifesaver. (0.84) |
| 5 | 21.2 | 21.25-22.16 | 23.4 / 23.49-24.41 | I owe you one (0.99) | same |
| CTA | 25.6 | 25.59-27.07 | 26.1 (silent) | which one will you try today? | - |

- "Cheers!": recognised every time (final v2 0.82, clip 0.97, same audio in v1 final 1.00). 0.57 s, not clipped at either edge.
- "lifesaver": recognised as "lifesaver" on the clip and in v1; in the v2 final whisper split it "life saver" with low confidence on "life". The audio is byte-identical to v1 (same md5), so this is whisper's decoding, not a different reading. No stray sound, no "Since."-type garble. Stress pattern not verifiable by me.
- Low-confidence "thanks" (0.46) in the final, 0.87 on the clip; same bytes as v1 (0.70). Not a defect on this evidence.
- A human should still play `b04-0.wav` (0.79 s) and `b05-0.wav` (1.32 s) once; that is 2 seconds of listening.

## Check 3: cut-off / UI zone / legibility - PASS

- Foreground text bounds over all frames: x 79-998 of 1080, lowest content y = 1045 of 1920 (CTA sub). The bottom 400 px (y > 1520) and in fact everything below y = 1045 holds only the dim word cloud. Nothing cut off.
- Widest lines: struck phrase x 82-997; "when someone really helps you" x 81-998 (wraps, "you" alone on line 2: cosmetic orphan).
- Counter 1/5 .. 5/5 present. Brand header at y 56-250 may sit under YouTube's own top bar on some phones (brand only).
- Labels stay 1.7-2.6 s on screen; enough for 1-5 words.
- Background words pass behind the headline band (e.g. dim "thanks a lot." behind "3 / 5" and "Cheers!" at ~12.8 s; "cheers" beside the hook at 0-3 s). Headlines remain clearly readable; the small grey counter is the only thing that gets muddy.
- Not checked: a real phone with the real Shorts UI.

## Check 4: background words - PASS

Every background word read in the frames is one of this unit's five answers (thanks a lot. / i really appreciate it. / cheers! / you're a lifesaver! / i owe you one.) plus the faint logo tiles. No words from another video. (v1's `final.bgbug.mp4` is the old bug; not present here.)

## Check 5: differences from v1 besides the hook

Intended and confirmed:
- Unit diff: only `id`, `lane`, hook `headline`, hook `speech`, `language_approval`.
- Audio: `b01-0.wav` differs (1.32 s vs 1.56 s); the other 12 clips are byte-identical (md5). Final audio from 5 s on correlates 0.9999 with v1 at a 0.24 s shift. Mean level -27.5 dB both; peak -4.8 dB (v1 -4.4).

Follow from the hook (not independent changes):
- Total 28.85 s vs 29.09 s; every later beat starts 0.24 s earlier.
- Strike at 1.3 s vs 1.6 s; "Say this instead" at 1.7 s vs 1.9 s.
- Hook line 1 is narrower ("Don't say" x 297-787 vs "Don't just say" x 178-905).

Not intended, real:
1. **Background word cloud has a different layout.** `build_stop_saying.py` seeds the cloud with the unit id (`word_tile(u["id"] + "a" ...)`), so v2's cloud is a different random arrangement of the same words. Brightness is equivalent (lower-frame mean luma 13.4-16.0 vs 13.1-16.3; brightest 0.1 % up to 66 vs 56 around 21 s). In v2 a large "cheers" and "thanks a lot." sit right beside the hook in the first 3 s; v1 had a quieter top area. Small, but it is a second visual difference in the first seconds of a test that claims one variable.
2. **Packaging is not held constant.** v1 (XCbX3pZOGGQ) was retitled on 10-03 to `Other Ways to Say "Thank You" in English #shorts`; v2's title is `Don't Say "Thank You" – Say This Instead #shorts`. v1's 2 views were earned under the old "Don't Just Say" title, so the hook comparison is against that, plus a different publish day and hour. H14's reading must say so.
3. Both videos carry the chip "EP 3". Two public Shorts with the same episode number; cosmetic.

## Second-by-second swipe risks

- 0.0-1.3: my phrase, struck out. I stay.
- 2.7-3.5: 0.8 s nothing new.
- 3.5-7.5: "Thanks a lot." I already say this. First real swipe risk: the first answer is the weakest of the five, and after it there is 1.5 s of silence (4.29-5.77) before "everyday".
- 7.5-12.3: fine; 1.3 s silence 8.85-10.12.
- 12.3-16.2: "Cheers!" as thanks is new to many; good. 1.2 s silence after it.
- 16.2-25.6: the two best items come last; many viewers are gone (channel average view is 14-16 s of 30).
- 25.6-28.85: CTA; speech ends 27.07, then 1.78 s silent tail.

## Takeaway test

One action: next time someone does me a favour, say "I owe you one"; when someone saves my day, "You're a lifesaver!". Nameable and correct, hence SOLVES.

## Retention risks

- Speech totals about 12.9 s of 28.85 s; about 16 s is silence on a static card. Held constant by the test, but it is the main cost.
- Weakest item first, strongest last.
- Seven identical beats, no picture, no self-test.
- The word cloud shows all five answers from second 0.

## Trust risks

- "Don't say thank you": overclaim (test variable).
- "Thanks a lot" without a sarcasm warning.
- American voice reading "Cheers! Casual, British" and card spelling "favour": consistent with each other, harmless.
- No wrong fact, no unnatural English, picture never contradicts the voice.

## Top 3 fixes (by impact; none blocks this upload)

1. growth-tester / whoever reads H14 (not a video fix): record that v1 vs v2 differs in hook wording, live title, publish slot and background layout. For future one-variable re-makes, shorts-builder should seed the word cloud from a fixed key (e.g. the unit id without the version suffix) so the background is identical.
2. scenario-writer (next version, not this test): put the strongest items first (You're a lifesaver! / I owe you one / Cheers!) and replace "Thanks a lot." with something a B1 learner does not already say (e.g. "Thanks a million." or "Much appreciated.").
3. shorts-builder (next version): cut the headline-to-label pause from ~1.3-1.5 s to ~0.7 s and the tail to ~1.0 s (saves about 4 s), and spend 2 s of it on a recall card before the CTA ("A friend lends you money. You say: I ___ you one.").

## What was and was not checked

- Checked: unit diff v1/v2; md5 of all 13 voice clips in both versions; faster-whisper small.en word timings on both final videos and on the six v2 headline clips; speech-energy runs; 18 frames per version on contact sheets plus four full-resolution close-ups; text bounds, strike timing and background brightness on 288 frames (10 fps) per version; background seed logic in `shorts/build_stop_saying.py`; YouTube text file.
- Not checked: anything by ear (pronunciation is inferred from whisper and clip identity with v1); LUFS; a real phone with the Shorts UI; NotebookLM (no query spent); the caps/audio gates' own logs.
- Nothing was edited, rendered or uploaded. Scratch files only under `/tmp/ty_frames`, `/tmp/tr_ty.py`, `/tmp/ty_an.py`.
