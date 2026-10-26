# Viewer-critic review: l3-yes-v1 (Say It Like a Native, EP 14, lab H15)

Reviewed 2026-10-04. Video: `state/shorts/l3-yes-v1/final.mp4` (25.73 s, 1080x1920, 30 fps, words only, voice kokoro am_michael 1.05).
Unit: `shorts/units/l3-yes-v1.json`. YouTube text: `content/youtube/l3-yes-v1.json` (title `Other Ways to Say "Yes" in English #shorts`).
Compared against the winner: `state/shorts/l3-i-dont-know-v1/final.mp4` (26.97 s).
Light checks at the end: `l3-good-luck-v1` (27.07 s), `l3-okay-v1` (27.37 s).

| Video | Verdict | Ship blockers |
|---|---|---|
| l3-yes-v1 | PARTLY | 0 |
| l3-good-luck-v1 | SOLVES | 0 |
| l3-okay-v1 | SOLVES | 0 |

## Verdict: PARTLY

The title promise is kept fast and correctly: my word is on screen at 0.4 s, crossed out at 1.2 s, the first alternative at 3.4 s, five correct ones by 21 s. But four of the five (Sure, Of course, Absolutely, Definitely) are words a B1 learner already knows, two labels ("strong", "certain") do not tell me when to pick one over the other, and the only new phrase ("You bet") is labelled by register, not by situation. I learn one new thing and one useful rule ("Of course" = to a request). Technically clean; the content is the weakest of the three.

## Ship blockers: 0

- No word spelled letter by letter: no "X -Y -Z" pattern in the whisper output of the final video or of any of the 13 voice clips.
- Every card matches the unit letter for letter; nothing clipped, nothing overflowing, nothing near the Shorts UI zone.
- Every beat is heard as shown (see "Answers as heard"). Caveat: measured by speech recognition, not heard. I have no ears.

Important note on the evidence: a plain whisper pass over the whole final file DROPPED three words ("Casual" at 5.1 s, "Absolutely" at 10.9 s, "Definitely" at 14.7 s) and printed only "Sure. Of course. To a request. Strong. Certain. You bet. Casual American." I did not wave that through. The speech-energy runs show sound at all three places (5.07-5.67, 10.87-11.69, 14.66-15.38 s); each beat cut out of the final audio and transcribed alone is recognised (Casual 0.83, Absolutely 0.87, Definitely 0.65), and the 3.0-22.2 s cut transcribes as all fifteen words in order ("Sure. Casual. Of course. To a request. Absolutely. Strong. Definitely. Certain. You bet. Casual American."). So the drops are a recogniser artifact of one-word utterances between 1.2 s silences, not missing audio. Any automatic audio gate that runs whisper on the whole file will see the same false miss.

## Pain

Evidence is thin, as in the earlier L3 reviews: no PROBLEM NN document, article or format file exists for this lane. The one verbatim corpus line (as quoted in `content/reviews/l3-im-sorry-v1.md`):

- "I can understand what you say clearly , the point is that when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"

The rest is search demand from `/workspace/glottos-auto/out/lab/lab.json`, H15: live autocomplete for "other ways to say" lists good luck, yes, okay. No NotebookLM query was spent.

Pain in the learner's words: "I say the same words all the time."
Solved would mean: tomorrow, when someone asks me something, I answer with something other than "yes", and I know it fits.

Pain -> what the video gives -> gap:
- Gives: Sure (casual), Of course (to a request), Absolutely (strong), Definitely (certain), You bet (casual, American). All natural, all labels true.
- Gap 1: novelty. Sure / Of course / Absolutely / Definitely are A2-B1 words. The winner taught "Beats me" and "I haven't got a clue"; this one teaches "You bet" and nothing else new.
- Gap 2: "strong" vs "certain" is not a difference I can act on. Both are simply an emphatic yes.
- Gap 3: "You bet. casual, American" tells me the register, not the moment (a friend asks a favour, or thanks you).
- Gap 4: no recall moment (template, held constant).
- Gap 5: the title is neutral ("Other ways to say"), the video commands "Don't say Yes". "Yes" is never wrong. Template, held constant; a searcher may find it bossy, a commenter will say so.

