# VISUALS: Words That Stick, Episode 3 "Review new words on these 3 days only" (NotebookLM infographic focus texts + draft unit plan)

> Language gate: approved 2026-09-27 by glottos-language-editor — pre-generation text gate (audio script, this file, content/youtube/ep03.json). Changes: rule line "not every day, not never" -> "not every day, and not just once" (voice, card, description); "check-in" -> "review"; "very hard to lose. It's strong." -> "much harder to forget. The memory is strong." (avoids overclaim and the "strong word" = rude/forceful word reading); sturdy scene "a ladder you can stand on" -> "a ladder that stays steady when you climb it"; hook point 2 made a full sentence; syn sheet title -> '5 ways to say strong'; forbidden tokens (Day 0/2/14/30, Anki, Duolingo, naked, recognise) removed from generation prompts to avoid priming, replaced by positive rules; description "Rule 3:" -> "The rule:"; tag "synonyms for strong" -> "other ways to say strong". NOT yet checked: the generated audio/transcript, both infographic PNGs, the unit JSON (gate again after generation). Caption fixes the unit will need: recognize->recognise, recognized->recognised, memorize->memorise, practice (verb)->practise, favorite->favourite, color->colour, "another word for dot net" or a split domain -> anotherwordfor.net.

Both infographics are generated LATER (visuals step), strictly in series, from the Ep03 AUDIO SCRIPT source only (`--source-ids <SRC03>`), so the synthesis's numbers, study names and app names stay out. Both images pass glottos-language-editor before rendering. Never ship a NotebookLM/Gemini watermark: the builder's crops drop the bottom strip.

Standing conventions for this episode:
- **Days:** you learn the word on the first day (unnamed); review on Day 1 (the next day), Day 3 and Day 7. Nothing may print or say "Day 0", and no other day number may appear as a label.
- **Spelling:** British, channel-wide (Ep1/Ep2 scripts use "recognise", "practised"). NotebookLM tends to print US spellings, so check every image.
- **Synonym spin = "strong"**, page https://anotherwordfor.net/another-word-for-strong/ (HTTP 200 on 2026-09-27; the page lists firm, sturdy, durable, mighty and muscular). The format plan's "remember" family has no page in the site's 78 posts (no remember/recall/memory/forget slug exists), so it was replaced. "Strong" is the closest fit: the article's point is that after Day 7 a word you've used yourself "is much harder to forget", and all five words have concrete pictures. They are "5 ways to say strong", one for each kind of thing (a grip, an object, a material, a tree, a body). They are NOT strict synonyms.
- The quiz answer ("recognise" / "recall" as the answer to the face-and-name question) must NEVER be printed on the main infographic. The builder renders the quiz as its own cards.

## 1. Main infographic: `state/nlm-raw/ep03-infographic.png` (unit key `infographic`, panels `title+1`, `2`, `3`, `4`, `5`)

Command flags: `infographic create <NB> --orientation portrait --style instructional --detail concise --language en --source-ids <SRC03>`

Focus text (exact):

> Portrait infographic with exactly 5 panels stacked from top to bottom, separated by clear white gaps. Big, simple pictures and very few words. Title exactly: 'Review new words on these 3 days only'.
> Panel 1 (the hook, a picture): a row of 7 small calendar squares numbered 1 to 7 from left to right. Squares 1, 3 and 7 are circled in thick red marker and have a small tick; squares 2, 4, 5 and 6 are plain and grey. No other text on this panel.
> Panel 2 (a picture): a simple curve that starts high on the left and falls to the right, with NO numbers, NO percentages, NO axis values and NO axis labels. A small flag stands on the curve just before its steepest drop, labelled exactly 'Review here'.
> Panel 3: a large calendar badge 'Day 1' next to a picture of an open notebook with one sentence in it and one word in that sentence underlined. Text exactly: 'See it again in its sentence'.
> Panel 4: a large calendar badge 'Day 3' next to a picture of a hand covering one word in the notebook with a blank card, NOTHING written on the card. Text exactly: 'Cover it. Recall it before you look.'
> Panel 5: a large calendar badge 'Day 7' next to a picture of a person speaking out loud to a friend across a café table, a speech bubble with no text in it. Text exactly: 'Use it in a new sentence, out loud.'
> Print no other text, labels, dates, names, study names or app names. The only day labels anywhere are 'Day 1', 'Day 3' and 'Day 7'. The only numbers are the title's 3 and the squares 1 to 7 in panel 1. No arrows, no logos. Check the spelling of every word.

Fallback: if NotebookLM merges panels or draws fewer than 5, rerun once with the same focus. If panel 2 (the curve) is still missing, drop it: beat 2 then reuses `title+1`.

## 2. Synonym picture sheet: `state/nlm-raw/ep03-synonyms-infographic.png` (unit key `extra_infographics.syn`, `split: {"syn": "bands"}`)

Five stacked full-width cards (Ep2 layout, so each crop is large). The word sits in its OWN strip under the picture, so the visuals step can also cut a picture-only (word-hidden) crop.

Command flags: `infographic create <NB> --orientation portrait --style instructional --detail concise --language en --source-ids <SRC03>` (fallback if the cards touch or the strip sits inside the picture: rerun with the same focus and `--style bento_grid`).

Focus text (exact):

