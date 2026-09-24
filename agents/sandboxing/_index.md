---
showArticleList: false
title: Sandboxing
created: 2026-09-24
visible: true
status: in progress
tags: [agents, sandboxing]
readability: 3
---

Where agent isolation should live: the workstation, the cluster, the wrapper, the framework, or the provisioning layer.

- [Agent Sandbox](agent-sandbox/index.md) - the Kubernetes SIG Apps CRD for declarative sandbox fleets, delegating isolation to gVisor or Kata.
- [aigate](aigate/index.md) - the fourteen-star kernel-enforced wrapper, kept as the reference design for small-scale OS-level agent sandboxing.
- [ArtifactFS](artifact-fs/index.md) - Cloudflare's FUSE driver that mounts big repos in seconds, the provisioning layer sandboxes need before isolation matters.
- [Clawk](clawk/index.md) - the disposable-VM workstation tool, the agent gets its own Linux machine instead of yours, pre-1.0 on macOS.
- [CubeSandbox](cubesandbox/index.md) - Tencent's E2B-compatible RustVMM/KVM microVM sandbox, sub-60ms boots, its traction built on launch announcements rather than community discussion.
- [Flue](flue/index.md) - the Astro team's agent framework whose contribution is a three-tier sandbox taxonomy and durable execution.
- [OpenSandbox](opensandbox/index.md) - the Apache-2.0 general sandbox platform (SDKs, CLI, MCP, K8s runtimes) that grew on GitHub trend charts, not Hacker News.
- [OpenShell](openshell/index.md) - NVIDIA's container-and-MicroVM runtime where declarative policy and inference-proxy keys make the boundary credible.

Its members are compared on shared rows in the [Sandboxing Feature Matrix](sandboxing-feature-matrix/index.md).

## Changes

- 2026-08-30 - Added Agent Sandbox.
- 2026-08-30 - Added aigate.
- 2026-08-30 - Added ArtifactFS.
- 2026-08-30 - Added Flue.
- 2026-08-30 - Added OpenShell.
- 2026-09-05 - Added Clawk.
- 2026-09-16 - Added CubeSandbox.
- 2026-09-16 - Added OpenSandbox.
