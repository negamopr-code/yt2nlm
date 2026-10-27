# Viewer-critic review: h113-very-worried-v1 (lab H113, Stop Saying "very worried": anxious / on edge / worried sick, two voices)

Reviewed 2026-10-27. File: /workspace/glottos-marketing/state/shorts/h113-very-worried-v1/final-sub.mp4 (md5 6ad33021..., 1440x2560, 30 fps, 20.00 s). Unit: shorts/units/h113-very-worried-v1.json (language approval 6f94994bdc12f1e1). Voices per kokoro_jobs.json: A = am_michael, B = af_heart, speed 1.05.
Checked: faster-whisper small.en word timings, ffmpeg silencedetect (-40 dB, 0.3 s), 1 frame per second plus 0/0.5/1.0/1.5 s and 12.0-12.3 s crops. Not checked: listening by ear, thumbnail, YouTube rendering.
Pain evidence: no NotebookLM query spent. content/problems/ does not exist, and there is no learner quote about overusing "very" on file (same gap as H102-H112). The pain below is the brief's, NOT verbatim: "I always say 'very worried'; give me better words." Solved means that tomorrow I say "I feel anxious about my exam" or "I'm worried sick" instead of "very worried".

## Verdict: PARTLY
The words and sentences are correct, natural and escalate well, and the emoji pictures match. But the two-voice hypothesis is only half met: the voices are easy to tell apart, but it is not a dialogue, three gaps of about 0.9 s plus a 2.15 s silent tail break the "no gap > 0.4 s" rule, and the subscribe time is not recorded in a meta file.

## Hypothesis check (H113)
- Clear who speaks: YES by sound. Male A and female B never overlap. But there are no on-screen speaker cues, and the roles are not a story. B says the word as a label ("Anxious."), then A says the whole example with the word already in it. Nobody says "very worried" and gets corrected, so the "plain line -> better answer" swap the lane promises never happens. It sounds like two narrators taking turns.
- No silent gap > 0.4 s: FAIL. silencedetect gaps: 1.49-1.85 (0.36 ok), 4.11-4.47 (0.36 ok), 6.99-7.91 (0.92), 8.51-8.89 (0.37 ok), 10.80-11.71 (0.91), 12.45-12.81 (0.35 ok), 14.69-15.60 (0.90), 17.86-20.02 (2.15 tail).
- 13-20 s: technically PASS (20.00 s), but only because of the 2.15 s silent tail. Speech ends at 17.86 s.

## Ship blockers
1. Silent gaps 0.92 s at 6.99 s, 0.91 s at 10.80 s, 0.90 s at 14.69 s and a 2.15 s tail at 17.86 s. This breaks the lab's own pass rule. Owner: shorts-builder (cut the between-beat pad to <=0.3 s and the end tail to <=0.5 s; the result is about 15.5 s).
2. Subscribe+bell: the animation IS in the video. At 12.0 s it starts (bottom-left, slides in from 12.1 s, "SUBSCRIBE" is readable at 12.3 s, then "SUBSCRIBED ✓" + bell, gone at about 17 s), and final-sub.subscribe.json says [12.0]. BUT there is no content/youtube/h113-very-worried-v1.json with "subscribe_at": [12.0] (h110 and h112 have one), so the video is not finished under the 2026-10-05 rule. Owner: shorts-builder.
- No spelled-out word: "anxious" 3.22, "on edge" 7.68, "worried sick" 11.60 are all heard as whole words.
- POLICY: none. Exam, sleeplessness, emoji only, safe for 13+.
- No magnifying glass, no NotebookLM/Gemini watermark. The logo is the channel avatar (top-left).

## Pain -> gives -> gap
- Gives: anxious (My exam is tomorrow. I feel anxious.), on edge (I can't sit still. I'm on edge.), worried sick (I can't sleep. I'm worried sick.). These are correct, natural and ordered from weak to strong.
- Gap 1: the strength order (anxious < on edge < worried sick) is never said or shown. "1/3, 2/3, 3/3" is not a scale.
- Gap 2: the context sentence ("My exam is tomorrow.", "I can't sit still.", "I can't sleep.") is heard but NEVER on screen. Only the short sub line is shown, so a B1 viewer reading with the sound off loses the reason for each word.
- Gap 3: there is no self-test moment. The end question "Which word will you use?" is a comment prompt, not a test.

## Second by second (heard / seen)
- 0.00-1.46 A: "Stop saying very worried." The frame at 0.0 is "Stop saying" only; the "very worried" title is on at 0.5 and the strike-through at about 1.0. It is my problem and it is clear.
- 1.85-3.2 B: "Here are three better words." Filler, but the voice change makes it feel like a reply. It is OK.
- 3.22 B: "Anxious." / 3.9-6.9 A: "My exam is tomorrow. I feel anxious." The emoji card (anxious face + paper/pencil) lands about 4.5 s and matches the exam.
- 6.99-7.91 0.92 s silence (swipe point 1).
- 7.68 B: "On edge." / 8.4-10.8 A: "I can't sit still. I'm on edge." Grimace + alarm clock. Fine, though the alarm clock reads more as "late" than "restless".
- 10.80-11.71 0.91 s silence (swipe point 2). At 11.3 s the screen is the headline only with no picture.
- 11.60 B: "Worried sick." / 12.4-14.7 A: "I can't sleep. I'm worried sick." Worried face + moon matches "can't sleep". The subscribe pill appears at 12.1-12.3 s, during this beat, bottom-left, and does not cover the card.
- 14.69-15.60 0.90 s silence (swipe point 3).
- 15.34-17.60 A: "Which word will you use? Comment yours!"
- 17.86-20.00 2.15 s of silence on the end card (the main risk to the loop/retention).
- The background word-wall (anxious / on edge / worried sick, overlapping and partly bold) is clutter behind the headline, and at 0-1.5 s it competes with "Stop saying". It is readable, but it is noisy.

## Takeaway test
Tomorrow I can say "I'm worried sick" or "I feel anxious about my exam". That is a real action. There is no self-test, and I am not told which word is the strongest, so the verdict stays at PARTLY.

## Retention risks
- Silence: about 4.9 s of 20 s are gaps > 0.4 s (0.92+0.91+0.90+2.15). The content fits in about 15.5 s.
- Pacing at 1.05 is good. The voice turn-taking adds life compared with H112.
- Legibility: the headlines and sub lines are large and fine. The context sentence is missing from the screen.

## Trust risks
- The English is correct and natural (the language-editor already replaced "relieved"). "Anxious" is milder than "very worried", so "better word" is slightly overclaimed without a strength note.
- The lane text promises "B answers with the better word", but the build has B announcing and A using. This is a hypothesis mismatch, not a viewer trust issue.

## Top 3 fixes (by impact)
1. shorts-builder: cut the three ~0.9 s gaps to <=0.3 s and the 2.15 s tail to <=0.5 s, and write content/youtube/h113-very-worried-v1.json with "subscribe_at": [12.0] (or the new time after the cut, still in the second half).
2. scenario-writer: make it a real dialogue. A: "I'm very worried about my exam." B: "You mean you're anxious." A: "I can't sit still." B: "You're on edge." ... In the last beat B gives the strongest word and says "strongest". This tests the H113 hypothesis properly and gives the scale.
3. shorts-builder/visuals: show the context sentence on the card (the "use" line), add a small A/B speaker cue (e.g. a coloured name tag or a side for each voice), and add a 1-second "which one? ___" self-test before the end.
