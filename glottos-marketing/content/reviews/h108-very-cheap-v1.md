# Viewer-critic review: h108-very-cheap-v1 (lab H108: real mistake-fact at frame 0, Stop Saying "very X" container)

Reviewed 2026-10-26. File: state/shorts/h108-very-cheap-v1/final.mp4 (md5 0a10694a…, 1440x2560, 30 fps, 17.9 s, kokoro am_michael 1.05, no music). Meta content/youtube/h108-very-cheap-v1.json has "subscribe_at": [12.5]. Transcript: faster-whisper small.en, word timings. Frames: 14 frames 0-17.8 s, plus 0.0/0.1/0.2/0.3 s.
Pain evidence: I spent no NotebookLM query. A corpus grep found NO learner quote about "cheap" (only producer notes), so the pain below is the brief's and is NOT verbatim: "I say 'very cheap' / 'cheap' and don't know it can sound like low quality." Solved means that tomorrow I say "an affordable phone" or "an inexpensive gift" when I mean a good price, AND I know when "cheap" is still fine.

## Verdict: PARTLY
The hook is a real, correctly hedged mistake-fact, and the three words are right and usable. But about 9.6 of the 17.9 s are silence. The "bad quality" claim is never shown (there is no cheap-vs-affordable contrast), so I learn three synonyms, not the nuance the hook promised.

## Ship blockers
None hard.
- No word is spelled out. "Budget friendly" is heard as two whole words at 13.12 and 14.84.
- Subscribe pill at about 12.5-15 s, bottom-left, "SUBSCRIBED" plus bell by 13.5 s. The time is recorded in the meta.
- POLICY: none. No magnifying glass, no NotebookLM/Gemini watermark seen. The logo is the channel avatar.
- Language approved (hash 7a9bc28d…). The fact is hedged with "can".

## Second by second (heard / seen)
- 0.00: frame 0 shows "Very cheap" struck through in red, but NOT the fact line. "can sound like BAD quality" pops in at about 0.2 s (6 frames). The H108 variable ("mistake-fact at frame 0") is therefore only 95% true at frame 0. A thumbnail or first-frame grab shows just "~~Very cheap~~".
- 0.00-2.20: "Very cheap can sound like bad quality." Strong. This is my problem, and the screen matches the voice.
- 2.20-2.92 gap, then 2.92-3.74 "Say these instead.", then 3.74-4.94 a 1.2 s silent hold. This is the first swipe point.
- 4.94 "Affordable." / 5.14-6.08 silence / 6.08-7.34 "An affordable phone." The picture card appears only at about 6.5-7.0. At 5.5 the screen is headline-only on a busy word-wall background.
- 7.34-8.78: 1.44 s silent. Swipe point 2.
- 8.78 "Inexpensive." / 9.32-10.48 silence (again no picture at 8.3) / 10.48-11.66 "An inexpensive gift."
- 11.66-13.12: 1.46 s silent. Swipe point 3.
- 13.12 "Budget friendly." / 13.76-14.54 silence / 14.54-16.02 "A budget friendly hotel."
- 16.02-17.9: a 1.9 s silent tail. The loop frame (17.8) is the struck "Very cheap" without the fact line, which matches frame 0.
- Pictures: each one is a small watercolour card with its OWN sentence in tiny print ("Get the utility you need with an affordable phone." / "Show appreciation with a beautiful, inexpensive gift." / "Enjoy your trip by staying in a budget-friendly hotel."). That is ad-copy English, unreadable on a phone at Short speed, and it competes with the sub line just above it. The picture matches the words (phone, gift, hotel), but it adds no meaning.
- The background word-wall (affordable/inexpensive/budget-friendly in large, faint type) is noisy behind the headline. It is readable, but it is clutter.

## Takeaway test
I can say "an affordable phone" tomorrow. I CANNOT say when "cheap" is fine ("cheap flights" and "cheap tickets" are normal English) or what the "bad quality" sense looks like ("a cheap bag that broke in a week"). The hook raises that question and the video never answers it. There is also no self-test moment.

## Retention risks
- Silence: about 9.6 s of 17.9 s (0.7+1.2+0.94+1.44+1.16+1.46+0.78+1.88). Each word is said twice with a hold in between. Content would fit in about 11 s.
- The pictures arrive 1-1.5 s after the word, so the first half of every beat is a text-only screen.
- The arm test is confounded by the dead air, as in H103/H106. If the control has the same holds, the comparison is fair, but absolute retention will be low.

## Trust risks
- The red strike on "Very cheap" says "wrong", while the voice says "CAN sound". This is mild, and the hedge is correct.
- "BAD" in caps on the card is fine. Nothing is overclaimed.
- The embedded picture sentences are unnatural marketing copy ("Get the utility you need"). They are not wrong, but they are not the English we teach.

## Top 3 fixes (by impact)
1. shorts-builder: cut the holds to 0.3-0.4 s and the tail to 0.5 s (target about 12 s). Draw the fact line at frame 0 with the strike (no 0.2 s pop-in). Show the picture card on the same frame as the headline.
2. scenario-writer: add one contrast beat so the hook pays off, e.g. "Cheap bag = it breaks. Affordable bag = good price." plus "Cheap flights? That's fine." Optionally end with a 1 s self-test ("A ___ hotel?").
3. visuals: pictures without embedded sentences (or with only the 3-word collocation, readable size), so the card adds meaning, e.g. a broken cheap bag vs a nice affordable one for the contrast beat.
