# M1 polish v2: changelog (m1-v1.mp4 → m1-v2.mp4)

Step "special M1: polish" (headless autopilot), 2026-09-28. Input `content/specials/M1/m1-v1.mp4` (347.70 s, untouched). Output `content/specials/M1/m1-v2.mp4`: 1280x720, 24 fps, H.264 CRF 18, AAC 44.1 kHz mono, **332.21 s (5:32.2)**, 7973 frames. sha256 617a1bbe69062cec46dfbd97cf47f5622a5b3931e4968b04d658339338cc6584.
Done with ffmpeg 7.0.2 (one render, -threads 4) plus Python/PIL/OpenCV overlays. No NotebookLM, no upload, glottos-auto/out not touched. Build scripts and overlay PNGs are in `content/specials/M1/polish-v2-build/` (`plan.py` holds every cut and freeze as source frame numbers; the scripts expect to run from a scratch dir that contains the source frames).

Timestamps: "src" = m1-v1, "new" = m1-v2. Cut boundaries were checked with faster-whisper small.en word timings plus ffmpeg silencedetect (-40 dB). All cuts are hard video cuts at frame boundaries inside a silence, with 8 ms audio fades at each join.

## Edits

| # | What | src | new | Notes |
|---|---|---|---|---|
| 1 | End card trimmed, fade out | keep < 344.333 (the end card starts at 344.583) | 331.81 to 332.21: 0.4 s fade to black; audio fades after the last word | The CTA ".net" ends at src 343.94 / new 331.82 and is complete |
| 2 | "Gemini Notebook" watermark removed | every frame (box x 1157-1271, y 700-709) | every frame | ffmpeg `delogo` over x1153 y697 w123 h16, plus the channel logo `state/brand/awf-logo-channel.jpg` as a 46 px rounded tile with a thin grey border at x1222-1270, y660-708 |
| 3a | Quiz pause, "very angry" | freeze frame 7566 (315.25) | 293.17 to 295.17 | silence between question and answer is now 3.0 s (was 1.0) |
| 3b | Quiz pause, "very busy" | frame 7637 (318.21) | 298.13 to 300.13 | gap 2.8 s (was 0.5) |
| 3c | Quiz pause, "very tired" | frame 7709 (321.21) | 303.13 to 305.13 | gap 2.7 s (was 0.7) |
| 3d | Quiz pause, "very happy" | frame 7783 (324.29) | 308.21 to 310.21 | gap 2.7 s (was 0.7) |
| 3e | Quiz pause, "very important" | frame 7849 (327.04) | 312.96 to 314.96 | gap 2.6 s (was 0.6) |
| 3f | "Livid." scroll answer leak hidden (inpainted) | 311.21 to 315.75 | 289.08 to 295.63 (incl. freeze) | The scroll shows "Livid." again from the moment the voice says "livid", so it works as a reveal |
| 3g | Both "Exhausted" leaks hidden (top-right watercolour and bottom "EXHAUSTED") | 319.75 to 321.54 | 301.63 to 305.42 (incl. freeze) | Both reappear from the moment the voice says "exhausted" |
| 3h | "very dizzy" → "very busy" | audio 317.10 to 317.97 replaced with the "very busy" clip from src 36.90 to 37.46 | ~297.06 | Ear check by two models: small.en AND medium.en both hear "very **dizzy**" (p=1.00). So NotebookLM really says "dizzy". Swapped. Whisper on v2 now hears "very busy" |
| 3i | Extra step labels on quiz slides removed (inpainted) | "Step 1: Identification / Step 2: Encoding / Step 3: Retrieval" 319.75 to 323.0; "Step 1: Focused Attention / Step 2: Association / Step 3: Recall" 325.75 to 328.42 | 301.63 to 306.88; 311.63 to 316.29 | Not in the brief. They were decorative "Step 1-3" labels that contradict the video's 3 steps |
| 4 | Step banner digit changed from 3 to 2 | 198.67 to 222.0 | 181.50 to 204.83 | Only the digit was repainted (hand-drawn stroke, matching style). Banner now reads **STEP 2: LEARN WHEN TO USE IT**. The voice says "Step three" at new 205.34, after the banner is gone |
| 5a | Cut filler "This frustrating cycle happens to almost everyone. But I want you to reassure yourself right now." | 6.792 to 12.292 | at 6.79 | "gone." → "Your memory is not broken." |
| 5b | Cut filler "That exact quote perfectly captures the frustration we all feel with traditional cramming." | 19.000 to 24.000 | at 13.50 | quote → "So first, a quick challenge." |
| 5c | Cut filler "And this brilliantly illustrates why it works." | 104.208 to 107.000 | at 93.71 | "...actively used them." → "Reading mostly trains recognition." |
| 5d | Cut overclaim "That physical power of writing it down is incredibly effective." | 128.583 to 132.458 | at 115.29 | quote 2 → "So what should you do?" |
| 5e | (optional, done) Cut "You can put it all together into a highly effective 15-minute daily routine." | 279.458 to 284.417 | at 262.29 | "...days one, three, and seven." → "For the first five minutes, your anchor phase..." The routine card (0-5 / 5-10 / 10-15 min) is on screen from new 262.29 |
| 6 | "A learner wrote:" tag on the quote cards | Q1 15.75 to 24.0; Q2 123.08 to 132.46; Q3 182.92 to 198.67 | Q1 10.25 to 13.50; Q2 109.79 to 115.29; Q3 165.75 to 181.50 | White rounded label with a dark outline and pink offset shadow (the card style), Liberation Sans 26 px, placed just above each card's top-left corner |
| 7a | Bar chart: raw-markdown caption removed, clean label added | 234.75 to 254.96 | 217.58 to 237.79 | The caption `*Active* recall makes your memory **stronger**.` was inpainted away. A new title sits above the chart: Liberation Sans Bold 24 px, dark, on a white box |
| 7b | Faded "③ Speakting in sentence" art line blanked (inpainted) | 234.75 to 279.63 (chart + Day 1/3/7 slides) | 217.58 to 262.33 | |

