# Viewer-critic review: words-that-stick-ep01-v5-podcast-cut (Ep 1 "Never learn a word alone", v5 podcast cut)

- Reviewed: 2026-09-27, glottos-viewer-critic (step 7b)
- Video: `state/shorts/words-that-stick-ep01-v5-podcast-cut/final.mp4` (1080x1920, 30 fps, **85.5 s**)
- Unit: `shorts/units/ep01_v5_podcast_cut.json` (language-gate hash 420b5df9e5a02088)
- Pain source: NotebookLM source 60678678 "PROBLEM 01 — synthesis" (read with `source content`, no query), article `content/articles/p01-why-you-forget-new-words.md` §1–§2, format decision `content/articles/p01-ep01-format.md`
- What I checked: 43 frames on a 2 s grid plus 12 beat midpoints and 3 hook frames (0.1 / 0.8 / 1.5 s) at 360 px; a local faster-whisper small.en transcript of final.mp4 with word timings (cpu_threads=4); ffmpeg scene cuts; the logo against `state/brand/awf-logo-channel.jpg`; a live probe of the CTA target anotherwordfor.net (search for livid / furious / angry).
- What I did not check: the audio mix or loudness by ear (only via the transcript), the real 0.9x ratio (I took it from the unit), YouTube UI overlap on a real phone, and the raw comment volumes (the quotes below come from the synthesis doc).

## Verdict: PARTLY
It explains why words disappear and gives one good rule ("put it in a sentence"). But the viewer never tests themselves. 30 s go to eight C1/C2 anger words that a B1 learner won't use tomorrow. And the closing action sends them to a site where searching "livid" returns "Sorry, but nothing matched your search terms."

## 1. The pain, in the learners' words
Verbatim, from PROBLEM 01 synthesis §3 (names removed):
- "I can understand 100% of the video, but when I try to speak, my mind goes blank"
- "I mostly avoid communicating in a crowd because I dont remember the words. dont know how to make phrases."
- "confidence on talking I forgetting everything as soon as I start talking 😢!"
- "when I start to talk in English I stock up for what i saying hahaha evry words starting forget"
- "when I try to speak I forgot every sentence in my mind !! My mind became blank ..."
- "I can write paragraphs in English without any difficulty but as soon as i speak my mind just shuts down"
- "my brain just went into a wall of white noise, i could access nothing, formulate nothing..."
- "if I try to open my mouth for speak english, its blank. I don't have any idea what i said next"

**The pain in one sentence:** "I learn words and I understand them, but when I have to speak they're gone. I don't remember the words and I don't know how to make phrases."
**What "solved" looks like tomorrow:** the learner does something different with the next new word, e.g. writes one sentence about their own life with it and tests themselves on it later, so it comes back *with a phrase attached* when they speak.

Note: the corpus pain is about words being **gone at speaking time**, not "forgotten within days" in the abstract. The video never mentions speaking.

## 2. Pain → what the video gives → gap
| Pain | What the video gives | Gap |
|---|---|---|
| "every words starting forget" | Forgetting-curve stat (56/66/75 %) and "isn't laziness" at 0–11 s. Good relief line. | Shows the curve but not how to beat it. Recall and review are left to Ep 2. |
| "dont know how to make phrases" | "Give it a scene. Put it in a sentence. He was livid when his flight was cancelled." (18–22 s) | The single most useful line lasts 4 s and is never repeated as the takeaway. The CTA replaces it with "grab five synonyms and a picture for each". |
| "my mind goes blank" when speaking | Nothing about speaking. | No "say it out loud" and no link back to the blank-mind moment. |
| Needs something to do | "Next time you look a word up, grab five of its synonyms and a picture for each … at anotherwordfor.net" | The site doesn't deliver this (see Trust risks). It also turns 1 word into 6 to remember, which adds to the load a forgetting learner already can't carry. |
| Recall beats re-reading (format decision: flip beats for cross / seething / livid / apoplectic) | Not implemented. Each synonym panel shows **both words printed above their pictures before the voice reaches them.** | Zero self-test moments. The one mechanic with the best reach evidence (active recall, 67x / 32.8x views/sub) is missing. |

