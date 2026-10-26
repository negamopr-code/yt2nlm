# Viewer-critic review: words-that-stick-ep06-v3 (Words That Stick #6 "Why your mind goes blank", series finale)

- Video: `content/episodes/E6/e6-v3.mp4` (1440x2560, 30 fps, 70.9 s). Unit: `shorts/units/ep06_v3.json` (language approval daf112343d3d6186). Subscribe: `content/episodes/E6/e6-v3.subscribe.json` = `[58.0]`, 5 s, corner bl. Meta: `content/youtube/ep06.json`.
- Pain source: the PROBLEM 01 quotes are the same verbatim set as in `content/reviews/words-that-stick-ep06-v2.md`. One of them ("as soon as i speak my mind just shuts down") was re-checked by grep in the repo. I also used `content/articles/p01-ep06-format.md` and article §7. No NotebookLM query was made.
- Checked:
  - 36 frames: hook at 0.3/0.8/1.4/3 s, every beat midpoint, end card.
  - 32 frames at 0.1 s steps over the quiz (27.3-30.5).
  - 22 frames at 0.25 s steps over the subscribe window (57.8-63.4).
  - Full-size crops of panel 2 (44 s) and the quiz reveal (29.5 s).
  - Transcript: faster-whisper small.en with word timings on the final mp4.
  - Silences: silencedetect (-45 dB, 0.7 s).
- Not checked: loudness by ear, a real phone with the YouTube UI, the site page.

## Verdict: SOLVES
The hook is my own sentence. The two panels show why my mind goes blank (three jobs at once) and what fixes it (two jobs "done in advance" on the shelf). "I was swamped at work this week." shows the method in one line. All three v2 blockers are fixed.

## Ship-blockers (0)
v2 blockers re-checked:
1. **Panel 2 (37.5-50.6 s): FIXED.** From 37.5 s to 50.6 s the screen shows the full header "With words learned in sentences" and the whole picture: a happy brain holding "Find the word", and a shelf with "Check if it fits ✓" and "Build the grammar ✓", labelled "Done in advance". The frame is not cut off and has no Gemini/NotebookLM watermark (full-size crop at 44 s). The picture matches the voice word for word ("two of those jobs in advance", 41.5 s).
2. **Quiz (27.5-30.3 s): FIXED, with a risk left (see Retention).** The freeze picture is on screen until about 27.6 s. Then:
   - Question card "A pub quiz. Your answer sheet is empty. / Your turn: you draw a …?" from about 27.7 to 29.1 s (about 1.4 s).
   - Reveal: pub-quiz picture with the "draw a blank" strip from about 29.2 to 30.0 s (about 0.9 s).
   - Voice comes back at 30.00 ("Telling a story…").
   - Silence lasts 2.79 s (27.50-30.28), under the 3 s gate.
   - The countdown digits and tongue-tied are gone, so it no longer looks like a glitch.
3. **Meta: FIXED.** `content/youtube/ep06.json` has `"subscribe_at": [58.0]` and `video_ids_local: ["words-that-stick-ep06-v3"]`. `PLAYLIST_URL_ADD_AT_PUBLISH` is still there. That's expected: the publisher replaces it at upload, and yt_meta_gate checks it (`publish_todo`).

Other checks:
- **Spelled-out words:** none in the transcript.
- **"blank" vs "blanket":** every "blank" is heard as "blank", never "blanket" (4.84 "goes blank", 12.28 "that blank moment"). The quiz answer is on screen only, so the presenter's "draw a blink" is not in the audio.
- **POLICY:** none. All pictures are cartoons with no real people, and the logo is the channel avatar. The panel-1 waiting figure is still a simple shirtless cartoon (14-22 s). It's non-sexual and doesn't block, but it's a visuals note for future sheets.
- **Subscribe animation:** runs 58.0-63.0 s in the second half, as the Short's closing call. It sits under the caption pill and covers no text or picture. SUBSCRIBE → SUBSCRIBED ✓ → yellow bell, then fades at about 63.2 s.

## Pain -> what the video gives -> gap
Learner quotes (verbatim, PROBLEM 01):
- "I can understand 100% of the video, but when I try to speak, my mind goes blank"
- "when I try to speak I forgot every sentence in my mind !! My mind became blank ..."
- "I can write paragraphs in English without any difficulty but as soon as i speak my mind just shuts down"
- "if I try to open my mouth for speak english, its blank. I don't have any idea what i said next"
- "I mostly avoid communicating in a crowd because I dont remember the words. dont know how to make phrases."
- "confidence on talking I forgetting everything as soon as I start talking"

**Pain in one sentence:** "I understand everything, but when I open my mouth my mind goes blank and I can't build the phrase."
**Solved tomorrow means:** I learn each new word inside one full sentence about my life and say that sentence out loud. In a real conversation I then only have to find the word, because the sentence comes with it.

