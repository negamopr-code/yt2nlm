# Viewer-critic review: T02 "Never Give Up Synonyms: 20 Other Ways to Say It": A (slide builder, revised) vs B (NotebookLM Video Overview)

Date: 2026-10-18. Reviewer: glottos viewer-critic (step 7b). Read-only: nothing was rendered, changed, deleted or uploaded, and no NotebookLM query was used.

Files judged
- **A** `/workspace/glottos-auto/out/long-never-give-up-synonym-v1.mp4` (2560x1440, 30 fps, 11:15.0, mean -16.5 dB), meta `content/youtube/long-never-give-up-synonym-v1.json` (subscribe_at [94.0, 312.0], 15 chapters)
- **B** `/workspace/glottos-auto/out/long-never-give-up-synonym-nlm-v1.mp4` (2560x1440, 30 fps, 9:56.3, mean -15.1 dB; byte-identical to `state/shorts/long-never-give-up-synonym-v1/nlm-version-ln.mp4`; built from `nlm-overview.mp4` 8:56.6 slowed to 0.9x, clips at 138 s and 182 s of the source), meta `content/youtube/long-never-give-up-synonym-nlm-v1.json` (subscribe_at [], no chapters)
- Script `content/longvideo/T02-script-v1.md` (revised 10-18), research `content/longvideo/T02-research.md`, earlier review `content/reviews/long-never-give-up-synonym-v1.md`

## Verdicts
- **A: SOLVES. Shippable.** Every earlier ship blocker is fixed, all 7 script fixes are in the audio, and the picture send-back is done. One retention weakness is left: the last 1:30 is text cards on black. That doesn't block shipping.
- **B: PARTLY. NOT shippable.** It covers all 20 words with a warmer voice and nicer slides, but it isn't practice. There is **no pause longer than 2.5 s anywhere in 9:56**, so no think time and no "your turn" time. Two quiz pictures show the answer before it is asked. It ends on a **"Gemini Notebook" brand card**. It has no subscribe animation, no chapters, no site link and no comment prompt.
- **Recommendation: publish A.** Keep B unsent and use it as a source of ideas (see the end).

### Ship blockers in B (ordered)
1. **POLICY/brand: "Gemini Notebook" end card visible, 9:52-9:56** (frames at 592 s, 595 s: logo + "Gemini Notebook" across the middle of the screen). House rule: never ship a NotebookLM/Gemini watermark. The corner logo cover doesn't help, because the card is full screen. Fix: cut the source's last ~4.5 s (shorts-builder).
2. **No practice possible.** Whisper word timings show 0 gaps > 2.5 s in B (A has 28 gaps, 104.5 s in total). "Now try saying a few of these out loud with me" (1:38) is followed by the lines read back to back with 0.6-1.2 s gaps. The quiz answers come 0.9-1.9 s after the question (A: 3.0-3.9 s). Mean pace 157 wpm even at 0.9x (A: 122 wpm including pauses). A learner can't answer or repeat anything. Fix: you'd have to insert silences by re-cutting the NLM audio. That is doable but means rebuilding the video (shorts-builder).
3. **Quiz pictures show the answer.** At 1:59-2:12 the "Third test failed? ___" slide shows a girl holding a sign that says **HANG IN THERE**. At 6:24-6:36 the "I'm ___ resilient" slide has **"✗NO ✓NOT"** printed at the top. The options are never shown on screen, only spoken. Fix: needs new NLM slides (visuals). We can't fix that inside NotebookLM.
4. **Unfinished per house rules:** no subscribe animation (`subscribe_at: []`), no chapters, and no end-screen hold (the voice stops at 9:52, then the Gemini card, then the end). Owner: shorts-builder.
5. **Magnifying glass that doesn't zoom** (Obstinate slide, 7:36-7:58): the lens holds an unrelated path landscape and doesn't enlarge anything. User rule 10-05: send back to visuals.

A has no ship blockers. Checked: no spelled-out word in either transcript, no magnifying glass in A, no NLM/Gemini mark in A, both at 1440.

