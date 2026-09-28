# S2 critic review, s2-v1.mp4 (Synonym Memory Challenge: SAD, P01, 16:9 NotebookLM whiteboard, 7:28)

Reviewer: glottos viewer-critic (headless autopilot step "special S2: critic"), 2026-09-28.
Watched as: a B1 to B2 learner who forgets new words within days and only ever says "sad" when speaking.
Method: 3 contact sheets (one frame every 5 s, 90 frames). Full-resolution frames at 0.7, 1.5, 8, 20, 33, 38, 58, 95, 110, 175, 200, 222, 237, 300, 320, 340, 360, 420, 430, 432.5, 437, 442 and 446 s, plus a watermark crop. Two scene-change passes (threshold 0.2 over the whole file, 0.06 over 0–60 s and 300–448 s). An ffmpeg silencedetect map (-35 dB, 0.8 s). The audio was transcribed with faster-whisper small.en (int8, cpu_threads=4, word timings), and 5 doubtful spots were re-transcribed as isolated clips (25.5–30.5, 128.5–132, 392.5–396.5, 418.8–421.8, 426.8–434.8 s). The references were script.md, focus.txt, meta.json, lang-gate-v1.md, the S1–S5 section of docs/autopilot.md, and /workspace/state/glottos-methods/P01/strategy.md plus proof_doc.md. NotebookLM was not touched. Nothing was rendered, uploaded or changed. The working files are in /tmp/s2c (outside the repo).

## Verdict: PARTLY (can ship after polish; no regeneration needed)

This is a better NotebookLM take than S1 v1:
- All 15 story words come in the script's exact order. Each is acted out with the right meaning and register, and a picture lands within 0.5 s of each word (with one exception).
- The transfer line "Tonight, try it with your own new words" is now spoken and drawn.
- The spoken 15-row recap is correct.

It still cannot ship as it is, for four reasons:
1. **The ladder table shows only 8 of the 15 words.** It has none of the 5 "sneaky" extras, and it drops unhappy and down in the dumps. The voice reads all 15 over it for 84 s, so for about 40 s the screen contradicts the voice. This is the one screen people screenshot.
2. **The comment call to action is gone.** "Comment your two scores" and "which score was higher?" were both dropped. Only "List versus story." survives, over a 2.4 s card with no instruction to comment. The whole engagement mechanic of the series depends on that line.
3. **The pause holds are too short.** They are about 1.0 s at pause 1 and 2.6 s at pause 2, against a 3 s target.
4. **"Gemini Notebook" appears on every frame, followed by a Gemini end card.**

All four can be fixed in post.

## Pain in the learner's words

