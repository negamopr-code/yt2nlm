# Viewer-critic review: l1-very-strong-h59-v1 (lab H59 "THE FIRST SECOND")

Reviewed 2026-10-11. File: state/shorts/l1-very-strong-h59-v1/final.mp4 (1440x2560, 30 fps, 25.2 s, voice Kokoro am_michael 1.05x).
Unit: shorts/units/l1-very-strong-h59-v1.json. Meta: content/youtube/l1-very-strong-h59-v1.json.
Compared with: content/reviews/l1-very-excited-v1.md (lane, with hook sentence).

## Verdict: PARTLY
Five correct words, each with a ready phrase and a picture, and the first one is on screen and in my ear inside the first half second; but nothing tells me which word goes with which kind of thing, I never try one myself, and the first picture is a thumbnail-sized engine with its caption printed across it.

Ship blockers for this video: 0. (Sister video l1-very-dirty-h59-v1: 2, see the end.)

## Pain -> what the video gives -> gap
- Pain (my wording, from the task brief): "I say 'very strong' for everything; give me better words I can use today."
- Learner evidence: content/problems does not exist; content/insights/audience-needs.md has no learner quote about overusing "very". What is on file is format feedback only: "great video but please shorten the intro!" (most-liked thread on the channel), "very helpful thanks :)", "Useful information... I'll share it to my close ones", and viewers adding their own word under these Shorts ("Frigid too", "Melancholic too", "There is also minuscule as in a minuscule mouse."). No NotebookLM query spent. The pain is assumed from the brief, not proven by quotes; the "shorten the intro" comment is the only real evidence, and it supports this test directly.
- Solved would mean: tomorrow I say "a powerful engine" or "a fierce wind" without thinking, and I do not say "a sturdy coffee".
- Gives: 5 words, each heard twice, each with one collocation and a picture. The collocations are well chosen and spread across the senses of "strong" (machine, furniture, taste, nature, weather).
- Gap: one example per word is the only guide to use. No tag such as "things that do not break" (sturdy) or "taste, feeling" (intense). "Mighty" is literary; that label is only in the YouTube description, not on screen. No moment where I produce a word.

## The five checks asked for
1. First second: PASS. Frame 0.0 s already shows "very strong" struck out in red and "Powerful" in yellow below it; both readable at once at phone size (the headline is still growing at 0.0 s and is full size by 0.5 s). Voice: "Powerful" 0.00-0.34 s, "instead of very strong" 0.34-1.7 s. Without a hook sentence I still understand the video: struck phrase + better word + "instead of very strong" + the STOP SAYING pill. Weak point: until about 3.0 s the lower 65 % of the screen is empty wallpaper; the picture and the example line arrive only with "a powerful engine" (2.8 s).
2. Resolution: PASS. Native 1440x2560 (stream header; no ffprobe, read from ffmpeg -i).
3. Subscribe + bell: PASS on frames. Fades in from about 17.5 s, full at 17.9 s, red SUBSCRIBE -> grey SUBSCRIBED by 20.2 s, bell yellow by 21.6 s, gone by 22.9 s. Recorded 17.8 s in final.subscribe.json and in the meta ("subscribe_at": [17.8]); 17.8 of 25.2 s = second half. Position: left, about 4-58 % of the width and 71-77 % of the height, directly under the picture, clear of the picture, above the Shorts title row and left of the right-edge buttons. Smaller than in the lane review and on the safe line: the earlier request looks fixed. NOT checked on a real phone in the Shorts feed.
4. Pictures:
   - 1 Powerful: fits, but the engine fills about a fifth of the card width and the caption "A powerful engine." is printed across the top of the drawing (a line of the engine runs through "engine"). On a phone it is a grey lump with text on it. Weakest picture, and it is the one in the opening. Not wrong, so not a blocker.
   - 2 Sturdy: thick wooden table, caption above it. Best picture.
   - 3 Intense: red chillies on orange, no caption. Reads as "hot/spicy"; acceptable for "an intense flavor".
   - 4 Mighty: rapids between rocks; caption "A mighty river." printed across the middle of the drawing.
   - 5 Fierce: bent trees, swirling wind; caption "A fierce wind." printed across the drawing.
   - Text inside the pictures: correct English, same words as the card (capital A and a full stop are the only difference). No garbled writing, no watermark, no magnifying glass in any picture.
   - Inconsistent: pictures.json rejects one take of picture 3 because it "wrote its phrase across the drawing", yet pictures 1, 4 and 5 ship with exactly that.
5. Pain: PARTLY, see verdict.

## Audio (faster-whisper small.en, word timings, final.mp4)
0.00 Powerful instead of very strong | 2.76 a powerful engine | 5.22 Sturdy | 7.20 a sturdy wooden table | 9.84 Intense | 11.50 an intense flavor | 13.88 Mighty | 15.68 a mighty river | 17.94 Fierce | 19.58 a fierce wind | 21.46 Which one will you use today? (ends about 23.3)
All scripted words recognised, none dropped, none spelled letter by letter. Level: max -1.5 dB, mean -19.7 dB.
NOT checked: I cannot listen. Recognition rules out a gross mispronunciation, not a wrong stress or an odd intonation on the bare first word.

