# S1 critic review, s1-v3.mp4 (Synonym Memory Challenge: HAPPY, P01, 16:9, 6:55.8)

Reviewer: glottos viewer-critic (headless autopilot step "special S1: critic" on the polished file), 2026-09-28.
Watched as: a B1 to B2 learner who forgets new words and only says "happy" when speaking.
Input: `content/specials/S1/s1-v3.mp4` (1280x720, 24 fps, AAC mono, 415.83 s). References: script.md, focus.txt, meta.json, critic-v1.md, polish-v2.md, polish-v3.md, lang-gate-v3.md, docs/autopilot.md ("Specials" and "S1–S5"), /workspace/state/glottos-methods/P01/strategy.md + proof_doc.md.
Method: faster-whisper small.en (int8, cpu_threads=4, word timings) on the full v3 audio; ffmpeg silencedetect (-40 dB, 0.4 s) over the whole file; 3 labelled contact sheets (54 frames: hook, list, both pause holds, the 52.9 s join ±0.5 s, the stress cue, one frame per story word, extras card, 9 ladder frames, CTA, fade); a full-res ladder frame; bottom-right crops at 14 times from 0.5 to 415.5 s; a pixel scan of the yellow ladder highlight at 19 times from 344.8 to 408.2 s, matched against whisper word starts; an energy/pitch contour of every spoken "content". NotebookLM was not touched. Nothing was rendered, uploaded or changed.

## Verdict: SOLVES. No ship-blocking defect.

All three v1 ship-blockers are fixed. The ladder is now correct and in sync with the voice. The pause holds are real (3.9 s and 3.5 s). There is no Gemini mark and no end card. All six challenge beats are there, in order. A B1 viewer finishes with two scores of their own and a correct, readable map of which HAPPY word to use where. The remaining issues (two scenes without pictures, recap-voice overstatements, the method never handed over for "your own words") make the video weaker, but they do not make it wrong. It may go on to **studio**.

## Pain in the learner's words (verbatim, P01 research, no names)

- "I've been trying to cram too many words and always forget them." (proof.json)
- "I forget every new word so of this works for me it will be life changing" (proof_doc.md)
- "I also find myself forgetting certain English words when I'm speaking." (proof_doc.md)
- "I reviewed but kept forgetting the words." (proof_doc.md)
- On the source method: "7 verbal, 15 visual. Just wow!" (strategy.md) and "I tried it and it worked, from scoring 4/10 to 10/10." (proof_doc.md)

In one sentence: "I learn words like *elated* or *thrilled*, forget them in days, and when I speak I only say *happy*."
Solved means that tomorrow I recall more of these words than I would from a list, and I pick the right one: *delighted* in an email, *chuffed* only with friends, *jubilant* when I read the news.

## 1. v1 ship-blockers: all FIXED

