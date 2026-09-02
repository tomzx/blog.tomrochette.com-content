---
title: Agent Sandbox
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, kubernetes, isolation, open-source]
readability: 3
audience_notes: >
  Platform engineers who want declarative, cluster-scale sandboxes for agent runtimes on Kubernetes.
  Assumes you know what a CRD, a RuntimeClass, and gVisor are.
---

Agent Sandbox is a Kubernetes SIG Apps project, announced by Google Cloud at KubeCon NA 2025, that provides a `Sandbox` CRD and controller for declaratively managing isolated, stateful, singleton pods with warm pools, aimed at AI agent runtimes and reinforcement learning, while delegating actual isolation to runtimes like gVisor or Kata.
Facts below verified as of 2026-09-02.

**Agent Sandbox is deliberately not an isolation boundary: it is the orchestration layer around one, and its own threat model says plainly that without gVisor or Kata configured, a sandbox is just an ordinary pod.**

## What it is

A Go operator introducing CRDs in the `agents.x-k8s.io` group at `v1beta1`: `Sandbox` (a single stateful pod with stable hostname and pause-resume lifecycle), `SandboxTemplate`, `SandboxWarmPool` (pre-warmed capacity), and `SandboxClaim` (allocation from a pool).
Go and Python SDKs, a router, an in-pod daemon, and an MCP server ship alongside; install paths cover kubectl, Helm, and OLM.
Isolation comes from the runtime you select via RuntimeClass, not from the project itself.
Apache-2.0, developed under Kubernetes SIG Apps with Google Cloud backing, built foundationally on gVisor; NVIDIA ships an official NeMo Gym integration for RL workloads.

## Status

Young but institutionally backed: 3,713 stars, 478 forks, 213 open issues and PRs as of 2026-09-02, created 2025-08-12, pushed 2026-09-01.
v1.0.0 released 2026-08-28, sixteen releases in about seven months, 918 commits.
**The v1.0.0 tag is not API stability: the API is `v1beta1`, v1alpha1 was removed in the same release, and upgrades from older versions require a documented four-step migration.**

## Strengths

- Warm pools and claims built for latency, with Google claiming sub-second allocation on GKE and the roadmap marking 300 sandboxes per second as done.
- Vendor-neutral isolation: pick gVisor or Kata per workload instead of marrying one sandbox technology.
- Real SDKs and a documented threat model, unusual rigor for a project this young.
- The Kubernetes-native path for agent fleets shared across teams and tenants, with RBAC and NetworkPolicy inherited.

## Cautions

- Hard Kubernetes requirement: this does not exist outside a cluster you operate.
- It isolates nothing by itself, and the default router authorizer is AllowAll, which the threat model admits.
- API churn: forced migrations between minor versions, direct upgrades below v0.5.0 unsupported.
- Missing connection-level limits on upgraded WebSocket connections, a roadmap item that matters for untrusted traffic.

## Pricing

N/A, Apache-2.0 open source with no commercial product.
Costs are the Kubernetes infrastructure; on GKE, adjacent managed features are billed separately by Google Cloud.

## Compared to

- [OpenShell](../openshell/index.md): the local-first, policy-engine-complete runtime for developer machines; choose agent-sandbox for cluster-scale, API-driven fleets, OpenShell for the workstation.
- Plain Docker: fine for local experiments; agent-sandbox is what those become when they need stable identity, warm pools, and multi-tenant hard isolation in production.
- E2B and Modal: hosted sandbox APIs with zero infrastructure; choose them for sporadic workloads and no-K8s teams, agent-sandbox for data residency and sustained volume cost control.

## Bottom line

**Recommended for platform teams already running Kubernetes who need to serve many agent runtimes or RL environments as governed infrastructure.**
Not for local developer sandboxing, and not for anyone expecting the 1.0 tag to mean a frozen API.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [OpenShell](../openshell/index.md) - the workstation-layer counterpart
- [Executions Feature Matrix](../executions-feature-matrix/index.md) - the runs these sandboxes would host
- [agent-skills-open-standard](../agent-skills-open-standard/index.md) - no relation, but the other infrastructure-flavored standard in the section

## References

- https://github.com/kubernetes-sigs/agent-sandbox - repository, CRDs, SIG Apps scope, SDKs
- https://github.com/kubernetes-sigs/agent-sandbox/releases/tag/v1.0.0 - the release, migration requirements, and integration news
- https://raw.githubusercontent.com/kubernetes-sigs/agent-sandbox/HEAD/docs/security/threat_model.md - the project's own security gaps, the critical source
- https://cloud.google.com/blog/products/containers-kubernetes/agentic-ai-on-kubernetes-and-gke - the Google announcement and gVisor foundation
- https://e2b.dev/docs - the hosted-sandbox comparison
- https://modal.com/docs/guide/sandboxes - the Modal sandbox comparison
