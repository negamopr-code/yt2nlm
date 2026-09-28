# P01 · Episode 5 "15 minutes a day. No app.": format decision (glottos-format-strategist, 2026-09-27)

Source: article §6, episode map row 5. Evidence is reused from `p01-ep01-format.md`, plus a quota-free `source content` read of the PROBLEM 01 synthesis (60678678). No query and no generation in this run.

## 1. Episode in one line
Once a day, 3 new words: minutes 0–5 Anchor (one sentence about your own life per word + its register) · 5–10 Recall (words from day 1 and day 3: cover, read the everyday phrase, say the stronger word before you look) · 10–15 Speak (words from day 7: two new sentences out loud each, as if telling a friend or a colleague) → "No streaks to protect, no decks to manage" → the "routine" family (make it a ritual, not a rut) → "Save this routine" → CTA.

## 2. Decision: NUMBERED PANELS (3-block timeline) + a "your turn" speak prompt; carousel spin-off
| Part | Format | Why |
|---|---|---|
| Hook "15 minutes a day. No app." | card | Counter-habit hook. It hits the app-fatigue gap in the synthesis ("Anki… feels like a chore; cards teach words in isolation", "5-min app streak = fluency" myth). |
| 0–5 / 5–10 / 10–15 | **3 numbered infographic panels** (a timeline block each, the current block lit) | A step-by-step method → numbered panels (heuristic). The synthesis's own best article outline is exactly this "15-minute routine (No Apps Required)". |
| "Your turn" | **speak-aloud prompt**: card "Say it out loud: one sentence about your week with *swamped*" + 3.0 s silent countdown, then the host's example ("I was swamped at work this week.") | Rank 5 "active output / self-talk" has the highest engagement rates in the dataset (linguamarina 5.69 %, POC English 5.10 %). |
| Synonym spin "routine" | picture reveals, 2 optional flips (ritual / rut) | Picture association (rank 3). The spin carries the episode's emotional point: a ritual, not a rut or a grind. |
| CTA "Save this routine" | card + full-timeline panel held 2 s | A saveable checklist. Carousel spin-off = the 3 panels as a photo post (local scan: carousels drive saves; web benchmark, unmeasured). |

**Quiz beat: NICE-TO-HAVE.** The "your turn" speak prompt uses the same inserted-silence mechanism but has no right/wrong reveal. It's valuable, but the episode works without it.

**Length:** target 75–90 s after 0.9× and cuts (+3 s speak pause). Fine for the brief format. Don't pad.

## 3. Rejected alternatives
- **Flashcards:** the routine is a procedure, not a vocabulary set. Deck imagery also contradicts the episode's "no decks to manage" message (the Kaufmann counter-evidence in Ep1).
- **Slide carousel as the Short itself:** motion + voice keeps watch time. The carousel is produced as a spin-off from the same panels (builder feature F).
- **Data table (routine vs Anki vs Duolingo):** needs app claims the article doesn't make and names brands. Rejected.
- **Minute-by-minute live demo (a real 15-minute session sped up):** needs screen recording or a face; the channel is faceless, and no such footage exists.

## 4. Synonym spin: "routine" family (8 pictures)
| # | Word | Scene | Notes for the language editor |
|---|---|---|---|
| 1 | routine | Morning sequence: alarm, kettle, the same bus | neutral |
| 2 | habit | Brushing teeth half-asleep, on autopilot | done without thinking |
| 3 | ritual | Sunday pancakes with the whole family, the same table every week | a special, meaningful repeat (positive) |
| 4 | drill | A fire drill: office staff calmly filing out to the car park | practice for an emergency; also "language drills". Picture = fire drill. |
| 5 | regimen | An athlete's training plan taped to the fridge, next to a water bottle | ⚠ formal; health/training. BrE also "regime" (which also means government). Check. |
| 6 | schedule | A train departures board | ⚠ times, not habits. Maybe say "a schedule is times, a routine is what you do". BrE also "timetable". |
| 7 | rut | A car's wheels spinning in a muddy groove | negative: stuck doing the same thing |
| 8 | the daily grind | Grey commuters queueing in the rain, coffee in hand | negative, casual |
Suggested closing line for the scenario writer (NEW wording, must pass the editor): **"Make it a ritual, not a rut."** Distinct fronts; flip candidates: ritual, rut, drill.

## 5. Beat outline
1. Card: **"15 minutes a day. No app."**
2. Card: "Three new words is plenty."
3. Panel: **0–5 min · Anchor** · one sentence about your own life + its register
4. Panel: **5–10 min · Recall** · cover it, read the everyday phrase, say the stronger word before you look
5. Panel: **10–15 min · Speak** · two new sentences out loud, as if telling a friend or a colleague
6. (optional) YOUR TURN: card "Say it out loud: one sentence about your week with *swamped*" · 3.0 s countdown · host's example sentence
7. Card: "No streaks to protect. No decks to manage."
8–15. Spin: routine → habit → ritual → drill → regimen → schedule → rut → the daily grind (~3 s each)
16. Card: "Make it a ritual, not a rut." (if the editor approves)
17. Panel: full 3-block timeline + **"Save this routine"** (hold 2 s) → CTA anotherwordfor.net · "Next: why your mind goes blank"

