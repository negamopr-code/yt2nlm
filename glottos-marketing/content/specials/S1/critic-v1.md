# S1 critic review, s1-v1.mp4 (Synonym Memory Challenge: HAPPY, P01, 16:9 NotebookLM whiteboard, 7:10)

Reviewer: glottos viewer-critic (headless autopilot step "special S1: critic"), 2026-09-28.
Watched as: a B1 to B2 learner who forgets new words and knows only "happy" when speaking.
Method: 3 contact sheets (one frame every 5 s, 86 frames), full-resolution frames at 0.7, 1.5, 8, 12, 20, 32, 70, 140, 208, 265, 300, 312, 325, 342, 355, 380, 422, 426 and 428 s, a watermark crop, a scene-change list (threshold 0.2), and an ffmpeg silencedetect map (-35 dB, 0.8 s). Audio transcribed with faster-whisper small.en (int8, cpu_threads=4, word timings). The references were script.md, focus.txt, meta.json, the S1 to S5 runbook in docs/autopilot.md, and state/glottos-methods/P01/strategy.md plus proof_doc.md. NotebookLM was not touched. Nothing was rendered, uploaded or changed.

## Verdict: PARTLY

The voice is very good. All six beats survived NotebookLM's retelling in the right order. All 15 story words come in exactly the script's mildest-to-strongest order, each acted out with a correct meaning. The "15, not 10" reveal and the comment-your-two-scores CTA are both there. But the video cannot ship as it is, for three reasons:
1. The one screen a learner would screenshot, the ladder recap table, is wrong. "Elated" appears twice, "Ecstatic" sits in row 5 next to "Thrilled" instead of at the top, the meaning cell for Jubilant is empty, and it uses the non-words "Uncontained" and "Joyous".
2. The two pause cues have almost no pause: 0.9 s and 0.5 s.
3. There is a "Gemini Notebook" watermark on every frame, plus a Gemini end card.

All three can be fixed in post. **No regeneration is needed.**

## Pain in the learner's words

Verbatim, from the P01 research (proof_doc.md, comments/0nFkQ4cQhME.jsonl, strategy.md), with no names:
- "I've been trying to cram too many words and always forget them."
- "I forget every new word so of this works for me it will be life changing"
- "I also find myself forgetting certain English words when I'm speaking."
- "I reviewed but kept forgetting the words."
- "That's called mnemonics. Really helps you learn languages, specifically vocabulary, where you can associate some bonkers, vivid and chaotic story with a meaning and a pronunciation of a word."
- Score comments on the source method's video: "7 verbal, 15 visual. Just wow!" and "I tried it and it worked, from scoring 4/10 to 10/10."

In one sentence: "I learn words like *elated* or *thrilled*, forget them in days, and when I speak I only say *happy*."

Solved means that tomorrow I can recall more of these words than from a list, and I know which one fits: *delighted* in an email, *chuffed* only with friends, *jubilant* when I read the news. I can also use the same silly-story trick for my own word groups.

## Beat survival (task item 1): all beats present and IN ORDER. No beats dropped or scrambled.

