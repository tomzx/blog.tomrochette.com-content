---
title: CLI Agent Orchestrator
created: 2026-10-28
updated: 2026-10-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, aws, python, tmux]
readability: 3
audience_notes: >
  Engineers choosing a supervisor layer over several coding-agent CLIs, weighing a vendor-backed framework against community tools.
  Assumes you know what Claude Code or Codex CLIs are and how tmux sessions work.
---

CLI Agent Orchestrator (CAO) is AWS Labs' Apache-2.0 Python framework that runs a local server, starts provider coding CLIs in isolated tmux sessions, and gives a supervisor agent tools to delegate work to specialist workers in parallel or sequence.

## What it is

A local `cao-server` hosts the control plane; a browser Web UI sits on localhost:9889 beside a shell CLI, an operations MCP server, and an HTTP API with PTY WebSocket streaming.
Twelve provider CLIs are documented, Kiro CLI the default, plus Claude Code, Codex, Antigravity, Hermes, Kimi, MiniMax Code, GitHub Copilot CLI, OpenCode, Oh My Pi, Cursor CLI, and Grok Build, each kept as a full CLI process with its native authentication.
The pattern is a supervisor profile: `cao install code_supervisor` gives one agent handoff, assign, and send-message tools over worker sessions, and the project adds scheduled flows, scoped skills, cross-session memory with opt-in self-learning, tool restrictions with allowlists, and an EKS example that runs a supervisor and worker fleet on Kubernetes.
It needs Python 3.10+, tmux 3.3+, and at least one authenticated provider CLI, installs from PyPI with trusted publishing, and ships an interactive course on the docs site.

## Status

Active and vendor-backed: 1,483 stars on a repository created 2025-07-29 under the awslabs org, pushed 2026-10-29, with PyPI 2.5.4 (2026-10-20) and GitHub release v2.5.3 (2026-10-08) (GitHub API, PyPI, as of 2026-10-28).
**No independent coverage exists: I found no HN thread, and the footprint is the vendor's own docs, course, and repository, the same launch-echo-only record that OpenHarness carried at admission.**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=awslabs/cli-agent-orchestrator&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=awslabs/cli-agent-orchestrator&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=awslabs/cli-agent-orchestrator&type=date&legend=top-left" />
</picture>

## Strengths

- The widest documented provider table in the category: twelve CLIs with per-provider behavior guides, mixable in one session.
- Operational depth past launching: role-based tool restrictions, cron-like flows, memory, opt-in self-learning, and a documented Kubernetes path.

## Cautions

- Vendor gravity: the default provider is AWS's own Kiro CLI and the scale example is EKS, so the happy path bends toward AWS shop shapes.
- Every claim is the vendor's own; no independent benchmark, review, or production report exists yet.
- The supervisor is an LLM driving other LLMs, so the trust question moves up a level, and the tool-restriction allowlists are the main answer CAO offers.

## Pricing

Does not apply: Apache-2.0, self-hosted; you pay the provider CLIs' own subscriptions and models.

## Compared to

OpenHarness is the peer vendor-backed command center, native-desktop with an encrypted relay, where CAO is Python-and-tmux and goes deeper on workflows, policy, and scheduled runs.
Bernstein is the counter-position: a deterministic scheduler with no LLM in the coordination loop, where CAO's supervisor is an LLM by design.
Agent Teams runs boss-and-team hierarchies in an AGPL desktop app; CAO runs the same hierarchy headless over tmux with an MCP surface and more providers.

## Bottom line

Recommended for AWS-leaning teams that want a vendor-maintained, scriptable supervisor over many coding CLIs without building the delegation layer themselves.
Not for anyone needing independent validation first, and not for local-first minimalists who will mind the Kiro and EKS defaults.

## Changes

- 2026-10-28 - Created.

## See also

- [OpenHarness](../openharness/index.md) - the standalone-ADE precedent this admission follows, vendor-backed with the same coverage caution.
- [Bernstein](../bernstein/index.md) - the deterministic, no-LLM-in-the-loop alternative to a supervisor agent.
- [Agent Teams](../agent-teams/index.md) - the desktop boss-and-team app CAO runs headless.
- [Omnara](../omnara/index.md) - the control plane that owns execution and state where CAO supervises existing CLIs.

## References

- https://raw.githubusercontent.com/awslabs/cli-agent-orchestrator/main/README.md - repository README grounding the architecture, provider list, and supervisor pattern.
- https://awslabs.github.io/cli-agent-orchestrator/ - the documentation site grounding the control-plane, flows, and course claims.
- https://pypi.org/project/cli-agent-orchestrator/ - the package, 2.5.4 released 2026-10-20 with provenance, grounding version and platform claims.
- https://api.github.com/repos/awslabs/cli-agent-orchestrator - repository metadata, counts, and dates (as of 2026-10-28).
- https://hn.algolia.com/api/v1/search?query=%22cli-agent-orchestrator%22&tags=story - the one-story HN footprint grounding the missing-coverage caution.
