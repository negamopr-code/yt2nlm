# S3 YouTube metadata gate v2 (content/youtube/s3.json vs s3-v2.mp4)

Gate: glottos-language-editor, headless autopilot step "special S3: yt_meta_gate", 2026-09-28 (UTC).
Upload file: content/specials/S3/s3-v2.mp4 (**439.00 s = 7:19**, 1280x720, 16:9, not a Short, private). sha256 a2f72389251f71a8dcc27903ae37a66ffdc831768594a00736149c4a74460cfd, 30831628 B. It is identical (same sha256) to /workspace/glottos-auto/out/specials/s3-v2.mp4.
Sources:
- Own faster-whisper small.en transcript of v2 (int8, cpu_threads=4, word timings, state/whisper-models, .nlmvenv): one full pass. Working files are in /tmp/s3m, outside the repo.
- PyAV frames at 5, 36.5, 332, 352, 380, 427 and 436.5 s, plus polish-v2-build/ladder_base.png (matches the rendered ladder at 380 s).
- critic-v2.md (SOLVES), lang-gate-v2-polish.md (APPROVED), script.md, meta.json.
- Link: curl https://anotherwordfor.net/another-word-for-big/ gives ssl_verify_result 10 (certificate expired). With -k it returns HTTP 200, and the page lists hefty, bulky, whopping, mammoth, considerable and jumbo.

meta.json was not changed. Nothing was uploaded. YouTube and NotebookLM were not touched.

## Verdict: APPROVED

## Table

| Line | Problem | Fix | Confidence |
|---|---|---|---|
| Title "Can You Remember 15 Synonyms for BIG? (Memory Challenge)" | none. 56 chars. It matches the 15 words (reveal 5:45, 15-row ladder) | unchanged | high |
| Hook "Ten words for BIG in a plain list, then one silly story... two scores" | none. Voice 0:00-0:15: "10 words for B-I-G", "a single, silly story", "Grab a pen, because you're getting two scores today" | unchanged | high |
| Steps 1-2 (list score / story score, "can recall, in order") | none. Voice 0:32-0:44 and 5:26-5:45; cards at 36.5 s ("Pause the video now...") and 332 s ("...In order.") | unchanged | high |
| Step 3 "surprise at the end, and the whole BIG ladder on one screen" | none. Reveal 5:45 "I gave you 15 words, not 10" plus the extras chips; "The BIG ladder" is one screen, 5:57-7:05 | unchanged | high |
| Step 4 "Comment your two scores: list versus story." | none. Spoken at 7:05 ("Comment your two scores, list versus story") and on the plate at 427 s | unchanged | high |
| Word order large ... ginormous | none. It matches the story onsets (0:58-5:05) and the ladder rows top-down | unchanged | high |
| "goes roughly from big to extremely big" | none. Voice 0:53 and 5:57; the ladder says "The order is a guide, not a rule." | unchanged | high |
| "you learn what it means and when to use it" | Overclaim. The WHEN cells for bulky ("a bulky box"), massive ("like a rock") and mammoth ("a mammoth task") hold an example or an image, not a usage label | "...what it means and, for most of them, when to use it:" (S2 precedent) | high |
| "for tall things" | "Very tall" is towering's meaning, not a use. The ladder's use label is "a bit literary: "towering trees"" | "...or when you want to sound a bit literary ("towering trees")" | high |
| "in formal English" | Stronger than the video, which says large is "a bit more formal than big" and considerable is "fairly formal" | "in more formal English" | high |
| (missing) whopping's use | The ladder shows "informal: often before a number"; the story says "a whopping 1200 kilos". Adding it makes the list match the ladder. It is phrased without "always", avoiding the spoken "almost always" (224 s) | added "before a number ("a whopping 1,200 kilos")" | high |
| "for sizes and amounts", "for money ("a hefty bill")", "for products ("a jumbo pack")", "for feelings ("immense relief")", "casual chat with friends (informal)" | none. These are the ladder's own labels (large, hefty, jumbo, immense, ginormous/jumbo/whopping/hefty) | unchanged | high |
| "Then try it with your own new words: one silly story, one picture for each word." | The voice at 7:10 starts with "Tonight, ..." (and so does the plate) | "Tonight, try it with your own new words: ..." (verbatim) | high |
| Link line 'For more words, look up "another word for big" on anotherwordfor.net: URL' | none. It matches the spoken CTA (7:15) and the plate "Look up: another word for big" with anotherwordfor.net (436.5 s). No promise of examples or a search box | unchanged | high |
| Tags (14) | none. 254 chars (267 with commas). Every term is in the video (huge, enormous, massive, vast, ginormous, hefty, bulky, whopping) | unchanged | high |
| Memory statistics | none in the description or the voice (no "most people", no numbers, no research) | none | high |

