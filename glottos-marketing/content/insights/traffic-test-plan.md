# Traffic first — cheap multi-hypothesis test (2026-09-30, DRAFT awaiting user decisions)

User 2026-09-30 (verbatim): "we need first see how to get traffic, because 0 views for two video in a row is definitely a sign that hypotesis is wrong" / "we need to test bunch of hypotesis at the lowest cost (see marcus campbell approach) also see the video of the guy who made influencers ai (the one from which we started) they all do it with traffic"

## Evidence (snapshot 2026-09-30T05:38Z)
- M1 GNH19NdTu9U (public since 09-28): 0 views (Studio: ~2 impressions → YouTube isn't showing it at all).
- S4 fPKxW7BuN8A BEAUTIFUL (public 09-29): 0 views.
- Ep1 Short Jc8HSUPqmHQ: 19 views, all from the Shorts feed, 77% swiped away → push stopped on day 1.
- The 110 old 2019–21 videos: 48.7k lifetime views, but only ~28 new views across all of them in 2.5 days → the channel has almost no live traffic to borrow.
- Cost: Ep2 ≥ $8.46 of Claude + ~34 h wall time (3 rejected NLM infographics). S5 $3.34 so far. The per-variant cost is far too high to test anything.

## Diagnosis
Long videos on a dormant channel get ~0 impressions (distribution, not packaging). The Shorts feed is the only surface that shows a new channel to strangers, and it does show every Short to a small test audience. So the cheap test = Shorts, and the variable to test = the angle/hook, not production quality.

## What the two sources say (same engine)
- Tilbury (state/tilbury-method-breakdown.md): steal a format that already works → run 3 bets in parallel → let the data pick → kill 2, scale 1.
- Marcus (consult 2026-09-30): "probability machine"; 2–5 Shorts/day in ONE lane with different hook angles; rule of 20 (1 in 20 pops); matrix 5 topics × 3 hooks × 2 visuals; ugly beats pretty; decide on CTR/stayed, not likes; winner → 5–10 copies of the exact structure; kill an angle after ~20 flat posts.

## Proposed test (20 Shorts, ~7 days, ≈$2–4 total)
One cheap template: text cards + edge-tts (saved voice en-US-AndrewMultilingualNeural), channel logo bar, big hook text in the first 1 s, ≤25 s, NO NotebookLM. One Claude call writes the batch; one language-editor pass gates the whole batch; a script renders all 20.
| Lane | Hook pattern (proven demand) | 5 variants |
|---|---|---|
| L1 | "Stop saying VERY ___ → 5 better words" (48.5M / 408k / 170k views on YT) | very big / very good / very tired / very happy / very bad |
| L2 | "If you know these 5 words, your English is advanced" (Brian Wiles 17.9M, ×5.8 views/sub) | 5 difficulty sets |
| L3 | "Don't say ___, natives say ___" (textbook vs natural) | I'm fine / I don't know / very tasty / … |
| L4 (control = current hypothesis) | "Why you forget new words — fix in 10 s" | 5 memory tricks |
Post 3/day, mixed across lanes. Read at 48 h per Short: views, stayed-vs-swiped %.
- Kill a lane: all 5 < 100 views and stayed < 40%.
- Winner: any Short > 1k views or stayed ≥ 50% → 10 more of exactly that structure.
Optional, zero extra production: the same files on TikTok + Instagram Reels (Tilbury's platforms) = 3 samples per variant.

## Needs from the user
1. Approve the 4 lanes (or swap).
2. Publishing: 3 public Shorts/day. Today the rule is "only the user publishes". Allow scheduled PUBLIC publishing for this test lane, or keep drafts for you to publish?
3. TikTok/Instagram accounts (only you can create them), or YouTube only.

## Build before the test (no NLM)
- cards+tts Shorts template (reuse build_short_v2.py caption/logo parts).
- stats.py: per-Short stayed-vs-swiped + impressions (Studio tab-reach_viewers) — without it only views are measurable.

## Paused meanwhile (autopilot, pause.json)
Ep2 and S5 finish to PRIVATE draft; Ep3–6 held; Claude channel steps held. Resume = delete glottos-autopilot/pause.json.