## 3. Second by second (final timeline, from the whisper transcript + frames)
| Time | Heard | Seen | Viewer reaction |
|---|---|---|---|
| 0.0–4.4 | "Forgetting three out of four new words isn't laziness. It's just human memory at work." | Text-only title card "Why you should never learn a word *alone*" on a plain cream background; caption "Forgetting three out". No picture. | The voice hook is good, straight to the point, and speaks to my problem. **The picture isn't**: frame 1 shows a rule, not my pain, and no image. Moderate swipe risk at 0–1.5 s for anyone scrolling with the sound off. |
| 4.6–11.0 | "We lose 56 percent in an hour, 66 percent in a day, and 75 percent in six days." | "STOP THE LEAK" brain-in-bin infographic, big numbers. | Strongest frame in the video. It stops me. In sync with the voice. |
| 11.4–17.5 | "Learning words in isolation is the issue. Livid equals very angry without context is just noise to your brain." | Tall narrow grey card "Avoid learning words in isolation", small body text, a third of the width empty on both sides. | The second sentence is hard for a B1 listener to parse (no subject; heard as "Livid equals very angry... is just noise"). "In isolation" is teacher jargon. **Swipe risk ~13–17 s.** |
| 18.1–26.2 | "Give it a scene. Put it in a sentence. He was livid when his flight was cancelled. Attaches a situation to a feeling, creating a solid memory anchor." | "USE THE SENTENCE HOOK INSTEAD" brain on a fishing line with a safe. | "Put it in a sentence" is the gold. "Attaches a situation…" has no subject and "memory anchor" is jargon. OK overall. |
| 27.0–35.7 | "Finally, use the synonym spin so they hold each other up. Don't learn livid alone. Assign a specific picture to each synonym, mild to extreme." | **8.7 s static text card** "The synonym spin / One picture for each word, from mild to extreme". | "Finally" at 27 s makes me think it's ending, but 58 s are left. "Synonym spin" is a brand term I don't know, "they" has no referent, and there's no picture for 9 s. **Highest single swipe point: 27–31 s.** |
| 35.7–41.3 | cross = mum and muddy shoes; irate = customer at the service desk | "One word, eight pictures" + CROSS → IRATE panel (both words already on screen) | Nice pictures, but tiny (a ~340 px-tall band in a 1920 px frame, lower 45 % of the screen empty). The arrow reads as "cross turns into irate". Both answers are shown before I can guess. |
| 41.9–50.1 | fuming = traffic, steam; seething = silent in a meeting, jaw clenched | FUMING → SEETHING | Same pattern again. I now know the rhythm, and nothing asks anything of me. |
| 51.2–56.7 | furious = slamming a door; livid = pale with rage, flight cancelled | FURIOUS → LIVID | **Swipe risk peaks ~50–56 s**: fifth and sixth word in the same cadence, no payoff in sight. |
| 57.4–65.2 | incensed = unfair headline; apoplectic = red-faced, can't even speak | INCENSED → APOPLECTIC | "Incensed" and "apoplectic" are words a B1 learner will not use this year. They feel like vocabulary-show-off, not help. |
| 65.9–70.5 | "Remembering one picture pulls up the whole family. Proving synonyms are for nuance, not decoration." | Text card "One word, eight pictures." + the ladder in small grey type | Abstract, and the second line is a fragment. Nothing to do. |
| 71.3–85.5 | "So to beat the forgetting curve, never learn a word alone. Next time you look a word up, grab five of its synonyms and a picture for each in seconds at anotherwordfor.net, and tune in for episode two to find out why rereading your word list doesn't work." | **14 s static CTA card** "Never learn a word alone." + a small grey subline | The instruction sits in one 37-word run-on sentence. The Ep 2 tease ("why rereading your word list doesn't work") is the best hook in the video, and it comes at 81 s, after most scrollers have left. |

User preferences: straight to the point (first word is the pain, no intro) ✓. No podcast markers ("This is the brief", Ebbinghaus / who-said-what, dangling "Second," are gone, and whisper confirms none are audible) ✓. Podcast voice at 0.9x (per unit, clear, whisper made 0 errors apart from "anotherword4") ✓. Synonym spin present ✓. Logo matches the official channel avatar ✓. No Gemini/NotebookLM watermark seen in any frame ✓.

## 4. Takeaway test
The one action a viewer can name after watching: "Next time I look up a word, find five synonyms and a picture for each."
- It is **not** the fix for forgetting. There's no recall and no review; the video itself says that's Ep 2.
- The tool it points to doesn't provide it (see below).
- The better action, "put it in one sentence", is said once at 19 s and dropped.
→ So the verdict is capped at PARTLY.

