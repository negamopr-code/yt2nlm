# M1 critic review, m1-v3.mp4 (P01, 16:9 NotebookLM whiteboard, 5:32)

Reviewer: glottos viewer-critic (headless autopilot step "special M1: critic", round after polish round 1), 2026-09-28.
Watched as: a B1 to B2 learner who forgets new words within days.
Input: `content/specials/M1/m1-v3.mp4` (1280x720, 24 fps, 332.21 s, AAC mono).
Method:
- Frames: contact sheets every 4 s (84 frames), the bottom-right corner cropped every 2 s (166 crops), full-resolution frames at 0.7, 6.5, 7.5, 6 to 14 s (every 1 s), 190 (banner), 225 (chart), 270 (routine), 286 to 317 s (quiz, every 1 s), 295.0/295.4/295.7 and 304.6 to 305.5 (answer reveals), 309 (happy), 313 (important), 331.0/331.9/332.15 (end).
- Sound: faster-whisper small.en (int8, cpu_threads=4, word timings, download_root state/whisper-models) on the whole file. ffmpeg silencedetect (-40 dB, 0.4 s). Sample-level check (level and max sample step in a ±50 ms window) at every cut and freeze seam listed in polish-v2.md.
- Read first: critic-v1.md, polish-v2.md, polish-v3.md, lang-gate-v2.md, lang-gate-v3.md, script.md, focus.txt, meta.json, decision.md, `/workspace/state/glottos-methods/P01/strategy.md`.
- Nothing was rendered, edited, uploaded or sent to NotebookLM.

## Verdict: SOLVES

The v1 ship-blockers are all fixed and I found no new ones. The video now does the job for the learner: it names the pain in the first four seconds, gives one method to lead with (use the word: one sentence about your own life, said out loud), then a when-to-use rule, a day 1/3/7 schedule and a 15-minute routine I can start tomorrow. It ends with a real self-test: questions only, about 3 s of silence, then the answer. What remains is polish (pacing, a slow hook picture, near-answers on one quiz slide). None of it stops the video from shipping.

**SHIP-BLOCKING defects remaining: NO.**

## Pain in the learner's words

