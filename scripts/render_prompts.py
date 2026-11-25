"""Render the GitHub gallery and copy-ready catalog from repository data."""
import argparse
import json
import re
from html import escape
from pathlib import Path
from urllib.parse import urlencode, urlsplit

ROOT = Path(__file__).resolve().parent.parent
MODES = {
    "text-to-video": "Text to video",
    "image-to-video": "Image to video",
    "reference-to-video": "Reference to video",
}
RATIOS = {"21:9", "16:9", "4:3", "1:1", "3:4", "9:16"}
FIELDS = {"slug", "title", "mode", "duration_seconds", "aspect_ratio", "assets", "prompt", "review"}
EVIDENCE = {"official-demo": "Official demo", "published-prompt": "Published prompt"}
CASE_FIELDS = {
    "slug", "title", "category", "model", "duration_seconds", "width", "height",
    "fps", "audio", "watch", "source", "credit", "evidence", "prompt", "description", "review",
}


def read_catalog():
    catalog = json.loads((ROOT / "prompts.json").read_text(encoding="utf-8"))
    if not isinstance(catalog, list) or not catalog:
        raise ValueError("prompts.json must contain a nonempty list of prompts")

    seen = set()
    for index, entry in enumerate(catalog, start=1):
        if not isinstance(entry, dict) or set(entry) != FIELDS:
            raise ValueError(f"Prompt {index} has unexpected or missing fields")

        slug = entry["slug"]
        if not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug) or slug in seen:
            raise ValueError(f"Prompt {index} must have a unique lowercase slug")
        seen.add(slug)

        mode = entry["mode"]
        if mode not in MODES or entry["aspect_ratio"] not in RATIOS:
            raise ValueError(f"{slug} has an unsupported mode or aspect ratio")
        seconds = entry["duration_seconds"]
        if type(seconds) is not int or not 4 <= seconds <= 30:
            raise ValueError(f"{slug} must use 4 to 30 whole seconds")

        for field in ("title", "prompt"):
            value = entry[field]
            if not isinstance(value, str) or not value.strip() or "```" in value:
                raise ValueError(f"{slug} must have a nonempty, copyable {field}")

        for field in ("assets", "review"):
            values = entry[field]
            if not isinstance(values, list) or any(not isinstance(value, str) or not value.strip() for value in values):
                raise ValueError(f"{slug} has an invalid {field} list")
        if not entry["review"] or bool(entry["assets"]) != (mode != "text-to-video"):
            raise ValueError(f"{slug} needs review criteria and the correct reference inputs")
    return catalog


def try_url(mode, slug):
    query = urlencode({
        "model": "magi-2",
        "utm_source": "github",
        "utm_medium": "referral",
        "utm_campaign": "magi2_prompt_library",
        "utm_content": slug,
    })
    return f"https://getmagi2.com/{mode}?{query}"


def render(catalog):
    lines = [
        "# MAGI-2 Prompt Catalog",
        "",
        "Pick a prompt and copy the text. Open its studio link, paste the prompt, and add the listed references if needed. Review the model, settings, and credit cost before generating.",
        "",
        "These original starter prompts have not been rendered or benchmarked. The review checks describe what to look for if you run one.",
        "",
        "[Return to the guide and video gallery](README.md)",
        "",
        "## Browse by input mode",
        "",
    ]
    for mode, label in MODES.items():
        lines.extend([f"### {label}", ""])
        for entry in catalog:
            if entry["mode"] == mode:
                lines.append(f"- [{entry['title']}](#{entry['slug']}) · {entry['duration_seconds']}s · {entry['aspect_ratio']}")
        lines.append("")

    for entry in catalog:
        slug = entry["slug"]
        mode = entry["mode"]
        lines.extend([
            f'<a name="{slug}"></a>',
            "",
            f"## {entry['title']}",
            "",
            f"**{MODES[mode]}** · {entry['duration_seconds']}s · {entry['aspect_ratio']}",
            "",
        ])
        if entry["assets"]:
            lines.extend(["**References**", ""])
            lines.extend(f"- {asset}" for asset in entry["assets"])
            lines.append("")

        lines.extend(["```text", entry["prompt"], "```", "", "**Review the output**", ""])
        lines.extend(f"- {check}" for check in entry["review"])
        lines.extend(["", f"[Try this mode on GetMagi2]({try_url(mode, slug)})", ""])
    return "\n".join(lines).rstrip() + "\n"


