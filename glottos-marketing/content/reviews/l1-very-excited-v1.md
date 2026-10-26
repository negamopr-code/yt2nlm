# Viewer-critic review: l1-very-excited-v1 (lab H38)

Reviewed 2026-10-08. File: state/shorts/l1-very-excited-v1/final.mp4 (1440x2560, 30 fps, 18.51 s, voice Kokoro am_michael 1.05x).
Unit: shorts/units/l1-very-excited-v1.json. Meta: content/youtube/l1-very-excited-v1.json.

## Verdict: PARTLY
The viewer gets three correct, usable replacements with a ready phrase each in 17 s, but nothing tells them when each word fits (after an event / informal / before an event), there is no self-test, and the "Pumped" picture does not show the meaning.

Ship blockers: 0. Fixes recommended before the next cut: 3 (below).

## Pain -> what the video gives -> gap
- Pain (my wording, lane-level): "I always say 'very excited'; I want one stronger word I can use today."
- Learner evidence: no verbatim learner quote about overusing "very" was found in content/problems or content/insights/audience-needs.md (grep only; no NotebookLM query spent). Only format praise is on file: "very helpful thanks :)", "Useful information... I'll share it to my close ones", and one viewer adding a word on the Very Small Short: "There is also minuscule as in a minuscule mouse." The pain is therefore taken from the task brief, not proven by quotes.
- Gives: 3 words + 3 phrases, each seen, heard twice, and pictured.
- Gap: the three words are not interchangeable. Exhilarated = after an intense experience; pumped = informal, American, before an event; thrilled = the general one. The card says none of this ("informal" is only in the YouTube description). A learner could write "I am pumped about the job offer" to a manager.

## Checks asked for
- Resolution: PASS. 1440x2560.
- Subscribe + bell: PASS. Visible from about 13.5 s to 18.0 s, bottom-left (red SUBSCRIBE -> grey SUBSCRIBED, bell rings yellow at about 16.5 s). It sits below the picture and the card text and covers neither. Recorded: final.subscribe.json and meta "subscribe_at": [13.4]. Second half of the Short: yes.
- Strike in frame 1: PASS (frame at 0.0 s already struck out).
- Magnifying glass: none in any picture.
- Garbled writing: none. Embedded captions read "Feeling exhilarated after the ride.", "Being pumped for the big game.", "Being thrilled about the trip."
- Cut off / overlap: nothing on the card. In picture 1 the face is cropped by the right edge of the source frame (minor). A faint smudge at the bottom-right of each picture (looks like a removed watermark); not visible at phone size. No NotebookLM/Gemini watermark seen.
- Spelled-out words: none.

## Audio (faster-whisper small.en, whole file and per beat)
Whole file: 0.00 Stop saying very excited. | 2.28 Say this instead. | 4.12 Exhilarated. | 5.70 Exhilarated after the ride. | 8.46 Pumped. | 9.34 Pumped for the big game. | 11.98 Thrilled. | 13.20 Thrilled about the trip. | 15.54 Which one is new to you? (ends 16.80)
All 29 scripted words recognised in the final mix; none dropped.
Per beat: b02-0 "Exhilarated." (0.85), b02-1 "exhilarated after the ride." (0.78 on the word), b04-0, b04-1, b05-0, b01-0, b01-1 all exact.
b03-0.wav (the lone "Pumped.") was heard in isolation as "pumped it." (0.65 / 0.40): the final plosive is released hard enough to sound like an extra syllable. In the final mix it is recognised as "Pumped." (0.95). Worth one human listen, not a blocker.
NOT checked: I cannot listen. "Exhilarated" is recognised correctly three ways, which rules out a gross mispronunciation, not a wrong stress. The language editor's note "listen to 'exhilarated' after voicing" is still open for a human ear.
Level: max -3.0 dB, mean -27.1 dB (includes the pauses).

## Second by second
- 0.0-1.6: "Stop saying very excited", struck out from frame 0. Clear, it is my phrase. I stay.
- 1.6-3.1: "Say this instead". Fine.
- 3.1-4.1: 1 s of silence before the first word; card shows "Exhilarated" from about 3.7 s. Slight dead air; tolerable.
- 4.1-8.0: Exhilarated + phrase + roller coaster. Picture and voice match. Longest and hardest word comes first; some B1 viewers will not be able to repeat it after one hearing.
- 8.4-11.5: Pumped. Picture: a gloved hand holding an American football on a tee, with flames. No person, no feeling. Viewers outside the US may not recognise the ball; "pumped" beside a ball reads as "pumped up with air". Weakest beat.
- 12.0-15.0: Thrilled + plane and island. Clear. The subscribe button pops in at 13.4, exactly as the third example is spoken (13.2-14.2), and pulls the eye off the word.
- 15.5-16.8: "Which one is new to you?" Easy to answer; good.
- 16.8-18.5: 1.7 s with no voice, animation finishing. Acceptable for a loop.
Swipe risk is low; at 18.5 s there is no intro and no chatter.

## Takeaway test
"Tomorrow I say 'I'm thrilled about the trip' instead of 'very excited'." Nameable, so not DOESN'T. It is not SOLVES because the viewer cannot tell which of the three to choose, and never tries one.

## Retention risks
- Example text in the pictures repeats the card line and is too small to read on a phone; harmless but wasted.
- Moving word wallpaper puts bright "exhilarated"/"thrilled" directly behind and above the headlines (13.6 s, 16.5 s). Adds clutter around the CTA.
- Subscribe row sits at about 76-84 % of the height. The Shorts player draws the channel name and title in that area; part of the animation may be hidden in the real feed. Check on a phone after the private upload.

## Trust risks
- "Stop saying" overclaims: "very excited" is correct English. Lane convention, accepted.
- "Pumped" shown with no register label on screen.
- "Exhilarated" is narrower than "very excited"; the example carries it, the card does not say so.

## Top 3 fixes (by impact)
1. visuals: replace the "Pumped" picture with a person visibly fired up before a match (fan or player, fist raised). Keep the caption.
2. scenario-writer + language-editor: add a 1-2 word usage tag on each card ("after a thrill", "informal", "good news") so the viewer can choose; or put Thrilled first as the safe default.
3. shorts-builder: start the subscribe animation at about 14.4 s (after "trip."), not 13.4, and verify on a phone that the Shorts overlay does not hide it; dim the wallpaper behind headlines.
