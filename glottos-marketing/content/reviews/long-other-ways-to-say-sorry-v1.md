# Viewer-critic review: long-other-ways-to-say-sorry-v1 + door Short l3-sorry-like-a-native-v1 (lab H49)

Date: 2026-10-09. Reviewer: glottos viewer-critic (step 7b). Read-only review: no video, unit or meta was changed, nothing rendered, nothing uploaded.

Files judged
- LONG: `state/shorts/long-other-ways-to-say-sorry-v1/final-sub.mp4` (2560x1440, 30 fps, 5:16.22; audio AAC 24 kHz mono)
- SHORT: `state/shorts/l3-sorry-like-a-native-v1/final-sub.mp4` (1440x2560, 30 fps, 24.41 s; audio AAC 44.1 kHz stereo)

## Verdicts

| Video | Verdict | Ship blockers |
|---|---|---|
| LONG | **PARTLY** (content would be SOLVES; one hard gate fails) | **1** |
| SHORT | **SOLVES** its job as a door | **0** |

LONG in one sentence: 15 natural phrases sorted into small slip / real apology / work, each with a meaning, an example and a line to say out loud, but in quiz 3 the voice asks a different question from the one on the screen.

## 1. The pain

Evidence, honestly: there is no PROBLEM document and no verbatim learner comment on file for this topic (`content/insights/audience-needs.md` has none about "sorry"). The pain is the search phrase from the launch brief. No NotebookLM query was spent, no quote was invented.
- Pain: "other ways to say sorry in english". I say "sorry" for everything, from bumping into someone to a late report.
- Solved means: tomorrow I pick a fitting phrase for a small slip, for a real apology and for a work email, and I do not write "my bad" to a customer.

## 2. What was checked

- Timed transcript of both final-sub.mp4 files (faster-whisper small.en, cpu, int8, 4 threads, word timings).
- All 75 voice clips of the long video and all 9 of the Short transcribed one by one and compared with the script; `kokoro_jobs.json` compared with the current unit text beat by beat.
- Frames: one per picture state of the long video (99 states, 11 contact sheets), 12 frames around the two subscribe animations (104.2-109.5 s, 202.5-207.8 s), 12 frames of the Short.
- NOT checked: I cannot listen (audio findings come from speech recognition); loudness and silence were not measured this time; thumbnails not judged; the Short was not viewed on a real phone.

## 3. Ship blockers

### LONG: 1

1. **Quiz 3: the voice and the screen are two different quizzes (4:09.5-4:22.2, i.e. 249.5-262.2 s, beat 24).**
   - On screen: `An email to a customer: "___, I sent you the wrong date."` with options `My apologies / My bad`; answer shown: `"My apologies, I sent you the wrong date."`
   - Heard: "An email to a customer. Blank, for the late reply. Please accept my apologies, or my bad?" (249.5-255.8 s), then "Please accept my apologies for the late reply." (259.0-262.2 s).
   - Cause: the quiz text was changed in the unit after the voice was made. `b24-0.wav` and `b24-1.wav` are from 08:12, `kokoro_jobs.json` is from 08:10 and still holds the old quiz; the unit was approved at 11:22. Beat 24 is the only beat where the voiced text differs from the unit (the other 26 match word for word).
   - Fix (voice, then shorts-builder): re-voice only `b24-0.wav` and `b24-1.wav` from the current unit speech ("Which phrase fits? An email to a customer. Blank, I sent you the wrong date. My apologies, or my bad?" / "My apologies, I sent you the wrong date."), rebuild the narration and the video, run `shorts/subscribe_anim.py` again. The new clips are shorter, so everything after 4:09 moves: regenerate `chapters.txt` ("Speaking practice: at work" 4:23 and "Your turn" 5:07 will change) and the chapter list in the description. The two subscribe times (104.3, 202.6) are before the change and should stay; confirm the printed `SUBSCRIBE_AT` equals `subscribe_at` in `content/youtube/long-other-ways-to-say-sorry-v1.json`.

### SHORT: 0

