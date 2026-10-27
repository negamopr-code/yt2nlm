# S3 (BIG) language gate v1: pre-generation text gate

Gate: glottos-language-editor (headless autopilot step "special S3: gate_text"). Date: 2026-09-28.
Scope: script.md (every spoken line + on-screen notes), focus.txt, meta.json. No unit JSON exists for specials, so there is no `lang_gate.py` stamp (same convention as S1/S2). No NotebookLM query was used.
Sources: Oxford Learner's (large, considerable, bulky, hefty, jumbo, huge, giant adj, enormous, massive, whopping, vast, towering, mammoth adj, immense, ginormous, big; fetched live), Cambridge (large, considerable, hefty, ginormous, whopping, giant, bulky, mammoth, towering, massive; fetched live), web search for "large is more formal than big".

## Verdict: APPROVED (after the fixes below)

| Line | Problem | Fix | Confidence |
|---|---|---|---|
| Considerable scene + recap | Oxford labels it "(rather formal)"; Cambridge has no label. "Formal" overstates it. Use is natural (Oxford's own example is "a considerable amount of time"), and it is used for time, not for a physical object. "The seller gives you…" is unclear (which seller?). | "Fairly formal" (scene + recap + focus.txt). "You pick up one pumpkin seed and a book with eight hundred pages." | high |
| Bulky scene | "a box of pumpkin food" is not idiomatic; "as big as a sofa, in a very strange shape" is awkward. The gloss "awkward" drifts from the dictionary. | "a box of plant food. It's as big as a sofa and a very strange shape … on the way out you walk straight into a lamppost". Gloss: "big and difficult to carry or move" (Oxford: "large and difficult to move or carry"). The recap matches. | high |
| Hefty scene + recap | Oxford labels the money sense "(informal)", but the script gave no register. | "With money, bigger than usual, and a bit informal" / recap "With money, a bit informal: "a hefty bill."" Cut "Your wallet is empty." (the picture shows it). | medium-high |
| Jumbo scene | Where the seed is planted was never said, but the next scene says "The pot is broken". | "you plant the seed in a flowerpot" | high |
| Giant scene | Oxford marks giant (adj) as [only before noun], but the script said "Usually". The timeline was broken: "Next day the headline says" and then "By lunch…". | "Only before a noun". "The local newspaper puts it online: "Giant pumpkin in Mill Lane!"" (the screen note now shows a phone with the website). | high |
| Massive scene | "your wheelbarrow, under it, is as flat as a pancake" is an odd word order. A draft "Then it rolls onto…" contradicted "it doesn't move". | "You try to push it into the shade, but it doesn't move at all. And your wheelbarrow is under it — as flat as a pancake." | high |
| Whopping scene | The number was said two ways ("one thousand two hundred" vs "twelve hundred"). "drives up with a truck scale" is jargon (a weighbridge). | "twelve hundred kilos" in both places (and in focus.txt). "A farmer arrives with a scale on his truck." Cut "and you all hold your breath" (length). | high |
| Vast scene | "football field" is American in a British setting (garden centre, till, wellies). "From the church roof" raises the question of who is on the roof. | "football pitch", "From the church tower". Vast is used for the area of the leaves, not for the pumpkin itself. This is correct (Oxford: "extremely large in area…"). | medium |
| Towering scene + recap | "It's towering over the whole street" is the verb *tower over*, not the adjective. Oxford marks towering as [only before noun], and Cambridge labels it "literary". No register was given. | "Everyone in the street stops and looks up at this towering pumpkin." Gloss: "very tall. A bit literary, and only before a noun". Recap: "Towering — very tall. A bit literary." It is now an adjective in both. | high |
| Ginormous scene + recap + focus | "The strongest word here" is not supported: Oxford and Cambridge both gloss it "extremely large", the same as enormous. | Dropped. Now "Informal and playful". focus.txt: "do not call any word 'the strongest'". Register confirmed: Oxford "(British English, informal)", Cambridge "informal". | high |
| Ginormous stress cue "jy-NOR-mous" | A respelling in the source risks NotebookLM reading it aloud, and "jy" is ambiguous. | Removed. The TOW-er-ing and im-MENSE cues stay (real spellings, screen only). | medium |
| Length | +3 words net after the fixes | Trims listed above | high |

Checked and passing, with no change:
- large: "a bit more formal than big". Cambridge's thesaurus labels *big* informal, and grammar sources agree. Oxford sense 2 supports the menu/clothes sizes.
- jumbo: Oxford "[only before noun] (informal) very large; larger than usual", with the example "a jumbo pack of cornflakes".
- huge ("extremely large", "a huge mistake").
- enormous (neutral).
- massive: Oxford sense 1 "very large, heavy and solid", with the example "a massive rock". The "serious" sense is not taught.
- whopping: Oxford "(informal) very big"; Cambridge "[before noun] informal".
- vast ("the vast majority").
- mammoth: Oxford adj "extremely large", [usually before noun], with the example "a mammoth task".
- immense ("extremely large or great"; "immense relief/pride").
- "flat as a pancake".
- "It's only a story".
- The hook, list, pause and score lines.
- The ladder is stated as approximate: "roughly", "a guide, not a rule".

Beat order: hook -> plain list of 10 -> spoken pause cue -> one continuous 15-word story (10 + 5 extras) -> second pause "in order" -> "fifteen, not ten" reveal + 15-row recap -> score comment -> transfer -> CTA. Result: OK.
Claims: no memory statistics, no "most people", no "10x", no "strongest", and no claim that the extras "came only from the story". No podcast markers. Result: OK.
CTA: "look up "another word for big" on anotherwordfor.net". The page https://anotherwordfor.net/another-word-for-big/ returns HTTP 200 with `-k`. The site's SSL certificate has expired (known, postponed), so browsers will show a warning. There is no promise of example sentences or a search box. The page does not list giant, towering or ginormous, but "for more words" stays true. Result: OK.
focus.txt / meta.json: focus.txt was updated to match the script (fairly formal, a bit informal, twelve hundred kilos, football pitch, towering adjective + a bit literary, ginormous "informal and playful", no "strongest"). meta.json (title, description, tags) is idiomatic and consistent. Result: OK, no change.
Final spoken words: 970 (same counting method as S2 = 968). That is ~6:56 of speech + ~6 s holds ≈ 7:00. S2 at the same length came back from NotebookLM at 7:28, so expect ~7:25.

## Not checked
- The generated NotebookLM video, its transcript, and the text inside images (critic step and re-gate).
- The title says "15" while the hook says "ten". This is kept as in S1/S2: it slightly spoils the reveal, but it is not a language error.
- The "Accuracy notes" table in script.md still holds the writer's original GATE questions. They are superseded by the "GATE RESOLUTIONS" paragraph added under it (these notes are not spoken, and they are not in focus.txt).
