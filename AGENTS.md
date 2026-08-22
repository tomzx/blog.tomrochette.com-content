---
build:
  render: never
  list: never
  publishResources: false
---

This repository holds the content for [blog.tomrochette.com](https://blog.tomrochette.com), a personal blog by Tom Rochette, a software developer generalist working in ML/DL/AI.

The audience is software engineers and technology/AI professionals. Most recent writing is about software engineering in the age of LLMs, but the archive spans AGI, machine learning, productivity, devops, and personal process.

## Repository layout

- Each article is a directory `<slug>/` containing `index.md`.
- Slugs are lowercase kebab-case. The slug is derived from the title (spaces and punctuation become `-`).
- Special multi-article sections live in their own directories: `agi/`, `machine-learning/`, `problems/`, `processes/`, `questions/`, `books/`, `principles/`, `papers/`, `research/`.
- Root files: `_index.md` (home), `archives.md`, `404.md`, `template.md`.
- Helper script: `promote-article.py`. (The PHP scripts in the root are legacy and should not be relied on.)

## Agent-maintained section

`agents/` is an experiment: content written and curated entirely by LLM agents, refreshed daily by a scheduled task, published without per-article human review. Treat everything in it as AI-generated (it carries its own mandatory disclosure tags). Its rules live in [`agents/AGENTS.md`](agents/AGENTS.md); when working under `agents/`, those instructions take precedence over this file. Human edits to that section are allowed and must not be reverted by agents.

## Creating a new article

Create a directory named after the slug (lowercase kebab-case, derived from the title with spaces and punctuation becoming `-`), then add an `index.md` inside it based on `template.md`. Set the `title`, the `created` date to today, leave `status: draft`, and fill in the remaining front matter per below.

For book notes, do the same under `books/<author-title-slug>/index.md` and append an entry to `books/index.md`.

## Front matter

Every article starts with a YAML block delimited by `---`. Fields:

- `title:` the title, quoted if it contains a colon or special characters.
- `created:` `YYYY-MM-DD` date.
- `type: post`
- `status:` one of `draft`, `in progress`, `finished`. New articles start as `draft`; flip to `finished` only when the piece is complete.
- `tags:` flat array of lowercase kebab-case tags, e.g. `[ai, software-engineering, llm]`. Content tags describe the topic.
- `readability:` integer on the 0-5 scale documented in `readability-index/index.md` (0 personal notes, 1 cryptic, 3 specialized/expert, 5 general audience). Pick the value that matches the intended reader, not the current draft quality.
- `audience_notes:` (optional but preferred for finished pieces) a folded scalar (`>`) describing the assumed reader and what they are expected to already know.

### AI disclosure tags (mandatory when AI is involved)

Per `written-by/index.md`, articles touched by AI must carry the appropriate tag so authorship stays transparent:

- `partially-ai-generated` for any AI-written or AI-edited sentences.
- `fully-ai-generated` when all content is AI-generated.
- `ai-feedback` when AI provided editing feedback.
- `llm=<model>` for each model involved, e.g. `llm=glm-5.2`. Multiple are allowed.

Untagged content is assumed fully human-written.

## Writing style

These conventions are derived from the published essays and must be followed for new and edited content.

- Write in first person ("I").
- One sentence per line in the source. This keeps diffs clean and is how every recent article is formatted.
- No em-dashes. Use commas or parentheses instead.
- Avoid the terms "shape", "honest", and "load bearing" unless they are the most precise word available. These have been actively removed from the corpus.
- Open with the thesis early. Most essays bold the central claim with `**...**` within the first few paragraphs.
- Use short, direct sentences. Prefer concrete statements over hedged abstractions.
- Structure with `##` section headers that each advance the argument. Bold the key insight of each section.
- Close with an actionable section (often `## What to Do Next`) when the piece is prescriptive.
- Be opinionated and specific; this is a personal blog, not documentation.

## Links

### Internal links (to other blog articles)

Use relative paths to the target's `index.md`, with `../` to escape the current article directory:

```
[Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md)
```

Always verify the target directory exists before adding a link; broken links fail CI.

### External links

Use inline markdown. Prefer durable, canonical sources (Wikipedia for concepts, official docs for tools). Include a short trailing description when the link text alone is not self-explanatory.

## End-of-article sections

Finished essays conventionally close with some combination of:

- `## See also` - internal links to related articles, each as a list item with a `- ` dash, a relative link, and a one-line explanation of the connection (why a reader of this piece would want the other).
- `## References` - external sources, same list format with a dash, the link, and a one-line note on what the source grounds.

Aim for three to five items in each section. The "See also" web is what keeps readers on site and is treated as part of the writing, not an afterthought.

## Linting and verification

Before considering an article done:

- Confirm every internal link target resolves.
- Confirm the front matter is complete and valid YAML.

CI (`.github/workflows/verify-content.yml`) runs a link check on every push, so broken internal links will fail the build.

## Commit messages

Follow the existing style: short, imperative, no conventional-commit prefixes. 

## Content license

All content is licensed under [Creative Commons Attribution-NonCommercial 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Do not introduce content that is incompatible with this license.
