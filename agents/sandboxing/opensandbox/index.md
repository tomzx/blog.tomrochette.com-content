---
title: OpenSandbox
created: 2026-09-16
updated: 2026-09-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, isolation, kubernetes]
readability: 3
audience_notes: >
  Engineers choosing a self-hosted sandbox platform for AI agent workloads such as code execution, GUI agents, or agent evaluations.
  Assumes you know what a container, a microVM, and a Kubernetes cluster are.
---

OpenSandbox is a general-purpose, Apache-2.0 sandbox platform for AI applications under the opensandbox-group GitHub organization, offering multi-language SDKs, a CLI, an MCP server, and Docker and Kubernetes runtimes for coding agents, GUI agents, evaluations, code execution, and RL training.
Facts below verified as of 2026-09-25.

## What it is

**OpenSandbox is not one boundary but a platform around boundaries: it standardizes sandbox lifecycle, execution, files, and credentials across runtimes, and you choose how hard each boundary is.**
The project transferred from alibaba/OpenSandbox (the old URL redirects), and the provenance still shows in the artifacts, which publish as com.alibaba.opensandbox on Maven, @alibaba-group/opensandbox on npm, and a github.com/alibaba module path for Go.
Surfaces shipped in-repo cover Python, Java/Kotlin, JavaScript/TypeScript, C#/.NET, and Go SDKs, the osb CLI, an MCP server, and a documented Sandbox Protocol with lifecycle and execution APIs.
An ingress gateway with per-sandbox egress controls handles network policy, a Credential Vault injects secrets for outbound requests without exposing them to workloads, and deployment is self-hosted: a Docker server locally, a Kubernetes runtime for clusters.

## Status

**Very active and exceptionally fast-growing for a nine-month-old repo, with traction that is vendor-driven rather than organic Hacker News adoption.**
15,504 stars and 1,425 forks as of 2026-09-25, repo created 2025-12-17, pushed 2026-09-24, latest release 1.1.0 on 2026-09-21, the first stable release of a unified umbrella version line that covers the server, component images, charts, CLI, and every SDK from one commit and a signed BOM.
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
- Component versioning ended with the 1.1.0 umbrella release, but a nine-month-old repo with a five-month-old organization still means API churn is likely.

## Pricing

Free, Apache-2.0, self-hosted; no hosted offering or pricing page found on open-sandbox.ai or in the repo as of 2026-09-18.
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

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [Agent Sandbox](../agent-sandbox/index.md) - the Kubernetes orchestrator OpenSandbox documents an integration example for
- [OpenShell](../openshell/index.md) - the workstation-first runtime with the parallel credential-injection design
- [Claude Code](../../harnesses/claude-code/index.md) - the coding agent with the most prominent worked example in the repo
- [Executions Feature Matrix](../../executions/executions-feature-matrix/index.md) - the unattended runs these sandboxes host

## References

- https://github.com/opensandbox-group/OpenSandbox - repository README: platform scope, SDKs, CLI, MCP, Sandbox Protocol, registries, cosign signing, badges
- https://api.github.com/repos/opensandbox-group/OpenSandbox - stars, forks, license, creation and push dates as of 2026-09-25
- https://api.github.com/repos/opensandbox-group/OpenSandbox/releases/latest - the first stable 1.1.0 umbrella release of 2026-09-21
- https://raw.githubusercontent.com/opensandbox-group/OpenSandbox/main/docs/guides/secure-container.md - the runc default plus gVisor, Kata, Firecracker, and Cloud Hypervisor runtimes
- https://open-sandbox.ai - the live project site
- https://hn.algolia.com/api/v1/items/47464648 - chenhunghan's local-sandbox comparison rating OpenSandbox container yes, VM no, network yes (March 2026)
- https://hn.algolia.com/api/v1/items/47203397 - the 2-point March 2026 thread linking the pre-transfer alibaba URL
- https://hn.algolia.com/api/v1/items/49100880 - the 4-point July thread titled with OpenSandbox's tagline but linking a competitor's repo
- https://hn.algolia.com/api/v1/items/46832620 - the unrelated same-name diggerhq project's Show HN thread
