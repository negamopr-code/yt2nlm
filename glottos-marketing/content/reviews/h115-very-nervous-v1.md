# Viewer-critic review: h115-very-nervous-v1 (lab H115, Stop Saying "very nervous")

## Re-check v2 (2026-10-27, after re-render)
File: /workspace/glottos-marketing/state/shorts/h115-very-nervous-v1/final-sub.mp4 (md5 82340ca7..., 10:38 UTC, 1440x2560, 30 fps, 18.70 s). Checked: 8 frames 6.8-11.5 s + full-res 8.5 s crop, pic-03.png itself, faster-whisper small.en transcript of the new file, content/youtube/h115-very-nervous-v1.json, final-sub.subscribe.json. Not re-checked: frames 0-6.8 and 11.5-18.7 (assumed unchanged; transcript identical to v1), listening by ear.

### Verdict: SOLVES
Both ship blockers are fixed; the story (anxious -> jittery -> on edge, Mia before her interview) gives a B1 viewer two phrases to use tomorrow ("I feel anxious about my interview", "I'm on edge"), and nothing left is a blocker.

- Blocker 1 (Jittery picture), RESOLVED: pic-03 (on screen 7.6-10.4 s) has no smeared inpaint bands; it is a clean watercolor hand with shake strokes, matching "her hands start to shake". Remaining weaknesses (non-blocking, owner visuals): the picture is a thin 720x230 strip (about 3:1), upscaled and soft, and much smaller than the Anxious/On edge pictures; a drawn "open hands" emoji at the right reads as waving/clapping, not shaking; a small white paper blob in the middle. Next time: a full-height picture of Mia holding a shaking paper/cup.
- Blocker 2 (subscribe time), RESOLVED: content/youtube/h115-very-nervous-v1.json has "subscribe_at": [11.3], same as final-sub.subscribe.json (5.0 s, corner bl); pill + bell visible at 11.5 s, second half of the Short.
- Transcript v2: identical to v1; "Anxious" 2.24, "Jittery" 6.98, "On edge" 10.52 are whole words, no spelled-out word. POLICY: none.
- Still open (non-blocking, from v1, owner shorts-builder unless noted): frame 0-0.1 s shows the question without the yellow "very nervous"; 2.15 s silent end card (16.55-18.70) + three ~0.56 s holds keep it at 18.7 s, above the 13-18 s H102 band; context sentences are only spoken (scenario-writer); no self-test at the end (scenario-writer).

---
## Review v1 (superseded)