Verbatim learner comments from the P01 research data (from critic-v1.md and the script's quote audit), with no names:
- "I've been trying to cram too many words and always forget them."
- "I also find myself forgetting certain English words when I'm speaking."
- "I forget every new word so of this works for me it will be life changing"
- "when I reviewed the Japanese words that I learnt several days before, I almost forgot 50% of them"
- "I reviewed but kept forgetting the words. I have more results creating sentences in my notebook"
- "I always forgetting my words when I deliver a speech in english"

In one sentence: "I learn a word, it's gone in a few days, and when I speak my mind goes blank." Solved means that tomorrow I learn only 3 words, write my own sentence for each and say it out loud, cover and recall them on day 3, use them in new sentences on day 7, and can find them when I speak.

## Pain → what the video gives (v3, heard) → gap

| Pain | What the video gives | Gap |
|---|---|---|
| Gone by Friday | 0:00 "you learn a new word on Monday ... by Friday, it's just gone" | The matching picture only arrives at 0:07 (see the notes) |
| I cram too many | 2:10 "A maximum of three new words a day is plenty" plus the clipboard "Maximum 3 new words a day" | none |
| Blank mind when speaking | 1:34 to 1:49 recognition vs finding the word, "your mind goes completely blank as soon as you speak"; 1:57 one sentence about your own life, out loud | none. It leads with the method that has the most proof (use it: 440 proof in strategy.md) |
| Isolated word lists | 2:14 to 3:00 "Never learn a word alone", the livid flight sentence, four hooks, Quote 3 | none |
| Freezing on register | 3:01 to 3:24 swamped/livid when to use it, a table plus the "STEP 2: LEARN WHEN TO USE IT" banner | none. The numbering now matches the voice |
| Reviewing doesn't work | 3:25 to 4:21 re-reading trains recognition, cover and recall, about 61% vs about 40% of a text a week later, day 1/3/7 | none. The chart title says "One week later: % of a text remembered" |
| What do I do daily | 4:22 to 4:48 Anchor 0-5 / Review 5-10 / Speak 10-15, voice and card | The sentence that named it "a 15-minute routine" was cut. The card carries it, but the voice jumps straight in |
| Proof that it works for me | 4:49 to 5:15 5-word test with pauses of about 2.6 to 3.0 s; 5:16 comment your score | Works. A small issue on the "very important" slide (see fix 2) |

## Check of every v1 ship-blocker in v3

| v1 defect | v3 status | Evidence |
|---|---|---|
| Quiz answers visible during the questions ("Livid" scroll, 2x "EXHAUSTED") | FIXED | Scroll is blank at 295.0 and 295.4. "Livid." appears at 295.7 (voice "livid" 295.54, silence ends 295.62). "EXHAUSTED" is blank at 304.6 to 305.2 and appears at 305.4 (voice 305.44). Both reveals line up with the voice. |
| 0.5 to 1.0 s question→answer gap | FIXED | Silences: angry 292.62–295.62 (3.0 s), busy 297.54–300.33 (2.8 s), tired 302.73–305.44 (2.7 s), happy 307.81–310.51 (2.7 s), important 312.64–315.20 (2.6 s). |
| "very dizzy" heard in the quiz | FIXED | small.en now hears "very busy" (≈297.1). Not checked by a human ear (statement intonation). |
| Two "STEP 3"s | FIXED | The banner reads "STEP 2: LEARN WHEN TO USE IT" (checked at 190 s). Voice: "Step one" 80.5, "step two" 134.1, "Step three" 205.3. Stray "Step 1/2/3" labels are gone from the quiz slides (not visible in any quiz frame from 286 to 317 s). |
| "Gemini Notebook" watermark on every frame | FIXED | Channel logo tile is bottom-right in all 166 corner crops (every 2 s, 0 to 330 s). No watermark text anywhere, including dark-art slides (313 s) and faded-white slides. |
| Full-screen Gemini end card | FIXED | 331.0 CTA → 331.9 fading → 332.15 near black, with the channel logo. No Gemini card. |
| NotebookLM filler ("reassure yourself", "brilliantly", "incredibly effective", "highly effective") | FIXED | None of these lines is in the v3 transcript. |
| Raw markdown caption / "Speakting" / garbled art | FIXED | Chart at 225 s: clean title, no asterisks. No "Speakting". Quote 2 ribbon gibberish and "Cognizaant" removed (lang-gate-v3). |
| Quote cards had no attribution; Q3 card ungrammatical | FIXED | "A learner wrote:" on Q1 (≈10 to 13 s), Q2, Q3. Q3 card reads "'Repeat the sentence I made myself over and over' was a game changer for me." |

## New-defect hunt (introduced by polish)

- Logo patch: present on every sampled frame, same place and size, no flicker between samples. On the gear slide (313 s) the delogo smear is not noticeable at 1x. OK.
- Cut seams (6.79, 13.50, 93.71, 115.29, 262.29) and freeze seams (293.17 to 314.96): every one sits in audio at −63 to −81 dB, max sample step ≤0.0008 (the file's median step is 0.0014). No click, no clipped word. The transcript flows naturally across each join. OK.
- "very busy" splice (≈297.06): inside speech, no step artefact beyond normal speech. Whisper reads it cleanly. The intonation is unchecked.
- Answer reveal timing: see above. No early reveals.
- Step numbers on screen vs voice: consistent.
- On-screen text read at full resolution: title card, Monday/Friday slide, Q1 card, challenge table (Livid / Swamped / Exhausted / Thrilled / Crucial), DAX/CONNECTION, brain/label/noise, "Use the word. Say it, and write it.", recognition/finding, Q2 card, "What You Should Do", "Never learn a word alone...", Livid/flight, Q3 card, STEP 2 table, Timing/pushing, chart, Day 1/3/7, routine card, 5 quiz slides, score CTA, anotherwordfor.net CTA. All correct English. No new misspellings.
- False claims: none. No "4x stronger connections", no "70% gone by day 3", no percentages on the forgetting curve. The only numbers are about 61% vs about 40% "of it" (a short text), a week later, same time. Forbidden words: none (no podcast, episode, show, welcome, today we, dive, naked, literally, proven, science). "explainer" is used once (0:20), which is acceptable.
- Mild intensifiers left (known, accepted in v1): "the method people most often say works **best** for them" (1:26) and "works **significantly** better" (3:33). Not blocking.

## Second by second: where I would swipe away

- 0:00 to 0:07: **Weakest picture moment.** The voice hits my pain right away ("Monday ... by Friday, it's just gone"), but the screen shows a generic "Remembering New Words" title card until about 0:06.8. The Monday/Friday slide arrives while the voice has already moved on to "Your memory is not broken". In a 16:9 feed or browse view the thumbnail and title carry the click, so this is a retention leak, not a blocker.
- 0:08 to 0:13: "The method is." then Quote 1 follows after only about 0.75 s, and the voice does not say "A learner wrote". The on-screen tag carries the attribution. Fine.
- 0:15 to 0:36: The challenge list, readable, with a promise ("we will test you"). This is a good reason to stay.
- 0:36 to 1:20: **Highest drop risk.** About 25 s on the DAX/CONNECTION slide, then about 20 s on the brain/bin slide. The theory is the least actionable part, and no forgetting curve is drawn.
- 1:20 to 2:14: Step one. The strongest part. The clipboard "What You Should Do" (1:55 to 2:14) is the screenshot moment.
- 2:14 to 3:24: Step two. The pace is fine. The table is readable.
- 3:25 to 4:21: Step three. The chart sits in the left half of a mostly white frame (small, but readable at 720p). The Day 1/3/7 slide is plain white with small text, and it holds for about 25 s. It is readable, but it looks thin.
- 4:22 to 4:48: The routine. It starts abruptly ("For the first five minutes, your anchor phase") with no "here's your 15-minute routine" lead-in. The card makes it clear.
- 4:49 to 5:15: The test. It works. I get time to think, and there are no early answers. On the "very important" slide, "vital", "pivotal" and "essential" are drawn around the question. They are real synonyms, so I might answer "vital" and then feel marked wrong when the answer is "crucial".
- 5:16 to 5:32: The CTA. It is clear and ends clean.

## Takeaway test

Tomorrow I can: take 3 new words, write one sentence about my own life for each and say it out loud (0-5 min), then read my day-1 words in their sentences and cover and recall my day-3 words (5-10 min), then say my day-7 words in two new sentences each (10-15 min). No app. **PASS**: this is one concrete, nameable action.

## Retention risks

- Length 5:32 is fine for the content. The main dead zones are 0:36 to 1:20 (two static slides, theory) and the plain white Day 1/3/7 hold.
- The hook picture lags the voice by about 7 s.
- The 0.9x NotebookLM voice is slightly slow, but it is clear for B1.
- Text legibility: fine at 720p everywhere except the small Day 1/3/7 sub-lines and the chart axis labels (readable, small).

## Trust risks

- Low. The numbers are sourced and correctly framed. There are no names and no Gemini branding. The quotes are verbatim and tagged.
- "works best" and "significantly better" are mild overstatements. They are acceptable.
- Near-answers (vital/pivotal/essential) on the quiz slide could make a viewer argue "vital is also right" in the comments. That is arguably good engagement, but the test looks sloppy.

## Top 3 fixes (NONE ship-blocking), ordered by impact

1. **Hook picture sync (shorts-builder).** Bring the Monday/Friday girl slide in at 0:00 instead of about 0:06.8 (drop or shorten the "Remembering New Words" title card), so the first frame shows my pain while I hear it. This also matters for the auto-thumbnail and the preview.
2. **Quiz slide "very important" (visuals, then shorts-builder).** Inpaint "vital", "vital", "pivotal" and "essential" (313 s, left swirl) during the question and pause, like "Livid" and "Exhausted", or reveal them only after "crucial" as bonus synonyms (which fits the Another Word For brand).
3. **Pacing in beat 2 and the routine lead-in (shorts-builder, language-editor recheck).** Trim or add motion to the 0:36 to 1:20 static holds (e.g. a simple drop-then-flatten curve overlay, no numbers, as the script asked). Consider adding a short on-screen title "Your 15-minute routine" at 4:22 to replace the cut spoken lead-in.

## Not checked

- No human listening. The "very busy" swap intonation and the general voice quality are checked by whisper only.
- Frames were sampled (every 4 s overall, every 1 to 2 s in the hook, corner and quiz), not every frame.
- meta.json was not re-audited (gated 2026-09-27T22:33Z). Its description still promises "3 easy steps" and the "5-word challenge", and both match v3.
- NotebookLM was not queried. The pain evidence came from local files.
