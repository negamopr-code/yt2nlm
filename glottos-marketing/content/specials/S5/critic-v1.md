# S5 critic review, s5-v1.mp4 (Synonym Memory Challenge: PROBLEM, P01, 16:9 NotebookLM whiteboard, 6:02)

Reviewer: glottos viewer-critic (headless autopilot step "special S5: critic"), 2026-09-29.
File checked: content/specials/S5/s5-v1.mp4, sha256 31e3daed…d233, 1280x720, 24 fps, AAC mono 44.1 kHz, 361.72 s (made on account default).
Watched as: a B1 to B2 learner who forgets new words within days and, when speaking, says "problem" for everything.

Method:
- 2 contact sheets (a frame every 5 s, 72 frames).
- Full-resolution frames at 0.7, 1.5, 8, 20, 33, 45, 100, 118, 133, 138, 148, 185, 245, 256, 262, 275, 300, 330, 356, 360 and 361.5 s.
- A grid of 20 frames at the voice midpoint of each beat and each story word (20, 33, 70, 84, 96, 110, 125, 148, 160, 173, 185, 200, 216, 230, 245, 256, 267, 277, 348, 356 s) to check that the picture matches the voice.
- Two scene-change passes (threshold 0.2 and 0.03, over the whole file).
- An ffmpeg silencedetect map (-35 dB, 0.7 s), plus fine passes (0.2 s) and volumedetect on the pause gaps and on 5 headwords that whisper left out.
- A full faster-whisper small.en transcript (int8, cpu_threads=4, word timings).
- References: script.md, focus.txt, meta.json, lang-gate-v1.md, the Specials / S1–S5 sections of docs/autopilot.md, S4 critic-v1.md and critic-v2.md (format), /workspace/state/glottos-methods/P01/strategy.md and proof_doc.md (quotes re-grepped in this run).

NotebookLM was not touched. Nothing was rendered, uploaded or changed, and state/autopilot.json was not edited. The working files are in /tmp/s5c (outside the repo).

Time map (scene cuts): title 0–2.63 · score boards 2.63–13.42 · plain list 13.42–28.50 · pause 1 card 28.50–37.25 · story cards 37.25–260.96 · pause 2 card 260.96–272.83 · reveal card 272.83–281.38 · ladder 281.38–343.79 · comment card 343.79–353.38 · site card 353.38–358.63 · Gemini end card 358.63–361.72.

## Verdict: PARTLY (can ship after polish; no regeneration needed)

The audio is very good, the best script fidelity in the series:
- All 6 beats are there, in order. The voice follows the gated script almost word for word.
- All 15 story words come in the script's order, each with the gated meaning. Snag is the only word with a register label ("Informal"). Hiccup, glitch and headache get no label, which is correct.
- The comment line, the transfer line and the anotherwordfor.net line are all spoken. There is no "examples" or search-box promise.
- There are no memory statistics, no "most people", no "always", no "top/bottom", no "worst/strongest", and no "satnav".
- Every story card cuts in 0.35–0.6 s before its spoken headword. Picture/voice sync is excellent.
- The list is shown once only, and the reveal card writes the 5 extras. Both S4 lessons worked.

It cannot ship as it is. These are the same kinds of defect as S4 v1:
1. **The ladder screen has only 8 of the 15 words** (281.38–343.79, 62 s). difficulty, complication, setback, headache, trouble, dilemma and predicament are missing, including 2 of the 5 extras. The voice reads 15 rows while the screen shows 8. The meanings are also cut down (issue = "worry", snag = "hidden problem"), and there is no "when to use" column.
2. **complication has no picture** (142.83–153.88, 11 s). A blank blue card shows only the word and meaning, while the voice tells the funniest moment of the story (the parrot lands in the cream, feathers on the cake). This is one of the 5 extras.
3. **Neither pause has a real hold.** Pause 1 has 0.89 s of silence after "remember." (31.48 → 32.37 "Done?"). Pause 2 has 0.55 s after "in order." (264.88 → 265.43 "Tip"). The focus text asked for 3 s silent.
4. **The disaster/ending panel breaks the brief.** A **burning house is drawn** at the left (about x 0–170, y 110–350, 237.38–260.96), and focus.txt says "Do NOT … draw fire". Also, **grandmother's speech bubble is empty** (about x 725–935, y 530–640) while the voice says "Best birthday in ninety years!" (255.40). The happy ending has no picture of its own; it sits on the disaster card.
5. **"Gemini Notebook" is on every frame, plus a Gemini end card (358.63–361.72).**

