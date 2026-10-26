# Viewer-critic review: words-that-stick-ep06-v2 (Words That Stick #6 "Why your mind goes blank", series finale)

- Video: `content/episodes/E6/e6-v2.mp4` (1440x2560, 70.2 s). Unit: `shorts/units/ep06_v2.json`. Subscribe: `content/episodes/E6/e6-v2.subscribe.json` = `[58.0]`, 5 s, bottom-left. Meta: `content/youtube/ep06.json`.
- Pain source: PROBLEM 01 synthesis (NotebookLM source 60678678). The verbatim quotes below are reused from `content/reviews/words-that-stick-ep05-v1.md` (synthesis §3), plus `content/articles/p01-ep06-format.md` and article §7 (`content/articles/p01-why-you-forget-new-words.md`). No NotebookLM query was used.
- Checked: 36 frames (hook 0.3/0.8/1.4/3, each beat midpoint, the subscribe window 57.8-63.5, the end card 64.8-70). Also 20 frames at 0.1 s steps over the quiz (27.5-29.4), a full-size frame at 43 s, a crop of the panel-1 top, and the source infographic `state/nlm-raw/ep06-infographic.png`. Transcript: faster-whisper small.en with word timings on the final mp4. Silences: silencedetect (-45 dB, 0.7 s).
- Not checked: loudness by ear, a real phone with the YouTube UI, the site page.

## Verdict: PARTLY
The hook is my pain word for word, and the mechanism (three jobs, two done in advance) is the right answer. But the key picture, "two jobs done in advance", never appears: for 13 s the screen shows only a cropped header strip. The "your turn" quiz flashes for 0.6 s, so it can't be answered or even read. I understand why my mind goes blank, but the screen never shows me the fix.