| Pain | Video gives | Gap |
|---|---|---|
| "my mind goes blank" | The hook card and voice give the quote verbatim (0-5.1 s) | None. |
| Why? | Panel 1: a brain juggling "Find the word / Check if it fits / Build the grammar" while a person waits (11.3-22.6 s) | None. |
| What fixes it | Panel 2: "Done in advance", with 2 of the 3 balls on the shelf (37.5-50.6 s) | Fixed vs v2. The picture now carries the idea for sound-off viewers. |
| "dont know how to make phrases" | Card "One job left: find the word / It arrives with its sentence." (50.7-58.2), then "I was swamped at work this week." + "swamped = very busy" (58.2-60.1) | Small. The voice never says "learn it like this", so the example is a bridge the viewer has to make alone. |
| Naming the feeling | freeze, draw a blank (quiz), lose your train of thought, stumble over your words | Four useful phrases, each with a scene. |

## Second by second
| Time | Heard | Seen | Note |
|---|---|---|---|
| 0.0-5.1 | "I can understand 100% of the video, but when I try to speak, my mind goes blank." | "…my mind goes blank." + the quote, on screen from frame 1 | Stops me: it's my sentence. |
| 5.3-6.0 | silence (0.7 s) | same card | Fine. |
| 6.0-10.6 | "Sound familiar? Well, don't worry, because your memory absolutely isn't broken." | "Sound familiar? / Your memory isn't broken." | Text only, with the lower 60 % empty. A mild swipe risk, but short. |
| 11.3-22.6 | three jobs, "total mental overload" | Panel 1 "Three jobs at once" (the header box's top edge sits tight under the brand bar) | Good sync. |
| 23.9-27.3 | "...job interview answer, you freeze." | freeze picture (a thin band) | OK. |
| 27.5-30.3 | silence | question 1.4 s -> draw-a-blank picture 0.9 s | It now reads as a deliberate "your turn". The question is still a tight read for B1, and the meaning line is missing (see Retention). |
| 30.0-36.4 | train of thought, stumble over your words | matching pictures | Good sync. |
| 37.5-49.7 | "Second, ... two of those jobs in advance ... the word's setting ... the grammar is ready." | Panel 2, full | This was the main swipe point in v2 and is now the strongest frame. |
| 50.7-57.7 | "Finally, ... only one job left, finding the word. It arrives with its sentence already attached." | "One job left: find the word / It arrives with its sentence." | OK. |
| 58.1-60.0 | "I was swamped at work this week." | quote card (switches at about 58.3, 0.15 s after the voice starts, not noticeable) + "swamped = very busy"; SUBSCRIBE from 58.0 | Good. |
| 60.5-64.5 | "You don't need a better memory. You just need to learn words that come with their sentences." | same text; SUBSCRIBED + bell until about 63 s | Good. |
| 65.2-69.7 | "That's the whole system. Watch the full series from Episode 1 in the Words That Stick playlist." | "Comment the word you always forget" + "Full series from Episode 1: the “Words That Stick” playlist · anotherwordfor.net" | **Series close present and clear** (65.2-69.7). The headline CTA (comment) is not voiced, which is acceptable. |
| 70.0-70.9 | silence | end card | A 0.9 s tail, fine. |

Captions vs audio: they match word for word. Whisper hears "word setting" and "practiced", and the captions write "word's setting" and "practised". That's the documented, approved caption edit, and the script says "the word's setting". No wrong caption was seen. Captions sit under the picture/card and never overlap the subscribe button.

## Takeaway test
"When I learn a new word, I learn it inside one sentence about my life, like 'I was swamped at work this week', and practise saying it." The screen supports it: panel 2 ("Done in advance"), then the swamped example, then "You need words that come with their sentences." I can name the action, so SOLVES holds. A "Tomorrow: 1 new word = 1 sentence about you, out loud" line would make it explicit, but that's not required.

## Retention risks
- **Quiz read time (27.7-29.1, about 1.4 s):** the question is 7 bold words + 6 small grey ones. A B1 reader gets the headline but probably not "Your turn: you draw a …?" before the reveal. Also, the reveal shows only the picture + "draw a blank". The unit's `a_sub` "You can't think of the answer." never appears in any frame. The empty clipboard implies the meaning, so this doesn't block, but the phrase isn't defined in words. A Shorts loop and replay soften it.
- The lower 40-60 % of the frame is empty on text-card beats (6-11, 50-70 s), and the synonym pictures are thin bands.
- At 70.9 s the length fits one mechanism + 4 phrases. The 0.9x voice is natural, and no pause is longer than 1 s except the quiz.

## Trust risks
- The facts are not overclaimed (no "science proves"). The idioms are correct and natural: freeze, draw a blank, lose your train of thought, stumble over your words. Tongue-tied was dropped, which removes v2's nervous-vs-forgetting confusion.
- "only one job left" is a light pleonasm the editor accepted. It's natural in speech.
- No picture contradicts the words. No garbled text in the pictures. No watermark.

## Top 3 fixes (by impact, none blocking)
1. **shorts-builder:** show the quiz `a_sub` "= you can't think of the answer" on the reveal. If the 3 s silence budget allows, take 0.1-0.2 s from the question to give the reveal about 1.1 s.
2. **scenario-writer (series template):** end finales with an explicit "Tomorrow:" action card ("1 new word = 1 sentence about you, said out loud"), e.g. as the sub of the "You don't need a better memory." card.
3. **visuals:** future sheets should fill the lower half on card beats and avoid shirtless cartoon figures (panel 1 here). Cosmetic.
