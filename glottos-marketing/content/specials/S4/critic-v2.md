# S4 critic review, s4-v2.mp4 (Synonym Memory Challenge: BEAUTIFUL, P01, 16:9, polish round 1, 6:53)

Reviewer: glottos viewer-critic (headless autopilot step "special S4: critic"), 2026-09-29.
File checked: content/specials/S4/s4-v2.mp4, sha256 2bdbc85d…510d, 1280x720, 24 fps, AAC mono 44.1 kHz, 413.29 s.
Watched as: a B1 to B2 learner who forgets new words within days and only ever says "beautiful" or "very beautiful".

Method:
- 2 contact sheets (a frame every 5 s, 83 frames).
- Full-resolution frames at 0.7, 1.5, 30.0, 33, 36, 41.3, 50, 60, 73.2, 286, 293, 300, 303, 306, 312, 319, 321, 327, 391, 395, 396.5, 398, 400, 405, 410, 412, 413.2 s and the last frame.
- Boundary frames around the cute panel (41.2/41.4, 76.2/76.4); a 24-frame strip of 412.3–413.29 s (end-card trim).
- Bottom-right corner crops at 5, 100, 180, 293, 319, 400 s, plus a pixel-zoom v1 vs v2 of the watermark area.
- Ladder highlight crops at 331.6, 351.2, 365.0, 380.3, 384.3, 389.2, 393.4 s against whisper word onsets.
- ffmpeg silencedetect (-35 dB, 0.7 s) over the whole file.
- Full faster-whisper small.en transcript (int8, cpu_threads=4, word timings).
References: script.md, meta.json, critic-v1.md, lang-gate-v2-polish.md, polish-v2-build/plan.py, docs/autopilot.md (Specials, S1–S5), S3 critic-v2.md (format), /workspace/state/glottos-methods/P01 (strategy.md, proof_doc.md, comments; quotes re-grepped this run).
NotebookLM was not touched. Nothing was rendered, uploaded or changed. Working files: /tmp/s4c2 (outside the repo).

Time map: v2 = v1 + 3.0 s after 30.10, + 6.0 s after 298.15 (two 72-frame freezes); cut at v1 407.3.

## Verdict: SOLVES. No ship-blocking defect remains.

All 5 v1 ship-blockers are fixed and verified on frames and audio. Both recommended on-screen fixes (reveal chips, comment plate) are also in. The challenge runs cleanly: list → pause (5.9 s silence) → story (15 pictures) → pause (3.7 s silence) → "15, not 10" with the extras written → a complete 15-row ladder synced to the voice → "Comment your two scores: list vs story" on screen and in the voice. What remains is cosmetic: a flat clip-art cute panel in a watercolour video, a faint grey smear next to the logo, a duplicate plain list, one highlight 0.8 s late, and two NotebookLM audio quirks.

## v1 ship-blockers: status in v2

| # | v1 defect | v2 evidence | Status |
|---|---|---|---|
| 1 | "Gemini Notebook" on every frame + Gemini end card 407.67–410.76 | Channel logo (AnotherWordFor avatar) sits at bottom right on every sampled frame (83 sheet frames + 6 corner crops). The v1 pixel zoom shows "Gemini Notebook" in that spot; in v2 no letters are legible. The file ends at 413.29 on a fade-to-dark of our own "Try it tonight … anotherwordfor.net" card; the 24-frame tail strip and the last frame show no Gemini logo or end card. | FIXED. A residue remains: a soft grey gradient smear, about x 1148–1225, y 695–718, left of the logo. It is visible on flat grid backgrounds (e.g. 293, 319, 400 s). Cosmetic. |
| 2 | Ladder showed 8 of 15 words, "STOQUINING" in the background | 323.67–398.67 (v2): our own full-frame table "The ladder: nice to look at → extremely beautiful", "The order is a guide, not a rule.", columns WORD / MEANING / WHEN TO USE IT, **all 15 rows** cute → breathtaking, orange dots on the 5 extras, footer "Read downward…" + legend. Every cell matches the spoken recap. Full-frame, so "STOQUINING" is gone. Row highlight follows the voice: 14 of 15 rows light up 0.0–0.35 s before the spoken headword (a good lead); **stunning is 0.84 s late** (highlight 389.58, voice 388.74). | FIXED. Readable at 720p (rows about 17 px text, meaning column smaller but legible full-screen). |
| 3 | cute had no picture (38.33–70.29) | 41.33–76.29 (v2): a panel on the yellow card showing a mountain station ("STATION" sign, house), two mountains, "you" in a yellow raincoat with green wellies and a camera, and a small white goat head peeking out of a brown bag. Clean cuts in at 41.3 and out at 76.3 (pretty). It matches the setup the voice tells (57.5–67.0). | FIXED. Weakness: flat vector clip-art in an otherwise watercolour video. The goat (pointed ears, no horns) reads as a cat or fox, the bag reads as a cardboard box, and the yellow raincoat is low-contrast on the yellow card. Not wrong, just the weakest picture. |
| 4 | Pause 2 had a 0.78 s hold; pause 1 was 2.88 s | Pause 1: silence **30.08–35.95 (5.88 s)** on the "Write down every word you remember…" card. Pause 2: "Write down every word you can recall in order." ends 301.12, silence **301.18–304.86 (3.68 s)** on the pause-2 card, then "Quick tip…". No visual glitch at either freeze. | FIXED |
| 5 | Ending card said "The happy couple takes it home." | 283.67–297.46 (v2): "The best photo of the day is the goat! The bride and groom take the goat home." Voice at 293.80: "The bride and groom take the goat home." | FIXED. The patched box has a slightly lighter rectangle behind the text (grid lines fainter), only visible if you look for it. |

