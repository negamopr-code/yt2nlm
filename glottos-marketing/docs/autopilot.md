# Words That Stick autopilot (user 2026-09-27)

User, verbatim: "you will upload all episodes to youtube channel automatically, you will wait each time for
different pieces to be produced, then render it and automatically upload. You will do this automatically
without me babysitting the process, meaning that you will automatically asking if limits on nlm side are over
and so one. Also episodes will be logically followed one by another as you mention that user will learn in
the next one this and that."
Also standing: "you do not publish, you prepare everything and I decide". Upload = PRIVATE only, never public or unlisted.

State: state/autopilot.json (one entry per episode, `step` = next step to do, `running` = step in flight).
Driver: an hourly session cron ("advance the Words That Stick autopilot"). If no session is running it, the
next Claude session re-arms it (memory: glottos_content_pipeline_agents.md).

## One tick
1. If `running` is set and that step is still in progress → do nothing (strictly serial: ONE step, agent,
   render or NLM generation at a time, machine-wide for this pipeline).
2. Otherwise take the lowest episode whose next step isn't blocked, and run exactly that one step. Blocked =
   `blocked_until` in the future, or an NLM step while an earlier episode still owes NLM work (see below).
3. Record the result in state/autopilot.json, then append one line to the NLM mirror journal.

## Steps per episode (in order)
scenario → gate_text → audio → gate_recording (stamps lang_gate) → visuals → render → critic → studio (cp -n to
glottos-auto/out, :8093) → yt_meta_gate → upload (private) → publish_log (journal + NLM sync + commit)

- NotebookLM rate-limit on audio/infographic → set `blocked_until` = now + 2 h and retry ONE attempt then.
  Never loop retries, never switch accounts (drawnformula only).
