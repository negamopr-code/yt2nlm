# P01 · Episode 2 "Stop re-reading your word list": format decision (glottos-format-strategist, 2026-09-27)

Source: article §3 (`p01-why-you-forget-new-words.md`), episode map row 2 (`p01-shorts-scenario.md`). Evidence is reused from `p01-ep01-format.md`, plus one quota-free `source content` read of the PROBLEM 01 synthesis (60678678). No notebook query and no generation in this run.

## 1. Episode in one line
Re-reading trains recognition, not recall → one week later, re-readers remembered about 40 % and recall practisers about 61 %, with the same study time → Rule 2 "Cover the answer. Make your brain fetch it." → live cover-the-answer quiz (very happy → thrilled, very important → crucial, very busy → swamped) → the "swamped" family, one picture each → CTA.

## 2. Decision: a QUIZ-LED Short (text quiz + infographic bars + picture reveals)
| Part | Format | Why |
|---|---|---|
| Hook + recognition vs recall | card (hook) → 1 infographic panel | The hook is a contrarian habit attack. It is a statement, not a picture. |
| 40 % vs 61 % | **infographic panel (2 bars)** | A number story. The "experiment proof" structure (EngFluent's list A vs list B split test) is one of the synthesis's high-spread patterns. |
| Cover-the-answer | **3 text quiz beats** (question card → 1.5 s silent pause → reveal card) | The episode's lesson IS the quiz. Active recall has the widest reach beyond subscribers in the dataset (67.0×, 32.84×, 27.72× views/sub). The "Stop saying VERY → stronger word" swap format: TikTok 597.3 K likes; the synthesis lists "Stop saying VERY → Say LIVID" as a faceless series pattern. |
| Synonym spin "swamped" | **picture reveals** (one per-cell crop per synonym, word visible), optionally 2 picture flips | 7 pictures after 3 quiz pauses would be too long for 7 more pauses. Picture association: rank 3 (WIRED 7.5 M; Rene Bastarache 19.95× reach). |
| CTA | card | |

**Quiz beat: ESSENTIAL** (the episode demonstrates its own method; without it this is a lecture about recall). Picture flips in the spin: nice-to-have.

**Length:** the podcast runs about 95–105 s at 0.9× with intros cut, plus 3 × 1.5 s of inserted silence. That's acceptable. Don't shorten: the quiz is the retention device.

## 3. Rejected alternatives
- **Two-host debate "is re-reading useless?"** (the default heuristic for nuance): the user wants a single-host brief. The article also doesn't claim re-reading is useless, so a debate would invent a controversy.
- **Infographic with the cover table printed on it:** it prints the answers and spoils the quiz. The quiz is rendered by the builder as text cards, never by NotebookLM.
- **All 5 table rows as quiz beats:** very angry → livid repeats Ep1, and very tired → exhausted is the weakest upgrade. 3 rows keep the pace. The 5-row table goes into the description/pinned comment as a "cover and try" list.
- **Picture flips for all 7 synonyms:** about 10 s longer, and swamped vs stretched thin are both "too much work" scenes (the Ep1 lesson).

## 4. Synonym spin: "very busy → swamped" (7 pictures)
| # | Word/phrase | Scene (one picture) | Notes for the language editor |
|---|---|---|---|
| 1 | swamped | An office worker at a desk while papers and emails rise around them like floodwater | Article's word. Casual to professional. |
| 2 | slammed | A restaurant kitchen at the dinner rush, order tickets lined up along the rail | ⚠ Mainly US, informal. Check the register tag. |
| 3 | run off my feet | A nurse hurrying down a hospital corridor | ⚠ Mainly British, informal ("run off her feet"). Check. |
| 4 | tied up | A person in back-to-back video meetings, phone buzzing unanswered | Means busy AND unavailable ("I'm tied up until four"). |
| 5 | a lot on my plate | A person holding a dinner plate piled with a laptop, keys, bills and a baby bottle | Idiom, neutral. Literal picture = strong anchor. |
| 6 | hectic | A family morning: burning toast, a missing shoe, the school bus at the door | ⚠ Describes a time or place, not a person: "a hectic morning", NOT "I'm hectic". Say so in the reveal. |
| 7 | stretched thin | One person pulled in four directions by hands reaching from four desks | ⚠ Also "spread too thin"; check which is more common and use that one. |
Excluded on purpose: **snowed under** (its scene, buried in paper, is too close to swamped: the Ep1 lesson) and "up to my eyes/neck" (same problem).
Picture flips if built (nice-to-have): **a lot on my plate**, **tied up**, **hectic** have the only unmistakable fronts.

## 5. Beat outline (podcast audio drives timing; `from` = transcript time after cuts)
1. Card: **"Stop re-reading your word list."** (first spoken sentence = first second)
2. Card or panel: re-reading = "oh yes, I know that one" (recognition) vs "what's the word for…?" (recall)
3. Panel (main infographic 1): bars "Re-read · about 40 %" / "Practised recall · about 61 %", "one week later · same study time"
4. Card: **Rule 2 — Cover the answer. Make your brain fetch it.**
5. QUIZ: "very happy → ?" · 1.5 s silence + countdown · reveal "thrilled"
6. QUIZ: "very important → ?" · 1.5 s · reveal "crucial"
7. QUIZ: "very busy → ?" · 1.5 s · reveal "**swamped**" + the article sentence ("I'm completely swamped with reports this week — can we talk on Monday?")
8. Card: "That little moment of effort is when the memory gets stronger."
9–15. Spin: "Swamped has a family." One per-cell picture per word, in table order (~3 s each)
16. CTA card: anotherwordfor.net · "Next: the 1·3·7 rule" (⚠ SSL blocker on the site, see scenario)

## 6. NotebookLM commands (to run LATER, after the scenario writer has written `content/articles/p01-ep02-audio-script.md` and the language editor has approved it)
```sh
N="docker exec -w /workspace/glottos-marketing -e NLM_PROFILE=drawnformula glottos-marketing .nlmvenv/bin/nlm"
NB=8306c0a9-1418-41e2-a988-1c0459eafc89
# 1) script as its own source (all generations use ONLY this source, so the synthesis's '4x' / '70%' can't leak in)
$N source add $NB --file content/articles/p01-ep02-audio-script.md --title "AUDIO SCRIPT — Ep02 Stop re-reading your word list" --wait --profile drawnformula   # → SRC02
# 2) voice
$N audio create $NB --format brief --length short --language en --source-ids SRC02 -y --profile drawnformula --focus "Perform the AUDIO SCRIPT source as ONE presenter, word for word and in order. Use only its facts and examples. Add no statistics or studies, and no names of researchers, universities or years. Your very first words are the script's first line: 'Stop re-reading your word list.' Never use podcast markers: no 'This is the brief', no 'debrief', no 'welcome', no 'today we', no 'in this episode', no 'let's dive in', no 'on this show', no mention of listeners, hosts, podcasts, shows or episodes, and no sign-off such as 'that's it for today', 'thanks for listening' or 'see you next time'. The numbers are about 40 percent for re-reading and about 61 percent for practising recall, one week later, with the same study time. Never say these are percentages of words; they are of what people studied. Never call re-reading useless. QUIZ LINES: say the everyday phrase as a question and stop, for example 'Very busy?', then say the answer alone as its own sentence: 'Swamped.' Never say the answer before or inside the question. Read the seven swamped synonyms in the script's order, one short picture each. End with the script's last line: another word for dot net, and next the one-three-seven rule. Never say 'naked' or 'literally'."
# 3) main infographic (bars) — portrait, few words, answers NOT printed
$N infographic create $NB --orientation portrait --style instructional --detail concise --language en --source-ids SRC02 -y --profile drawnformula --focus "Portrait infographic with exactly 2 panels, large and simple. Title exactly: 'Re-reading vs recalling'. Panel 1: two bars side by side, labelled exactly 'Re-read' with 'about 40%' and 'Practised recall' with 'about 61%'; one caption under the bars, exactly: 'Remembered one week later. Same study time.' Panel 2: a hand covering the right half of a two-column list; the left column says exactly 'very busy', the right column is a blank covered card with NOTHING written on it. Print no other numbers, dates, names, study names or university names. Never print the words 'words', 'vocabulary', 'neural', '4x', '70%', 'useless' or 'proven'. Never print any answer word (swamped, thrilled, crucial, livid, exhausted). Check the spelling of every word."
# 4) synonym picture sheet — word in a strip UNDER each picture so the builder can crop picture-only fronts
$N infographic create $NB --orientation portrait --style bento_grid --detail concise --language en --source-ids SRC02 -y --profile drawnformula --focus "Portrait picture sheet. Title exactly: 'Very busy: 7 pictures'. 7 separate cards on a white background with clear white gaps between them, 2 columns. Each card = one picture on top and, underneath it in a solid coloured strip at the bottom of the card, ONLY the word or phrase given here. Nothing else is written on the card. In this order: 1 'swamped' - an office worker at a desk while papers and emails rise around them like floodwater; 2 'slammed' - a restaurant kitchen at the dinner rush, order tickets lined along the rail; 3 'run off my feet' - a nurse hurrying down a hospital corridor; 4 'tied up' - a person in back-to-back video meetings, phone buzzing unanswered; 5 'a lot on my plate' - a person holding a dinner plate piled with a laptop, keys, bills and a baby bottle; 6 'hectic' - a family morning with burning toast, a missing shoe and the school bus at the door; 7 'stretched thin' - one person pulled in four directions by hands reaching from four desks. Print NO labels such as mild, strong, casual, formal, informal, British, American, positive or negative. No scales, arrows, rankings, numbers or example sentences. No text anywhere except the title and the 7 words."
```
Every generated text (transcript and both images) passes glottos-language-editor before rendering. **Any podcast marker that still appears** ("This is the brief…", "debrief", "welcome", "in this episode", sign-offs) **is cut from the audio at acoustic boundaries** (`audio.cuts`, as in ep01_v5), never re-voiced with TTS. `bento_grid` for the sheet is untested. If it doesn't give gutter-separated cards, rerun with `--style instructional` and the same focus.

## 7. Builder features this episode needs
| Feature | Status | Need |
|---|---|---|
| **Inserted silence in the podcast track** (`audio.pauses: [{"at": <cut-timeline s, just before the answer word>, "dur": 1.5}]`, applied AFTER cuts; everything after `at` shifts by `dur`) | missing | **ESSENTIAL** (3×) |
| **Quiz beat**: question card ("very busy → ?", with an empty highlighted answer slot) held through the silence with a 1.5 s countdown bar, then a reveal card (answer word highlighted + example sentence as sub). Implementable as 2 beats (question `from` = prompt word; reveal `from` = answer word) + the pause + a countdown overlay on the question beat. | missing | **ESSENTIAL** |
| **Caption guard**: no caption during the silence; a chunk must never cross the question → answer boundary (the 3-word `chunks()` could otherwise show "Swamped." early). A beat boundary at the answer word already guarantees this, as long as the reveal beat starts exactly at the answer word. | partly (beat boundary) | essential |
| Per-cell crops of the synonym sheet (1 picture per beat, watermark strip dropped) | `grid` split exists but is untested on this layout; `bands-nolabel` gives pairs as a fallback | needed |
| Word-masked crop (picture only, bottom word strip removed) for picture flips | missing | nice-to-have |
| Podcast-marker scan in `--prep`/lang_gate (flags brief/debrief/welcome/episode/podcast/listeners/"today we") | missing | nice-to-have (the language editor does it by hand today) |

## 8. Flags for the language editor
- 40 %/61 % comes from prose passages. Never render or say "40 % of words". The source line belongs in the description only (Roediger & Karpicke 2006). No names or years in the voice.
- Register tags for slammed (US) and run off my feet (UK). Check hectic usage and stretched thin vs spread too thin.
- The quiz answers must match the article table exactly: thrilled, crucial, swamped.
