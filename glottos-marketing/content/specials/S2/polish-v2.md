# S2 polish v2: changelog (s2-v1.mp4 → s2-v2.mp4)

Step "special S2: polish" (headless autopilot), 2026-09-28, after `critic-v1.md` (PARTLY, 4 ship-blocking defects, all fixable in post). Source `s2-v1.mp4` (448.05 s, untouched). Output `content/specials/S2/s2-v2.mp4`: 1280x720, 24 fps, H.264 CRF 18, AAC mono, **453.29 s (7:33)**, 10878 frames. ONE ffmpeg render (~45 s, -threads 4), same pipeline as S1 v3. Build dir `polish-v2-build/` (`plan.py` = all frame numbers, `audio.py`, `ladder.py`, `cards.py`, `logo.py`, `render.py <out>`). No NotebookLM, no upload, glottos-auto/out not touched.
"src" = s2-v1, "new" = s2-v2 (new = src + holds inserted before it).

## Changes (critic item → what was done)
1. **Watermark + end card (blocking 1).** Trim at frame 10675 (444.79 s; CTA audio ends 444.30, Gemini end card began 444.96), 0.4 s fade to black. `delogo` x1153 y695 w125 h20 on every frame + channel logo tile (`state/brand/awf-logo-channel.jpg`, 46 px rounded, x1222-1270 y660-708, as M1/S1).
2. **15-row ladder (blocking 2).** NotebookLM's 8-row table (src 347.17-431.29) is covered by our own full-frame 15-row ladder, rows in script order blue → inconsolable, top → bottom, with the 5 extras marked by an orange dot. Rows follow script.md Beat 5 (shortened where a column had to fit). Karaoke highlight per row, timed 0.10 s before the voice onsets in critic-v1 (blue 357.36 … inconsolable 427.46 src).
3. **Comment CTA (blocking 3).** Text plate over the score card: `Which score was higher?` / `Comment your two scores: list vs story.` (src 431.67-433.67 plus a 3.0 s hold of the score card frame at src 433.08, new 438.57-441.57; audio silence 3.86 s). No voice was added (no spoken "comment" exists in the audio).
4. **Pause holds (blocking 4).** +3.0 s freeze at src 33.2 (pause 1: silence now 4.00 s, was 1.03), +2.5 s freeze at src 327.6 (pause 2: silence now 5.13 s, was 2.63). Both on the pause card.
5. **Spoken slip (non-blocking 5).** "Someone or someone you love is gone" → the second "someone" (src 420.34-420.56) replaced by "something" (src 271.86-272.24, same narrator, story recap); the extra 0.125 s is removed from the silence after "gone." so every later timing is unchanged. 10 ms fades at both joins. whisper small.en on the new audio: "Someone or something you love is gone."
7. **Early Blue card (non-blocking 7).** Card `One story.` / `15 words.` / `Now watch the story.` (paper-grid look of the pause cards) over src 42.29-57.7 (new 45.29-60.7); the Blue picture now comes up on the word (voiced src 57.86).

## On-screen text added (for the language editor gate)
- Card (new 45.3-60.7): `One story.` · `15 words.` · `Now watch the story.`
- CTA plate (new ~437.2-442.1 + hold): `Which score was higher?` · `Comment your two scores: list vs story.`
- Ladder (new 352.7-436.7): title `The SAD ladder`; note `The order is a guide, not a rule.`; headers `WORD` `MEANING` `WHEN TO USE IT`; footer `Read it from the top down: from a little bit sad to extremely sad.` + `= one of the 5 sneaky extras`; rows (word · meaning · when):
  Blue · a little sad · informal: "feeling blue" | Disappointed · sad because something wasn't as good as you hoped · fine anywhere | Glum · quiet and a bit sad · informal: "a glum face" | Unhappy · not happy, or not satisfied · neutral, fine at work | Down in the dumps · unhappy and low · informal: with friends | Gloomy · sad and without hope · also for dark weather | Upset · unhappy because something bad just happened · very common in speech | Melancholy · a quiet, deep sadness that stays · literary: books and songs | Dejected · disappointed after trying and failing · often in sports news | Forlorn · alone and sad · literary | Miserable · very unhappy or uncomfortable · everyday; also for weather | Sorrowful · very sad · old-fashioned, literary: poems | Heartbroken · extremely sad: someone or something you love is gone · — | Devastated · extremely upset and shocked · speech and news | Inconsolable · nobody can make you feel better · the strongest word here
- Removed: `Gemini Notebook` (every frame), the Gemini end card, NotebookLM's 8-row table.

## QA done
- Duration/frames as planned (audio 453.29 s = 444.79 + 8.5 s holds). Contact sheets `polish-v2-build/qa/sheet0-2.jpg` + `o_*.jpg`: title card, pause card in freeze, Blue card, reveal chalkboard, ladder at 353/400/425.4 (rows lit), CTA plate at 438/440/441.9, transfer line 443, site card 452, fade 453. Logo tile on every frame, no watermark text, no end card.
- silencedetect (-38 dB): pause 1 33.22-37.23 (4.00 s), pause 2 330.51-335.64 (5.13 s), CTA hold 438.57-442.43 (3.86 s).
- whisper small.en on the new audio: 30-42 "Pause the video now. Write down every word you remember. | Okay." ; 421-432 recap incl. the fixed slip; 436-453 "List vs. Story … Tonight, try it with your own new words … For more words, look up another word for sad on anotherwordfor.net".

## Not done / still open (non-blocking)
- **No picture for "dejected"** (src 191.33-210.96): every other scene is a watercolour illustration; a PIL-drawn panel would clash and no matching NotebookLM art exists. Left as is.
- Legibility scrims (glum, forlorn, inconsolable captions) and the optional stress cues (MEL-an-chol-y, for-LORN, in-con-SOLE-a-ble): not done.
- Girl/man protagonist continuity, "so" in the melancholy line: not fixable in post.
- Language gate: first pass NEEDS FIX (row 15 said `the top of the ladder` on the bottom row of a top-down table; optional `it` → `something` in the Disappointed row). Both applied, ladder + video re-rendered (same s2-v2.mp4 path, overwritten within this tick, sha256 `886656ca59ea54a1ccf9aeed7875beed4166e25c0c551b802bd5011022b1c447`). See lang-gate-v2.md. Not applied (invented content): filling the Heartbroken `—` cell.
- No human listen (the splice, pronunciations); critic not yet re-run on v2 (next step).
