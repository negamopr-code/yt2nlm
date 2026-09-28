# VISUALS: Words That Stick, Episode 5 "The 15-minute routine" (NotebookLM infographic focus texts + draft unit plan)

> Language gate: APPROVED by glottos-language-editor 2026-09-27T17:39Z — pre-generation text gate (audio script, this file, content/youtube/ep05.json). Changes: CTA "look up 'never give up synonym'" -> "find more ways to say 'never give up'" (the old line is search-box English, not something a native teacher says; voice, row 15 card headline "More ways to say *never give up*", description line "More ways to say \"never give up\":"); synonym-sheet title now quotes the phrase ('5 ways to say "never give up"') so it cannot be read as the command "never give up"; row 13 obstinate chip "formal · negative" -> "negative · disapproving" (Oxford Learner's: "often disapproving", no formal label); row 12 "Often about things" -> "Often about hard things" (relentless collocates with unpleasant things: rain, pressure, criticism). Chips checked: tenacious = formal in Oxford Learner's, so "a bit formal · positive" stands; determined, keep going = neutral. Accepted as native: "Three new words is plenty" (amount = singular), "as if you were telling a friend or a colleague", "That's the bad kind: just stubborn", "no decks to manage" (article wording; card shows it). The audio script header was rewritten so the NotebookLM source no longer quotes the page's other words or the dropped CTA. ⚠ Publishing issue for the user: anotherwordfor.net's TLS certificate expired 2024-02-05; the page returns 200 only with certificate checks off, browsers show a security warning. NOT yet checked: the generated audio and transcript, both infographic PNGs, the unit JSON (gate again after generation). Caption fixes the unit will need: practice (verb) -> practise, color -> colour, favorite -> favourite; "15 minute" -> "15-minute" when it is an adjective; "another word for dot net" or a split domain -> anotherwordfor.net; the CTA is "Find more ways to say 'never give up'" (the search-style phrase "never give up synonym" is never voiced or printed).

Both infographics are generated LATER (visuals step), strictly in series, from the Ep05 AUDIO SCRIPT source only (`--source-ids <SRC05>`), so the synthesis's numbers, study names and app names stay out. Both images pass glottos-language-editor before rendering. Never ship a NotebookLM/Gemini watermark: the builder's crops drop the bottom strip.

Standing conventions for this episode:
- **Register labels are builder text only.** NotebookLM never prints casual / neutral / formal / positive / negative. Every chip and avoid-when line on screen comes from the unit JSON, which the language editor gates.
- **Spelling:** British, channel-wide ("practise" as a verb, "colour", "favourite", "recognise"). NotebookLM and the transcriber tend to print US spellings, so check every image and caption.
- **Continuity:** Ep4 ends "Next: the 15-minute routine", so the hook keeps that promise ("Fifteen minutes a day, no app: here's the routine."). Ep5 ends "Next: why your mind goes blank." (article §7 = Ep6). Callbacks, one line each: *livid* (Ep1 spin, used as the recall example "very angry" -> livid, the article §3 cover table) and *swamped* (Ep2 quiz answer, the "your turn" word; Ep4 used it too).
- **Synonym spin = "never give up"**, page https://anotherwordfor.net/never-give-up-synonym/ (HTTP 200 on 2026-09-27). Checked the same day and all 404: /another-word-for-routine/, -habit/, -ritual/, -schedule/, -practice/, -daily/, -repeat/, -grind/, -regular/, -drill/, -plan/, -method/, -system/, -regimen/, -consistent/, -rut/. The site's post sitemap (wp-sitemap-posts-post-1.xml, 78 posts) has no routine-family page, so the format plan's "routine" x8 spin is replaced. "Never give up" fits the episode's point: a routine works only if you keep going. It is also one of the site's ranking pages (journal: "never give up synonym" is in the ranking cluster). **What the page actually is:** a long children's-style article, not a plain word list. It names persist, relentless/unrelenting, tenacious, determined, resolute, obstinate, unshakable and more, and its heading is "Keep Going: Finding Other Words for 'Never Give Up'". Every spin word is on that page ("keep going" is its heading). Nothing about the page is claimed in voice, cards or description; only its URL appears, in the description.
- **Day-label decision (settles the flag in `p01-ep05-format.md` §8):** there are NO day labels in voice, panels, cards or description. Article §6 says Recall = "words from day 1 and day 3" and Speak = "words from day 7". Ep3 (from article §4) said Day one = see the word again in its sentence, Day three = cover it and recall it, Day seven = use it in a new sentence out loud. The two readings clash on day 1 (see again vs recall), so the Ep5 blocks only name the action: Anchor = one sentence about your own life per new word, Recall = cover and say the stronger word before you look, Speak = two new sentences out loud per word. This matches Ep3's day three and day seven steps without numbering days, and adds nothing that Ep3 contradicts. The article's §6 wording is untouched (article-writer decision, still open).
- The "your turn" example ("I was swamped at work this week.") must NEVER be printed on an infographic. The builder renders the prompt and the example as its own cards.

## 1. Main infographic: `state/nlm-raw/ep05-infographic.png` (unit key `infographic`, panels `title+1`, `2`, `3`)

Command flags: `infographic create <NB> --orientation portrait --style instructional --detail concise --language en --source-ids <SRC05>`

Focus text (exact):

> Portrait infographic with exactly 3 panels stacked from top to bottom like a timeline, separated by clear white gaps. Big, simple pictures and very few words. Title exactly: 'The 15-minute routine'.
> Panel 1: a person at a kitchen table writing in a paper notebook with a pen, a cup of tea next to the notebook. Header exactly: '0-5 min · Anchor'. Text exactly: 'Write one sentence about your own life with each new word.'
> Panel 2: a hand covering one column of a handwritten word list in a paper notebook. Header exactly: '5-10 min · Recall'. Text exactly: 'Cover the stronger word. Say it before you look.'
> Panel 3: a person on a sofa talking to a friend, both relaxed and smiling. Header exactly: '10-15 min · Speak'. Text exactly: 'Say two new sentences out loud with each word.'
> Each panel's header and text sit in their own strip under the picture, never on top of the picture. Print no other text: no other times, no dates, no app names, no phones, no screens, no logos, no arrows except one simple line joining the three panels. Check the spelling of every word.

Fallback: if NotebookLM merges panels or draws fewer than 3, rerun once with the same focus. If the headers are still wrong, the builder shows each block as a card over its picture (header + text from the unit JSON).

## 2. Synonym picture sheet: `state/nlm-raw/ep05-synonyms-infographic.png` (unit key `extra_infographics.syn`, `split: {"syn": "bands"}`)

Five stacked full-width cards (Ep2-Ep4 layout, so each crop is large). The word sits in its OWN strip under the picture, so the visuals step can also cut a picture-only crop.

Command flags: `infographic create <NB> --orientation portrait --style instructional --detail concise --language en --source-ids <SRC05>` (fallback if the cards touch or the strip sits inside the picture: rerun with the same focus and `--style bento_grid`).

Focus text (exact):

> Portrait picture sheet. Title exactly: '5 ways to say "never give up"'. Exactly 5 cards stacked in ONE column from top to bottom, each card the full width of the page, on a white background with clear white gaps between the cards. Each card = one large picture on top and, underneath it, a separate solid dark strip that contains ONLY the words given here, in large white letters. The words are never inside the picture and never on top of the picture. Nothing else is written on the card. In this order:
> 1 'keep going': a runner in a rain jacket running along a wet street in heavy rain.
> 2 'determined': a young girl in a helmet getting back on her bike after falling off, with a grazed knee and a firm face.
> 3 'tenacious': a small terrier pulling hard on a rope toy and not letting go.
> 4 'relentless': big grey waves crashing against dark rocks on the coast.
> 5 'obstinate': a donkey on a country path refusing to move while a farmer pulls on its rope.
> Print NO labels on the cards: nothing about tone, style or strength. No scales, arrows, rankings, numbers, scores, example sentences or speech bubbles. No text anywhere except the title and the 5 words. Check the spelling of every word.

## 3. Do-not-say / do-not-print list (voice, captions, cards, images; the builder cuts any of these from the recording)
- Podcast markers: "this is the brief", "debrief", "welcome", "today we", "in this episode", "let's dive in", "let's break it down", "listeners", "you're listening", "podcast", "show", "episode", "host", "video", "deep dive", any sign-off ("that's it", "thanks for listening", "see you next time", "until next time").
- Sources and science: names, universities, years, "a study", "researchers", "scientists", "science says", "proven", "your brain is wired". No percentages (the article's 75%, 40% and 61% belong to Ep1/Ep2, never here).
- Numbers and times: none except fifteen, the blocks 0-5 / 5-10 / 10-15, three (words), one and two (sentences) and five (spin). No days (no "day 1 / day 3 / day 7"; see the day-label decision), no weeks, no "30 days", no "habit in 21 days".
- Apps: no app, program, deck tool or brand name; no comparison with apps; no "streak" apart from the one line "no streaks to protect". Pictures: no phones or screens.
- Spin: never "synonyms of never give up", "means the same", "same meaning". Never present obstinate as praise: it is the bad kind (stubborn). Never "relentless" as advice to the learner ("be relentless"). The page's other words (sedulous, indefatigable, pertinacious, inexorable, resolute, staunch, unshakable, persist) are NOT in this episode; cut them if the presenter improvises them. Never "superhero".
- Format-plan words no longer used: routine family (habit, ritual, drill, regimen, schedule, rut, the daily grind) and "Make it a ritual, not a rut". Cut them if improvised; "routine" itself is fine (hook).
- Frequency: never "review every day", "every word every day". The routine is done once a day.
- CTA: never "search", "search for", "type in", "look up 'never give up synonym'" (search-style English), "sites like", "websites like"; never claim the site has pictures, example sentences, register notes, quizzes, audio, stories or an app. The article's closing sentence "every synonym comes with a sentence, a register tag and a note on when to avoid it" must NOT be voiced or printed.
- Filler: "literally", "basically", "honestly", "super", "amazing", "game-changer", "hack", "trick", "secret".
- Teaser: only "Next: why your mind goes blank." Never a different next topic, never "next time".

## 4. Draft unit plan (NOT a unit JSON yet)
The beats are timed later from the real recording, and the order follows what the presenter actually says. Planned unit id: `words-that-stick-ep05-v1` (file `shorts/units/ep05_v1.json`), series "Words That Stick", episode 5, `script` = `content/articles/p01-ep05-audio-script.md`, `visuals` = this file, `infographic` = `state/nlm-raw/ep05-infographic.png`, `extra_infographics.syn` = `state/nlm-raw/ep05-synonyms-infographic.png`, `split: {"syn": "bands"}`, audio = the NotebookLM brief overview slowed to 0.9x (`state/nlm-raw/ep05-podcast-brief-0.9.mp3` + `.words.json`), with `cuts`/`pauses`/`fixes` set after transcription. Target 65-75 s after cuts and the pause (spoken script about 180 words + one "your turn" pause of 3.0 s); hard ceiling 90 s.

| # | Talking point | Visual | Builder text (cards / prompt) |
|---|---|---|---|
| 1 | Hook: fifteen minutes a day, no app: here's the routine (≤4 s) | card over panel `title+1` (title strip visible) | headline: "15 minutes a day." · sub: "No app." |
| 2 | Once a day; three new words is plenty | card | headline: "3 new words a day" · sub: "That's plenty." |
| 3 | 0-5 min · Anchor: one sentence about your own life per new word | panel `title+1` (block 1 lit) | progress strip "0-5 · 5-10 · 10-15", first block lit (if the builder has it; else none) |
| 4 | 5-10 min · Recall: cover the stronger word, read "very angry", say "livid" before you look | panel `2` above a mini cover card | cover card: "very angry -> ?" then reveal "livid" at the spoken word (no pause; this is an example, not the quiz) |
| 5 | 10-15 min · Speak: two new sentences per word, out loud, to a friend or a colleague | panel `3` | progress strip, third block lit |
| 6 | YOUR TURN: one sentence about your week with "swamped", out loud; then the example | speak-prompt card (no picture) | headline: "Your turn: say it out loud" · sub: "one sentence about your week with *swamped*" · inserted 3.0 s pause with a countdown bar, no reveal chip · then card: "I was swamped at work this week." (reveal_at = start of the spoken example) |
| 7 | No streaks to protect, no decks to manage. Just keep going. | card | headline: "No streaks. No decks." · sub: "Just keep going." |
| 8 | Five ways to say never give up | `syn` title band, or a card | headline: "5 ways to say *never give up*" |
| 9 | Runner in the rain: keep going | `syn:1` | chip "neutral · everyday" |
| 10 | Girl back on her bike: determined | `syn:2` | chip "neutral · positive" |
| 11 | Dog with the rope toy: tenacious | `syn:3` | chip "a bit formal · positive" |
| 12 | Waves on the rocks: relentless | `syn:4` | chip "strong · never stops" · "Often about hard things: relentless rain, relentless pressure" |
| 13 | Donkey that won't move: obstinate, the bad kind: just stubborn | `syn:5` | chip "negative · disapproving" · "= stubborn" |
| 14 | Action for tomorrow: pick three new words, set a timer for fifteen minutes | full-timeline panel (whole `infographic` crop) held 2 s static for the screenshot | headline: "Tomorrow: 3 words, 15 minutes" · sub: "Save this routine." |
| 15 | CTA + teaser | card | headline: "More ways to say *never give up*" · sub: "anotherwordfor.net · Next: why your mind goes blank" |

Notes for the builder / language editor:
- All chips for the five spin words are MY proposals; check them against dictionary labels, especially: tenacious (approving; formal?), relentless (often of unpleasant things: rain, pressure, criticism), obstinate (disapproving; formal), determined (neutral, approving), keep going (neutral phrase).
- Row 12 "Often about hard things" line is optional. Drop it if the editor finds it unhelpful at B1.
- Row 4 is an example of the recall step, not a quiz: no inserted pause, so the length stays inside 75 s. If the presenter turns it into a question ("very angry... what's the stronger word?"), a 1.5 s pause may be inserted before "livid".
- Captions come from the transcript. Set `fixes` for US spellings and for the domain ("another word for dot net" or a split domain -> anotherwordfor.net), and "15 minute routine" -> "15-minute routine".
- If the presenter adds content that is not in the script (numbers, days, apps, studies, website features, the page's other words), cut it at acoustic boundaries; do not re-voice.
- If the recording is still over 75 s after the cuts, trim filler first, then the "whatever you do" and "still running" scene tails, then point 2's "Do it once a day" (card 2 carries it), then shorten the pause to 2.0 s. Do not drop spin words (this episode has exactly 5), the "your turn" beat or the action. Never exceed 90 s; if it would, ask the user instead.
- Carousel spin-off (format plan feature F, nice-to-have): title + the three timeline panels + the CTA card, 1080x1350.
