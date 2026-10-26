# Viewer-critic review: long-another-word-for-angry-v1 (search phrase "another word for angry", lab H19)

Reviewed 2026-10-04. Video: `state/shorts/long-another-word-for-angry-v1/final.mp4` (1920x1080, 30 fps, 242.3 s, AAC 24 kHz mono).
Unit: `shorts/units/long-another-word-for-angry-v1.json` (language-editor hash 445599adb95e3d2d).

## Verdict: SOLVES - with 1 ship blocker (the "Cross" picture)

A searcher who typed "another word for angry" gets ten correct, natural words sorted by strength, each with a plain meaning and a usable sentence, tests themselves four times and says all ten sentences out loud; nothing in the text or the audio is wrong. One picture (Cross) is a broken crop that shows nothing, and it sits in the first frame of the video, so it must be replaced before hand-over.

## Pain

Evidence is thin and I am saying so. There is no `content/problems/` folder and no PROBLEM document for "stop saying very / basic words"; PROBLEM 01 in `content/articles/p01-why-you-forget-new-words.md` is "learn words, forget them in days". Verbatim learner lines I could find in `state/corpus-glottos-niche/raw` (comment lines):

- "I can understand what you say clearly , the point is that when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "when I'm in front of people I forget how to speak or I forget the words"
- "my pronunciation and conversation and vocabulary is small, Please help me with advice."
- From the channel's own comments (`content/insights/audience-needs.md`, most-liked thread): "great video but please shorten the intro!"

That is one direct quote for this pain; the rest is adjacent. The real support for the video is search demand for the phrase, not quotes. No NotebookLM query was spent.

Pain in the learner's words: "I say the same words all the time" - I always say "angry" / "very angry" and want other words I can remember and use.
Solved would mean: tomorrow I say or write "I was annoyed that...", "I'm fed up with...", "My boss was furious" instead of "angry", and I know which word is weak and which is strong.

Pain -> what the video gives -> gap:
- Gives: 10 words on a two-step scale (a little / very), meaning in A2 English, one natural sentence each, 4 quiz questions, 10 listen-and-say sentences.
- Gap 1: the quiz does not test the thing the learner needs (which angry word), because the wrong options are absurd (thrilled, vast, radiant, essential). I never have to choose between two angry words.
- Gap 2: no register help. "Irate" is formal/written, "livid" and "fuming" are informal, "cross" is mild. Only "cross" gets a label. A learner may say "I am irate" to a friend.
- Gap 3: the pictures are small and several do not show the feeling (details below), so the "with pictures" promise in the title is only half kept.

## Answer speed (the main question)

- 0.00 s: card "Another word for "angry" / 10 words with pictures and examples", voice from 0.0 "Looking for another word for angry?" - the searcher knows at once this is the right video. Good.
- 9.79 s: first words visible as small labels under the pictures (Annoyed, Irritated, Cross, Grumpy, Fed up).
- 13.30 s: "Annoyed" on screen as a headline; spoken at 13.68 s; meaning at 14.5 s; example at 16.6 s.
- So: **13.7 s to the first spoken answer.** Acceptable for a 4-minute search video, but slower than it needs to be: 9.8 s of one static slide, then 3.5 s of "Part 1. Five words for a little angry." The channel's most-liked comment is "please shorten the intro".

## Audio check (voice vs unit)

Transcribed final.mp4 with faster-whisper small.en (word timings). Every sentence matches the unit; nothing added, dropped or spelled letter by letter. Whisper heard exactly the target words:

- "Irate" 153.3 s, "irate customer" 159.0 s and 217 s. Kokoro phonemes for the unit text: aɪɹˈeɪt = eye-RATE. Correct.
- "Livid" 129.6 s: lˈɪvɪd. Correct.
- "Fuming" 145.0 s, 150.8 s: fjˈuːmɪŋ. Correct.
- "Cross." 29.6 s: kɹˈɔs, heard as "Cross". Correct.
- "Fed up." 47.1 s: fˈɛd ˈʌp, heard as "Fed up". Correct.
- "blank" in all four quiz lines (56 s, 69 s, 165 s, 177 s): heard as "blank". Correct.
- "another word for dot net" 230 s: heard "another word for .NET". Correct.

