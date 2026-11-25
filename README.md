<a href="https://getmagi2.com/?utm_source=github&amp;utm_medium=referral&amp;utm_campaign=magi2_prompt_library&amp;utm_content=cover#tool-generator">
  <img src="public/images/magi-2-cover.webp" alt="MAGI-2 Prompt Library by GetMagi2, with concept scenes of a desk lamp, train platform, and paper boat" width="100%" />
</a>

# 🎬 Awesome MAGI-2 Prompts

[![GitHub stars](https://img.shields.io/github/stars/Chang-Hai/awesome-magi-2-prompts?style=social)](https://github.com/Chang-Hai/awesome-magi-2-prompts/stargazers)
[![Validate catalog](https://github.com/Chang-Hai/awesome-magi-2-prompts/actions/workflows/validate.yml/badge.svg)](https://github.com/Chang-Hai/awesome-magi-2-prompts/actions/workflows/validate.yml)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-2b7a5e)](docs/CONTRIBUTING.md)

A curated collection of MAGI-2 video prompts for Sand.ai’s model. Explore product demos, cinematic scenes, dialogue, foley, and mixed references. Each original recipe includes a prompt, suggested settings, reference inputs, and a checklist for reviewing the output.

**English** · [简体中文](README.zh-CN.md) · [日本語](README.ja-JP.md) · [Español](README.es-ES.md)

---

## 🌐 Browse the gallery and try MAGI-2

| On GitHub | In the GetMagi2 studio |
| --- | --- |
| Browse by use case and view storyboard stills. | Pick a generation mode and configure its available settings. |
| Copy the complete prompt and see which inputs it uses. | Paste the prompt and add your own photos, video, or audio if supported. |
| Watch source-attributed examples from Sand.ai. | Check the selected model and credit cost before generating. |

**[Browse web prompt ideas](https://getmagi2.com/?utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=web_gallery#tool-generator)** · **[Open the MAGI-2 studio](https://getmagi2.com/text-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=readme)**

### 🏷️ Browse by category

- [Product and e-commerce](#product-and-e-commerce) · Product reveals, consistent packaging, readable details, and short ad formats.
- [Cinematic scenes](#cinematic-scenes) · Slow camera moves, continuous atmosphere, and natural environmental sound.
- [Dialogue and sound](#dialogue-and-sound) · Two-person dialogue, timing a sound effect, and keeping ambience continuous through action.
- [Miniatures and animation](#miniatures-and-animation) · Handmade sets, style transitions, and controlled camera reveals.

**By input** · [Text to video](PROMPTS.md#text-to-video) · [Image to video](PROMPTS.md#image-to-video) · [Reference to video](PROMPTS.md#reference-to-video)

**By technique** · [Continuous shot](#rain-platform-departure) · [Style transition](#paper-boat-style-transition) · [First and last frames](#paper-mobile-window) · [Lip sync](#ferry-ticket-hall-dialogue) · [Foley timing](#orchard-crate-foley)

---

## 📖 Table of contents

- [What is MAGI-2?](#what-is-magi-2)
- [Library statistics](#library-statistics)
- [Featured prompts](#featured-prompts)
- [Official video gallery](#official-video-gallery)
- [All prompts](#all-prompts)
- [How to contribute](#how-to-contribute)

<a name="what-is-magi-2"></a>

## What is MAGI-2?

Sand.ai’s flagship generates video and synchronized sound in the same workflow. It supports up to 30 seconds of 1080p video at 25 fps. Mixed-reference mode can use images for appearance, video for motion, and audio for sound. First and last frames may be available in a separate image-to-video mode. The downloadable 114B MAGI-2 Preview has a separate pipeline for fixed 10-second clips. [Flagship release](https://sand.ai/blog/magi-2) · [Preview repository](https://github.com/SandAI-org/MAGI-2-preview) · [Frequently asked questions](docs/FAQ.md)

<a name="library-statistics"></a>

## 📊 Library statistics

<div align="center">

| Original prompts | Featured prompts | Official videos | Last updated |
| ---: | ---: | ---: | --- |
| 14 | 5 | 4 | 2026-11-25 |

</div>

The still images in the prompt cards are AI-generated storyboards created for this repository. They illustrate the brief. The [official video gallery](#official-video-gallery) contains separate MAGI-2 generation examples from Sand.ai.

<a name="featured-prompts"></a>

## ⭐ Featured prompts

<a name="two-angle-desk-lamp"></a>

### 1. Two-angle desk lamp launch

`Reference to video` · `12s` · `16:9` · `Product commercial` · `Sound cue`

**Description**

A short product spot that uses two photos to preserve the lamp’s appearance and a phone clip to guide the camera. The switch click lands when the light comes on.

**Prompt**

```text
Use the front photo to match the cream shade and the side photo to match the hinge and cord. Take only the camera direction and pace from the reference video. From 0–5 seconds, slide left across the dark desk, keeping the complete lamp in frame. Cut at 5 seconds to a fixed view of the hinge. A hand flips the switch once at 7 seconds. Add a single small click as the lamp lights up. At 9 seconds cut back to a steady wide shot and hold the same pool of light through the end.
```

**Storyboard preview**

<p align="center">
  <img src="public/images/two-angle-desk-lamp.webp" alt="A cream desk lamp casting warm light on a wooden desk" width="700" />
</p>

*AI-generated concept still illustrating the brief.*

**Inputs and output checks**

Upload:

- Front and side photos of the same desk lamp
- A phone clip showing the intended lateral camera slide

- The front and side views show the same hinge and cord position.
- The click and the first visible change in brightness occur together.

**Details** · GetMagi2 Editorial · Original prompt · English · 2026-11-25

**[Try reference to video on GetMagi2](https://getmagi2.com/reference-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=two-angle-desk-lamp)** · [Copy-ready catalog](PROMPTS.md#two-angle-desk-lamp)

---

<a name="rain-platform-departure"></a>

### 2. Rainy station departure in one take

`Text to video` · `10s` · `21:9` · `Cinematic` · `Continuous shot`

**Description**

A continuous blue-hour shot with a fixed camera. The door tone, train movement, and fading hum give the clip a clear sequence.

**Prompt**

```text
One continuous wide shot from waist height at an empty above-ground train platform at blue hour. A stationary regional train waits on the right. Fine rain catches the platform lights and makes a pale reflection on the concrete. Keep the camera fixed. Sound begins with rain and an idle electric hum. At 4 seconds, add one short door tone and let the visible door finish closing. At 6 seconds, the train begins to roll right; the hum fades as it leaves frame. Hold on the empty platform for the final second.
```

**Storyboard preview**

<p align="center">
  <img src="public/images/rain-platform-departure.webp" alt="A regional train stopped at a rain-slick platform at blue hour" width="700" />
</p>

*AI-generated concept still illustrating the brief.*

**Inputs and output checks**

- Check that the door closes before the train begins moving.
- Look for steady platform geometry and listen for the order of tone, motion and fade.

**Details** · GetMagi2 Editorial · Original prompt · English · 2026-11-25

**[Try text to video on GetMagi2](https://getmagi2.com/text-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=rain-platform-departure)** · [Copy-ready catalog](PROMPTS.md#rain-platform-departure)

---

<a name="ferry-ticket-hall-dialogue"></a>

### 3. Two lines of dialogue in a ferry ticket hall

`Text to video` · `14s` · `21:9` · `Dialogue` · `Lip sync`

**Description**

A short, two-person exchange with a pause and a visible reaction. Both faces stay in frame for checking lip sync and speaker order.

**Prompt**

```text
Use one medium-wide shot of a traveler and a ticket clerk at a small ferry terminal. Between 0 and 3 seconds, hold both people in frame as the traveler looks up from a folded map. At 3 seconds the traveler asks, [line one: “Where do I board for the island?”]. Leave a brief pause. At about 7 seconds the clerk replies, [line two: “The second gate on your left.”]. Let the traveler nod after the answer. Ease the camera forward from 9 to 13 seconds. Keep a distant ventilation hum beneath the exchange, soft enough to hear both voices clearly.
```

**Storyboard preview**

<p align="center">
  <img src="public/images/ferry-ticket-hall-dialogue.webp" alt="A traveler with a folded map speaking to a clerk inside a ferry terminal" width="700" />
</p>

*AI-generated concept still illustrating the brief.*

**Inputs and output checks**

- Both lines are audible in the intended order, with a discernible pause between speakers.
- Each speaking voice matches the mouth movement of its speaker, and the listener keeps their mouth still during the other line.
- The nod follows the answer and both people stay in frame during the approach.

**Details** · GetMagi2 Editorial · Original prompt · English · 2026-11-25

**[Try text to video on GetMagi2](https://getmagi2.com/text-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=ferry-ticket-hall-dialogue)** · [Copy-ready catalog](PROMPTS.md#ferry-ticket-hall-dialogue)

---

<a name="paper-boat-style-transition"></a>

### 4. Paper boat through two visual styles

`Text to video` · `14s` · `16:9` · `Animation` · `Style transition`

**Description**

One paper boat travels through a watercolor scene and into a handmade miniature. Its direction and the sound of the water carry through the style change.

**Prompt**

```text
A small orange paper boat drifts from left to right along a shallow gutter in one continuous low tracking shot. From 0–6 seconds, render the street as a soft hand-painted watercolor with loose washes. Between 6 and 9 seconds, the boat passes under a small wooden footbridge and the materials gradually resolve into felt and layered paper. From 9–14 seconds, maintain the same boat shape and motion in the new tactile miniature style. A soft trickle of water continues through the transition. Keep one direction of travel and no cuts.
```

**Storyboard preview**

<p align="center">
  <img src="public/images/paper-boat-style-transition.webp" alt="An orange paper boat beside a tiny bridge in a watercolor and paper landscape" width="700" />
</p>

*AI-generated concept still illustrating the brief.*

**Inputs and output checks**

- The bow and orange paper fold match before and after the style change.
- Watch for an unintended cut or break in water ambience under the bridge.

**Details** · GetMagi2 Editorial · Original prompt · English · 2026-11-25

**[Try text to video on GetMagi2](https://getmagi2.com/text-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=paper-boat-style-transition)** · [Copy-ready catalog](PROMPTS.md#paper-boat-style-transition)

---

<a name="tidepool-ebb-sound"></a>

### 5. A tidepool fills and recedes

`Reference to video` · `18s` · `4:3` · `Mixed references` · `Field sound`

**Description**

An image defines the rocks, a video shows the direction of the wave, and an audio reference guides the wash and its quiet bubbling tail.

**Prompt**

```text
Open on the rock shelf in the image reference at low tide. For the first four seconds, glide the camera a little forward, keeping the same arrangement of dark stones and [foreground detail: amber seaweed]. Use the motion reference to guide the water. At 5 seconds a shallow wave enters from the left, with the wash audible as the white edge reaches the stones. From 8 to 14 seconds let the water drain back in the same direction and reveal the seaweed. Use the field recording to guide the wash and a brief bubbling sound as the last water settles. Hold the final framing through 18 seconds.
```

**Storyboard preview**

<p align="center">
  <img src="public/images/tidepool-ebb-sound.webp" alt="A shallow wave washing over slate stones and amber seaweed in a tidepool" width="700" />
</p>

*AI-generated concept still illustrating the brief.*

**Inputs and output checks**

Upload:

- Image reference of the rock shelf showing the target composition and rock colors
- Motion reference clip of a shallow wave entering and receding from a small tidepool
- Field audio reference of soft wash, with one quiet bubbling tail

- The water enters from the left between 4 and 6 seconds, and the sound of the wash begins as it reaches the foreground stones.
- The same foreground stones stay in view as the water drains, with the foreground detail visible by 14 seconds.
- The bubbling tail follows the retreating wave and fades before the end.

**Details** · GetMagi2 Editorial · Original prompt · English · 2026-11-25

**[Try reference to video on GetMagi2](https://getmagi2.com/reference-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=tidepool-ebb-sound)** · [Copy-ready catalog](PROMPTS.md#tidepool-ebb-sound)

---

<a name="video-gallery"></a>
<a name="official-video-gallery"></a>

## 🎞️ Official video gallery

Published by Sand.ai in its [official MAGI-2 showcase](https://sand.ai/blog/magi-2#showcase). These videos open at their original source. The exact prompts for these clips were not published with the showcase. Related exercises in this repository are original examples.

### Through Five Art Styles

Follow the subject and camera through five different visual styles within a single continuous take.

**Source** · Sand.ai · November 24, 2026

**[Watch original MP4](https://static.magi.world/media/website/01f847c8f459fa2b2831796dade7fa9b72acdfe5f77538044d455973f07c6362.mp4)** · [Sand.ai showcase](https://sand.ai/blog/magi-2#showcase) · [Related original exercise](#paper-boat-style-transition)

### Into the Giant Flower World

Compare the character reference sheet with the wardrobe in close-ups, low angles, and wide shots across three environments.

**Source** · Sand.ai · November 24, 2026

**[Watch original MP4](https://static.magi.world/media/website/7e823798bc17774a51d5f9ef8ad1cf6b1db750058c7c80a24bde83a46d83debc.mp4)** · [Sand.ai showcase](https://sand.ai/blog/magi-2#showcase) · [Related original exercise](#two-angle-desk-lamp)

### Precision Timeline and Shot-Cut Control

Watch for the entry, action, and cuts that Sand.ai directed with a written timeline.

**Source** · Sand.ai · November 24, 2026

**[Watch original MP4](https://static.magi.world/media/website/173dba46280a4b05ae603bd9f5b43a1fed9239a815ff5db022381bdf93693018.mp4)** · [Sand.ai showcase](https://sand.ai/blog/magi-2#showcase) · [Related original exercise](#miniature-stage-light-cue)

### From Preview to MAGI-2

Sand.ai uses a source screen recording and a text instruction to change the scene, including a cursor action and a transition.

**Source** · Sand.ai · November 24, 2026

**[Watch original MP4](https://static.magi.world/media/website/4a6c7a224b68c5637bd2c1e6cd75d723a205f57cd75a52fbcbe684544dd14c38.mp4)** · [Sand.ai showcase](https://sand.ai/blog/magi-2#showcase)

---

<a name="all-prompts"></a>

## 📋 All prompts

<a name="product-and-e-commerce"></a>

### Product and e-commerce

Product reveals, consistent packaging, readable details, and short ad formats.

<a name="running-shoe-vertical-reveal"></a>

#### 6. Running shoe reveal for a vertical ad

`Image to video` · `8s` · `9:16` · `Vertical ad` · `Product photography`

**Description**

An eight-second vertical product reveal that keeps the shoe’s construction visible and reserves space for a caption.

**Prompt**

```text
Use the supplied product photo as the opening frame of an eight-second vertical ad. Keep the actual toe shape, lace pattern, upper color and sole profile. At 0–3 seconds, push in slowly from the original three-quarter view while a narrow band of window light travels across the upper. At 3–6 seconds, stop the push and let the light reveal the stitching and rubber tread. Hold the full shoe in frame at 6–8 seconds. Use faint room tone. Leave clear space above the shoe for a caption to be added in editing.
```

**Storyboard preview**

<p align="center">
  <img src="public/images/running-shoe-vertical-reveal.webp" alt="An unbranded teal running shoe on a concrete block" width="600" />
</p>

*AI-generated concept still illustrating the brief.*

**Inputs and output checks**

Upload:

- A vertical product photo of your own unbranded running shoe

- Compare the sole outline and count the lace eyelets in the first and last frames.
- Check that the shoe stays inside the vertical crop with space for a caption.

**Details** · GetMagi2 Editorial · Original prompt · English · 2026-11-25

**[Try image to video on GetMagi2](https://getmagi2.com/image-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=running-shoe-vertical-reveal)** · [Copy-ready catalog](PROMPTS.md#running-shoe-vertical-reveal)

**Featured** · [Two-angle desk lamp launch](#two-angle-desk-lamp)

<a name="tea-steam-packshot"></a>

#### 7. A quiet tea packshot with room for copy

`Image to video` · `6s` · `4:3` · `Packshot` · `Food and drink`

**Description**

A quiet product shot with controlled steam and gentle window light. The product stays fixed and the frame has room for sales copy.

**Prompt**

```text
Begin with the supplied still of a tea box and a clear cup on a dark wooden counter. For the full six seconds, keep the camera fixed and the package front unchanged. A small ribbon of steam begins above the cup and drifts toward the window. A soft shadow moves very slowly across the background while the packaging stays readable. Use low kitchen room tone. Keep the upper right open for a price card added later.
```

**Storyboard preview**

<p align="center">
  <img src="public/images/tea-steam-packshot.webp" alt="A clear glass of tea steaming next to dark packaging" width="600" />
</p>

*AI-generated concept still illustrating the brief.*

**Inputs and output checks**

Upload:

- A still of your product package next to a glass of tea

- Pause at 0, 3 and 6 seconds and check the shape and placement of the package and label.
- Check that steam never covers the area reserved for the price card.

**Details** · GetMagi2 Editorial · Original prompt · English · 2026-11-25

**[Try image to video on GetMagi2](https://getmagi2.com/image-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=tea-steam-packshot)** · [Copy-ready catalog](PROMPTS.md#tea-steam-packshot)

<a name="ceramic-vase-listing-fidelity"></a>

#### 8. Preserve a ceramic vase in a product orbit

`Reference to video` · `8s` · `16:9` · `E-commerce` · `Object consistency`

**Description**

A narrow camera orbit built around two views of the same vase. Use it to check whether the handle, rim, and glaze stay consistent across angles.

**Prompt**

```text
Use the front image for the vase's height, lip and blue glaze. Use the three-quarter image for the curve of the handle. Over eight seconds move the camera only far enough to reveal that handle and stop. The vase stays on the same white plinth under a soft key light throughout. Carry over only the speed of the optional motion reference. Avoid any change in glaze, rim width, handle join, or background shape. Use quiet gallery ambience.
```

**Storyboard preview**

<p align="center">
  <img src="public/images/ceramic-vase-listing-fidelity.webp" alt="A blue ceramic vase with one handle on a white gallery plinth" width="600" />
</p>

*AI-generated concept still illustrating the brief.*

**Inputs and output checks**

Upload:

- Front and three-quarter photos of the same ceramic vase
- An optional short clip demonstrating the camera speed

- Match the handle shape through the turn and count the visible handles before and after.
- Compare the rim width and glaze color to both reference photos.

**Details** · GetMagi2 Editorial · Original prompt · English · 2026-11-25

**[Try reference to video on GetMagi2](https://getmagi2.com/reference-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=ceramic-vase-listing-fidelity)** · [Copy-ready catalog](PROMPTS.md#ceramic-vase-listing-fidelity)

<a name="field-recorder-close-up"></a>

#### 9. Field recorder demo with a readable final frame

`Image to video` · `9s` · `3:4` · `Product demo` · `Macro`

**Description**

A short demonstration that shows a record button press, an indicator light, and a synchronized click. It reserves space for a caption.

**Prompt**

```text
Start with the supplied diagonal view of a handheld field recorder on a slate surface. Hold the recorder still. For 0–4 seconds, bring the camera gently lower until the record button is near center. At 5 seconds, one index finger presses the button and the red indicator comes on. A soft tactile click lines up with the press. Hold the new angle with room below the device for a label added in post. Keep all ports and buttons in their original positions.
```

**Storyboard preview**

<p align="center">
  <img src="public/images/field-recorder-close-up.webp" alt="A matte handheld field recorder with a red indicator on a slate surface" width="600" />
</p>

*AI-generated concept still illustrating the brief.*

**Inputs and output checks**

Upload:

- A clean product photo of your field recorder from a diagonal angle

- Look for any renamed controls or extra ports before using the clip commercially.
- Pause at the press and check that the indicator changes and the click is heard at that instant.

**Details** · GetMagi2 Editorial · Original prompt · English · 2026-11-25

**[Try image to video on GetMagi2](https://getmagi2.com/image-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=field-recorder-close-up)** · [Copy-ready catalog](PROMPTS.md#field-recorder-close-up)

---

<a name="cinematic-scenes"></a>

### Cinematic scenes

Slow camera moves, continuous atmosphere, and natural environmental sound.

**Featured** · [Rainy station departure in one take](#rain-platform-departure)

**Featured** · [A tidepool fills and recedes](#tidepool-ebb-sound)

---

<a name="dialogue-and-sound"></a>

### Dialogue and sound

Two-person dialogue, timing a sound effect, and keeping ambience continuous through action.

<a name="orchard-crate-foley"></a>

#### 10. An orchard crate lands on a wooden table

`Text to video` · `6s` · `16:9` · `Foley` · `Food and drink`

**Description**

A close shot built around one wooden thump and one rolling pear. It makes the synchronization point easy to see and hear.

**Prompt**

```text
Make a six-second close-up of a farm worker setting a shallow crate of [fruit: green pears] onto an outdoor packing table. Begin with the crate held just above the table. At 1.5 seconds the crate touches down with one low wooden thump. One pear rolls a few centimeters and settles around 2.5 seconds. Move the camera slowly right, keeping the crate rim and the rolling pear in focus. Use distant birds and a low rustle of leaves for the rest of the sound bed.
```

**Storyboard preview**

<p align="center">
  <img src="public/images/orchard-crate-foley.webp" alt="A wooden crate filled with green pears being set on an orchard packing table" width="600" />
</p>

*AI-generated concept still illustrating the brief.*

**Inputs and output checks**

- The crate makes visible contact at 1.5 seconds within half a second, and the thump lands within 150 milliseconds of that contact.
- One pear rolls and stops before the fourth second, with the crate shape and the direction of the camera move consistent through the shot.

**Details** · GetMagi2 Editorial · Original prompt · English · 2026-11-25

**[Try text to video on GetMagi2](https://getmagi2.com/text-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=orchard-crate-foley)** · [Copy-ready catalog](PROMPTS.md#orchard-crate-foley)

**Featured** · [Two lines of dialogue in a ferry ticket hall](#ferry-ticket-hall-dialogue)

<a name="ink-roller-pass"></a>

#### 11. An ink roller crosses a printmaking bench

`Image to video` · `8s` · `3:4` · `Art process` · `Foley`

**Description**

An overhead tabletop scene in which one roller makes a single timed pass. Its sound begins and ends with visible contact.

**Prompt**

```text
Start with the overhead arrangement in the supplied photograph. Keep the plate and the camera fixed. At 2 seconds, a hand takes the roller from the upper-left corner. At 3 seconds the roller meets the plate and makes a quiet tacky sound. From 3 to 6 seconds, make one slow pass toward the lower edge, spreading a thin layer of [ink color: deep blue]. Let the rolling sound continue while the roller is in contact. At 6 seconds lift the roller with a brief release sound, then hold on the inked plate.
```

**Storyboard preview**

<p align="center">
  <img src="public/images/ink-roller-pass.webp" alt="A printmaker moving a roller across a plate of blue ink" width="600" />
</p>

*AI-generated concept still illustrating the brief.*

**Inputs and output checks**

Upload:

- First-frame overhead photo of a clean roller, a blank printing plate, and a dab of ink in the intended color

- The first frame uses the same camera angle and object positions as the reference photo.
- The rolling sound starts on contact and stops within 200 milliseconds of the lift.
- The roller makes one continuous pass, and the ink stays within the plate edges.

**Details** · GetMagi2 Editorial · Original prompt · English · 2026-11-25

**[Try image to video on GetMagi2](https://getmagi2.com/image-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=ink-roller-pass)** · [Copy-ready catalog](PROMPTS.md#ink-roller-pass)

<a name="paper-mobile-window"></a>

#### 12. A paper mobile turns beside a window

`Image to video` · `10s` · `1:1` · `First and last frames` · `Soft motion`

**Description**

A slow movement exercise with countable paper shapes and one quiet contact sound. An optional end frame helps set the resting angle.

**Prompt**

```text
Start on the supplied image. Between 1 and 5 seconds, a draft slowly turns the handmade paper mobile until its largest shape is nearly face-on. Keep the camera fixed. At about 5 seconds, two pieces of [paper color: off-white] brush once, with a delicate papery rasp. Let the movement diminish over the next three seconds and settle into the supplied final composition if a final frame is present. Preserve the number of paper shapes and their thread positions. Use a low indoor room tone throughout.
```

**Storyboard preview**

<p align="center">
  <img src="public/images/paper-mobile-window.webp" alt="Off-white pieces of a handmade paper mobile suspended beside a window" width="600" />
</p>

*AI-generated concept still illustrating the brief.*

**Inputs and output checks**

Upload:

- First-frame photo of an unbranded handmade paper mobile in the starting position
- Optional final-frame photo of the same mobile at the desired resting angle in the same light

- Count the same number of paper pieces at the start, at maximum turn, and at rest.
- The rasp coincides with visible paper contact within 200 milliseconds.
- If a final-frame image is supplied, the largest piece has the same orientation in the ending composition.

**Details** · GetMagi2 Editorial · Original prompt · English · 2026-11-25

**[Try image to video on GetMagi2](https://getmagi2.com/image-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=paper-mobile-window)** · [Copy-ready catalog](PROMPTS.md#paper-mobile-window)

---

<a name="miniatures-and-animation"></a>

### Miniatures and animation

Handmade sets, style transitions, and controlled camera reveals.

**Featured** · [Paper boat through two visual styles](#paper-boat-style-transition)

<a name="miniature-bakery-finish"></a>

#### 13. Miniature bakery from a fixed first frame

`Image to video` · `8s` · `1:1` · `Miniature` · `Sound cue`

**Description**

A fixed starting scene in a miniature bakery, ending on a brass counter bell. A paper bag and the bell provide two simple timed actions.

**Prompt**

```text
Keep the supplied miniature bakery as the starting frame. Use a slow, shallow camera tilt from the middle tray to a counter bell, keeping exactly three trays visible until the angle naturally crops them. Between 3 and 5 seconds, one paper bag is placed next to the bell by a single hand. Let the bag settle. At 6 seconds, the hand taps the bell once. Hold on the bell and bag for the rest of the square clip with very quiet room tone.
```

**Storyboard preview**

<p align="center">
  <img src="public/images/miniature-bakery-finish.webp" alt="Miniature bread trays and a brass counter bell in a handmade bakery" width="600" />
</p>

*AI-generated concept still illustrating the brief.*

**Inputs and output checks**

Upload:

- A still of a miniature bakery counter with three bread trays

- Check that the trays remain fixed in place as the camera tilts.
- Make sure the bell is tapped once and the ring follows the tap.

**Details** · GetMagi2 Editorial · Original prompt · English · 2026-11-25

**[Try image to video on GetMagi2](https://getmagi2.com/image-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=miniature-bakery-finish)** · [Copy-ready catalog](PROMPTS.md#miniature-bakery-finish)

<a name="miniature-stage-light-cue"></a>

#### 14. A miniature stage lights up on cue

`Reference to video` · `24s` · `9:16` · `Miniature` · `Timing and cuts`

**Description**

A miniature theater rehearsal with a timed switch, a rising camera, and two short voice cues around the reveal.

**Prompt**

```text
Make a 24-second vertical scene at a miniature stage rehearsal. For 0 to 6 seconds, show the operator's hand near the single switch on the desk from the image. An adult offscreen says, [cue line: “Ready for the blue wash?”], at 4 seconds. At 7 seconds the hand flips the switch with one relay click like the audio reference. Show the pale blue stage light starting on that same beat. From 8 to 16 seconds follow the slow camera rise in the motion reference and reveal the curtain and the lit set from the stage image. At 17 seconds an adult with a different voice replies, [response line: “Hold that level.”]. Keep the set still from 19 seconds to the end, with a quiet ventilation hum beneath the dialogue.
```

**Storyboard preview**

<p align="center">
  <img src="public/images/miniature-stage-light-cue.webp" alt="A handmade miniature stage with a pale blue curtain and a small lighting console" width="600" />
</p>

*AI-generated concept still illustrating the brief.*

**Inputs and output checks**

Upload:

- Image reference of a handmade miniature stage and its pale blue curtain
- Image reference of the lighting operator's desk and its single rocker switch
- Motion reference clip of a slow camera rise from desk height to stage height
- Audio reference recording of the relay click and low ventilation hum

- The switch moves, the relay clicks, and the blue light comes on within a 250-millisecond window.
- Both spoken lines can be understood, in order, with the relay quieter than the dialogue.
- The rise reveals the miniature set without cutting, and the stage proportions and curtain color match the references at the end.

**Details** · GetMagi2 Editorial · Original prompt · English · 2026-11-25

**[Try reference to video on GetMagi2](https://getmagi2.com/reference-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=miniature-stage-light-cue)** · [Copy-ready catalog](PROMPTS.md#miniature-stage-light-cue)

---

<a name="how-to-contribute"></a>

## 🤝 How to contribute

Add an original prompt or a documented generation. Include the model version, settings, actual prompt and reference inputs, and the source or permission for every asset you submit. [Contribution guidelines](docs/CONTRIBUTING.md) · [Local development](docs/LOCAL_DEVELOPMENT.md) · [Machine-readable catalog](prompts.json)

Maintained by [GetMagi2](https://getmagi2.com/), an independent online studio and model guide. Sand.ai develops MAGI-2. Linked official videos are credited to and hosted by Sand.ai. [Repository layout reference](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts)
