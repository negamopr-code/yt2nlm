# T02 research brief: "Other ways to say never give up" / "never give up synonym"

Writer: glottos-longvideo-writer, 2026-10-17. Status: DRAFT, goes to glottos-language-editor with the script.
Sources: notebook "Glottos — long-video research" `82b6f926-bf99-4830-a7fe-3992c4789fbe` (drawnformula), sources
`cf19ee82…` (LV T02 transcripts, 19 videos), `9cb5ee1b…` (LV T02 comments), `3129ed93…` (LV T02 our page). 3 queries
(q1 best practice on transcripts, q2 viewer questions/praise on comments, q3 our page vs videos, gaps). Local data:
`/workspace/state/glottos-longvideo/T02/{ledger.json,comments/*.jsonl,transcripts/*.txt,page.txt}`.
Rule used below: **[V]** = verified in the local files, **[U]** = NotebookLM said it, not found in the files (unverified),
**[X]** = NotebookLM said it and the files contradict it.

## 1. Why this topic
- Search Console (anotherwordfor.net, user screenshot 2026-10-17): *other ways to say never give up* (1 click), *to never give
  up synonym*, *thesaurus never give up*, *what's another word for never giving up* (topics.json `source`) [V].
- Ahrefs (user 2026-10-17): *never give up synonym* = Easy, >100/month. Our page https://anotherwordfor.net/never-give-up-synonym/
  ranks on Google page 4 (user) [V in topics.json; not re-measured by me].
- Rank probe 10-17 (discussion journal, 3 reads): Google page 1 = Collins, Quora, powerthesaurus ×3, a Facebook post, a
  13-year-old Reddit thread, dictionary.com/Cambridge — **no video on page 1**. YouTube top 10 for the phrase = songs +
  motivational speeches, **0 lessons with the phrase in the title** [V in docs/nlm-mirror/discussion-journal.md].
- Google Trends (`/workspace/glottos-auto/out/lab/trends.json`, read 2026-10-17 17:53Z, worldwide, 3 months) [V]:
  *other ways to say never give up* last 42 / avg 11.5, "rising" (tiny, spiky volume); *other ways to say* last 46 / avg 63.2,
  rising; *stop saying* last 60 / avg 74.1, flat; *another word for* last 38 / avg 54.7, rising. (The "63" and "74" in the
  brief are the 3-month averages, not the last reading.)
