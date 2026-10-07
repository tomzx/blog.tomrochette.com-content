---
build:
  render: never
  list: never
  publishResources: false
---

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

- One directory per article, lowercase kebab-case slug, containing `index.md`, placed inside its category directory: `agents/<category>/<slug>/index.md`; the category directories are named for the sections (automated-research, harnesses, surfaces, orchestration, protocols, context-engines, skills, retrieval, memory, executions, hybrid-execution, code-review, evaluation-review, sandboxing, spec-driven-development, task-management, control-planes, assistant-runtimes, software-factory, session-analytics, people-and-publications), and each category's feature matrix and its own `_index.md` index page live in the same directory (see Category index pages).
- Essays, `model-provider-feature-matrix` (which has no category), and the control files stay at the section root.
- Front matter fields: `title`, `created` (YYYY-MM-DD), `status` (`draft` while writing, `finished` when complete), `tags`, `readability`, `updated` (set when you revise), and `audience_notes` (folded `>`, for finished pieces).
- Every article ends with `## Changes`, `## See also`, `## References`, in that order; `## Changes` is the article's dated changelog (see Writing rules).
- Any article whose `## Pricing` section states actual prices must also carry a separate `## Price history` section immediately after it, holding a table that tracks price changes over time: one row per dated change (columns: Date, Plan, Change, Source), oldest first, append-only, every row sourced. Seed the first row with the baseline price known when the article was created, append a row in the same run whenever a price or tier changes, and record that change in `## Changes`. Notes whose `## Pricing` section says pricing does not apply get no price history table.
- Never set a `type` field (in particular not `type: post`): articles in this section are section pages, not posts, and typing them as posts pulls them into the blog's post listings.
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
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=<model>, <content-tags>]
readability: 3
audience_notes: >
  <who this note is for and what they are assumed to know>
---

<One-sentence definition of the thing.>

## What it is

<2-4 sentences: what it does, surfaces, deployment model, license, who makes it.>

## Status

<Lifecycle: active, dormant, dead, pivoted, or superseded, with the evidence:
commit activity, stars or downloads as of a stated date, funding, shutdown or deprecation notice.>

## Strengths

- <what it does well>

## Cautions

- <limitations, lock-in, cost traps, preview churn>

## Pricing

<Tiers and licensing model, or why it does not apply.>

## Price history

<Include only when Pricing states actual prices; omit when pricing does not apply.>

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| YYYY-MM-DD | <plan> | <introduced at $X, or $X -> $Y> | <url> |

## Compared to

<2-3 direct alternatives and when to choose each.>

## Bottom line

Recommended for <X>. Not for <Y>.

## Changes

- YYYY-MM-DD - Created.

## See also

- <title linked per the Writing rules depths> - <replace with related notes and corpus articles, three to five>

## References

- <url> - <what it grounds>
```

Citation standards for notes:

- Minimum 5 sources, primary first (official docs, repo, pricing page, funding announcements).
- At least one critical or skeptical source when one exists; a missing community footprint is itself a signal worth stating.
- Every URL fetched during the run that cites it.
- Volatile numbers (stars, pricing, funding) carry "as of <date>".
- Dead tools keep their note, marked dead in `## Status`; deaths are information.

People-and-publications notes additionally carry a `## Top 5 recommended reading` section between `## Bottom line` and `## Changes`: the five pieces a new reader should start with, one per line, linked, each with a one-line why, best first.
The five are the person's own output (essays, posts, books, talks, interviews given, threads they answered); third-party coverage about them does not count.
For thin-record voices the five may lean on interviews and threads, and the section says so rather than padding.
Every URL in the section is fetched in the run that adds or edits it, and the note's `## Changes` records the section's addition or material revision.

## Comparison matrices

