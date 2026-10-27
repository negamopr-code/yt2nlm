# S5 critic review, s5-v3.mp4 (Synonym Memory Challenge: PROBLEM, P01, 16:9, polish round 1 + language fix, 6:04)

Reviewer: glottos viewer-critic (headless autopilot step "special S5: critic", second critic on the polished file), 2026-09-30.
File checked: content/specials/S5/s5-v3.mp4, sha256 8345dbe1…46844 (matches polish-v2.md), 1280x720, 24 fps, AAC mono 44.1 kHz, 364.29 s.
Watched as: a B1 to B2 learner who forgets new words within days and says "problem" for everything.

Method:
- 3 contact sheets (a frame every 5 s, 73 frames).
- Full-resolution frames at 0.7, 1.5, 33.4 (pause-1 freeze), 151 (complication), 193 (trouble 2nd line), 245 / 258 / 262 (disaster + ending bubble), 269.5 (pause-2 freeze), 283 (reveal), 300 / 330 / 346 (ladder), 356, 362, 364.1 s.
- Bottom-right corner crops at 12 times (1 → 363 s) plus a pixel zoom of the old watermark box.
- Ladder highlight tracked automatically at 10 fps over 286–350 s (yellow-row detection) against whisper word onsets.
- Scene-change pass (threshold 0.2) over the whole file; ffmpeg silencedetect (-35 dB, 0.7 s); astats around both freeze joins and the final 1 s (clicks / clipped last word).
- Full faster-whisper small.en transcript (int8, cpu_threads=4, word timings). No spelled-out word anywhere; no "Gemini"/"notebook" spoken.
References: critic-v1.md, polish-v2.md, lang-gate-v2-polish.md, script.md, docs/autopilot.md (Specials, S1–S5), S4 critic-v2.md (format), /workspace/state/glottos-methods/P01 (quotes re-grepped this run).
NotebookLM was not touched. Nothing was rendered, uploaded or changed; state/autopilot.json not edited. Working files: /tmp/s5c3 (outside the repo).

Time map: v3 = v1 until 31.9; v1 + 3.0 s from 31.9 to 265.0; v1 + 6.0 s after 265.0; cut at v1 358.3. Verified: the last word ends at 363.98 (= v1 357.98 + 6), every card cut lands at v1 + 3/6 (e.g. complication 145.83, disaster 240.38, ladder 287.38, comment 349.79). No A/V drift.

## Verdict: SOLVES. No ship-blocking defect remains.

All 5 v1 ship-blockers and the recommended trouble line are fixed and verified on frames and audio, and the language-gate item (Difficulty example) is on screen. The challenge now works as a challenge: list → pause (3.8 s real silence) → 15-picture story → pause "in order" (3.5 s silence) → "15, not 10" with the extras written → a complete 15-row ladder whose highlight follows the voice → "Comment your two scores: list vs story" spoken and on screen → the site line. What remains is cosmetic: an obvious blank paper rectangle where the burning house was (23.6 s), a flat clip-art complication panel in a watercolour video, a faint grey smear left of the logo, and the known protagonist-continuity weakness from NotebookLM.

## v1 ship-blockers: status in v3

