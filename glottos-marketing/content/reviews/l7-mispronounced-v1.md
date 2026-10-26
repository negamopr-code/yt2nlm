# Viewer-critic review: l7-mispronounced-v1 (lab H41, pronunciation, "Say It Right")

Reviewed 2026-10-07. Video: `state/shorts/l7-mispronounced-v1/final.mp4` (19.93 s, 1440x2560, 30 fps). Unit: `shorts/units/l7-mispronounced-v1.json`. Read-only review: nothing rendered, changed or uploaded.

## Verdict: PARTLY (SOLVES once blocker 1 is cleared)

For these three words the video does the job: I see the way I read it crossed out, I hear the real word slow and then normal, and I get a spelling I can read. Tomorrow I say WENZ-day. But in a video whose only product is the sound, the slow model of "Salmon" starts with an extra low voiced sound before the "s" (8.40-8.50 s), and nobody has listened to it with human ears. Until that one clip is clean, I cannot call it solved.

Ship blockers: **1** (audio, slow "Salmon"). Everything else passes.

## Pain (learner's words) -> what the video gives -> gap

No PROBLEM NN document exists for this lab Short. Quotes are verbatim from the learner comment corpus (`reports/monitor-awf/archives/youtube-comments-vol*.md`, grep "pronounc / pronunciation"):

- "Actually I did know the word but didn't know how to pronounce it."
- "Why do you write a letter and pronunce another?"
- "it is hard sometimes for us who learn English cuz often the pronunciation is kinda confusing."
- "I have to check each and every word how to pronounce in Cambridge dictionary to sound it correct and then continue to read"
- "A traditional italian accent (speaking english like italian) would change a lot the vowels sounds and pronounce almost every letter"
- "me too bro, my pronunciation is so bad"
- "I'm worried about my pronunciation of the vocabulary word"

Note: none of these names Wednesday, salmon or island. The corpus supports the general pain (reading every letter), the three words come from the lab hypothesis, not from comments.

Pain in one sentence: "I know the word from reading, I say every letter I see, and nobody tells me the real sound."
Solved would mean: tomorrow I say these words the short way without stopping to think, and I know which part of my version was wrong.

What the video gives: my reading crossed out (Wed-nes-day, sal-mon, is-land), the word big, the real sound twice (slow, then normal), a respelling (WENZ-day, SAM-un, EYE-lund), and a question that makes me check myself.

Gap:
1. The big word never shows WHICH letter is silent. I have to compare "sal-mon" with "SAM-un" myself. The d, the l and the s are the whole lesson and they look like every other letter.
2. The respelling arrives only with the second (normal) take: 6.6 s, 10.0 s, 13.6 s. During the slow take, the moment I am matching sound to letters, it is not on screen. It then stays about 1.8 s.
3. Nothing tells me to say it. There is a 1.2 s gap after each normal take that is clearly meant for me, but "say it out loud" is only in the description.
4. Three words, no pattern. It fixes three words, it does not teach me to suspect the next one. Fine for a 20 s test, but that is the ceiling.

