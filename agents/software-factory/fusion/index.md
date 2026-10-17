---
title: Fusion
created: 2026-10-11
updated: 2026-10-17
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, software-factory, kanban, multi-agent, worktrees, open-source]
readability: 3
audience_notes: >
  Engineers who want a factory that owns the loop from a rough idea to merged code, profiled against
  SuperPlane, Zeroshot, and Loki Mode. Assumes you know what Git worktrees and review gates are.
---

Fusion is an MIT software factory run from a kanban board: a triage agent turns a rough idea into a PROMPT.md spec with acceptance criteria, and every task flows through plan, review, execute, review steps in an isolated worktree, with auto-merge when the quality gates pass.

**Its differentiator is that the board is the factory control surface and it follows you to every node you own, laptop to server to phone, on a multi-node mesh with shared state.**

## What it is

A TypeScript application installed from npm (`npx runfusion.ai`, Homebrew, or an install script), with native iOS, Android, macOS, Windows, and Linux apps, a web dashboard, and Docker or headless deployment, early preview, shipping weekly.
The agent runtime stands on Pi (the minimal extensible coding-agent CLI), with Hermes, Paperclip, Droid, and Cursor as first-class provider plugins and an ACP runtime that drives Gemini CLI, Claude, or any ACP agent; a model router with cheap-tier routing and fallback spans Anthropic, OpenAI, Gemini, Z.ai, and Ollama, with five model lanes (executor, planner, validator, title, workflow) overridable per task.
Around the loop it adds missions (Mission, Milestone, Slice, Feature, Task, with autopilot), inter-agent mailbox chat, qmd markdown memory, Paperclip-format agent-company import, cron automations, plugins (every Pi extension works), and a Command Center of eleven analytics views (tokens, USD cost, autonomy ratio, per-agent output, model mix) with CSV and OpenTelemetry export.
The dashboard is built on dustinbyrne/kb; the docs are in-repo and unusually complete, down to an evidence gate that blocks a goals feature until actual usage pain is documented.

## Status

**Active and heavily pushed, but early preview, and the stable npm channel lags the repository.**
1,270 stars, 162 forks, and 86 open issues and pull requests as of 2026-10-13, created 2026-04-13, pushed 2026-10-15 (GitHub API).
The newest GitHub release and npm beta is still v0.78.0-beta.7 (2026-09-25, re-verified 2026-10-17); npm `latest` is still 0.77.0 (2026-09-02), so the stable channel ran six weeks behind a repository that pushes near-daily.
The package drew 2,629 npm downloads in the month ending 2026-10-12, and a Hacker News search returns no story about it (2026-10-13).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Runfusion/Fusion&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Runfusion/Fusion&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Runfusion/Fusion&type=date&theme=dark&legend=top-left" />
</picture>

## Strengths

- **The per-step loop is the strictest gate rhythm in the category**: every task step is planned, reviewed, executed, and reviewed again before the board moves, and oversight levels (off, observe, steer, autonomous) put a human-confirmation gate on merge, PR, and destructive actions by default.
- Worktree isolation with teeth: Fusion tracks which files each task touches and auto-rebases dependent tasks in order, so parallel tasks are claimed to merge with zero conflicts.
- Auto-merge when every gate (docs, QA, security, performance, accessibility) passes keeps history linear and the human out of the merge queue.
- The multi-node mesh plus phone apps make it the only member of this category you can steer from a train, with settings, missions, and board state synced across nodes.

## Cautions

- **Early preview means the guarantees are the demo's**: the site's "agents work 24/7", "run for weeks", and "1,500+ tool calls per human touch" claims are unaudited, and the stable npm channel has not shipped since September 2 while the marketing badge says shipping weekly.
- The scope is enormous for a nine-month-old project (factories, missions, companies, glasses plugins, research views), and feature breadth at this cadence historically trades against durability.
- The self-improvement claim is self-referential: agents rewrite their own AGENTS.md after each task, which is the input to their next run, so drift compounds unless someone reads the diffs.
- The docs record an internal evidence gate for one feature slice, which is admirable discipline and also an admission that the roadmap outruns verified demand.

## Pricing

Pricing does not apply: Fusion is free and MIT, self-hosted on your nodes, with your model subscriptions or API keys as the only running cost and no hosted tier as of 2026-10-11.

## Compared to

- [SuperPlane](../superplane/index.md): both own the loop as a product; SuperPlane turns confidence-gated backlog issues into review-ready PRs with durable run records, Fusion is board-first with worktree auto-rebase and auto-merge, and is younger and less durable-looking.
- [Zeroshot](../zeroshot/index.md): Zeroshot's acceptance rule is two independent reviewers who never wrote the code; Fusion's is per-step review plus configurable quality gates, with the human confirmation default as the backstop.
- [Loki Mode](../loki-mode/index.md): Loki derives a delivery contract and closes with a signed Evidence Receipt you can check offline; Fusion traces runs in Command Center but has no offline-checkable receipt.

## Bottom line

**Recommended for a developer with two or more machines (or a phone habit) who wants a gate-gated factory they can steer from anywhere and can tolerate early-preview churn.**
Not for teams that need a durable run ledger as the product (SuperPlane), an offline acceptance receipt (Loki Mode), or independent reviewers as the acceptance rule (Zeroshot).
My disagreeable claim: auto-merge on green gates is where this category is going and Fusion is simply there first, which is exactly why its unverifiable reliability claims deserve more skepticism than its competitors'.

## Changes

- 2026-10-11 - Created after the orchestration resolution flagged the repository to this category, with the early-preview-versus-weekly-shipping gap and the unaudited autonomy claims recorded as the critical angle.

## See also

- [SuperPlane](../superplane/index.md) - the platform column this note's board-first loop is measured against
- [Zeroshot](../zeroshot/index.md) - the two-reviewer acceptance rule counterpoint
- [Loki Mode](../loki-mode/index.md) - the evidence-receipt acceptance counterpoint
- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - the category comparison this note joins
- [Agent Kanban](../../task-management/agent-kanban/index.md) - the task board that shares the kanban surface without owning the loop

## References

- https://github.com/Runfusion/Fusion - repository facts: 1,270 stars, 162 forks, MIT, created 2026-04-13, pushed 2026-10-13 (GitHub API, as of 2026-10-13)
- https://raw.githubusercontent.com/Runfusion/Fusion/main/README.md - the loop description, PROMPT.md planning, worktree flow, install paths, and the dustinbyrne/kb credit
- https://raw.githubusercontent.com/Runfusion/Fusion/main/docs/README.md - the documentation map: oversight levels, workflow steps, missions, storage, mesh protocol, sandbox backends, plugins
- https://runfusion.ai - the product site: board and Command Center tours, model lanes, mesh nodes, mobile apps, Paperclip compatibility, and the autonomy claims recorded as cautions
- https://api.github.com/repos/Runfusion/Fusion/releases - v0.78.0-beta.7 (2026-09-25) newest release
- https://registry.npmjs.org/@runfusion/fusion - dist-tags: latest 0.77.0 (2026-09-02), beta 0.78.0-beta.7
- https://api.npmjs.org/downloads/point/last-month/@runfusion/fusion - 2,629 downloads in the month ending 2026-10-12
- https://hn.algolia.com/api/v1/search?query=runfusion&tags=story - the footprint scan finding no story (2026-10-11)