## 1. The pain (learner's own words, from `T02-research.md` §4, recounted from raw comments; no names)
- "When I feel give up I take a deep breath…" (6 likes; 9 comments make this mistake)
- "Never give up learning English in my self" (14)
- "I'm no resilient. I have to give up…" (5)
- "'congratulations, you're a good dancer' it really sounds sarcastic" (9)
- "the picture is suggestive of perseverance rather than resilience" (3)
- "I don't know how to answer when someone encourages me." (0)
- "I wish I had someone to give me a hug and talk me through…" (58)
- format: repeat sentences "excessively long" (3), "intro … takes so long" (0), "please speak a little fast" (3)

**Pain in one sentence:** "I only know 'never give up', I write 'when I feel give up', and I don't know which word is kind, which is formal, and which sounds rude or sarcastic."
**Solved means:** tomorrow I say "Hang in there" or "Keep at it" to a friend, write "when I feel like giving up", put "determined" (not "stubborn") in a reference, and answer "Thanks, I needed that."

## 2. A: re-check of every earlier finding
| earlier finding | now in A | status |
|---|---|---|
| Blocker 1: cliffhanger to the unreleased T05 | 10:51-10:55 "And next, the video on your screen." Card: "Next: the video on your screen". 20 s hold to 11:15 | FIXED, true whatever video is there |
| Blocker 2: no meta, no subscribe_at, not at chapter starts | meta exists, `subscribe_at [94.0, 312.0]`. 94 s = chapter "1:33 Speaking practice" ✓ (seen in frame: SUBSCRIBED + bell over "Say it with me"). 312 s is 10 s after chapter "5:02 More formal words", over the Persevere card | FIXED. The 2nd one is 10 s late but covers no text |
| Send-back: persevere = woman asleep | woman awake at her desk with a pen and books, determined face | FIXED, matches the word |
| hang in there = biceps; keep at it = wind; you've got this = handshake; resolute = floating woman | kitten clinging to a branch; boy with a plaster on his knee back on his skateboard; friend with a hand on the shoulder + thumbs-up at a door; man in a sou'wester standing firm in a storm | FIXED, all four read at a glance |
| blurred erase rectangles (0:57, 1:06, 1:16) | zoomed the new keep at it / stick with it (jigsaw) / you've got this pictures: none | FIXED |
| B2 13 s empty card | gone; Part 1 starts at 0:17.5 ("…who wants to quit, or to yourself") | FIXED |
| "Keep blank it" heard as "blanket" | 1:22 "Which is right: keep at it, or keep with it?" | FIXED |
| house story never closed | 4:22-4:30 "Back to our house… they get up off the ground. That's what pick yourself up means." The clip really shows the two crawling out from under the twisted house and standing up | FIXED, best payoff in the video |
| describing words never turned into encouragement | 7:30-7:41 "You're so determined. You'll get there. … You've been so resilient this year. I'm proud of you." | FIXED (text-only card) |
| obstinate card said "criticism" vs thumbnail "insult" | card: "(an insult if you say it about someone)"; voice: "And here's our insult" | FIXED |
| skip-three 21.6 s | 9:45-9:57, 11.6 s | FIXED |
| tail 9:34-11:17 without pictures | still text cards on black, 9:45-11:15 (≈ 70 s of voice + 20 s hold) | **NOT FIXED** (retention, not a blocker) |

Whisper's full pass printed "You tell him don't think he's ready to quit" at 2:22. Re-transcribing 139.5-147.5 s alone gives the correct "You tell him don't throw in the blank, towel or hat". That was a transcriber error; the audio is clean.

## 3. B: what the learner gets
Voice: one natural NotebookLM narrator, warm, with good signposting ("First up… Next is… And finally…"). Clearly more human than Kokoro. But it paraphrases the approved script up a level: "elevate your vocabulary", "high-stakes environments", "vastly different connotations", "a little linguistic joke that brilliantly illustrates this", "incredibly harsh criticism in a professional context", "exceptionally rare", "like canning food". Those are C1 words in a B1-B2 video. It also skipped the language gate: the approved wording was not what got voiced.

