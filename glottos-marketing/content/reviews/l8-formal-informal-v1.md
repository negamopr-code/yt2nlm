# Viewer-critic review: l8-formal-informal-v1 (lab H42, register in two columns, "Formal vs Informal")

Reviewed 2026-10-07. Video: `state/shorts/l8-formal-informal-v1/final.mp4` (24.52 s, 1440x2560, 30 fps). Unit: `shorts/units/l8-formal-informal-v1.json`. Read-only review: nothing rendered, changed or uploaded.

## Verdict: PARTLY (SOLVES for a 24 s test once blocker 1 is cleared)

I typed "formal vs informal english" and I get exactly that: five everyday words, each with its formal twin next to it, and one line that says where to use them. Tomorrow I can write "purchase" instead of "buy" in a work email. But the right column and the tip line run to 90 px from the right edge in the lower half of the screen, where the Shorts like / comment / share buttons sit: by my measurement the end of "conclude" and of "essays." is under those buttons. And I get five swaps with no sentence, so I do not see how "inform" or "assist" sits in a real line.

Ship blockers: **1** (layout, right-hand button column). Audio, text, resolution and the subscribe animation pass.

## Pain (learner's words) -> what the video gives -> gap

No PROBLEM NN document exists for this lab Short. Quotes are verbatim from the learner comment corpus (`reports/monitor-awf/archives/youtube-comments-vol*.md`, grep "formal"):

- "Could you please tell me if these words are used in formal or informal English? thank you"
- "Could we use these vocabs in formal writings? or these are only for informal speaking?"
- "Can these be used in formal writing?"
- "Are there any dictionaries or references to formal words?"
- "No, you can not use these words on the IELTS! Coz these are informal words."
- "Bro but we don't speak like that... This sounds way too formal. It's not grammatically incorrect but it's also not the way we speak."
- "This are too formal, I think some words can be used but if someone always speaks like this he'd sound like a knew it all."
- "It's too formal for a conversation. Thank you!!"

Pain in one sentence: "I know the everyday word, I do not know its formal twin, and nobody tells me where each one belongs."
Solved would mean: tomorrow, in an email to my boss or in an essay, I swap the everyday word for the formal one, and I do not use the formal one when I talk to friends.

What the video gives: five pairs side by side (buy - purchase, help - assist, tell - inform, need - require, end - conclude), each heard once and left on screen; the full table stays up for 5 s (14.7-19.7 s); one rule, "Use formal words in work emails and essays."; one question that makes me check which word I did not know.

Gap:
1. No sentence. I see "tell - inform", I do not see "I will inform the team". Five swaps without one line of use is a word list, not a skill.
2. Only half of "when". The tip says where formal words go. It never says "not with friends", which is the other half of what the corpus complains about ("way too formal", "not the way we speak").
3. These five are easy. A B1-B2 learner knows purchase, assist and require. Only "conclude" and maybe "inform" are likely to be new. The closing question will get short answers.
4. Each word is heard once at speed 1.05 with no gap to repeat. Fine for a list, weak for memory.

