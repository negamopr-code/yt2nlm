# S3 critic review, s3-v2.mp4 (Synonym Memory Challenge: BIG, P01, 16:9, polish round 1, 7:19)

Reviewer: glottos viewer-critic (headless autopilot step "special S3: critic"), 2026-09-28.
File checked: content/specials/S3/s3-v2.mp4, sha256 a2f72389…0cfd, 1280x720, 24 fps, AAC mono, 439.00 s.

Method:
- 2 contact sheets (a frame every 5 s, 88 frames).
- Full-resolution frames at 0.7, 1.5, 36.5, 105, 125, 219, 255, 332.5, 350, 360, 426, 432, 438.5 and 438.9 s.
- Ladder highlight frames at 403, 411.5 and 423 s.
- 21 boundary frames around every patch, freeze and overlay edge (37.6, 40.2, 99.3/99.5, 119.2/119.4, 135.5/135.7, 215.0, 229.3/229.5, 248.0, 268.4, 330.0, 333.5, 344.5, 356.5–357.6, 425.6/426.0).
- A frame-by-frame strip of 118.5–119.7 s.
- Bottom-right corner crops at 219 and 380 s.
- A zoomed crop of the towering patch.
- An ffmpeg silencedetect map (-35 dB, 0.8 s).
- A full faster-whisper small.en transcript (int8, cpu_threads=4, word timings).

References: script.md, focus.txt, meta.json, critic-v1.md, lang-gate-v2-polish.md, polish-v2-build/plan.py, state/autopilot.json specials.S3.note, the Specials section of docs/autopilot.md, S2 critic-v2.md (format), and /workspace/state/glottos-methods/P01 (quotes re-grepped in this run).

NotebookLM was not touched. Nothing was rendered, uploaded or modified. The working files are in /tmp/s3c2, outside the repo.

## Verdict: SOLVES. No ship-blocking defect.

All 5 ship-blockers from critic-v1 are fixed and verified on the file:
1. bulky and hefty now have their own pictures.
2. whopping has its word and meaning on screen.
3. towering reads "Very tall. A bit literary, only before a noun."
4. Both pauses are real holds: 5.4 s and 3.6 s of silence.
5. The Gemini mark is gone from every checked frame, and the end card is cut.

The polish also did recommended fixes 6, 8 and 9:
- a 15-row ladder with a karaoke highlight in sync with the voice;
- CTA plates for "Comment your two scores", "Tonight…" and "Look up…";
- the 5 extras named on the reveal card.

All six challenge beats are there, in order: list score, story, story score, "15, not 10", ladder, then comment your scores and try it tonight. A B1 learner who forgets words leaves with two numbers to compare, a clear sense of which BIG word fits where, and one thing to do tonight.

What is left is cosmetic or audio-only and cannot be fixed without splicing: "Pause the explainer" ×2, "almost always" for whopping, and a 0.25 s picture/caption mismatch at 119.05 s.

## Pain in the learner's words

These quotes are verbatim from /workspace/state/glottos-methods/P01. Each one was re-grepped in this run. No names are given.
- "I've been trying to cram too many words and always forget them."
- "I forget every new word so of this works for me it will be life changing"
- "I reviewed but kept forgetting the words."
- "That's called mnemonics. Really helps you learn languages, specifically vocabulary, where you can associate some bonkers, vivid and chaotic story with a meaning and a pronunciation of a word." (quoted in critic-v1)
- Score comments on the source method: "7 verbal, 15 visual. Just wow!" and "I tried it and it worked, from scoring 4/10 to 10/10."

In one sentence: "I learn words like *vast* or *hefty*, forget them in days, and when I speak I only say *big* or *very big*."

Solved means that tomorrow:
- I remember more of a word group from a silly story than from a list;
- I know *a hefty bill*, *a whopping 1,200 kilos*, *a mammoth task* and *immense relief*, and that *ginormous* is only for chatting with friends;
- I can build my own story for my next word group.

## critic-v1 ship-blockers: verification on s3-v2

| # | v1 defect | v2 evidence | Result |
|---|---|---|---|
| 1 | Gemini watermark on every frame, plus a Gemini end card from 433.29 s | The corner crops at 219 and 380 s show only the AnotherWordFor channel logo. The file ends at 439.00 (source 433.0 + 6 s of freezes). The last frames (438.5 and 438.9) are the CTA card fading to black. No end card. | FIXED |
| 2 | Pause holds of 2.4 s and 1.4 s | Silence 34.72–40.12 (**5.4 s**) on the pause 1 card. Silence 330.03–333.63 (**3.6 s**) on the pause 2 card, straight after "in order.", before the tip. The picture is frozen on the card and there is no audio bleed. | FIXED |
| 3 | bulky and hefty had no picture | bulky (99.46–119.05): a sofa-sized "PLANT FOOD (extra large)" box on green-welly feet, BONK! into a lamppost. hefty (119.3–135.6): a receipt printer with TOTAL 1,240 circled and paper rolling across the floor out of a door. Both match the story as it is heard. | FIXED (the style is flat vector, not watercolour; see minor 2) |
| 4 | The word whopping was never on screen | "whopping" plus "Very big. Informal, often right before a number." from 215.10. The voice says "Whopping" at 215.30. The card sits in the free upper left and does not cover the truck, scale or "1200". It goes at 229.4 exactly on the cut to vast. | FIXED |
| 5 | towering said "Very literary" and had no meaning | "Very tall. A bit literary, only before a noun." from 248.0 to 268.4. The voice says "very tall … a bit literary, and only used before a noun" at 260.4. The patch is clean, with only a hair-thin rectangle edge visible when zoomed (invisible at normal size). | FIXED |

