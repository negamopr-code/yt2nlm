# Viewer-critic review: pd3-clock-it-v1 (lab H86 batch 2, old movie x Gen Z slang)
Reviewed 2026-10-22. `state/shorts/pd3-clock-it-v1/final.mp4`: 1440x2560, 30 fps, 14.80 s. Clip: Neighbors (1920). Segments [60.4,62.4] [62.4,64.4] [66.9,68.4] [69.0,72.0] [72.0,75.0] [75.2,77.3] (13.6 s of footage for T = 14.76, so a 1.2 s freeze). subscribe_at [7.6] in final.subscribe.json, but NOT recorded: content/youtube/pd3-clock-it-v1.json does not exist.
Source shot changes (ffmpeg scene > 0.25): 58.04 | 60.67 | 62.67 | 64.54 | 66.96 | 68.75 | 77.33 | 78.75. The shot after 77.33 is a different woman in another yard, so the cut-away is real.

## Verdict: PARTLY - the story (girl hides a love note, dad spots it and takes it) teaches "clock it" well, but frame 0 is a 0.27 s flash of the vignetted note insert, there is a 2-frame stray flash at 3.97, and the subscribe button covers the tag
## Pain (verbatim from the learner corpus, no NotebookLM query)
- "Defo... accent or slang words just make the things more difficult."
- "Is crashing out actually real? I get that it's used online but is it actually spoken?"
- "A lot of the English is a movie is slang ... it is difficult for a person who is not from the USA"
Pain: "I see slang in comments and I don't get it." Solved means I see "I clocked it" or "she clocked him" and know it means noticed (something hidden).

## Heard (faster-whisper small.en)
0.00 She's reading a love note from the boy next door. 3.24 Then her dad walks out. / 5.12 To clock something means to notice it, even when someone tries to hide it. / 9.70 Dad clocked that note in two seconds. / 12.14 Has anyone ever clocked you like this? (ends 14.06; about 0.7 s of silence on the freeze). "clock/clocked" is pronounced naturally. No spelled-out words.

## Second by second
- 0.00-0.27 STRAY / FRAME 0: 8 frames of the vignetted "I love you 2" note insert (source 60.4-60.67, the tail of the 58.04-60.67 shot). Frame 0, the thumbnail-like first frame, is a white card with script handwriting. To a scroller it looks like an intertitle card, and it's gone before anyone can read it.
- 0.27-2.23 The girl reads the note, then looks up dreamily. "She's reading a love note". Good.
- 2.23-3.93 Dad steps out of the doorway. "Then her dad walks out" (3.24-4.5). Good.
- 3.97-4.00 STRAY: 2 frames of the girl again (source about 64.4, the next shot starting).
- 4.03-5.5 Dad walking. 5.5-14.8 one long two-shot (source 68.75-77.33): dad walks up, the girl clutches the note to her chest (hiding it), and dad takes it. That shows "notice what someone tries to hide" while it's said. Strong.
- 9.6-11.75 "he clocked it / he noticed it right away": dad holding the note. Match.
- About 11.5: a 0.2 s jump inside the same shot (segment join 75.0 to 75.2).
- 12.0-13.6 The girl runs off while dad points with the note. 13.6-14.8 FREEZE on dad holding the note (1.2 s, the last 0.7 s silent). This is dead air before the loop.
- Subscribe + bell: appears at about 7.6 and is red 7.75-9.5, sitting ON the "Gen Z slang" tag (the 2-line beat-2 sub pushes the tag onto the button row). From 9.6 it shows SUBSCRIBED + bell under the "example" tag with no overlap.
- Card: the hook wraps as "POV: your dad sees the love / note", with the orphan word "note". It's cosmetic.
- Loop: the frozen dad goes to the note flash and then the girl. The flash makes the loop seam visible.

## HARD RULE
Clean. A teen love note ("I love you 2") and a father taking it: no romance beyond that, no violence, nothing sexual. NO blackface in any frame used (the whole range 60.4-77.3 was checked frame by frame at 4 fps plus every cut; the 77.33 shot after it is not used). The trans "clocking" sense is not taught. Safe for a 13-year-old. No POLICY hit.

## Takeaway test
I can read "I clocked it right away" or "she clocked him" and understand it. Yes. No self-test beat (format-wide).

## Top 3 fixes
1. visuals: re-cut to remove both flashes and the jump, and shorten the freeze. Use the unused girl-with-note shot 64.54-66.96 (she reads and sniffs the note: good beat-1 footage):
   [60.85,62.5] girl reads, then [64.75,66.7] girl sniffs the note and smiles, then [62.85,64.3] dad steps out (lands at about 3.6, under "Then her dad walks out"), then [67.15,68.55] dad walks, then [68.95,77.15] the whole two-shot in ONE piece (no 75.0/75.2 jump).
   That's about 14.1 s of footage for T = 14.76: the freeze drops to about 0.6 s on dad holding the note. Keep 0.15 s margins at every shot change, because the builder's cut landed about 0.15 s off the detected 64.54 change. Check frame by frame after the render.
   (Option instead of removing the note insert: hold it on purpose for at least 1.0 s as the opening, [59.6,60.6], under the hook. It's readable, "I love you 2" IS the love note, and it's text in the film rather than a title card. Removing it is the safer choice for the no-intertitle rule.)
2. shorts-builder: rerun subscribe_anim with SUBSCRIBE_AT >= 9.6 (after the 2-line beat-2 card), or language-editor shortens the beat-2 sub to one line ("to notice what someone is hiding"). Create content/youtube/pd3-clock-it-v1.json with "subscribe_at": [<new time>].
3. scenario-writer (cosmetic): a hook without the orphan, e.g. "POV: dad sees your love note".

---
# Pass 2 (2026-10-22, re-render 17:47)
Segments [60.85,62.5] [64.75,66.7] [62.85,64.3] [67.15,68.55] [68.95,77.15]. 1440x2560, 14.80 s. Meta content/youtube/pd3-clock-it-v1.json has subscribe_at [9.6], the same as final.subscribe.json.
## Verdict: SOLVES (for this format) - ship
- Frame 0 is now the girl reading the note under "POV: your dad sees the love note". The note-insert flash is gone, and so is the 2-frame girl flash at about 4.0.
- Cuts (frame by frame): 1.70 girl looking up to girl sniffing the note (same set-up, so it reads as a small jump cut, acceptable). 3.633 to dad in the doorway, under "Then her dad walks out" (3.24-4.5), which is a better match than pass 1. 5.10 doorway to dad walking (similar framing, fine). 6.57 to the long two-shot, ONE piece to the end. The 75.0/75.2 jump is gone.
- Nit (not blocking): frame 3.600 (n108), the last frame before dad, is one brighter, slightly different exposure of the girl (a source flicker at about 66.65). It's barely visible. If visuals touch it again, end segment 2 at 66.6.
- Freeze: footage is 14.65 s for T = 14.76, so about 0.1 s, invisible. The ending is now dad holding the note, still moving.
- Subscribe appears at 9.6 under the 1-line "he clocked it" card, red to about 11.5, then SUBSCRIBED + bell, gone by about 14.6. It sits below the "example" tag and covers no text. "Gen Z slang" is fully visible 5.1-9.6.
- Hook-text orphan ("...love / note") unchanged; cosmetic, language-gated, accepted.
- Policy: the new footage (64.75-66.7, the girl smelling the note) is clean. No blackface anywhere in 60.85-77.15. No POLICY hit. Transcript unchanged, no spelled-out word.
- Loop: dad with the note goes back to the girl reading the note. Clean, and it fits the story.
