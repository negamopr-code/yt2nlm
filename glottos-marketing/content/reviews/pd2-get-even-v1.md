# Viewer-critic review: pd2-get-even-v1 (lab H85, old-movie situation Short)

Reviewed 2026-10-17. File `state/shorts/pd2-get-even-v1/final.mp4`: 1440x2560, 30 fps, 12.30 s, AAC 48 kHz stereo, mean -17.8 dB, peak -1.5 dB. Unit `shorts/units/pd2-get-even-v1.json` (language hash 33e48e1d9d743653). Clip: Big Business (1929), segments 858-861, 865-868, 884-888 (10.0 s of footage for a 12.24 s voice track). `final.subscribe.json` subscribe_at [6.2].

## Verdict: PARTLY - 3 blockers, do not ship
The words are right, and the window-smashing revenge fight is the perfect picture for "get even". But the segment in/out points ignore the film's shot cuts, so two stray shots flash by at 2.6-3.4 s. The footage runs out at 10.0 s and the last 2.3 s are a frozen, empty dark window. The promise card is also too wide for the screen and is clipped at both edges.

## Pain (learner's words; there is no PROBLEM doc for this lane, so I reused the batch-1 corpus evidence and spent no NotebookLM query)
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank."
- "great video but please shorten the intro!"
- "You have use the wrong synonym for rude"
Pain: "I say the same words all the time". Every time it's "revenge".
Solved means: tomorrow I say "I'll get even with him" or "she finally settled the score".
What it gives: three correct expressions with meanings and tags (informal, everyday, idiom). Gap: the broken picture at the start and the end undermines it, and there is no self-test.

## What is heard (faster-whisper small.en, word timings)
0.00 Your neighbour took your parking space. / 2.44 You don't just want revenge. / 4.44 You want to get even. / 6.08 You want to pay him back. / 7.82 You want to settle the score. / 9.82 Would you get even, or let it go? (ends about 11.6). Every word is heard as written. No spelled-out words (whisper prints "neighbor", which is only its spelling). Gaps are about 0.6 s.

## Source shot map (frame-difference cuts in big-business-1929.webm)
857.92 | 860.62 | 862.54 | 865.42 | 868.04 | 870.67 | 873.42 | 876.42 | 883.50 | 886.88 | 891.0
- 857.92-860.62: Laurel and Hardy smash the front window (wide).
- 860.62-862.54: a policeman in his car, close-up.
- 862.54-865.42: the homeowner wrecks their car while a crowd watches.
- 865.42-868.04: window smash continues (wide).
- 868.04-870.67: the car and the crowd, wide.
- 870.67-873.42: the car explodes in white smoke.
- 873.42-876.42: the policeman again.
- 876.42-883.50: the car wreck aftermath, wide.
- 883.50-886.88: a man hacks at the house wall with a pickaxe.
- 886.88-891.0: an empty smashed window, dark close-up.

