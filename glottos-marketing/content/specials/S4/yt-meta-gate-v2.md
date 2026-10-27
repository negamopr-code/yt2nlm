# S4 YouTube metadata gate v2 (content/youtube/s4.json vs s4-v2.mp4)

Gate: glottos-language-editor, headless autopilot step "special S4: yt_meta_gate", 2026-09-29 (UTC). Approval stamp: 2026-09-29T05:49:57Z.
Upload file: content/specials/S4/s4-v2.mp4 (**413.29 s = 6:53**, 1280x720, 16:9, not a Short, private). sha256 2bdbc85d2578063199e6ad12453a51b95c38a0b6f66bbb7b6351b28a5083510d, 30107062 B. It is identical (same sha256) to /workspace/glottos-auto/out/specials/s4-v2.mp4.
Sources:
- Own faster-whisper small.en transcript of v2 (int8, cpu_threads=4, word timings, state/whisper-models, .nlmvenv, run with nice): one full pass. Working files are in /tmp/s4m, outside the repo.
- PyAV frames at 5, 20, 33, 70, 97, 150, 207, 237, 252, 280, 290, 302, 318, 361, 401 and 411 s. The ladder frame (361 s) matches polish-v2-build/ladder_base.png.
- critic-v2.md (SOLVES), lang-gate-v2-polish.md (APPROVED), script.md (Beats 4-6), meta.json.
- Link: curl https://anotherwordfor.net/another-word-for-beautiful/ gives ssl_verify_result 10 (certificate expired). With -k it returns HTTP 200, and the page lists exquisite, gorgeous, graceful, radiant and stunning.

meta.json was not changed. Nothing was uploaded. YouTube, NotebookLM and state/autopilot.json were not touched.

## Verdict: APPROVED

## Table