def read_gallery(catalog):
    gallery = json.loads((ROOT / "data" / "gallery.json").read_text(encoding="utf-8"))
    slugs = {entry["slug"] for entry in catalog}
    if set(gallery["cards"]) != slugs:
        raise ValueError("Every prompt needs exactly one gallery card")

    grouped = [slug for group in gallery["groups"] for slug in group["prompts"]]
    if len(grouped) != len(slugs) or set(grouped) != slugs:
        raise ValueError("Every prompt must appear in exactly one use-case group")

    featured = gallery["featured"]
    if not featured or len(featured) != len(set(featured)) or not set(featured) <= slugs:
        raise ValueError("Featured prompts must be unique catalog entries")

    for path in [gallery["cover"], *(f"public/images/{slug}.webp" for slug in slugs)]:
        if not (ROOT / path).is_file():
            raise ValueError(f"Missing gallery image {path}")

    return gallery


def read_video_cases(catalog):
    cases = json.loads((ROOT / "data" / "video-cases.json").read_text(encoding="utf-8"))
    if not isinstance(cases, list) or not cases:
        raise ValueError("video-cases.json must contain at least one attributed video")

    prompt_slugs = {entry["slug"] for entry in catalog}
    case_slugs = set()
    watch_links = set()
    for case in cases:
        if not isinstance(case, dict) or not CASE_FIELDS <= case.keys() <= (CASE_FIELDS | {"related_prompt"}):
            raise ValueError("A video case has missing or unexpected fields")

        slug = case["slug"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug) or slug in case_slugs or case["watch"] in watch_links:
            raise ValueError(f"Use a unique slug and video URL for {slug}")
        case_slugs.add(slug)
        watch_links.add(case["watch"])

        for name in ("source", "watch"):
            url = urlsplit(case[name])
            if url.scheme != "https" or not url.netloc:
                raise ValueError(f"{slug} needs a public HTTPS {name} URL")
        if any(type(case[key]) not in (int, float) or case[key] <= 0 for key in ("width", "height", "fps", "duration_seconds")):
            raise ValueError(f"{slug} needs measured dimensions, frame rate, and duration")
        if type(case["audio"]) is not bool or case["evidence"] not in EVIDENCE:
            raise ValueError(f"{slug} needs an audio-stream flag and an evidence label")
        if bool(case["prompt"]) != (case["evidence"] == "published-prompt"):
            raise ValueError(f"{slug} must only show the actual prompt when the source has published it")
        if "related_prompt" in case and case["related_prompt"] not in prompt_slugs:
            raise ValueError(f"Unknown related exercise {case['related_prompt']} for {slug}")
    return cases


def case_duration(case):
    return f"{case['duration_seconds']:.2f}".rstrip("0").rstrip(".") + "s"


def case_category(case):
    return case["category"].replace("-", " ").capitalize()


