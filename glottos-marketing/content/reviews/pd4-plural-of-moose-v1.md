# Viewer-critic review: pd4-plural-of-moose-v1 (lab H87, trend-riding, old-movie situation)
Reviewed 2026-10-23. `state/shorts/pd4-plural-of-moose-v1/final.mp4`: 1440x2560, 30 fps, 14.10 s. Clip: Two Tars (1928), segments [153.3,156.8] [162.2,166.8] [167.0,171.8]. final.subscribe.json subscribe_at [8.6].

## Verdict: SOLVES. Ship. The question in the hook ("meese?") gets its answer at 3.2 s ("one moose, two moose"), and the two real vowel-change plurals show why the joke works.
## Pain
There are no learner-corpus quotes (I grepped: no hit). The evidence is Google Trends 2026-10-17: "plural of moose joke" Breakout, and "plural of moose is meese". I made no NotebookLM query.
In my words: "Is it two meese? Two mooses?" Solved means I say and write "two moose" tomorrow and I get the joke when someone says "meese".

## Heard (faster-whisper small.en)
0.00 Your friend says, one moose, two meese. / 3.24 Sorry, it's one moose, two moose. Same word. / 6.16 But goose does change. One goose, two geese. / 9.24 And mouse, one mouse, two mice. / 11.64 So, who's going to tell your friend? (ends 13.3). Whisper hears "meese" clearly. No spelled-out word.

## Second by second
- 0.00 Frame 0 shows the two sailors in the car with "POV: your friend says 'one moose, two meese'". The promise "plural of moose: is it 'meese'?" fits the width with a small margin. It stops the scroll.
- 0-2.73 Laurel talks and Hardy drives. That fits "your friend says".
- 2.73 Jump cut at the same angle (segment join 156.8 to 162.2): the heads and Laurel's hat change position. It is noticeable but not a flash. 3.57 Hardy grimaces and leans in, which fits "Sorry, it's one moose, two moose" as a reaction.
- 6-11 Both argue/talk under goose/geese and mouse/mice. The history line "one moose → two moose · one goose → two geese" fits.
- 11.6-14.1 Both sailors under "So, who's going to tell your friend?". The last frame shows both in the car, and frame 0 shows the same framing, so the loop is near-seamless.
- Subscribe: it fades in at 8.6, is red at about 8.8-10.5, then SUBSCRIBED + bell. It sits under the "irregular" tag and covers nothing. The rest is motion throughout (only 4-frame film dupes at 13.0 and 13.7). No watermark, no intertitle.

## Facts
Correct: moose has the same singular and plural; "meese" is a joke form; goose/geese and mouse/mice are vowel-change irregular plurals. No overclaim.

## Takeaway test
I write "two moose" and I can explain the meese joke. Yes. The closing line is a comment prompt (soft self-test).

## Risks (not blocking)
- The jump cut at 2.73 is mild. Visuals could start segment 2 at a frame closer in pose, but it is not required.
- The lower third of the screen is empty (format-wide).

## HARD RULE
Clean. No POLICY hit.

## Must-do before hand-over
- shorts-builder/publisher: no `content/youtube/pd4-plural-of-moose-v1.json` exists. Create it with `"subscribe_at": [8.6]`.
