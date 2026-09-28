# S1 YouTube metadata gate v3 (content/youtube/s1.json vs s1-v3.mp4)

Gate: glottos-language-editor, headless autopilot step "special S1: yt_meta_gate", 2026-09-28 (UTC).
Upload file: content/specials/S1/s1-v3.mp4 (415.83 s = 6:56, 1280x720, 16:9, not a Short, private). sha256 0787a7f36640e3e6da2cd08885731680aa8f2da73cdc91084a2f7325e69ca370, size 28781570 B. It is identical (same sha256) to /workspace/glottos-auto/out/specials/s1-v3.mp4.
Sources: own faster-whisper small.en transcript of v3 (int8, cpu_threads=4, download_root state/whisper-models, .nlmvenv), which was a full pass plus isolated word-timed re-checks of 28-34, 50-68, 212-218, 366-378 and 396-408 s. Also critic-v3.md (SOLVES), polish-v2.md, polish-v3.md, lang-gate-v3.md, script.md, focus.txt, docs/autopilot.md (S1-S5), and PyAV frames at 5, 27, 312.5, 334, 380 and 413.5 s. content/specials/S1/meta.json was not changed. Nothing was uploaded. YouTube and NotebookLM were not touched.

## Verdict: APPROVED

## Transcript caution
The full-pass whisper made two context errors in the recap. It heard "Jubilant is for a positive, hopeful mood" at 370.6 and "Content is almost entirely written" at 399.9. Isolated re-checks of those clips (with and without previous-text conditioning, same result both times) heard **"Upbeat** is for a positive, hopeful mood" at 370.30 and **"Jubilant** is almost entirely written" at 399.64. This matches critic-v3 and the ladder highlight at those times. The voice is correct, so this is not a defect in the video.

## Table

| Line | Problem | Fix | Confidence |
|---|---|---|---|
| Title "How to Remember 15 Synonyms for HAPPY With One Story (Easy Memory Challenge)" | 76 chars (over 70). "How to" promises a method you can reuse, but critic-v3 notes the video never hands it over for your own words. "Easy" is not backed by the video. | "Can You Remember 15 Synonyms for HAPPY? (Memory Challenge)" (58 chars). It keeps the runbook's "15" and the playlist wording, and a question matches a challenge. | high |
| Steps 1-2 "(score 1)", "(score 2)" | The voice says "your first score, your list score" and "score number two, your story score" | "That's your list score." / "That's your story score." Also "write down every word you can recall, in order" (voice 5:08) | high |
| Missing reveal step | The description began with "Ten words" but listed 15, and the title says 15, with nothing in between to connect them. The video does the "15 words, not 10" reveal at 5:29 and shows the ladder at 5:45 | New step 3: "Stay for the surprise at the end, and the whole HAPPY ladder on one screen." | high |
| "Comment your two scores: list vs story." | The voice says "list versus story" (6:48) | "list versus story" | medium |
| "On the way you climb a ladder from a little bit happy to extremely happy" | Unnatural wording, and it implies an exact order. The voice says "roughly" and the screen says "The order is a guide, not a law." | "The story goes roughly from a little bit happy to extremely happy:" | high |
| Word ladder content ... ecstatic | none. It matches the story order in v3 (content 0:52 ... ecstatic 4:53) and the on-screen ladder read from the bottom up (frame 380 s) | none | high |
| "(formal, informal, British)" | Nothing in v3 says "formal". The labels in the video are everyday speech, neutral/work, polite emails, informal, British, and more common in writing / mostly written | "...when to use it: in everyday speech, at work, in polite emails, in casual chat with friends (informal; chuffed is British), or mostly in writing." | high |
| Link line 'More ways to say "happy": URL' | Close to the CTA but not the same | 'For more words, look up "another word for happy" on anotherwordfor.net: URL'. This is the spoken CTA (6:51) and the CTA card (413.5 s). There is no promise of examples or a search box. | high |
| Hook "Ten words for HAPPY... one silly story... two scores" | none. Voice 0:00-0:12 says "10 words for happy", "a single, silly visual story" and "two scores today, so grab a pen" | none | high |
| Tags (14) | none. 286 chars including commas, and every term is backed | unchanged from meta.json | high |
| Memory statistics | none in the description or the video | none | high |

## Challenge beats in v3 (all present, in order)
List 0:13-0:23 (delighted, glad, ecstatic, pleased, thrilled, content, overjoyed, cheerful, elated, over the moon) -> pause cue 0:23 plus a 3.9 s hold on the card "Pause now. Write down every word you remember to get your list score." -> story of 15 words 0:51-5:07 -> second pause 5:07 "in order" plus a 3.5 s hold -> reveal 5:29 "I gave you 15 words, not 10", with the extras card (chuffed, upbeat, joyful, on cloud nine, jubilant) at 334 s -> ladder 5:45-6:48 -> CTA 6:48-6:55 "Comment your two scores, list versus story. For more words, look up another word for happy on anotherwordfor.net."

## Checks
Title 58 chars (limit 100, target 70). No < or > anywhere. Tags 286 chars (limit 500). Privacy private, made_for_kids false, Education, en, no #Shorts, playlist "Synonym Memory Challenge". video_ids_local = specials/s1-v3 only. Format 6:56.

## Non-blocking (known, not fixable by metadata)
- The recap voice overstates two things: "Joyful is heavily used in writing" and "Jubilant is almost entirely written". The on-screen ladder labels are accurate. The description uses the accurate label ("mostly in writing").
- The voice's line "If you wrote down any of those five, they came entirely from that visual story trick" (5:38) is a soft overclaim, but it is not a statistic.
- There is no art for cheerful or thrilled.
- The voice may say CON-tent at 52.3 and 63.2 s. The con-TENT cue on screen teaches the right stress.
- Whisper heard "got him?" at 31.6 and "You pass your exam" at 215.3. The card says "passed".
- The title's "15" slightly spoils the reveal. This is kept because the runbook specifies it.
- https://anotherwordfor.net returns HTTP 200 (and the page lists elated, jubilant and ecstatic), but **its SSL certificate has expired**. Browsers will show a warning when a viewer clicks the link. This is the known postponed P0 and is not a language issue. The user should know before publishing.

## Not done
- shorts/lang_gate.py approve does not apply (s1.json has no "beats"). The approval was written by hand into s1.json "language_approval".
- No human listening. The stress and ear-check items rely on whisper only. Frames were sampled, not viewed in full.
- meta.json keeps the old title and description because it is the pre-generation source. s1.json is the upload file.
