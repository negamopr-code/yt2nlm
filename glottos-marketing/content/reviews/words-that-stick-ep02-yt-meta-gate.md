# Ep2 YouTube metadata gate (content/youtube/ep02.json vs words-that-stick-ep02-v1/final.mp4)

Gate: glottos-language-editor, headless autopilot step "episode 2: yt_meta_gate", 2026-09-30 (UTC). Approval stamp: 2026-09-30T05:50:02Z (written into ep02.json "language_approval").
Upload file: state/shorts/words-that-stick-ep02-v1/final.mp4 (53.3 s, 1080x1920, 9:16 Short, private). sha256 f4da3476ea17d120664f7b8a6708a5d69c68488d97c4b61f00fd0e381e0054ab. It is identical (same sha256) to /workspace/glottos-auto/out/words-that-stick-ep02-v1.mp4.
Sources:
- My own faster-whisper small.en transcript of final.mp4 (int8, cpu_threads=4, word timings, state/whisper-models, .nlmvenv, run with nice). One full pass. Working files are in /tmp/ep02m, outside the repo.
- PyAV frames at 2, 7, 15, 22, 29.5, 31, 33.5, 37, 40, 42.2, 43.5, 46.3 and 50 s.
- Critic report content/reviews/words-that-stick-ep02-v1.md (PARTLY, no ship-blockers), unit shorts/units/ep02_v1.json, and the article content/articles/p01-why-you-forget-new-words.md (cover table, R&K paragraph). I also read content/articles/p01-ep03-format.md to check the Ep3 teaser.
- Roediger & Karpicke (2006), full text (Psychological Science 17(3), Exp. 2). The SSSS group read the passage in four 5-min study periods. The STTT group studied it in one period and then took three recall tests. At 1 week: STTT 61%, SSST 56%, SSSS 40% (idea units, prose passages).
- Link: curl https://anotherwordfor.net/another-word-for-important/ gives ssl_verify_result 10 (certificate expired). With -k it returns HTTP 200, title "Another Word For Important", and the page lists crucial, vital, essential, urgent, critical, significant and key. There is no search form on the page.

Nothing was uploaded. YouTube, NotebookLM and state/autopilot.json were not touched. Privacy, made_for_kids, category, language, playlist ("Words That Stick") and video_ids_local are unchanged.

## Verdict: APPROVED WITH FIXES

## What is heard (transcript)
- 0.00 "Passively rereading word lists really only trains your brain to recognize words on a page."
- 5.68 "But if you want to effortlessly retrieve those words in a real conversation, you've got to change how you study."
- 11.56 "People who practice active recall remember about 61% of what they studied a week later, while passive rereaders hit only 40%."
- 20.68 "Instead of just memorizing ways to say very important, link them to clear images. A match-deciding penalty kick is [pause] crucial."
- 30.06 "The air in a diver's tank is vital, and a passport on a trip abroad is essential."
- 35.50 "Read the meaning, say the word out loud, and then check the answer."
- 39.10 "If you're very busy, [pause] you're swamped."
- 42.70 "A burst pipe you must fix right now? [pause] Urgent."
- 46.90 "Those small moments of mental effort, forcing your brain to search for the answer, are exactly what make the memory stronger."
On screen: title "Stop re-reading your word list", panel 1 "You re-read it. Then it's gone."; Recognise / Recall; bars "about 40%" Re-read / "about 61%" Practised recall, "Remembered one week later. Same study time."; "very important → ?" + "Say it before you see it."; picture cards crucial (penalty kick), vital (diver checking the tank gauge), essential (passport over a packed suitcase); panel 4 (hand covering the right column of a list: very busy / very important); "very busy → ?" then "swamped", "I'm completely swamped with reports this week."; "A burst pipe you must fix right now → ?", "Very important, and it can't wait.", then urgent (burst pipe under a kitchen sink); CTA card "Look up another word for important", "anotherwordfor.net · Next: the best days to review".

## Table