Reviewed 2026-10-27. File: /workspace/glottos-marketing/state/shorts/h115-very-nervous-v1/final-sub.mp4 (md5 6486009f..., 1440x2560, 30 fps, 18.70 s, kokoro am_michael 1.15, no music). Unit: shorts/units/h115-very-nervous-v1.json (language approval aba1130b686dba1e). Subscribe: final-sub.subscribe.json = [11.3], corner bl.
Checked: faster-whisper small.en with word timings, ffmpeg silencedetect (-40 dB, 0.3 s), 37 frames (0.0/0.1/0.3/0.5/1.0/1.5/2.0/2.1/2.25/2.4/2.5/3.0/3.5/4.0/4.7/5.0/6.5/6.8/7.0/7.3/7.6/8.5/9.8/10.4/10.6/10.8/11.2/11.5/12.5/13.5/14.8/16.0/17.0/17.5/18.3/18.65) plus full-res frame 5.5 s and a full-res crop of the Jittery picture at 8.5 s. Not checked: listening by ear, thumbnail, YouTube rendering.
Pain evidence: no NotebookLM query spent. content/problems/ does not exist, and there is still no verbatim learner quote about overusing "very" on file (same gap as H102-H114). The only on-file evidence is demand, not a quote (content/insights/audience-needs.md: "Stop Saying Very X" Shorts lead the channel). Pain (the brief's, NOT verbatim): "When I'm stressed I only know 'very nervous'." Solved = tomorrow I say "I feel anxious about the interview" / "I'm on edge", and I know "jittery" is the shaky, body feeling.

## Verdict: PARTLY
The question hook works (topic heard at 1.2-1.8 s, first better word on screen at 2.1 s) and the Mia story escalates cleanly, but the Jittery picture is visibly damaged (two smeared inpaint blocks across the hand, not "faint"), the subscribe time is not in a youtube meta, and 2.15 s of silent end card plus three 0.56 s holds push it to 18.7 s.

## Ship blockers
1. VISUALS: Jittery picture (pic-03, on screen 7.6-10.4 s). At phone size the two grey smeared bands across the hand and a grey blob top-right read as a broken/censored image, not as a "faint" band. The picture is also a tight crop of one hand with motion strokes; without the sound a viewer cannot tell it is "shaking hands". Owner: visuals (regenerate or re-inpaint; show Mia's whole upper body with shaking hands holding a paper/phone).
2. SUBSCRIBE TIME NOT RECORDED. The animation is there (pill + bell 11.3-~16 s, bottom-left, in the second half: OK), but there is no content/youtube/h115-very-nervous-v1.json, so "subscribe_at": [11.3] is not on the :8093 card. Not finished per the 2026-10-05 rule. Owner: shorts-builder.
- No spelled-out word: "Anxious" 2.24, "Jittery" 6.98, "On edge" 10.52 are whole words.
- POLICY: none. Job interview, hands, heartbeat; nothing sexual, no real people, safe for 13+.
- No magnifying glass. No NotebookLM/Gemini watermark seen. Logo = channel avatar (top-left).

## H115 hypothesis check
- Spoken question at 0.0 s: YES. "What do you say instead of very nervous?" 0.00-1.84.
- On screen at frame 0: HALF. At 0.0 and 0.1 s the card shows only "What do you say instead of" - the yellow "very nervous"? line is missing; it pops in by 0.3 s. Frame 0 (and any auto-picked frame) has no topic. Fix: render the full question on frame 0.
- First better word on screen by ~2 s: YES, "Anxious" headline at 2.1 s (spoken 2.24). Curiosity gap = 2.1 s, inside the 3-second rule.
- "3 better words" sub (unit hook card) never appears on screen in any sampled frame 0-2.0 s. Minor, but the promise of a count is lost.
- Held constant vs H102: length 18.7 s is above the 13-18 s band, mainly the silent tail. That confounds the stayed % comparison a little.

## Pain -> gives -> gap
- Gives: anxious (Mia is waiting for her job interview. She feels anxious.), jittery (Her hands start to shake.), on edge (Her heart is pounding.). One person, one situation, rising tension: this is the best "story" in the very-X lane so far, and the sentences are natural.
- Gap 1: the context sentences ("Mia is waiting for her job interview", "Her hands start to shake", "Her heart is pounding") are only spoken, never on screen. The screen shows "She feels X." from the start of each beat. A B1 viewer with sound off, or who misses "pounding", gets only "She feels X" three times.
- Gap 2: nuance is implied, never said. "Jittery" is the body (shaky, often from coffee); "on edge" is tense, waiting for something bad. The story carries this implicitly, which is acceptable.
- Gap 3: no self-test. The end asks "Which word will you use? Comment yours!" - a soft prompt, not a test.

## Second by second (heard / seen)
- 0.00-1.84 "What do you say instead of very nervous?" Frame 0.0-0.1: "What do you say instead of" only. 0.3 s: + yellow "very nervous"?. It is MY question, I stop - once the yellow line is there.
- 1.84-2.24 short gap, card switches to "1/3 Anxious" at 2.1 s. Good.
- 2.24 "Anxious" / 3.02-4.74 "Mia is waiting for her job interview." Screen from 3.0: "She feels anxious." + picture of a worried woman on a waiting-room chair (matches). The screen line is ahead of the voice.
- 4.86-5.21 0.35 s gap / 5.26-6.08 "She feels anxious."
- 6.22-6.78 0.56 s silent.
- 6.98 "Jittery" / 7.50-8.68 "her hands start to shake." 6.8-7.3: headline only, no picture, no sentence. Picture at ~7.6: damaged hand crop (blocker 1). Swipe risk here: the image looks broken.
- 9.06-10.10 "She feels jittery." / 9.94-10.51 0.57 s silent.
- 10.52 "On edge" / 11.42-12.30 "her heart is pounding." 10.6-11.2: headline only. Picture ~11.3 (woman bent forward, red heart with pulse line - matches well). Subscribe pill appears the same moment, bottom-left, over the bottom of the picture; it then clicks to SUBSCRIBED + bell. It covers Mia's feet, acceptable.
- 12.76-13.62 "She feels on edge." / 13.78-14.35 0.57 s silent.
- 14.38-16.22 "Which word will you use? Comment yours."
- 16.55-18.70 2.15 s silent end card (swipe point). At ~18.3 the loop frame shows the hook with "very nervous" struck in red: the loop works, but the strike only appears at the very end, never at the start.

## Takeaway test
I can say "I feel anxious about my interview" and "I'm on edge" tomorrow. That is a real action. Jittery I would understand from the story, but if I learn from the screen only, I get "She feels jittery" with a broken picture.

## Retention risks
- Silence: 0.35 + 0.56 + 0.57 + 0.57 + 2.15 = 4.2 s of 18.7 s. Content fits in about 14.5 s; cutting the tail to 0.5 s and the holds to 0.3 s gives ~15.5 s, inside the H102 band.
- Each beat opens on a bare headline for 0.5-0.8 s before the picture arrives (6.8-7.5, 10.5-11.3).
- Voice at 1.15 is clear and quick, no podcast drag. Text sizes are fine on a phone; the background word wall (anxious/jittery/on edge + faint logo tiles) is busy behind the headlines.

## Trust risks
- The damaged Jittery picture is the one real trust hit.
- Faint blur strip also on the Anxious picture at the right edge by the door (inpainted text); visible at full res, minor on a phone.
- English: all lines natural and correct. "Anxious" for "very nervous" is fair; "on edge" fits (Cambridge: nervous and unable to relax).

## Top 3 fixes (by impact)
1. visuals: redo pic-03 (Jittery) with no inpaint bands, a readable scene (Mia, shaking hands, paper/coffee cup), and clean the right-edge strip on pic-02.
2. shorts-builder: write content/youtube/h115-very-nervous-v1.json with "subscribe_at": [11.3]; put the full question (incl. "very nervous") and "3 better words" on frame 0; cut the end tail to ~0.5 s and the holds to ~0.3 s; show the picture on the same frame as the headline.
3. scenario-writer (then language-editor gate): put the context sentence on screen while it is spoken ("Her hands start to shake." above "She feels jittery."), and end with a 1-second self-test instead of "Comment yours" only, e.g. "Before an exam, your hands shake. You feel ___?"
