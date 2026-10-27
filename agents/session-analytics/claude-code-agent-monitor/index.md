---
title: Claude Code Agent Monitor
created: 2026-10-10
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, observability, claude-code, codex, cursor, open-source]
readability: 3
audience_notes: >
  Engineers running Claude Code, Codex, or Cursor who want one live local view over all of them, and anyone comparing live session-analytics mechanisms.
  Assumes you know what a session transcript and a hook event are.
---

Claude Code Agent Monitor (CCAM) is an MIT-licensed local dashboard that watches Claude Code, Cursor, and Codex sessions in real time through native hooks and transcript discovery, rendering conversations, agent trees, token cost, and workflow analytics in one web interface.

**CCAM is the broadest live view in this category and the only member that watches Cursor live, and it pushes one step past observation into operation: the same dashboard can launch, steer, and resume the agents it watches, which makes it partly an operations tool rather than only an analytics one.**

## What it is

A Node.js application (22.22 or newer) built on Express, React, SQLite, and WebSockets, run from source (npm run setup, with the dashboard on localhost:5173 in development and 4820 in production), as Electron desktop apps (macOS DMG and Windows NSIS or portable), or in Docker and Podman with Kubernetes and Terraform deployment docs.
Claude Code and Codex report through their native hooks, while Cursor rides compatible live events plus native `~/.cursor` transcript discovery, and history import pulls Claude transcripts from `~/.claude` and Codex rollouts from `~/.codex/sessions` with snapshot retention so conversations survive source removal; since v2.4.0 a remote-ingest endpoint accepts transcript uploads from machines that cannot run hooks locally.
The views cover live fleet state, full conversations with rendered Markdown and tool-specific renderers, parent-child agent trees, workflow analytics across eleven D3 sections, alerts with webhook fan-out to 14 providers, and configuration explorers that inspect Claude Code and Codex settings, skills, hooks, MCP servers, rules, plugins, and memory.
Cost tracking is configurable per model and per session, with dated introductory rates, per-subagent cost, the 272K GPT token boundary, and separate Cursor-native and third-party pricing catalogs.
A `ccam` CLI and a local MCP server (103 typed tools across 16 modules) expose the same data to agents and scripts, and the repository also ships 14 plugins, 66 plugin skills, 18 subagents, 34 commands, and 77 repository skills.
Made by hoangsonww under MIT, listed under Session Monitors in the awesome-claude-code directory.

## Status

Young and active: 1,061 stars, 261 forks, created 2026-03-05, pushed 2026-10-23, latest release v2.4.5 on 2026-10-23 (a release-tooling version bump with no feature changes) after v2.4.4 on 2026-10-22 (patch releases that count events_today from local midnight and repair the release tooling), v2.4.0 on 2026-10-20, and v2.3.0 on 2026-10-10, as of 2026-10-25.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=hoangsonww/Claude-Code-Agent-Monitor&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=hoangsonww/Claude-Code-Agent-Monitor&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=hoangsonww/Claude-Code-Agent-Monitor&type=date&legend=top-left" />
</picture>

One maintainer writes almost all of it: hoangsonww has 963 commits against 36 for the next contributor, as of 2026-10-19.
The community footprint is nearly empty: a single 1-point Hacker News thread from 2026-05-05 and no Reddit discussion I could find, so distribution runs through the directory listing and the star curve rather than through public argument.
**A single-maintainer control room with genuine adoption signals and no independent scrutiny, so read its docs and issue tracker rather than its README claims before depending on it.**

## Strengths

- The broadest live coverage in the category: Claude Code, Codex, and Cursor in one view, where agents-observe stops at two harnesses and every archive tool starts after the run.
- Live hooks and retrospective transcript import in one tool, so a machine crash loses nothing the transcripts still hold.
- Operational reach no other member has: launch, steer, resume, and reattach to agents from the dashboard, with concurrency caps and same-origin protection on spawning.
- Configuration inspection is unique here: twelve-tab explorers over Claude Code and Codex skills, hooks, MCP, rules, plugins, and memory, with backup-first edits and symlink-escape guards.
- The delivery surface is serious for its age: desktop apps, containers, Kubernetes and Terraform docs, remote push ingestion for machines behind NAT, alerts, five UI languages, and a local MCP server.

## Cautions