All five can be fixed in post. Regeneration is not needed. The runbook trigger "ask_user about our own renderer" (beats dropped or scrambled twice) does **not** apply: no beat was dropped or scrambled.

## Pain in the learner's words

These quotes are verbatim from /workspace/state/glottos-methods/P01 (proof_doc.md, strategy.md). Each one was re-grepped in this run. No names are given.
- "I’ve been trying to cram too many words and always forget them."
- "I forget every new word so of this works for me it will be life changing"
- "I reviewed but kept forgetting the words."
- "I wrote the word in my notebook and I thought I'll use it later but it was a lie, I knew that I won't use it, I just use the same words all time."
- "That's called mnemonics. Really helps you learn languages, specifically vocabulary, where you can associate some bonkers, vivid and chaotic story with a meaning and a pronunciation of a word."
- Score comments on the source method's video: "I tried it and it worked, from scoring 4/10 to 10/10." (strategy.md also cites "7 verbal, 15 visual".)

In one sentence: "I write down words like *setback* or *predicament*, forget them in days, and when I speak I just say *problem* for everything."

Solved means that tomorrow:
- I remember more of a word group from a silly story than from a list, and I can prove it with my two scores;
- I say *a small hitch*, *a technical glitch*, *a setback*, *I'm in trouble*, *it went without a hitch*, and I know a *dilemma* is a hard choice, not any problem;
- I can build my own silly story for my next word group.

## Beat survival: all present, in order, no spoken cue dropped