- **NotebookLM steps (audio, visuals) run in EPISODE ORDER** (user 2026-09-27: "everything which rate limited by
  nlm goes in series, not in parallel ... first complete episode 2 instead of trying to generate pictures or audio
  for episode 4"). Episode N may start an NLM step only after every earlier episode is past `visuals`. A
  rate-limited episode makes the later ones WAIT (due.py marks them `nlm_wait`); it never hands the quota on.
  Later episodes' NON-NLM steps (scenario, gate_text, ...) may proceed meanwhile, still one at a time.
- Render: only when `free -m` available ≥ 3000 MB (VM has no swap). New unit id per version; never overwrite.
- Critic DOESN'T → one revision (new version id) → critic again. A second DOESN'T → stop that episode and
  ask the user. PARTLY → upload anyway and list the critic's notes in the report.
- Teaser chain (the last line of each episode must name the next one's topic):
  1→2 "why re-reading your word list isn't enough" · 2→3 "the best days to review" · 3→4 "why you freeze
  mid-sentence" · 4→5 "the 15-minute routine" · 5→6 "why your mind goes blank" · 6 → series close
  ("that's the whole system" + pointer to the playlist/first episode).
- Upload: `docker exec yt-studio /home/app/yt-profile/.venv/bin/python /opt/yt/upload.py <video-id> epNN.json`,
  ONLY the final approved file for that episode, never other versions. No dry runs (attaching a file already
  creates a draft). Afterwards verify in Studio: Private, tags, not for kids, Education, English; fix in Edit draft.
- Stop and ask the user when: NLM account signed out, YouTube signed out, a false claim can't be cut cleanly,
  second DOESN'T.

## Channel care (user 2026-09-27: "an agent which is monitoring how video is doing … and an agent which is answering the comments of users (you prepare them and I decide if they go live)")
Interleaved with the episode steps, still ONE step at a time:
- **post_replies** (EVERY tick, mechanical, no Claude): `sh /workspace/yt-studio/post_approved.sh`. It posts only
  replies the user APPROVED on http://localhost:8093/ → Replies, then marks them posted. Drafts and rejected items
  are never posted.
- **monitor** (daily: first tick after 07:00 UTC; every 6 h while an episode is <72 h public): agent
  `glottos-performance-monitor` → read-only snapshot (`yt-studio/snapshot.sh`) + `out/analytics/report.md`
  (:8093 → Performance) + `content/insights/audience-needs.md`.
- **reply_drafts** (after a monitor run that found unanswered comments not yet queued): agent
  `glottos-comment-responder` → drafts (self language-gated) added to the queue through the :8093 API. It never posts.
- State lives in `state/autopilot.json` → `"channel": {"last_monitor", "last_reply_drafts"}`.
- The user publishes videos. Autopilot never changes a video's visibility.

## Playlist and order (user 2026-09-27: "it should be logical with episodes you are posting in the play list")
- **Upload in episode order only:** episode N's `upload` step waits (does nothing) until episode N-1 is uploaded.
  Production of later episodes may run ahead; uploads may not. The teasers ("Next: …") then always point to an
  episode that already exists in the channel.
- Every uploaded episode goes into the playlist **"Words That Stick"** (create it once if missing, public, with a
  description of the series), at the end, so the playlist order = episode order. Ep1 (already public) is added first.
- Ep6's closing line points to the playlist ("watch the whole series from Episode 1").

## Method research (user 2026-09-27) — feeds every NEW series/episode plan
A separate always-on daemon (awf-monitor-runner: state/glottos-methods/, NotebookLM work2, notebook 35d9f7ee
"Glottos — Methods that work") researches each learner pain in series: expert YouTube videos -> transcripts (video
sources deleted) -> comments -> which methods learners CONFIRM worked + what gets watched with engagement ->
`Strategy — P0x` (state/glottos-methods/P0x/strategy.md, also on the :8093 Research tab).
- Before writing a new article/scenario, read that pain's strategy + the Research tab data (confirmed methods,
  proof quotes, format/title engagement, our own numbers vs theirs) and adapt: lead with the best-confirmed method,
  feature a real proof quote, copy the format/title patterns that carry engagement.
- The autopilot never touches work2 or that notebook; the daemon never touches drawnformula.
- New pain -> append it to state/glottos-methods/pains.json (status "queued"); it starts after the current one.

## Specials — one-off pieces outside the episode chain (state: `specials` in state/autopilot.json)
Same tick rules (one step per tick, foreground agents, blocked_until on NLM limits, ask_user when stuck).
### M1 — P01 mid-length video (user 2026-09-27: "you can generate video exactly in the sweet spot ... which will
adress our particular problem/pain and having format needed for views and engagement" → "yes, do that")
Account (user 2026-09-27: "on a account which is free on nlm quote"): the FIRST of specials.M1.accounts
(work2 → work4 → default) whose video generation isn't limited — `/workspace/glottos-marketing/.nlmvenv/bin/nlm ...
--profile <acct>`; NEVER drawnformula (episodes, already at its audio/infographic limits). The episode NLM series rule
doesn't apply (different accounts). Record the account that made the video in specials.M1.video_account. Format is
already decided by the user (specials.M1.format_decision, content/specials/M1/decision.md): mid-length 5–8 min.
Files: content/specials/M1/.
Steps: wait_strategy (due.py, no Claude) → decide → script → gate_text → nlm_video → critic → polish → critic (on
the polished file) → studio → yt_meta_gate → upload (PRIVATE) → publish_log.
- **decide** (skipped when specials.M1.format_decision is set — the user decided): read /workspace/state/glottos-methods/P01/strategy.md and /workspace/glottos-marketing/state/methods/
  research.json (P01: methods, formats, title_patterns, videos). The earlier "Mid (1-8 min)" sweet spot was ONE video
  (MEMORIZE Academy, 17.2M views, 36x views/sub), so re-check it on the full data: Mid needs >= 5 videos AND a higher
  median views/sub AND median engagement % than Shorts and Long. Write content/specials/M1/decision.md with the
  numbers. If Mid does NOT hold → step ask_user: "the full data says <format> performs best (<numbers>); make M1 as
  <format> instead, or mid-length anyway?" (also to ask-user.md). If it holds → step script.
- **script**: glottos-scenario-writer (+ article-writer's fact rules): a 5–7 min explainer (~800–1000 spoken words)
  on P01 that LEADS with the best-confirmed method from the strategy, features 2–3 real learner proof quotes verbatim
  (no names, attributed as "a learner wrote"), uses the title/hook patterns that carry views/sub in title_patterns, and
  the "what NOT to claim" list (plus the known bad figures: no "4x stronger connections", no "70% gone by day 3";
  Ebbinghaus/Roediger&Karpicke figures only as in the P01 editor's note). Save script.md + focus.txt (the exact
  steering text for NotebookLM) + meta.json (title, description, tags).
- **gate_text**: glottos-language-editor on script.md, focus.txt, meta.json (mandatory; approval stamped).
- **nlm_video**: try the accounts in order. On an account: production notebook "Glottos — Production (<acct>)"
  (create once per account, store ids in specials.M1.prod_notebooks{acct: id}). If `nlm video create` reports a
  limit/quota/"try again later" → note it (specials.M1.limited[acct] = now) and try the NEXT account in the same tick;
  only when all three are limited → blocked_until = now + 2 h. The account ALSO running a glottos-methods research
  worker is fine (research uses sources/queries, not video generation). It must contain ONLY our approved script.md as a source (never the expert transcripts — NotebookLM
  would retell competitors' videos and their unsourced claims). `nlm video create <prod_nb> --format explainer
  --style whiteboard --language en --source-ids <script source> --focus "$(cat focus.txt)" -y --profile <acct>`, poll
  until ready, `NLM_PROFILE=<acct> nlm download video <nb> --id <artifact> -o ...` (download has no --profile flag) → content/specials/M1/m1-v1.mp4. Record duration (ffprobe): must land 1–8 min; outside → one retry
  with a tighter/longer focus, else ask_user.
- **critic**: glottos-viewer-critic on the mp4 vs P01 learner pain (SOLVES / PARTLY / DOESN'T). DOESN'T → one
  revision (new version id, re-run nlm_video) → critic again; a second DOESN'T → ask_user. PARTLY with fixable
  defects (or any watermark / end card) → **polish**.
- **polish** (added 2026-09-27 after M1 v1: the critic said PARTLY "cannot ship as it is" and the old flow went
  straight on to upload): glottos-shorts-builder (16:9 mode) + visuals apply the critic's in-post fixes to make vN+1
  (new file, never overwrite). ALWAYS on every NotebookLM video, even when the critic doesn't mention it: trim the
  Gemini/NotebookLM end card, cover the "Gemini Notebook"/NotebookLM watermark on every frame with the channel logo
  (state/brand/awf-logo-channel.jpg) or a background-matched patch, and check that on-screen step numbers match the
  voice. Then the language editor re-gates any changed on-screen text, and the step goes back to **critic** on the new
  file. Only SOLVES, or PARTLY where the critic lists no ship-blocking defect, may go on to studio / upload. Two
  polish rounds without that → ask_user.
- **studio**: cp -n to /workspace/glottos-auto/out/specials/ (shows on :8093 Videos tab); note in ask-user.md that
  M1 is ready for review.
- **yt_meta_gate / upload / publish_log**: as for episodes, but it is a normal 16:9 video (not a Short), PRIVATE
  only; the user decides visibility. Not part of the Words That Stick playlist order unless the user says so.

### S1–S5 — "Synonym Memory Challenge" (user 2026-09-27: "take the method from this super popular video on memorizing and make several videos with this method but applying it to synonyms")
Source method: MEMORIZE Academy "How to Memorize Fast and Easily" (0nFkQ4cQhME, 17.2M views, 36x views/sub, 7 min;
transcript in state/glottos-methods/P01/transcripts/). We take the METHOD (the centuries-old story/link method + its
self-test challenge), never its text, story, drawings or name. Words: S1 happy · S2 sad · S3 big · S4 beautiful ·
S5 problem (our channel's best-performing synonym videos). Same steps/accounts/rules as M1 (format already decided:
mid-length 5–7 min), NotebookLM video generation strictly in series M1 → S1 → S2 … (due.py `nlm_wait`).
- **script** (content/specials/Sn/script.md + focus.txt + meta.json), beats in this order:
  1. Hook (≤15 s): "Most people remember 5 of these 10 words. With one trick you'll remember 15 — and know exactly
     when to use each." Promise the score challenge.
  2. VERBAL TEST: the 10 synonyms shown as a plain list, ~2 s each, then "Pause the video. Write down every word you
     remember." (a clear pause beat).
  3. VISUAL STORY: ONE continuous, vivid, slightly absurd scene with 15 synonyms (the 10 + 5 "sneaky" extras), each
     synonym ACTED OUT so its nuance is visible and correct (e.g. happy: *content* = relaxed in a hammock, *cheerful* =
     whistling to strangers, *delighted* = receiving a gift, *thrilled* = jumping, *elated* = floating up, *ecstatic* =
     out-of-control dancing, *overjoyed* = crying with joy, *glad* = relief, *jubilant* = crowd celebrating a win …).
     Order the story from mildest to strongest where the word family allows (intensity ladder = the lesson).
  4. Second pause: "write down every word you can recall — in order."
  5. Reveal: "I gave you 15, not 10." + the ladder recap on one screen (word → one-line meaning → when to use it).
  6. Challenge: "Comment your two scores: list vs story." + "For more words, look up "another word for <word>" on anotherwordfor.net" (the site has no example sentences or search box — language editor 2026-09-27; never promise "examples").
  Accuracy rules: every meaning/usage must be right for B1 learners (register: *jubilant* is formal/written,
  *over the moon* is informal …); no invented memory statistics — say "most people" only for what the video itself
  demonstrates; no claims about "10x faster" etc.
- **gate_text**: glottos-language-editor must check EACH synonym's acted-out meaning and register, not just grammar.
- **nlm_video**: whiteboard style suits the "draw the story" method. The focus text must list the beats and demand:
  the plain list first, the pause cues spoken, the story in the given order, the 15-not-10 reveal, the score challenge.
- **critic**: also verifies the challenge beats survived NotebookLM's retelling (list → pause → story → pause →
  reveal → comment prompt). If NotebookLM drops or scrambles them twice, ask_user proposing our own renderer
  (build_short_v2 in 16:9 + edge-tts voice + NotebookLM infographic panels for the story frames) for the series.
- **meta**: title from the research title patterns (number + "you" + synonym word), e.g. "Remember 15 Synonyms for
  HAPPY With One Story (Memory Challenge)"; a "Synonym Memory Challenge" playlist, private uploads only.
