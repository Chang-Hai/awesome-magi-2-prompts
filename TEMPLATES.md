# MAGI-2 Video Templates

Choose a format, replace the bracketed fields, and copy the block into the matching generation mode. The examples are original writing templates. To study real model outputs first, open the [video case library](CASES.md). Check the model, settings, and credit cost before generating.

| Format | Starting settings | Useful for |
| --- | --- | --- |
| [Continuous cinematic take](#continuous-cinematic-take) | Text to video · 10s · 21:9 | One action and one coherent camera move |
| [Product ad with mixed references](#product-ad-with-mixed-references) | Reference to video · 12s · 9:16 | Preserving a product across two angles |
| [A 30-second scene with planned cuts](#a-30-second-scene-with-planned-cuts) | Text to video · 30s · 16:9 | Timing a three-shot sequence |
| [Two-person dialogue and reactions](#two-person-dialogue-and-reactions) | Text to video · 14s · 16:9 | Speaker order, lip sync, and room tone |
| [Start and end on specific frames](#start-and-end-on-specific-frames) | Image to video · 8s · 16:9 | A defined opening and final composition |
| [A sound cue you can measure](#a-sound-cue-you-can-measure) | Reference to video · 6s · 4:3 | Synchronizing contact and sound |

## Continuous cinematic take

Use this when every part of the shot should feel like it belongs to the same place and moment. Give the camera one direction and the subject one main movement.

```text
Make a 10-second continuous wide shot at [location and time of day].
0–3s: establish [subject] from [height and angle]. Begin with [quiet ambience].
3–8s: the subject [one visible action]. Move the camera [one direction and pace] and keep [fixed landmark] in a consistent relationship to the subject.
8–10s: let the camera settle on [final framing]. Keep the same lighting and room tone throughout.
```

Check for unexpected cuts and for any landmark that jumps relative to the subject. If movement drifts, shorten the camera path on the next take. [Worked prompt](PROMPTS.md#rain-platform-departure) · [Try text to video](https://getmagi2.com/text-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=template_continuous_take)

## Product ad with mixed references

Use photos of your actual product variant. Give each reference a single job.

```text
Make a 12-second vertical ad for [product].
Use [front image] to guide [exact finish, label placement, and overall shape].
Use [side image] to guide [specific part visible at an angle].
Use [motion clip] to guide only [camera speed and direction].
0–4s: show the product from the front, then begin one slow camera move.
4–8s: cut to the product detail. At 6s, [one hand action] and one [sound cue] happen together.
8–12s: cut to the final product view and leave clean space at [position] for text added in editing.
```

Compare the product shape, logo, and number of visible parts across each cut. If label accuracy matters, check it at delivery size or add the approved label in post. [Worked prompt](PROMPTS.md#two-angle-desk-lamp) · [Try reference to video](https://getmagi2.com/reference-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=template_product_ad)

## A 30-second scene with planned cuts

Use this when the reveal depends on where each shot starts and finishes. Test the hardest cut or performance beat in a shorter version before spending on the full clip.

```text
Generate a 30-second scene in [location] with [subject description].
0–8s: [wide framing]. Establish [location and story question] with one visible action. Play [ambient sound].
At 8s: cut to [camera angle]. From 8–18s, [main action] happens in this order: [first] then [second]. At [exact second], [sound or spoken line] occurs when [visible action].
At 18s: cut to [reveal framing]. From 18–30s reveal [one concrete visual change]. Hold the last [number] seconds on [end image].
Maintain [specific wardrobe item or object geometry] and carry [ambient sound] across the cuts.
```

Find each actual cut on the exported timeline. Record its observed time, the shot before and after, and whether the intended action was already underway. [Official time-directed showcase](https://sand.ai/blog/magi-2#showcase) · [Try text to video](https://getmagi2.com/text-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=template_30_second_scene)

## Two-person dialogue and reactions

Keep both faces visible when you are testing speaker assignment. Give each line time to finish and preserve the pause before a reaction.

```text
Make a 14-second medium two-shot in [location]. Keep speaker A [position] and speaker B [position].
0–3s: both people [settle into the scene]. Use [quiet background sound].
At 3s: speaker A says “[short line]” in [language and delivery]. Speaker B looks at A and listens silently.
At 7s: speaker B answers “[short reply]” in the same language. Speaker A waits until the line finishes, then [small visible reaction].
9–14s: keep both faces visible and hold through the reaction. Keep ambience low and dialogue clear.
```

Review the spoken words, speaker order, and lips on a second pass. If the wrong face moves, keep framing fixed and simplify one cue instead of lengthening the dialogue. [Worked prompt](PROMPTS.md#ferry-ticket-hall-dialogue) · [Try text to video](https://getmagi2.com/text-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=template_dialogue)

## Start and end on specific frames

Use a supported first-and-last-frame mode when the starting and closing compositions matter. In some APIs this is separate from mixed references. Use similarly lit photos of the same subject and check the movement between them. [Higgsfield image-to-video settings](https://open.higgsfield.ai/models/sand/magi-2/image-to-video/api-reference)

```text
Begin on the supplied first frame and settle into the supplied ending view.
0–2s: hold the initial composition for a beat.
2–6s: [one small subject movement or camera move] leads from the first view into the second.
6–8s: hold the final composition. Keep [subject proportions, colors, and fixed background elements] consistent across the move.
Play [simple sound bed] beneath the motion.
```

Compare the ending framing and inspect the middle of the transition for newly invented parts. If the two images demand an abrupt spatial change, try a smaller transition or make the cut in editing. [Worked prompt](PROMPTS.md#paper-mobile-window) · [Try image to video](https://getmagi2.com/image-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=template_frames)

## A sound cue you can measure

Record a clean sound reference with some room tone. Choose an action whose contact frame is visible at the angle you plan to use.

```text
Make a six-second close-up of [object] on [surface], using [image] for its appearance.
0–2s: hold the camera still. Include only [quiet ambience].
At 2s: [hand or object] touches [visible surface]. Play a single [sound effect like the audio reference] on the frame where contact occurs.
2–6s: let [small consequence of the contact] settle. Return to the original room tone.
```

Find the contact frame and the start of the sound in your editor. Record the time difference. If you need the exact supplied recording, use it in the final edit. [Worked prompt](PROMPTS.md#orchard-crate-foley) · [Try reference to video](https://getmagi2.com/reference-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=template_sound_cue)