## Second by second (cuts in the final at 2.62, 3.00, 3.42, 6.00, 8.92)
- 0.0 Frame 0: the yellow hook "POV: your neighbour took your parking space" over two men tearing a window frame off a house. There is motion from frame 0 and the situation reads at once. Good hook.
- 0.0-4.4 The grey promise "3 better ways to say 'get revenge'". BLOCKER: it is wider than the 1440 px frame. The "3" is cut in half on the left and the closing quote is cut off on the right (frame 1.0 checked at full size).
- 2.62-3.00 BLOCKER: a stray close-up of a policeman at a steering wheel (source 860.62-861.0, the next shot after the window smash).
- 3.00-3.42 BLOCKER: another stray shot, a wide shot of a crowd around a wrecked car (source 865.0-865.42, the tail of the 862.54 shot), before the window smash returns at 3.42. A viewer sees two random flashes under "You don't just want revenge". It looks like an editing error.
- 3.42-6.0 Window smash (wide). get even / hurt someone back as much as they hurt you / informal (spoken 4.94). Match. The sub wraps with "you" alone on line 2, which is minor.
- 6.0-8.92 A man hacks at the house wall with a pickaxe. pay someone back / punish someone for what they did / everyday (spoken 6.56). Match.
- 6.2 Subscribe + bell at the bottom left, under the tag. It is red SUBSCRIBE at about 6.5-7.5, SUBSCRIBED by about 8, and the bell rings at about 9.5. It covers no text. 6.2/12.3 = 50%, so it is in the second half.
- 7.7 settle the score / get revenge for something in the past / idiom (spoken 8.26). It starts over the pickaxe, but at 8.92 the picture cuts to an empty, dark smashed window (source 886.88-, a different shot). That is a weak match.
- 9.7 The hook box swaps to "Would you get even, or let it go?" (2 lines; "go?" sits alone on line 2).
- 10.0-12.3 BLOCKER: FROZEN. The footage ends at 10.0 s (segment 884-888) and the last frame of the dark window is held for 2.3 s (motion 0.0-0.4). The closing question and the loop sit over a still image, which is exactly the "frozen tail" the format forbids.

## Loop
A frozen dark window jumps to a bright window smash. The freeze makes the seam obvious. Audio: "...or let it go? / Your neighbour took..." with no echo.

## Takeaway test
"I'll get even with him." / "She finally settled the score." I can name them, so the verdict is PARTLY rather than DOESN'T. The register tags are useful: get even = informal.

## Checklist
- 1440x2560: yes. The promise overflows the width (above). Everything else fits.
- Credit "Big Business (1929)": shown. No intertitle, no modern intro, no watermark, no magnifying glass.
- Subscribe + bell at 6.2 s: yes.
- Meta: `content/youtube/pd2-get-even-v1.json` DOES NOT EXIST yet. It must record `"subscribe_at"` after the re-render (shorts-builder / publisher).

## Retention risks
- The stray flashes at 2.6-3.4 s fall exactly in the "do I keep watching" window.
- 12.3 s is the longest pd2 Short, and its last 2.3 s are frozen.
- The empty black bottom band (about 30%).

## Trust risks
- The hook (a parking space) is invented, while the picture is a house being smashed. As a POV joke this is acceptable: escalation is the gag.
- "pay him back" (spoken) vs "pay someone back" (card): this is a normal citation form, fine.

## Top 3 fixes, by impact
1. Re-cut the segments so each one sits inside a single shot and the footage covers the whole 12.3 s (visuals, then shorts-builder). The build should cut on the shot boundaries above. Suggested order, about 12.35 s in total (check the frames before you commit):
   - 858.0-860.6: window smash, under the hook.
   - 865.45-868.0: window smash, under "don't just want revenge" / "get even".
   - 862.6-865.4: the homeowner wrecks their car, under "pay him back".
   - 870.7-873.4: the car explodes, under "settle the score".
   - 883.55-885.25: the pickaxe on the house, under "Would you get even, or let it go?".
   This removes both strays and the freeze, and every word gets an act of revenge on screen. Avoid the policeman shots (860.62-862.54, 873.42-876.42) and the dark window (886.88-).
2. Fit the promise inside the frame (shorts-builder). Auto-shrink the promise text to the frame width, OR shorten it to "3 ways to say 'get revenge'" (scenario-writer + language-editor). The builder should also refuse any card wider than the frame, because this went out unchecked.
3. After the re-render, create `content/youtube/pd2-get-even-v1.json` with the new `subscribe_at` (shorts-builder / publisher). Optionally, re-wrap the get-even sub so "you" is not alone on its own line, e.g. "hurt someone as much as they hurt you" (language-editor).

---

## Pass 2 (2026-10-17, re-cut 858.0-860.6 / 865.45-868.0 / 862.6-865.4 / 870.7-873.4 / 883.55-885.25)

