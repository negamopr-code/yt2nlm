# P01 · Episode 4 "This is why you freeze mid-sentence": format decision (glottos-format-strategist, 2026-09-27)

Source: article §5, episode map row 4. Evidence is reused from `p01-ep01-format.md`, plus a quota-free `source content` read of the PROBLEM 01 synthesis (60678678). No query and no generation in this run.

## 1. Episode in one line
You freeze not because you forgot the word but because you're unsure it fits (too formal? too rude? too dramatic?) → learn each word's register and when to avoid it: swamped / livid / let me look into that → the "I don't know" ladder from friends to work, as a "Friends or work?" guessing game → Rule 4 "Learn the setting, not just the meaning" → CTA.

## 2. Decision: QUIZ-LED Short ("Friends or work? Guess before it flips"), register shown as builder text
| Part | Format | Why |
|---|---|---|
| Hook + the doubt | card → 1 infographic panel (a speaker mid-sentence with 3 doubt bubbles) | Pain callout: "Forget Words When Speaking English? Here Is Why!" 8.38 M views; "Do you forget words when you speak English" 3.4× reach, 4.69 % engagement. |
| 3 article words | **3 word cards (builder text): word · register · example · avoid when** | This is the AWF wedge. The synthesis gap table: thesaurus sites list synonyms "without register tags, example sentences or 'avoid when' guardrails". **Register tags are never rendered by NotebookLM.** In Ep1 it printed "Mild" over IRATE, and register is exactly the kind of label it gets wrong. |
| "I don't know" ladder | **quiz beats**: the phrase on a card + "Friends or work?" → 2.0 s silent pause → reveal = picture + register chip + avoid-when line; 3 quiz + 3 straight reveals | Nuance/comparison formats get strong reactions on TikTok: "Difference between these English terms" 3.6 M likes; "Last one's tricky / Test your word choice" 537.3 K. Guessing the setting is the episode's own skill. |
| Rule 4 + CTA | card | |

