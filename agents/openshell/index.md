---
title: OpenShell
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, isolation, security, nvidia, open-source]
readability: 3
audience_notes: >
  Engineers running autonomous coding agents who need kernel-enforced isolation and egress policy rather than trust.
  Assumes you know what containers, seccomp, and an egress proxy are.
---

OpenShell is NVIDIA's Apache-2.0, Rust-based runtime that runs AI coding agents inside isolated containers or MicroVMs governed by declarative YAML policies enforced at the kernel and an L7 egress proxy, so agents work without unrestricted access to files, credentials, or the network.
Facts below verified as of 2026-09-04.

**OpenShell is the first sandbox built for the agent era by a hardware vendor rather than a harness vendor, and its most interesting idea is not the isolation but the credential architecture: provider keys are injected at an inference proxy and never enter the sandbox filesystem.**

## What it is

A Rust CLI plus gateway control plane that runs each agent in its own Docker or Podman container, MicroVM, or Kubernetes pod, with four policy domains: filesystem via Landlock, process via unprivileged identity and seccomp, network via an L7 proxy that can allow GET but deny POST per destination, and inference via an `inference.local` endpoint that intercepts model API traffic so keys stay outside.
Claude Code, OpenCode, Codex, and Copilot CLI work out of the box, OpenClaw and Hermes through NVIDIA's NemoClaw, plus bring-your-own-container and a community catalog.
Policies are versioned YAML files you commit, telemetry is anonymous and can be compiled out, and a Python SDK exists.
Linux, macOS (Apple Silicon), and Windows via WSL 2 (experimental); Apache-2.0, from NVIDIA as part of its Agent Toolkit with security partners including Cisco and CrowdStrike.

## Status

Fast adoption, self-declared alpha: 8,485 stars, 1,251 forks, 547 open issues and PRs as of 2026-09-02, created 2026-02-24.
v0.0.116 released 2026-08-28 with near-daily point releases before it, 1,271 commits, about 110 contributors.
**NVIDIA's own blog calls it an early preview, and v0.0.x versioning plus experimental Kubernetes and GPU features say production use is a bet on the vendor staying in.**

## Strengths

- Defense in depth beyond a container boundary: Landlock, seccomp privilege drop, and per-method L7 egress policy.
- The credential architecture keeps provider keys out of the sandbox entirely, the cleanest answer to key exfiltration in the category.
- Agent-agnostic with the four major coding agents first-class and a BYOC path.
- Unusual transparency: auditable versioned policies and fully removable telemetry.

## Cautions

- Alpha by its own badge, with breaking changes expected and the Kubernetes path explicitly experimental.
- Telemetry is on by default in a tool whose pitch is privacy; anonymous, but verify it against your threat model.
- Effective security equals the YAML policies you write and maintain, which is real ongoing work.
- 511 open issues and PRs on a six-month-old codebase.

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

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [agent-sandbox](../agent-sandbox/index.md) - the Kubernetes-native layer below
- [Claude Code](../claude-code/index.md) - the built-in sandboxing counterpoint
- [MCP](../mcp/index.md) - one of the surfaces agents use that egress policy must cover

## References

- https://github.com/NVIDIA/OpenShell - repository, protection layers, supported agents, license, alpha badge
- https://docs.nvidia.com/openshell/latest/index.html - the Landlock, seccomp, and threat-model documentation
- https://docs.nvidia.com/openshell/latest/about/how-it-works - the CLI, gateway, and supervisor architecture
- https://blogs.nvidia.com/blog/secure-autonomous-ai-agents-openshell/ - NVIDIA's positioning and early-preview status
- https://docs.claude.com/en/docs/claude-code/sandboxing - the built-in sandboxing comparison
- https://github.com/NVIDIA/OpenShell/releases/tag/v0.0.116 - release cadence evidence
