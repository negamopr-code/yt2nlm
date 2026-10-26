# Viewer-critic review: long-never-give-up-synonym-v1 (T02 "Never Give Up Synonyms: 20 Other Ways to Say It")

Date: 2026-10-18. Reviewer: glottos viewer-critic (step 7b). Read-only: no video, unit, meta or page was changed, nothing rendered or uploaded, no NotebookLM query spent.

Files judged
- `state/shorts/long-never-give-up-synonym-v1/final-sub.mp4` (2560x1440, 30 fps, 11:17.6, AAC 48 kHz mono)
- unit `shorts/units/long-never-give-up-synonym-v1.json` (53 beats, language-approved 2026-10-17, hash d754a4e5976b5524)
- `chapters.txt`, `thumbnail.jpg`, `final-sub.subscribe.json` (subscribe_at [70.0, 340.0]), `states.txt` (165 picture states, sum 677.5 s)
- `content/longvideo/T02-research.md`, `T02-script-v1.md` (coverage table + 12-point checklist), `T02-page-v1.md`

## Verdict: **SOLVES** the pain on content. **NOT READY TO SHIP**: 2 ship blockers + 1 send-back to visuals.

One sentence: a B1-B2 learner leaves knowing what to say to a friend instead of "never give up" (hang in there, keep at it, stick with it), how to fix "when I feel give up", and why "determined" and not "stubborn" goes in a job reference. All of that is spoken, shown and tested. It can't ship yet because the closing promise points at a video that doesn't exist, the publishing record has no subscribe times, and one picture says the opposite of its word.

### Ship blockers (ordered)
1. **Cliffhanger points at a video that doesn't exist yet (10:50-10:57).** The voice says "And next: other words for hopeful, plus one phrase that means you're hoping for the impossible. It's on your screen now." The T05 unit exists (`shorts/units/long-another-word-for-hopeful-v1.json`, and it does contain *wishful thinking* / *hope against hope*, so the promise can be kept), but there is no render (`state/shorts/long-another-word-for-hopeful-*` doesn't exist), so it can't be public or on an end screen. If this goes out first, "it's on your screen now" is false for every viewer. Fix: publish T05 first and put it as end-screen element 1, OR re-voice B53's last sentence as "And next: the video on your screen." (the script §5 already plans this fallback) and re-gate. Owner: scenario-writer (line) + voice + shorts-builder (splice), or the publisher (order).
2. **Subscribe times not recorded and not at chapter starts.** No `content/youtube/<meta>.json` exists for this video, so `"subscribe_at"` isn't recorded and the :8093 card can't show it. User rule: "a video without … the recorded time is not finished." Also, the long-video rule says the animation goes at chapter starts, but it plays at 70 s (in the middle of "You've got this", chapter start 0:30) and 340 s (in the middle of "Determined", chapter start 5:05). It covers no text (bottom-left, checked on frames), so this is a rule breach, not something viewers will notice. Fix: create the meta with `"subscribe_at": [70.0, 340.0]`, or better re-run `subscribe_anim.py` at chapter starts (e.g. 104.7 s "Speaking practice" and 305 s "More formal words"). Owner: shorts-builder.

### Send back to visuals (not a policy issue, but it hurts trust)
3. **"Persevere" (5:11-5:21) is a woman asleep on a pile of books.** To a learner that looks like giving up, the opposite of the word. This is the key word of part 3 and the picture contradicts it. Also weak or off pictures: *Hang in there* = flexed biceps (that means "strong"), *Keep at it* = a man breathing out swirls of wind (unreadable), *You've got this* = a handshake (that means "deal"), *Resolute* = a woman floating on a glowing pedestal. And **blurred rectangles left over from erasing something** are visible inside the pictures at *You've got this* (left edge, ~1:16), *Stick with it* (top, ~1:06) and *Keep at it* (top, ~0:57). Owner: visuals (`pic-never-give-up-friend-v1`, `pic-never-give-up-formal-v1`).

Checked and clean: **no spelled-out word** anywhere in the transcript; **no magnifying glass**; **no NotebookLM/Gemini watermark** seen; render at 1440 ✓.

