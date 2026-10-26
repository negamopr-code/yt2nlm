# Viewer-critic review: pd2-made-up-v1 (lab H85 batch 2, old-movie situation Short)

Reviewed 2026-10-17. File `state/shorts/pd2-made-up-v1/final.mp4`: 1440x2560, 30 fps, 10.40 s, AAC 48 kHz stereo, peak -1.4 dB, mean -18.0 dB. Unit `shorts/units/pd2-made-up-v1.json` (language hash 0c662b04315ef5f6). Clip: Big Business (1929), source 1092.1-1099.0 + 1099.5-1101.45 + 1101.6-1104.45. `final.subscribe.json` subscribe_at [5.3].

## Verdict: SOLVES - no blocker
The policeman pushes the two enemies into a handshake and everyone cries into their handkerchiefs. That is exactly "patched things up / buried the hatchet / made peace", and it is on screen under every word.

## Pain (learner's words)
I reused the batch-1 corpus evidence and spent no NotebookLM query:
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them?"
- "I can understand 100% of the video, but when I try to speak, my mind goes blank."
- "great video but please shorten the intro!"
- "You have use the wrong synonym for rude"

Pain: "I say the same words all the time". Every reconciliation is "we made up".
Solved means: tomorrow I say "we patched things up" or "they finally buried the hatchet".
What it gives: three correct expressions in natural past-tense sentences, with meanings and tags. Gap: no self-test. The fight itself is never shown; only the debris in the background hints at it.

## What is heard (faster-whisper small.en, word timings)
0.00 After a big fight, / 1.40 you didn't just make up, (ends 2.50) / 3.12 you patched things up, / 4.74 you buried the hatchet, / 6.48 you made peace, / 7.86 ever had a fight "in" like this. (ends 9.48, then 0.92 s of silence to the loop). Whisper heard "end" as "in" (8.66-8.92). The voice probably drops the final /d/ before "like". It is not a spelled-out word. Check it by ear; if "end" is really mumbled, re-voice that line only. Gaps are 0.6-0.7 s. No dead air.

## Second by second (cuts at 6.90 and 8.85, the segment joins; both are clean, with no flash frames, frames checked around each)
- 0.0 Frame 0: the yellow hook "POV: after a big fight". The policeman has his arms round the bald neighbour and Laurel, and both hold handkerchiefs. The figures are large, at medium distance. There is motion from the first frames (the cop pulls them together, and they shake hands by about 1.5 s). A good hook: three faces and a clear social situation.
- 0.0-3.0 Grey promise "3 better ways to say 'made up'". The handshake happens under "you didn't just make up".
- 3.0 "patched things up / fixed things after a fight / everyday" (spoken 3.24). Picture: the cop pushes their hands together and they shake. Match.
- 4.7 "buried the hatchet / agreed to forget an old fight / idiom" (spoken 4.92). Picture: still shaking hands, and the cop wipes his eyes. Match.
- 5.3 Subscribe + bell slides in at bottom-left (frames 5.5 and 6.0 checked). SUBSCRIBED by about 7, the bell rings by about 8.5. It covers no text.
- 6.4 "made peace / agreed to stop fighting / neutral" (spoken 6.60). At 6.90 it cuts to a wide shot: four men (Hardy has joined) all crying into handkerchiefs in front of the wrecked garden. Match, and the wreck finally hints at the "big fight".
- 7.8 The hook box swaps to "Ever had a fight end like this?" (2 lines).
- 8.85 Cut to Laurel, the neighbour and Hardy smiling. Laurel hands something over, a peace offering. A good closing image.
- 10.4 End. No frozen tail (no freeze found in the picture band).

## Loop
It ends on the three smiling men and loops to the cop's embrace. That reads as a replay. Audio: "...end like this? / After a big fight..." No echo.

## Takeaway test
"We had a big argument, but we patched things up." I can use it tomorrow.

## Checklist
- 1440x2560: yes. Text is the same as in batch 1 and readable. "buried the hatchet" is the longest headline and fits on one line.
- Subscribe + bell at 5.3 s (51%): yes, visible, and it covers nothing.
- No intertitle (the next source cut is at 1106.09, after the clip ends at 1104.45; no title card on screen). No watermark. The credit shows "Big Business (1929)" only.
- Meta: `content/youtube/pd2-made-up-v1.json` DOES NOT EXIST yet. `"subscribe_at": [5.3]` must be recorded there.

## Retention risks
- The promise card "3 better ways to say 'made up'" is ambiguous out of context. B1 learners know "made up" = invented ("a made-up story") and "make-up" = cosmetics. The hook "after a big fight" sits right above it and resolves the sense, so the risk is small, but the title and description must keep the fight context.
- The black band at the bottom (about 30%).

## Trust risks
- "patched things up / fixed things after a fight": the meaning is a bit vague. "Fixed a relationship after a fight" would be clearer. Minor (language-editor).
- The fight is never seen. The picture shows only the end of it, which the hook word "after" covers honestly.

## Top 3 fixes (none blocking)
1. Create `content/youtube/pd2-made-up-v1.json` with `"subscribe_at": [5.3]`, and keep the fight sense in the title and line 1 (for example "Another word for made up? After a big fight, you didn't just make up."). Keep "public domain" out of every field (publisher / shorts-builder).
2. Check by ear the word "end" at 8.66-8.92. If it really comes out as "in", re-voice beat 5 only, keeping the length (voice).
3. Optional: change the patched-things-up meaning to "fixed a relationship after a fight" (language-editor, then a re-render of the card only).