## Does the searcher get what the title promises: YES

- 0.0 s "Don't say"; 0.4 s `"Yes"` in yellow; 1.2 s red strike; 1.6-1.8 s "Say this instead"; 3.4 s first answer. The dim background cloud shows all five answers from second 0.
- Voice: "Don't(0.00) say(0.30) yes(0.50-0.94). Say(1.72) this(1.78) instead(2.04-2.52)."
- Dead air: 2.58-3.39 s (0.8 s, same as the winner).

## Template check against the winner: PASS

| Item | l3-i-dont-know-v1 | l3-yes-v1 |
|---|---|---|
| Voice / speed / pause | am_michael, 1.05, 1.0 | same |
| Phrase fully on / strike / "Say this instead" | 0.4 / 1.5 / 1.9 s | 0.4 / 1.2 / 1.6 s (shorter phrase) |
| First answer card | 3.7 s | 3.4 s |
| Headline end -> label voice | 1.26-1.36 s | 1.22-1.27 s |
| CTA voice / tail | 23.71-25.19, 1.79 s | 22.47-23.95, 1.80 s |
| Mean / peak level | -27.7 / -6.4 dB | -27.3 / -5.0 dB |
| Bright text bounds | x 64-1012, lowest y 1045 | x 68-996, lowest y 1045 |
| Background luma, headline band | 21.5 | 21.9 |

`b01-1.wav` and `b07-0.wav` are byte-identical to the winner's (md5). Unit differs only in id, episode, lane, phrase, answers, labels, approval.

## Answers as heard: PASS

| # | Card on (s) | Headline voice (s) | Label on / voice (s) | Heard, beat cut from final | Heard, clip alone |
|---|---|---|---|---|---|
| hook | 0.0 | 0.07-0.97 | 1.6 / 1.59-2.58 | Don't say yes. (yes 0.74) Say this instead. | same (yes 0.51) |
| 1 | 3.4 | 3.39-3.84 | 5.0 / 5.07-5.67 | Sure. (0.65-0.79) / Casual. (0.83) | Sure. (0.65) / Casual. (0.59) |
| 2 | 6.8 | 6.91-7.55 | 8.8 / 8.79-9.57 | Of course. (0.97) / to a request. (0.98) | same |
| 3 | 10.8 | 10.87-11.69 | 12.9 / 12.96-13.54 | Absolutely. (0.87) / strong (0.54; 0.99 in the long cut) | Absolutely. (0.86) / Strong. (0.50) |
| 4 | 14.6 | 14.66-15.38 | 16.6 / 16.60-17.17 | Definitely. (0.65; 0.98 long cut) / Certain. (0.56; 0.99) | Definitely. (0.54) / certain (0.37) |
| 5 | 18.3 | 18.31-18.86 | 20.0 / 20.09-21.18 | You bet. (0.99) / Casual American (0.63-0.98) | same |
| CTA | 22.4 | 22.47-23.95 | 22.9 (silent sub) | Which one will you try today? | same |

Language-editor risks, one by one:
- "Sure. Casual." clipped or run together: NO. "Sure" is 0.45 s of sound inside a 0.68 s clip (0.04 s lead, 0.18 s tail, first/last samples at zero), then 1.23 s of silence before "Casual". Low single-word confidences (0.5-0.65) are normal for a lone word; in context they read 0.79-0.94.
- "Definitely. Certain." clipped or run together: NO. 0.72 s and 0.57 s of sound, 1.22 s apart, clean edges.
- "To a request." rising like a question: NO. Pitch falls 132 -> 90 Hz (-6.7 semitones), a statement.
- "You bet. Casual, American." pause at the comma: there is NO audible pause; the label is one unbroken 1.09 s run ("casual" to 0.50 s, "American" straight after). It is heard as "casual American". Not wrong, the card carries the comma; a human should play `b06-1.wav` once to decide whether it sounds like "a casual American". Pitch in that clip peaks at 286 Hz (the others stay under 210): a lift on "casual", list intonation or a blip.
- All pitch contours fall at the end; no clip ends on a rise.

## Legibility / cut-off / picture-voice sync: PASS