| # | Required beat | Heard (whisper, s) | On screen (s) | Result |
|---|---|---|---|---|
| 1 | Hook ≤15 s, two scores | 0.00–12.68 "10 words for problem. How many can you remember? We'll use one trick, a single silly story, and then we test you again. You'll also learn when to use each word. Grab a pen. You're getting two scores." | 0–2.63 title "Synonym Challenge: PROBLEM" (a smiling baker holding a cake, surrounded by problem icons). 2.63–13.42 two wooden boards "Score 1:" / "Score 2:" with a pen and a notebook. | OK: 12.7 s. "problem" is spoken as a word, not spelled out. The pen/score picture matches "Grab a pen". |
| 2 | Plain list of 10, in script order | 13.62 "First, the plain list. Just read and listen." 17.14–27.86: dilemma, snag, trouble (19.50, confirmed by the audio level; whisper left it out), obstacle, issue, disaster, hitch, setback, difficulty, headache. | 13.42–28.50 all 10 words in one paragraph, correct order, printed once, no pictures and no meanings. A yellow highlight follows the voice. | OK. The words are not shown one at a time as planned, but the paragraph is readable and not duplicated (the S4 lesson worked). |
| 2b | Spoken pause cue plus a ~3 s hold | 28.62–31.48 "Pause the video now. Write down every word you remember." **Silence 31.48–32.37 (0.89 s).** 32.37 "Done?" 33.28 "Count them. That's score number one, your list score. Keep it." | 28.50–37.25 pause icon plus "Write down every word you remember." (a hand writing) | The cue is present and says "video". **There is no real hold (0.89 s).** |
| 3 | ONE story, 15 words, script order | Intro 37.36–46.88 ("We're using pictures instead of a list … roughly from small problems to very serious ones"). Headword onsets: hiccup 47.60 ("First up, hiccup"), snag 62.96, hitch 78.60, glitch 91.28, issue 102.18, difficulty 118.08, obstacle 132.58, complication 143.40, setback 154.40, headache 167.70, trouble 179.32, dilemma 192.04, predicament 208.62, crisis 224.02, disaster 237.73 (confirmed by the audio level; whisper starts at "Then the water sprinklers", 238.78). Happy ending 252.40–260.38 ("In the ending, your grandmother laughs and says, best birthday in 90 years. Everyone eats cake soup with spoons. It's only a story."). | Cards: hiccup 37.25, snag 62.38, hitch 78.25, glitch 90.83, issue 101.79, difficulty 117.63, obstacle 132.17, complication 142.83, setback 153.88, headache 167.21, trouble 178.83, dilemma 191.67, predicament 208.21, crisis 223.63, disaster 237.38 (it also covers the ending, to 260.96). | **Exact order, nothing merged or skipped.** Every card lands 0.35–0.6 s before its headword. The first scene is drawn at once (the S4 lesson worked). Picture defects are covered below. |
| 4 | Second pause "in order" + ~3 s hold, tip after | 260.98–264.88 "Pause the video again. Write down every word you can recall. In order." **Silence 264.88–265.43 (0.55 s).** 265.48 "Tip. Walk through the story again." 268.34 "Done? Count them. That's score number two. Your story score." | 260.96–272.83 "Write down every word you can recall, in order." ("in order" highlighted), pause icon, brain | The cue and "in order" are present on the card and in the voice. **There is no hold: the tip comes 0.55 s after the cue.** The tip does come before "Done?", as the script asked. The script's example "The mixer, the hole in the cake tin, the van door…" was dropped (harmless). |
| 5 | "15, not 10" reveal + ladder | 273.12 "I gave you 15 words, not 10. The extra words, hiccup, glitch, complication, predicament, crisis." 281.64 "Here's the whole ladder on one screen. Roughly from small problems to very serious ones. The order is a guide, not a rule." Then the spoken recap of all 15, in order, with the script's Beat 5 labels (onsets below). | 272.83–281.38 "15, not 10! Extra words" with a box listing hiccup, glitch, complication, predicament, crisis. 281.38–343.79 **one static 2-column table (Word, Meaning) with only 8 rows.** | The voice is correct. It makes no "came only from the story" claim (it dropped "Did any of them make it onto yours?", which is harmless). The reveal card is correct and writes the 5 extras. **The ladder screen is not correct** (see On-screen text). |
| 6 | Comment CTA, transfer, site | 343.92–347.74 "**Which score was higher? Comment your two scores. List versus story.**" 348.46–352.66 "Tonight, try it with your own new words. One silly story, one picture for each word." 353.50–358.02 "For more words, look up another word for problem on anotherwordfor.net." | 343.79–353.38 "Comment your two scores: list vs story." (speech bubble, pointing hand). 353.38–358.63 "Look up another word for problem on anotherwordfor.net" (globe, magnifier). | **All three lines are spoken exactly, and both key lines are on screen.** There is no search-box or examples promise. |
| – | End | – | **358.63–361.72 full-screen "Gemini Notebook" end card** (the voice ends at 358.02) | Brand violation |

Spoken recap onsets (for the ladder overlay): hiccup 288.08, snag 291.32, hitch 295.94, glitch 298.82, issue 303.54, difficulty 307.24, obstacle 310.90, complication 313.22, setback 316.54, headache 319.76, trouble 322.64, dilemma 327.52, predicament 331.74, crisis 335.20, disaster 338.68. whisper left out the headwords "Issue", "Difficulty" and "Trouble" (it heard only their meanings). A silencedetect at 0.2 s and a volumedetect (about -22 to -25 dB mean) confirm that speech is present at those onsets.

## Accuracy for B1 (acted meaning and register per synonym)

