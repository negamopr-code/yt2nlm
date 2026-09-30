# Glottos / anotherwordfor.net go-to-market — discussion journal (verbatim)

Canonical copy: `glottos-marketing/docs/nlm-mirror/discussion-journal.md` (customer-comments repo).
Mirrored into NotebookLM "Glottos — go-to-market" (8306c0a9, account drawnformula) by
`glottos-marketing/scripts/sync-nlm-mirror.sh` after every substantive exchange.
RULE (user 2026-09-27, universal for all projects): every exchange is stored here one-to-one —
USER messages verbatim (typos kept), then what was answered/decided/done. History is never rewritten.

---

## 2026-09-27 — session with Claude Code (nlm-slot-manager workspace)

### USER
> you have access to glottos marketing and to anotherwordfor.net project is it connected to any of nlm accounts?

**Answer / findings:** glottos-marketing (:8097) had NO NotebookLM access (no cookie store mounted); glottos-shell (:8092) has the nlm CLI but no profile. The anotherwordfor.net market monitor (awf-monitor-runner, yt2nlm `monitor`) runs on account `default` (bbubu2748), notebook "AWF market monitor" 5ea409b1 — healthy. Warning: that notebook is at 38/50 sources (23 comment volumes of ~250k words, 12 transcript volumes) and heading for the same wall EV hit.

### USER
> then let us create a glottos go to market nlm in one of the free account now

**Decision:** `default` is at 99/100 notebooks (and busiest) → new notebook on **drawnformula** (6 notebooks, only patent tab t10, idle). Created **"Glottos — go-to-market" `8306c0a9-1418-41e2-a988-1c0459eafc89`** with the 10 go-to-market docs from glottos-marketing/state/ as sources (AWF traffic engine, AWF × glottos content plan, elevator pitch, first content batch, struggles vs coverage, pain→feature matrix, TikTok hooks «понимаю, но не говорю», Tilbury method + playbook, week-1 clip scripts).

### USER
> drawnformula is signed in btw

**Result:** keeper confirmed `drawnformula refreshed … google account=drawnformula@gmail.com` (ListAccounts account-pin gate passed).

### USER
> where then pains from people studing language which we did inside of glottos project were stored if it was not nlm?

**Answer:** they WERE in NotebookLM — two notebooks in `default`: "Glottos niche — language learning" (59036a79, 50 sources) and "…_part 2" (95cbcdab, 50 sources); the analysis files built from them live in glottos-marketing/state/.

### USER
> but it would make sense to have all of those nlm under the roof of the same account

**Decision:** drawnformula becomes the glottos home. All 100 sources' raw text fetched (quota-free `source content`), 8.84M chars; local backup `glottos-marketing/state/corpus-glottos-niche/raw/` (100 files).

### USER
> how they are called those comments studies of languages learners and to which project belonging?

**Answer:** the yt2nlm run `glottos-niche-language-learning` (customer-comments project), collected 2026-05-31: 59 language-learning YouTube videos + comment threads.

### USER
> if you move them, then you will delete if from the main, right in order to not have it double

### USER
> and also we need to make sure, that we implement our newest approach of transcribing and moving links out

**Done:** packed into 5 text volumes ("Glottos learners — video transcripts vol. 1" = 41 transcripts; "Glottos learners — comments vol. 1–4" = 59 comment threads, ≤2.4M chars each), NO YouTube links kept. Verified 100/100 originals present (id marker + 5 content probes each). Then **deleted** 59036a79 + 95cbcdab from default (99 → 97 notebooks). yt2nlm ledger marked `migrated`.

### USER
> I want to see yt2nlm as an expert in the expert list if you solicitting it and building data base on it

**Done:** heartbeats `glottos-pipeline.json` / `glottos-comments.json` → Experts table row "glottos-niche (yt2nlm) · 3_drawnformula · 📼 41/59 · 💬 59/59"; slot-manager assignment "glottos go-to-market → drawnformula".

### USER
> but you confirm me, that the logic we had in y2nlm before is not the one we are using now, meaning that we do not store now as much information, we digesting it and pack at maximum at which avalable document size inside of nlm

