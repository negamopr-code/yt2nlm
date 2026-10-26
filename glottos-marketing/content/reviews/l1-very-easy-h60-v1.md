# Viewer-critic review: l1-very-easy-h60-v1 (lab H60 "THE ENDING": no closing question, loop back to the opening)

Reviewed 2026-10-11. File: state/shorts/l1-very-easy-h60-v1/final.mp4 (1440x2560, 30 fps, 27.1 s, voice Kokoro am_michael 1.05x).
Unit: shorts/units/l1-very-easy-h60-v1.json. Meta: content/youtube/l1-very-easy-h60-v1.json.
Compared with: content/reviews/l1-very-strong-h59-v1.md. Sisters glanced at: l1-very-funny-h60-v1 (28.4 s), l1-very-fast-h60-v1 (25.9 s).
Not judged as defects (they are the test): no closing question, the 0.7 s return of the opening card, the old opening sentence, emoji cards.

## Verdict: PARTLY
Five correct, common words, each heard twice with one ready phrase, clean sound and readable cards; but nothing tells me which of the five fits which kind of thing, I never try one myself, and the last picture I see before the loop (frying pan) looks like a magnifying glass over an egg.

Ship blockers: easy 1 (a judgement call, see below); funny 0; fast 0.

## Pain -> what the video gives -> gap
- Pain (my wording, from the task brief): "I say 'very easy' about everything; give me better words I can use today."
- Learner evidence: unchanged from the H59 review. content/problems does not exist and content/insights/audience-needs.md has no learner quote about overusing "very"; the only quotes on file are format feedback ("great video but please shorten the intro!", "very helpful thanks :)") and viewers adding their own word under these Shorts ("Frigid too", "Melancholic too"). No NotebookLM query spent. The pain is assumed from the brief, not proven by quotes.
- Solved would mean: tomorrow I say "straightforward instructions" or "a foolproof recipe" without thinking, and I do not say "a painless puzzle".
- Gives: 5 words, each heard twice, each with one collocation and an emoji picture. The set is good for B1-B2: all five are everyday words (better than "mighty" in H59), and the collocations are natural.
- Gap: one example per word is the only guide to use. "Effortless" (no effort from the doer), "painless" (no trouble) and "foolproof" (cannot go wrong) are not interchangeable and nothing on screen says so. No moment where I produce a word; with the closing question removed (the test) there is now no prompt at all.

## Hard gates
1. Resolution: PASS. 1440x2560 on all three (ffmpeg -i stream header).
2. Subscribe + bell: PASS on all three, on frames.
   - easy: recorded 17.6 s (final.subscribe.json and meta "subscribe_at": [17.6]); red SUBSCRIBE at 18 s, grey SUBSCRIBED at 19 s, bell yellow by 21 s, gone by 22 s. 17.6 of 27.1 s = second half.
   - funny: recorded 18.4 s, fading in at 18 s, red at 19 s, yellow bell at 21.5 s. fast: recorded 16.5 s, red at 17 s, yellow bell at 20 s.
   - Position in all three: left, about 4-52 % of the width, 71-77 % of the height, under the picture. It covers no headline, no example line and no picture. Closest case: fast, "lightning-fast internet" picture, bottom edge at about 64 % of the height, pill starts at 71 %: clear.
   - Same remark as H59: the button arrives on the bare headline of word 4, about 1.5 s before its picture, so for a moment it is the only colourful thing under the word.
3. Readability and safe area: PASS with one unverified risk.
   - Every headline and example line is readable at phone size. Long headlines ("Straightforward", "Side-splitting", "Laugh-out-loud", "Lightning-fast") are set smaller and run from about 7 % to 93 % of the width, at about 25 % of the height: above the Shorts buttons.
   - Two-emoji picture cards run to about 95 % of the width between 40 % and 68 % of the height. The top Shorts buttons (like / dislike) may sit on the right edge of the second emoji. Lane layout, same as shipped emoji Shorts; NOT checked on a real phone.
   - Nothing sits in the bottom caption zone (lowest element is the subscribe pill at 77 %).