| # | Required beat | Heard (whisper) | On screen | Result |
|---|---|---|---|---|
| 1 | Hook ≤15 s, promise | 0:00.0 to 0:10.8: "10 words for happy. How many can you actually remember? We're gonna do a quick test, then I'll show you a trick, a single, silly visual story, and then test you again. You're getting two scores today, so grab a pen." | 0:00 to 0:11.3 title card "Synonym Challenge: HAPPY" with a doodle (10 WORDS scroll, rocket, moon) | OK, 10.8 s. The script's "you'll also learn when to use each word" was dropped, and the "Score 1 / Score 2" card was not drawn. Minor. |
| 2 | Plain list of 10, about 2 s each | 0:11.6 "First up is the **playlist** [probably "plain list", ear check]. I want you to just read and listen to this **stark baseline test**." 0:17.1 to 0:29.9 the 10 words in the script's order, about 1.3 s each | 0:11.3 to 0:30.7: all 10 words at once in speech bubbles around a boy at a desk. No meanings, no word pictures, correct order. | OK in order and content. They are shown all at once rather than one by one, which is acceptable because the viewer still gets only a plain list. |
| 2b | Spoken pause cue | 0:31.1 "Pause the video now. Write down every word you remember." 0:34.6 "Okay, got them? Count them up. That is your first score. Your list score. Hold onto that." | 0:30.7 to 0:41.1 card "Pause now. Write down every word you remember to get your list score." with a pause icon | The cue is present, **but the silent hold is only 0.9 s** (33.68 to 34.58). The script asked for 3 s. Anyone who doesn't hit pause hears "got them?" immediately. |
| 3 | ONE continuous story, 15 words, mildest to strongest | content 1:01.6, glad 1:17.4, pleased 1:35.2, chuffed 1:51.8, cheerful 2:11.2, upbeat 2:27.1, joyful 2:43.2, delighted 3:01.8, thrilled 3:20.5, over the moon 3:37.7, overjoyed 3:57.0, on cloud nine 4:12.7, elated 4:30.9, jubilant 4:45.4, ecstatic 5:02.2 | One slide per word, each with a blue caption card (word plus a one-line meaning). The scene changes line up with the words (77.1, 94.8, 111.5, 131.0, 146.6, 162.7, 181.3, 200.4, 217.5, 236.5, 252.3, 270.6, 285.0, 302.0). | **Exact order, nothing merged or skipped.** One story with continuity (hammock, cows, ducks, rocket, cloud, stadium). The picture is a series of separate slides, not one growing drawing (see the defects). |
| 4 | Second pause (recall in order) | 5:18.6 "Pause the video again. Write down every word you can recall, in order. A quick tip here..." 5:29.8 "Got them? ... That is score number two, your story score." | 5:18.4 to 5:34.7 card "Pause again. Write down every word you recall from the story, in order." | The cue is present, **but the silent hold is only 0.5 s** (322.04 to 322.56) before "A quick tip here". |
| 5 | Reveal "15 not 10" plus ladder recap | 5:34.9 "I gave you 15 words, not 10. The extras were chuffed, upbeat, joyful, on cloud nine, and jubilant..." 5:53.2 to 6:55.9 spoken recap of all 15 | 5:34.7 to 5:53.1 card "The sneaky extras were:" with the 5 words on leaves (correct). 5:53.1 to 6:56.5 **one ladder table, which has errors** (see below) | Beat present. The voice is correct. The table is wrong. The voice groups the two idioms before overjoyed (a small reorder in the recap only). |
| 6 | Comment two scores plus site | 6:56.6 "So what does this all mean for your memory? Comment your two scores. List versus story. For more words, look up another word for happy on anotherwordfor.net." (ends 7:05.9) | 6:56.5 to 7:06.6 card "Share your two scores! For more, look up another word for happy on anotherwordfor.net." | OK. It makes no promise of examples or a search box. The first sentence is a dangling filler question. |
| - | End | - | **7:06.6 to 7:09.7: full-screen "Gemini Notebook" end card** | Brand violation |

**Beats dropped or scrambled: NO.** The runbook's "ask_user about our own renderer" trigger (dropped or scrambled twice) does **not** apply.

## Accuracy for B1 (task item 2)

