# T05 research brief: "Another word for hopeful" (KEYWORD CLUSTER) — page https://anotherwordfor.net/hope/

Writer: glottos-longvideo-writer, 2026-10-17. Status: DRAFT, goes to glottos-language-editor with the script and the page.
Sources: notebook "Glottos — long-video research" `82b6f926-bf99-4830-a7fe-3992c4789fbe` (drawnformula), sources
`23a3111f…` (LV T05 transcripts, 17 videos), `7091b3a4…` (LV T05 comments, 19 videos), `a8773838…` (LV T05 our page).
3 queries: q1 best practice (transcripts + our page), q2 viewer questions/praise (comments), q3 follow-up on engagement
moments and the "hopeful" gap (transcripts + comments). Local data: `/workspace/state/glottos-longvideo/T05/{ledger.json,
comments/*.jsonl,transcripts/*.txt,page.txt}`; counts below are my own regex counts over the raw files (no names read out).
Marks: **[V]** = verified in the local files · **[U]** = NotebookLM or the brief said it, not found in the files ·
**[X]** = NotebookLM said it and the files contradict it.

## 1. Why this topic (the cluster)
- **Ahrefs** (user 2026-10-17, journal lines 797–800) [V in docs/nlm-mirror/discussion-journal.md + topics.json]: /hope/ = 6 visits/month,
  **38 % of the site's US organic traffic**, 100 % US; its only keyword *another word for hopeful* = **Google position 7, 700/month**
  (site view); keyword view: master >100 Easy; sub-keywords <100 each: *what is / what's another word for hopeful*, *another word
  for hopeful outcome*, *hopeful outlook*, *hopeful thinking* (Easy), *hopeful person*, *hopeful future*.
