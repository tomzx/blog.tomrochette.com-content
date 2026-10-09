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
- [Brig](brig/index.md) - NOFire AI's per-agent microVM sandbox for Apple Silicon and Linux, the category's most detailed published security claims and cosign-verified boot assets.
- [Clawk](clawk/index.md) - the disposable-VM workstation tool, the agent gets its own Linux machine instead of yours, pre-1.0 on macOS.
- [CubeSandbox](cubesandbox/index.md) - Tencent's E2B-compatible RustVMM/KVM microVM sandbox, sub-60ms boots, its traction built on launch announcements rather than community discussion.
- [Drop](drop/index.md) - the rootless namespace sandbox that reuses your installed Linux distro instead of an image or VM, optional gVisor underneath.
- [E2B](e2b/index.md) - the hosted Firecracker-microVM sandbox API the category's self-hosted members measure themselves against, with its runtime now open source.
- [Fence](fence/index.md) - Tusk's container-free CLI wrapping any command or agent in sandbox-exec or bubblewrap, Landlock, and seccomp, one fence.json, deny-by-default network.
- [Flue](flue/index.md) - the Astro team's agent framework whose contribution is a three-tier sandbox taxonomy and durable execution.
- [Greywall](greywall/index.md) - the Fence fork that adds proxy-swapped credentials and an allow-by-default watch mode with a live dashboard, quiet since August 2026.
- [Microsandbox](microsandbox/index.md) - the libkrun microVM runtime with container workflows, agent-created sandboxes via skills and MCP, and the category's largest HN launch.
- [NemoClaw](nemoclaw/index.md) - NVIDIA's Apache-2.0 reference stack that installs, hardens, and operates OpenClaw, Hermes, and LangChain Deep Agents inside OpenShell sandboxes with managed inference and lifecycle ops.
- [nono](nono/index.md) - the Sigstore team's kernel capability sandbox that brokers each delegated tool separately and proxies credentials scoped per endpoint.
- [NVX](nvx/index.md) - Microsoft's OpenVMM research sandbox for agentic workloads with Windows hypervisor paths and limits docs that name what the ABI does not do.
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
- 2026-09-29 - Added Drop.
- 2026-10-06 - Added Brig.
- 2026-10-06 - Added E2B.
- 2026-10-07 - Added nono.
- 2026-10-07 - Added Microsandbox.
- 2026-10-07 - Added Fence.
- 2026-10-07 - Added NVX.
- 2026-10-07 - Added NemoClaw.
- 2026-10-08 - Added Greywall.
