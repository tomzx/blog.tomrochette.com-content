---
title: AX
created: 2026-09-21
updated: 2026-09-21
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, kubernetes, multi-agent, open-source, google]
readability: 3
audience_notes: >
  Engineers running agent fleets as infrastructure who want a declarative control plane instead of a desktop dashboard.
  Assumes you know Kubernetes concepts (apply, watch, namespaces) and what an MCP server is.
---

AX is Google's open-source, Kubernetes-based orchestrator (Go, Apache-2.0) that runs agent workloads as sandboxed, declaratively configured tasks at cluster scale.
Facts below verified as of 2026-09-21.

**AX is the first orchestration entrant in this category that treats agents as a datacenter workload class rather than a desktop session problem, and its kubectl-style interface is the tell: it wants to be the Kubernetes of agents, not another dashboard.**

## What it is

A cluster control plane with four YAML primitives: **Task** (a sandboxed agent run with CPU and memory limits), **Workspace** (pre-wired git repos, MCP servers, and skill packages), **Gateway** (an outbound network allowlist), and **Model** (provider config and secrets in one manifest).
Everything is `ax.io/v1alpha1` manifests applied with `ax apply`, watched with `ax watch`, and inspected with `ax ssh`, and idle tasks checkpoint and resume in about a second.
It runs on top of Agent Substrate (also Apache-2.0), a compute runtime built for dense, stateful actor lifecycles, and it explicitly targets billions of tasks per cluster.

## Status

Active and newly prominent: the repo was created 2026-03-30, but its public arrival was the 450-point HN thread as of 2026-09-21 (414 when first fetched on launch day 2026-09-20), and v0.3.0 shipped the same day.
About 3,940 stars as of 2026-09-21, with the README carrying an explicit warning that core concepts, protocols, and specifications will see major breaking changes before a stable release.
The site says it was born at Google from agentic-runtime research, though HN commenters caution that the Google label covers a team project, not a product line.

## Strengths

- **Declarative fleet management is the differentiator**: network fencing, workspace pre-wiring, and model rotation as reviewable YAML, which no desktop dashboard in this category offers.
- Sub-second suspend and resume turns idle waiting (model responses, human approvals) into reclaimed compute instead of billed sandbox time.
- Generative workspaces let you describe an environment in plain English and have an agent prepare it before the task starts.
- A kubectl-style CLI means the operational skill transfer is real for anyone who already runs clusters.

## Cautions

- **This is cluster infrastructure, not a developer tool**: you need Kubernetes, ko, a container registry, and Agent Substrate to run anything, so it is a category error to compare it directly with Conductor or Paseo.
- Pre-stable by its own warning, with major breaking changes promised before 1.0.
- The name collides with Ax (axllm.dev), a DSPy-style framework, so search results mix them.
- HN commenters raise the Google graveyard question and note the branding is loose, so durability depends on the team, not a Google roadmap.

## Pricing

Free and open source under Apache-2.0; you pay for your cluster and your model bills.
No hosted tier exists.

## Compared to

- [Omnara](../omnara/index.md): the developer-scale control plane; Omnara supervises agents you already run from a dashboard and phone, AX schedules sandboxes for them at fleet scale.
- [Gas Town](../gastown/index.md): the single-machine supervision hierarchy; both put oversight above sessions, but Gas Town is a town on your laptop and AX is a datacenter primitive.
- Plain Kubernetes Jobs: the incumbent answer; AX argues agents need checkpoint-resume, network fencing, and warm workspaces that batch jobs never grew.

## Bottom line

**Recommended for teams running agent fleets as production or research infrastructure who already operate Kubernetes.**
Not for developers who want a desktop app supervising a handful of sessions; pick Conductor, Paseo, or Omnara for that.

## Changes

- 2026-09-21 - Created from the same-day entrant resolution (414-point HN launch thread on 2026-09-20).

## See also

- [Omnara](../omnara/index.md) - the developer-scale control plane this contrasts with
- [Gas Town](../gastown/index.md) - the single-machine counterpart in the supervision story
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this column joins
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - where orchestration sits in the map

## References

- https://github.com/google/ax - repository, Apache-2.0, about 3,940 stars, Go, created 2026-03-30 (GitHub API, 2026-09-21)
- https://agentexecutor.io - official site: Task, Workspace, Gateway, and Model primitives, suspend/resume, Agent Substrate relationship
- https://raw.githubusercontent.com/google/ax/HEAD/README.md - quick start, kubectl-style CLI, and the pre-stability warning
- https://github.com/google/ax/releases/tag/v0.3.0 - latest release, published 2026-09-20 (GitHub API)
- https://github.com/agent-substrate/substrate - the runtime underneath AX, Apache-2.0, about 2,368 stars (GitHub API, 2026-09-21)
- https://hn.algolia.com/api/v1/items/49780797 - the launch thread (450 points as of 2026-09-21) and its skepticism (Google graveyard, branding, name collision)
