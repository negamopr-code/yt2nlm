# Viewer-critic review: long-other-ways-to-say-yes-v1 + door Short l3-yes-like-a-native-v1 (lab H45)

Date: 2026-10-09. Reviewer: glottos viewer-critic (step 7b). Read-only review: no video, unit or meta was changed, nothing uploaded.

Files judged
- LONG: `state/shorts/long-other-ways-to-say-yes-v1/final-sub.mp4` (2560x1440, 30 fps, 5:54.04; audio AAC 24 kHz mono)
- SHORT: `state/shorts/l3-yes-like-a-native-v1/final-sub.mp4` (1440x2560, 30 fps, 22.44 s; audio AAC 44.1 kHz stereo)

## Verdicts

| Video | Verdict | Ship blockers |
|---|---|---|
| LONG | **PARTLY** solves the pain (close to SOLVES) | **2** (1 hard gate, 1 audio that needs a human ear before it can be cleared) |
| SHORT | **SOLVES** its job as a door (3 usable answers with a situation label, clear pointer to the lesson) | **0** |

LONG in one sentence: the learner really does get 20 natural answers sorted into four situations with an example each and a speaking drill, but three of the four quizzes do not test the thing they came for (choosing the right "yes" for the situation), there is no work/boss case, and the word "Yeah" is not reliably heard as "Yeah".

## 1. The pain

Evidence base, honestly: there is no "PROBLEM NN" document for this lab hypothesis (it is a search-phrase piggyback on the Short "Other Ways to Say Yes in English"). The pain was taken from the launch brief (search intent "other ways to say yes (in english)"). The only verbatim learner comments on file for this topic are two, on that Short (`content/insights/audience-needs.md` line 6): "I am in absolute agreement with your sentence" and "but why?". No NotebookLM query was spent. No quotes were invented.

- Pain in the learner's words (search phrase): "other ways to say yes in english". I answer everything with a flat "yes"; I want natural alternatives and I want to know which one fits a friend, a boss, an invitation. The comment "but why?" on the Short points the same way: a list is not enough, they want the when and why.
- "Solved" means: tomorrow, when a friend proposes a plan, a colleague asks for a file, or someone invites me, I pick a fitting answer other than "yes" without thinking, and I do not say "Yep" to the wrong person.

## 2. What was checked (evidence)

