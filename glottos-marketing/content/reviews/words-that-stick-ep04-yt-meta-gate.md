# Ep4 YouTube metadata gate (content/youtube/ep04.json vs words-that-stick-ep04-v2)

Gate: glottos-language-editor, step "episode 4: yt_meta_gate". Stamp: 2026-10-26T08:35:17Z (in ep04.json "language_approval").
Verdict: APPROVED, after two small edits.

Upload file: content/episodes/E4/e4-v2.mp4 (75.2 s, 9:16). sha256 2f3869aa4793c7dc906b51ab5704a4ff642eafb9b20d4bec8a13823925201862, the same as /workspace/glottos-auto/out/words-that-stick-ep04-v2.mp4.

Sources:
- My own faster-whisper small.en transcript (int8, one full pass, .nlmvenv). Working files are in /tmp/ep04m, outside the repo.
- PyAV frames at 1, 5, 14, 20, 25, 30, 35, 40, 46, 52, 56, 59.5, 62, 66 and 72 s.
- Critic report content/reviews/words-that-stick-ep04-v2.md (SOLVES; its only blocker, subscribe_at + video_ids_local, is now fixed in ep04.json).

## Heard (summary)
- Hook: "This is why you freeze mid-sentence. It's not that you forgot the vocabulary word. You're just not sure if it fits the setting. Is this word too formal? Is it rude or is it too dramatic?"
- swamped: fine at work, not for one or two small tasks. livid: too dramatic for someone slightly annoyed. let me look into that: suits emails and meetings, weird in chats with friends.
- Five ways to say help, casual to formal: friends moving a sofa / give me a hand (quiz: casual); neighbour with shopping / help, fine anywhere; IT team fixing a laptop / support; hotel receptionist / "How may I assist you?" (quiz: formal, stiff with friends); lorries after a flood / aid.
- Rule "Learn the setting, not just the meaning", CTA "Tomorrow, next to each new word, write where it fits. Like friends, work, or both", link line, teaser "Next, the 15-minute routine."
- Frames match: every word has its own picture card; rule, tomorrow and CTA cards present; subscribe animation at 58-63 s.

## Checks
| Item | Result |
|---|---|
| Title (74 chars) | Natural; matches the spoken hook and title card. Not misleading. PASS |
| Opening lines | Match 0-11 s. PASS |
| "livid: a bit dramatic" | Understates the word (livid = extremely angry, Cambridge/Merriam-Webster). EDIT: "livid: very angry. Avoid it when someone is just slightly annoyed." |
| swamped / let me look into that | Match audio; senses correct. PASS |
| 5 "help" words + pictures | All 5 match audio and frames; order casual -> formal; senses and register correct. "common at work" and "on the news" are true extra notes, not contradicting the video. PASS |
| "Try it tomorrow: ... write where it fits: friends, work, or both." | Two colons in one sentence. EDIT: "... write where it fits (friends, work, or both)." |
| Teaser | "Next, the 15-minute routine" heard at 72.9 s, on the CTA card. PASS |
| Link | https://anotherwordfor.net/another-word-for-help/ gives HTTP 200 with curl -k. PASS |
| Spelling | British (neighbour, lorries) consistent with the captions/cards. PASS |
| Tags | Natural, relevant, no misleading tags. PASS |
| Policy | No sexual or unsafe content, no real people, made_for_kids false. POLICY: none. PASS |
| subscribe_at | [58.0] present in JSON (matches e4-v2.subscribe.json), absent from the description. video_ids_local = words-that-stick-ep04-v2. PASS |

## Not checked
- Video not watched at full frame rate; frames sampled.
- No NotebookLM query used (none needed). lang_gate.py approve n/a (metadata only, no beats).
