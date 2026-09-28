# S1 language gate v2: s1-v2.mp4 (changed on-screen text + "content" stress ruling)

Gate: glottos-language-editor (headless autopilot step "special S1: polish", re-gate). Date: 2026-09-28 (UTC).
Input: `content/specials/S1/s1-v2.mp4` (sha256 860f463b…), changelog `polish-v2.md` ("On-screen text added or changed"), source of truth `script.md` Beat 5 (gated 2026-09-27T22:59Z).
Method: full-resolution frames at new 347, 350, 356.5, 380, 405 and 409.9 s (bundled ffmpeg `glottos-auto/node_modules/ffmpeg-static/ffmpeg`), read and compared string by string with polish-v2.md; faster-whisper small.en word timings on new 50-57 s and 351.5-356.5 s; 30 ms energy/f0 contours of all three spoken "content" tokens; 50 ms energy around the drill span. Nothing edited in the video, nothing uploaded, NotebookLM not touched. No stamp via `shorts/lang_gate.py`: specials have no unit JSON (same convention as M1 lang-gate-v2/v3); the verdict is recorded here.

## Verdict: NEEDS FIX (one audio cut). The on-screen ladder text itself passes as is.

- Ladder screen (new 346.83-410.08): APPROVED, no string changes needed.
- "content" drill (new 53.00-54.90): ship-blocking, must be cut (exact range below).
- Recommended alongside the cut (not blocking): an on-screen stress cue `con-TENT` on the hammock scene.

## 1. Ladder screen: rendered text vs polish-v2.md

All 6 frames show the same static text. Everything matches polish-v2.md exactly: title, grey italic subtitle, column headers `WORD / MEANING / WHEN TO USE IT`, all 15 rows and the footer. No typos, no truncation (the longest cell, `songs, celebrations; more common in writing`, ends at about x 1168 inside the card), nothing under the logo tile, and the highlight band does not cover any text. Karaoke highlights seen on Delighted (380) and Jubilant (405). No highlight at 347/350 (before the voice reaches "content"), as planned.

| Line | Check (meaning + register, per Cambridge/Collins learner senses) | Fix | Confidence |
|---|---|---|---|
| `The HAPPY ladder` / `The order is a guide, not a law.` | Idiomatic; the hedge is right because the ordering is approximate | none | high |
| `Read it from the bottom up: from a little bit happy to extremely happy.` | Natural; matches the voice ("roughly from a little bit happy…") | none | high |
| Ecstatic · so happy you can hardly contain it · the top of the ladder | Correct sense (extremely happy/excited); "hardly contain it" is idiomatic | none | high |
| Jubilant · very happy and celebrating a win · mostly written: news and books | Correct (triumphant happiness after a success); written/journalistic register is right; no false "formal" label | none | high |
| Elated · extremely happy after a success · more common in writing | Sense a bit narrow (also for good news in general) but it is the typical use; register fine | none | medium-high |
| On cloud nine · extremely happy, as if floating · informal | Correct; informal idiom | none | high |
| Overjoyed · extremely happy about news or an event · neutral | Correct ("overjoyed at/by the news") | none | high |
| Over the moon · extremely happy, usually about good news · informal | Correct. Cambridge marks it UK informal; "informal" alone is not wrong | optional: `British, informal` | medium |
| Thrilled · very happy and excited · great in everyday speech | Correct | none | high |
| Delighted · very pleased · polite and safe in emails | Correct (Cambridge: "very pleased"); fits "I'd be delighted to…" | none | high |
| Joyful · full of joy · songs, celebrations; more common in writing | Correct, though the definition uses the word's own root (B1 learners know "joy"). Now consistent with script; the voice's stronger "heavily used in writing" remains a small mismatch, not an error | none | medium-high |
| Upbeat · positive and hopeful · for moods, people and music | Correct; upbeat mood/person/music are all standard collocations | none | high |
| Cheerful · happy in a way people can see · for people, voices, even rooms | Correct; "a cheerful room" (bright, pleasant) is a dictionary sense | none | high |
| Chuffed · pleased, often with yourself · British, informal: with friends | Correct sense and register (UK informal; "chuffed with yourself" is a common pattern) | none | high |
| Pleased · satisfied with a result · neutral, fine at work | Correct | none | high |
| Glad · happy about one thing, often relief · everyday speech | Understandable note style, but "often relief" is a noun where the column otherwise uses adjective phrases | optional: `happy about one thing, often relieved` | medium |
| Content · calm and satisfied · a quiet, easy kind of happy | Correct adjective sense. The "when" cell describes the feeling rather than a context; it reads fine as a note | optional: `for a quiet, easy kind of happy` (script wording) | medium |