Every research index category has a companion feature matrix article (listed under Comparison matrices in [`agents/_index.md`](_index.md)) comparing the category's members on shared rows, every cell traced to its member note or its references.
**Column entries are sorted alphabetically by member title, case-insensitive, with no privileged position for founders, roots, or baseline conventions: when membership changes, re-sort the columns in the same run rather than appending or inserting in place.**
**A category's matrix is created in the same run the category is seeded, even when the category starts with a single member: the single column is the scaffold the next member extends, with the gap named in prose until then.**
Once a matrix exists, it never lags its category: any membership change, a new note, a move between categories, or a retirement, updates the matrix in the same run as the note that caused it, with the front matter `updated` field set to the revision date.
A matrix that lags its category is a defect, not a deferred task.
Matrices carry no verification preamble line ("Everything below was verified ..."); verification history lives in `## Changes`, and volatile cells carry their own "as of" qualifiers.
An unsorted matrix is the same defect; fixing the sort order belongs in the same commit as whatever surfaced it.

## Category index pages

Every category directory has its own index page at `agents/<category>/_index.md`, and that page is the canonical list of the section's entries; the section index links each category by its index page and lists no research notes itself.
A category index page is a section page, not an article: no `type` field, no `menu` field, no article tags, no See also, no References.
Its front matter: `showArticleList: false`, `title` (the category name), `created` (YYYY-MM-DD), `visible: true`, `status`, `tags: [agents, <category-tag>]`, `readability: 3`.
The page opens with one or two sentences on the category's scope, then lists its research notes alphabetically with one-line summaries (same format as the section index uses), then links the category's feature matrix.

**A category's index page is created in the same run the category is seeded, even with a single entry, and it never lags its category: any membership change updates the page's list in the same run as the note that caused it.**
A missing or stale category index page is a defect, the same as a lagging matrix.

Every category index page ends with `## Changes`, the section's append-only membership log: one `- YYYY-MM-DD - Added <Title>.` bullet per entry when it joins the category, one `- YYYY-MM-DD - Removed <Title>.` bullet when an entry is retired, and one `- YYYY-MM-DD - Moved <Title> to <Category>.` bullet when an entry changes category, oldest first, never deleted or rewritten.
When a page is created for a category that already holds entries, seed it with one `Added <Title>.` bullet per entry, each dated to that entry's `created` date.
The bullets are sourced from `agents/log.md` like article Changes; the log stays the audit trail, the page's Changes is the reader-facing summary.

## Writing rules

Inherit the blog's style, with these specifics:

- First person ("I"), one sentence per line in the source.
- No em-dashes; use commas or parentheses.
- Avoid the words "shape", "honest", "load bearing" unless no other word fits.
- Open with the thesis early, bolded with `**...**` within the first few paragraphs.
- Short, direct sentences; concrete statements over hedged abstractions.
- Structure with `##` headers that each advance the argument; bold the key insight of each section.
- Close with `## What to Do Next` when prescriptive, then `## Changes`, `## See also` (internal links), and `## References` (external sources), three to five items each for See also and References.
- `## Changes` is the article's append-only changelog: one `- YYYY-MM-DD - <what changed>` bullet per material change, oldest first, the first bullet records creation, sourced from `agents/log.md` (the log stays the full audit trail; Changes is the reader-facing summary). Corrections, status moves, pricing changes, added or removed facts, category moves, and matrix membership changes are changes; routine volatile-number refreshes are not. Append the bullet in the same run as the change it records; never delete or rewrite old bullets.
- Internal links: articles in the same category are `../<slug>/index.md`; articles in another category are `../<category>/<slug>/index.md`; a category index page is `<category>/_index.md` from the section index, `../../<category>/_index.md` from a section-root article (essays, the model-provider matrix), and `../_index.md` from a note in that category; section-root articles (essays, the model-provider matrix) are `../../<slug>/index.md`; the section index and control files are `../../` (for example `../../_index.md`, `../../AGENTS.md`); main corpus articles are `../../../<slug>/index.md`. Always verify the target directory exists before adding a link (CI fails on broken links).
- External links must be durable and canonical (official docs, Wikipedia for concepts); verify the URL fetches before citing it.
- All content must be compatible with CC BY-NC 4.0; quote sparingly, link generously.

## Article queue

The queue of articles to write lives in [`agents/queue.md`](queue.md).
Every item is standing: take them in order, highest first, and keep working all of them indefinitely; a pass over an item completes work, it does not close it.
Never mark a queue item done, strike it through, or remove it, and never treat a section, category, or article as complete.
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
- Trackers state their as-of date in the first paragraph as one short clause and update it when facts change; run-by-run verification logs ("Everything below was verified ...") stay out of prose and live in `## Changes`.
- If nothing is worth publishing today, do maintenance only (link checks, fact checks, pruning) and say so in the log.
There is no volume quota and no numeric cap; the quality bar is the only limit.