**Answer:** correction — we store ALL of it verbatim, just packed (old: 1 link source + 1 comment source per video, `_part N` notebooks; new: text only, links removed, volumes up to ~2.4M chars ≈ 400k words, under NLM's ~500k-word/source limit). Digests are a separate layer on top. Caveat: the `yt2nlm youtube` command itself still has the old per-video logic (to be upgraded).

### USER
> was y2tnlm strictly language related or we had something else on it?

**Answer:** no — 5 runs: @affiliatemarketingdude (became the affdude pipeline), Claude × Perplexity/web-search MCP (1c8de9c6), Claude × TradingView (a86ba710, feeds tradinglivedata skill), glottos niche (moved), @Handler_AI (1 video). Same codebase runs the AWF monitor + scraper-pro/affdude/smb-options/ev-gebraucht-wagen/adintel daemons.

### USER
> yes, yes, yes

(= upgrade `yt2nlm youtube` to the new approach · pack Claude×Perplexity/TradingView/Handler_AI the same way · fix false "LOGIN NEEDED" on slow page loads.) **Done so far:** keeper fix 22b2c76 (no build label → "PAGE DID NOT LOAD", not LOGIN NEEDED). The other two are queued.

### USER
> now in the glottos nlm and taking into account the pain "Learners constantly memorize new words only to forget them within days " let us make an extensive search in youtube or tiktok or instagram or pinterest or all together, what competition is doing as particular content to adress this particular problem and what can we do under anotherwordfor.net brand, faceless, but following "

<pasted_content>
Done. Both artifacts saved to state/. Here's the read.

## First — the thing that blocks everything
AWF's SSL certificate has been expired since Feb 5, 2024 — still dead today (curl exit 60, I verified the cert dates). Google won't rank an HTTPS-broken domain, and any viral video you make points followers straight at a full-page "connection not private" wall → 100% bounce. Fixing this (certbot on the openresty server, free, ~15 min) is worth more than any content this month. Publish nothing until it's live.

## What's actually getting traction (live-checked)
The "professional / résumé synonym" cluster is what ranks: *unique synonym, work ethic synonym, never give up synonym, bad attitude synonym*. Audience = US/Indonesia/India ESL, IELTS, résumé-builders, writers. And their real questions (from the monitor) hand us the viral format on a plate — someone literally asked *"why do we use 'very' so much?"* which is the "stop saying very" trend.

## The wedge (why our content wins)
Competitor users complain, over and over, that thesaurus.com/Merriam/QuillBot give no example sentences, no register, no nuance — plus ads and paywalls. So every AWF page does exactly that: each synonym gets meaning + register (formal/casual) + a real example + "avoid when." That's what makes it genuinely helpful *and* what earns saves/shares — and it's templatable, so it's automatable.

## Influencer needed? — No. Go faceless.
In this niche the words are the star (informational, not parasocial), so a face adds only maintenance cost. Faceless text-on-screen + TTS word-swaps is the proven-viral format and it's the only version that can be truly *automatic*. Tilbury needed a persona because health/wealth/relationships are parasocial; vocabulary isn't. The brand is the template, not a person.

## The engine
One structured data unit per topic (base word → 6 upgrades with example + register) powers both the SEO page and the vertical video. Pipeline: topic queue → LLM generates the unit (with quality guardrails) → render page + render video → publish to site + TikTok/Reels/Shorts/Pinterest → double down on whatever pops. Views are a volume+hook game (post 1–2/day; ~1 in 10–20 breaks out; "stop saying very" clips routinely do 100k–1M), so Tilbury-scale is reachable in weeks; SEO compounds behind it as the durable moat. **glottos slots in *afterwards* (link-in-bio + soft in-page unit) once traffic + a list exist — and since glottos is language-flexible, this English/ESL audience is now fair game.

## Delivered in state/
- awf-traffic-engine.md — the P0, traction diagnosis, faceless verdict, the factory pipeline, KPIs/path-to-views.
- first-content-batch.md — 8 production-ready units** (each a full SEO page *and* a video script with real synonyms/examples), grounded in the ranking terms + real questions. Units 2–5 are upgrades of pages that *already rank* = fastest wins.

## Next step — pick one and I'll build it now:
1. Give you the exact SSL fix (certbot commands for the openresty box + renewal cron) so the P0 clears today;
2. Build the automatic pipeline spec (data-unit schema + page HTML template + video-render script with edge-TTS) so the factory is real, not manual;
3. Produce the next 20 units (scale the "stop saying" + "corporate email translator" families) so there's a month of content queued.

One caveat: the AWF *site repo* isn't mounted in this session, so I enumerated pages via site: search, not the codebase — to wire auto-publish I'll need that workspace mounted (or I hand you a portable spec, option 2).

Sources: [AWF pages](https://anotherwordfor.net/another-word-for-unique/) · [viral "stop saying" format](https://www.tiktok.com/discover/big-words-to-use) · monitor data (reports/monitor-awf/)
</pasted_content>

> " glottos marketing strategy which was discused on http://localhost:8097/ also take into account the format and what can be used automatically with nlm stuffs like infographics together with your own scripts to put logo on it, brand it and adjust to viral stuffs

### USER
> and everything you find you should classify under nlm document by specific problem adressed

### USER
> you can also consult scraper pro buddy which should help you to gather info

### USER
> like you should fire up all guys who treated the problem in their videos, treat it with our method "transcribe and move link out", then see how much traction, views and engagements those videos made and document it under this specific problem document in nlm

**Done:** scraper-pro consulted (TikTok = rung 2, embedded JSON; browser only to render). YouTube: 210 search results → 203 on-topic → top 40 by views; traction via yt-dlp (views, likes, comments, engagement %, subscribers, date; HTTP 429 → slow backoff); transcripts via the house method (add link to this notebook → `source content` → delete the link): **38/40 transcripts, 40/40 traction**. Data: awf-monitor-runner `/app/state/glottos-problems/p01/` (videos.json, transcripts/). TikTok: rendered discover pages (captions + like counts). Long-form YouTube is dominated by face-on-camera teachers (POC English 8.4M, Speak English With Tiffani 7.8M, WIRED 7.5M, Steve Kaufmann 5M); faceless short-form formats that pull: "A BIG word a day keeps the BRAIN ROT away" series (episodic, "$45 word" hook), "Stop saying VERY" (englifyeasy 597k likes-scale), spaced-repetition explainers (studytok, 1.4–2.2M), "20 Minuten" NotebookLM-flashcards hack (119.6k).

### USER
> also connect to nlm glottos go to market tohttp://localhost:8097/ as it does pretty much the same "

<pasted_content>
Rendered clean. Here's everything.

## Competitor scan — what everyone does for "I forget words in days"
Across YouTube / TikTok / IG / Pinterest the *message* is one worn script: Ebbinghaus forgetting curve (lose ~50% in 1h, ~70% in 24h, ~90% in a week) → spaced repetition fixes it → active recall and words-in-context beat isolated flashcards. Packaging by platform: YouTube = 8–15 min Anki tutorials; TikTok = 15–45s faceless stat-hook tips (educational short-form gets 2.8× watch-time); Instagram = carousels + downloadable lists (drive saves); Pinterest = forgetting-curve / review-schedule infographics (evergreen search). No faces — the tip is the star.

The gap they leave open: everyone *names* spaced repetition, then funnels you to a paid app. Almost nobody hands you the sticky word in a sentence in one scroll.

## Our angle under AWF (faceless) — the alignment that wins
AWF's core page content (word + example sentence + register + "avoid when") *is* the scientifically-correct anti-forgetting method — the research says isolated words are exactly what you forget. So our positioning is the honest answer to the trend:

> *"You don't forget words because your memory is bad. You forget them because you learned them naked — no sentence, no context."*

We can run the whole forgetting-curve/spaced-repetition trend and convert it, because our free pages/downloads are the tool that makes the tip real.

## The NLM + my-scripts automation (your format ask)
Key idea — NLM is the content brain; my scripts are the brand+format+virality layer. NLM will never put your logo on or crop to 9:16. So: NLM emits a structured unit {hook, stat, steps, words[{word,example,register}], cta} (verified against the 30k-comment corpus, in the audience's own words) → my scripts (extending gen_pins.py + the headless-Chrome render + edge-TTS/ffmpeg) bake in the AWF logo/palette and output the 9:16 video + carousel + Pinterest pin, batched. NLM's *native* infographic export is weak/unbranded, so we use its text/insight + audio-overview, and render the picture ourselves.

## Proof — I built the first branded asset by script
state/awf-forgetting-curve.png (1080×1920) — AWF-branded, viral-styled: hook → the two-line forgetting curve (cram vs review) with −50/−70/−90 callouts → "THE FIX: day 1·3·7 + in a sentence" → save CTA. That's the pipeline output, live. (+ editable .svg source.)

Full scan + 5 formats + the 3 flagship scripts (exact on-screen text) → state/retention-pain-competitor-scan-and-plan.md.

Two caveats I flagged: the "[Pasted text #4]" 28 lines never reached me (re-paste if it had specifics), and the glottos NLM CLI isn't mounted this session, so the NLM half is a ready-to-run design, not yet executed.

## Next step — pick one:
1. Render the other two flagship pieces now (F3 "1-3-7 schedule" carousel + F4 "never-forget word bank" from the live /very/ synonyms) so you have a 3-piece launch set;
2. Build the reusable branded-template script (the gen_pins.py extension: one JSON unit → pin + carousel + 9:16 frames + TTS video) so it's a real factory;
3. Write the exact NLM prompt that returns the structured content unit from the glottos notebook, ready for when it's mounted.

Sources: [forgetting curve](https://en.wikipedia.org/wiki/Forgetting_curve) · [spaced repetition (language)](https://www.busuu.com/en/languages/spaced-repetition) · [faceless IG carousels](https://virlo.ai/blog/faceless-instagram-account-ideas) · [educational short-form benchmarks](https://www.hooked.so/trends/tiktok/educational)
</pasted_content>

> "

**Done:** :8097 now has NotebookLM: shared host cookie store mounted, profile drawnformula copied into it (slot manager keeps it renewed), nlm CLI in glottos-marketing/.nlmvenv, system prompt section "NOTEBOOKLM KNOWLEDGE BASE" (notebook id, read/query/studio commands, quota etiquette, write rules), new `serve.sh`; commit 8a9f722. Note for accuracy: the "~90% in a week" figure is not Ebbinghaus's data — he measured ≈56% forgotten after 1 hour, ≈66% after 1 day, ≈75% after 6 days.

### USER
> "Real commands confirmed (infographic, slides, data-table, download and more). Adding the NotebookLM section to the assistant's instructions:" and whenever you make a video or picture, you should remove nlm watermark and put logo of anotherwordfor.net (you will find it on the site) instead

**Done:** BRANDING RULE added to the :8097 system prompt; real logo fetched from the site (open book, blue covers, orange bookmark — WordPress custom logo `cropped-word-synonym-finder.png`) → glottos-marketing/state/brand/ (+README: low-res source → corner mark ≤160 px + typed wordmark; never redraw).

### USER
> awf is nlm based? we should have in the list of experts if it is collecting info on a daily basis

**Done:** yes (continuous cycles, not just daily). `/app/state/awf_heartbeat.py` publishes the monitor's own counts every 5 min (1,581/2,047 videos transcribed, 1,997 with comments, 191 batches digested, 49 channels) → Experts row "awf-market-monitor"; re-armed on restart by `ensure_awf_heartbeat` in runner/loop.sh.

### USER
> the target would be to generate a youtube shorts formatted video to post it on anothewordfor.net youtube channel by starting the series of video adressing this particular pain point
> https://www.youtube.com/@anotherword8913
> this is the channel

**Done (draft):** series "Words That Stick", Ep 1 rendered by a reusable builder `glottos-marketing/shorts/build_short.py` (JSON unit → HTML frames with real AWF logo → headless Chrome PNG → edge-tts en-US-ChristopherNeural → ffmpeg): 44.8 s, 1080×1920, Shorts safe zones respected, hook "You'll forget 3 out of 4 new words by next week" (Ebbinghaus-correct), preview http://localhost:8097/state/words-that-stick-ep01.mp4. Existing videogen (Phase A) has no YouTube OAuth yet → upload is manual until the one-time OAuth is done. Built BEFORE the rule below → draft only.

### USER
> you should use at maximum possibilities of nlm to build a structured template with nice infographics and mix this with available out of the shelf video libraries for python and create and automatic video based on bullit proof feedback from market. But before any video you should write an article ready to be published on the anotherwordfor.net site and this will be you scenario for the video shorts. Which should be addictive to scroll and which will give immence value to user to solve this defined problem based on best practices what worked at competition. All our exchange on this topic here you should also double store as a chat history in the nlm document in ordert that we can always come back and correct something, this rule of chat saving is universal for all projects we run, so you can see how it is realised in those ones

**Decision / order:** (1) this journal + status mirrored into the notebook now (universal rule); (2) "PROBLEM 01" evidence document (40 competitor videos, traction + transcripts) into the notebook; (3) NotebookLM analysis of what worked; (4) publish-ready anotherwordfor.net article = the Shorts scenario; (5) only then the video: NotebookLM infographics (re-branded: watermark removed, AWF logo) + a Python video library.

**Progress after that message (2026-09-27, same session):**
- Chat mirror set up: `docs/nlm-mirror/discussion-journal.md` + `status.md`, `scripts/sync-nlm-mirror.sh` → sources "MIRROR — discussion journal (verbatim)" / "MIRROR — status". Universal rule saved to Claude's memory for all projects.
- PROBLEM 01 document added: "PROBLEM 01 — memorize new words, forget them in days: competitor traction + transcripts" (40 videos: median 614,706 views, median engagement 3.68%, max 7.13%; 38 transcripts; TikTok discover findings). Breakouts are SMALL channels: "easyway, actually" 157k subs → 5.2M views (32.8×), "The Peak Circuit" 51k → 1.4M (27.7×), Wealth & Drive 67×.
- NotebookLM synthesis (1 query) added: "PROBLEM 01 — synthesis …". Ranking: (1) words in context/sentences = biggest total reach; (2) active recall = biggest reach beyond subscribers; (3) mnemonics/memory palace; (4) spaced repetition = highest engagement (Dogen 7.13%); (5) output/self-talk. Learners' words centre on the blank mind when speaking ("I can understand 100% of the video, but when I try to speak, my mind goes blank"). Two NotebookLM figures rejected as overstated ("4× stronger", "70% by day 3").
- ARTICLE written (the Shorts scenario): `content/articles/p01-why-you-forget-new-words.md` — "Why You Forget New Words in Days — and the 15-Minute Sentence Method That Makes Them Stick", 1,291 words, 7 sections, rules: sentence not naked word · cover-and-recall · day 1·3·7 · register + avoid-when · speak it; sources Ebbinghaus 1885, Roediger & Karpicke 2006 (≈61% vs ≈40% after a week), Cepeda et al. 2006. Added as source "ARTICLE — P01 …".
- SCENARIO: `content/articles/p01-shorts-scenario.md` — 6 episodes, one per article section; added as source "SCENARIO — P01 …".
- First NotebookLM infographic requested (portrait, instructional, focus = Ep 1) to test the infographic → rebrand pipeline.

**2026-09-27 ~11:08 — session crash (whole WSL VM rebooted, all containers restarted).** Ep 1 v2 render was cut off mid-run; the layout patch (panel split on blank gaps, bigger panels, centred cards, captions break at punctuation) had already been saved. Re-rendered after restart: 46.9 s, 1080×1920.

**USER (verbatim):** "and let me know where I can see this video"
→ Published: http://localhost:8093/words-that-stick-ep01-v2.mp4 (glottos-files static server).

**USER (verbatim):** "would be moving to cloud solution "cloud sessions, on top of your plan limits" solve the problem of crash? what really happened btw.?"
→ The WSL/Docker Desktop VM itself restarted at ~11:08 (host uptime reset, every container restarted at 11:08:52). The Linux logs from before the reboot are gone, so the exact trigger isn't provable from inside. Swap now reads 0 (the .wslconfig swap=8GB from 08-22 isn't active) → a memory spike has no cushion. Cloud sessions would survive a local reboot, but they can't reach the local Docker containers, localhost ports or NLM cookie stores this work depends on → not a fix for this project.

**USER (verbatim):** "the logo is wrong you can look to youtube channel to see the right one https://www.youtube.com/@anotherword8913"
→ Official logo = the channel avatar (boy reading + "AnotherWordFor" + "Find Synonyms In Seconds"), saved as state/brand/awf-logo-channel.jpg; builder top bar + :8097 branding rule switched to it; the book icon (awf-logo-512.png) is favicon only.

**USER (verbatim):** "also make a tab in somewhere here http://localhost:8093/ to have choice between less robotized voices"
→ http://localhost:8093/ is now "Glottos Studio" with Videos + Voices tabs. 8 edge-tts voices read the same Ep 1 lines (Multilingual "conversation" voices = least robotic) + the NotebookLM podcast card. "Use this voice" saves voices/choice.json; the builder uses it unless a unit locks its voice. glottos-files now runs glottos-auto/files_server.py (static + /api/files + /api/voice).

**USER (verbatim):** "also you should add a synonym spin of it, because the channel is about synonyms and this goes hand in hand in "not learning words naked", meaning that you give 5-10 synonyms and this way learn picture aligned with word"
→ Ep 1 got a synonym ladder for "livid": cross → irate → fuming → seething → furious → livid → incensed → apoplectic, one picture each (NotebookLM infographic "One word, eight pictures", split into 4 band panels). Standing rule: every episode carries a synonym spin.

**USER (verbatim):** "i want you to have voices which are much more like podcast inside of nlm, you can make a sript for it and they will do the job, make a script ready for the audio overview (brief one) and try to do it this way"
→ content/articles/p01-ep01-audio-script.md → source "AUDIO SCRIPT — Ep01 …" → `audio create --format brief --length short` with a perform-this-script focus. First run used the old "naked" wording → regenerated after the wording fix.

**USER (verbatim):** "I am not sure that "naked" is appropriate word and take this en-AU-WilliamMultilingualNeural to try out anouther version, also save it under another name"
→ Agreed: "learn a word naked" isn't idiomatic; the standard phrase is words "in isolation" vs "in context"; hook = "Never learn a word alone". Fixed in unit, article, scenario, audio script, NotebookLM sources, and a new Ep 1 infographic was ordered (the old one printed "NAKED WORD"). William version = shorts/units/ep01_v3_william.json → words-that-stick-ep01-v3-william (v2 kept).

**USER (verbatim):** "btw. you should have a language expert who is checking this each time you are writing a scenario, meaning ask the nlm or even yourself, is it correct english to say "word naked"? and I am sure you will not come up with such video. This check routine should be part of the process/agent"
→ Hard gate: shorts/lang_gate.py stamps a hash of all text; build_short_v2.py REFUSES to render an unapproved unit, and any text edit voids the approval. Agent glottos-language-editor (web/dictionary check, NotebookLM second opinion for doubtful cases, also checks text inside images). Rule added to the :8097 assistant.

**USER (verbatim):** "btw. create agent responsible for each and every step in the process we discussed so far"
→ ~/.claude/agents/: glottos-pain-researcher, glottos-article-writer, glottos-format-strategist, glottos-scenario-writer, glottos-language-editor, glottos-visuals, glottos-voice, glottos-shorts-builder, glottos-publisher. Map: docs/pipeline.md.

**USER (verbatim):** "also consider other format like flashcards if they are more appropriate for the episode content you are about to make. For this you should create a dedicated agent checking this"
→ glottos-format-strategist (step 2b, before the scenario): picks infographic Short / flashcards / quiz / slides / podcast / video overview / data table / mind map per episode, from competitor evidence. First run on Ep 1 includes a real NotebookLM flashcard test.

**Language editor, first runs (2026-09-27):** Ep 1 text approved after fixes ("learned the word alone" → "on its own"; "nothing to hold it in place"; audio script "literally can't speak" → "barely"; article grammar). Caveats for the user: synonym order is solid only at the ends (cross … apoplectic), the middle words differ in flavour, not strength; Ebbinghaus 56/66/75% are savings scores, so "you'll forget 3 of 4 words by next week" overclaims (proposed: "Most new words are gone within a week"), user decision pending.
**New Ep 1 infographic (v3)** had a typo ("56% ofter 1 hour", "deletes words on schedule") → not used except its correct card "Avoid learning words in isolation" (grid split). Regeneration was rate-limited by NotebookLM.
**Format strategist on Ep 1:** flashcards fit the synonym part, not the whole episode: picture-first quiz cards for cross / seething / livid / apoplectic (unambiguous pictures), show-with-word for irate / fuming / furious / incensed (scenes too similar). NotebookLM flashcards test: 8 text cards, good after edits, not publishable raw (strength labels contradict the infographic, "literally"). The builder needs a flip-card beat + word-hidden picture crops (not built yet). Spin-off idea: "Picture test: 8 kinds of angry" Short. File: content/articles/p01-ep01-format.md.

**USER (verbatim):** "I would apply the voice from podcast but at 0.9 speed as they are way to fast"
→ The NotebookLM brief podcast (single host, 85.7 s) slowed to 0.9× with pitch kept (95.3 s), transcribed locally (faster-whisper small.en, word timings). New podcast mode in the builder: the recording drives the timing, pictures are pinned to what the host is saying, captions come from the transcript. Language gate on the real recording: cut "of memory" ("we lose 56 percent in an hour") and "literally", re-cut by the editor at acoustic boundaries; caption fixes Hermann / cancelled / anotherwordfor.net. The editor BLOCKED the synonym sheet: its label "Mild" sits above IRATE (irate = very angry) → the strength labels are cropped off in all versions. Unit: shorts/units/ep01_v4_podcast.json → words-that-stick-ep01-v4-podcast. The Voices tab's NotebookLM card now plays the 0.9× podcast.

**USER (verbatim):** "I do not see video"
→ My fault: the render loop had no publish step. Published http://localhost:8093/words-that-stick-ep01-v4-podcast.mp4 (94.7 s), then v3-william (70.9 s); v2 re-renders with Andrew (picked on the Voices tab) → words-that-stick-ep01-v2-andrew.mp4. Old "naked" v2 removed from :8093.

**USER (verbatim):** "what about agents, did you create all of them and now have a clear path which one does what and when?"
→ Yes: 9 agents (~/.claude/agents/glottos-*), order + owner per step in docs/pipeline.md. Gap found: publishing to :8093 must always follow a render (publisher step).

**USER (verbatim):** "also we need to put the video directly to youtube studio and I will approve them or delete from there directly" / "final word is mine, but video should be in the channel account alreadz" / "you should also prepare description for the video" / "for youtube"
→ Decisions (user answers): the channel belongs to a SEPARATE Google account; upload via YouTube Studio browser automation (the official API locks uploads from unaudited apps to Private, so the user couldn't publish). New container yt-studio (:8115 noVNC, own Chromium profile volume yt-studio-chrome, uploader yt-studio/upload.py → always PRIVATE draft + ledger). Metadata content/youtube/ep01.json (title "Stop forgetting new words: never learn a word alone | Words That Stick #1", description, tags), language-gated (fixes: synonym list not a strict ranking; "re-reading isn't enough"). Waiting: the user signs in once at http://localhost:8115/vnc.html as the channel account.

**USER (verbatim, replying to the Ebbinghaus question):** "I would say that this is indeed useless information especially for shorts format. Nobody cares who said what. You should go straight to the point without saying "debrief" and so on. If possible to cut audio without revamping everything, do it"
→ Cut from the podcast audio (no regeneration): "This is the brief on why you should never learn a word alone." and "First, why does the brain dump words? Herman Ebbinghaus found in 1885,"; the language editor also cut the orphaned "Second," and re-approved. Ebbinghaus removed from the YouTube description. Standing rule in the scenario-writer/voice agents: hook in the first second, no intros, no who-said-what. Result = new version v5 (words-that-stick-ep01-v5-podcast-cut).

**USER (verbatim):** "continue to generate other videos for other episodes taking into account what we discussed and do not delete any versions of videos, just add new ones"
→ Rule: never delete/overwrite; the builder now refuses to render into an existing version. Honest loss report: the 11:34/11:45 "naked" v2 renders are gone (published copy deleted before the rule; working copy overwritten by the Andrew re-render). All other versions are on :8093 (v1, v2-andrew, v3-william, v4-podcast, v5 when rendered). Episodes 2–6 started: format strategist deciding formats + synonym spins for all five.

**USER (verbatim):** "podcast voice is the one you should use but avoid anything which indicates that this is podcast, like "debrief" and so on"
→ Standing rule (voice, scenario-writer, language-editor agents + memory): every episode = NotebookLM brief Audio Overview at 0.9×; the script focus forbids podcast markers (brief/debrief, welcome, today we, in this episode, let's dive in, listeners, podcast, show, sign-offs); anything that slips through is cut from the audio at acoustic boundaries and re-gated.

**USER (verbatim):** "you do not publish you just give it at http://localhost:8093/ and I decide further"
→ Rule: the deliverable ends at http://localhost:8093/ (videos + YouTube metadata ready in content/youtube/). No upload anywhere unless the user explicitly asks for a specific video. yt-studio (:8115) stays on standby, unused.

**USER (verbatim):** "you need also to create agent which task is to see those videos from user point of view and answer "does it solve the pain point we identified earlier"?"
→ New agent glottos-viewer-critic (step 7b, after render, before handing to the user on :8093): learner quotes from the PROBLEM doc → frames per beat + timed transcript of the final video → verdict SOLVES / PARTLY / DOESN'T, swipe-away moments, the one action a viewer can take, top 3 fixes with owner agent → content/reviews/<video-id>.md. Read-only.

**USER (verbatim):** "yes everything should run strictly in series"
→ Rule: one step / agent / render / NotebookLM generation at a time; the next starts only when the previous has finished.

**USER (verbatim, relayed by the coordinator during the Ep2–6 format run):** "podcast voice is the one you should use but avoid anything which indicates that this is podcast, like "debrief" and so on"
→ Applied in glottos-format-strategist Ep2–6 (content/articles/p01-ep02…06-format.md): voice = NotebookLM brief Audio Overview at 0.9× for every episode. Every audio focus forbids podcast markers ("This is the brief", "debrief", "welcome", "today we", "in this episode", "let’s dive in", "on this show", listeners/hosts/podcast/episode mentions, sign-offs), starts on the hook and ends on the CTA. Anything that still slips through is cut from the audio at acoustic boundaries.
**Format decisions Ep2–6 (strategist, 2026-09-27; evidence = PROBLEM 01 synthesis read via source content, no query, no generation):** Ep2 quiz-led (3 cover-the-answer quizzes, 40 vs 61 bars; spin swamped ×7). Ep3 calendar panels, shorter 60–75 s (spin "remember" ×7; quiz optional). Ep4 quiz-led "Friends or work?" with register chips rendered by the builder, never by NotebookLM (spin "I don’t know" ladder ×6). Ep5 numbered 3-block panels + "your turn" speak pause (spin routine ×8). Ep6 mechanism panels + comment CTA, shorter 65–80 s (spin "mind goes blank" ×8; optional series mind map). Builder gaps: inserted silence in the podcast track + quiz beat (essential for Ep2 and Ep4), tag card, picture+text beat, word-masked crops, carousel export. Open question for the article writer: Day 1 = "see again" (§4) vs "recall words from day 1" (§6).

**Viewer critic on Ep1 v5 (2026-09-27): PARTLY solves the pain.** Good: opens on the pain, one good rule ("give it a scene, put it in a sentence"), no podcast markers, logo right, no watermark. Gaps: no self-test; 85 s with ~38% text-only cards; eight C1/C2 anger words (too many for B1); the only takeaway ("grab five synonyms") doesn't fix forgetting; fragment lines; weak text-only first frame. Swipe risks at 0–1.5 s, 27–36 s (static "synonym spin" card), 66–85 s (long static CTA). Full review: content/reviews/words-that-stick-ep01-v5-podcast-cut.md.
**Site check (verified):** anotherwordfor.net has 78 posts; search for livid/furious returns "nothing matched"; no pages for angry, busy, remember → the Ep1 CTA sends viewers to an empty result. SSL certificate expired 2024-02-05 (still). Decision (default, user may override): from Ep2 on, the synonym-spin word must be one with an existing page and the CTA names that page; ≤60 s; one real self-test (quiz beat); end on an action for tomorrow. Ep1 versions stay as they are. Open for the user: renew SSL; whether the site should get new pages for the words the videos need.

**Ep2 progress:** script + visuals text language-gated (site has no search box → CTA "look up 'another word for important' on anotherwordfor.net"; "word family" removed). Pictures BLOCKED: NotebookLM infographic daily limit on drawnformula (every attempt 13:23–13:44 rate-limited) → retry tomorrow. Audio made (artifact 11e2f926, from source ff55e7a9): NotebookLM paraphrased, reordered, added "This is the brief…", "Keep it punchy", "literally", a car comparison; skipped the opening line and one quiz. Cut to 67.7 s with 3 inserted quiz pauses.
**Question to the user:** NotebookLM paraphrases instead of reading the script; how should episodes get their voice?
**USER (answer):** "Podcast voice, flexible script" → rule: scripts = talking points; beats, pictures and quiz cards are built around what the host actually says; cut only podcast markers, false claims, filler, excess length.
autopilot 2026-09-27T17:10Z: Ep4 gate_text done — glottos-language-editor approved audio script, visuals and ep04.json (register labels for the 'help' ladder fixed, aid framed as a news noun, §5 site overclaim kept out, CTA /another-word-for-help/ verified live, teaser → the 15-minute routine). Next step: Ep4 audio.
autopilot 2026-09-27T17:19:04Z: channel reply_drafts done — glottos-comment-responder queued 2 reply drafts on :8093 Replies (awaiting user approval, nothing posted); 4 of 6 unanswered comments skipped (spam/meme/timestamps; the 'how did you edit this video' question needs the user).
autopilot 2026-09-27T17:21Z: Ep4 audio — source 4faf3c0a added (Ep4 audio script), audio create RATE-LIMITED by NotebookLM (no retry); Ep4 blocked until 2026-09-27T19:21Z, next attempt reuses the source.
autopilot 2026-09-27T17:37Z: Ep5 scenario done — glottos-scenario-writer wrote p01-ep05-audio-script.md, p01-ep05-visuals.md, content/youtube/ep05.json (hook keeps Ep4's promise, teaser 'Next: why your mind goes blank', 'your turn' speak beat with swamped). Spin word 'never give up' (anotherwordfor.net/never-give-up-synonym/ 200; no routine/habit/ritual page exists). Next step: Ep5 gate_text.
autopilot 2026-09-27T17:39Z: Ep5 gate_text done — glottos-language-editor approved audio script, visuals and ep05.json (CTA reworded to 'Find more ways to say "never give up" on anotherwordfor.net', obstinate chip → 'negative · disapproving', relentless line clarified, audio-script header trimmed). Next step: Ep5 audio.
autopilot 2026-09-27T17:42Z: Ep5 audio — source ce29fbdc added (Ep5 audio script, focus in state/nlm-raw/ep05-focus.txt), audio create RATE-LIMITED by NotebookLM (no retry); Ep5 blocked until 2026-09-27T19:45Z, next attempt reuses the source.
autopilot 2026-09-27T17:47Z: Ep6 scenario done. glottos-scenario-writer wrote p01-ep06-audio-script.md, p01-ep06-visuals.md and content/youtube/ep06.json. The hook is the article's verbatim 'mind goes blank' quote, which keeps Ep5's promise; the spin is 5 'blank moment' phrases (choke, clam up and lost for words dropped); the CTA is the anotherwordfor.net homepage (no forget/blank page returns 200); it ends with the series close and the pointer to the 'Words That Stick' playlist. Next step: Ep6 gate_text.
autopilot 2026-09-27T17:51Z: Ep6 gate_text done — glottos-language-editor approved audio script, visuals and ep06.json ('sentence method' → 'learning words in sentences', closing line → 'Watch the full series from Episode 1 in the "Words That Stick" playlist.', playlist URL placeholder in description, 5 phrase labels checked against Cambridge/Longman). ~195 words, at the 75 s cap. Next step: Ep6 audio.
autopilot 2026-09-27T17:58Z: Ep6 audio — source f3b1640e added (Ep6 audio script, focus in state/nlm-raw/ep06-focus.txt), audio create RATE-LIMITED by NotebookLM (no retry); Ep6 blocked until 2026-09-27T19:58Z, next attempt reuses the source.
autopilot 2026-09-27T19:52Z: Special S1 (Synonym Memory Challenge: HAPPY) script done — glottos-scenario-writer wrote content/specials/S1/script.md (995 spoken words, list → pause → 15-word story ladder content…ecstatic with 5 sneaky extras → pause → '15, not 10' reveal → score challenge), focus.txt (1777 chars) and meta.json. Hook softened to avoid an unsupported 'most people remember 5' claim; title drops 'you' per research (0.40 vs 0.72 median views/sub). Next step: S1 gate_text.
autopilot 2026-09-27T19:57Z: Special M1 (P01 mid-length explainer) script done — glottos-scenario-writer wrote content/specials/M1/script.md (893 spoken words, ~6:35), focus.txt and meta.json. Leads with the best-confirmed method 'use it: speak/write' (440 proof, 90% confirm), then words in sentences, then spaced recall as timing; 3 verbatim learner quotes; title 'How to Remember New Words: 3 Easy Steps That Make Them Stick' (how-to/easy/number patterns, no 'you'). Next step: M1 gate_text.
autopilot 2026-09-27T22:33Z: Special M1 gate_text done. glottos-language-editor APPROVED script.md, focus.txt and meta.json (a re-run: the 19:58Z run had stalled). Fixes: the false 'search / example sentences' website line became 'look up "another word for happy" on anotherwordfor.net'; the day 1/3/7 review steps are now consistent; about 14 wording fixes; the description sources line cites Roediger & Karpicke 2006 and doesn't name Ebbinghaus. 922 spoken words (~6:46). Next step: M1 nlm_video.
autopilot 2026-09-27T22:47Z: special M1 nlm_video done on work2 — new notebook 'Glottos — Production (work2)' (968fad6b) with only the approved script as source; explainer/whiteboard video 'Remembering New Words' downloaded → content/specials/M1/m1-v1.mp4 (5:48). Next: critic.

autopilot 2026-09-27T22:52:09Z: special M1 critic → PARTLY (critic-v1.md): method-first + routine land, no forbidden figures; fix-in-edit list: quiz gaps/leaked answers 5:11–5:28, Gemini watermark + end card, duplicate STEP 3 banner, markdown caption. Next: studio.
autopilot 2026-09-27T22:53:18Z: special M1 studio done — m1-v1.mp4 copied to glottos-auto/out/specials/ (on :8093 Videos); the critic's PARTLY fix list is in ask-user.md for the user's review. Next: M1 yt_meta_gate.
autopilot 2026-09-27T22:55:54Z: special M1 yt_meta_gate done — content/youtube/m1.json approved by the language editor unchanged (16:9, PRIVATE, not in the playlist). Open: anotherwordfor.net TLS cert expired (site P0). Next: M1 upload (PRIVATE).
autopilot 2026-09-27T22:57:04Z: special M1 upload BLOCKED — yt-studio says NOT SIGNED IN (Studio → accounts.google.com); nothing uploaded. M1 → ask_user: sign in at http://localhost:8115/vnc.html, then resume the upload (question on :8093 ask-user.md).
autopilot 2026-09-27T23:00:24Z: Special S1 (HAPPY) gate_text done — glottos-language-editor APPROVED script.md, focus.txt, meta.json after fixes: false 'examples' CTA → 'look up "another word for happy" on anotherwordfor.net'; on cloud nine / jubilant / joyful / elated / over the moon meanings+registers corrected; upbeat line made logical; 'content' pronunciation cue. 973 spoken words (~7 min). Note: runbook CTA 'every synonym with examples' is false for the site — fix for S2–S5. Next: S1 nlm_video.
autopilot 2026-09-28T05:29:59Z: special M1 polish round 1 done — m1-v2 (end card/watermark/quiz/step-number/filler fixes) → language gate NEEDS FIX (quote 3 grammar, quote 2 gibberish) → m1-v3.mp4 (332 s) → lang-gate-v3 APPROVED. Next: critic on m1-v3.
autopilot 2026-09-28T05:44:18Z: special M1 critic on m1-v3.mp4 → SOLVES, no ship-blocking defect (all v1 blockers fixed; minor notes: late hook slide, near-answer words on the 'crucial' quiz slide, slow theory stretch). Next: M1 studio (copy v3 to :8093).
autopilot 2026-09-28T05:45:09Z: special M1 studio done — m1-v3.mp4 (critic SOLVES) copied to :8093 Videos (specials/m1-v3.mp4), review note added to ask-user.md. Next: M1 yt_meta_gate (point m1.json at v3, 5:32); upload still waits for YouTube sign-in.
- autopilot 2026-09-28T05:49:10Z: special M1 yt_meta_gate done — language editor APPROVED content/youtube/m1.json against m1-v3 (5:32); one description line reworded (15-minute routine, no 'daily'). Next: M1 upload (private).
- autopilot 2026-09-28T05:50:25Z: special M1 upload STOPPED — YouTube Studio signed out (upload.py NOT SIGNED IN), nothing uploaded. M1 → ask_user (resume_step upload); user asked to sign in at :8115 (ask-user.md). S1 continues independently.
autopilot 2026-09-28T06:05:13Z: special S1 nlm_video done on work2 — approved S1 script added as the only source used (11854cfd) in 'Glottos — Production (work2)'; explainer/whiteboard video downloaded → content/specials/S1/s1-v1.mp4 (7:10). Next: S1 critic.

- autopilot 2026-09-28T06:21:09Z: S1 critic on s1-v1.mp4 (7:10) → PARTLY. All challenge beats survived in order; blocking = Gemini watermark/end card, wrong ladder-recap table (Elated twice, Jubilant blank), no real pause after the pause cues — all fixable in post. Next: polish → s1-v2.
autopilot 2026-09-28T06:39:07Z: special S1 polish → s1-v2.mp4 (6:58; end card+watermark fixed, own 15-row HAPPY ladder, 3 s pause holds, filler cuts). Language gate v2 NEEDS FIX: 'Say it with me. Content.' drilled as CON-tent → next tick polish s1-v3 cuts that line, then critic.
autopilot 2026-09-28T10:52:46Z: Ep2 visuals — main infographic create RATE-LIMITED by NotebookLM (drawnformula, code 8); nothing generated, no retry; Ep2 blocked until +2 h, Ep3–6 NLM steps keep waiting in series.
- autopilot 2026-09-28T10:55:59Z: special S1 polish finished. s1-v3.mp4 (415.83 s) cuts the wrong-stress 'Say it with me, CON-tent' drill, adds a con-TENT on-screen cue and fixes the ladder Glad row wording. The language gate v3 APPROVED it. Next: critic on s1-v3.
- autopilot 2026-09-28T11:00:21Z: special S1 critic on s1-v3.mp4 (6:56) → SOLVES, no ship-blockers (ladder correct, real pause holds, no Gemini branding). Non-blocking: no art for cheerful/thrilled, possible CON-tent in voice. Next: studio.
- autopilot 2026-09-28T11:01:12Z: special S1 studio — s1-v3.mp4 copied to glottos-auto/out/specials/ (:8093 Videos), review note in ask-user.md. Next: yt_meta_gate (then private upload, which needs the YouTube sign-in).
- autopilot 2026-09-28T11:06:26Z: special S1 yt_meta_gate APPROVED against the final s1-v3.mp4 → content/youtube/s1.json (title 'Can You Remember 15 Synonyms for HAPPY? (Memory Challenge)', description now matches the video's own wording and labels). Next: private upload, which needs the YouTube sign-in (signed out since 05:50Z).
- autopilot 2026-09-28T11:07:21Z: special S1 upload — YouTube Studio still signed out (signed_in.py SIGNED_OUT); nothing uploaded. S1 parked at ask_user (resume_step=upload), question written to ask-user.md; auto-resumes after sign-in at :8115.
- autopilot 2026-09-28T11:13:44Z: special S2 (SAD) script written — content/specials/S2/script.md + focus.txt + meta.json; 10-word list + 15-word birthday story (blue → inconsolable), 995 spoken words (~7:12), title 'Can You Remember 15 Synonyms for SAD? (Memory Challenge)'. Next: gate_text (language editor).
- autopilot 2026-09-28T11:17:04Z: special S2 (SAD) gate_text — glottos-language-editor APPROVED script.md, focus.txt, meta.json after minimal fixes (glum informal label, melancholy used in its own story line, down-in-the-dumps and miserable glosses, recall tip in order, light trims → 969 spoken words, ~7 min). Next: S2 nlm_video.
- autopilot 2026-09-28T11:30:38Z: special S2 (SAD) nlm_video done on work2 — approved S2 script as the only source used (64c4b4c5) in 'Glottos — Production (work2)'; explainer/whiteboard video downloaded → content/specials/S2/s2-v1.mp4 (7:28). Next: S2 critic.

- autopilot 2026-09-28T11:36:33Z: special S2 critic on s2-v1.mp4 → PARTLY (beats + 15 words intact; ladder table 8/15 rows, comment CTA dropped, short pauses, Gemini watermark/end card — all fixable in post). Next step: polish → s2-v2. Report content/specials/S2/critic-v1.md.

autopilot 2026-09-28T11:43:32Z: special S2 polish -> s2-v2.mp4 (end card/watermark gone, 15-row ladder, comment CTA + 3 s hold, longer pause holds, spoken-slip splice); language gate APPROVED after one fix; next step = critic on v2.
- autopilot 2026-09-28T11:56:53Z: special S2 critic on s2-v2.mp4 → SOLVES, no ship-blockers (beats intact, v1 blockers all fixed). Next step: studio. Report content/specials/S2/critic-v2.md.
- autopilot 2026-09-28T11:57:48Z: special S2 (SAD) studio — s2-v2.mp4 copied (cp -n, verified) to glottos-auto/out/specials/ (:8093 Videos); review note added to ask-user.md. Next step: yt_meta_gate.
- autopilot 2026-09-28T12:01:32Z: special S2 (SAD) yt_meta_gate → APPROVED on final s2-v2.mp4 (7:33); content/youtube/s2.json written (2 small description fixes to match the voice). Next step: upload (PRIVATE, needs YouTube sign-in).
- autopilot 2026-09-28T12:02:25Z: special S2 (SAD) upload — YouTube signed out (signed_in.py SIGNED_OUT); nothing uploaded; S2 parked at ask_user (resume_step=upload, auto-resumes on sign-in), question written to ask-user.md.
user 2026-09-28T16:05Z (verbatim): "you generated two identical videos on http://localhost:8093/ , one is 5:32 long and another 5:47, meaning you spent twice precious limits of nlm to generate same videos, why?"
claude: not a second generation. m1-v1 (5:47) = the ONE NotebookLM video (09-27 22:34, work2); m1-v3 (5:32) = a local ffmpeg polish of v1, no NLM. Real bug: the studio step adds every version to :8093 and never retires the old one. Proposed (awaiting the user): remove m1-v1 from :8093 + studio step replaces the previous version.
user 2026-09-28T16:08Z (verbatim): "I think you can remove now \"voices \" tab, as we decided to go along with the nlm podcast voice over"
claude: DONE. :8093 Voices tab removed (glottos-auto/out/index.html, backup index.html.bak-20260928-voices). Decision: voice-over = NotebookLM podcast. /api/voice and voices/choice.json (Andrew) are left in place, and only an edge-tts fallback render (a unit without "audio") still reads it.
user 2026-09-28T16:15Z (verbatim): "if you did not spend limits of nlm twice, you can have both videos with different vesions, I wanted to be sure that there no fundamental bug"
claude: decision = keep every version on :8093 (no retire-old-version change). Confirmed: 1 NLM video generation per special (M1 22:34, S1 05:51, S2 11:17), and polish versions are local ffmpeg.
autopilot 2026-09-28T16:17Z: ep2 visuals — syn sheet done (split→gap); main infographic rejected (NLM added forbidden captions/'brain', leaked letters in panel 4); regenerate main sheet next tick, no rate limit.
user 2026-09-28T16:30Z (verbatim): "why it takes so long to upload videos?"
claude: cause = due.py priority: a due EPISODE step always won over specials, so M1/S1/S2 (auto-resumed to upload 15:53) queued behind Ep2 visuals ticks (~23 min each, repeated while NLM infographics get rejected). Fix: due.py now runs any due upload (episode or special) first (backup due.py.bak-20260928-uploadfirst). Takes effect after the running Ep2 tick; order M1 → S1 → S2, one tick each.
autopilot 2026-09-28T16:33Z: ep2 visuals — syn sheet done; main sheet regen (art 983e7148) never completed (status unknown 25 min, download fails) → treated as NLM limit, ep2 blocked_until 18:35Z; later episodes keep waiting.

autopilot 2026-09-28T16:43:28Z: special M1 upload — 'How to Remember New Words: 3 Easy Steps That Make Them Stick' (m1-v3, 5:33) uploaded as PRIVATE draft https://youtu.be/GNH19NdTu9U; Studio-verified metadata. Fixed upload.py link selector (it crashed after creating the draft). Next: publish_log.
autopilot 2026-09-28T16:48:58Z (auto_upload, no Claude): special S1 upload attempt 1 failed (  - waiting for locator("#next-button"))
autopilot 2026-09-28T16:52:21Z (auto_upload, no Claude): special S1 'Can You Remember 15 Synonyms for HAPPY? (Memory Challenge)' uploaded as PRIVATE draft https://www.youtube.com/watch?v=O5vQex4ylbw; finish: language=English, playlist created PRIVATE + added; verify: ALL OK; outside view: private ✓
autopilot 2026-09-28T17:05:26Z (auto_upload, no Claude): special S2 upload attempt 1 failed (  - waiting for locator("#create-icon"))
autopilot 2026-09-28T17:07:32Z (auto_upload, no Claude): special S2 'Can You Remember 15 Synonyms for SAD? (Memory Challenge)' uploaded as PRIVATE draft https://www.youtube.com/watch?v=GeqYKAA7DyQ; finish: language FAILED (TimeoutError), category FAILED (TimeoutError), playlist FAILED (TimeoutError); verify: CHECK title, language, category, playlist, not_for_kids, studio_private; outside view: oEmbed 200 ✗
claude 2026-09-28T17:17:01Z: CORRECTION — S2 17:07Z 'oEmbed 200 / may be viewable' was a FALSE alarm: the recorded link GeqYKAA7DyQ is a Creator Insider video from the Studio dashboard (page-wide link selector). S2's real id gets resolved by exact title on the next upload run; alert entry removed from ask-user.md.
autopilot 2026-09-28T17:20Z: channel monitor ran but YouTube Studio is signed out — no new snapshot (report.md marked stale, audience-needs.md created from 09-27 data); nothing new to draft replies for. Resumes after sign-in (already asked in ask-user.md).
autopilot 2026-09-28T17:19Z: special M1 publish_log — M1 v3 'How to Remember New Words: 3 Easy Steps That Make Them Stick' (5:32, critic SOLVES, lang/meta gates APPROVED) is a PRIVATE draft https://youtu.be/GNH19NdTu9U (Studio-verified: private, not for kids, Education, English); user decides visibility. Mirror synced, text artifacts committed.
autopilot 2026-09-28T17:21Z: special S1 publish_log — S1 v3 'Can You Remember 15 Synonyms for HAPPY? (Memory Challenge)' (6:56, critic SOLVES, lang/meta gates APPROVED) is a PRIVATE draft https://www.youtube.com/watch?v=O5vQex4ylbw, in the private playlist 'Synonym Memory Challenge'; user decides visibility. Mirror synced, text artifacts committed.
autopilot 2026-09-28T17:27Z: special S3 (BIG) script — script.md (967 spoken words, ~7 min, pumpkin-show story, 15-word ladder large→ginormous) + focus.txt + meta.json written; next step gate_text (language editor to verify register labels and the 'strongest word' claim).
autopilot 2026-09-28T17:32Z: special S3 (BIG) gate_text — language editor APPROVED script.md/focus.txt/meta.json after 12 fixes (register labels verified vs Oxford/Cambridge; 'ginormous = strongest' claim dropped; respelling removed); 970 spoken words; next step nlm_video.

autopilot 2026-09-28T17:48:14Z: special S3 nlm_video done — work2 video limited, work4 generated s3-v1.mp4 (7:16) from the approved script; next step critic.

- autopilot 2026-09-28T17:54:30Z: special S3 critic on s3-v1.mp4 (work4, 7:16) → PARTLY, fixable in post: bulky/hefty lack pictures, whopping not captioned, pause holds too short, towering caption overstated, Gemini watermark/end card. Report content/specials/S3/critic-v1.md; next step polish (s3-v2).
user 2026-09-28T20:50Z (verbatim): "the quality of video is not HD, but SD, you need to do better than that, at least HD" + "you can do it only for those which are not uploaded yet on youtube"
claude: facts: NotebookLM specials are 1280x720 at 0.4-0.8 Mbit/s. DONE: auto_upload.py makes a 1440p master (short side 1440, lanczos+unsharp, x264 CRF 16, source untouched, <vid>-hd1440.mp4) before every NEW upload; M1/S1/S2 (already on YouTube) are left as-is (S2 hd_master=false).
user 2026-09-28T20:55Z (verbatim): "also you need to have agent which does thumbnail" + "and agent which make several proposals for A/B testing"
autopilot 2026-09-28T20:56Z: ep2 visuals — the stuck MAIN-sheet regen (art 983e7148) had actually completed; downloaded ep02-infographic-v2.png and QA'd it against focus-v2.txt. It fixed all of v1's over-generation defects (no stray captions/headers, blank card, empty thought bubble) but dropped the required Title 'Stop re-reading your word list' entirely → REJECTED (kept as ep02-infographic-rejected2.png). Wrote ep02-focus-v3.txt making the title an explicit separate mandatory line above Panel 1. Next visuals tick: one new attempt with focus-v3.txt, then split/lang-gate/render. No rate limit hit, ep2 unblocked.
autopilot 2026-09-28T20:59Z: ep2 visuals — attempted MAIN sheet v3 (focus-v3.txt, title fix) via nlm infographic create → immediate "Rate limited" (API code 8), no artifact queued. No retry per rule; blocked_until=2026-09-28T23:00Z. syn sheet still fine (unchanged); no panel PNGs exist yet for ep02 — panel-naming convention to mirror confirmed from ep01 for the next split. Next tick after unblock: one retry of the same command, then QA/split/lang-gate/render.

autopilot/language-editor 2026-09-28: special S3 polish gate v2 (s3-v2.mp4) — checked every new on-screen string from critic-v1.md's fix set (whopping word+meaning card, towering caption patch, pause-2 'In order.' chip, 'The extras:' reveal chips, the full 15-row ladder.py replacement table, 3 CTA plates, plus incidental bulky/hefty picture labels). Verified by extracting real composited frames from the rendered s3-v2.mp4 (not just the raw overlay PNGs). Cross-checked the ladder footer 'Read it from the top down' against the exact S2 lang-gate-v2 defect (a row claiming 'the top' while sitting at the bottom) — S3's layout is internally consistent (Large physically at top, Ginormous at bottom, arrow points down), so no repeat of that bug. towering no longer says 'Very literary' (now 'A bit literary', matching the voice and lang-gate-v1). Verdict: APPROVED. Report content/specials/S3/lang-gate-v2-polish.md.
autopilot 2026-09-28T21:11Z: special S3 polish done — resumed the polish-v2-build/ pipeline from an earlier interrupted tick (all overlay assets existed, render.py had never been run) and rendered s3-v2.mp4 (439.0s): pictures for bulky/hefty, whopping word+meaning card, corrected towering caption, 3s freeze holds, own 15-row ladder table, 5-extras reveal, 3 CTA plates, watermark/end-card removed. QA caught a real bug in the towering patch (background color sampled from a column that clipped into the tree illustration, leaving a dark band across the caption) — fixed by resampling from a clean column and re-rendering. Language-editor re-gate of all new text → APPROVED. Next step: critic on s3-v2.mp4.
autopilot 2026-09-28T21:18Z: special S3 critic on the polished s3-v2.mp4 (439.0s) → SOLVES, nothing ship-blocking. All 5 critic-v1 blockers verified fixed; all 6 challenge beats (list → pause → story → pause "in order" → 15-not-10 reveal + ladder → score challenge) present in order. Non-blocking notes in content/specials/S3/critic-v2.md (6-frame bulky/hefty overlap in a silent gap, clip-art style, voice "almost always" vs screen "often"). Next step: studio.
autopilot 2026-09-28T21:19Z: special S3 studio — cp -n content/specials/S3/s3-v2.mp4 → /workspace/glottos-auto/out/specials/s3-v2.mp4 (now on :8093 Videos tab); note added to ask-user.md for user review (no answer needed to continue). Next step: yt_meta_gate.
- autopilot 2026-09-28T21:24:31Z: special S3 (BIG) yt_meta_gate → APPROVED on final s3-v2.mp4 (7:19); content/youtube/s3.json written (description aligned with the voice and ladder labels, report content/specials/S3/yt-meta-gate-v2.md). Next step: upload (PRIVATE, needs YouTube sign-in).
- autopilot 2026-09-28T21:31:32Z: special S4 (BEAUTIFUL) script — content/specials/S4/script.md (988 spoken words), focus.txt, meta.json written by glottos-scenario-writer; list: exquisite, cute, gorgeous, attractive, lovely, stunning, handsome, pretty, elegant, good-looking; +5 extras picturesque, graceful, striking, radiant, breathtaking (mountain-wedding story). Register labels flagged GATE for verification. Next step: gate_text.
- autopilot 2026-09-28T21:37:32Z: special S4 (BEAUTIFUL) gate_text → APPROVED (content/specials/S4/lang-gate-v1.md). script.md + focus.txt fixed in place (stunning 'rather informal', elegant/handsome/striking meanings corrected, exquisite/radiant/graceful per Oxford/Cambridge, story timeline), meta.json unchanged; 991 spoken words. Next step: nlm_video.
- autopilot 2026-09-28T22:02Z: special S4 (BEAUTIFUL) nlm_video — work2 (notebook 968fad6b) rate-limited on the first try, no job queued. Switched to work4 (notebook 9b6f4036) and found two video jobs already sitting there from an earlier, uncompleted attempt (state had never recorded them) — did not start a third generation, just polled: 35b1b87b 'Synonyms for Beautiful' had finished, downloaded → content/specials/S4/s4-v1.mp4 (6:50.76, within the 1-8 min window). The sibling job 47ccbc33 is an unused leftover duplicate on the same notebook. Next step: critic.

autopilot 2026-09-28T22:09:52Z: special S4 critic on s4-v1.mp4 (BEAUTIFUL, work4) → PARTLY, no regeneration; 5 in-post fixes (15-row recap overlay, cute panel, 3 s pause-2 freeze, 'bride and groom' card text, Gemini watermark/end card). Report content/specials/S4/critic-v1.md. Next: S4 polish.
autopilot 2026-09-29T05:16Z: ep2 visuals — after blocked_until expired, retried the one allowed attempt of the MAIN sheet v3 (focus-v3.txt) via nlm infographic create on notebook 8306c0a9 -> immediate "Rate limited" (API code 8) again, no artifact queued (nlm studio status confirmed all 10 items completed, nothing pending). No further retry per rule; blocked_until=2026-09-29T07:16Z. No other episode's NLM work started this tick (ep3-6 remain nlm_wait behind ep2). Next visuals tick after unblock: one more retry of the same command, then QA/split/lang-gate/render.
autopilot/language-editor 2026-09-29: special S4 polish gate v2 (s4-v2.mp4, polish-v2-build/) — checked all 9 on-screen string groups from the autopilot ticket's checklist (ladder heading/note/headers, all 15 ladder rows, ladder footer + 'sneaky extras' legend, patched ending-card text, reveal chips, split CTA plate). Verified against script.md Beat 5's already-approved recap and lang-gate-v1.md's Ending fix; verified by reading actual composited frames from polish-v2-build/qa/ (v2_361.8.png ladder, v2_290.5.png ending patch, v2_319.3.png reveal chips, v2_401.08.png CTA). All 15 ladder rows match script.md verbatim (word/meaning/register notes unchanged, e.g. gorgeous keeps 'a bit informal'; stunning correctly still has no register label). Footer 'Read downward: nice to look at, then extremely beautiful' avoids 'top'/'bottom'/'strongest' entirely (stricter than the S3 precedent) and matches the actual layout (Cute drawn first, Breathtaking last, rail arrow points down) — no repeat of the S2 top/bottom-contradiction defect. Ending-card patch confirmed identical to lang-gate-v1's approved 'The bride and groom take the goat home.' Noted (not a defect, out of this ticket's scope): the pre-existing 'Which score was higher?' base card has unrelated decorative background art reading 'captivating' — same category as S3's allowed 'Gargantuan/Immense' tags. Verdict: APPROVED. Report content/specials/S4/lang-gate-v2-polish.md. Next step: critic on s4-v2.mp4 (once render.py has produced it).
autopilot 2026-09-29T05:38Z: special S4 polish complete — s4-v1.mp4 -> s4-v2.mp4 (413.29s) via content/specials/S4/polish-v2-build/ (glottos-shorts-builder, reusing S3's pattern). All 5 ship-blocking fixes from critic-v1.md applied plus 2 recommended (15-row ladder overlay replacing the half-empty/misspelled table, drawn "cute" picture, pause-1/pause-2 freeze holds, ending-card text patch, watermark/end-card removal, reveal chips, split CTA plate); items 8-11 skipped as non-blocking. Language-editor re-gate APPROVED (lang-gate-v2-polish.md, confirmed above). state/autopilot.json: S4.step -> critic, video_file -> s4-v2.mp4. Next step: critic on s4-v2.mp4.
autopilot 2026-09-29T05:45:19Z: special S4 critic on s4-v2.mp4 (polished) → SOLVES, no ship-blockers (all 5 v1 blockers fixed; cosmetic notes in content/specials/S4/critic-v2.md). Next: studio.
autopilot 2026-09-29T05:46Z: special S4 studio — cp -n content/specials/S4/s4-v2.mp4 → /workspace/glottos-auto/out/specials/s4-v2.mp4 (now on :8093 Videos tab); note added to ask-user.md for user review (no answer needed to continue). Next step: yt_meta_gate.
- autopilot 2026-09-29T05:50:55Z: special S4 (BEAUTIFUL) yt_meta_gate → APPROVED on final s4-v2.mp4 (6:53); content/youtube/s4.json written (description aligned with the ladder labels, report content/specials/S4/yt-meta-gate-v2.md). Next step: upload (PRIVATE, needs YouTube sign-in).
- autopilot 2026-09-29T05:57:04Z: special S5 (PROBLEM) script — glottos-scenario-writer wrote content/specials/S5/script.md (968 spoken words, 6 beats; birthday-cake + parrot story, 15-word ladder hiccup→disaster), focus.txt, meta.json ("Can You Remember 15 Synonyms for PROBLEM? (Memory Challenge)"). Next step: gate_text (language editor must check register labels, dilemma/disaster meanings).
autopilot 2026-09-29T06:01:43Z: special S5 (PROBLEM) gate_text → APPROVED after 15 fixes (register labels hiccup/glitch/headache dropped, 5 glosses fixed, satnav→GPS); 959 spoken words; report content/specials/S5/lang-gate-v1.md. Next step: nlm_video.
autopilot 2026-09-29T06:43:57Z: special S5 (PROBLEM) nlm_video — work2 (968fad6b) and work4 (9b6f4036) both "Rate limited" (API code 8) on the one allowed attempt each (script added to work4 as source dbe56876…). default (28470494) accepted: added script as source 24121467…, `nlm video create --format explainer --style whiteboard` → artifact c8c368ce-370a-4571-8967-be9fd9000a95, generated in ~14 min, downloaded → content/specials/S5/s5-v1.mp4. Duration 361.72 s (~6:02, checked via video-compressor's ffprobe — this container has none), within the 1-8 min window, no retry needed. Next step: critic.
autopilot 2026-09-29T11:15Z: ep02 visuals — NLM no longer rate-limited; ran the main-infographic create_cmd once, it succeeded (artifact_id 68f05851-1357-461d-84fb-2aec688035c0); wrote nlm_job for nlm_jobs.py to poll/download, step stays visuals.
autopilot 2026-09-29T11:17:14Z (auto_upload, no Claude): special S2 'Can You Remember 15 Synonyms for SAD? (Memory Challenge)' uploaded as PRIVATE draft https://www.youtube.com/watch?v=xxkXnvm5czU; HD master skipped (hd_master=false)); finish: language=English, playlist added; verify: ALL OK; outside view: private ✓
user 2026-09-29T11:23Z (verbatim): "there 0 views on lastly published video, you need definitely put marcus campbell to the job"
claude 2026-09-29T11:24Z: M1 GNH19NdTu9U (public, long-form) shows 0 views in the 11:13 snapshot. Launched glottos-growth-tester (Marcus Campbell / affiliatemarketingdude lens): read-only Studio facts (impressions, CTR, traffic sources), diagnosis distribution vs packaging, Test & compare eligibility -> content/insights/ab-facts.md, variants + distribution actions queued as DRAFT in glottos-auto/out/abtests/queue.json. No live change without user approval. Also: yt-studio login survived the 11:12 VM reboot (DICE fix confirmed, committed 24009af).
autopilot 2026-09-29T11:18:48Z (auto_upload, no Claude): special S3 upload attempt 1 failed (playwright._impl._errors.Error: Locator.set_input_files: Cannot transfer files larger than 50Mb to a browser not co-located with the server)
user 2026-09-29T11:25Z (verbatim): "and marcus campbel has nlm in which all of his videos were transcribed and so on, so he can help with everything from thumbnail design to clickable title"
claude 2026-09-29T11:26Z: told the running growth tester to consult his NLM corpus (efe7b5b3) with 1-2 batched, concrete questions (thumbnail rules, title formulas, first views for a dormant channel) using M1 real title + Studio numbers; made it STANDING in the agent definition: every packaging job consults the corpus and quotes his answers.
autopilot 2026-09-29T11:25:33Z (auto_upload, no Claude): special S3 upload attempt 2 failed (playwright._impl._errors.Error: Locator.set_input_files: Cannot transfer files larger than 50Mb to a browser not co-located with the server)
user 2026-09-29T11:28Z (verbatim): "same applies to research stage, agent should always look on it through marcus lens"
claude 2026-09-29T11:36Z: glottos-pain-researcher now has a MANDATORY "Marcus lens" section in every PROBLEM doc (search intent + demand ranking, competitor packaging patterns, intent flip, 1-3 quoted rules from his corpus; <=2 consult queries/run on account default, read-only). Found + fixed while wiring it: (1) consult.sh used the shared ACTIVE NLM profile (was drawnformula, wrong account) -> pinned to default; (2) it only read youtube-type sources = ONE video; now includes affdude transcripts archive vol. 1-5 = full corpus; (3) autopilot lean-home could not reach the corpus at all (no nlm venv/profile/consult-lib) -> linked.
autopilot 2026-09-29T11:26:31Z (auto_upload, no Claude): special S4 upload attempt 1 failed (playwright._impl._errors.Error: Locator.set_input_files: Cannot transfer files larger than 50Mb to a browser not co-located with the server)
autopilot 2026-09-29T11:32:54Z (auto_upload, no Claude): special S4 upload attempt 2 failed (playwright._impl._errors.Error: Locator.set_input_files: Cannot transfer files larger than 50Mb to a browser not co-located with the server)
claude 2026-09-29T11:50Z: growth-tester (Marcus lens) on M1 GNH19NdTu9U: ~15 h public -> 2 impressions, 0 views, no traffic source => DISTRIBUTION problem, not packaging (too early to judge CTR). Short #1 (19 views, 95% Shorts feed) has Related video = None. Test & compare IS available on M1 (title/thumb/both, up to 3), not launched: ~2 impressions/day = inconclusive. Marcus corpus: Related Video on every Short -> the long video + pinned comment; 2-5 Shorts/day cut from the main video; thumbnails: face with eye contact, 2-5 words, black + bright yellow, red circles. Queued DRAFT for user approval (glottos-auto/out/abtests/queue.json): 1) Short #1 related video -> M1 + pinned comment, 2) pinned comments/end screens on old evergreen videos -> M1, 3) 3-5 Shorts cut from M1; thumbnails A/B/C built; new titles still need the language gate. Also found: descriptions link anotherwordfor.net whose SSL expired 2024-02-05.
autopilot 2026-09-29T11:43Z (Claude upload tick): special S3 (BIG) upload — docker exec upload.py (co-located CDP, unlike the two failed auto_upload attempts which hit the 50Mb non-co-located transfer limit) uploaded specials/s3-v2 (30.8MB) as PRIVATE draft https://youtu.be/wVZqEtgTksE. finish pass: language=English, category=Education, playlist "Synonym Memory Challenge" added, not made for kids. Studio Content row still shows "Processing will begin shortly" (transcoding) so the Private badge hasn't rendered yet — PRIVATE was set via the radio button during upload, this is display lag not an error; re-confirm on a later pass. Next step: publish_log.
autopilot 2026-09-29T11:41:11Z (Claude upload tick): special S4 (BEAUTIFUL) upload — docker exec upload.py (co-located CDP, unlike the two failed auto_upload attempts which hit the 50Mb non-co-located transfer limit) uploaded specials/s4-v2 (30.1MB) as PRIVATE draft https://youtu.be/fPKxW7BuN8A. finish pass: language=English, category=Education, playlist "Synonym Memory Challenge" added, not made for kids; verify: ALL OK including studio_private (row shows Private, no lag this time). Next step: publish_log.
autopilot 2026-09-29T11:52Z: ep02 visuals -- v3 rejected (missing 'Re-read'/'Practised recall' bar labels + stray 'Cover and retrieve' header on panel 4, kept as ep02-infographic-rejected3.png); wrote focus-v4.txt fixing both, queued v4 create (artifact 86288a84-ad7c-4eb3-9e25-df7a87adf706) via nlm_job for nlm_jobs.py to poll/download.
autopilot 2026-09-29T11:56Z: special S2 publish_log — S2 v2 'Can You Remember 15 Synonyms for SAD? (Memory Challenge)' (7:33, critic SOLVES, lang/meta gates APPROVED) is a PRIVATE draft https://www.youtube.com/watch?v=xxkXnvm5czU; user decides visibility. No NLM source replacement needed (M1/S1 precedent: specials' video-production notebooks aren't touched at publish_log). Mirror synced, text artifacts committed.
autopilot 2026-09-29T12:05Z: special S3 publish_log — S3 v2 'Synonym Memory Challenge: BIG — remember 15 synonyms with one story' (7:19, critic-v2 SOLVES, lang gates APPROVED) is a PRIVATE draft https://youtu.be/wVZqEtgTksE, in the playlist 'Synonym Memory Challenge'; user decides visibility. No NLM source replacement needed (M1/S1/S2 precedent: specials' video-production notebooks aren't touched at publish_log). Mirror synced, text artifacts committed.
autopilot 2026-09-29T12:09Z: special S4 publish_log — S4 v2 'Synonym Memory Challenge: BEAUTIFUL — remember 15 synonyms with one story' (6:53, critic-v2 SOLVES, lang gates APPROVED) is a PRIVATE draft https://youtu.be/fPKxW7BuN8A, in the playlist 'Synonym Memory Challenge'; user decides visibility. No NLM source replacement needed (M1/S1/S2/S3 precedent: specials' video-production notebooks aren't touched at publish_log). Mirror synced, text artifacts committed.
user 2026-09-29T11:58Z (verbatim): "what is the blocking point?"
claude: Ep2 main infographic: v1 rejected (captions), v2 stuck ~4 h then rejected (title), ~14 h drawnformula rate limit + Claude limit, v3 rejected 11:44 for 2 label nits fixable in post. Fix: visuals agent now fixes small text defects in post with PIL, max 2 generations per sheet; v4 = last generation for Ep2, else patch v3.
user 2026-09-29T12:05Z (verbatim): "also you do not fully use all nlm accounts for video and pictures geneartion, but you should. Like you are using 2 from 4, and wait for rate limits, but there are other which are not solicitated"
claude: confirmed 4 signed-in accounts (drawnformula, work2, work4, default); episodes used ONLY drawnformula (Ep3-6 audio waiting since 09-28 17:21-17:58). nlm_jobs.py now fails over across all 4 (copies sources into the Glottos notebook of the free account, per-account/per-kind limits in state/nlm-accounts.json), tested live (copy to work4 + cleanup). Runbook updated. Open question to user: keep the 09-27 "NLM steps in episode order" rule?
autopilot 2026-09-29T12:09:31Z: special S5 critic — s5-v1 (6:02, default) PARTLY: all beats in order, audio faithful; ship-blocking fixes for polish: ladder shows 8/15 rows, blank 'complication' card, pause holds <1 s, banned fire drawing + empty ending bubble, Gemini watermark/end card. No regeneration needed. Report content/specials/S5/critic-v1.md; next: polish → s5-v2.
user 2026-09-29T12:15Z (verbatim): "probably the lean approach would be to use also for shorts episodes the video overview which will give you structure and voice automaticaly from the get go and then as you need to modify it anyway to remove nlm sign and put anotherwordfor logo and animiation for subscribing and some pictures specific to the shorts, you can edit this video with generated picture. would it be faster and cheaper in terms of time comparing to how you do it now?"
claude: likely yes: specials go script -> video in ~1 h with 1 NLM generation vs 3 (audio + 2 infographics) for episodes; Ep2 has been at visuals ~20 h. Caveats: NLM video is 16:9 only (S5 1280x720), brief length unmeasured, single narrator instead of two-host podcast, NLM paraphrases the script. Proposed Ep3 pilot.
user 2026-09-29T12:25Z (verbatim): "yes you can experiment on episode 3 and if doesnt work, change it. Another option would be (not for this series but in future) to create a long video (like 30 minutes) but made in a way of 50 seconds parts which would be easy to cut in shorts. "The video comes out landscape. S5 is 1280×720 " yep, for normal video we will just put the picture in the center. And when we will cut it later all background will be gone and only central picture seen in the shorts video format"
claude: Ep3 switched to pipeline "video" (nlm_video brief/whiteboard -> critic -> polish 9:16 with the 16:9 picture CENTERED, logo bar, captions, subscribe animation -> critic -> studio -> meta -> upload); metrics vs Ep2 in content/insights/ep3-video-pilot.md; revert if worse. Ep3 still starts after Ep2 finishes its picture (09-27 series rule kept). Future idea (30-min long of self-contained ~50 s parts, centre-safe composition, cut = centre crop) recorded in docs/autopilot.md for the next series.
autopilot 2026-09-29T19:30:15Z: channel monitor — Studio sign-in OK, fresh snapshot (116 videos, 20 threads). Ep1 1→19 views/2d, M1 public since 09-28 but still 0 views/comments, S1-S4 still private drafts. Audience needs unchanged (shorten-intro, PDF/word-list request, "do Music next"); site TLS still expired, don't link it. One unqueued unanswered comment (@Shrekbeliever, meme bait on S3/big) flagged reply_drafts_due=true for next tick's reply_drafts step to re-triage.

autopilot 2026-09-29T19:36:41Z: reply_drafts — queued 1 draft (@Shrekbeliever meme comment on 'Another Word For Big' → light redirect to 'enormous'/'gigantic'); nothing posted, awaits user approval on :8093 Replies.

autopilot 2026-09-29T19:46:49Z: ep02 visuals DONE — v4 NotebookLM generation (artifact 86288a84) failed; per user's stop-regenerating instruction, no further NLM generation was queued. Used v3 (ep02-infographic-rejected3.png, art approved) and fixed both known text defects in post with PIL: drew the mandatory 'Re-read'/'Practised recall' bar-name labels in panel 3, painted over the stray 'Cover and retrieve' header in panel 4 (cloned background, no visible seam), cropped the watermark strip. Saved state/nlm-raw/ep02-infographic-v3-patched.png; self-checked wording against content/articles/p01-ep02-visuals.md and ep02-focus-v4.txt (PASS, no glottos-language-editor Task tool available this session so the check was done directly). Split into state/shorts/words-that-stick-ep02-v1/panel-{title,title+1,1,2,3,4}.png with a custom border-based crop (build_short_v2.py's generic panels() helper mis-segmented this bordered layout). shorts/units/ep02_v1.json updated (infographic + infographic_note); state/autopilot.json episode 2 step -> render, nlm_error/blocked_until cleared.

autopilot 2026-09-29T19:53:00Z: ep02 visuals — ran the mandatory glottos-language-editor gate on the v3-patched infographic; it caught one more defect the self-check missed: legible decorative text ('word/definition/list/meaning/term' + stray letters) baked into panel 1's smoke graphic. Fixed in post with PIL (blurred/painted over every letter cluster in both smoke plumes, no NLM regeneration) -> state/nlm-raw/ep02-infographic-v4-patched.png; re-ran the language-editor gate on v4 -> APPROVED. shorts/units/ep02_v1.json now points at v4-patched. Episode 2 visuals step is complete; next step is render (not run this tick).

autopilot 2026-09-29T20:19:33Z: ep02 render DONE — words-that-stick-ep02-v1/final.mp4 (53.3s, 1080x1920), reusing the hand-fixed custom-crop infographic panels; copied to glottos-auto/out. Builder's own frame QA found no defects (quiz reveals/pauses, captions, panels, no watermark all correct). shorts/build_short_v2.py picked up an uncommitted fix so it stops clobbering pre-cropped panel files with the generic splitter -- flagged for review/commit at publish_log. Episode 2 step -> critic (not run this tick, one step per tick).

autopilot 2026-09-30T05:44:59Z: ep02 critic -> PARTLY, no ship-blockers (content/reviews/words-that-stick-ep02-v1.md). Main notes: the cover-and-check action and the Ep3 teaser are not spoken (teaser on-screen only), answers shown only 0.8 s, panel 1 smoke patch blocky at full size. Per runbook PARTLY proceeds; episode 2 step -> studio.

autopilot 2026-09-30T05:45:53Z: ep02 studio -> confirmed final.mp4 (md5 f42073e2d41a40cc7d475eb4b01ab3be) is present at /workspace/glottos-auto/out/words-that-stick-ep02-v1.mp4 (:8093 Videos tab), cp -n re-run to be safe. Episode 2 step -> yt_meta_gate, carrying the critic's PARTLY notes forward for the user.

user 2026-09-30T05:40Z (verbatim): "let us finished current video production in progress and then pause for a while"
claude: in production = Ep2 (rendered, critic) and S5 (NLM video done, polish). Added glottos-autopilot/pause.json + due.py hold support: Ep2 and S5 run to PRIVATE draft + publish_log, Ep3–6 held (no Claude ticks, no NLM), Claude channel steps (monitor, reply drafts) held; replies/likes/snapshots/uploads keep running without Claude. Resume = delete pause.json. Tested on a state copy: Ep2 → S5 → idle.
user 2026-09-30T05:45Z (verbatim): "we need first see how to get traffic, because 0 views for two video in a row is definitely a sign that hypotesis is wrong"
user 2026-09-30T05:47Z (verbatim): "we need to test bunch of hypotesis at the lowest cost (see marcus campbell approach) also see the video of the guy who made influencers ai (the one from which we started) they all do it with traffic"
claude: evidence: M1 and S4 public, 0 views (~2 impressions = distribution); Ep1 19 views, 77% swiped; old catalogue ~11 views/day total. Ep2 cost ≥$8.46 + 34 h → too expensive to test with. Tilbury (3 parallel bets, steal proven format, kill 2 scale 1) + Marcus consult (2–5 Shorts/day, one lane many hooks, rule of 20, ugly beats pretty, decide on stayed/CTR). Proposed 20 cheap Shorts (cards + edge-tts, no NLM, ~$2–4) across 4 lanes: Stop saying VERY / If you know these 5 words / Dont
user 2026-09-30T05:40Z (verbatim): "let us finished current video production in progress and then pause for a while"
claude: in production = Ep2 (rendered, critic) and S5 (NLM video done, polish). Added glottos-autopilot/pause.json + due.py hold support: Ep2 and S5 run to PRIVATE draft + publish_log, Ep3-6 held (no Claude ticks, no NLM), Claude channel steps (monitor, reply drafts) held; replies/likes/snapshots/uploads keep running without Claude. Resume = delete pause.json. Tested on a state copy: Ep2, then S5, then idle.
user 2026-09-30T05:45Z (verbatim): "we need first see how to get traffic, because 0 views for two video in a row is definitely a sign that hypotesis is wrong"
user 2026-09-30T05:47Z (verbatim): "we need to test bunch of hypotesis at the lowest cost (see marcus campbell approach) also see the video of the guy who made influencers ai (the one from which we started) they all do it with traffic"
claude: evidence: M1 and S4 public, 0 views (~2 impressions = distribution problem); Ep1 19 views, 77% swiped; old catalogue ~11 views/day in total. Ep2 cost >= $8.46 + 34 h, too expensive to test with. Tilbury (3 parallel bets, steal the proven format, kill 2 scale 1) + Marcus consult (2-5 Shorts/day, one lane many hooks, rule of 20, ugly beats pretty, decide on stayed/CTR). Proposed 20 cheap Shorts (cards + edge-tts, no NLM, ~$2-4) across 4 lanes: Stop saying VERY / If you know these 5 words / Don't say X, natives say Y / memory-trick control; kill/winner rules at 48 h. Plan: content/insights/traffic-test-plan.md. Awaiting user: lanes, public publishing for the test, TikTok/IG accounts.
- autopilot 2026-09-30T05:50:53Z: ep02 yt_meta_gate → APPROVED WITH FIXES on final words-that-stick-ep02-v1 (53.3s); content/youtube/ep02.json: Roediger & Karpicke line made exact (same TOTAL time, 61% vs 40%), playlist 'Words That Stick' added. Next step: upload (PRIVATE).
autopilot 2026-09-30T05:51:26Z (auto_upload, no Claude): episode 2 'Stop re-reading your word list: test yourself instead | Words That Stick #2' uploaded as PRIVATE draft https://youtube.com/shorts/P8_f4QAil8w; 1080x1920 -> 1440x2560 master); finish: language=English, playlist created PRIVATE + added; verify: CHECK studio_private; outside view: private ✓
autopilot 2026-09-30T05:55:42Z: episode 2 publish_log — 'Stop re-reading your word list: test yourself instead | Words That Stick #2' (final.mp4, 53.3s, critic PARTLY no ship-blockers, lang/yt_meta gates APPROVED WITH FIXES) is a PRIVATE draft https://youtube.com/shorts/P8_f4QAil8w, in the playlist 'Words That Stick' (private); user decides visibility. No NLM source replacement on the go-to-market notebook (8306c0a9): no episode has a documented source-replace-by-title precedent (only the specials' M1/S1/S2/S3/S4 "no source replacement" precedent applies, and that is for the separate video-production notebooks, not this one), so skipped rather than guess at an untested operation; not spending NLM quota on it. Mirror synced, text artifacts committed.