- **Search Console** (topics.json `source`): *another word for hope* (2) [V].
- **Rank probe 10-17** (journal line 799) [V]: Google p1 = thesaurus.plus letter pages + a Facebook post, **no video**; YouTube **0 titles
  with the phrase**, top hits 7–3,367 views → the title must start "Another Word for Hopeful". (The brief's simplegrammer "25 other ways
  to say hopeful" and merriam-webster on p1 are not in the journal line → [U], plausible, not re-measured.)
- **Google Trends** (`/workspace/glottos-auto/out/lab/trends.json`, read 2026-10-17 17:54Z, worldwide, 3 months) [V]:
  *another word for hopeful* last 0 / avg 3.1, "rising" (tiny); **rising AND top related query = "another word for hopefully" (+140 %,
  top 100)** → own chapter; stems *other ways to say* last 46 / avg 63.2 rising, *another word for* last 38 / avg 54.7 rising,
  *synonym* 46 / 63.2 rising; *delulu* last 63 / avg 67.1 flat (→ cliffhanger into T07).
- **Marcus (cluster, 10-17)** [V topics.json `cluster.plan`]: master long video with the master phrase first and ONE CHAPTER PER
  SUB-KEYWORD; one door Short per sub-keyword (Related video = master); hub page with one H2 per sub-keyword + anchors; playlist;
  end screens; order page → master → Shorts 1–2/day. Our correction: links in Shorts are not clickable → Short leads to the long video,
  the long video's description leads to the page. A separate page only where the intent differs (*hopeful person* = an optimist, a noun).
- **Five-way fit**: trend 1 (phrase tiny, "hopefully" rising, stems rising) · addiction 2 (two open loops, 11 quizzes, joke, film clips,
  the comment prompt that produced the most comments in the corpus) · entertainment 2 (train joke, crooked-house callback, wrecked-car
  "wishful thinking") · usefulness 2 (register + traps + the hope/wish questions nobody answers in one place) · search 2 (Easy, pos 7 page,
  no video on p1, empty YouTube title slot).

## 2. The videos (ledger.json, sorted by views) [V]
| id | title | channel | views | subs | likes | comments | length | chapters | transcript/comments |
|---|---|---|---|---|---|---|---|---|---|
| 3VO1F_XZBFQ | Difference between ' I Hope ' and ' I Wish ' - English Grammar lesson | Learn English / Let's Talk | 565897 | 8370000 | 6397 | 400 | 10:48 | 3 | done/done |
| LJcXRxy-nDU | Grammar: 5 different ways to use 'wish' in English | BBC Learning English | 164687 | 11000000 | 4585 | 83 | 4:57 | 7 | done/done |
| gqZpGAG9FHU | Wishes and regrets / WISH / IF ONLY / HOPE - English grammar | Oxford English Now | 153689 | 134000 | 4066 | 175 | 8:00 | 9 | done/done |
| U4OBY5n2BvM | IDIOMS to Express Hope & Inspiration / Vocabulary Lesson | Interactive English | 143761 | 1460000 | 7551 | 400 | 16:40 | 14 | done/done |
| nEjeGjzZPZY | How to learn English: Hope vs. Wish | ESLgold.com | 110838 | 56300 | 2764 | 9 | 6:55 | 12 | done/done |
| 8emPUKiH_jA | Should I use "WISH" or "HOPE"? Learn fluent English vocabulary | Speak English With Vanessa | 95200 | 7700000 | 3910 | 400 | 3:59 | 5 | done/done |
| 2tPRuyStRtU | HOPE vs. WISH / ESL VOCABULARY LESSON | Mad English TV | 89433 | 582000 | 3003 | 350 | 13:27 | 11 | done/done |
| Ss96xfZCBv4 | HOPE vs WISH - What is the DIFFERENCE? | English Speaking 360 | 80952 | 374000 | 3064 | 186 | 27:05 | 8 | done/done |
| HxwnrFGbxMw | Wish vs Hope / Grammar and Use | Love English with Leila & Sabrah | 64196 | 357000 | 2483 | 160 | 8:04 | 8 | done/done |
| vZNLYEBRySA | HOPE and WISH…. Explained! (Essential B2 Grammar Lesson) | English with Greg | 52804 | 613000 | 2343 | 81 | 14:36 | 12 | done/done |
| DpEzZC6-TCE | Hope vs Wish - Basic English Grammar | JForrest English | 48278 | 2370000 | 2952 | 329 | 8:41 | 5 | unavailable/done |
| QEqvt2nhYTU | Confusing Words in English: WISH and HOPE | Espresso English | 45256 | 707000 | 544 | 2 | 3:12 | 2 | done/done |
| 7B26Vygr6po | 'Hope' - Spoken Word (college poem) | Christelijke Hogeschool Ede | 41228 | 1010 | 463 | 14 | 3:21 | 4 | done/done |
| _wdyyGhI_m0 | (song) (HOPE) Is Just Another Word With A Hole In It | Nothing (band) | 38196 | 20900 | 563 | 26 | 5:49 | 0 | unavailable/done |
| BUaO5Lm6-Vc | How to Use Hope vs Wish in English / Daily English Conversations | Speak English Fluently | 32050 | 9670 | 1222 | 65 | 16:38 | 10 | done/done |
| wjWJzqoDaGs | Prophetic Word - Another beautiful and hopeful word for someone | Bold Existence Ministries | 31051 | 42800 | 2622 | 0 | 7:17 | 4 | done/done |
| QyO6Tr5301Y | 'Wish, If only & Hope' in English – Wishes & Regrets | Lingportal | 20389 | 196000 | 432 | 28 | 8:16 | 7 | done/done |
| DmXN0Pp7og8 | Using HOPE correctly instead of WISH | English for Everyone | 14428 | 462000 | 604 | 16 | 2:57 | 0 | done/done |
| Azx3kbTAI4M | English Vocabulary: HOPE Definition and Examples | To Fluency | 13284 | 1190000 | 265 | 38 | 3:10 | 0 | done/done |

Notes [V]: 19 videos, 17 transcripts, **2,762 comments (2,290 by viewers, 472 creator replies; 1,658 viewer likes)**. 16 of 19 are
*hope vs wish* grammar or idiom lessons; one song, one sermon, one student poem. **Not one title contains "hopeful" as a lesson topic**
(the sermon's title has it). **Length:** top 5 by views = 10:48, 4:57, 8:00, 16:40, 6:55 → median **8:00**. But here the *least* viewed
lessons are the 3-minute clips (DmXN0Pp7og8 14 k, Azx3kbTAI4M 13 k, QEqvt2nhYTU 45 k), and the best likes-per-view are the long idiom list
U4OBY5n2BvM (16:40, 7,551 likes = 5.3 % of views, the most-liked video of the corpus) and Vanessa (4.1 %). A cluster video with 7
sub-keyword chapters cannot fit 8 min → target **≈ 14 min** (est. 14:22), justified by the 16:40 idiom list being the most liked.

## 3. Best practice (q1 + q3, checked in the transcripts)
**Openings** [V by transcript head]
- Let's Talk 3VO1F_XZBFQ (566 k): a real situation first — invited to a party, far away, traffic jam: "so I hope I can reach there on time …
  then I wish I could fly" — then the topic. (It also opens with "hi friends … today" — we do NOT copy that, house rule.)
- BBC LJcXRxy-nDU (165 k): a skit — "I wish I wish I wish I wish I wish! Oh! It only works if you know the grammar rules!" then "Are you ready? Go!"
- Oxford English Now gqZpGAG9FHU (154 k): exam promise + open loop to the end — "keep watching the video till the end where you'll have some exercises".
- Interactive English U4OBY5n2BvM (144 k): value line — "if you'd like to express hope and inspiration then this lesson is for you".
- Vanessa 8emPUKiH_jA (95 k): a real student's mistake — "I wish that I will get the scholarship … what's the problem with this sentence?"
- Mad English 2tPRuyStRtU (89 k): a picture + question — "this guy wants that car … should he use hope or wish?"
- English Speaking 360 Ss96xfZCBv4: "don't miss the final quiz because it is very hard" — its pinned creator comment advertises the MONSTER FINAL QUIZ (14 likes [V]).

**Structure the most viewed share**: one clear contrast (possible vs unreal), examples per situation, a summary rule, and (Oxford, ESLgold,
English Speaking 360, Speak English Fluently, Lingportal) an end quiz. The only *vocabulary* lesson (Interactive English) = one idiom per
chapter, 14 chapters, 16:40 — the chapter-per-item structure we use for the sub-keywords [V ledger chapters].

**What they teach** [V by grep over the 17 transcripts]: hope / wish everywhere; *optimistic* only as a word inside an explanation (Mad English
"here I'm hopeful I'm optimistic", Oxford "if it's optimistic then we use hope", English Speaking 360); *hopeful* = 1 mention (Mad English) +
the sermon; *wishful thinking* = 1 passing mention (Let's Talk); idioms only in Interactive English: keep your chin up, hang in there, break
a leg, in the bag, the sky's the limit, the world is your oyster, light at the end of the tunnel, plenty of fish in the sea, look on the bright
side, pull yourself together, fingers crossed, blessing in disguise.
**Not in any transcript** [V by grep]: hopefully (q1 claims Speak English Fluently teaches "Hopefully, tomorrow is sunny" → **[X]**, not in the
file), an optimist, upbeat, promising, favourable, encouraged, a good sign, looking up, glass half full, silver lining, rose-tinted, a ray of
sunshine, idealistic, dreamer, sanguine, a long shot, pipe dream, hope against hope, here's hoping, with any luck, if all goes well, high
hopes, look forward to, a bright future, positive thinking.

**Teaching devices and where they sit**
| device | where (video) | most viewed? |
|---|---|---|
| real situation / real learner mistake as the opening | Let's Talk 3VO1F_XZBFQ (traffic), Vanessa 8emPUKiH_jA (scholarship), Speak English Fluently BUaO5Lm6-Vc ("I wish it doesn't rain tomorrow") [V] | yes (566 k, 95 k) |
| skit / humour opening | BBC LJcXRxy-nDU [V] | yes (165 k) |
| picture + "which word?" question | Mad English 2tPRuyStRtU (car) [V] | 89 k, 350 comments |
| open loop to an end quiz | Oxford gqZpGAG9FHU, English Speaking 360 Ss96xfZCBv4 [V] | yes (154 k) |
| fill-in quiz with pause ("feel free to stop the video") | ESLgold nEjeGjzZPZY [V], Oxford, English Speaking 360 (20 questions) | yes (111 k) |
| one idiom per chapter, meaning from the literal picture ("in a tunnel it's very dark … you see this light") | Interactive English U4OBY5n2BvM [V] | most liked (7,551) |
| comment prompt "write two sentences using hope and wish" | Vanessa 8emPUKiH_jA [V]; Speak English Fluently BUaO5Lm6-Vc ("one sentence about something you hope happens tomorrow and one … you wish were different") [V] | **the strongest engagement device of the corpus** (see §4) |
| speaking drill / repeat | Speak English Fluently BUaO5Lm6-Vc ("try saying your own sentences out loud") [V] | small (32 k) |

**Our page** (page.txt, q1 §5) [V by reading page.txt]: written for "hope" (noun/verb), **never covers the adjective *hopeful***, has no
*hopefully*, treats *wish* as a plain synonym of hope (the #1 confusion of the corpus), lists dictionary filler (*sanguineness, rosiness,
buoyancy, reverie, stock, fancy*), negative ideas without a warning (*fool's paradise, pipe dream, castles in air, utopia*), an unrelated
"greedy glutton", and stiff made-up phrases ("aspired-for event", "wished-for development", "anxiously awaiting our next encounter",
"inquiring about your current state"). Keep: the useful situations (hope this email finds you well, hope you feel better, hope to see you
soon) — but rewritten to what people say.

## 4. Viewer questions and signals (q2/q3 recounted from the raw comments) — weight = comments / likes [V unless marked]
| # | group | weight [V, my regex] | example (no names) | answered by any video? |
|---|---|---|---|---|
| G1 | hope + will / would / "I hope you pass or you'll pass?" | 66 question comments (24 likes); 77 comments with "hope … will" (48 likes), 41 under Vanessa | "Can I say I hope you pass your exam instead of I hope you'll pass your exam?" | yes, scattered (Vanessa, English for Everyone) — but the "both are fine" answer is missing |
| G2 | I wish I were vs I wish I was | 35 questions (21 likes); 53 comments in all (83 likes) | "what's the difference between I wish I were taller and I wish I was taller?" | partly: English Speaking 360 says "were for all persons"; nobody says *was* is normal speech |
| G3 | "we wish you a merry Christmas" — is it unlikely? (wish + person + noun) | 26 questions (28 likes) in 8 videos; **most-liked question of the corpus = 17 likes** (vZNLYEBRySA); 38 mentions (33 likes) | "So when we say 'We wish you a Merry christmas', means that it'll be unlikely?" | 5 videos teach it; Mad English's creator replied "I forgot to talk about that in this lesson! Sorry" [V] |
| G4 | wish + would vs wish + past; wish + can → could | 53 comments with "wish … would" (57 likes); "I wish I can" 8 comments (0 likes) | "Is this wrong to say I wish you will pass your exam?" (under BBC) | wish+would yes (BBC); can→could only in passing |
| G5 | hope about the past ("I hope she got home safely") | 14 questions (1 like); 21 comments (3 likes) | "I hope she got home safely (something happened & we don't know yet) Is it correct?" | yes (English with Greg, Let's Talk) |
| G6 | missing idioms: every cloud has a silver lining, a glimmer of hope, a leap of faith | 9 questions (4 likes) under U4OBY5n2BvM; silver lining 3 comments | "What about the idiom 'every cloud has a silver lining'?" | **no** |
| G7 | own sentences with mistakes: wish + present, "I hope see you", "I wish I can" | 12 + 16 + 8 comments, 0–1 like each (q2's "14" and "10" instances are close to mine) | — | partly |
| G8 | accent / teacher comments, off-topic (prices, other words, Brexit) | accent 12 (55 likes) | — | off-topic |
| — | next-video requests (q2): apparently, remain, liable vs likely, ironically/literally, chocolates | each 0–1 like [V spot-checked liable/likely, chocolates] | — | off-topic |
q2/q3 numbers checked: "I forgot to talk about that" creator reply [V]; Vanessa prompt line [V]; "Fingers crossed for my future IELTS exam" 11
likes [V]; light-at-the-end-of-the-tunnel train joke **28 likes** [V]. q3 says **332** own sentences under Vanessa and **201** under Mad English →
my count of comments that START with "I hope / I wish" = **281** and **128** → q3 numbers [U] (theirs may count sentences anywhere in a comment).
q3's "Angelina Jolie" example sentence (Let's Talk) and the compliment it drew are about a real named person's looks → **not used** (POLICY).
q2's "2:53 You wish" moment: the comment exists [V], the line is not in the transcript text → [U].

**The strongest signal: viewers WRITE.** 701 of 2,290 viewer comments (31 %, 413 likes) start with "I hope …" / "I wish …"; under Vanessa
281 of 390 viewer comments, and her two most-liked comments (66 and 41 likes) are such sentences. The prompt that produces this is hers:
"in the comments below this video I want you to write two sentences using hope and wish" [V]. → copied as our CTA.
**What viewers praise** [V]: the real-mistake framing (Vanessa), the car picture (Mad English: viewers joke back, "I hope you get married soon" 16
likes), the playful skit and music (BBC), the monster quiz (English Speaking 360), clear simple explanations (77 "clear/understand" comments,
83 likes), idioms they can use at once ("Fingers crossed for my exam" 11 likes; a viewer's own story with light at the end of the tunnel 8 likes).
**What did not work** [V]: speed ("4:49 very fast"), a typo on screen ("finger's crossed", 14:02), a rule that misses a case (merry Christmas).

## 5. Gap = OUR angle (what the best video still leaves out)
Most viewed = Let's Talk 3VO1F_XZBFQ (hope vs wish, 3 chapters, no quiz, no synonyms). Most liked = Interactive English U4OBY5n2BvM (12 idioms,
no adjectives, no register, no traps). **No video in the corpus teaches other words for the adjective *hopeful*** — the search phrase itself.
1. **The searcher's actual question**, sorted by the 6 sub-keywords: what is another word for hopeful / outcome / outlook / person / future /
   thinking — plus *hopefully* (Trends' rising query). 35 words, none of them in a competitor transcript except 6 idioms from U4OBY5n2BvM.
2. **Register and traps**: confident ≠ hopeful (sure vs might); *encouraged* vs *encouraging*; *promising* vs *promised*; *rose-tinted glasses*
   and *wishful thinking* = criticism; *positive thinking* = praise; *sanguine* very formal; *an optimist* (noun) vs *optimistic*.
3. **The hope/wish questions in one place**, by weight: hope + present for the future (G1), were/was (G2, nobody says *was* is normal speech),
   *we wish you a merry Christmas* (G3, the corpus' most-liked question), can → could (G4), hope + past (G5).
4. **What viewers asked for and nobody gave**: silver lining (G6).
5. **Fixing our own page** (no *hopeful*, filler words, "greedy glutton") — said honestly in the video, like T02.
6. **The T02 payoff**: *hope against hope* (in no transcript, no comment) = "the phrase for hoping for the impossible" our T02 video promises.
7. **Search packaging**: the phrase first in the title — 0 competitors have it.
