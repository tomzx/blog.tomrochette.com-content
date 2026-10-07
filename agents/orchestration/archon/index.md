---
title: Archon
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, workflow-engine, worktrees]
readability: 3
audience_notes: >
  Engineers who want a coding-agent pipeline that runs the same way every time, and anyone comparing workflow runners.
  Assumes you already run Claude Code or Codex and know what a git worktree is.
---

Archon is Cole Medin's MIT workflow engine for AI coding agents: you define a development process as a YAML graph of deterministic and AI nodes, and it runs that graph reliably, each run in its own git worktree, from the CLI, web UI, Slack, Telegram, GitHub, or Discord.

**Archon markets itself as the first open-source harness builder, but its product reality is the workflow-runner seat of this category: the harnesses stay yours (Claude Code SDK, Codex SDK, or local models via Pi), and Archon owns the structure around them, which is exactly the job Crewplane and Bernstein do with less ambition.**

## What it is

A Bun-built CLI and web application, MIT licensed, installed by script, Homebrew, or Docker, with the docs at archon.diy (23,636 stars, pushed 2026-10-07, as of 2026-10-07).
Workflows live as YAML files in `.archon/workflows/`, committed to your repo: nodes form a DAG with dependencies, loops, and conditional logic; deterministic nodes run bash scripts, tests, and git operations; AI nodes do planning, implementation, and review; a loop node iterates until a condition with fresh context per iteration.
Every workflow run gets its own git worktree, so parallel runs do not collide, and a kicked-off run completes on its own and returns a finished PR with review comments.
Setup runs through Claude Code itself (the guided wizard is a Claude Code session, and compiled binaries want a `CLAUDE_BIN_PATH`), with multi-provider support for the Claude Code SDK, Codex SDK, and local models via Pi.

## Status

Active: created 2025-02-07, 23,636 stars, release v0.11.1 published 2026-09-25, as of 2026-10-07.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=coleam00/Archon&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=coleam00/Archon&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=coleam00/Archon&type=date&legend=top-left" />
</picture>

The project restarted on this workflow-engine concept in 2026 after an earlier life as an agent-building platform, which the repo's created date predates; the current line is the one this note covers.
Trendshift carried its badge during the 2026 surge, and its HN footprint is minimal (a single 1-point submission), so the adoption case is the star curve and the docs, not independent coverage.

## Strengths

- The determinism pitch is the category's sharpest: the workflow owns phases, gates, and artifacts, and the model fills in intelligence only inside nodes, so the same input walks the same path.
- Worktree-per-run isolation is native rather than a recommendation, which is what makes five parallel fixes safe.
- Workflow files are versioned in the repo and portable across triggers, so the process survives tool changes and travels with the code.
- Trigger breadth (CLI, web, Slack, Telegram, GitHub, Discord) covers the fire-and-forget and the delegate-from-chat cases in one engine.

## Cautions

- The engine currently assumes the Claude Code ecosystem for setup and binaries, so non-Claude shops start with friction despite the Codex and Pi support.
- One lead maintainer's project with fast star growth, the profile that has produced most of this category's orphaned tools.
- YAML workflow graphs re-introduce the configuration surface that plain-Python runners avoid, and complex DAGs will need debugging tools the young web UI may not have yet.
- The "first open-source harness builder" claim is marketing over a category that already holds a dozen workflow runners; the differentiator is the worktree-per-run and trigger breadth, not primacy.

## Pricing

Free and open source under MIT; there is no paid tier, so pricing does not apply.
Costs are your harness subscriptions and tokens, plus the compute for parallel worktrees.

## Compared to

- [Crewplane](../crewplane/index.md): the minimal CLI workflow runner that turns agent stages into resumable Markdown; Archon adds worktree isolation, triggers, and a UI at the cost of a heavier install.
- [Bernstein](../bernstein/index.md): the governance layer running parallel agents behind merge gates on a deterministic scheduler; Archon is the developer-facing sibling where Bernstein is the audit-facing one.
- [Ruflo](../ruflo/index.md): the meta-harness with 100-plus agents and swarms; Archon bets on fewer, structured workflows instead of many agents.

## Bottom line

**Recommended for engineers who keep re-explaining their process to agents and want it encoded once as a repo-committed workflow with parallel worktree runs.**
Not for teams outside the Claude Code ecosystem today, and not for anyone who needs a governance-grade audit trail, where Bernstein's lane is stronger.

## Changes

- 2026-10-07 - Created.

## See also

- [Crewplane](../crewplane/index.md) - the minimal workflow runner sharing this category seat
- [Bernstein](../bernstein/index.md) - the deterministic parallel-agent sibling with the audit focus
- [Ruflo](../ruflo/index.md) - the many-agent alternative to Archon's structured workflows
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/coleam00/Archon - repository, MIT license, the workflow YAML model, worktree isolation, and the trigger list (fetched 200, 2026-10-07)
- https://api.github.com/repos/coleam00/Archon - stars, created date, and push date for the as-of status (fetched 200, 2026-10-07)
- https://archon.diy/docs/ - the docs hub: workflow engine definition, portability claims, multi-provider support (Claude Code SDK, Codex SDK, Pi), and install paths (fetched 200, 2026-10-07)
- https://api.github.com/repos/coleam00/Archon/releases - the v0.11.1 release of 2026-09-25 (fetched 200, 2026-10-07)
- https://raw.githubusercontent.com/coleam00/Archon/HEAD/README.md - the setup flow through Claude Code, the CLAUDE_BIN_PATH requirement, and the deterministic-versus-mood argument (fetched 200, 2026-10-07)