## Ship-blockers (3)
1. **Panel 2 is cut off, 36.8-49.9 s (about 13 s).** The screen shows only the strip "With words learned" (the first line of the header, with its border cut at both sides) on an empty cream frame. The panel itself is missing: the happy brain holding "Find the word" and the shelf with "Check if it fits ✓ / Build the grammar ✓ - Done in advance". It is in `state/nlm-raw/ep06-infographic.png`, but the `panel: 2` crop takes only the header row. This is the payoff of the whole episode, and a sound-off viewer gets nothing. Owner: visuals (re-split the sheet so panel 2 = header "With words learned in sentences" + picture, without the "Gemini Notebook" watermark at the bottom right) + shorts-builder (re-render).
2. **The quiz can't be done, 27.8-29.4 s.** The question card "A pub quiz. Your answer sheet is empty. / Your turn: you draw a …?" is on screen for about 0.6 s (27.8-28.4). That's 12 words, which nobody reads in 0.6 s, let alone answers. The countdown shows only "1". The reveal (pub-quiz picture + "draw a blank") lasts about 0.3 s (28.5-28.7). The a_sub "You can't think of the answer." never shows in any frame, so the meaning of "draw a blank" is never given. Then "tongue-tied" holds for 0.6 s (28.8-29.4) with no voice and no meaning. The whole 2.09 s silence (27.50-29.58) goes by as a flicker. The v2 fix shortened v1's 5 s silence to pass gate_av's 3 s limit. That made the gate pass, but the beat became useless: it's a self-test in name only, and it looks like a glitch. Owner: shorts-builder + scenario-writer. Use the 3 s budget for ONE item: question 1.6 s + reveal with meaning 1.2 s for draw a blank. Show tongue-tied as a silent overlay later over voiced footage, or drop it. Alternatively, put the question text on the freeze panel during voice so the reading happens while the voice plays.
3. **Meta not finished: `content/youtube/ep06.json`** has no `"subscribe_at": [58.0]`, and `video_ids_local` points to `words-that-stick-ep06-v1`. By house rule the video is not finished without the recorded time. The `PLAYLIST_URL_ADD_AT_PUBLISH` token is still there too (it's known and gated at publish). Owner: shorts-builder/publisher.

Spelled-out words: none in the transcript. Every "blank" is heard as "blank" (0.0-5.1 "my mind goes blank", 12.28 "that blank moment"), never "blanket". POLICY: none. Everything is cartoon, there are no real people, the logo is the channel avatar, and no frame shows a watermark. Note: the waiting figure in panel 1 is a simple shirtless cartoon in jeans. It's non-sexual and doesn't block, but visuals could ask for a shirt next time.

## Pain -> what the video gives -> gap
Learner quotes (verbatim, PROBLEM 01 synthesis):
- "I can understand 100% of the video, but when I try to speak, my mind goes blank"
- "when I try to speak I forgot every sentence in my mind !! My mind became blank ..."
- "I can write paragraphs in English without any difficulty but as soon as i speak my mind just shuts down"
- "if I try to open my mouth for speak english, its blank. I don't have any idea what i said next"
- "I mostly avoid communicating in a crowd because I dont remember the words. dont know how to make phrases."
- "confidence on talking I forgetting everything as soon as I start talking"

**Pain in one sentence:** "I understand everything, but when I open my mouth my mind goes blank and I can't build the phrase."
**Solved tomorrow means:** I learn each new word inside one full sentence about my life and say that sentence out loud. Then, in a real conversation, I only need to find the word, because the sentence comes with it.

| Pain | Video gives | Gap |
|---|---|---|
| "my mind goes blank" | The hook reads the quote verbatim, voice and card match (0-5.1 s) | None. This is the best hook in the series. |
| Why? | Panel 1: brain juggling 3 labelled balls + a waiting person (11.3-22.6 s) | Clear. The top border of the panel is slightly clipped under the header, which is cosmetic. |
| What fixes it | Voice: "learning words inside full sentences does two of those jobs in advance..." (36.8-48.9 s) | **The picture that proves it is missing** (blocker 1). The screen is blank apart from the strip "With words learned". |
| "dont know how to make phrases" | One example: "I was swamped at work this week." + "swamped = very busy" (57.6-59.3 s) | Good, but the voice never says "this is what I mean". The example lands after "attached" with no bridge. A B1 viewer may not connect it to "learn the word in this sentence". |
| Naming the feeling | freeze, (draw a blank), (tongue-tied), lose your train of thought, stumble over your words | Three are voiced with a scene and work. Two flash by silently in under 0.6 s (blocker 2). |

## Second by second
| Time | Heard | Seen | Note |
|---|---|---|---|
| 0.0-5.1 | "I can understand 100% of the video, but when I try to speak, my mind goes blank." | "…my mind goes blank." + the quote | This stops me: it's my sentence. |
| 6.0-10.6 | "Sound familiar? Well, don't worry, because your memory absolutely isn't broken." | "Sound familiar? / Your memory isn't broken." | Fine. Text only, with the lower 60 % empty. |
| 11.3-22.6 | three jobs, "It's total mental overload." | Panel 1, large and readable | Good sync. |
| 23.9-27.3 | "...job interview answer, you freeze." | freeze picture (a thin band, about 1/5 of the frame) | The picture is small, but fine. |
| 27.5-29.6 | silence | quiz card 0.6 s -> draw a blank 0.3 s -> tongue-tied 0.6 s | **Looks like a glitch. Swipe/confusion risk.** Blocker 2. |
| 29.3-35.7 | train of thought, stumble over your words | matching pictures | Good sync. |
| 36.8-49.0 | "Second, ... two of those jobs in advance ... the grammar is ready." | only "With words learned" strip | **13 s of almost empty screen during the key idea. Main swipe point.** Blocker 1. |
| 50.0-57.0 | "Finally, this leaves only one job left, finding the word. It arrives with its sentence already attached." | "One job left: find the word / It arrives with its sentence." | OK. "only one job left" is a pleonasm the editor accepted. |
| 57.6-59.3 | "I was swamped at work this week." | quote card + "swamped = very busy"; SUBSCRIBE from 58.0 | The animation sits below the caption and covers no text. |
| 59.8-63.8 | "You don't need a better memory. You just need to learn words that come with their sentences." | same text; SUBSCRIBED + yellow bell until about 63 s | Good. |
| 64.5-69.0 | "That's the whole system. Watch the full series from Episode 1 in the Words That Stick playlist." | "Comment the word you always forget" + "Full series from Episode 1: the “Words That Stick” playlist · anotherwordfor.net" | **The series-close line is present** (64.52). The headline is the comment CTA, which the voice never says. That's acceptable (the voice CTA was garbled and cut). |
| 69.3-70.2 | silence | end card | A 0.9 s tail, fine. |

Captions vs audio: they match word for word ("100%", "word's", "practised" UK spelling where whisper writes "practiced", quotes around the playlist name). No wrong caption was seen. Draw a blank and tongue-tied are correctly never captioned (the presenter mispronounced them, and they were cut).

## Takeaway test
"When I learn a new word, I learn it inside one sentence about my life (like 'I was swamped at work this week') and say it out loud." I can name this only from the voice. The screen, which should show "done in advance", is broken, and there's no "Tomorrow:" card like ep05 had. For a finale, a one-line action ("Tomorrow: 1 new word = 1 sentence about you, said out loud") would close the loop.

## Retention risks
- 36.8-49.9 s: an empty screen (blocker 1). This is the biggest swipe risk.
- 27.5-29.6 s: a silent flicker (blocker 2).
- The lower half of the frame is empty in every beat. Synonym pictures are thin bands.
- At 70 s the length is fine for one mechanism. The pace is OK. The 0.9x voice sounds natural.

## Trust risks
- The facts are correct and not overclaimed (no "proven", no anxiety claims). "draw a blank" and "tongue-tied" are shown without meanings. Tongue-tied (nervous/shy) is not the same as forgetting, and the video gives no note on it. That's a minor issue.
- No fake or garbled words in any picture: all pictures use labelled strips only, and the panel-1 labels are spelled correctly.

## Top 3 fixes (by impact)
1. **visuals + shorts-builder (BLOCKER):** re-crop panel 2 to the full "With words learned in sentences" header + the brain/shelf picture with "Done in advance", leaving out the Gemini watermark, and show it for 36.8-49.9 s. Re-render.
2. **shorts-builder + scenario-writer (BLOCKER):** rebuild the 27.5-29.6 s beat. Use one readable quiz (short question, e.g. "Pub quiz. Empty sheet. You draw a …?", at least 1.5 s with countdown 2-1, then the reveal with "= you can't think of the answer" for at least 1 s), within the 3 s silence limit. Move tongue-tied off the silence or drop it.
3. **shorts-builder/publisher (BLOCKER, meta):** add `"subscribe_at": [58.0]` to `content/youtube/ep06.json` and point `video_ids_local` at `words-that-stick-ep06-v2` (or v3 after the re-render, with the new time). Not blocking: scenario-writer/shorts-builder could add a "Tomorrow: 1 word = 1 sentence about you, out loud" sub on the "You don't need a better memory" card.
