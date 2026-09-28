# P01 · Episode 1 "Never learn a word alone": format decision (glottos-format-strategist, 2026-09-27)

## 1. Episode in one line
Forgetting curve (Ebbinghaus 56/66/75 %) → "livid = very angry" alone vs. "He was livid when his flight was cancelled" → synonym ladder (cross → irate → fuming → seething → furious → livid → incensed → apoplectic, one picture each) → CTA anotherwordfor.net.

## 2. Decision: a HYBRID Short, not an all-flashcard Short
| Part | Beats (ep01_v2) | Format | Why |
|---|---|---|---|
| Hook + forgetting curve | 1–2 | **Infographic panel + voice** (keep as is) | A number story and a mechanism. A flip card can't carry a curve. |
| Word alone vs in a sentence | 3–4 | **Infographic panel** (keep) | This is a before/after comparison, not something to recall. |
| Synonym ladder | 5–8 | **Scene → word flip cards ("picture test")**: front = picture with the word hidden + "Which word?", 1.2–1.5 s answer pause, back = word + one example sentence + its place on the ladder | Recall beats re-reading. This is the episode's own lesson, and the viewer gets to *do* it. It's also the only part where the content is a vocabulary set. |
| Ladder recap + CTA | 9–10 | Card (keep) | |

**Only 4 of the 8 synonyms should be quiz flips (with a pause): cross, seething, livid, apoplectic.** Their scenes point to one answer: the mildest, the hidden one, the word we just taught, and the most extreme. **Irate, fuming, furious and incensed get a straight reveal** (picture and word together, no pause). The flashcard test shows why: the fronts for irate, fuming and furious ("arguing loudly at the service desk", "steam coming out of your ears", "slamming the door") fit all three words. The audio script itself says the middle words are close in strength. A quiz with no single right answer feels unfair. With 8 pauses the Short would also run about 10 s longer.

### Evidence (PROBLEM 01 competitor document f3b77a74, synthesis 60678678; read with `source content`, no queries)
- **There is no Shorts evidence on YouTube.** The top 40 by views include 0 Shorts, all long-form (median 614,706 views, 3.68 % engagement). So the choice of format inside a Short rests on the TikTok discover pages and on technique evidence. There is no measured A/B test.
- **Active recall** (rank 2) has by far the widest reach beyond each channel's subscribers: 67.0× (Wealth & Drive), 32.84× (easyway, actually), 27.72× (The Peak Circuit). → A self-test beat is justified.
- **Picture association** (rank 3): WIRED 7.5 M views; Rene Bastarache 6.69 % engagement and 19.95× reach; Jim Kwik's "turn it into a picture". → One picture per synonym is right.
- **TikTok, picture→word and quiz formats** (like counts as shown on the discover pages, a weak signal): "Everyday Home Objects in English" 8.4 M; "Birds Vocabulary" 971.3 K; "Kitchen Utensils… Can you name all of them?" 912.1 K; "Last one's tricky 🤔 / Test your word choice" 537.3 K; "Stop saying VERY → stronger words" 597.3 K; "Difference between these English terms (Coffin vs Casket…)" 3.6 M. Picture-to-name and "can you name them?" formats get strong reactions. Nuance and comparison do too.
- **Counter-evidence and guardrail.** The gap table records deck fatigue ("Anki… feels like a chore; cards teach words in isolation"), and Steve Kaufmann (4.97 M views) says he doesn't believe in flip cards. → Don't brand the beat as "flashcards" or a "deck". Every card is **scene-first** and the back **always carries a sentence**. That way the format supports the episode's rule instead of contradicting it.

## 3. Rejected alternatives
- **All-flashcard Short:** loses the curve (a number story) and the before/after argument. 8 quiz pauses plus the curve would push past 60 s.
- **Keep the ladder as passive panels (current v2):** the viewer only watches. It misses the recall mechanic with the best reach evidence, and there is no answer moment that invites comments.
- **Quiz Short (multiple choice):** 2–4 options per card crowd a 9:16 frame and slow it down. A hidden-word flip does the same job.
- **Two-host podcast:** fits nuance and debate (Ep2 "is re-reading useless?"), not a picture ladder. The audio script (source 72c8e8e7) already exists if an audio version is wanted.
- **Mind map / data table:** fine for a pinned comment or thumbnail, not for the Short itself.
- **Worth doing as a spin-off, from the same assets:** a stand-alone 25–30 s "Picture test: 8 kinds of angry" Short with all 8 flips and a word bank at the bottom, which removes the ambiguity. Use it later as a teaser for Ep2 (recall vs re-reading).

