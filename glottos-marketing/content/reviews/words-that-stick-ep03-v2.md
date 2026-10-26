# Viewer-critic: Words That Stick Ep3, POLISHED e3-v2.mp4

Reviewed 2026-10-26 by glottos-viewer-critic (step "episode 3: polish" re-review).
- Video: `content/episodes/E3/e3-v2.mp4`, 1440x2560, 78.17 s. Subscribe+bell at 61.1 s (`content/episodes/E3/e3-v2.subscribe.json`).
- Build: `content/episodes/E3/polish-v1-build/` (plan.py cuts, stage2.py cards/captions).
- Previous review: `content/reviews/words-that-stick-ep03-v1.md` (5 blockers on the raw file).
- Heard audio: faster-whisper small.en with word timings, run on the v2 audio, plus silencedetect (-40 dB, 0.6 s). Frames: 32 frames (every beat plus the seams at 2.9/3.3, 21.0-23.1 and 42.8-45.2), plus full-res crops of the quiz, sturdy and subscribe areas.
- Pain evidence: same as v1 (PROBLEM 01 synthesis quotes in the v1 review §1). No NotebookLM query was used.

## Verdict: PARTLY. It is one small rebuild away from SOLVES.
All 5 v1 blockers are fixed, and the takeaway is clear. But the subscribe button covers the second line of the rule caption ("...and 7." / "...just once.") for about 5 s (61.2-66.0). That rule is the one line a viewer would screenshot. Also, the Ep3 meta has no `subscribe_at` and still points to v1, so under the 2026-10-05 rule the video is not finished.

**ship_blockers: 2.** No spelled-out word. No POLICY hit.