Coverage vs the approved script:
| in the script | B |
|---|---|
| 20 words, meaning + example | ✓ all 20 |
| hook phrase at 0:00 + insult loop | ✓ "Looking for never-give-up synonyms…" at 0.0; insult paid at 7:36 |
| 8 quizzes with think time | 7 asked, all answered in 0.9-1.9 s, 2 shown in the picture first, options never on screen |
| 4 say-it-with-me blocks (20 lines) | 3 blocks, 8 lines, no pauses; Part 4 practice missing |
| house story + payoff | ✓ told as "Imagine someone built their own house…" + clips at 2:32-2:40 and 3:24-3:28, "you stand up off the ground anyway" (3:21) tied to pick yourself up. Nice |
| feel like + -ing / give up + -ing / give up on | ✓ 4:06-4:42 ("Many people write…"; the "nine comments" evidence is dropped) |
| persevere pronunciation | partly: "severe hiding right inside it", stress on the last syllable; no "say it with me", no noun, the spelling rule isn't said |
| persevere vs resilient, not/no | ✓ |
| **describing word → encouragement ("You're so determined…")** | **MISSING** |
| skip three | ✓ but 23 s (5:15-5:38), the length A was told to cut |
| rest don't quit / I'm here for you / what to say back / I believe in you | ✓ |
| site link + "tell us in the comments" + cliffhanger | **all MISSING**: it asks the question, then says "Try to use at least one phrase from these slides in your daily life this week" ("these slides" = NotebookLM wording) |

Pictures: one illustrated slide per section, colourful and consistent (anime/watercolour). But each one stays on screen while several words are explained: "Everyday English" bullet slide **0:44-1:52 (~68 s, one frame)**, "After a setback" bullets **2:32-3:48 (~76 s**, broken only by the two clip insets), "Formal words" office **4:48-5:52 (~64 s)**, "Praise or criticism" bullets **6:48-7:32 (~48 s)**. In B, a word never gets its own picture. A gives each word its own picture plus a card with the meaning and example.
Wrong/Right slide (4:08-4:40): angry girl at a shape sorter vs happy girl at a map puzzle, labelled. Clear.
Logo: the official channel avatar (kid with book) bottom-right ✓, but a beige cover patch sticks out to its left all video long (cosmetic).

## 4. Second by second (where a viewer leaves)
**A**
- 0:00-0:17: phrase spoken at 0.0 s, static title card with 6 pictures. A searcher stays; a browser sees one frame for 17 s.
- 0:17-1:22: new picture every ~4-9 s; the new pictures make part 1 the strongest it has been.
- 1:05-1:30: two quizzes, 3.0-3.9 s pauses ✓. 1:33-2:10 shadowing ✓.
- 2:13-2:43 and 4:22-4:30: One Week clips play and match the voice ✓ (small box on black, as before).
- 4:32-4:49: 17 s text-only Wrong/Right card; 5:20-5:35: 15 s text-only pronunciation card. Flat but short.
- 7:30-7:41: new "Say it to someone" card, text only.
- **9:45-11:15: exit zone.** Skip-three, rest don't quit, don't say it, what to say back, I believe in you, site, CTA: 7 cards on black, then 20 s hold. The content is the warmest in the video, but the screen looks finished, so viewers leave.

**B**
- 0:00-0:22: good spoken hook, attractive title slide.
- **0:22-0:37: "Here is exactly how we've organized these words"**, a 15 s agenda (the "intro takes so long" complaint).
- **0:44-1:52: one slide for 68 s** while 5 phrases + practice are read. First big drop risk.
- 1:52-2:28: quizzes answered before a viewer can think; the picture already says HANG IN THERE.
- **2:32-3:48: one slide for 76 s.** Second big drop.
- 4:48-5:52: office slide for 64 s while persevere and its pronunciation go by.
- 6:48-7:32: bullet slide for 48 s.
- 9:22-9:52: ends warmly with "Keep at it. I believe in you", then **the Gemini Notebook card**, then the video ends. No end screen space.

## 5. Takeaway test
- A: **"Next time a friend fails, say 'Hang in there' (not 'congratulations'), and write 'when I feel like giving up'."** Taught, quizzed with think time, and repeated aloud. Passes.
- B: the same sentence is *heard*, but never practised (no pause to answer or repeat). The viewer leaves with a list they heard once. It only partly passes, so B is PARTLY at best.

