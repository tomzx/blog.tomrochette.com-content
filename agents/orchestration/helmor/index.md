---
title: Helmor
created: 2026-09-27
updated: 2026-09-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, orchestration, worktrees, local-first, desktop]
readability: 3
audience_notes: >
  Engineers deciding between local-first desktop workbenches for parallel coding agents.
  Assumes you already run Claude Code, Codex, or Cursor and know what a git worktree is.
---

Helmor is an Apache-2.0, local-first desktop workbench that orchestrates coding agents across git worktrees through planning, running, review, testing, merge, and shipping loops.

**Helmor's bet is that the part AI did not accelerate is finishing the loop, so it wraps agents in the review, test, merge, and one-click PR steps that stand between a generated diff and shipped software.**

## What it is

A desktop app (Tauri plus React, buildable from source with Bun) from dohooo that runs Claude Code, Codex, Cursor, OpenCode, and Kimi Code, each in its own git worktree and branch under `~/helmor/workspaces/`.
Every workspace holds the conversation, diffs, a Monaco editor, and terminals side by side, with one-click actions to create a PR or MR, merge, fix CI, resolve conflicts, and stack PRs against GitHub or GitLab.
Agent CLIs are bundled so there is nothing extra to install, and it adds a `helmor` CLI and an MCP server over stdio so a terminal or another agent can drive it, plus skills, a quick-launch panel (Shift+Option+Space), a Terminal Mode that runs prompts in the agent's native TUI, and an experimental mobile companion over a Cloudflare tunnel.
macOS (Apple Silicon and Intel) and Windows x64 are the supported desktop platforms.

## Status

Active but cooling: about 1,308 stars and 120 forks as of 2026-10-02, created 2026-04-02, with 1,831 commits.
The latest release, v0.46.0 (which added Codex 1.0 and Claude Code 2.0 support), landed 2026-07-24, and the last default-branch commit was 2026-08-22, roughly six weeks before this check, so momentum has slowed even as the feature set matured.
**For a tool still advertising forthcoming plan mode and Slack and GitHub context, a six-week quiet spell is the first data point to watch between now and the next release.**

## Strengths

- The full loop, not just dispatch: review, test, merge, fix CI, and PR/MR creation from one window, including stacked PRs.
- Local-first by construction: everything lives under `~/helmor/`, credentials stay on the machine, and there is no cloud dependency.
- Apache-2.0 and community-oriented (Discord, discussions, source-available architecture docs).
- Bundled agent CLIs and bring-your-own logins and providers, so setup is one download.
- A CLI and MCP server make it scriptable and drivable by other agents, and the quick panel lowers the cost of starting a task.

## Cautions

- Six weeks without a commit and the last release in July 2026 as of 2026-10-02; treat the roadmap items as unshipped.- Desktop only, and no Linux build; the macOS DMG is around 462 MB.
- Its documentation site (docs.helmor.ai) did not resolve during this run, so the README and releases are the practical documentation.
- Review is local and Git-host-facing; there is no fleet-scale issue board or cloud execution.
- Independent coverage is thin and mostly directory listings; the recurring open question is whether teams want another orchestration surface rather than better defaults inside the agents they already use.

## Pricing

Free and open source under Apache-2.0.
No paid tier, no hosted service, and no token markup; agents run on your own logins and subscriptions.

## Compared to

- [Conductor](../conductor/index.md): the closed, better-funded Mac dashboard with the deepest review flow; choose Helmor for an open license, Windows support, and local-first credentials.
- [Superset](../superset/index.md): source-available and macOS-first with SDK programmability; choose Helmor for a shipped Windows build and one-click PR and merge actions.
- [Orca](../orca/index.md): MIT and cross-platform with a mobile companion and 27 agents; choose Helmor for a leaner workbench centered on finishing the loop.

## Bottom line

**Recommended for macOS or Windows engineers who want an open, local-first workbench that carries agent work through review, test, merge, and one-click PR.**
Not for Linux users, and not for anyone who needs fleet-scale orchestration or assurance of active development.

## Changes

- 2026-09-27 - Created.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Conductor](../conductor/index.md) - the closed Mac review-first incumbent
- [Superset](../superset/index.md) - the source-available macOS IDE
- [Orca](../orca/index.md) - the cross-platform ADE
- [Lanes](../lanes/index.md) - the board-first macOS workspace

## References

- https://github.com/dohooo/helmor - repository, feature set, license, stars, and last-commit date
- https://helmor.ai/ - product positioning, current version, and download platforms
- https://raw.githubusercontent.com/dohooo/helmor/HEAD/README.md - workspaces, agents, review and ship features, CLI, and MCP server
- https://github.com/dohooo/helmor/releases - release cadence and v0.46.0 notes
- https://hysenlabs.com/en/projects/dohooo-helmor - independent summary of the local-first worktree model