Limit of this check: I cannot listen. Pronunciation is confirmed by (a) whisper recognising the intended word and (b) the phonemes Kokoro's own tokenizer produces for the text. Intonation and any odd rhythm were not judged.

Pauses: quiz think time 3.5 s (3-2-1 countdown), say-it pauses 4.0-6.1 s after sentences of 2.1-3.7 s. Enough to repeat. No dead air except 3.1 s of silence on the last card (fine for an end screen).

Loudness: integrated -23.1 LUFS, true peak -1.2 dBFS (same as long-stop-saying-very-v1). YouTube's reference is about -14 LUFS and it does not turn quiet videos up, so this plays about 9 dB quieter than the video before it.

## Words, meanings, text on screen

All ten meanings are accurate and at B1 level; all ten examples are natural. Screen text matches the unit word for word. Text is large and stays long enough to read (meaning 2-4 s before the example, example 3.4-6.4 s). Chapters in `chapters.txt` match the slide times (9.79 / 81.43 / 117.48 / 188.09 / 233.60 s). No NotebookLM/Gemini watermark is visible in any picture (checked the corners at full size; the source frames had "Gemini Notebook", it is painted out).

## Pictures: do they fit?

| Word | Time | Picture | Fits? |
|---|---|---|---|
| Annoyed | 0:14 | orange card, small man at a desk with clocks inside a magnifier | Weak: face is too small to read; garbled AI text around it ("WAST DUE", "URGST") |
| Irritated | 0:21 | empty armchair, noise cloud with an angry emoji | OK idea, small |
| **Cross** | 0:31 | half an orange rectangle over half a clock, an empty armchair, a teacup | **No. Nobody is in it, nothing is cross. It looks like a rendering error.** |
| Grumpy | 0:40 | an unmade bed, alarm clock, coffee | Weak: no person, shows "morning", not "grumpy" |
| Fed up | 0:48 | queue at a rainy bus stop, woman with a sour face | Good |
| Furious | 2:03 | cracked window, small dark figure | OK, small |
| Livid | 2:10 | red fist crushing a paper bill | Good (reads slightly bloody) |
| Outraged | 2:17 | small protest scene inside a magnifier | OK, very small |
| Fuming | 2:26 | angry driver in a traffic jam | Very good |
| Irate | 2:34 | angry customer at a counter | Very good |

Four strong, four passable, one weak, one broken. The pictures take about a fifth of the frame and most of that area is a flat NotebookLM card that repeats the word and sentence already on the left; the actual drawing is roughly 10% of the screen, while the bottom 40% of every word slide is empty. On a phone the faces in Annoyed, Furious and Outraged cannot be read.

## Second-by-second

- 0:00-0:09.8 Hook card. Right problem at once. But one still slide for 9.8 s, and the tallest picture in the strip is the broken Cross crop. Strip shows 6 pictures for "10 words". "Each one comes with a picture and an example. Let's start." is filler - first swipe risk at about 0:05-0:09.
- 0:09.8-0:13.3 "Part 1. Five words for a little angry." Useful label, 3.5 s; the five words are already readable here.
- 0:13.3-0:54.9 Five mild words, about 8 s each. Clear, steady. Word number "1 / 5" helps. At 0:31-0:39 the Cross picture confuses. "This one is mainly British" is said after the example; the card shows it from 0:31.
- 0:54.9-1:21.4 Two quiz questions. I do answer in my head, but "cross or thrilled", "grumpy or vast" need no thought. Swipe risk for a B2 viewer: "this is for beginners".
- 1:21.4-1:57.5 Repeat after me, 5 sentences, LISTEN / YOUR TURN labels are clear. This is the part that changes what I do tomorrow. 36 s; a viewer who only wanted the list leaves here, which is fine - part 2 has a chapter.
- 1:57.5-2:43.5 Five strong words. Best pictures are here (Fuming, Irate).
- 2:43.5-3:08.1 Quiz: "livid or radiant", "outraged or essential". Same problem.
- 3:08.1-3:46.7 Repeat after me. Last pause is 6.1 s, slightly long.
- 3:46.7-3:53.6 Site tip. Short, relevant to this searcher.
- 3:53.6-4:02.3 "Which one was new to you? Write it in the comments, and try using it today." Clear action.

## Takeaway test

Named action: tomorrow, instead of "angry", say one of the sentences I repeated - "I'm fed up with waiting...", "I was annoyed that...", "My dad was livid when...". Passes.

