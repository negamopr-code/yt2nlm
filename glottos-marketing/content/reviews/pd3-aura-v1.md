# Viewer-critic review: pd3-aura-v1 (lab H86)
Reviewed 2026-10-18. `state/shorts/pd3-aura-v1/final.mp4`: 1440x2560, 30 fps, 14.70 s. Clip: Two Tars (1928). Segments [329.6,332.0] [362.3,371.8] [372.05,373.05] [373.25,375.2] (14.85 s of footage for T = 14.64). subscribe_at [7.4], NOT yet recorded in content/youtube.

## Verdict: PARTLY (closest to ship of the three) - the picture tells "-1000 aura" by itself, but there is a 0.54 s unreadable flash and a 1 s cut to another location
## Pain: same corpus quotes as pd3-rizz-v1.md.

## Heard
0.00 He tries to look cool in front of the girls. Then the gum machine breaks. / 5.10 Aura is the cool, confident vibe you give off. / 8.32 Crawling on the ground for gumballs? / 10.62 Minus a thousand aura. / 12.46 Ever lost aura like this? (ends 13.9). No spelled-out words.

## Second by second
- 0.00-1.92 Frame 0: "POV: instant -1000 aura" (one line, readable) over Hardy grinning smugly beside the gumball jar. A strong match for "tries to look cool".
- 1.92-2.46 A 0.54 s wide shot of the sailors and girls at the counter (a source cut at 331.46 inside segment 1). It is too short to read, so "in front of the girls" goes by unseen.
- 2.46-12.0 Hardy on his knees in a sea of spilled gumballs, scooping them and stuffing them into his top. "aura / the cool, confident vibe you give off" plays over the crawl, which gives a contrast (acceptable, since the hook already set up the loss). "-1000 aura / that was so embarrassing" matches perfectly.
- 12.0-13.08 OTHER LOCATION: Laurel and two girls in the car on the street (source 371.88-373.26, the film's cross-cut). Laurel looks bored, not shocked. It lands under "Ever lost aura like this?" and reads as a random new scene.
- 13.08-14.7 Back to the crawl. There is motion until the end, so no freeze. No intertitle.
- Subscribe + bell: red at about 7.5-8.75, SUBSCRIBED with the bell to about 12. It covers no text.
- Loop: crawl back to the grin. A clean cut, and a good loop (the cool face returns).

## HARD RULE
Clean. The stuffing of gumballs into his sailor top is plain slapstick and not suggestive. No POLICY hit.

## Takeaway test
I see "-1000 aura" in comments and know it means "that was so embarrassing". I can say "I tripped in front of everyone, minus a thousand aura." Yes.

## Top 3 fixes
1. visuals: drop the cross-cut and give the girls shot enough time to read. New segments: [329.6,331.4] (grin), [331.5,332.8] (the wide shot with the girls, 1.3 s), [362.3,371.8] (crawl), [373.3,375.5] (crawl). That is 14.8 s of footage, at least T = 14.64, and the crawl starts at about 3.1, under "Then the gum machine breaks". Then shorts-builder re-renders and reruns subscribe_anim.
2. shorts-builder/publisher: record "subscribe_at" in content/youtube/pd3-aura-v1.json.
3. scenario-writer (format-wide, optional): add a 1 s self-test before the closing question (e.g. "You trip in class. Aura: plus or minus?").

---
# Pass 2 (2026-10-18, re-render 13:00)
Segments [329.6,331.4] [331.5,332.8] [362.3,371.8] [373.3,375.5]. 1440x2560, 14.70 s. Meta has subscribe_at [7.4].
## Verdict: SOLVES (for this format) - ship
- 0-1.92 The smug grin by the gumball jar. 1.92-3.25 the sailors with the girls at the counter (1.3 s, now readable, under "in front of the girls"). 3.25-12.75 the gumball crawl (under "the gum machine breaks", "aura", "-1000 aura / that was so embarrassing"). 12.75-14.7 the crawl from the wider angle under "Ever lost aura like this?".
- The cross-cut to the car is gone, and there are no stray frames (every cut checked frame by frame). The 9.92 detector hit is motion inside the crawl shot. No freeze, no intertitle.
- Subscribe red at about 7.5-8.8, then SUBSCRIBED + bell. It covers no text. No spelled-out word. Policy clean: no POLICY hit. Loop: crawl back to the grin, clean.
