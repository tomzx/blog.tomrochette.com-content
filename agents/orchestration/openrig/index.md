---
title: OpenRig
created: 2026-10-02
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, orchestration, control-plane, cross-harness, tmux, persistent-agents]
readability: 3
audience_notes: >
  Engineers who already run several Claude Code and Codex terminal sessions and want to define, boot, and restore the whole team as one managed unit.
  Assumes you know tmux, git, and what a CLI coding harness is.
---

OpenRig is an Apache-2.0, self-hosted control plane that turns ordinary Claude Code, Codex, and Pi terminal sessions into a persistent, named team defined in YAML.

**OpenRig's bet is that the missing layer is topology, not another agent: it makes the team itself the configurable, restartable artifact and treats a cross-harness team (Claude Code and Codex together) as the default rather than a feature.**

## What it is

A TypeScript daemon (a Hono HTTP server with SQLite) plus a `rig` CLI, a terminal UI, and an MCP server, built on tmux by Mike Schwarz's Esoteric Labs.
The unit is the rig: a `rig.yaml` (RigSpec) declaring pods, seats, edges, continuity policies, and a `CULTURE.md`, with reusable AgentSpec blueprints for individual agents.
The daemon boots each seat as an actual Claude Code or Codex tmux session with a stable address such as `dev-owner@first-project`, so the conversation can change while the seat keeps its name, role, and accumulated context.
Seats coordinate over the terminal itself (`rig send`, `rig broadcast`, `rig chatroom`, `rig capture`, `rig transcript`), pass owned work through `rig queue` (one owner and one state per item), and follow declared workflows and watchdogs.
Working state lives on disk as projects, missions, and slices with specs, progress, and proof; `rig down --snapshot` and `rig up <name>` snapshot and restore the team by name with a per-seat outcome, `rig discover` and `rig adopt` can absorb existing tmux sessions, and a RigBundle is a portable archive with SHA-256 integrity.
It ships no model and holds no API keys: it drives the Claude Code and Codex logins you already have.

## Status

Active and early: about 5.3k stars and 366 forks as of 2026-10-06, created 2026-04-01, 24 contributors, 94 open issues and pull requests, and v0.6.5 published 2026-10-04, with npm `@openrig/cli` at 0.6.5 after 55 versions since 2026-04-06.
**The adoption signal is thin where it matters: GitHub traction is respectable, but the Hacker News footprint is a pair of Show HN threads at 8 and 6 points plus a 2-point repost, and the documentation index still names release 0.5.14 while npm ships 0.6.5.**
The project describes itself as built by its own network of agent teams since March 2026, a self-reported claim that independent field reports do not yet corroborate.

## Strengths

- Cross-harness by default: Claude Code and Codex as peers in one rig, plus Pi and Oh My Pi through RPC runners, where much of the category pins to a single vendor.
- Persistent seats with snapshot and restore by name, reporting each seat as resumed, rebuilt, fresh, waiting on a decision or attention, or failed, which answers the which-tab-was-the-reviewer problem directly.
- Terminal-native coordination with no second API: agents message each other by typing into tmux panes, so anything a human can do in a session an agent can do.
- An agent-first CLI and MCP server (`rig_up`, `rig_ps`, `rig_send`, `rig_chatroom_send`) that lets the team manage its own topology.
- Local and self-hosted with no cloud dependency and no token markup, running on the subscriptions you already pay for.

## Cautions

- The human is still the reviewer: a Show HN commenter notes that unsupervised agents degrade quickly, and the design routes work and attention rather than removing the review step, which the author describes as operating with a hand near the wheel.
- No agent isolation: seats share the host network and filesystem through tmux, and the author confirmed in-thread that isolating agents is not solved yet, so it assumes a single trusted machine.
- Setup is invasive: it writes provider trust settings and executable hooks, edits `~/.tmux.conf`, `~/.claude.json`, `~/.codex/config.toml`, `.claude/settings.local.json`, and `.mcp.json`, and pre-trusts the workspace, with no complete preservation or rollback guarantee, so back up before first use.
- Platform limits: macOS or Linux with Node 22 or 24 and tmux; native Windows is unsupported and WSL2 is untested.
- Early and churning: 0.6.x with 39 releases in six months, documentation that lags the package, and a popularity story that leans on the author's own accounts.
- The permission model needs care: agents can run `rig` commands without repeated prompts if you accept the setup offer, and `--dangerously-interact` lets one seat answer another's permission prompt (off by default, recorded with a reason), which is the trust boundary a long-running fleet puts pressure on.

## Pricing

Free and open source under Apache-2.0.
No hosted tier, no token markup, and no OpenRig API keys; agents run on the Claude Code and Codex subscriptions you already have, so model usage is billed by those providers.

## Compared to

- [Omnara](../omnara/index.md): the other control plane that owns agent execution and state, with machine pools and dashboard, phone, CLI, API, and Slack supervision; choose Omnara for hosted execution and mobile reach, OpenRig for cross-harness teams of actual Claude Code and Codex sessions on your own machine.
- [Conductor](../conductor/index.md): the polished closed macOS GUI for parallel sessions; choose Conductor for a shallow, well-reviewed Mac workflow, OpenRig for a self-hosted daemon that defines, boots, and restores a named team.
- [Squad](../squad/index.md): a persistent agent team as versioned repo files inside GitHub Copilot CLI; choose Squad to stay inside Copilot, OpenRig for harness-independent, tmux-backed seats with a durable cross-session queue.

## Bottom line

**Recommended for terminal-native engineers who already run several Claude Code and Codex sessions and want to define, boot, and restore the team as infrastructure.**
Not for anyone who needs agent sandboxing, a Windows desktop, or a managed cloud with a support contract.

## Changes

- 2026-10-02 - Created.
- 2026-10-02 - Re-verified the note against the GitHub API, npm, and openrig.dev hours after creation: v0.6.4, 24 contributors, 39 releases, npm 0.6.4 across 54 versions since 2026-04-06, the 0.5.14 docs lag, and both HN thread point counts all confirmed, and the MCP server, discover and adopt, RigBundle integrity, and permission-override claims all checked against the live site.
- 2026-10-05 - Recorded v0.6.5 (October 4) as the latest release on GitHub and npm, and refreshed star and fork counts.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Omnara](../omnara/index.md) - the closest control-plane rival
- [Conductor](../conductor/index.md) - the closed Mac GUI incumbent
- [Squad](../squad/index.md) - the Copilot CLI team harness
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this category extends

## References

- https://openrig.dev/ - definition, self-hosted positioning, install path, and the Claude Code, Codex, and Pi framing
- https://openrig.dev/docs/getting-started - prerequisites, starters, seat and pod concepts, and the human-and-agent user model
- https://openrig.dev/what-is - architecture, primitives, and the software-factory framing
- https://github.com/mvschwarz/openrig - repository, Apache-2.0 license, stars, and the what-it-changes-on-your-machine table
- https://www.npmjs.com/package/@openrig/cli - package version 0.6.5 and the release history
- https://openrig.dev/blog/orchestrator - launch demo, the two-orchestrator high-availability pair, and the September 2026 permission-override update
- https://openrig.dev/blog/cross-harness-agents - the cross-harness thesis and the terminal-as-transport mechanism
- https://esoteric.run/blog/why-i-built-openrig - the author's design rationale and the restore-everything motivation
- https://openrig.dev/compare/claude-managed-agents - the managed-cloud counterpart and the local-versus-hosted split
- https://news.ycombinator.com/item?id=47772935 - the Show HN launch thread and the supervision concern
- https://news.ycombinator.com/item?id=48241066 - the control-plane thread and the agent-isolation question
