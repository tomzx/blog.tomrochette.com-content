---
title: CubeSandbox
created: 2026-09-16
updated: 2026-09-16
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, microvm, security]
readability: 3
audience_notes: >
  Engineers comparing self-hosted alternatives to hosted sandbox APIs, who need to serve untrusted agent code at density on their own fleet.
  Assumes you know what KVM, a microVM, and an SDK base-URL swap are.
---

CubeSandbox is Tencent's Apache-2.0, self-hosted sandbox service that builds each AI agent workload a dedicated-kernel microVM on RustVMM and KVM, boots it in tens of milliseconds, and exposes an E2B-compatible API so existing E2B client code migrates by changing a base URL.
Facts below verified as of 2026-09-16.

## What it is

**The pitch is density without giving up the boundary: a dedicated kernel per sandbox at under 5MB of memory overhead, thousands of sandboxes per node through kernel sharing and copy-on-write.**
The architecture splits into CubeAPI (a Rust E2B-compatible gateway), CubeMaster (cluster orchestration), CubeProxy, Cubelet (per-node lifecycle), CubeVS (an eBPF virtual switch for kernel-level network isolation), CubeEgress (an OpenResty L7 egress gateway with per-domain policy and credential injection), and CubeHypervisor with a containerd shim.
It requires x86_64 Linux with KVM (ARM64 supported since v0.5, a QEMU dev environment exists but is flagged as poor performance), deploys to Kubernetes in preview since v0.6, and gained cross-node pause and resume over S3 in v0.7.
Documentation, changelogs, and examples (code execution, browser automation, OpenClaw assistants, RL training) live in-repo, with a Python SDK on PyPI.

## Status

**Five months from first release to v0.7.1 with 12,537 stars, while the community discussion never escaped single digits on Hacker News.**
Created 2026-04-10, first release v0.1.0 on 2026-04-20, latest v0.7.1 on 2026-09-11, pushed the day of verification, 1,123 forks, 143 open issues and PRs as of 2026-09-16.
The team launched on HN themselves as "a less than 60ms, open-source alternative to E2B using RustVMM and KVM" (7 points), and the same project drew two more submissions from other accounts within four days at 5 and 3 points.
The sub-60ms figure is single-concurrency on bare metal by the project's own benchmark, degrading to a 67ms average and 137ms P99 at 50 concurrent creations, and no independent benchmark, audit, or critical write-up exists that I could find.

## Strengths

- A real isolation boundary by default: every sandbox is its own microVM with a dedicated kernel, plus eBPF inter-sandbox network isolation.
- The E2B compatibility is architectural (the gateway and proxy speak the protocol), so migration is one environment variable, and the roadmap explicitly tracks closing remaining E2B gaps.
- State management is a differentiator: CubeCoW snapshots with instant clone and rollback at hundred-millisecond granularity, AutoPause for idle sandboxes, and cross-node pause/resume over S3.
- The credential vault and L7 egress policy mirror what OpenShell sells: keys injected at the proxy, never visible to sandbox code.

## Cautions

- **Every performance and density claim is self-reported, from the sub-60ms boot to the <5MB overhead, with no independent replication I could find.**
- KVM on Linux servers is a hard requirement, which excludes macOS and constrained CI environments by design.
- The license is Apache-2.0 "except for the third-party components listed below" (permissive items such as cilium/bpf under BSD-2-Clause), which is why GitHub detects NOASSERTION and compliance tooling will flag it.
- The absence of any critical coverage is itself the risk: 143 open issues and PRs on a five-month-old codebase, and a "Cube 100 Program" recruiting its first 100 production teams, suggest operational evidence is still being collected.

## Pricing

Free and self-hosted; no hosted tier or pricing page found on cubesandbox.com or in the repo as of 2026-09-16.
Costs are the KVM-capable Linux fleet plus snapshot storage (S3 for cross-node resume).

## Compared to

- [OpenSandbox](../opensandbox/index.md): the platform play, broader in surface (five SDKs, MCP, GUI and desktop environments) but container-first with opt-in hardening; CubeSandbox is narrower and boundary-first with microVMs by default.
- [Clawk](../clawk/index.md): the workstation end of the same spectrum, one disposable VM per agent on a laptop, macOS-first; CubeSandbox is a shared service for many concurrent sandboxes on Linux fleet hardware.
- E2B and other hosted sandbox APIs: zero operations and per-second billing; CubeSandbox is the drop-in self-hosted replacement for exactly that API, at the cost of running KVM-capable nodes.

## Bottom line

**Recommended for teams already running E2B-style code execution who want hardware-level isolation and high density on their own Linux fleet, paying in operations rather than per-second billing.**
Not for macOS or workstation use, and not for anyone who needs independently verified performance numbers before committing.

## Changes

- 2026-09-16 - Created.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [OpenSandbox](../opensandbox/index.md) - the platform-first sibling released the same season
- [Clawk](../clawk/index.md) - the workstation-VM end of the same isolation spectrum
- [OpenShell](../openshell/index.md) - the other credential-vault-and-egress-proxy design
- [Agent Sandbox](../agent-sandbox/index.md) - the Kubernetes orchestrator alternative for fleet scale

## References

- https://github.com/TencentCloud/CubeSandbox - repository README: architecture, component table, benchmarks, roadmap, community programs
- https://api.github.com/repos/TencentCloud/CubeSandbox - stars, forks, license detection, creation and push dates as of 2026-09-16
- https://api.github.com/repos/TencentCloud/CubeSandbox/license - the LICENSE text: Apache-2.0 plus the listed third-party component licenses
- https://api.github.com/repos/TencentCloud/CubeSandbox/releases/latest - the v0.7.1 release of 2026-09-11
- https://pypi.org/pypi/cubesandbox/json - the Python SDK on PyPI (0.7.0 at verification)
- https://cubesandbox.com - the live project site
- https://hn.algolia.com/api/v1/items/47863430 - the team's 7-point Show HN launch and the confirming team comment
- https://hn.algolia.com/api/v1/items/47879216 - the 5-point second submission one day later
- https://hn.algolia.com/api/v1/items/47848628 - the 3-point third submission, one day earlier
