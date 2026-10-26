# Viewer-critic review: h107-very-sick-v1 (lab H107: micro-story inside "Stop Saying Very X")

Reviewed 2026-10-26. File: state/shorts/h107-very-sick-v1/final-ln.mp4 (1440x2560, 30 fps, 20.3 s, Kokoro am_michael 1.05x, no music).
Unit: shorts/units/h107-very-sick-v1.json. Meta: content/youtube/h107-very-sick-v1.json. Subscribe: final-sub.subscribe.json = {"subscribe_at": [15.0], "seconds": 5.0, "corner": "bl"}.
Frames checked: 0.0, 0.7, 1.4, 2.5, 4, 5.5, 7, 8.5, 10, 11.5, 13, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5 s, plus 1440-wide crops at 5.5/10/13/15.5 s.
Not judged as defects (they are the test): story lines on cards, loop back to frame 0, no music.

## Verdict: PARTLY
I get three usable phrases and a story I can follow by ear, but the last beat pairs "Seriously ill" with "A week later, he's back at school!" over a picture of abstract cells, the subscribe pill covers the example sentence while it is spoken, and every picture carries a visible blur patch (plus a non-zooming magnifier in the bed picture).

## Ship blockers
1. Subscribe pill covers the example line (15.0-16.3 s). At 15.5 s the screen reads "SUBSCRIBE [bell] s..ously ill." - the red pill and bell sit on top of "He was seriously ill.", exactly while the voice says it (15.20-16.32). The one sentence that shows the word in use is unreadable. Owner: shorts-builder (start the animation at the end card, ~16.9 s, or move the corner/raise it off the sub line; then update meta "subscribe_at").
2. Meta "subscribe_at": [15.5] does not match the render (15.0 in final-sub.subscribe.json). The :8093 card shows a wrong time. Owner: shorts-builder.
3. "Seriously ill" beat teaches the wrong thing (judgement blocker). Card line "A week later, he's back at school!" = recovery; picture = abstract cells/veins/a dark cluster that reads as a tumour/microscope slide, no Leo. A B1 viewer hears "Seriously ill" while seeing "back at school!" and a science diagram: the meaning is carried only by the 1 s recap line (which is covered, blocker 1). The cell cluster also looks like cancer imagery - not a policy hit, but a heavy picture for a light story. Owner: scenario-writer (put the illness on this beat, e.g. "The doctor sends him to hospital." / "He's seriously ill."; recovery can go on the end line), visuals (Leo in a hospital bed / with a doctor, same character style).
4. Magnifying glass that does not zoom (bed picture, 7.9-11.5 s): a magnifier icon sits over Leo's face/pillow and enlarges nothing. User rule 2026-10-05 = defect, back to visuals.
5. Blur/smudge patches in all three pictures (masked NotebookLM embedded text): a grey pixel block left of Leo's arm (Feverish), a big grey block on the blanket (Bedridden), a pale block mid-left (Seriously ill). They look like censored areas/broken images. Owner: visuals (regenerate or crop clean; pictures.json shows embedded text "? He feels feverish 50%", "A complete loss of mobility...", "A grave, encompassing state...").

Clean, checked: no word spelled letter by letter (whisper heard Feverish 3.60, Bedridden 7.90, Seriously ill 12.62 whole); 1440 short side; no NotebookLM/Gemini watermark seen; official channel avatar logo top left; subscribe+bell animation present (15.0 s, second half, presses to SUBSCRIBED + bell by 16.5 s). POLICY: none (fictional Leo, illness described factually).

## Pain -> what the video gives -> gap
- Evidence: no NotebookLM query spent; content/problems/ has no file for this lane. Same corpus as H102 review (content/insights/audience-needs.md), verbatim: "great video but please shorten the intro!", "very helpful thanks :)", and viewers adding their own words under Stop Saying Shorts: "Frigid too", "Melancholic too", "There is also minuscule as in a minuscule mouse.". No learner quote about overusing "very sick" exists; the pain is the brief's.
- Pain (assumed, learner voice): "I always say 'very sick'; give me a word that says how sick."
- Solved = tomorrow I say "I feel feverish", "He was bedridden for days", "She was seriously ill" and know which level of sick each one is.
- Gives: three correct, natural words in natural sentences; feverish and bedridden are well illustrated by the story (hot and shaky; can't stand up).
- Gap: the ladder (a bit hot -> can't get up -> dangerous) is the real lesson and the last rung is broken (blocker 3). "Seriously ill" is still adverb + adjective - a viewer may ask "so 'seriously' is just another 'very'?"; nothing says it is the fixed phrase for dangerous illness. No self-test moment except "Comment yours!".

## Second by second
- 0.0-1.3 "Stop saying very sick." Card at frame 0, red strike drawn by 0.7 s. My phrase, I stop.
- 1.3-1.7 silence; 1.7-3.1 "Here are three better words." + "3 better words" sub. 3.6 s to the first word: acceptable.
- 3.6 "Feverish" - 4.3-5.8 "Leo wakes up hot and shaky." Picture: man in an armchair with red heat glow; says "wakes up" but he is in a chair, not bed - minor mismatch. Grey blur block on his arm.
- 6.2-7.3 "He feels feverish." Good, readable.
- 7.3-7.9 short gap. 7.9 "Bedridden" - "Soon he can't even stand up." Picture fits (man in bed) but magnifier icon over his face and a grey blur block on the blanket.
- 10.3-11.5 "He's bedridden for days." Good.
- 11.5-12.6 1.1 s silence - swipe risk (pattern known).
- 12.6-14.8 "Seriously ill, a week later he's back at school." Cells picture + recovery line: confusing, "huh?" moment (blocker 3).
- 15.0 subscribe pill slides in over the sub line; 15.2-16.3 "He was seriously ill." mostly covered (blocker 1).
- 16.9-18.1 "Which word will you use?" 18.5-19.1 "Comment yours!" End card is mostly empty black with the SUBSCRIBED pill; 19.1-20.3 silence then loop. ~3 s of no new content - swipe risk but harmless for loop.

## Takeaway test
"Tomorrow, instead of 'very sick', I say 'I feel feverish' (fever) or 'I was bedridden for two days' (couldn't get up)." Nameable for two words; the third is muddled by the beat. PARTLY.

## Retention risks
- 20.3 s vs 13-16 s target (same overrun as H102): 1.1 s holds after each example, 0.4 s hook gap, ~1.2 s dead tail.
- Picture styles consistent (watercolour) for beats 1-2, then beat 3 switches to a science diagram - breaks the story.
- Text legibility fine (big yellow headlines, white lines on dark pills) except where the subscribe pill covers the sub line.
- Voice natural, 1.05x Kokoro; "Seriously ill," and "a week later" run together with no pause, so the word does not land.

## Trust risks
- Story logic: "Seriously ill" + "back at school!" reads like the word means "got better".
- Blur blocks look like a broken/censored image.
- Meta subscribe_at wrong (15.5 vs 15.0).

## Top 3 fixes (by impact)
1. Move the subscribe animation off the example line (start ~16.9 s on the end card, or another corner above the subtitle) and write the real time into the meta. Owner: shorts-builder.
2. Rewrite beat 3 so the story line shows the danger ("The doctor sends him to hospital.") and make a matching picture of Leo (hospital bed/doctor), no cells. Owner: scenario-writer, then language-editor re-gate, then visuals.
3. Regenerate/clean all three pictures: no blur blocks, no non-zooming magnifier, Feverish shows him waking in bed. Owner: visuals.
