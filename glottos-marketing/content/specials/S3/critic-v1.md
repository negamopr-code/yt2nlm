# S3 critic review, s3-v1.mp4 (Synonym Memory Challenge: BIG, P01, 16:9 NotebookLM whiteboard, 7:16)

Reviewer: glottos viewer-critic (headless autopilot step "special S3: critic"), 2026-09-28.
Watched as: a B1 to B2 learner who forgets new words within days and only ever says "big" or "very big" when speaking.

Method:
- 3 contact sheets (one frame every 5 s, 88 frames).
- Full-resolution frames at 0.7, 1.5, 8, 17, 25, 33, 36, 58, 80, 100, 115, 116.2, 117, 150, 160, 200, 213, 215, 222, 235, 250, 300, 310, 330, 345, 352, 380, 420, 425, 430, 433, 434.5 and 436 s.
- A watermark crop.
- Two scene-change passes (threshold 0.2 and 0.06, over the whole file).
- An ffmpeg silencedetect map (-35 dB at 0.8 s and at 0.7 s).
- A faster-whisper small.en transcript (int8, cpu_threads=4, word timings), plus 9 doubtful spots re-transcribed as isolated clips (0–3.5, 16–21, 30.5–34.5, 178.5–183, 211.5–215, 219.5–226.5, 314.5–318.5, 322.5–324.5 and 395.5–398 s).
- References: script.md, focus.txt, meta.json, lang-gate-v1.md, the S1–S5 section of docs/autopilot.md, /workspace/state/glottos-methods/P01/strategy.md and proof_doc.md.

NotebookLM was not touched. Nothing was rendered, uploaded or changed. The working files are in /tmp/s3c (outside the repo).

## Verdict: PARTLY (can ship after polish; no regeneration needed)

This is the best NotebookLM take in the series so far:
- **The audio is almost exactly the script.** All 6 beats are in order. All 15 story words come in the script's order, each with the right meaning and register.
- **The comment call to action is spoken word for word:** "Which score was higher? Comment your two scores, list versus story." This is the first time in the series; S1 and S2 dropped it.
- The transfer line and the anotherwordfor.net line are both there.
- The recap table has all 15 words and agrees with the voice.
- There are no memory statistics.

It cannot ship as it is:
1. **3 of the 5 "sneaky" extras have no picture, or no word on screen.** bulky (96.5–116.3) and hefty (116.3–132.6) are yellow caption cards on a blank background. whopping (211.7–226.4) has a picture (the truck scale and "1200") but **no word title and no meaning card**, so the word "whopping" never appears on screen in the story. These are exactly the words the reveal is about, and the story method depends on "one picture per word".
2. **The pause holds are too short:** 2.4 s at pause 1 and at most 1.4 s at pause 2, against a 3 s target. Pause 2 goes straight into the tip.
3. **The towering card says "Very literary"** while the voice says "a bit literary". This is a stronger label, which the gate and focus.txt ban, and the card has no meaning ("very tall").
4. **"Gemini Notebook" is on every frame, plus a Gemini end card (433.29–436.35).**

All four can be fixed in post. Regeneration is not needed, and the runbook trigger "ask_user about our own renderer" (beats dropped or scrambled twice) does **not** apply.

## Pain in the learner's words

