# VISUALS: Words That Stick, Episode 4 "This is why you freeze mid-sentence" (NotebookLM infographic focus texts + draft unit plan)

> Language gate: approved 2026-09-27 by glottos-language-editor — pre-generation text gate (audio script, this file, content/youtube/ep04.json). Changes: panel 2 wall calendar removed (it invites dates/numbers, which the same focus forbids); unit-plan rows 4a/8/11/13 aligned with the fixed voice lines ("not when you only have one or two small tasks", "a neighbour carrying your heavy shopping", aid = "you hear it on the news, not in everyday chat", "write where it fits"); row 11 gains an avoid-when line so aid is never shown as an everyday spoken verb; builder note on quiz 1 resolved ("casual" kept: give sb a hand is an informal idiom, and the binary is formal vs casual); description aid/help lines fixed the same way. Register chips checked: give me a hand = casual, help = neutral · fine anywhere, support = neutral · common at work, assist = formal (Cambridge label), aid = formal · news and charities. Generation prompts use positive rules only (no forbidden tokens primed). CTA page verified (HTTP 200, plain word list); the article §5 site overclaim appears only in the do-not list below, never in a source or prompt. NOT yet checked: the generated audio/transcript, both infographic PNGs, the unit JSON (gate again after generation). Caption fixes the unit will need: neighbor->neighbour, favor/favorite->favour/favourite, color->colour, practice (verb)->practise, recognize->recognise, apologize->apologise, trucks->lorries (only where the presenter said "lorries"); "another word for dot net" or a split domain -> anotherwordfor.net; "15 minute" -> "15-minute"; "mid sentence" -> "mid-sentence".

Both infographics are generated LATER (visuals step), strictly in series, from the Ep04 AUDIO SCRIPT source only (`--source-ids <SRC04>`), so the synthesis's numbers, study names and app names stay out. Both images pass glottos-language-editor before rendering. Never ship a NotebookLM/Gemini watermark: the builder's crops drop the bottom strip.

Standing conventions for this episode:
- **Register labels are builder text only.** NotebookLM never prints casual / neutral / formal (Ep1 printed "Mild" over IRATE). Every register chip and avoid-when line on screen comes from the unit JSON, which the language editor gates.
- **Spelling:** British, channel-wide ("recognise", "practise", "neighbour", "colour"). NotebookLM and the transcriber tend to print US spellings, so check every image and caption ("neighbor" -> "neighbour").
- **Continuity:** Ep3 ends "Next: why you freeze mid-sentence", so the hook keeps that promise. Ep4 ends "Next: the 15-minute routine" (article §6). Callbacks: *swamped* (Ep2 quiz answer) and *livid* (Ep1 spin), each in one line.
- **Synonym spin = "help"**, page https://anotherwordfor.net/another-word-for-help/ (HTTP 200 on 2026-09-27; the page is a plain word list that includes aid, hand, helping hand, support and assist). The format plan's "I don't know" ladder has no page among the site's posts (no know/idk/unsure slug), so it was replaced. "Help" is the clearest register ladder on the site: *give me a hand* (casual) -> *help* (neutral) -> *support* (neutral, common at work) -> *assist* (formal) -> *aid* (formal, news and charities), and every one has a concrete picture. They are "5 ways to say help", each for a different setting, NOT strict synonyms. ("Give me a hand" uses the page's "hand".)
- The quiz answers ("casual", "formal") must NEVER be printed on any infographic. The builder renders the quiz as its own cards.

## 1. Main infographic: `state/nlm-raw/ep04-infographic.png` (unit key `infographic`, panels `title+1`, `2`, `3`, `4`)

Command flags: `infographic create <NB> --orientation portrait --style instructional --detail concise --language en --source-ids <SRC04>`

Focus text (exact):

> Portrait infographic with exactly 4 panels stacked from top to bottom, separated by clear white gaps. Big, simple pictures and very few words. Title exactly: 'Why you freeze mid-sentence'.
> Panel 1 (the hook, a picture): a person talking to a colleague, stopped in the middle of a sentence with an open mouth and a worried face. Above the person, exactly three thought bubbles that contain exactly 'Too formal?', 'Too rude?' and 'Too dramatic?'. No other text on this panel.
> Panel 2: a tired person at an office desk behind tall piles of reports and papers. Text exactly: 'swamped'.
> Panel 3: a woman standing at the open door of a flat, red-faced and furious, talking to her landlord, who is holding an envelope. Text exactly: 'livid'.
> Panel 4: a meeting table; a manager asks a question and a person makes a note on a laptop. Text exactly: 'let me look into that'.
> Each panel's text sits in its own strip under the picture, never on top of the picture. Print no other text: no labels about tone or style, no example sentences, no numbers, no names, no arrows, no logos. Check the spelling of every word.