Recommended v1 fixes:
- 6 Reveal chips: DONE. "picturesque · graceful · striking · radiant · breathtaking" (orange chips) under the reveal card from 315.0 (v2); voice names them 315.66–321.16. No overlap with the box or the sparkles.
- 7 Comment plate: DONE. "Comment your two scores: / list vs story" plate at the top of the "Which score was higher?" card from 399.0 to 403.2; voice 399.12–402.48. It overlaps only the decorative word cards at top right.
- 8 Duplicate plain list (15.50–26.96): NOT done. The 10 words still appear twice (bullets left + scroll). Cosmetic.
- 9 Caption overlaps (attractive, exquisite, breathtaking): NOT done. Still readable.
- 10 Audio quirks: unchanged (no splice was asked). "It's incredibly common in British English" (114.70; card and recap say "very common") and "you take a group photo that turns the sky orange and pink" (255.74).

## Challenge beats (v2 times)

| # | Beat | Heard | On screen | Result |
|---|---|---|---|---|
| 1 | Hook ≤15 s | 0.00–10.74 "Ten words for beautiful. How many can you actually remember? … two scores today." | Title "Synonyms for Beautiful" + goat, then "Grab a pen! Track your list and story scores." | OK |
| 2 | Plain list of 10 | 15.98–26.22, script order | "The Plain List", 10 words (shown twice) | OK |
| 2b | Pause 1 | 27.00–30.06 "Pause the video now. Write down every word you remember." + 5.88 s silence | pause-1 card | OK |
| 3 | One story, 15 words in order | cute 67.4 … breathtaking 278.0, ending 284.0–296.8 | 15 word cards, each with a matching picture (cute now drawn) | OK |
| 4 | Pause 2 "in order" | 297.90–301.12 + 3.68 s silence, then the tip | pause-2 card, includes "in order" | OK |
| 5 | 15-not-10 reveal + ladder | 313.10 "I gave you 15 words, not 10." extras 315.66–321.16; recap 323.98–397.44 | reveal card + extra chips; full 15-row ladder with synced highlight | OK |
| 6 | Comment CTA, transfer, site | 399.12 "Which score was higher? Comment your two scores. List versus story." 403.76 "Tonight, try it with your own new words…" 408.82 "…another word for beautiful on anotherwordfor.net." (whisper hears the domain correctly this time) | "Comment your two scores: list vs story" plate; "Try it tonight with your own words! Find more synonyms on anotherwordfor.net." | OK. No "examples" promise. |

## Pain in the learner's words (verbatim, re-grepped in /workspace/state/glottos-methods/P01, no names)

- "I’ve been trying to cram too many words and always forget them."
- "I forget every new word so of this works for me it will be life changing"
- "I reviewed but kept forgetting the words."
- "…you can associate some bonkers, vivid and chaotic story with a meaning and a pronunciation of a word."
- Score comments on the source method's video: "7 verbal, 15 visual. Just wow!" / "I tried it and it worked, from scoring 4/10 to 10/10."

One sentence: "I learn words like *exquisite* or *striking*, forget them in days, and when I speak I only say *beautiful*."
Solved means tomorrow I (a) have my own two scores proving story beats list, (b) say *a picturesque village*, *a radiant smile*, *a breathtaking view*, *a handsome man*, and know *gorgeous* is a bit informal, (c) can build a silly story for my next word group.

