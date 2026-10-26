# Viewer-critic review: pd2-broke-v1 (lab H85, old-movie situation Short)

Reviewed 2026-10-17. `state/shorts/pd2-broke-v1/final.mp4`: 1440x2560, 30 fps, 12.20 s, AAC 48 kHz. Unit `shorts/units/pd2-broke-v1.json` (language hash 33bacae9867c563). Clip: Cops (1922), segments 157.2-161.9, 162.05-168.5 (11.17 s of footage for T = 12.19 s). `final.subscribe.json` subscribe_at [6.15].

## Verdict: PARTLY - 1 blocker (frozen tail), with a one-number fix; otherwise ready
This is the best of the pd2 batch so far. A man sits on the kerb next to his furniture piled on the pavement. He throws his hat up and wails. The picture tells "you can't pay rent" without words. Each card sits over him and his stuff, the expressions are right, and the tags are useful. The only defect is that the footage runs out about 1 s before the end and the last frame freezes.

## Pain (corpus quotes reused from the batch-1 evidence; no NotebookLM query)
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank."
- "great video but please shorten the intro!"
Pain: "I say the same words all the time", and it is always "broke".
Solved means: tomorrow I say "I'm a bit strapped for cash this month".
Gap: there is no self-test, and the closing "Ever been this broke?" invites a comment rather than a try-out.

## Heard (faster-whisper small.en)
0.00 You can't pay the rent and your stuff is out on the street, / 3.32 you're not just broke. / 5.14 You're hard up. / 6.64 You're strapped for cash. / 8.30 You don't have a penny to your name. / 10.36 Ever been this broke? (ends about 11.4). No spelled-out words, no intro.

## Second by second (source cuts 157.08 | 161.96 | 171.83)
- 0.0 Frame 0: the POV hook "POV: you can't pay rent" (1 line) over a close-up of the man in a bowler hat in front of a mattress and a barrel. He is calm and looking away. It is acceptable, but at 1.0-2.5 he throws his hat and yells, which is the stronger picture. Optional: start segment 1 at 158.3 if that frame reads well.
- 0.0-4.7 The close-up: hat thrown, wailing. Under "can't pay the rent... not just broke". Match.
- 4.7 Cut to the wide shot: the man sits on the kerb next to a big pile of furniture. No intertitle, no stray shot (the 161.9 to 162.05 join skips the 161.96 cut cleanly).
- 5.18-6.27 "hard up / have very little money / informal". He waves his hat and wails. Match.
- 6.57-7.98 "strapped for cash / short of money right now / everyday". He sits, head down, hat in hand. Match.
- 8.28-9.97 "not a penny to your name / have no money at all / idiom". A man in a straw hat walks in from the left past him. The seated man and his furniture stay in frame, so it still reads. Acceptable.
- 10.27 The hook box swaps to "Ever been this broke?".
- 11.25-12.19 BLOCKER: FROZEN for about 0.95 s (motion 0.0-1.0), with the walking man stuck in mid-stride. Cause: footage of 11.17 s for T = 12.19 s.

## Subscribe, cards, loop
- Subscribe + bell at 6.15 s, bottom left under the tag. It is red SUBSCRIBE at 6.5-7.5, SUBSCRIBED by 8, and the bell rings at about 9.5. It covers no text. 6.15/12.19 = 50%. OK.
- Cards: all readable. "not a penny to your name" is the widest and fits with a small margin. Nothing is clipped.
- Loop: wide shot to the close-up. With the freeze it is a stop-then-jump. After the fix, it is a clean cut. The audio loops cleanly.
- `content/youtube/pd2-broke-v1.json` does not exist yet, so subscribe_at is not recorded.
- Policy: clean. No intertitle, no watermark, no magnifying glass.

## Takeaway test
"Sorry, I'm a bit strapped for cash this month." I can name it, so the verdict is PARTLY only because of the freeze. Fix it and this is SOLVES-level for the format.

## Top 3 fixes
1. Unit `segments[1]`: change [162.05, 168.5] to [162.05, 169.6]. The shot runs unbroken to 171.83; at 169.2-169.8 the straw-hat man turns to face the seated man (checked). The footage then reaches about 12.25 s, at least T. Owner: visuals, then shorts-builder re-render + subscribe_anim.
2. Record subscribe_at in content/youtube/pd2-broke-v1.json after the re-render. Owner: shorts-builder / publisher.
3. Optional: frame 0 on the hat-throw (segments[0] start at about 158.3; check that the footage still covers T, or extend segments[1] further to about 170.7). Owner: visuals.

---
# Pass 2 (2026-10-17, re-render 23:16)
Segments: [158.3,161.9] [162.05,170.7], so 12.25 s of footage for T = 12.19. 1440x2560, 12.20 s.

## Verdict: SOLVES (for this format) - ship
The freeze is gone (the lowest motion is above 1.5 to the end). There is no intertitle; the only cut is at 3.6, the segment join. No blackface-like or unsafe frame. The transcript is identical to pass 1, and no word is spelled out.

## Picture under each card
- 0.0 Frame 0: the man in the bowler, hat in hand, face twisted, in front of his mattress and barrel, under "POV: you can't pay rent". This is stronger than pass 1's calm look-away.
- 0.0-3.6 He throws his hat up and wails. Match.
- 3.6 Cut to the wide shot: he sits on the kerb next to the pile of furniture on the pavement.
- 5.18-6.27 "hard up": he waves his hat and wails. Match.
- 6.57-7.98 "strapped for cash": he sits head down, and a straw-hat man stands behind. Match.
- 8.28-9.97 "not a penny to your name": the straw-hat man walks past him. The seated man and the furniture stay in frame. Acceptable.
- 10.27-12.19 "Ever been this broke?": the straw-hat man turns to him, and he waves his hat up at him. There is motion to the end.

## Subscribe, cards, loop, meta
- Subscribe + bell at 6.15 s: red at about 6.25-8.0, SUBSCRIBED by about 8.3, the bell lit about 9.5-10.5, and it fades by about 11. It covers no text.
- Cards are readable and none are clipped ("not a penny to your name" fits).
- Loop: from the wide shot back to the close-up, a clean cut. The audio loops cleanly.
- `content/youtube/pd2-broke-v1.json` has `"subscribe_at": [6.15]`. The metadata is clean. Nit: the description line for "Strapped for cash" has no "(everyday)" tag, unlike the card (owner: publisher, optional).

## Remaining nits (optional)
1. There is no self-test beat (format-wide; owner: scenario-writer).