## 6. NotebookLM commands (run LATER, after `content/articles/p01-ep05-audio-script.md` is written and approved)
```sh
N="docker exec -w /workspace/glottos-marketing -e NLM_PROFILE=drawnformula glottos-marketing .nlmvenv/bin/nlm"
NB=8306c0a9-1418-41e2-a988-1c0459eafc89
$N source add $NB --file content/articles/p01-ep05-audio-script.md --title "AUDIO SCRIPT — Ep05 The 15-minute routine" --wait --profile drawnformula   # → SRC05
$N audio create $NB --format brief --length short --language en --source-ids SRC05 -y --profile drawnformula --focus "Perform the AUDIO SCRIPT source as ONE presenter, word for word and in order. Use only its facts and examples. Add no statistics or studies, and no names of researchers, universities, apps or years. Your very first words are the script's first line: 'Fifteen minutes a day. No app.' Never use podcast markers: no 'This is the brief', no 'debrief', no 'welcome', no 'today we', no 'in this episode', no 'let's dive in', no 'on this show', no mention of listeners, hosts, podcasts, shows or episodes, and no sign-off such as 'that's it for today', 'thanks for listening' or 'see you next time'. The three blocks are exactly minutes zero to five (anchor), five to ten (recall) and ten to fifteen (speak), with three new words a day. Add no other blocks or times. YOUR TURN LINE: say 'Your turn: say one sentence about your week with swamped, out loud.' and stop; then give the example as its own new sentence. Read the eight routine words in the script's order, one short picture each. End with the script's last line: another word for dot net. Never say 'naked' or 'literally'."
$N infographic create $NB --orientation portrait --style instructional --detail concise --language en --source-ids SRC05 -y --profile drawnformula --focus "Portrait infographic, exactly 3 panels stacked vertically with white gaps between them, like a timeline. Title exactly: 'The 15-minute routine'. Panel 1 header exactly '0-5 min · Anchor', text exactly 'Pick 3 words. Write one sentence about your own life for each.' Panel 2 header exactly '5-10 min · Recall', text exactly 'Cover the words. Say the stronger word before you look.' Panel 3 header exactly '10-15 min · Speak', text exactly 'Say two new sentences out loud with each word.' Print no other times, days, numbers, percentages, app names, streaks or brand names. Never print 'Day 14', 'Day 30', 'proven', 'neural' or 'naked'. Check the spelling of every word."
$N infographic create $NB --orientation portrait --style bento_grid --detail concise --language en --source-ids SRC05 -y --profile drawnformula --focus "Portrait picture sheet. Title exactly: 'Routine: 8 pictures'. 8 separate cards on a white background with clear white gaps between them, 2 columns, 4 rows. Each card = one picture on top and, underneath it in a solid coloured strip at the bottom of the card, ONLY the word given here. In this order: 1 'routine' - a morning sequence of alarm clock, kettle and the same bus; 2 'habit' - a person brushing their teeth half-asleep; 3 'ritual' - a family eating Sunday pancakes together at the same table; 4 'drill' - office staff calmly walking out of a building during a fire drill; 5 'regimen' - an athlete's training plan taped to a fridge next to a water bottle; 6 'schedule' - a train departures board; 7 'rut' - a car's wheels spinning in a deep muddy groove; 8 'the daily grind' - grey commuters queueing in the rain holding coffee cups. Print NO labels such as positive, negative, formal, informal, casual, good or bad. No scales, arrows, rankings, numbers except the title's 8, no example sentences. No text anywhere except the title and the 8 words."
```
The language editor gates all text. **Any leftover podcast marker is cut from the audio at acoustic boundaries** (`audio.cuts`), not re-voiced.

## 7. Builder features this episode needs
| Feature | Status | Need |
|---|---|---|
| Per-cell crops: vertical 3-panel timeline + 8-card sheet | `panels()` gap split exists for the timeline; `grid` untested on the sheet | needed |
| Inserted silence (3.0 s) + "your turn" card with a countdown bar, no reveal chip (the host's example sentence is the reveal) | missing | nice-to-have |
| Timeline progress strip (0–5 · 5–10 · 10–15, the current block lit) | missing (panels carry it) | nice-to-have |
| "Hold for save" static end frame | partly | nice-to-have |
| Carousel export 1080×1350 (title + 3 blocks + CTA) | missing | nice-to-have (spin-off) |

## 8. Flags for the language editor / article writer
- ⚠ Same consistency question as Ep3: "Recall (words from day 1 and day 3)" vs §4's "Day 1 = see it again". The panel text above avoids the day labels on purpose until this is settled.
- regimen vs regime, schedule vs timetable (UK/US).
- "Make it a ritual, not a rut" is new wording and needs approval.
