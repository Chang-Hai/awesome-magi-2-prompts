# Local development

Run these commands from the repository root with Python 3. The renderer uses the standard library. Running it uses no API keys or generation credits.

## Edit the source files

| Source | What to change |
| --- | --- |
| [prompts.json](../prompts.json) | Prompt text, suggested settings, input roles, and review checks |
| [data/gallery.json](../data/gallery.json) | Gallery entries, sources, and prompt associations |
| [data/README.template.md](../data/README.template.md) | Homepage layout and static copy |
| [public/images](../public/images/) | Images and storyboard [generation briefs](../public/images/README.md) |

## Render and validate

```bash
python3 scripts/render_prompts.py
python3 scripts/render_prompts.py --check
```

The first command writes [README.md](../README.md) and [PROMPTS.md](../PROMPTS.md). Review the diff and include regenerated files with the source changes. If a generated section needs a layout or copy change, update the renderer so later runs retain it.

The second command validates the catalog and checks generated files without rewriting them. CI runs the same check. If it fails after an edit, read the reported issue, correct the source or regenerate stale output, and rerun the check.

## Review the rendered result

Open both generated Markdown files in a preview. Follow new prompt anchors, source links, and local image paths. Check that thumbnails have descriptive labels and that any input, storyboard, or output is identified by role. These checks verify the documentation. A hosted generation requires a separate provider account and a run using the declared assets and settings.