- 18 frames on contact sheets plus a close-up at 21.2 s. Cards: "Sure." / "Of course." (two lines) / "Absolutely." / "Definitely." / "You bet." with labels casual / to a request / strong / certain / casual, American; CTA "Which one will you try today?" / "Write it in the comments."
- Bright text x 68-996 of 1080 (widest: "Absolutely.", about 70 px margin each side); lowest text y 1045 of 1920. Builder safe line is 1520; nothing is within 470 px of it.
- "to a request" and "casual, American" sit on one line each, fully inside the frame.
- Each headline appears within 0.1 s of its voice; each label appears as it is spoken.
- Labels stay on 1.7-2.4 s ("strong" and "certain" 1.7 s: one word, enough).
- Cosmetic: "Of course." is set larger and broken into "Of / course." while the longer "Absolutely." stays on one line. Readable, but "Of" alone on a line looks odd.
- Background words drift behind headlines; headlines and labels stay clear, the small grey counter gets muddy at 4/5.
- Not checked: a real phone with the real Shorts UI.

## Second-by-second swipe risks

- 0.0-1.2: my word, struck out. I stay.
- 2.6-3.4: 0.8 s nothing new.
- 3.4-6.8: "Sure." I know it. 1.2 s silence, then "casual". First swipe risk: the very first answer is the most obvious one.
- 6.8-10.8: "Of course." Known, but "to a request" is the one useful rule in the video.
- 10.8-14.6: "Absolutely. strong." Known.
- 14.6-18.3: "Definitely. certain." Known, and it feels the same as the last one. Biggest swipe risk: three known words in a row, the middle sags harder than in the winner.
- 18.3-22.4: "You bet." The only new one arrives at second 18. Many will not get here.
- 22.4-25.7: CTA; speech ends 23.95, 1.8 s silent tail.

## Takeaway test

One action: when someone asks me for something ("Can you help me?"), answer "Of course"; with a friend, try "You bet". Nameable, but thin: I could already do the first. Hence PARTLY.

## Retention risks

- Speech is about 10.2 s of 25.7 s; about 15.5 s is silence on a static card (winner: same ratio, held constant).
- Best item is last; weakest is first. The winner opened with "No idea" and had three idioms.
- Seven identical beats, no picture, no self-test.

## Trust risks

- "Don't say Yes": overclaim (template).
- "Sure. casual": true, but a flat "Sure" can sound unenthusiastic; the label does not warn. Minor.
- "Absolutely" and "Definitely" as separate items with near-synonym labels looks like padding to a sharp viewer.
- No wrong fact, no unnatural English, picture never contradicts the voice.

## Top 3 fixes (by impact; none blocks this upload, and H15 measures the title, not the list)

1. scenario-writer (next version): replace "Definitely." with something new to a B1 learner and put a new one first, e.g. "For sure." (casual) or "Sounds good." (to a plan); order: You bet / Of course / Sounds good / Absolutely / Sure.
2. scenario-writer / language-editor (next version): labels that say WHEN, not how it feels: "You bet. - to a friend's request"; "Absolutely. - when you fully agree".
3. shorts-builder (template, after H15 is read): keep short two-word headlines on one line ("Of course."); cut headline-to-label silence from 1.2 s to about 0.7 s and the tail to 1.0 s. Also make the builder's audio gate transcribe per beat, not the whole file: whole-file whisper drops one-word beats (it did here three times).

## Other two, light check

Same method: 18 frames each (hook at 6 points, every answer with and without its label, CTA twice), one close-up each, faster-whisper small.en on the final video and on all 13 clips, speech-energy runs, pitch contour and internal gaps per clip, text bounds over all frames at 10 fps.

### `state/shorts/l3-good-luck-v1/final.mp4` (27.07 s): SOLVES, 0 blockers

