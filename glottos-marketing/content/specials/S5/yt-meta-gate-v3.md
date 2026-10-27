# S5 YouTube metadata gate v3 (content/youtube/s5.json vs s5-v3.mp4)

Gate: glottos-language-editor, headless autopilot step "special S5: yt_meta_gate", 2026-09-30 (UTC). Approval stamp: 2026-09-30T06:31:03Z.
Upload file: content/specials/S5/s5-v3.mp4 (**364.29 s = 6:04**, 1280x720, 16:9, not a Short, private). sha256 8345dbe14c9f34b40734cd71c61f540c875070f7fb80fb51a096952bf4246844, identical to /workspace/glottos-auto/out/specials/s5-v3.mp4. Upload id: specials/s5-v3.
Sources:
- Own faster-whisper small.en transcript of v3 (int8, cpu_threads=4, beam 5, word timings, state/whisper-models, .nlmvenv): one full pass. Working files in /tmp/s5m (outside the repo).
- PyAV frames at 1, 20, 33, 80, 91, 101, 143, 192, 207, 223, 269.5, 283, 300, 355 and 362 s (all viewed).
- critic-v3.md (SOLVES), lang-gate-v2-polish.md, script.md, meta.json (pre-generation, lang-gate-v1.md).
- Link: curl https://anotherwordfor.net/another-word-for-problem/ gives ssl_verify_result 10 (certificate expired). With -k: HTTP 200; the page contains issue, trouble, dilemma, predicament, obstacle, complication, hitch, headache.

meta.json was not changed. Nothing was uploaded. YouTube, NotebookLM and state/autopilot.json were not touched.

## Verdict: APPROVED

## Table

| Line | Problem | Fix | Confidence |
|---|---|---|---|
| Title "Can You Remember 15 Synonyms for PROBLEM? (Memory Challenge)" | none. 60 chars. 15 words (reveal 4:38 "I gave you 15 words, not 10", 15-row ladder) | unchanged | high |
| Hook "Ten words for PROBLEM in a plain list, then one silly story... two scores" | none. Voice 0:00-0:12: "10 words for problem. How many can you remember? ... a single silly story ... Grab a pen. You're getting two scores." | unchanged | high |
| Step 1 (list score) | none. 0:28 "Pause the video now. Write down every word you remember." + 3.8 s hold (card at 33 s); 0:37 "That's score number one, your list score." | unchanged | high |
| Step 2 ("can recall, in order", story score) | none. 4:24-4:28 voice; card at 269.5 s "Write down every word you can recall, in order." + 3.5 s hold; 4:36 "your story score" | unchanged | high |
| Step 3 "surprise at the end, and the whole PROBLEM ladder on one screen" | none. Reveal 4:38 + extras card (hiccup, glitch, complication, predicament, crisis); 4:47 "Here's the whole ladder on one screen"; 15-row table 4:47-5:50 | unchanged | high |
| Step 4 "Comment your two scores: list versus story." | none. Spoken 5:51-5:54; card at 355 s "Comment your two scores: list vs story." | unchanged | high |
| "roughly from small problems to very serious ones" + word order hiccup ... disaster | none. Voice 0:46 and 4:49 verbatim; story headwords 0:50-4:01 and ladder rows in exactly this order | unchanged | high |
| hitch: "a problem that causes a short delay ... "without a hitch" means with no problems at all" | none. Card (91 s) + voice 1:28-1:33 verbatim. Note: "without a hitch" is spoken only, not on a card; the description says "you learn", which is true | unchanged | high |
| glitch: "a small fault in a machine or computer" | Narrower than the video: card "a small fault that stops something working properly."; voice 1:40 "... often for machines and computers"; ladder "Often machines and computers." | "a small fault that stops something working properly, often in machines and computers ("a glitch")" | high |
| obstacle: "something in your way" | none. Card (143 s) and ladder | unchanged | high |
| dilemma: "a very difficult choice, often between two things" | none. Card (207 s), voice 3:25, ladder verbatim | unchanged | high |
| predicament: "a difficult situation that is hard to get out of" | none. Ladder and recap 5:38 verbatim (story card says "an unpleasant situation...", same sense) | unchanged | high |
| "You also learn which one is informal ("snag")" | Implies snag is the only informal word; learner dictionaries also mark "headache" (this sense) as informal. The video only labels snag | "You also learn that "snag" is informal," | high |
| "and what "in trouble" means" | none. Card line (192 s) "In trouble: someone is angry with you." + voice 3:10 + ladder | unchanged | high |
| "Tonight, try it with your own new words: one silly story, one picture for each word." | none. Voice 5:54-5:58 verbatim | unchanged | high |
| Link line 'For more words, look up "another word for problem" on anotherwordfor.net: URL' | none. Voice 5:59-6:04 and the final card (362 s). No promise of examples or a search box | unchanged | high |
| Tags (14) | none. 257 chars (283 with separators). "dilemma vs predicament", "hitch snag glitch", "setback meaning": every word is defined in the video | unchanged | high |
| Memory statistics | none in the description or the voice | none | high |