> Portrait picture sheet. Title exactly: '5 ways to say strong'. Exactly 5 cards stacked in ONE column from top to bottom, each card the full width of the page, on a white background with clear white gaps between the cards. Each card = one large picture on top and, underneath it, a separate solid dark strip that contains ONLY the one word given here, in large white letters. The word is never inside the picture and never on top of the picture. Nothing else is written on the card. In this order:
> 1 'firm': two business people shaking hands, a close-up of the handshake, both hands gripping.
> 2 'sturdy': a painter standing high on a wooden ladder, the ladder standing straight and steady on the floor.
> 3 'durable': a pair of old, muddy hiking boots on a mountain trail, worn but whole, the laces still tied.
> 4 'mighty': a huge old oak tree on a hill in a storm, its wide trunk and thick branches standing against the wind.
> 5 'muscular': a weightlifter holding a heavy barbell above their head, big arms.
> Print NO labels on the cards (no register, strength, country or day labels). No scales, arrows, rankings, numbers, scores, clocks, example sentences or speech bubbles. No text anywhere except the title and the 5 words. Check the spelling of every word.

## 3. Do-not-say / do-not-print list (voice, captions, cards, images)
- Podcast markers: "this is the brief", "debrief", "welcome", "today we", "in this episode", "let's dive in", "let's break it down", "listeners", "you're listening", "podcast", "show", "episode", "host", "video", "deep dive", any sign-off.
- Sources in the voice: names (Ebbinghaus, Cepeda), universities, years, "a study", "researchers", "scientists", "science says", "proven". The 1-3-7 schedule is a practical rule, not a study result.
- Numbers: none except days 1, 3, 7 and "five/5" (spin). No percentages. No Day 0, Day 2, Day 14, Day 30, "a month".
- Apps: no app, flashcard program or algorithm by name ("Anki", "Duolingo", "spaced-repetition app"). The Anki/app-fatigue gap belongs to Ep5.
- "Review every day" as advice (only inside "not every day, and not just once").
- Spin: never "synonyms of strong", "means the same"; never apply the five words to memory ("a mighty memory", "muscular words").
- CTA: never "search", "type in", "sites like", "websites like"; never claim the site has pictures, example sentences, register notes, quizzes, audio or an app (the strong page is a plain word list).
- Filler: "literally", "basically", "honestly", "super", "amazing", "game-changer", "hack", "trick", "secret".
- "It's strong" / "a strong word" after point 7 ("a strong word" means a forceful or rude word); the bridge is "The memory is strong."
- "Not never" (double negative; learners are taught to avoid it): the rule is "Not every day, and not just once."

## 4. Draft unit plan (NOT a unit JSON yet)
The beats are timed later from the real recording, and the order follows what the presenter actually says. Planned unit id: `words-that-stick-ep03-v1` (file `shorts/units/ep03_v1.json`), series "Words That Stick", episode 3, `script` = `content/articles/p01-ep03-audio-script.md`, `visuals` = this file, `infographic` = `state/nlm-raw/ep03-infographic.png`, `extra_infographics.syn` = `state/nlm-raw/ep03-synonyms-infographic.png`, `split: {"syn": "bands"}`, audio = the NotebookLM brief overview slowed to 0.9x (`state/nlm-raw/ep03-podcast-brief-0.9.mp3` + `.words.json`), with `cuts`/`inserts`/`fixes` set after transcription. Target 60-75 s after cuts and pauses.

| # | Talking point | Visual | Builder text (cards / quiz) |
|---|---|---|---|
| 1 | Hook: review new words on these three days only (≤4 s) | panel `title+1` (7 squares, 1·3·7 circled) | none (picture hook, not a text-only card) |
| 2 | Recall works best just before you'd forget | panel `2` (curve + 'Review here') | none |
| 3 | Day 1: see it again in its sentence | panel `3` | none |
| 4 | Day 3: cover it, recall it before you look | panel `4` | none |
| 5 | QUIZ: face but not name, recognise or recall? | quiz beat | q: "You know her face, but not her name. *Recognise* or *recall*?" · q_sub: "Say it before you see it." · pause 2.0 s with countdown · a: "You *recognise* the face. You can't *recall* the name." (reveal_at = start of the spoken answer; if the presenter never asks it as a question, the question card sits over the preceding line and the pause is inserted before the spoken answer) |
| 6 | Day 7: use it in a new sentence, out loud | panel `5` | none |
| 7 | Each review resets the curve, it falls more slowly; after Day 7 the word is much harder to forget, the memory is strong | panel `2` again (curve), or `title+1` if panel 2 was dropped | none |
| 8-12 | Five ways to say strong: handshake → firm, steady ladder → sturdy, boots → durable, oak → mighty, weightlifter → muscular | `syn:1` … `syn:5`, one beat per word (about 3 s each); if the visuals step cuts word-hidden crops, show the picture-only crop on the scene and the full band on the word | none. Optional 2nd quiz ONLY if the presenter asks one as a question (e.g. "a handshake that's strong?" → *firm*, reveal_panel `syn:1`). Maximum 2 quizzes in total. |
| 13 | Rule: Days 1, 3 and 7, not every day, and not just once | card, held 2 s static for the screenshot | headline: "Days *1 · 3 · 7*" · sub: "Not every day. Not just once. Screenshot this." |
| 14 | Action for tomorrow: see today's new words again, in their sentences | card (or panel `3` if the builder prefers a picture) | headline: "Tomorrow: see them again" · sub: "Today's new words, in their sentences" |
| 15 | CTA + teaser | card | headline: "Look up *another word for strong*" · sub: "anotherwordfor.net · Next: why you freeze mid-sentence" |

Notes for the builder / language editor:
- Captions come from the transcript. Ep2's captions ended up with US spellings from the transcriber ("recognize", "practice"); set `fixes` so on-screen text uses British spelling ("recognise") to match the cards and the channel.
- If the presenter adds content that is not in the script (study names, numbers, apps, extra days), cut it at acoustic boundaries; do not re-voice.
- If the recording is still over 75 s after the cuts, trim filler and the bridge line ("The memory is strong") first. Do not drop spin words: the pipeline rule is 5-10 synonyms per episode and this episode has exactly 5. Ask the user instead.