4. Magnifying glass / stray text: no real magnifying glass, no watermark, no garbled text in any of the three. But see the frying pan below. The drifting wallpaper words are the lane's, not stray text; in places they pile into nonsense right behind the content ("painless" in large letters behind "a painless way to learn" at 19-21 s in easy; "pricebside-spl" at 16-20 s in funny; "breakneck" directly under "Swift" at 9 s in fast). Readable, but noisy.

## Pictures (does the emoji fit the example?)
easy:
- 1 Simple, "a simple puzzle": one green puzzle piece. Fits.
- 2 Effortless, "an effortless win": trophy + relaxed face. Fits well.
- 3 Straightforward, "straightforward instructions": clipboard + right arrow. Weakest fit: reads "list, next". Acceptable.
- 4 Painless, "a painless way to learn": open book + smiling face. Fits.
- 5 Foolproof, "a foolproof recipe": frying pan with an egg + OK hand. The meaning fits, the drawing does not: the Noto pan is a dark round rim with a long diagonal handle, and at phone size (and on the 1 fps contact sheet) I read it as a magnifying glass looking at an egg. It is also the last picture before the loop. BLOCKER (judgement): the pictures of this batch were redone precisely because of a magnifying glass on every frame; a card that looks like one will be taken for the same defect. One emoji to swap (pot of food, chef, cake), one re-render. If the user is known to accept it, this drops to fix no. 1.
funny (glance): face with tears of joy; cat + rolling-laughing face ("cat video" has no video, fine); theatre masks + laughing face (one mask is the sad one, fine); TV + tears of joy; astonished face + rolling-laughing face for "a priceless reaction" (reads "surprised, then laughing", acceptable). No defect.
fast (glance): chart going up + seedling; incoming envelope + lightning; plaster + flexed arm (best of the batch); lightning + signal bars; racing car + dash cloud. No defect.

## Audio (faster-whisper small.en, word timings; .ttsvenv has no faster_whisper, run with .nlmvenv)
easy: 0.00 Stop saying very easy. | 2.08 Here are five better words. (ends 3.5) | 4.3 Simple | 5.9 a simple puzzle | 8.2 effortless | 10.2 an effortless win | 12.6 straightforward | 14.5 straightforward instructions | 17.3 painless | 19.3 a painless way to learn | 22.1 foolproof | 23.8 a foolproof recipe (ends 25.2-25.3)
funny: all words recognised as scripted: Hilarious 4.5, Hysterical 8.9, Side splitting 13.5, Laugh out loud 18.5, Priceless 23.4, "a priceless reaction" ends 26.3-26.6.
fast: all words recognised as scripted: Rapid 4.5, swift 8.1, speedy 12.2, lightning fast 16.3, breakneck 21.2, "at breakneck speed" ends 23.9-24.2.
- No word dropped, clipped or spelled letter by letter in any of the three. "Straightforward", "Foolproof", "Side-splitting", "Laugh-out-loud", "Lightning-fast", "Breakneck" are each recognised twice (bare and in the phrase).
- Whisper printed "Subs by www.zeoranger.co.uk" at 26.3-28.3 s of funny. That is a known whisper hallucination on silence, not sound in the file: the tail after 26.7 s peaks at -59 dB.
- Ending: after the last word there is 1.8 s of silence in easy and funny, 1.7 s in fast (tail peak -59, -59 and -84 dB). No cut word, no click measurable.
- Level: mean -19.6 dB, max -1.5 dB (same as the lane).
- NOT checked: listening by ear. Recognition rules out a gross mispronunciation, not a wrong stress.

