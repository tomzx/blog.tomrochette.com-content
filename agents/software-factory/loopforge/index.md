---
title: LoopForge
created: 2026-11-21
updated: 2026-11-21
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, software-factory, sop, workflow-engine, self-hosted, docker]
readability: 3
audience_notes: >
  Teams that want one saved, gated delivery workflow to carry every coding-agent requirement
  from intake to merged pull request. Assumes you know what a workflow node, a sandbox,
  and a human approval gate are.
---

LoopForge is Tencent's MIT-licensed, self-hosted delivery platform for coding agents: a chat workbench where a Main Bot drives a Docker sandbox from a conversation, beside an SOP engine that runs saved workflows of agent, script, human-gate, sub-SOP, and preview nodes in order, so a way of working that proves itself in chat becomes the fixed pipeline every later requirement follows.

## What it is

**The product's bet is that a factory's process should be a stored, editable SOP, not a per-task prompt: chat explores, the SOP repeats.**
A deployment is a Go server you start with Docker Compose (a pinned ghcr.io image, port 8090), with MySQL state, per-run Docker sandboxes that check out your repositories, and a web console.
Ten coding-agent CLIs serve as executors: CodeBuddy, Codex, Claude Code, OpenCode, Cursor CLI, Antigravity, Kimi Code, Pi, DeepSeek Harness, and ZCode, with CodeBuddy and Codex bundled in the image and the rest installed on first use.
Roles (planner, implementer, reviewer, tester) carry their own prompt, executor, model, rules, Skills, and MCP tools, built-in blueprint SOPs cover backend, frontend, product proposal, and bug fix, and a visual SOP designer edits the graph with rework edges back to earlier steps.
Around the engine it adds a LoopForge Local edition (`npx loopforge-cli`) that runs the delivery workflows inside Claude Code, Codex, CodeBuddy, or Cursor, optional GitHub OAuth (SSH keys work for GitLab, Gitea, or Gogs), token and cost reporting per requirement, an OpenAPI-described HTTP API with MCP exposure, scheduled AI tasks, and WeCom notifications.

## Status

