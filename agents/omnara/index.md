---
title: Omnara
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, agent-control-plane, mobile, self-hosted, yc]
readability: 3
audience_notes: >
  Engineers who run multiple coding agents and want one control plane to supervise them
  from a dashboard, phone, or API, instead of per-agent CLI sessions.
  Assumes you know what a harness, MCP, and BYOK mean.
---

Omnara (YC S25) is an open-source, model-agnostic control plane for managed agents: you define agents in YAML, it handles execution and state, and you drive them from a web dashboard, mobile apps, CLI, REST API, or Slack.
Facts below verified as of 2026-09-02.

**Omnara has quietly pivoted from "run Claude Code from your phone" into the open-source alternative to Claude Managed Agents, and that repositioning makes it infrastructure for serving agents, not just supervising them.**

## What it is

A Go platform (Apache-2.0) where an agent is a small YAML config: instruction, model provider config, tools, permissions, MCP servers, skills, and the machine pool it runs on.
It exposes a dashboard, CLI, and REST API, plus first-party iOS/Android apps and a Slack connector, with approvals, questions, streamed events, and artifacts as first-class API concepts.
Self-host it or use Omnara Cloud (app.omnara.com); models are BYOK through provider configs such as OpenRouter presets.
Founded by Ishaan Sehgal (ex-Microsoft, led Kaito) and Kartik Sarangmath, per its YC profile.
It sits in the orchestration layer of this section's taxonomy (control plane and supervision, like Paseo), not the harness layer: it drives and manages agents rather than being one.

## Status

**Active, well-capitalized by YC standards, and shipping daily.**
2,782 stars and 213 forks as of 2026-09-02 on a repo created July 9, 2025, with pushes landing September 2, 2026 (GitHub API).
Two HN threads anchor its traction: a 310-point Show HN on August 12, 2025 ([HN](https://news.ycombinator.com/item?id=44878650)) and a 147-point Launch HN on February 12, 2026 ([HN](https://news.ycombinator.com/item?id=46991591)).
The product's own framing moved between those dates, from "run Claude Code from anywhere" to "the API for production-grade agents" with managed-agent execution.

## Strengths

- **The mobile-and-API surface is the differentiator**: approvals, questions, and streamed events work the same from an iPhone, Slack, or a REST call, which is exactly what unattended agent fleets need.
- Agent-as-YAML makes agents reviewable artifacts: configs live in your repo, execution and state live in Omnara, and machine pools separate where code runs from who can invoke it.
- Model-agnostic and BYOK by design, with self-hosting under Apache-2.0 if you want the control plane on your own hardware.
- Its positioning against Claude Managed Agents gives it a crisp comparison point for teams avoiding vendor lock-in.

## Cautions

- **The pitch has moved twice already** (mobile Claude Code remote, then managed-agents control plane), so the product you adopt today may be framed differently a year from now.
- You are trusting a young startup (YC S25) with the execution and state layer for your agents; self-hosting mitigates but does not eliminate that.
- The docs are thinner than the platform's ambition; the feature surface (machine pools, integrations) is documented but young.
- As a control plane it still needs actual harnesses underneath; it does not replace your choice of agent.

## Pricing

The platform is open source under Apache-2.0 and self-hostable at no cost.
Omnara Cloud is the hosted option; I found no public per-seat pricing page as of 2026-08-30.
You pay your own model costs either way.

## Compared to

- [Paseo](../paseo/index.md): the closest sibling, also FOSS self-hosted supervision from your phone; Paseo wraps CLI agents you already run, while Omnara wants to own execution and state via its API.
- [Conductor](../conductor/index.md): the Mac-native multi-session manager for local parallel work; Conductor is a desktop app around Claude Code/Codex sessions, Omnara is a server-grade control plane.
- [Claude Code](../claude-code/index.md): Anthropic's own managed-agent offering is the closed counterpart Omnara positions against; pick Claude Managed Agents for turnkey, Omnara for openness and BYOK.

## Bottom line

**Recommended for teams running agents as products or internal services who want approvals, events, and mobile control behind one API on their own infrastructure; not for solo developers who just want to drive one CLI agent from their phone (Paseo or the harness's own remote features do that with less machinery).**
I believe every serious agent deployment eventually needs exactly what Omnara is building, and I think the open-source control plane will beat vendor-owned managed agents the same way Postgres beat proprietary databases.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the supervision layer Omnara belongs to
- [Paseo](../paseo/index.md) - the closest open-source sibling for phone-based agent supervision
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where control planes sit above harnesses
- [OpenChamber](../openchamber/index.md) - self-hosted scheduling, the unattended complement to interactive supervision

## References

- https://github.com/omnara-ai/omnara - repository, Apache-2.0, 2,782 stars as of 2026-09-02
- https://docs.omnara.com/introduction - agent YAML model, dashboard/CLI/API surfaces, use cases
- https://raw.githubusercontent.com/omnara-ai/omnara/main/README.md - current positioning and getting-started flow
- https://www.omnara.com/ - "open-source alternative to Claude Managed Agents" positioning
- https://www.ycombinator.com/companies/omnara - YC S25 batch, founders, self-host-or-cloud model
- https://news.ycombinator.com/item?id=44878650 - the August 12, 2025 Show HN, 310 points (verified via Algolia API)
- https://news.ycombinator.com/item?id=46991591 - the February 12, 2026 Launch HN, 147 points (verified via Algolia API)