Story voice-over, word by word (meaning and register as heard):
- content: "quietly satisfied, you don't want anything else". Correct. The con-TENT stress cue became "Say it with me. Content." **Ear check needed**: if it is said as CON-tent (the noun), this is a pronunciation error on the first story word.
- glad: "happy about one particular thing, often with a real sense of relief". Correct.
- pleased: "happy and satisfied with how something turned out". Correct.
- chuffed: "British and informal ... pleased, especially about something you pulled off yourself". Correct. ("pulled off" is B2 but clear from the scene.)
- cheerful: "happy in a way that everyone around you can clearly see and hear". Correct.
- upbeat: "staying positive and hopeful even when something goes wrong". Correct, and the scene flavour is fine.
- joyful: "full of joy ... music, celebrations, and you'll see it quite a bit in writing". Correct.
- delighted: "very pleased, usually about a gift, an invitation, or some really good news". Correct.
- thrilled: "very happy and very excited at the exact same time". Correct.
- over the moon: "a great, informal idiom that means extremely happy, usually about receiving some fantastic news". Correct. Whisper hears "You **pass** your exam" (3:46.6), which should be "passed" (ear check).
- overjoyed: "extremely happy ... about some news or an event that just happened". Correct.
- on cloud nine: "another informal phrase ... extremely happy, practically like you're floating on a cloud". Correct. The invented "for a long time" did not come back.
- elated: "extremely happy and excited, usually after a big success". Correct.
- jubilant: "very happy and celebrating, especially after a big win". Correct.
- ecstatic: "so intensely happy you can hardly even contain it". Correct.

Recap voice (5:53 to 6:56). Mostly right, with small overstatements (none are ship-blocking):
- "Joyful is **heavily** used in writing" (6:23). The script says "more common in writing". This is an overstatement.
- "Jubilant is **almost entirely** written" (6:47). The script says "mostly written". This is an overstatement.
- glad: "when you're relieved about one specific thing". This narrows glad to relief (the story said "often"). chuffed: "when you're proud of yourself" (narrowed). Over the moon and on cloud nine are "both **very** informal" (slightly strong). All are acceptable for B1.
- The register calls are correct: chuffed British and informal, over the moon and on cloud nine informal, delighted "a safe bet for polite emails", pleased "neutral, perfect for work", jubilant and elated written. Nothing calls jubilant or elated casual, and nothing says chuffed is fine in formal writing.

Memory claims: **clean.** There are no statistics, no "most people", no "10x", no researchers, and no age of the method. "they came entirely from that visual story trick" (5:47) is only about the viewer's own extras, which is fine.

NotebookLM additions (not in the script):

| Time | Line (heard) | Problem | Clean cut? |
|---|---|---|---|
| 0:11.6 | "First up is the playlist." | Probably "plain list" misheard (ear check). If it really says "playlist", it is wrong. | Only together with the next line |
| 0:13.3 to 0:16.7 | "I want you to just read and listen to this stark baseline test." | "stark baseline test" is unnatural and above B1 | Yes. Cut 13.2 to 16.9 (gaps 12.66 to 13.30 and 16.66 to 17.10) |
| 0:35.1 | "Okay, got him?" | whisper hears "got him", which is likely "got 'em" (ear check) | Leave |
| 0:41.3 to 0:42.7 | "Right, let's dive into the trick." | "dive into" filler (same family as the banned "let's dive in") | Yes. Cut 41.2 to 43.2 |
| 0:46.2 to 0:50.2 | "We're gonna build one continuous whiteboard drawing that grows from left to right." | The narrator reads our stage direction, and **the picture contradicts it** (separate slides) | Yes. Cut 45.9 to 50.5 |
| various | "literally" ×6 (2:19, 2:56, 3:28, 4:20, 5:06, 6:54) | intensifier habit. Harmless but noisy. | No (mid-sentence) |
| 5:53.2 | "Let's look at the whole shebang on this ladder" | slang a B1 viewer won't know | No (mid-sentence), low risk |
| 6:56.6 to 6:58.5 | "So what does this all mean for your memory?" | dangling question that is never answered | Yes. Cut 416.5 to 419.0 |

## On-screen text, numbering, watermark (task item 3)

