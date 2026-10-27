# Viewer-critic review: h116-very-hard-part2-v1 (lab H116, Stop Saying "very hard" Part 2)

Reviewed 2026-10-27. File: /workspace/glottos-marketing/state/shorts/h116-very-hard-part2-v1/final-sub.mp4 (md5 9a6001cf..., 10:59 UTC, 1440x2560, 30 fps, 20.70 s, kokoro am_michael 1.15, no music). Unit: shorts/units/h116-very-hard-part2-v1.json (language approval 5458f4125c9c8483). Subscribe: final-sub.subscribe.json = [12.5], 5.0 s, corner bl; content/youtube/h116-very-hard-part2-v1.json has "subscribe_at": [12.5] (match).
Checked: faster-whisper small.en with word timings, ffmpeg silencedetect (-40 dB, 0.3 s), 18 frames (0.0/0.5/1.5/2.5/3.1/3.6/5.0/7.0/8.6/9.5/11.0/12.4/12.8/14.0/15.5/17.0/19.5/20.6) at 360 px, plus 720 px crops of the three pictures at 7.0/11.0/15.5 s; youtube meta. Not checked: listening by ear, thumbnail, YouTube rendering.
Pain evidence: no NotebookLM query spent. content/problems/ does not exist; there is still no verbatim learner quote about overusing "very" on file (same gap as H102-H115). On-file evidence is demand only (content/insights/audience-needs.md: Stop Saying Shorts lead; viewers add their own words, e.g. "Frigid too", "Melancholic too"). Pain (the brief's, NOT verbatim): "Everything difficult is 'very hard' for me." Solved = tomorrow I say "It's a challenging job", "I had a rough morning", "What a draining day!".

## Verdict: PARTLY
The cafe story is clear and the three words are useful and correctly used, but the Rough picture carries a visible smeared inpaint band (same defect class as the H115 Jittery blocker), the Challenging picture has a magnifying glass that does not zoom, the first better word arrives at 3.1 s (not the H115 "by 2 s" build the lane claims), and 2.1 s of silent end card makes it 20.7 s.

## Ship blockers
1. VISUALS: Rough picture (pic-03, on screen ~8.6-12.4 s). A wide white blurred rectangle across the front of the coffee machine (left-middle of the picture) reads as a broken/censored patch at phone size, not as steam. Owner: visuals (re-inpaint or regenerate: broken machine leaking coffee, Leo hands on head, no smear).
2. VISUALS (rule 2026-10-05): Challenging picture (pic-02, ~6.8-8.5 s) shows a magnifying glass at the top, cut by the frame, lens content not enlarged. A non-zooming magnifying glass is a defect. Owner: visuals (remove it; it means nothing in "busy cafe, new job").
3. SHORTS-BUILDER (hypothesis integrity): the lane says "H115 build (first better word on screen by 2 s)", but the hook speech runs 0.00-2.88 ("Stop saying very hard. Here are three more words.") and "Challenging" appears at 3.1 s (spoken 3.20). Frame 0 again shows only "Stop saying" (yellow "very hard" pops in by 0.5 s; "3 more words to use" only at ~2.5 s). If shipped as is, H116 does not test the H115 build. Either cut the hook to "Stop saying very hard." (~1.4 s) with all hook text on frame 0, or relabel the lane.
- No spelled-out word: "Challenging" 3.20, "Rough" 8.70, "Draining" 12.50 are whole words.
- POLICY: none. Cafe job, coffee machine, tired worker; nothing sexual, no real people, safe for 13+.
- No NotebookLM/Gemini watermark seen. Logo = channel avatar (top-left). Subscribe pill + bell 12.8-~17.5 s, bottom-left, second half: OK and recorded.

## Pain -> gives -> gap
- Gives: challenging (new job at a busy cafe), rough (the coffee machine breaks), draining (he serves every customer, day ends exhausted). One person, rising trouble, resolution: the story works, and all three sub-lines are natural English a B1 viewer can reuse.
- Gap 1: the story lines ("Leo starts a new job at a busy cafe.", "Then the coffee machine breaks.", "But he serves every customer!") are only spoken; on screen each beat shows the bare headline for ~2-3 s (3.1-6.7, 8.6-~9.5, 12.4-~14.8) and then only the "It's a X ..." line. Sound-off viewers lose the story.
- Gap 2: nuance never said. Draining = it takes all your energy (tiring), not "difficult"; rough = an unpleasant time/period. The pictures carry it (head in hands / head on the counter); acceptable, but "draining" as a straight swap for "very hard" is a stretch.
- Gap 3: no self-test; the end is "Which word will you use? Comment yours!" only.

## Second by second (heard / seen)
- 0.00-1.38 "Stop saying very hard." Frame 0.0: "Stop saying" only; 0.5: + yellow "very hard"; 1.5: red strike. It is my problem, I stop - after 0.5 s.
- 1.62-2.88 "Here are three more words." Screen adds "3 more words to use" at ~2.5. Filler sentence: swipe risk, nothing new for 1.3 s.
- 3.1 "1/3 Challenging" headline, no picture. 3.20 "Challenging" / 4.02-6.18 "Leo starts a new job at a busy cafe." Screen: headline only until ~6.7.
- 6.34-6.74 0.40 s silent. 6.72-7.92 "It's a challenging job." + picture (nervous young barista, busy cafe, matches) + floating non-zooming magnifying glass (blocker 2).
- 8.01-8.55 0.54 s silent.
- 8.6 "2/3 Rough". 8.70 "Rough" / 9.18-10.46 "then the coffee machine breaks." Picture with steam, spilled coffee, Leo hands on head (matches the words) but with the white smear (blocker 1).
- 10.90-11.76 "It's a rough morning." / 11.83-12.37 0.54 s silent.
- 12.4 "3/3 Draining" headline only. 12.50 "Draining" / 13.14-14.52 "but he serves every customer." Subscribe pill from ~12.8.
- 14.90-15.80 "What a draining day." Picture: Leo with head on the counter, cups stacked (matches, clean). Thin wide strip, smaller than the other two.
- 15.88-16.43 0.55 s silent. 16.44-18.30 "Which word will you use? Comment yours."
- 18.56-20.70 2.14 s silent end card (swipe point). 20.6 loop frame = hook with struck "very hard": loop works.

## Takeaway test
I can say "It's a challenging job" and "I had a rough morning" tomorrow; "What a draining day!" too. Real actions, so not DOESN'T.

## Retention risks
- Length 20.7 s, above the 13-18 s H102 band. Silence 0.40+0.54+0.54+0.55+2.14 = 4.2 s; with tail 0.5 s and holds 0.3 s it is ~17 s; with the hook cut to one sentence ~15.5 s.
- Each beat opens on a bare headline for 1-3 s before picture/sentence (worst: Challenging 3.1-6.7 s, 3.6 s of headline only).
- Voice 1.15 is clear, no podcast drag. Text large and legible; the background word wall plus faint logo tiles behind "It's a challenging job." is busy.

## Trust risks
- The Rough smear is the main trust hit; the magnifying glass is a second, smaller one.
- English: all lines natural and correct (language-editor gate passed; caps fine). "Draining" is about energy, not difficulty: minor overclaim as a "very hard" replacement.
- Description links Part 1 (BquM8WfPvfY): fine.

## Top 3 fixes (by impact)
1. visuals: clean the white smear on pic-03 (Rough) and remove the non-zooming magnifying glass from pic-02 (Challenging); ideally give Draining a full-height picture like the other two.
2. shorts-builder: full hook text on frame 0, cut "Here are three more words." (or move the count to the card only) so "Challenging" lands by ~1.6-2 s as the lane promises; show the picture on the same frame as the headline; end tail ~0.5 s, holds ~0.3 s.
3. scenario-writer (then language-editor gate): put the story line on screen while it is spoken (card.use above the "It's a X" line), and end with a 1-second self-test, e.g. "Your phone breaks before work. It's a ___ morning."
