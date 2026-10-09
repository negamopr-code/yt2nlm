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

- NotebookLM rate-limit on audio/infographic/video → do NOT set blocked_until and do NOT retry yourself: write the
  `nlm_job` (see "NotebookLM jobs") and end the tick. nlm_jobs.py (no Claude) FAILS OVER across ALL 4 signed-in
  accounts (user 2026-09-29: "you do not fully use all nlm accounts ... there are other which are not solicitated"):
  pool drawnformula → work2 → work4 → default, per-account per-kind limits in state/nlm-accounts.json; it copies the
  job's --source-ids to that account's Glottos notebook and rewrites the command. So create_cmd MUST name its sources
  with --source-ids. Only when every account is limited does the item wait (blocked_until = earliest reset).
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
--profile <acct>`; drawnformula is ALSO in the pool now (2026-09-29): nlm_jobs.py fails over across all 4 accounts. The episode NLM series rule
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

## NotebookLM jobs: NEVER poll or wait in a tick (user 2026-09-29: "do them as cheap as possible from token perspective")
Overrides every "poll until ready" / "retry ONE attempt" above. A headless tick that waits for NotebookLM gets killed
when it exits, and the next tick starts over (S5 nlm_video burned 4+ ticks that way). Instead:
1. Prepare everything (notebook, source ids, focus file), then write into the item (episode or special) in
   state/autopilot.json:
   `"nlm_job": {"profile": "<acct>", "notebook": "<nb id>", "kind": "video|audio|infographic",
     "create_cmd": "<the exact full nlm ... create command, runnable from /workspace/glottos-marketing>",
     "out": "<path relative to glottos-marketing for the download>", "artifact_id": null}`
   You MAY run create_cmd once yourself and put the artifact id in `artifact_id`, or leave it null and let the script
   start it. Then END THE TICK (one line). Do not poll, sleep or start a background waiter.
2. `glottos-autopilot/nlm_jobs.py` (no Claude, every loop pass) starts/retries it (rate limit → blocked_until +2 h,
   retried by the script, not by a tick), polls `nlm studio status`, downloads to `out`, then removes nlm_job and sets
   `nlm_done` {out, artifact_id, profile, at}, or `nlm_error` on failure. due.py skips an item while nlm_job exists.
3. The next tick for that step sees `nlm_done` → CONTINUE from the downloaded file (duration/QA/split etc.), then clear
   `nlm_done` and advance. Sees `nlm_error` → decide (other account per the specials order, new focus, ask_user), clear it.
Multi-account specials: on a rate limit, you may point nlm_job at the next account in the order before ending the tick.

## Episode 3 VIDEO PILOT (user 2026-09-29: "yes you can experiment on episode 3 and if doesnt work, change it")
Episode 3 has `pipeline: "video"`. ONE NotebookLM video overview replaces audio → gate_recording → visuals → render.
Steps: nlm_video → critic → polish → critic → studio → yt_meta_gate → upload → publish_log (same as the specials).
Single NotebookLM narrator instead of the two-host podcast: accepted by the user for this pilot.
- **nlm_video:** source = the approved Ep3 text (`content/articles/p01-ep03-audio-script.md`, already gated; add it as
  ONE source if it isn't in the notebook). Write an `nlm_job` (kind video) with
  `nlm video create <nb> --format brief --style whiteboard --language en --source-ids <id> --focus "<beats in order,
  the exact example words, no intro/outro chatter, aim 60–150 s>" -y --profile <acct>`. nlm_jobs.py picks a free
  account (pool of 4). Output `content/episodes/E3/e3-v1.mp4`. Measure the duration. Over 3:00 → cut at beat
  boundaries in polish, or ONE regeneration with a tighter focus.
- **critic** (glottos-viewer-critic) + language check on what is HEARD (transcript), since NotebookLM paraphrases the script.
- **polish → 9:16 1080×1920, "put the picture in the center" (user):** branded top bar with the OFFICIAL channel logo
  (`state/brand/awf-logo-channel.jpg`); the 16:9 video scaled to 1080 px wide and CENTERED vertically; background
  above/below = the blurred enlarged frame or the brand colour; big word-synced captions under the picture; NotebookLM
  watermark + end card removed; subscribe animation at the end; replace weak slides with Short-specific pictures where
  it helps. Reuse the S3/S4 polish-build pattern and shorts/build_short_v2.py pieces. Small text defects → fix in post.