- Five-way fit (docs/autopilot.md): trend 1 (stem "other ways to say" rising, phrase itself tiny) · addiction 2 (open loop,
  quizzes, story clip, comment prompt with proven pull) · entertainment 1–2 (old-film house story, "I'm determined, you're
  stubborn" joke) · usefulness 2 (register + mistakes nobody teaches) · search 2 (Easy KD, no video on Google p1, empty YouTube title slot).

## 2. The videos (ledger.json, sorted by views) [V]
| id | title | channel | views | subs | likes | comments | length | chapters | transcript/comments |
|---|---|---|---|---|---|---|---|---|---|
| 7DKeKD59DUA | Do not Give Up / Buddhism In English I Inner Guide Special Video | Buddhism | 2431215 | n/a | n/a | n/a | 11:29 | 0 | dropped/dropped |
| 7cpZ7mGj0Xg | How to Give Advice in English - recommend, suggest, advise, encourage. | English with Alex · engVid | 327607 | n/a | n/a | n/a | 5:46 | 0 | dropped/dropped |
| DvVYP4Maji4 | English Lesson - Phrases to encourage people ( Free English speaking l | Learn English / Let's Talk - Free  | 175255 | 8370000 | 2751 | 148 | 10:38 | 10 | done/done |
| MrS4a6Zo8xs | LEARNING ENGLISH - LESSON 1 ( Don't Give Up / You can do it ) | English Addict with Mr Duncan | 135388 | 1880000 | 2059 | 70 | 3:00 | 0 | done/done |
| ChVGiyU8JZY | Words of Encouragement When You’re Feeling Down | Bob Baker Affirmations | 133007 | 436000 | 2798 | 290 | 8:53 | 0 | unavailable/done |
| Tcf1dbiWKsk | How resilient are you? 6 Minute English | BBC Learning English | 114036 | 11000000 | 2643 | 69 | 6:32 | 0 | done/done |
| ISdq6slvUZ8 | Pronounce determine and determined correctly - Business English | Derek Callan - English for Profess | 100088 | n/a | n/a | n/a | 4:43 | 0 | dropped/dropped |
| PEa9qxnzCN0 | How to Reassure & Encourage someone? – English Speaking phrases to spe | Learn English / Let's Talk - Free  | 58677 | 8370000 | 1162 | 103 | 10:08 | 7 | done/done |
| AKpfup9Hgi4 | Don't Give Up on English / Easy Motivation for Beginners / English Pod | Mr. English Channel | 55131 | 1530000 | 2980 | 239 | 12:44 | 9 | done/done |
| TIKrfdvZdes | How to Encourage Someone in English | Learn English with Bob the Canadia | 51047 | 2600000 | 4311 | 295 | 6:29 | 6 | done/done |
| wM9hbLo_j7s | 10 English Phrases for Encouraging Someone | Espresso English | 44102 | 707000 | 357 | 4 | 2:54 | 10 | done/done |
| eHbg9FPta4U | 55 Motivational Daily English Phrases To Expand Your Fluency in Englis | Club James Studios - English Speak | 43305 | 943000 | 1897 | 63 | 15:05 | 19 | done/done |
| VgMKgkUKEvs | How to Express Appreciation in English / 6 Ways to Encourage Others | Speak Confident English | 40114 | 1110000 | 1564 | 78 | 14:45 | 0 | done/done |
| N99hmmBkVKA | 25 Words (Or Sayings) Of Encouragement For Kids | CareerVidz | 38344 | 5350000 | 292 | 18 | 3:50 | 14 | done/done |
| mC0fZ0D_2IY | Encouragement phrases in English - Basic English Lesson | eVidyarthi - Basics of English Spe | 27629 | 769000 | 109 | 2 | 2:55 | 0 | done/done |
| HzkyjNQ6AqY | Encouraging and Supportive English Phrases (Don't Say Congratulations  | Go Natural English - Real Life Eng | 26815 | 2270000 | 2085 | 145 | 8:49 | 5 | done/done |
| 2DCV_z3pAhc | How to Pronounce Persevere and Perseverance | SpeechModification | 15372 | 213000 | 286 | 42 | 4:45 | 0 | done/done |
| a4qD1tLq5Lw | How to Encourage a Sick Person in English | Mad English TV | 14651 | 582000 | 817 | 65 | 4:28 | 0 | done/done |
| v_tRYO72AvM | Resilience in the workplace - Business English | British Council / English | 12364 | 941000 | 293 | 6 | 3:17 | 0 | unavailable/done |
| V3JCxD7JJn0 | Simple English Phrases to Encourage others | TutorialsPoint | 11290 | 3740000 | 202 | 10 | 5:47 | 3 | done/done |
| E9DAc2VREvo | How To Encourage And Support Colleagues At Work - Business English | Derek Callan - English for Profess | 9891 | 258000 | 380 | 14 | 7:02 | 0 | done/done |
| qaYVZR4x42I | 50 Morning Motivation Phrases — Learn English FAST / Day 17 Shadowing  | Speak English Daily | 8186 | 384000 | 302 | 46 | 25:06 | 9 | done/done |
| 0TI3aISY51g | C1 English Listening Challenge // Build Mental Resilience 💪 // English | Learn English Lab | 5666 | 182000 | 125 | 10 | 34:46 | 10 | done/done |
| 1fpTA_SuRuY | When You Feel Tired, Don't Give Up / Motivation in English / A1–B1 Pod | Daily English Talk | 5104 | 112000 | 256 | 25 | 20:56 | 9 | done/done |

Notes [V]: 24 videos listed, 3 dropped by the loop (no transcript/comments: the 2.4 M Buddhism talk, engVid advice, Derek
Callan "determined" pronunciation), 2 with comments only (Bob Baker, British Council). 19 transcripts, 1,742 comments
(1,424 by viewers, the rest creator replies). Not one title contains "never give up synonym" or "other ways to say never give up".
**Length:** top 5 lessons by views with data = 10:38, 3:00, 6:32, 10:08, 12:44 → median **10:08**; with Bob Baker's 8:53
instead of the 12:44 podcast → 8:53. The least viewed are the 20–35 min podcasts (5–8 k views) — q1 also notes that. Target ≈ 10–12 min.

## 3. Best practice (q1 + q3, checked in the transcripts)
**Openings**
- Let's Talk DvVYP4Maji4 (175 k, the most viewed lesson): relatable struggle first — "life is quite a struggle … that's exactly
  the reason why we all love to hear words that encourage us. Am I right?" — then straight into phrase 1 "Give it a try" [V].
  (It also has the "Hello friends, I am Niharika … in this lesson today" intro we do NOT copy — house rule.)
- Mr Duncan MrS4a6Zo8xs (135 k, 3:00): no greeting; an essay hook "The hardest parts of doing anything often occur at the start"
  and an open loop "But I know what you're thinking. What does this have to do with learning English? Well, I will tell you…" [V].
- BBC 6 Minute English Tcf1dbiWKsk (114 k): a question in the first 30 s ("how resilient are you?") + a quiz (a/b/c: what does
  resilience mean in science?) answered at the end — "I'll let you know if you were correct at the end" [V].
- Daily English Talk 1fpTA_SuRuY (5 k): explicit open loop "What do you think Tom did … write your answer in the comments right
  now. We will tell you the answer at the very end of the video. No skipping to the end" [V].

**Structure the most viewed share** [V via transcripts + ledger]
- Situation-grouped phrase list, 10 min, with chapters (Let's Talk DvVYP4Maji4: people who haven't started → doing well →
  hard time → speeches; 10 chapters; its sister PEa9qxnzCN0, 7 chapters). Mid-length (3–10 min) beats the long podcasts.
- Every phrase gets a situation ("friend learning to drive", "son riding a cycle" — DvVYP4Maji4) [U for the exact list; the
  situation device itself V].

**What they teach** (phrases found in the transcripts) [V by grep]: hang in there (DvVYP4Maji4, E9DAc2VREvo), keep at it
(TIKrfdvZdes), you've got this (TIKrfdvZdes, E9DAc2VREvo, VgMKgkUKEvs), it's worth a shot / never say die (DvVYP4Maji4),
push through (1fpTA_SuRuY), carry on / quitting is not an option / perseverance always wins (MrS4a6Zo8xs), pull through
(VgMKgkUKEvs, a4qD1tLq5Lw), bounced back (a4qD1tLq5Lw, 0TI3aISY51g), persevere(nce) (2DCV_z3pAhc, MrS4a6Zo8xs), persist
(N99hmmBkVKA), resilient/resilience (Tcf1dbiWKsk, 0TI3aISY51g), rest don't quit (AKpfup9Hgi4).
**Not in any transcript** [V by grep]: stick with it, stay the course, throw in the towel, soldier on, give up on, tenacious,
relentless, resolute, stubborn, obstinate, sedulous. ("determin…" appears in 3 transcripts only as ordinary use; q3's claim that
Speak Confident English *teaches* "determined" is [U].)

**Teaching devices and where they sit**
| device | where (video) | in most viewed? |
|---|---|---|
| situation per phrase | DvVYP4Maji4, PEa9qxnzCN0, TIKrfdvZdes [V] | yes (175 k, 59 k, 51 k) |
| quiz with the answer held back | BBC Tcf1dbiWKsk [V]; 5-situation "say congratulations or not?" quiz Go Natural HzkyjNQ6AqY [V: "dancer" story + quiz] | yes (114 k); praised in comments of HzkyjNQ6AqY |
| speak directly to the viewer where they are ("maybe you're sitting on the subway … at your kitchen table") | Bob the Canadian TIKrfdvZdes [V] | 51 k, most likes per view (4,311) and comments quote it back [V] |
| story of failing and trying again | Daily English Talk 1fpTA_SuRuY (fell off the bike "maybe the 15th time": "That's it, I give up, I will walk everywhere") [V]; Mr. English Channel AKpfup9Hgi4 (host felt like giving up) [V] | only in the small podcasts |
| "rest, don't quit — like a runner in a race, they stop to drink water but they don't leave the race" | AKpfup9Hgi4 [V] | 55 k |
| don't say X, say this instead (contrast) | Go Natural HzkyjNQ6AqY ("Don't say congratulations") [V] | 27 k, most-liked joke of the corpus |
| wrong → right grammar | 1fpTA_SuRuY ("Wrong: When I will feel tired …") [V] | small only |
| repeat after me / shadowing | E9DAc2VREvo, qaYVZR4x42I, eHbg9FPta4U, a4qD1tLq5Lw [U for all; a4qD1tLq5Lw "Relax & Repeat" V in comments] | small/mid only |
| pronunciation via a word you know: "persevere has the word severe in it … the main stress is on the veer syllable" | SpeechModification 2DCV_z3pAhc [V], 15 k views for one word | — |
| comment prompt "tell us what you do when you feel like giving up" | AKpfup9Hgi4 [V: 68 "give up" comments in the corpus, the "When I feel…" answers are under this video] | 239 comments |

## 4. Viewer questions and signals (q2, recounted from the raw comments) — weight = comments / likes [V unless marked]
Honest read: the comments contain **few real questions** (61 comments with a "?" out of 1,424, 35 likes in total, most of them
off-topic: "where are you from?", course prices). The weight is in what viewers *do* in the comments.
| # | group | weight [V] | example (no names) | answered by any video? |
|---|---|---|---|---|
| G1 | "When I feel like giving up, I…" — viewers write their own giving-up strategy (and learning English) | 68 comments mention give up, 75 likes; 51 about learning English, 85 likes | "Never give up learning English in my self" (14 likes) | the prompt is AKpfup9Hgi4's; nobody corrects the English |
| G2 | the learner mistake inside G1: "When I feel give up / feel giving up" | 9 comments, 7 likes (all under AKpfup9Hgi4) + "give up to beating" (1) | "When I feel give up I take a deep breath…" (6 likes) | **no** (q3: no video teaches feel like + -ing / give up + -ing / give up on) |
| G3 | emotional need: wanting to hear encouragement, "I believe in you" | Bob Baker comments: 125, 58, 29, 18, 17, 17, 16 likes (top comments of the corpus) | "I wish I had someone to give me a hug and talk me through…" (58) | Bob Baker (affirmation, not a lesson) |
| G4 | tone: sounding sarcastic ("congratulations" for small things) | 3 comments, 14 likes; plus ~20 "congratulations" comments under HzkyjNQ6AqY | "'congratulations, you're a good dancer' it really sounds sarcastic" (9) | yes, HzkyjNQ6AqY (for congratulations only) |
| G5 | meaning differences: perseverance vs resilience, resilient for a body, adversity, "I'm no resilient" | 23 comments mention persever/persist/tenac/determin/resilien, 34 likes; direct questions 4, 0–5 likes | "the picture is suggestive of perseverance rather than resilience" (3); "I'm no resilient. I have to give up…" (5) | BBC answered the body question in a reply; **nobody contrasts perseverance vs resilience** (q3) |
| G6 | pronunciation / spelling of persevere | a whole 15 k-view video for it; ~4 confused comments (stress per-SEH-ver?, "perserved", "perservance") 1–2 likes | "I twice recently have heard someone put the primary accent on the second syllable" | yes, 2DCV_z3pAhc only |
| G7 | format complaints | repeat sentences "excessively long" (3 likes), "too many slangs and idioms" (1), "intro … takes so long" (0), "please speak a little fast" (3) | — | — |
| G8 | how to answer when someone encourages you | 1 direct question (0 likes) + 1 related; q2/q3 call it "major" — that is **[X]**: small | "I don't know how to answer when someone encourages me." | **no** |
| — | next-video requests (q2) | hair salon, IELTS, tenses, "fierce", "sacrifice", 30-min episodes, PDFs — each 0–1 like [V spot-checked: fierce, hair salon, sacrifice] | — | off-topic for T02 |
q2 numbers checked: "I go where I am celebrated…" 125 likes [V]; "sounds sarcastic" 9 [V]; "Relax & Repeat" 5 [V]; "sentences …
excessively long" 3 [V]; "I don't like too much this format" 9 [V]. q2's "Group A 4 comments 0 likes" etc. are its own small
samples [U]; the table above uses my regex counts over all 1,424 viewer comments.

**What viewers praise** [V]: Bob the Canadian speaking to them where they are ("You catch me, I am sitting at the kitchen table");
a quiz they can score ("My result of the quiz is 4+ out of 5" under HzkyjNQ6AqY [V]); the sarcastic-congratulations
joke (9 likes); "Relax & Repeat" shadowing (5); "I believe in you" (Bob Baker); teachers who are calm and positive.
**What did not work** [V]: long repeat sentences, too many idioms at once, slow intros, speaking slowly.

## 5. Gap = OUR angle (what the best video still leaves out)
Most viewed lesson = Let's Talk DvVYP4Maji4 (situations, chapters, no quiz, no register, no mistakes). q3 rates Daily English
Talk 1fpTA_SuRuY "strongest" on content (stories + wrong/right grammar) but it has 5 k views and is 21 min — strength of
method, not of reach. Neither does, and no video in the corpus does [V by grep / q3]:
1. **The register ladder**: friend → after a setback (idioms) → formal (job application) → praise or insult. No video goes from
   "hang in there" to "persevere / tenacious / resilient" in one lesson.
2. **Praise or insult**: determined vs stubborn vs obstinate (relentless both ways). Nobody covers it; our own page calls
   obstinate a synonym of never give up (wrong).
3. **The mistakes viewers actually make** — "when I feel give up" (9 comments), "I'm no resilient", "perserved", give up + -ing,
   give up on someone. Nobody corrects them.
4. **Persevere vs resilient** contrast (a viewer noticed the BBC picture mixed them up; nobody explains it).
5. **What to say back** when someone encourages you, and **when not to say "never give up"** (rest, don't quit; pressure on a
   sad friend) — the old page's "know when to take a break" idea, kept and made adult.
6. **Fixing the list**: drop sedulous / pertinacious (rare), inexorable (not about people), obstinate (criticism).
7. **Search packaging**: the phrase in the title — zero competitors have it.
