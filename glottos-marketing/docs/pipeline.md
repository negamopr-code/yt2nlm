# Glottos go-to-market: content pipeline (user 2026-09-27: "an agent responsible for each step")

Agents live in `~/.claude/agents/glottos-*.md` (user-level, usable from any Claude session).

| # | Step | Agent | Main output |
|---|------|-------|-------------|
| 1 | Learner pain + competitor evidence | glottos-pain-researcher | `PROBLEM NN — <pain>` doc (NotebookLM + content/problems/) |
| 2 | Long-form article for anotherwordfor.net (with synonym spin) | glottos-article-writer | content/articles/pNN-*.md |
| 2b | **Format choice per episode**: infographic Short, flashcards, quiz, slides, podcast, video overview, data table, mind map | glottos-format-strategist | content/articles/pNN-epMM-format.md |
| 3 | Episode map, unit JSON, podcast audio script | glottos-scenario-writer | shorts/units/*.json, pNN-shorts-scenario.md, pNN-epMM-audio-script.md |
| 4 | **English-language gate (mandatory, every text change)** | glottos-language-editor | approval stamp in the unit (`shorts/lang_gate.py`); the builder refuses to render without it |
| 5 | NotebookLM infographics → panels, watermark removed, wording in the image checked | glottos-visuals | state/nlm-raw/*.png |
| 6 | Voice: edge-tts (choice on http://localhost:8093/ Voices tab) or NotebookLM brief podcast | glottos-voice | voices/choice.json, nlm-podcast-*.mp3 |
| 7 | Render + frame QA | glottos-shorts-builder | state/shorts/<id>/final.mp4 |
| 7b | **Viewer's view: "does it solve the pain point?"**: frames + timed transcript vs the learners' own words, verdict SOLVES / PARTLY / DOESN'T + top 3 fixes | glottos-viewer-critic | content/reviews/<video-id>.md |
| 8 | YouTube metadata (content/youtube/epNN.json, language-gated) (NO upload: the user takes it from :8093 and decides; yt-studio :8115 only on explicit request) + publish to :8093, replace NotebookLM sources, mirror journal, commit | glottos-publisher | http://localhost:8093/<id>.mp4 |

Standing rules: **everything runs strictly in series** (one agent / render / NotebookLM generation at a time; user 2026-09-27) · new version = new unit id (never overwrite a version the user has seen) · official logo = @anotherword8913 channel avatar · every episode carries the synonym spin (5–10 synonyms, one picture each) · nothing is posted externally without the user's go.
