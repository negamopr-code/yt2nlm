# Viewer-critic review: pd4-get-well-soon-v1 (lab H87, trend-riding, old-movie situation)
Reviewed 2026-10-23. `state/shorts/pd4-get-well-soon-v1/final.mp4`: 1440x2560, 30 fps, 13.70 s. Clip: The Battle of the Century (1927), segments [571.15,581.45] [571.15,572.4]. final.subscribe.json subscribe_at [8.6].

## Verdict: SOLVES. Ship. In 13 s the viewer gets three ready phrases, each with a register tag, so I know which one to use and where.
## Pain
There are no learner-corpus quotes for this phrase (I grepped the monitor archives and insights: no hit). The evidence is Google Trends 2026-10-23, "other ways to say get well soon" +70 % rising. I made no NotebookLM query.
In my words: "I always write 'get well soon' and it feels flat." Solved means that tomorrow I can write a sick or hurt friend or colleague something else that fits.

## Heard (faster-whisper small.en, word timings)
0.00 Your friend just slipped on a banana peel, don't just say get well soon. / 4.84 Try feel better soon. / 6.72 Hope you're back on your feet soon. / 8.94 Wishing you a speedy recovery. / 11.52 What would you say to your friend? (ends 12.9). No spelled-out word.

## Second by second
- 0.00 Frame 0: "POV: your friend just slipped on a banana peel" (yellow, 2 lines, readable) over the peel on the pavement. The promise "3 ways to say 'get well soon'" is grey, but readable. It stops the scroll: it is my problem plus a gag.
- 0.0-1.33 The peel is still. The voice says "slipped" at 0.72, but the slip only comes at about 1.6-3.0 (the pie man falls). The voice is about 1 s ahead of the picture. Minor.
- 1.33-6.17 Wide shot: the slip, pies fly, Laurel and Hardy look on. "feel better soon / everyday" comes in at about 4.8. It fits.
- 6.17-10.33 Close-up of the pie man sitting among the pies, checking his hand. "back on your feet = healthy and active again / warm", then "speedy recovery / formal". The picture fits (a hurt man on the ground).
- 10.33-13.70 Cut back to the peel, slowed (1.25 s of source stretched to about 3.3 s; grain holds every 6 frames) under "What would you say to your friend?". It is static, but it is the loop: the last frame is the peel and frame 0 is the peel, so the loop is seamless.
- Subscribe: it fades in at 8.6, is red at about 8.8-10.5, then SUBSCRIBED + bell until about 13.6. It sits under the tag ("warm", then "formal") and covers no text. The history line "feel better soon · hope you're back on your feet soon" fits the width.
- Cuts: 1.33, 6.17 and 10.33 are all clean. No stray frames, no flash. No watermark, no intertitle.

## Takeaway test
Tomorrow I text "Hope you're back on your feet soon" to a friend, or write "Wishing you a speedy recovery" to a colleague. Yes. The last line is a soft self-test (comment prompt).

## Retention and trust risks (not blocking)
- The peel is static at 0-1.33 and at 10.33-13.7, which is about 4.6 s of a still peel per loop. That is acceptable because it makes the loop.
- The lower third of the screen is empty black (a format-wide trait).
- Logic nit: after a slip you would first say "Are you OK?". "Get well soon" works for a later message. The language editor accepted it; no change needed.

## HARD RULE
Clean: slapstick fall, no injury shown, 1927 public-domain film. No POLICY hit.

## Must-do before hand-over (not a picture fix)
- shorts-builder/publisher: no `content/youtube/pd4-get-well-soon-v1.json` exists. Create it with `"subscribe_at": [8.6]`. Under the rule, the video is not finished without it.