The voice uses the gated meaning for all 15 words and makes no wrong register claim. Picture by picture:
- **hiccup**: the mixer with a "PAUSED" tag and a spark, the parrot in a magnifier, a "90th Birthday!" banner, a "90" calendar. Right sense. But the person baking is **the grandmother herself**, while the voice says "you are baking the cake" (see Continuity).
- **snag**: a cake tin with one drop falling from its bottom, and the parrot below. Right. Most of the picture is behind the blue card. Card: "a problem, often small, hidden or unexpected. Informal." This matches the voice.
- **hitch**: the van with a "stuck" door, a 5-minute stopwatch, then the door open with the cake inside and a green tick. Right, and very clear.
- **glitch**: a GPS with a cracked screen showing a boat on the sea, a map, a small computer. Right.
- **issue**: the parrot wearing a chef's hat, a "NO ANIMALS ALLOWED" sign, a reception bell, an old phone with a "!". Right (the "hides under your hat" gag becomes "wears the hat").
- **difficulty**: a huge cake carried up a narrow staircase with a "6" on it. Only hands are visible, and most of it is behind the card. Right, but weak.
- **obstacle**: a sofa stuck on the stairs. The picture shows **two removal men carrying it, and a third man with boxes**, not "you with the cake who can't get past". A viewer still gets "something in your way".
- **complication**: **no picture** (defect 2).
- **setback**: a leg slipping on a feather, the stairs, an oven, a hand putting a cake in. Right.
- **headache**: an oven, many phones, worried relatives' faces, a calendar. Right, and busy in a good way.
- **trouble**: an **angry man in a chef's jacket** points at the rainbow parrot standing on a ruined cake. The script's angry manager with a clipboard is not drawn. A viewer reads "the chef is angry with the parrot", which is still "someone is angry with you" (the parrot is in trouble). Acceptable. The card shows only "problems and worry" and leaves out "in trouble" (spoken 187.78).
- **dilemma**: a woman holding a cake box, a sofa on the stairs, and an arrow to a tiny old lift. Right: two options.
- **predicament**: a man in a suit with the cake and the parrot, stuck in a lift between "4" and "5", with a "PARTY STARTS IN 5 MINS" sign. Right, and very clear.
- **crisis**: ninety candles, smoke, an alarm bell, frightened people in a lift. Right. The candle flames are small and fine.
- **disaster**: sprinklers, wet guests with plates, a melted cake, grandmother laughing. Right for "the party is a disaster". But there is also a **burning house at the left and flood water at the right**. They illustrate the spoken "Also a terrible event like a flood or a fire" (249.44), but focus.txt and the script ban drawing fire (defect 4). Grandmother's **speech bubble is empty**.

Voice wording that differs from the script (none teaches anything wrong; no splice needed):
- 252.40 "In the ending, your grandmother laughs" (the script says "And the ending? Your grandmother laughs"). This is slightly unnatural English, but clear. Language-editor note only.
- 275.30 "The extra words, hiccup, glitch…" replaces "Hiccup, glitch … were never on the list. Did any of them make it onto yours?". There is no "came only from the story" claim.

Memory claims: **clean.** There are no statistics, no "most people", no "10x", no researchers, no age of the method, and no claim that the words become permanent. A transcript grep for always, most, top, bottom, worst, strongest, formal, welcome, dive, explainer, episode, podcast, example, search and satnav finds only "informal" (snag, correct) and "the top of the cake" (story, correct).

## On-screen text, pictures, watermark

