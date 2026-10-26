# Viewer-critic review: l3-because-v1 (Say It Like a Native, EP 8, lab H21)

Reviewed 2026-10-03. Video: `state/shorts/l3-because-v1/final.mp4` (29.88 s, 1080x1920, 30 fps, words only).
Unit: `shorts/units/l3-because-v1.json`. YouTube text: `content/youtube/l3-because.json`.
Siblings glanced at (frames only): `state/shorts/l3-in-conclusion-v1/final.mp4` (31.99 s), `state/shorts/l3-congratulations-v1/final.mp4` (28.00 s).

## Verdict: PARTLY

I get five real replacements, each in a correct, natural sentence, in 30 s with a clean layout. But the video tells me "don't say because, say this" and never tells me that two of the five cannot be dropped into a "because" sentence, nor which ones are for an essay and which for a chat, so tomorrow I can use three of them safely and will probably misuse the other two. On top of that the first answer word, "Since.", is not read cleanly (see ship blocker).

## Ship blockers: 1

1. **"Since." headline (3.51-4.04 s) is not a clean "since".** faster-whisper small.en could not recognise it in three attempts: "zenta" (p=0.45) in the final video, "Center" (p=0.28) on `b02-0.wav` alone, "ZENZO" (p=0.30) on the same clip padded with silence. The same voice's "since" inside the example sentence is recognised (p=0.84), and every other headline is recognised. The waveform of `b02-0.wav` shows why: s (0.06-0.15 s), vowel (0.18-0.27), n (0.30-0.36), a very short weak final s (0.39-0.44, -31 dB), and then about 150 ms of low-frequency voiced sound at -26 dB (0.45-0.60 s) after the word should have ended. It reads as "sins-uh" / "sin-ta". "As." has no such tail (the s decays straight into silence).
   Caveat: this is measured, not heard. I have no ears; someone must play `state/shorts/l3-because-v1/b02-0.wav` once (0.75 s). If it sounds like a plain "since" to a human, this blocker is void and the count is 0.
   Fix (voice / shorts-builder): cut the tail after ~0.45 s with a short fade and pad with silence to keep the 0.75 s length, or splice the same voice's own "Since" from `b02-1.wav` (0.00-0.33 s), or regenerate the headline. It is the first answer of a series called "Say It Like a Native"; it should not ship garbled.

Not a spelled-out word: no word in the video is read letter by letter.

## Pain

Evidence is thin and I am saying so. There is no PROBLEM NN document, article or format file for this theme, and `state/corpus-glottos-niche/raw` contains no learner line about replacing "because" (searched for other way / another word / instead of / synonym together with "because": 0 hits). The only verbatim corpus line that states the neighbouring pain is the one already used for the "Stop saying" lane:

- "I can understand what you say clearly , the point is that when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"

The real basis is search demand, per H21 in `/workspace/glottos-auto/out/lab/lab.json`: 'another word for because' +50 %, 'other ways to say because' a top query (28), both in YouTube autocomplete. No NotebookLM query was spent.

Pain in the searcher's words: "other ways to say because" - I use "because" in every sentence (probably in an essay, it is essay season) and want replacements.
Solved would mean: tomorrow I write or say a sentence with one of them and it is correct and fits the situation.

Pain -> what the video gives -> gap:
- Gives: since, as, due to, thanks to, seeing as; one model sentence each; all five sentences correct and natural.
- Gap 1 (grammar): "since / as / seeing as" replace "because" (+ clause). "Due to / thanks to" replace "because of" (+ noun). The video frames all five as swaps for "because". The examples are correct ("due to fog", "thanks to you") but a B1 learner does not infer a rule from one example; the predictable output is "I was late due to I missed the bus". The note exists only in the description, which most Shorts viewers never open.
- Gap 2 (register): the winner template had a register label under each word; this version replaced it with the example and lost it. "Seeing as" is chatty and wrong in an essay; "due to" and "as" are formal/written. A searcher in essay season needs exactly this and gets nothing.
- Gap 3 (meaning): "thanks to" is for a good result (or irony). Not said in the video or the description.
- Gap 4: "Don't say because" is an overclaim. "Because" is correct everywhere. Template wording, accepted for the lab, but a learner may take it literally.

## Is the "due to / thanks to + noun" point a ship blocker? No.

