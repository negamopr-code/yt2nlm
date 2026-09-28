# S2 critic review, s2-v2.mp4 (Synonym Memory Challenge: SAD, P01, 16:9, polish round 1, 7:33)

Reviewer: glottos viewer-critic (headless autopilot step "special S2: critic"), 2026-09-28.
File checked: content/specials/S2/s2-v2.mp4, sha256 886656ca…c447 (the same file as the final re-render in polish-v2.md), 1280x720, 24 fps, 453.29 s.
Method:
- One contact sheet (a frame every 5 s, 91 frames).
- Full-resolution frames at 1, 35, 50, 200, 360, 430, 440, 450 and 453 s.
- Ladder highlight frames at 364, 374, 383, 403, 412, 418 and 434 s, and CTA frames at 437.5 and 441.5 s.
- Bottom-right corner crops at 5, 20, 100, 250, 320, 340, 400, 445 and 452 s.
- An ffmpeg silencedetect map (-35 dB, 0.8 s).
- A full faster-whisper small.en transcript (int8, cpu_threads=4, word timings).

References: script.md, focus.txt, meta.json, critic-v1.md, polish-v2.md, lang-gate-v2.md, the Specials section of docs/autopilot.md, and /workspace/state/glottos-methods/P01/strategy.md. NotebookLM was not touched. Nothing was rendered, uploaded or modified. The working files are in /tmp/s2c2.

## Verdict: SOLVES. No ship-blocking defect.

All 4 ship-blocking defects from v1 are fixed and verified on the file:
- The table now has all 15 rows, with the 5 extras marked and a karaoke highlight in sync with the voice.
- The comment CTA is on screen.
- The pauses are real: 4.0 s and 5.1 s of silence.
- The watermark is covered on every frame and the end card is gone.

The challenge works as designed: list score → story → story score → "15, not 10" reveal → full ladder → "comment your two scores" → "tonight, try it with your own words". A B1 learner who forgets words leaves with a number to compare and a method to reuse tonight. The remaining issues are cosmetic or minor: dejected still has no picture, the CTA is on screen but not spoken, and there are 3 caption overlaps.

## Pain in the learner's words (verbatim, from P01 research, as quoted in critic-v1 and strategy.md)
- "I've been trying to cram too many words and always forget them."
- "I forget every new word so of this works for me it will be life changing"
- "I also find myself forgetting certain English words when I'm speaking."
- "I reviewed but kept forgetting the words."
- "That's called mnemonics. Really helps you learn languages, specifically vocabulary, where you can associate some bonkers, vivid and chaotic story with a meaning and a pronunciation of a word."
- Score comments on the source method: "7 verbal, 15 visual. Just wow!" and "I tried it and it worked, from scoring 4/10 to 10/10."

In one sentence: "I learn words like gloomy or devastated, forget them in days, and when I speak I only say sad."
Solved means that tomorrow I recall more of a word group from a silly story than from a list, I know which SAD word fits which situation, and I can build my own story for my next word group.