## Second by second
- 0.0-1.7: struck "very strong" + "Powerful", spoken at once. It is my phrase and I already have a word. I stay. Better opening than the lane's 3 s of "Stop saying... Say this instead".
- 1.7-2.8: 1 s of silence, big empty screen. First place I might swipe: nothing has moved yet.
- 2.8-5.0: example + picture arrive. Engine too small to enjoy.
- 5.2-9.5: Sturdy. Word, then about 1.2 s of nothing, then phrase and table. Clear.
- 9.8-13.5: Intense. Same rhythm. By now I know the pattern; the 1 s gap after each bare word starts to feel slow.
- 13.9-17.5: Mighty.
- 17.5-21.0: Fierce. The red SUBSCRIBE button arrives half a second before "Fierce" is spoken and sits alone on the empty card until the picture appears at about 19.5 s. For two seconds the button is the most colourful thing on screen, competing with word 5.
- 21.5-23.3: "Which one will you use today?" Easy to answer.
- 23.3-25.2: 1.9 s, no voice. Fine for the loop.
Swipe risk: low in second 0-2 (the point of the test), moderate around 10-14 s where the pattern is known and nothing new happens.

## Takeaway test
"Tomorrow I say 'a powerful engine', 'a sturdy table', 'a fierce wind' instead of 'very strong ...'." Nameable, so not DOESN'T. Not SOLVES: I cannot tell which of the five to pick for a new noun (strong coffee? strong man? strong smell?), and I never tried.

## Retention risks
- 25.2 s against 18.5 s for the lane Short: five words at one fixed rhythm (word, 1 s pause, phrase). Words 3-4 are where the curve will sag.
- Empty lower two thirds of the screen for the first 3 s of a test whose whole point is the first second.
- Subscribe button on the bare card of word 5 (see above).
- Wallpaper words ("sturdy", "fierce") drift in bright yellow right behind the headline and the CTA.

## Trust risks
- "Stop saying": "very strong" is correct English. Lane convention, accepted.
- "Mighty" has no register label on screen; a learner will write "a mighty coffee" or use it in an email.
- "Intense" shown with chillies teaches "spicy" more than "strong taste".
- No wrong facts, no unnatural English found.

## Top 3 fixes (by impact)
1. visuals: redo picture 1 so the engine fills the card and no caption lies across the drawing (same for 4 and 5 if a clean take exists). It is the only picture a 3-second viewer ever sees.
2. scenario-writer + language-editor: add a 1-3 word use tag under each headline (machines / things that do not break / taste, feeling / literary / weather, animals) so the viewer can choose; this is what moves the verdict to SOLVES.
3. shorts-builder: bring the first picture in with frame 1 (or by 1.0 s) so the opening is not two thirds empty, and start the subscribe animation when the picture of word 5 is already up (about 19.6 s) or on the CTA card, not on the bare headline.

## Sister videos (qa.jpg glance, plus frames of l1-very-dirty)
- l1-very-nice-h59-v1: no blocker seen. Beat 1 "a lovely evening": small drawing pushed into the bottom-left corner of a mostly white card. Beat 2 "a delightful little café": picture cropped to a thin strip, chairs cut at both ends. Language editor's "listen to café" note still needs a human ear.
- l1-very-crazy-h59-v1: no blocker seen. Pictures are emoji pairs, not NotebookLM drawings like the three sisters (if the test is supposed to change one thing only, this is a second variable). "Outrageous" headline is set smaller than the others.
- l1-very-dirty-h59-v1: 2 blockers.
  1. Beat 1 picture (pic-01.png, seen in the video at 4.2 s): a hard-edged flat yellow rectangle at the top right slices the fingertips of the right hand (a retouch patch), and there is a letter-like scribble on the left wrist at the bottom, plus a strip of squared paper along the bottom edge of the source picture. Owner: visuals.
  2. Beat 4 "Foul" picture: a large magnifying glass over the water. The waterline runs straight through the lens and the algae patches inside are the same scale as outside; I see no enlargement. Under the 2026-10-05 rule that is a defect: back to visuals. (Judged from stills; borderline, a human should confirm.)
  - Beats 3 "Squalid" and 4 "Foul" DO show their example line and picture in the video (frames at 11.0, 12.8, 15.2, 16.6 s). The qa.jpg is wrong, not the video: it has 7 panels instead of 8, no Squalid panel, Foul sampled before its picture, no CTA panel. Regenerate it; as it stands it proves nothing.
  - SUBSCRIBED pill touches the bottom border of the "polluted air" picture (about 20.3 s). "Squalid" picture is a thin strip. Transcript clean, no spelled-out word.

## What was not checked
Listening by ear (all four videos); the Shorts feed overlay on a real phone; transcripts of l1-very-nice and l1-very-crazy (qa.jpg only); YouTube itself (not touched). No file rendered, changed or uploaded; this review is the only file written. Mirror rule not applied (no user message in this task).


## After the review (2026-10-11T13:29:26Z, produce tick)
Both blockers on `l1-very-dirty-h59-v1` repaired: picture 1 'Filthy' cut again from the NotebookLM film without the magnifying glass and without the yellow patch (the scribble inpainted); picture 4 'Foul' replaced by the glass-free drawing of the same scene (stump over a foul puddle). Rendered again, audio gate OK, qa.jpg regenerated with all six beats. The non-blocking remarks are not acted on in this batch.
