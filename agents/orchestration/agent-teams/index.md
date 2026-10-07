---
title: Agent Teams
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, desktop, kanban, multi-cli, agpl]
readability: 3
audience_notes: >
  Engineers choosing a desktop app to run teams of coding agents across CLIs,
  who already know Agent Orchestrator and Emdash and want the newer AGPL option
  compared. Assumes familiarity with coding-agent CLIs.
---

Agent Teams is a free AGPL desktop app that runs a boss-and-team hierarchy of coding agents across CLIs on a kanban board, with agent-to-agent messages and peer review.

## What it is

Agent Teams, created 2026-02-21 and licensed AGPL-3.0, is a TypeScript desktop application distributed from its own site, agentteams.live, with a Discord as the community channel.
Its model puts you as the boss over an organization of agents with roles, runtimes, and models, who handle tasks autonomously, message each other, and review each other's work.
It connects Claude Code, Codex, OpenCode, Cursor, SuperGrok, GitHub Copilot, Z.AI, MiniMax, and Kiro, and ships a built-in free model that needs no signup, API key, or card.

## Status

Active and young: 2,234 stars, a push on 2026-10-07, and release v2.17.1 on 2026-09-28 as of 2026-10-07 (GitHub API), on a repository created 2026-02-21.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=777genius/agent-teams-ai&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=777genius/agent-teams-ai&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=777genius/agent-teams-ai&type=date&theme=dark&legend=top-left" />
</picture>

**The independent record is empty so far: I found no Hacker News thread, no press coverage, and no third-party review this run, which makes 2.2k stars in eight months a bottom-up adoption signal that nothing yet corroborates.**
The screenshots document the feature set honestly (kanban with team messages, execution logs with tool calls, token and budget analytics, code review with file-level and hunk-level controls), and the product screenshots are the only evidence besides the repo itself.

## Strengths

- Built-in review tooling with file-level and hunk-level controls, deeper than most of the board genre ships.
- Token usage, cost, and budget analytics in the box.
- A free model with no auth lowers the first-run floor to zero.

## Cautions

- AGPL-3.0 is a real licensing consideration for anyone embedding it in a hosted product.
- A v2.17 version line within eight months says the interface is still moving fast.
- The 777genius organization publishes no visible company or maintainer identity, and with no independent coverage the project's accountability rests entirely on its repo.

## Pricing

Free, no paid tier found; the built-in free model requires no account, and bring-your-own providers carry their own costs.

## Compared to

Agent Orchestrator is the open-source kanban with the bigger star count and a nightly release train, but with a thinner review surface.
Emdash is the Apache-2.0 cross-platform alternative with 25-plus auto-detected CLIs and SSH-first execution.
Helmor is the local-first workbench that carries a task through merge and one-click PR rather than a team hierarchy.

## Bottom line

Recommended for engineers who want a zero-cost, review-first desktop for hierarchical agent teams and accept AGPL and an unverified adopter base.
Not for teams that need vendor accountability or a permissive license.

## Changes

- 2026-10-07 - Created.

## See also

- [Agent Orchestrator](../agent-orchestrator/index.md) - the category's kanban volume leader, the direct comparison for board-style multi-CLI orchestration.
- [Emdash](../emdash/index.md) - the Apache-2.0 cross-platform alternative with SSH-first execution.
- [Helmor](../helmor/index.md) - the local-first workbench alternative that owns the merge and PR step.
- [AgentGrid](../agentgrid/index.md) - the closed-source canvas counterpart at the same early stage.

## References

- https://github.com/777genius/agent-teams-ai - the repository, README provider list, stars, license, and releases.
- https://agentteams.live/ - the product site and download page.
- https://agentteams.live/docs - the documentation site.
- https://github.com/777genius/agent-teams-ai/releases - the release list, v2.17.1 (2026-09-28) latest at verification.
- https://raw.githubusercontent.com/777genius/agent-teams-ai/main/README.md - the README's provider list and feature screenshots as fetched this run.
