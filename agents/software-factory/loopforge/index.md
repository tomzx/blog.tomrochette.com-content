---
title: LoopForge
created: 2026-11-21
updated: 2026-11-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, software-factory, sop, workflow-engine, self-hosted, docker]
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
Ten coding-agent CLIs serve as executors: CodeBuddy, Codex, Claude Code, OpenCode, Cursor CLI, Antigravity, Kimi Code, Pi, DeepSeek Harness, and ZCode, with CodeBuddy, Codex, and DeepSeek Harness bundled in the production image (CodeBuddy optional on source builds) and the rest installed on first use.
Roles (planner, implementer, reviewer, tester) carry their own prompt, executor, model, rules, Skills, and MCP tools, built-in blueprint SOPs cover backend, frontend, product proposal, and bug fix, and a visual SOP designer edits the graph with rework edges back to earlier steps.
Around the engine it adds a LoopForge Local edition (`npx loopforge-cli`) that runs the delivery workflows inside Claude Code, Codex, CodeBuddy, or Cursor, optional GitHub OAuth (SSH keys work for GitLab, Gitea, or Gogs), token and cost reporting per requirement, an OpenAPI-described HTTP API with MCP exposure, scheduled AI tasks, and WeCom notifications.

## Status

Active and trending: 5,352 stars as of 2026-11-21, 850 forks and 373 open issues as of 2026-11-25, since creation on 2026-07-28, pushed 2026-11-25, MIT (a Tencent LICENSE file that grants MIT beside a third-party-components list, which GitHub's classifier reads as no standard license), per the GitHub API.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Tencent/LoopForge&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Tencent/LoopForge&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Tencent/LoopForge&type=date&legend=top-left" />
</picture>

**The train moves weekly (v0.3.6 on 2026-11-11, v0.3.8, v0.4.0 on 2026-11-17, v0.4.1-rc.1 on 2026-11-20, v0.4.1, v0.4.2 on 2026-11-23), 16 contributors commit to it, and the launch drew third-party writeups, though no Hacker News story exists about it (the search's hits name the unrelated LoongForge, 2026-11-22).**
The breakout was mid-November 2026: roughly 700 stars with 174 gained in one day around 2026-11-14 per the GitHub counters third-party coverage cites, and the repository's trendshift badge now sits in the README.
Independent coverage is young and thin: a podcast walkthrough of the Compose install, a directory listing, and one substantive third-party review, whose critical read is the closest thing to evaluation the platform has.
v0.4.2 (2026-11-23) brings pure-AI decisions with custom CLI or API reviewers to assisted approval review, and main past it (unreleased, 2026-11-24 to 2026-11-25) added project-scoped sandbox credentials, shared execution machines with separate CLI model catalogs, Feishu and DingTalk chat bots with web-confirmed writes, and tokens for generic HTTP repositories, per the release notes and commit history.

## Strengths

- **The SOP is a first-class artifact**: a delivery workflow is stored, versioned, visually editable, and re-runnable, with agent roles, deterministic script nodes, human gates, sub-SOPs, and preview builds as node kinds, the clearest process-as-stored-workflow statement in this category.
- Deterministic scripts sit inside the loop where they belong: tests, lint, and reports run as script nodes no agent can talk past, and failed checks rework the run to an earlier step.
- **Every run keeps evidence**: node status, tool traces, worker logs, per-node artifacts, retry or rerun from any node, and token cost rolled up per requirement rather than per API key.
- The executor roster is the widest in the category, ten CLIs with a managed daily updater that verifies npm integrity by SRI before running lifecycle scripts.

## Cautions

- **The sandbox is the host's Docker socket**, which third-party coverage rightly calls root-equivalent trust on the host: new installs listen on all interfaces on port 8090, the first registered account becomes administrator, and open signup is a default you must turn off.
- **CodeBuddy keeps the default gravity**: built-in templates and newly created roles and static previews still default to CodeBuddy, legacy bare model IDs remain CodeBuddy IDs, and the production image bundles it, though the 2026-11-21 update made every model picker accept the other CLIs' models through CLI-prefixed IDs, scheduled prompts use the schedule's own CLI, and the platform can run without a CodeBuddy installation or key once its workflows use other CLIs.
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
- 2026-11-22 - Volatile re-verification: pushed date and counts refreshed (776 forks, 300 open issues), the release train unchanged (v0.4.1-rc.1, 2026-11-20, still the newest tag), the zero-HN search re-run and holding; recorded the 2026-11-21 CodeBuddy optionalization the README and deployment doc now carry (every model picker accepts the supported CLIs' models through CLI-prefixed IDs with CodeBuddy still the fallback default, scheduled prompts use the schedule's CLI, the platform runs without a CodeBuddy install or key once its workflows use others, and the production image bundles Codex, DeepSeek Harness, and by default CodeBuddy, optional on source builds), with the What-it-is roster line and the CodeBuddy caution rewritten.
- 2026-11-25 - Recorded v0.4.2 (2026-11-23: assisted approval review with pure-AI decisions and custom CLI or API reviewers) as the newest tag and the unreleased main batch after it (project-scoped sandbox credentials, shared execution machines with separate CLI model catalogs, Feishu and DingTalk chat bots with web-confirmed writes, generic HTTP repository tokens); pushed date refreshed to 2026-11-25.

## See also

- [SuperPlane](../superplane/index.md) - the platform factory this note's SOP-owned loop is measured against
- [Machinist](../machinist/index.md) - the control-plane-and-runners alternative that never starts an agent
- [Fusion](../fusion/index.md) - the board-first loop with auto-merge, beside the SOP's human-gate ending
- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - where the SOP-engine column sits among the factories

## References

- https://github.com/Tencent/LoopForge - repository, the chat-plus-SOP model, executor roster, and license (GitHub API, as of 2026-11-22)
- https://raw.githubusercontent.com/Tencent/LoopForge/main/README.md - the SOP node kinds, built-in blueprints, the executor pickers' CLI-prefixed model IDs, LoopForge Local, FAQ positioning against Dify and n8n, and the trendshift badge
- https://raw.githubusercontent.com/Tencent/LoopForge/main/LICENSE - the MIT grant with the third-party-components preamble
- https://raw.githubusercontent.com/Tencent/LoopForge/main/docs/deployment.md - the deployment runbook: pinned image, first-use CLI installs, the managed updater's SRI checks, the bundled-CLI list, and the Choosing-an-executor section's CodeBuddy defaults
- https://api.github.com/repos/Tencent/LoopForge/releases - the release train, v0.4.1-rc.1 (2026-11-20) newest as of 2026-11-22
- https://loopforge.cn - the product site: MIT, self-deployable, cloud sandboxes, shared sessions, gated SOPs
- https://explainx.ai/blog/tencent-loopforge-self-hosted-sop-coding-agents-claude-codex-2026 - the third-party critical read: the Docker-socket trust call, the 0.0.0.0:8090 and first-admin defaults, the CodeBuddy-pinned subsystems it found in November, and the planned-not-shipped SOP export
- https://hn.algolia.com/api/v1/search?query=loopforge&tags=story - the footprint scan finding no story about the platform (the hits name the unrelated LoongForge, 2026-11-22)
- https://github.com/varun1505/awesome-software-factories - the third-party curated list that surfaced this note
