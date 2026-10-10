---
title: Microsandbox
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, microvm, isolation, open-source]
readability: 3
audience_notes: >
  Engineers who want hardware-isolated sandboxes with container-style ergonomics on their own machines, including letting agents spawn VMs themselves.
  Assumes you know what a microVM, an OCI image, and libkrun are.
---

Microsandbox is a local-first, Apache-2.0 microVM runtime and library, built on libkrun, that runs untrusted workloads in fast virtual machines with Docker-like workflows, OCI images, fork and snapshot semantics, and support for Linux, macOS, and Windows hosts.

**Microsandbox made VMs behave like containers, and it is the only member of this category built for agents to create their own sandboxes: a shipped Agent Skills package and MCP server let a running agent spawn microVMs as tools.**

## What it is

A runtime binary plus an embeddable library: you pull standard OCI images from Docker Hub, GHCR, or any registry, then run, exec, and attach to them like containers, except each one is a hardware-isolated VM with its own kernel.
The README claims average boot times under 100 milliseconds, a self-reported figure footnoted to guest boot on an M1 machine, and the state model goes beyond containers: pause and resume, snapshots, and forking a live sandbox.
Credentials are advertised as "secret keys that never enter the VM", the project's own unverified claim of unexploitable secret handling.
It embeds in application code (no long-running daemon required), runs sandboxes in detached mode for long-lived sessions, and ships a companion Agent Skills repository and MCP server so agents can create and manage their own sandboxes.
The project carries a Y Combinator badge and has moved organizations more than once since its 2024 launch, landing at superradcompany/microsandbox.

## Status

Large by this category's standards and still shipping weekly: 8,617 stars, 105 open issues and PRs, pushed 2026-10-09 as of 2026-10-09, created 2024-10-03.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=superradcompany/microsandbox&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=superradcompany/microsandbox&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=superradcompany/microsandbox&type=date&theme=dark&legend=top-left" />
</picture>

v0.7.5, v0.7.6, and v0.7.7 shipped within a week ending 2026-10-05, a fast pre-1.0 minor-version cadence.
**Its Show HN of 2025-05-30 drew 402 points, the largest community thread of any member of this category, while a June 2026 resubmission drew 3 points, so the launch was a 2025 event and the current proof of life is the release train, not public debate.**

## Strengths

- A hardware boundary with container ergonomics: OCI images, docker-like commands, and sub-second starts remove most of the friction that kept VMs out of agent loops.
- The agent-self-service angle (skills plus MCP) is unique in the category and matches how agents actually operate.
- Fork and snapshot of live VMs enable checkpointing, backtracking, and fan-out patterns containers cannot express as cleanly.
- Cross-platform including Windows, which almost no workstation member here can say.

## Cautions

- Every performance and security claim is self-reported: the sub-100ms boot figure, the unexploitable-secrets claim, none independently audited or benchmarked.
- Pre-1.0 with rapid minor-version churn and three organization homes since 2024 (the launch linked microsandbox/microsandbox, later zerocore-ai, now superradcompany), a provenance trail adopters should watch.
- The 402-point launch is a 2025 memory; the 2026 resubmission's 3 points mean the project must be judged on its repo, not its HN history.
- libkrun shares the virtualization story with its upstream: capable, but the isolation claims ride on a dependency this project does not control.

## Pricing

Free and open source under Apache-2.0, self-hosted, no hosted offering or pricing page found as of 2026-10-07.
Costs are the local or fleet hardware you run it on.

## Compared to

- [CubeSandbox](../cubesandbox/index.md): Tencent's server-fleet E2B-compatible microVM service for many concurrent sandboxes on KVM nodes; Microsandbox is the local-first, embeddable runtime for your own machine.
- [E2B](../e2b/index.md): the hosted baseline with per-second billing; Microsandbox is the buy-nothing path to the same VM boundary.
- [NVX](../nvx/index.md): Microsoft's research-grade microVM sandbox with the Windows-native hypervisor paths; Microsandbox is the productized one, NVX the instrumented one.

## Bottom line

**Recommended for engineers who want VM isolation with container workflows on their own hardware, and for agent-framework authors who want the agent itself to spawn isolated environments.**
Not for anyone needing audited claims, a stable 1.0 API, or a hosted service.

## Changes

- 2026-10-07 - Created from the entrant-resolution run, profiling the libkrun-based microVM runtime behind the category's largest HN thread, with its self-reported-claims and provenance cautions.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [CubeSandbox](../cubesandbox/index.md) - the server-fleet counterpart to this local runtime
- [NVX](../nvx/index.md) - the research-grade microVM sandbox from Microsoft
- [E2B](../e2b/index.md) - the hosted API this runtime's skill story parallels

## References

- https://github.com/superradcompany/microsandbox - repository, feature list, libkrun acknowledgement, YC badge, organization moves
- https://api.github.com/repos/superradcompany/microsandbox - stars, open issues, creation and push dates as of 2026-10-07
- https://api.github.com/repos/superradcompany/microsandbox/releases - the v0.7.5 through v0.7.7 release record
- https://docs.microsandbox.dev/ - the documentation site
- https://hn.algolia.com/api/v1/items/44135977 - the 402-point Show HN of 2025-05-30, including the isolation-tradeoff questions in the thread
