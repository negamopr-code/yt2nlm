# Viewer-critic review: pd3-delulu-v1 (lab H86 batch 2, old movie x Gen Z slang)
Reviewed 2026-10-22. `state/shorts/pd3-delulu-v1/final.mp4`: 1440x2560, 30 fps, 14.10 s. Clip: Big Business (1929). Segments [219.5,222.4] [239.4,240.9] [228.6,230.3] [230.5,232.8] [298.6,302.0] [308.5,310.8]. subscribe_at [7.2] in final.subscribe.json, but NOT recorded: content/youtube/pd3-delulu-v1.json does not exist.

## Verdict: PARTLY - the meaning lands and the picture tells the joke, but there is a 3-frame bright flash at 6.30-6.37 and the subscribe button covers the "Gen Z slang" tag
## Pain (verbatim from the learner corpus, no NotebookLM query)
- "Defo... accent or slang words just make the things more difficult."
- "Is crashing out actually real? I get that it's used online but is it actually spoken?"
- "A lot of the English is a movie is slang ... it is difficult for a person who is not from the USA"
- "that's just an escape to delulu-land" (the word really shows up in comments)
Pain: "I see slang in comments and I don't get it." Solved means I read "delulu" tomorrow and know it means believing something that will clearly not happen.

## Heard (faster-whisper small.en)
0.00 He's sure his charm can sell a Christmas tree to anyone. / 4.16 Delulu means believing something that is clearly not going to happen. / 8.82 Spoiler, nobody wants the tree. 11.00 Totally delulu. / 12.08 Ever been this delulu? (ends 13.3). No spelled-out words.

## Second by second
- 0.00-2.93 Frame 0: "POV: you think your charm can sell anything" over a dark BACK view of a man carrying a tree to a door. It's readable as "a guy selling a tree", but it's dark, and the hook text does the work. It's acceptable.
- 2.93-4.4 Laurel and Hardy grinning at the door, under "his charm". Good match.
- 4.4-6.30 Insert of the sign "POSITIVELY NO PEDDLERS OR SOLICITORS" under the "delulu" definition. It's a diegetic sign, not an intertitle, and it is the joke (they knock anyway). But B1 viewers won't know "peddlers/solicitors", and it competes with the card for 1.9 s. Acceptable, and it's not a blocker.
- 6.30-6.37 STRAY: 3 frames of an over-exposed, brighter version of the sign (source about 230.5-230.67: there are shot changes at 230.59 and 230.67). It reads as a flicker.
- 6.40-8.55 Hardy laughing confidently under "delulu / believing...". Good.
- 8.57-11.6 The customer at his door refuses. "Spoiler: nobody wants the tree / totally delulu". Match.
- 11.6-14.1 Hardy and the customer with the tree, under "Ever been this delulu?". The answer is clear. It moves to the end with no freeze.
- Subscribe + bell: appears at about 7.25 and is red 7.5-8.4. In that window the button and bell sit ON the "Gen Z slang" tag (the beat-2 sub wraps to 2 lines and pushes the tag down to the button row). From 8.5 it shows SUBSCRIBED + bell under the "slang" tag with no overlap, and it is gone by about 12.
- Loop: Hardy with the tree goes back to Hardy walking with the tree. That's a clean, fitting loop. No watermark, no intertitle.

## HARD RULE
Clean. A tree-selling gag, no mockery of the actors, nothing sexual. Safe for a 13-year-old. No POLICY hit.

## Takeaway test
I can read "delulu-land" or "totally delulu" in a comment and understand it, and I can say "I was so delulu" about a plan of mine. Yes. There is no self-test beat (format-wide, same as batch 1).

## Top 3 fixes
1. visuals: change segment 4 [230.5,232.8] to [230.75,232.8] (skips the bright sign fragment and the 230.59/230.67 shot changes). Footage drops by 0.25 s, so extend the last segment to [308.5,311.1] so it still covers T = 14.02. Check that 311.1 is still the same shot; there is no scene change detected before 314.8.
2. shorts-builder: rerun subscribe_anim with SUBSCRIBE_AT >= 8.5 (after the 2-line beat-2 card ends at 8.49), so it never covers the "Gen Z slang" tag. Or language-editor shortens the beat-2 sub to one line. Then create content/youtube/pd3-delulu-v1.json with "subscribe_at": [<new time>].
3. visuals (optional): to make the opening easier to read, start on [222.4-ish] Hardy at the door instead of the dark back view. Not required.

---
# Pass 2 (2026-10-22, re-render 17:43)
Segments [219.5,222.4] [239.4,240.9] [228.6,230.3] [230.75,232.8] [298.6,302.0] [308.5,311.1]. 1440x2560, 14.10 s. Meta content/youtube/pd3-delulu-v1.json has subscribe_at [8.6], the same as final.subscribe.json.
## Verdict: SOLVES (for this format) - ship
- Every cut was checked frame by frame (2.93 door to L&H, 4.50 to the sign, 6.23 sign to L&H, 8.17 L&H to the customer, 11.77 to Hardy/Laurel with the tree). The bright 3-frame sign flash is gone. 8.27-8.80 is a 0.5 s wide shot of the customer's door, then the film's own cut to a closer shot of the same moment. It's the same place and action, not a stray.
- Subscribe appears at 8.6 under the 1-line "totally delulu" card, red 8.6-about 11, then SUBSCRIBED + bell. It sits BELOW the "slang" tag and covers no text. The "Gen Z slang" tag is now fully visible 4.0-8.5.
- Frame 0 is unchanged (the dark back view with the tree; the hook text carries it). Motion runs to the end with no freeze. Loop: Hardy and Laurel with the tree go back to Hardy carrying the tree, clean.
- Transcript unchanged, no spelled-out word. No POLICY hit.