Nothing on screen or in the voice is wrong, the examples model the right pattern, and the description carries the rule. For a 48-hour lab test of H21 (trend phrase + search title) it can ship. But it is the main reason the verdict is PARTLY and not SOLVES, and it must be fixed in the next version and in any long video made from a winner: it costs three characters on the card ("+ noun").

## Check 1: hook in the first 2 s - PASS

- 0.00-0.10 s "Don't say" alone; by 0.20 s yellow "Because" in quotes is on. Voice "Don't say because" 0.00-1.07.
- Red strike drawn between 1.4 and 1.6 s.
- "Say this instead" on from ~1.8 s, voice 1.70-2.69. Readable (on screen ~1.7 s).
- 2.69-3.51 s silence on the hook card (0.8 s). Slightly long.
- First answer "Since" on screen at ~3.5 s, spoken 3.51 s.
- As a scroller: yes, I stop; it names a word I overuse and the strike says a list is coming. "1 / 5" confirms it.

## Check 2: beats

| # | t (s) | Headline | Example on card | Readable / inside safe area | Note |
|---|---|---|---|---|---|
| hook | 0.0-3.5 | Don't say "Because" (struck) | Say this instead | yes | |
| 1 | 3.5-8.0 | Since | Since it's late, let's go home. | yes | headline audio defect (blocker) |
| 2 | 8.0-12.3 | As | As it was raining, we stayed in. | yes | |
| 3 | 12.3-16.9 | Due to | The flight was late due to fog. | yes | needs "+ noun" |
| 4 | 16.9-21.7 | Thanks to (wraps to 2 lines) | Thanks to you, we finished early. | yes | needs "+ noun"; positive only |
| 5 | 21.7-26.6 | Seeing as | Seeing as you're here, let's start. | yes, widest line: x 78-1003 of 1080 | informal, not labelled |
| CTA | 26.6-29.9 | Which one will you try today? | Write it in the comments. | yes, lowest text y=1045 | |

- Nothing is cut off. Measured foreground text bounds: left >= 78 px, right <= 1003 px, lowest content y = 1045 of 1920 (CTA). The whole lower 45 % of the frame is empty apart from the dim word cloud, so the YouTube caption/buttons zone is clear. Brand header starts at y = 56; YouTube's own top bar may sit over it on some phones (brand only, no content; same as the template).
- Headline appears alone for ~1.2 s, then the example appears together with the spoken example. Text and voice are in sync on every beat.
- Example sentences stay on screen 2.8-3.0 s each (appear at speech start, held through the 1.2 s pause). Enough for 6-7 words at B1.
- Orphans: "home.", "fog.", "start." sit alone on a second line. Cosmetic.
- Background word cloud: dim, but it shows all five answers from second 0 (spoils the list) and at 12.3-16.9 s a cloud "thanks to" / "seeing a" sits directly behind the yellow "Due to". Still readable in this video.
- No pictures, so no watermark risk; none seen.

## Check 3: audio

Heard (faster-whisper small.en, word timings, final video): "Don't say because, say this instead, [zenta], since it's late let's go home, as, as it was raining we stayed in, due to, the flight was late due to fog, thanks to, thanks to you we finished early, seeing as, seeing as you're here let's start, which one will you try today."

- "As." (7.96-8.29 s, clip 0.53 s): fine. Recognised "as" p=0.98 in the video, 0.73 alone. Vowel ~0.2 s, final fricative ~0.1 s, clean decay, not clipped at either edge. Short, but it is a short word. Not verifiable by me: whether the final sound is z or s.
- "Since." : see ship blocker. Not clipped (the clip starts and ends in silence); the problem is an extra sound after the word.
- "Due to." recognised in the video (p=0.82/0.88); alone whisper wrote "Do too", which is the same sounds. Fine.
- "Thanks to.", "Seeing as." fine.
- All example sentences and the CTA match the approved unit text word for word.
- No word spelled letter by letter.
- Pauses: 1.12-1.30 s after each headline and after each example; consistent. Tail: 1.76 s of silence on the CTA.
- Levels: mean -27.7 dB, peak -4.7 dB. No music.
- Not checked: LUFS; everything "by ear" (I only have transcript, probabilities and waveform measurements).

## Second-by-second swipe risks

- 0.0-2.7: clear, my word, struck out. I stay.
- 2.7-3.5: 0.8 s of nothing new. Small risk.
- 3.5-5.2: "Since" alone on black for 1.2 s after a smudged reading. First real risk; the same silent gap repeats at 8.3, 12.9, 17.6, 22.5.
- 8.0-12.3: "As". A learner who knows "as" only as "like / while" may be confused, the example saves it.
- 12.3-21.7: two answers that are not swaps for "because". No swipe risk, but this is where the wrong lesson is learned.
- 26.6-29.9: CTA with 1.76 s silent tail; I am gone at 28.