def render_video_index(cases, case_page=""):
    lines = [
        "| Video case | Use | Runtime | Evidence | Play |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for case in cases:
        slug = case["slug"]
        label = EVIDENCE[case["evidence"]]
        lines.append(
            f"| [{case['title']}]({case_page}#{slug}) | {case_category(case)} | "
            f"{case_duration(case)} | {label} | [▶ Watch Video]({case['watch']}) |"
        )
    return "\n".join(lines)


def render_casebook(cases):
    sections = [
        "# MAGI-2 Video Case Library",
        "[Back to the homepage](README.md) · [Original templates](TEMPLATES.md) · [Retest protocol](docs/RETEST.md)",
        "Each case links to Sand.ai’s source and the published MP4. Runtime, frame rate, dimensions, and audio-stream flags describe the published files. Source notes identify which model and inputs are documented.",
        render_video_index(cases),
    ]
    for case in cases:
        label = EVIDENCE[case["evidence"]]
        audio = "audio stream present" if case["audio"] else "no audio stream"
        detail = f"{case_duration(case)} · {case['width']} × {case['height']} · {case['fps']:g} fps · {audio}"
        card = [
            f'<a name="{case["slug"]}"></a>',
            "",
            f"## {case['title']}",
            "",
            f"**{label}** · {case['model']} · {case_category(case)}",
            "",
            f"**[▶ Watch Video]({case['watch']})** · [Original source]({case['source']}) · **Credit** {case['credit']}",
            "",
            detail,
            "",
            case["description"],
            "",
            "**What to watch for**",
            "",
            *(f"- {check}" for check in case["review"]),
            "",
        ]
        if case["prompt"]:
            card.extend(["**Input prompt quoted from the original source**", "", "```text", case["prompt"], "```", ""])
        else:
            card.extend(["**Input prompt** · Full text unavailable in the cited source.", ""])
        if related := case.get("related_prompt"):
            card.append(f"[Try a separate original exercise](PROMPTS.md#{related})")
        sections.append("\n".join(card).rstrip())
    return "\n\n".join(sections) + "\n"


def render_card(entry, metadata, number, updated, featured=False):
    slug = entry["slug"]
    mode = entry["mode"]
    width = 700 if featured else 600
    heading = "###" if featured else "####"
    tags = [MODES[mode], f"{entry['duration_seconds']}s", entry["aspect_ratio"], *metadata["tags"]]
    lines = [
        f'<a name="{slug}"></a>',
        "",
        f"{heading} {number}. {entry['title']}",
        "",
        " · ".join(f"`{tag}`" for tag in tags),
        "",
        "**Description**",
        "",
        metadata["description"],
        "",
        "**Prompt**",
        "",
        "```text",
        entry["prompt"],
        "```",
        "",
        "**Storyboard preview**",
        "",
        '<p align="center">',
        f'  <img src="public/images/{slug}.webp" alt="{escape(metadata["alt"], quote=True)}" width="{width}" />',
        "</p>",
        "",
        "*AI-generated concept still illustrating the brief.*",
        "",
        "**Inputs and output checks**",
        "",
    ]
    if entry["assets"]:
        lines.extend(["Upload:", "", *(f"- {asset}" for asset in entry["assets"]), ""])
    lines.extend(f"- {check}" for check in entry["review"])
    lines.extend([
        "",
        f"**Details** · GetMagi2 Editorial · Original prompt · English · {updated}",
        "",
        f"**[Try {MODES[mode].lower()} on GetMagi2]({try_url(mode, slug)})**"
        f" · [Copy-ready catalog](PROMPTS.md#{slug})",
    ])
    return "\n".join(lines)


def render_readme(catalog, gallery, cases):
    entries = {entry["slug"]: entry for entry in catalog}
    featured = gallery["featured"]
    groups = gallery["groups"]
    cards = gallery["cards"]
    updated = gallery["updated"]

    categories = "\n".join(f"- [{group['title']}](#{group['id']}) · {group['brief']}" for group in groups)
    featured_content = "\n\n---\n\n".join(
        render_card(entries[slug], cards[slug], index, updated, featured=True)
        for index, slug in enumerate(featured, start=1)
    )
    chapters = []
    number = len(featured)
    for group in groups:
        chapter = [f'<a name="{group["id"]}"></a>', f"### {group['title']}", group["brief"]]
        for slug in group["prompts"]:
            if slug in featured:
                chapter.append(f"**Featured** · [{entries[slug]['title']}](#{slug})")
            else:
                number += 1
                chapter.append(render_card(entries[slug], cards[slug], number, updated))
        chapters.append("\n\n".join(chapter))

    published_prompts = sum(case["evidence"] == "published-prompt" for case in cases)
    stats = "\n".join([
        "| Source-checked videos | Exact prompts from sources | Original prompts | Last updated |",
        "| ---: | ---: | ---: | --- |",
        f"| {len(cases)} | {published_prompts} | {len(catalog)} | {updated} |",
    ])
    sections = {
        "COVER": gallery["cover"],
        "CATEGORIES": categories,
        "STATS": stats,
        "FEATURED": featured_content,
        "VIDEO_INDEX": render_video_index(cases, "CASES.md"),
        "ALL_PROMPTS": "\n\n---\n\n".join(chapters),
    }
    template = (ROOT / "data" / "README.template.md").read_text(encoding="utf-8")
    return re.sub(r"\{\{([A-Z_]+)\}\}", lambda match: sections[match[1]], template)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify README.md, PROMPTS.md, and CASES.md match the data")
    args = parser.parse_args()
    catalog = read_catalog()
    gallery = read_gallery(catalog)
    cases = read_video_cases(catalog)
    outputs = {
        "README.md": render_readme(catalog, gallery, cases),
        "PROMPTS.md": render(catalog),
        "CASES.md": render_casebook(cases),
    }
    for name, markdown in outputs.items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != markdown:
                parser.exit(1, f"{name} is out of date. Run python3 scripts/render_prompts.py.\n")
        else:
            path.write_text(markdown, encoding="utf-8")
    verb = "Validated" if args.check else "Rendered"
    print(f"{verb} README.md, PROMPTS.md, and CASES.md for {len(catalog)} prompts and {len(cases)} videos.")


if __name__ == "__main__":
    main()