## 4. Hard gates

| Gate | LONG | SHORT |
|---|---|---|
| Short side at least 1440 | PASS (2560x1440) | PASS (1440x2560) |
| Subscribe + bell visible at the recorded time | PASS: 104.3 s (seen 104.5-109.2 s, gone at 109.5) and 202.6 s (seen 202.8-207.5 s, gone at 207.8); matches meta and `.subscribe.json` | PASS: 19.2 s (seen 19.4-23.5 s), in the second half, matches meta |
| Animation not on a part-title card, quiz or text | PASS: both run on word cards ("I am so sorry", "I apologise"), lower left, in empty space; the part cards end at 103.77 s and 202.07 s, before the animation starts. At 206.3-207.6 s the example line is on screen well above the overlay. Only faint background words are behind it. | PASS: under the closing text, covers nothing |
| Not in first 15 s / last 20 s (long) | PASS | n/a |
| Magnifying glass | none | none |
| Text on screen = what is said | **FAIL, quiz 3 (blocker 1)** | PASS |
| Spelled-out word | none | none |
| Watermark / logo | none / channel avatar | none / channel avatar |

## 5. Audio (speech recognition)

- "Looking for other ways to say sorry in English?" is the first sentence, 0.0-2.9 s. PASS.
- All 15 headline phrases are heard as whole phrases, none spelled, none clipped, both in the full video and as single clips: My bad (17.9), Sorry about that (26.2), My mistake (36.0), Excuse me (44.6), Pardon me (52.6), I am so sorry (103.8), That was my fault (116.1), I owe you an apology (124.2), Please forgive me (134.8), I feel terrible (143.8), I apologise (202.3), My apologies (210.5), Sorry for the delay (219.0), I take full responsibility (227.1), Please accept my apologies (237.5).
- "I apologise" clean three times (clip confidence 0.92-0.96). "My bad" clean (17.9, 24.0, 75.9 s). "Pardon me" clean (52.6, 56.0, 88.5 s).
- Quizzes: question, 3 s countdown, then the answer, in all three (answer at 69.6, 161.9, 259.0 s). Quiz 1 and 2 match the screen. Quiz 3 does not (blocker).
- Repeat after me: each of the 15 lines is followed by a silent "YOUR TURN: SAY IT" pause of 1.6-4.7 s. Works.
- Recogniser slips that the single clips do not confirm (so not voice faults): "We miss the train" (clip: "missed"), "I owe you apology" at 130.9 s (clip: "an apology").
- One to listen to once: 240.6 s, "It is a very formal sorry" was written by the recogniser as "formal sari" in the single clip (`b23-1.wav`), and as "sorry" in the full video. Probably fine.
- "another word for dot net" is spoken as words; the card shows the address at that moment.

## 6. Picture

- Text is readable, nothing is cut at the edge, each element appears as it is spoken (headline, then meaning and picture, then example).
- Emoji pairs, all 15 fit the example: coffee + facepalm (My bad); document + sweat smile (wrong file); clock at three + grimace (meeting at three); raised hand + walker (get past); collision + flushed face (bump into someone); birthday cake + crying face; train + sad face; speaking head + folded hands (what I said); broken heart + pleading face (broke my promise); open book + disappointed face (losing your book); bar chart + bowing person (mistake in the report); calendar + bowing person (wrong date); alarm clock + incoming envelope (delay, report); parcel + raised hand (order was late, responsibility); envelope + fountain pen (formal, in writing).
- Weakest: "Sorry about that" uses a laughing sweat-smile, a bit too cheerful; "I take full responsibility" (raised hand) reads as "stop" as easily as "it was me".
- Cosmetic: in quiz 2 the two option pills touch each other ("I owe you an apology" / "My mistake", 152-166 s); headlines "Please forgive / me" and "Sorry for the / delay" break with one word alone on line two; faint background words run behind the countdown digits.

## 7. Does it solve the pain (LONG)