## 4. NotebookLM test result (the one allowed generation; nothing more is needed)
Command run (artifact `36d60c41-bb6e-419c-bb48-13c7567b3c9b`, source 72c8e8e7 = Ep01 audio script, easy):
`nlm flashcards create 8306c0a9-… --difficulty easy --source-ids 72c8e8e7-… --focus "Synonym ladder for livid, one card per synonym, 8 cards only: cross, irate, fuming, seething, furious, livid, incensed, apoplectic. FRONT = the everyday scene from the script … phrased as a question: which word fits? BACK = the single word + one short natural example sentence + how strong it is (mild / strong / extreme). Use only the scenes and facts in the script; no statistics. Plain, natural English for B1 learners. Never use the word naked; never say a word is learned in isolation." -y`
Downloaded: `state/nlm-raw/ep01-flashcards-livid.json` (`{title, cards:[{front, back}]}`, text only, **no images**) and `.md`.

Sample cards (verbatim):
- Front: "A mum looking at muddy shoes on a clean carpet: which word fits?" / Back: "Cross. Example: She was cross when she saw muddy shoes on the carpet. (Strength: mild)"
- Front: "Silent, jaw clenched, with anger boiling underneath in a meeting: which word fits?" / Back: "Seething. Example: She sat seething with her jaw clenched during the meeting. (Strength: strong)"
- Front: "Pale with rage when your flight is cancelled: which word fits?" / Back: "Livid. Example: He was livid when his flight was cancelled. (Strength: extreme)"
- Front: "Red-faced and so angry that you literally cannot speak: which word fits?" / Back: "Apoplectic. Example: He became apoplectic with anger during the argument. (Strength: extreme)"

**Verdict: usable as a text source after a light edit. Not publishable raw.**
- ✅ Exactly 8 cards in ladder order. Each one reuses the script's scene. The English is natural and B1-friendly. "naked" appears 0 times and nothing is invented.
- ⚠ Ambiguous fronts: irate / fuming / furious (and incensed vs livid) are interchangeable as quiz answers. → Hence the 4-flip / 4-reveal split.
- ⚠ Card 8 drifts from the script: "literally cannot speak" (the script says "can barely speak"; ep01_v2 says "can't even speak"). "literally" is filler. Its example ("during the argument") drops the scene, so it's a weaker anchor. Suggest: "Red-faced and so angry you can barely speak" / "He was apoplectic, so angry he could barely speak."
- ⚠ The strength labels clash with the synonyms infographic. The flashcards put irate at "strong" and livid at "extreme"; the infographic bands say Mild = cross, irate · Simmering = fuming, seething · Intense = furious, livid · Extreme = incensed, apoplectic. Pick ONE scale (the infographic bands, since they're already on screen) and drop "(Strength: …)" from the card text.
- All card text must go through glottos-language-editor before rendering (hard gate).

## 5. What the scenario writer and shorts builder need (does NOT exist yet in shorts/build_short_v2.py)
The builder currently has only two beat types: `panel` (image crop, slow push-in) and `card` (headline/sub). The beat length is always the TTS audio length + 0.35 s.
1. **New `flip` beat type** (missing): `{"flip": {"front_panel": "syn:…", "mask": "word", "prompt": "Which word?", "back_word": "seething", "back_example": "…", "pause": 1.3}, "speech_front": "…", "speech_back": "…"}`. It needs two TTS segments with a **silent answer pause** between them (a visible countdown or ticking bar), then a reveal (flip or slide animation, optional sound effect).
2. **A word-masked picture crop** (missing): every word is printed in big letters ABOVE its picture in `ep01-synonyms-infographic.png` (the 4 bands are split into left and right cells). The current `band_panels` split returns whole bands with the words visible, which would spoil the quiz. Needed: per-cell crops (left/right half of each band), with a "picture only" version (the header row with the word cut off) for the front and the full cell for the back. Alternatively, generate a word-free picture sheet. That would be a new infographic generation, not done here.
3. **`reveal` beat** (picture + word at once, no pause) for irate, fuming, furious and incensed. This can be approximated today with `panel` on a per-cell crop, but only after item 2.
4. **A ladder progress strip** (optional, missing): a small 8-dot mild→extreme bar that lights the current word. It replaces the "(Strength: …)" text.
5. **A card importer** (optional): read `state/nlm-raw/ep01-flashcards-livid.json` into flip beats. Text still goes through the language gate, so there's no raw passthrough.
6. The watermark: the synonyms sheet carries "Gemini Notebook" bottom-right. The per-cell crops must exclude it (the existing band splitter already drops the watermark strip; keep that).

Rough timing: beats 1–4 unchanged (~25 s) + 4 flips × ~4.5 s + 4 reveals × ~2.5 s + recap/CTA ~9 s ≈ 62 s. Tight. If it runs over 60 s, cut beat 9 (the recap card) or merge it into the CTA.

Not done (by instruction): no edits to shorts/units/*.json, the article or the scripts; no `notebook query`; no other generations.