**Quiz beat: ESSENTIAL** (the episode's promise is "guess before it flips", and the skill taught is judging fit).

**Length:** this is the densest episode. The podcast will likely run 100–115 s at 0.9× plus 3 × 2.0 s pauses. Acceptable under the 3-minute limit, but it's the longest in the series. To keep it tight, the 3 article words get one compact card each (word · register · avoid when; the example sentence is voiced, not printed in full). If it runs over ~120 s, drop the straight reveals for "Let me check" and "I'll get back to you on that". Don't drop the quiz.

## 3. Rejected alternatives
- **Infographic "register cards" from NotebookLM** (the episode map's visual): NotebookLM would print the register labels, which is the highest-risk text in the series (see the Ep1 "Mild"/IRATE block). Pictures come from NotebookLM; tags come from the builder, which the language editor gates.
- **Data table (phrase × register × avoid when):** good as a **pinned comment / description block**, too dense for 9:16 motion.
- **3-way "casual / neutral / formal?" question:** the neutral middle has no single right answer (the Ep1 lesson). The binary "Friends or work?" is only asked for phrases with a clear answer. The middle phrases get straight reveals that say "fine in both".
- **Two-host debate:** user rule is single-host brief.

## 4. Synonym spin: "let me look into that" ↔ other ways to say "I don't know" (6 pictures, friends → work)
| # | Phrase | Scene | Register (builder chip) | Avoid when (builder line) | Quiz? | Notes for the language editor |
|---|---|---|---|---|---|---|
| 1 | Beats me. | Friends on a sofa; one asks how the film ended, the other shrugs with popcorn | casual | with your boss or a customer: it can sound like you don't care | **QUIZ → friends** | check "informal" tag |
| 2 | Your guess is as good as mine. | Two tourists staring at a paper map at a crossroads | casual | you're the one who is supposed to know (e.g. a customer asks you) | reveal | |
| 3 | Let me check. | A friend asks "Free on Saturday?"; the person looks at their phone calendar | neutral: fine in both | — (safe almost everywhere) | reveal ("fine in both") | |
| 4 | Let me look into that. | Meeting table; a manager asks for numbers; the person makes a note on a laptop | professional | chatting with friends about personal preferences (article) | **QUIZ → work** | article's phrase |
| 5 | I'll get back to you on that. | Typing an email reply: "I'll get back to you on that by Friday." | professional | you have no plan to follow up: it's a promise | reveal | |
| 6 | I'm afraid I don't have that information at the moment. | Call-centre agent with a headset, polite smile | formal, polite | with friends: it sounds cold | **QUIZ → work** | ⚠ "to hand" is British; "at the moment" is safer. Check. |
All register and avoid-when lines are MY proposals. **Every one needs the language editor's check** (dictionary register labels) before rendering. Scenes are distinct by setting (sofa / street map / phone calendar / meeting / email / call centre). The setting IS the register, which is the lesson.
The 3 article words (card beats, text verbatim from §5): **swamped** (casual to professional, fine at work · avoid when you only have one or two small tasks) · **livid** (neutral, a bit dramatic · avoid when someone is just slightly annoyed) · **let me look into that** (professional, emails and meetings · avoid when chatting with friends about personal preferences).

## 5. Beat outline
1. Card: **"This is why you freeze mid-sentence."**
2. Panel: speaker mid-sentence, 3 doubt bubbles "Too formal?" "Too rude?" "Too dramatic?"
3. Card: "You didn't forget the word. You're not sure it *fits*."
4. Word card: swamped · casual to professional · avoid when: one or two small tasks
5. Word card: livid · neutral, a bit dramatic · avoid when: just slightly annoyed
6. Word card: let me look into that · professional · avoid when: chatting with friends
7. Card: "Same meaning, different setting: 6 ways to say *I don't know*"
8. QUIZ: "Beats me." · Friends or work? · 2.0 s · reveal: sofa picture + "casual" + avoid-when
9. Reveal: Your guess is as good as mine (map picture + chip)
10. Reveal: Let me check (calendar picture + "fine in both")
11. QUIZ: "Let me look into that." · 2.0 s · reveal: meeting picture + "work"
12. Reveal: I'll get back to you on that (email picture)
13. QUIZ: "I'm afraid I don't have that information at the moment." · 2.0 s · reveal: call-centre picture + "formal"
14. Card: **Rule 4 — Learn the setting, not just the meaning.**
15. CTA: every word on anotherwordfor.net comes with a sentence and an avoid-when note · "Next: the 15-minute routine"

## 6. NotebookLM commands (run LATER, after `content/articles/p01-ep04-audio-script.md` is written and approved)
```sh
N="docker exec -w /workspace/glottos-marketing -e NLM_PROFILE=drawnformula glottos-marketing .nlmvenv/bin/nlm"
NB=8306c0a9-1418-41e2-a988-1c0459eafc89
$N source add $NB --file content/articles/p01-ep04-audio-script.md --title "AUDIO SCRIPT — Ep04 Know the word's setting" --wait --profile drawnformula   # → SRC04
$N audio create $NB --format brief --length short --language en --source-ids SRC04 -y --profile drawnformula --focus "Perform the AUDIO SCRIPT source as ONE presenter, word for word and in order. Use only its facts, examples, register notes and avoid-when notes, and invent no new ones. Add no statistics or studies, and no names of researchers, universities or years. Your very first words are the script's first line: 'This is why you freeze mid-sentence.' Never use podcast markers: no 'This is the brief', no 'debrief', no 'welcome', no 'today we', no 'in this episode', no 'let's dive in', no 'on this show', no mention of listeners, hosts, podcasts, shows or episodes, and no sign-off such as 'that's it for today', 'thanks for listening' or 'see you next time'. QUIZ LINES: read the phrase, then ask 'Friends or work?' and stop; then say the answer as its own new sentence, for example 'Work.' Never give the answer before or inside the question. Read the six ways to say I don't know in the script's order, from friends to work. End with the script's last line: another word for dot net. Never say 'naked' or 'literally'."
$N infographic create $NB --orientation portrait --style instructional --detail concise --language en --source-ids SRC04 -y --profile drawnformula --focus "Portrait infographic with exactly 1 panel plus a title. Title exactly: 'Why you freeze mid-sentence'. Picture: a person speaking to a colleague, stopped mid-sentence, with exactly three thought bubbles containing exactly 'Too formal?', 'Too rude?' and 'Too dramatic?'. Print no other text: no register labels, no word lists, no numbers, no names. Never print 'naked', 'anxiety disorder' or 'neural'. Check the spelling of every word."
$N infographic create $NB --orientation portrait --style bento_grid --detail concise --language en --source-ids SRC04 -y --profile drawnformula --focus "Portrait picture sheet. Title exactly: '6 ways to say I don't know'. 6 separate cards on a white background with clear white gaps between them, 2 columns, 3 rows. Each card = one picture on top and, underneath it in a solid coloured strip at the bottom of the card, ONLY the phrase given here. In this order: 1 'Beats me.' - friends on a sofa, one shrugging with popcorn after a film; 2 'Your guess is as good as mine.' - two tourists staring at a paper map at a crossroads; 3 'Let me check.' - a person looking at the calendar on their phone; 4 'Let me look into that.' - a meeting table, a person making a note on a laptop while a manager asks a question; 5 'I'll get back to you on that.' - a person typing an email reply; 6 'I'm afraid I don't have that information at the moment.' - a call-centre agent with a headset, smiling politely. IMPORTANT: print NO register or tone labels anywhere - never write casual, informal, neutral, professional, formal, polite, rude, friends, work, mild or strong. No scales, arrows, rankings, numbers or example sentences. No text anywhere except the title and the 6 phrases."
```
The language editor gates all text, including the phrases in the images (punctuation, apostrophes). **Any leftover podcast marker is cut from the audio at acoustic boundaries** (`audio.cuts`), not re-voiced.

## 7. Builder features this episode needs
| Feature | Status | Need |
|---|---|---|
| **Inserted silence** (`audio.pauses`, 2.0 s ×3, after cuts) | missing | **ESSENTIAL** |
| **Quiz beat (text front)**: phrase card + "Friends or work?" in two big pill buttons + countdown bar, held through the silence; the reveal beat starts exactly at the spoken answer | missing | **ESSENTIAL** |
| **Tag card**: headline = word/phrase, a coloured **register chip**, one example line, one "Avoid when: …" line. Used for beats 4–6 and every reveal (picture above, chip + avoid-when below) | missing; `card(headline, sub)` can fake it (sub = "casual · avoid when …") with weaker hierarchy | essential (degraded fallback exists) |
| Picture + text in one beat (per-cell crop above a tag card) | missing (one visual per beat) | essential for the reveals; fallback = picture beat followed by tag card beat (costs pace) |
| Per-cell crops of the 6-card sheet | `grid` exists, untested on this layout | needed |
| Register scale strip (friends ←→ work, the current phrase lit) | missing | nice-to-have |

## 8. Flags for the language editor
- Verify every register chip and avoid-when line in §4 (my proposals, not from the article; only the 3 article words are sourced).
- "at the moment" vs "to hand"/"on hand"; "Beats me" and "Your guess is as good as mine" = informal in both UK and US?
- The hook "This is why…" is fine. It is NOT the banned podcast opener "This is the brief…". Don't let a cut remove it by mistake.
