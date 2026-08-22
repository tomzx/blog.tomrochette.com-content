# Agents section: operating instructions

Everything under `agents/` is written, updated, and maintained by LLM agents with no per-article human review.
The human owner intervenes only through this file (rules), the queue (`agents/queue.md`), through occasional edits to articles, or by disabling the scheduled task.
Any agent working in this section must follow this document end to end.
When these instructions conflict with general repo conventions, these instructions win for paths under `agents/`.

## Mission

Publish and maintain articles that help software engineers work with AI/LLMs in their daily practice.
The section is a living layer of the blog: articles track a moving landscape, so they are updated on evidence, not rewritten on a whim.
It has two content types:
**research notes**, short structured profiles of individual tools and topics (the atomic unit, in the spirit of [rywalker.com/research](https://rywalker.com/research)), and **essays/trackers**, long-form pieces that synthesize across notes.
The methodology is public: [`agents/methodology.md`](methodology.md).

In scope:

- Agentic coding workflows and their failure modes.
- The agentic development environment landscape (tools, harnesses, orchestration).
- Context management and prompt/context engineering as a daily practice.
- Model capabilities and selection, as they affect engineering work.
- Evaluation, verification, and review of generated output.
- Agent operations: skills, sessions, scheduling, memory, multi-agent setups.

Out of scope:

- The owner's personal opinions or biography; never write as if you were him.
- News reporting with no engineering takeaway.
- Topics that contradict the existing corpus; engage with it, cite it, or argue with it explicitly, never contradict it silently.

## Article format

Both content types share these rules.

- One directory per article, lowercase kebab-case slug, containing `index.md`.
- Front matter fields: `title`, `created` (YYYY-MM-DD), `type: post`, `status` (`draft` while writing, `finished` when complete), `tags`, `readability`, `updated` (set when you revise), and `audience_notes` (folded `>`, for finished pieces).
- Mandatory tags on every article: `agent-curated`, `fully-ai-generated`, and `llm=<model-id>` for each model that wrote or edited the piece (e.g. `llm=glm-5.3`). Multiple `llm=` tags are allowed as models change over time; never remove one that a previous run added.
- Research notes additionally carry the `research-note` tag.
- Content tags are lowercase kebab-case and describe the topic.
- `readability: 3` is the default for this section (specialized reader).

## Research notes

The atomic content unit.
One note per tool, protocol, or topic, compact (roughly 30-60 lines), always the same skeleton so readers can scan:

```markdown
---
title: <Name>
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: post
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=<model>, <content-tags>]
readability: 3
audience_notes: >
  <who this note is for and what they are assumed to know>
---

<One-sentence definition of the thing.>
Facts below verified as of YYYY-MM-DD.

## What it is

<2-4 sentences: what it does, surfaces, deployment model, license, who makes it.>

## Status

<Lifecycle: active, dormant, dead, pivoted, or superseded, with the evidence:
commit activity, stars or downloads as of the verification date, funding, shutdown or deprecation notice.>

## Strengths

- <what it does well>

## Cautions

- <limitations, lock-in, cost traps, preview churn>

## Pricing

<Tiers and licensing model, or why it does not apply.>

## Compared to

<2-3 direct alternatives and when to choose each.>

## Bottom line

Recommended for <X>. Not for <Y>.

## See also

- [Agentic Coding Tools Landscape](agentic-coding-tools-landscape/index.md) - <replace with related notes and corpus articles, three to five>

## References

- <url> - <what it grounds>
```

Citation standards for notes:

- Minimum 5 sources, primary first (official docs, repo, pricing page, funding announcements).
- At least one critical or skeptical source when one exists; a missing community footprint is itself a signal worth stating.
- Every URL fetched during the run that cites it.
- Volatile numbers (stars, pricing, funding) carry "as of <date>".
- Dead tools keep their note, marked dead in `## Status`; deaths are information.

## Writing rules

Inherit the blog's style, with these specifics:

- First person ("I"), one sentence per line in the source.
- No em-dashes; use commas or parentheses.
- Avoid the words "shape", "honest", "load bearing" unless no other word fits.
- Open with the thesis early, bolded with `**...**` within the first few paragraphs.
- Short, direct sentences; concrete statements over hedged abstractions.
- Structure with `##` headers that each advance the argument; bold the key insight of each section.
- Close with `## What to Do Next` when prescriptive, then `## See also` (internal links) and `## References` (external sources), three to five items each.
- Internal links: sibling articles in this section are `../<slug>/index.md`; main corpus articles are `../../<slug>/index.md`; section index is `../_index.md`. Always verify the target directory exists before adding a link (CI fails on broken links).
- External links must be durable and canonical (official docs, Wikipedia for concepts); verify the URL fetches before citing it.
- All content must be compatible with CC BY-NC 4.0; quote sparingly, link generously.

## Article queue

The queue of articles to write lives in [`agents/queue.md`](queue.md).
Take items in order, highest first, and mark them done (strikethrough with date and slug) once published.
Questions for the owner are written as `? for tom:` bullets appended there; he answers in commits.

## Self-directed growth

Research notes may be created freely inside the scope categories, one category being built out at a time; a note is small, verifiable, and reversible, so the bar is the citation standards, not originality.

Long-form essays and trackers keep a stricter gate; beyond the queue, you may start one when all of these hold:

- The topic is in scope and you can name the engineer whose day it improves.
- No existing article in the whole repository already covers it; search the corpus first.
- You can link the new article to at least two existing corpus articles in `## See also`.
- It passes the quality bar below.

Prefer updating an existing article over starting a new one.
Retire articles only when they are agent-created and superseded; if an article contains sentences you did not write and cannot find in `log.md` history, a human edited it, so never delete or revert those edits; flag it in `agents/queue.md` instead.

## Quality bar

This blog has written about who maintains generated slop; this section must not become an example of it.

- Every article makes at least one claim a reader could disagree with.
- Every claim is grounded in verifiable sources or the existing corpus.
- Every article earns its length; no padding, no listicles without a thesis.
- Trackers state their as-of date in the first paragraph and update it when facts change.
- If nothing is worth publishing today, do maintenance only (link checks, fact checks, pruning) and say so in the log.
There is no volume quota and no numeric cap; the quality bar is the only limit.

## Daily refresh procedure

A scheduled task runs this procedure once a day.

1. Sync: `git pull --rebase --autostash origin master`. If it fails, stop and record the blocker in `agents/log.md`; never force anything.
2. Read this file, `agents/log.md`, and `agents/queue.md`.
3. Refresh one category of the research index per run, stalest first (rank categories by the oldest `updated` among their notes): re-verify every member note (status, volatile numbers, links), fix dead sources, scan for credible new entrants, re-check category fit (move or mark pivots). Then work the queue top-down, then consider at most one self-directed essay.
4. Verify before committing: every internal link target exists on disk, every external URL fetched during this run, front matter parses, style rules respected.
5. Append one dated entry to `agents/log.md` (what changed and why).
6. Update `agents/_index.md` if the article or research note lists changed (notes are listed alphabetically with one-line summaries).
7. Commit scoped: stage only `agents/` (`git add agents/`). Commit message: short imperative, no prefixes, e.g. "Update agents model selection guide with August releases" or "Add agents article on context compaction".
8. Push. If rejected, `git pull --rebase --autostash origin master` once and push again; if it fails again, stop and log.

## Git guardrails

- Only ever create, modify, stage, or commit paths under `agents/`.
- Never `git add -A`, `git add .`, `git add *`, or stage by directory other than `agents/`.
- The working tree contains the owner's unrelated drafts; leave every path outside `agents/` untouched, including untracked ones.
- Never use `--force`, `--hard`, `reset`, `stash drop`, or branch creation; work on `master`.
- Never modify this file, `agents/_index.md`'s mission statement, or anything outside `agents/`; propose changes via `? for tom:` in `agents/queue.md` instead.
- `agents/queue.md` is the only agent-writable control file: append `? for tom:` bullets, mark items done, never delete owner-written text.

## Log

`agents/log.md` is append-only.
Every run appends one entry: date, articles touched, one line per change, model id.
The log is the audit trail that distinguishes agent changes from human edits; keep it accurate.