- One maintainer carries 962 of roughly 1,016 commits, and the surface they carry is enormous (14 plugins, 66 plugin skills, 77 repository skills, 103 MCP tools), a lot of audit area for a bus factor of one.
- No independent scrutiny: one 1-point Hacker News thread and no third-party review, so the cost and workflow numbers rest on the project's own claims.
- The run-and-resume control overlaps the mission-control tool family (claudecodeui and neighbors) that sits outside this section's notes, so adopters should know they are taking on an operations tool, not only an analytics one.
- It reads the same transcripts everyone else does, so it inherits the harness undercount caveats (Claude WebSearch side-calls and friends) that the other members document.
- Node 22.22 or newer is a hard floor, and the release train moves fast enough that a long-running deployment needs its own upgrade discipline.

## Pricing

Free and open source under MIT.
No paid tiers are published, and nothing in the default path requires a hosted service.

## Compared to

- [agents-observe](../agents-observe/index.md): the lighter plugin path for Claude Code and Codex live observation; CCAM adds Cursor, history import, and agent control at the price of a much larger surface.
- [claude-devtools](../claude-devtools/index.md): the deepest retrospective reconstruction of one Claude Code session; CCAM trades that per-turn depth for breadth and a live view.
- [Token Monitor](../token-monitor/index.md): the always-on usage and limits widget across 47-plus tools; CCAM watches fewer tools but reads their conversations and can drive them.

## Bottom line

**Recommended for engineers running two or more of Claude Code, Codex, and Cursor who want one local control room that watches sessions and can drive the agents behind them.**
Not for minimal-footprint audit tooling (ccusage and AgentTrace stay far smaller), and not for anyone who needs many maintainers or independent verification behind a dependency.

## Changes

- 2026-10-10 - Created.
- 2026-10-19 - Rotation re-verification: every cited URL re-fetched and live, no release after v2.3.0 with one outside-contributor fix merged unreleased on 2026-10-17 (a custom title equal to the folder name no longer overwritten), the one-point Hacker News footprint unchanged, and repository and contributor counts refreshed (forks 248 to 251, hoangsonww 962 to 963 commits).
- 2026-10-21 - Recorded v2.4.0 (2026-10-20): the custom-title fix released, a remote-ingest endpoint accepting transcript uploads (POST /api/hooks/ingest-transcript), automated version-bump pull requests, and two first-time outside contributors (lasse-tech, houdinisparks); repository counts refreshed (forks 251 to 253), and the pushed date moved to 2026-10-20.
- 2026-10-25 - Recorded v2.4.5 (2026-10-23), a release-tooling version bump with no feature changes; repository counts refreshed (forks 253 to 261) and the pushed date moved to 2026-10-23.

## See also

- [agents-observe](../agents-observe/index.md) - the lighter live-view member this tool broadens
- [claude-devtools](../claude-devtools/index.md) - the retrospective depth play for the same primary harness
- [Token Monitor](../token-monitor/index.md) - the live widget alternative for usage and limits
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins

## References

- https://raw.githubusercontent.com/hoangsonww/Claude-Code-Agent-Monitor/master/README.md - the product summary, deployment options, extension counts, and local-first security statements
- https://raw.githubusercontent.com/hoangsonww/Claude-Code-Agent-Monitor/master/README-EN.md - the full feature reference: hooks and Cursor live events, history import, cost tracking, the MCP server, alerts, desktop apps, and the Run Claude controls
- https://api.github.com/repos/hoangsonww/Claude-Code-Agent-Monitor - 1,058 stars, 245 forks, MIT license, created 2026-03-05, pushed 2026-10-10, as of 2026-10-10
- https://api.github.com/repos/hoangsonww/Claude-Code-Agent-Monitor/releases - v2.4.5 (2026-10-23), v2.4.4 (2026-10-22), v2.4.3 (2026-10-21), v2.3.0 (2026-10-10), v2.2.6 and v2.2.5 (2026-10-04) (re-fetched 2026-10-25)
- https://api.github.com/repos/hoangsonww/Claude-Code-Agent-Monitor/contributors - the maintainer concentration behind the single-maintainer caution
- https://hn.algolia.com/api/v1/search?query=Claude-Code-Agent-Monitor - the one 1-point thread behind the empty-community-footprint claim
- https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/HEAD/README.md - the Session Monitors listing that grounds the distribution claim
