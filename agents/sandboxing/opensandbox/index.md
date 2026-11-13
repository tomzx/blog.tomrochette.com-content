---
title: OpenSandbox
created: 2026-09-16
updated: 2026-11-13
readability: 3
audience_notes: >
  Engineers choosing a self-hosted sandbox platform for AI agent workloads such as code execution, GUI agents, or agent evaluations.
  Assumes you know what a container, a microVM, and a Kubernetes cluster are.
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, isolation, kubernetes]
---

OpenSandbox is a general-purpose, Apache-2.0 sandbox platform for AI applications under the opensandbox-group GitHub organization, offering multi-language SDKs, a CLI, an MCP server, and Docker and Kubernetes runtimes for coding agents, GUI agents, evaluations, code execution, and RL training.

## What it is

**OpenSandbox is not one boundary but a platform around boundaries: it standardizes sandbox lifecycle, execution, files, and credentials across runtimes, and you choose how hard each boundary is.**
The project transferred from alibaba/OpenSandbox (the old URL redirects), and the provenance still shows in the artifacts, which publish as com.alibaba.opensandbox on Maven, @alibaba-group/opensandbox on npm, and a github.com/alibaba module path for Go.
Surfaces shipped in-repo cover Python, Java/Kotlin, JavaScript/TypeScript, C#/.NET, and Go SDKs, the osb CLI, an MCP server, and a documented Sandbox Protocol with lifecycle and execution APIs.
An ingress gateway with per-sandbox egress controls handles network policy, a Credential Vault injects secrets for outbound requests without exposing them to workloads, and deployment is self-hosted: a Docker server locally, a Kubernetes runtime for clusters.

## Status

