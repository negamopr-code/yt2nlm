# P01 · Episode 6 "My mind goes blank": format decision (glottos-format-strategist, 2026-09-27)

Source: article §7 (+ the learner quote in the intro), episode map row 6. Evidence is reused from `p01-ep01-format.md`, plus a quota-free `source content` read of the PROBLEM 01 synthesis (60678678). No query and no generation in this run.

## 1. Episode in one line
"I can understand 100 % of the video, but when I try to speak, my mind goes blank." → the blank mind = your brain doing 3 jobs at once (find the word, check if it fits, build the grammar) while someone waits → the sentence method removes 2 of them in advance (you know its setting, you practised the sentence) → the word arrives with its sentence → the "mind goes blank" family (freeze … lost for words) → "Comment the word you always forget" → CTA + series recap.

## 2. Decision: INFOGRAPHIC PANELS (visual mental model) + picture reveals; comment CTA; mind map for the series
| Part | Format | Why |
|---|---|---|
| Hook = learner quote | card with the **verbatim** comment in quotes (no name) | The empathetic pain callout is the biggest hook pattern in the dataset: "Forget Words When Speaking English? Here Is Why!" 8.38 M views; "Do you forget words when you speak English" 3.4× reach, 4.69 % engagement. The corpus has a dozen near-identical "mind goes blank" quotes. |
| 3 jobs → 2 removed | **2 infographic panels**: (a) brain juggling 3 labelled jobs + a waiting listener; (b) the same with 2 jobs ticked "done in advance" | A mechanism shown as a visual mental model: the synthesis's high-spread openings ("ocean surface" memory, Luca Lampariello's "word spider web"). |
| Synonym spin "mind goes blank" | picture reveals; 3 optional flips (tongue-tied, clam up, lost for words) | Picture association (rank 3). The phrases name the exact feeling (freeze, tongue-tied), so the comment prompt lands. |
| CTA | card: "Comment the word you always forget" + series recap line | Rank 5 (output/self-talk) and the pain callouts have the highest engagement %. This is the finale, so it drives comments. |

**Quiz beat: NICE-TO-HAVE** (3 picture flips in the spin). The episode is a mechanism + an emotional payoff; the comment is the interaction.

**Length: SHORTER is better.** One mechanism. Target 65–80 s after 0.9× and cuts.

**Extra (series finale, not in the Short):** a **mind map** of the 6 rules as the pinned comment / series thumbnail / playlist cover (heuristic: series overview → mind map). Command below, optional.

## 3. Rejected alternatives
- **Quiz-led Short:** nothing here is a single right answer except the spin.
- **Two-host debate "is it anxiety or memory?":** it drifts into anxiety/therapy claims the article doesn't make. The single-host rule applies anyway.
- **Screen-record product demo (the RU→FR hooks in `state/tiktok-hooks-ponimayu-no-ne-govoryu.md`):** that's the Glottos product funnel, not this AWF series; AWF has no speaking feature to show.
- **Paraphrased hook** "I understand everything… then my mind goes blank" (episode map): in quote marks it pretends to be a quote. Use the article's verbatim comment, or drop the quote marks.

## 4. Synonym spin: "my mind goes blank" family (8 pictures)
| # | Word/phrase | Scene | Notes for the language editor |
|---|---|---|---|
| 1 | freeze (up) | A job interview: the candidate turned to ice mid-answer, the interviewer waiting | "I froze." |
| 2 | draw a blank | A pub quiz: pen hovering over an empty answer sheet | "I drew a blank on her name." |
| 3 | tongue-tied | Talking to a crush at a party, a literal knot in the tongue | nervous/shy; flip candidate |
| 4 | lose your train of thought | Telling a story at dinner; a small train drives away out of the thought bubble | |
| 5 | clam up | Asked a personal question, the person snaps shut like a clam shell | goes quiet ON PURPOSE / from nerves: different from forgetting. Flip candidate. |
| 6 | choke | A footballer missing an easy penalty in a final | ⚠ informal; fail under pressure, not only speech. Check that it fits the set. |
| 7 | stumble over your words | Giving a wedding toast, tripping over big letter blocks | |
| 8 | lost for words | A surprise party: the person gasping, hand over mouth | ⚠ usually surprise or emotion, often POSITIVE. Not the same as a blank mind. Say "avoid when" in the reveal. Flip candidate. |
Distinct settings: interview / quiz / party-crush / dinner / personal question / football / wedding / surprise party. Note: the party-crush and the surprise party are both parties. Make the surprise party very visual (balloons, "SURPRISE" banner with no text, just balloons) so the fronts don't collide.

## 5. Beat outline
1. Card: the verbatim quote **"I can understand 100% of the video, but when I try to speak, my mind goes blank."** (the host reads it; no name)
2. Card: "Your memory isn't broken. Your brain is doing three jobs at once."
3. Panel (a): brain juggling **Find the word · Check if it fits · Build the grammar** + someone waiting
4. Panel (b): **Check if it fits ✓ · Build the grammar ✓** "done in advance"; **Find the word** stays
5. Card: "You practised it in a sentence. You know its setting. You've said it out loud."
6. Card: "The word arrives with its sentence attached."
7–14. Spin: "What it feels like, in 8 pictures": freeze → draw a blank → tongue-tied → lose your train of thought → clam up → choke → stumble over your words → lost for words (~3 s each)
15. Card: **"You don't need a better memory. You need words that come with their sentences."**
16. CTA: "Comment the word you always forget" · anotherwordfor.net · (optional) "Series recap in the pinned comment"

