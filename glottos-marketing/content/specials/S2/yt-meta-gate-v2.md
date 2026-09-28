# S2 YouTube metadata gate v2 (content/youtube/s2.json vs s2-v2.mp4)

Gate: glottos-language-editor, headless autopilot step "special S2: yt_meta_gate", 2026-09-28 (UTC).
Upload file: content/specials/S2/s2-v2.mp4 (**453.29 s = 7:33**, 1280x720, 16:9, not a Short, private). sha256 886656ca59ea54a1ccf9aeed7875beed4166e25c0c551b802bd5011022b1c447, size 32381276 B. It is identical (same sha256) to /workspace/glottos-auto/out/specials/s2-v2.mp4.
Note: the task brief gave 448.05 s (7:28). That is the length of s2-v1. The polish added 8.5 s of holds, and PyAV measures the final file at 453.29 s, so s2.json says 7:33.
Sources:
- Own faster-whisper small.en transcript of v2 (int8, cpu_threads=4, state/whisper-models, .nlmvenv): a full pass, plus isolated word-timed re-checks of 340.5-346 s and 432-438.6 s, run with and without previous-text conditioning (same result both ways).
- PyAV frames at 5, 35, 50, 346, 400, 440, 445 and 451 s.
- critic-v2.md (SOLVES), polish-v2.md, lang-gate-v2.md (APPROVED), meta.json, and docs/autopilot.md (Specials S1-S5).

meta.json was not changed. Nothing was uploaded. YouTube and NotebookLM were not touched.

## Verdict: APPROVED

## Table

| Line | Problem | Fix | Confidence |
|---|---|---|---|
| Title "Can You Remember 15 Synonyms for SAD? (Memory Challenge)" | none. 56 chars. It matches the video's 15 words (reveal 5:41, 15-row ladder) and the challenge format | unchanged | high |
| Hook "Ten words for SAD in a plain list, then one silly story... two scores" | none. Voice 0:00-0:17: "10 words for sad", "a single, silly story", "grab a pen. You're getting two scores today", "the plain list" | unchanged | high |
| Steps 1-2 (list score / story score, "can recall, in order") | none. Voice 0:30-0:43 and 5:18-5:40, pause cards at 35 s | unchanged | high |
| Step 3 "surprise at the end, and the whole SAD ladder on one screen" | none. Reveal 5:41 "15 words, not 10" plus the extras chalkboard (346 s); "The SAD ladder" on one screen (400 s) | unchanged | high |
| Step 4 "Comment your two scores: list versus story." | The voice only says "List versus story" (7:17). The on-screen plate says "Comment your two scores: list vs story." (440 s), so the claim is true on screen | unchanged | high |
| Word order blue ... inconsolable | none. It matches the story onsets (1:00-4:57) and the ladder rows top-down | unchanged | high |
| "goes roughly from a little bit sad to extremely sad" | none. Voice 0:53 and 5:54; the screen says "a guide, not a rule" | unchanged | high |
| "For each word, you learn what it means and when to use it" | Slight overclaim. Heartbroken's WHEN cell is "—", and the voice gives it no register | "...what it means and, for most of them, when to use it:" | high |
| Register list (everyday speech, at work, casual chat with friends (informal), sports news, books/songs/poems (literary)) | none. These are the video's own labels: very common in speech / speech and news, neutral fine at work, informal: with friends, often in sports news, literary: books and songs, old-fashioned literary: poems | unchanged | high |
| "Then try it with your own new words: one silly story, one picture for each word." | The video does say this. The voice at 7:22 starts "Tonight, ..." | "Tonight, try it with your own new words: ..." (verbatim) | medium |
| Link line 'For more words, look up "another word for sad" on anotherwordfor.net: URL' | none. It matches the spoken CTA (7:28) and the site card (451 s). No promise of examples or a search box | unchanged | high |
| Tags (14) | none. 279 chars including commas; every term is backed (melancholy, down in the dumps, heartbroken/devastated/miserable are all in the video) | unchanged | high |
| Memory statistics | none in the description or the video (no "most people", no numbers) | none | high |

## Challenge beats in v2 (all present, in order)
1. Hook 0:00-0:14.
2. Plain list 0:18-0:29: melancholy, upset, blue, heartbroken, gloomy, disappointed, devastated, down in the dumps, unhappy, miserable.
3. Pause cue 0:30, with a 4.0 s hold on "Write down every word you remember. / List Score".
4. Bridge 0:45-1:00.
5. Story 1:00-5:17: 15 words, happy ending.
6. Second pause 5:18 "in order", with the tip and a 5.1 s hold.
7. Reveal 5:41 "15 words, not 10" and the extras chalkboard (glum, dejected, forlorn, sorrowful, inconsolable).
8. Ladder 5:52-7:17.
9. Comment plate plus "List versus story" at 7:17.
10. "Tonight, try it with your own new words. One silly story, one picture for each word." at 7:22.
11. CTA at 7:28: "For more words, look up another word for sad on anotherwordfor.net."

## Checks
- Title: 56 chars (limit 100). No < or > anywhere.
- Tags: 279 chars (limit 500).
- Settings: privacy private, made_for_kids false, Education, en, no #Shorts, playlist "Synonym Memory Challenge".
- video_ids_local = specials/s2-v2 only. Format 7:33.

## Non-blocking (in the video, not fixable by metadata, none of them false claims)
- At 5:42 the voice says "I **give** you 15 words, not 10." The isolated re-check heard "give" both times, so this is a tense slip ("gave" was meant). It is grammatical enough and not a false claim. The description does not quote it.
- The comment CTA is on screen only, not spoken. The publisher should add a pinned comment "List: __ / Story: __".
- Dejected has no picture (3:14-3:34). The main character switches between a girl and a man.
- Whisper heard "ride out the door" at 5:00 (probably "right out the door"). This was not ear-checked and does not affect the metadata.
- The title's "15" and the "One story. 15 words." card slightly spoil the reveal. This is kept because the runbook specifies it.
- anotherwordfor.net/another-word-for-sad/: plain curl fails TLS (the **SSL certificate has expired**); with -k the page returns HTTP 200 and lists dejected, forlorn and melancholy. Browsers will warn viewers who click the link. This is the known postponed P0, not a language issue. The user should know before publishing.

## Not done
- shorts/lang_gate.py approve does not apply (s2.json has no "beats"). The approval was written by hand into s2.json "language_approval".
- No human listening; whisper only. Frames were sampled, not viewed in full.
- meta.json keeps the pre-generation description. s2.json is the upload file.
