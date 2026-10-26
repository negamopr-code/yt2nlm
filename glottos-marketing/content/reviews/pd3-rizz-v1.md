# Viewer-critic review: pd3-rizz-v1 (lab H86, old movie x Gen Z slang)
Reviewed 2026-10-18. `state/shorts/pd3-rizz-v1/final.mp4`: 1440x2560, 30 fps, 11.90 s. Clip: Two Tars (1928). Segments [199.4,201.9] [215.6,219.8] [222.8,226.2] [226.4,228.0] (11.7 s of footage for T = 11.83). subscribe_at [6.0], NOT yet recorded in content/youtube (no pd3 meta file exists).

## Verdict: PARTLY - the meaning lands, but the opening is wrong: the hook sits over the girls and there is a 0.3 s stray-shot flicker at 2.4-2.7
## Pain (verbatim from the learner corpus, no NotebookLM query)
- "Defo... accent or slang words just make the things more difficult."
- "Is crashing out actually real? I get that it's used online but is it actually spoken?"
- "A lot of the English is a movie is slang ... it is difficult for a person who is not from the USA"
- "how do you build your on your vocab if not studying slang and idioms?"
- "Don't try to rizz my gummy bear" (the word really shows up in comments)
Pain: "I see slang in comments and I don't get it." Solved means I read "rizz" tomorrow and know it means charm or flirting skill.

## Heard (faster-whisper small.en)
0.00 Two sailors see two girls, and they think they are so smooth. / 4.18 Rizz means charm, the skill of attracting someone. / 7.54 If he's got rizz, he's good at flirting. / 10.16 Do they have rizz? (ends 11.0). No spelled-out words.

## Second by second
- 0.00 Frame 0: "POV: they think they have rizz" (2 lines, big, readable) over the TWO GIRLS (one with the gumball jar). "They" reads as the girls. The sailors are not shown.
- 0.00-2.40 Girls. The voice says "Two sailors see two girls", but I only see girls.
- 2.43-2.53 STRAY: a 4-frame flash of the two sailors in their car (source 201.80-201.9, the shot that should be the establishing shot).
- 2.57-2.70 STRAY: a 5-frame flash back to the girls (source 215.6-215.76) before the cut.
- 2.73-6.7 Hardy close-up, grinning, then looking down coyly. "rizz / charm; the skill of attracting someone". Good match.
- 6.7-9.33 Laurel grinning. "he's got rizz / he's good at flirting". Match.
- 9.33-10.5 The girl smiles back. Good. There is a 0.2 s jump at 10.07 (segment join 226.2 to 226.4 inside the same shot).
- 10.5-11.9 Laurel grinning under "Do they have rizz?". It moves until the end, so no freeze.
- No intertitle in the final (the "The fleet's in!" title at about 211 s is avoided). No watermark.
- Subscribe + bell: it appears at 6.0, is red 6.25-7.5, shows SUBSCRIBED from about 7.75 with the bell, and is gone by about 11. It sits under the tag and covers no text.
- Loop: Laurel back to the girls, a clean cut. The audio loops cleanly.

## HARD RULE
Clean. 1920s clothed women, grins, and "good at flirting" with no body talk. Safe for a 13-year-old. No POLICY hit.
Note: the frame-0 composition (the hook word "rizz" over two women at chest height) is the weakest framing in the batch. Moving frame 0 to the sailors (fix 1) also removes that.

## Takeaway test
I can read "he's got rizz" in a comment and understand it. I could say "he's got rizz" about a friend. Yes. There is no self-test beat (format-wide).

## Top 3 fixes
1. visuals: re-cut the opening so the sailors come first, and remove both flashes. New segments: [202.3,204.6] (sailors in the car, Laurel turns to look; the shot runs 201.80-204.71), [199.6,201.75] (girls), [215.85,219.0] (Hardy), [222.8,227.6] (Laurel, girl smiles, Laurel, in one piece; this also removes the 10.07 jump). That is 12.4 s of footage, at least T = 11.83. Check that 202.3 is a clean frame. Then shorts-builder re-renders and reruns subscribe_anim.
2. shorts-builder/publisher: create content/youtube/pd3-rizz-v1.json with "subscribe_at": [<new time>].
3. scenario-writer (optional): the hook "POV: they think they have rizz" works once frame 0 shows the sailors. No text change is needed.

---
# Pass 2 (2026-10-18, re-render 12:59)
Segments [202.3,204.6] [199.6,201.75] [215.85,219.0] [222.8,227.6]. 1440x2560, 11.90 s. Meta content/youtube/pd3-rizz-v1.json has subscribe_at [6.0].
## Verdict: SOLVES (for this format) - ship
- 0.00-2.42 Frame 0 shows the two sailors in their car, and Laurel turns to look, under "POV: they think they have rizz" and "Two sailors see two girls". "They" now means the sailors.
- 2.42-4.58 The girls (1 shot). 4.58-7.79 Hardy grins, then looks down coyly, under "rizz / charm". 7.79-10.38 Laurel grins under "he's got rizz". 10.38-11.9 the girl smiles back under "Do they have rizz?". That works as an answer.
- Every cut was checked frame by frame. No stray frames, no flicker, and the 10.07 jump is gone. There is one frame of film dirt over Laurel at about 2.3 (in the source, negligible). No freeze; there is motion to the end. No intertitle.
- Subscribe red at about 6.2-7.5, then SUBSCRIBED + bell. It covers no text. Transcript unchanged, no spelled-out word. Policy clean: no POLICY hit. Loop: girl back to sailors, clean.
- Remaining nit (format-wide): no self-test beat.
