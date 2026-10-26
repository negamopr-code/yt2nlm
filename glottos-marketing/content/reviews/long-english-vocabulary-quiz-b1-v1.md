# Viewer-critic review: long-english-vocabulary-quiz-b1-v1 (lab H72, quiz format)

Reviewed 2026-10-13. File: `state/shorts/long-english-vocabulary-quiz-b1-v1/final.mp4` - 2560x1440, 30 fps, 516.6 s (8:36.6), AAC 48 kHz mono, -13.7 LUFS.
Unit: `shorts/units/long-english-vocabulary-quiz-b1-v1.json` (language hash 9581c1e63d000965, approved 20:31:20).

## Verdict: SOLVES (second pass, 2026-10-13, rebuilt file 520.8 s) - no ship blockers. First pass was: DOESN'T solve it - as rendered, 1 render blocker (stale narration one beat behind).

The text below this line up to "Second pass" describes the FIRST render (516.6 s) and is kept as the record. The current state is in the section "Second pass" at the end.

The pictures are right and clean. The sound belongs to the previous version of the script and runs ONE QUESTION BEHIND the picture from 0:30 to the end. A viewer sees question 2 and hears question 1, sees the answer "miserable" and hears "Delighted". The quiz cannot be played with the sound on. With the correct narration this would be SOLVES (see "After the repair").

## SHIP BLOCKERS

### 1. Narration is stale and shifted by one beat (0:00-8:36, whole video)
Cause (evidence, not a guess): 42 of the 46 `bNN-*.wav` files are dated 20:22-20:25, before the unit was revised at 20:31:20 (title card removed, so every beat moved up by one). `kokoro_jobs.json` lists only 4 new jobs (1-1, 7-1, 13-1, 19-1). The voice cache is keyed by beat number, not by text, so the old files were reused under the new numbers. Picture durations in `states.txt` were taken from those wrong files, so the timeline looks consistent.
Confirmed three ways: whisper small.en on the whole video, a second run on cut pieces without context, and the single wav files (`b01-0.wav` = old intro, `b02-0.wav` = "Question one...", `b26-0.wav` = old closing line "Then keep going. The next video on your screen has more words like these for you").

What is heard against what is seen:
| Time | On screen | Heard |
|---|---|---|
| 0:00-0:13 | Question 1 + choices | Old intro: "English vocabulary quiz, B1 level, twenty questions. In each one, find a better word for a plain one, like very happy or very tired. You have five seconds for each answer. Count your points." Question 1 and its choices are NOT read |
| 0:13.7-0:18.7 | Countdown Q1 | ticks (starts with the choices never read) |
| 0:18.8-0:28.4 | Answer Q1 | Answer Q1 (correct, one of the 4 new files) |
| 0:30.1-0:38.2 | Question 2 (very sad) | "Question one. Find a better word for very happy... Delighted, disappointed, or confused?" |
| 0:44.2-0:50.3 | Answer Q2 "miserable" | "Delighted. I was delighted when I passed the exam..." |
| 0:51.9 on | Question 3 | "Question two..." - the same shift for Q3-Q5 |
| 2:02.9-2:11.2 | Round 2 card (+ subscribe animation) | "Question five... Furious, curious, or generous?" |
| 2:15.0-2:18.9 | Question 6 (on screen only 4.5 s before the countdown) | "Round two: describing people and things. Keep counting your points." |
| 2:24.4 | Answer Q6 | Answer Q6 (correct, new file) |
| 2:34.8 on | Question 7 | "Question six..." - shift for Q7-Q10 |
| 4:03.7-4:13.1 | Round 3 card | "Question ten..." |
| 4:14.2-4:16.7 | Question 11 (on screen only 2.9 s) | "You're halfway there. Round three: verbs." |
| 4:31 on | Question 12 | "Question eleven..." - shift for Q12-Q15 |
| 6:01.8-6:09.8 | Round 4 card | "Question fifteen..." |
| 6:10.7-6:14.9 | Question 16 (4.3 s) | "Round four: the last five questions..." |
| 6:30 on | Question 17 | "Question sixteen..." - shift for Q17-Q20 |
| 8:02.6-8:11.1 | Score card (+ subscribe animation) | "Question twenty... Despite, instead of, or due to?" |
| 8:14.0-8:24.3 | Closing card "Write your score in the comments" | "That's twenty questions. How many did you get? Seventeen to twenty: excellent..." |
| 8:24.3-8:36.6 | Closing card | no voice, 12 s of music only |