- Heard, whole file, every word: "Don't say good luck, say this instead, best of luck, polite, break a leg, before a show, fingers crossed, hopeful, you've got this, encouraging, I'm rooting for you, supportive, which one will you try today?" All answer words 0.96-1.00 except "best" 0.71.
- "rooting": recognised as "rooting" at 0.99-1.00 in the final (19.84 s), in the beat cut and in the clip alone. A ROW-ting or RUT-ting reading would normally print "routing" / "rutting"; it did not. Not heard by a human: play `b06-0.wav` once.
- Cards match the unit: Best of luck. / Break a leg. / Fingers crossed. (two lines) / You've got this. (two lines) / I'm rooting for you. (two lines: "I'm rooting / for you.", widest line well inside the frame). Bright text x 80-981, lowest y 1045.
- Hook: phrase on 0.4 s, strike 1.4 s, "Say this instead" 1.8 s, first answer 3.6 s. Sync within 0.1 s on every beat; headline-to-label silence 1.27-1.33 s. Level -27.2 dB mean, -4.0 dB peak.
- Notes, not blockers: the background cloud is the busiest of the three (large dim "break a leg." and "you've go" pass right behind "You've got this." and "I'm rooting for you." at 16-23 s); still readable in the close-up. Small 0.11 s dips inside "good luck" and "best of luck" are the stop of the k, not a cut.
- Why SOLVES: all five are phrases a B1 learner does not use yet, and the labels tell me when ("before a show"). Tomorrow: "You've got this" to a friend before an exam.

### `state/shorts/l3-okay-v1/final.mp4` (27.37 s): SOLVES, 0 blockers

- Heard, whole file: "Don't say okay, say this instead, all right, every day, got it, I understand, works for me, agreeing to a plan, fine by me, casual, fair enough, accepting a point, which one When will you try today?"
- The stray "When" (24.54 s, p=0.23) is a recogniser artifact: the CTA clip is byte-identical to the winner's and the 23.8-25.9 s cut alone reads "Which one will you try today?" cleanly.
- "everyday" as one word: YES. One unbroken 0.60 s run (5.56-6.16 s), no gap inside; whisper spells it "every day", same sounds.
- "Got it. I understand." as a sixth phrase: by ear alone it IS a full sentence in the same voice after 1.3 s, so a listener not looking at the screen can take it for another answer. On screen it is clearly the small white label under the yellow headline, and the counter stays 2/5. Low risk, not a blocker. Fix for a next version (scenario-writer): label "when you understand".
- Low-confidence words, all correctly transcribed: "okay" 0.35 (whisper splits between "okay" and "OK"), "All" 0.34 (clip alone prints "Alright."), "Fine" 0.34-0.82 in the final, and "Find by me." (0.37) on the clip alone. "fine by" and "find by" are near-identical sounds; a human should play `b05-0.wav` once.
- Cards match the unit: All right. / Got it. / Works for me. (two lines) / Fine by me. (two lines) / Fair enough. Labels "agreeing to a plan" and "accepting a point" on one line, fully inside. Bright text x 80-966, lowest y 1045.
- Hook: phrase on 0.4 s, strike 1.3 s, "Say this instead" 1.6-1.9 s, first answer 3.4 s. Sync within 0.1 s on every beat. Level -27.7 dB mean, -3.0 dB peak (3.4 dB hotter than the winner's peak; no clipping).
- Cosmetic: "Fine by me." is set very large on two lines while the equally long "Fair enough." is small on one line.
- Why SOLVES: "Works for me", "Fine by me", "Fair enough" are new and each label names the situation. Tomorrow: "Works for me" when a colleague proposes a time.

## What was and was not checked

- Checked: three units against the winner's; YouTube text files against the units (titles exact, bullets = cards); md5 of shared hook/CTA clips; faster-whisper small.en word timings on four final videos, on all 39 voice clips, and on 18 beats cut from the final audio; speech-energy runs; card, label and strike times from 10 fps frames; bright-text bounds over every frame; pitch contour, lead/tail and internal gaps of every clip; 18 contact-sheet frames per video plus three close-ups.
- Not checked: anything by ear (pronunciation, stress, "rooting", "fine by", the comma in "casual, American" are inferred from recognition and measurements); phonemes (espeak is not installed); LUFS; a real phone with the Shorts UI; NotebookLM (no query spent); the builders' own gate logs.
- Nothing was edited, rendered or uploaded. Scratch files only under `/tmp/h15/`.
