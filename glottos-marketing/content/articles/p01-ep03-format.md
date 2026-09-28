# P01 · Episode 3 "Review new words on these 3 days only": format decision (glottos-format-strategist, 2026-09-27)

Source: article §4, episode map row 3. Evidence is reused from `p01-ep01-format.md`, plus a quota-free `source content` read of the PROBLEM 01 synthesis (60678678). No query and no generation in this run.

## 1. Episode in one line
Recall works best just before you'd forget → Day 1 see the word again in its sentence · Day 3 cover it and recall it before you look · Day 7 use it in a new sentence of your own, out loud → each check-in resets the curve, and it falls more slowly each time → Rule 3 "days 1, 3 and 7, not every day, not never" → the "remember" family (recognise … reminisce) → "Screenshot this schedule" → CTA.

## 2. Decision: INFOGRAPHIC PANELS (a 3-step calendar) + picture reveals; SHORTER Short
| Part | Format | Why |
|---|---|---|
| Hook + "just before you'd forget" | card → 1 panel (the curve shape only, no numbers) | A mechanism, so panel + voice. |
| Day 1 · 3 · 7 | **3 numbered infographic panels (calendar)**, one per day, then 1 full-calendar panel held ~2 s for the screenshot | A schedule is a sequence to save, not something to recall. Spaced repetition is rank 4 by reach but has the **highest engagement** in the dataset (Dogen 7.13 %, RealLife English 4.03 %). The local scan (`state/retention-pain-competitor-scan-and-plan.md`) rates the 1-3-7 schedule the "super-saveable" pin/carousel piece (web benchmarks, not measured). |
| Synonym spin "remember" | picture reveals, grouped under the 3 days where they fit | Picture association (rank 3). |
| Optional quiz | "You know her face but not her name: recognise or recall?" (2-option question, 2.0 s pause, reveal "You **recognise** the face, but you can't **recall** the name.") | Ties back to Ep2 (recognition vs recall). Nice-to-have. |
| CTA | card + "Screenshot this schedule" | |

**Quiz beat: NICE-TO-HAVE** (one 2-option question). The saveable calendar is the payoff.

**Length: this topic should be SHORTER.** There are 3 facts and 1 rule. Target 60–75 s after the 0.9× slowdown and cuts. Script ≈ 150–170 words (the Ep1 script of ~330 words became 85.7 s raw, so a brief overview compresses. Length control through the script is approximate, not guaranteed). If NotebookLM pads with invented content, the language gate cuts it.

## 3. Rejected alternatives
- **Flashcards/quiz-led Short:** there's nothing to recall in a schedule. A quiz on "which day do you recall?" tests trivia, not vocabulary.
- **Data table (1-3-7 vs Anki vs every day):** would bring in app comparisons and "Anki" branding. The article only says "you don't need a complicated app". The Anki/app-fatigue gap is handled in Ep5.
- **Two-host podcast:** the user rule is a single-host brief.
- **Carousel as the Short itself:** kept as a **spin-off** (a 4-slide photo post: title / Day 1 / Day 3 / Day 7). It reuses the same panels and needs the carousel export (builder feature F).

## 4. Synonym spin: "remember" family (7 pictures, different kinds of remembering)
| # | Word/phrase | Scene | Ties to | Notes for the language editor |
|---|---|---|---|---|
| 1 | recognise | Spotting a friend's face in a busy train-station crowd | Day 1 (see it again) | ⚠ British spelling (article uses "practise"); US "recognize". Choose one channel-wide. |
| 2 | recall | At a cash machine, eyes closed, fetching the PIN | Day 3 | |
| 3 | memorise | An actor pacing backstage, mouthing lines from a script | | ⚠ same spelling choice (memorize) |
| 4 | ring a bell | Hearing a name on the phone; a small bell rings above the head | | Idiom: familiar but vague. "That name rings a bell." |
| 5 | on the tip of your tongue | A word bubble stuck at someone's lips, finger raised | | ⚠ This is ALMOST remembering. The host must say so. The article intro uses the phrase too. |
| 6 | jog your memory | A detective showing a witness an old photo | | "Does this jog your memory?" |
| 7 | reminisce | Grandparents laughing over an old photo album | | Remembering happy past times, not facts. Avoid for vocabulary. |
Not strict synonyms. The host must say "seven ways to remember", NOT "seven synonyms of remember". Fronts are distinct (crowd / cash machine / backstage / phone bell / stuck word / detective / album). Excluded: "learn by heart" (same picture idea as memorise), "retain" (no concrete picture).

## 5. Beat outline
1. Card: **"Review new words on these 3 days only."**
2. Panel: forgetting-curve SHAPE with a small "review" mark just before it drops (no numbers)
3. Panel: **Day 1** · "See it again in its sentence" (+ recognise picture)
4. Panel: **Day 3** · "Cover it. Recall it before you look." (+ recall picture)
5. (optional) QUIZ: "Her face, but not her name: recognise or recall?" · 2.0 s · reveal
6. Panel: **Day 7** · "Use it in a new sentence, out loud."
7. Panel: full 1·3·7 calendar · "Each check-in resets the curve"
8–12. Spin: memorise, ring a bell, on the tip of your tongue, jog your memory, reminisce (~3 s each; recognise/recall were already shown at beats 3–4)
13. Card: **Rule 3 — Days 1, 3 and 7. Not every day, not never.** + "Screenshot this" (hold 2 s)
14. CTA: anotherwordfor.net · "Next: the one thing to learn with every word" (Ep4)

