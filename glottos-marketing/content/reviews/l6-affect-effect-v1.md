# Viewer-critic review: l6-affect-effect-v1 (lab H40, "one decision" format)

Reviewed 2026-10-07. Video: `state/shorts/l6-affect-effect-v1/final.mp4` (25.97 s, 1440x2560, 30 fps). Unit: `shorts/units/l6-affect-effect-v1.json`. Read-only review: nothing rendered, changed or uploaded.

## Verdict: PARTLY

The rule is correct and readable, and I do get one self-test, but the thing that is supposed to make it stick (A = Action, E = End result) is never shown as letters, the second card strikes out the word I was just told is right, and the voice says the same sound for both words, so I leave knowing the rule I have already heard and forgotten before.

Ship blockers: **0** (all seven mandatory checks pass, four of them with defects noted below). It can go out as the H40 test, but it tests a weaker version of the idea than it could.

## Pain (learner's words) -> what the video gives -> gap

No PROBLEM NN document exists for this lab Short. Quotes are verbatim from the learner comment corpus (`reports/monitor-awf/archives/youtube-comments-vol*.md`, grep "affect and/or/vs effect"):

- "The difference between Affect and Effect gets me every time"
- "Effect vs Affect always gets me"
- "I took the quiz and I got 8 correct out of 10, affect and effect is still confusing to me"
- "I always used to mess affect and effect up so much!"
- "Can someone tell me what the differences between effect and affect are?"
- "do some example about affect and effect"
- "affect and effect are difficult"

Pain in one sentence: "I know there is a rule, I have seen it, and I still pick the wrong one every time I write."
Solved would mean: tomorrow, writing a sentence, I have a two-second trick that tells me which spelling to type, without thinking about grammar terms.

What the video gives: verb/noun rule ("usually the verb" / "usually the noun"), one example each with the same rain sentence, one memory line ("Affect is the action. Effect is the end result.").

Gap:
1. "every time" / "still confusing" is a memory problem, not an information problem. The memory line is the cure, and it sits as small white sub text for 4 s. The trick works by first letters (A-ffect = A-ction, E-ffect = E-nd), and nothing on screen marks the A or the E. I have to notice it myself.
2. Only one self-test (verb?). I am never asked to use it on a sentence ("Rain ___ my mood").
3. The voice cannot carry the difference at all (see check 7).

## Mandatory checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Resolution >= 1440 short side | PASS | ffmpeg probe: h264 1440x2560, 30 fps |
| 2 | Subscribe + bell visible in 21.0-26.0 s, not covering card text | PASS | Frames 21.6 s (red SUBSCRIBE + bell) and 23.5 s (grey SUBSCRIBED + bell, cursor). Button sits at about y 1910-2125 px, the card text ends at about y 1580 px. Recorded: `final.subscribe.json` and `content/youtube/l6-affect-effect-v1.json` both `subscribe_at [21.0]`. Note: the button's lower edge is about 35 px above the 400 px overlay zone, and the bell reaches x about 1300 px, close to the Shorts like/comment column. |
| 3 | Either/or on screen at once | PASS, with a defect | Frames 0-4 (0.00-0.13 s) show only the logo, the "CONFUSING WORDS" pill and the dim background words. "Affect or Effect?" is fully visible from frame 5 = 0.167 s (hard cut, no fade). Not noticeable while watching, but frame 0 is empty, the voice already says "Affect" over it, and a loop restart flashes an empty card. "Which one is the verb?" (the actual decision) only appears at about 1.8 s. |
| 4 | Countdown "2" and "1" visible, readable, no overlap | PASS, with a defect | "2" on screen about 3.4-4.27 s, "1" about 4.27-5.07 s, large yellow, below the question, not touching card text. Defect: both digits sit on top of the grey decorative background word "remember" (crop at 4.6 s), which makes the "1" look like it is inside a word. |
| 5 | Cards readable, nothing cut off, nothing under bottom 400 px, struck-out word readable | PASS | All five cards checked at 7.5, 12.5, 18.5, 23.5 s plus full-resolution crop at 7.5 s. Lowest card element (emoji panel) ends at about y 1820 px. Struck-out "effect"/"affect" is light grey with a red line, readable at full resolution, but at 7.5 s it lies on top of a drifting background logo tile. |
| 6 | Pictures help or confuse; no fake magnifying glass | PASS, weak | No magnifying glass anywhere. Rain cloud + sad face is the SAME picture on the Affect and the Effect card (`pictures.json`: both `1f327 1f614`): it illustrates the sentence, not the difference, so it adds nothing to the choice. Clapperboard + chequered flag on Remember does help ("action" / "end"), if I know a clapperboard means "Action!". |
| 7 | Audio: every word audible; affect vs effect; silences | PASS, with a defect | No spelled-out word. Every word of the unit is heard. But faster-whisper (small.en) hears "Effect" for every "affect": "Effect or effect." (0.0-0.9 s), "Effect. Usually the verb." (4.9-7.4 s), "Effect is the action. Effect is the end result." (17.3-19.9 s); same result on the per-beat files b01-0, b02-0, b04-1. Only "affects" (8.0 s) is heard correctly. With eyes off the screen the memory line is nonsense. The screen carries 100 % of the difference. Silences: see retention. |

## Transcript as heard (final.mp4)

