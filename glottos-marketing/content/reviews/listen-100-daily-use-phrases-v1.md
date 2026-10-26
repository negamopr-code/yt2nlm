# Viewer critic — listen-100-daily-use-phrases-v1 (lab H22, long 16:9)

Reviewed 2026-10-03. Video: `state/shorts/listen-100-daily-use-phrases-v1/final.mp4` (1920x1080, 25:23.4, audio AAC 24 kHz mono 40 kb/s).
Title: "100 Daily Use English Phrases | Listen and Repeat Practice".

## Verdict: SOLVES — 0 ship blockers

It is exactly the drill the title and thumbnail promise: 100 numbered everyday phrases, each heard twice with a real pause to say it, then all ten again; usable with the screen off; first phrase at 0:22. The defects found are polish (tip card text, abrupt ending, small counter), none of them stops a learner from doing the drill.

## Pain -> what the video gives -> gap

- Pain source: no PROBLEM-NN doc for this lab unit, so no learner quotes are used (none invented). The pain is the search intent given in the brief: an A2–B1 learner typing "100 daily use english phrases / listen and repeat" wants a long, calm drill — hear an everyday phrase, get time to say it, hear it again, without having to watch the screen.
- "Solved" means: tomorrow they can say a handful of these phrases out loud without building them word by word.
- What the video gives: 100 phrases in 10 everyday situations, each spoken aloud by the learner 3 times (2 in the drill + 1 in the recap) = 300 speaking turns in 25 minutes. 72% of the runtime is the learner's own speaking time.
- Gap: small. No meaning support (no context line, no translation) — for A2 a few items ("What have you been up to?", "I don't mind", "Keep the change") are repeated without knowing when to use them. The cluster's competitors mostly don't give it either, so it is not a broken promise.

## Evidence

### (1) Promise vs delivery — delivered
- Audio segmentation of the whole track: 339 speech segments, exactly the 339 expected from the unit (6 hook sentences, 10 part titles, 90 phrases x2, 10 "instead" intros + 10 stronger phrases x2, 10 recap intros + 100 recap phrases, tip, closing), in the right order.
- Whisper (small.en) over the full 25 min: every phrase present and correct. The 31 spots where my automatic alignment disagreed were word-timestamp drift at segment edges; all 19 I re-transcribed in isolation came back clean (e.g. 6:51 "Now say all 10 again", 7:45 "How much is this?", 16:43 "What's the deadline?", 23:12 "I'm going to bed.").
- No word spelled letter by letter anywhere in the transcript. No caps artefacts.
- Counter reaches 100 / 100 at 24:24 ("Take care."). Length 25:23 sits at the short end of the cluster (17–73 min) — fine.
- Chapters file matches the audio to the second (0:19, 2:41, 5:06, 7:43, 10:16, 12:55, 15:36, 18:04, 20:23, 22:56, 25:16).

### (2) Pacing — right, slightly generous
Measured from the audio (silence between speech segments):
- Pause after a phrase: min 2.74 s, median 3.5 s, max 4.92 s. No silence longer than 4.92 s anywhere, no pause shorter than 2.74 s.
- Shortest phrases: "Good night!" 0.70 s spoken -> 2.74 s pause; "Good morning!" 0.76 s -> 3.06 s; "What's new?" 0.76 s -> 2.80 s; "I'm full." -> 2.9 s. Enough to say it once comfortably, with about 1–1.5 s left over.
- Longest: "Excuse me, where is the station?" 1.9 s -> 4.9 s; "Can you speak more slowly, please?" 1.92 s -> 4.4 s. Not rushed.
- Note for the builder: the real pause is about 3.2x the audible phrase, i.e. roughly 1 s longer than "1.4 x phrase + 0.8 s" suggests, because the formula is applied to the TTS clip including its leading/trailing silence ("Good morning!" clip is 1.56 s, audible speech 0.76 s). For A2 this is comfortable; a B1 viewer gets about 1 s of dead air per turn, x300 turns. Do not shorten for this release; worth an A/B later.
- Announcements are tight: "Instead of ..., say this" -> phrase after 0.6–0.8 s; "Now say all ten again" -> 1.0 s; part titles -> 0.8–1.1 s.

### (3) First 30 seconds — clear, a little wordy
- 0:00–0:19 spoken instructions (6 sentences, 0.5–0.7 s gaps, no dead air, no channel intro, no names, no jargon). 0:20 "Part 1. Greetings." 0:22.3 first phrase "Good morning!". First own speaking turn at 0:23.
- The first sentence is the title itself ("One hundred English phrases for daily use. Listen and repeat."), so a clicker gets confirmation in 3 s.
- Weak point: the first frame is a 9-line block of small text under a "LISTEN" pill — the hook card headline "100 Daily Use English Phrases / Listen and repeat" from the unit is never shown. It looks like a transcript, not a title. 19 s of talk before the first phrase is acceptable for this genre but could be 10–12 s.