## 6. NotebookLM commands (run LATER, after `content/articles/p01-ep03-audio-script.md` is written and approved)
```sh
N="docker exec -w /workspace/glottos-marketing -e NLM_PROFILE=drawnformula glottos-marketing .nlmvenv/bin/nlm"
NB=8306c0a9-1418-41e2-a988-1c0459eafc89
$N source add $NB --file content/articles/p01-ep03-audio-script.md --title "AUDIO SCRIPT — Ep03 The 1-3-7 rule" --wait --profile drawnformula   # → SRC03
$N audio create $NB --format brief --length short --language en --source-ids SRC03 -y --profile drawnformula --focus "Perform the AUDIO SCRIPT source as ONE presenter, word for word and in order. Keep it short. Use only its facts and examples. Add no statistics, percentages or studies, and no names of researchers, universities or years. Your very first words are the script's first line: 'Review new words on these three days only.' Never use podcast markers: no 'This is the brief', no 'debrief', no 'welcome', no 'today we', no 'in this episode', no 'let's dive in', no 'on this show', no mention of listeners, hosts, podcasts, shows or episodes, and no sign-off such as 'that's it for today', 'thanks for listening' or 'see you next time'. The only days are day one, day three and day seven; never mention day zero, day fourteen, day thirty or any app by name. Do not call the schedule scientifically proven. Say the seven ways to remember in the script's order and say that on the tip of your tongue means almost remembering. End with the script's last line: another word for dot net. Never say 'naked' or 'literally'."
$N infographic create $NB --orientation portrait --style instructional --detail concise --language en --source-ids SRC03 -y --profile drawnformula --focus "Portrait infographic, 4 panels stacked vertically with white gaps between them. Title exactly: 'The 1 · 3 · 7 rule'. Panel 1: a simple falling curve with NO numbers, NO percentages and NO axis values, and a small flag just before it drops, labelled exactly 'Review here'. Panel 2: a calendar day marked 'Day 1' with the text exactly 'See it again in its sentence'. Panel 3: 'Day 3' with exactly 'Cover it. Recall it before you look.' Panel 4: 'Day 7' with exactly 'Use it in a new sentence, out loud.' Print no other days (never Day 0, Day 14 or Day 30), no percentages, no names, no dates, no app names. Never print 'proven', 'science', 'neural' or 'naked'. Check the spelling of every word."
$N infographic create $NB --orientation portrait --style bento_grid --detail concise --language en --source-ids SRC03 -y --profile drawnformula --focus "Portrait picture sheet. Title exactly: '7 ways to remember'. 7 separate cards on a white background with clear white gaps between them, 2 columns. Each card = one picture on top and, underneath it in a solid coloured strip at the bottom of the card, ONLY the word or phrase given here. In this order: 1 'recognise' - spotting a friend's face in a busy train-station crowd; 2 'recall' - a person at a cash machine, eyes closed, remembering the PIN; 3 'memorise' - an actor pacing backstage, mouthing lines from a script; 4 'ring a bell' - a person on the phone hearing a name, a small bell ringing above their head; 5 'on the tip of your tongue' - a word bubble stuck at someone's lips, one finger raised; 6 'jog your memory' - a detective showing a witness an old photo; 7 'reminisce' - grandparents laughing over an old photo album. Print NO labels such as mild, strong, formal, informal, positive, negative, Day 1, Day 3 or Day 7. No numbers except the title's 7, no arrows, no example sentences. No text anywhere except the title and the 7 words or phrases. Spell recognise and memorise with s."
```
The language editor gates all text. **Any leftover podcast marker is cut from the audio at acoustic boundaries** (`audio.cuts`), not re-voiced.

## 7. Builder features this episode needs
| Feature | Status | Need |
|---|---|---|
| Per-cell crops for the 4-panel calendar + the picture sheet | `panels()` gap split exists (good for the vertical calendar); `grid` for the sheet is untested | needed |
| Two images in one beat (day panel + its picture crop side by side / stacked) for beats 3–4 | missing (one visual per beat today) | nice-to-have (fallback: separate beats) |
| Quiz beat + inserted silence (2.0 s, 2-option question card) | missing | nice-to-have |
| "Hold for screenshot" static end frame (2 s, no push-in, no caption) | partly (a card beat with a silence at the end) | nice-to-have |
| Carousel export: 1080×1350 stills of beats 3, 4, 6, 7 + title, for an IG/TikTok photo post | missing | nice-to-have (spin-off) |
| Day-progress strip (1 · 3 · 7 dots, the current one lit) | missing | nice-to-have |

## 8. Flags for the language editor / article writer
- ⚠ **Consistency question to settle BEFORE generating Ep3 or Ep5 visuals:** §4 says Day 1 = "see it again" (not recall), but §6 says minutes 5–10 = "Recall (words from day 1 and day 3)". Also, is the learning day Day 0 or Day 1? The visuals print these labels, so the article writer or the user must pick one reading. I did not change anything.
- "Each check-in resets the forgetting curve" is a simplification. Keep it as the article's wording. Don't add numbers.
- The 1·3·7 schedule is a practical rule, not a study result (Cepeda 2006 supports spacing in general). The description may cite Cepeda; the voice must not claim "science says 1, 3, 7".
- Channel-wide spelling: recognise/memorise (UK, consistent with the article's "practise") vs US.