**Very active and exceptionally fast-growing for a nine-month-old repo, with traction that is vendor-driven rather than organic Hacker News adoption.**
15,883 stars and 1,472 forks as of 2026-10-16, repo created 2025-12-17, pushed 2026-11-13, on a unified umbrella version line that covers the server, component images, charts, CLI, and every SDK from one commit and a signed BOM, with latest stable release 1.2.1 on 2026-11-13, the patch-line umbrella cut shipping server, CLI, charts, images, and all five SDK packages together after release-1.2.1-rc.1 (2026-11-04) and release-1.2.1-rc.2 (2026-11-11).
The 1.1.1 cut fixes the broken 1.1.0 opensandbox-server wheel (the committed FastPath gRPC stubs now ship in the package, and PyPI is immutable so the fix lives on this line) and adds identity-bound filesystem operations across all five SDKs, multi-tenant isolation in a shared Kubernetes namespace, a typed upstream-proxy egress configuration, and pause/resume bridged to the kubernetes-sigs/agent-sandbox CRD's operating mode.
The 1.2.0 line opened with release-1.2.0-rc.1 on 2026-10-15, carrying OSEP-0024 auto-pause and wake-on-access for fast sandboxes end to end (the opt-in lifecycle.idlePolicy field, the server-side idle sweeper, and the SDK wake-retry contract), an opt-in experimental egress-sidecar revision with live credential-bound Vault admission, an SDK fix that stops capping file transfers at the 30-second request timeout, and a first optional web console slice; SDK and CLI packages publish only at the stable bump.
Release-1.2.0-rc.2 followed on 2026-10-21 with the Credential Vault (OSEP-0022) landed end to end for fast sandboxes: the egress sidecar holds the vault with durable per-subject persistence and sealed snapshot transfer across pause and resume, the server exposes a user-reachable vault API whose reads never return credential values, and a pool-pinned MITM CA terminates the inspected traffic, while the classic profile gains port-scoped NetworkRules that fast sandboxes reject fail-closed until their enforcement path ships.
The stable 1.2.0 cut followed on 2026-10-27, asking everyone on 1.1.x to upgrade and carrying a post-release-candidate hardening delta, with SDK and CLI packages publishing at the stable bump.
Release-1.2.1-rc.1 (2026-11-04) cut the first patch-line candidate from 1.2.0 with OSEP-0025 Credential Vault Exchange: an `exchange` credential source resolving per-request headers through a pluggable resolver, fail-closed and never persisted, wired across the egress sidecar, the server, and all five SDKs, plus execd atomic uploads that keep the old file on a failed write, digest validation for rootfs snapshots, Kubernetes create-timeout startup diagnostics, and informer-cache scoping for large clusters; rc releases publish images but hold SDK and CLI packages for the 1.2.1 stable bump.
Release-1.2.1-rc.2 followed on 2026-11-11 with OSEP-0026 resource-aware oversubscription landed end to end (template machine shapes recorded at build time, forwarded as per-sandbox limits on ResourceAware pools, and replayed across snapshot restores under a dedicated KVM verify lane), fast-sandbox port-scoped egress parity, the OSEP-0023 subject revision runtime reaching an enforced readiness gate, opt-in rootfs-only OCI snapshots, and a batch closing data-loss and availability bugs (closed request objects now reject unknown fields, a controller restart can no longer evict the pods of live sandboxes, and the server-proxied data path entered maintenance mode).
The stable 1.2.1 cut followed on 2026-11-13, publishing the SDK and CLI packages at last alongside the server, charts, and images: OSEP-0025 exchange credentials and OSEP-0026 oversubscription stable across all five SDKs (Kotlin and C# consumers must recompile against the widened credential models), multi-version managed Firecracker bundles (1.16.1 and 1.17.0) that restore with the exact recorded VMM version, staged uploads and controller-restart pod recovery against overwrite data loss, the server-proxied data path entering maintenance mode in favor of the ingress gateway, unknown-field rejection on closed request objects, Docker writable-layer disk quotas, SHA-256-pinned OCI template artifacts, and a browser PTY shell in the console.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=opensandbox-group/OpenSandbox&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=opensandbox-group/OpenSandbox&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=opensandbox-group/OpenSandbox&type=date&legend=top-left" />
</picture>

The current organization was created 2026-06-04 as part of the transfer out of Alibaba.
Hacker News is conspicuously absent: the threads are a 2-pointer from March 2026 linking the pre-transfer alibaba URL, a 1-pointer to the website, and a 4-pointer whose title borrows OpenSandbox's tagline but whose URL points at a competitor's repo (a submission error), while a 4-point January "Show HN: Open Sandbox" is an unrelated same-name project.

## Strengths

- The broadest surface in the category: five SDK languages, CLI, MCP, sandbox environments for code execution, browsers, and full desktops, and worked examples for Claude Code, Codex, Gemini CLI, OpenCode, and more.
- Supply-chain hygiene beyond peers: release images are cosign-signed keylessly with provenance attestations across Docker Hub, GHCR, and Alibaba's registry, with a published verification guide.
- Isolation is selectable per trust level: default runc, or gVisor, Kata on QEMU, Firecracker, or Cloud Hypervisor via the secure-container guide.
- An open Sandbox Protocol and enhancement proposals make the platform extendable rather than a closed product.

## Cautions

- **The default boundary is an ordinary runc container, so an unconfigured deployment has container-grade isolation only, with the strong runtimes behind opt-in configuration.**
- chenhunghan's March 2026 sandbox comparison rated OpenSandbox container yes, VM no, network yes; the comparison predates the current guide's Firecracker and Cloud Hypervisor options, but independent adversarial review of the platform itself is still thin.
- The missing HN footprint alongside 15k stars, plus the Trendshift badge, Discord and DingTalk groups, and triple-registry presence, reads as deliberate promotion machinery; treat the stars as marketing reach, not field evidence.
- Component versioning ended with the 1.1.0 umbrella release, but a nine-month-old repo with a five-month-old organization still means API churn is likely, and the umbrella process already shipped one dud: the 1.1.0 server wheel on PyPI was broken at import time, with the fix arriving on the 1.1.1 line nine days later.

## Pricing

Free, Apache-2.0, self-hosted; no hosted offering or pricing page found on open-sandbox.ai or in the repo as of 2026-10-02.
Costs are the Docker or Kubernetes infrastructure you run it on.

## Compared to

- [Agent Sandbox](../agent-sandbox/index.md): the Kubernetes CRD orchestrates sandbox pods and deliberately delegates the isolation boundary; OpenSandbox ships runtimes and an SDK surface instead, so the two are complementary rather than competing.
- [OpenShell](../openshell/index.md): NVIDIA's runtime is workstation-first with kernel policy domains and key interception at an inference proxy; choose OpenSandbox for platform scale and workload breadth, OpenShell for per-developer policy.
- E2B-class hosted APIs: zero infrastructure and per-second billing; OpenSandbox is the self-hosted platform answer with no hosted tier, so you trade operations for control.

## Bottom line

**Recommended for teams that want one self-hosted platform serving coding agents, GUI agents, and evaluations across Docker and Kubernetes, with the isolation level chosen deliberately per workload.**
Not for anyone who needs hardened isolation by default, an independently audited boundary, or a hosted API today.

## Changes

- 2026-09-16 - Created.
- 2026-09-25 - Growth refreshed (15,504 stars, 1,425 forks), and the latest release recorded as the first stable 1.1.0 umbrella release of 2026-09-21, which retires the component-wise server/v0.2.3 versioning the note previously described.
- 2026-09-27 - Growth refreshed (15,529 stars, 1,429 forks, pushed 2026-09-27); 1.1.0 remains the latest release, holding the umbrella line steady.
- 2026-10-02 - Recorded the 1.1.1-rc.1 prerelease (2026-09-28), cut to fix the broken 1.1.0 opensandbox-server wheel on PyPI, added that fact to Cautions, and refreshed growth (15,641 stars, 1,443 forks, pushed 2026-10-01).
- 2026-10-07 - Added the opensandbox-group/OpenSandbox star history chart to the Status section.
- 2026-10-10 - Recorded the stable 1.1.1 cut of 2026-10-09 (the wheel fix shipped, identity-bound filesystem operations in all five SDKs, multi-tenant namespace isolation, typed upstream-proxy config, and pause/resume bridged to the agent-sandbox CRD), and refreshed counts (15,768 stars, 1,451 forks, pushed 2026-10-10).
- 2026-10-17 - Recorded release-1.2.0-rc.1 (2026-10-15, OSEP-0024 auto-pause and wake-on-access end to end, the experimental egress-sidecar revision with credential-bound Vault admission, the file-transfer timeout fix, and the first web console slice; rotation re-verification, every cited URL re-fetched).
- 2026-10-23 - Recorded release-1.2.0-rc.2 (2026-10-21, the OSEP-0022 Credential Vault landed end to end for fast sandboxes: egress-held vault with durable per-subject persistence and sealed pause/resume transfer, a user-reachable server-routed vault API whose reads never return credential values, a pool-pinned MITM CA, and port-scoped NetworkRules in the classic profile).
- 2026-11-01 - Recorded the stable 1.2.0 release of 2026-10-27 (the OSEP-0024 auto-pause and OSEP-0022 credential-vault umbrella cut, the post-rc hardening delta, SDK and CLI packages publishing at the stable bump, and an upgrade ask for everyone on 1.1.x), with the post-stable train opening OSEP-0025 egress work and the repository pushed 2026-11-01.
- 2026-11-07 - Recorded release-1.2.1-rc.1 (2026-11-04, the first patch-line candidate cut from 1.2.0: OSEP-0025 Credential Vault Exchange with the pluggable per-request header resolver fail-closed across egress, server, and all five SDKs, execd atomic uploads, digest-validated rootfs snapshots, Kubernetes create-timeout diagnostics, and informer-cache scoping, images published but packages held for the stable bump), with the repository pushed 2026-11-07.
- 2026-11-08 - Volatile refresh for the post-rc train (OSEP-0023 fast-sandbox subject-snapshot mutations, port-scoped egress rules enforced per subject in the fast-sandbox profile, and the PATCH policy-merge fixes keeping untouched same-scope rules), with release-1.2.1-rc.1 still the newest release and the repository pushed 2026-11-08.
- 2026-11-13 - Recorded the stable 1.2.1 release of 2026-11-13 (the umbrella cut publishing server, CLI, charts, images, and all five SDK packages at 1.2.1: OSEP-0025 exchange credentials and OSEP-0026 resource-aware oversubscription stable with a Kotlin and C# recompile requirement, multi-version managed Firecracker bundles with exact-recorded-version restores, staged uploads and controller-restart pod recovery, the server-proxied data path in maintenance mode, unknown-field rejection, Docker writable-layer disk quotas, SHA-256-pinned OCI template artifacts, and a browser PTY console shell), with the repository pushed 2026-11-13.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [Agent Sandbox](../agent-sandbox/index.md) - the Kubernetes orchestrator OpenSandbox documents an integration example for
- [OpenShell](../openshell/index.md) - the workstation-first runtime with the parallel credential-injection design
- [Claude Code](../../harnesses/claude-code/index.md) - the coding agent with the most prominent worked example in the repo
- [Executions Feature Matrix](../../executions/executions-feature-matrix/index.md) - the unattended runs these sandboxes host

## References

- https://github.com/opensandbox-group/OpenSandbox - repository README: platform scope, SDKs, CLI, MCP, Sandbox Protocol, registries, cosign signing, badges
- https://api.github.com/repos/opensandbox-group/OpenSandbox - stars, forks, license, creation and push dates as of 2026-09-25
- https://api.github.com/repos/opensandbox-group/OpenSandbox/releases/latest - the latest stable release record, now the 1.1.1 cut of 2026-10-09
- https://api.github.com/repos/opensandbox-group/OpenSandbox/releases/tags/release-1.1.1 - the 1.1.1 release notes: the wheel fix and the server and SDK changes
- https://api.github.com/repos/opensandbox-group/OpenSandbox/releases/tags/release-1.2.0-rc.1 - the 1.2.0-rc.1 release notes: OSEP-0024 auto-pause, the egress-sidecar revision, and the SDK timeout fix
- https://raw.githubusercontent.com/opensandbox-group/OpenSandbox/main/docs/guides/secure-container.md - the runc default plus gVisor, Kata, Firecracker, and Cloud Hypervisor runtimes
- https://open-sandbox.ai - the live project site
- https://hn.algolia.com/api/v1/items/47464648 - chenhunghan's local-sandbox comparison rating OpenSandbox container yes, VM no, network yes (March 2026)
- https://hn.algolia.com/api/v1/items/47203397 - the 2-point March 2026 thread linking the pre-transfer alibaba URL
- https://hn.algolia.com/api/v1/items/49100880 - the 4-point July thread titled with OpenSandbox's tagline but linking a competitor's repo
- https://hn.algolia.com/api/v1/items/46832620 - the unrelated same-name diggerhq project's Show HN thread