What the video gives: all three. The story is funny and concrete (the goat eats the daisy, holds the car door, falls in the lake, has the rings, tries to eat the aunt's hat, photobombs the sunset). Each word shows meaning + when to use it on its card, and the ladder is now a complete screenshot-able summary. Gap: none that blocks. The "for a woman, handsome = attractive in a strong way" nuance is spoken (153.6) but not on the ladder; fine.

## Accuracy for B1

Audio is unchanged from v1 and was verified there: all 15 scenes act out the right sense, and the register labels match the gate (gorgeous "a bit informal", stunning with no register label, jubilant-style overclaims absent). The new ladder cells repeat the gated Beat 5 labels verbatim (checked row by row on the 327 s frame). No memory statistics, no "most people", no "top/bottom/strongest"; the reveal asks "Did any of those make it onto your list?" rather than claiming anything.

## On-screen text spelling

Checked on full-res frames: title, list, both pause cards, all 15 word cards, ending card, reveal card + chips, the full ladder (heading, note, headers, 45 cells, footer, legend), comment plate, final card. No misspellings. Background ghost words on the cute card (GORGEOUS, STUNNING, STRIKING, EXQUISITE) are spelled correctly. The CTA card's decorative word cards read "stunning", "radiant", "exquisite", "captivating": correct words, left as decoration (as in S3).

## Second by second: where a viewer would swipe

- 0:00–0:11: my problem as a question, I stop. The title card is static but short.
- 0:16–0:27: the list; the duplicate copy is a small "20 words?" moment.
- 0:27–0:36: pause with real silence. Good.
- 0:41–1:16: the cute card now has a picture of the setup; still 35 s on one card while the story is set up, and the flat drawing looks cheaper than everything after it. Mildest swipe risk left.
- 1:16–4:57: the story holds: a new watercolour card every 13–18 s, in sync.
- 4:57–5:12: pause 2 with 3.7 s of silence before the tip. Good enough; a viewer who wants more time presses pause (the voice tells them to).
- 5:13–5:23: the reveal with the 5 extras written: the "aha".
- 5:24–6:39: 75 s ladder. It is now complete and the moving highlight gives the eye something to follow; long, but it is the summary a learner screenshots.
- 6:39–6:53: comment, try tonight, the site; fade out. No Gemini card.

## Takeaway test

Tonight: take my own new word group, make one silly story with one picture per word, and comment "list X / story Y". Both are spoken and now both are on screen. Plus concrete collocations: *a picturesque village*, *exquisite rings*, *a radiant bride*, *a breathtaking view*, *a handsome man on a handsome horse*. Passes.

## Retention risks

- Length 6:53, inside 5–7 min. Pacing steady in the story; the two long holds are the cute setup card (35 s) and the ladder (75 s), both now with content.
- Legibility: story captions large; ladder rows small but readable full-screen at 720p, tight on a phone in portrait.
- Sync: story cards on their scenes; ladder highlight 0–0.35 s ahead of the voice except stunning (0.84 s late).

## Trust risks

- None blocking. Minor: the grey smear left of the logo (reads as a smudge, not as a brand), "incredibly common in British English" (spoken once, the card says "very common"), "a group photo that turns the sky orange and pink" (illogical, harmless).
- meta.json title "Can You Remember 15 Synonyms for BEAUTIFUL?" still pre-spoils the "15, not 10" reveal (same as S3; not a defect of this file).

## Remaining fixes (none ship-blocking), by impact

1. **Cute panel style (visuals, then shorts-builder), optional for S4, lesson for S5.** Redraw in the series watercolour style with an unmistakable baby goat (small horns/beard, goat face) in a real camera bag, and a non-yellow outline on the raincoat. For S5 put "Draw the first scene" in focus.txt so NotebookLM draws it.
2. **Watermark cover residue (shorts-builder).** Replace the grey gradient patch left of the logo (about x 1145–1225, y 690–720) with a background-matched fill or widen the logo plate; apply to the logo.py used for S5 too.
3. **Small polish (shorts-builder).** Move the stunning highlight to 388.6 s (v2); cover the duplicate plain list (15.5–27.0); optionally re-letter the three overlapped captions. None needed to ship.

Ship: yes, to studio / yt_meta_gate / PRIVATE upload.

## Not checked

- No human listening; headwords checked by whisper small.en only (all 15 correct in story and recap).
- Frames sampled every 5 s plus about 45 targeted frames; a defect shorter than about 3 s between samples could be missed (the overlay windows and both freezes were checked at their edges).
- The PROBLEM 01 NotebookLM source and the P01 article were not re-read this round (no quota spent); pain quotes come from the P01 evidence files and were re-grepped.
- anotherwordfor.net SSL status not re-checked (known expired certificate, postponed P0).
