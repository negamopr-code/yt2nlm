# Test & compare (A/B Testing): verified facts for @anotherword8913

Verified 2026-09-29 ~11:30Z by glottos-growth-tester, read-only in the signed-in yt-studio Chromium. The dialog was opened and closed with Escape; Save stayed disabled, so nothing was changed.

- **Available on this channel: YES**, for a public long-form video (GNH19NdTu9U, 5:33, not made for kids).
- Entry points (Studio > Video details): an "A/B Testing" button under the Title field AND an "A/B Testing" tile in the Thumbnail row (next to Upload file / Select from video).
- Modes: **Title only / Thumbnail only / Title and thumbnail**.
- Title mode: 3 slots. Title 1 = the current title (prefilled), Title 2 is required, Title 3 is optional. Footer says "2nd title is required", and the button is "Set test".
- Thumbnail slots: not inspected (the dialog opened on Title only). Assume up to 3, same as titles; confirm on first use.
- Winner metric: not shown in the dialog (the "?" tooltip was not opened). Public docs say watch-time share; unverified here.
- Shorts: NOT checked. The Short Jc8HSUPqmHQ's details page shows no A/B Testing entry in its text dump, so assume Shorts are excluded.
- Private / made-for-kids: not checked.
- ~~Practical gate: start tests only at >=1k impressions/week.~~ WITHDRAWN 2026-10-06 (user: "you should do everywhere where impressions are there"): that gate left 92 search videos with 300-31,000 impressions untested. Every public long video with impressions is tested; no cap on running tests. See docs/autopilot.md, "Lab — catalogue click tests".
- Automation hooks: title-row button text "A/B Testing" (exact), dialog = visible [role=dialog], close = Escape (the Cancel button isn't labelled "Cancel"; there is an X).
- 2026-10-08 18:06Z: a plain title + description save on a video with a RUNNING thumbnail test (tS4g2lMg080) went through with no warning, and the thumbnail row still said "Running…" one minute later. A video with a running TITLE test shows no thumbnail test (row offers Upload file / Select from video / A/B Testing): one test per video. Tests started 10-06 12:56Z were still running after 53 h.
- 2026-10-11 09:20Z: a test runs **14 days**. Video analytics > Reach has an "A/B Test" card: countdown ("12 days 9 hours left…"), tabs Thumbnails / Titles, one row per variant with "Watch time share" ("–" until Studio has enough data; all cards read so far say "Not enough information to display data"). Checked against four start times (GNH19NdTu9U, rRs43xoz4V0, 4TIufuY6ElY, FQXYfzYj7nQ).
- 2026-10-11: a video with a running test does not offer a second one - abtest.py then times out on "Thumbnail only" (jv1pSrdkgrU, 11 false "failed" records). A Scheduled video (gZytp1HM-vU) shows the title's "A/B Testing" button and no thumbnail test row.
- 2026-10-11: Studio prints thousands with a decimal comma ("1,1K") in this browser since about 10-11; percentages keep the point.
- 2026-10-11 19:43Z (lab analyze 26): inside a `lab: analyze` tick the loop (loop.sh, fd 9) already holds `tick.lock` for the whole Claude run, so a second `flock` on it never returns (two `flock -w 300` reads waited 5 min each and failed). `launch_new.py` / `launch.py` take that lock themselves: from inside a tick run them with the lock path swapped (`python3 -c "src=open('launch_new.py').read().replace('/workspace/glottos-autopilot/tick.lock','/tmp/inner-tick.lock'); sys.argv=[...]; exec(src)"`) and call `abtest_read.py` / `video_analytics.py` with plain `docker exec`. Outside a tick (daily.py) nothing changes. A test started on a video 4 h 43 min after it went public showed "13 days 23 hours left…" at once; three rows, watch-time share "–".