- Timed transcript of what is heard: faster-whisper small.en, cpu, int8, 2 threads, word timings, on both final-sub.mp4 files. Note: faster-whisper is in `.nlmvenv`, not in `.ttsvenv` (the brief's path fails with ModuleNotFoundError).
- Each of the 99 voice clips of the long video (`bNN-M.wav`) transcribed in isolation and compared with its script text in `kokoro_jobs.json`; clip heads and tails measured for cut-off.
- Frames: one frame for each of the 131 picture states of the long video (11 contact sheets), plus full-size frames at 96.05 / 96.2 / 96.34 / 98.5 / 100.8 / 260.05 / 260.2 / 260.4 / 262.5 / 264.6 s; 12 frames of the Short plus a full-size frame at 17.4 s (overlay position measured in pixels).
- ffmpeg silencedetect and volumedetect on both.
- NOT checked: I cannot listen; all audio findings are from speech recognition and the loudness envelope. The thumbnail and the three A/B thumbnails were not judged. The Short safe area was judged against the usual Shorts layout (buttons on the right from about half height down, caption in the bottom fifth), not on a real phone.

## 3. Answers to the six questions

### Q1. Search phrase and count
- "Looking for other ways to say yes in English?" is the first sentence: 0.00-2.6 s. PASS. The on-screen headline at 0 s is `Other ways to say "yes"` (no "in English" on screen; fine).
- 20 answers, counted on screen and in the transcript, none repeated: Sure, Yeah, Yep, Okay, You bet / Of course, Certainly, No problem, By all means, Gladly / Absolutely, Definitely, Exactly, Totally, For sure / Sounds good, Good idea, Works for me, Count me in, I would love to. PASS. The closing line "That's twenty ways to say yes" (345.7 s) is true.

### Q2. Audio
- No word is spelled out letter by letter anywhere (both videos). No quote marks are read aloud. 91 of 99 clips are heard word for word as written; the other 8 are listed here. No clip is cut at the start or the end (edges silent).
- Dialogues are read as two lines with a pause of 0.7-1.0 s between question and answer (pen? 22.46 -> Sure 23.22; tonight? 30.28 -> Yeah 31.30; door? 37.64 -> Yep 38.48; taxi? 272.64 -> Good idea 273.54; dinner? 300.92 -> I would love to 301.62). One voice plays both speakers, so only the pause and the yellow colour mark the change of speaker.
- **"Yeah" (problem):**
  - headline at 25.6 s: heard in the full video as "Yep."; the isolated clip `b04-0.wav` (0.68 s) is heard as "Jaffa" / "YAFON" / "yep" (confidence 0.06-0.35);
  - example at 31.3 s: heard correctly, "Yeah, see you at eight" (0.86). In the full-video pass an extra "I" appeared ("Yeah, I see you at eight"); the isolated clip does not have it, so that is the recogniser, not the voice;
  - "Repeat after me" line at 74.7 s (`b09-2.wav`): heard as "**Yes**, see you at 8" (0.70), three decodings, all the same.
  - So in two of its three appearances, including the model the learner is told to repeat, answer no. 2 is not heard as "Yeah". All other single-word headlines (Sure, Okay, Gladly, Exactly, Totally, Certainly ...) are recognised in isolation.
- "Yep": headline at 34.3 s heard as "Yep." in the full video, but the isolated clip `b05-0.wav` is heard as "Yappo" (0.44); the loudness envelope shows no stop-and-release for the final p. In the dialogue (38.5 s), the drill (79.3 s) and the quiz (141.0 s) it is heard as "Yep" (0.84-0.87). Probably fine; listen once together with "Yeah" because the two headlines come 9 s apart and may sound the same.
- "You bet": clean every time (49.0, 55.4, 88.0 s; 0.88-0.99).
- "By all means": clean (121.9, 127.3, 163 s; 0.83-1.00).
- "Blank": heard as "Blank," in all four quizzes (60.4, 139.6, 219, 307.6 s). Confidence is lower (0.40-0.60) but the word is right. From the learner's seat it is an odd thing to hear ("Blank, sir"), yet the card shows the gap at the same moment, so it is understood.
- "another word for dot net" (341.6-344.5 s): heard as "another word for .NET", which means "dot net" is spoken as two words; the card shows anotherwordfor.net at that moment. Fine.
- Part intros: recogniser wrote "Part 1 5 Relaxed Answers" for "Part 1. Five relaxed answers" (numbers only, not a voice fault).
- No doubled word found. No music; all silences longer than 2.4 s are the planned quiz countdowns and "your turn" pauses (2.5-4.0 s each). The video ends with 3.1 s of silence on the closing card.
- Loudness: long mean -24.7 dB, peak -0.5 dB; Short mean -27.3 dB, peak -4.6 dB. The Short is about 2.5 dB quieter than the long video.

### Q3. Picture and text
- Nothing is cut off at the frame edge and nothing is unreadable at phone size. Headlines: "By all means" fits on one line (125 s), "Works for me" fits on one line (276 s). Quiz cards with quoted lines are readable; the green answer and the struck-out wrong option are clear. Drill cards (LISTEN / YOUR TURN: SAY IT, 1/5 counter) are clear.
- Defects, none of them a blocker:
  1. **"I would love / to"**: the headline breaks with "to" alone on line two (293.3-304.2 s) and the same in the Part 4 strip label (255.3 s).
  2. **"No / problem"** breaks into two big lines (120.6 s) while the longer "By all means" is shrunk to one line. Inconsistent.
  3. **The example is a clean two-line dialogue on only 8 of 20 cards** (Sure, Yeah, Yep, You bet, No problem, Absolutely, Exactly, Works for me). On the other 12 the text wraps by width, not by speaker. Worst cases split the very phrase being taught: `"Okay, six / is fine."` (44.2 s), `"By all / means."` (125.6 s), `"Definitely, I / wouldn't miss it."` (190.6 s), `"Totally, / I love it."` (203.5 s), `"For / sure, look at those clouds."` (212.0 s), `"Sounds / good."` (264.1 s), `"Good / idea, it's late."` (272.0 s).
  4. Grey background words touch foreground text in places: a ghost "yep" sits right after `"Yep, all done."` (36.9 s); the countdown digits sit on ghost words (141.8 s on "no problem / certainly", 222.4 s on "definitely", 310.6 s on "sounds good"). Low contrast, cosmetic.
- Emoji pairs: all 20 match their example (pen + thumbs up; wave + night city; key + door; clock at six + OK hand; ticket + popcorn; window + smile; bill + plate; laptop + outbox; pointing hand + chair; bags + handshake; clapperboard + star eyes; church + love letter; headphones + notes; rain cloud + umbrella; pizza + yum; taxi + bulb; calendar + tick; football + raised hand; plate + hearts). Weakest: "Exactly" = a calendar page reading "July 17" + a dartboard; the target says "exactly", the date is random.
- No magnifying glass anywhere. No NotebookLM/Gemini watermark. The logo is the channel avatar.

### Q4. Hard gates
- Resolution: LONG 2560x1440, SHORT 1440x2560. PASS.
- Subscribe + bell present: LONG at 96.0 s and 260.0 s (seen at 98.5 and 262.5 s: grey SUBSCRIBED + ringing bell, bottom left), SHORT at 16.9 s (seen 17.4-20.6 s). Times match `subscribe_at` in both metas and the `.subscribe.json` files. PASS on presence and record.
- **Covering text: FAIL on the long video, twice.** The animation starts while the part-title card is still on screen, and the red SUBSCRIBE pill slides in over the first label under the emoji strip:
  - 96.00-96.37 s: pill covers the label "Of course" (Part 2 card ends at 96.37 s);
  - 260.00-260.43 s: pill covers the label "Sounds good" and the bell touches "Good idea" (Part 4 card ends at 260.43 s).
  About 0.4 s each, but it is red on top of yellow text and the rule is "not covering any text". After the card change (word cards) the overlay sits in empty space and covers nothing, including when the example line appears (100.8 s, 264.6 s).
- Last 20 s (334.0-354.0 s): no subscribe animation. PASS. (See nice-to-have 7 about the end-screen tiles.)
- Magnifying glass: none. PASS.

### Q5. Length (planned 3-5 min, render 5:54)
From the learner's seat it does not drag badly, because the extra minute is the speaking pauses, which are the useful part. What repeats without adding anything:
- Quiz 1 and quiz 2 reuse, word for word, an example shown 30-40 s earlier ("Can I borrow your pen?", "Could I have the bill, please?"), and quiz 4 reuses the football line. With options like Sure / Sorry, Exactly / Never, Count me in / No thanks, nobody can get them wrong. That is about 45 s that tests nothing.
- Each drill repeats all five lines; the one-word lines ("Of course.", "Gladly.", "Exactly.", "You bet.") each cost 3-4 s for very little.
- Each answer starts with about 1 s of headline alone on an empty card.
If a cut is wanted: drop the four one-word drill lines (about 15 s) and the 1 s headline-only state (about 20 s); that gives roughly 5:15. I would not cut for length alone; I would rather replace the quizzes (fix 2 below) at the same length.

### Q6. Short
- Text is inside the safe area: headlines sit in the top third (x 8-92 % of width), the labels under them are centred and short; nothing is in the bottom fifth. Labels ("to a plan", "to join in", "to give permission") are readable.
- Closing card "Want 20 ways to say yes? / Watch the full lesson on this channel." is clear (16.9-22.4 s; voice 16.7-20.7 s). The yellow second line runs to about 92 % of the width at about 48 % of the height, right where the like button column begins. Probably clear, worth one look on a phone.
- The subscribe pill and bell sit at x 100-1294 of 1440 and y 1910-2129 of 2560 (75-83 % of the height). The bell (x 1094-1294) is likely to sit under the right-hand buttons, and the lower edge reaches the caption zone. It covers no text.
- Hook: text and voice start at 0.0 s ("Don't just say yes"), the word is struck out by 3 s, first answer at 4.8 s. Good.
- The background is much busier than in the long video (brighter ghost phrases plus faded logo tiles); a ghost "by all means." sits directly behind the headline "By all means." at 12.6 s. Still readable.

## 4. Pain -> what the video gives -> gap (LONG)

- Gives: 20 answers grouped by situation, a plain meaning for each, register flags where they matter ("informal, American" for You bet, "polite, formal" for Certainly, "informal" for Totally and For sure, "use it to give permission" for By all means, "people often shorten it to I'd love to"), a short dialogue for each, and 20 lines to say out loud with a pause.
- Gaps:
  1. The choice is never practised. Only quiz 2 (Certainly / Yep to a customer asking for the bill, 136.6 s) makes the learner choose between two ways to say yes. The other three offer a non-yes word as the wrong option.
  2. No boss or work case, although the learner asks "friend vs boss". The nearest are "No problem, I'll send it now" and "Works for me", neither marked as work-safe or not. Nothing says what NOT to use (for example Yep or You bet in a formal email).
  3. Part 3 "When you agree" mixes two things: agreeing with an opinion (Exactly, Totally) and a strong yes to a question (Absolutely: "Was the film worth seeing?", For sure: "Is it going to rain?"). "Definitely" answers a wedding invitation, which belongs to Part 4. A learner sorting by situation gets a blurred picture here.
  4. "Yeah", the most frequent of all 20 in real speech, is the one with doubtful audio.

## 5. Second-by-second notes (LONG)

- 0.0-2.6 s: my search phrase, spoken and on screen. I stay.
- 2.6-13.6 s: one static card for 13.6 s while the voice lists the four situations. Slowest stretch of the video; a search viewer accepts it, a browse viewer may leave around 8-10 s.
- 13.6-18.2 s: Part 1 card with five emoji tiles and the five answers. Good preview.
- 18.2-57.5 s: five cards, about 7.5 s each, picture and voice in step (headline, then meaning, then example, each appearing as it is spoken). 25.6 s: "Yeah" headline is the doubtful audio.
- 57.5-68.3 s: quiz 1 (Sure / Sorry). Too easy; 3 s silent countdown.
- 68.3-91.3 s: drill 1. Works. 74.7 s: the "Yeah" model line heard as "Yes".
- 96.0-96.4 s: subscribe pill over the label "Of course".
- 91.3-172 s: Part 2. Best part: Certainly vs Yep quiz at 136.6 s is the one moment the video teaches register.
- 172-255 s: Part 3. Category blur as described. Drill pauses up to 4.0 s of pure silence (no music); risk of a swipe at 232-255 s, the third identical drill block.
- 260.0-260.4 s: subscribe pill over the label "Sounds good".
- 255-338 s: Part 4, the most useful set for daily life. 293.3 s: "I would love / to" orphan line; the spoken note about "I'd love to" is good.
- 338.9-345.8 s: site tip. 345.8-354.0 s: question for the comments, then 3.1 s of silence.

## 6. Takeaway test

LONG: yes, an action can be named: "Tomorrow, when someone proposes a plan, say 'Sounds good' or 'Works for me'; when someone asks for something, say 'Of course' or 'No problem'." The closing question "Which answer will you use today?" pushes exactly that.
SHORT: yes: say "Sounds good" to a plan, "Count me in" to join, "By all means" to give permission.

## 7. Risks

Retention (LONG): 13.6 s static hook card; four identical quiz+drill blocks; about 75 s of total silence without any sound bed; one voice for both speakers. Voice speed 1.0 is fine for B1-B2.
Trust (LONG): "Yeah" audio; quizzes that cannot be failed; "Certainly, sir." is waiter English (true, but it is the only formal example); Part 3 label vs examples. No wrong facts found, register labels are accurate, the English is natural.
Trust (SHORT): none found. Title says "Like a Native Speaker", content matches.

## 8. Ship blockers

### LONG: 2
1. **Subscribe animation covers text** at 96.00-96.37 s (label "Of course") and 260.00-260.43 s (label "Sounds good"). Change: start the animation after the part-title card has gone, at about 96.5 s and 260.6 s (word cards have empty space bottom left), re-run `shorts/subscribe_anim.py`, and copy the new printed times into `content/youtube/long-other-ways-to-say-yes-v1.json` -> `subscribe_at`. Owner: shorts-builder.
2. **"Yeah" is not heard as "Yeah"** at 25.6 s (headline, heard "Yep" / "Jaffa") and 74.7 s (drill model line, heard "Yes, see you at 8"). I cannot listen, so this is a blocker until a person has listened to 0:25, 0:31 and 1:14. If the ear confirms it: take the voice's own good "Yeah" from the example clip `b04-2.wav` (31.3 s, recognised at 0.86) and splice it into the headline and the drill line, keeping the lengths identical (method as in `content/specials/S3/polish-v2-build/fix_big.py`), or re-voice the two clips. Listen to the "Yep" headline at 0:34 in the same pass. If the ear says "Yeah" is clear, this blocker falls away. Owner: voice.

### SHORT: 0

## 9. Nice-to-have fixes

LONG
1. (scenario-writer) Replace quizzes 1, 3 and 4 with register choices between two real ways to say yes, in a new sentence, for example: boss asks "Can you send me the report by five?" -> Certainly / Yep; friend says "Pizza tonight?" -> Sounds good / Certainly, sir. Add one work example. This is what would move the verdict to SOLVES.
2. (shorts-builder) Force the line break between the two speakers on every example card, and never break inside the taught phrase (7 cards listed in Q3).
3. (shorts-builder) Headline fitting: keep "I would love to" on one line or break as "I would / love to"; treat "No problem" the same way as "By all means". Fix the Part 4 strip label too.
4. (scenario-writer) Part 3: either rename it "A strong yes" or move "Definitely" to an opinion example ("Is she the best player?" "Definitely.").
5. (shorts-builder) Hook: change the picture at least once during the first 13.6 s (show the four situation names as they are spoken).
6. (shorts-builder) Keep ghost background words out of the countdown area and away from line ends.
7. (shorts-builder / publisher) The closing card (345.8-354.0 s) has its text in the centre of the frame, where end-screen tiles go; place the tiles so the question stays readable, or move the text up.
8. (voice / shorts-builder) Long audio is 24 kHz mono, the Short is 44.1 kHz stereo and 2.5 dB quieter; bring both to one standard.
9. (voice) A second voice for the answering speaker would make the dialogues easier to follow.

SHORT
1. (shorts-builder) Move the subscribe pill and bell up and left so the bell is not under the right-hand buttons (now at 75-83 % of the height, bell at x 1094-1294 of 1440).
2. (shorts-builder) Wrap the yellow closing line a little narrower (it runs to about 92 % of the width at mid height).
3. (visuals) Tone the ghost phrases and logo tiles down to the level of the long video.

## 10. Top 3 fixes by impact (LONG)
1. voice: confirm by ear and repair "Yeah" (25.6 s, 74.7 s).
2. shorts-builder: move the two subscribe animations off the part-title cards (96.5 s, 260.6 s) and update `subscribe_at`.
3. scenario-writer: make the quizzes test the choice of register (boss vs friend) and add one work example.