Verbatim, from /workspace/state/glottos-methods/P01 (proof_doc.md, strategy.md, comments/*.jsonl). All were re-checked by grep in this run. No names are given.
- "I've been trying to cram too many words and always forget them."
- "I forget every new word so of this works for me it will be life changing"
- "I reviewed but kept forgetting the words."
- "That's called mnemonics. Really helps you learn languages, specifically vocabulary, where you can associate some bonkers, vivid and chaotic story with a meaning and a pronunciation of a word."
- Score comments on the source method's video: "7 verbal, 15 visual. Just wow!" and "I tried it and it worked, from scoring 4/10 to 10/10."

In one sentence: "I learn words like *vast* or *hefty*, forget them in days, and when I speak I only say *big* or *very big*."

Solved means that tomorrow I recall more of these words than I could from a list, and I know which one fits: *a hefty bill*, *a whopping 1,200 kilos*, *a mammoth task*, *immense relief*, and *ginormous* only with friends. I can also build a silly story for my own next word group.

## Beat survival: all beats are present and IN ORDER, and no spoken cue was dropped

| # | Required beat | Heard (whisper, s) | On screen (s) | Result |
|---|---|---|---|---|
| 1 | Hook ≤15 s, two scores | 0.00–15.20: "10 words for **B-I-G**. How many can you actually remember? Well, we're gonna test you. Then I'll show you one trick, just a single silly story, and we'll test you again. You'll also learn exactly when to use each word. Grab a pen, because you're getting two scores today." | 0–15.79 title card "Synonym Challenge: BIG" (pumpkin). 15.79–20.63 "How many words can you remember?" | OK: 15.2 s. Note: "B-I-G" takes 1.16 s (1.36–2.52), so it is most likely **spelled out letter by letter** (it was written in capitals in the script). This is harmless but odd. Ear check it. |
| 2 | Plain list of 10, in script order | 16.06 "First up is the plain list. Just read, listen, and try to **walk them in**." (Probably "lock them in". The clip also hears "walk"; ear check.) 21.14–~31.1: vast, jumbo, huge, considerable, ginormous, large, massive, immense, giant, enormous. | 20.63–31.67 "The Plain List": all 10 at once, in the correct order, with no pictures and no meanings | OK |
| 2b | Spoken pause cue plus a hold of at least 3 s | ~31.9 "Pause the **explainer** now. Write down every word you remember." (ends 34.68) then 36.98 "Done? Count them up. That's score number one, your list score. Keep it safe." | 31.67–54.42 card "Pause the video now. Write down every word you remember." with a pause icon | The cue is present. **The hold is 2.40 s** (silence 34.72–37.12), which is short. "explainer" is meta wording (the card says "video"). |
| 3 | ONE story, 15 words in the script's order | Set-up 41.2–52.7. Word onsets: large 55.06, considerable 76.08, bulky 96.86, hefty 116.50, jumbo 133.10, huge 149.24, giant 166.36, enormous 184.24, massive 199.44, whopping 212.18, vast 226.88, towering 245.70, mammoth 266.04, immense 284.76, ginormous 301.56. Happy ending 312.2–322.2 ("You win first prize [whisper: 'price'] ... your cat moves right into the empty shell. Don't worry, it's only a story."). | One card per word. Cuts at 54.42, 75.71, 96.46, (hefty: a caption swap with no scene cut, about 116.3), 132.63, 148.79, 165.63, 183.71, 198.54, 211.71, 226.38, 245.00, 265.38, 284.21, 300.88. Each is 0.3–0.9 s before the word. | **Exact order, nothing merged or skipped.** Picture/voice sync is excellent. Picture defects are covered in the next section. |
| 4 | Second pause "in order" | 322.98 "Pause the explainer again. Write down every word you can recall, in order." (ends 327.02) 328.40–333.82 tip "just walk through the story again. The large coffee, the 800-page book, the box you can't see over." 334.58 "Done? Count them up. That's score number two, your story score." | 323.04–339.54 TV card "Pause the video again. Write down every word you can recall." (It leaves out "in order", which the voice says.) | The cue is present. **The hold is ~1.4 s** (327.02–328.40) and **1.09 s** (333.83–334.92). There is no real pause. |
| 5 | "15, not 10" reveal plus ladder | 339.84 "And here is the sneaky part. I gave you fifteen words, not ten. Bulky, hefty, whopping, towering, and mammoth. Be honest, did any of them make it onto your list?" 351.20 "Here is the whole ladder on one screen, roughly from big to extremely big. Remember, the order is a guide, not a strict rule." 359.50–418.80: spoken recap of all 15 in order, with the script's labels. | 339.54–351.17 "I gave you 15 words, not 10! Did any of the extras make it onto yours?" (The 5 extras are not written.) 351.17–419.50 one static table (see below). | OK. The voice is correct, with no "only from the story" claim and no "top/bottom/strongest". |
| 6 | Comment CTA, transfer, site | 419.80–423.28 "**Which score was higher? Comment your two scores, list versus story.**" 423.88–428.30 "Tonight, try it with your own new words. One silly story, one picture for each word." 428.30–432.64 "For more words, look up another word for big on anotherwordfor.net." | 419.50–433.29 one card: "Which score was higher, list or story?" plus "anotherwordfor.net" | **The CTA is spoken exactly.** The card has no "comment" and no transfer text. It also has decorative word tags ("Gargantuan", "Colossal", "Titanic", "Immense") that the video never teaches. |
| – | End | – | **433.29–436.35 full-screen "Gemini Notebook" end card** (audio is silent 432.63–436.35) | Brand violation |

## Accuracy for B1

The story voice follows the gated script almost word for word. Every meaning and register is correct: large (a bit more formal than big), considerable (fairly formal; time, money, effort), bulky, hefty (money sense a bit informal), jumbo (informal, products), huge (very common in speech), giant (only before a noun), enormous (neutral), massive (heavy and solid, like a rock), vast (areas, spaces, amounts), towering (spoken: "a bit literary and only used before a noun"; correct), mammoth ("a mammoth task/job"), immense (feelings: "immense relief"), and ginormous ("informal and playful ... not so much for work emails").

Problems:
- **whopping, story, 221.66: "it almost always sits right before a number".** This overclaims: the script says "often" (and so does the recap at 396, "often right before a number"). It is a small trust issue, and the language-editor should decide. Fix 7 gives a splice.
- **The pronunciation of "whopping" as a headword.** Whisper hears "**Whooping**" at 212.18 (story headword) and "**Wapping**" at 396.14 (recap headword), but "whopping" at 216.66, 224.22 and 345.94. If the narrator really says /ˈhuːpɪŋ/ as the headword, a teaching video is modelling a wrong pronunciation. **Ear check is mandatory.** If it is wrong, splice in the correct "whopping" from 216.66–217.16.
- 180.30: "We only use this before **and now**" (heard the same on the isolated clip). This is probably "before a noun", slurred. Ear check it.
- 315.28 "first **price**": probably "prize" (a whisper artefact). Ear check it.
- "Pause the explainer" (×2): unnatural meta wording ("the video" is what learners expect). It is understandable, and the cards say "video". Not worth a splice ("video" is never spoken anywhere in the audio).
- NotebookLM additions are harmless: "Picture yourself in a yellow raincoat and green wellies" (this reads out our character note, but as natural narration), "you know", "literally", "Be honest", "six grueling hours", "Don't worry, it's only a story". No stage direction is read out as an instruction, and there is no "say it with me" drill.

Memory claims: **clean.** There are no statistics, no "most people", no "10x", no researchers, no age of the method, no "came only from the story" (it asks "did any of them make it onto your list?"), no "strongest", and no "top/bottom of the ladder". The CTA makes no promise of a search box or example sentences.

## On-screen text, pictures, watermark

- **bulky (96.46–~116.3) and hefty (~116.3–132.63): NO picture.** Each is a yellow card (word plus a correct one-line meaning) on a faded background with a ghost knight. The lamppost scene and the receipt out of the door are heard but never seen. That is about 36 s with no image, on 2 of the 5 extras.
- **whopping (211.71–226.38): picture but NO word and NO meaning.** It shows the truck, the farmer, the scale, and a stylised "1200" with an elephant and whale doodle. It is the only one of the 15 story words that is never written on screen during the story.
- **towering (245.00–265.38): the caption reads "Very literary, and only used before a noun."** The voice (259.9) and the gate say "a bit literary" (Cambridge "literary"; Oxford has no label). "Very literary" is stronger than the source, and the meaning "very tall" is missing from the card. It is also the only card with a register-first caption. The picture is good (house, beanstalk, bird nest, "towering trees" and "towering cliffs" labels).
- massive (198.54–211.71): the picture is a hand pushing **a black rock** with a flattened wheelbarrow, not the pumpkin. The meaning matches ("like a rock"), but the story continuity breaks for one scene. This is minor.
- The protagonist "you in a yellow raincoat" is spoken at 55.9 but never drawn. There is no recurring character. This is minor, because the pumpkin carries the continuity (it grows scene by scene: armchair size, car size, taller than the house).
- The other captions are all correct and legible: large, considerable, jumbo, huge (the title slightly overlaps the pumpkin, but it is readable), giant, enormous, vast, mammoth (small type in a small card, readable at 720p), immense, and ginormous.
- **Pause 2 card (323.04–339.54):** it reads "Write down every word you can recall." and leaves out "**in order**", which the voice says. This is minor. It can be added in the same overlay as the freeze.
- **Reveal card (339.54–351.17):** "I gave you 15 words, not 10! Did any of the extras make it onto yours?" It is correct, but the 5 extras are not written. Adding "bulky · hefty · whopping · towering · mammoth" would help the viewer check their list.
- **Ladder table (351.17–419.50, 68 s):** all **15 words, correct, no invented rows**. It is a 2-column layout with 8+7 rows (Word | Use | Word | Use). Read row by row, left to right, it matches the voice order exactly (Large, Considerable / Bulky, Hefty / Jumbo, Huge / Giant, Enormous / Massive, Whopping / Vast, Towering / Mammoth, Immense / Ginormous). Read column by column (which is what eyes usually do), the ladder order looks scrambled. It breaks the "one row per word, no pairs" instruction, and it has only a "Use" column with no meanings. The cells are fine: "Hefty: Heavy, money", "Immense: Big, great, feelings", "Towering: Very tall" (correct here), "Jumbo: Products (Informal)", "Ginormous: Playful, informal". It does not contradict the voice. This is not ship-blocking, but for consistency with the S1/S2 polished ladders it should be overlaid (fix 5).
- **CTA card (419.50–433.29):** "Which score was higher, list or story?" plus anotherwordfor.net. It has no "Comment your two scores" (the voice says it) and no transfer line. The tags "Gargantuan", "Colossal" and "Titanic" are real synonyms but are not taught. A learner may wonder whether they missed them, but they are not false.
- **Watermark: "Gemini Notebook" is in the bottom-right corner of EVERY frame** (about x 1155–1275, y 695–715 at 1280x720), including the table and CTA cards (crop: /tmp/s3c/wm.png). **Full-screen Gemini end card from 433.29 to 436.35.**

## Second by second: where a viewer would swipe away

- 0:00–0:03: "10 words for B-I-G. How many can you actually remember?" This is my problem as a question, so I stop. The spelled-out "B-I-G" is a slight speed bump.
- 0:03–0:15: the promise, "grab a pen". OK.
- 0:16–0:31: the list. Readable, all on screen for 11 s.
- 0:32–0:37: **2.4 s of silence after "Write down every word you remember"**. If I don't press pause, I can't write 10 words, and score 1 (the whole comparison) is weak.
- 0:41–0:55: set-up talk over the pause card (14 s). This is a mild drop risk, but shorter than in S2.
- 0:55–5:22: the story. It is funny and concrete: an 800-page book until dark, a pumpkin in the living room, the cat climbing it like a mountain, a wheelbarrow flat as a pancake, 50 neighbours and a small dog pulling ropes, a girl shouting "It's ginormous!". There are **two dead zones: 1:36–2:12 (bulky, hefty) with plain yellow cards and no pictures.** This is the most likely mid-video swipe, because after four illustrated scenes the video suddenly looks like slides. Then 3:32–3:46: whopping shows a truck but no word, so a visual learner doesn't know what to remember.
- 5:23–5:39: **the second pause has no real hold.** The tip talks straight through the moment when you should be writing.
- 5:40–5:51: the reveal. A genuine "aha", and the voice names the 5.
- 5:51–6:59: 68 s on one static table. Complete, but slow and in two columns.
- 6:59–7:13: "Comment your two scores" is spoken (good), the transfer is spoken, and the site is spoken and shown.
- 7:13–7:16: the Gemini end card.

## Takeaway test

After watching I can say *a hefty bill*, *a whopping 1,200 kilos*, *a mammoth task* and *immense relief*. I know *ginormous* and *jumbo* are informal, and I know *considerable* is fairly formal. And I know **tonight I build one silly story, with one picture per word, for my own new words** (spoken at 423.9). That is a real action for the P01 pain. The social action is also there: "Comment your two scores" is spoken. The weak point is that the method's promise, "one picture for each word", is visibly broken for bulky, hefty and (as a word) whopping.

## Retention risks

- Length is 7:16 (7:13 after trimming the end card, and about 7:18 with the pause freezes). That is just over the 5–7 min target. The story carries it.
- Pacing: the story is steady at about 16–20 s per word. The two no-picture cards (36 s) and the static table (68 s) drag.
- Sync: excellent. Every story card appears 0.3–0.9 s before its word, the pause cards land on the cue, and the table and CTA land on the voice.

## Trust risks

- The towering card says "Very literary" against the voice's "a bit literary", and the gate bans stronger labels.
- The whopping headword may be mispronounced ("whooping"). Ear check this before shipping.
- "almost always sits right before a number" overclaims.
- The Gemini watermark and end card break the brand rule.
- There are no memory statistics or false claims about the method.

## Defects and fixes

### Ship-blocking (all can be fixed in post, no regeneration)

1. **Watermark and end card (shorts-builder).** Trim at **433.0 s** (the CTA audio ends at 432.64, and the end card starts at 433.29). Cover the bottom-right "Gemini Notebook" mark (about x 1150–1280, y 690–720) on every frame with the channel logo `state/brand/awf-logo-channel.jpg` or a background-matched patch.
2. **Pause holds (shorts-builder).** Insert a silent **3 s freeze** of the pause 1 card at **34.70 s** (after "remember.", inside the existing 2.40 s silence, for about 5.4 s in total). Insert a silent **3 s freeze** of the pause 2 card at **327.05 s** (straight after "in order.", before the tip). On that freeze, add "in order" to the card text ("Write down every word you can recall, **in order**."). That adds about 6 s.
3. **Missing pictures for bulky and hefty (visuals, then shorts-builder).** Draw two whiteboard panels in the same watercolour style, and place them in the empty upper and right area of the yellow cards (the card leaves about x 0–1000 × y 60–330 and the right-hand third free).
   - bulky, **96.46–116.30**: you carrying a box of plant food as big as a sofa, a strange shape, walking into a lamppost.
   - hefty, **116.30–132.63**: a very long receipt rolling across the floor and out of the door, with the total circled.
   - Check the exact caption swap frame between 116.0 and 116.5.
4. **whopping has no word on screen, 211.71–226.38 (shorts-builder, with a language-editor check of the text).** Overlay a caption card in the series style in the upper left of the yellow card (about x 50–330, y 70–170 is free; the truck fills the lower half): "**whopping**" plus "Very big. Informal, often right before a number." From 212.1.
5. **towering caption, 245.00–265.38 (shorts-builder, then a language-editor re-gate).** Patch the caption line "Very literary, and only used before a noun." (about x 170–560, y 265–310 at 1280x720) with "**Very tall. A bit literary, only before a noun.**" This matches the voice and the gate.

### Recommended (in post)

6. **Ladder table, 351.17–419.50 (visuals, then shorts-builder, then language-editor).** Overlay our own **15-row, single-column** ladder (heading "big → extremely big", word · meaning · when, with the script's Beat 5 labels, and the 5 extras marked). Reuse the S2 polish builder and highlight each row as the voice reaches it: large 359.50, considerable 363.14, bulky 368.30, hefty 371.36, jumbo 376.30, huge 381.54, giant 385.34, enormous 389.30, massive 392.78, whopping 396.14, vast 400.36, towering 404.64, mammoth 407.86, immense 411.98, ginormous 416.14. The current table is correct but paired, has no meanings, and misreads if scanned by column.
7. **whopping audio (shorts-builder, then a language-editor ear check).**
   - (a) If the headword at **212.18–212.50** (and **396.14–396.34**) is really "whooping", replace it with the narrator's correct "whopping" from **216.66–217.16** or **224.22–224.64**, using a ~20 ms crossfade.
   - (b) Optional: replace "almost always" (in 221.66–~223.4) with nothing, or splice "often" from the recap at about 397.5. Let the language-editor decide whether "almost always" is acceptable.
8. **CTA card, 419.50–433.0 (shorts-builder).** Overlay "Comment your two scores: list vs story" (from 420.9) and "Tonight: one silly story, one picture per word" (from 423.9). Cover the untaught "Gargantuan / Colossal / Titanic" tags, or leave them (they are not false). Pin a comment "List: __ / Story: __ ?" at publish (publisher).
9. **Reveal card, 339.54–351.17 (shorts-builder).** Add the 5 extras as text: "bulky · hefty · whopping · towering · mammoth" (spoken at 344.54–348.2).
10. Ear checks only (language-editor): "B-I-G" spelled out (1.36–2.52), "walk them in" (18.6), "before a noun" (180.3), and "first prize" (315.28). Fix only if one is a real error. Splicing the hook "big" is not possible, because "big" alone is said only inside phrases (e.g. "extremely big" at 52.2).
11. For S4–S5 (scenario-writer, focus.txt): NotebookLM followed the exact CTA sentence this time, so keep that rule. Add: "Every one of the 15 words must have a drawn picture AND its word written on screen", "Captions must use the same register words as the voice (never 'very literary')", "Write the word in lower case in the focus text, never in capitals (BIG was spelled out)", and "say 'pause the video', not 'explainer'". Plan the pause freezes in polish anyway (this is the third video where the holds were short).

After fixes 1 to 5 (ideally with 6 and 7a), this should reach **SOLVES**. Re-run the critic on the polished file.

## Not checked

- No human listening. The pronunciation of "whopping", the spelled "B-I-G", "walk them in", "before a noun" and "prize" are whisper small.en readings (the isolated clips gave the same readings).
- Frames were sampled every 5 s, plus scene changes and 33 full-resolution frames. A defect lasting less than about 3 s between samples could be missed.
- meta.json was not re-audited (it was gated). The title "Can You Remember 15 Synonyms for BIG?" slightly spoils the "15, not 10" reveal, as the gate noted.
- The anotherwordfor.net SSL status was not re-checked (the gate recorded the certificate as expired, with a browser warning).