## 6. Retention risks
- A: 11:15 for 20 words + 8 quizzes + 4 drills is justified. Static stretches: 0:00-0:17, 4:32-4:49, 5:20-5:35, 9:45-11:15. Kokoro voice at 1.0 is clear but flat next to B.
- B: 9:56 sounds shorter, but it's denser (157 wpm, no gaps). The long statics (68/76/64/48 s) break the 20-40 s change rule. The 0.9x slow-down didn't make it easier to follow, because there are still no pauses.

## 7. Trust risks
- A: no wrong facts found; picture = word everywhere now. The title "20 Other Ways to Say It" includes stubborn/obstinate, but the video says so openly (unchanged, acceptable).
- B: overclaims: "Persevere… This is a very formal word"; "stubborn or obstinate would be incredibly harsh criticism" (stubborn is usually mild criticism); "After the phrase feel like, you must use an ING verb" (also "feel like a coffee"; the script has the same simplification). Unnatural/over-level wording (list in §3). Answer-revealing quiz pictures make the quizzes feel fake. The "Gemini Notebook" card tells the viewer it is AI-made by someone else's brand.

## 8. POLICY (hard rule)
- A: clean. Nothing sexual or suggestive, no profanity, no real person as the topic (1920 film credited, actor not named), no mockery (the joke is I/you/he), nothing dangerous. Safe for 13-year-olds.
- B: the content is clean. **Brand/watermark blocker** (Gemini Notebook end card, see blocker 1). Watch item, not a block: the "Support: I'm here for you" picture (9:12-9:32) shows two teenage boys forehead to forehead holding glowing hands. It's not sexual, but it's more intimate than "support" needs. Swap it if B is ever reworked.

## 9. Addictive-learning ingredients
| ingredient | A | B |
|---|---|---|
| hook in second 1 | ✓ phrase at 0.0 s + insult loop | ✓ phrase at 0.0 s + insult loop |
| change every 20-40 s | ✓ except the 9:45-11:15 tail | ✗ 4 slides of 48-76 s |
| open loops closed | ✓ insult, towel, house (now closed with a clip) | ✓ insult; house is narrated, not a cliffhanger |
| self-test | ✓ 8 quizzes, 3-4 s think time, options on screen | ✗ 1-2 s, answers in the pictures, options not shown |
| say-it-aloud | ✓ 4 blocks, 20 lines, LISTEN / YOUR TURN | ✗ 3 blocks, 8 lines, no gaps |
| comment prompt | ✓ "Tell us in the comments, and use one phrase" | ✗ question asked, no prompt to comment |
| cliffhanger + end screen | ✓ "the video on your screen" + 20 s hold | ✗ none, Gemini card |
| subscribe animation | ✓ 1:34, 5:12 | ✗ none |

## 10. COMPARISON A vs B
| | A: slide builder (revised) | B: NotebookLM Video Overview | better |
|---|---|---|---|
| Hook (0-15 s) | "Never give up synonyms." at 0.0, insult loop by 0:15; static dark card | "Looking for never-give-up synonyms…" at 0.0, loop by 0:21; bright slide; then a 15 s agenda | tie (A gets to content faster: 0:17 vs 0:37) |
| Clarity for B1-B2 | approved, gated wording, short lines ≤ 8 words, meaning + register + example on every card | paraphrased to C1 ("connotations", "high-stakes", "elevate"), meanings only spoken, bullets only | **A** |
| Voice naturalness | Kokoro: clear, even, a bit robotic | natural, warm, good transitions | **B** |
| Pictures | one picture per word, all 20 now match their word; 2 real film clips; tail is text on black | cohesive illustrated slides, but one per section (48-76 s static); 2 answer-revealing quiz pictures; non-zooming magnifier; Gemini end card | **A** on teaching, B on looks |
| Pace / length | 11:15, 122 wpm with real pauses | 9:56, 157 wpm, zero pauses > 2.5 s | **A** (B is shorter only because the practice was dropped) |
| Quizzes / practice | 8 quizzes (3.0-3.9 s think time) + 4 drills (20 lines) | 7 quizzes answered in 0.9-1.9 s, 3 drills with no repeat gaps | **A**, clearly |
| Coverage: 20 phrases | 20/20 | 20/20 | tie |
| Coverage: viewer questions G1-G8 + critic gaps | all, incl. "say it to someone", "nine comments", site link, comment prompt | G1-G6, G8 ✓; "say it to someone" ✗, comment prompt ✗, site link ✗ | **A** |
| Retention risk | tail 9:45-11:15 | 0:22-0:37 agenda, 0:44-1:52, 2:32-3:48, 4:48-5:52 statics; abrupt end | **A** (lower) |
| House rules | 1440 ✓, logo ✓, subscribe ✓ recorded ✓, chapters ✓, end hold ✓, language gate ✓ | 1440 ✓, logo ✓; watermark ✗, subscribe ✗, chapters ✗, end hold ✗, gate ✗ (paraphrased) | **A** |
| Production cost / effort | high: unit, 4 picture sets + 3 redo rounds, Kokoro, build_long, critic loops (2 days) | low: one NLM generation + speed/overlay pass (~1 h), but almost nothing can be fixed: the wording, pauses and slides belong to NotebookLM | **B** on cost, A on control |