## Pain → given → gap
- Pain (learners' words): "when I try to speak I forgot every sentence in my mind !! My mind became blank ..."; "I can understand 100% of the video, but when I try to speak, my mind goes blank". In one sentence: "I learn new words, but a few days later they are gone."
- Given: the 1-3-7 schedule with one action per day, a recognise/recall self-test with a real 2 s pause, the rule "not every day, not just once", a clear action for tomorrow, and 5 ways to say STRONG as a channel bonus.
- Gap: the hook is a promise, not a pain callout ("Forget new words in days?"). That is acceptable. The rule caption gets hidden at the exact moment it matters.

## v1 blockers: status
1. "The secret?": GONE. Heard: "...these three days only. A word sticks best..." with about 0.6 s between them and a clean seam at about 2.9 s.
2. Hook picture: FIXED. The card "Review new words on these 3 days only" with DAY 1/3/7 tiles is on screen 0-3.0 s and matches the voice from frame 1.
3. Quiz pause: FIXED. The silence is exactly 20.99-23.00 s (2.0 s). The question frame and the caption "Recognise or recall?" are held. The answer picture is first seen at 23.1, together with "Well".
4. "Think of it like this": FIXED. The audio is silent 42.48-44.21. The card "5 ways to say STRONG" is clear. The flexed arm on the memory slide is now a green check, and the arm appears only for "muscular".
5. CTA magnifier: FIXED. Logo + anotherwordfor.net + "another word for STRONG", with no magnifier and no search box. Own teaser card "NEXT: Why you freeze mid-sentence" at 76.1-78.2. The Gemini end card is cut.

## Heard transcript (v2, language check)
0.00 Review new words on these three days only. / 3.12 A word sticks best when you recall it just before you forget it. / 7.62 So day one, see the word again in its sentence. / 11.26 Then, day three, cover it up and recall it before you look. / 15.48 Think about this. You know her face, but not her name. / 19.48 Recognize or recall? / [2.0 s silence] / 22.72-23.0 Well, you recognize the face, you just can't recall the name. / 26.64 Finally, day seven, use it in a new sentence of your own, out loud. / 31.96 Why do this? Each review resets the forgetting curve, and it falls more slowly each time. / 37.84 By day seven, a word you used yourself is much harder to forget. The memory's strong. / [silent card] / 44.26 A good handshake is firm. / 47.02 A ladder that stays steady when you climb it is sturdy. / 50.84 Hiking boots that last for years are durable. / 53.72 A huge old oak tree is mighty. / 58.12 And a weightlifter's arms are muscular. / 61.18 So remember, days one, three and seven. Not every day, and not just once. / 66.94 Try it tomorrow. See today's new words again in their sentences. / 71.76 Look up another word for strong on anotherwordfor.net. / 76.5 Next: why you freeze mid-sentence. (end 78.0)
- No spelled-out word. The only hyphen token is "mid-sentence", which is a normal word. No banned words ("secret", "proven", "search", app names).
- Captions are word-synced, in UK spelling ("Recognise", "recognise"), and the English is natural. Caption "After day 7," is shown while the voice says "By day seven". This is the intended correction, and a B1 viewer will barely notice it.
- The slide text inside the picture says "when you climb is sturdy" (no "it") while the voice and caption say "climb it". The sentence is still grammatical. Minor.

## Second by second (scroller view)
- 0-3.0: big hook card, voice from 0.0. Clear and on-topic. Low swipe risk for anyone who forgets words, but it doesn't say "forget".
- 3.0-15: the slides with DAY 1 and DAY 3 chips are legible. Inner gaps are about 0.8-1.0 s. Fine.
- 15.5-23: quiz. The 2 s freeze works as a real self-test.
- 23-42.5: answer, DAY 7, then the curve slide (the zig-zag stock chart is still weak; known, optional) and the memory slide with a check and a lock. OK.
- 42.5-44.5: "5 ways to say STRONG" card. It overlaps 0.3 s into "A good handshake" (the card ends at 44.55). Minor.
- 44.3-60: five word slides, readable. **Sturdy slide (47-50.7):** the tree-climber patch is a VISIBLE flat pale rectangle in the lower right. It breaks the grid paper and has leftover slivers at the bottom edge. It looks like a cover-up. Not a blocker, but it looks cheap.
- **61.2-66.0: the SUBSCRIBE / SUBSCRIBED + bell button sits on the second caption line.** It hides "and 7." and then "just once." The DAY 1·3·7 chip above stays visible and the voice says the rule, so this is not fatal, but it is the most screenshot-worthy line in the video.
- 66.9-71: the "Tomorrow..." slide is clear. The "17" calendar date is random but harmless.
- 71.7-78.2: CTA card, then the teaser card, with a fade-out. Good ending. No dead air.
- Every slide has a small grey smudge in the lower right where the watermark was removed (delogo). Barely visible. OK.
- Layout: the 16:9 picture band plus the captions use the upper two-thirds, and the bottom third is empty. That is acceptable for Shorts, because the platform UI covers that area.

## Takeaway test
"Tomorrow, look at today's new words again in their sentences. Cover and recall them on day 3. Say them in your own sentence on day 7." It is heard at 61-71 s and shown as DAY 1·3·7. PASS.

## Retention / trust
- Length 78 s for 12 points is OK. Pacing is natural (no 0.9x slowdown). No repetition problem.
- Trust: no false facts. "Celebrity" tag on a drawn face in the quiz (top left, small): no real or named person. Low risk, optional fix. POLICY: none.

## Ship-blockers
1. **61.2-66.0 subscribe animation covers the rule caption** ("days 1, 3 and 7." / "Not every day, and not just once."). Fix: move the animation corner or y-position clear of the caption box (e.g. into the empty bottom third, around y 1900-2100 at 1440 width), or move it to 66.9-71 or after the CTA (about 71-76, which is still in the second half). Owner: shorts-builder.
2. **`content/youtube/ep03.json` has no `"subscribe_at"`, and `video_ids_local` still lists `words-that-stick-ep03-v1`.** Add `"subscribe_at": [61.1]` (or the new time after fix 1) and point it to the v2 render. Owner: shorts-builder.

## Top 3 fixes by impact
1. shorts-builder: re-place the subscribe animation so it doesn't touch the rule caption, and record `subscribe_at` + v2 in ep03.json.
2. visuals/shorts-builder: refill the sturdy-slide patch with grid-paper texture (or crop/zoom that slide) so no flat rectangle shows.
3. visuals (optional): replace the zig-zag forgetting-curve picture with a curve that drops more slowly after each review, and remove the "Celebrity" tag. Then the language-editor gives the final pass.

## Not checked
- I did not listen by ear. The audio check used whisper and silencedetect only, so I can't rule out a click at the 2.85 s or 22.45 s seams.
- I did not view every frame (32 frames + 4 full-res crops). The mirror journal was not touched, because this step has no user message.

## Rebuild (2026-10-26, file content/episodes/E3/e3-v2.mp4, mtime 03:54)
**Verdict: SOLVES.** Both earlier ship-blockers are fixed. **ship_blockers: 0.** No POLICY hit. Audio was not re-checked because the builder says it is unchanged.
- Format: 1440x2560, 24 fps, 78.17 s. PASS.
- 60-67 s: the layout is higher now. At 61.5-65.5 s the SUBSCRIBE button, then SUBSCRIBED, and the bell sit BELOW the caption box ("So remember: days 1, 3 and 7." / "Not every day, and not just once."). The DAY 1·3·7 chip and the full caption stay readable the whole time. FIXED (blocker 1).
- ep03.json: `"subscribe_at": [61.1]`, and `video_ids_local` now lists `words-that-stick-ep03-v2`. FIXED (blocker 2).
- 44-45 s: the "5 ways to say STRONG" card is still on screen at 44.2 with the first caption word. By 44.35 the handshake slide is showing. The overlap is about 0.1 s, which nobody will notice. OK.
- 47-51 s, sturdy slide: the patch is bigger but still a FLAT pale-green rectangle, about 310x285 px in the lower right of the picture band. It is a different colour from the grid paper, has no grid lines and runs over the band's bottom border line. It is more visible than before and still looks like a cover-up. This does not block shipping, but it is now the top cosmetic fix. Fix: fill it with grid-paper texture (clone a nearby patch), or crop or zoom that slide so the climber is cut out. Owner: visuals/shorts-builder.
- Whole-video pass (28 frames, 1-77 s): the logo header is on every slide, the captions are clear of the picture, and there are no empty or black frames. CTA and NEXT cards are fine. The bottom third is empty, which is fine because the Shorts UI covers it.
- Not checked: listening by ear, and every single frame.