## Mandatory checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Resolution >= 1440 short side | PASS | ffmpeg probe: h264 1440x2560, 30 fps, 24.52 s, AAC 44.1 kHz stereo. |
| 2 | Subscribe + bell visible inside 19.5-24.5 s, not covering card text | PASS | First visible on the frame at 19.567 s (half-transparent red SUBSCRIBE + bell) under the tip line: button top about y 2015 px, tip text bottom y 2001 px, 14 px apart, no overlap. By 19.9 s it rests at y 1918-2130 px under the closing card (lowest card text "comments." ends y 1565 px: 350 px clear). Red SUBSCRIBE + cursor to about 21 s, grey "SUBSCRIBED" + bell from about 21.3 s, yellow ringing bell from about 22.5 s, fade-out 24.0-24.4 s. Recorded: `final.subscribe.json` `subscribe_at [19.5]` and `content/youtube/l8-formal-informal-v1.json` `"subscribe_at": [19.5]`. Note: the resting button spans design y 1438-1598; the bottom zone starts at design y 1520 (`SAFE_BOTTOM` in the builder), so its lower half is inside the zone, and the bell reaches x 1300 px. Same position as l6 and l7. It is an animation, not lesson text, so not a blocker, but see blocker 1: check it on the same phone screenshot. |
| 3 | Nothing important under the Shorts UI zone (bottom about 400 design px, right-hand button column) | **FAIL (right column), measured, not seen on a phone** | Bottom: PASS. Tip text ends y 2001 px = design 1501, 19 design px above the 1520 line. Right: bright-text boxes at full resolution: "purchase" x 266-1349 (y 632-740), "require" to x 1290 (y 1312-1420), "conclude" to x 1341 (y 1538-1624), tip line 2 "work emails and essays." x 99-1334 (y 1913-2001). Right margin 90-106 px of 1440 (67-80 design px). "purchase" is high on the screen (25-29 % of height), above the button stack: fine. "conclude" sits at 60-63 % of height and "essays." at 75-78 %, which is where the like / dislike and comment / share buttons stand; the stack takes roughly the right 150 design px (x above about 1240 px). So about 100 px of "conclude" (the "de") and of "essays." (the "s.") lie under the buttons. See blocker 1. |
| 4 | On-screen text equals the unit text, nothing cut at the frame edges | PASS | Column titles "INFORMAL" / "FORMAL"; hook "Formal vs Informal" (yellow) "English" (white) / "5 words you need."; rows buy - purchase, help - assist, tell - inform, need - require, end - conclude (left white, right yellow, lower case as in the unit); tip "Use formal words in / work emails and essays."; close "Which formal word is new to you?" / "Write it in the comments." All identical to the unit, full stops and question mark included. Nothing touches a frame edge: smallest margin is 90 px on the right ("purchase"), 99 px on the left (tip line 2). Header: "anotherwordfor.net", pill "FORMAL VS INFORMAL" (series name), official channel logo. |
| 5 | Audio complete, no stray sounds, no cut words | PASS (measured, not listened to) | All 14 clips start and end in silence (first 20 ms -71 to -79 dB, last 20 ms -73 to -77 dB), tails decay smoothly, no cut onsets. Onsets of the one-word clips: "Buy" has an 80 ms low voiced lead-in (20-100 ms, 95-100 % of energy under 500 Hz, rising -56 to -27 dB) that runs straight into the vowel: that is the voicing of the "b", not a separate sound. "Need" the same for the "n". "End" (`b06-0.wav`): silence to 0.10 s (-66 to -72 dB), then the vowel at once, nothing before it. "Purchase", "Tell", "Conclude" start on their consonant bursts. Mix: max -3.6 dB, no clipping; every clip is present in final.mp4 at full length (speech runs match clip lengths). Recogniser: final.mp4 = "Buy, purchase, help, assist, tell, inform, need, require, and conclude" (the bare "End." at 13.71-14.15 s is printed as "and"); alone, the clips read "Bye." / "Perches" / "Help." / "assist." / "TELL" / "Inform." / "need." / "Require." / "End." / "Conclude.". "Bye" is a homophone of "buy"; "End" is recognised when alone, so "and" in the run is the recogniser's guess from the list rhythm; "Perches" appears only for the isolated clip, in the mix it prints "purchase". No blocker: each word is on screen the moment it is spoken. Loudness is uneven between one-word clips (peaks: "Buy" -2.8 dB, "Need" -6.5 dB, "Five words you need" -0.5 dB): small. |
| 6 | The first frame tells the viewer what this is | PASS, with a defect | Frame 0 shows the logo, "anotherwordfor.net", the yellow pill "FORMAL VS INFORMAL" and the grey column titles "INFORMAL" / "FORMAL". So the topic is readable. Defect: the big hook headline is NOT in frames 0-4 (0.000-0.133 s); it appears at 0.167 s. The voice starts at 0.065 s. In frame 0 the grey title "FORMAL" has a grey background word "purchase" lying across it. If YouTube takes frame 0 as the cover, the cover is an empty table. |
| 7 | Background flying words do not make a row unreadable | PASS, with a defect | Every row is readable at full resolution: white and yellow at full brightness with a dark outline, background words at about 15-20 % brightness. Defect: from about 12 s to 20 s a cluster of very large background words ("require", "purchase", "conclude", "inform") drifts exactly behind rows 3-5; at 15.2 s a dim yellow "conclude" lies behind the yellow "require". At 5.2 s a large grey "buy" sits in the still-empty FORMAL cell of row 1, and at 14.0 s a dim yellow "conclude" hangs in the right column before the real "conclude" arrives. The background is made of the ten answer words, so the answers float around before they are revealed. Messy at phone size, not unreadable. |
| - | Spelled-out word | PASS | None in the transcript. |
| - | Magnifying glass / watermark | PASS | No pictures by design; no NotebookLM/Gemini mark. |
| - | Title / description promise only what the video contains | PASS | "Formal vs Informal English: 5 Words You Need #shorts": five pairs, yes. Description lists the same five pairs in order, the tip and the question verbatim. |

## Transcript as heard (final.mp4, faster-whisper small.en, word timings)

