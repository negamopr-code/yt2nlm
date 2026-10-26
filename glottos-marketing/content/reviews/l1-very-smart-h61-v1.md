# Viewer-critic review: l1-very-smart-h61-v1 (lab H61 "THE PACE": the 5-word lane in about 17 s) + sisters old, clean

Reviewed 2026-10-11. Files (all 1440x2560, 30 fps, voice Kokoro am_michael 1.05x, no music):
- state/shorts/l1-very-smart-h61-v1/final.mp4 (16.8 s) - full review
- state/shorts/l1-very-old-h61-v1/final.mp4 (17.1 s) - quick check
- state/shorts/l1-very-clean-h61-v1/final.mp4 (16.9 s) - quick check
Units: shorts/units/l1-very-{smart,old,clean}-h61-v1.json. Meta: content/youtube/l1-very-{smart,old,clean}-h61-v1.json.
Not judged as a defect (it is the test): the pace itself (pause after the word 0.25 s, trimmed clip ends, 0.15 s after the example, short closing card).

## Verdict: PARTLY (all three)
Five correct words with one ready phrase each, and at 17 s every word is still heard and every card can still be read; but one example is the only guide to use, I never try a word myself, and in smart the fifth word "Astute" is not recognisable by ear.

Ship blockers: smart 2, old 1, clean 0.

## BLOCKERS (fix before the user sees it)
1. smart + old: the subscribe button covers the picture.
   - smart, 11.4-12.45 s, beat 5 "Ingenious / an ingenious idea": the red SUBSCRIBE pill lies over the lower-left corner of the light-bulb card and the bell sits on the base of the bulb (frames 11.55, 12.00, 12.40 s).
   - old, 11.8-12.49 s, beat 5 "Vintage / a vintage radio": the pill covers the lower-left of the radio (its speaker grille and left foot), the bell touches the left dial (frames 11.95, 12.40, 12.44 s).
   - Cause: a single-emoji card is tall (bottom edge at about 79 % of the height); the pill sits at 71-77 %. Two-emoji cards are wide and low (bottom at about 68 %) and stay clear: that is why clean ("sparkling windows", window + sparkles) passes and why beat 6 passes in all three.
   - Fix (visuals, then shorts-builder re-render of smart and old): make picture 5 a two-emoji card - smart pictures.json key "5": "1f4a1 2728" (light bulb + sparkles); old pictures.json key "5": "1f4fb 1f3b6" (radio + notes). Alternative for shorts-builder: start the animation at the start of beat 6 (smart 12.45 s, old 12.49 s) with a 4 s length, and record the new time in final.subscribe.json and in the meta "subscribe_at". Do not move the pill lower: it would enter the caption zone.
2. smart, beat 6, 12.45-13.2 s: the bare word "Astute" is not heard as "astute".
   - Whole video, faster-whisper small.en: "A student and a student investor." (12.62-14.50 s). Segment 12.3-14.8 s alone: small.en "a student, an astute investor"; base.en "As Dude, an Astute Investor" / "As Dude and As Dude Investor". The clip b06-0.wav alone: "as dude" (both models). The first render with the 0.3 s pause gives the same "A student and a student investor", so this is the voice clip, not the pace.
   - The clip ends on a very weak final "t" (last 70 ms at -40 to -49 dB after the vowel); whether the trim took some of it cannot be told, the untrimmed clip was overwritten.
   - Why it blocks: it is the one C2 word of the set, the one I do not know; if I hear "a student" I learn a wrong sound for it. Same class as the "Since" case of H21 in the builder.
   - Fix, either: (a) scenario-writer + language-editor: replace beat 6 of shorts/units/l1-very-smart-h61-v1.json with a word Kokoro says cleanly and a B1-B2 learner will use, e.g. "Clever: a clever plan" (new approval hash, new picture 6); or (b) voice: a checked clip of the same voice for 6-0. Note for shorts-builder: with "trim_silence" set, build_stop_saying.py loads `AudioFileClip(j["out"])` directly and skips the `override-<beat>-<part>.wav` lookup of speak(), so an override file would be ignored on this path until that line is changed.
   - Not checked by ear (no playback here). Two recognisers and three runs agree; a human listen of 12.4-14.8 s settles it in ten seconds.

## THE question: can a learner catch each word and read its example at this pace?
Yes, with the one exception above, and with little to spare.

