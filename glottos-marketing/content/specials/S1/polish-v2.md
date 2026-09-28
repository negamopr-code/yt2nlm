# S1 polish v2: changelog (s1-v1.mp4 → s1-v2.mp4)

Step "special S1: polish" (headless autopilot), 2026-09-28, after `critic-v1.md` (PARTLY, 3 ship-blocking defects). Input `content/specials/S1/s1-v1.mp4` (429.69 s, untouched, sha256 `496a1903…22b8ec`). Output `content/specials/S1/s1-v2.mp4`: 1280x720, 24 fps, H.264 CRF 18, AAC 44.1 kHz mono, **417.75 s (6:57.8)**, 10026 frames. sha256 `860f463bab526f5a214000c1331122aa7f4d268db01949d0c78978c6f3cf2cfc`.
Done with ffmpeg 7.0.2 (ONE render, -threads 4, ~45 s; `free` showed ~7.1 GB available) plus Python/PIL overlays, reusing the M1 v2 pipeline (cuts + freezes in one select/loop chain, delogo + logo tile, 8 ms audio fades at every join). No NotebookLM, no upload, glottos-auto/out not touched. Build dir: `content/specials/S1/polish-v2-build/` (`plan.py` = every cut/freeze/overlay range as source frame numbers; `audio.py` → `audio_v2.wav`; `ladder.py` → `ladder_base.png` + `ladder_hl_00..14.png`; `logo.py` → `logo.png`; `render.py <out.mp4>`; run from the build dir).

Timestamps: "src" = s1-v1, "new" = s1-v2. Cut boundaries come from faster-whisper small.en (and medium.en for the ear checks) word timings plus ffmpeg silencedetect (-40 dB). All cuts are hard video cuts at frame boundaries inside a silence.

## Edits