0.00 "Effect or effect." | 1.76 "Which one is the verb?" | (silence 2.95-5.13) | 4.86 "Effect." | 6.58 "Usually the verb. Rain affects my mood." | 10.50 "Effect." | 11.54 "Usually the noun. Rain has an effect on my mood." | 15.40 "Remember." | 17.34 "Effect is the action. Effect is the end result." | 21.06 "Which word pair confuses you? Write it in the comments." | (silence 24.28-25.98)

## Second-by-second notes

- 0.00-0.17: empty card, voice already talking. Too short to swipe on, but it is not "from the first frame".
- 0.17-1.8: "Affect or Effect?" big and yellow. Yes, this is my problem. I stop.
- 1.8-2.9: "Which one is the verb?" Good, one clear question.
- 2.95-5.07: total silence for 2.2 s; the "2" only arrives at 3.4 s, so for half a second nothing happens at all. No tick, no sound. First swipe risk: it feels like the video froze. The countdown itself works once it shows.
- 5.07-6.47: "Affect" with small struck-out "effect". This is the payoff and it is clear. But for 1.4 s the card is just one word and the voice is silent for 0.85 s.
- 6.5-10.1: "usually the verb. Rain affects my mood." Clear, readable in time.
- 10.1-11.5: "Effect" with struck-out "affect". Here I get confused: you told me five seconds ago that "affect" was the right answer, now it is crossed out. Nobody asked "which one is the noun?", so the cross-out has no question to answer.
- 11.5-15.5: "usually the noun. Rain has an effect on my mood." Good pair of sentences; the same picture again tells me nothing new.
- 15.5-17.0: the word "Remember" alone for 1.5 s, voice silent for 0.95 s. Second swipe risk: I already have the answer and this looks like the outro.
- 17.0-21.0: "Affect is the action. Effect is the end result." The best line in the video, in the smallest text, and the voice says "effect ... effect".
- 21.0-26.0: closing question + subscribe. Fine. Last 1.7 s is silent.

## Takeaway test

Action I can name: "If the word is the action (the verb), write affect; if it is the thing/result (a, an, the before it), write effect." So an action exists, and the verdict is not DOESN'T. It is the same rule every other video gives; whether I still have it next week depends on the A/E trick, which the video says but does not show.

## Retention risks

- Length: 26.0 s against the 15-20 s written in H40's test. silencedetect (-35 dB) counts about 12 s of the 26 s as silence (46 %). The content is 20 s of material at most.
- Three "headline alone" holds (5.07-6.47, 10.13-11.47, 15.53-17.0) plus the 2.2 s silent countdown: four moments where nothing new arrives.
- Countdown promised as "2 seconds" runs about 1.67 s after a 0.5 s blank wait. Fine for thinking time, bad as silence.
- Pacing of the voice (1.05) is fine; legibility of card text is fine; picture/voice sync is fine (text appears with the words).
- Background: drifting words "affect / effect / remember" and logo tiles behind every card. In a video about telling two near-identical words apart, having both words floating everywhere behind the answer is noise, and it sits behind the countdown digits and the struck-out word.

## Trust risks

- Facts: correct. "usually" is the right hedge. Examples are natural English.
- The voice saying "effect is the action, effect is the end result" is how it lands for a listener. In real speech the two words are near-homophones, so this is honest English, but the video never says so. One line ("they sound almost the same, the spelling is the problem") would turn a weakness into a point.
- Cross-out on the Effect card contradicts the previous card for a moment (see 10.1 s).
- H40 comparability: the test said 15-20 s and "countdown in the first second"; the video is 26 s with the countdown at 3.4 s. Read the stayed % with that in mind.

## Top 3 fixes (by impact)

1. **Show the A and the E on the Remember card** (scenario-writer for the card text, shorts-builder for the colour): "**A**ffect = **A**ction. **E**ffect = **E**nd result." with the four first letters in yellow, at headline size instead of sub size. This is the whole memory trick and the only part the voice cannot deliver.
2. **Cut the dead time to land at 19-20 s** (shorts-builder): start the "2" as the question ends (about 2.9 s) and put a soft tick under each digit; shorten the headword-alone holds from about 1.4 s to about 0.6 s (`pause_after_word` 0.6 is turning into 0.85-0.95 s of real silence); trim the silent tail to 0.8 s; draw the hook text on frame 0.
3. **Make the Effect card answer a question, and make the pictures differ** (scenario-writer + visuals): either drop the struck-out "affect" on card 3 or label it ("the noun?"); give Affect an action picture (rain falling ON the face, an arrow) and Effect a result picture (the sad face alone), so the pictures show cause against result instead of the same pair twice. Optional second self-test before the CTA: "Rain ___ my mood." with a one-beat reveal.

Smaller: remove or strongly dim the background words behind the countdown and the struck-out word (shorts-builder).

## What was checked / not checked

Checked: ffmpeg probe; 130-frame contact sheet at 5 fps; first 9 frames one by one; 12 consecutive frames across the 2-to-1 change; frames at 0.05, 0.4, 1.0, 2.5, 3.6, 4.2, 4.6, 5.4, 7.5, 12.5, 18.5, 21.6, 23.5 s; full-resolution crops of the struck-out word, the countdown and the subscribe button; faster-whisper small.en word timings on final.mp4 and on all nine beat wavs; silencedetect; unit JSON; H40 in `/workspace/glottos-auto/out/lab/lab.json`; `content/youtube/l6-affect-effect-v1.json`.
Not checked: the video on a real phone inside the Shorts player (overlay positions are estimated from pixel coordinates); `final-nosub.mp4` (only confirmed it differs from final.mp4); human listening (the audio judgement rests on whisper output); no NotebookLM query used.