## The ending (the thing under test, checked as built)
- The opening card returns at 26.40 s in easy (27.63 funny, 25.13 fast) and stays 0.7 s: "Stop saying" + struck-out "very easy", no "5 better words" line, same as the first second of the video. The fifth card stays 1.1 s after its last word before that.
- It is the same picture as the opening, but not the same as frame 0: the video starts with the headline at about three quarters of its size and grows to full size in about 0.3 s, and the wallpaper is in a different place. So on replay the title is full size, shrinks in one frame, and grows again. A small visible pop, not a seamless loop. Not a blocker; it weakens the exact effect the test wants to measure.
- Sound across the seam: 1.8 s of silence, then "Stop" at 0.00 s with no lead-in. Clean.

## Second by second (easy)
- 0.0-1.5: "Stop saying very easy", struck out in red from frame 1. It is my phrase. I stay.
- 1.5-4.3: "Here are five better words" + "5 better words" line; lower two thirds of the screen empty. 4.3 s before the first better word: the slowest part, and the first place I might swipe (H59 put the first word at 0.0 s).
- 4.3-8.0: Simple / a simple puzzle. Clear. But "simple" is a word I already know; the first reward is the weakest of the five.
- 8.2-12.3: Effortless. Good picture.
- 12.6-17.0: Straightforward: the most useful word here, and the longest beat (4.8 s).
- 17.3-21.8: Painless. Subscribe button arrives with the bare word, 1.5 s before the picture.
- 22.1-25.3: Foolproof. The pan that looks like a magnifying glass.
- 25.3-26.4: fifth card held in silence. 26.4-27.1: opening card back. Nothing asks me anything; I either let it loop or leave.
Swipe risk: moderate at 1.5-4.3 s, moderate at 12-17 s where the pattern is known.

## Takeaway test
"Tomorrow I say 'straightforward instructions', 'an effortless win', 'a foolproof recipe' instead of 'very easy ...'." Nameable, so not DOESN'T. Not SOLVES: I cannot tell which word to pick for a new noun (a very easy exam? a very easy job?), and I never tried one.

## Retention risks
- 27.1 s for five words at one fixed rhythm (word, about 1.2 s of silence, phrase): half of the running time is silence or a bare headline.
- 4.3 s before the first new word.
- Loop seam pop (above). 1.1 s of nothing happening before the loop card.
- Wallpaper words drifting behind the content.

## Trust risks
- "Stop saying": "very easy" is correct English. Lane convention, accepted.
- "Simple" is offered as a better word for "very easy"; it means "easy", not "very easy". Small overclaim.
- funny: "hysterical" and "priceless" are informal; no label on screen. fast: "breakneck" is used almost only in "at breakneck speed/pace": the example shows that correctly, but a learner will still write "a breakneck car".
- No wrong facts, no unnatural English found in any of the three.

## Top 3 fixes (by impact)
1. visuals (then shorts-builder re-render of easy only): replace the frying-pan emoji on "a foolproof recipe" with one that cannot be read as a magnifying glass (pot of food, cake, chef) and keep the OK hand.
2. shorts-builder: make the loop card equal to frame 0, or start the video with the headline already at full size, so the replay has no size pop; keep the wallpaper phase the same if cheap. Applies to all three and to the lane if H60 wins.
3. scenario-writer + language-editor: a 1-3 word use tag under each headline (no effort / no trouble / cannot go wrong ...) so the viewer can choose a word for a new noun; this is what moves the lane from PARTLY to SOLVES. Next batch, not this render.
Smaller: start the subscribe animation when the picture of that beat is up; put the strongest word first instead of "Simple".

## Sister videos
- l1-very-funny-h60-v1: no blocker. Resolution, subscribe animation (18.4 s recorded in json and meta), transcript, ending, pictures all pass.
- l1-very-fast-h60-v1: no blocker. Same (16.5 s recorded in json and meta). Best pictures of the three.
- Both have the same loop seam pop as easy.

## What was not checked
Listening by ear (all three); the Shorts feed overlay on a real phone (right-edge buttons over the second emoji); sisters were checked at 1 frame per second plus close-ups of beats 2-5, not frame by frame; YouTube itself (not touched). No file rendered, changed or uploaded; this review is the only file written. Mirror rule not applied (no user message in this task).