Verbatim, from the P01 research (proof_doc.md, comments/*.jsonl, strategy.md). All were re-checked by grep in this run. No names are given.
- "I've been trying to cram too many words and always forget them."
- "I forget every new word so of this works for me it will be life changing"
- "I also find myself forgetting certain English words when I'm speaking."
- "I reviewed but kept forgetting the words."
- "That's called mnemonics. Really helps you learn languages, specifically vocabulary, where you can associate some bonkers, vivid and chaotic story with a meaning and a pronunciation of a word."
- Score comments on the source method's video: "7 verbal, 15 visual. Just wow!" and "I tried it and it worked, from scoring 4/10 to 10/10."

In one sentence: "I learn words like *gloomy* or *devastated*, forget them in days, and when I speak I only say *sad*."

Solved means that tomorrow I can recall more of these words than I could from a list, and I know which one fits: *upset* when talking to a friend, *disappointed* anywhere, *dejected* when I read sports news, and *sorrowful* only in a poem. I can also build a silly story for my own next word group.

## Beat survival (task item 1): all six beats are present and IN ORDER. Nothing was scrambled. One spoken cue was dropped (the comment CTA).

| # | Required beat | Heard (whisper, s) | On screen (s) | Result |
|---|---|---|---|---|
| 1 | Hook ≤15 s, two scores | 0.00–14.52: "10 words for sad. How many can you remember? We'll do a quick test, then I'll show you one trick, just a single, silly story, and we'll test you again. You'll also learn exactly when to use each word. So grab a pen. You're getting two scores today." | 0–3.54 title card "Synonym Challenge: SAD" (girl in the rain). 3.54–15.08 "Grab a pen! You are getting two scores." | OK: 14.5 s, the full promise, and the pain question lands in the first 3 s. |
| 2 | Plain list of 10, in order | 15.28 "First up, the plain list. Just read and listen." 18.80–29.46: melancholy, upset, blue, heartbroken, gloomy, disappointed, devastated, down in the dumps, unhappy, miserable (about 1.2 s each). The main transcript shows "Unhappy. Unhappy." at 27.98–28.52, but the isolated clip shows it is said only once, so this is a whisper artefact. | 15.08–30.13 card "10 Plain Words" with all 10 at once, in the correct order, with no meanings and no pictures (a magnifier doodle only). | OK. The words are shown all at once rather than about 2 s each. That is acceptable, because it is still a plain list. |
| 2b | Spoken pause cue plus 3 s silence | 30.34 "Pause the video now." 31.80–33.16 "Write down every word you remember." 34.06 "Okay." 35.72 "All done? Count them up. That right there is score number one. Your list score. Keep it safe." | 30.13–42.29 card "Write down every word you remember. List Score" with a pause icon | The cue is present. **The hold is 1.03 s** (silence 33.20–34.23), then "Okay", then 1.24 s (34.78–36.02). There are never 3 s of continuous silence. |
| 3 | ONE story, 15 words, mildest to strongest | Set-up 42.54–56.94 (includes "roughly from a little bit sad to extremely sad", "don't worry, it ends well"). Word onsets: blue 57.86, disappointed 72.58, glum 86.00, unhappy 102.32, down in the dumps 122.10, gloomy 134.84, upset 154.44, melancholy 172.30, dejected 191.64, forlorn 211.20, miserable 227.22, sorrowful 243.64, heartbroken 260.56, devastated 274.16, inconsolable 293.68. Happy ending 308.18–314.40 ("your dog comes home, bringing the cat, and a brand new birthday cake. Hey, it's only a story."). | One card per word: a word title plus a one-line meaning on a green caption card, with a scene drawing behind it. Scene cuts at 72.13, 85.79, 102.00, 121.67, 134.38, 154.08, 171.88, 191.33, 210.96, 226.75, 243.17, 260.08, 273.71, 292.96, each 0.2–0.7 s before the spoken word. | **Exact script order, nothing merged or skipped.** The plot is continuous (birthday, dentist card, cake contest, dump, goose, goat judge, park bench, home, poem, dog next door, storm, river of tears, dog returns). Exceptions are listed under the defects: the Blue card appears 15.6 s early (42.29), dejected has no picture, and the "you" character changes between a girl and a man. |
| 4 | Second pause (recall in order) | 315.30–319.70 "Pause the video again, write down every word you can recall, in order." 320.46–327.36 tip: "walk through the story again in your head. The gray sky, the dentist's card, the cold cereal." 329.80 "All done? Count them up. That is score number two, your story score." | 315.12–335.21 card "Write down every word you recall in order. This is your story score." with a pause icon | The cue is present. **The hold is 2.63 s** (silence 327.51–330.14), after the tip. There is only 0.76 s between the cue and the tip. Close to the target, but still short. |
| 5 | "15 not 10" reveal plus ladder recap | 335.32 "Now here's the sneaky part. I gave you 15 words, not 10. Glum, dejected, forlorn, sorrowful, and inconsolable. Did any of those make it onto your list?" 347.16–430.74: spoken recap of all 15, in order, with the script's labels. | 335.21–347.17 chalkboard with the 5 extras (correct; there is no "15, not 10!" headline, but the voice covers it). **347.17–431.29 one static table with only 8 rows** (see below). | The beat is present and the voice is correct. **The table is incomplete.** |
| 6 | Comment two scores, transfer, site | 431.98–433.02 "List versus story." 434.16–438.80 "Tonight, try it with your own new words. One silly story, one picture for each word." 439.80–444.30 "For more words, look up another word for sad on anotherwordfor.net." | 431.29–433.67 two empty panels "Your List Score" and "Your Story Score". 433.67–439.46 "Try it with your own new words: one silly story, one picture for each." 439.46–444.96 "Look up another word for Sad on anotherwordfor.net." | **"Comment your two scores" and "which score was higher?" were both DROPPED** (confirmed on the isolated clip 426.8–434.8). "List versus story." hangs without a verb. The transfer line and the site line are OK: there is no promise of a search box or examples, and the on-screen text matches the voice. |
| – | End | – | **444.96–448.05 full-screen "Gemini Notebook" end card** | Brand violation |

**No beats were dropped or scrambled** (the CTA cue lost its key sentence, but the beat position survives). The runbook trigger "ask_user about our own renderer" (dropped or scrambled twice) does **not** apply.

## Accuracy for B1 (task item 2)

The story voice-over, as heard. Every meaning and register matches the gated script:
- blue: "informal for a little sad ... I'm feeling a bit blue". Correct.
- disappointed: "sad because something just wasn't as good as you hoped". Correct.
- glum: "quiet and a bit sad. And it really shows on your face. It's a bit informal." Correct (Cambridge informal).
- unhappy: "not happy ... unhappy with something ... not satisfied ... the customer was unhappy with the service". Correct.
- down in the dumps: "Literally." (confirmed on the clip) "an informal idiom meaning unhappy and low". Correct. It makes no claim about where the idiom comes from.
- gloomy: "sad and without hope ... a gloomy day". Correct.
- upset: "unhappy because something bad has just happened ... very common in everyday speech ... don't be upset". Correct.
- melancholy: "a quiet, deep sadness that stays with you, and you can't always explain why. It's a literary word, so it's very common in books and songs". The meaning is correct. "so" is a slightly odd causal link, but harmless.
- dejected: "unhappy and disappointed, especially after you tried and failed ... sports news, the dejected players". Correct.
- forlorn: "alone and sad. Almost as if nobody cares ... another literary word". Correct.
- miserable: "very unhappy, often because you're cold, wet, tired, or uncomfortable ... everyday ... miserable weather". Correct.
- sorrowful: "very sad. But it's old-fashioned and literary ... poems and old stories. Definitely not for a quick chat with friends." Correct.
- heartbroken: "extremely sad, usually because someone or something you love is gone". Correct.
- devastated: "extremely upset and shocked when something very bad happens ... super common in speech ... we were devastated when we lost the final". Correct.
- inconsolable: "so sad that absolutely nobody can make you feel better". Correct ("The top of the ladder" was dropped; the recap says "And finally").

The recap voice (357–431) follows the script's Beat 5 labels line by line. There is one spoken error:
- **419.92–421.24: "Heartbroken, extremely sad. Someone or someone you love is gone."** This should be "someone or something". The isolated clip hears the same thing, so it is very likely a real NotebookLM slip. Ear check it, but plan the splice (fix 5).
- "Literary, pokes and songs" (395.2) is heard on the clip as "Books and songs". That is fine. "Every day, also for weather" is "Everyday" (whisper punctuation only).
- No label is stronger than in the script. There is no "very informal" and no "only in writing". Blue and down in the dumps are never called formal, and melancholy, forlorn and sorrowful are never called casual.

Memory claims: **clean.** There are no statistics, no "most people", no "10x", no researchers, no age of the method, and no "came only from the story" (the voice asks "Did any of those make it onto your list?"). There is no depression, illness or death (a sneeze and a broken heater only). The dog comes back, so there is a happy ending.
NotebookLM additions: "Keep it safe", "Hey, it's only a story", "yep", "super common", "Literally". All are harmless and natural, and none is a stage direction read aloud (the S1 "continuous whiteboard drawing" problem did not recur). There is no "say it with me" drill. The pronunciation of melancholy, forlorn and inconsolable was **not** checked by a human ear.

## On-screen text, watermark, voice/picture match (task item 3)

- **The ladder table (347.17–431.29, 84 s, SHIP-BLOCKING)** has 8 rows only: Blue / A little sad / Informal · Disappointed / Hopes not met / Neutral · Gloomy / Without hope / Neutral · Upset / Bad event / Speech · Melancholy / Deep sadness / Literary · Miserable / Very unhappy / Everyday · Heartbroken / Love is gone / Neutral · Devastated / Shocked / Speech.
  - **Missing rows (7): glum, unhappy, down in the dumps, dejected, forlorn, sorrowful, inconsolable.** That is all 5 extras (the point of the reveal) and the top of the ladder. While the voice says "Glum, quiet and a bit sad" (365.8), "Unhappy" (371), "Down in the dumps" (376.3), "Dejected" (396.5), "Forlorn" (401.7), "Sorrowful" (411.3) and "And finally, inconsolable" (427.5), the screen does not show those words at all. The voice and the screen disagree for about 40 of the 84 s.
  - Weak cells: "Upset: **Bad event**" is a cause, not a meaning. "Heartbroken: **Love is gone**" reads as "the love has ended" (it is narrower than "someone or something you love is gone"). "Devastated: **Shocked**" loses "extremely upset". "Gloomy: Without hope" loses "sad". The labels "Speech" and "Everyday" are fine.
  - There are no duplicates, no non-words and no wrong order among the 8 rows that are shown (the order is ladder order minus the missing rows). There is no bottom-to-top layout: blue is at the top of the table. That is acceptable if the rebuilt table's heading says "a little sad → extremely sad".
  - There is faint ghost text "sorrow · loneliness" at the bottom left (about x 75–215, y 660) on the table and on the dejected card. It is barely visible and harmless, and the new overlay covers it anyway.
- **Score card (431.29–433.67):** two empty panels "Your List Score" / "Your Story Score". There is no "comment" anywhere on screen, and it lasts only 2.4 s.
- Story caption cards: all 15 word titles are spelled correctly, and each one-line meaning matches the voice. Legibility issues (all readable, none clean):
  - glum (85.8–102): the end of the line "your face. A" runs over the dog drawing.
  - forlorn (211–226.7): "nobody cares. A literary word." is crossed by the bench legs.
  - inconsolable (293–315): the title is overlapped by the tissue box and the cake.
  - down in the dumps (121.7–134.4): the card covers almost all of the dump picture, and only a small figure on bin bags is visible at the right.
- **dejected (191.33–210.96): NO picture.** The card sits on a blank, faded background, so the goat judge holding up "0" is heard but never seen. This is the only one of the 15 words with no image, and it is an extra (one the viewer never saw in the list), so it most needs the picture.
- The Blue card (with the girl at a rainy window) is up from **42.29**, while the voice is still on the set-up until 57.86. For 15.6 s the picture is ahead of the voice. The other 14 words line up within 0.7 s.
- The protagonist is not consistent: a girl for blue, unhappy and upset, a man in a coat for melancholy and miserable. This is a minor continuity break in a "one story about YOU".
- The on-screen stress cues from the script (MEL-an-chol-y, for-LORN, in-con-SOLE-a-ble) were not drawn. Nothing wrong is shown, but the cue is missing.
- The reveal chalkboard has the 5 extras but no "15, not 10!" headline. That is OK, because the voice says it.
- **Watermark: "Gemini Notebook" is in the bottom-right corner of EVERY frame** (about x 1155–1275, y 695–715 at 1280x720), including the table and the CTA cards.
- **Full-screen "Gemini Notebook" end card from 444.96 to 448.05.** The CTA audio ends at 444.30, and 444.28–448.05 is silent.

## Second by second: where a viewer would swipe away

- 0:00–0:03: "10 words for sad. How many can you remember?" Strong: this is my problem, as a question. The picture is a generic title card, which is fine for 16:9.
- 0:03–0:15: the hook promise, "grab a pen". OK.
- 0:15–0:30: the list. Fast (about 1.2 s per word) but readable, because all 10 stay on screen for 15 s.
- 0:30–0:42: **the pause cue with no real pause.** "Write down every word you remember." is followed 0.9 s later by "Okay ... All done?". Anyone who doesn't hit pause has no time to write, so score 1 is never collected, and the comparison (the whole hook) collapses. This is the biggest engagement leak together with the missing CTA.
- 0:42–0:58: set-up talk while the Blue card is already up. This is a mild drop risk (15 s before the first story word), but it is shorter and cleaner than in S1.
- 0:58–5:14: the story, at about 13–20 s per word. It is funny and concrete (dentist card, goose, goat judge, a poem to a cake, the roof flying off like a hat), and every card changes on the word. The weak spots are the dejected blank card (3:11–3:31) and the down in the dumps card, which hides its picture.
- 5:15–5:35: the second pause is better (2.6 s of silence after the tip), but the tip itself fills the moment when you should be writing.
- 5:35–5:47: the reveal is a genuine "aha" moment, and the card is correct.
- 5:47–7:11: **84 s on one static, incomplete table.** It is slow, and a careful viewer will notice that glum, dejected, forlorn, sorrowful and inconsolable (the words just "revealed") are not on it. This is the likeliest late drop and the likeliest "you forgot half" comment.
- 7:11–7:13: "List versus story." It never asks me to comment, so I don't.
- 7:14–7:24: the transfer line and the site. Clear.
- 7:25–7:28: the Gemini end card.

## Takeaway test

After watching I can use *upset* and *disappointed* in speech, recognise *dejected* in sports news, keep *sorrowful*, *forlorn* and *melancholy* for books, songs and poems, and **tonight build one silly story, with one picture per word, for my own new words**. That line is spoken at 434–438 and drawn. It is a real, nameable action that addresses the P01 pain (forgetting). The S1 gap is closed. The missing half is the social action: without "comment your two scores" the viewer compares privately, if at all.

## Retention risks

- Length is 7:28 (7:25 after trimming the end card, and about 7:31 with the pause freezes). That is just over the 5–7 min target. The story carries it, and the 84 s table is the drag.
- Pacing: the story is steady. The 0.9 s pause-1 hold defeats the self-test.
- Picture/voice sync: excellent within the story (14 of 15 within 0.7 s). It breaks for the early Blue card and for about 40 s of the table.

## Trust risks

- The table leaves out the 5 words the video just called "sneaky extras". Viewers will read this as sloppy.
- "someone or someone you love is gone" (7:00) is an audible slip.
- The Gemini watermark and end card mark the video as AI-generated from a notebook and break the brand rule.
- The facts and registers are otherwise clean. There are no memory statistics.

## Defects and fixes (task item 4)

### Ship-blocking (all can be fixed in post, no regeneration)

1. **Watermark and end card (shorts-builder).** Trim at **444.8 s** (the CTA audio ends at 444.30, and the end card starts at 444.96). Cover the bottom-right "Gemini Notebook" mark (about x 1150–1280, y 690–720) on every frame with the channel logo `state/brand/awf-logo-channel.jpg` or a background-matched patch.
2. **Incomplete ladder table, 347.17–431.29 s (visuals, then shorts-builder, then a language-editor re-gate).** Put a full-frame overlay of our own **15-row** ladder over the whole span, in script order (blue to inconsolable, with a heading "a little sad → extremely sad"). Each row is word · meaning · when, using the script's Beat 5 labels exactly (for example "Upset · unhappy because something bad just happened · very common in speech", "Heartbroken · someone or something you love is gone", "Devastated · extremely upset and shocked · speech and news", "Sorrowful · very sad · old-fashioned, literary: poems"). Mark the 5 extras. Reuse the S1 polish builder (`content/specials/S1/polish-v2-build/ladder.py`, per-row highlight frames). Highlight each row as the voice reaches it, at these onsets: blue 357.36, disappointed 361.24, glum 365.80, unhappy 371.04, down in the dumps 376.28, gloomy 381.18, upset 385.40, melancholy 390.54, dejected 396.48, forlorn 401.66, miserable 405.96, sorrowful 411.26, heartbroken 417.02, devastated 422.06, inconsolable 427.46. Patching cells is not enough, because 7 rows are missing.
3. **Missing comment CTA, 431.29–433.67 s (shorts-builder, with a language-editor check of the text).** Freeze the "Your List Score / Your Story Score" frame for **+3 s** (from 433.0, after "List versus story.") and overlay large text: "Which score was higher? Comment your two scores: list vs story." There is no spoken "comment" anywhere in the audio, so a voice splice is impossible. Do not insert a different TTS voice. Back it up with a pinned comment ("List: __ / Story: __ ?") at publish time (publisher). The description already asks for it.
4. **Pause holds (shorts-builder).** Insert a silent **3 s freeze** of the pause card at **33.2 s** (after "remember.", before "Okay"), and a **2.5 s freeze** at **327.5 s** (after "the cold cereal", extending the existing 2.63 s silence to about 5 s). An alternative for pause 2 is 3 s at 319.75 (straight after "in order."). That adds about 5.5 s in total.

### Non-blocking (recommended, in post)

5. **Spoken slip at 419.92–421.24 ("Someone or someone you love is gone") (shorts-builder, then language-editor ear check).** Replace it with the same narrator's correct phrase from the story, **271.24–273.10** ("someone or something you love is gone", 1.86 s against 1.32 s). There is room, because 421.24–422.06 is a pause before "Devastated". Use a short crossfade (about 20 ms) at both ends. As a minimal alternative, swap only the second "someone" (420.34–420.56) for "something" (271.86–272.22).
6. **The dejected card has no picture, 191.33–210.96 (visuals).** Draw a panel: a serious goat in a chef's hat holding up a "0" card, and "you" walking away with your head down. Place it in the free space right of or above the caption (the card leaves about x 1000–1280 and the upper half empty).
7. **The Blue card is early, 42.29–57.86 (shorts-builder).** Hold a frame of the pause-1 card, or a plain "One story. 15 pictures." card, until 57.8, so that "Blue" appears on the word.
8. Legibility scrims (visuals): glum at 85.8–102 (the line end over the dog), forlorn at 211–226.7 (the text crossed by the bench), inconsolable at 293–315 (the title overlapped by the tissue box).
9. Optional on-screen stress cues (visuals, then language-editor): "MEL-an-chol-y" at 172.3–191.3, "for-LORN" at 211.2–226.7 and "in-con-SOLE-a-ble" at 293.7–315.1. Keep them small and near the word title.
10. For S3–S5 (scenario-writer, focus.txt): NotebookLM again summarised the table to a subset, and it dropped the one sentence with "comment". Add to focus.txt: "The recap table must have exactly 15 rows", and "Say the exact sentence: Which score was higher? Comment your two scores: list versus story." Plan the table overlay and the pause freezes in polish anyway, because this is the second video where they failed.

After fixes 1 to 4 (ideally with 5 and 6), this should reach **SOLVES**. Re-run the critic on the polished file.

## Not checked

- No human listening. The "someone or someone" slip, the pronunciation of melancholy, forlorn and inconsolable, and "Books" (395) are whisper small.en readings (the slip was confirmed on an isolated clip).
- Frames were sampled every 5 s, plus scene changes and 23 full-resolution frames. A defect lasting less than about 3 s between samples could be missed.
- meta.json was not re-audited (it was gated at 11:16Z). The title "Can You Remember 15 Synonyms for SAD?" spoils the "15, not 10" reveal slightly, as the gate already noted.
- The anotherwordfor.net SSL status was not re-checked in this step (the gate recorded the certificate as expired, with a browser warning).
