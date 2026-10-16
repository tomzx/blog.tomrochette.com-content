---
title: Pad
created: 2026-10-11
updated: 2026-10-16
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, task-management, project-management, local-first, mcp, open-source]
readability: 3
audience_notes: >
  Developers who want a tracker with a browser UI that their agents operate as first-class users, and who want the rules the agents follow stored as data.
  Assumes you know what an MCP server is and what a TTL lease means.
---

Pad is an Apache-2.0, single-binary project tracker with a CLI, an embedded web UI, and a versioned MCP server, built so agents read and write the same items, plans, conventions, and playbooks that humans manage in the browser.

**Conventions and playbooks as tracked items are the differentiator: the rules the agents follow are rows in the same database as the work, versioned and attributable, not prose scattered through config files.**

## What it is

A Go binary (Cobra CLI, chi REST API, embedded SvelteKit UI) over SQLite with FTS5, installed by Homebrew, Docker, or Nix, with Postgres plus Redis for multi-instance deployments and Pad Cloud as the hosted option.
Work lives in typed collections: tasks, ideas, plans, docs, plus two agent-facing ones, conventions (trigger-based rules such as "run tests before marking a task done") and playbooks (multi-step workflows invocable as `/pad ship PLAN-42`).
Agents get the `/pad` skill, a Claude Code plugin with typed shortcuts, live item notifications, and a side panel, plus installs for Cursor, Windsurf, Codex, OpenCode, Copilot, Amazon Q, and JetBrains Junie, and an MCP server whose catalog is versioned (`tool_surface_version` 0.85, ten resource-action tools plus workspace pinning).
Coordination is built in: `pad item claim` takes an atomic lease with a TTL where a 409 names the live holder, named agents (`PAD_AGENT`, `pad session register`) put the agent's name on its writes, and consent-gated `pad push` injects direction into a running Claude Code session only after that session opts in.
Perpetual Software LLC maintains it; every change is versioned per item with the actor recorded, person or named agent.

## Status

Active and pre-1.0.
As of 2026-10-16: 193 stars (as of 2026-10-14), 24 forks, created 2026-03-26, pushed 2026-10-16, on a roughly weekly release cadence with v0.18.0-rc.11 (2026-10-15) the newest tag, and the changelog delegated to signed GitHub Releases carrying SBOMs and SLSA provenance.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=PerpetualSoftware/pad&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=PerpetualSoftware/pad&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=PerpetualSoftware/pad&type=date&legend=top-left" />
</picture>

An HN search for the project returns zero story hits as of 2026-10-14; the community gathers on the project's own r/getpad subreddit instead, so adoption evidence is the repository curve and the dogfooded workspace the site shows (3,205 items, with 40 pull requests merged in one September day all traced to items).

## Strengths

- Conventions and playbooks make agent behavior project data: trigger rules and workflows are items every session can load, not per-agent prompting to maintain by hand.
- The claim lease and agent naming give multi-agent attribution out of the box, and the activity feed shows which named agent changed what.
- Three surfaces over one store (CLI, browser, MCP) with live updates between them, so a task an agent creates in the terminal appears in the browser as it happens.
- Upgrade discipline is serious for pre-1.0: forward-only migrations, a schema-ahead guard that refuses downgraded binaries, and automatic pre-migration SQLite snapshots.

## Cautions

- 190 stars and a weekly release train mean churn; the recovery path for a bad upgrade is reinstall-forward, not rollback.
- The optional decision provider sends item content (title, field values, body up to 16,000 characters, the last ten comments) to a third-party model API when enabled; it is off by default, but it is a data boundary worth knowing in a local-first pitch.
- Pad Cloud is the visible business, and its free tier (10 workspaces, 1,000 items per workspace, 3 collaborators, 500 MB) sketches where the walls will go; paid prices are unlisted.
- No HN footprint and a young subreddit leave adoption uncorroborated by independent discussion.

## Pricing

Self-hosted: free under Apache-2.0, with no feature gates between the binary and the cloud product.
Pad Cloud: free tier with 10 workspaces, 1,000 items per workspace, 3 collaborators, and 500 MB of storage; a paid plan lifts the limits, with no listed price as of 2026-10-14.

## Compared to

- [It's a Plan](../its-a-plan/index.md): both are full tracker platforms; It's a Plan is AGPL-3.0 self-hosted team software built around agents as assignees, Pad is local-first single-binary with an opt-in cloud.
- [Operon](../operon/index.md): both make the agent write through the human's system; Operon's store is the Obsidian vault with receipted plans, Pad's is its own SQLite with claim leases and conventions.
- [kanban-md](../kanban-md/index.md): the files-first counterpoint; kanban-md's board lives in your repository as markdown, Pad's lives in its database.

## Bottom line

**Recommended for solo developers and small teams who want a browser-grade tracker that agents operate as first-class users, and who accept a pre-1.0 weekly-churn dependency.**
Not for repo-native workflows where the board must be diffable files, or teams that need a mature vendor behind the tool.
My disagreeable claim: conventions-as-items is a bigger idea than the task board it ships inside, and every other member of this matrix would be better with it.

## Changes

- 2026-10-11 - Created after the topic search surfaced the conventions-and-playbooks design.
- 2026-10-11 - Added the star history chart.

## See also

- [It's a Plan](../its-a-plan/index.md) - the self-hosted platform counterpart
- [Operon](../operon/index.md) - the knowledge-vault counterpart for agent-write contracts
- [kanban-md](../kanban-md/index.md) - the markdown-files counterpoint
- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/PerpetualSoftware/pad - README: architecture, CLI, MCP catalog, claims and leases, session pushes, upgrade model (fetched 2026-10-11)
- https://getpad.dev - the site: the three-surface pitch, conventions and playbooks, the dogfooded workspace figures, Pad Cloud tiers
- https://getpad.dev/changelog - the changelog policy: signed GitHub Releases as the source of truth
- https://api.github.com/repos/PerpetualSoftware/pad - stars, forks, dates, Apache-2.0 as of 2026-10-14
- https://api.github.com/repos/PerpetualSoftware/pad/releases - v0.18.0-rc.10 (2026-10-09) and the weekly cadence
- https://hn.algolia.com/api/v1/search?query=%22pad%22%20%22getpad%22&tags=story - zero story hits as of 2026-10-14, the missing HN footprint