## Mandatory checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Resolution >= 1440 short side | PASS | ffmpeg probe: h264 1440x2560, 30 fps, 19.93 s |
| 2 | Subscribe + bell visible inside 14.9-19.9 s, not covering card text | PASS | Fades in at about 15.0 s under the Island card; red SUBSCRIBE + bell + cursor at 15.2-16.5 s; grey "SUBSCRIBED" + bell from about 16.6 s; yellow bell from about 18.2 s; fades out by 19.8 s. Button about y 1912-2140 px, lowest card text ("comments.") ends about y 1410 px: 500 px clear. Recorded in `final.subscribe.json` and `content/youtube/l7-mispronounced-v1.json`: `subscribe_at [14.9]`. Note: the button's lower edge is about 20 px above the 400 px bottom zone and the bell reaches x about 1300 px, near the Shorts like/comment column (same position as l6). |
| 3 | Card text inside safe area, nothing cut off, readable over the background | PASS, with a defect | All card text sits between about y 400 and y 1410 px, full width with margins, nothing cropped. Headlines and respellings are fully readable. Defect: the small grey struck-out form lies on top of grey background words of the same colour: "is-land" directly over a large grey background "island" (14.6 s), "sal-mon" over a logo tile and a grey "wednesday" (11.0 s). Readable at full resolution, messy at phone size. |
| 4 | Struck-out form on screen from the first frame | PASS | Frame 0 (0.000 s): "3 words you're probably mispronouncing" plus yellow "Wed-nes-day" with the red line, fully drawn. No empty first frame (the l6 defect is gone). |
| 5 | Each word audibly said twice; slow take not distorted or clipped | FAIL on one clip | Twice: yes, all three (silencedetect speech: Wednesday 4.77-5.61 and 6.57-7.20; Salmon 8.40-9.12 and 10.09-10.64; Island 11.89-12.67 and 13.67-14.20). Slow takes are native Kokoro speed 0.8, not time-stretched (`kokoro_jobs.json`). No clipping: peaks -3.5 to -6.1 dB, flat factor 0, every clip starts and ends in silence (-73 dB or lower in the first and last 20 ms), no cut onsets or tails. BUT `b03-0.wav` (slow Salmon) has a voiced sound BEFORE the "s": 0.06-0.15 s, pitch about 113 Hz, 89 % of energy under 500 Hz, -27 dB (about 10 dB under the vowel), with two click-like vertical lines at about 0.09-0.11 s on the spectrogram. The normal take `b03-1.wav` starts straight on the "s" (0 % energy under 500 Hz). It is in the final mix at 8.40-8.50 s. faster-whisper small.en hears "The Salmon" on the isolated slow clip (it hears plain "salmon" on final.mp4). See blocker 1. |
| 6 | On-screen text matches the approved unit character for character | PASS | Hook: "3 words you're probably mispronouncing" / struck "Wed-nes-day" / "Say them like this." Cards: "Wed-nes-day" / "Wednesday" / "WENZ-day"; "sal-mon" / "Salmon" / "SAM-un"; "is-land" / "Island" / "EYE-lund". Close: "Which word did you say wrong?" / "Write it in the comments." All identical to the unit, including capitals, hyphens, apostrophe and full stops. Header: "anotherwordfor.net", pill "SAY IT RIGHT" (series name), official channel logo. |
| 7 | No magnifying glass | PASS | No pictures at all; none in any frame. |
| 8 | Title / description promise only what the video contains | PASS | "3 Words You're Probably Mispronouncing": three words, yes. Description: the three respellings as on screen; "Listen to each word twice, slow and then at normal speed": true; closing question identical. No overclaim. |
| - | Spelled-out word | PASS | None in the transcript. |
| - | Watermark | PASS | No NotebookLM/Gemini mark. |

## Transcript as heard (final.mp4, faster-whisper small.en, word timings)

0.00 "Three words you're probably mispronouncing." (to 2.24) | 3.00 "Say them like this." (to 4.22) | 4.94 "Wednesday," | 6.08 "Wednesday," | 8.48 "salmon," | 10.70 "salmon," | 12.12 "island," | 13.60 "island." | 15.28 "Which word did you say wrong?" (to 16.64) | 17.14 "Write it in the comments." (to 18.02) | silence 18.23-19.93

Silences (silencedetect -35 dB): 0.60 s at 2.25; 0.88 at 3.89; 0.96 at 5.61; 1.20 at 7.20; 0.97 at 9.12; 1.25 at 10.64; 1.01 at 12.67; 1.19 at 14.20; 0.40 at 16.69; 1.71 at 18.23. About 10.2 s of 19.9 s (51 %).

## Second-by-second notes

- 0.00-2.2: "3 words you're probably mispronouncing" and a crossed-out "Wed-nes-day". That is exactly how I say it. I stop. Best hook of the lab Shorts so far: my mistake is on screen in frame 0.
- 2.2-4.7: "Say them like this." Fine, short. 0.9 s of silence before the first word is the only slow moment in the hook.
- 4.7-6.6: "Wednesday", slow. I hear it has two beats, not three. But the screen shows only the crossed-out form and the normal spelling: no respelling yet, so I cannot see what I just heard.
- 6.6-8.4: "WENZ-day" appears with the normal take. Now it clicks. 1.2 s gap: I would repeat it if someone told me to.
- 8.4-10.0: "Salmon", slow, with a small extra sound in front of the "s" (blocker 1).
- 10.0-11.8: "SAM-un". Clear. This is the one I really did say wrong.
- 11.8-15.4: "Island", "EYE-lund". Clear. At 15.0 s the subscribe button slides in under the card while I am still reading; it does not cover anything.
- 15.4-18.2: "Which word did you say wrong?" Good question, I have an answer (salmon).
- 18.2-19.9: 1.7 s silent tail with the yellow bell. Acceptable for the loop, a little long.
- No point where I would swipe. The risk is not swiping, it is that the three word beats feel identical and half of each is silence.

## Takeaway test

Action I can name: "Say Wednesday as WENZ-day, salmon as SAM-un, island as EYE-lund: do not say the d, the l or the s." Concrete, usable tomorrow. Passes.

## Retention risks