Never spoken at all: the answers to questions 5, 10, 15 and 20; the closing line "Write your score in the comments... thirty words to use instead of very". So the voice does NOT name the next video (check 6 fails on the sound). Spoken twice: the answers to questions 1, 6, 11, 16.
Fix: voice regenerates every wav from the approved unit text (and keys the cache by text hash, not beat number); shorts-builder rebuilds states, chapters, loudness, subscribe animation. Chapter times and `subscribe_at` in `content/youtube/long-english-vocabulary-quiz-b1-v1.json` will move and must be copied again. Then critic again - this review does not cover the new sound.

No other render blocker found. No spelled-out word anywhere in the transcript. No magnifying glass.

## Pain
No PROBLEM document and no `content/problems/` folder for the synonym lane (same as the Hot/Small reviews). No NotebookLM query spent. Verbatim from the comment corpus (`reports/monitor-awf/archives/youtube-comments-vol1*.md`):
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "my English is not good enough, what's why I'm using simple words"
- "One more thing do not repeat the same words in one sentence"
- "Overall after this time when i will learn new word how can i get good or similar synonym with the first word when i write down new word?"
- "Please recommend us nice book for synonym?"
- "The synonyms are useful for all sections of the IELTS"
- "Integrating these advanced words into your active vocabulary is difficult even for narive speakers"
- quiz behaviour on our own channel: a bare "3/5" comment under a quiz Short.

Pain in their words: "I say the same words all the time."
Solved means: tomorrow I say delighted / exhausted / furious instead of "very happy / very tired / very angry", and write "However," / "In addition," / "due to" instead of but / also / because of.

Gives (on the pictures): 20 plain-word -> better-word pairs, each in a sentence plus a second example, a self-test with a score. Gap as rendered: the sound contradicts the picture, so nothing is learned. Gap after the repair: recognition only (pick from three); the distractors are opposites, so the right answer is found by elimination without knowing the word.

## The eight checks

1. **0:00-0:20.** Question 1 with three choices is on screen at frame 0 (frames 0.0 / 0.5 / 1.5 identical): PASS. Search phrase "English vocabulary quiz, B1 level" is spoken 0.0-3.6 s: PASS. Countdown starts 13.7 s, but the voice has NOT read the question or the choices (old intro plays): FAIL, part of blocker 1.
2. **Cards, all 20 questions x 3 states looked at** (question, countdown "1", answer; incl. 4, 8, 12, 13, 17, 18, 19, 20). Readable; no overlap between emoji, text, buttons, example line and digit; right answer green in the sentence and on the button, the two wrong buttons dimmed and struck red; example line yellow with the word green. No answer shown before the countdown ends - question and countdown frames are identical except the digit. Emoji fit and give nothing away (party face, tear, snowflake, plane, angry face, wave, dress, house, car, sandal, stethoscope, chair, pasta, window, hotel, books, pill, loudspeaker, memo, rain cloud). Closest spot: Q6, the subtitle `"very interesting"` ends about 10 px from the wave emoji - touching distance, not overlapping. PASS on the picture.
3. **Five seconds.** In the design each question is on screen 8-10 s while it is read, then 5 s: enough for B1. In this render Q6, Q11, Q16 are on screen only 4.5 / 2.9 / 4.3 s before the countdown (the round-card speech plays there) - a side effect of blocker 1. Pace: 20 identical 23-second cycles; the three round cards and "You're halfway there" are the only breaks. Bearable for someone who came to be tested, monotonous for anyone else.
4. **Resolution.** 2560x1440 in the stream header: PASS.
5. **Subscribe + bell.** Visible 123.0-128.0 s on the Round 2 card and 483.0-488.0 s on the score card, bottom-left, covers no text at all, no question card touched; second one ends 28.6 s before the end; none in the first 15 s. Times recorded in the meta json. PASS (times will move after the rebuild).
6. **Closing card.** On screen 494.15-516.6 = 22.4 s: PASS. Text sits in the band 28-65 % of the height across almost the full width; the lower third is free, the sides are not - an end-screen video fits only at the bottom. The voice does not name the next video in this render: FAIL, part of blocker 1.
7. **Audio.** I cannot listen; judged by recogniser. ", blank," is recognised as "blank" in all 20 questions, with a pause before it at 18 and 19 ("Blank, it is very noisy"). All 20 answer words recognised as the intended word. One doubt: "included in the price" printed as "prize" in two separate runs (7:35-7:38) - check by ear after the rebuild. Loudness: speech was raised 12 dB by the normaliser, the music in the gaps 19 dB (music-only tail: -40.9 dB before, -21.9 dB after; speech about -12 dB), peaks at 0.0 dB. The music is therefore much louder between sentences than under them. Not judged by ear.
8. **Thumbnails** (1280x720 each). `new-question.jpg`: sentence readable at 168 px, the three buttons are not; it promises exactly the first frame. `new-yellow.jpg`: best at small size ("VOCABULARY QUIZ B1", 20 QUESTIONS). `new-score.jpg`: readable, but the phrase "vocabulary" is missing from the picture. PASS.

