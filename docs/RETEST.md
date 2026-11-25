# Retest a MAGI-2 video prompt

Use this protocol to compare MAGI-2 with Seedance or another model for a specific shot. Pick the acceptance checks before generating and retain failed or rejected attempts.

## Identify the starting point

| Baseline | What it records |
| --- | --- |
| `official-demo` | A video published by the model developer. Keep the original source URL and record which inputs and settings the developer disclosed. |
| `published-prompt` | A prompt supplied by a specific public source. Link the exact page or post. Record which references, settings, and output are available. |
| `original-template` | An original recipe from this repository or the contributor. Link the prompt or quote the exact text. A storyboard illustrates the brief. |

Call a run an exact rerun only when the original prompt, reference files, input roles, and requested settings are available and used. If anything is missing or changed, record the difference and describe the run as an adaptation.

## Match the requests

1. Save the exact prompt, the reference files in order, and what each controls. Use the same files on each model. Record the model variant, provider, date, mode, resolution, duration, aspect ratio, audio setting, and seed when available. Save any provider prompt rewrite separately.
2. Choose a duration, ratio, and resolution both providers accept. Record requested and measured duration. Start with a short clip to isolate an action or audio cue. Compare longer clips separately at the same supported length.
3. Keep audio settings comparable. Record whether a model can generate audio, take audio references, or only export a silent clip. Keep the visual comparison if audio support differs. Mark unavailable audio checks as such and report any score from a separate audio workflow on its own.
4. Pick the same attempt budget and stopping rule before the first run. Record queue time and render time separately where available. Keep the exact submitted settings and accessible evidence for each run.

## Review the video

- **Shot cuts.** Log the requested and observed timestamp for each cut. Choose a tolerance before the run and record missing or extra cuts.
- **Dialogue and foley.** Verify the words and speaker order. Review the mouth around a clear consonant or the hand at a visible impact. Compare when the event appears on screen with the corresponding audio onset. Record the offset and whether the sound was early or late.
- **Continuity.** Compare the subject, accessories, positions, and scene geometry at the start, middle, end, and both sides of each cut. In longer clips, log when drift first becomes visible and whether motion or ambient sound carries through each transition.

Keep the raw output for review where you have permission to share it. For each run, record accepted, completed but rejected, or failed, with the reason. Capture the provider error if there is no output.

## Record cost and submit findings

Count the actual billed amounts for all attempts, including billed retries and completed clips you discard. Record refunds and any costs that are unknown. Divide total net spend by the number of clips that met the acceptance checks. If none pass, report total spend and zero accepted clips. Keep credits and currency amounts separate unless you can document the conversion for the plan used.

Open a [video case issue](https://github.com/Chang-Hai/awesome-magi-2-prompts/issues/new?template=video-case.yml) with the source, inputs, output link or failure evidence, settings, and checks. Share materials you have permission to publish. See the [contribution guide](CONTRIBUTING.md) for provenance and gallery requirements.
