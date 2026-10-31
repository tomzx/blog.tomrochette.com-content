---
title: Commonly
created: 2026-10-31
updated: 2026-10-31
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, team-collaboration, task-board]
readability: 3
audience_notes: >
  Engineers on small teams who each already run their own coding agents and need shared context without another dashboard.
  Assumes you know what a task board and an agent CLI are.
---

Commonly is an open-source team-pod workspace where each person's coding agents join shared conversations and one task board as named, owned members.

**Commonly's bet is that multi-agent coordination fails at the human seam, so it makes the team's chat and board the shared runtime instead of building another orchestrator dashboard.**

## What it is

A hosted workspace at commonly.me plus a self-hostable Apache-2.0 TypeScript app: one pod holds the people, their agents, the conversation, and the task board.
Every agent is a named member with an owner, so the board answers who has what without a supervision process.
Your own Claude Code or Codex connects from your machine through the @commonlyai/cli daemon (npm 0.1.208 as of 2026-10-31), or a hosted agent starts in one click, and both answer @mentions in the pod.
Agents file and claim task cards, post what they tried, and ask a human on the card when the decision is theirs; tool connections carry per-pod, per-agent scoped grants instead of personal keys, and Linux Claude Code runs are bubblewrap-sandboxed by the CLI itself.
By Team-Commonly, repository created 2025-02-03, v3.0.0 released 2026-10-28.

## Status

Active: 1,374 stars, 189 forks, and 208 open issues and pull requests as of 2026-10-31 (GitHub API), pushed 2026-10-31, with v3.0.0 three days earlier and the release train running v1.0.0 (2026-04-07), v2.0.0 (2026-07-06), v2.1.0 (2026-07-23).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Team-Commonly/commonly&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Team-Commonly/commonly&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Team-Commonly/commonly&type=date&legend=top-left" />
</picture>

The npm CLI moves daily-pace (0.1.208 published 2026-10-31, 14,919 downloads October 1 to 31), and the AMO orchestrator directory added it under Coordination And Team Systems on 2026-10-30.
Zero independent coverage: a Hacker News search finds no story about the project as of 2026-10-31, so the footprint is the repository, the CLI downloads, and the hosted site itself.

## Strengths

- **The roster model is the differentiator: agents as owned, named members on one board answers "who is doing what" without a supervisor process to feed.**
- Bring-your-own-agent is real, not a slogan: the agent runs where you already run it, and the pod is the shared room rather than another place to configure keys.
- Scoped tool grants per pod and per agent attack the shared-credential problem most team setups ignore, with read-only grants enforced down to read actions.

## Cautions

- No independent coverage at all: no HN thread, no third-party write-up found; adoption evidence is the star count and CLI downloads, both young.
- The hosted pod is the default path and the vendor publishes no price list (the site's pricing path redirects home), so cost at team scale is unknown until billing appears.
- The board is the whole work model: no worktree machinery, no review surface, so teams needing PR-centric loops still need the harness underneath.

## Pricing

The Apache-2.0 app is free to self-host.
The hosted commonly.me run requires an account, and no published price list exists as of 2026-10-31.

## Compared to

- [OpenHarness](../openharness/index.md): the standalone ADE admitted beside it; OpenHarness supervises autonomous runs, Commonly coordinates the people and agents around shared work.
- [Swarm Orchestrator](../swarm-orchestrator/index.md): per-task worktree workers under one supervisor; Commonly has no worktree machinery, its unit is the conversation and the card.
- [Vibe Kanban](../vibe-kanban/index.md): board-first agent orchestration for solo operators; Commonly's pod adds the humans and the chat as first-class members.

## Bottom line

**Recommended for small teams whose members already run their own coding agents and want shared context without a dashboard to feed.**
Not for solo worktree automation, and not for anyone needing a review or PR-centric loop out of the coordination layer.

## Changes

- 2026-10-31 - Created.

## See also

- [OpenHarness](../openharness/index.md) - the standalone-ADE admission whose precedent this note rides
- [Swarm Orchestrator](../swarm-orchestrator/index.md) - the supervisor-plus-worktree contrast to the pod model
- [Vibe Kanban](../vibe-kanban/index.md) - the board-first solo counterpart
- [hcom](../hcom/index.md) - the message-fabric alternative that keeps your multiplexer

## References

- https://github.com/Team-Commonly/commonly - repository, feature set, license, and counts as of 2026-10-31
- https://raw.githubusercontent.com/Team-Commonly/commonly/HEAD/README.md - the pod model, agent roster, scoped grants, and adapters
- https://github.com/Team-Commonly/commonly/releases - the release train through v3.0.0 (2026-10-28)
- https://commonly.me - the hosted default and the vendor's product page
- https://docs.commonly.me/quickstart - the documented setup path
- https://registry.npmjs.org/@commonlyai/cli - the CLI package and its publish dates
- https://api.npmjs.org/downloads/point/2026-10-01:2026-10-31/@commonlyai/cli - October 2026 downloads (14,919)
- https://hn.algolia.com/api/v1/search?query=%22commonly.me%22&hitsPerPage=5 - the zero-story Hacker News footprint as of 2026-10-31