Fallback: if NotebookLM merges panels or draws fewer than 4, rerun once with the same focus. If panel 1 is still missing its three bubbles, the builder shows the hook as a text card over panel 1 and puts the three questions on the card.

## 2. Synonym picture sheet: `state/nlm-raw/ep04-synonyms-infographic.png` (unit key `extra_infographics.syn`, `split: {"syn": "bands"}`)

Five stacked full-width cards (Ep2/Ep3 layout, so each crop is large). The phrase sits in its OWN strip under the picture, so the visuals step can also cut a picture-only (phrase-hidden) crop for the quiz questions.

Command flags: `infographic create <NB> --orientation portrait --style instructional --detail concise --language en --source-ids <SRC04>` (fallback if the cards touch or the strip sits inside the picture: rerun with the same focus and `--style bento_grid`).

Focus text (exact):

> Portrait picture sheet. Title exactly: '5 ways to say help'. Exactly 5 cards stacked in ONE column from top to bottom, each card the full width of the page, on a white background with clear white gaps between the cards. Each card = one large picture on top and, underneath it, a separate solid dark strip that contains ONLY the words given here, in large white letters. The words are never inside the picture and never on top of the picture. Nothing else is written on the card. In this order:
> 1 'give me a hand': two young friends in T-shirts carrying a big sofa up a narrow staircase, one at each end, laughing.
> 2 'help': a friendly neighbour carrying an older woman's heavy shopping bags up the steps to her front door.
> 3 'support': an IT worker with a lanyard sitting next to an office worker, fixing her laptop at her desk.
> 4 'assist': a smiling hotel receptionist in a smart uniform behind a reception desk, greeting a guest with a suitcase.
> 5 'aid': lorries unloading boxes of food and bottled water in a flooded village, volunteers carrying the boxes.
> Print NO labels on the cards: nothing about tone, style, setting or strength. No scales, arrows, rankings, numbers, scores, example sentences or speech bubbles. No text anywhere except the title and the 5 phrases. Check the spelling of every word.

## 3. Do-not-say / do-not-print list (voice, captions, cards, images; the builder cuts any of these from the recording)
- Podcast markers: "this is the brief", "debrief", "welcome", "today we", "in this episode", "let's dive in", "let's break it down", "listeners", "you're listening", "podcast", "show", "episode", "host", "video", "deep dive", any sign-off ("that's it", "thanks for listening", "see you next time", "until next time").
- Sources and science: names, universities, years, "a study", "researchers", "scientists", "science says", "proven", "your brain is wired". Register is a usage fact, not a study result. No percentages; the article's "about 75% within a week" belongs to Ep1, never here.
- Numbers: none except "one or two" (tasks), "five/5" (spin) and "15" (teaser). No rule number ("Rule 4" is article numbering; on screen it is "The rule:").
- Spin: never "synonyms of help", "means the same", "same meaning". Never "Can you aid me?" or "assist me, mate" style mixes as advice. Never call "support" formal or casual on its own (it is neutral; chip = "neutral · common at work").
- Register claims beyond the script: never call "swamped" rude or slang; never call "livid" rude; never say "let me look into that" is wrong, only that it doesn't suit chats with friends. Never say "help" is informal.
- The old format plan's phrases ("Beats me", "Your guess is as good as mine", "I'm afraid I don't have that information") are NOT in this episode; cut them if the presenter improvises them.
- CTA: never "search", "search for", "type in", "sites like", "websites like"; never claim the site has pictures, example sentences, register notes, avoid-when notes, quizzes, audio or an app (the help page is a plain word list). The article's §5 sentence "every word on anotherwordfor.net comes with an example sentence and a note on when to use it" must NOT be voiced or printed.
- Filler: "literally", "basically", "honestly", "super", "amazing", "game-changer", "hack", "trick", "secret".
- Teaser: only "Next: the 15-minute routine." Never a different next topic, never "next time".

## 4. Draft unit plan (NOT a unit JSON yet)
The beats are timed later from the real recording, and the order follows what the presenter actually says. Planned unit id: `words-that-stick-ep04-v1` (file `shorts/units/ep04_v1.json`), series "Words That Stick", episode 4, `script` = `content/articles/p01-ep04-audio-script.md`, `visuals` = this file, `infographic` = `state/nlm-raw/ep04-infographic.png`, `extra_infographics.syn` = `state/nlm-raw/ep04-synonyms-infographic.png`, `split: {"syn": "bands"}`, audio = the NotebookLM brief overview slowed to 0.9x (`state/nlm-raw/ep04-podcast-brief-0.9.mp3` + `.words.json`), with `cuts`/`pauses`/`fixes` set after transcription. Target 60-75 s after cuts and pauses (spoken script ≈170 words + 2 quiz pauses of 2.0 s).

