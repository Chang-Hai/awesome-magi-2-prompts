# FAQ

## Which model do the prompts target?

The catalog targets Sand.ai’s hosted MAGI-2 flagship. Sand.ai describes synchronized picture and audio and output up to 30 seconds at 1080p and 25 fps. Check the chosen interface for the settings it exposes. [Sand.ai model announcement](https://sand.ai/blog/magi-2#capabilities)

## Which input mode should I pick?

Use text-to-video if you are starting from a description. Use image-to-video when a specific picture should define the opening frame. Some providers let you supply a target ending frame in that mode. Use reference-to-video when you want separate assets to guide appearance, motion, or sound. Higgsfield documents distinct schemas for image-to-video and mixed references. [First and last frame fields](https://open.higgsfield.ai/models/sand/magi-2/image-to-video/api-reference) · [Mixed reference fields](https://open.higgsfield.ai/models/sand/magi-2/reference-to-video/api-reference)

## How many references can I use?

Sand.ai describes a model capability of up to 10 images, five video clips, and five audio clips. The interface or API can impose additional limits on the number of parts, file size, and combined reference duration. Check those limits before preparing a request. [Model capabilities](https://sand.ai/blog/magi-2#capabilities) · [Sand.ai API request limits](https://platform.sand.ai/docs/create-generation/)

## How much does it cost to run a prompt?

Reading the catalog uses no credits. GetMagi2's browser studio uses credits for generation. Check the displayed credit cost and applicable plan before submitting. Higgsfield's separate MAGI-2 API listed US$0.08 per requested output second as of November 25, 2026, including generated audio. At that rate, five seconds costs US$0.40 and 30 seconds costs US$2.40. [GetMagi2 pricing](https://getmagi2.com/pricing) · [Higgsfield API pricing](https://open.higgsfield.ai/models/sand/magi-2/text-to-video/api-reference#4-pricing-and-limits)

## Can I run MAGI-2 locally?

Sand.ai released weights and inference code for its 114B MAGI-2 Preview. Its documented setup calls for eight NVIDIA Hopper GPUs, about 307 GB of checkpoints, and fixed 10-second outputs. Sand.ai announced a future weights release for the 480B flagship in its November 24, 2026 post. [Preview setup and weights](https://github.com/SandAI-org/MAGI-2-preview) · [Flagship announcement](https://sand.ai/blog/magi-2)

## What do the gallery images show?

Check the label on each entry. Storyboards illustrate possible framing or action. Official showcase clips are Sand.ai’s examples. A documented output links to the exact prompt, references, and generation settings used for that run. Use the review checklist to judge your own result.