- **Ladder table (5:53.1 to 6:56.5, held for about 63 s, the screenshot screen). SHIP-BLOCKING.** The rows are pairs that do not match the ladder:
  - "Overjoyed / Elated" and "On cloud nine / **Elated**": **Elated appears twice.**
  - "Thrilled / **Ecstatic**" is in row 5 with "Excited / **Uncontained**" / "Everyday / The top". Ecstatic is moved from the top to the middle of the ladder while the voice says "right at the top, ecstatic". "Uncontained" is not a natural meaning label.
  - "Joyful / Delighted" is glossed "**Joyous** / Very pleased". Joyous is a circular gloss and a harder word than the one it explains.
  - "Jubilant": **the Meaning cell is empty** (covered by the crowd drawing).
  - "Cheerful / Upbeat" gets the register "Everyday / Moods". "Moods" is not a register. Chuffed has no "British" label (only a UK-flag icon).
  - The row icons are misaligned (a shocked face next to "Over the moon", a moon next to "Overjoyed / Elated").
  - A learner who copies this table learns wrong pairings and loses where ecstatic sits.
- Story cards: there are **no pictures for cheerful (2:11 to 2:26) and thrilled (3:20 to 3:37)**. The blue caption card covers everything, and only faded ghost art remains. So the "acted out" scene for 2 of the 15 words is only heard, never seen. Non-blocking, but it weakens the method (the whole point is the image).
- Legibility: the content caption (1:01 to 1:17) is white text on a light picture, with low contrast. The on cloud nine definition "as if you are floating on a cloud" is partly covered by the cloud (4:12 to 4:30). The joyful caption has drawing strokes over "Full of joy". "The sneaky extras were:" is crossed by the fox's ear. All are readable, but none is clean.
- Typos: none in the card text itself. The list bubbles have "Content" without a comma (trivial).
- Numbering: the video has no on-screen step or word numbers, so there is no voice/number mismatch. The "15" and "10" in the voice match the reveal card.
- **Watermark: "Gemini Notebook" is in the bottom-right corner of EVERY frame** (about x 1155 to 1275, y 697 to 713 at 1280x720). **Full-screen "Gemini Notebook" end card from 7:06.58 to 7:09.7.** Brand violation, ship-blocking.

## Second by second: where a viewer would swipe away

- 0:00 to 0:11: the audio hook is strong and personal ("How many can you actually remember?"). The picture is a static generic title card. It is fine for 16:9, but it does not show "Score 1 / Score 2".
- 0:11 to 0:17: "playlist ... stark baseline test". This is the first confusing moment for a B1 ear.
- 0:17 to 0:30: the list. It is good and fast. All 10 words stay readable on screen.
- 0:31 to 0:34: **the pause cue has no pause.** A scroller who didn't reach for the pause button has no time to write, so score 1 is not collected. Where comments come from, this is the biggest engagement leak.
- 0:41 to 1:01: 20 s of set-up talk before the first story word ("dive into", the continuous-drawing claim, "vividly imagine"). This is the likeliest early drop point.
- 1:01 to 5:18: the story at about 16 to 20 s per word. The voice is vivid and funny (cow knitting a scarf, duck band, seagull stealing a sandwich). The pacing is steady, maybe one sentence too long per word, but the continuing plot pulls you along. The blank cheerful and thrilled cards are dull spots.
- 5:18 to 5:22: second pause, again with no hold (0.5 s).
- 5:35 to 5:53: the reveal is a nice "aha" moment and the card is correct.
- 5:53 to 6:56: 63 s on one static table while the voice goes word by word. It is slow, and the table disagrees with the voice.
- 6:56 to 7:06: the CTA is clear. 7:06 to 7:10: Gemini end card.

## Takeaway test

After watching I can: use *delighted* in a polite email ("I'd be delighted to help" is not spoken, but "a safe bet for polite emails" is), keep *chuffed* and *over the moon* for friends, recognise *jubilant* and *elated* in the news, and compare my two scores. That is a real, nameable action for these 15 words. **Gap:** the video never says "do this with your own new words tomorrow". The method transfer to my own forgetting problem (the P01 pain) is only implied. This is non-blocking. Consider it for S2 to S5 (scenario-writer).