## 6. NotebookLM commands (run LATER, after `content/articles/p01-ep06-audio-script.md` is written and approved)
```sh
N="docker exec -w /workspace/glottos-marketing -e NLM_PROFILE=drawnformula glottos-marketing .nlmvenv/bin/nlm"
NB=8306c0a9-1418-41e2-a988-1c0459eafc89
$N source add $NB --file content/articles/p01-ep06-audio-script.md --title "AUDIO SCRIPT — Ep06 The blank mind" --wait --profile drawnformula   # → SRC06
$N audio create $NB --format brief --length short --language en --source-ids SRC06 -y --profile drawnformula --focus "Perform the AUDIO SCRIPT source as ONE presenter, word for word and in order. Keep it short. Use only its facts and examples. Add no statistics or studies, no names of researchers, universities, commenters or years, and no medical or anxiety claims. Your very first words are the quote on the script's first line, read as a quote. Never use podcast markers: no 'This is the brief', no 'debrief', no 'welcome', no 'today we', no 'in this episode', no 'let's dive in', no 'on this show', no mention of listeners, hosts, podcasts, shows or episodes, and no sign-off such as 'that's it for today', 'thanks for listening' or 'see you next time'. The three jobs are exactly: find the word, check if it fits, build the grammar. The sentence method removes two of them in advance: checking the fit and building the grammar. Read the eight phrases in the script's order, one short picture each, and say that lost for words is usually about surprise, not forgetting. End with the script's last line: comment the word you always forget, and another word for dot net. Never say 'naked' or 'literally'."
$N infographic create $NB --orientation portrait --style instructional --detail concise --language en --source-ids SRC06 -y --profile drawnformula --focus "Portrait infographic, exactly 2 panels stacked vertically with a white gap between them. Title exactly: 'Why your mind goes blank'. Panel 1: a cartoon brain juggling three balls labelled exactly 'Find the word', 'Check if it fits' and 'Build the grammar', while a person waits with a speech bubble containing only '...'. Panel 2 headed exactly 'With the sentence method': the same brain holding only one ball, 'Find the word'; the other two, 'Check if it fits' and 'Build the grammar', sit on a shelf with a tick and the label exactly 'Done in advance'. Print no other text, numbers, percentages or names. Never print 'neural', 'anxiety', 'cure', 'proven' or 'naked'. Check the spelling of every word."
$N infographic create $NB --orientation portrait --style bento_grid --detail concise --language en --source-ids SRC06 -y --profile drawnformula --focus "Portrait picture sheet. Title exactly: 'Mind gone blank: 8 pictures'. 8 separate cards on a white background with clear white gaps between them, 2 columns, 4 rows. Each card = one picture on top and, underneath it in a solid coloured strip at the bottom of the card, ONLY the word or phrase given here. In this order: 1 'freeze' - a job-interview candidate turned to ice mid-answer, the interviewer waiting; 2 'draw a blank' - a pub quiz, a pen hovering over an empty answer sheet; 3 'tongue-tied' - a nervous person at a party talking to someone they like, their tongue drawn as a knot; 4 'lose your train of thought' - a person telling a story at dinner while a small toy train drives out of their thought bubble; 5 'clam up' - a person asked a personal question, drawn closing like a clam shell; 6 'choke' - a footballer missing an easy penalty in a final; 7 'stumble over your words' - a man giving a wedding toast, tripping over big letter blocks; 8 'lost for words' - a person at a surprise party with balloons, gasping with a hand over their mouth. Print NO labels such as positive, negative, mild, strong, formal, informal or casual. No scales, arrows, rankings, numbers except the title's 8, no example sentences. No text anywhere except the title and the 8 phrases."
# OPTIONAL series extra (pinned comment / playlist cover), after all 6 scripts are sources:
$N mindmap create $NB --title "Words That Stick: 6 rules" --source-ids SRC01,SRC02,SRC03,SRC04,SRC05,SRC06 -y --profile drawnformula   # SRC01 = Ep01 audio-script source 72c8e8e7-…; mindmap has NO --focus flag, so the sources alone drive it; output must pass the language editor
```
The language editor gates all text. **Any leftover podcast marker is cut from the audio at acoustic boundaries** (`audio.cuts`), not re-voiced.

## 7. Builder features this episode needs
| Feature | Status | Need |
|---|---|---|
| Per-cell crops: 2-panel mechanism sheet + 8-card sheet | `panels()` for the stacked panels; `grid` untested on the sheet | needed |
| Quote card style (large quote marks, italics, no attribution) | missing; `card()` works with plain quotes | nice-to-have |
| Word-masked crop + quiz beat + inserted silence (1.5 s) for 3 picture flips | missing | nice-to-have |
| Tick/strike animation over the 3 jobs | missing (2 static panels do it) | nice-to-have |

## 8. Flags for the language editor / article writer
- Which two jobs are removed: §7 says "removes two of those jobs" but then lists three things practised. My mapping (fit + grammar removed, finding the word remains) is an interpretation. Confirm before the infographic is generated.
- Hook quote must be verbatim (article intro), not the episode map's paraphrase.
- choke (informal, sport) and lost for words (positive surprise): keep them with honest "avoid when" notes, or drop them if the editor thinks they blur the set.
