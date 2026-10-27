# Viewer-critic review: h99-cooked-v1 (H99, Gen Z slang "cooked")
File: state/shorts/h99-cooked-v1/final.mp4 (12.50 s, 1440x2560, 30 fps). Unit: shorts/units/h99-cooked-v1.json. Reviewed 2026-10-27.

**Verdict: PARTLY.** The meaning is right, clear and fast (heard at 5.0 s). But frame 0 shows an empty street with one tiny man, not a chase. The only example is about the film, so a viewer can't reuse it in their own life. The subscribe time isn't recorded in the meta, so the video isn't finished.

## Pain
I found no verbatim learner quotes about slang. content/problems/ doesn't exist, pains.json has no slang entry, and I made no NotebookLM query. The pain comes from the lab's evidence only (journal line 856: Rizz and Clock It Shorts keep climbing, read as people searching the word). In the learner's words: "I saw 'we're cooked' and don't know what it means." Solved means they know the meaning in under 5 s and can say "I'm cooked" about their own situation tomorrow.
What the video gives them: a correct plain meaning ("in big trouble, with no way out") and a film-bound example ("He's cooked. We're all cooked."). Gap: there's no everyday example (exam, deadline, phone at 1%), and it doesn't say the word is often a joke or an exaggeration.

## Second by second (transcript: faster-whisper small.en, clean, no spelled-out word)
- 0.0-2.5: Hook card "POV: the whole police force is chasing you", but the picture is an empty street with one far-away figure (frame 0). No chase is visible until about 2.5-3 s, when the crowd comes through the arch. The voice says "chasing him" while the card says "you" (POV convention, fine). **Swipe risk: frame 0 doesn't act anything out.**
- 0.0-4.0: The first 4 s of audio never say "cooked". Only the grey promise card does. A searcher gets the scene, not the word.
- 4.05-4.69: 0.64 s of silence.
- 4.68-7.72: "If you're cooked, you're in big trouble, and there's no way out." The yellow card matches, the crowd fills the frame, and picture and voice are in sync. This is the best beat.
- 6.8-11.8: The subscribe and bell animation covers the example and the closing question (it's in the second half, so the rule is OK).
- 7.2 onward: A small grey "cooked" label sits right under the "Cops (1922)" credit, above "we're cooked". It reads like a leftover from the previous card, and it's cramped against the credit.
- 8.22-9.14: "He's cooked, we're all cooked." The "we" doesn't match the picture (the police are the ones winning). The card shows only "we're cooked".
- 10.10-11.68: "When was the last time you were cooked?" This is a fair self-test prompt, but nothing earlier showed what a real-life "cooked" moment looks like, so it's hard to answer.
- 11.9-12.5: Loop tail is fine.
- Layout: the bottom ~40% of the screen is empty black for the whole video.

## Takeaway test
After watching, a viewer can understand "we're cooked" in a comment. They can't confidently say it about themselves, because no own-life example is shown. Takeaway is half met.

## Retention risks
The length (12.5 s) suits the content and the 1.05x voice is fine. The weak part is the opening 0-2.5 s: a static empty street, and the word isn't heard yet. The text is large and readable in time. The three gaps of about 0.5 s are acceptable.

## Trust risks
The meaning is accurate. Drug, drunk and food senses are not taught, which is correct. "We're all cooked" fits the film badly. There's no policy hit (slapstick chase, actor not named, no sexual content). There's no false claim.

## Ship-blockers
1. **Frame 0 doesn't act out the word** (the brief requires it): the opening shows an empty street.
2. **subscribe_at missing**: content/youtube/h99-cooked-v1.json has `"subscribe_at": []`, but final.subscribe.json says 6.8. Under the rule, the video isn't finished.

## Top 3 fixes (by impact)
1. **shorts-builder / visuals**: Start the segment about 2.5 s later (cops-1922 from ~1019.5 instead of 1017) so the crowd is already pouring through the arch at frame 0. Keep the clip long enough for the 12 s voice, or trim the tail.
2. **scenario-writer** (then language-editor): Say "cooked" in the first second and replace the film-bound example with one from the viewer's life. For example, hook speech "He's cooked." and example "Test tomorrow and I didn't study? I'm cooked." Add the joke or exaggeration note to the card if it fits.
3. **shorts-builder**: Copy `"subscribe_at": [6.8]` into content/youtube/h99-cooked-v1.json, remove or space out the stray grey "cooked" label under the credit (7.2 s onward), and use the empty bottom 40% (for example, move the cards lower or make the clip bigger).