The three optional edits are polish only. None blocks the release, and applying them would mean a re-render plus a re-read of the frame.

Not in scope, seen in passing: the NotebookLM caption on the hammock scene, `content` / `Quietly satisfied. You do not want anything else.`, is correct English (the critic's low-contrast note still applies).

## 2. Ruling: "content" said as CON-tent (noun stress)

Measured on s1-v2 audio (whisper small.en word times + 30 ms energy/f0):

| Token | new time | Evidence | Reading |
|---|---|---|---|
| "First up, content." | 52.20-52.62 | 1st vowel ~0.09 s, −16 dB, f0 ~104 Hz; 2nd ~0.06 s, −21 dB, unvoiced by the tracker | leans CON-tent but short/ambiguous |
| "Say it with me, content." (drill) | 54.14-54.75 | 1st vowel **0.30 s**, −15 dB, f0 rising 118→131 Hz; 2nd only ~0.06 s, −18 dB, f0 falling 107→88 | **clearly CON-tent** (noun: "the content of a video") |
| Recap "We start with content, for a calm…" | 353.26-353.62 | both syllables short and weak; no clear prominence | ambiguous, not demonstrably wrong |

**Ruling: the drill is ship-blocking.** "Say it with me" asks the learner to copy the voice, and the voice gives the noun stress for the adjective, which is a different word (con-TENT = satisfied; CON-tent = what is inside something). A vocabulary brand cannot drill a wrong pronunciation. The two other tokens are short and unclear. Without a drill they pass as normal connected speech.

**Minimal fix: cut the drill line.** Re-voicing is not needed and would add a voice-match risk. An on-screen mark alone is not enough, because the audio would still drill CON-tent against the label.

- Cut new **53.00 → 54.90** in s1-v2 (removes 1.90 s: "Say it with me, content."). Do not use polish-v2.md's 53.05-54.70: the release of the drilled "content" still runs to about 54.80 (−39 to −35 dB at 54.70-54.75). Measured levels: 52.65-53.15 ≤ −64 dB, 54.85-55.40 ≤ −53 dB, so both edges are in silence. About 0.87 s of silence remains between "content." (ends ~52.62) and "You're lying down…" (55.42). Use 8 ms audio fades as in the other joins.
- Visual: the hammock scene has a slow zoom, so a hard cut will show a small scale jump between frames 53.00 and 54.90 (the same slide at both points). Either accept it or use a 4-6 frame crossfade. No slide change, no text change.
- Everything after it shifts by −1.90 s (ladder 344.93-408.18, highlight timings, pause hold 2, CTA); re-derive the highlight times from the plan.

**Recommended with the cut (not blocking):** with the drill gone, the video no longer shows how to say the adjective, which script.md promised ("pronunciation cue con-TENT"). Add a small overlay on the hammock scene (new 51.75-67.75 before the shift), under or next to the existing `content` caption. Exact string: `con-TENT`, or `say it: con-TENT` if a label is wanted. It can share the backing plate that fixes the critic's low-contrast caption note. Do not put the stress mark in the ladder's Word column: `Content (con-TENT)` is too wide at 24 px bold.

## What must be re-gated after the fix
- Listen to the new join (whisper check "content. | You're lying down in a hammock.").
- If the stress overlay is added: read the rendered frame (exact string, contrast, no overlap with the "Quietly satisfied…" line).
- The ladder strings need no re-gate unless an optional edit above is applied.

## Not checked
- Only sampled frames (6 on the ladder screen plus 3 on the hammock scene), not every frame. The ladder overlay is a static PNG set (`polish-v2-build/ladder_base.png`, `ladder_hl_00..14.png`), so the text is the same across the whole range.
- No human listening. Stress judgements come from energy/f0 contours plus duration, not from native-ear review; the drill token is unambiguous, the other two are not.
- No WebSearch or NotebookLM second opinion. Every sense and register was already dictionary-checked at the 2026-09-27 script gate, and this pass found no new doubtful claims.
- Other v1 items still open in polish-v2.md (missing cheerful/thrilled art, low-contrast captions, "literally" ×6, "got him?") were not part of this gate.
