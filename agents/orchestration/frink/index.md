---
title: Frink
created: 2026-10-21
updated: 2026-10-21
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, workflows, desktop, triggers]
readability: 3
audience_notes: >
  Engineers who want coding-agent runs to start themselves from tickets, errors, or schedules,
  and to stop for approval before anything ships. Assumes you already run Claude Code, Codex,
  OpenCode, GitHub Copilot, or Cursor and are comfortable reviewing diffs in a desktop app.
---

Frink is a free, MIT-licensed desktop app (macOS and Linux) that runs up to four coding agents side by side in worktrees and turns plain-language routines into Flows, multi-step workflows that start on a schedule, a webhook, or an event from tools like Linear, Shortcut, ClickUp, Sentry, PostHog, or Vercel.

**Frink's bet is that the trigger, not the session, is what turns an agent from a chat into infrastructure: define the routine once, and the app runs it, waits at approval steps, and queues everything that needs you.**

## What it is

A desktop application from benord-labs, TypeScript under MIT, with its repository created 2026-09-26.
The main window splits into up to four panes, each pane an agent (Claude Code, Codex, OpenCode, GitHub Copilot, or Cursor) with its own model and its own diff to review, and each chat can run in a worktree that copies untracked files like `.env` and runs setup commands from a committed `.frink/worktrees.json`.
Flows are the automation half: exactly one trigger (manual, webhook, schedule, or post-task) starts a graph of agent, command, approval, condition, and custom JavaScript steps, with data passing between blocks through `{{previous.*}}` templates.
Every run from every project lands in a Work Queue with states from Pending through Plan Ready, Needs Attention, and Ready for review, so approvals and agent questions wait behind a badge.
Plugins connect Linear, Shortcut, ClickUp, Sentry, PostHog, Vercel, GitHub, Notion, and Slack as chat tools and Flow triggers, and MCP servers attach the usual way.
It is local-first: chats, Flows, and tasks live in SQLite on your machine, no account is needed, agent logins stay with the tools themselves, and the telemetry doc lists exactly what official builds send.

## Status

Active and very young: 58 stars and 5 forks as of 2026-10-21, repository created 2026-09-26, default-branch pushes through 2026-10-23, and a steady release train (0.2.0 on October 6, 0.3.0 on October 8, 0.4.0 on October 16) (GitHub API and releases, as of 2026-10-23).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=benord-labs/frink&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=benord-labs/frink&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=benord-labs/frink&type=date&legend=top-left" />
</picture>

No independent coverage exists as of 2026-10-21: searching the name surfaces the Frink programming language and Frinkiac, not this product.
**The missing community footprint is itself the status signal: four weeks of shipping and documentation are the only evidence there is.**

## Strengths

- The trigger catalog is the widest in its cohort: schedules, any webhook, and six named event sources feed the same Flow engine the chat can author in plain language.
- Approval steps are first-class Flow blocks, so unattended runs stop at named gates instead of finishing unreviewed.
- Worktree mode copies untracked files and runs committed setup commands, so an agent's checkout is usable the moment it opens.
- Per-agent diffs, a built-in editor, rollback, and the Work Queue cover the review loop inside one window.
- Custom steps are JavaScript ES modules in `~/.frink/nodes/` that you or the agent writes and reuses across Flows.

## Cautions

- Four weeks old, 58 stars, one organization, zero independent coverage: bus factor and longevity are unknowns.
- Flows run only on Claude or OpenAI accounts; a project on OpenCode, GitHub Copilot, or Cursor cannot run Flows yet (docs, as of 2026-10-21).
- Everything runs on your computer while Frink is open, so this is a desktop scheduler, not a server; nothing executes unattended with the app closed.
- Windows is announced on the pricing page but not shipped.
- The name collides with the Frink calculator language, which will hurt search and citation.

## Pricing

Free: every feature, no account, no card (frink.dev/pricing, as of 2026-10-21).
You bring your own agent subscriptions or API keys; a pasted API key is stored encrypted on your machine.

## Compared to

- [Archon](../archon/index.md): also trigger-led, with Slack, Telegram, GitHub, and Discord triggers, but it encodes workflows as committed YAML; choose Frink when you want the desktop app and plain-language flow authoring.
- [Conductor](../conductor/index.md): the deeper Mac review surface for parallel sessions, with no triggered automation; choose Frink when the runs should start themselves.
- [OpenChamber](../../surfaces/openchamber/index.md): scheduled sessions without a workflow engine; Frink's Flows chain agent, command, and approval steps under one trigger.

## Bottom line

Recommended for engineers who want ticket-, error-, and schedule-driven agent routines with human approval gates, on their own machine.
Not for headless or server-side automation, and not for anyone who needs a track record before adopting.

## Changes

- 2026-10-21 - Created.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Archon](../archon/index.md) - the YAML workflow engine with the closest trigger model
- [Conductor](../conductor/index.md) - the Mac parallel-session counterpart without triggers
- [Crewplane](../crewplane/index.md) - the CLI workflow runner that owns the same seat from the terminal
- [OpenChamber](../../surfaces/openchamber/index.md) - scheduled sessions, the lighter scheduling answer

## References

- https://github.com/benord-labs/frink - repository, feature table, supported agents, license, and install builds
- https://frink.dev/ - product page, download surfaces, and the no-account positioning
- https://frink.dev/pricing - free, every feature, no account, no card (as of 2026-10-21)
- https://api.github.com/repos/benord-labs/frink - stars, forks, dates, license, and language (as of 2026-10-21)
- https://api.github.com/repos/benord-labs/frink/releases - the 0.2.0, 0.3.0, and 0.4.0 release train
- https://raw.githubusercontent.com/benord-labs/frink/main/user-docs/flows.md - flow anatomy, the one-trigger rule, and the Claude/OpenAI limitation
- https://raw.githubusercontent.com/benord-labs/frink/main/user-docs/plugins.md - the plugin kinds and the trigger catalog
- https://raw.githubusercontent.com/benord-labs/frink/main/user-docs/worktree-setup.md - worktree mode, .env copying, and setup commands
- https://raw.githubusercontent.com/benord-labs/frink/main/user-docs/task-lifecycle.md - task states and the approval model