| # | v1 defect | v3 evidence | Status |
|---|---|---|---|
| 1 | "Gemini Notebook" on every frame + Gemini end card 358.63–361.72 | Channel logo (AnotherWordFor avatar) at bottom right on all 73 sheet frames and 12 corner crops; no letters legible in the old box (pixel zoom at 300 s). File ends at 364.29 on our own site card fading to dark from 363.89; no Gemini card, no end card. The last word ("…anotherwordfor.net") finishes at 363.98 before the file ends (peak after 364.0 is -54 dB), so the trim clips nothing. | FIXED. Residue: a soft grey gradient smear, about x 1145–1225, y 690–718, left of the logo, visible on flat grid backgrounds on every frame (same residue as S4 v2). Cosmetic. |
| 2 | Ladder had 8 of 15 rows | 287.38–349.79: full-frame "The ladder: small problem → very serious problem", "The order is a guide, not a rule.", WORD / MEANING, **all 15 rows** hiccup → disaster, orange dots on hiccup, glitch, complication, predicament, crisis, footer "Read downward…" + "= one of the 5 sneaky extras". Snag carries "Informal."; Trouble carries "\"In trouble\": someone is angry with you."; **Difficulty reads "a problem. \"I have difficulty doing it.\""** (language-gate fix present). Every cell matches the spoken recap. Text is about 17 px, clearly legible at 720p. | FIXED |
| 3 | complication had no picture (142.83–153.88) | 145.83–156.88: a 3-tier cake, a green parrot diving head-first into the cream, flying "feathers", "Uh-oh!" bubble, above the word and meaning, no overlap with the text or the magnifier. Matches "the parrot … lands in the cream. Now there are feathers on the cake." (147.62–152.74). | FIXED. Weakness: flat vector clip-art in a watercolour video (the same weakness as S4's cute panel); the green "feathers" read more like leaves, and this parrot looks like no other parrot in the video. Not wrong. |
| 4 | Pause holds 0.89 s and 0.55 s | Pause 1: "…every word you remember." ends 31.50, **silence 31.56–35.37 (3.80 s)** on a frozen pause-1 card, then "Done?" 35.28. Pause 2: "…In order." ends 267.88, **silence 267.91–271.43 (3.53 s)** on a frozen pause-2 card, then "Tip." 271.32. No click at either join (the insert at 268.0 cuts the decaying tail of "order" at -45 dB, then true silence). No visual jump in or out of either freeze. | FIXED. 3.5 s is still short for writing 10–15 words, but the spoken "Pause the video" does the real work; the hold now gives time to press pause. |
| 5 | Burning house drawn; grandmother's bubble empty | 240.38–263.96: no fire, flame or smoke anywhere; the left region is covered. Bubble reads "Best birthday / in ninety years!" from 255.4 to 263.96 (checked 258, 262); the voice says "best birthday in 90 years" at 257.94. Empty before 255.4 (245 s), as planned. | FIXED (content). **Cosmetic defect introduced:** the patch is an obvious flat paper rectangle (x 0–235, y 0–360) with hard right and bottom edges; it cuts off the left sprinkler spray at x ≈ 235 and the tip of a party hat at y ≈ 355. It looks like a blank sticky note stuck on the scene for 23.6 s. Not a brief violation, not ship-blocking. |
| 6 (rec.) | Trouble card lost "in trouble" | 190.78–194.67: second line "\"In trouble\": someone is angry with you." under "problems and worry."; voice "In trouble, someone is angry with you or you may be punished." 190.78–193.96. Exact sync. | FIXED. Minor: bold Arial next to the card's rounded font, and "you." runs onto the cake crumbs at the right (still readable). |

## Challenge beats (v3 times)

| # | Beat | Heard | On screen | Result |
|---|---|---|---|---|
| 1 | Hook ≤15 s, two scores | 0.00–12.68 "10 words for problem. How many can you remember? … Grab a pen. You're getting two scores." | title "Synonym Challenge: PROBLEM" (0–2.63), Score 1 / Score 2 boards with a pen | OK. "problem" spoken as a word. |
| 2 | Plain list of 10 | 13.60 "First, the plain list." 17.14–27.84 dilemma … headache (whisper skips trouble/difficulty, as in v1; audio present) | 10 words once, highlight follows the voice | OK |
| 2b | Pause 1 + hold | 28.62–31.50 "Pause the video now. Write down every word you remember." + 3.80 s silence | pause-1 card, frozen | OK |
| 3 | ONE story, 15 words, script order | hiccup 50.60 … disaster 240.98; ending 255.34–263.40 | 15 cards in order, every card 0.35–0.6 s before its headword; complication now drawn; ending bubble filled | OK |
| 4 | Pause 2 "in order" + hold, tip after | 264.40–267.88 "Pause the video again. … In order." + 3.53 s silence, "Tip. Walk through the story again." 271.32 | pause-2 card with "in order" highlighted, frozen | OK |
| 5 | 15-not-10 reveal + ladder | 278.90 "I gave you 15 words, not 10. The extra words, hiccup, glitch, complication, predicament, crisis." 287.32 "Here's the whole ladder on one screen." recap 294.38–349.10 | reveal card with the 5 extras (278.83–287.38); full 15-row ladder (287.38–349.79) | OK |
| 6 | Comment CTA, transfer, site | 350.20 "Which score was higher? Comment your two scores. List versus story." 354.48 "Tonight, try it with your own new words. One silly story, one picture for each word." 359.56 "…look up another word for problem on anotherwordfor.net." | "Comment your two scores: list vs story." (349.79–359.38); "Look up another word for problem on anotherwordfor.net" (359.38–end) | OK. No "examples" or search-box promise. |

## Ladder highlight vs voice (detected at 10 fps)

| Row | Highlight on | Voice headword | Lead |
|---|---|---|---|
| Hiccup | 293.9 | 294.38 | 0.5 s |
| Snag | 297.1 | 297.32 | 0.2 |
| Hitch | 301.8 | 301.94 | 0.1 |
| Glitch | 304.6 | 304.82 | 0.2 |
| Issue | 309.3 | ≈309.5 (whisper skips the headword; meaning 310.34) | 0.2 |
| Difficulty | 313.0 | 313.26 | 0.3 |
| Obstacle | 316.7 | 316.96 | 0.3 |
| Complication | 319.0 | 319.22 | 0.2 |
| Setback | 322.3 | 322.64 | 0.3 |
| Headache | 325.5 | 325.78 | 0.3 |
| Trouble | 328.5 | ≈328.6 (meaning 329.86) | 0.1 |
| Dilemma | 333.3 | 333.54 | 0.2 |
| Predicament | 337.5 | 337.74 | 0.2 |
| Crisis | 341.0 | 341.20 | 0.2 |
| Disaster | 344.5 | 344.42 | 0.0 |

No row lights late; no row is skipped. The base table (no highlight) shows from 287.38 while the voice introduces it; the highlight clears at 349.6 as the comment card arrives. Better than S4 v2 (one row 0.84 s late there).

## Pain in the learner's words (verbatim, re-grepped in /workspace/state/glottos-methods/P01, no names)

- "I’ve been trying to cram too many words and always forget them."
- "I forget every new word so of this works for me it will be life changing"
- "I reviewed but kept forgetting the words."
- "I wrote the word in my notebook and I thought I'll use it later but it was a lie, I knew that I won't use it, I just use the same words all time."
- "…you can associate some bonkers, vivid and chaotic story with a meaning and a pronunciation of a word."
- On the source method's video: "I tried it and it worked, from scoring 4/10 to 10/10."

In one sentence: "I write down words like *setback* or *predicament*, forget them in days, and when I speak I just say *problem* for everything."
Solved means that tomorrow I can prove to myself (two scores) that a silly story beats a list, I use *a hitch / without a hitch*, *a glitch*, *a setback*, *I'm in trouble*, *a dilemma* (a hard choice, not any problem), and I build my own story for my next word group.

What the video gives: the self-test with two real pause moments, 15 acted scenes in a fixed order, a complete screenshot-able ladder with meanings and the key patterns (*without a hitch* in the story, *in trouble*, *have difficulty doing it*, snag = informal), and a spoken + written instruction to try it tonight and comment both scores. Gap: the story's "you" changes person every scene (grandmother, removal men, a chef, a woman, a man in a suit), which weakens the "imagine yourself" part of the method; not fixable in post.

## Second by second: where a viewer would swipe away

- 0:00–0:03 "10 words for problem. How many can you remember?" My problem, as a question. I stay.
- 0:13–0:28 the list, readable, once. Fine.
- 0:28–0:35 pause cue, then 3.8 s of real silence on a still card. I have time to hit pause. The v1 "wait, I wasn't ready" moment is gone.
- 0:40–2:25 hiccup → obstacle, a new card every 11–16 s, perfect sync. Holds.
- 2:25–2:36 complication now has a picture (bird in the cream, "Uh-oh!"). It looks like a different, cartoon video for 11 s, but the joke lands.
- 3:10–3:14 "In trouble: someone is angry with you" appears exactly when spoken. Good.
- **4:00–4:24 disaster + ending: a blank off-white box sits in the top-left corner for 23.6 s**, cutting a sprinkler in half. A careful viewer will wonder what was covered. Small drop, the likeliest remaining "cheap edit" impression. The filled bubble on "best birthday in 90 years" works.
- 4:24–4:31 pause 2 with "in order" and 3.5 s silence before the tip. OK.
- 4:38–4:47 reveal with the 5 extras written. The "aha".
- 4:47–5:50 62 s ladder: now all 15 rows, highlight walking down with the voice. Still the longest static-ish stretch (main swipe risk for non-note-takers), but it now rewards a screenshot instead of breaking trust.
- 5:50–6:04 comment both scores, try it tonight, the site. Ends on our card; no Gemini.

## Takeaway test

Tonight: take my own new word group, make one silly story with one picture per word, then comment "list X / story Y". Both actions are spoken (350.2, 354.5) and the comment line is on screen. Plus concrete phrases I can say tomorrow: *it went without a hitch*, *a technical glitch*, *a setback*, *I'm in trouble*, *I have difficulty doing it*, *a dilemma* = a hard choice. Passes.

## Retention risks

- Length 6:04, inside the 5–7 min target; nothing was dropped.
- Pacing: story steady at 11–16 s per word; the 62 s ladder is the long stretch, now justified by content.
- Legibility: story captions large; ladder rows ~17 px, readable full-screen at 720p, tight on a phone in portrait.
- Picture/voice sync: excellent (story cards 0.35–0.6 s early, ladder highlight 0.0–0.5 s early, trouble line and bubble on the spoken words). No drift after either freeze.
- Style: three visual languages now (NotebookLM watercolour cards, flat clip-art complication, our clean table). The table is fine as a "summary slide"; the complication panel is the odd one out.

## Trust risks

- None on content: no memory statistics, no "most people", no wrong register labels, no fire drawn, no promise of examples. Ladder and voice agree row by row.
- Cosmetic trust hits: the blank rectangle over the disaster scene; the grey smear by the logo.
- Unchanged audio quirk: "In the ending, your grandmother laughs" (255.34), understandable, teaches nothing wrong.
- No spelled-out word (whisper shows no letter-by-letter token anywhere).

## Ship-blocking defects remaining: NONE

## Top 3 fixes (optional, ordered by impact; none blocks shipping)

1. **House patch, 240.38–263.96 (visuals, then shorts-builder).** Replace the flat rectangle with a background-matched fill that continues the left sprinkler spray and the ceiling line (or a small drawn element: another wet guest / more spray), with feathered edges on all inner sides; keep x 0–235, y 0–360 clear of any fire. Or crop-zoom the whole disaster shot slightly so the left strip falls outside the frame.
2. **Logo smear (shorts-builder).** Widen/re-match the delogo patch (about x 1140–1230, y 688–720) or put the logo on a small solid plate that also covers the smear. Same residue as S4; fix it in the shared polish recipe once for S1–S5.
3. **For the rest of the series (scenario-writer / visuals).** Budget the ladder overlay and pause freezes in polish from the start (they failed in NotebookLM again and succeeded in post), draw replacement panels in the video's own watercolour style rather than flat clip-art, and ask NotebookLM for one consistent protagonist and a small caption label so the drawings are not hidden by the blue card.

Also (publisher): pin "List: __ / Story: __ ?" to seed the score comments.

## Not checked

- No human listening; spoken words checked with whisper small.en. Headwords whisper skipped (list "trouble"/"difficulty"; recap "issue"/"trouble") were already confirmed by level in v1; the audio is unchanged except the two inserted silences, so they were not re-measured.
- Frames sampled every 5 s plus ~30 targeted frames and a 10 fps highlight track over the ladder; a defect shorter than ~3 s outside those windows could be missed.
- meta.json, the anotherwordfor.net certificate and the YouTube metadata were not re-audited here.