## 5. Retention risks
- **Length vs content:** 85.5 s for 2 ideas (curve + sentence) plus a 30 s list. The format decision budgeted about 62 s and warned about going past 60 s.
- **Static text:** 0–4.6, 27–35.7, 65.9–85.5 s = **about 32 s of 85 (38 %) are text-only cards** with no image.
- **Repetition of cadence:** 8 x "[Word] is [scene]" in 30 s with identical pair panels, and no rise or turn.
- **Pacing:** about 2.8 words/s with 0.5–1.0 s gaps after every sentence. Comfortable for B1 comprehension, but with 85 s total it feels slow. The 0.9x setting is right for the voice. The script length is the problem, not the speed.
- **Legibility:** captions (1–3 words, centred) are easy to read. Panel text inside the isolation card and the recap ladder subline is small, and the pictures use about a third of the frame's height.
- **Picture/voice sync:** good. Panel changes land within ~0.3 s of the spoken word (4.6 / 11.4 / 18.1 / 27.0 / 35.7 s…). But the pair panels show the **next** word before it's spoken (spoiler).

## 6. Trust risks
1. **The CTA fails on contact.** Probed live on 2026-09-27: `anotherwordfor.net/?s=livid` → "Sorry, but nothing matched your search terms."; `?s=furious` → same; `?s=angry` → one unrelated post, "Another Word For Great". No per-synonym pictures anywhere. "Grab five synonyms and a picture for each **in seconds** at anotherwordfor.net" is an overclaim a viewer can disprove in 10 seconds.
2. **The numbers apply to nonsense syllables.** Ebbinghaus measured DAX/BOK syllables, and the article itself says meaningful material fades more slowly. "We lose 56 percent in an hour" is stated as a fact about the viewer's words. The user chose to keep the percentages; it's still a trust risk with any viewer who knows the study.
3. **Unsupported claim:** "Remembering one picture pulls up the whole family." There's no source, and it's the video's main argument for the spin.
4. **Ladder order is contestable.** Irate (= very angry) sits next to "mild" cross; the language editor already blocked the "Mild" label over IRATE in v4, but the arrows still imply a step from cross to irate. "Incensed" above "livid" is also debatable.
5. **Unnatural or garbled English as heard:** "Livid equals very angry without context is just noise to your brain." / "Attaches a situation to a feeling, creating…" (no subject) / "so they hold each other up" (no referent) / "Proving synonyms are for nuance, not decoration." (fragment). For a channel that sells *better English*, the voice has to model complete sentences.
6. "One word, eight pictures" is shown over the cross/irate panel, but it's eight *words*. That confuses a B1 reader.

## 7. Top 3 fixes (by impact)
1. **Make the ending an action that works tomorrow, and stop promising what the site doesn't have.** Owners: scenario-writer, language-editor (re-gate). End on: "Tonight, take one new word. Write one sentence about *your* life with it. Picture the scene." Keep anotherwordfor.net as "find the word's synonyms" only if a real page answers (today it doesn't for livid, angry or furious; that is a site/SEO problem to raise with the owner, not a video fix). Say it as 2–3 short sentences, not one 37-word run-on, and move the Ep 2 tease up.
2. **Put the self-test in (the format decision's flip beats), with word-masked pictures.** Owners: visuals (per-cell crops with the word cut off), shorts-builder (flip/reveal beat + inserted silence in the podcast track, 1.3 s "Which word?" pause). At minimum: cross, seething, livid, apoplectic as quiz flips, and never show the next word before it's spoken. This is the only moment a scroller *does* something, and it's the episode's own lesson.
3. **Cut to ≤60 s and remove the dead cards.** Owners: scenario-writer (script), shorts-builder (layout). Open on the curve panel with the pain as on-screen text ("You'll lose 3 of 4 new words by next week") instead of a text-only title. Drop the 8.7 s "synonym spin" card and the "Proving synonyms…" recap. Cut the ladder to 4–5 words with B1 value (e.g. cross, fuming, furious, livid), or move all 8 to the planned "Picture test: 8 kinds of angry" spin-off. Scale the pictures up to fill the empty middle of the frame. If the NotebookLM recording can't be re-cut into complete sentences, re-script those lines for a new brief audio or TTS pickups (voice) rather than shipping fragments.