- Gives: three situations as the learner asked, register words in each meaning ("very casual", "polite", "formal", "very formal, mostly used in writing"), the note that people say "I'm so sorry", a work part with five email-safe phrases, 15 lines to say aloud.
- Gaps:
  1. Only quiz 3 tests the choice of register (My apologies / My bad to a customer), and that is the broken one. Quiz 1 and quiz 2 reuse an example shown 30-40 s earlier, word for word, so they test memory, not choice.
  2. "Excuse me" and "Pardon me" are said BEFORE a small trouble, the other three after it; the meaning lines say so, but nothing contrasts them.
  3. Nothing says outright "do not use My bad at work"; after the fix quiz 3 will carry this alone.

## 8. Second by second (LONG)

- 0.0-2.9 s: my search phrase, spoken and on screen. I stay.
- 2.9-13.7 s: one static card for 13.7 s. Slowest stretch.
- 13.7-60.5 s: part 1, five cards of about 9 s each. Good pace.
- 60.5-71.9 s: quiz 1, too easy (same sentence as 36-42 s).
- 71.9-97.6 s: speaking practice 1. Works.
- 97.6-152.6 s: part 2, the strongest part; 104.3 s subscribe animation, harmless.
- 152.6-166.4 s: quiz 2, again the example from 20 s before.
- 166.4-197.0 s: speaking practice 2, pauses up to 4.5 s with no sound bed.
- 197.0-248.0 s: part 3, what the work learner came for.
- 249.5-262.2 s: quiz 3, the voice reads another question than the screen. A learner reading along loses trust here.
- 263.6-300.4 s: speaking practice 3. 300.4-316.2 s: site tip, question for the comments.

## 9. Takeaway test

LONG: yes. "Small slip: My mistake / Sorry about that. Real apology: I owe you an apology. Work email: My apologies / Sorry for the delay."
SHORT: yes. My mistake (got it wrong), I owe you an apology (serious), My apologies (formal, at work).

## 10. Short (l3-sorry-like-a-native-v1)

- Hook: text and voice at 0.0 s ("Don't just say sorry"), the word is struck out by 3.5 s, first phrase at 5.0 s.
- Heard = shown on all five cards; the three phrases are all in the long video; "15 ways" is true; the closing card and voice (18.4-22.6 s) point to the full lesson.
- Subscribe animation 19.2-24.2 s under the closing text, covers nothing.
- Notes: the bell sits at the far right edge near 83 % of the height, probably under the Shorts buttons; the background (ghost phrases plus logo tiles) is busy and bright compared with the long video; 1.8 s of silence at the end.

## 11. Risks

Retention (LONG): 13.7 s static hook; three identical quiz + practice blocks; long silent pauses without a sound bed; one voice for both speakers in the part 1 dialogues.
Trust (LONG): quiz 3 mismatch. No wrong facts found; register labels are accurate; British spelling on screen ("apologise") with an American voice is fine.
Trust (SHORT): none found.

## 12. Non-blocking fixes

LONG
1. (scenario-writer) Make quiz 1 and quiz 2 a register choice in a NEW sentence (for example, a friend's birthday forgotten: I am so sorry / My bad).
2. (shorts-builder) Change the picture at least once during the 13.7 s hook.
3. (shorts-builder) Put a gap between the option pills in quiz 2; avoid one-word second lines in headlines.
4. (visuals) Calmer face for "Sorry about that"; clearer "it was me" picture for "I take full responsibility".
5. (voice / shorts-builder) One audio standard for long and Short (24 kHz mono vs 44.1 kHz stereo).
6. (voice) Listen once to 4:00 ("very formal sorry").

SHORT
1. (shorts-builder) Move the subscribe pill and bell up and left, away from the right-hand buttons.
2. (visuals) Tone the background down to the level of the long video.

## 13. Top 3 fixes by impact (LONG)
1. voice + shorts-builder: re-voice beat 24, rebuild, regenerate chapters after 4:09.
2. scenario-writer: quizzes 1 and 2 as register choices in new sentences.
3. shorts-builder: break up the 13.7 s static hook card.
