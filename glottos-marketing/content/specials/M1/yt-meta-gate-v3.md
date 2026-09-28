# M1 YouTube metadata gate v3 (content/youtube/m1.json vs m1-v3.mp4)

Gate: glottos-language-editor, headless autopilot step "special M1: yt_meta_gate", 2026-09-28 (UTC).
Upload file: content/specials/M1/m1-v3.mp4 (332.21 s = 5:32, 16:9, not a Short, private).
Sources: own faster-whisper small.en transcript of v3 (int8, cpu_threads=4, download_root state/whisper-models), critic-v3.md (SOLVES), polish-v2.md, polish-v3.md, lang-gate-v3.md, script.md accuracy notes, frames at 266 s and 285 s (routine card). Nothing uploaded; YouTube and NotebookLM not touched.

## Verdict: APPROVED

| Line | Problem | Fix | Confidence |
|---|---|---|---|
| video_ids_local | pointed at specials/m1-v1 | ["specials/m1-v3"] | high |
| format | said 5:48 | 5:32 | high |
| "Then a 15-minute daily routine that puts all three together." | The spoken lead-in ("a highly effective 15-minute daily routine") was cut in polish v2. v3 gives three 5-minute phases (voice 4:22-4:43, card 0-5 / 5-10 / 10-15 mins), but nothing says "daily" or "puts all three together" | "Then a simple 15-minute routine: 5 minutes for new words, 5 for review and 5 for speaking." | high |
| Hook "Learn a new word on Monday, lose it by Friday?" | none (voice 0:00-0:07) | none | high |
| 5-word challenge at start + test at end | none (0:15-0:36, test 4:49-5:16 with 2.6-3.0 s pauses) | none | high |
| 1. own-life sentence, out loud | none (1:57-2:04, "Step one" 1:20) | none | high |
| 2. inside a sentence + when to use / avoid | none (2:16 "Learn it inside a complete sentence"; 3:01-3:24 swamped/livid; banner STEP 2 matches voice) | none | high |
| 3. cover, recall, days 1/3/7 | none (3:25-4:21, "Step three" 3:25) | none | high |
| "No app needed." | none (voice "No apps needed", 4:43) | none | high |
| CTA: score + one sentence | none (5:16-5:23) | none | high |
| "happy" link | none (voice 5:26 "look up another word for happy on anotherwordfor.net") | none | high |
| Roediger & Karpicke line (61% vs 40% of a text, same time) | none; matches voice 3:38-3:51 and script.md accuracy note, identical to ep02 | none | high |
| Title (60 chars) | none; "three easy steps" is said at 1:17 | none | high |
| Tags (15, 298 chars incl. commas) | none | none | high |

Checks: no "4x stronger", no "70%", no < or >, title 60 chars (limit 100), tags 298 chars (limit 500), privacy private, made_for_kids false, Education, en, no #Shorts. The site's SSL was not flagged (the user postponed it).

## Not done
- shorts/lang_gate.py approve does not apply (m1.json has no "beats"). The approval was written by hand into m1.json "language_approval".
- meta.json (the pre-generation source) still has the old "daily routine" line. It was not edited because m1.json is the upload file.
- No human listening. Frames were sampled only at the routine card.
