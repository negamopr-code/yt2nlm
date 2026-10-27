# M1 retitle gate (GNH19NdTu9U, m1-v3.mp4, 5:32), 2026-10-15

Gate: glottos-language-editor. Input: content/youtube/m1-retitle-plan-20261015.json (new_title, new_description) and content/youtube/m1-thumb-20261015.jpg.
Evidence: critic-v3.md transcript timings (faster-whisper small.en), yt-meta-gate-v3.md, script.md, and frames I pulled from m1-v3.mp4 at 0:00.5, 0:15.5, 0:36.5, 1:20.5, 2:14.5, 3:25.5, 4:23, 4:50. Every chapter frame shows the matching slide: title card, 5-word table, DAX/CONNECTION, "Use the word", "Never learn a word alone", "Timing and recall", Anchor/Review/Speak card, "What is the word for very angry?". YouTube and NotebookLM were not touched.

## Verdict: APPROVED after 3 edits (made in the plan JSON; old_title and old_description were left as they were)

| Line | Problem | Fix | Confidence |
|---|---|---|---|
| Title "Stop Forgetting New English Words: 3 Easy Steps" | none. It's idiomatic, 47 characters, has no < or >, and "three easy steps" is spoken at 1:17 | none | high |
| Line 1 "...3 easy steps to remember new vocabulary for good." | "for good" means permanently, which is an overclaim. The video only says that each review on days 1, 3 and 7 makes the curve fall more slowly. Also, "new English words ... new vocabulary" ended on a promise the video never makes | "Stop forgetting new English words: 3 easy steps to help you remember new vocabulary." | high |
| 0:00 "Why new words are gone by Friday" | The hook (0:00-0:15) states the problem ("by Friday, it's gone ... the method is" broken) but explains no "why". The why is the 0:36 chapter, so this label promised the wrong thing | "0:00 Learned on Monday, gone by Friday" | high |
| 3:25 "Step 3: Recall on days 1, 3 and 7" | This is inaccurate. On day 1 you re-read the word in its sentence, on day 3 you recall it, and on day 7 you use it in new sentences. Only day 3 is recall | "3:25 Step 3: Recall and review on days 1, 3 and 7" | medium-high |
| 0:15 The 5-word challenge / 0:36 Why some words fade fast / 1:20 Step 1: Use the word / 2:14 Step 2: Learn it inside a sentence / 4:22 A 15-minute routine / 4:49 The 5-word test | none. The labels match the voice and the slides. "Why some words fade fast" fits the DAX/BOK vs. meaning contrast | none | high |
| Chapter validity | none. There are 8 chapters, the first is 0:00, they ascend, and the shortest is 4:22-4:49 (27 s). The last runs 4:49-5:32 | none | high |
| Body (hook, 3 steps, routine, CTA, link, Roediger & Karpicke) | none. Unchanged from the version approved in yt-meta-gate-v3.md | none | high |
| Thumbnail "WORDS THAT STICK" + "Livid = Very Angry" tag into a bin | none. The text is natural, the caps are on the image only and never spoken, and it matches the 0:36-1:20 "brain clears isolated labels" idea. The small NotebookLM label "recycled" is barely legible but acceptable | none | medium-high |

Not done: no fresh transcription (no faster-whisper or ffmpeg in glottos-autopilot/glottos-marketing; I took frames with the ffmpeg in the video-compressor container). The chapter times rest on frames plus the critic-v3 transcript timings. lang_gate.py approve does not apply (this is metadata, not a unit). No caps check was needed because none of this is spoken.
