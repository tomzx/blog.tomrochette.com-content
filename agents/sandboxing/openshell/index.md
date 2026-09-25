---
title: OpenShell
created: 2026-08-30
updated: 2026-09-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, isolation, security, nvidia, open-source]
readability: 3
audience_notes: >
  Engineers running autonomous coding agents who need kernel-enforced isolation and egress policy rather than trust.
  Assumes you know what containers, seccomp, and an egress proxy are.
---

OpenShell is NVIDIA's Apache-2.0, Rust-based runtime that runs AI coding agents inside isolated containers or MicroVMs governed by declarative YAML policies enforced at the kernel and an L7 egress proxy, so agents work without unrestricted access to files, credentials, or the network.
Facts below verified as of 2026-09-25.

**OpenShell is the first sandbox built for the agent era by a hardware vendor rather than a harness vendor, and its most interesting idea is not the isolation but the credential architecture: provider keys are injected at an inference proxy and never enter the sandbox filesystem.**

## What it is

A Rust CLI plus gateway control plane that runs each agent in its own Docker or Podman container, MicroVM, or Kubernetes pod, with four policy domains: filesystem via Landlock, process via unprivileged identity and seccomp, network via an L7 proxy that can allow GET but deny POST per destination, and inference via an `inference.local` endpoint that intercepts model API traffic so keys stay outside.
Claude Code, OpenCode, Codex, and Copilot CLI work out of the box, OpenClaw and Hermes through NVIDIA's NemoClaw, plus bring-your-own-container and a community catalog.
Policies are versioned YAML files you commit, telemetry is anonymous and can be compiled out, and a Python SDK exists.
Linux, macOS (Apple Silicon), and Windows via WSL 2 (experimental); Apache-2.0, from NVIDIA as part of its Agent Toolkit with security partners including Cisco and CrowdStrike.

## Status

Fast adoption, self-declared alpha: 8,787 stars, 1,275 forks, 416 open issues and PRs as of 2026-09-25, created 2026-02-24.
v0.0.116 released 2026-08-28 remains the latest stable, with the v0.1.0 pre-release train advancing through v0.1.0-pre.11 (2026-09-23) alongside rolling dev and vm-runtime prerelease channels, 1,512 commits, 123 contributors.
**NVIDIA's own blog calls it an early preview, and v0.0.x versioning plus experimental Kubernetes and GPU features say production use is a bet on the vendor staying in.**
In September 2026 the team also published a formal-methods discussion of encoding the full OpenShell policy as formal logic and proving containment queries with SAT, SMT, and Z3, which reached 40 points on Hacker News.

## Strengths

- Defense in depth beyond a container boundary: Landlock, seccomp privilege drop, and per-method L7 egress policy.
- The credential architecture keeps provider keys out of the sandbox entirely, the cleanest answer to key exfiltration in the category.
- Agent-agnostic with the four major coding agents first-class and a BYOC path.
- Unusual transparency: auditable versioned policies and fully removable telemetry.

## Cautions

- Alpha by its own badge, with breaking changes expected and the Kubernetes path explicitly experimental.
- Telemetry is on by default in a tool whose pitch is privacy; anonymous, but verify it against your threat model.
- Effective security equals the YAML policies you write and maintain, which is real ongoing work.
- 416 open issues and PRs as of 2026-09-25, down from 537 at the prior verification, on a six-month-old codebase.

## Pricing

Free and open source under Apache-2.0, no paid tiers found.
Costs are the local runtime and the policy authoring effort.

## Compared to

- Plain Docker: isolation without egress policy or credential injection unless you build it; choose OpenShell when network and key policy are the point.
- Harness built-ins (Claude Code sandbox, Codex landlock and Seatbelt): zero infrastructure and always in sync, but per-tool and per-workstation; choose OpenShell for multiple agents, central audit, and private inference routing.
- [agent-sandbox](../agent-sandbox/index.md): the Kubernetes-native building block without the agent policy layer; choose it for cluster-scale fleets, OpenShell for the policy engine out of the box.

## Bottom line

**Recommended for teams running multiple autonomous agents that need declarative egress and credential policy now, with alpha risk priced in.**
Not for production-critical paths this quarter, or shops that cannot run Docker or Podman on developer machines.

## Changes

- 2026-08-30 - Created in the Sandboxing category, recording NVIDIA's agent runtime with alpha and default-telemetry cautions.
- 2026-09-16 - Growth refreshed (8,627 stars, 1,254 forks, 560 open issues and PRs, 118 contributors, 1,387 commits) and the unverifiable 2026-09-05 prerelease claim corrected to the verifiable v0.1.0-pre.1 tag of 2026-09-01 plus the dev and vm-runtime prerelease channels.
- 2026-09-16 - Added the team's formal-methods policy-prover post and its 33-point HN discussion to Status and References.
- 2026-09-18 - The v0.1.0 pre-release train advanced (pre.2 on 2026-09-16, pre.3 on 2026-09-17, stable still v0.0.116), the formal-methods HN thread rose from 33 to 39 points, and growth refreshed (8,683 stars, 1,261 forks, 528 open issues and PRs, 119 contributors, 1,430 commits).
- 2026-09-21 - The pre-release train advanced again with v0.1.0-pre.4 (2026-09-18, stable still v0.0.116), and growth refreshed (8,715 stars, 1,268 forks, 537 open issues and PRs, 120 contributors), fixing a stale 560 in Cautions to the verified 537.
- 2026-09-25 - The pre-release train reached v0.1.0-pre.11 (2026-09-23, stable still v0.0.116), the formal-methods HN thread rose from 39 to 40 points, and growth refreshed (8,787 stars, 1,275 forks, 416 open issues and PRs, 123 contributors, 1,512 commits).

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [agent-sandbox](../agent-sandbox/index.md) - the Kubernetes-native layer below
- [Claude Code](../../harnesses/claude-code/index.md) - the built-in sandboxing counterpoint
- [MCP](../../protocols/mcp/index.md) - one of the surfaces agents use that egress policy must cover

## References

- https://github.com/NVIDIA/OpenShell - repository, protection layers, supported agents, license, alpha badge
- https://docs.nvidia.com/openshell/about/overview - the Landlock, seccomp, and threat-model documentation
- https://docs.nvidia.com/openshell/latest/about/how-it-works - the CLI, gateway, and supervisor architecture
- https://blogs.nvidia.com/blog/secure-autonomous-ai-agents-openshell/ - NVIDIA's positioning and early-preview status
- https://code.claude.com/docs/en/sandboxing - the built-in sandboxing comparison
- https://github.com/NVIDIA/OpenShell/releases/tag/v0.0.116 - release cadence evidence
- https://hn.algolia.com/api/v1/items/49713261 - the 33-point HN discussion of the team's formal-methods policy-prover post