Heard (faster-whisper small.en, word timings):
- smart: 0.00 Stop saying very smart. | 1.64 Here are five better words. (ends 2.98) | 3.60 Brilliant | 4.20 a brilliant scientist | 5.84 Sharp | 6.44 a sharp mind | 7.82 Gifted | 8.52 a gifted student | 9.86 Ingenious | 10.92 an ingenious idea | 12.62 "A student" [= Astute, FAIL] | 13.5 "a student investor" [= an astute investor] | 14.88 Which one will you use today? (ends 16.14)
- old: 0.00 Stop saying very old. | 1.80 Here are five better words. | 3.56 Ancient | 4.38 an ancient temple | 5.72 Elderly | 6.54 an elderly neighbor | 7.98 Antique | 8.86 an antique clock | 10.30 Vintage | 11.12 a vintage radio | 12.72 Age-old | 13.52 an age-old tradition | 15.20 Which one will you use today? (ends 16.48)
- clean: 0.00 Stop saying very clean. | 1.66 Here are five better words. | 3.58 Spotless | 4.24 a spotless bathroom | 5.84 Immaculate | 6.82 an immaculate suit | 8.56 Pristine | 9.12 a pristine lake | 10.42 Sparkling | 11.34 sparkling windows | 12.90 Gleaming | 13.64 gleaming white teeth | 15.04 Which one will you use today? (ends 16.34)
- No word spelled letter by letter. No word dropped.

Clipping / run-on (measured, all 39 voice clips and the three finals):
- Every clip starts from below -60 dB and ends in a fall to -40..-60 dB over its last 60 ms; no clip stops at full level. "Brilliant", "Sharp", "Age-old", "Immaculate", "teeth" are each recognised alone and in the final with their last sound. "Astute" is the only one in doubt (above).
- Silence between a word and its example: 0.29-0.38 s in the finals. Silence between the end of an example and the next word: 0.20-0.26 s. Nothing overlaps, nothing runs into the next word. It does sound like one list read in a row: whisper joined "pristine, a pristine lake, sparkling, sparkling windows" (clean 8.56-12.42 s) into one sentence.
- old, bare "Antique" (7.98 s): small.en hears "Antique", base.en hears "and teak". Stress on the second syllable is right; noted, not a blocker.

On screen (from the clip lengths and the frames):
- Headline word: 2.0-2.7 s per card (shortest: smart "Sharp" 2.01 s). Enough.
- Example line + picture: appear together 0.9-1.1 s after the headline and stay 1.14-1.59 s. The example is spoken for all of that time, so I read along; the picture grows for its first 0.35 s, so it stands still for only 0.8-1.2 s.
  - Tightest: smart beat 3 "a sharp mind" 1.14 s (12 characters, fine); clean beat 4 "a pristine lake" 1.18 s; smart beat 4 "a gifted student" 1.23 s.
  - Most text per second: clean beat 6 "gleaming white teeth" 15.1 characters/s (1.32 s); old beat 3 "an elderly neighbor" 14.7 (1.29 s); smart beat 2 "a brilliant scientist" 14.6 (1.44 s). A learner reads comfortably at 12-13; these three pass only because the voice says the line at the same moment.
  - No card fails outright. But I get the line OR the picture on the first viewing, not both, and from 11.4-11.8 s a moving red button competes for the same second. The second loop fixes that; the first does not.
- Closing card: 1.9-2.0 s; "Which one will you use today?" is spoken (1.5 s), "Write it in the comments." is on screen from about 0.3 s in but not spoken. Readable once; no time left to decide which word.
- First better word at 3.2-3.6 s (lane: 4.3-4.5 s).

## Mandatory gates
1. Resolution: PASS, 1440x2560 on all three (ffmpeg stream header).
2. Subscribe + bell: present on all three at the recorded time, 5 s, lower-left; recorded in final.subscribe.json and in the meta "subscribe_at" (smart 11.4, old 11.8, clean 11.6); second half of the video. Red SUBSCRIBE -> grey SUBSCRIBED -> yellow bell, gone before the last 0.3 s.
   - smart: FAIL on position at 11.4-12.45 s (covers the light bulb). Clear on beat 6 and the closing card.
   - old: FAIL on position at 11.8-12.49 s (covers the radio). Clear after.
   - clean: PASS (pill under the window card, 71-77 % of the height; card ends at about 68 %).
   - It never covers a headline or an example line in any of the three.
3. Pictures fit the example: PASS.
   - smart: scientist with flask; brain + lightning; graduate + star; light bulb; rising chart + money bag. All read at once.
   - old: classical temple; old woman + house; mantel clock; radio; red lantern + fireworks (weakest: reads "festival", acceptable for "tradition").
   - clean: bathtub + sparkles; person in tuxedo (shows "suit", not "immaculate": acceptable); lake landscape; window + sparkles; grinning face + tooth.
4. Shorts interface zones: nothing in the bottom caption zone (lowest element is the subscribe pill at 77 %). Two-emoji cards and the long headlines ("Immaculate", "Ingenious") run to about 93-95 % of the width; the right-edge buttons may touch the second emoji. Lane layout, same as shipped Shorts; NOT checked on a phone.
5. Magnifying glass: none. No watermark, no garbled text. Logo is the channel avatar.