## Second by second (as rendered)
- 0-13 s: my question is on screen, the voice explains rules. I stay.
- 30 s: voice asks question 1 again while I read question 2. Confusion.
- 44 s: screen says miserable, voice says delighted. I leave here; anyone still watching leaves at the next question.
After the repair the expected swipe points are question 6-8 (same cycle the seventh time) and 8:24 (12 s hold with nothing new - needed for the end screen).

## Takeaway test
As rendered: none. After the repair: "write However, / In addition, / due to; say delighted, exhausted, furious instead of very + word."

## Trust risks (text, valid after the repair too)
- Too easy for the label "B1": wrong choices are opposites or unrelated (boring / ordinary / fascinating). Most viewers score 20/20; "17-20 excellent" then means nothing. Only Q5 (furious / curious) and Q18-20 make one think. "These are a little harder" before Q16 ("improve") is not true.
- British spelling on cards (neighbours, practise, cancelled) with an American voice. Harmless.
- English is natural throughout; nothing wrong found in the 20 sentences or examples.

## After the repair - expected verdict SOLVES for the searcher (test + answers + better words), PARTLY for the deeper pain (recognition, not production).

## Top 3 fixes
1. **voice + shorts-builder:** regenerate all narration from the approved unit, rebuild, re-copy chapters and `subscribe_at`. Add a gate: transcribe the final file and compare beat by beat with the unit before hand-over.
2. **shorts-builder:** loudness - the normaliser lifts the music in the gaps 7 dB more than the speech; use the linear two-pass path or lower the bed; keep peaks under -1 dB.
3. **scenario-writer (next quiz, not this one):** one near-synonym distractor per question from round 2 on, so that B1 is tested and the score spreads.

## Not checked
Listening by ear (stress, vowel quality, music level as perceived, tick sound); the corrected narration (does not exist yet); the two door Shorts; the end-screen target video; phone-size playback on a real device.


---

# Second pass (2026-10-13, after the repair of blocker 1)

File: `state/shorts/long-english-vocabulary-quiz-b1-v1/final.mp4`, built 20:52 - 2560x1440, 30 fps, 520.79 s (8:40.8), AAC 24 kHz mono, -14.0 LUFS.
Scope: only what changed (sound, loudness, subscribe animation, resolution). Cards were not looked at again, except the frames named in check 3.

## Verdict: SOLVES - no ship blockers.
The quiz can now be played with the sound on: every question is read on its own card, the voice is silent in every countdown, every answer is spoken on its answer card. For the person who typed "english vocabulary quiz b1" this is the test, the answers and 20 better words. It stays PARTLY for the deeper pain ("I say the same words all the time"): it is recognition, and mostly by elimination (see "Trust risks" above, unchanged).

## 1. Sound against picture, whole video - PASS
Two independent measures:
- **Voice energy** of `narration.wav` (same length as the video, 20 ms steps, threshold -50 dB) against the 145 states of `states.txt`: voice in 0 of the 100 countdown states. In every one of the 45 speaking states the voice starts 0.02-0.12 s after the card appears and ends before the card leaves: 0.36-0.51 s before the countdown on the 20 question cards, 1.24-1.40 s before the next card on the 20 answer cards.
- **Recogniser** (faster-whisper small.en, word timings) on `final.mp4`, compared state by state with the unit: all 20 questions, all 20 answers, three round cards, score card, closing line found once each, in order, on their own cards. Nothing twice, nothing missing.

