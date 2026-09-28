# M1 critic review, m1-v1.mp4 (P01, 16:9 NotebookLM whiteboard, 5:48)

Reviewer: glottos viewer-critic (headless autopilot step "special M1: critic"), 2026-09-27.
Watched as: a B1 to B2 learner who forgets new words within days.
Method: 70 frames (one every 5 s) plus 19 scene-change points, full-resolution checks at 0.7 s, 1.5 s, 199 s, 250 s, 262 s, 312 to 345 s. Audio transcribed with faster-whisper small.en (int8, cpu_threads=4, word timings). Silence map from ffmpeg silencedetect. NotebookLM was not touched, and nothing was rendered, uploaded or changed.

## Verdict: PARTLY

The spoken content does what it should. It follows the approved script closely, leads with the best-confirmed method (use it: say it and write it) and ends on a 15-minute routine I could start tomorrow. But it cannot ship as it is. The self-test at the end is broken: the answers are on screen during the questions, and there are only 0.5 to 1.0 s between each question and its answer. The on-screen step numbers contradict the voice ("STEP 3" appears twice). NotebookLM also added some unsourced praise lines, the timing beat has garbled whiteboard text, and a "Gemini Notebook" watermark is on every frame, plus a full-screen Gemini end card. That breaks the brand rule. All of this can be fixed in post. No regeneration is needed.

## Pain in the learner's words