### (4) Screen — correct, nothing clipped (about 60 frames sampled)
- Phrase text about 80 px high at 1080p, white on black, karaoke word in yellow, 2 lines max in the samples ("Can you speak more slowly, please?", "Excuse me, where is the station?") — readable on a phone, nothing cut off.
- Labels correct in every sample: LISTEN (0:22.5) -> YOUR TURN: SAY IT, green (0:24) -> LISTEN AGAIN (0:26) -> YOUR TURN: SAY IT (0:28). SAY THIS INSTEAD, yellow, with the sub-line `instead of "I'm fine."` at 1:42.5, then the normal LISTEN / YOUR TURN cycle at 10 / 100. ALL TEN AGAIN + "Say all ten again" at 1:54.6, 11:59, 24:30. PART n OF 10 cards at 0:21, 2:43, 12:55.
- Counters correct in every sample: 1, 2, 3, 9, 10, 20, 25, 26, 31, 50, 51, 69, 100 of 100; recap 1/10, 2/10, 3/10, 4/10, 5/10, 7/10, 8/10, 9/10, 10/10.
- Karaoke highlight matches the voice where checked (0:22.5 "Good", 1:44.2 "great,", 12:59 "is").
- Defect A (tip, 12:48–12:54): the card shows the TTS respelling as text — "look it up on another word for dot net." — under a "LISTEN" pill. The unit's card ("Need another word? / anotherwordfor.net") is not shown. The only place the video sells the site spells the address wrong on screen. The header does carry "anotherwordfor.net" all the time, which softens it.
- Defect B (end, 25:16–25:23): the closing card is again the full speech as a small paragraph under "LISTEN", and the file ends 0.9 s after "Write it in the comments." No time to read the question, no room for a YouTube end screen (needs 5–20 s).
- Defect C: the counter ("10 / 100") is small, thin and grey (about 28 px at 1080p) — hard to read on a phone. It is the only progress signal.
- Defect D: during YOUR TURN the waveform disappears and nothing moves; there is no bar showing how much pause is left. Screen-off users don't care; screen-on users can't tell if the video froze.
- One static host picture for 25 minutes. Acceptable for a drill that tells you not to look.

### (5) Would a learner leave in the first minute?
- Low risk. No intro bumper, no chatter, first phrase at 0:22, phrases are the expected ones ("Good morning!", "How are you today?", "Nice to meet you."). Thumbnail (100 / DAILY USE ENGLISH PHRASES / LISTEN & REPEAT + host) matches the first frame.
- The only early swipe reasons: the text wall at 0:00–0:19, and a viewer who expected a slower "teacher" voice — phrases are said at natural speed ("Good morning!" in 0.76 s). The second hearing and the recap compensate.

## Second-by-second notes (where someone could leave)
- 0:00–0:19 instruction text wall; a small share will skip ahead (chapters let them).
- 0:22–1:40 drill starts, steady rhythm, nothing to leave for.
- 1:41 first "say this instead" — a pleasant change of colour and voice pattern.
- 1:54–2:40 first "all ten again": a third pass over phrases heard 20 s ago. B1 viewers will skip recaps; A2 will use them. Chapters make skipping easy.
- 12:48 tip: 6 s, short enough not to lose anyone; text looks wrong (Defect A).
- 25:16–25:23 closing question, then a hard stop.

## Takeaway test
Passed: "I said 100 everyday phrases out loud three times each; today I pick one and use it" — the closing line asks exactly that.

## Retention risks
- 72% silence is by design, but about 1 s per turn is spare for B1 (see pacing).
- One voice, one picture, identical rhythm for 25 min; the "instead" beat every tenth phrase is the only variation.
- Recaps add 7.5 min; fine for the genre.

## Trust risks
- "Instead of X, say this" overclaims a little for three pairs where X is perfectly good English: "Thank you" -> "I really appreciate it" (21:52), "Goodbye" -> "Take care" (24:20), "I agree" -> "Absolutely" (17:05). The hook softens it ("a stronger way to say something simple"); a comment like "so thank you is wrong?" is possible.
- Stronger phrases don't always fit their part: "I'm exhausted" in "At home in the morning", "It's enormous" in "Getting around".
- "another word for dot net" written on screen (Defect A).
- English itself is natural US usage throughout (check, credit card, checkout).

## Fixes, ranked
1. shorts-builder — tip beat (12:48): show the card, not the TTS string: headline "Need another word?", sub "anotherwordfor.net", pill "TIP" instead of "LISTEN". Keep the spoken respelling in audio only.
2. shorts-builder — ending: show the closing card as a headline ("Which phrase will you use today?" / "Write it in the comments.") and hold it 8–10 s after the last word so an end screen fits.
3. shorts-builder — hook: show the unit's headline card ("100 Daily Use English Phrases" / "Listen and repeat") for 0:00–0:19 instead of the 9-line paragraph, or cap the caption at 2 lines at a time. Optional for scenario-writer: cut the hook to about 10 s (drop "Every tenth phrase..." — the SAY THIS INSTEAD label explains itself).
4. shorts-builder — make the counter bigger and brighter (about 44 px, white at 80%), and add a thin bar that drains during YOUR TURN.
5. shorts-builder (next unit, as an A/B, not this one) — compute the pause from the audible phrase length, not the padded clip; target about 2.2–2.5x audible length.
6. scenario-writer (next unit) — soften the three "instead of" pairs where the plain phrase is not weak ("Another way to say thank you:"), and place each stronger phrase in a part it belongs to.

None of 1–6 blocks publishing v1. 1 and 2 are cheap and worth doing before upload if a re-render is affordable.

## What was checked / not checked
- Checked: full-track silence/speech segmentation (all 339 segments, durations and gaps); full faster-whisper small.en transcript with word timings plus 22 isolated re-transcriptions; about 60 frames (0:00–0:45 dense, 1:36–2:43 dense, 4:12–4:16, 5:50–6:02, 7:54, 11:56–13:02, 16:59, 24:24–25:23); thumbnail; chapters vs audio; unit text vs audio.
- Not checked: I did not hear the audio (prosody, intonation of questions, clicks at clip joins, how 40 kb/s mono sounds) — whisper only; not every frame (parts 3–4 and 7–9 have one or two frames each); karaoke sync only at three points; competitor videos were not opened (pause norms taken from the brief).