## Takeaway test

One action: tomorrow, start a sentence with "Since ..." or "Seeing as ..." instead of "..., because ...". Nameable, so PARTLY rather than DOESN'T. Not SOLVES: 2 of 5 need a rule the video hides, none of the 5 says where it fits (essay vs chat), there is no self-test, and the first word is read badly.

## Retention risks

- Length is right for five items (29.9 s). About 9 s of it is silence between headline and example and at the tail.
- Five identical beats, identical rhythm, no picture; nothing changes after the hook.
- No recall moment.
- Word cloud reveals the answers at second 0.

## Trust risks

- "Since." pronunciation (blocker).
- "Don't say because": overclaim.
- Due to / thanks to presented as replacements for "because" with no "+ noun" on screen.
- No register: "seeing as" next to "due to" as if interchangeable.
- English of all five examples is correct and natural. "As it was raining, we stayed in" is a little bookish/British but fine.

## Top 3 fixes (by impact)

1. voice / shorts-builder: repair the "Since." headline before upload (trim the ~150 ms tail after 0.45 s and pad, or splice "Since" from `b02-1.wav`, or regenerate) and have a human listen once. Add bare one-word headlines to the audio gate: if whisper does not return the headline word, fail the build.
2. scenario-writer (+ language-editor): next version puts the rule and the register on the card at no extra length. Headline "Due to + noun", "Thanks to + noun" (or a small tag under the headline), and a one-word register tag per card (formal / everyday / casual) next to the "1 / 5" counter. Order the list clause-words first (since, as, seeing as), then the "because of" pair, so the switch is visible. Consider "because of" itself or "so" in place of one item.
3. shorts-builder: cut each headline-to-example pause from ~1.2 s to ~0.7 s and the tail to ~1.0 s (saves ~3 s), and use the saved second for a recall card before the CTA ("____ it's late, let's go home."). Also dim the word cloud further or keep it out of the headline band.

## Siblings (frames only, layout)

l3-in-conclusion-v1 (7 frames: 0.3, 3.0, 7.5, 12.5, 22.5, 27.5, 30.5 s):
- No cut-off text, nothing in the bottom UI zone, strike and "Say this instead" clear, counter 1/5..5/5 present, chip "EP 6".
- Defect: the background word cloud is brighter and larger here than in "because" and collides with the foreground. Cloud words ("to conclude", "to sum up", "overall", "ultimately") sit directly behind the yellow headlines "To sum up", "In summary", "To conclude" and behind the white example lines (e.g. "To sum up, both plans have risks." has "to sum" / "to conclude" under and beside it). Still readable, but visibly noisy; this is the worst of the three. Fix: lower cloud opacity or mask the top 45 %.
- Two-line headlines ("To sum up", "In summary", "To conclude") break with one word on the second line. Cosmetic.

l3-congratulations-v1 (7 frames: 0.3, 3.2, 5.0, 15.0, 19.5, 23.5, 26.5 s):
- No cut-off text; "Congratulations" fits on one line in the hook with the strike across the full word; register labels present ("casual, American", "warm", "after hard work"); chip "EP 7".
- Same cloud collision, milder: "congrats!" / "you deserve" / "well done!" behind "Way to go!" and "I'm so happy for you!".
- The 1 / 5 beat at 5.0 s showed the headline without its label yet (normal: label appears with the second audio segment).
- No other layout defect seen. Audio of both siblings NOT checked (out of scope: frames only).

## What was checked / not checked

- Checked: 21 frames at 360 px across all beats, 14 fine-step hook frames, full-resolution crops of "Seeing as" and "Due to", measured text bounding boxes on 4 frames, full transcript with word times, each headline wav transcribed alone ("Since." three ways), 30 ms energy / spectral-centroid profile of `b02-0.wav`, `b03-0.wav` and the "since" in `b02-1.wav`, silencedetect, levels, unit JSON, YouTube JSON, H21 in lab.json, corpus search.
- Not checked: listening by ear (the "Since." finding needs a human ear to confirm), playback on a real phone with the YouTube UI overlaid, LUFS, thumbnail, sibling audio.
- Nothing was changed: unit, video, state files untouched. Scratch files only in `/tmp/vc-because/`.