| Line | Problem | Fix | Confidence |
|---|---|---|---|
| Title "Can You Remember 15 Synonyms for BEAUTIFUL? (Memory Challenge)" | none. 62 chars. It matches the 15 words (reveal 5:13, 15-row ladder) | unchanged | high |
| Hook "Ten words for BEAUTIFUL in a plain list, then one silly story... two scores" | none. Voice 0:00-0:11: "Ten words for beautiful", "a single silly story", "Grab a pen because you're getting two scores today" | unchanged | high |
| Steps 1-2 (list score / story score, "can recall, in order") | none. Voice 0:27-0:40 and 4:58-5:12; cards at 33 s and 302 s ("...every word you can recall in order...") | unchanged | high |
| Step 3 "surprise at the end, and the whole BEAUTIFUL ladder on one screen" | none. Reveal 5:13 "I gave you 15 words, not 10" plus the extras chips; voice 5:24 "Here's the entire ladder on one screen"; one full-frame 15-row table 5:24-6:38 | unchanged | high |
| Step 4 "Comment your two scores: list versus story." | none. Spoken at 6:40-6:42 and on the plate at 401 s ("Comment your two scores: list vs story") | unchanged | high |
| Word order cute ... breathtaking | none. It matches the story onsets (1:07-4:38) and the ladder rows top-down | unchanged | high |
| "goes roughly from nice to look at to extremely beautiful" | none. Voice 0:50 verbatim; ladder heading and note "The order is a guide, not a rule." | unchanged | high |
| "you learn what it means and who or what it is for" | Overclaim. The ladder's WHEN cells for lovely ("very common in British English"), striking ("you notice it at once") and gorgeous ("a bit informal, very common when you speak") are usage or register notes, not a who/what | "...what it means and, for most of them, who or what it's used for:" (S2/S3 precedent) | high |
| "men ("handsome")" | Stronger than the video: ladder "usually for men; also "a handsome horse."", voice 2:33 "We usually use it for men" | "usually men ("handsome")" | high |
| "small, delicate things ("exquisite jewellery")" | Acceptable, but the ladder cell is "small things made with great care"; aligned to it. "exquisite jewellery" kept: the scene is two gold rings (3:19, frame 207 s), and it is a standard collocation | "small, delicate things made with great care ("exquisite jewellery")" | high |
| "happy faces ("a radiant smile")" | Narrower than the video: radiant = "glowing with happiness or health" (ladder), use "faces and smiles" | "faces and smiles ("a radiant smile")" | high |
| "and casual chat ("gorgeous" is a bit informal)" | A register note sitting inside a who/what list; "casual chat" is not in the video | Moved out into a new sentence using verbatim ladder cells: "You also learn that "lovely" is very common in British English, and that "gorgeous" is a bit informal and very common when you speak." | high |
| "babies and small animals ("cute")", "places and views ("a picturesque village", "a breathtaking view")", "the way someone or something moves ("graceful")" | none. Ladder cells and cards (picturesque 97 s "For places and views"; breathtaking 280 s "We often use it for views"; the story's village "like a painting", "The view is breathtaking" 4:38) | unchanged | high |
| "Tonight, try it with your own new words: one silly story, one picture for each word." | none. Voice 6:44-6:48 verbatim | unchanged | high |
| Link line 'For more words, look up "another word for beautiful" on anotherwordfor.net: URL' | none. It matches the spoken CTA (6:49-6:53) and the final card "Find more synonyms on anotherwordfor.net" (411 s). No promise of examples or a search box | unchanged | high |
| Tags (14) | none. 276 chars (302 with separators). Every term is in the video (gorgeous, stunning, breathtaking, pretty, handsome, picturesque) | unchanged | high |
| Memory statistics | none in the description or the voice (no "most people", no numbers, no research) | none | high |

## Final description (as written to s4.json)
The paragraph that changed now reads: "For each word, you learn what it means and, for most of them, who or what it's used for: babies and small animals ("cute"), usually men ("handsome"), places and views ("a picturesque village", "a breathtaking view"), the way someone or something moves ("graceful"), small, delicate things made with great care ("exquisite jewellery"), and faces and smiles ("a radiant smile"). You also learn that "lovely" is very common in British English, and that "gorgeous" is a bit informal and very common when you speak." Everything else is identical to meta.json. I re-read the whole description after the edit.

## Challenge beats in v2 (all present, in order)
1. Hook 0:00-0:11.
2. Plain list 0:16-0:26: exquisite, cute, gorgeous, attractive, lovely, stunning, handsome, pretty, elegant, good-looking (shown twice on screen, cosmetic).
3. Pause cue 0:27 with a 5.9 s hold, then "your first score. The list score" at 0:36.
4. Bridge 0:41-0:57, including "roughly from nice to look at to extremely beautiful".
5. Story 0:57-4:57: 15 words, with a happy ending ("The bride and groom take the goat home. Okay, it's only a story.").
6. Second pause 4:58 "in order", with a 3.7 s hold, the tip "walk through the story again", and "your story score".
7. Reveal 5:13 "15 words, not 10", with the extras chips (picturesque, graceful, striking, radiant, breathtaking).
8. Ladder 5:24-6:38, 15 rows, highlight following the voice.
9. Comment line, spoken and on a plate, at 6:39.
10. Transfer line 6:44: "Tonight, try it with your own new words. One silly story, one picture for each word."
11. CTA 6:49: "For more words, look up another word for beautiful on anotherwordfor.net."

## Checks
- Title: 62 chars (limit 100). No < or > in s4.json at all (title, description, tags, notes).
- Tags: 276 chars, 302 including separators (limit 500).
- Settings: privacy private, made_for_kids false, Education, en, no #Shorts, playlist "Synonym Memory Challenge".
- video_ids_local = specials/s4-v2 only. Format 6:53.

## Non-blocking (in the video, not fixable in metadata, none a false claim that contradicts the screen)
- lovely, 1:55: the voice says "It's incredibly common in British English"; the card and the ladder say "very common". A mild spoken overstatement; the description uses "very common".
- 4:16: "you take a group photo that turns the sky orange and pink" (illogical, harmless NotebookLM wording).
- handsome, 2:34: "for a woman, it means attractive in a strong way" is spoken only, not on the ladder. Correct, just not repeated.
- Plain list shown twice (bullets + scroll), cute panel in flat clip-art style, grey smear left of the logo, stunning highlight 0.8 s late (critic-v2 minors). Cosmetic.
- The title's "15" slightly spoils the reveal. Kept per the runbook (same as S2/S3).
- anotherwordfor.net: the **SSL certificate has expired**, so browsers will warn viewers who click the link. Known postponed P0, not a language issue. The user should know before publishing.
- Publisher: pin the comment "List: __ / Story: __".

## Not done
- shorts/lang_gate.py approve does not apply (s4.json has no "beats"). The approval was written by hand into s4.json "language_approval".
- No human listening; one whisper pass only (all 15 headwords heard correctly in the story and the recap; the domain heard correctly). Frames were sampled, not viewed in full.
- No WebSearch and no NotebookLM query. Every changed phrase copies a label already on screen and already dictionary-checked in lang-gate-v1.md ("exquisite jewellery" was already in the gated meta.json).
- meta.json keeps the pre-generation description. s4.json is the upload file.