- 51 % silence. Here most of it is useful (repeat gaps), but the video never asks me to repeat, so to a scroller it is just quiet. A "Your turn" cue would turn dead air into the exercise.
- Three structurally identical beats of 3.5 s. Works at 20 s; would not survive five words.
- Background: drifting "wednesday / salmon / island" plus logo tiles behind every card. On the Wednesday card the next two answers are already floating around; the small struck-out word sits on same-colour background words.
- Text legibility of headline and respelling: good. Voice speed 1.05: fine. Text and voice in sync.

## Trust risks

- Facts: correct for General American. Salmon has no accepted l variant, Wednesday and island claims are true. The swap away from "comfortable" by the language editor was right.
- "EYE-lund": a learner who reads letters literally may say "lund" with a full u. The voice corrects it, the text alone does not.
- A synthetic voice as pronunciation model is the hypothesis' own named risk ("the language editor must LISTEN to each word in the render"). The approval note asks for a check by ear; the evidence so far (phonemes, whisper) is machine evidence, and the machine evidence shows the artefact in blocker 1.
- H41 comparability: the test text holds "word-by-word captions" constant; this render has none by design. Read stayed % with that in mind, and correct the H41 text.

## SHIP BLOCKERS

1. **Slow "Salmon" has an extra voiced sound before the word (8.40-8.50 s in final.mp4; `b03-0.wav` 0.06-0.15 s).** Measured: about 90 ms, pitch about 113 Hz, 89 % of energy under 500 Hz, -27 dB, with click-like lines at 0.09-0.11 s; absent in the normal take; whisper prints "The Salmon" for the isolated clip. In a pronunciation video the slow take IS the product; "uh-salmon" is a wrong model. Owner: **voice** (regenerate the 0.8 clip, or cut the first 0.15 s of `b03-0.wav` and fade in over about 10 ms, padding with silence so the length stays identical), then **shorts-builder** re-mux, then **language-editor** listens to all six word clips by ear. If a human listens and hears nothing before the "s", this blocker is cleared without a rebuild; I could not listen, I can only measure.

## Notes for the next test (not blockers)

1. **Mark the silent letter in the big word** (scenario-writer + shorts-builder): Wednesday with the first d grey, Salmon with the l grey, Island with the s grey. This is the one-glance answer to "why do you write a letter and pronounce another".
2. **Show the respelling from the slow take on** (shorts-builder), not only with the normal take; the slow take is when eyes and ears are matched.
3. **Fill the repeat gap** (scenario-writer): a small "Your turn" on the card during the 1.2 s after each normal take; "say it out loud" is now only in the description.
4. **Clean the background on word cards** (shorts-builder): no grey background words behind the grey struck-out form, and no upcoming answers drifting behind the current word.
5. **Correct H41's "held constant" list** (lab owner): it says word-by-word captions; this render has none. Also trim the silent tail from 1.7 s to about 0.8 s.

## What was checked / not checked

Checked: ffmpeg probe; 100-frame contact sheet at 5 fps; frames at 0.0, 0.033, 0.1, 0.3, 1.5, 3.8, 6.5, 10.0, 13.5, 15.1, 15.2, 15.8, 16.5, 17.5, 18.5, 19.0, 19.6, 19.85 s; full-resolution crops of the hook, the three word cards (slow and normal phase) and the subscribe button; faster-whisper small.en word timings on final.mp4 and on all nine beat wavs; silencedetect; per-clip peak, flat factor, onset and tail levels; 50 ms energy / zero-crossing profile of the slow clips; spectrograms of `b03-0.wav` and `b03-1.wav`; band-energy check of final.mp4 at 8.3-8.9 s and 9.95-10.55 s; unit JSON; `kokoro_jobs.json`; `final.subscribe.json`; `content/youtube/l7-mispronounced-v1.json`; H41 in `/workspace/glottos-auto/out/lab/lab.json`; learner comment corpus.
Not checked: human listening (every audio judgement is measurement or whisper; whether the l is truly silent in the slow Salmon take rests on the phonemes and on whisper, the spectrogram shows the same vowel-to-m shape in both takes but that is not proof); the video on a real phone inside the Shorts player (overlay positions estimated from pixel coordinates); `final-nosub.mp4` (only confirmed it differs from final.mp4); no NotebookLM query used.

## After the review (autopilot, 2026-10-07T19:15Z)
Ship blocker fixed: the 0.17 s before the "s" of the slow "Salmon" clip was replaced by silence with a 12 ms fade-in
(`state/shorts/l7-mispronounced-v1/override-3-0.wav`, same clip length) and the Short was rendered again. Measured in the new
`final.mp4` at 8.3-8.8 s: digital silence, then the "s" at once (no voiced sound before it); the recogniser prints "Salmon" for the
clip alone. Audio gate OK (19.9 s, longest silence 1.5 s). Measured, not listened to by a person.
