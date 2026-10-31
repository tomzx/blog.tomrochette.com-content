---
title: It's a Plan
created: 2026-10-07
updated: 2026-10-31
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
Andrii Poluosmak (the croffasia identity) maintains it under AGPL-3.0, except the runner package under Apache-2.0; the Pro edition introduced with v1.8.0 (2026-10-23) is the paid path for organizations, and its license funding the Community work is stated on the pricing page.

## Status

Young, active, and climbing fast for its age.
As of 2026-10-31: 963 stars (as of 2026-10-14), 275 forks, 57 open issues and pull requests, 39 contributors, created 2026-07-14, pushed 2026-10-30, 29 releases on a steady train, and 942 npm downloads over the trailing month to 2026-10-31 for @itsaplan/runner.
v1.9.0 (2026-10-27) added a Pro help desk: public forms that create issues from a script tag on a trusted site, a per-workspace requests portal where senders sign in with an email code and reply onto their issues, Trello import beside the Linear and Plane paths, all-project search behind the command palette and a `search_issues_all_projects` MCP tool, inline property editing in the Table and Timeline, and Docs mentions that can address an agent and get its answer.
v1.8.0 (2026-10-23) launched the paid Pro edition and fixed three high security advisories, two of them agent-permission holes: an internal agent run in one project could read and change issues in the agent's other projects, and a member who shared one project with an agent could regenerate its key and act as the agent in every project it had.
The breaking changes refuse cross-project objects from a run with 403 and restrict agent administration to team owners, managers, or members of every project of the agent.
v1.7.0 (2026-10-22) added agent run history (an issue's Activity page lists every run of its internal and external agents, and an AI Team runner queue lists active and past external runs, with transcripts since runner 0.7.0), run time limits (a god-mode cap up to 60 minutes per internal run with per-agent overrides, a run that hits its limit failing but keeping its output), and Traditional Chinese beside Turkish and Persian, while fixing four high and two medium security advisories.
v1.6.0 (2026-10-20) is the largest post-1.0 release: an external agent can receive its tasks at a signed invocation URL, so a serverless agent on AWS Lambda, Azure Functions, or Cloudflare Workers needs no polling runner (runner 0.6.0 can also listen on a port), invites expire after a configurable lifetime, new accounts can be limited to allowed email domains, mail can send through Microsoft 365 with OAuth, and the MCP surface gained client visibility (a security page listing connected clients with immediate disconnect, a consent screen naming the client, account, and host, and a get_current_user tool), alongside breaking changes that moved every team into a workspace, removed POST /projects, and require MCP OAuth clients to re-register.
v1.4.0 (2026-10-08) added agent schedules that also trigger when an issue enters a chosen state, plus Linear import, and v1.5.0 (2026-10-13) added agent usage accounting (cost, tokens, and runs by model, agent, project, and day, with admin-set prices for models the built-in table lacks), account deactivation, an api-on-subpath deployment mode, and the better-auth 1.7.7 fix for the critical OIDC sign-in advisory GHSA-965c-763c-88jm.
Pro runs the same Community stack on its own images: per-workspace SAML and SCIM, an audit log of every human, agent, and SCIM action with before-and-after values, a workspace dashboard, issue-event schedule triggers (issue created, assigned, labeled, or commented, with view filters and run caps) beside the timer and state triggers Community ships, agent analytics by trigger and person, and AI budgets per workspace, team, project, or person; without a license key the Pro images work as Community.

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

- **The community footprint is near zero: the only HN thread got 1 point and no comments, so 963 stars in thirteen weeks is uncorroborated by any independent discussion.**
- AGPL-3.0 triggers corporate policy reviews, and the escape hatch is now the priced Pro edition rather than an unlisted commercial license; a keyless Pro install falls back to Community features.
- Pre-1.0 churn is declared in the README, and a multi-service self-hosted stack (Postgres, object store, api, worker, bot, web) is heavier than every repo-local tracker here.
- One maintainer identity (croffasia), donations, and a Telegram roadmap channel concentrate bus risk.

## Pricing

Free, self-hosted, AGPL-3.0 (Community); the @itsaplan/runner package is Apache-2.0.
Pro, introduced with v1.8.0 on 2026-10-23, costs $24 per month or $240 per year for one instance (one domain) with unlimited seats and workspaces; it adds the organization features above and its license funds the Community edition, and an expired or missing key reverts the instance to Community.
Model costs follow your own API keys.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-07 | Community (self-hosted) | Baseline: free under AGPL-3.0 with no paid tier; a commercial license for companies AGPL does not fit existed with no listed price. | https://itsaplan.dev/pro |
| 2026-10-23 | Pro edition | Introduced at $24/month or $240/year per instance (one domain, unlimited seats and workspaces); Community stays free under AGPL-3.0. | https://itsaplan.dev/pro |

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
- 2026-10-09 - Recorded the v1.4.0 release (2026-10-08: agent schedules that also run the agent when an issue enters a chosen state, Linear import, cross-project issue moves through the move_issue MCP tool) and refreshed counts (913 stars, 150 forks, 31 contributors, 24 releases, 758 npm downloads).
- 2026-10-13 - Recorded the v1.5.0 release (2026-10-13: agent usage accounting with cost, tokens, and runs by model, agent, project, and day plus admin-set model prices, account deactivation, an api-on-subpath deployment mode, an installable web app, and the better-auth 1.7.7 fix for the critical OIDC sign-in advisory GHSA-965c-763c-88jm) and refreshed counts (963 stars, 159 forks, 42 open issues and pull requests, 25 releases, 797 npm downloads).
- 2026-10-21 - Recorded v1.6.0 (2026-10-20: external agent tasks delivered to a signed invocation URL with no polling runner, expiring invites, allowed email domains, Microsoft 365 OAuth mail, Turkish beside Persian, the MCP client-visibility surface with disconnect and a naming consent screen, get_current_user, and the breaking team-to-workspace, POST /projects removal, and MCP OAuth re-registration changes) and refreshed counts (233 forks, 49 open issues and pull requests, 39 contributors, 26 releases, 818 npm downloads, runner at 0.6.0).
- 2026-10-23 - Recorded v1.7.0 (2026-10-22: agent run history on issue Activity and an AI Team runner queue with transcripts since runner 0.7.0, run time limits up to 60 minutes with per-agent overrides, Traditional Chinese, and fixes for four high and two medium security advisories) and refreshed counts (252 forks, 50 open issues and pull requests, 27 releases, runner at 0.7.0).
- 2026-10-25 - Recorded v1.8.0 (2026-10-23: the Pro edition launched at $24/month or $240/year per instance with per-workspace SAML and SCIM, audit log, workspace dashboard, issue-event schedule triggers, agent analytics, and AI budgets; three high security advisories fixed, two of them agent-permission holes closed by refusing cross-project runs and restricting agent administration) and refreshed counts (254 forks, 54 open issues and pull requests, 28 releases, pushed 2026-10-25, 1,036 runner npm downloads); Pricing rewritten and Price history added.
- 2026-10-28 - Recorded v1.9.0 (2026-10-27: the Pro help desk with public forms and a per-workspace requests portal, Trello import, all-project search with an MCP tool, inline Table and Timeline editing, and Docs mentions that can address an agent) and refreshed counts (266 forks, 52 open issues and pull requests, 29 releases, pushed 2026-10-28, 859 runner npm downloads over the trailing month to 2026-10-28).
- 2026-10-31 - Refreshed counts (275 forks, 57 open issues and pull requests, pushed 2026-10-30, 942 runner npm downloads over the trailing month to 2026-10-31); v1.9.0 still the newest release.

## See also

- [beads](../beads/index.md) - the repo-local shared queue this platform parallels from the team side
- [Backlog.md](../backlog-md/index.md) - the markdown counterpoint where the plan lives in git
- [Task Master](../task-master/index.md) - the PRD pipeline counterpart
- [Ordewell](../ordewell/index.md) - the planner layer that could feed boards like this one
- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the category comparison this note joins

## References

- https://itsaplan.dev - the product site: agents as teammates, views, deployment paths, the Product Hunt badge
- https://github.com/croffasia/itsaplan - README: features, stack, license split, deployment options, the breaking-changes warning
- https://api.github.com/repos/croffasia/itsaplan - stars, forks, contributors, dates, AGPL-3.0 as of 2026-10-31
- https://api.github.com/repos/croffasia/itsaplan/releases - v1.9.0 (2026-10-27) and the release train, fetched 2026-10-28
- https://itsaplan.dev/pro - the Pro edition: $24/month or $240/year per instance, unlimited seats, the Pro feature list, and the Community-at-$0 comparison (fetched 2026-10-25)
- https://api.github.com/repos/croffasia/itsaplan/releases/tags/v1.8.0 - the v1.8.0 notes: the Pro launch, the three high advisories with the two agent-permission holes, and the breaking changes
- https://itsaplan.dev/changelog - the release train: v1.0.0 2026-09-15 through v1.8.0 2026-10-23, Plane import, Linear import, OIDC and SCIM
- https://github.com/croffasia/itsaplan/releases/tag/v1.5.0 - the v1.5.0 notes: usage accounting, account deactivation, the subpath deployment mode, the better-auth security fix
- https://api.github.com/repos/croffasia/itsaplan/releases/tags/v1.6.0 - the v1.6.0 notes: the agent invocation URL, expiring invites, allowed email domains, Microsoft 365 OAuth mail, the MCP client-visibility surface, and the breaking changes
- https://news.ycombinator.com/item?id=49971516 - the 1-point, comment-free throwaway thread, the missing-community-footprint signal
- https://api.npmjs.org/downloads/point/2026-10-01:2026-10-31/@itsaplan/runner - 942 downloads over the trailing month to 2026-10-31 for the external-runner package
- https://registry.npmjs.org/@itsaplan/runner/latest - the runner package at 0.7.0
