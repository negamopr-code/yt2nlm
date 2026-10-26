# Ep3 YouTube metadata gate (content/youtube/ep03.json vs words-that-stick-ep03-v2)

Gate: glottos-language-editor, headless autopilot step "episode 3: yt_meta_gate". Stamp: 2026-10-26T03:58:54Z (in ep03.json "language_approval").
Verdict: APPROVED, after one small edit.

Upload file: content/episodes/E3/e3-v2.mp4 (78.2 s, 9:16). sha256 0c3d4ef016e8f96a997eb02d66f1e118ceef436da6a33af69fd4a706dd3f6d55, the same as /workspace/glottos-auto/out/words-that-stick-ep03-v2.mp4.

Sources:
- My own faster-whisper small.en transcript (int8, one full pass). Working files are in /tmp/ep03m, outside the repo.
- PyAV frames at 3, 8, 12, 17, 20, 24, 28, 34, 40, 45, 48, 52, 57, 59, 63, 68 and 75 s.
- Critic report content/reviews/words-that-stick-ep03-v2.md.

## Heard (summary)
- 0-6 s: "Review new words on these three days only. A word sticks best when you recall it just before you forget it."
- Day 1: see the word again in its sentence.
- Day 3: cover it up and recall it before you look.
- Quiz: "You know her face, but not her name. Recognize or recall? ... you recognize the face, you just can't recall the name."
- Day 7: use it in a new sentence of your own, out loud.
- "Each review resets the forgetting curve, and it falls more slowly each time. By day seven, a word you used yourself is much harder to forget."
- Five words: a good handshake is firm, a steady ladder is sturdy, hiking boots that last for years are durable, a huge old oak tree is mighty, a weightlifter's arms are muscular.
- Recap: "days one, three, and seven, not every day, and not just once." Then the CTA "Tomorrow, see today's new words again in their sentences", the link, and the teaser "Next, why you freeze mid-sentence."
- The frames match. Each of the 5 words has its own picture card, and there is a "The Rule" card with Day one/three/seven.

## Checks
| Item | Result |
|---|---|
| Title (75 chars) | Natural, matches the opening line and the card. Not misleading. PASS |
| Day 1/3/7 bullets | Match the audio and cards. PASS |
| "After Day 7, a word you've used yourself..." | Video says "By day seven". EDIT: "By Day 7, a word you've used yourself is much harder to forget." |
| Face/name quiz | Matches. PASS |
| 5 "strong" words + pictures | All 5 match the audio and frames, and every sense is correct. PASS |
| "Screenshot the schedule." | A viewer CTA, not a claim about the video. The rule card is on screen. Kept. |
| Teaser | Heard at about 76 s. PASS |
| Citation | Cepeda, Pashler, Vul, Wixted & Rohrer (2006), Psychological Bulletin 132(3), 354-380 (PMID 16719566, doi 10.1037/0033-2909.132.3.354). Verified. The claim is limited to "spacing beats cramming", and 1-3-7 is presented as a practical rule. PASS |
| Link | https://anotherwordfor.net/another-word-for-strong/ gives HTTP 200 with curl -k. PASS |
| Spelling | British "recognise" is used throughout, consistent with the cards. PASS |
| Policy | No sexual or unsafe content. "Muscular arms" is a clean, factual example. No real people. made_for_kids false. PASS |
| subscribe_at | [61.1] is present in the JSON and absent from the description. PASS |

## Not checked
- I did not watch the video at full frame rate. Frames were sampled.
- I did not run a NotebookLM query (none was needed).
