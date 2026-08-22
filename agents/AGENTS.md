# Agents section: operating instructions

Everything under `agents/` is written, updated, and maintained by LLM agents with no per-article human review.
The human owner intervenes only through this file (rules, queue), through occasional edits to articles, or by disabling the scheduled task.
Any agent working in this section must follow this document end to end.
When these instructions conflict with general repo conventions, these instructions win for paths under `agents/`.

## Mission

Publish and maintain articles that help software engineers work with AI/LLMs in their daily practice.
The section is a living layer of the blog: articles track a moving landscape, so they are updated on evidence, not rewritten on a whim.

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

- One directory per article, lowercase kebab-case slug, containing `index.md`.
- Front matter fields: `title`, `created` (YYYY-MM-DD), `type: post`, `status` (`draft` while writing, `finished` when complete), `tags`, `readability`, `updated` (set when you revise), and `audience_notes` (folded `>`, for finished pieces).
- Mandatory tags on every article: `agent-curated`, `fully-ai-generated`, and `llm=<model-id>` for each model that wrote or edited the piece (e.g. `llm=glm-5.3`). Multiple `llm=` tags are allowed as models change over time; never remove one that a previous run added.
- Content tags are lowercase kebab-case and describe the topic.
- `readability: 3` is the default for this section (specialized reader).

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

Work items the owner has requested. Take them in order, highest first.

1. **Agentic coding tools landscape** - a maintained map of the agentic development environment landscape (harnesses, coding agents, orchestration layers), updated as the landscape shifts. Complements [the existing landscape article](../../the-agentic-development-environment-landscape/index.md) by tracking what exists now rather than arguing what it means.
2. **Model selection for coding tasks** - a maintained, opinionated guide to choosing models for coding, review, and agentic work, with the trade-offs that matter to practitioners.
3. **Context management patterns** - practical patterns for fitting large codebases and long tasks into context windows (chunking, retrieval, summarization, compaction), grounded in current tool behavior.

? for tom: the-agentic-development-environment-landscape/ exists on disk but is untracked, so linking it from agents/ would fail the CI link check; commit it (or tell me to link anyway) and I will cross-link the tracker both ways.

Questions for the owner are written as `? for tom:` bullets appended here; he answers in commits.

## Self-directed growth

Beyond the queue, you may start new articles when all of these hold:

- The topic is in scope and you can name the engineer whose day it improves.
- No existing article in the whole repository already covers it; search the corpus first.
- You can link the new article to at least two existing corpus articles in `## See also`.
- It passes the quality bar below.

Prefer updating an existing article over starting a new one.
Retire articles only when they are agent-created and superseded; if an article contains sentences you did not write and cannot find in `log.md` history, a human edited it, so never delete or revert those edits; flag it in the queue instead.

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
2. Read this file, `agents/log.md`, and the queue.
3. Work the queue top-down, then update existing articles whose facts may have moved (trackers first), then consider at most a couple of self-directed pieces.
4. Verify before committing: every internal link target exists on disk, every external URL fetched during this run, front matter parses, style rules respected.
5. Append one dated entry to `agents/log.md` (what changed and why).
6. Update `agents/_index.md` if the article list changed.
7. Commit scoped: stage only `agents/` (`git add agents/`). Commit message: short imperative, no prefixes, e.g. "Update agents model selection guide with August releases" or "Add agents article on context compaction".
8. Push. If rejected, `git pull --rebase --autostash origin master` once and push again; if it fails again, stop and log.

## Git guardrails

- Only ever create, modify, stage, or commit paths under `agents/`.
- Never `git add -A`, `git add .`, `git add *`, or stage by directory other than `agents/`.
- The working tree contains the owner's unrelated drafts; leave every path outside `agents/` untouched, including untracked ones.
- Never use `--force`, `--hard`, `reset`, `stash drop`, or branch creation; work on `master`.
- Never modify this file, `agents/_index.md`'s mission statement, or anything outside `agents/`; propose changes via `? for tom:` in the queue instead.

## Log

`agents/log.md` is append-only.
Every run appends one entry: date, articles touched, one line per change, model id.
The log is the audit trail that distinguishes agent changes from human edits; keep it accurate.
