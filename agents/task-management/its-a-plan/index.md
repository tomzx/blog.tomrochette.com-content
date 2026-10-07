---
title: It's a Plan
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, task-management, issue-tracking, self-hosted, multi-agent, agpl]
readability: 3
audience_notes: >
  Teams choosing a self-hosted tracker where AI agents hold assignee slots like teammates, and engineers comparing platform-style trackers with repo-local ones.
  Assumes you know what AGPL-3.0 means for corporate use and what an MCP server is.
---

It's a Plan is an AGPL-3.0, self-hosted issue tracker and project-management platform where AI agents are project members with roles, permissions, and their own assignee slots on the same board as people.

**An agent holding an assignee slot, not a chat window, is the interface the rest of this category approaches from the repo side, and It's a Plan is the first full team platform in this section built around it.**

## What it is

An open-source alternative to Linear, Jira, Trello, and Plane that runs on your own server (Docker Compose, Railway, Coolify, or Helm) with projects, boards, cycles, custom fields, dashboards, docs, and notes.
Agents work like teammates: an internal agent runs on any model you key (the agent runtime is Mastra), an external agent runs on your machine through the @itsaplan/runner package driving Claude Code, Codex, OpenCode, Antigravity, Copilot, or a custom command, and runs start on an @mention, an assignment, or a schedule.
Everything is reachable over a REST API with OpenAPI, an MCP server, and webhooks, with pull request links from five forges.
Andrii Poluosmak (the croffasia identity) maintains it under AGPL-3.0, except the runner package under Apache-2.0, and sells a commercial license for companies AGPL does not fit.

## Status

Young, active, and climbing fast for its age.
As of 2026-10-07: 896 stars, 145 forks, 34 open issues, 29 contributors, created 2026-07-14, pushed 2026-10-06, 23 releases, with v1.0.0 on 2026-09-15 and v1.3.0 (workspaces, project archiving) on 2026-10-04, and 727 npm downloads last month for @itsaplan/runner.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=croffasia/itsaplan&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=croffasia/itsaplan&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=croffasia/itsaplan&type=date&legend=top-left" />
</picture>

**The HN footprint is the weak signal: one 1-point thread with zero comments, posted by a throwaway account on 2026-10-05, so the adoption evidence is the repo's own growth curve, not independent discussion.**
The launch instead ran on Product Hunt per the site's own badge, and the changelog shows a steady train (Plane import in v1.1.0, OIDC and SCIM in v0.16.0, a docs tree in v0.17.0).
The README warns to expect breaking changes before the first stable release.

## Strengths

- Agents hold assignable teammate slots with role-based permissions, so delegation, audit, and access control are board concepts instead of prompt conventions.
- The tracker is complete without turning on a single agent, which makes the agent layer opt-in per project.
- Self-host with your own database and model keys, no per-seat fees, and one-click paths for Railway, Coolify, and Helm.
- MCP server, OpenAPI-documented REST, and webhooks make the board scriptable from any client.

## Cautions

- **The community footprint is near zero: the only HN thread got 1 point and no comments, so 896 stars in twelve weeks is uncorroborated by any independent discussion.**
- AGPL-3.0 triggers corporate policy reviews, and the escape hatch is a commercial license with no listed price.
- Pre-1.0 churn is declared in the README, and a multi-service self-hosted stack (Postgres, object store, api, worker, bot, web) is heavier than every repo-local tracker here.
- One maintainer identity (croffasia), donations, and a Telegram roadmap channel concentrate bus risk.

## Pricing

Free, self-hosted, AGPL-3.0; the @itsaplan/runner package is Apache-2.0.
No per-seat fees and no hosted plan exists; model costs follow your own API keys, and the commercial license offered for companies AGPL does not fit has no listed price.

## Compared to

- [beads](../beads/index.md): both give agents structured work, but beads is a repo-local shared queue for coding agents while It's a Plan is a whole-team platform the repository sits beside.
- [Backlog.md](../backlog-md/index.md): the plan-in-diffs counterpoint; choose Backlog.md when the tracker must live inside git.
- [Task Master](../task-master/index.md): pipeline versus platform; Task Master decomposes documents into tasks, It's a Plan hosts the board the work lands on.

## Bottom line

**Recommended for teams that want a self-hosted Linear-class tracker and are ready to put agents on the roster with managed permissions.**
Not for repo-local, git-diff-first workflows (that is beads or Backlog.md), or for anyone who needs a community-vetted system at maturity.
My disagreeable claim: an assignee slot is a sharper agent interface than an MCP tool catalog, because it forces the permission and audit questions the catalog lets a team skip.

## Changes

- 2026-10-07 - Created after the HN by-date scan surfaced the launch thread, recording the agents-as-assignees design, the license split, and the near-zero HN footprint.

## See also

- [beads](../beads/index.md) - the repo-local shared queue this platform parallels from the team side
- [Backlog.md](../backlog-md/index.md) - the markdown counterpoint where the plan lives in git
- [Task Master](../task-master/index.md) - the PRD pipeline counterpart
- [Ordewell](../ordewell/index.md) - the planner layer that could feed boards like this one
- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the category comparison this note joins

## References

- https://itsaplan.dev - the product site: agents as teammates, views, deployment paths, the Product Hunt badge
- https://github.com/croffasia/itsaplan - README: features, stack, license split, deployment options, the breaking-changes warning
- https://api.github.com/repos/croffasia/itsaplan - stars, forks, contributors, dates, AGPL-3.0 as of 2026-10-07
- https://itsaplan.dev/changelog - the release train: v1.0.0 2026-09-15 through v1.3.0 2026-10-04, Plane import, OIDC and SCIM
- https://news.ycombinator.com/item?id=49971516 - the 1-point, comment-free throwaway thread, the missing-community-footprint signal
- https://api.npmjs.org/downloads/point/last-month/@itsaplan/runner - 727 downloads last month for the external-runner package
- https://registry.npmjs.org/@itsaplan/runner/latest - the runner package at 0.5.2
