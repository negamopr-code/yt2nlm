# Viewer-critic review v1: h110-dont-say-im-tired-v1

Reviewed 2026-10-27. File: /workspace/glottos-marketing/state/shorts/h110-dont-say-im-tired-v1/final-ln.mp4 (1440x2560, 30 fps, 16.90 s, kokoro am_michael 1.2x, same voice as H102). Unit: shorts/units/h110-dont-say-im-tired-v1.json (language_approval present). Lab H110 (lane port of the H102 story build).
Pain evidence: there is no verbatim learner quote about "I'm tired" on file (no content/problems/ dir; nothing in pains.json or the articles). I did not spend a NotebookLM query, and I invented no quotes. The pain, in the brief's words: "I always say 'I'm tired' / 'very tired'; give me what people really say." Solved means that tomorrow, after work, I say "I'm beat" or "I'm wiped out" instead of "I'm tired".

## Verdict: PARTLY (the content is right; ship after 2 cheap fixes)
The three phrases are correct, natural and everyday, and the Leo story makes each meaning clear. All 3 pictures match their story lines, and they appear in sync with the voice. Two things cost stayed%, which is the lab metric. The video ends on 1.85 s of silence (15.05-16.90). And the very first frame shows only "Don't say" without "I'm tired". The magnifier in picture 3 also does not zoom (house rule).

## Ship blockers
1. Dead tail: 15.05-16.90 s is silent on the static "Comment yours!" card. That is 11% of the Short and the place where loopers swipe. H109 had a 0.35 s tail. Cut it to about 0.3 s, so the total is about 15.3 s. Owner: shorts-builder.
2. Magnifier rule (2026-10-05), picture 3 "Running on empty" (6.9-9.6 s): the lens shows a hunched man and a low battery. That is NOT an enlargement of the gauge under it, so the glass just sits on the picture. Re-pick or redraw so the lens enlarges the needle on "E", or drop the lens. Owner: visuals.

## Pictures vs the Leo story
- Pic 2 (3.6-6.0, "Leo walks home after work. I'm beat."): a tired man walks with a bag past a street lamp and a clock. MATCH. Defect: a blank white panel with a grey smudge and an orange bubble-tail on the left half. It looks like erased text (detext residue) and reads as a glitch. Owner: visuals (minor).
- Pic 3 (6.9-9.6, "He skipped lunch. He's running on empty."): a fuel gauge on E plus a magnifier. MATCH for the metaphor (no lunch or Leo shown, which is acceptable). Blocker 2 applies, and there is a small white smudge at the bottom-left of the lens.
- Pic 4 (10.4-12.9, "He falls asleep on the sofa. He's wiped out."): a man asleep on a sofa. MATCH, the clearest picture of the three.

## Second by second (faster-whisper small.en, word timings)
- 0.00 frame 0: "Don't say" only. "I'm tired" pops in at about 0.2 s. A weak first frame for the feed or preview: the phrase that is my problem is missing.
- 0.00-0.98 "Don't say I'm tired." The strike-through arrives at about 1.5 s. A strong, personal hook. 1.26-2.56 "Here are three better ways." No picture until 3.6 s, which is a mild swipe risk (same as the H102 build).
- 2.90 "I'm beat." 3.76 "Leo walks home after work." 5.16 "I'm beat." The picture lands at 3.6 s, in sync.
- 6.12 "Running on empty." 7.14 "He skipped lunch." 8.18 "He's running on empty." The picture lands at about 7.0 s.
- 8.8-13.8 subscribe and bell play, bottom-left. They start in the gap before "Wiped out" (9.64) and then sit over the bottom-left corner of the sofa picture for the whole 3rd beat. The caption is not covered (better than H109). Acceptable, but at about 13.0 s on the empty end card it would hide nothing.
- 9.64 "Wiped out." 10.36 "He falls asleep on the sofa." 12.04 "He's wiped out."
- 13.10 "Which one will you use?" 14.32 "Comment yours." Then 1.85 s of silence (blocker 1).
- Gaps between lines are 0.3-0.5 s, and the pacing is brisk. No spelled-out word. POLICY: clean.

## Takeaway test
"I'm beat." I can say it tomorrow after work, and the card shows the exact sentence. PASS. There is no try-it moment.

## Retention / trust risks
- The story lines ("Leo walks home after work", "He skipped lunch", "He falls asleep on the sofa") are spoken only, never shown. A B1 viewer who misses "skipped lunch" by ear loses the reason for "running on empty". Each card shows only the payoff line, and that line appears before the voice says it (for example 7.5 s).
- The busy background word-wall ("i'm beat / wiped out / running on...") competes with the cards. This is the template, cosmetic.
- Language and facts: correct. All three are informal but fine in everyday speech. No overclaim.
- Meta: content/youtube/h110-dont-say-im-tired-v1.json does not exist yet. "subscribe_at": [8.8] must be recorded (subscribe rule), or [~13.0] if it is moved.

## Top 3 fixes (by impact)
1. Trim the end silence from 1.85 s to about 0.3 s, and render frame 0 with the full hook "Don't say "I'm tired"" (no 0.2 s pop-in). Owner: shorts-builder.
2. Fix picture 3: a real zoom (the lens enlarges the E needle) or no lens. Clean the white-panel residue in picture 2. Owner: visuals.
3. Show each story line as a small line above the payoff, timed to the voice, and optionally move subscribe to about 13.0 s over the end card. Record subscribe_at in the meta. Owner: shorts-builder (the scenario-writer already has the "use" text in the unit).