## Final description (as written to s3.json)
The paragraph that changed now reads: "For each word, you learn what it means and, for most of them, when to use it: for sizes and amounts, for money ("a hefty bill"), for products ("a jumbo pack"), before a number ("a whopping 1,200 kilos"), for feelings ("immense relief"), in more formal English, in casual chat with friends (informal), or when you want to sound a bit literary ("towering trees")." The transfer line now reads "Tonight, try it with your own new words: one silly story, one picture for each word." I re-read the whole description after both edits.

## Challenge beats in v2 (all present, in order)
1. Hook 0:00-0:15.
2. Plain list 0:21-0:31: vast, jumbo, huge, considerable, ginormous, large, massive, immense, giant, enormous.
3. Pause cue 0:32 with a 5.4 s hold, then "your list score" at 0:40.
4. Bridge 0:44-0:58, including "roughly from big to extremely big".
5. Story 0:58-5:25: 15 words, with a happy ending ("it's only a story").
6. Second pause 5:26 "in order", with a 3.6 s hold, the tip "walk through the story again", and "your story score".
7. Reveal 5:45 "15 words, not 10", with the extras chips (bulky, hefty, whopping, towering, mammoth).
8. Ladder 5:57-7:05, 15 rows, with a highlight that follows the voice.
9. Comment line, spoken and on a plate, at 7:05.
10. Transfer line 7:10: "Tonight, try it with your own new words. One silly story, one picture for each word."
11. CTA 7:15: "For more words, look up another word for big on anotherwordfor.net."

## Checks
- Title: 56 chars (limit 100). No < or > in the title, the description or the tags.
- Tags: 254 chars, 267 including commas (limit 500).
- Settings: privacy private, made_for_kids false, Education, en, no #Shorts, playlist "Synonym Memory Challenge".
- video_ids_local = specials/s3-v2 only. Format 7:19.

## Non-blocking (in the video, not fixable in metadata, none a false claim that contradicts the screen)
- whopping, 224 s: the voice says "it almost always sits right before a number". The card, the ladder and the recap say "often". This is a mild spoken overclaim, and the screen and the description carry the correct version.
- "Pause the explainer" (×2, 0:32 and 5:26). This is meta wording; both cards say "video".
- In the hook, "B-I-G" is spelled out. Whisper also heard "walk them in" (0:19, probably "lock them in") and "before and now" (3:04, 6:37, probably "before a noun"; the screen says "only before a noun"). None of these has been checked by a human ear.
- The whopping headword was heard as "Wapping" in the recap (6:40). The polish formant check accepted it. No human has listened to it.
- A 6-frame bulky-over-hefty picture flash at 119.05-119.30 s (critic-v2 minor 1). This is cosmetic.
- The title's "15" slightly spoils the reveal. This is kept per the runbook (same as S2).
- anotherwordfor.net: the **SSL certificate has expired**, so browsers will warn viewers who click the link. This is the known postponed P0, not a language issue. The user should know before publishing.
- Publisher: pin the comment "List: __ / Story: __".

## Not done
- shorts/lang_gate.py approve does not apply (s3.json has no "beats"). The approval was written by hand into s3.json "language_approval".
- No human listening; one whisper pass only. There were no isolated re-checks, because the timings and wording agree with critic-v2's independent transcript. Frames were sampled, not viewed in full.
- No WebSearch and no NotebookLM query. Every changed phrase copies a label already on screen and already dictionary-checked in lang-gate-v1.md.
- meta.json keeps the pre-generation description. s3.json is the upload file.
