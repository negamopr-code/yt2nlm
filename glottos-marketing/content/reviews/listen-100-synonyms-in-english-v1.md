# Viewer critic — listen-100-synonyms-in-english-v1 (lab H25, long 16:9)

Reviewed 2026-10-04. Video: `state/shorts/listen-100-synonyms-in-english-v1/final.mp4` (1920x1080, 25:55.1, AAC 24 kHz mono).
Unit: `shorts/units/listen-100-synonyms-in-english-v1.json`. Builder: `shorts/build_podcast.py`.
Planned title: "100 Synonyms in English | Listen and Repeat Practice".

## Verdict: PARTLY as rendered — 1 ship blocker. SOLVES once it is fixed.

The drill delivers what the title promises (100 pairs, each new word in a sentence, said aloud twice, first pair at 0:22), but three lines teach a wrong pronunciation, in a video whose whole promise is "learn to SAY them". Everything else found is polish.

## Pain -> what the video gives -> gap

- Pain source: no PROBLEM-NN document for this lab unit, so no learner quotes are used (none invented). Pain as given in the brief: a learner who types "100 synonyms in english" wants other words for the common words they already use and wants to be able to say them; channel pain P01 = new words are forgotten because they are met alone, without a sentence and without saying them.
- "Solved" means: tomorrow they say "I'd like to inquire about the price" or "We have plenty of food" instead of the plain word, without thinking.
- What the video gives: 100 pairs in 10 topics; each new word is announced ("Another word for buy is purchase"), heard in a short sentence twice, and said aloud by the learner twice = 200 speaking turns. Works with the screen off.
- Gap: (a) three mispronounced lines (blocker); (b) the learner is never asked to produce the new word from the old one — no self-test, no recap, so the "forgetting" half of P01 is only half answered; (c) nothing tells the learner that about 20 of the new words are formal ("assist", "inquire", "comprehend", "sufficient", "numerous", "occupation", "verify", "modify", "enhance"); the "=" sign says they are interchangeable.

## Ship blocker (1)

**B1. Three lines are spoken with the wrong pronunciation.**
Evidence: the phoneme string kokoro_onnx sends to the model for each line (same tokenizer, `en-us`, as `shorts/kokoro_tts.py` uses), plus a vowel measurement on the rendered clips for the first two. Not confirmed by a human ear — listen to the three timestamps (30 seconds) before deciding.

| Time | Line | What is said | Evidence |
|---|---|---|---|
| 11:25 and 11:32 (word 45 / 100) | "I read the entire book in one day." | "I REED the entire book in one day" (present-tense vowel in a past-tense sentence). The learner repeats it twice. | phonemes `aɪ ɹˈiːd ðɪ ɛntˈaɪɚ…`; measured first formant of the vowel in `b050-1.wav` is 263–345 Hz (an "ee"; the "e" of "tell", "test" in the same voice measures 580–730 Hz) |
| 4:51 (word 19 / 100) | `Another word for "remember" is "recall".` | "REE-call" (the noun, as in a product recall). The sentence right after says "re-CALL" correctly, so the same word is heard two ways. | phonemes `"ɹˈiːkɔːl"` in the intro vs `ɹᵻkˈɔːl` in the sentence; measured vowel of the first syllable in `b021-0.wav`: 205–243 Hz / 2000–2500 Hz = long "ee" |
| 22:51 (word 90 / 100) | `Another word for "build" is "construct".` | "CON-struct" (the noun stress). The sentence then says "con-STRUCT-ing". | phonemes `"kˈɑːnstɹʌkt"` vs `kənstɹˈʌktɪŋ` |

Fix (unit text, then language-editor re-approval because the hash changes, then a re-render under a new id or with `--overwrite`). Each replacement below was checked against the same tokenizer and gives the right phonemes:
- beat 50: card headline and speech `I read the entire book in one day.` -> `I've read the entire book.` (gives `aɪv ɹˈɛd`). "Yesterday I read…" does NOT fix it (still `ɹˈiːd`). Alternative that avoids the word: `We spent the entire day at the beach.`
- beat 21: speech `Another word for "remember" is "recall".` -> `Another word for "remember" is "to recall".` (gives `tə ɹᵻkˈɔːl`).
- beat 100: speech `Another word for "build" is "construct".` -> `Another word for "build" is "to construct".` (gives `tə kənstɹˈʌkt`).
- Builder gate so it cannot recur (shorts-builder): for every "instead" beat, phonemize the intro and the sentence and refuse the build when the stressed vowel of the new word differs between the two; flag the words "read", "live", "lead", "wind", "close", "use", "tear", "minute" for a manual look.

