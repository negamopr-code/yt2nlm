# Viewer-critic review: h103-very-pretty-v1 (lab H103 arm a: "Did you know" hook in Stop Saying "very pretty")

Reviewed 2026-10-25 (the autopilot skipped the critic, "ran on arm 1"). File: /workspace/glottos-auto/out/h103-very-pretty-v1.mp4 (same md5 as state/shorts/h103-very-pretty-v1/final.mp4). It is 1440x2560, 30 fps, 22.7 s, Kokoro am_michael at 1.05, no music. Meta: content/youtube/h103-very-pretty-v1.json is there with "subscribe_at": [12.5].
Pain evidence: I spent no NotebookLM query, and there is still no learner quote about "very" on file (the same gap as h102/tasty). The pain is the brief's: "I always say 'very pretty'; give me better words." Solved means that tomorrow I can say "The sunset is gorgeous / It looks stunning / The flowers are lovely."

## Verdict: PARTLY
The hook stops me and the three words are correct and usable. But about 6.5 s is silence, the length is 22.7 s against a 13-16 s target, the screen shows the payoff line while the voice is telling the story line, and the "stunning" picture has no dress in it.

## Ship blockers
None hard. Checked:
- The subscribe animation is present (pill from about 12.2 s, "SUBSCRIBED" plus bell by 14-15 s, bottom-left) and its time is recorded. This was fixed after tasty.
- No word is spelled out: whisper heard "Gorgeous" 4.26, "Stunning" 9.48 and "Lovely" 13.94 as whole words. "Lovely" got a 0-length word timing, so check by ear that its onset is not clipped.
- The language is correct.
- POLICY: none. No watermark, no magnifying glass.
- Hook caveat: the hook as spoken, "Did you know there are better words than very pretty?", is a "better words" hook, NOT the "you're using this word wrong" mistake-fact hook the arm describes. It is the same as tasty, so the arm is consistent with itself but not with its stated variable. The lab entry should record the hook as it actually is.

## Second by second
- 0.0: frame 0 shows "Did you know there are better words than" but NOT "very pretty". The key words draw in at about 0.5 s, so frame 0 does not show my problem yet.
- 2.5-3.0: the red strike lands on "very pretty". The language editor approved it as normal English, so the strike says "wrong" about something that is fine.
- 3.7-4.3 and 4.7-5.3: gaps. Voice: "Mia watches the sunset." Screen: "The sunset is gorgeous." The story line is never shown, and the same mismatch happens at 10.1 and 14.4.
- 8.1-9.5 (1.4 s), 12.4-13.9 (1.5 s), 17.3-18.3 (1.0 s): silent holds. These are the swipe points.
- 9.5-10.8: "Stunning" plays with NO picture (headline only). The picture that follows has crying statue faces and a woman shading her eyes, and NO dress, while the voice says "she sees a dress". The picture does not match the words.
- 20.3-22.7: a 2.4 s silent tail. The loop card comes back already struck, so it does not match frame 0.

## Takeaway test
I can use "The sunset is gorgeous" tomorrow. Nothing asks me to try a word myself, and the nuance (gorgeous/stunning = strong, lovely = warm) is not given.

## Length vs the arm's test
Yes, the length hurts the test. About 6.5 s of silence plus the spoken story lines pushes it 7-9 s past the target. Retention for arm (a) will measure the length and the dead air as much as the hook. Both arms share this, so the result is confounded unless the control is the same length.

## Top 3 fixes
1. shorts-builder: cut the holds to 0.4 s and the tail to 0.5 s (about 16 s), show "very pretty" at frame 0, and make the loop card match frame 0.
2. scenario-writer/shorts-builder: show the story line on screen while it is spoken (or drop it), and make the spoken hook match the arm (a mistake-fact) or relabel the arm.
3. visuals: redraw "stunning" with a dress and get the picture on screen at 9.5 s.
