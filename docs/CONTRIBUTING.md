# Contributing

Open a pull request with an original prompt, a correction, or an example with clear provenance. Describe what changed and how you checked it.

## Add or update a prompt

1. Edit [prompts.json](../prompts.json). Use a unique lowercase `slug` with words separated by hyphens. Keep a published slug stable because it is used in links.
2. Set `title`, `mode`, `duration_seconds`, and `aspect_ratio`. The catalog accepts `text-to-video`, `image-to-video`, and `reference-to-video`, with durations of 4–30 whole seconds.
3. List the required or optional references in `assets`, in the order the prompt mentions them. Keep `assets` empty for text-to-video. Explain what each reference controls and distinguish first or last frames from general references.
4. Write the copy-ready `prompt` and add practical `review` checks. For example, check that a switch click lands on contact and the product shape stays consistent at the cut.
5. Regenerate the Markdown and run the [local checks](LOCAL_DEVELOPMENT.md).

## Add a video case or a retest

Use the [video case issue form](https://github.com/Chang-Hai/awesome-magi-2-prompts/issues/new?template=video-case.yml) or update [data/video-cases.json](../data/video-cases.json). Include the creator, original source, published MP4 URL, model, and the distributed file’s measured duration, dimensions, frame rate, and audio-stream flag. Add viewing notes that someone can check against the clip.

- `official-demo` pairs a video with its source. Leave the prompt field empty when the exact text is unavailable.
- `published-prompt` includes the creator's actual prompt when its source permits sharing or quotation. State which inputs and settings the source discloses.
- `original-template` is a new or adapted recipe. Add it to the [prompt catalog](../prompts.json) or [templates](../TEMPLATES.md). Its storyboard may illustrate the brief.

For a cross-model run, follow the [retest protocol](RETEST.md) and record rejected or failed runs alongside accepted results. Link original footage where you have permission to reference it. For any uploaded video or image, document the source, creator, and permission to redistribute.

## Add a storyboard

Edit [data/gallery.json](../data/gallery.json) and place an original or permitted WebP in [public/images](../public/images/) with the same filename stem as the prompt slug. Describe it as a storyboard and supply alt text. A case may link a related exercise separately from the source’s actual inputs.