## Retention risks

- 13.7 s to the first word; a search viewer compares this with list videos that say a word in 3 s.
- Every slide has the same layout for 4 minutes; no recap ladder that shows all ten words from weak to strong at the end.
- Quiz is too easy to feel like a test.
- Quiet audio (-23 LUFS).
- Voice speed 1.0 is fine; no podcast chatter, no jargon, no names.

## Trust risks

- Cross picture looks like a bug.
- Garbled English-like text inside the Annoyed picture ("WAST DUE", "URGST 3:05PM") in a video that teaches English; tiny, but visible on a TV or desktop.
- A thin black line along the bottom edge of the Annoyed, Irritated, Grumpy and Fed up pictures (leftover from the source frame).
- Background ghost words overlap each other ("grumpyirritated", "fumingirate", "furiouslivid") - reads as a layout slip.
- An American voice says "my mum" - harmless, and the British label covers it.
- No factual error, no overclaim, no unnatural English found.

## Ship blockers (1)

1. **Cross picture is a broken crop** - 0:00-0:09.8 (hook strip, tallest tile), 0:09.8-0:13.3 (section strip, centre), 0:30.9-0:39.4 (word slide). File `state/shorts/pic-angry-mild-v1/pic-04.png`; `pictures.json` already marks it `"matched": false`, and `pic-04-1.png` / `pic-04-2.png` are the same crop. Fix (visuals): make a new picture for Cross that shows a mother with folded arms at the door and a clock showing a late hour, with the person filling the frame; or, as the quick route, use the whole NotebookLM frame like the other four mild words - but that frame still has no person, so a new picture is the real fix. Then shorts-builder rebuilds; the hook and section strips pick it up automatically.

## Nice-to-haves (ordered by impact)

1. **Quiz distractors** (0:55, 1:08, 2:44, 2:55) - scenario-writer, then language-editor. Use a word from the other part so I must think about strength: "My mum was ___ with me for coming home ten minutes late. cross / livid"; "He's always ___ in the morning, before his first coffee. grumpy / outraged"; keep one clear right answer.
2. **First word sooner** (0:00-0:13.7) - scenario-writer. Cut "Each one comes with a picture and an example. Let's start." and say three words in the hook: "Looking for another word for angry? Annoyed, furious, livid - here are ten, from a little angry to very angry." First answer at about 3 s, part 1 starts at about 6 s.
3. **Loudness** (whole video) - shorts-builder. Normalise to about -16 LUFS with a limiter (peaks are already at -1.2 dBFS, so it needs compression, not just gain). Applies to the builder, not only this video.
4. **Bigger pictures** (all word slides) - shorts-builder. Crop to the drawing and let it fill the right half and the empty bottom of the slide; the NotebookLM card repeats text that is already on the left.
5. **Register labels** (2:10 Livid, 2:26 Fuming, 2:34 Irate) - scenario-writer, language-editor. Add "(informal)" to livid and fuming and "(formal)" to irate, as was done for cross.
6. **Recap ladder before the CTA** (about 3:46) - scenario-writer / shorts-builder. One slide with all ten words from weakest to strongest, 4 s.
7. **Annoyed and Grumpy pictures** (0:14, 0:40) - visuals. Show a person's face; remove the garbled text in Annoyed.
8. **Cosmetics** - shorts-builder. Trim the black line at the bottom of four pictures; stop the ghost words overlapping; show 10 tiles (or none) in the hook strip, not 6.

## Top 3 fixes

1. Replace the Cross picture (visuals, then shorts-builder) - blocker.
2. Make the quiz choose between two angry words (scenario-writer, language-editor).
3. Say the first words in the hook and cut the filler sentence so the answer arrives in about 3 s (scenario-writer).

## What was checked / not checked

- Checked: all 77 slides (contact sheets of `frames/s0000-s0076.png`), ten word slides and the Cross source frames at larger size, picture corners for watermarks, 10 frames pulled from final.mp4 to confirm the video matches the slides, the thumbnail, full whisper transcript with word times, Kokoro phonemes for the six risk words, silences, loudness, chapter times, slide text against the unit.
- Not checked: the audio by ear (intonation, clicks at joins), the YouTube title/description/tags file, how the thumbnail looks next to competitors in search, mobile rendering in the YouTube app.
