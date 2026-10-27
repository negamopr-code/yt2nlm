# Viewer-critic review: h114-said-v1 (lab H114, Stop Saying "said": whispered / replied / explained)

Reviewed 2026-10-27. File: /workspace/glottos-marketing/state/shorts/h114-said-v1/final-sub.mp4 (md5 8436856d..., 1440x2560, 30 fps, 17.30 s, kokoro am_michael 1.05, no music). Unit: shorts/units/h114-said-v1.json (language approval hash e97b7fd190c97ffd). Meta: content/youtube/h114-said-v1.json.
Checked: faster-whisper small.en transcript with word timings, ffmpeg silencedetect (-40 dB, 0.3 s), 19 frames from 0 to 16.2 s plus the loop frame at 17.0 (hook at 0/0.5/1.0/1.5 s, every beat), full-resolution crops of the Replied and Explained pictures. Not checked: listening by ear, the thumbnail, YouTube rendering.
Pain evidence: I spent no NotebookLM query. content/problems/ does not exist, and content/insights/audience-needs.md has no learner quote about "said" or about overusing basic words (the same gap as the H102-H113 reviews). Note: the journal (line 1023) lists H114 as "drop 'very'", but the unit and the brief say "plain overused word 'said'". Pain (the brief's, NOT verbatim): "I always use the same basic word; give me better ones." Solved means that tomorrow I write or tell a story with "he explained" or "she whispered" where it adds something, and I still know that "said" is fine.

## Verdict: PARTLY
The three words and example sentences are correct, but the headline teaches something false ("said" is the normal, correct reporting verb, and these three words do not replace it; they add meaning), two of the three pictures do not match their words, and about 7.7 s of the 17.3 s is silence.

## Ship blockers
1. POLICY (doubt = block): Replied beat, 9.0-12.0 s. The picture is a drawn Black man in a grey suit, with a US flag and a judge's gavel, while the voice says "Yes, I can". Many viewers will read this as a reference to a real politician and his "Yes we can" slogan. It is not named, but with that line the doubt is real. It is also simply the wrong picture: a courtroom, nobody is replying to anyone. Owner: visuals (two people talking, one answering; no flag, no gavel). Or scenario-writer changes the line, e.g. "'Yes, I'm free,' he replied."
2. MAGNIFYING GLASS THAT DOES NOT ZOOM (user rule 2026-10-05): Explained beat, 13.0-16.3 s. The lens over the light bulb is an empty grey circle; it does not enlarge anything. The picture (light bulb, book, gears) also has nothing to do with "The bus was late," he explained. Owner: visuals (e.g. a late boy at a door talking to a teacher, a bus behind him; no lens).
- No spelled-out word: "said" 0.70, "Whispered" 4.20, "Replied" 7.78, "Explained" 12.10 are each heard as whole words.
- Subscribe + bell: present. The pill appears at about 11.3 s, the click and "SUBSCRIBED" plus the bell by about 13 s, gone by about 16.3 s (second half of a 17.3 s video). final-sub.subscribe.json says [11.3] and the meta's "subscribe_at" is [11.3]; the meta note calls it a placeholder copied from h112, but it matches this render. OK. Minor: at 11.5-16 s the pill and the bell sit over the bottom-left corner of the Replied/Explained pictures.
- No NotebookLM/Gemini watermark seen. The logo is the channel avatar (top-left, "anotherwordfor.net / STOP SAYING"). Render is 1440 wide. OK.
- Nothing sexual, no profanity, safe for 13+ apart from blocker 1.

## Pain -> gives -> gap
- Gives: whispered ("Be quiet," she whispered), replied ("Yes, I can," he replied), explained ("The bus was late," he explained). Each word is spoken, on the card, and in a quoted example.
- Gap 1 (trust, the big one): "Stop saying said" is wrong advice. "Said" is the standard, neutral word, and good writers use it most of the time. Whispered/replied/explained are not "better"; each one adds information (quiet voice / an answer / a reason). A learner who believes the video will write "he explained" for every line, which sounds odd. One line fixes it: "Said is fine. Use these when you want to show HOW."
- Gap 2: the examples are dialogue tags with quotation marks, which is a written-story form. B1-B2 learners mostly speak. The speaking form ("He explained that the bus was late", "She told me to be quiet") is never shown. Also, by ear the quotes disappear: I hear "Whispered. Be quiet, she whispered." and the voice does not whisper, so the picture-in-sound is missing.
- Gap 3: no moment where I test myself.
- Gap 4: the most common "said" mistake for learners (said vs told: "he said me") is not touched. This is my knowledge as a reviewer, not a quote on file.

## Second by second (heard / seen)
- 0.00-1.06 "Stop saying said." Frame 0: "Stop saying" plus "said" struck in red. Clear, and the voice matches the screen. "3 better words" is NOT on screen at 0-1.5 s; it appears at about 2.5 s, after the voice has already said it.
- 1.14-1.73 0.59 s silent.
- 1.68-3.26 "Here are three better words." Filler that repeats the card.
- 3.28-4.07 0.79 s silent, static hook card (swipe point 1, about 3-4.2 s of no new information).
- 4.20 "Whispered." / 4.75-5.53 silent; at 5.0 s the screen is the headline only, no sentence, no picture. 5.42-6.66 "Be quiet, she whispered." The woman with a finger on her lips (shh) matches. Good picture.
- 6.77-7.88 1.12 s silent (swipe point 2).
- 7.78 "Replied." / 8.57-9.40 silent / 9.34-10.96 "Yes I can, he replied." The man in a courtroom with a flag and gavel does not show replying (see blocker 1).
- 11.01-12.12 1.11 s silent (swipe point 3). The subscribe pill appears here.
- 12.10 "Explained." / 12.89-13.70 silent / 13.62-15.32 "The bus was late, he explained." Light bulb plus a non-zooming lens; no bus, nobody late (see blocker 2).
- 15.61-17.31 1.70 s silent tail. The loop frame (17.0) is the hook card, which matches frame 0. Fine for the loop, but it is almost 2 s of nothing.
- The background word wall (whispered/replied/explained, large and faint, plus small logo tiles) is clutter behind the headline and makes the hook card busy. Readable, but noisy.
- Card text is large and readable in time; each sentence stays 2-3 s.

## Takeaway test
I can write "'Be quiet,' she whispered" in a story tomorrow. That is a real but narrow action (writing fiction-style dialogue). For speaking, I get nothing I can use directly, and I may wrongly stop using "said". So PARTLY, not SOLVES.

## Retention risks
- Silence: about 7.7 s of 17.3 s (0.59+0.79+0.78+1.12+0.83+1.11+0.81+1.70). The content fits in about 10-11 s.
- Each word is said twice (alone, then at the end of the sentence) with a 0.8 s hold between, and the sentence and picture arrive about 1.5 s after the headline. The first half of every beat is a bare headline.
- "Here are three better words" is 1.6 s that repeat the card.
- As a lab arm (ONE change = the word, H112 container), this is a fair comparison with H112, which had the same holds. Absolute retention will be low again.

## Trust risks
- The headline claim "Stop saying said" is false as language advice (Gap 1). Native viewers and teachers will say so in the comments.
- Replied picture: political/courtroom reading (blocker 1). Explained picture: a generic "idea" image with a fake magnifier (blocker 2). Two of three pictures contradict or ignore the words.
- The English in the three sentences is natural and correct.

## Top 3 fixes (by impact)
1. visuals: replace the Replied picture (two people, one answering; no flag, no gavel, no recognisable public-figure look) and the Explained picture (a late student explaining, a bus in the background; no magnifying glass). Owner: visuals, then shorts-builder re-renders.
2. scenario-writer (then the language-editor gate): make the claim honest. Hook sub "3 words that say HOW" or a 1 s line "Said is fine - these show how"; add the speaking form to one beat ("He explained that the bus was late."); optionally end with a 1 s self-test ("'Sorry, I'm late,' he ___." -> explained). Consider "said vs told" as its own unit.
3. shorts-builder: cut the holds to 0.3-0.4 s and the tail to 0.5 s (target about 11 s); show the sentence and picture on the same frame as the headline; put "3 better words" on frame 0; keep the subscribe pill off the picture (move it below the picture frame).

## Re-check (2026-10-27, after the visuals fixes)
File: state/shorts/h114-said-v1/final-sub.mp4, md5 c72b3cd2fc6f676950766592d452fb73 (new render, 09:53), 17.30 s. Checked: 12 frames (0, 0.5, 1.5, 5.5, 6.5, 9.5, 10.5, 11.5, 12.5, 14, 15, 16.5 s), full-resolution crops of the Replied and Explained pictures, a new faster-whisper small.en transcript with word timings, silencedetect (-40 dB, 0.3 s). Not checked: listening by ear, the thumbnail.

**Verdict: PARTLY** (unchanged). Both ship blockers are cleared. The video still teaches "stop saying said", which is wrong advice, has about 7.7 s of silence and no self-test, so it does not yet change what I do tomorrow beyond writing story dialogue.

- Blocker 1 (POLICY, Replied 9.0-12.0 s): CLEARED. The picture is now a tight crop of the man in a grey suit: no flag and no gavel. Only a wooden bench edge and a chair are left at the right edge, and they read as an office. I no longer see a strong public-figure cue. A small risk stays because a lone man in a suit says "Yes, I can". To remove it fully, the scenario-writer can change the line (e.g. "Yes, I'm free"). Not a block. The picture still does not show *replying*: one person and nobody to answer.
- Blocker 2 (magnifying glass, Explained 13.0-16.3 s): CLEARED. It is now just the light bulb with swirls and no lens. It is a generic "idea" picture with no bus and nobody late, so it matches the word only loosely. Not a blocker.
- Audio is the same as v1: "Stop saying said" 0.00-1.06, "Whispered" 4.20, "Replied" 7.82, "Explained" 12.14. No word is spelled out letter by letter. Silences: 0.59 + 0.79 + 0.78 + 1.12 + 0.83 + 1.11 + 0.81 + 1.70 = about 7.7 s.
- Subscribe + bell: the pill appears at about 11.3 s and shows SUBSCRIBED + the bell by about 14 s. It still covers the bottom-left corner of the Replied/Explained pictures. final-sub.subscribe.json = [11.3]. OK.
- Logo is the channel avatar, there is no NotebookLM/Gemini watermark, render is 1440 wide, nothing sexual. OK.
- Still open (fixes 2 and 3 of the first review, not started): scenario-writer should make the claim honest ("said is fine, these show HOW"), add the spoken form and add a 1 s self-test. shorts-builder should cut the holds and the 1.7 s tail (target about 11 s), put "3 better words" on frame 0 and move the subscribe pill off the picture.