| v1 defect | v3 evidence | Status |
|---|---|---|
| Wrong ladder table | 344.92 to 408.12 s: our own "The HAPPY ladder" table. It has **15 unique rows**, top to bottom Ecstatic, Jubilant, Elated, On cloud nine, Overjoyed, Over the moon, Thrilled, Delighted, Joyful, Upbeat, Cheerful, Chuffed, Pleased, Glad, Content (Content at the bottom, which is the script's mildest-to-strongest order, and the footer says "Read it from the bottom up"). There are no pairs, no duplicate Elated, and no "Uncontained"/"Joyous". **Every cell is filled** (word, meaning, when to use it). All rows are legible at 720p (full-res frame at 380 s), and the title is not clipped. | FIXED |
| Pause holds too short | Silence after "…every word you remember." is 28.08 to 31.94 = **3.85 s**, on the pause card. After "…recall in order." it is 310.96 to 314.44 = **3.48 s**, on the pause card. v1 had 0.9 s and 0.5 s. | FIXED (it meets the script's 3 s) |
| "Gemini Notebook" watermark + end card | Bottom-right crops at 0.5, 5, 20, 30, 60, 120, 180, 240, 300, 313, 330, 380, 412, 415.5 s all show the channel logo tile and no "Gemini Notebook" text. The last frames (415.6, 415.75) are the CTA card fading to black. There is **no end card**. | FIXED |

## 2. Challenge beats: all present, IN ORDER

| # | Beat | Heard (v3 whisper) | On screen | OK |
|---|---|---|---|---|
| 1 | Hook ≤15 s | 0.00 to 10.86 "10 words for happy. How many can you actually remember? … two scores today, so grab a pen." | Title card "Synonym Challenge: HAPPY" | Yes, 10.9 s |
| 2 | Plain list of 10 | 11.42 "Ready?" then 12.72 to 24.24 delighted, glad, ecstatic, pleased, thrilled, content, overjoyed, cheerful, elated, over the moon (the script's order) | The 10 words in bubbles, with no meanings | Yes |
| 2b | Pause cue + hold | 25.34 "Pause the video now. Write down every word you remember." then a 3.85 s hold, then 31.60 "Okay, got him[=them]? … your list score." | Pause card | Yes |
| 3 | Story, 15 words, mildest to strongest | content 52.28, glad 66.3, pleased 84.0, chuffed 100.8, cheerful 120.2, upbeat 135.8, joyful 152.2, delighted 170.6, thrilled 189.3, over the moon 206.9, overjoyed 225.9, on cloud nine 241.5, elated 260.0, jubilant 274.1, ecstatic 291.1 | One scene card per word, each changing within about 0.3 s of the word | Yes. Exact script order, nothing merged or skipped |
| 4 | Second pause "in order" | 307.46 "Pause the video again, write down every word you can recall in order." then a 3.48 s hold | Pause card | Yes |
| 5 | Reveal 15 not 10 + ladder | 328.94 "I gave you 15 words, not 10. The extras were chuffed, upbeat, joyful, on cloud nine and jubilant." then 345.16 to 407.94 recap of all 15 | "The sneaky extras were:" card (the correct 5), then the ladder | Yes |
| 6 | Comment prompt + site | 408.42 "Comment your two scores. List versus story. For more words, look up another word for happy on anotherwordfor.net." (ends 415.22) | "Share your two scores! For more, look up another word for happy on anotherwordfor.net." | Yes. No promise of examples or a search box, and the dangling "So what does this all mean…" is gone |

Beats dropped or scrambled: **none**. The runbook's own-renderer trigger does not apply.

## 3. Polish edits

- **Drill cut join (~52.9 s): clean.** Heard: "First up, content.[52.28-52.50] | You're[53.60] lying down in a hammock…". The silence between them is 52.63 to 53.70 (1.07 s), which sounds like a natural beat. No clipped word and no fragment of "Say it with me". Frames at 52.5, 52.85, 53.0 and 53.3 show the same hammock zoom, with no visible jump.
- **con-TENT cue: legible.** It is visible at 52.5 to 65.5 s ("con-" white, "TENT" yellow, on a dark plate) and absent at 51.5 and 66.5. It sits right of the caption and above the "Quietly satisfied" line. It is small, but readable at 720p. Caveat (non-blocking, trust): polish-v2 measured the voice saying noun-stress CON-tent on "First up, content." The drill is gone, but that one spoken instance (and "That is content." at 63.2) may still contradict the cue. My contour is inconclusive for 52.3 and 63.2 because the whisper word boundaries are loose there. The list instance at 18.7 has a louder, higher second syllable (≈-11 dB/≈200 Hz vs -16 dB/113 Hz), which is con-TENT. The screen teaches the right stress, so a learner is steered correctly.
- **Ladder highlight vs voice: in sync.** Pixel scan (row = yellow band) against whisper word starts: content 351.5 ✓, glad 354.5 ✓, pleased 359.3 ✓, chuffed 363.7 ✓, cheerful 367.7 ✓, joyful 374.1 ✓, delighted 378.2 ✓, thrilled 382.2 ✓, over the moon 387.0 ✓, on cloud nine 389.0 ✓, overjoyed 392.2 ✓, elated 396.3 ✓, jubilant 399.6 ✓, ecstatic 404.0 ✓ (lit from "And right at the top" at 403.9). At 370.0 the highlight is still on Cheerful while "Upbeat" starts at ≈369.7 (≈0.3 s late, not noticeable). Before 344.92 and after 408.12 no highlight shows. Because the voice reads the two idioms before overjoyed, the highlight jumps Thrilled → Over the moon → On cloud nine → back down to Overjoyed → Elated. That is honest to the voice, and only a sharp-eyed viewer would notice.
- **A/V sync:** every story scene card changes within about 0.3 s of its word (e.g. the glad scene is in at 65.96, "Next is glad" at 66.26). The CTA voice ends at 415.22, before the fade (415.35 to 415.83), so no word is clipped at the end.
- The hook's title card (0 to 11.4 s) still carries the soft blue delogo smear noted in polish-v2 (no text). This is cosmetic.

## 4. Accuracy for B1

- Story meanings (voice + cards): all correct and B1-appropriate. content "quietly satisfied"; glad "about one particular thing, often with relief"; pleased "happy and satisfied with how something turned out"; chuffed "British and informal … pleased, especially about something you pulled off yourself"; cheerful "happy in a way everyone can see and hear"; upbeat "positive and hopeful even when something goes wrong"; joyful "full of joy … music, celebrations"; delighted "very pleased … gift, invitation, good news"; thrilled "very happy and very excited"; over the moon "informal idiom, extremely happy, usually about good news"; overjoyed "extremely happy about news or an event"; on cloud nine "informal … extremely happy, like floating" (the invented "for a long time" sense has not come back); elated "extremely happy and excited, usually after a big success"; jubilant "very happy and celebrating after a big win"; ecstatic "so intensely happy you can hardly contain it".
- Ladder table: matches script.md Beat 5 and lang-gate-v3 (Glad = "often relieved"). Registers are correct: chuffed British/informal, both idioms informal, jubilant mostly written, elated more common in writing, delighted polite/safe in emails, pleased neutral/work.
- Recap voice overstatements (non-blocking; the table on screen carries the accurate labels): "Joyful is **heavily** used in writing" (374.0), "Jubilant is **almost entirely** written" (399.5), "both **very** informal" (389), "Chuffed … for when you're proud of yourself" (narrowed), "Thrilled is **awesome** for everyday speech" (casual, fine).
- Memory claims: clean. There are no statistics, no "most people", no "10x", no researchers. One soft overclaim: "If you wrote down any of those five, they came entirely from that visual story trick" (337.7). A viewer may already have known *joyful* or *upbeat*. It is minor and not a statistic.
- Ear-check leftovers (whisper only): "Okay, got him?" at 31.6 (likely "got 'em"); "You pass your exam" at 215.3 (the card says "You passed your exam!", and polish-v2's medium.en heard "passed").

## Second by second: where a viewer would swipe away

- 0:00 to 0:11: the audio hook is personal and fast. The picture is a static title card. It is acceptable for 16:9 search/browse traffic.
- 0:11 to 0:25: the list is quick and clean. **Good.**
- 0:25 to 0:32: the pause card with a 3.9 s hold. Anyone who didn't pause now at least gets a visible breath. **Fixed.**
- 0:38 to 0:51: 13 s of set-up (down from 20 s in v1). Acceptable.
- 0:51 to 5:07: the story at about 15 to 19 s per word, and the funny continuity carries it. **Weak spots: cheerful (2:00 to 2:15) and thrilled (3:09 to 3:26) are blank blue caption cards with no drawing**, in a video whose whole promise is "pictures instead of a list". These are the likeliest mid-video drop points.
- 5:07 to 5:14: second pause with a 3.5 s hold. Good.
- 5:26 to 5:44: the "15, not 10" reveal is the aha moment. Strong.
- 5:45 to 6:48: 63 s on one table. It is now correct and has the karaoke highlight, so it is watchable and very screenshot-worthy. It is still the slowest stretch.
- 6:48 to 6:56: the CTA, then a clean fade.

## Takeaway test

Tomorrow I can (a) compare my two scores and comment them, (b) write *delighted* in a polite email, keep *chuffed* and *over the moon* for friends, and recognise *jubilant* and *elated* in the news, (c) screenshot the ladder. That is a real, nameable action, so it passes. **Gap:** the video never says "do this with your own new words tomorrow". The method transfer to the P01 pain ("I forget every new word") is only implied. It is non-blocking for S1. It should be written into S2 to S5.

## Retention risks

- Length 6:56 fits the 5 to 7 min target. The pacing is steady, and the 0.9x voice is fine for B1.
- The two blank scene cards and the 63 s static table are the slow spots.
- Legibility: the ladder text is small (meaning 21 px, register 19 px at 720p). It is fine on desktop and tight on a phone in 16:9. The low-contrast NotebookLM captions from v1 remain (white "content" caption on the light hammock picture, the cloud over the on cloud nine definition), and they are readable.

## Trust risks

- A possible voice/screen mismatch on "content" stress (see above). Only a careful listener would catch it.
- The recap voice's register overstatements, which the correct table offsets.
- Nothing is factually wrong on screen.

## Ship-blocking defects: NONE

## Non-blocking fixes, by impact

1. **Draw the missing cheerful and thrilled scenes** (visuals → shorts-builder). Add a panel beside the blue card at 120.2 to 135.8 s (whistling walker waving at a lamppost) and at 189.3 to 206.1 s (jumping and punching the air, holding the rocket ticket). This strengthens the core method, and it is worth doing if a polish round is ever reopened. It is not required to ship.
2. **For S2 to S5: add the transfer line and tighten the recap** (scenario-writer, language-editor). In focus.txt add "Tell the viewer: tonight, make one silly story for your own new words" before the CTA. Also add "Recap: use exactly the Beat 5 labels (more common in writing / mostly written), no 'heavily', 'almost entirely', 'very informal'", and "Do not say the extras 'came entirely from' the story".
3. **Ear check "content" stress at 52.3 and 63.2 and "got him" at 31.6** (voice, human listen). If CON-tent is confirmed and ever bothers viewers, re-voice the one word "content." at 52.28. The screen cue already teaches the right stress, so this does not block.

## Not checked

- No human listening. Stress and the ear-check words are whisper plus the energy/pitch contour only.
- Frames were sampled (about 54 frames plus 14 corner crops plus 19 highlight probes), not every frame. A sub-3 s defect between samples could be missed. The watermark area is a static delogo+logo overlay, so full coverage is expected.
- meta.json was not re-audited (language-gated 2026-09-27). The title's "15" still slightly spoils the "15, not 10" reveal.