## Beat survival: all present, in order (v2 timeline)

| # | Beat | Heard (s) | On screen | Result |
|---|---|---|---|---|
| 1 | Hook ≤15 s | 0.00–15.20 "10 words for B-I-G. How many can you actually remember? … Grab a pen, because you're getting two scores today." | Title "Synonym Challenge: BIG" (pumpkin), then "How many words can you remember?" | OK. "B-I-G" still sounds spelled out (unchanged, audio). |
| 2 | Plain list of 10 | 21.1–~31.1 vast, jumbo, huge, considerable, ginormous, large, massive, immense, giant, enormous | "The Plain List", all 10 words in order, no pictures | OK |
| 2b | Pause 1 + 3 s silence | 32.0 "Pause the explainer now. Write down every word you remember." Then **5.4 s silence**. 40.1 "Done? Count them up… your list score." | Pause card with a pause icon | OK |
| 3 | Story, 15 words, script order | Onsets: large 58.1, considerable 79.1, bulky 99.9, hefty 119.5, jumbo 136.1, huge 152.2, giant 169.4, enormous 187.2, massive 202.4, whopping 215.3, vast 229.9, towering 248.7, mammoth 269.0, immense 287.8, ginormous 304.6. Happy ending 315.2–325.2 ("You win first prize … it's only a story"). | Each of the 15 has a picture AND its word and meaning on screen, with cuts 0.3–0.9 s before the word | **Exact order, nothing merged or skipped** |
| 4 | Pause 2 "in order" + 3 s silence | 326.3 "Pause the explainer again. Write down every word you can recall, in order." Then **3.6 s silence**. 333.5 tip "walk through the story again…". 341 "your story score." | TV pause card + highlighted "In order." chip | OK |
| 5 | "15 not 10" reveal + ladder | 345.5 "I gave you 15 words, not 10. Bulky, hefty, whopping, towering, and mammoth. Be honest…" 357.5 "the whole ladder on one screen… a guide, not a strict rule." Then the recap of all 15. | Reveal card + "The extras:" chips (from 350.3, the voice names them at 350.6). Then the 15-row "The BIG ladder" (357.2–425.5) with the 5 extras dotted and a row highlight that follows the voice (large 365.5, whopping 402.1, towering 410.6, ginormous 422.3, all verified). | OK. No "top/bottom/strongest" on screen or in the voice. |
| 6 | Comment CTA, transfer, site | 425.4 "**Which score was higher? Comment your two scores, list versus story.**" 429.9 "Tonight, try it with your own new words. One silly story, one picture for each word." 434.9 "For more words, look up another word for big on anotherwordfor.net." | "Comment your two scores: list vs story" (426.9), then "Tonight: one silly story, one picture for each word" (429.9), then "Look up: another word for big" (434.3), each over "Which score was higher, list or story?" + anotherwordfor.net | OK. Every plate lands on its spoken line. No promise of a search box or examples. |

## Accuracy for B1 (acted meaning and register per synonym)

All 15 story scenes act out the right sense:
- **large**: a large coffee on a menu (sizes and amounts, a bit more formal)
- **considerable**: an 800-page book until dark (large in amount, fairly formal: time, money, effort)
- **bulky**: a sofa-sized box you walk into a lamppost with (big and hard to carry)
- **hefty**: a receipt out of the door (big bill, a bit informal)
- **jumbo**: a jumbo pack of popcorn (products, informal)
- **huge**: a pumpkin in the living room (very common in speech)
- **giant**: the neighbour's pumpkins are peas, plus a "giant pumpkin" headline (bigger than others of its kind, only before a noun)
- **enormous**: car-sized, the cat climbs it (neutral)
- **massive**: won't move, a flattened wheelbarrow (heavy and solid). The picture still shows a rock, not the pumpkin, as in v1. Minor.
- **whopping**: 1,200 kilos on the truck scale (before a number, informal)
- **vast**: leaves over the football pitch (areas, spaces, amounts)
- **towering**: taller than the house, a bird's nest on top (very tall, a bit literary)
- **mammoth**: the whole village pulling ropes (a mammoth task)
- **immense**: relief on arrival (feelings)
- **ginormous**: a girl shouts "It's ginormous!" (informal, playful)

The on-screen ladder and the captions agree with the voice. They were gated APPROVED in lang-gate-v2-polish.md, and I found nothing to contradict that.