## 11. Recommendation
**Publish A.** It is the only version where the learner *does* something (answers, repeats, writes a comment), and that is the whole difference between watching and learning. A's last weakness (the text-only tail) costs watch time at the end, not learning. B would need at least: the Gemini card cut, silences cut in for every quiz and drill, new quiz slides, a subscribe pass, chapters and an end hold. That rebuild is bigger than A's remaining polish, and it still wouldn't bring back the gated wording.

### What B teaches us (to put into A-style production)
1. **Voice warmth and signposting.** "First up… Next is… And finally…", "All right, let's test this", "Let's see if you remember this one". Add 1-3-word transitions like these to our scripts. Test a more natural TTS voice for the long videos (voice agent). This is the one area where B clearly wins.
2. **Weave the story into the word.** "Imagine that storm wrecks your house, but you stand up off the ground anyway." It ties pick yourself up to the clip at the moment the word is taught, not in a separate beat (scenario-writer).
3. **Use illustrated scene slides instead of black text cards.** NotebookLM's section slides (runner drinking water for "rest, don't quit", Pressure vs Support split, Wrong/Right with two kids) are exactly what A's tail is missing (visuals: generate those scenes for A's B49-B54 the same way, without the answer-revealing text).

## 12. Top 3 fixes (by impact)
1. **A: put pictures into the 9:45-11:15 tail** (runner stops for water; two friends, one listening, for "I'm here for you"; someone smiling at a message for "Thanks, I needed that"; a One Week still for "I believe in you"), then re-render. Optional: move subscribe #2 to 302 s and update the meta. Owner: visuals, then shorts-builder. *Not required to ship; do it as v2 in place if A gets impressions but loses viewers at the end.*
2. **B: do not send.** If the route is tried again, the NLM pass needs: cut the end card, insert 3-4 s silences after every quiz question and drill line, overlay the options, record `subscribe_at` and chapters, and run the language gate on the transcript *as voiced*. Owner: shorts-builder (cut/silences/subscribe), visuals (quiz slides), language-editor (paraphrase gate).
3. **Process:** test a more natural voice and signpost phrases inside the A pipeline (cheap, and it copies B's one real strength). Owner: voice + scenario-writer.

## What was checked / not checked
Checked: hook frames at 0.2/0.8/1.4 s for both; contact sheets at one frame every 4 s (A 169 frames, B 150 frames); full-size frames of B at 120, 400, 465, 560, 589-596 s and the logo corner; A's new pictures zoomed (34, 52, 63, 316, 488 s), the house-return clip (10 frames, 258-272 s, motion confirmed), the keep-at-it card; full faster-whisper small.en transcripts of both (word timings, cpu_threads=4, temp output in the container's /tmp/vc-t02) + one segment of A re-transcribed alone; gap/pace statistics from the word timings; volumedetect on both; A chapters vs heard times (all 15 within 1 s); meta files of both; official logo vs the one used.
Not checked: `gate_av.py` (read-only role); the NLM source video `nlm-overview.mp4` itself (only via B); thumbnails beyond file identity (both are the same 142,306-byte file); YouTube end-screen setup (nothing uploaded).
