# M1 language gate v2: m1-v2.mp4 (on-screen text changed in post)

Gate: glottos-language-editor (headless autopilot step "special M1: polish", re-gate). Date: 2026-09-28T01:00Z (UTC).
Input: content/specials/M1/m1-v2.mp4 (332.21 s), changelog polish-v2.md, critic-v1.md, script.md.
Method: full-resolution frames from m1-v2.mp4 (ffmpeg -ss ... -frames:v 1) at 11, 12.5, 111, 114, 170, 178, 183, 195, 204.5, 220, 230, 250, 260, 263, 290-316 (quiz), plus an 18-frame spot sheet (3 to 330 s) and 2x crops of the quote-2 slide. Audio: faster-whisper medium.en (int8, word timings) on 0-20, 76-140, 160-210, 255-268, 284-332 s. No stamp via shorts/lang_gate.py (M1 has no unit JSON); the verdict is recorded here. Nothing was edited, uploaded or sent to NotebookLM.

## Verdict: NEEDS FIX (2 items, both on-screen; audio passes)

| # | Line / item (new time) | Problem | Fix | Confidence |
|---|---|---|---|---|
| 1 | Quote 3 card, 165.75-181.50: `A learner wrote:` + "Repeat the sentence I made myself over and over was a game changer." | With the new "A learner wrote:" tag the card now claims to be the learner's exact words, but it is (a) ungrammatical: an imperative "Repeat ..." cannot be the subject of "was"; the original only works because the phrase is inside inner quotes; and (b) silently shortened ("I must say that" and "for me" dropped, no ellipsis). A B1-B2 learner may copy the broken structure. The voice reads the full quote correctly. | Re-letter the card body (same font, same yellow highlights on "sentence" and "game changer") to: `…'Repeat the sentence I made myself over and over' was a game changer for me.` (acceptable shorter form: `'Repeat the sentence I made myself over and over' was a game changer for me.`). Keep the "A learner wrote:" tag. | high |
| 2 | Quote 2 slide, about 109.8-115.3 (behind the card) | Legible NotebookLM garbage, clear at 720p: the ribbon under the card reads "Töring toe the worab and ceadwe will be wed to welsh..." (gibberish), and the notebooks on the left are labelled **"Cognizaant"** twice (misspelling of *cognizant*). A misspelled vocabulary word on screen breaks credibility for a vocabulary brand, the same way "Speakting" did. It was also in v1 but was not in the critic's list. | Inpaint the ribbon text (leave an empty ribbon) and either repaint "Cognizaant" as "Cognizant" (both notebooks) or blank both labels. "Ephemeral" is spelled correctly and can stay. | high |

## Items checked and passed

| Item | Result | Confidence |
|---|---|---|
| `A learner wrote:` (x3) | Natural, standard attribution. It matches the script wording ("A learner wrote: ..."). The tag is on screen before the voice starts each quote (Q1 10.25 vs voice 10.42; Q2 109.79 vs 110.26; Q3 165.75 vs 166.08). Q1 card is verbatim. Q2 card is marked as truncated ("it...") and reads correctly. Q3: see fix 1. | high |
| `One week later: % of a text remembered` | Clear, idiomatic enough for a chart title. It says "of a text", not "of words", which matches the P01 note (about 61% vs about 40% of a text, one week later). The bars (40 / 61, "Re-read text" / "Cover and recall") and the y-axis "Memory Retained (%)" are consistent. Optional polish only: "Remembered one week later (% of the text)". | high |
| `STEP 2: LEARN WHEN TO USE IT` (181.5-204.8) | Correct. The voice at 181.8 says "When to use it.", then swamped/livid register. The voice says "Step three" at 205.26, after the banner is gone. No more double "Step 3". | high |
| Quiz audio "very busy" (297.10) | medium.en hears "Very busy." then "Swamped." at 300.16. The whole quiz reads: very angry / Livid, very busy / Swamped, very tired / Exhausted, very happy / Thrilled, very important / Crucial, with 2.6-3.0 s pauses. The on-screen question "What is the word for very busy?" matches. Statement intonation is fine: whisper also hears the other four prompts as statements, so it is consistent. | high (whisper only, no human ear) |
| Cut joins | 6.79 "It's just gone. / Your memory is not broken. The method is." · 13.50 "...always forget them. / So first, a quick challenge." · 93.71 "...they actively used them. / Reading mostly trains recognition." · 115.29 "...on paper. / So what should you do?" · 262.29 "...just days 1, 3, and 7. / For the first five minutes, your anchor phase, take three new words..." All grammatical, no clipped words. The last join is a little abrupt without the "15-minute routine" sentence, but the Anchor / Review / Speak card (0-5 / 5-10 / 10-15 mins) is on screen from 262.29 and carries it. | high |
| Removals | No "Speakting", no raw markdown asterisks, no "Gemini Notebook" watermark or end card seen in any checked frame. The quiz slides show no "Livid"/"Exhausted" leak and no stray "Step 1-3" labels. The channel logo is bottom-right. | high |

## Not checked / known and left as is (not blocking)

- Human listening was not done. The audio checks are whisper medium.en only.
- Frames were sampled, not every frame. A short text defect between samples could be missed.
- Faint low-contrast leftover art on the chart and timeline slides ("Comprehension" x2, "e.g. meaning & meaning", "Garden", "blossom", "perfume", "memory album", "network of associations"). It is hard to read, so I accept it. If fix 2 is done by inpainting anyway, "e.g. meaning & meaning" is the next candidate.
- Known v1 items that are still there: fake handwriting on the "Use it" slide ("Create ... Produce ... certzgation"), "Use|the" partly covered by the microphone, random words in the routine notebook. These were already in critic-v1.md.
- Pre-existing table cell "Good Context: Fine at work" for "swamped" is slightly ambiguous ("fine to use at work"), but acceptable. The voice says "swamped is totally fine at work".
- "mins" on the routine card is informal but acceptable.

## Re-gate condition

After fixes 1 and 2, re-extract frames at about 112 s and 170 s and re-gate those two slides only. Everything else above stays approved unless other edits are made.
