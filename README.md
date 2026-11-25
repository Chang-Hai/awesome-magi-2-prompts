# Awesome MAGI-2 Prompts

A copy-ready prompt library for Sand.ai’s MAGI-2 video model. Start with product reveals, dialogue, sound effects, camera moves, or mixed reference media. Watch the official video examples to see what the model can do before you pick a prompt.

**[Browse the prompt library](PROMPTS.md) · [Watch official demo clips](#video-gallery) · [Try MAGI-2 online](https://getmagi2.com/text-to-video?model=magi-2&utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=readme) · [简体中文](README.zh-CN.md)**

Maintained by the team behind [GetMagi2](https://getmagi2.com/), an independent web studio and model guide. Sand.ai makes MAGI-2. GetMagi2’s studio uses paid credits for Sand.ai’s MAGI-2 model.

## Start with the right input

| What you have | Starting point | Example |
| --- | --- | --- |
| A scene in mind | Describe one visible action, one camera move, and one sound cue. | [Rainy station departure](PROMPTS.md#rain-platform-departure) |
| A photo that must set the shot | Use image-to-video and describe how the scene should move from that frame. | [Vertical running shoe reveal](PROMPTS.md#running-shoe-vertical-reveal) |
| Photos for appearance and footage for motion | Use reference-to-video. Tell the model which part of each file to follow. | [Two-angle desk lamp launch](PROMPTS.md#two-angle-desk-lamp) |
| A story beat that crosses a change in style | Specify the transition point and which object, motion, or sound should carry through it. | [Paper boat in two visual styles](PROMPTS.md#paper-boat-style-transition) |

Copy the prompt from its code block, use the corresponding studio link, and paste it into the prompt box. Add your own reference files if the prompt calls for them. The suggested length and aspect ratio are starting settings. Check whether your mode supports them and review the shown credit cost before you generate.

## Video gallery

Sand.ai published the four clips below in its [official MAGI-2 showcase](https://sand.ai/blog/magi-2#showcase). The MP4 links open the original videos. The repository prompts are independent exercises, with no paired output or reproduction claim.

| Official demo | What to watch | Source video |
| --- | --- | --- |
| Through Five Art Styles | Follow the subject and camera through consecutive visual styles in one take. | [Watch MP4](https://static.magi.world/media/website/01f847c8f459fa2b2831796dade7fa9b72acdfe5f77538044d455973f07c6362.mp4) |
| Into the Giant Flower World | Compare the character reference sheet with the wardrobe in close-ups, low angles, and wide shots across three environments. | [Watch MP4](https://static.magi.world/media/website/7e823798bc17774a51d5f9ef8ad1cf6b1db750058c7c80a24bde83a46d83debc.mp4) |
| Precision Timeline & Shot-Cut Control | Watch for specific actions starting at the requested points and the timing of the intervening cuts. | [Watch MP4](https://static.magi.world/media/website/173dba46280a4b05ae603bd9f5b43a1fed9239a815ff5db022381bdf93693018.mp4) |
| From “Preview” to “MAGI-2” | Watch a text-guided edit of a source screen recording, including a cursor action and a transition. | [Watch MP4](https://static.magi.world/media/website/4a6c7a224b68c5637bd2c1e6cd75d723a205f57cd75a52fbcbe684544dd14c38.mp4) |

## Before you generate

- **Pick the version.** Sand.ai’s hosted flagship supports up to 30 seconds of 1080p video at 25 fps with synchronized audio. Sand.ai’s downloadable 114B MAGI-2 Preview has a published pipeline that produces fixed 10-second clips. [Flagship release](https://sand.ai/blog/magi-2) · [Preview code and weights](https://github.com/SandAI-org/MAGI-2-preview)
- **Plan the reference roles.** The flagship supports up to 10 images, five video clips, and five audio clips in mixed-reference mode. Some providers expose first and last frames in a separate mode. Check their media limits before supplying assets. [Sand AI API reference](https://platform.sand.ai/docs/api-reference/) · [Higgsfield image-to-video reference](https://open.higgsfield.ai/models/sand/magi-2/image-to-video/api-reference)
- **Budget for retries.** Higgsfield listed US$0.08 per requested second for the 1080p MAGI-2 API as of November 25, 2026. That is US$0.40 for one five-second request and US$2.40 for one 30-second request at that rate. The GetMagi2 browser studio has its own credit pricing. [Higgsfield API pricing](https://open.higgsfield.ai/models/sand/magi-2/text-to-video/api-reference#4-pricing-and-limits) · [GetMagi2 pricing](https://getmagi2.com/pricing?utm_source=github&utm_medium=referral&utm_campaign=magi2_prompt_library&utm_content=pricing)
- **Check what you actually need.** Replay the first take with sound off to check objects, expressions, or camera motion. Then listen for the cue you named. If one element drifts, change that instruction or source asset before paying for a longer take.

## Contribute a prompt or a documented result

Open a pull request with an original prompt, the input mode, the suggested duration and aspect ratio, and the checks someone else can run. If you include a real output, list the model version, provider, exact prompt, reference inputs, and source or permission for each asset. Link to third-party clips at their original source.

`prompts.json` is the editable catalog. After an edit, refresh the rendered prompt page with `python3 scripts/render_prompts.py`. Run `python3 scripts/render_prompts.py --check` to verify that the catalog and page agree.
