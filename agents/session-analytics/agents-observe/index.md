---
title: agents-observe
created: 2026-09-16
updated: 2026-09-16
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, observability, claude-code]
readability: 3
audience_notes: >
  Engineers running Claude Code or Codex agent teams who want to watch what their agents are doing while it happens, not after.
  Assumes you know what Claude Code hooks and a subagent tree are.
---

agents-observe is an MIT-licensed real-time observability dashboard for Claude Code and Codex sessions: a Claude Code plugin whose hooks stream every agent event to a local Dockerized server that feeds a live web dashboard with multi-agent trees, replay, and token and cost breakdowns.
Facts below verified as of 2026-09-21.

**agents-observe is the live half of session analytics: it watches the hook stream while your agents run, where the category's other tools only parse what the agents already wrote to disk.**

## What it is

A Claude Code plugin (`claude plugin marketplace add simple10/agents-observe`) that registers hooks on every agent event, a Node shim that POSTs each event to an API server running as a Docker container, and a React dashboard on localhost:4981 that renders the stream live over websockets from a local SQLite store.
The dashboard groups events into agent and subagent trees, expands any event to its full payload (command, tool call, result), filters and searches across sessions, and replays past sessions; version 0.9.7 added per-session token usage and cost breakdowns.
Codex is supported through a manual CLI path, and the prerequisites are Docker, Node.js, and bash, without which the plugin fails to load.
Made by simple10, an independent developer, under MIT.

## Status

Young and active: 679 stars, 68 forks, created 2026-03-26, pushed 2026-09-04, latest release v0.9.12 on 2026-07-22 as of 2026-09-21.
Launched on Hacker News on 2026-04-01 with 77 points.
**A single-maintainer project that found a real gap (live multi-agent visibility) and a real audience, but it is pre-1.0 with months between releases.**

## Strengths

- The one genuinely live cell in its category: hook events stream into the dashboard as agents run, so you watch a subagent tree work instead of reconstructing it from logs.
- Full-payload transparency: every event expands to the raw tool call, command, and result, which is the ground truth the terminal hides.
- Replay, filtering, and token and cost breakdowns give it retrospective value too, not just live view.
- Easy entry through the Claude Code plugin marketplace, with `/observe` skills for status, logs, and debugging.

## Cautions

- Two harnesses only, Claude Code and Codex, against agentsview's 60-plus auto-discovered formats.
- The architecture carries weight a single user may not want: hooks, Node, and a Docker server for what is a local single-player setup, an HN commenter challenged exactly this and the author's answer leaned on latency (a background hook shim cut per-hook overhead from roughly 50-60 ms to 3-5 ms).
- Pre-1.0, single maintainer, and the last release shipped in July, so expect churn and gaps.
- Its launch thread featured an exchange about bot comments, with the author acknowledging that recently created "green" accounts had inflated the discussion, a discount to apply to its community traction.

## Pricing

Free and open source under MIT.
No paid tiers are published.

## Compared to

- [agentsview](../agentsview/index.md): the retrospective complement, indexing 60-plus agent formats after the fact for multi-month cost and history questions; choose agents-observe for right-now visibility, agentsview for the archive.
- [ctx](../ctx/index.md): a search-and-provenance CLI whose consumer is your next agent session; neither tool replaces the other's job.
- Harness-native views (Claude Code's own status and cost displays): zero-install and authoritative for one session, but single-session and tree-blind; agents-observe exists because those views cannot show a five-subagent fan-out.

## Bottom line

**Recommended for Claude Code (and Codex) users running agent teams who want to see what each agent is doing now, replay it after, and keep token costs visible.**
Not for multi-harness archive analytics, code provenance, or anyone unwilling to run Docker and Node alongside their coding agent.

## Changes

- 2026-09-16 - Created.

## See also

- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison whose live-observation gap this note fills
- [agentsview](../agentsview/index.md) - the retrospective archive this tool complements
- [ctx](../ctx/index.md) - the search-and-provenance CLI in the same category
- [Claude Code](../../harnesses/claude-code/index.md) - the harness whose hooks feed the whole pipeline

## References

- https://github.com/simple10/agents-observe - repository, description, MIT license, stars and forks as of 2026-09-21
- https://raw.githubusercontent.com/simple10/agents-observe/main/README.md - architecture, plugin install, prerequisites, skills, token and cost breakdowns
- https://github.com/simple10/agents-observe/releases - v0.9.12 release date
- https://news.ycombinator.com/item?id=47602986 - the launch thread, 77 points on 2026-04-01
- https://hn.algolia.com/api/v1/items/47602986 - thread content: the server-necessity challenge and answer, the hook latency numbers, the bot-comment exchange