- **Measure + decide:** write `content/insights/ep3-video-pilot.md`: wall time script→studio, ticks, cost
  (glottos-autopilot/costs.jsonl rows for "episode 3"), NotebookLM generations, critic verdict; compare with Ep2
  (classic route). If the pilot is worse, set Ep3 back to `pipeline` absent + `step: audio` and say why. If better,
  propose switching Ep4–6 (ask_user; don't switch them yourself).

## Future format idea (user 2026-09-29, NOT for this series)
A long video (~30 min) built from self-contained ~50 s parts, each a clean cut into a Short. Long-form = 16:9 with the
picture in the CENTER; cutting the Short = crop the centre, so the background disappears and only the central picture
remains in 9:16. Plan it when the next series is designed (format-strategist).

## Lab — permanent hypothesis testing (user 2026-10-03)

User, verbatim: "research of new testing hypotesis should be permanent … You should ask Markus how to find viral content ideas
and you should produce them in "non sent" tab. My job is to approve them or to give you hints. By test of hypotesis should be
permanent, non stop process" and "we have in essence only two videos which got some views it stop saying big and stop saying I do
not know. Other did not do well at all and all this should be analysed by marcus, proposed something else, repeat, produce, adjust".

The loop never waits for the user: analyse → propose → produce into "Not sent yet" → the user sends (or not) → read the result →
adjust → again. State = `/workspace/glottos-auto/out/lab/lab.json` (shown on the :8093 **Lab** tab). The user's hints arrive in
`/workspace/glottos-auto/out/lab/hints.jsonl` (typed on the Lab tab) — read ALL unread hints first in every lab step, quote them
verbatim in the hypothesis they change, and record `hints_read` (count) in lab.json. A hint always beats your own ranking.

`lab.json`: `{"cycle": n, "last_analyze", "last_produce", "max_unsent": 8, "paused": false, "hints_read": n, "lessons": [dated one-liners
with numbers], "hypotheses": [{"id": "H07", "statement", "why" (evidence: our numbers + Marcus, source named), "test" (what exactly is
produced and what result = win / lose, decided BEFORE the test), "format", "videos": [{"vid" (local file id on :8093), "youtube" (id once
sent), "views", "engaged_pct"}], "status": "proposed" | "producing" | "waiting_send" | "live" | "verdict", "verdict": "win" | "lose" |
"mixed", "result" (numbers), "next" (what it changes)}]}`. Never delete a hypothesis; a lost one stays with its numbers.

### Lab — the scoreboard the user reads, and the numbers every verdict must use (user 2026-10-05)
User, verbatim: "you have tab 'research' and 'lab' tabs, but they do not give an idea of what you tested, what worked, what not, how you
changed/adapted it, what marcus said, what is the next step. I do see that some videos having 3-5% CTR which is a success, meaning we
need to see how we implement this success elswhere. We have a lot of videos, we have statistics, we need to use it!!!!"
- `glottos-autopilot/lab_board.py` (every loop pass, no Claude) writes `glottos-auto/out/lab/board.json`: `lanes` (every public video
  grouped by title pattern, the 2019-21 library included: videos, views, middle video, thumbnail impressions, click-through rate,
  stayed %), `top_ctr` (videos with the best thumbnail click-through rate, at least 200 impressions, with their main source and search
  terms), `search` (the search terms that brought viewers), `marcus` (every answered question with his answer). The Lab tab shows it
  first, then one row per test. `yt-studio/deep_long.sh` (weekly) reads the whole long-video catalogue; `deep.sh` (daily) the last 14 days.
- EVERY `lab: analyze` reads `board.json` FIRST and uses it: (1) a verdict names the numbers that decided it - for long videos
  thumbnail impressions + click-through rate + average view, for Shorts stayed % + views; views alone are not a verdict;
  (2) at least ONE hypothesis in every cycle must come from the top of `top_ctr` or the best `lanes` row: say which video or pattern is
  being copied, what exactly is copied (title form, thumbnail, length, topic) and the ONE thing changed; (3) a new word or topic for an
  existing lane is picked from the words whose old video has the best click-through rate or search share, not by guess.
- Every hypothesis carries three short plain-English fields, shown on the scoreboard, kept current in every analyze:
  `"changed"`: what we changed or adapted because of this test (title, look, length, lane dropped ...), with the date; "nothing yet" if so;
  `"marcus"`: what Marcus said that this test rests on - a transcript quote with its video id, or "not in his transcripts";
  `"next"`: the ONE next step and its date. `result` stays numbers only.
- Marcus's answers: `consult.sh` answers at once or queues; `resolve.sh` drains the queue. Until 2026-10-05 a parsing bug threw away
  every answer and reported "still rate-limited" (17 questions, 3 days). If the queue ever again reports a rate limit for more than one
  cycle, run ONE raw `nlm notebook query --json -p default <notebook> "<short question>"` and read the output before believing it.
  Read `~/.claude/skills/affiliatemarketingdude/references/resolved-consults.md` in every analyze and fold his answers into the
  hypotheses' `marcus` fields and into `lab.json.marcus`.

### Step `lab: analyze` (due every 12 h)
1. Data: `glottos-auto/out/analytics/latest.json` (all videos: views, visibility, date), `analytics/deep.json` (per video: engaged views,
   stayed %, average view duration, traffic sources, search terms), `glottos-auto/out/yt/status.json` (which local file is which
   YouTube video; what is still unsent), `content/insights/ab-lessons.md`.
2. For every hypothesis with status `waiting_send` / `live`: fill `youtube`, `views`, `engaged_pct`. A video public for ≥ 48 h is readable:
   compare with the win/lose rule written in `test`, set `verdict` + `result` + `next`, append ONE dated line with numbers to `lessons`
   and to `content/insights/ab-lessons.md`. Unsent after 72 h on "Not sent yet" = the user did not want it: note it, don't count it as a loss.
3. Ask Marcus (skill `affiliatemarketingdude`, `scripts/consult.sh`; at most 3 questions per cycle, each question carries our real
   numbers and asks for a decision, e.g. "which of these three next tests would you run first and why"). NotebookLM sometimes repeats our
   own numbers back as his opinion — mark such lines "unverified" and never cite them as Marcus. Also look outward ONE way per cycle:
   YouTube autocomplete / top results for the winning hooks (`shorts/pain_demand.py`, `state/yt-demand/`), or one competitor video
   the user named.
4. Write 1–3 NEW hypotheses (`proposed`), ranked: a hint from the user first; then "double down on a winner with ONE thing changed";
   then one new direction. Each must be producible with what we have (builders below) and must say what is held constant.
5. Set `last_analyze`, `cycle += 1`. One line in the journal. Do NOT produce in this step.

### Step `lab: produce` (due whenever a hypothesis is `proposed` — NO cap on waiting videos, user 2026-10-03: "there should be no cap! we should test as much as we possibly can till the moment we find the right format for the right audience!")
Produce the test batch of the FIRST `proposed` hypothesis (2–4 videos, never more), then set it `waiting_send` with its `videos`.
- Builders: Shorts `shorts/build_stop_saying.py <unit>` (units like `shorts/units/l1-very-sad-v1.json` / `l3-*.json`), long
  `shorts/build_long.py`, listen-and-repeat `shorts/build_podcast.py`. Pictures: `shorts/pictures_from_nlm.py <unit>` then ALWAYS
  `.ttsvenv/bin/python shorts/frames_by_word.py <unit-id>` (picks the frame by the word written in it); emoji: `shorts/emoji_pics.py`.
  NotebookLM generation inside this step is allowed for pictures (one unit after another; rate limit → leave the hypothesis
  `producing`, set `blocked_until` in lab.json = now + 2 h, stop).
- Gates, all mandatory, in this order: unit text → `glottos-language-editor` (lang_gate.py approve); pictures → look at every
  picture (contact.jpg) and let `glottos-language-editor` read the text INSIDE them (wrong / garbled text → `shorts/detext.py --crop`);
  render; `python3 shorts/gate_av.py <final.mp4>` (audio); `glottos-viewer-critic` on at least one video of the batch; YouTube text
  `content/youtube/<name>.json` with `video_ids_local` → `glottos-language-editor` stamp (`gate: yt_meta_gate`).
- Hand-over: copy `final.mp4` to `/workspace/glottos-auto/out/<vid>.mp4`. With an approved YouTube text it appears on :8093
  "Not sent yet". NEVER upload, schedule, publish or delete: the user presses Send; the schedule keeper spaces the row.
- A video that fails a gate twice: drop it from the batch and say why in the hypothesis; never ship a weaker gate.
- Set `last_produce`. One line in the journal: hypothesis id, the files, what the user should look at.

### Rules
- One lab step per tick. Channel care (replies, monitor) and the user's Send queue always go first.
- Change ONE thing per test and keep the rest equal to the winner it is compared with; write that down in `test`.
- Winners so far (2026-10-03): "Stop Saying "Very Big"" (1.27k views, 34 % engaged) and "Don't Say "I Don't Know"" (985, 53 %).
  Losers: "(Part N)" advanced words, memory-tip hooks, Memory Challenge long videos (0–4 views: no traffic source).
- Stop switch: `"paused": true` in lab.json (or the user's hint "pause the lab").

### Lab — assessment and traffic map (user 2026-10-03: "i do not see closed loop of research, marcus assesement of why videos are not shown by youtube and so on. We need to go where traffic is!")
Every `lab: analyze` REWRITES `lab.json.assessment` — this is what the user reads first on the Lab tab, so write it in plain English, short lines, with numbers:
`{"at", "by": "lab analyze cycle N", "why_not_shown": [3-6 lines: why YouTube stopped showing / never showed our videos — our numbers + Marcus, only transcript-cited quotes], "where_traffic_is": [{"source", "evidence" (search suggestions, views of the top results, our own videos that earn there), "we_have"}], "next_actions": [what the lab produces next, each with its hypothesis id]}`.
Traffic first: each cycle extends the traffic map by ONE new look (YouTube autocomplete for a seed, the top 10-20 results with views and age for a query, the traffic sources and search terms of our own videos in analytics/deep.json, or a competitor video the user named) and keeps the earlier rows. The next hypotheses must come from the TOP of that map: prefer a test that opens a traffic source where demand is proven and we have nothing, over another variation of what the Shorts feed already gave us.

- No cap (user 2026-10-03): never hold production back because videos are waiting for Send. When no hypothesis is `proposed`, the next `lab: analyze` must add new ones (at least 3 open at any time), so the loop never runs dry.

### Lab — what the loop is FOR (user 2026-10-03)
User, verbatim: "the target is not producing videos for sake of production, but testing where searches are, what result of research and experience of marcus are telling us to do and then execution and publishing. Btw. time of publishing should be also tested, probably there is a difference... If Marcus say we should do more then one long video per day and more then 4 shorts per day, do it. Marcus is your expert"
- Search first, always (Marcus, transcript: "key word first … before you turn your camera on … find the keyword phrase"; "when you focus on keywords that get views already you are going into a pool that already has traffic"). A `lab: produce` step may only run a hypothesis whose `why` names (a) the search phrase with its evidence (autocomplete suggestions and/or the views of the top results) and (b) the Marcus rule it follows, quoted from his transcripts. No evidence = go back to analyze, do not produce.
- Titles follow the phrase people type; the first two description lines say what the video is about with that phrase (Marcus, transcript).
- Marcus is the expert for cadence, packaging and what to do next: ask him, act on what his transcripts actually say, and say "not in his transcripts" when they are silent — then run our own test instead of inventing his opinion.
- Cadence lives in `/workspace/glottos-auto/out/lab/schedule-policy.json` (`short_gap_hours`, `long_gap_hours`, `why`); the schedule keeper and the Send queue read it. Change it only on a transcript-quoted Marcus statement or a measured result, and write the reason into `why`.
- Publishing time is a standing test (H18): record the publish hour (UTC) of every Short with its 24 h and 48 h views in `lab.json.publish_time` and compare within the same lane; when one window is clearly better over at least 10 Shorts, propose moving the row there (write the proposal to ask-user.md).

### Lab — scout: find what gets views NOW, on our own (user 2026-10-04)
User, verbatim: "this video I found and suggested you for the analysis, but you should find those on your own, with markus or from
statistic of youtube or from 'get ideas for next video' from youtube and then by applying marcus recomandation produce videos on it,
the long ones and see what works, all this in automatic".
Every `lab: analyze`, FIRST (no Claude tokens, the tick already holds the lock): `python3 /workspace/glottos-autopilot/scout.py`
-> `glottos-auto/out/lab/scout.json`. It reads Studio's "Get ideas for your next video" list and YouTube search for the seed phrases
in `out/lab/scout-seeds.json`, keeps young long videos from SMALL channels with many views per subscriber ("breakouts"), and profiles
the channel behind each: repeated title formula, share of uploads using it, median views, length, days between uploads, typed phrases.
Then, in the same analyze step:
1. For each breakout with `new: true` (and any channel whose `formula_share` >= 0.5): is the title phrase typed (the profile's
   `typed_phrases`)? Does the video rank for a head phrase, or only for its own title (= suggested traffic, Marcus's "dynamic inventory")?
2. Ask Marcus about the best one or two (inside the 3-question budget): what he would point to, how to pattern after it, what to
   change so it is ours ("pattern after what the views are already going to"; "we're not copying ... put our own unique spin on it").
3. Write ONE hypothesis per chosen formula as a long-video SERIES: title patterned on the formula + one sub-keyword angle per video,
   same length class as the breakout, keyword-first description, one official playlist, end screens from our old ranking videos
   (`yt-studio/endscreen.py`), 3 a week, judged after 20 videos (his "rule of 20") on average view duration and suggested-traffic share.
4. Add every typed phrase worth watching to `scout-seeds.json` (keep it under ~15 phrases), so the next scout looks there too.
5. `lab: produce` then makes the series like any other hypothesis - unless `lab.json` says `"produce_paused": true` (then it only queues).
English only (user 2026-10-04, verbatim: "let us stay in english without going to Hindi. However, keep an eye on what exotic pairs of
english can be interesting for the audience. Like gap in market nobody adress. Like serbian who is learning english or albanian who is
learning english"): `breakouts` holds only videos that teach in English; videos that teach English THROUGH another language sit in
`other_language_breakouts` - never model a series on them, never use Hindi (or any other language) in our videos.
Pairs watch: once a week the scout fills `pairs` (20 languages: the learner's own query for "English for beginners", how many phrases
are typed, views and channels of the top 10 results). Each analyze: name the 1-3 pairs where learners type a lot and the serving
videos are few, small or generic ("50 languages" compilations), say so on the Lab tab ("where_traffic_is"), and add or correct
languages/queries in `PAIRS` when a better native phrase is known. It is a WATCH: propose a pair video only as its own hypothesis and
only after asking Marcus; nothing in another language is produced without the user saying so.
Show the scout's result on the Lab tab assessment ("where_traffic_is"): the breakouts, the formula, what we made on it, what it earned.

### Lab — channel survey and packaging watch (user 2026-10-03)
User, verbatim: "but your loop should also permanently judge if thumbnail change is relevant for long videos for example, title change a/b test , all aligned with marcus and constantly surveying the channel from all statistical point of view" and "you have also google trends and other viral statistics where marcus can help you to piggyback on what is trending"
Part of EVERY `lab: analyze`, before new hypotheses are written:
1. Survey the whole channel, not only the test videos: for every public video of the last 60 days and the 20 most-viewed older ones, read
   views now vs the previous snapshot (`analytics/latest.json`: `views`, `views_prev`), and from `analytics/deep.json` the engaged views, average
   view duration, traffic sources and search terms. Write `lab.json.survey`: {"at", "rows": [{"id", "title", "kind", "views", "delta",
   "main_source", "search_terms", "flag"}]} with a `flag` per video: "earning" (still gaining), "stalled" (flat after a burst), "never_shown"
   (under 20 views after 48 h), "search" (search is over 20 % of its views).
2. Packaging decisions, per Marcus (transcript: "it's a title update based on views and stats"; "changing one word in your title is the
   difference between getting like 7,000 views a month and like four views a month"; "the top two lines of your description are the most
   important"; "I post videos they get no views. Okay I need to stop and ask why … are they titled wrong"): for every long video and every
   "never_shown" or "stalled" video decide ONE of: keep · title update (new title patterned on the search phrase) · description update
   (keyword in the first two lines) · thumbnail test (YouTube "Test & compare", 2-3 variants) · re-make (H13). Hand the proposals to
   `glottos-growth-tester`, which APPLIES them itself (user 2026-10-03, verbatim: "what do you mean? you manage it dependely on marcus
   feedback" - no approval step): `yt-studio/retitle.py` for title + description, `yt-studio/thumbnail.py --force` for a plain swap,
   `yt-studio/abtest.py` for a Studio A/B test (thumbnails or titles), all under tick.lock, wording language-gated, every thumbnail looked
   at first, and each change written to `abtests/queue.json` (status "applied", old value, Marcus quote) and reported to the user
   afterwards. Each change must rest on a transcript-cited Marcus rule or a measured result. A thumbnail test on a video with few
   impressions may end without a result - start it anyway when the title/description are already fixed, and note the impressions.
   Never change visibility, never delete. Record each decision in `lab.json.packaging` with the reason and, later, the result.
3. Trends, one look per cycle (Marcus, transcript: "when you focus on keywords that get views already you are going into a pool that
   already has traffic"; "pattern after what the views are already going to"): Google Trends (rising queries for "another word for",
   "other ways to say", "english speaking practice", "synonym"; region worldwide and the channel's top countries), YouTube trending /
   most-viewed videos of the last 7-30 days for our search phrases, and seasonal hooks (exams, holidays, a word in the news). A trend
   is usable only if a learner would search it AND we can answer it with our formats within 24 h. Put usable ones at the top of
   `assessment.where_traffic_is` with the date seen, and make the fastest format first (a Short; then a long video if the Short gets shown).
   If a trend source cannot be reached from the container, say so in `lab.json.outward` and use YouTube autocomplete instead - never invent a trend.

### Pictures — magnifying glass (user 2026-10-05, future production only)
User, verbatim: "In generated by nlm pictures often we have magnifying glass which does not really zooming anything. Whe it does it is ok,
but when it just seats in the middle of the picture, it does not really make sense. So you should judge if there is a zoom or just remove
it." Visuals step: ask NotebookLM for no magnifying glass; look at every picture; keep a glass only if the content inside the lens is
visibly enlarged, otherwise paint it out, crop it or regenerate (max 2 generations per sheet). Critic step: a glass that magnifies nothing
is a defect to send back. Videos already produced are NOT reworked.

### Send controller (user 2026-10-05)
User, verbatim: "you need to have an agent which is controlling that everything goes right when buttone 'send to youtube' is pushed".
`glottos-autopilot/send_watch.py` runs every loop pass without Claude (queue alive, no hanging job, no crash in yt_sendq.log, every sent
video really Scheduled/Public on the channel, sent at >= 1440) and repairs what it can; report `out/yt/send-watch.json`, red banner on
:8093. Step `send: repair` (due only when the same problem stayed for 2 runs): run the agent `glottos-send-controller` - find the cause,
fix the code, bring each job to its true state, never upload twice, write the outcome to ask-user.md, set `agent_done_for`.
Missing-video rule (2026-10-05, after one snapshot with an empty Shorts tab made 16 live Shorts look deleted): one read of the channel
never proves a deletion. `glottos-autopilot/channel_truth.py` answers "is it gone" for `send_watch.py` and for the queue's "deleted" state
(which unlocks a second upload): only absent in the last TWO complete snapshots counts; a half-read snapshot (a tab empty, or more than 5
videos fewer than one read earlier) is "cannot read the channel". `yt-studio/stats.py` does not save such a snapshot (`--accept-shrink` overrides).

### Video quality: 1440 minimum (user 2026-10-05)
User, verbatim: "videos should be in 1440 quality and not in 1080 (as all of videos now in 'not sent' tab)". Nothing goes to YouTube
under 1440 on the short side. Builders render natively at 1440 since 2026-10-05: `build_stop_saying.py` (lane Shorts, 1440x2560), `build_long.py` and
`build_podcast.py` (2560x1440), `build_talk.py` (2560x1440). Their layout numbers stay in DESIGN units (1080x1920 / 1920x1080) and are
scaled by K = 4/3 when drawn (helpers `px()` / `sc()`, class `D`): write any new coordinate in design units, never in real pixels.
NOT converted: `build_short_v2.py` and `build_short.py` (the old "Words That Stick" episode builders, episodes on hold) - convert the
same way before using them again. Safety
net: the Send queue makes a 1440 master in `out/.hd/` for any smaller file and uploads that (`upload.py --file`); the source stays.
The critic step fails a render under 1440.

### Subscribe + bell animation is a MUST (user 2026-10-05)
User, verbatim: "also animation for subscribing and bell should be a must. And if it is present put in the description on which time it
appears for me to check". Every new video gets `shorts/subscribe_anim.py` after the render: a long video at chapter starts (never in the
first 15 s, never in the last 20 s end-screen window; one near the start of the body and one before the closing call), a Short once in
its second half as the closing call. The script prints `SUBSCRIBE_AT: [seconds]` and writes `<video>.subscribe.json`; copy the list
into the video's `content/youtube/<meta>.json` as `"subscribe_at": [..]` - the :8093 card then shows "Subscribe + bell animation at
m:ss" so the user can jump there and check (a video without it shows a red "none recorded"). Gates: the critic step fails a video
that has no animation or whose recorded time does not show it on the extracted frame; `yt_meta_gate` refuses a meta without
`subscribe_at`. The times are for the user's check on :8093 - do NOT write them into the public YouTube description.

Exception (user 2026-10-05, verbatim: "exceptionally what stays in pipeline 'not sent' do not need to be redone for 1440, ok?"): the videos
already rendered at 1080 and waiting on "Not sent yet" are NOT re-rendered. They are sent as they are; the Send queue's 1440 master
(upscale) is all they get. Native 1440 applies to videos produced from now on.

### Long-video launch loop (user 2026-10-09) - 3 new long videos, as a complete loop
User, verbatim: "where we are in youtube traffic aquisition and you are allowed to produce new 3 long videos (remember 1440 quality, notification
for subscribing, thumbnails for A/B testing from the beginning and therefore you need from the start produce those thumbnails, end screen strategy ,
check with marcus about the topics). But before launching those you need to check why very last videos got 0 views, put A/B test in place, learn
from A/B tests already launched etc. It should be a complete loop. And everything I wrote here you should document and save in the journal as
memory." · a few minutes later: "and of course 3 new long video should be in the hypotesis testing framework."
The allowance is THREE long videos (`lab.json` "produce_order": kind "long", count 3). It is not a general un-pause: after the third, set
`produce_paused` = true again and say so. The order of work is fixed - a later step never starts before the earlier one is written down:
1. `lab: analyze` FIRST (before any of the three is produced), and its assessment on the Lab tab opens with these four answers:
   a. Where we are in traffic acquisition: views by source (Shorts feed / Home / search / suggested), what moved since the last cycle, in numbers.
   b. Why the last long videos got 0 views. Start from the facts in hints.jsonl (10-09 note: crowded copied titles, 354 subscribers, no Short
      as a door), then read Studio for each of them (restrictions column, impressions, sources) and say what is confirmed and what is not.
   c. A/B tests in place: every public long video under test; for each Scheduled long video the pictures ready and its title checked against
      the uploads of this week for the same phrase (search filter "this week"; a title that 3 or more fresh videos of other channels carry
      almost word for word is changed before it goes public).
   d. What the launched tests teach: read the oldest and the highest-impression tests (`yt-studio/abtest_read.py`, the video's Reach tab);
      a finished one -> result per variant, winners per technique; a running one -> say so with its age, and compare the video's click-through
      during the test with `ctr_before` as a weaker sign, marked as such. Never report "no result" without having read Studio in this cycle.
2. Marcus on the topics (skill `affiliatemarketingdude`, one batched consult): give him our candidates with their numbers and ask which three
   he would make and why. The three hypotheses must come out of 1a-1d + his answer + the scout; each is a NUMBERED hypothesis in `lab.json`
   with `statement`, `why`, `test` (the number that decides it and the day it is read), `changed`, `marcus`, `next`. No video outside the ledger.
   Each of the three tests a DIFFERENT thing. A topic is allowed only if (i) its title is not a crowded copied title (check 1c) and
   (ii) it has a door: a public Short of ours on the same phrase that is being shown, set to point to the long video ("Related video"),
   or a named search phrase where a small channel's fresh video is being shown.
3. `lab: produce`, one long video per step. A long video is finished only when ALL of this lies next to it - the launch kit:
   - native 1440 (2560x1440), `gate_av.py`, critic;
   - subscribe + bell animation, times in the meta as `subscribe_at`;
   - THREE thumbnails made NOW, at production, not after publication: `abtests/catalog/make_new2.py` (or the NotebookLM worker) -> control +
     two different click techniques, looked at, reviewed by Marcus (`marcus_review.py`), files written into the meta as `"ab_thumbs": [..]`
     and into `abtests/catalog/new.json` "order", so the test starts the day the video is public with no further work;
   - end-screen plan written into the meta as `"endscreen": {"watch_next": "<one specific video id>", "pointed_from": ["<old video ids>"],
     "playlist": "<name>"}` - Marcus: a hand-picked specific video, old videos pointing at the new one, the official playlist;
   - the door: the Short(s) that will point to it, named in the meta as `"door_shorts": [..]`.
   A long video without the whole kit does not go to "Not sent yet"; the critic step fails it.
4. After the user sends them: the day each goes public - thumbnail test started, end screen set both ways, door Short linked; at 48 h and
   7 days the hypothesis is read against its own number and the result is written to `lessons`, then the next hypothesis follows from it.
5. Journal: every step writes its line; the user's messages above are in `docs/nlm-mirror/discussion-journal.md` verbatim.

#### Two rules for every long-video launch (user 2026-10-09, later the same day)
User, verbatim: "\"No Short as a door. The one long video that was shown rose while its sister Shorts had waves. These three had no Short on
their phrase being shown.\" meaning that you need to make sure every time that long video is launched to piggyback the shorts success. And second
\" Long videos are barely shown.\" here I think you should go for testing ranking strategy which marcus like, meaning you take an easy keywords
(examples from ahrefs I provided before) and you look what from those is ranking on google as a first result, then analyse if those are small
channel and then you have a chance to rank their also" · "marcus has tons of information on it" · "if it is not enough, you should create a dedicate
nlm folder \"youtube traffic developement\" and go for each and every higly appreciated videos on youtube on the topic, transcribe them, store them
as a skill (our usual drill)"
- TOPIC GATE - TWO GATES (user 2026-10-09). First, verbatim: "\"piggyback rule\" and piggybacking means that you need to send only long videos on
  topics which worked on shorts"; then, after Marcus and the traffic corpus were asked (both: sound as one gate, too narrow as the only one -
  "it's two different audiences"), asked "one gate or two?", verbatim: "1. both". So a long video is made and sent ONLY when its topic passes
  gate A OR gate B, and its hypothesis names which one, with the numbers:
  - GATE A - proven by a Short (the user's method): a public Short of ours on the same topic did better than our normal Short. The lab writes
    its line with numbers (the Short's views against the middle of our last 20 Shorts; stayed %). No such Short = make the Short first and wait.
  - GATE B - proven by search (the ranking test): an easy keyword where a weak video (small channel, or few views, or old) holds a place on
    Google page 1 in at least 2 of 3 reads (`yt-studio/rank_probe.py`), or a recent long video on a small channel that did many times its
    channel's normal (scout). A big channel holding the place is NOT a pass.
  A topic that passes neither is not made as a long video ('Another Word for Amazing', 10-09, passed neither - made before this rule).
  Launch order for gate A (traffic corpus): the long video first, then its Shorts on exactly the same subject and look, each with "Related
  video" and a pinned comment. Door Shorts made WITH a long video are held on its day by a pin (`out/lab/schedule-policy.json` "pins":
  {"<id>": "<UTC time>"}, read by `yt-studio/schedule_keeper.py`); a Short that is the FIRST test of a topic is not pinned.
- PIGGYBACK, every time: a long video is launched ON a Short's success. Its phrase is the phrase of a Short of ours that had a wave (read
  `analytics/latest.json`), the launch day is set while Shorts of that phrase are being shown, each of those Shorts gets the long video as its
  "Related video" the hour it is public, and a new Short on the same phrase is sent in the same days. `door_shorts` in the meta is mandatory -
  a long video with an empty list is not sent. This holds for every later long video too, not only for the three.
- RANKING TEST (Marcus's method; at least one of the three long videos is this test, and it is a lab hypothesis with its own number):
  1. Keywords: the ones Ahrefs marks Easy (`glottos-auto/out/ahrefs/table.csv`; more on request via `ahrefs_ask.py`).
  2. Per keyword read Google page 1 and YouTube's top results: `glottos-auto/out/lab/rank-probe.json` (`glottos-autopilot/rank_probe.py`, no Claude) -
     is a YouTube video on Google page 1, whose is it (subscribers, views, age), how many of the top 10 carry the exact phrase in the title, where
     our own old video stands.
  3. Green light (Marcus): a video is on Google page 1 AND it is beatable (small channel, few views or old) AND three or fewer of the top 10
     carry the exact phrase. Rank the keywords; the best one becomes the video.
  4. Build to take the spot: the exact phrase FIRST in the title and in the top two lines of the description, said aloud in the first 30 s, as a
     tag, in the official playlist; the video embedded on the anotherwordfor.net page of that word (ask the user for the embed - the site is his);
     end screens of our old ranking videos of the same word pointing at it.
  5. Read: search the exact phrase on Google and on YouTube at 48 h and 7 days (`rank_probe.py --check <id> "<phrase>"`); the position is the
     hypothesis's number. Marcus expects 24-48 h.
- Notify box (lab H50, 2026-10-09): `yt-studio/notify.py <id>` reads the box 'Publish to subscriptions feed and notify subscribers' of a
  scheduled video, `--off` / `--on` sets it (Save, read back; under tick.lock; written to `abtests/queue.json`). Only for a numbered hypothesis.
- More knowledge than Marcus has: skill `youtube-traffic-development` (NotebookLM notebook "youtube traffic developement"), once its corpus
  is in; ask it the same way as Marcus (one batched question per cycle).

### Lab — catalogue click tests: EVERY video that gets impressions is under test (user 2026-10-06)
User, verbatim: "I see in the studio plenty of videos where youtube gave impressions, but nobody clicked. but you run a/b test only on one of those" ·
"you should do everywhere where impressions are there, rigth?" · "remember we should explore as much as possible hypotesis this applies not only
searching topics for videos but also towards what is clicked, why, what Marcus thinks. If youtube is givin impressions, youtube already made his
part of the job to find the audience, now it is your job to convince to click and for this you can implement techniques from marcus, spy on
thumbnail of the competition, produce you own thumbnails and test them" · "to do thumbnails you can use nlm, right? it is not used for a while now
and we have 4 accounts!"
Rule: every public long video with impressions has a Studio thumbnail (or title) A/B test RUNNING, or a finished one with its result recorded and
the next test started. There is NO cap on running tests and NO minimum of impressions (the old "at most 3 tests" / "1,000 impressions a week" gate
is withdrawn - it left 92 search videos with 300-31,000 impressions untested). A test that ends without a winner is a result too: write it down and
start the next hypothesis. Shorts have no thumbnail click (feed autoplay) and Studio offers no test for them.
Everything lives in `glottos-auto/out/abtests/catalog/`:
- `make_thumbs.py` (.venv python, no Claude): per video the control (the thumbnail it wears) + six designed hypotheses - `black` (Marcus: yellow on
  black, the title's words), `band` (frame + keyword band), `stop` ("STOP SAYING X / SAY THIS INSTEAD", the pattern of the 0.5-2.9M-view competitors),
  `ugly` (Marcus: raw, hand-drawn red circle), `face` (Marcus: face + eye contact, the channel host), `xcheck` (red X / green tick, the better word left
  open). `plan.json` = all videos by impressions.
- `nlm/worker.py` (no Claude, run from glottos-marketing): a NotebookLM-drawn thumbnail per video on all 4 accounts (source "Thumbnail briefs" in each
  Glottos notebook, ids in `nlm/sources.json`; styles clay/anime/sketch_note/kawaii; watermark painted out) -> `<id>/nlm.jpg`, state in `nlm/jobs.json`.
  A rate limit parks one account for 3 h, the others go on. Start it again whenever pictures are missing: `docker exec -d -w /workspace/glottos-marketing
  glottos-autopilot sh -c '/workspace/.venv/bin/python /workspace/glottos-auto/out/abtests/catalog/nlm/worker.py >> .../nlm/worker.log 2>&1'`.
- LOOK at every NLM picture before it goes live (spelling of the words, the face, nothing else written, no watermark, no magnifying glass): accepted
  ids go to `nlm/reviewed.json` "ok", rejected to "bad" (a rejected video gets two designed variants instead, or one more generation).
- `launch.py` (no Claude; takes tick.lock per video): `--reviewed` starts the tests whose NLM picture was accepted (control + one designed + NLM),
  `--rest` starts everything else (control + two designed), `<id> ...` named videos. Ledger `tests.json`; every start is also written to
  `abtests/queue.json` (status "applied") as before.
- `spy/spy.py "<search phrase>" ...` (no Claude): the top 12 YouTube results for a phrase with views and a sheet of their thumbnails
  (`spy/sheet-*.jpg`, `spy/search.json`). Marcus: "look at the other thumbnails ... see what's going on", then pattern after the winners or break the pattern.
Every `lab: analyze`:
1. New public long video with impressions and no test -> `make_thumbs.py`, worker, review, launch. Missing NLM pictures -> worker.
2. Tests that ended (Studio shows a winner or "no clear winner"; read the video's edit page / Reach tab): write per variant the watch-time share
   into `tests.json` ("result": winner name, shares, dates), keep the winner live, and add one line to `glottos-marketing/content/insights/ab-lessons.md`.
3. Count winners PER TECHNIQUE over all finished tests (black / band / stop / ugly / face / xcheck / nlm-clay / nlm-anime / ...): that table is the
   answer to "what gets clicked" - show it on the Lab tab scoreboard and use the leading technique for new videos' thumbnails.
4. Next round on each finished video: a NEW hypothesis, never the same pair again - the winner against a technique it has not met, a title test
   (`abtest.py --titles`; own statistics: "Another Word For X" titles earn about twice the clicks of "Synonyms For X [Learn English ...]" on the same
   word), or a technique newly seen at a competitor (run spy.py on the video's search phrase first) or newly quoted from Marcus (one batched question).
A thumbnail must stay true to the video: no numbers or words the video does not contain.

### Lab — tab "ahrefs traffic info" (user 2026-10-06) - NO Claude tokens
User, verbatim: "also in hypotesis assumtions, you can take the ahrefs tool, add the tab in local host and I can provide you with pictures to look
for" · "call this tab 'ahrefs traffic info'" · later the same day: "the pictures in ahrefs tab should be collected in pdf progressively in nlm like
we did in other projects, meaning that whatever is uploaded in this tab goes to pdf in nlm without spending any claude tokens and information (very
basic as it is just level of difficulty of the word and volume) assesed by nlm and table (in googlesheets for example) is created and nlm is using
this table than as a source (we have to sources basically pdf which is rewritten with every new screenshot uploaded to the tab and googlesheet which
is rewritten with each new screenshot uploaded to the tab). All this is done with script without token spend and when information from
research/lab departement needed, you forward the question by using basic cheap model and ask nlm to answer"
How it works (all script, `glottos-autopilot/ahrefs_sync.py`, run by loop.sh on every pass; state `glottos-auto/out/ahrefs/nlm.json`):
pictures dropped on :8093 -> `ahrefs/index.json` -> ONE PDF of all pictures (`ahrefs/ahrefs-screenshots.pdf`, header text printed on each page) ->
replaces the source "AHREFS - screenshots (rolling PDF)" in the Glottos notebook (8306c0a9, account drawnformula) -> `nlm data-table create` (NotebookLM
reads the pictures: Keyword | Difficulty | Volume | Type | Updated | Screenshot) -> the table is written into ONE Google Sheet, always the same
file and the same link (`ahrefs/sheet.json`; user 2026-10-06, verbatim: "the point is to have only one file like we have one pdf and we rewrite
this same file with new information coming from new pictures"): created once by `nlm export to-sheets`, ever after rewritten in place by
`yt-studio/sheet_write.py` (a throwaway headless browser with the drawnformula session: select all, delete, paste, read back as proof) -> the same
NotebookLM source "Glottos - Ahrefs keyword table" is re-synced (`nlm source sync`; re-attached only if it did not take the change) ->
`ahrefs/table.csv` for the tab. A failed step is retried on a later pass. NEVER call `nlm export to-sheets` again for this table: it makes a new file.
Rules for every Claude step (lab analyze, research, any session):
- Do NOT open the pictures yourself and do NOT read them into context. An upload does not make a tick due.
- Need something from this data -> forward the question: `python3 /workspace/glottos-autopilot/ahrefs_ask.py "<question>"` (prints NotebookLM's
  answer only, no citations; `--all` asks over the whole notebook). In an interactive session do it through a cheap-model subagent (Haiku) that runs
  the command and returns the answer verbatim. One batched question per need (shared quota).
- For plain look-ups (which keywords are Easy, a volume) `ahrefs/table.csv` is enough - a few lines, read it directly.
- The numbers are Ahrefs' (web search), not YouTube's: say which is which when both appear in a hypothesis. NotebookLM reads printed text reliably;
  if a row looks wrong, the picture is linked on the tab.
PRIORITY and the DAILY LIMIT (user 2026-10-06, verbatim: "the priority should be not the old videos, but the one we generated and published
recently!" · about fPKxW7BuN8A: "this one for example was shown to the audience 32 times, but clicked only once"):
- Recent videos come FIRST, always: a long video published in the last 30 days gets its thumbnails made for it by hand from its own frames, words and
  true numbers (`abtests/catalog/make_new.py` - styles stop15 / ugly15 / xreal; frames by `glottos-auto/node_modules/ffmpeg-static/ffmpeg`), Marcus
  looks at them (`marcus_review.py pics <json>`), and the test starts with his first pick in slot 1 (`launch_new.py`; Studio keeps slot 1 when a
  test ends without a winner). 2026-10-06: three of the six recent videos (Beautiful, Big, Sad) wore a bare video frame with no title words at all -
  check EVERY newly published long video the same day: does its thumbnail say the search phrase?
- YouTube has a DAILY LIMIT for custom thumbnails for the whole channel. On 2026-10-06 it was reached after 33 tests (about 100 uploaded pictures):
  Studio then says "You've reached the daily limit for A/B Tests with thumbnails. Please try again in 24 hours" and ALSO refuses a plain thumbnail
  change ("Daily custom thumbnail limit reached") - so a video sent that day cannot get its thumbnail. Never spend the day's allowance on old
  videos: `abtests/catalog/daily.py` (no Claude; run by loop.sh on every pass, with `nlm/worker.py --once` before it) starts at most 20 tests per
  rolling 24 h in this order - recent videos, old videos with an accepted NLM picture, the other old videos by impressions - and waits 3 h after a
  refusal. Title-only tests are not under this limit.
- State on 2026-10-06 13:50Z: 32 catalogue tests running (29 old videos + Beautiful, Big, Sad) plus the older test on GNH19NdTu9U; NOT started:
  Happy (O5vQex4ylbw), Stop Saying Very (aXghTlqKcHQ), Problem (M2euCrHGQqQ; it got Marcus's first pick `new-ugly15.jpg` as a plain thumbnail at
  13:46Z) - first in the queue - and 66 old videos. NLM pictures: 6 drawn, then every generation failed on all four accounts (daily allowance,
  my reading); the worker parks an account 4 h after a failure.
- Scheduled videos (2026-10-07, lab cycle 16): `daily.py` treats every id in `new.json` as "new" and `launch_new.py` starts it without looking
  at its visibility, so a video that is not public yet must NOT be in `new.json`. `make_new2.py` therefore registers only ids that are Public in
  `analytics/latest.json`; for a scheduled video it makes the pictures and leaves them in `catalog/<id>/` - run `make_new2.py` again after the
  video went public (it shows up in `daily.json` "untested_new") and it is registered and started on the next pass. Styles for the
  "100 ... | Listen and Repeat" series: `goods` (three real phrases/pairs from the list, ticked) and `circle` (host + 100 in a red circle).
  End screens for scheduled videos: put the pair in `yt/endscreen-chain.json` "map" with a target that is public BEFORE the source goes public.
- Still to build: the reader of finished tests (BACKLOG). `l28THsee6TI` ("30 More English Words", published 10-05, no impressions yet) is not in
  `plan.json`: add it to `make_new.py` when it has impressions.