## Pain -> what the video gives -> gap
- Pain (my wording, from the brief): "I say 'very smart' about everybody; give me stronger words I can really use."
- Learner evidence: unchanged from the H59/H60 reviews. content/problems does not exist; content/insights/audience-needs.md has no quote about overusing "very", only format feedback ("great video but please shorten the intro!", "very helpful thanks :)") and viewers adding their own word under these Shorts ("Frigid too", "Melancholic too", "There is also minuscule as in a minuscule mouse."). No NotebookLM query spent. The pain is assumed from the brief, not proven by quotes.
- Solved would mean: tomorrow I say "a sharp mind" or "a gifted student" without thinking, and I do not say "an ingenious student".
- Gives: 5 words, each heard twice, one collocation and one picture each, in 17 s. The intro complaint is answered better than in the lane (first word a second earlier).
- Gap: nothing says which word fits which noun (brilliant/gifted = people, ingenious = ideas and devices, astute = judgement; elderly = people only, antique/vintage = things; pristine = untouched, not "washed"). No moment where I produce a word. At this pace there is also no silence in which I could repeat the word aloud: the lane's 1 s pause was the only place for that.

## Second by second (smart)
- 0.0-1.4: "Stop saying" + struck-out "very smart" from frame 1. My phrase. I stay.
- 1.5-3.2: "Here are five better words" / "5 better words". Shorter than the lane; lower two thirds empty.
- 3.2-5.6: Brilliant / a brilliant scientist. Clear; a word I half know.
- 5.6-7.6: Sharp / a sharp mind. Fastest card (2.0 s); fine because it is short.
- 7.6-9.7: Gifted / a gifted student. Fine.
- 9.7-12.45: Ingenious / an ingenious idea. Good. At 11.4 s the red button slides over the light bulb.
- 12.45-14.8: Astute. I read it, I hear "a student". I do not know this word and now I do not know how to say it.
- 14.8-16.8: question, 2 s, loop.
Swipe risk: low. Nothing drags; 17 s is over before I think of leaving. The risk here is the opposite: it ends before anything stuck.

## Takeaway test
"Tomorrow I say 'a sharp mind' / 'a gifted student' / 'a brilliant scientist' instead of 'very smart'." Nameable, so not DOESN'T. Not SOLVES: I cannot choose a word for a new noun, I never tried one, and one of the five I cannot pronounce after watching.

## Retention risks
- Length is no longer a risk. Density is: 10 spoken items in 11.5 s with 0.2-0.4 s between them.
- Picture stands still for about 1 s; on the first viewing it is a flash.
- Subscribe animation runs over 30 % of the video (5 of 17 s), across word 4, word 5 and the question.
- Wallpaper words drift behind the content (lane).

## Trust risks
- "Stop saying": "very smart" is correct English. Lane convention.
- smart: "Astute" misheard (blocker 2). "Astute" is C2 and formal; no label.
- old: "elderly" is for people only and "antique"/"vintage" for objects; shown correctly, not said. "neighbor" is US spelling, consistent with the voice.
- clean: "pristine" means untouched, "gleaming" means shining; neither is simply "very clean". Examples are natural.
- No wrong facts, no unnatural English.

## Top 3 fixes (by impact)
1. visuals + shorts-builder: subscribe button off the picture in smart (beat 5) and old (beat 5) - blocker 1.
2. scenario-writer + language-editor (or voice): "Astute" in smart - blocker 2; and shorts-builder: let the trim path honour override-<beat>-<part>.wav.
3. shorts-builder (unit keys): "tail_after_example" 0.15 -> 0.35 in all three. Costs 1.0 s in total (about 18 s), gives every picture and example about 20 % more standing time. Only if the test may keep "under 19 s"; otherwise leave it, the pace passes.
Next batch (scenario-writer): a 1-3 word use tag under each headline (people / ideas / things), the same fix that the lane needs to move from PARTLY to SOLVES.

## Sisters
- l1-very-old-h61-v1: 1 blocker (subscribe button over the radio, 11.8-12.49 s). Sound, pace, pictures, resolution pass.
- l1-very-clean-h61-v1: no blocker. The cleanest of the three; can go as it is.

## What was checked / not checked
Checked: stream headers; 40 frames per video (every beat: bare word, just before the example, example at +0.2 and +0.45 s, last frame of the card; subscribe animation at 7 moments; closing card); faster-whisper small.en with word timings on the three finals and on smart's first render; small.en and base.en on each of the 39 voice clips; head and tail level of every clip; silence map of each final.
Not checked: listening by ear; the Shorts feed overlay on a real phone; the untrimmed voice clips (overwritten by the trim); YouTube itself. No file rendered, changed or uploaded; this review is the only file written in the project (working frames in /tmp/h61). Mirror rule not applied (no user message in this task).