0.00 "Formal versus informal English." (to 2.06) | 2.80 "Five words you need." (to 3.86) | 4.66 "Buy," | 5.46 "purchase," | 6.68 "help," | 7.84 "assist," | 8.88 "tell," | 9.90 "inform," | 11.14 "need," | 12.28 "require," | 13.82 "and" (= "End.") | 14.04 "conclude." | 16.00 "Use formal words in work emails and essays." (to 18.46) | 19.66 "Which formal word is new to you?" (to 21.30) | 21.64 "Write it in the comments." (to 22.62) | silence 22.83-24.52

Silences (silencedetect -35 dB): 0.56 s at 2.15; 0.71 at 3.87; 0.55 at 5.02; 0.69 at 6.16; 0.54 at 7.29; 0.65 at 8.36; 0.53 at 9.44; 0.67 at 10.61; 0.54 at 11.79; 0.72 at 12.99; 0.54 at 14.15; 0.67 at 15.33; 1.02 at 18.68; 0.43 at 21.15; 1.69 at 22.83. About 10.5 s of 24.5 s (43 %).

Picture / voice sync (4 fps contact sheet): buy 4.5 s (voice 4.58), purchase 5.5 (5.57), help 6.75 (6.85), assist 7.75 (7.83), tell 9.0 (9.01), inform 10.0 (9.96), need 11.25 (11.28), require 12.25 (12.33), end 13.75 (13.71), conclude 14.75 (14.68), tip 16.0 (16.0), closing card about 19.7 (19.70). In sync everywhere.

## Second-by-second notes

- 0.00-0.13: logo, pill, two grey column titles, an empty dark screen with dim words. For five frames there is no headline. Too short to swipe on, but it is the frame YouTube may show as the cover.
- 0.17-2.1: "Formal vs Informal English", big, yellow. That is what I typed. I stop.
- 2.1-4.5: "5 words you need." Short promise, I know how long this takes. 0.7 s of quiet before the first word.
- 4.5-6.8: "buy" on the left, then "purchase" in yellow on the right. I understand the game at once: left = what I say, right = the upgrade. This is the best moment of the video.
- 6.8-13.7: help - assist, tell - inform, need - require. Same rhythm, 2.2 s a pair. I know three of these. I stay because the table is filling and I want to see it complete, but nothing new happens: no sentence, no surprise. A weaker learner stays, a B2 learner may swipe around 9-11 s ("I know these").
- 13.7-15.3: "end - conclude". The voice's bare "end" is short and flat; the word is on screen, so I get it. "conclude" is the one I would write in the comments.
- 15.3-19.6: "Use formal words in work emails and essays." Good, now I know where. The whole table plus the rule is on screen for 3.6 s: this is the frame I would screenshot. On my phone the end of "conclude" and of "essays." would sit under the like and share buttons.
- 19.6-22.8: the table is gone, "Which formal word is new to you? Write it in the comments." with the subscribe button under it. I have an answer (conclude). Fine.
- 22.8-24.5: 1.7 s silent tail with the bell. A little long.

## Takeaway test

Action I can name: "In a work email or an essay write purchase, assist, inform, require, conclude instead of buy, help, tell, need, end." Concrete, usable tomorrow. Passes.

## Retention risks

- Five structurally identical beats of 2.2 s (4.5-15.3 s = 44 % of the video) with no change of pattern. The growing table carries it; a sixth pair would not survive.
- Easy pairs: the stronger half of the audience already knows three or four of the five.
- 43 % silence, in 0.5-0.7 s pieces between single words. It reads as a calm list rhythm, not dead air. The 1.7 s tail is the only real dead air.
- The table uses only y 632-1624 px; the lower 35 % of the screen is empty except for the tip. Legibility is good (row text about 100 px high). The column titles are small and grey: fine once the pill is read.
- The screenshot moment (full table + tip) lasts 3.6 s and then the table disappears for the closing card. A viewer who wants to keep the list has to be fast.
- Voice speed 1.05, fine. Text and voice in sync.

## Trust risks

