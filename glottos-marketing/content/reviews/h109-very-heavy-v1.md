# Viewer-critic review v2: h109-very-heavy-v1 (rebuilt with build_first_frame.py)

Reviewed 2026-10-27 (re-review after v1 DOESN'T). File: /workspace/glottos-marketing/state/shorts/h109-very-heavy-v1/final.mp4. It is 1440x2560, 30 fps, 15.80 s, Kokoro voice. Meta: content/youtube/h109-very-heavy-v1.json has subscribe_at [9.0].
Pain evidence: there is still no learner quote about "very heavy" on file. I spent no NotebookLM query. The pain is the brief's: "I always say 'very heavy'; give me better words." Solved means that tomorrow I say "This bag is hefty" or "It's back-breaking work."

## Verdict: PARTLY (fixed since v1, but not shippable as is)
The v1 blockers are gone: no prompt leak, the pictures are text-free, subscribe and bell play at 9.0 s, the video is 15.8 s, and the longest silence is 0.35 s (tail). Two words are usable, but every picture contradicts its story line, "massive" teaches size, and the subscribe pill covers the payoff caption.

## Ship blockers
1. The subscribe/bell overlay covers the caption "It's back-breaking work." at about 11.7-12.7 s. The pill and the bell sit on the same row as the line, so the viewer reads "...r[bell]king work." It also covers the very sentence I need to copy. Move the overlay (corner "bl" lands on the caption row) or lift the caption.
2. The pictures contradict the words in all 3 beats:
   - 3.2-6.0 "Mia lifts a big box": a boulder with an arrow. No Mia, no box.
   - 6.2-8.7 "She drops it on her foot. Ouch!": boxes on a cart, an oil can, an electric-hazard sign and a spring. No woman, no foot, no drop. The hazard sign suggests "electric", which is a false clue.
   - 9.2-12.7 "SHE moves boxes": a MAN on stairs.
   A viewer who has to choose between the picture and the words loses trust.
3. The brief claim "picture 1 at frame 0" is FALSE. Frame 0 to about 3.1 s is the text hook only ("Stop saying 'very heavy'" / "3 better words"). The first picture appears at about 3.2 s with "Massive". The H109 variable is not met, so the lab result for H109 must not be counted as tested.

## Pain -> gives -> gap
- Gives: massive, hefty, back-breaking, each in a spoken sentence and on a card.
- Gap: "Massive" is a SIZE word (very big), not very heavy. The boulder picture even reinforces "big". There is no nuance (hefty = a heavy object, back-breaking = hard physical work), and there is no self-test moment.

## Second by second (faster-whisper small.en)
- 0.00-1.22 "Stop saying very heavy." Strong hook with the red strike. It is text only.
- 1.52-2.74 "Here are three better words." This is the third second without a picture, so it carries a mild swipe risk.
- 3.16 "Massive, Mia lifts a big box." 5.04 "It's massive." Boulder picture, card in sync.
- 6.16 "Hefty, she drops it on her foot." 8.08 "Ouch, it's hefty." The confusing cart/hazard picture.
- 9.0 subscribe + bell start. 9.24 "Backbreaking, she moves boxes all day." 11.66 "It's backbreaking work." The man-with-boxes picture, with a magnifying-glass lens that does enlarge him (small stair figures outside the lens), so the lens passes. The overlay hides the caption.
- 13.06 "Which word will you use?" 14.62 "Comment yours." The end card is fine. The tail is 0.35 s, so the loop is OK.
- Gaps between lines are 0.25-0.29 s. No word is spelled out ("Backbreaking" is one word). POLICY: clean.

## Takeaway test
"It's back-breaking work." and "This box is hefty." are usable tomorrow. "Massive" does not answer "very heavy", and there is no try-it moment.

## Retention / trust risks
- Pacing is good (15.8 s, no dead air).
- Legibility: the overlay collides with the line at 11.7-12.7 s.
- Sync: the cards match the voice, but the pictures do not match the story (see blocker 2).
- Language: massive used as a weight word.

## Top 3 fixes (by impact)
1. visuals: redraw 3 text-free pictures of the SAME woman (Mia): lifting a heavy box (straining, not just big), the box on her foot with "ouch", and her carrying boxes all day. Drop the hazard sign. shorts-builder: put picture 1 on screen at frame 0 (behind the hook).
2. shorts-builder: place subscribe_anim where it cannot overlap a caption (e.g. top-right, or at 13-15 s over the end card's empty area), and re-record subscribe_at.
3. scenario-writer + language-editor: replace "massive" with a weight phrase ("It weighs a ton" / "heavy as a rock"), or add "...and heavy". Add a 1 s self-test ("Your suitcase is... ?") before "Comment yours."