Verbatim learner comments from the P01 research data, with no names:
- "I've been trying to cram too many words and always forget them." (the video's Quote 1)
- "I also find myself forgetting certain English words when I'm speaking."
- "I forget every new word so of this works for me it will be life changing"
- "when I reviewed the Japanese words that I learnt several days before, I almost forgot 50% of them"
- "I reviewed but kept forgetting the words. I have more results creating sentences in my notebook"
- "I always forgetting my words when I deliver a speech in english"
- "I've been memorizing word by word every single page and never understood a thing ... and I still forget."

In one sentence: "I learn a word, it's gone in a few days, and when I speak my mind goes blank." Solved means that tomorrow I learn only 3 words, write my own sentence for each and say it out loud, cover and recall them on days 1, 3 and 7, and can actually produce them when I speak.

## What the video gives, and the gap

| Pain | What the video gives (heard) | Gap |
|---|---|---|
| Words disappear by Friday | 0:00 "you learn a new word on Monday ... by Friday, it's just gone". An exact mirror of the pain. | none |
| I cram too many | 2:26 "A maximum of three new words a day is plenty" | none (the script said "three", the video says "maximum". Fine.) |
| Blank mind when speaking | 1:47 to 2:02 recognition vs finding the word, plus one sentence about your life, out loud | none. This is the lead method, as the strategy says (use it: 440 proof in strategy.md, 742 in the refreshed proof_doc.md, rank #1 in both) |
| Isolated word lists | 2:31 to 3:18 "livid" inside the flight sentence, four hooks, own-sentence quote | none |
| Wrong register makes me freeze | 3:19 to 3:41 swamped and livid, when to use them and when not | The on-screen banner calls this "STEP 3". See the fixes. |
| Reviewing doesn't work | 3:42 to 4:39 cover and recall, 61% vs 40% of a text, days 1, 3 and 7 | The chart has no "one week later" or "of a text" label, and the caption shows raw markdown |
| What do I do daily | 4:39 to 5:10 the 15-minute routine (anchor, review, speak), shown on a card | none. This is the takeaway. |
| Proof that it works for me | 5:11 to 5:28 5-word test | **Broken.** Answers are visible and there is no time to think. |

Note: proof_doc.md was refreshed at 22:45Z, after the script was written. "Active recall / self-testing" is now #2 (412 proof), ahead of words in context (337). The video still covers recall as Step 3, so no content change is needed. For M2+, consider giving recall more weight.

## Second by second: where a viewer would swipe away

- 0:00 to 0:06: Strong. The pain is stated in the first sentence. The picture (girl with a "Vocabulary Fundamentals" book, word blowing away) matches the words. 0:00 to ~0:02 is a generic "Remembering New Words" title card. Acceptable for 16:9.
- 0:07 to 0:12: "This frustrating cycle happens to almost everyone. But I want you to reassure yourself right now." This is NotebookLM filler, not in the script. "Reassure yourself right now" is unnatural English. It is the first soft spot.
- 0:15 to 0:23: Quote 1 is read with no "A learner wrote", so for a second the narrator seems to be confessing. Then comes the added line "That exact quote perfectly captures the frustration we all feel with traditional cramming." That is filler.
- 0:24 to 0:47: The challenge list is shown as a clear two-column table (meaning / word). The words can be read at 1280x720. Good.
- 0:47 to 1:30: **Highest swipe risk.** About 40 s on only two static slides (the DAX/CONNECTION pair for ~35 s, then the brain and bin slide). The drop-then-slow forgetting curve from the script is never drawn, so "memory drops fast, then slows" has no picture.
- 1:30 to 1:45: "Use the word. Say it, and write it." The text is partly covered by the microphone drawing ("Use|the"). The paper in the drawing has fake handwriting ("Create ... Produce ... certzgation").
- 1:44 to 1:47: "And this brilliantly illustrates why it works." Filler, not in the script, and it points at nothing.
- 1:47 to 2:03: One static slide (recognition / finding) for about 18 s. The content is clear, the pacing is slow.
- 2:08 to 2:12: "That physical power of writing it down is incredibly effective." An unsourced overclaim added by NotebookLM.
- 2:12 to 2:30: The "What You Should Do" clipboard (one sentence about your life, say it out loud, max 3 words a day). **The best frame in the video.** It stays up about 20 s, which is good for a screenshot.
- 2:31: Whisper hears "Now it's moved to step two." That is ungrammatical if accurate (probably "Now let's move to step two"). Needs an ear check.
- 3:03 to 3:07: The Quote 3 card drops "I must say that" and the inner quotation marks: "Repeat the sentence I made myself over and over was a game changer." The voice reads the full quote correctly. The card is a truncation, which is acceptable, but it is not verbatim.
- ~3:19 to 3:41: The banner "**STEP 3: LEARN WHEN TO USE IT**" appears while the voice is still in step two. At 3:42 the voice says "Step three is all about timing and recall." There are now two step 3s, which confuses the "3 easy steps" promise in the title.
- 3:55 to 4:10: Bar chart, 40 vs 61, y-axis "Memory Retained (%)", bars "Re-read text" and "Cover and recall". Caption in tiny type: `*Active* recall makes your memory **stronger**.` These are raw markdown asterisks. Faded leftover art behind the chart ("blossom", "Garden", "perfume", "memory album", "Comprehension", "network of associations", "**Speakting** in sentence", misspelled).
- 4:15 to 4:39: Day 1 / 3 / 7 timeline. The text is correct and readable. It has the same faded leftover art with "Speakting".
- 4:39 to 4:43: "a **highly effective** 15-minute daily routine". The routine is our own synthesis and was never tested. A mild overclaim.
- 4:40 to 5:10: Routine card (Anchor 0-5, Review 5-10, Speak 10-15). Correct and readable. The background notebook shows random words ("VIGILANT", "EFFERVESCENT", "serendipity") that are not in the lesson. Harmless but noisy.
- 5:11 to 5:28: **Quiz fails as a test.** Gap between each question and its answer: angry 1.03 s, busy 0.51 s, tired 0.72 s, happy 0.71 s, important 0.58 s (script: 2 s silent pause). Answers leak on screen: at 5:13 to 5:17 a scroll says "Livid" under "What is the word for very angry?". At 5:20 to 5:23 "EXHAUSTED" appears twice under "very tired?". "Very important?" shows vital/pivotal/essential (not the answer, but it invites a different answer). Whisper hears "very dizzy" at 5:17.4 (probably a mumbled "busy"). Needs an ear check.
- 5:28 to 5:44: CTA ("write your score + one sentence", "look up another word for happy on anotherwordfor.net"). On screen: "Look up another word for happy on anotherwordfor.net" with a globe icon over "for". Readable. No search box is drawn. Good.
- 5:44 to 5:48: **Full-screen "Gemini Notebook" end card.** Brand violation.
- Every frame: "Gemini Notebook" watermark in the bottom-right corner (about 120x16 px at 1280x720). Brand violation.

## Takeaway test

Tomorrow I can: learn 3 new words, write one sentence about my own life for each and say it out loud, then cover and recall them on day 3 and use them in two new sentences on day 7, in 15 minutes a day. That is a clear, nameable action, so the content passes this test. The PARTLY verdict comes from the broken self-test and the ship-blocking defects, not from missing substance.

## Script adherence and claims (task item 2)

The voice follows all 7 beats in order and keeps close to the script. No researcher, university, year, app or channel is named. No "4x stronger connections", no "70% gone by day 3", no percentages on the forgetting curve. The only figures are about 61% vs about 40% of a text, a week later, same time, which matches the P01 editor's note. Ebbinghaus is described only as "first measured using completely meaningless syllables", with no name, as allowed. None of the forbidden words appear (podcast, episode, show, welcome, today we, let's dive in, naked, literally), and there is no sign-off.

Lines NotebookLM added, with cut points (silence-bounded where possible):

| Time | Line (heard) | Problem | Clean cut? |
|---|---|---|---|
| 0:07.1 to 0:12.1 | "This frustrating cycle happens to almost everyone. But I want you to reassure yourself right now." | unsourced generalisation plus unnatural English | Yes. Cut ~6.9 to 12.3. "Your memory is not broken" still follows naturally. |
| 0:19.2 to 0:23.4 | "That exact quote perfectly captures the frustration we all feel with traditional cramming." | filler, "we all" | Yes. Cut ~19.0 to 23.9, but then add an on-screen "A learner wrote:" tag to the quote card. |
| 1:36.6 | "...the method people most often say works **best** for them" | script says "works for them". "Best" slightly overstates what the proof counts show. | No (mid-sentence). Low risk, keep. |
| 1:44.5 to 1:46.6 | "And this brilliantly illustrates why it works." | filler, refers to nothing | Yes. Cut ~1:44.2 to 1:47.0. |
| 2:08.8 to 2:11.9 | "That physical power of writing it down is incredibly effective." | unsourced overclaim | Yes. Cut ~2:08.5 to 2:12.3. |
| 3:50.5 | "works **significantly** better" | intensifier not in the script. The underlying result is real. | No. Keep. |
| 4:39.6 to 4:43.8 | "You can put it all together into a highly effective 15-minute daily routine." | "highly effective" is untested | Optional. The whole sentence can be cut, since the routine card shows the 0-5 / 5-10 / 10-15 minutes. Low priority. |

On-screen claims: the bar chart shows y-axis "Memory Retained (%)" with no "a week later" and no "of a text". A learner can read it as "40% of words remembered", which the ep02 rule forbids. The "Cover and recall" bar label is a simplification of the study's recall practice. It is acceptable because the voice frames it correctly.

## Learner quotes (task item 3)

All three are present in the voice, word for word (0:15.9, 2:03.7, 3:03.1), with no names spoken or shown. But none of them has "A learner wrote" (NotebookLM dropped the attribution). The quote-bubble cards are the only cue. Quote 3's card is shortened (see 3:03). Quote 2's card ends with "it..." (truncated, which is acceptable).

## On-screen English and watermark (task item 4)

- Misspelled or garbled: "Speakting in sentence" (faded art, 3:55 to 4:39). `*Active* recall makes your memory **stronger**.` (raw markdown, 3:55 to 4:10). Fake handwriting on the "Use it" slide (1:30 to 1:45). Random words in the routine notebook.
- Wrong: the "STEP 3: LEARN WHEN TO USE IT" banner (~3:19 to 3:41) contradicts the spoken step 3 (timing).
- Answer leaks in the quiz: "Livid" (5:13 to 5:17), "EXHAUSTED" twice (5:20 to 5:23).
- Watermark: "Gemini Notebook" bottom-right on every frame, plus the full-screen Gemini Notebook end card from 5:44 to 5:48. This must go before publishing.
- Everything else is correct English: title cards, the quiz table, the "What You Should Do" card, the Day 1/3/7 text, the routine card and the CTA.

## Retention risks

- Length 5:48 is inside the 5 to 7 min target, and the density is fine. But beat 2 (0:47 to 1:30) and the recognition slide (1:47 to 2:03) are long static holds, where I would most likely drop.
- NotebookLM filler ("brilliantly", "incredibly effective", "reassure yourself") adds about 15 s of empty praise that a learner hears as ad talk.
- Picture and voice are in sync everywhere except the step-3 banner.
- The payoff (the quiz) is the part that breaks, and it is exactly where comments ("my score") would come from.

## Trust risks

- The two "Step 3"s make the "3 easy steps" title look sloppy.
- Answers on screen during the test mean the test proves nothing, and viewers notice.
- The Gemini watermark tells viewers this is AI-generated from a notebook and breaks the brand rule.
- Unsourced "incredibly effective" / "highly effective" lines are small overclaims next to an otherwise careful, sourced script.

## Top 3 fixes, by impact (all can be done in post, no NotebookLM regeneration)

1. **Repair the quiz (shorts-builder, with visuals).** Insert a 2 s freeze-frame with silence at each question-answer boundary: 5:15.26 (angry), 5:18.20 (busy, inside 317.95 to 318.46), 5:21.20 (tired), 5:24.30 (happy), 5:27.00 (important). Cover the leaked answers with a paper-texture patch during the question and pause: the "Livid" scroll (lower middle, 5:13 to 5:15.8) and both "Exhausted" labels (top right and bottom centre, 5:20 to 5:21.5). Optionally reveal each answer as a text overlay only after the pause. Ear-check "very dizzy" at 5:17.4. If it really says "dizzy", the voice line needs a fix (voice) or the builder swaps in the "very busy" audio from 0:36.8.
2. **Remove every Gemini watermark (shorts-builder).** Trim the end at ~5:44.3 (the CTA audio ends at 5:43.94) to drop the end card. Cover the bottom-right corner watermark on every frame with the official channel logo `state/brand/awf-logo-channel.jpg` or a background-matched patch.
3. **Fix the step numbering, the garbled text and the filler (visuals, then shorts-builder, then language-editor recheck).** Overlay the banner at ~3:19 to 3:41 with "STEP 2: KNOW WHEN TO USE IT" (or blank out "STEP 3:"). On the 3:55 to 4:10 chart, cover the markdown caption and add "one week later, % of a text remembered". Blank out the faded "Speakting in sentence" art line (3:55 to 4:39). Cut the filler lines at 0:06.9 to 0:12.3, 0:19.0 to 0:23.9, 1:44.2 to 1:47.0 and 2:08.5 to 2:12.3 (about 15 s total). Add "A learner wrote:" tags to the three quote cards. Then the language-editor re-gates the cut video.

After fixes 1 and 2 (and ideally 3), this should reach SOLVES. Re-run the critic on the rebuilt file.

## Not checked

- No human listening. "Now it's moved to step two" (2:31) and "very dizzy" (5:17) are whisper small.en readings and need an ear check.
- Frames were sampled every 5 s plus at scene changes. A brief on-screen defect shorter than ~3 s between samples could be missed.
- meta.json (title, description) was not re-audited. It was gated by the language-editor at 22:33Z.