- The pairs are correct and safe (the language editor's swap away from "enquire" and "commence" was right).
- "Use formal words in work emails": mild overclaim. Plenty of good work emails say "help" and "need"; "I want to inform you" in an ordinary email to a colleague is stiff. The learner corpus already has this complaint ("This sounds way too formal", "he'd sound like a knew it all"). The line is defensible for emails to a client or a boss and for essays; without a "not with friends" half some viewers will overuse the right column.
- The pairs are not drop-in swaps in every sentence ("help me with" - "assist me with", "tell me" - "inform me": fine; "tell a story", "the end" are not "inform a story", "the conclude"). No sentence on screen means nothing guards against that.
- H42 comparability: the hypothesis text holds constant "the struck-out wrong form on screen from the first frame" and "word-by-word captions". This render has neither, by design. Correct the H42 text before reading stayed %. The hypothesis also still lists the old pairs (ask - enquire, start - commence) and the old tip.

## SHIP BLOCKERS

1. **Right column and tip line run under the Shorts button column (15.3-19.7 s for "conclude" and the tip; "require" from 12.3 s is borderline).** Measured at full resolution: "conclude" right edge x 1341 px at y 1538-1624 px (60-63 % of height); "work emails and essays." right edge x 1334 px at y 1913-2001 px (75-78 %); "require" x 1290 px at y 1312-1420 px. Right margin 90-106 px of 1440. The like / dislike / comment / share stack takes roughly the right 150 design px (x above about 1240 px) from mid-screen down, so about 100 px of each of these words is under an icon in the one frame a viewer wants to screenshot. Owner: **shorts-builder** (`shorts/build_stop_saying.py`, two-column layout: move the right column centre left, or cap the right column and the tip at about x 920 design px, or lift the table so all five rows end above mid-screen and wrap the tip narrower), then re-render and re-run the subscribe step. This is an estimate from pixel coordinates: I could not see the video inside the Shorts player. One phone screenshot at about 18 s that shows "conclude" and "essays." clear of the buttons clears this blocker without a rebuild.

## Notes for the next test (not blockers)

1. **Put the hook headline in frame 0** (shorts-builder): it is missing in frames 0-4 (0.000-0.133 s). No fade-in on the first card.
2. **One sentence of use** (scenario-writer): after the table, one line that changes on screen, for example "I need help." becoming "I require assistance." That turns a word list into something I can copy. If only one thing is added, add this.
3. **Say the other half of the rule** (scenario-writer, language-editor): "Work emails and essays: right side. Friends: left side." Also consider "emails to a client" instead of all work emails.
4. **Harder pairs** (scenario-writer): keep one or two easy ones as the entry, then pairs a B2 learner does not know (get - obtain, ask for - request, show - demonstrate, enough - sufficient). The closing question then gets real answers.
5. **Clean the background behind the table** (shorts-builder): no flying words inside the table box, and do not build the background from the answer words (they float around before they are revealed; a dim yellow "conclude" hangs in the right column at 14.0 s).
6. **Keep the table to the end** (shorts-builder): put the closing question under the table instead of replacing it, so the screenshot moment lasts to the last frame; trim the silent tail from 1.7 s to about 0.8 s.
7. **Correct H42's text** (lab owner): pairs, tip and the "held constant" list do not match what was built.
8. **Listen once to "End." at 13.7 s** (language-editor): the recogniser prints "and" in the run. Measured clean, but a bare "end" at speed 1.05 is the weakest word of the ten.

## What was checked / not checked

Checked: ffmpeg probe; 4 fps contact sheet of the whole video (98 frames); full-resolution frames at 0.0, 0.033, 0.1, 0.2, 0.3, 1.5, 4.3, 5.2, 14.0, 15.2, 16.5, 18.5, 19.4, 19.6, 20.0, 21.5, 22.5, 23.5, 24.4 s; frame-by-frame pixel test of the hook headline (0-0.4 s), of the subscribe button against the tip line (19.4-19.9 s) and of the fade-out (23.8-24.4 s); bright-text bounding boxes per row at full resolution (margins); full-resolution crops of rows 4-5, of the tip with the button, and of row 1; faster-whisper small.en word timings on final.mp4 and on all 14 beat wavs; silencedetect and volumedetect on final.mp4; per-clip peak, onset and tail levels and 20 ms energy / low-band profile of the first 0.3 s; spectrograms of "Buy", "Purchase", "Tell", "End", "Conclude"; unit JSON; `kokoro_jobs.json`; `final.subscribe.json`; `content/youtube/l8-formal-informal-v1.json`; `SAFE_BOTTOM` in `shorts/build_stop_saying.py`; H42 in `/workspace/glottos-auto/out/lab/lab.json`; learner comment corpus (grep "formal").
Not checked: human listening (every audio judgement is measurement or the recogniser); the video on a real phone inside the Shorts player (blocker 1 and the button position are estimated from pixel coordinates and the usual place of the buttons, not seen); `final-nosub.mp4` (only confirmed it differs from final.mp4); no NotebookLM query used.

## After the review (autopilot 2026-10-07, lab produce H42)
Blocker 1 fixed in `shorts/build_stop_saying.py` and rendered again: both columns moved left (centres 250 / 700 design px), the tip line set smaller on two lines. Measured on the final file at 18.0 s and 19.3 s: all card text lies between x 65 and 911 and y 474 and 1481 design px (limits: 930 right, 1520 bottom). Also taken from the suggestions: the hook headline is in frame 0; the background no longer flies the formal answer words (everyday words only). Subscribe + bell again at 19.5 s; audio gate OK (24.5 s). Not done: no phone screenshot in the Shorts player, nobody listened to the clips.
