# MAGI-2 Prompt Catalog

Pick a prompt and copy the text. Open its studio link, paste the prompt, and add the listed references if needed. Review the model, settings, and credit cost before generating.

These original starter prompts have not been rendered or benchmarked. The review checks describe what to look for if you run one.

[Return to the guide and video gallery](README.md)

## Browse by input mode

### Text to video

- [Rainy station departure in one take](#rain-platform-departure) · 10s · 21:9
- [Paper boat through two visual styles](#paper-boat-style-transition) · 14s · 16:9
- [An orchard crate lands on a wooden table](#orchard-crate-foley) · 6s · 16:9
- [Two lines of dialogue in a ferry ticket hall](#ferry-ticket-hall-dialogue) · 14s · 21:9

### Image to video

- [Running shoe reveal for a vertical ad](#running-shoe-vertical-reveal) · 8s · 9:16
- [A quiet tea packshot with room for copy](#tea-steam-packshot) · 6s · 4:3
- [Miniature bakery from a fixed first frame](#miniature-bakery-finish) · 8s · 1:1
- [Field recorder demo with a readable final frame](#field-recorder-close-up) · 9s · 3:4
- [An ink roller crosses a printmaking bench](#ink-roller-pass) · 8s · 3:4
- [A paper mobile turns beside a window](#paper-mobile-window) · 10s · 1:1

### Reference to video

- [Two-angle desk lamp launch](#two-angle-desk-lamp) · 12s · 16:9
- [Preserve a ceramic vase in a product orbit](#ceramic-vase-listing-fidelity) · 8s · 16:9
- [A tidepool fills and recedes](#tidepool-ebb-sound) · 18s · 4:3
- [A miniature stage lights up on cue](#miniature-stage-light-cue) · 24s · 9:16

<a name="running-shoe-vertical-reveal"></a>

## Running shoe reveal for a vertical ad

**Image to video** · 8s · 9:16

**References**

- A vertical product photo of your own unbranded running shoe

```text
Use the supplied product photo as the opening frame of an eight-second vertical ad. Keep the actual toe shape, lace pattern, upper color and sole profile. At 0–3 seconds, push in slowly from the original three-quarter view while a narrow band of window light travels across the upper. At 3–6 seconds, stop the push and let the light reveal the stitching and rubber tread. Hold the full shoe in frame at 6–8 seconds. Use faint room tone. Leave clear space above the shoe for a caption to be added in editing.
```

**Review the output**

- Compare the sole outline and count the lace eyelets in the first and last frames.
- Check that the shoe stays inside the vertical crop with space for a caption.

[Try this mode on GetMagi2](https://getmagi2.com/image-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=running-shoe-vertical-reveal)

<a name="two-angle-desk-lamp"></a>

## Two-angle desk lamp launch

**Reference to video** · 12s · 16:9

**References**

- Front and side photos of the same desk lamp
- A phone clip showing the intended lateral camera slide

```text
Use the front photo to match the cream shade and the side photo to match the hinge and cord. Take only the camera direction and pace from the reference video. From 0–5 seconds, slide left across the dark desk, keeping the complete lamp in frame. Cut at 5 seconds to a fixed view of the hinge. A hand flips the switch once at 7 seconds. Add a single small click as the lamp lights up. At 9 seconds cut back to a steady wide shot and hold the same pool of light through the end.
```

**Review the output**

- The front and side views show the same hinge and cord position.
- The click and the first visible change in brightness occur together.

[Try this mode on GetMagi2](https://getmagi2.com/reference-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=two-angle-desk-lamp)

<a name="rain-platform-departure"></a>

## Rainy station departure in one take

**Text to video** · 10s · 21:9

```text
One continuous wide shot from waist height at an empty above-ground train platform at blue hour. A stationary regional train waits on the right. Fine rain catches the platform lights and makes a pale reflection on the concrete. Keep the camera fixed. Sound begins with rain and an idle electric hum. At 4 seconds, add one short door tone and let the visible door finish closing. At 6 seconds, the train begins to roll right; the hum fades as it leaves frame. Hold on the empty platform for the final second.
```

**Review the output**

- Check that the door closes before the train begins moving.
- Look for steady platform geometry and listen for the order of tone, motion and fade.

[Try this mode on GetMagi2](https://getmagi2.com/text-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=rain-platform-departure)

<a name="tea-steam-packshot"></a>

## A quiet tea packshot with room for copy

**Image to video** · 6s · 4:3

**References**

- A still of your product package next to a glass of tea

```text
Begin with the supplied still of a tea box and a clear cup on a dark wooden counter. For the full six seconds, keep the camera fixed and the package front unchanged. A small ribbon of steam begins above the cup and drifts toward the window. A soft shadow moves very slowly across the background while the packaging stays readable. Use low kitchen room tone. Keep the upper right open for a price card added later.
```

**Review the output**

- Pause at 0, 3 and 6 seconds and check the shape and placement of the package and label.
- Check that steam never covers the area reserved for the price card.

[Try this mode on GetMagi2](https://getmagi2.com/image-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=tea-steam-packshot)

<a name="paper-boat-style-transition"></a>

## Paper boat through two visual styles

**Text to video** · 14s · 16:9

```text
A small orange paper boat drifts from left to right along a shallow gutter in one continuous low tracking shot. From 0–6 seconds, render the street as a soft hand-painted watercolor with loose washes. Between 6 and 9 seconds, the boat passes under a small wooden footbridge and the materials gradually resolve into felt and layered paper. From 9–14 seconds, maintain the same boat shape and motion in the new tactile miniature style. A soft trickle of water continues through the transition. Keep one direction of travel and no cuts.
```

**Review the output**

- The bow and orange paper fold match before and after the style change.
- Watch for an unintended cut or break in water ambience under the bridge.

[Try this mode on GetMagi2](https://getmagi2.com/text-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=paper-boat-style-transition)

<a name="miniature-bakery-finish"></a>

## Miniature bakery from a fixed first frame

**Image to video** · 8s · 1:1

**References**

- A still of a miniature bakery counter with three bread trays

```text
Keep the supplied miniature bakery as the starting frame. Use a slow, shallow camera tilt from the middle tray to a counter bell, keeping exactly three trays visible until the angle naturally crops them. Between 3 and 5 seconds, one paper bag is placed next to the bell by a single hand. Let the bag settle. At 6 seconds, the hand taps the bell once. Hold on the bell and bag for the rest of the square clip with very quiet room tone.
```

**Review the output**

- Check that the trays remain fixed in place as the camera tilts.
- Make sure the bell is tapped once and the ring follows the tap.

[Try this mode on GetMagi2](https://getmagi2.com/image-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=miniature-bakery-finish)

<a name="ceramic-vase-listing-fidelity"></a>

## Preserve a ceramic vase in a product orbit

**Reference to video** · 8s · 16:9

**References**

- Front and three-quarter photos of the same ceramic vase
- An optional short clip demonstrating the camera speed

```text
Use the front image for the vase's height, lip and blue glaze. Use the three-quarter image for the curve of the handle. Over eight seconds move the camera only far enough to reveal that handle and stop. The vase stays on the same white plinth under a soft key light throughout. Carry over only the speed of the optional motion reference. Avoid any change in glaze, rim width, handle join, or background shape. Use quiet gallery ambience.
```

**Review the output**

- Match the handle shape through the turn and count the visible handles before and after.
- Compare the rim width and glaze color to both reference photos.

[Try this mode on GetMagi2](https://getmagi2.com/reference-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=ceramic-vase-listing-fidelity)

<a name="field-recorder-close-up"></a>

## Field recorder demo with a readable final frame

**Image to video** · 9s · 3:4

**References**

- A clean product photo of your field recorder from a diagonal angle

```text
Start with the supplied diagonal view of a handheld field recorder on a slate surface. Hold the recorder still. For 0–4 seconds, bring the camera gently lower until the record button is near center. At 5 seconds, one index finger presses the button and the red indicator comes on. A soft tactile click lines up with the press. Hold the new angle with room below the device for a label added in post. Keep all ports and buttons in their original positions.
```

**Review the output**

- Look for any renamed controls or extra ports before using the clip commercially.
- Pause at the press and check that the indicator changes and the click is heard at that instant.

[Try this mode on GetMagi2](https://getmagi2.com/image-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=field-recorder-close-up)

<a name="orchard-crate-foley"></a>

## An orchard crate lands on a wooden table

**Text to video** · 6s · 16:9

```text
Make a six-second close-up of a farm worker setting a shallow crate of [fruit: green pears] onto an outdoor packing table. Begin with the crate held just above the table. At 1.5 seconds the crate touches down with one low wooden thump. One pear rolls a few centimeters and settles around 2.5 seconds. Move the camera slowly right, keeping the crate rim and the rolling pear in focus. Use distant birds and a low rustle of leaves for the rest of the sound bed.
```

**Review the output**

- The crate makes visible contact at 1.5 seconds within half a second, and the thump lands within 150 milliseconds of that contact.
- One pear rolls and stops before the fourth second, with the crate shape and the direction of the camera move consistent through the shot.

[Try this mode on GetMagi2](https://getmagi2.com/text-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=orchard-crate-foley)

<a name="ferry-ticket-hall-dialogue"></a>

## Two lines of dialogue in a ferry ticket hall

**Text to video** · 14s · 21:9

```text
Use one medium-wide shot of a traveler and a ticket clerk at a small ferry terminal. Between 0 and 3 seconds, hold both people in frame as the traveler looks up from a folded map. At 3 seconds the traveler asks, [line one: “Where do I board for the island?”]. Leave a brief pause. At about 7 seconds the clerk replies, [line two: “The second gate on your left.”]. Let the traveler nod after the answer. Ease the camera forward from 9 to 13 seconds. Keep a distant ventilation hum beneath the exchange, soft enough to hear both voices clearly.
```

**Review the output**

- Both lines are audible in the intended order, with a discernible pause between speakers.
- Each speaking voice matches the mouth movement of its speaker, and the listener keeps their mouth still during the other line.
- The nod follows the answer and both people stay in frame during the approach.

[Try this mode on GetMagi2](https://getmagi2.com/text-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=ferry-ticket-hall-dialogue)

<a name="ink-roller-pass"></a>

## An ink roller crosses a printmaking bench

**Image to video** · 8s · 3:4

**References**

- First-frame overhead photo of a clean roller, a blank printing plate, and a dab of ink in the intended color

```text
Start with the overhead arrangement in the supplied photograph. Keep the plate and the camera fixed. At 2 seconds, a hand takes the roller from the upper-left corner. At 3 seconds the roller meets the plate and makes a quiet tacky sound. From 3 to 6 seconds, make one slow pass toward the lower edge, spreading a thin layer of [ink color: deep blue]. Let the rolling sound continue while the roller is in contact. At 6 seconds lift the roller with a brief release sound, then hold on the inked plate.
```

**Review the output**

- The first frame uses the same camera angle and object positions as the reference photo.
- The rolling sound starts on contact and stops within 200 milliseconds of the lift.
- The roller makes one continuous pass, and the ink stays within the plate edges.

[Try this mode on GetMagi2](https://getmagi2.com/image-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=ink-roller-pass)

<a name="paper-mobile-window"></a>

## A paper mobile turns beside a window

**Image to video** · 10s · 1:1

**References**

- First-frame photo of an unbranded handmade paper mobile in the starting position
- Optional final-frame photo of the same mobile at the desired resting angle in the same light

```text
Start on the supplied image. Between 1 and 5 seconds, a draft slowly turns the handmade paper mobile until its largest shape is nearly face-on. Keep the camera fixed. At about 5 seconds, two pieces of [paper color: off-white] brush once, with a delicate papery rasp. Let the movement diminish over the next three seconds and settle into the supplied final composition if a final frame is present. Preserve the number of paper shapes and their thread positions. Use a low indoor room tone throughout.
```

**Review the output**

- Count the same number of paper pieces at the start, at maximum turn, and at rest.
- The rasp coincides with visible paper contact within 200 milliseconds.
- If a final-frame image is supplied, the largest piece has the same orientation in the ending composition.

[Try this mode on GetMagi2](https://getmagi2.com/image-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=paper-mobile-window)

<a name="tidepool-ebb-sound"></a>

## A tidepool fills and recedes

**Reference to video** · 18s · 4:3

**References**

- Image reference of the rock shelf showing the target composition and rock colors
- Motion reference clip of a shallow wave entering and receding from a small tidepool
- Field audio reference of soft wash, with one quiet bubbling tail

```text
Open on the rock shelf in the image reference at low tide. For the first four seconds, glide the camera a little forward, keeping the same arrangement of dark stones and [foreground detail: amber seaweed]. Use the motion reference to guide the water. At 5 seconds a shallow wave enters from the left, with the wash audible as the white edge reaches the stones. From 8 to 14 seconds let the water drain back in the same direction and reveal the seaweed. Use the field recording to guide the wash and a brief bubbling sound as the last water settles. Hold the final framing through 18 seconds.
```

**Review the output**

- The water enters from the left between 4 and 6 seconds, and the sound of the wash begins as it reaches the foreground stones.
- The same foreground stones stay in view as the water drains, with the foreground detail visible by 14 seconds.
- The bubbling tail follows the retreating wave and fades before the end.

[Try this mode on GetMagi2](https://getmagi2.com/reference-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=tidepool-ebb-sound)

<a name="miniature-stage-light-cue"></a>

## A miniature stage lights up on cue

**Reference to video** · 24s · 9:16

**References**

- Image reference of a handmade miniature stage and its pale blue curtain
- Image reference of the lighting operator's desk and its single rocker switch
- Motion reference clip of a slow camera rise from desk height to stage height
- Audio reference recording of the relay click and low ventilation hum

```text
Make a 24-second vertical scene at a miniature stage rehearsal. For 0 to 6 seconds, show the operator's hand near the single switch on the desk from the image. An adult offscreen says, [cue line: “Ready for the blue wash?”], at 4 seconds. At 7 seconds the hand flips the switch with one relay click like the audio reference. Show the pale blue stage light starting on that same beat. From 8 to 16 seconds follow the slow camera rise in the motion reference and reveal the curtain and the lit set from the stage image. At 17 seconds an adult with a different voice replies, [response line: “Hold that level.”]. Keep the set still from 19 seconds to the end, with a quiet ventilation hum beneath the dialogue.
```

**Review the output**

- The switch moves, the relay clicks, and the blue light comes on within a 250-millisecond window.
- Both spoken lines can be understood, in order, with the relay quieter than the dialogue.
- The rise reveals the miniature set without cutting, and the stage proportions and curtain color match the references at the end.

[Try this mode on GetMagi2](https://getmagi2.com/reference-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=miniature-stage-light-cue)
