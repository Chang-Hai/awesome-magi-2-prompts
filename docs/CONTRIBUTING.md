# Contributing

Open a pull request with an original prompt, a correction, or an example with clear provenance. Describe what changed and how you checked it.

## Add or update a prompt

1. Edit [prompts.json](../prompts.json). Use a unique lowercase `slug` with words separated by hyphens. Keep a published slug stable because it is used in links.
2. Set `title`, `mode`, `duration_seconds`, and `aspect_ratio`. The catalog accepts `text-to-video`, `image-to-video`, and `reference-to-video`, with durations of 4–30 whole seconds.
3. List the required or optional references in `assets`, in the order the prompt mentions them. Keep `assets` empty for text-to-video. Explain what each reference controls and distinguish first or last frames from general references.
4. Write the copy-ready `prompt` and add practical `review` checks. For example, check that a switch click lands on contact and the product shape stays consistent at the cut.
5. Regenerate the Markdown and run the [local checks](LOCAL_DEVELOPMENT.md).

## Add a gallery entry

Edit [data/gallery.json](../data/gallery.json) and place any accompanying original or permitted image in [public/images](../public/images/). Use a relative path for a repository asset and a source URL for an externally hosted example.

- **Storyboard or illustration.** Identify the prompt it illustrates by slug and label the image as a storyboard or illustration. Put example input assets in their own roles so readers can tell what to supply.
- **Documented output.** Identify the exact prompt, input files in their original order and roles, model and provider, duration, aspect ratio, and any relevant settings such as audio or seed. Include the result link and the generation date. If the run used edited text or different inputs, record those differences with the result.
- **Official showcase.** Credit the publisher and link to the original clip or showcase. Keep its documented inputs and outputs together. Pair the clip with a repository prompt only if that exact prompt and its inputs produced the clip.

For media you upload, record the creator or source and the basis for redistributing it. Use assets you created or have permission to share. Use a source link if you only have permission to reference the work.