| # | Talking point | Visual | Builder text (cards / quiz) |
|---|---|---|---|
| 1 | Hook: this is why you freeze mid-sentence (≤4 s) | panel `title+1` (speaker + 3 doubt bubbles) | none (picture hook) |
| 2 | You didn't forget the word; you're not sure it fits. Too formal? Too rude? Too dramatic? | panel `title+1` held (bubbles) | card over the tail: headline "You didn't forget it." · sub "You're not sure it *fits*." |
| 3 | Learn each word's setting, and when to avoid it | card | headline: "Learn the *setting*" · sub: "…and when to avoid the word" |
| 4a | Swamped: fine at work, but not when you only have one or two small tasks | panel `2` above a tag card | tag: **swamped** · chip "casual to professional" · "Avoid when: you only have one or two small tasks" |
| 4b | Livid: too dramatic for someone slightly annoyed | panel `3` above a tag card | tag: **livid** · chip "neutral, a bit dramatic" · "Avoid when: someone is just slightly annoyed" |
| 5 | Let me look into that: emails and meetings, not chats with friends | panel `4` above a tag card | tag: **let me look into that** · chip "professional" · "Avoid when: chatting with friends" |
| 6 | Five ways to say help, casual to formal | `syn` title band, or a card | headline: "5 ways to say *help*" · sub: "casual → formal" |
| 7 | QUIZ 1: friends moving a sofa, "Can you give me a hand?" | quiz beat: picture-only crop of `syn:1` if cut, else card | q: "Can you give me a hand?" · q_sub: "Formal or casual?" (two pill buttons) · pause 2.0 s with countdown · reveal: `syn:1` + chip "casual" (reveal_at = start of the spoken answer) |
| 8 | A neighbour carrying your heavy shopping: help, fine anywhere | `syn:2` | chip "neutral · fine anywhere" |
| 9 | IT team fixing your laptop: support | `syn:3` | chip "neutral · common at work" |
| 10 | QUIZ 2: hotel receptionist, "How may I assist you?" → formal; with friends it sounds stiff | quiz beat: picture-only crop of `syn:4` if cut, else card | q: "How may I assist you?" · q_sub: "Formal or casual?" · pause 2.0 s · reveal: `syn:4` + chip "formal" + "Avoid when: talking to friends (sounds stiff)" |
| 11 | Lorries bringing food after a flood: that's aid; you hear it on the news, not in everyday chat | `syn:5` | chip "formal · news and charities" + "Avoid when: asking a friend for help" |
| 12 | Rule: learn the setting, not just the meaning | card, held 2 s static for the screenshot | headline: "The rule: learn the *setting*" · sub: "not just the meaning. Screenshot this." |
| 13 | Action for tomorrow: next to each new word, write where it fits: friends, work, or both | card | headline: "Tomorrow: tag each new word" · sub: "friends · work · both" |
| 14 | CTA + teaser | card | headline: "Look up *another word for help*" · sub: "anotherwordfor.net · Next: the 15-minute routine" |

Notes for the builder / language editor:
- All register chips and avoid-when lines for the five "help" phrases are MY proposals (only swamped / livid / let me look into that are sourced, from article §5). Check against dictionary labels, especially: "give sb a hand" (informal?), "assist" (formal), "aid" as a verb/noun (formal), "support" (neutral).
- Quiz answers must be unambiguous: "Can you give me a hand?" is used at work among colleagues too, so the question is "Formal or casual?" (answer: casual), NOT "Friends or work?". Language editor 2026-09-27: "casual" is kept (give sb a hand is an informal idiom; against "formal" the answer is unambiguous).
- Captions come from the transcript. Set `fixes` for US spellings ("neighbor" -> "neighbour") and for the domain ("another word for dot net" or a split domain -> anotherwordfor.net).
- If the presenter adds content that is not in the script (numbers, studies, the old "I don't know" phrases, website features), cut it at acoustic boundaries; do not re-voice.
- If the recording is still over 75 s after the cuts, trim filler first, then the "You hear it on the news, not in everyday chat" tail and the "Fine anywhere" tail (their chips carry the same information). Do not drop spin words (5-10 per episode; this episode has exactly 5) or quizzes. Ask the user instead.
