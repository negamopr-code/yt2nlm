# Viewer-critic review: h103-very-tasty-v1 (lab H103 arm a: "Did you know" hook in Stop Saying "very tasty")

Reviewed 2026-10-25. File: state/shorts/h103-very-tasty-v1/final.mp4 (1440x2560, 30 fps, 23.7 s, Kokoro am_michael, no music). Unit: shorts/units/h103-very-tasty-v1.json. Meta: content/youtube/h103-very-tasty-v1.json DOES NOT EXIST.
Pain evidence: no NotebookLM query spent; content/problems does not exist. There is still no learner quote about overusing "very" on file (same gap as the h102 review), so the pain is the brief's: "I always say 'very tasty'; give me other words, fast." Solved = tomorrow I say "The soup is delicious", "It looks mouth-watering", "The cake is scrumptious".

## Verdict: PARTLY
The hook is my problem at frame 0 and the three words are right and usable, but the subscribe animation is missing, the run is 23.7 s with about 6 s of dead air, and the screen shows the payoff sentence while the voice is still telling the story line.

## Ship blockers
1. Subscribe + bell animation MISSING (frames at 2 fps from 11.5 s to the end: no pill, no bell), and there is no meta file to hold "subscribe_at". Owner: shorts-builder (shorts/subscribe_anim.py once in the second half, e.g. on the Scrumptious beat at about 15 s; create the meta with "subscribe_at").
Checked and clean: no word spelled letter by letter (whisper heard Delicious 4.22, Mouth watering 8.94, Scrumptious 14.36 whole); 1440 short side; no magnifying glass; no watermark; POLICY: none (the drooling face on the mouth-watering picture is a bit ugly, but it is not a policy issue).

## Second by second
- 0.0-2.5 "Did you know there are better words than very tasty?" The card is there at frame 0. I stop. Then the red strike on "very tasty" draws in, which says "wrong", while the language editor ruled that it is normal English (a small trust tension).
- 2.5-4.2 "Here are three" ... 0.8 s gap ... "Delicious". From 3.6 s the headline sits alone with no picture.
- 5.3-7.6 Voice: "Mia tries the soup." Screen: "The soup is delicious." The story line is never shown on screen, so the picture and the voice run out of step (the same happens at 9.9 s with the pie line and at 15.4 s with the cake line). The pictures repeat the example as small text and highlight the NOUN ("soup", "looks", "cake"), not the new word.
- 7.6-8.9, 13.4-14.4, 18.2-19.3: holds of 1.0-1.3 s of silence after each beat. These are the swipe points: by beat 2 I know the pattern.
- 8.9 "Mouth-watering": the picture is a cupcake or pastry, not a pie, and the face is smelling it while the line says "looks".
- 19.3-21.3 "Which word will you use? Comment yours." Then 2.4 s of silence. At about 22.3 s the hook card comes back already struck through, with "Here are 3" showing. Frame 0 is not struck, so the loop seam does not match.

## Takeaway test
I can name it: "The soup is delicious / It looks mouth-watering / The cake is scrumptious" instead of "very tasty". But nothing on screen asks me to try a word myself, and "scrumptious" is not marked as informal/playful.

## Retention and length
The video is 23.7 s against a 13-16 s target. About 6 s of the extra time is silence: the hook gap, the gap before the first word, three holds of about 1.1 s, and a 2.4 s tail. The spoken story lines add about 3 s more. With the holds at about 0.4 s and the tail at 0.5 s it comes to about 17 s with no words lost. As it stands, the arm-(a) result will measure the length and the dead air as much as the hook, so the hook variable is confounded.

## Top 3 fixes (by impact)
1. shorts-builder: add the subscribe animation and create the meta with subscribe_at; cut the post-beat holds and the end tail (target 16 s or less); make the loop card match frame 0 (no strike, no "Here are 3").
2. shorts-builder/scenario-writer: put the story "use" line on the card while it is spoken, then swap to the example sentence (or drop the spoken story line), so the screen matches the voice.
3. visuals: highlight the target word in the picture text (or remove the duplicate text from the pictures); make the pie a pie and drop the tongue-out drool face.
