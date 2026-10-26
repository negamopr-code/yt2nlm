# Viewer-critic review: pd1-in-tears-v1 (public-domain situation test, 4 of 4)

Reviewed 2026-10-16. File `state/shorts/pd1-in-tears-v1/final.mp4`: 1440x2560, 30 fps, video 11.57 s / audio 11.72 s. Unit `shorts/units/pd1-in-tears-v1.json` (language hash ee62c38c536c84a4). Clip: Big Business (1929).

## Verdict: PARTLY - 1 blocker
The sob and bawl pictures are excellent (handkerchief sobbing, Stan open-mouthed bawling), but frame 0 shows a man with a wide grin under "When the movie has a sad ending" - at phone size he reads as laughing, so the hook contradicts itself in the one second that decides the swipe, and the loop lands on that grin again.

## Pain
Same evidence as the other pd1 reviews (no PROBLEM doc for this lane; no NotebookLM query spent):
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank."
- "great video but please shorten the intro!"
- "Melancholic too" (viewer adding a word under a Very Sad Short)

Pain in their words: "I say the same words all the time" - everyone is just "sad" or "crying".
Solved means: tomorrow I say "I was in tears at the end" or "the baby was bawling".

Gives: three correct words with meaning + tag, a clear intensity ladder (in tears -> sob -> bawl), recap row. Gap: no situation picture (nobody watches a movie); no self-test.

## What is heard (faster-whisper small.en)
0.00 The movie has a sad ending. / 2.32 They're not just sad, / 3.62 they're in tears. / 5.08 He's sobbing. / 6.54 Now everyone's bawling. / 8.44 Do you cry too when the movie has a sad ending? (ends ~11.1, 0.6 s silence to loop). All heard as written. No spelled-out words.

## Second by second
- 0.0 Frame 0: 2-line hook + Finlayson next to the cop with a big open-mouth grin. Expert target (text + moving clip) met technically, but the face says "funny", not "sad". BLOCKER.
- 0.0-3.6 Lower ~45 % of the screen empty until the first card.
- 3.6-5.03 "in tears / crying": Finlayson now holds a handkerchief - match OK. Voice says "They're" while one man cries.
- 5.03-6.42 "sob" (1.4 s): handkerchief to face, shoulders shaking - strong match.
- 6.42-11.6 "bawl": cut to Laurel and Hardy; Stan's open-mouth bawl at ~7.6 is a perfect match; Ollie at ~6.6 looks half-laughing. Subscribe + bell 6.3-11.3, covers nothing.
- 8.4 hook box becomes 1 line "Do you cry at movies?".

## Word-picture match
in tears: OK. sob: yes. bawl: yes (Stan). Hook situation: not shown, and the opening face reads as the opposite emotion.

## Loop
Audio: "...when the movie has a sad ending? / The movie has a sad ending." - echo, works. Picture: visible restart - from the crying cop + Finlayson with handkerchiefs back to the grinning Finlayson; word stack vanishes; hook 1 -> 2 lines.

## Takeaway test
"I was in tears at the end of the movie." Clear and usable tomorrow; the voice gives "They're in tears".

## Retention risks
Frame-0 grin; empty lower half 0-3.6 s; sob card 1.4 s (meaning "to cry loudly, with short breaths" is 6 words - tight).

## Trust risks
Laughing face under "sad ending" (above). "They're in tears" over one person. Tags OK per language editor.

## Blockers vs nice-to-haves
Blocker: grinning frame 0 under a sad hook.
Nice-to-have: start the clip on the handkerchief/sobbing moment; "He's in tears" instead of "They're"; hold sob >=1.8 s.

## Top 3 fixes
1. Move the clip in-point so frame 0 (and the loop seam) is Finlayson already crying into the handkerchief (visuals + shorts-builder).
2. Make the narration match the screen: "He's not just sad. He's in tears." (scenario-writer, then language-editor).
3. Hold the sob card longer by trimming the gap before "in tears" (shorts-builder).

---

## Second pass (re-render 16:46, language re-approved 16:36:40)
File now video 11.50 s, Big Business 1081-1093. Line 2 is "He's not just sad. He's in tears." Subscribe 6.2 s, recorded in `content/youtube/pd1-in-tears-v1.json`.

**Final verdict: SOLVES - no blocker.**

- Earlier blocker FIXED in substance. Frame 0 shows Finlayson holding the handkerchief and looking down at it, so the crying cue is there from the first frame. Zoomed frames: at 0.5 s he squints with a wide mouth, which can still read as a laugh for half a second. At 1.0 s it is an unmistakable open-mouth wail, and at 2.0-3.0 his face is in the handkerchief. That is enough for the hook. A later in-point would be cleaner.
- Narration now matches the screen: "He's in tears" (3.54-4.10) plays over Finlayson crying into the handkerchief. A cut to Laurel and Hardy at about 4.0 s shows Ollie smiling in the last 0.1 s of that line, which a viewer will not notice.
- Sob (4.96-5.18): Ollie wails, then puts the handkerchief to his face. Good. Bawl (6.44-7.26): the cop wails with his mouth wide open. Good. The crowd crying into handkerchiefs at 9.5 s supports "everyone's bawling".
- Transcript: 0.00 The movie has a sad ending. / 2.32 He's not just sad, he's in tears. / 4.96 He's sobbing. / 6.44 Now everyone's bawling. / 8.32 Do you cry too when the movie has a sad ending? The last line ends at 10.93, with 0.58 s of silence before the loop. No spelled-out words.
- Grey promise line "3 better ways to say 'crying'" shows from 0 to 3.5 s and is readable.
- Loop: the last frame has the cop smiling with an arm around Finlayson, then jumps back to Finlayson with the handkerchief. Same setting, small jump. The audio loop works.

Nice-to-haves: start about 0.7 s later so the 0.5 s squint-grin is gone. The sob card is still 1.4 s. The watching-a-movie situation is still never shown; the hook carries it.
