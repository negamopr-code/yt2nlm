# S2 (SAD) language gate v2: text added in the polish (s2-v2.mp4 / polish-v2.md)

Gate: glottos-language-editor (headless autopilot step "special S2: polish", re-gate). Date: 2026-09-28 (UTC).
Scope: ONLY the on-screen text added in polish-v2.md (Blue card, CTA plate, 15-row ladder incl. title, note, headers, footer, legend) plus the one audio splice (item 5) as text. Everything else was approved in lang-gate-v1 and is not re-read here.
Sources of truth: script.md Beat 5 and lang-gate-v1.md (Oxford/Cambridge senses already checked there). Rendered frames read: polish-v2-build/qa/o_425.4.jpg (ladder), o_441.9.jpg (CTA plate), o_50.jpg (Blue card).
Nothing was edited except this report. No NotebookLM query, no WebSearch needed (all senses were already dictionary-checked in v1).
No `lang_gate.py` stamp: specials have no unit JSON (same convention as lang-gate-v1 and S1 lang-gate-v3). The approval is the verdict line below.

## Verdict: NEEDS FIX (one string; everything else passes)

| Line | Problem | Fix | Confidence |
|---|---|---|---|
| Ladder row 15, WHEN cell: `the top of the ladder` | It contradicts the screen. The ladder is laid out top to bottom from blue to inconsolable, the footer says "Read it from the top down: from a little bit sad to extremely sad", and the down-arrow on the rail points to the last row. So Inconsolable sits at the BOTTOM of the table but the cell says "the top". A B1 learner sees "top" on the bottom row. (The script's "The top." assumed blue at the bottom, but the drawn ladder is reversed.) | Replace with `the strongest word here` (same slot, shorter, no direction). Optional alternative: `the last and strongest step`. Re-render the 15 highlight PNGs and the base. The voice says "The top." over this row; that is a spoken metaphor for "the strongest" and is tolerable, or trim the audio if the user prefers exact match. | high |

## Passing (checked, no change needed)

| Line | Check | Result |
|---|---|---|
| Card `One story.` / `15 words.` / `Now watch the story.` | Natural, correct, B1. Note (not a language error): "15 words" is shown before the "fifteen, not ten" reveal in Beat 5, so it spoils part of the reveal. Same trade-off as the title "15" that v1 already accepted. | PASS |
| CTA plate `Which score was higher?` / `Comment your two scores: list vs story.` | Idiomatic; "vs" is correct on screen (it is not read by TTS here, and the voice says "versus"). Matches the spoken line in Beat 6 and the score card labels "Your List Score / Your Story Score". | PASS |
| Title `The SAD ladder` | Fine. | PASS |
| Note `The order is a guide, not a rule.` | Same wording v1 approved. | PASS |
| Headers `WORD` / `MEANING` / `WHEN TO USE IT` | Correct. | PASS |
| Footer `Read it from the top down: from a little bit sad to extremely sad.` | Correct and idiomatic; consistent with the table layout (it is the row-15 cell above that is inconsistent). | PASS |
| Legend `= one of the 5 sneaky extras` | Matches the script's "sneaky part" wording. | PASS |
| Blue: a little sad / informal: "feeling blue" | Identical to script Beat 5. | PASS |
| Disappointed: sad because it wasn't as good as you hoped / fine anywhere | Script has "something wasn't". "it" has no antecedent in a table cell but is clear enough at B1. OPTIONAL: `sad because something wasn't as good as you hoped` if it fits the column. | PASS (optional) |
| Glum: quiet and a bit sad / informal: "a glum face" | Identical to script and to v1 fix (Cambridge: informal). | PASS |
| Unhappy: not happy, or not satisfied / neutral, fine at work | Identical to script. | PASS |
| Down in the dumps: unhappy and low / informal: with friends | Identical to script (v1-fixed). | PASS |
| Gloomy: sad and without hope / also for dark weather | Identical. | PASS |
| Upset: unhappy because something bad just happened / very common in speech | Script wording. "just happened" is fine in a cell. | PASS |
| Melancholy: a quiet, deep sadness that stays / literary: books and songs | Identical; register label literary, as required. | PASS |
| Dejected: disappointed after trying and failing / often in sports news | Identical; Oxford sense "unhappy and disappointed". | PASS |
| Forlorn: alone and sad / literary | Identical; register literary. | PASS |
| Miserable: very unhappy or uncomfortable / everyday; also for weather | Identical (v1 fix). | PASS |
| Sorrowful: very sad / old-fashioned, literary: poems | Shortened from "poems and old stories"; still accurate and the register matches. | PASS |
| Heartbroken: extremely sad: someone or something you love is gone / `—` | Meaning identical to script (no register in the script). A dash in a "WHEN TO USE IT" column is acceptable. OPTIONAL: `everyday; in speech too` (accurate: neutral, used in speech), which would fill the empty cell. | PASS (optional) |
| Devastated: extremely upset and shocked / speech and news | Identical (Cambridge sense). | PASS |
| Inconsolable: nobody can make you feel better | Meaning identical to script. Only the WHEN cell needs the fix above. | PASS |
| Register labels overall | informal: blue, glum, down in the dumps. literary: melancholy, forlorn, sorrowful (plus old-fashioned). Neutral/everyday: the rest. All match the approved script and v1. | PASS |
| Audio splice (item 5) | Text: "Someone or something you love is gone." Grammatical (singular agreement), idiomatic, and exactly the approved recap line in Beat 5 ("someone or something you love is gone"). The whisper check in polish-v2.md reads the same. | PASS |

## Not checked
- No human listening to the splice (prosody at the join) or to the narration; only the text of it, plus polish-v2.md's whisper result.
- Frames sampled: ladder at 425.4 s (row 13 lit), CTA plate at 441.9 s, Blue card at 50 s. The other 14 ladder highlight PNGs use the same base text, so I did not open each one. Layout, clipping and karaoke timing are for the critic.
- Not re-gated: the parts already approved in lang-gate-v1 (spoken script, focus.txt, meta.json).

## To get APPROVED
Change the row-15 WHEN string in polish-v2-build/ladder.py (line 25) from `'the top of the ladder'` to `'the strongest word here'`, re-run ladder.py and render.py, and re-read that one cell. No other text needs to change.


---
## Resolution (autopilot, 2026-09-28)
Fix applied: row 15 `the top of the ladder` → `the strongest word here`; optional edit applied: Disappointed `it` → `something`. Ladder and s2-v2.mp4 re-rendered and the ladder frame re-checked at 425.4 s. The `—` cell of Heartbroken stays (no invented register). **Verdict: APPROVED** (specials have no unit JSON to stamp; this record is the approval).