| Card | On screen | Voice |
|---|---|---|
| Q1 + search phrase | 0.00-14.49 | 0.04-14.10 ("English vocabulary quiz, B1 level..." first words) |
| Round 2 | 124.43-132.15 | 124.47-128.59 |
| "You're halfway there. Round three: verbs." | 246.31-249.89 | 246.39-248.79 |
| Round 4 | 364.02-368.98 | 364.04-367.82 |
| Score card | 484.79-498.18 | 484.83-495.09 |
| Closing card | 498.18-520.78 (22.6 s) | 498.20-508.66, "...gives you thirty words to use instead of very"; then 12.1 s music only |

The recogniser on the full file lost three stretches (choices of Q5 at 107.7-110.2; sentence and choices of Q15 at 343.2-349.0 and the word "Provide" at 354.4; the word "Effective" at 406.8) and printed "The hotel will blank towels" under the answer card of Q15. These are recogniser faults, not sound faults: the voice energy is there at those times, and the four clips (`b05-0`, `b17-0`, `b17-1`, `b20-1`) transcribed alone give the unit text word for word. All 45 `.wav.txt` texts equal the unit text (0 mismatches); `kokoro_jobs.json` holds 45 jobs.

Chapters in `chapters.txt` and in `content/youtube/long-english-vocabulary-quiz-b1-v1.json` match the states: 2:04 = 124.43, 4:06 = 246.31, 6:04 = 364.02, 8:04 = 484.79, 8:18 = 498.18.

## 2. Words the recogniser gets wrong
- **"price" (7:17, 437 s):** full file with music -> "prize" again; the clip alone (`b21-1.wav`) -> "price". Judged: said correctly, the error comes from the mix. Not heard by ear.
- **"very" in the closing line (504 s and 508 s):** printed "vary" twice, in the full file and in the clip alone (`b25-0.wav`). The same voice's "very happy / very sad..." is printed correctly 9 times. "The word very" said as a quoted word may carry a more open vowel. For this American voice the two words are near-identical anyway; the card shows "very" in text. Non-blocking, one listen by ear.
- "replaced the word" printed "replace the word" (d + th run together) - normal speech.
- "but" in Q19 printed "butt" - same sound.
- `b05-1.wav` alone printed "Furious?" with a question mark - possible rising tone on the answer word of Q5. One listen by ear.
- No word spelled letter by letter anywhere.

## 3. Subscribe + bell - PASS
Frames at 125.2 / 126.5 / 128.0 / 129.5: button and bell bottom-left on the Round 2 card, click -> "SUBSCRIBED", bell rings; gone by 131.0; question 6 at 133.0 is clean. Frames at 485.7 / 487.0 / 489.0: same on the score card, below the text, covers nothing; gone by 490.5. Second animation ends 30.3 s before the end; none in the first 15 s; none on a question. `final.subscribe.json` and the meta json both hold `[125.0, 485.5]`.

## 4. Loudness (measured, not heard)
- Integrated -14.0 LUFS. Speech about -14.1 dB mean.
- Music alone: -29.4 dB mean on the closing card (510-520 s), -29.6 dB on the Round 2 card (129-132 s). First render: -21.9 dB. The music is now about 15 dB under the speech and the same level in the gaps as under the voice - the pumping is gone.
- Countdown stretches: -28.7 dB mean, ticks peak at -8.3 dB.
- **Peaks are over the top (non-blocking):** true peak +2.2 dBTP; decoded as float the peak is +0.99 dB, 43 samples at or over full scale. The limiter's ceiling sits at 0 dB and the AAC encode pushes over it. Next build: ceiling at -1.5 dB.
- Audio is now 24 kHz mono (was 48 kHz). The voice loses nothing (it is made at 24 kHz); the music has nothing above 12 kHz.

## 5. Resolution - PASS
2560x1440 in the stream header.

## Ship blockers
None.

## Non-blocking notes
1. shorts-builder: limiter ceiling -1.5 dB (true peak is +2.2 dBTP now).
2. voice / anyone with ears: one listen at 115.6 s ("Furious"), 437 s ("price"), 504-508 s ("very").
3. shorts-builder: five unused old clips lie in the build folder (`b06-1.wav`, `b12-1.wav`, `b18-1.wav`, `b24-1.wav`, `b26-0.wav`, dated before the rebuild). Not in the video; they are what caused the first blocker, so the builder should not be able to pick them up again.
4. Unchanged from the first pass: too easy for "B1" (opposites as wrong choices); 12 s of music only at the end (needed for the end screen).

## Not checked in the second pass
Listening by ear; the cards themselves (unchanged, passed in the first pass - only 13 frames looked at now); thumbnails; the two door Shorts; the end-screen target; a phone.