## Beat survival (item 1): all present, in order
| # | Beat | Heard (s, v2 timeline) | On screen | Result |
|---|---|---|---|---|
| 1 | Hook | 0.00–14.52 "10 words for sad. How many can you remember? … grab a pen. You're getting two scores today." | Title "Synonym Challenge: SAD", then "Grab a pen! You are getting two scores." | OK. The pain question comes at 2 s. |
| 2 | Plain list of 10 | 18.80–29.46: melancholy, upset, blue, heartbroken, gloomy, disappointed, devastated, down in the dumps, unhappy, miserable | "10 Plain Words" card, all 10 in order, no pictures | OK (exact order) |
| 2b | Pause cue and hold | 30.54 "Pause the video now." 31.86–33.18 "Write down every word you remember." Silence 33.20–37.23 (**4.03 s**), then "Okay … All done? Count them up … Your list score." | Pause card "Write down every word you remember. / List Score", frozen during the hold | **Fixed** (was 1.03 s) |
| – | Bridge | 45.56–59.96 set-up: "roughly from a little bit sad to extremely sad … it ends well" | "One story. / 15 words. / Now watch the story." from about 45 to 60.7, then the Blue picture at 60.7 on "Let's start with blue" (60.74) | **Fixed** (the Blue card is no longer 15 s early). The "15 words" card pre-empts the reveal a little; the title already does the same. Not blocking. |
| 3 | One story, 15 words, mild → strong | Onsets: blue 60.7/64.3, disappointed 75.6, glum 89.3, unhappy 105.3, down in the dumps 125.1, gloomy 137.8, upset 157.6, melancholy 175.3, dejected 194.5, forlorn 214.2, miserable 230.2, sorrowful 246.6, heartbroken 263.6, devastated 277.1, inconsolable 296.7. Happy ending 311.3–317.4 | One card per word, in the same order | OK. Exact script order, one continuous plot, nothing merged or skipped. |
| 4 | Second pause, "in order" | 318.32–322.70 "Pause the video again, write down every word you can recall in order." Tip 323.5–330.4. Silence 330.51–335.64 (**5.13 s**) | "Write down every word you recall in order. This is your story score." | **Fixed** (was 2.63 s). The tip still runs over the first 7 s of writing time, but the viewer who pauses loses nothing. |
| 5 | "15, not 10" reveal and ladder | 341.16 "Now here's the sneaky part. I give/gave you 15 words, not 10. Glum, dejected, forlorn, sorrowful and inconsolable. Did any of those make it onto your list?" Recap of all 15 from 363.06 to 436.18 | Chalkboard with the 5 extras, then **our own 15-row "The SAD ladder"** (about 352.7–436.7). The rows run top-down from Blue to Inconsolable, the 5 extras have orange dots, and there is a karaoke row highlight | **Fixed.** Highlights were checked at 364 (Blue), 374 (Glum), 383 (Down in the dumps), 403 (Dejected), 412 (Miserable), 418 (Sorrowful), 430 (Devastated) and 434 (Inconsolable). Each lit row matches the word being spoken. |
| 6 | Comment prompt, transfer, site | 437.26 "List versus story." Silent hold 438.57–442.43. 442.16–447.30 "Tonight, try it with your own new words. One silly story, one picture for each word." 448.30–452.78 "For more words, look up another word for sad on anotherwordfor.net." | Plate "Which score was higher? / Comment your two scores: list vs story." over the score card (seen at 437.5–441.5), then the transfer card, then the site card, then a fade | **Fixed on screen.** There is still no *spoken* "comment". There is no promise of examples or a search box. |
| – | End | – | A fade to black on the site card at about 453. **No Gemini end card.** | OK |

No beat was dropped or scrambled, so the runbook's ask_user trigger ("our own renderer") does not apply.

## Accuracy for B1 (item 2)
- **Story voice:** all 15 meanings and registers are as gated. Blue is informal. Disappointed means "not as good as you hoped". Glum is quiet, a bit sad and shows on your face, and is a bit informal. Unhappy with means not satisfied. Down in the dumps is an informal idiom. Gloomy means without hope, and is also used for weather. Upset means something bad just happened, and is common in speech. Melancholy is literary. Dejected means "tried and failed" and is used in sports news. Forlorn is literary. Miserable is used for cold, wet or uncomfortable, and for weather. Sorrowful is old-fashioned and literary. Heartbroken means someone or something you love is gone. Devastated means extremely upset and shocked, and is used in speech. Inconsolable means nobody can make you feel better. Every acted scene fits its word: the dentist card, the silent breakfast with the dog, the leaning cake, sitting on bin bags, the black clouds, the goose, the harmonica, the goat judge's zero, the lone bench, the cold soup, the candle poem, the dog next door, the roof blown away, and the river of tears.
- **Ladder text:** every row matches script Beat 5 and lang-gate-v2 (APPROVED after the "strongest word here" fix). The voice says "Poems and old stories" while the cell says "old-fashioned, literary: poems". That is a shortening, not a contradiction. Heartbroken's WHEN cell is "—", which is acceptable.
- **Splice:** "Someone or something you love is gone." (425.42–426.88) is heard correctly. The prosody at the join was not ear-checked.
- **"I give you 15 words"** (342.86): whisper reads "give", while v1 read "gave" at the same audio. This is most likely a whisper artefact. Ear-check it; it is not blocking either way.

## Memory claims (item 3): clean
There are no statistics, no "most people", no "average person", no researchers and no "10x". The reveal asks "Did any of those make it onto your list?" and does not claim that the words came only from the story. There is no depression, illness or death, and the story has a happy ending.

## Watermark and end card (item 4)
Channel-logo tiles are present at the bottom right in all 9 corner crops (5 s to 452 s), including the ladder and the CTA, and there is no "Gemini Notebook" text anywhere. The Gemini end card has been trimmed: the video ends on the site card with a fade. **Pass.**