## Awesome list sources

Curated "awesome" directories whose entries overlap the notes this section covers are standing entrant sources, scanned every run alongside the owner's stars and the orchestrator directory.
Each category subagent scans the sources mapped to its category, and the cross-category subagent scans the broad sources that span categories.
A repository surfaced by a source is an entrant candidate and resolves in the run that surfaces it: a note if it clears the citation bar, an explicit logged rejection with reasons if it does not.
The list was compiled 2026-10-07 by searching GitHub for "awesome" repositories whose entries match existing notes; the refresh re-checks each source for reachability and relevance, and retires or replaces one that goes stale.

Broad sources, scanned by the cross-category subagent:

- [andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators) - orchestration, harnesses, and surfaces.
- [Agent-Analytics/awesome-multi-agent-orchestrators](https://github.com/Agent-Analytics/awesome-multi-agent-orchestrators) - orchestration and control planes.
- [ai-for-developers/awesome-ai-coding-tools](https://github.com/ai-for-developers/awesome-ai-coding-tools) - harnesses, surfaces, code review, task management, and model access.
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - harnesses, skills, protocols, and session analytics.
- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - orchestration, assistant runtimes, and hybrid execution.
- [slavakurilyak/awesome-ai-agents](https://github.com/slavakurilyak/awesome-ai-agents) - orchestration, memory, model access, and retrieval.

Category-specific sources:

- Context engines: [Meirtz/Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering).
- Control planes: [agentrust-io/awesome-ai-governance](https://github.com/agentrust-io/awesome-ai-governance).
- Evaluation and review, session analytics: [anhermon/awesome-agent-observability](https://github.com/anhermon/awesome-agent-observability).
- Memory: [TeleAI-UAGI/Awesome-Agent-Memory](https://github.com/TeleAI-UAGI/Awesome-Agent-Memory).
- Model access: [rafska/awesome-local-llm](https://github.com/rafska/awesome-local-llm).
- Orchestration: [kaushikb11/awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents).
- Protocols: [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers), [punkpeye/awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients), [insodimension/awesome-agent-protocols](https://github.com/insodimension/awesome-agent-protocols).
- Retrieval: [Yigtwxx/awesome-rag-production](https://github.com/Yigtwxx/awesome-rag-production), [Danielskry/Awesome-RAG](https://github.com/Danielskry/Awesome-RAG).
- Sandboxing: [arjan/awesome-agent-sandboxes](https://github.com/arjan/awesome-agent-sandboxes).
- Skills: [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills), [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills), [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents).
- Spec-driven development: [Engineering4AI/awesome-spec-driven-development](https://github.com/Engineering4AI/awesome-spec-driven-development).

Categories with no dedicated source (automated research, code review, executions, hybrid execution, software factory, surfaces, task management, trackers and leaderboards) rely on the broad sources above, and each refresh checks whether a credible dedicated list has appeared.

## Parallel section processing

Run each section as its own subagent so the refresh happens in parallel instead of one long serial pass.
A section here is one category directory, the unit the daily procedure already refreshes independently.
Dispatch one subagent per category, plus one subagent for the section-root content (essays, trackers, `model-provider-feature-matrix`, and the section index) and one subagent for the cross-category scan (the owner's GitHub stars, the curated orchestrator directory, and the broad awesome-list sources).
Each category subagent also scans the awesome-list sources mapped to its category in Awesome list sources.
Give every subagent the shared context it needs: this file, `agents/log.md`, `agents/queue.md`, and the current `agents/starred-checkpoint.txt`.
Confine each subagent to its own paths under `agents/` and have it return its proposed edits, its log lines, its `## Changes` bullets, and every entrant candidate it resolved or rejected.
The main run owns every shared file: it collects the subagent results, resolves cross-section effects (a category move touches two sections), updates `agents/_index.md`, appends the log entry, verifies, and commits.
Subagents propose and the main run writes the shared files once, so parallel work never races on `agents/log.md`, `agents/queue.md`, or `agents/_index.md`.

## Daily refresh procedure

A scheduled task runs this procedure once a day.

1. Sync: `git pull --rebase --autostash origin master`. If it fails, stop and record the blocker in `agents/log.md`; never force anything.
2. Read this file, `agents/log.md`, and `agents/queue.md`.
3. Refresh every category each run, all in parallel, one subagent per section (see Parallel section processing): across research notes, essays, trackers, matrices, and category index pages, check links, front matter, and as-of dates, and fix anything broken. Deep-refresh every category in the same run (no stalest ranking): re-verify status and volatile numbers, fix dead sources, scan for credible new entrants, re-check category fit (move or mark pivots), and keep every matrix matched to its category's membership and every category index page's entry list current, all re-verified in the same run. The scan includes the owner's GitHub stars: fetch `https://api.github.com/users/tomzx/starred?per_page=100&sort=created&direction=desc` with the `application/vnd.github.star+json` media type so each entry carries its `starred_at` timestamp, newest first, and cross-check the starred repositories against every category's membership, since a repository the owner stars is an entrant signal; use `gh api` (with `-H "Accept: application/vnd.github.star+json"`) when the unauthenticated rate limit bites. Page only until a `starred_at` is at or before the checkpoint in `agents/starred-checkpoint.txt` (a single ISO 8601 UTC line, written by the previous run), since the descending order guarantees everything past it was already cross-checked; fetch to the last page only when no checkpoint exists yet, and overwrite `agents/starred-checkpoint.txt` with the newest `starred_at` seen. A starred repository that fits a category resolves as an entrant candidate in the same run. The scan also covers every source in Awesome list sources (the curated directories whose entries overlap this section's notes, including [Awesome Multi-Agent Orchestrators](https://github.com/Agent-Analytics/awesome-multi-agent-orchestrators) at openorchestrators.org), each cross-checked against every category's membership the same way, since it is maintained by practitioners in this space: a category subagent scans its mapped sources and the cross-category subagent scans the broad ones. Every entrant candidate resolves in the run that surfaces it: a note if it clears the citation bar, an explicit logged rejection with reasons if it does not; a candidate carried across runs as "pending" is a defect. Then work every standing queue item, then consider at most one self-directed essay.
4. Verify before committing: every internal link target exists on disk, every external URL fetched during this run, front matter parses, style rules respected, and every feature matrix and category index page matches its category's current membership.
5. Append one dated entry to `agents/log.md` (what changed and why), and append the matching bullet to each touched article's `## Changes` section, and to the affected category index page's `## Changes` whenever membership changed.
6. Update `agents/_index.md` if the essay, tracker, or matrix lists changed; it links each category by its index page and lists no research notes itself, its essays and trackers list newest first, and its matrix list and category list are alphabetical, case-insensitive. Update the affected category's `_index.md` entry list and append its `## Changes` bullet in the same run whenever membership changed (see Category index pages), and update the affected category's feature matrix in the same run whenever membership changed (see Comparison matrices).
7. Commit scoped: stage only `agents/` (`git add agents/`). Commit message: short imperative, no prefixes, e.g. "Update agents model selection guide with August releases" or "Add agents article on context compaction".
8. Push. If rejected, `git pull --rebase --autostash origin master` once and push again; if it fails again, stop and log.

## Git guardrails

- Only ever create, modify, stage, or commit paths under `agents/`.
- Never `git add -A`, `git add .`, `git add *`, or stage by directory other than `agents/`.
- The working tree contains the owner's unrelated drafts; leave every path outside `agents/` untouched, including untracked ones.
- Never use `--force`, `--hard`, `reset`, `stash drop`, or branch creation; work on `master`.
- Never modify this file, `agents/_index.md`'s mission statement, or anything outside `agents/`; propose changes via `? for tom:` in `agents/queue.md` instead.
- `agents/queue.md` is the only agent-writable control file apart from `agents/starred-checkpoint.txt`, which the daily refresh overwrites with the newest `starred_at`: append `? for tom:` bullets, mark items done, never delete owner-written text.

## Log

`agents/log.md` is append-only.
Every run appends one entry: date, articles touched, one line per change, model id.
The log is the audit trail that distinguishes agent changes from human edits; keep it accurate.
