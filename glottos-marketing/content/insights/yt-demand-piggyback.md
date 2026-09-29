# YouTube demand vs our videos — piggyback plan (2026-09-29)

User 2026-09-29 (verbatim): "the fact that there are only 3 impressions of videos by youtube can mean that there are no such search in youtube and this means that either we should piggy back on what is viral and working already or the problem you found is not really existing and searched by people, so you should make a search of what is searched on youtube and align it with our videos that from 3 impressions we are getting at least one click, here you should consult marcus campbell on piggy back strategy"

Data (raw, reproducible): `state/yt-demand/autocomplete.json` (YouTube autocomplete, 16 seeds × a–z), `serp.json` (top 15 long results per query, views), `shorts_winners.json` (Shorts-filtered search + winners' views/subscriber). Marcus consult: affiliatemarketingdude `consult.sh` 2026-09-29 (piggyback / YSI vs YDI / red flags).

## Verdict: the user is right — our TITLES target phrases with ~no YouTube demand
| Our phrase | YouTube reality |
|---|---|
| "synonyms for big" | long: median of top 15 = **222 views** (top 72k from a 939k-sub channel). Shorts: median **9**. Marcus red flag: years-old results with a few thousand views = no audience. |
| "another word for big/happy/sad/beautiful" | YouTube treats it as a MUSIC query (Tom Odell "Another Love", One Direction). It's a GOOGLE phrase (that's anotherwordfor.net's traffic), not a YouTube one. Our 2019 "Another Word For Happy" = 3,304 views in 6 years. |
| "Can You Remember 15 Synonyms for BIG? (Memory Challenge)" | nobody types it; "memory challenge english words" median 11.6k, owned by Mindvalley's 936k "MEMORY CHALLENGE: Can you remember all these words in order?" |
| "never learn a word alone" (Ep1) | zero: results are songs. |
| "How to Remember New Words" (M1) | REAL demand ("how to remember english words" median **124k**, autocomplete: …forever / easily / vocabulary permanently) but big channels (Kaufmann 5M, Lucy 3M). |

## Where the demand IS (same content, different front door = Marcus "intent flip")
Synonyms sell on YouTube only when packaged as **"Stop saying X / better words than X"**:
- long: "Improve your Vocabulary: Stop saying VERY!" 48.5M · "100+ Ways To Avoid Using The Word VERY" 5.0M · "Stop saying 'very good' & 'very bad'" 1.4M · linguamarina "Stop saying 'Very'" 1.2M. Autocomplete: "words to use instead of very", "…of said / because / thank you / sorry".
- Shorts: "Speak Like a Pro | Better Words than 'Drinking'" **48.3M** · "Stop Saying 'Increase'! Use These 9 Better English Words" **408k** · "Stop Saying 'VERY'! 5 Stronger English Words | Part 2" 170k.
- Identity/quiz hook: Brian Wiles "If You Know These 15 Words, Your English is EXCELLENT!" **17.9M on 3.09M subs = ×5.8 views/sub** (Marcus: high views/sub = the topic itself is recommended, YDI) — and it's the same "15 words" number as our specials.

## Proposed titles (NOT applied — user approves; language editor checks; content must deliver what the title says)
| Video | Now | Proposal (piggyback pattern) |
|---|---|---|
| S3 | Can You Remember 15 Synonyms for BIG? (Memory Challenge) | Stop Saying "Very Big" – 15 Stronger Words (Can You Remember Them?) |
| S1 | …for HAPPY? | Stop Saying "Very Happy" – 15 Better Words (Memory Challenge) |
| S2 | …for SAD? | Stop Saying "Very Sad" – 15 Better Words (Memory Challenge) |
| S4 | …for BEAUTIFUL? | Stop Saying "Very Beautiful" – 15 Better Words (Memory Challenge) |
| M1 | How to Remember New Words: 3 Easy Steps That Make Them Stick | How to Remember English Words Forever (3 Easy Steps) |
| Ep1 Short | Stop forgetting new words: never learn a word alone | How to Remember English Words (Stop Learning Them Alone) #shorts |
Also: tags/description lead with the searched phrase ("words to use instead of very", "how to remember english words forever").
Thumbnails (Marcus): big high-contrast text of the BANNED word crossed out ("VERY BIG" ✗ → "HUGE ✓"), face/eye contact if we ever have one; ugly > polished.

## Shorts engine (Marcus: 2–5/day, one lane, many angles, double down on the one that pops)
Lane = "Stop saying ___ → 5 better words" (very big / very good / very tired / very happy / said / because …), one Short per word, cheap format (cards + edge-tts, no NotebookLM infographic), so volume is possible. Ep2 took ~34 h on NotebookLM infographic retries — that production path can't feed 2–5/day.

## How we'll know (target: ≥1 click per 3 impressions ≈ 33% CTR is unrealistic; YouTube norm 2–10%)
Measure impressions + CTR per video in Studio (stats.py extension, P3 of the plan) 7 days after each change; A/B title test once a video has ≥1k impressions/week.
