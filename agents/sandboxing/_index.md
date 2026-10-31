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
- [aicontainer](aicontainer/index.md) - the twenty-star devcontainer-spec sandbox, auto-approve CLIs behind a digest-pinned Docker socket proxy with sanitized host config, the footprint carried by its boundary documentation.
- [aigate](aigate/index.md) - the fourteen-star kernel-enforced wrapper, kept as the reference design for small-scale OS-level agent sandboxing.
- [ArtifactFS](artifact-fs/index.md) - Cloudflare's FUSE driver that mounts big repos in seconds, the provisioning layer sandboxes need before isolation matters.
- [Brig](brig/index.md) - NOFire AI's per-agent microVM sandbox for Apple Silicon and Linux, the category's most detailed published security claims and cosign-verified boot assets.
- [Brood Box](brood-box/index.md) - Stacklok's review-gated libkrun microVM runner, changes land only after a per-file diff of a copy-on-write snapshot.
- [Clawk](clawk/index.md) - the disposable-VM workstation tool, the agent gets its own Linux machine instead of yours, pre-1.0 on macOS.
- [Container Use](container-use/index.md) - Dagger's MCP server giving each agent a container on its own git branch, the parallel-workflow entry whose release train stopped in August 2025.
- [CubeSandbox](cubesandbox/index.md) - Tencent's E2B-compatible RustVMM/KVM microVM sandbox, sub-60ms boots, its traction built on launch announcements rather than community discussion.
- [Drop](drop/index.md) - the rootless namespace sandbox that reuses your installed Linux distro instead of an image or VM, optional gVisor underneath.
- [E2B](e2b/index.md) - the hosted Firecracker-microVM sandbox API the category's self-hosted members measure themselves against, with its runtime now open source.
- [Fence](fence/index.md) - Tusk's container-free CLI wrapping any command or agent in sandbox-exec or bubblewrap, Landlock, and seccomp, one fence.json, deny-by-default network.
- [Flue](flue/index.md) - the Astro team's agent framework whose contribution is a three-tier sandbox taxonomy and durable execution.
- [Greywall](greywall/index.md) - the Fence fork that adds proxy-swapped credentials and an allow-by-default watch mode with a live dashboard, quiet since August 2026.
- [Landrun](landrun/index.md) - the Landlock-only kernel CLI wrapper with the category's largest wrapper-class footprint and Ubuntu and Debian packages, commit train resumed October 2026 with unreleased ABI 10 and UDP work.
- [Microsandbox](microsandbox/index.md) - the libkrun microVM runtime with container workflows, agent-created sandboxes via skills and MCP, and the category's largest HN launch.
- [NemoClaw](nemoclaw/index.md) - NVIDIA's Apache-2.0 reference stack that installs, hardens, and operates OpenClaw, Hermes, and LangChain Deep Agents inside OpenShell sandboxes with managed inference and lifecycle ops.
- [nono](nono/index.md) - the Sigstore team's kernel capability sandbox that brokers each delegated tool separately and proxies credentials scoped per endpoint.
- [NVX](nvx/index.md) - Microsoft's OpenVMM research sandbox for agentic workloads with Windows hypervisor paths and limits docs that name what the ABI does not do.
- [OpenSandbox](opensandbox/index.md) - the Apache-2.0 general sandbox platform (SDKs, CLI, MCP, K8s runtimes) that grew on GitHub trend charts, not Hacker News.
- [OpenShell](openshell/index.md) - NVIDIA's container-and-MicroVM runtime where declarative policy and inference-proxy keys make the boundary credible.
- [Overalls](overalls/index.md) - Geoffrey Huntley's self-hosted platform of persistent Firecracker microVM dev machines, the renamed Weaving Loom, opening as a research preview on 3 November 2026.
- [Sandstorm](sandstorm/index.md) - DeepLethe's fleet-scale sandbox lifecycle manager, pausing idle gVisor containers and Firecracker microVMs to disk and restoring them on demand, unreleased since July 2026.
- [Yolobox](yolobox/index.md) - the container wrapper that gives coding agents full sudo inside while the home directory stays unmounted, accidents fenced and attackers out of scope by its own docs.

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
- 2026-10-09 - Added Landrun.
- 2026-10-09 - Added Yolobox.
- 2026-10-12 - Added aicontainer.
- 2026-10-12 - Added Brood Box.
- 2026-10-12 - Added Container Use.
- 2026-10-21 - Added Overalls.
- 2026-10-31 - Added Sandstorm.
