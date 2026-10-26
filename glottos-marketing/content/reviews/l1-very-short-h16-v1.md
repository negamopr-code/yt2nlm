# Viewer-critic review: l1-very-short-h16-v1 (Stop Saying, EP 13, lab H16)

Reviewed 2026-10-03. Video: `state/shorts/l1-very-short-h16-v1/final.mp4` (26.87 s, 1080x1920, 30 fps).
Sibling glanced at: `state/shorts/l1-very-cold-h16-v1/final.mp4` (29.03 s).

## Verdict: PARTLY

It hands the learner five correct, clearly spoken replacements in 27 s with no defects, but only two or three of them (brief, quick, concise) are words a B1 learner will actually say tomorrow, there is no moment where I test myself, and the hook never tells me which "short" is meant.

## Pain

Evidence is thin and I am saying so. There is no PROBLEM NN document for this theme. The corpus (`state/corpus-glottos-niche/raw`, comment lines only) has exactly one verbatim line that states this pain directly:

- "I can understand what you say clearly , the point is that when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"

Adjacent, weaker: "Learning any new language is tough but first learn the basic vocab. Then try to learn synonyms. It helps".

The "332 pain lines" in `content/insights/pain-demand-2026-09-30.md` are inflated: the regex also counts praise such as "Very good recommendations thank you..." and "very nice video". The real support for this lane is YouTube demand ("Stop saying VERY!" 48.5M etc.), not learner quotes. No NotebookLM query was spent.

Pain in the learner's words: "I say the same words all the time" and I want new ones I can remember and use.
Solved would mean: tomorrow, in a meeting or message, I say "a brief call" / "a quick break" instead of "very short", and I still remember it.

Pain -> what the video gives -> gap:
- Gives: 5 words, each with one natural collocation, a matching picture, word spoken twice.
- Gap 1: the learner asked how to "memorize ... and use them". Nothing here makes me recall a word (no quiz, no recap). The CTA "Which one will you use today?" is the only nudge.
- Gap 2: "fleeting" and "momentary" are literary/C1; a B1 learner in a meeting will not say "a fleeting smile". Useful yield is 3 of 5.
- Gap 3: "concise" is not "very short", it is "short and clear". Fine as an upgrade, but the video does not say so.

## Check 1: first better word under 3.0 s - PASS

- 0.00-1.35 voice "Stop saying very short." Card "Stop saying "very short"" on from frame 1.
- ~1.7 s red strike through "very short".
- ~2.05 s "5 better words" fades in; gone by ~2.45 s.
- ~2.45-2.50 s "Brief" on screen (hook still at 2.40, Brief at 2.50). Spoken 2.50-3.02 (silencedetect), whisper 2.18-2.88.
- So: on screen at about 2.5 s, speech starts 2.5 s. Under 3.0. The spoken word finishes at 3.02.
- Sibling: "Freezing" on screen by ~2.5-2.9 s, spoken 2.54-3.18. Also passes.

Is the fast opening understandable? Yes. "Stop saying "very short"" plus the strike plus the "STOP SAYING - EP 13" chip is enough; the "1 / 5" counter on the first word tells me a list is coming.
Is "5 better words" readable? No. It is fully visible for roughly 0.3-0.4 s (fades in around 2.05, cut at ~2.45). A B1 reader will not catch it. It is not harmful because "1 / 5" carries the same information, but as built the line is decoration.

## Check 2: beats

| # | t (s) | Word | Card phrase | Picture | Text in picture | OK? |
|---|---|---|---|---|---|---|
| 1 | 2.5-6.5 | Brief | a brief phone call | hand with old phone receiver + stopwatch | "A brief phone call." clean, "brief" highlighted | yes |
| 2 | 6.5-10.5 | Quick | a quick lunch break | sandwich on plate + hourglass | "A quick lunch break." clean | yes |
| 3 | 10.5-14.7 | Fleeting | a fleeting smile | sketched smiling face, no text | none | matches, but a still smile does not show "fleeting"; meaning rests on the word alone |
| 4 | 14.7-19.2 | Momentary | a momentary silence | empty room, armchair, shush emoji, pause icon | "A momentary silence." clean | yes; pause icon is a nice cue |
| 5 | 19.2-23.6 | Concise | a concise email | envelope, fountain pen, check mark | "A concise email." clean | yes |
| CTA | 23.6-26.9 | - | Which one will you use today? / Write it in the comments. | - | - | yes |

- Watermark: none found (no NotebookLM / Gemini mark in any frame I looked at).
- Garbled text / half-drawn frame: none.
- Artifact, all text pictures, both videos: a thin black line along the bottom edge of each picture that stops at about 84% width with a small soft grey nub (present in the source `pic-02.png` too). It looks like the bottom edge of the NotebookLM frame plus the blur where something was removed. Small, but once seen it reads like a paused video progress bar. Non-blocking.
- "Fleeting" picture: two tiny dark specks lower right of the paper. Not noticeable at phone size.
- Bottom UI zone: lowest content is the picture bottom at about y=1320 (Concise). Nothing below y=1520 except the dim background word cloud. CTA text sits at y~1470-1640 for the yellow "Write it in the comments." line: the last line may touch the caption/UI area on some phones. Minor.
- Layout: word alone for ~1.3 s, then example + picture appear together with the spoken example. Picture and voice are in sync on every beat.