## 1. The pain (learner's own words)
Source: `content/longvideo/T02-research.md` §4, comments counted from the raw files ([V] there). No names, nothing invented:
- "When I feel give up I take a deep breath…" (6 likes; 9 comments make this mistake)
- "Never give up learning English in my self" (14 likes)
- "I'm no resilient. I have to give up…" (5)
- "'congratulations, you're a good dancer' it really sounds sarcastic" (9)
- "the picture is suggestive of perseverance rather than resilience" (3)
- "I don't know how to answer when someone encourages me." (0)
- "I wish I had someone to give me a hug and talk me through…" (58)
- format complaints: "intro … takes so long", sentences "excessively long", "please speak a little fast"
- plus the search queries themselves: *other ways to say never give up*, *what's another word for never giving up*, *thesaurus never give up*.

**Pain in one sentence:** "I only know 'never give up', I make mistakes like 'when I feel give up', and I don't know which word is nice, which is formal, and which sounds rude or sarcastic."
**Solved means:** tomorrow I can say "Hang in there" or "Keep at it" to a friend, write "when I feel like giving up", write "determined" (not "stubborn") about someone, and answer "Thanks, I needed that" when someone encourages me.

## 2. What the video gives them → gap
| Pain | Delivered | Where | Gap |
|---|---|---|---|
| alternatives with register | 20 word cards, each with a meaning, a register label and an example, in 4 parts: friend → setback → formal → praise/insult | 0:30-9:01 | half of the 20 (determined, persistent, tenacious, resilient, dogged, resolute, relentless, stubborn, obstinate) are *describing* words, not things you say *to* someone. The video never shows how to use them as encouragement ("You're so determined, you'll get there"). The searcher who wants "something to say instead" really gets 10 phrases + 10 descriptors |
| "when I feel give up" | Wrong → Right card + rule (feel like + -ing), give up + -ing, give up on | 4:34-5:04 | it's a 17 s text-only card with no quiz on this exact mistake (the one with the most evidence). One "When I feel like ___" quiz would turn it into a habit |
| sounding sarcastic | quiz "Hang in there / Congratulations!" + "would sound sarcastic" | 1:18-1:33 | — |
| perseverance vs resilience | contrast card + persevered/preserved quiz + "I'm not/no resilient" quiz from a real comment | 6:13-6:52 | — |
| persevere pronunciation | "severe → persevere", stress, spelling per+severe | 5:22-5:36 | text-only card, 15 s |
| what to say back | "Thanks, I needed that. / That means a lot." | 10:15-10:22 | not practised (no "your turn") |
| emotional need | "Keep at it. I believe in you." | 10:23-10:34 | lands well, said slowly and warmly |
| praise or insult (thumbnail promise) | "Obstinate. And here's our insult." + joke + job-reference quiz | 8:25-9:00 | delivered at 8:26 of 11:17 (long wait, but it's said in the hook and again at 7:39, so the loop is held honestly). The card itself says "criticism", the voice says "insult" (see trust) |

## 3. Second by second (where a viewer swipes away)
- **0:00-0:01 hook.** Voice at 0.0 s: "Never give up synonyms." Title card + 6 small pictures. A searcher knows at once it's the right video ✓. For a browser it's a dark, static card, nothing moves.
- **0:00-0:30 risk #1.** Two static cards for 30 s: B1 (17.3 s, same frame the whole time) and B2 (13.2 s, text only: "Wherever you are right now"). "Maybe you're on a bus… kitchen table…" is warm but empty for a searcher who came for the list. Many will skip ahead or leave here. The script itself says "cut B2 first". Do it.
- 0:30-1:17 part 1: a new card every ~4 s, picture after the headline ✓.
- 1:18-1:43 two quizzes: voice and screen ask the same thing; 3-2-1 countdown; voice pause 3.2-3.9 s before the answer ✓ (enough for two options).
- 1:44-2:23 shadowing: "LISTEN" then "YOUR TURN: SAY IT", 3-4 s gaps for 5-7 word lines ✓ (answers the "sentences too long" complaint).
- **2:24-2:54 film story** (One Week 1920): the clips really play (frames differ; people walk in, a ladder moves; the storm clip opens with an iris). Picture matches voice ("Crooked", "Then a storm came and twisted the whole house") ✓. Credit on screen ✓. But the clip only fills ~30 % of the frame, in a box on black, so on a phone it's small. And **the story is never finished**: we never learn whether he gave up or soldiered on. The best-paying moment of the video ends without a payoff. A 5-10 s return at 4:03 ("He didn't throw in the towel: he picked himself up…") would close it.
- 2:54-4:33 part 2 + 2 quizzes + shadowing ✓. The boxer picture fits "throw in the towel" well.
- 4:34-5:04 mistakes: 17 s on one text card, then two short ones. Good content, flat picture.
- 5:05-7:31 part 3: persevere picture contradicts (blocker 3); the 15 s pronunciation card is text only.
- 7:32-9:33 part 4: strongest part. Stubborn = man too proud to read the map (fits). Obstinate = sulking child (fits). Joke "I'm determined. You're stubborn. He's obstinate." lands. A/B/C quiz with a 3.4 s pause, a bit short for 3 options, but OK.
- **9:34-11:17 risk #2.** 1 min 43 s of **text-only cards on black, no pictures at all**: skip-three (21.6 s on one card), rest don't quit, don't say it, what to say back, I believe in you, site link, CTA. Content is good (rest-don't-quit, "I'm here for you", what to say back), but this is where watch time bleeds. The "3 words to skip" card (21.6 s about words the viewer will never meet) is the weakest 20 s of the video.
- 10:42-11:17 CTA + cliffhanger, voice ends 10:57.4, then a 20.2 s hold for the end screen ✓ (only the music bed plays; whisper made up "Thanks for watching" in it, but no voice is there).

## 4. Takeaway test
One action: **next time a friend fails something, say "Hang in there" (not "never give up", never "congratulations"), and write "when I feel like giving up".** Clear, practised twice (quiz + say-it-with-me). Passes.

## 5. Quiz audit (voice = screen?)
| t | screen | voice | pause before answer |
|---|---|---|---|
| 1:18 | Hang in there. / Congratulations! | same | 3.9 s |
| 1:34 | Keep ___ it! at / with | "keep blank it. At or with?" | 3.2 s, **"blank it" runs together and sounds like "blanket"** (whisper heard "blanket" twice, also with the clip cut out alone). A B1 ear will hear the same word |
| 2:31 | throw in the ___ towel / hat | same | 3.7 s |
| 3:42 | ___ back bounce / jump | same | 3.7 s |
| 3:54 | soldier on / throw in the towel | same | 3.5 s |
| 6:24 | persevered / preserved | same | 3.8 s |
| 6:40 | not / no | same | 3.5 s |
| 8:48 | A stubborn / B determined / C obstinate | no letters spoken (screen has letters; fine) | 3.4 s |
All 8 ask the same question by voice and on screen, and each has exactly one right answer. The 3-option pause is the tightest.

## 6. Retention risks
- Length 11:17 vs research target 10-12 min ✓; 20 words + 8 quizzes + 4 drills justify it.
- Static stretches: 0:00-0:30 (2 cards), 4:34-4:51 (17 s), 5:22-5:37 (15 s), 9:34-11:17 (no pictures at all). Changes still come every ≤ 22 s, so the "20-40 s" rule passes on paper, but in the tail every change is a black text card.
- Repetition is deliberate (each word: card → example → quiz → say-it-with-me), good for B1 learners, and drills stay ≤ 8 words.
- Pace: voice speed 1.0, clear; no podcast chatter, no intro, no names.
- Legibility: headlines large; the definition lines (white bold ~26 px at 640 wide) read fine; the dark ghost words in the background are busy but don't block reading.
- Music bed: -23 to -26 dB in the pauses vs speech ~-16 dB mean. It fills the think pauses without fighting the voice.

## 7. Trust risks
- "**ONE IS AN INSULT**" (thumbnail) → delivered by voice at 8:26 ("And here's our insult"), but the obstinate card says "(formal, criticism)" and the page says "criticism, not praise". Saying obstinate is an *insult* stretches it a little (it's a negative word, often insulting when said to someone). Acceptable, but put "INSULT" on the obstinate card so the thumbnail promise is visibly paid off.
- Title "20 Other Ways to Say It" includes stubborn + obstinate, which the video itself says *not* to use as encouragement. That's slightly misleading but the video says so openly (the whole point of part 4). OK.
- Facts checked: boxing towel ✓, per+severe spelling and stress ✓, not/no rule ✓, preserve ✓, relentless both senses ✓, inexorable ✓, "nine comments" matches the research count ✓.
- Picture contradicts word: Persevere (asleep) ✗, see blocker 3.

## 8. POLICY (hard rule)
Clean. No sexual meaning, innuendo or body description; no profanity; nobody real is the topic (the 1920 film actor isn't named; the film is credited, public domain, no sound); no mockery of real people (the stubborn/obstinate joke is about "I/you/he"); nothing dangerous. Watch item, not a block: the "throw in the towel" boxer has light cuts on his face (sport illustration, no gore). The thumbnail's sulking child is a drawing, not a real person. Safe for a 13-year-old.

## 9. Addictive-learning ingredients
| ingredient | status |
|---|---|
| hook in second 1 | ✓ search phrase spoken at 0.0 s + open loop by 0:15 |
| change every 20-40 s | ✓ on paper; ✗ in feel for 0:00-0:30 and 9:34-11:17 |
| open loops closed | insult loop ✓ (8:26); towel loop ✓ (2:42→2:58); storm "part two is about this moment" ✓; **house story itself never closed** ✗ |
| self-test | ✓ 8 quizzes + 4 say-it-with-me drills |
| cliffhanger into the next video | written ✓, **broken until T05 is public** (blocker 1) |
| comment prompt | ✓ "What do you do when you feel like giving up? … use one phrase from this video" (it makes them practise in the comments) |

## 10. Top 3 fixes (by impact)
1. **Make the ending true and finished**: publish T05 first and set it as the end-screen video, or re-voice B53's last line to "And next: the video on your screen."; create the YouTube meta with `subscribe_at` and move the two subscribe animations to chapter starts (~104.7 s, ~305 s). Owner: scenario-writer + voice (line), shorts-builder (animation, meta), publisher (order).
2. **Fix the pictures that lie or look broken**: a new *Persevere* picture (someone still at the desk, late at night, NOT asleep: keeps going), clearer *Hang in there* / *Keep at it* / *You've got this* pictures, and remove the blurred erase rectangles. Then add pictures to the 1:43 text-only tail: the runner picture for "rest, don't quit", a friend-on-a-bench for "I'm here for you", and a One Week frame for the closing. Owner: visuals, then shorts-builder re-render.
3. **Tighten the dull ends and close the story**: cut B2 (−13 s), shorten "skip these three" to one sentence (−12 s), add a 5-10 s return to the One Week house after part 2 ("he picked himself up and…"), and make the Keep ___ it quiz say "Keep… what… it?" so it doesn't sound like "blanket". Owner: scenario-writer (re-gate with language-editor), voice, shorts-builder.

## What was checked / not checked
Checked: 169 frames (hook at 0.2/0.7/1.2/1.6 s + the midpoint of every one of the 165 picture states) on 15 contact sheets; 10 frames inside the two film-clip beats (motion confirmed); 2 full-size zooms for erase artifacts; thumbnail; full faster-whisper small.en transcript with word timings (cpu_threads=4) + 4 segments re-transcribed alone (Part 3 present; "We'll soldier on" OK; "blanket" confirmed; end hold = music only); volumedetect in pauses and the end hold; chapters vs heard times (all 15 match within 1 s); T05 unit content vs the cliffhanger promise.
Not checked: `gate_av.py` was not run (read-only role); the 20 source pictures themselves (only as rendered); YouTube end-screen setup (not uploaded); the live page (T02-page-v1.md read as a draft only, and it's consistent with the video).
