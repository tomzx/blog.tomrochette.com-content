---
title: Veritas Kanban
created: 2026-10-11
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, task-management, kanban, governance, local-first, open-source]
readability: 3
audience_notes: >
  Developers who want a board they own locally with an agent layer they switch on in measured steps,
  profiled against Agent Kanban, Kata, and Pad. Assumes you know what an MCP server and a tool allowlist are.
---

Veritas Kanban is an MIT local-first kanban board (React UI, Node server, packaged Mac app) whose agent layer is opt-in in verified layers, and whose v6 runtime gates what an agent may do per execution phase, with digest-pinned, approval-bound run-scoped tool catalogs.

**Its differentiator is authority as data: an agent's permissions are a function of the task's execution phase, enforced through durable compare-and-set transitions and tool catalogs whose digests bind every approval, not through prompts asking the agent to behave.**

## What it is

A TypeScript application from Brad Groux (Digital Meld's CEO and a podcast host), started as a local board: markdown task files with YAML frontmatter under `tasks/`, with file and SQLite repositories carrying a lease-safe worker foundation, a CLI (`vk`), and a packaged, signed Mac app through Homebrew cask.
The agent surface mounts in layers, each with a readiness stop point: board only, CLI, MCP read, MCP write (a 42-tool server), agent-ready (runners for Buzz, Grok Build, Codex, Claude Code, Copilot CLI, Hermes, and OpenClaw), then external wake and delivery through Squad Chat webhooks or OpenClaw.
The v6 control plane is the substance: phase capability profiles (versioned execution-phase authority contracts with deterministic intersections), a phase transition journal (durable compare-and-set transitions with approval and override controls and restart recovery), a run access summary (one digest-bound, redacted view of a run's filesystem, network, tools, budgets, and authority), and run-scoped tools (per-launch catalogs from validated server definitions, immutable `run-tool-catalog/v1` digests, denied and approval-required tools withheld from native provider configs, approvals bound to exact arguments and catalog digest, credential-bound entries mediated through a one-shot bridge).
Around the board: subtasks, bidirectional depends_on and blocks dependencies with cycle detection, sprints, templates, RBAC with agent tokens, YAML pipelines, enforcement gates, PRD-driven autonomous development (stories run in fresh context under a 4-by-10 review-gate score), team rosters with capability routing for delegated intake, and reflection-to-memory promotion.

## Status

**Active, six versions deep in one year, single-maintainer.**
839 stars, 100 forks, and 43 open issues and pull requests, created 2026-01-26, pushed 2026-10-06, as of 2026-10-11 (GitHub API).
The newest tagged release is v6.2.1 (2026-09-10); the dependency model landed in v3.3.0, team rosters in v5.2, and the run-scoped tool control plane in v6, all inside the project's first year.
A Hacker News search returns no story about it (2026-10-11), so adoption evidence is the repository curve plus the docs' own governance records.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=BradGroux/veritas-kanban&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=BradGroux/veritas-kanban&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=BradGroux/veritas-kanban&type=date&theme=dark&legend=top-left" />
</picture>

## Strengths

- **The run-scoped tool catalog is a governance mechanism no other member ships**: each launch compiles an immutable, digest-pinned catalog from validated server definitions, denied tools are never exposed to the provider, and an approval binds to the exact arguments and the catalog digest, so "the agent was allowed" is checkable after the fact.
- Phase authority makes autonomy configurable per stage: what the agent may do while planning differs from while executing, and transitions are compare-and-set journal entries that survive restarts rather than chat state.
- The layered readiness ladder (board, CLI, MCP read, MCP write, agent-ready, wake-ready) is the clearest adoption path in this category, and it fails closed between layers.
- The docs match the ambition: FEATURES.md alone runs thousands of lines, and the architecture docs specify the authority, credential, and certification boundaries.

## Cautions

- **Version velocity is churn**: three major version renumberings in the first year (v3, v5, v6), each moving core concepts, so docs and muscle memory from six months ago mislead.
- The packaged desktop app is macOS-only; Windows and Linux users run the server from source or self-host it behind a reverse proxy.
- One maintainer, a 43-issue backlog against 839 stars, and no tagged release in a month while pushes continue, so the release train and the repo have diverged before.
- The spec vocabulary (capability profiles, deterministic intersections, certification boundaries) is heavy for a board you install to move cards; expect reading before configuring.

## Pricing

Pricing does not apply: the board, server, CLI, MCP server, and Mac app are free and MIT, self-hosted, with no documented paid tier as of 2026-10-11.
The costs are your model subscriptions and the machine that runs the server.

## Compared to

- [Agent Kanban](../agent-kanban/index.md): both enforce governance in the product rather than the prompt; Agent Kanban's rule is one invariant (the assignee cannot accept its own review, bound to verified sessions), Veritas's is per-phase authority with approval-bound tool mediation, far broader and far heavier.
- [Kata](../kata/index.md): both sit outside the repo for loop speed; Kata is a millisecond ledger with hooks for 18 harnesses, Veritas is a governed platform whose speed is not the point.
- [Pad](../pad/index.md): both make agent behavior project data; Pad tracks conventions and playbooks as items, Veritas compiles authority and tool catalogs per run.

## Bottom line

**Recommended for a developer or small team handing agents consequential tool access who wants the permissions checkable after the fact, and who will read the architecture docs before turning the layers on.**
Not for a quick shared grocery list of coding tasks (kanban-md or Backlog.md), Mac-less desktop users, or anyone allergic to governance vocabulary.
My disagreeable claim: the run-scoped tool catalog belongs at the MCP layer, not inside a tracker, and if the protocol grows digest-pinned catalogs every member of this category will be retrofitting Veritas's design.

## Changes

- 2026-10-11 - Created after the orchestration resolution flagged the repository to this category, with the phase-authority and run-scoped-tool-catalog mechanisms recorded as the differentiators against the review-gate and ledger members.

## See also

- [Agent Kanban](../agent-kanban/index.md) - the other governance-first board, one invariant versus a control plane
- [Kata](../kata/index.md) - the speed-first local ledger counterpoint
- [Pad](../pad/index.md) - the conventions-as-items counterpoint
- [beads](../beads/index.md) - the graph-issue-database counterpoint
- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/BradGroux/veritas-kanban - repository facts: 839 stars, 100 forks, MIT, created 2026-01-26, pushed 2026-10-06 (GitHub API, as of 2026-10-11)
- https://raw.githubusercontent.com/BradGroux/veritas-kanban/main/README.md - the board-first pitch, setup layers, documentation map, provider list, and maintainer background
- https://raw.githubusercontent.com/BradGroux/veritas-kanban/main/docs/FEATURES.md - the feature reference: markdown storage, dependencies with cycle detection, run-scoped tools v6, team rosters, PRD-driven development, release provenance of v3.3.0/v5.2/v6
- https://raw.githubusercontent.com/BradGroux/veritas-kanban/main/docs/SETUP-PATHS.md - the layered readiness ladder and the board-only quick start
- https://api.github.com/repos/BradGroux/veritas-kanban/releases - v6.2.1 (2026-09-10) newest tagged release
- https://hn.algolia.com/api/v1/search?query=%22veritas%20kanban%22&tags=story - the footprint scan finding no story (2026-10-11)