- **Style:** this is not the whiteboard look. Every story frame is a watercolour drawing with a large blue caption card (about x 60–1000, y 75–645) on top of it. The card hides 40–60% of most pictures (snag, difficulty, glitch, setback). The captions are large and very readable. The pictures, which are the method itself, are partly buried.
- **Continuity:** the "you" of the story is never the same person. The title shows a young female baker. In hiccup the grandmother is baking. In difficulty there are only hands. Obstacle shows removal men, trouble an angry male chef, dilemma a woman in jeans, and predicament a man in a suit. The chef's hat ends up on the parrot. The parrot changes species and colour (grey in hiccup, a blue-yellow macaw in snag, white in issue, a rainbow parrot in trouble and predicament). The S2 lesson ("same character in every scene") did not survive. The cake, the stairs, the lift and "a parrot" do carry the story, so this weakens the method but does not break it.
- **complication (142.83–153.88): a blank blue card**, "complication / something that makes a situation more difficult.", on an empty faded background. It is the only word of the 15 without a picture.
- The story captions all match the gated meanings. Some are shorter than the voice, but none contradicts it. Missing parts: "without a hitch" (hitch), "Often used at work" (issue), "Often for machines and computers" (glitch), "in trouble: someone is angry with you" (trouble), "Also a flood or a fire" (disaster). The "in trouble" loss matters most, because it is the most useful phrase in that scene.
- **Ending (252.40–260.96):** there is no own panel for it; it stays on the disaster card. **The speech bubble next to grandmother is empty.** A **burning house** is at the left edge.
- **Pause cards:** both have a pause icon and the "write down" line. Pause 2 includes "in order". OK.
- **Reveal card (272.83–281.38):** "15, not 10! Extra words", with hiccup, glitch, complication, predicament and crisis written. OK. It is small and plain (about 60% of the frame is empty paper).
- **Ladder (281.38–343.79, 62 s):** a 2-column table (Word | Meaning) with only these **8 rows: hiccup "small problem", snag "hidden problem", hitch "short delay", glitch "small fault", issue "worry", obstacle "in your way", crisis "time of danger", disaster "complete failure"**.
  - **7 words are missing:** difficulty, complication, setback, headache, trouble, dilemma, predicament. That includes 2 of the 5 extras the reveal just named, and dilemma, the one word the script works hardest to explain ("Not just any problem: a hard choice").
  - There is no heading ("small problem → very serious problem"), no "when to use" column, and no "Informal" on snag.
  - "issue = worry" and "snag = hidden problem" are cut-down glosses, and "disaster = complete failure" drops "a very bad situation". They are weaker than the voice, but not false.
  - Faded decorative words behind the table ("Dilemma" ×2, "Issue", "Predicament" ×2, "Challenge") are spelled correctly.
  - For 62 s the learner hears rows that are not on the screen. Anyone who screenshots "the whole ladder" gets about half of it.
- **CTA cards:** "Comment your two scores: list vs story." and "Look up another word for problem on anotherwordfor.net". Both are correct and promise no examples.
- **Watermark: "Gemini Notebook" in the bottom-right corner of EVERY frame** (about x 1155–1275, y 697–715), plus the **full-screen Gemini end card from 358.63 to 361.72**.

## Second by second: where a viewer would swipe away

- 0:00–0:03: "10 words for problem. How many can you remember?" It is my problem as a question, so I stop. The title card is clean.
- 0:03–0:13: the score boards and the pen, matching "grab a pen". Good.
- 0:13–0:28: the list, readable, with a highlight following the voice. Fine.
- **0:28–0:33: the pause cue, then only 0.9 s of silence before "Done? Count them."** If I don't press pause fast, score 1 is gone. This is the first trust hit ("wait, I wasn't ready").
- 0:37–0:47: the story intro over the first drawing (the kitchen, the mixer, the parrot). Good: no blank card this time.
- 0:47–2:23: hiccup to obstacle, concrete scenes (the stuck van door and the GPS in the sea are the best). New card every 11–16 s, perfect sync. It holds. Small doubts: "who is 'me' in this story?" (grandmother baking, removal men).
- **2:23–2:34: blank blue "complication" card** during the funniest line ("the parrot lands in the cream"). A small drop.
- 2:34–4:13: setback to disaster. It holds; predicament and hitch are the clearest pictures in the video.
- 4:12–4:21: the happy ending line over the disaster card with an empty speech bubble and a burning house. Flat, and slightly off-tone.
- **4:21–4:25: the second pause has no hold (0.55 s).** The tip talks over the writing moment, so score 2, the whole point of the video, is shaky.
- 4:33–4:41: the reveal, with the extras written. Good "aha" moment.
- **4:41–5:44: 62 s on a static 8-row table.** From 5:07 the voice reads difficulty, complication, setback, headache, trouble, dilemma and predicament, and I can't find them on screen. This is the main swipe zone and a trust hit ("did I miss something?").
- 5:44–5:58: comment the scores, try it tonight, the site. Spoken and on screen. OK.
- 5:58–6:02: the Gemini end card.