No word is spelled letter by letter anywhere (full transcript + all 213 clips transcribed one by one). No cut-off audio: every clip starts and ends in silence (trailing silence 0.08–0.38 s), every expected speech window in the final track has sound, every pause is digitally silent.

## Evidence

### Promise vs delivery — delivered
- All 213 voice clips (hook, 10 part titles, 100 intros, 100 sentences, tip, closing) transcribed in isolation with faster-whisper small.en: 210 match the unit word for word; the 3 differences are harmless ("seat" heard as "seed" in isolation, correct in the full pass at 2:12; "dot net" printed as ".NET"; "They're" heard as "They are" at 22:52).
- Counter runs 1 / 100 -> 100 / 100 (seen at 1, 6, 13, 26, 28, 38, 50, 66, 70, 77, 85, 91, 93, 99, 100).
- `chapters.txt` matches the rebuilt timeline to the second (0:19, 2:48, 5:18, 7:55, 10:24, 12:54, 15:21, 17:56, 20:24, 23:04, 25:41).
- Thumbnail (100 / ENGLISH SYNONYMS / LISTEN & REPEAT + host) matches the first frame.

### First 20 seconds — clear
- 0:00–0:19.7: one static card "100 English Synonyms / Listen and repeat" (the text wall of the H22 review is gone) while the voice gives the rules in 7 short sentences, no channel intro. First sentence = the title.
- 0:19.7 "Part 1. Everyday actions." 0:22.4 first pair. 0:27.8 first own speaking turn.
- 19 s of instructions before the first pair is still long; 10–12 s would do.

### Pause — long enough, not too long
- Audible sentence: 1.1–2.5 s (median 1.7 s). Silence after it: 3.1–5.1 s (median 4.0 s) = 1.9x–4.6x the sentence, median 2.4x.
- Shortest case "Don't yell at me." 1.2 s -> 3.3 s of silence; longest "The kids are eager to open their presents." 2.5 s -> 4.8 s; two-sentence items "I was sick. Therefore, I stayed home." 2.4 s -> 4.9 s. Enough to say each once with 1–2 s spare, which a learner meeting "courteous" or "sufficient" for the first time needs.
- Gap between the announcement and the sentence: 0.5–0.9 s. Tight, good.

### Screen — nothing clips or overflows (about 36 frames looked at)
- Announcement card: yellow "ANOTHER WORD" pill, the sentence in large type with the new word in yellow, small grey "purchase = buy" under it. 3 lines at most; longest sentences ("The kids are eager to open their presents.", "The staff were courteous and helpful.", "My aim is to speak English fluently.") fit, clear of the waveform.
- Then LISTEN (white, word-by-word highlight) -> YOUR TURN: SAY IT (green, new word yellow, waveform off) -> LISTEN AGAIN -> YOUR TURN: SAY IT. Labels and counters right in every sample.
- Two-sentence items in part 10 wrap to 2–3 lines, readable; highlight follows the voice (23:10.2 "raining.", 23:11.5 "went").
- Part cards ("PART 6 OF 10 / Good and bad"), tip card (12:48–12:55, "Need another word? / anotherwordfor.net" — correct address now) and closing card ("Which word will you use today? / Write it in the comments.", held 7.1 s after the last word, room for an end screen) are all fine.
- Weak points, none misleading:
  - The "X = Y" line is the answer to the search query and it is the smallest, greyest text on the card, visible only 2.6–3.7 s (median 3.1 s), then gone for the 11 s of the drill. Three words can be read in that time, but not together with the three-line sentence above it. A viewer who looks up during the pause no longer sees which plain word this replaces.
  - During the announcement the big text is the sentence, while the voice says "Another word for buy is purchase" — eye and ear get different things for 3 s.
  - Card order is "purchase = buy", voice order is "buy … purchase".
  - Tip and closing cards carry the pill "LISTEN".
  - Counter still small and grey (noted in the H22 review).

### Voice
- Phrase pairs: 12:35 "Another word for a lot of is plenty of." and 17:41 "…for in the end is eventually." are understandable. 25:09 "Another word for for example is for instance." has a "for for" stumble; 25:26 "Another word for in conclusion is to sum up." is fine. With no audible quote marks, "Another word for so is therefore" (23:39) and "…for but is however" (23:07) are hard to parse with the screen off.
- Loudness is even across all 100 sentences (RMS 0.060–0.080).