## Final description paragraph that changed
"For each word, you learn what it means, for example: a problem that causes a short delay ("a hitch", and "without a hitch" means with no problems at all), a small fault that stops something working properly, often in machines and computers ("a glitch"), something in your way ("an obstacle"), a very difficult choice, often between two things ("a dilemma"), and a difficult situation that is hard to get out of ("a predicament"). You also learn that "snag" is informal, and what "in trouble" means."
Everything else is identical to meta.json. I re-read the whole description after the edit.

## Challenge beats in v3 (all present, in order)
1. Hook 0:00-0:12.
2. Plain list 0:17-0:28: dilemma, snag, trouble, obstacle, issue, disaster, hitch, setback, difficulty, headache (frame 20 s; whisper skips trouble/difficulty, on screen and confirmed by the critic).
3. Pause 1 at 0:28 + 3.8 s hold; list score 0:37.
4. Bridge 0:40-0:50 incl. "roughly from small problems to very serious ones".
5. Story 0:50-4:23, 15 words, happy ending ("best birthday in 90 years", "It's only a story").
6. Pause 2 at 4:24 "in order" + 3.5 s hold; tip "Walk through the story again"; story score 4:36.
7. Reveal 4:38 "15 words, not 10" + extras card.
8. Ladder 4:47-5:50, 15 rows, highlight follows the voice.
9. Comment line 5:50, spoken and on a card.
10. Transfer line 5:54.
11. CTA 5:59: "For more words, look up another word for problem on anotherwordfor.net."

## Checks
- Title 60 chars (limit 100). No < or > anywhere in s5.json.
- Tags 257 chars, 283 incl. separators (limit 500).
- Settings: privacy private, made_for_kids false, Education, en, playlist "Synonym Memory Challenge", video_ids_local = specials/s5-v3 only, format 6:04.
- Caps: "PROBLEM" in title/description is text only (not voiced); the voice says "problem" as a word (0:00).

## Non-blocking (video only, not a metadata issue)
- 4:15 "In the ending, your grandmother laughs" (slightly odd NotebookLM wording; harmless).
- Blank paper patch over the disaster scene 4:00-4:24, grey smear left of the logo, flat clip-art complication panel (critic-v3 cosmetics).
- The title's "15" slightly spoils the reveal; kept per the series runbook (S2-S4).
- anotherwordfor.net **SSL certificate has expired**: browsers will warn viewers who click the link. Known postponed P0; the user should know before publishing.
- Publisher: pin "List: __ / Story: __".

## Not done
- shorts/lang_gate.py approve not applicable (s5.json has no "beats"); approval written by hand into s5.json "language_approval".
- No human listening; one whisper pass. Frames sampled, not viewed in full.
- No WebSearch and no NotebookLM query: both edits copy wording already on screen/voiced or narrow a claim.