## On-screen text vs voice (item 5)
- The list, pause cards, story word cards, reveal chalkboard, 15-row ladder (with the highlight on the spoken row), transfer card and site card all match the voice.
- The one exception is the CTA plate: it asks for a comment while the voice only says "List versus story." This is an addition, not a contradiction.
- The dejected card (194.5–214) has **no picture**: text on a blank, faded background. The goat judge is heard but never seen.
- Caption overlaps are unchanged from v1 but still readable: the end of the glum line over the dog, the forlorn line over the bench legs, and the inconsolable title over the tissue box. The down in the dumps card still hides most of the dump.
- The main character is a girl in some scenes and a man in others. This cannot be fixed in post.

## v1 critic issues: status (item 6)
| v1 issue | v2 status |
|---|---|
| B1 Watermark and end card | FIXED (logo on every frame, trimmed at 444.79 src) |
| B2 Table had 8 of 15 rows | FIXED (15 rows, extras marked, highlight in sync) |
| B3 Comment CTA dropped | FIXED on screen (text plate plus a 3 s hold); still not spoken |
| B4 Pause holds 1.0 / 2.6 s | FIXED (4.03 / 5.13 s) |
| 5 "someone or someone" slip | FIXED (spliced; whisper hears "someone or something") |
| 6 Dejected has no picture | NOT FIXED (polish judged that a PIL-drawn panel would clash) |
| 7 Blue card 15 s early | FIXED ("One story. 15 words." bridge card) |
| 8 Caption scrims | NOT DONE |
| 9 Stress cues | NOT DONE (acceptable: focus.txt forbids pronunciation drills) |
| 10 focus.txt rules for S3–S5 | Still open for scenario-writer (see fixes) |

## Second by second: swipe risks
- 0:00–0:15: strong. The first 2 s ask my question ("How many can you remember?").
- 0:30–0:45: the pause now gives me time to write even without pressing pause. Good.
- 0:45–1:01: 15 s of set-up on a text card. This is the mildest dip; the promise ("one story") holds me.
- 1:01–5:17: the story, at 13–20 s per word, is funny and concrete. The weak spot is dejected (3:14–3:34), a blank card.
- 5:18–5:36: the second pause is fine.
- 5:41–5:53: the reveal is a real "aha".
- 5:53–7:17: 84 s on the ladder. It is still long, but the moving highlight keeps it alive, and it is the screenshot moment.
- 7:17–7:22: the silent 3.9 s CTA hold. A scroller may wonder whether the video froze, but the plate is large and clear.
- 7:22–7:33: the transfer line and the site, then the end.

## Takeaway test
Tonight I can take my own new words and make one silly story, with one picture per word. This is spoken at 7:22 and drawn. I also know the practical registers: *upset* and *devastated* in speech, *dejected* in sports news, and *sorrowful*, *forlorn* and *melancholy* only for books, songs and poems. I also get a concrete social action: comment "List x / Story y". → **Passes.**

## Retention risks
- The length is 7:33, just over the 5–7 min target.
- The ladder takes 84 s.
- The CTA hold is silent for 3.9 s.
- The 0.9x NotebookLM voice is steady and clear.
- Picture and voice are in sync for all 15 story words and for the ladder.

## Trust risks
- One story word (dejected) has no picture, in a video about the "picture method".
- The main character changes between a girl and a man.
- The "gave/give" reading has not been ear-checked.
- There are no factual or register errors and no overclaims.
- The anotherwordfor.net SSL certificate is still expired according to the v1 gate. That is not a video defect, but viewers who follow the call to action will see a browser warning (owner: site hosting, outside this pipeline).

## Top fixes (all non-blocking), ordered by impact
1. **Dejected picture, 194.5–214 s (visuals).** If a round 2 happens for any reason, generate one watercolour-style panel that matches the other scenes: a serious goat judge holding up a "0" card, and "you" walking away head down. Otherwise ship without it.
2. **Spoken comment CTA for S3–S5 (scenario-writer, focus.txt).** Require the exact sentence: "Which score was higher? Comment your two scores: list versus story." and "the recap table must have exactly 15 rows". NotebookLM dropped both in S1 and S2, so plan the overlay and the pause freezes in polish anyway. At publish time, add a pinned comment "List: __ / Story: __ ?" (publisher).
3. **Caption scrims on glum, forlorn and inconsolable, plus an ear check of the 342.9 "gave/give" and the 425–427 splice (visuals, language-editor).** Cosmetic.

## Not checked
- No human listening (the splice prosody, "gave/give", and the pronunciation of melancholy, forlorn and inconsolable).
- Frames were sampled every 5 s plus the key points listed above, so a defect shorter than about 3 s between samples could be missed.
- meta.json was not re-audited (it was gated at 11:16Z).
