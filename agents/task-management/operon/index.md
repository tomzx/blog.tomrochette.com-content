---
title: Operon
created: 2026-10-08
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, task-management, obsidian, markdown, local-first, gpl, multi-agent]
readability: 3
audience_notes: >
  Engineers who live in Obsidian and want agent work tracked in the same vault as their notes, under a write contract safer than raw file edits.
  Assumes you know what an Obsidian plugin is and what JSONL is.
---

Operon is a GPL-3.0 Obsidian plugin that turns a vault's scattered checkboxes and notes into one indexed task system for humans and agents: tasks stay Markdown, every task carries a durable `operonId`, and agent writes land only through previewed, receipted plans issued by its own runtime.

**The tracker inside the knowledge base is the differentiator, and the sealed preview-and-apply mutation gateway is the strongest agent-write contract in this category; nobody else here makes the agent's edit a verified plan with a receipt.**

## What it is

An Obsidian plugin (TypeScript, 1,060 commits) with a companion CLI (`@stratejya/operon-cli`, also GPL-3.0) and a 133-guide documentation site at [operon.cc](https://operon.cc).
Tasks remain Markdown in two forms: inline checkbox lines carrying `{{key:: value}}` containers, and file tasks with frontmatter, unified by one index keyed on `operonId` so the same task moves through Table, Calendar, Kanban, filters, recurrence, reminders, and time tracking without duplication.
Agent access runs through the Agent Runtime: `operon-cli` with typed requests or persistent JSONL sessions for scripts and agents, an in-process Developer API for other Obsidian plugins, and a Property Catalog that exposes the vault's own field names so an agent uses your conventions instead of guessing them.
Every write goes through the Mutation Gateway's preview-to-apply: the runtime computes what a change would do, seals that plan, applies only that plan, and returns receipts with postflight verification; direct Markdown editing stays supported as the unversioned path.
The hasanyilmaz identity maintains it in ten interface languages.

## Status

Active and shipping steadily.
As of 2026-10-08: 250 stars, 24 forks, 4 watchers, 7 open issues, 1 open pull request, created 2026-05-19, pushed 2026-10-06, latest release 3.12.0 on 2026-10-06 (after 3.11.0 on 2026-10-01 and 3.10.2 on 2026-09-28), 362 npm downloads last month for `@stratejya/operon-cli`, GPL-3.0 on both plugin and CLI.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=hasanyilmaz/operon&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=hasanyilmaz/operon&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=hasanyilmaz/operon&type=date&legend=top-left" />
</picture>

**The community footprint is the weak signal: an HN search for Operon and Obsidian returns zero hits and this run's searches found no independent coverage, so the 250 stars rest on the project's own growth curve.**
macOS is supported, native Linux and Windows 11 are public beta, WSL is unsupported, and the Runtime lives inside a running Obsidian process, so nothing works headless.

## Strengths

- Tasks live where the human already works; the vault is the store and the notes are the context, with no second place to reconcile.
- The sealed preview-and-apply write path with receipts and postflight verification is verification discipline the rest of this category leaves to agent discretion.
- The Property Catalog and key mappings mean an agent reads the vault's canonical vocabulary, not guessed YAML conventions.
- Inline and file tasks convert both ways with identity preserved, so a task can grow into a note and shrink back without losing its record.

## Cautions

- GPL-3.0 on both plugin and CLI, which triggers the corporate policy reviews this category's MIT members do not.
- No headless mode: the runtime requires a running Obsidian, so a server-side agent fleet cannot touch the tracker while the human is away.
- One maintainer identity carries a 133-guide API surface, a bus-factor concentration It's a Plan shares and the repo-local tools do not.
- The zero-coverage signal above: nothing independent corroborates the adoption numbers yet.

## Pricing

Free and open source under GPL-3.0 (plugin and CLI).
No paid tier or hosted service exists.

## Compared to

- [Backlog.md](../backlog-md/index.md): both keep tasks as Markdown; Backlog.md lives in the project repository and gates on human review, Operon lives in the knowledge vault and gates on receipted plans.
- [beads](../beads/index.md): repo-local graph state for coding agents sharing a queue, versus a vault-local task system for humans and agents working side by side.
- [It's a Plan](../its-a-plan/index.md): both give agents structured slots; It's a Plan is a separate self-hosted server platform, Operon is inside the note-taking app.

## Bottom line

**Recommended for Obsidian-based engineers who want agent work inside their vault and accept a single-maintainer plugin plus a running-Obsidian dependency.**
Not for server-side fleets (no headless runtime) or teams that need a standalone tracker with a vendor to escalate to.
My disagreeable claim: receipted, previewed writes are a bigger agent-safety advance than this category has credited, and most tracker integrations are prompt conventions by comparison.

## Changes

- 2026-10-08 - Created after the entrant sweep; the sealed-plan agent runtime and the zero-HN footprint recorded.

## See also

- [Backlog.md](../backlog-md/index.md) - the project-repository Markdown counterpart
- [beads](../beads/index.md) - the shared-queue graph counterpoint for coding agents
- [It's a Plan](../its-a-plan/index.md) - the platform-style agents-as-teammates entrant
- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/hasanyilmaz/operon - repository: README, surfaces, agent runtime introduction, topics (fetched 2026-10-08)
- https://api.github.com/repos/hasanyilmaz/operon - stars, forks, dates, license as of 2026-10-08
- https://raw.githubusercontent.com/hasanyilmaz/operon/main/README.md - inline and file tasks, operonId, the CLI and JSONL sessions, the 133 guides
- https://operon.cc/docs/docs-118-operon-agent-runtime-overview/ - the sealed preview-and-apply mutation gateway, receipts, Property Catalog, platform support
- https://api.npmjs.org/downloads/point/last-month/@stratejya/operon-cli - 362 downloads last month
- https://api.github.com/repos/hasanyilmaz/operon-cli - the official CLI repository, GPL-3.0
- https://api.github.com/repos/hasanyilmaz/operon/releases - 3.12.0 (2026-10-06) and the release train