## Check 3: audio

Heard (faster-whisper small.en, word timings): "stop saying very short, brief, a brief phone call, quick, a quick lunch break, fleeting, a fleeting smile, momentary, a momentary silence, concise, a concise email. Which one will you use today?"

- Every word present and clear; matches the approved unit text exactly.
- No word spelled letter by letter.
- Pauses 1.06-1.36 s between word and example and between beats; consistent, nothing clipped at segment edges.
- Whisper printed a "No." at 25.08-26.08: hallucination. That stretch peaks at -41 dB, i.e. silence.
- Tail: 1.75 s of silence on the CTA card. Acceptable (time to read "Write it in the comments."), could be 1.0 s.
- Levels: mean -27.6 dB, peak -4.3 dB. No music. Not checked: loudness in LUFS, pronunciation judged by ear (I only have the transcript and levels; whisper recognised every target word correctly, which is indirect evidence).

## Check 4: does a B1 learner leave with usable words?

- Yes for brief / quick / concise. These fit "call", "break", "email", "meeting" directly.
- Time/length sense vs height: the hook does not disambiguate, and "very short" for most learners first means a short person. The first example ("a brief phone call") fixes it within 4 s, and nothing in the video suggests these words describe people, so it is not wrong. Risk: a learner who came for height leaves with nothing, and a careless one writes "a brief man". One word in the title/description ("for time") would close it; that is outside this file.

## Second-by-second swipe risks

- 0.0-1.4: clear, it names a phrase I use. I stay.
- 2.05-2.45: "5 better words" flashes; unreadable. No harm.
- 2.5-4.3: "Brief" alone on a black card, 1.3 s of silence. First real swipe risk: nothing to look at yet. Same gap repeats on every beat (6.6, 10.6, 14.8, 19.4).
- 10.5-19.2: two unfamiliar, bookish words in a row (fleeting, momentary). A B1 viewer who wanted "words for today" may leave here.
- 23.6-26.9: CTA, 1.75 s silent tail.

## Takeaway test

One action: next time I would say "a very short call / break / email", say "a brief call", "a quick break", "a concise email". Nameable, so PARTLY rather than DOESN'T. Not SOLVES because there is no recall step and 2 of 5 words are not for tomorrow.

## Retention risks

- Length is right (26.9 s vs 32 s for l1-very-sad-v1; I did not review that one frame by frame).
- Five identical beats with identical rhythm and 1.3 s empty pauses; no change of pace, no self-test.
- "5 better words" too brief to read.
- Background word cloud shows the answers (brief, quick, fleeting...) from second 0, dim but legible: it spoils the list slightly and adds noise behind the headline.

## Trust risks

- English is natural; collocations are idiomatic. No wrong facts.
- "Concise" presented as a synonym of "very short" without the "and clear" nuance.
- "Fleeting" picture does not show brevity.
- Bottom-edge line/nub on pictures looks like a leftover from the source video.

## Top 3 fixes (by impact)

1. scenario-writer: for the next units in this lane, pick five words a B1 learner can say at work or in chat (e.g. swap "fleeting"/"momentary" for everyday ones), or mark register. This is what moves PARTLY towards SOLVES.
2. shorts-builder: keep the H16 hook, but either show "5 better words" from ~0.8 s (together with the headline) so it is on screen about 1.5 s, or drop it and rely on "1 / 5". Also crop 6-8 px off the bottom of the NotebookLM frames to remove the black line and nub.
3. scenario-writer / format-strategist: add a recall moment that costs no extra length, e.g. the CTA card shows "a ____ phone call" for one second before "Which one will you use today?".

## Sibling: l1-very-cold-h16-v1 (glance only)

- Audio complete and matches: freezing / icy / frozen / bitter / arctic, all examples, CTA. No spelled words. First word at ~2.5 s.
- No watermark, no garbled text.
- "Arctic" picture (23.6-25.8 s): the inpainted patch where the calendar was removed IS visible, a pale X / diamond-shaped ghost in the top right of the sky. On screen about 2 s near the end. Not a watermark and not text, but a visible smear. I would fix it before shipping (re-inpaint or crop the frame); if it ships as is, it is a cosmetic flaw, not a factual one.
- "Frozen" picture: the baked-in sentence "Frozen fingers after the snowball fight." overlaps the drawing of the hands (the word "fight." sits on a finger). Readable, slightly messy. The card repeats the phrase above, so nothing is lost.
- Same bottom-edge line/nub as above.

## What was checked / not checked

- Checked: 18 frames per video at 360 px, 12 fine-step hook frames, full-resolution crops of all five pictures (short) and of Frozen/Arctic (cold), full transcript with word times for both, silencedetect, tail level.
- Not checked: playback on a real phone with YouTube UI overlaid, LUFS, the title/description/thumbnail, a frame-by-frame comparison with l1-very-sad-v1.