## Second-by-second notes (where someone could leave)
- 0:00–0:19 rules; a few skip ahead (chapters allow it).
- 0:22–2:48 part 1: rhythm is clear after the first pair; "begin", "finish", "receive", "repair", "reply" are words a B1 learner already uses — "I know these" is the first swipe reason. The harder words ("inquire", "comprehend", "courteous", "sufficient") start at 3:21.
- 4:51 "REE-call" then "re-CALL" — a careful listener hears the mismatch.
- 11:25 "I reed the entire book in one day" — the learner copies it twice.
- 12:48 tip, 7 s, harmless.
- Every pair is the same 11.5–18.4 s cycle (median 14.7 s), 100 times, with no recap and no question. Part titles and one tip are the only breaks in 26 minutes. Screen-off listeners cope; screen-on viewers drift around part 4–5.
- 25:41 closing question, 7 s hold, clean end.

## Takeaway test
Passed: "I said 100 sentences with a new word for a word I already use; today I pick one and use it" — the closing line asks exactly that. What is missing is the reverse step (I think "ask", can I produce "inquire"?), which is what the learner needs in a real conversation.

## Retention risks
- 26 minutes of one unchanged cycle; silence is about 55% of the runtime by design.
- Part 1 opens with the easiest, least "new" pairs.
- One picture, one voice.

## Trust risks
- B1 above (three wrong pronunciations).
- "=" overclaims for the formal words: "Can you assist me with this box?" (3 / 100) and "We have sufficient time." (44 / 100) are correct but stiff; nobody tells the learner. A comment "nobody says assist me with this box" is likely.
- Loose pairs presented as equal: sleepy = tired, eager = excited, amazed = surprised, road = street, caring = kind, relaxed = calm, clarify = explain. Normal for the genre, still a comment risk.
- "Another word for" used for phrases ("a lot of", "in the end", "for example", "in conclusion").
- "afraid = scared", "little = small", "large = big", "begin = start" give the learner nothing new.

## Fixes, ranked
1. (blocker) scenario-writer + language-editor, then shorts-builder re-render — the three text changes under B1; shorts-builder adds the intro-vs-sentence phoneme gate.
2. shorts-builder — keep the "purchase = buy" line on screen through LISTEN / YOUR TURN (pass `sub=c["sub"]` to the `karaoke(...)` and `turn(...)` calls of the "instead" branch) and make it larger and white. One-line change, can ride on the same re-render.
3. scenario-writer (next unit, with a builder beat) — a self-test at the end of each part: "Another word for buy?" -> pause -> "purchase", for the ten words of that part. This is the missing recall step for P01 and the only variation the 26 minutes would get.
4. scenario-writer (next unit) — mark register in the sub line: "inquire = ask (formal)", "mad = angry (informal)"; say it once in the hook ("some are more formal — the screen tells you").
5. scenario-writer — phrase pairs: "Another way to say 'for example' is 'for instance'." (removes "for for"); start part 1 with less familiar words; cut the hook to about 12 s.
6. shorts-builder — pill "TIP" on the tip card and no "LISTEN" pill on the closing card; announcement card with the pair as the headline ("buy -> purchase") instead of the sentence; bigger counter.

Only fix 1 blocks publishing.

## Sibling video (listen-100-synonyms-for-very-v1) — not reviewed
Only an automatic scan of its `kokoro_jobs.json` with the same phoneme check: no intro/sentence pronunciation mismatch and no "read"-type trap found ("wind" at beat 76 is the noun, "live" at 112 the verb — both right). Its frames, audio and transcript were not looked at.

## What was checked / not checked
- Checked: beat timeline rebuilt from the 213 clip lengths (ends at 25:55.14, same as the file); full faster-whisper small.en transcript of final.mp4 with word timings; all 213 clips transcribed one by one; sound present in all 300 speech windows and silence in all 200 pauses; clip edges; phoneme strings of all 213 lines; vowel measurement for "read" and "recall"; about 36 frames (0:00.5, 0:10, 0:20.5, first pair in all five states, 1:36, 3:22, 6:39, 7:10, 7:15, 9:40, 9:46, 12:36, 12:38, 12:51, 12:56, 16:40, 17:42, 17:45, 19:24, 21:33, part 10 pairs 91, 93, 99, 100, closing card twice); thumbnail; chapters.
- Not checked: nothing was heard by ear — prosody, question intonation, how the quoted words sound in isolation, and the three blocker lines themselves rest on phonemes + measurements; karaoke timing only at 4 points; not every frame; no competitor video opened; the 127 "mismatches" of the automatic full-pass alignment were word-timestamp drift at segment edges and were settled by the per-clip transcripts, not re-listened.