## Takeaway test

Tonight: take my own new word group, make one silly story with one picture per word, then comment "list X / story Y". Both actions are spoken (343.9, 348.5) and the comment action is also on screen. I also leave knowing *a hitch* (and *without a hitch*), *a glitch* in the GPS, *a setback*, *I'm in trouble*, *a predicament* in a stuck lift, that a *dilemma* is a hard choice between two things, and that *snag* is informal. That is a real action for the P01 pain, so the verdict is not capped by the takeaway test. It is capped by the half-empty ladder, the missing complication picture and the missing pause holds, which break the method's own promise on screen.

## Retention risks

- Length is 6:02 (5:58 after trimming the end card, about 6:04 with the pause freezes). That is inside the 5–7 min target, and the shortest in the series (NotebookLM compressed the 959-word script to 6:02 without dropping a beat).
- Pacing: the story runs at about 11–16 s per word and is steady. The drags are the blank complication card (11 s) and the 62 s static half-table.
- Legibility: the captions are large and readable at 720p. The ladder rows are readable. The reveal card text is small.
- Sync: excellent. Every story card lands just before its headword; the pause, reveal and CTA cards land on the voice.
- Pictures: the blue card hides a large part of most drawings, and the main character changes in every scene. For a "pictures instead of a list" video, this is the main quality gap that polish cannot fully fix.

## Trust risks

- The ladder contradicts the voice by omission (8 rows on screen, 15 spoken).
- A burning house is drawn in a "nobody is hurt" story, against the brief.
- The ending shows an empty speech bubble while grandmother's line is spoken.
- The Gemini watermark and end card break the brand rule.
- "In the ending, your grandmother laughs" is slightly unnatural English (minor).
- There are no memory statistics, no false claims about the method, and no wrong register labels.

## Defects and fixes (all in post; no regeneration)

### Ship-blocking