| Line | Problem | Fix | Confidence |
|---|---|---|---|
| Title "Stop re-reading your word list: test yourself instead \| Words That Stick #2" | none. 75 chars (limit 100). Idiomatic. Matches the on-screen title and the three self-test quizzes | unchanged | high |
| "Re-reading your word list feels like studying. But it mostly trains you to recognise a word, not to find it when you need to speak." | none. The voice says "really only" (critic: an overclaim). "Mostly" is the article's wording and the safer claim. The meaning matches the voice at 0:00-0:11 and the Recognise / Recall panel | unchanged ("mostly" kept on purpose) | high |
| "The fix: cover the answer and make your brain find it." | none. It describes the method and does not say the video says it. The covering is shown in panel 4 (0:35), and the voice says "search for the answer" (0:47) | unchanged | high |
| Cover list (very angry → livid, very busy → swamped, very tired → exhausted, very happy → thrilled, very important → crucial) | none. It is a practice exercise for the reader (the article's cover table), not a claim about the video. Livid, exhausted and thrilled are not in the video, and the description does not say they are. Meanings are correct (livid = extremely angry, swamped = having too much work, exhausted = extremely tired, thrilled = extremely pleased and excited, crucial = extremely important). Swamped and crucial are quizzed in the video | unchanged | high |
| "4 words for "very important", one picture each" + crucial / vital / essential / urgent scenes | none. There are four picture cards and they match the frames: penalty kick (29.5 s), diver's tank (31 s), passport on a trip (33.5 s), burst pipe (46.3 s). "Urgent" is framed in the video as "Very important, and it can't wait", so it fits the group | unchanged | high |
| "Try it tomorrow: cover the new words on your list, read the meaning, say the word, then check." | none. It is advice, not a claim that the video says "cover" or "tomorrow" (it does not: the critic noted that "cover" is never said aloud). The voice line at 0:35 is "Read the meaning, say the word out loud, and then check the answer." | unchanged | high |
| "More words for "important": URL" | none. Link HTTP 200 (with -k). It promises no examples and no search box, and the page does list more words for important | unchanged | high |
| "Next episode: the best days to review a new word." | none. It does not claim the teaser is spoken (it is on the CTA card only). It matches the Ep3 format ("Review new words on these 3 days only") | unchanged | high |
| Source sentence "students who practised recall remembered about 61% of a text; students who re-read it remembered about 40%, with the same study time." | Inexact. In Exp. 2 the recall group (STTT) studied the text in only one 5-min period and spent the other three periods on recall tests. What was equal was the total time (four 5-min periods), not the study time. The experiment was also not named | "Experiment 2: one week later, students who read a short text once and then practised recalling it remembered about 61% of it; students who spent the same total time re-reading it remembered about 40%." | high |
| Hashtags "#Shorts #EnglishVocabulary #LearnEnglish #Synonyms #VocabularyTips" | none. #Shorts is kept. All are relevant | unchanged | high |
| Tags (11): english vocabulary, learn english, how to remember new words, active recall, stop rereading, vocabulary tips, another word for important, synonyms for important, crucial meaning, english words, anotherwordfor | none. 210 chars including separators (limit 500). Every term is in the video or the description ("active recall" is spoken at 0:11, crucial is quizzed, and "another word for important" is on the CTA card) | unchanged | high |

## Checks
- Title 75 chars. No < or > anywhere (the "→" arrows are allowed). JSON is valid (python -m json.tool).
- Figures: 61% vs 40% after one week are exactly the published STTT and SSSS means. "About" is harmless. The voice says "of what they studied", which is OK.
- Settings unchanged: private, made_for_kids false, Education, en, playlist "Words That Stick", video_ids_local ["words-that-stick-ep02-v1"].
- I re-read the whole description after the edit.

## Non-blocking (in the video, not fixable in metadata)
- The bar panel says "Same study time." That is a simplification: the total time was the same, but the recall group studied less and was tested more. It is not false in spirit. The description now states it exactly.
- The voice says "really only trains your brain to recognize" (an overclaim vs "mostly"), and "link them to clear images" blurs the recall lesson (critic).
- "Cover" is never said aloud, and the Ep3 teaser is on-screen only (critic fix 1, not done in this video). The description is honest about both.
- anotherwordfor.net: the **SSL certificate has expired**, so viewers who click the link get a browser warning. This is the known postponed P0. The user should know before publishing.
- Critic cosmetics: panel 1 smoke mosaic, 0.8 s reveals, empty lower half of the frame, "?" wrapping onto its own line.

## Not done
- shorts/lang_gate.py approve does not apply (ep02.json has no "beats"). I wrote the approval by hand into ep02.json "language_approval" (S4 precedent).
- No human listening; one whisper pass only. I sampled frames and did not watch the whole video frame by frame.
- No NotebookLM query. I did one WebSearch plus the paper's full text for R&K. The word meanings are standard dictionary senses, already checked in the article gate.
