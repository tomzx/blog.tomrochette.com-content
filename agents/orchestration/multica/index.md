---
title: Multica
created: 2026-09-27
updated: 2026-09-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, orchestration, self-hosted, issue-tracking, agents-as-teammates]
readability: 3
audience_notes: >
  Teams assigning work to coding agents on a shared board, weighing a source-available self-hosted platform.
  Assumes you run one or more agent CLIs and are comfortable operating Postgres if you self-host.
---

Multica is a source-available, self-hostable workspace that treats coding agents as teammates, letting a team assign issues to agent CLIs and track their runs, comments, diffs, and skills in one place.

**Multica's bet is that the right abstraction for agent work is the issue, not the prompt: make agents first-class assignees with profiles and runtimes, and the durable artifact becomes the ticket that connects intent, execution, decisions, and the diff.**

## What it is

A platform from multica-ai (the LICENSE names Index Labs (Hong Kong) Limited) with a Next.js frontend, a Go backend, and PostgreSQL with pgvector, offered as a desktop app plus a self-hosted server (Docker Compose, single binary, or Kubernetes/Helm).
You create an agent with a name, provider, and runtime; the runtime is a daemon on any connected machine (a laptop or a cloud box) that auto-detects installed agent CLIs and executes the work there.
An issue assigned to an agent moves through enqueue, claim, start, and complete or fail, streaming progress to the UI, and the platform adds squads, reusable skills, autopilots on a cron, chat, projects, execution-log replay, run steering, usage analytics, review gates, an inbox, and automatic retries.
It self-describes as supporting 26 agent CLIs (Claude Code, Codex, Cursor, Copilot, Kimi, OpenCode, and more), integrates with GitHub, GitLab, Gitea, and Forgejo plus Slack, Lark, DingTalk, WeCom, and Telegram, and ships desktop and iOS apps.

## Status

Actively shipped and unusually high-profile: about 51,631 stars and 6,668 forks as of 2026-09-29, created 2026-01-13, with 1,703 open issues and a latest release of v0.6.0 on 2026-09-28.
Releases land every one to three days, which corroborates real maintenance.
**Two caveats travel with the headline number: the star count is extraordinary for an eight-month-old repo, and independent reviewers found at least eight near-identical zero-star clones carrying the same marketing description, a pattern associated with star farming, while the license is a custom Apache-2.0-derived "Multica License" that GitHub reports as NOASSERTION.**

## Strengths

- The issue-and-assignee model maps onto how teams already work, and the runtime abstraction cleanly separates where code runs from who can invoke it.
- Broad agent-CLI support (26 claimed) with daemon auto-detection, so it is a layer over the tools you already use rather than a new harness.
- Self-hostable end to end, with any Git host and five chat integrations, and no GPU requirement because it runs no models itself.
- Strong operational surface: execution-log replay, run steering, review gates, retries and timeouts, and per-run usage analytics.
- Desktop app plus web plus iOS, so a team can watch and unblock work from wherever it works.

## Cautions

- The star count is a caveated signal: reviewers flag fast growth for the repo's age and multiple near-identical clones, though forks, issues, and commit volume suggest genuine activity underneath.
- The license is not plain Apache-2.0: the Multica License adds conditions on hosted services and commercial embedding, so read it before either use.
- Skills do not compound automatically yet; reviewers report most teams still hand-write them like runbooks.
- Self-hosting means operating PostgreSQL with pgvector, and agent failure modes (loops, repeated state transitions) can swamp a human-run board.
- No published pricing page was found; hosted pricing exists only behind a free trial and a sales conversation, and self-hosted images can lag the cloud by a release.

## Pricing

No public price table was found on multica.ai as of 2026-09-27; the site offers a free trial and a "talk to sales" path, and self-hosting requires no hosted account.
The source is available under the custom Multica License; agents run on your own provider accounts, and Multica does not charge for tokens.

## Compared to

- [Omnara](../omnara/index.md): an Apache-2.0 control plane where agents are YAML and supervision spans dashboard, phone, CLI, API, or Slack; choose Multica for an issue-board and teammate model with a desktop and mobile app.
- [LobeHub](../lobehub/index.md): a Chief Agent Operator that hires, schedules, and reports on agents; choose Multica when the unit of work is a ticket assigned to a named agent.
- [Superset](../superset/index.md): a local IDE for parallel worktree sessions; choose Multica when work is team-scoped and needs assignment, review gates, and an audit trail.

## Bottom line

**Recommended for teams of two to ten already running coding agents who want to assign issues to them on a shared, self-hostable board with review gates and an audit trail.**
Not for solo developers running one agent, teams needing per-agent budget caps today, or anyone unwilling to read a custom license or operate Postgres.

## Changes

- 2026-09-27 - Created.
- 2026-09-29 - Recorded v0.6.0 (September 28) and refreshed star and issue counts.
- 2026-09-29 - Reworded two banned-term compounds ("team-shaped", "human-shaped") to plain wording, meaning unchanged.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Omnara](../omnara/index.md) - the YAML-config control plane alternative
- [LobeHub](../lobehub/index.md) - the agent-hiring and scheduling platform
- [Superset](../superset/index.md) - the local parallel-session IDE
- [Managing Many Concurrent LLM Agent Sessions](../../../managing-many-llm-agent-sessions/index.md) - the supervision problem Multica answers

## References

- https://github.com/multica-ai/multica - repository, architecture, agent support, license metadata, stars, and release data
- https://multica.ai/ - product positioning, teammate model, runtimes, and integrations
- https://multica.ai/docs - issues, agents, squads, skills, autopilots, runtimes, runs, and security model
- https://raw.githubusercontent.com/multica-ai/multica/HEAD/LICENSE - the custom Multica License and its hosted-service and commercial-embedding conditions
- https://www.promptquorum.com/power-local-llm/multica-review - the star-count caveat, the license analysis, and the absence of a public price table
- https://andrew.ooo/posts/multica-open-source-managed-agents-platform/ - independent review of the runtime abstraction and its limitations
