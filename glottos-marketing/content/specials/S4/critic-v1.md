# S4 critic review, s4-v1.mp4 (Synonym Memory Challenge: BEAUTIFUL, P01, 16:9 NotebookLM whiteboard, 6:51)

Reviewer: glottos viewer-critic (headless autopilot step "special S4: critic"), 2026-09-28.
File checked: content/specials/S4/s4-v1.mp4, sha256 de575864…778e, 1280x720, 24 fps, AAC mono, 410.76 s (made on work4).
Watched as: a B1 to B2 learner who forgets new words within days and, when speaking, only ever says "beautiful" or "very beautiful".

Method:
- 2 contact sheets (a frame every 5 s, 83 frames), plus a 1 fps strip of 36–86 s and a 4 fps strip of 405–411 s.
- Full-resolution frames at 0.7, 1.5, 13, 20, 33, 50, 75, 330, 350, 400, 405, 409 and 410.5 s.
- Frames at the midpoint of the voice for 17 story/beat moments (78, 93, 108, 120, 147, 165, 218, 232, 275, 288, 296, 300, 304, 308, 314, 320 and 395 s) to check that the picture matches the voice.
- Caption crops at 120, 200 and 275 s, and a zoomed crop of the ladder background.
- Two scene-change passes (threshold 0.2 and 0.05, over the whole file).
- An ffmpeg silencedetect map (-35 dB, 0.7 s).
- A full faster-whisper small.en transcript (int8, cpu_threads=4, word timings).
- References: script.md, focus.txt, meta.json, lang-gate-v1.md, the Specials / S1–S5 sections of docs/autopilot.md, S3 critic-v1.md and critic-v2.md (format), /workspace/state/glottos-methods/P01/strategy.md and proof_doc.md (quotes re-grepped in this run).

NotebookLM was not touched. Nothing was rendered, uploaded or changed. The working files are in /tmp/s4c (outside the repo).

## Verdict: PARTLY (can ship after polish; no regeneration needed)

The audio is the best in the series:
- All 6 beats are in order, and the voice follows the gated script almost word for word.
- All 15 story words come in the script's order. Each has the right meaning and register, and the recap uses exactly the Beat 5 labels.
- The comment line is spoken word for word: "Which score was higher? Comment your two scores. List versus story."
- The transfer line and the anotherwordfor.net line are both there. There is no "examples" promise.
- There are no memory statistics, no "most people", no "always", no "strongest" and no "top/bottom".
- Every story card changes on its word. Picture/voice sync is good.

It cannot ship as it is:
1. **The ladder screen has only 8 of the 15 words** (317.67–392.67, 75 s). picturesque, good-looking, handsome, graceful, radiant, gorgeous and stunning are missing, including 3 of the 5 "sneaky" extras. The voice reads 15 rows while the screen shows 8. This is the summary screen people screenshot.
2. **cute has no picture.** From 38.33 to 70.29 (32 s) a blank yellow card shows "cute" plus its meaning. The first scene of the story (the goat in your camera bag), heard at the exact moment the voice says "pictures instead of a list", is never drawn.
3. **The second pause has no real hold:** 0.78 s of silence after "in order." (298.12 → 298.90), then the tip straight away. The first pause is 2.88 s, which is borderline.
4. **The ending card says "The happy couple takes it home."** (280.67–294.46). The language gate rejected exactly this wording (lang-gate-v1.md, Ending row: "it" is ambiguous, "couple take/takes" confuses B1) and replaced it with "The bride and groom take the goat home.", which is what the voice says (289.74).
5. **"Gemini Notebook" is on every frame, plus a Gemini end card (407.67–410.76).**

All five can be fixed in post. Regeneration is not needed, and the runbook trigger "ask_user about our own renderer" (beats dropped or scrambled twice) does **not** apply: no beat was dropped or scrambled.

## Pain in the learner's words

