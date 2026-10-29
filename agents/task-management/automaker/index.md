---
title: Automaker
created: 2026-10-28
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, task-management, kanban, multi-agent, electron, open-source, dormant]
readability: 3
audience_notes: >
  Engineers who want a desktop board where each card is implemented end to end by an AI agent, and anyone weighing the kanban-to-code pattern it demonstrated.
  Assumes you know what a git worktree is and what an Electron app is.
---

Automaker is an MIT-licensed, Electron-and-web AI development studio that turned a kanban board into an agent orchestrator: each feature card dragged to In Progress was implemented end to end by an agent working in its own git worktree, and the repository is now unmaintained by its own written declaration.

**The board-as-orchestrator idea earned 3,227 stars and a v1.0.0 in its first year and still died with the course funnel that built it, and the repository says so itself: the LICENSE file opens with "This project is no longer actively maintained."**

## What it is

An Electron desktop app (React 19, Vite, Express 5) also runnable in a browser or Docker, built as an npm-workspace monorepo with seven shared packages.
The board runs Backlog, In Progress, Waiting Approval, and Verified: cards are feature descriptions carrying text, screenshots, and configuration, and moving one to In Progress spawns an agent, the Claude Agent SDK by default with Codex, Copilot, Cursor, Gemini, and OpenCode as further providers, inside an isolated git worktree.
Four planning modes from skip to full let a team dial autonomy per card, plan approval gates implementation, spec mode spawns one dedicated agent per subtask, and verification is structural: finished cards land in Waiting Approval with a git diff, and approval is what releases the commit and the pull request.
Storage is file-based JSON under the project's `.automaker/` directory plus a global DATA_DIR, with no database.
It came out of the Agentic Jumpstart camp, Web Dev Cody's $129 Claude Code and Cursor course, as that community's flagship demonstration, with the README and Discord routing users to the course.

## Status

Dormant, and declared dead by its own repository.
As of 2026-10-28: 3,227 stars, 589 forks, 10 open issues, created 2025-12-07, pushed 2026-05-22, and v1.0.0 (2026-03-15) is the final tagged release.
Both the README and the LICENSE file carry the same declaration: no bug fixes, no security updates, no new features, community contributions accepted with no guarantee of review.
The product site, automaker.app, returns 404.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=AutoMaker-Org/automaker&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=AutoMaker-Org/automaker&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=AutoMaker-Org/automaker&type=date&legend=top-left" />
</picture>

**The independent footprint is zero: an HN title search returns only car-industry stories, and this run's searches found no third-party coverage, so the adoption evidence is the repository's own curve.**
The maintenance arc is visible in the repo itself: v0.15.0 (2026-02-25) removed an earlier maintenance notice from the README, development continued through v1.0.0 in March and a final push on 2026-05-22, and the declaration now sits at the top of the LICENSE file.

## Strengths

- The kanban card as the unit of autonomous work is the cleanest board-to-agent mapping any member of this category has shipped: describe a feature, drag it, watch it build in its own worktree.
- The verification column is structural: cards land in Waiting Approval with a diff to review, and approval releases the commit and pull request, the same gate Agent Kanban enforces and this product actually executed.
- Four planning levels (skip, lite, spec, full) make autonomy a per-card setting, and spec mode's agent-per-subtask split is the same idea CCPM runs across GitHub issues.
- The security writing is blunt: the README's own disclaimer tells you not to run it on your daily machine and to sandbox it in Docker or a virtual machine.

## Cautions

- **It is dead: the LICENSE and README declare no maintenance, the product site is gone, the last push landed 2026-05-22, and the ten open issues belong to whoever forks it.**
- The default provider's economics changed after the last release: since 2026-06-15 the Claude Agent SDK draws from a separate monthly credit pool instead of subscription limits, a billing model the unmaintained README documents but the software will never adapt to.
- The README's own disclaimer is the critical source: agents get full file-system and command access, the reviewed code carries no warranty, and Docker isolation is recommended, not default.
- The distribution is a course funnel: the README, Discord, and community route through a $129 course, so the star count measures marketing reach as much as adoption.

## Pricing

The application is free under MIT.
Agent costs ride your own provider accounts; for the default Claude provider, the Agent SDK billing change of 2026-06-15 moved usage to a separate monthly credit pool claimed once per account, $20 on Pro, $100 on Max 5x, and $200 on Max 20x, metered at standard API rates with no rollover, as of 2026-10-28.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-28 | Claude Agent SDK credit pool (the app itself is free, MIT) | Baseline: the separate monthly credit pool effective 2026-06-15, $20 Pro, $100 Max 5x, $200 Max 20x, claimed once, no rollover, recorded at profile time. | https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan |

## Compared to

- [Agent Kanban](../agent-kanban/index.md): the living board of this category; Agent Kanban enforces review but executes nothing, while Automaker executed everything and can no longer enforce anything.
- [Task Master](../task-master/index.md): the other pipeline that outlived its repository; Task Master went commercial and quiet, Automaker went unmaintained in plain words.
- [Veritas Kanban](../veritas-kanban/index.md): the governed-execution counterpoint, alive and phase-gated where Automaker was free-form and is gone.

## Bottom line

**Recommended for no new adoption: read it as the reference implementation of kanban-to-code and as a caution about course-funnel products.**
Not for anyone needing a maintained tracker, and not for teams that cannot sandbox an agent with full file-system access.
My disagreeable claim: Automaker's death is worth more to this category than its feature list, because the board-as-orchestrator products that survived, Agent Kanban and Veritas Kanban, are the ones that separated the board from the runtime.

## Changes

- 2026-10-28 - Created from the software-factory worker's cross-category flag, recording the kanban-to-code design, the LICENSE's no-longer-maintained declaration, the dead product site, and the zero independent footprint.

## See also

- [AI Dev Tasks](../ai-dev-tasks/index.md) - the category's other dormant ancestor, two prompt files where Automaker was a full studio
- [Agent Kanban](../agent-kanban/index.md) - the board-without-execution counterpoint
- [Veritas Kanban](../veritas-kanban/index.md) - the governed-execution counterpoint
- [CCPM](../ccpm/index.md) - the issue-as-card parallel-execution recipe that stayed MIT and alive

## References

- https://github.com/AutoMaker-Org/automaker - repository: stars, forks, dates, and the README's workflow and architecture
- https://raw.githubusercontent.com/AutoMaker-Org/automaker/main/README.md - the kanban-to-code workflow, planning modes, storage layout, the security disclaimer, and the maintenance declaration
- https://raw.githubusercontent.com/AutoMaker-Org/automaker/main/LICENSE - MIT plus the no-longer-actively-maintained declaration at the top of the file
- https://api.github.com/repos/AutoMaker-Org/automaker - stars, forks, dates, and last push as of 2026-10-28
- https://api.github.com/repos/AutoMaker-Org/automaker/releases - v1.0.0 (2026-03-15), the final release, and v0.15.0 (2026-02-25), which removed the earlier maintenance notice
- https://automaker.app/ - the dead product site, 404 as of 2026-10-28
- https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan - the Agent SDK credit-pool billing that grounds the pricing section
- https://agenticjumpstart.com/ - the $129 course business the README and Discord route through
- https://hn.algolia.com/api/v1/search?query=automaker&tags=story - the title search returning only car-industry stories, the zero-footprint signal
- https://github.com/varun1505/awesome-software-factories - the source list whose 2026-10-26 entry flagged the repository here