1. **Watermark and end card (shorts-builder).** Trim at **358.3 s** (the CTA audio ends at 358.02, and the end card starts at 358.63). Cover the bottom-right "Gemini Notebook" mark (about x 1150–1280, y 690–720) on every frame with the channel logo `state/brand/awf-logo-channel.jpg` or a background-matched patch (S4 v2 left a faint grey smear left of the logo; make the patch wider or match the background better).
2. **Ladder, 281.38–343.79 (visuals, then shorts-builder, then a language-editor re-gate).** Overlay our own full-frame **15-row, single-column** ladder, one row per word, no pairs, hiccup first and disaster last, heading "small problem → very serious problem" and "The order is a guide, not a rule.", with word · meaning · when to use, using exactly the script's Beat 5 labels (snag "Informal" is the only register label). Mark the 5 extras. Reuse the S4 polish-v2 builder with a row highlight on the voice: hiccup 288.08, snag 291.32, hitch 295.94, glitch 298.82, issue 303.54, difficulty 307.24, obstacle 310.90, complication 313.22, setback 316.54, headache 319.76, trouble 322.64, dilemma 327.52, predicament 331.74, crisis 335.20, disaster 338.68 (lead each by about 0.2 s).
3. **complication picture, 142.83–153.88 (visuals, then shorts-builder).** Draw one watercolour panel in this video's style: the parrot landing in the cream on top of the cake, feathers flying, "Uh-oh!" bubble. Place it in the empty upper part of the blue card, above the word (about x 100–1000, y 130–450; the word and meaning sit at about y 470–570 in the 1280x720 frame), or full-frame behind a smaller card. Show it for the whole card, 142.83–153.88.
4. **Pause holds (shorts-builder).** Insert a silent **3 s freeze** of the pause 1 card at **31.9 s** (inside the silence 31.48–32.37, after "remember.", before "Done?"), and a silent **3 s freeze** of the pause 2 card at **265.0 s** (inside the silence 264.88–265.43, after "in order.", before "Tip"). This adds about 6 s. Every later timestamp in this report then shifts (+3 s after 31.9, +6 s after 265.0).
5. **Disaster/ending panel, 237.38–260.96 (visuals, then shorts-builder, then a language-editor re-gate).** Cover the **burning house** at the left (about x 0–175, y 100–360) with the paper background, or with more wet guests / sprinkler spray. Fill the **empty speech bubble** (about x 725–935, y 530–640) with "**Best birthday in ninety years!**" from **252.4** (the ending starts; the line is spoken at 255.40) to 260.96. From 237.38 to 252.4 the bubble can stay empty or also be covered. Optional: switch the caption to "It's only a story." with no card from 252.4. Keep the flood water on the right (it matches "a flood or a fire" in the voice and hurts nobody), or cover it too for consistency with the brief.

### Recommended (in post)

6. **Trouble caption, 178.83–191.67 (shorts-builder, then a language-editor re-gate).** Add a second line "in trouble: someone is angry with you" under "problems and worry." from **187.78** (spoken 187.78–190.98). This is the phrase a learner will actually use.
7. **Other caption extras (shorts-builder, optional).** Small sub-lines in the voice's exact words: hitch "without a hitch = with no problems at all" (87.48–91.2), issue "Often used at work" (114.22–117.6), glitch "Often machines and computers" (99.76–101.8).
8. **Pinned comment (publisher).** "List: __ / Story: __ ?" to seed the score comments.
9. **Audio (language-editor decides; do not splice unless asked).** "In the ending, your grandmother laughs" (252.40). Understandable, and it teaches nothing wrong.
10. **For future specials (scenario-writer, focus.txt).** The S3/S4 lessons worked: the word was spoken not spelled, "pause the video", "in order" on the card and in the voice, the extras written on the reveal card, the list printed once, the first scene drawn at once, and exact register words. These still fail every time: **the full 15-row ladder (third video in a row with a shortened table), a real silent hold after both pause cues (fifth video in a row), and one consistent protagonist.** Stop asking NotebookLM for these three and budget them in polish from the start (ladder overlay, freezes). The blue caption card hiding the drawings is new in this account's style; if S-series continues, ask for "caption as a small label, the drawing fills the frame".

After fixes 1 to 5 (ideally with 6), this should reach **SOLVES**. Re-run the critic on the polished file.

## Not checked

- No human listening. The headwords were checked by whisper small.en. "Trouble" (list, 19.50), "Disaster" (story, 237.73), and "Issue", "Difficulty" and "Trouble" (recap) were not transcribed; their presence is confirmed only by silencedetect and volumedetect at the expected times, not by the words themselves.
- Frames were sampled every 5 s, plus both scene-cut lists and about 40 targeted frames. A defect lasting less than about 3 s between samples could be missed.
- meta.json was not re-audited (it was gated). As with S3 and S4, the title "Can You Remember 15 Synonyms for PROBLEM?" slightly spoils the "15, not 10" reveal.
- The anotherwordfor.net SSL status was not re-checked (the gate recorded the certificate as expired).
- The exact pixel boxes for the fixes were read off 1280x720 frames by eye; the builder should confirm them on the frames.