These quotes are verbatim from /workspace/state/glottos-methods/P01 (proof_doc.md, strategy.md, comments/*.jsonl). Each one was re-grepped in this run. No names are given.
- "I’ve been trying to cram too many words and always forget them."
- "I forget every new word so of this works for me it will be life changing"
- "I reviewed but kept forgetting the words."
- "That's called mnemonics. Really helps you learn languages, specifically vocabulary, where you can associate some bonkers, vivid and chaotic story with a meaning and a pronunciation of a word."
- Score comments on the source method's video: "7 verbal, 15 visual. Just wow!" and "I tried it and it worked, from scoring 4/10 to 10/10."

In one sentence: "I learn words like *exquisite* or *striking*, forget them in days, and when I speak I only say *beautiful* or *very beautiful*."

Solved means that tomorrow:
- I remember more of a word group from a silly story than from a list, and I can prove it with my two scores;
- I say *a picturesque village*, *a breathtaking view*, *a radiant smile*, *exquisite jewellery*, *a handsome man*, and I know *gorgeous* is a bit informal;
- I can build my own silly story for my next word group.

## Beat survival: all present, in order, no spoken cue dropped

| # | Required beat | Heard (whisper, s) | On screen (s) | Result |
|---|---|---|---|---|
| 1 | Hook ≤15 s, two scores | 0.00–10.74 "Ten words for beautiful. How many can you actually remember? Then we're going to try one trick, a single silly story, and test you again. Grab a pen because you're getting two scores today." | 0–11.33 title "Synonyms for Beautiful" (goat drawing). 11.33–15.50 "Grab a pen! Track your list and story scores." | OK: 10.7 s, and "beautiful" is spoken as a word, not spelled out (the S3 lesson worked). Dropped: "You'll also learn when to use each word" (harmless). The "Grab a pen" card comes 2.6 s after the voice. |
| 2 | Plain list of 10, in script order | 11.70 "First up, the plain list. Just read and listen as they appear." 15.98–26.20: exquisite, cute, gorgeous, attractive, lovely, stunning, handsome, pretty, elegant, good-looking. | 15.50–26.96 "The Plain List": all 10 at once, correct order, no pictures and no meanings. **The same 10 words are printed twice** (a bullet list on the left, and again on a scroll in the middle). | OK. The duplicate list is cosmetic (see fix 8). |
| 2b | Spoken pause cue plus a ~3 s hold | 27.04–30.04 "Pause the video now. Write down every word you remember." Silence **30.08–32.95 (2.88 s)**. 32.88 "All done? Count them up. That's your first score. The list score. Keep that handy." | 26.96–38.33 card "Write down every word you remember. Count them for your first score!" | Cue present, and it says "video" (the S3 "explainer" lesson worked). The hold is 2.88 s, just under target. |
| 3 | ONE story, 15 words, script order | Set-up 38.60–58.0 (the photographer in a "bright yellow raincoat"). Word/scene onsets: cute 58.3 (the word at 64.4), pretty 70.5, picturesque 86.3, lovely 97.9, attractive 114.7, good-looking 128.4, handsome 141.2, elegant 158.3, graceful 171.8, exquisite 189.6, striking 207.1, radiant 222.6, gorgeous 237.4, stunning 252.4, breathtaking 266.0. Happy ending 280.8–293.8 ("…take the goat home. Okay, it's only a story."). | Cuts: cute 38.33, pretty 70.29, picturesque 86.04, lovely 99.33, attractive 114.33, good-looking 128.29, handsome 140.67, elegant 157.92, graceful 171.46, exquisite 189.04, striking 207.04, radiant 222.38, gorgeous 237.13, stunning 252.29, breathtaking 265.63, ending card 280.67. | **Exact order, nothing merged or skipped.** Every card lands within 0.4 s of its scene (lovely is 1.4 s late, still fine). Picture defects are covered below. |
| 4 | Second pause "in order" + ~3 s hold | 294.68–298.12 "Pause the video again. Write down every word you can recall in order." 298.90–300.44 "Quick tip, walk through the story again." Silence 300.41–302.53 (2.12 s). 302.26 "Done? Count them up. That's score number two, your story score." | 294.46–306.71 card "Write down every word you can recall in order. Count them for your second score!" (brain + pause icon) | The cue is present, and the card includes "in order". **The hold after the cue is 0.78 s**, and the tip talks through the writing moment. The only real gap (2.12 s) comes after the tip. |
| 5 | "15, not 10" reveal + ladder | 306.76 "I gave you 15 words, not 10. The sneaky extras were picturesque, graceful, striking, radiant, and breathtaking. Did any of those make it onto your list?" 317.96 "Here's the entire ladder on one screen." Then the spoken recap of all 15, in order, with the script's labels (onsets below). | 306.71–317.67 "I gave you fifteen words, not ten! Did the extra five make your list?" (the 5 extras are not written). 317.67–392.67 **one static 2-column table (Word, Meaning) with only 8 rows.** | The voice is correct, with no "came only from the story" claim, and no "top/bottom/strongest". **The screen is not correct** (see On-screen text). The voice drops "roughly … a guide, not a rule" here, but it was said at 47.2 ("a guide, not an exact science"). |
| 6 | Comment CTA, transfer, site | 393.02–396.48 "**Which score was higher? Comment your two scores. List versus story.**" 397.76–402.32 "Tonight, try it with your own new words. One silly story. One picture for each word." 402.84–407.04 "For more words, look up another word for beautiful on anotherwordfor.net" (whisper writes "anotherword4.net", a homophone artefact). | 392.67–397.21 "Which score was higher?" (books, scales, a road). 397.21–407.67 "Try it tonight with your own words! Find more synonyms on anotherwordfor.net." | **All three lines are spoken exactly.** The first card has no "Comment your two scores". There is no promise of a search box or examples. |
| – | End | – | **407.67–410.76 full-screen "Gemini Notebook" end card** (audio silent after 407.04) | Brand violation |

Spoken recap onsets (for the ladder overlay): cute 320.86, pretty 325.28, picturesque 330.92, lovely 335.52, attractive 340.28, good-looking 344.86, handsome 348.96, elegant 353.54, graceful 358.24, exquisite 363.48, striking 368.68, radiant 373.90, gorgeous 377.98, stunning 383.68, breathtaking 387.02 ("And finally, breathtaking"; the word itself at 388.08).

## Accuracy for B1 (acted meaning and register per synonym)

All 15 story scenes act out the right sense, and the voice uses the gated meaning and register:
- **cute**: a baby goat jumps into your camera bag (babies, small animals, small things). Heard only; there is no picture (defect 2).
- **pretty**: the flower girl's pink dress, and the goat eats a daisy ("attractive, but not as strong as beautiful … girls and women, small things").
- **picturesque**: old stone houses, a bridge, mountains, "like a painting" ("pretty, often in an old-fashioned way … places and views").
- **lovely**: grandmother holding the goat, "What a lovely day." The voice says "**incredibly** common in British English" (107.5–113.5) where the script and the card say "very common". This is a mild intensification, not a new claim; the card and the recap (337.5, "Very common") are right.
- **attractive**: the garden tables with white cloths and flowers (neutral, people and things).
- **good-looking**: the twin brothers checking their hair in your lens. The picture shows one man with a magnifying glass, not twins; minor.
- **handsome**: the groom on a white horse, "a handsome man on a handsome horse" (usually men; for a woman, attractive in a strong way; horses and buildings).
- **elegant**: the mother's simple long blue dress and an old car ("attractive and stylish"; no "simple" in the meaning, as the gate required).
- **graceful**: the swan glides, the goat falls in ("moving in a smooth, beautiful way … dancers, swans and cats").
- **exquisite**: tiny flowers on the rings ("very beautiful and delicate, small things made with great care").
- **striking**: the aunt's red hair and huge green hat, every head turns ("very attractive, often in an unusual way").
- **radiant**: the bride glowing ("so happy or healthy that you seem to glow … faces and smiles").
- **gorgeous**: the cake taller than the groom, "That's gorgeous." ("a bit informal").
- **stunning**: the sunset group photo ("extremely beautiful … people, clothes and views"; no register label, as the gate required).
- **breathtaking**: the goat leads everyone up a hill at night, the valley and fireworks ("often for views").

NotebookLM additions that are harmless but slightly odd English (language-editor to decide; none is worth a splice):
- 252.4–256.7: "As the sun sets, you take a group photo that turns the sky orange and pink". Taken literally, the photo turns the sky orange. The script says "The sky turns orange and pink". It is illogical, but a learner still gets the scene.
- 222.6–226: "she literally seems to glow". This is the usual spoken use of "literally", and it teaches nothing wrong.
- "photo bombing" (259), "Panic sets in" (189.6), "in awe" (145): natural spoken English, and above B1 only mildly.

Memory claims: **clean.** There are no statistics, no "most people", no "10x", no researchers, no age of the method, and no "came only from the story" (it asks "Did any of those make it onto your list?"). Nothing claims the words become permanent.

## On-screen text, pictures, watermark

- **cute (38.33–70.29, 32 s): NO picture.** A plain yellow card, "cute" plus "Nice to look at, for babies, small animals and small things.", on a faded background with ghost words. The set-up (wedding, photographer, yellow raincoat, mountain station) and the goat in the camera bag are heard over it, but nothing is drawn. It is the only one of the 15 without a picture, and it is the first image of the "pictures instead of a list" promise.
- The other 14 story cards all have the word, a correct one-line meaning that uses the voice's register words, and a matching drawing with the goat. This is a clear improvement on S3 v1.
- Caption obstructions (readable, cosmetic): attractive (114.33–128.29), where a vase of flowers covers "for p[e]ople"; breathtaking (265.63–280.67), where the hill edge clips the "o" of "often"; exquisite (189.04–207.04), where the ring box overlaps "great care".
- handsome card: "Good-looking. Usually for men. Also for horses and buildings." It leaves out "for a woman, attractive in a strong way" (spoken at 150.5), but it does not contradict the voice.
- **Ending card (280.67–294.46): text only, "The best photo of the day is the goat! The happy couple takes it home."** This is the gate-rejected wording, and it disagrees with the voice ("The bride and groom take the goat home."). There is also no drawing of the best photo (the goat with the flowers).
- The protagonist "you in a bright yellow raincoat" is spoken (58.3) but never drawn. The goat carries continuity in every scene, so this is minor (same as S3).
- **Pause 2 card (294.46–306.71):** it includes "in order". OK.
- **Reveal card (306.71–317.67):** "I gave you fifteen words, not ten! Did the extra five make your list?" It is correct, but the 5 extras are not written, while the voice names them at 309.0–315.2.
- **Ladder (317.67–392.67, 75 s):** a 2-column table (Word | Meaning) with only these **8 rows: cute "nice to look at", pretty "attractive", lovely "beautiful & pleasant", attractive "pleasant to look at", elegant "attractive & stylish", exquisite "beautiful & delicate", striking "very attractive", breathtaking "takes breath away"**.
  - **7 words are missing:** picturesque, good-looking, handsome, graceful, radiant, gorgeous, stunning. That includes 3 of the 5 extras the reveal just named.
  - There is no "when to use" column and no heading.
  - "pretty = attractive" drops "not as strong as beautiful". That is weaker than the voice, but not false.
  - The faded background has decorative ghost words, including a **misspelt "STOQUINING"** (about x 70–185, y 290–320). A vocabulary video should not show a misspelling, even a faint one.
  - For 75 s the learner hears rows that are not on the screen. Anyone who screenshots "the whole ladder" gets half of it.
- **CTA cards:** "Which score was higher?" (392.67–397.21) has no "Comment your two scores: list vs story". "Try it tonight with your own words! Find more synonyms on anotherwordfor.net." (397.21–407.67) is correct and promises no examples.
- **Watermark: "Gemini Notebook" in the bottom-right corner of EVERY frame** (about x 1150–1280, y 695–715), plus the **full-screen Gemini end card from 407.67 to 410.76**.

## Second by second: where a viewer would swipe away

- 0:00–0:04: "Ten words for beautiful. How many can you actually remember?" It is my problem as a question, so I stop. There is no spelled-out word this time.
- 0:04–0:15: the promise and "grab a pen". The title card is static for 11 s: fine for a 16:9 video people click on purpose, weak as a scroll-stopper.
- 0:16–0:27: the list, readable. It is printed twice, which is a small "wait, are there 20?" moment.
- 0:27–0:33: the pause cue plus 2.9 s of silence. Just enough if I press pause, too short if I don't.
- **0:38–1:10: 32 s on a blank yellow "cute" card** while the voice sets up the story. This is the most likely swipe in the video: the voice has just promised "pictures instead of a list", and the screen shows none.
- 1:10–4:40: the story. It is funny and concrete (the goat eats the flower girl's daisy, holds the car door, falls in the lake, has the rings in its mouth, tries to eat the aunt's hat, photobombs the sunset photo), with a new drawing every 13–18 s and good sync. It holds.
- 4:41–4:54: the ending is a text-only card. It is a flat moment after 14 drawings.
- **4:55–5:02: the second pause has no hold.** The tip talks over the moment when I should be writing, so score 2, the whole point of the video, is shaky.
- 5:07–5:17: the reveal, the "aha" moment. The voice names the 5 extras; the screen does not.
- **5:18–6:32: 75 s on a static half-empty table.** The voice reads picturesque, good-looking, handsome, graceful, radiant, gorgeous and stunning, and I can't find them on screen. This is the second swipe zone, and it is a trust hit ("did I miss something?").
- 6:33–6:47: comment the scores, try it tonight, the site. All spoken. OK.
- 6:47–6:51: the Gemini end card.

## Takeaway test

Tonight: take my own new word group, make one silly story with one picture per word, then comment "list X / story Y". Both actions are spoken (393.0, 397.8). The "try it tonight" action is also on screen, and the "comment" action is only heard. I also leave knowing *a picturesque village*, *exquisite jewellery*, *a radiant smile*, *a breathtaking view*, *a handsome man on a handsome horse*, and that *gorgeous* is a bit informal. That is a real action for the P01 pain, so the verdict is not capped by the takeaway test. It is capped by the broken ladder and the missing cute picture, which break the method's own promise on screen.

## Retention risks

- Length is 6:51 (6:47 after trimming the end card, about 6:53 with the pause freezes). That is inside the 5–7 min target, and the shortest in the series so far.
- Pacing: the story runs at about 13–18 s per word and is steady. The drags are the 32 s blank cute card and the 75 s static half-table.
- Legibility: the story captions are large and readable at 720p, apart from 3 small overlaps. The ladder rows are readable but small.
- Sync: good. Every story card lands on its scene, the pause and reveal cards land on the voice, and the CTA cards land on the voice.

## Trust risks

- The ladder contradicts the voice by omission (8 rows on screen, 15 spoken).
- The ending card uses gate-rejected wording and disagrees with the voice.
- "STOQUINING" is a faint misspelling in the ladder background.
- "incredibly common in British English" is spoken once (the card says "very common").
- The Gemini watermark and end card break the brand rule.
- There are no memory statistics and no false claims about the method.

## Defects and fixes (all in post; no regeneration)

### Ship-blocking

1. **Watermark and end card (shorts-builder).** Trim at **407.3 s** (the CTA audio ends at 407.04, and the end card starts at 407.67). Cover the bottom-right "Gemini Notebook" mark (about x 1150–1280, y 690–720) on every frame with the channel logo `state/brand/awf-logo-channel.jpg` or a background-matched patch.
2. **Ladder, 317.67–392.67 (visuals, then shorts-builder, then a language-editor re-gate).** Overlay our own **15-row, single-column** ladder, one row per word, no pairs, cute first and breathtaking last, heading "nice to look at → extremely beautiful", with word · meaning · when to use, using exactly the script's Beat 5 labels. Mark the 5 extras. The overlay must also cover the "STOQUINING" ghost text (or cover the full frame). Reuse the S3 polish builder with a row highlight on the voice: cute 320.86, pretty 325.28, picturesque 330.92, lovely 335.52, attractive 340.28, good-looking 344.86, handsome 348.96, elegant 353.54, graceful 358.24, exquisite 363.48, striking 368.68, radiant 373.90, gorgeous 377.98, stunning 383.68, breathtaking 387.02.
3. **cute picture, 38.33–70.29 (visuals, then shorts-builder).** Draw one whiteboard/watercolour panel in the series style: a tiny mountain railway station, you (yellow raincoat, green wellies, big camera round the neck), and the baby goat's head and big eyes peeking out of your open camera bag. Place it in the empty upper area of the yellow card (about x 100–930, y 125–395; the word and meaning sit below y 400, and the magnifier is at x 920–1060). Show it from 38.33, or at least from 52.7 ("So picture this"), to 70.29.
4. **Pause holds (shorts-builder).** Insert a silent **3 s freeze** of the pause 2 card at **298.15 s** (straight after "in order.", before "Quick tip"). For consistency with S3 v2, also insert a **2–3 s freeze** of the pause 1 card at **30.10 s** (inside the existing 2.88 s silence, for about 5–6 s in total). This adds about 5–6 s.
5. **Ending card text, 280.67–294.46 (shorts-builder, then a language-editor re-gate).** Patch "The happy couple takes it home." with "**The bride and groom take the goat home.**" (the gate's wording, and what the voice says at 291.0). Keep "The best photo of the day is the goat!"

### Recommended (in post)

6. **Reveal card, 306.71–317.67 (shorts-builder).** Add the extras as chips, "picturesque · graceful · striking · radiant · breathtaking", from **309.0** (spoken at 309.0–315.2).
7. **CTA cards (shorts-builder).** Overlay "Comment your two scores: list vs story" on the "Which score was higher?" card from **393.0** to 397.2. Optionally add "Look up: another word for beautiful" from 402.84 on the second card. Pin a comment "List: __ / Story: __ ?" at publish (publisher).
8. **Plain list, 15.50–26.96 (shorts-builder).** Cover the duplicate copy of the list (the scroll in the middle, about x 470–700, y 180–590) with blank parchment, or cover the left bullet list, so that 10 words are shown once.
9. **Caption overlaps (shorts-builder, optional).** Re-letter the meaning lines of attractive (114.33–128.29), breathtaking (265.63–280.67) and exquisite (189.04–207.04) above the drawings, with identical text.
10. **Audio (language-editor decides; do not splice unless asked).** "incredibly common in British English" (≈109–113.5; the card and recap say "very common"), and "you take a group photo that turns the sky orange and pink" (252.4–256.7). Both are understandable, and neither teaches a wrong meaning.
11. **For S5 (scenario-writer, focus.txt).** The S3 lessons worked: the word was spoken not spelled, "pause the video", "in order" was on the card, 14 of 15 pictures, and captions in the voice's register. Add: "The ladder screen MUST list all 15 words, one row each — never a shortened table", "Draw the first scene (not just a card)", and "Stay silent for 3 seconds right after the second pause cue, BEFORE the tip". Plan the pause freezes and a ladder overlay in polish anyway (this is the fourth video with short holds, and NotebookLM keeps shortening the table).

After fixes 1 to 5 (ideally with 6 and 7), this should reach **SOLVES**. Re-run the critic on the polished file.

## Not checked

- No human listening. The headwords were checked only by whisper small.en (all 15 transcribed correctly). "anotherword4.net" is assumed to be a homophone artefact of "anotherwordfor.net".
- Frames were sampled every 5 s, plus both scene-cut lists and about 35 targeted frames. A defect lasting less than about 3 s between samples could be missed.
- meta.json was not re-audited (it was gated). As with S3, the title "Can You Remember 15 Synonyms for BEAUTIFUL?" slightly spoils the "15, not 10" reveal.
- The anotherwordfor.net SSL status was not re-checked (the gate recorded the certificate as expired).
