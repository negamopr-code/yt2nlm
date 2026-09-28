# VISUALS: Words That Stick, Episode 2 "Stop re-reading your word list" (NotebookLM infographic focus texts)

Both infographics are generated LATER (visuals step), strictly in series, from the Ep02 AUDIO SCRIPT source only (`--source-ids <SRC02>`). This keeps the synthesis's "4x" / "70%" numbers out. Both images pass glottos-language-editor before rendering. Never ship a NotebookLM/Gemini watermark: the builder's crops drop the bottom strip.

The quiz answers (swamped, crucial, urgent) must NEVER be printed on the main infographic. The builder renders the quiz as its own cards.

## 1. Main infographic: `state/nlm-raw/ep02-infographic.png` (unit key `infographic`, panels `title+1`, `2`, `3`, `4`)

Command flags: `infographic create <NB> --orientation portrait --style instructional --detail concise --language en --source-ids <SRC02>`

Focus text (exact):

> Portrait infographic with exactly 4 panels stacked from top to bottom, separated by clear white gaps. Big, simple pictures and very few words. Title exactly: 'Stop re-reading your word list'.
> Panel 1 (the hook, a picture): a tired learner at a desk reading the same notebook page of words again, while the words float out of their head and fade away like smoke. One line of large text on this panel, exactly: 'You re-read it. Then it's gone.'
> Panel 2 (two pictures side by side): LEFT, a person looking at a word on a page and nodding, labelled exactly 'Recognise' with the small line exactly 'Oh yes, I know that one.' RIGHT, a person talking to a friend, with an empty thought bubble above their head, labelled exactly 'Recall' with the small line exactly 'What's the word for...?'
> Panel 3 (two bars side by side): one short bar labelled exactly 'Re-read' with 'about 40%', and one taller bar labelled exactly 'Practised recall' with 'about 61%'. One caption under the bars, exactly: 'Remembered one week later. Same study time.'
> Panel 4 (a picture): a hand covering the right half of a two-column list on paper. The left column shows exactly 'very busy' and 'very important'. The right column is hidden under a blank card with NOTHING written on it.
> Print no other text, labels, numbers, dates, names, study names or university names. Never print the words 'words', 'vocabulary', 'neural', 'brain science', '4x', '70%', 'useless', 'proven', 'research' or 'scientists'. (The caption's 'study time' is the only allowed use of 'study'.) Never print any of these answer words anywhere: swamped, crucial, urgent, vital, essential, thrilled, livid, exhausted. No arrows, no logos. Check the spelling of every word.

## 2. Synonym picture sheet: `state/nlm-raw/ep02-synonyms-infographic.png` (unit key `extra_infographics.syn`, `split: {"syn": "bands"}`)

Four stacked full-width cards, so each crop is large; the Ep1 review found the pair bands used only about a third of the frame. The word sits in its OWN strip under the picture, so the visuals step can also cut a picture-only (word-hidden) crop.

Command flags: `infographic create <NB> --orientation portrait --style instructional --detail concise --language en --source-ids <SRC02>` (fallback if the cards touch or the strip sits inside the picture: rerun with the same focus and `--style bento_grid`).

Focus text (exact):

> Portrait picture sheet. Title exactly: 'Very important: 4 pictures'. Exactly 4 cards stacked in ONE column from top to bottom, each card the full width of the page, on a white background with clear white gaps between the cards. Each card = one large picture on top and, underneath it, a separate solid dark strip that contains ONLY the one word given here, in large white letters. The word is never inside the picture and never on top of the picture. Nothing else is written on the card. In this order:
> 1 'crucial': a football player about to take a penalty kick at the end of a match, the goalkeeper ready, the whole crowd holding its breath.
> 2 'vital': a scuba diver underwater checking the air tank on their back, bubbles rising.
> 3 'essential': an open suitcase on a bed, and a hand putting a passport on top of the clothes.
> 4 'urgent': a kitchen with a burst pipe spraying water across the floor, a person rushing in with a toolbox.
> Print NO labels on the cards such as mild, strong, formal, informal, casual, British, American, positive, negative, very important. No scales, arrows, rankings, numbers, scores, scoreboards, clocks, example sentences or speech bubbles. No text anywhere except the title and the 4 words. Check the spelling of every word.

## Checks for the visuals step and the language editor
- The main sheet has exactly 4 panels: `title+1` = picture hook + 'You re-read it. Then it's gone.' This is the FIRST frame of the Short (review lesson: the hook is a picture plus pain text, never a text-only card).
- Bars: 'about 40%' / 'about 61%' only; the caption must not turn them into "% of words".
- The sheet's 4 words are spelled exactly crucial / vital / essential / urgent, and each word is in a strip BELOW its picture. The urgent picture must be word-hideable: beat 11 shows the question card first and reveals `syn:4` on the answer word.
- No answer word on the main sheet. Reject and regenerate if 'swamped', 'crucial' or 'urgent' appear there.