| # | What | src | new | Notes |
|---|---|---|---|---|
| 1 | Gemini end card trimmed, fade to black | keep < 426.500 (frame 10236); end card starts 426.58 | 417.35 to 417.75: 0.4 s video fade; audio fades over the last 0.35 s, after the last word | CTA ".net." ends src 425.89 / new 417.14, complete |
| 2 | "Gemini Notebook" watermark removed | every frame (text at x 1157-1272, y 700-710) | every frame | ffmpeg `delogo` x1153 y697 w123 h16 + channel logo `state/brand/awf-logo-channel.jpg` as a 46 px rounded tile with thin grey border at x1222-1270, y660-708 (same as M1) |
| 3 | Ladder table replaced by our own 15-row ladder | 353.083 to 416.333 (frames 8474-9991; scene change at 353.083) | 346.83 to 410.08 | Full-frame overlay, top = Ecstatic, bottom = Content, one row per word (word · meaning · when to use it) from script.md Beat 5. Paper background with faint grid (the pause-card look), white table card, dark text, blue accent for the "when" column, brown ladder rail on the left. Row height 38 px, word 24 px bold, meaning 21 px, register 19 px (measured fits asserted in `ladder.py`). **Karaoke highlight:** the row the voice is reading gets a yellow marker band (the video's own highlighter colour) plus a dot on the rail, timed from whisper word starts (content 353.2 new … ecstatic 405.7 new). During "Then we have our idioms" (387.3-388.5 new) no row is lit; the voice reads over the moon and on cloud nine before overjoyed, and the highlight follows the voice (rows are still in ladder order) |
| 4a | Pause hold 1, after "remember." | freeze frame 816 (34.000, pause card, inside silence 33.75-34.60) | 28.33 to 31.38 (+3.0 s) | Measured silence before "Okay, got them?" now **3.89 s** (was 0.85) |
| 4b | Pause hold 2, after "in order." | freeze frame 7736 (322.333, pause card, inside silence 322.13-322.61) | 313.08 to 316.13 (+3.0 s) | Measured silence before "A quick tip here" now **3.48 s** (was 0.48) |
| 5a | Cut "First up is the playlist. I want you to just read and listen to this stark baseline test." | 11.250 to 16.917 (frames 270-406) | at 11.25 | "…so grab a pen. \| Ready? Delighted." Ear check: small.en hears "playlist", medium.en hears "plain list" (p=0.75), so it is ambiguous by ear; cutting the whole line removes both the ambiguity and "stark baseline test". The cut lands exactly on NotebookLM's own hard cut from the title card to the list slide (11.29), so there is no visual jump. Join silence 0.54 s |
| 5b | Cut "Right, let's dive into the trick." | 41.000 to 43.000 (frames 984-1032) | at 38.33 | "Hold on to that. \| We're trading a boring list for pictures." Pause card → hammock slide. Join silence 0.98 s |
| 5c | Cut "We're gonna build one continuous whiteboard drawing that grows from left to right." (stage direction the picture contradicts) | 45.917 to 50.500 (frames 1102-1212) | at 41.25 | "…for pictures. \| It's one single story going from calm to wild…" Join silence 0.46 s |
| 5d | Cut "So what does this all mean for your memory?" | 416.333 to 418.833 (frames 9992-10052) | at 410.08 | "…can't contain it. \| Comment your two scores, list versus story." Ladder → CTA card. Join silence 0.65 s |

Removed in total: 14.75 s of cuts (354 frames) and 3.19 s of end card/tail. Added: 6.0 s of pause holds. 429.69 − 14.75 − 3.19 + 6.00 = 417.75 s.

## On-screen text added or changed (for the language editor gate)

All on the new ladder screen (new 346.83 to 410.08 s), which fully replaces NotebookLM's table (the old strings `Words / Meaning / Register`, `Content / Glad`, `Satisfied / Relieved`, `Quiet / Everyday`, `Pleased / Chuffed`, `Satisfied / Proud`, `Neutral / Informal`, `Cheerful / Upbeat`, `Visible / Positive`, `Everyday / Moods`, `Joyful / Delighted`, `Joyous / Very pleased`, `Celebrations / Polite`, `Thrilled / Ecstatic`, `Excited / Uncontained`, `Everyday / The top`, `Over the moon`, `Extremely happy`, `Informal idiom`, `Overjoyed / Elated`, `Neutral / Written`, `On cloud nine / Elated`, `Jubilant`, `Mostly written` are gone, with their icons).

1. Title: `The HAPPY ladder`
2. Next to the title (grey italic): `The order is a guide, not a law.`
3. Column headers (grey caps, rendered in upper case): `WORD` · `MEANING` · `WHEN TO USE IT`
4. Rows, top to bottom (word · meaning · when to use it), exact:
   - `Ecstatic` · `so happy you can hardly contain it` · `the top of the ladder`
   - `Jubilant` · `very happy and celebrating a win` · `mostly written: news and books`
   - `Elated` · `extremely happy after a success` · `more common in writing`
   - `On cloud nine` · `extremely happy, as if floating` · `informal`
   - `Overjoyed` · `extremely happy about news or an event` · `neutral`
   - `Over the moon` · `extremely happy, usually about good news` · `informal`
   - `Thrilled` · `very happy and excited` · `great in everyday speech`
   - `Delighted` · `very pleased` · `polite and safe in emails`
   - `Joyful` · `full of joy` · `songs, celebrations; more common in writing`
   - `Upbeat` · `positive and hopeful` · `for moods, people and music`
   - `Cheerful` · `happy in a way people can see` · `for people, voices, even rooms`
   - `Chuffed` · `pleased, often with yourself` · `British, informal: with friends`
   - `Pleased` · `satisfied with a result` · `neutral, fine at work`
   - `Glad` · `happy about one thing, often relief` · `everyday speech`
   - `Content` · `calm and satisfied` · `a quiet, easy kind of happy`
5. Under the table (grey italic): `Read it from the bottom up: from a little bit happy to extremely happy.`
6. Removed, no replacement text: the `Gemini Notebook` watermark (every frame) and the Gemini end card.

Wording notes for the gate: every meaning and register is Beat 5 of script.md (approved 2026-09-27T22:59Z), shortened where a column had to fit: Glad drops the example "I'm glad you came."; Pleased drops "We're pleased with the results."; Chuffed drops "not in a report"; Delighted drops "I'd be delighted to help."; Ecstatic's "The top." became `the top of the ladder` (Beat 3 wording). No new claims. The voice still says "Joyful is heavily used in writing" and "Jubilant is almost entirely written"; the table carries the script's softer labels, as the critic asked.

Audio: no words were changed or re-voiced; only the cuts and the two silent holds above.

## QA done on s1-v2.mp4

- Duration 417.75 s, 10026 video frames (= plan: 10236 − 354 + 144).
- Frames looked at (half-res contact sheets, labelled): every join ±0.05 s (11.2/11.3, 38.29/38.38, 41.21/41.29, 410.04/410.13), inside both freezes (28.3, 29.8, 31.3, 31.45; 313.05, 314.6, 316.1, 316.2), the ladder edges (346.79 = "sneaky extras" card, 346.88 = ladder) and highlights at 360 (Glad), 395 (Overjoyed), 407 and 410.04 (Ecstatic), the CTA (417.3) and the fade (417.7). Full-res ladder frame at 380 (v2 test render, identical overlay): all 15 rows legible at 720p, no clipping, nothing under the logo tile.
- Watermark: bottom-right crops at 0.5, 11.2, 29.8, 60, 130, 200, 260, 314.6, 380, 412, 417.5 s: channel logo on every one, no "Gemini Notebook" text. On the title card (0 to 11.25) the delogo box leaves a soft blue smear where the card's blue line runs under it (no text).
- End card: gone; last frame is the CTA fading to black.
- Joins by whisper small.en on the v2 audio: "pen. | Ready? Delighted." (11.25), "that. | We're trading" (38.33), "pictures. | It's one single story" (41.25), "contain it. | Comment your two scores" (410.08). No clipped word. Silence at the joins 0.46 to 0.98 s (silencedetect -40 dB).
- Pause holds: silence 28.08 to 31.97 (3.89 s) and 312.88 to 316.36 (3.48 s), both on the pause card.
- Ladder highlight vs voice (whisper word starts on v2): content 353.26 (row lit 353.17), glad 356.30 (356.04), pleased 361.16 (361.04), chuffed 365.52 (365.46), cheerful 369.40 (369.46), upbeat 372.26 (372.17), joyful 375.92 (375.67), delighted 380.02 (379.25, on "Then we step up to"), thrilled 384.04 (383.83), over the moon 388.80 (388.54), on cloud nine 390.54 (390.17), overjoyed 394.06 (393.96), elated 397.38 (397.96, lit ~0.6 s late by whisper's clock), jubilant 401.58 (401.46), ecstatic 406.92 (405.67, on "And right at the top").

## Open / not done

- **"content" is said with noun stress, CON-tent, both times** (src 61.4 "First up, content." = new 52.2, and src 63.4 "Say it with me, con-tent" = new 54.2). Evidence: energy/pitch contour (30 ms frames). At 61.41-61.74 the first syllable is 0.15 s long, peak −15.9 dB, f0 ~105-114 Hz; the second is 0.09 s, −20.7 dB, f0 ~90-96 Hz. In the drilled one at 63.38-63.89 the first syllable is 0.27 s, −15 dB, f0 117-130 Hz, and the second is 0.09 s, −19 dB, f0 falling 107→83 Hz. A long, loud, high first syllable with a full vowel is CON-tent. The adjective con-TENT has a reduced, short first syllable. medium.en splits the drill as "con -tent" (p 0.26/0.79), which does not show stress. Not re-voiced (per brief). Options for the user: re-voice these two words, or cut "Say it with me. Content." (src 62.3-63.95, inside silences) so the wrong stress is not drilled; the first "content." would stay. In v2 that span is new 53.05 to 54.70.
- Missing scene art for cheerful (src 131.0-146.6, new 121.75-137.35) and thrilled (src 200.4-217.5, new 191.15-208.25): not added. A clean drawn panel was not quick with the tools here (PIL only, no drawing model); the blue caption card stays with its empty top half.
- Legibility (critic item 6) not done: low-contrast white "content" caption on the hammock picture (src 61-77, new 51.75-67.75), cloud over the on cloud nine definition line, strokes over "Full of joy", fox ear over "The sneaky extras were:".
- Voice lines kept (mid-sentence or not requested): "literally" ×6, "the whole shebang", "Okay, got him?" (probably "got 'em"), "Joyful is heavily used in writing", "Jubilant is almost entirely written". small.en/medium.en both hear "You passed your exam" (fine).
- The "first up / plain list" framing line is gone with cut 5a; the list slide plus "Ready?" introduces the list.
- The recap voice order puts the two idioms before overjoyed; the table keeps the script's ladder order and the highlight jumps to follow the voice.
- Not done: human viewing/listening, language-editor gate on the strings above, and the critic re-run on s1-v2.mp4.