Things that remain in the audio (not changed by the polish; none is ship-blocking):
- whopping, 223.9: "it almost always sits right before a number". The card, the ladder and the recap all say "often". This is a mild overclaim in one spoken sentence, and the screen shows the correct version.
- "Pause the explainer" (×2): meta wording. Both cards say "video".
- "B-I-G" is spelled out in the hook. "walk them in" (18.6) is probably "lock them in". "before and now" (184.6 and 397.8) is probably "before a noun", slurred. The screen shows "only before a noun" both times.
- The whopping headword ("Whooping"/"Wapping" in whisper): the polish checked the formants of all 4 utterances and found the same vowel. I accept that. It is a whisper artefact, but no human has listened to it.

Memory claims: clean. There are no statistics, no "most people", no researchers, and no "came only from the story".

## New defects introduced by the polish

1. **119.05–119.30 s (6 frames): the bulky picture sits over the hefty caption.** The underlying NotebookLM caption swaps at about 119.05 (source ≈116.05), but the bulky overlay runs to source 116.30. This is in the silent gap between "bulky suitcase." (118.18) and "Hefty." (119.54), so it is a quarter-second flash and does not affect the voice. It is cosmetic and not ship-blocking. Fix: end BULKY at fr(116.05) (shorts-builder).
2. The bulky and hefty panels are flat vector clip art in a watercolour video. They are readable and match the story, but you can see they were added later. The hefty panel has no "you" in it. This is cosmetic.
3. towering: the patch leaves a faint 1 px rectangle edge (visible only when zoomed). The channel logo partly covers the bottom "towering cliffs" label, which was in the source drawing, where "towering cliffs" appears twice. Cosmetic.
4. On the CTA card, the plates cover most of the untaught "Gargantuan"/"Immense" tags. One edge of "Gargantuan" is still visible under plate 2. Harmless.

There are no audio pops at the freeze boundaries: both freezes sit inside silence. Picture/voice sync after the freezes is preserved. Every later overlay was checked against the v2 word timings: the whopping card, the extras chips, all 15 ladder rows, and the 3 CTA plates.

## Second by second: where a viewer would swipe away

- 0:00–0:15: the pain question arrives at 2 s ("How many can you actually remember?"). The title card is static for 15 s, which is fine for a 16:9 video people click into on purpose, and weak as a scroll-stopper.
- 0:21–0:31: the list is readable.
- 0:32–0:40: now a real 5 s pause, so a lazy viewer can still write something.
- 0:44–0:58: set-up talk (14 s). This is a mild drop risk.
- 0:58–5:25: the story. Every scene now has a picture and a word, so the v1 "slides" dead zone at 1:36–2:12 is gone. The pacing is steady, at 16–20 s per word.
- 5:26–5:41: the pause, then the tip. This works now.
- 5:45–5:57: the reveal with the 5 extras written. This is the "aha" moment.
- 5:57–7:05: a 68 s recap on the ladder. The moving highlight keeps it alive, but it is the slowest part. Swipe risk is moderate for viewers who already feel done.
- 7:05–7:19: comment the scores, try it tonight, the site. It ends clean.

## Takeaway test

Tonight: take my own new word group, make one silly story, one picture per word. Then comment "list X / story Y" under the video. Both actions are spoken AND on screen. I also know *a hefty bill*, *a whopping 1,200 kilos*, *a mammoth task*, *immense relief*, that *ginormous* and *jumbo* are informal, and that *considerable* is fairly formal.

## Retention risks

- The length is 7:19. That is slightly above the 5–7 min target. The story carries it, and the 68 s recap drags a little.
- The narrator's pace is natural.
- Text legibility: the ladder is legible at 720p. The mammoth caption text is small but readable.
- Sync: excellent throughout.

## Trust risks

- "almost always before a number" (spoken once; the screen says "often").
- "Pause the explainer" (×2).
- Only whisper has checked the audio ear-check items.

None of these contradicts the screen in a way that teaches something wrong.

## Top fixes (none ship-blocking; optional before publish)

1. **shorts-builder:** end the bulky overlay at source 116.05 s, not 116.30, to remove the 6-frame bulky-over-hefty flash (v2 119.05–119.30).
2. **language-editor, then shorts-builder:** decide on "almost always" (v2 ≈223.9–225.9). Either accept it, or splice "often" from the recap (v2 ≈403.5). If you keep it, the screen already carries the correct "often".
3. **scenario-writer (S4–S5 focus.txt):** carry forward the critic-v1 fix 11 rules ("picture AND word for all 15", "caption register = voice register", lower-case target word, "say 'pause the video'"). The rules are still needed, because this polish had to repair all of them in post.

Publisher: pin the comment "List: __ / Story: __ ?" at publish.

## Not checked

- No human listening. The whisper small.en readings of "B-I-G", "walk them in", "before and now", "Wapping" and "prize" are unverified by ear.
- Frames were sampled every 5 s, plus about 40 targeted frames. A defect shorter than about 2 s away from a patch edge could be missed.
- meta.json was not re-audited. The title "Can You Remember 15 Synonyms for BIG?" slightly spoils the "15, not 10" reveal, as noted by lang-gate-v1 and critic-v1.
- The anotherwordfor.net SSL state was not re-checked.