Removed in total: 22.13 s of cuts (531 frames) and 3.36 s of end card and tail. Added: 10.0 s of quiz pauses.

## On-screen text added or changed (for the language editor gate)

1. `A learner wrote:` (added, 3 times: quote cards 1, 2 and 3)
2. `One week later: % of a text remembered` (added, bar chart title)
3. `STEP 2: LEARN WHEN TO USE IT` (changed. Was `STEP 3: LEARN WHEN TO USE IT`. Only the digit changed. I did NOT use the brief's alternative wording "KNOW WHEN TO USE IT", because keeping the original hand lettering was cleaner, and "learn" matches the voice: "Learn one more thing with every word: when to use it")
4. Removed, no replacement text: `*Active* recall makes your memory **stronger**.`, `Speakting in sentence` (with its faded ③), `Livid.` (during the question and pause only), `Exhausted'` and `EXHAUSTED` (during the question and pause only), and `Step 1: Identification`, `Step 2: Encoding`, `Step 3: Retrieval`, `Step 1: Focused Attention`, `Step 2: Association`, `Step 3: Recall`, plus the `Gemini Notebook` watermark.
5. Audio change (not on-screen, but the gate should know): the quiz question "very dizzy" is replaced with "very busy". This clip is the narrator's own "very busy" from the challenge list, so it is said as a statement, not as a rising question.

## QA done on m1-v2.mp4

- Frames: one every 10 s (34 frames, contact sheets) plus full-resolution frames at every cut (±0.05 s), inside every freeze, at the banner (190, 204.7, 204.9), chart (225), timeline (250), quiz slides (290 to 316), CTA (320, 330.5) and the end (331.9, 332.15).
- Watermark: the bottom-right corner was checked at 0.5, 11, 112, 190, 225, 250, 290, 313.5 and 330.5 s. No trace of "Gemini Notebook" text is left. On the dark gear art of the "very important" slide the delogo area shows a faint soft smear left of the logo, but no text.
- End card: gone. The last frame is the CTA slide fading to black.
- Answer leaks: the scroll is blank during "very angry?" and its freeze, and "Livid." appears at 296 s. Both Exhausted labels are blank during "very tired?" and its freeze, and appear at 306 s. The "happy" and "important" slides show no answer ("vital / pivotal / essential" are still there, see below).
- Step numbers: on screen only STEP 2 at 181.5 to 204.8. Voice: "three easy steps" 78.0, "Step one" 80.5, "let's move to step two" 134.9, "Step three" 205.3, "That is step one already working" 324.0. They match.
- Words at the cuts (whisper small.en on v2 plus silencedetect): 6.79 "gone. | Your memory", 13.50 "them. | So first", 93.71 "them. | Reading", 115.29 "paper. | So what", 262.29 "seven. | For the first". No word is clipped. Each join has 0.5 to 0.8 s of silence. The quiz reads "very angry … livid, very busy … swamped, very tired … exhausted, very happy … thrilled, very important … crucial", with 2.6 to 3.0 s of silence before each answer (silencedetect).
- Duration 332.21 s (5:32).

## Not fixed / open

- "very important?" slide: `vital`, `pivotal`, `essential` stay on screen (not the answer, but they invite other answers) and so does the small `very important?` tag. Left as is.
- Faded background art on the chart and timeline slides still shows faint `① Comprehension`, `② network of associations`, `Garden`, `blossom`, `perfume`, `memory album` and faint circled 2 / 3 at the top. It is very low contrast. Only the misspelled line was blanked.
- The opening title card "Remembering New Words" stays up for 0 to 6.8 s while the hook is spoken. After cut 5a, the girl slide ("You learn a new word on Monday, but by Friday, completely gone.") comes in at 6.79 under "Your memory is not broken". This was already offset in v1.
- Beat 2 static holds (the DAX/CONNECTION pair and the brain/bin slide) and the long recognition/finding slide were not changed. There is no forgetting-curve drawing.
- Quote 3 card is still shortened ("Repeat the sentence I made myself over and over was a game changer."). Quote 2 card still ends with "it...".
- Fake handwriting on the "Use it" slide and random words in the routine notebook (`VIGILANT`, `EFFERVESCENT`) were not touched.
- "the method people most often say works best for them" (src 1:36.6) and "works significantly better" (src 3:50.5) are mid-sentence, so they were kept, as the critic said.
- Ear check of "Now it's moved to step two" (src 2:31): medium.en hears "Now let's move to step 2". No change needed.
- The swapped "very busy" has statement intonation, and its 2.8 s pause follows it. Not checked by a human ear.
- Not done: human listening, and a second critic pass (the next step is the language-editor gate on the strings above, then critic on m1-v2.mp4).
