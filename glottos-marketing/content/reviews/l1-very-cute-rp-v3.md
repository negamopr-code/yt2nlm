# Viewer-critic review: l1-very-cute-rp-v3 (step 7b, 2026-10-14)

Video: `state/shorts/l1-very-cute-rp-v3/final.mp4` (= `/workspace/glottos-auto/out/l1-very-cute-rp-v3.mp4`, same md5), 1440x2560, 27.7 s, kokoro am_michael 1.05, no music.
Frames: `state/shorts/l1-very-cute-rp-v3/critic/f0.png f0.5.png f1.png f2.png f3.png` + beat midpoints f5.9, f9.6, f13.3, f17.2, f21.1, end f23.5/f25/f26.5, loop f27.4.

## Verdict: PARTLY
It gives five usable replacements with a picture and a short phrase, and you can copy one tomorrow. But the "when/why" half of the pain is only a small silent pill of text. Two of the five usage lines are wrong or empty ("for babies and baby animals" is too narrow; "easy to love" just restates the word). Nothing tells me to repeat the phrase in the gap.

## Pain (learner words) -> what the video gives -> gap
Verbatim learner evidence (NotebookLM learner-comment sources vol. 1-4 + channel comments in `content/insights/audience-needs.md`):
- "Very very thanks 😊"
- "very very nice more more video make you"
- "You are an amazing teacher: explain clearly, very profesionally, very very sympathic"
- "when I have a meeting I say the same words all the time , what is the best way to memorize the new words and use them"
- "Can u help me how and when to use literally and basically"
- "It's great because it also gives you the context it can be used in and synonyms of the word"
- "but why?" (channel comment under a synonym Short)
- "There is also minuscule as in a minuscule mouse." / "Frigid too" (viewers add their own word)

Pain in one sentence: "I always say the same words (very, very very) and nobody tells me which better word fits where." Solved = tomorrow I say "an adorable puppy" or "a charming little village" instead of "very cute", and I know I would not call a village "adorable".

Gives: 5 words, each with a picture, a spoken 3-4 word chunk and a usage pill. Gap: the usage pill is never spoken and sits on screen for about 3.5 s next to a headline, a picture and an example. The voice says only "Adorable: an adorable puppy". A B1 viewer reads the big word, looks at the picture and hears the chunk, and never reads the "why". So the "but why?" pain is barely touched.

## Required checks
- 2(a) Promise without answer in the first 2 s: **YES.** At 0-3.9 s only "Stop saying 'very cute'" is on screen (struck through at about 0.5-1.0 s) plus "5 better words" from 2 s. The first answer word is heard and shown at about 3.9 s (beat 2 starts at 3.89). The background floats only "very cute" and no answer words.
- 2(b) Dead look repeated: **NO.** There is no full-frame clay mascot (pictures are kawaii puppy, pencil teddy, watercolour child, comic street, LEGO dog), no answer in frame 0 and no idiom badge. The only boy is the tiny faint logo tile in the floating background.
- Spelled-out word: **none** (whisper: "adorable", "cuddly", "lovable" all read as words).
- Repeat gap: about 0.95 s tail after each example plus wav tail, so about 1.0-1.3 s of silence after each chunk (beat lengths 3.56-3.93 s). OK. But there is **no cue** ("say it!" or a mouth icon), so most viewers won't use the gap.
- Closing heard: "Which word will you use? Comment your own word for very cute" at 22.9-26.6 s. **YES.** Loops back to the hook card at 27.2 s.
- Text lines: **FAIL on 2 of 5 beats.** Adorable has headline + 2-line pill ("for babies and baby / animals") + example = 4 lines. Charming has headline + pill + 2-line example ("a charming little / village") = 4 lines. The others have 3.
- Legibility: headline and example are large and fine. The pill is about half the size, white on grey, readable but competing.
- UI zones: the brand top bar is fine. The subscribe+bell sits bottom-left at about y 74% (22.6-27 s), just above the title/channel overlay, OK but tight. The picture card runs to about x 92%, so its right edge (the bear's arm, the LEGO wall) sits under the like/comment rail. Not critical.
- Picture vs words: puppy, teddy, smiling child and village all match. **"a lovable old dog" = a top-down grey LEGO dog with motion-blurred ears.** At phone size it reads as a robot or insect, not an old dog, and "lovable" does not show.
- NotebookLM/Gemini mark: the source PNGs carry "Gemini Notebook" bottom-right, but the card crop removes it. **None visible** in any frame checked.
- subscribe_at [22.6] recorded in `content/youtube/l1-very-cute-rp-v3.json`. OK.

## Second-by-second (where I'd swipe)
- 0.0-1.4 "Stop saying very cute": a black card with text. It stops me only if "very cute" is my phrase. "Cute" is less of an everyday pain than tired/big, so expect a weaker stop than the winners.
- 1.4-3.5 "Here are five better words": promise. This is the first swipe risk at about 2-3 s, because nothing visual happens after the strike line.
- 3.9-22.9 five beats at about 3.7 s each with a progress bar. The pace is good, every beat changes picture style, and there's no dead air.
- 19.2-22.9 Lovable: the weakest picture. A viewer may pause on "what is that?" (fine for retention, bad for meaning).
- 22.9-27.2 end card plus subscribe animation. The question is clear.

## Takeaway test
One action: "Instead of 'very cute' for a puppy or a baby, say 'adorable'; for a place, say 'charming'." This is nameable, which is why it isn't DOESN'T.

## Retention risks
27.7 s against 25.5-25.9 s for the winners: fine. The hook is 3.9 s of text-only screen, the same as the winners. Repetition: the word is said twice per beat, good. The usage pill competes for reading time.

## Trust risks
- "Adorable: for babies and baby animals" overclaims. Natives say "an adorable couple", "an adorable little café". A learner will over-restrict it.
- "Lovable: easy to love" is circular and teaches nothing.
- Lovable picture doesn't show an old dog.

## Ship-blockers
None (no spelled word, no watermark, subscribe present and recorded, 1440).

## Top 3 fixes (by impact)
1. **scenario-writer + voice:** speak the usage line in about 4 words ("Adorable, for babies and pets: an adorable puppy") so the "why" is heard, not just printed. That answers the "but why?" pain.
2. **language-editor:** rewrite the Adorable pill ("very cute, makes you smile") and the Lovable pill ("you can't help loving it" or similar, not circular).
3. **shorts-builder + visuals:** cap the cards at 3 lines (widen the pill box or shorten the text, Adorable/Charming), add a 1 s "say it" cue in the repeat gap, and replace the Lovable LEGO picture with a readable old dog.