**Verdict: SOLVES the pain, but HOLD: one ship-blocker remains, a 1-frame stray at 8.07 s.** The re-cut fixed everything from Pass 1: there are no policeman flashes, no frozen tail, every word lands on an act of revenge, and the promise card fits. But one foreign frame flashes in exactly where I said to cut.

What I checked:
- Frame-difference over the picture band for all 367 frames.
- Frame-by-frame strips at every cut.
- The segment files `state/shorts/pd2-get-even-v1/seg0-4.mp4`.
- A contact sheet every 0.5 s.
- A faster-whisper transcript of `final.mp4`.

### Ship-blocker
- **8.07 s (output frame 242): one frame of the window-smash shot (bright white house wall) sits between the dark car-wreck shot and the car-explosion shot.** It shows as a white flicker under "settle the score". Cause: `seg2.mp4` (source 862.6-865.4) is encoded as 69 frames at 24 fps = 2.875 s. That runs it to about 865.475, past the shot boundary at 865.45. Its last frame (n=68) is the first frame of the window-smash shot. I verified this in the seg2 tail frames, and seg3 starts clean on the car.
  - Fix (shorts-builder): end segment 3 at **865.35** instead of 865.4. A general fix is better: make the builder floor segment length to whole source frames, so it never rounds past `end`. If the 0.05 s needs to come back, extend the last segment to 883.55-885.30 (the pickaxe shot runs to 886.88).
  - Seg0 (2.63 s, to about 860.63) brushes the policeman shot at 860.62. The output frames there (74-82) are all window smash, so it is fine as rendered. The builder fix above would protect it as well.

### The rest (passes)
- **Cuts:**
  - 2.6 s: smash to smash, a clean join.
  - 5.23 s: smash to the homeowner wrecking his car.
  - 8.07/8.10 s: the stray above.
  - 10.80 s: smoke to the pickaxe, clean.
  - The 8.97 s peak is the explosion flash itself, not a cut.
- **Heard vs picture:**
  - 0.00 "Your neighbour took your parking space" / 3.04 "revenge": window smash. Match.
  - 4.94-5.3 "get even": window smash. The cut comes right after the word ends. Match.
  - 6.56 "pay him back": the homeowner tears up the car. Match.
  - 8.26-8.9 "settle the score": the car sits still for about 0.9 s, then explodes at 8.97, just after "score". This is acceptable, and it reads as the punchline.
  - 9.82-11.4 "Would you get even, or let it go?": smoke, then the pickaxe on the house. Match.
  - No spelled-out words. Whisper hears "neighbor", which is just its US spelling.
- **Tail / loop:** live pickaxe footage to the last frame (diff 4-5 per frame up to 12.2 s), so there is no freeze. The loop goes house to house (pickaxe to window smash) and reads naturally.
- **Cards inside the frame:**
  - The promise "3 ways to say 'get revenge'" is now fully inside, with a margin.
  - All word cards and tags fit.
  - Minor, not a blocker: two orphan wraps. The sub "hurt someone back as much as they hurt / you" and the hook "Would you get even, or let it / go?" each leave one word alone on line 2. Owner: language-editor, e.g. "hurt someone as much as they hurt you" and "Get even, or let it go?".
- **Subscribe:** red SUBSCRIBE is visible from 6.2 s (sheet frames 6.5-7.5), changes to SUBSCRIBED by about 8.0, the bell rings about 9.3-10.6, and it fades by about 11.0. It covers no text. 6.2/12.3 = 50%.
- **Takeaway test:** "I'll get even with him." / "She paid him back." / "He finally settled the score." The register tags (informal / everyday / idiom) tell me when to use each one.

### Top fixes
1. Trim the stray frame: segment 3 ends at 865.35, plus a frame-floor in the builder (shorts-builder). This is the only thing between this cut and SOLVES-and-ship.
2. Optional: fix the two orphan wraps (language-editor).