## Retention risks

- Length 7:10 (7:06 after trimming the end card) is at the top of the 5 to 7 min target. The story beat carries it.
- The weak spots are the 20 s set-up (0:41 to 1:01) and the 63 s static table (5:53 to 6:56).
- The picture and voice are in sync for every story word (the scene changes land within 0.5 s of each word). They are out of sync only for the "continuous drawing" claim and the ladder table.

## Trust risks

- The ladder table contradicts the voice ("ecstatic at the top" is in row 5, and "elated" is shown twice). An attentive viewer will comment on it.
- The Gemini watermark and end card mark the video as AI-generated from a notebook and break the brand rule.
- "heavily used in writing" / "almost entirely written" are small register overstatements. The corrected table can carry the accurate labels.

## Defects and fixes

### Ship-blocking (all can be fixed in post, no regeneration)

1. **Brand watermark plus end card (shorts-builder).** Trim at **426.5 s** (the CTA audio ends at 425.90, and the end card starts at 426.58). Cover the bottom-right "Gemini Notebook" mark on every frame with the official logo `state/brand/awf-logo-channel.jpg` or a background-matched patch.
2. **Wrong ladder table, 353.1 to 416.5 s (visuals, then shorts-builder, then a language-editor re-gate).** Put a full-frame overlay of our own 15-row ladder over this span, in the script's order (content at the bottom, ecstatic at the top), with word · one-line meaning · register/when, taken from script.md Beat 5 ("Chuffed: British, informal", "Joyful: more common in writing", "Jubilant: mostly written"...). It must include no pairs, no "Uncontained", no "Joyous", and no duplicate Elated. Patching single cells is not enough (the pairing itself is the error).
3. **Pause holds (shorts-builder).** Insert a silent **3 s freeze** of the pause card at **33.7 s** (after "remember.") and at **322.1 s** (after "in order."). That is +6 s in total.

### Non-blocking (recommended, in post)

4. Filler cuts (shorts-builder, then language-editor): 13.2 to 16.9 ("stark baseline test"), 41.2 to 43.2 ("let's dive into the trick"), 45.9 to 50.5 (the continuous-drawing claim that the picture contradicts), 416.5 to 419.0 ("So what does this all mean for your memory?"). About 11 s saved, which offsets the pause freezes.
5. Missing scene art for cheerful (131.0 to 146.6) and thrilled (200.4 to 217.5) (visuals). Add a drawn panel beside the caption card (whistling walker waving at a lamppost; jumping and punching the air with a rocket ticket). Optional, but it strengthens the method.
6. Legibility patches (visuals): a darker scrim under the content caption (61 to 77), and cover or re-set the on cloud nine definition line (252 to 270).
7. Ear checks (a human, or the language-editor with the audio): "playlist" at 0:12.4, the stress of "content" at 1:01.6 and 1:03.8 (it must be con-TENT; if it is CON-tent, re-voicing is needed, which is a voice fix, not NotebookLM), "got him" at 0:35.1, "pass" at 3:46.6.
8. For S2 to S5 (scenario-writer, focus.txt): add "Tell the viewer to do the same with their own new words tomorrow", "Do not read stage directions aloud", and "Recap table: one row per word, no pairs" to focus.txt. Also ask for real silent holds on the pause cards. Those are likely to be ignored by NotebookLM again, so plan for them in post.

After fixes 1 to 3 (ideally with 4), this should reach **SOLVES**. Re-run the critic on the rebuilt file.

## Not checked

- No human listening. Stress on "content" and the words "playlist", "got him" and "pass" are whisper small.en readings.
- Frames were sampled every 5 s plus at every scene change. A defect lasting less than about 3 s between samples could be missed.
- meta.json was not re-audited (gated by the language-editor at 22:59Z). The title "How to Remember 15 Synonyms..." spoils the "15, not 10" reveal slightly, as the editor already noted.