Active and trending: 5,352 stars, 738 forks, and 277 open issues since creation on 2026-07-28, pushed 2026-11-21, MIT (a Tencent LICENSE file that grants MIT beside a third-party-components list, which GitHub's classifier reads as no standard license), per the GitHub API as of 2026-11-21.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Tencent/LoopForge&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Tencent/LoopForge&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Tencent/LoopForge&type=date&legend=top-left" />
</picture>

**The train moves weekly (v0.3.6 on 2026-11-11, v0.3.8, v0.4.0 on 2026-11-17, v0.4.1-rc.1 on 2026-11-20), 16 contributors commit to it, and the launch drew third-party writeups, though no Hacker News story exists about it (the search's hits name the unrelated LoongForge, 2026-11-21).**
The breakout was mid-November 2026: roughly 700 stars with 174 gained in one day around 2026-11-14 per the GitHub counters third-party coverage cites, and the repository's trendshift badge now sits in the README.
Independent coverage is young and thin: a podcast walkthrough of the Compose install, a directory listing, and one substantive third-party review, whose critical read is the closest thing to evaluation the platform has.

## Strengths

- **The SOP is a first-class artifact**: a delivery workflow is stored, versioned, visually editable, and re-runnable, with agent roles, deterministic script nodes, human gates, sub-SOPs, and preview builds as node kinds, the clearest process-as-stored-workflow statement in this category.
- Deterministic scripts sit inside the loop where they belong: tests, lint, and reports run as script nodes no agent can talk past, and failed checks rework the run to an earlier step.
- **Every run keeps evidence**: node status, tool traces, worker logs, per-node artifacts, retry or rerun from any node, and token cost rolled up per requirement rather than per API key.
- The executor roster is the widest in the category, ten CLIs with a managed daily updater that verifies npm integrity by SRI before running lifecycle scripts.

## Cautions

- **The sandbox is the host's Docker socket**, which third-party coverage rightly calls root-equivalent trust on the host: new installs listen on all interfaces on port 8090, the first registered account becomes administrator, and open signup is a default you must turn off.
- **Tencent's own CodeBuddy gets the gravity**: requirement clarification, notification summaries, and scheduled assistant tasks pin their model pickers to CodeBuddy and reject other CLIs rather than silently swapping, so a team standardizing on Claude Code meets the edge in three subsystems.
- The built-in SOPs are read-only templates, not drop-in production paths, and SOP export from the platform to LoopForge Local is documented as planned, not shipped.
- No Hacker News discussion and no independent evaluation exist as of 2026-11-21; the validation record the repository links (one four-role CodeBuddy run, three passing tests, a human gate) is the maker's own.

## Pricing

MIT, free, and self-hosted on your own Docker host; there is no hosted tier and no published prices.
You bring model keys for whichever executors your roles select.

## Compared to

- [SuperPlane](../superplane/index.md) is the closest peer: both are Go platforms owning the intake-to-PR line with durable run records; SuperPlane gates intake by confidence and prices hosted plans, LoopForge gates delivery with stored SOPs and ships no hosted tier.
- [Machinist](../machinist/index.md) splits the loop across a control plane that never starts agents and dial-in runners you own; LoopForge's engine runs the SOP itself inside your Compose stack.
- [Fusion](../fusion/index.md) owns the loop board-first with per-step gates and auto-merge; LoopForge's loop is the saved SOP, and acceptance ends at a human gate rather than an automatic merge.
- [Open SWE](../open-swe/index.md) is the hosted-stack alternative that needs LangSmith's Managed Deep Agents; LoopForge runs entirely on your host against the CLIs already installed.

## Bottom line

**Recommended for a trusted team that wants one auditable, gated delivery workflow around the coding CLIs it already pays for, on hardware it controls.**
Not for a solo developer inside one harness, not for multi-tenant exposure, and not for anyone who needs independent evaluation or a stable 1.0 first.

## Changes

- 2026-11-21 - Created from the varun1505 2026-11-14-through-11-19 sweep resolution (the list's Tencent/LoopForge entry, 5,352 stars as of 2026-11-21), admitted on the SuperPlane platform line with the stored-SOP loop as the differentiator and the zero-HN footprint recorded.

## See also

- [SuperPlane](../superplane/index.md) - the platform factory this note's SOP-owned loop is measured against
- [Machinist](../machinist/index.md) - the control-plane-and-runners alternative that never starts an agent
- [Fusion](../fusion/index.md) - the board-first loop with auto-merge, beside the SOP's human-gate ending
- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - where the SOP-engine column sits among the factories

## References

- https://github.com/Tencent/LoopForge - repository, the chat-plus-SOP model, executor roster, and license (GitHub API, as of 2026-11-21)
- https://raw.githubusercontent.com/Tencent/LoopForge/main/README.md - the SOP node kinds, built-in blueprints, LoopForge Local, FAQ positioning against Dify and n8n, and the trendshift badge
- https://raw.githubusercontent.com/Tencent/LoopForge/main/LICENSE - the MIT grant with the third-party-components preamble
- https://raw.githubusercontent.com/Tencent/LoopForge/main/docs/deployment.md - the deployment runbook: pinned image, first-use CLI installs, the managed updater's SRI checks, and the CodeBuddy defaults
- https://api.github.com/repos/Tencent/LoopForge/releases - the release train, v0.4.1-rc.1 (2026-11-20) newest as of 2026-11-21
- https://loopforge.cn - the product site: MIT, self-deployable, cloud sandboxes, shared sessions, gated SOPs
- https://explainx.ai/blog/tencent-loopforge-self-hosted-sop-coding-agents-claude-codex-2026 - the third-party critical read: the Docker-socket trust call, the 0.0.0.0:8090 and first-admin defaults, the CodeBuddy-pinned subsystems, and the planned-not-shipped SOP export
- https://hn.algolia.com/api/v1/search?query=loopforge&tags=story - the footprint scan finding no story about the platform (the hits name the unrelated LoongForge, 2026-11-21)
- https://github.com/varun1505/awesome-software-factories - the third-party curated list that surfaced this note
