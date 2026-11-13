---
title: Agent Sandbox
created: 2026-08-30
updated: 2026-11-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, kubernetes, isolation, open-source]
readability: 3
audience_notes: >
  Platform engineers who want declarative, cluster-scale sandboxes for agent runtimes on Kubernetes.
  Assumes you know what a CRD, a RuntimeClass, and gVisor are.
---

Agent Sandbox is a Kubernetes SIG Apps project, announced by Google Cloud at KubeCon NA 2025, that provides a `Sandbox` CRD and controller for declaratively managing isolated, stateful, singleton pods with warm pools, aimed at AI agent runtimes and reinforcement learning, while delegating actual isolation to runtimes like gVisor or Kata.

**Agent Sandbox is deliberately not an isolation boundary: it is the orchestration layer around one, and its own threat model says plainly that without gVisor or Kata configured, a sandbox is just an ordinary pod.**

## What it is

A Go operator introducing CRDs in the `agents.x-k8s.io` group at `v1beta1`: `Sandbox` (a single stateful pod with stable hostname and pause-resume lifecycle), `SandboxTemplate`, `SandboxWarmPool` (pre-warmed capacity), and `SandboxClaim` (allocation from a pool).
Go and Python SDKs, a router, an in-pod daemon, and an MCP server ship alongside; install paths cover kubectl, Helm, and OLM.
Isolation comes from the runtime you select via RuntimeClass, not from the project itself.
Apache-2.0, developed under Kubernetes SIG Apps with Google Cloud backing, built foundationally on gVisor; NVIDIA ships an official NeMo Gym integration for RL workloads.

## Status

Young but institutionally backed: 4,268 stars, 564 forks, 180 open issues and PRs as of 2026-10-16, created 2025-08-12, pushed 2026-11-12.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=kubernetes-sigs/agent-sandbox&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=kubernetes-sigs/agent-sandbox&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=kubernetes-sigs/agent-sandbox&type=date&legend=top-left" />
</picture>

v1.0.0 released 2026-08-28 with v1.0.1 on 2026-09-03, v1.0.2 on 2026-09-11, v1.0.3 on 2026-09-17, v1.0.4 on 2026-09-24, v1.0.5 on 2026-10-01 (a runtime connectivity layer for the TypeScript SDK, native in-cluster sandboxd transport, streaming file transfers, and an OpenAI Agents integration), and v1.0.6 on 2026-10-08 (the first part of a multi-cluster warm-pool fleet planner, interactive processes via `commands.start()` in the TypeScript SDK, and Go and Python SDK parity, with a name-length CEL rule that fails updates of pre-existing over-length `spec.service` sandboxes), and v1.0.7 on 2026-10-15 (optional bearer-token authentication for sandboxd, streaming command execution in the Go SDK, closer Python and TypeScript SDK parity, and warm pools that hold members waiting on scheduling gates instead of deleting them, with behavior changes to signal exit codes and the Python SDK's logging setup), twenty-nine releases since October 2025, 1,167 commits as of the v1.0.7 recording.
v1.0.8 followed on 2026-10-22: MCP `execute_command` output is now bounded to a 30,000-character default with four new required truncation fields (breaking for strict schema-validating clients), failed Pods get opt-in recovery, GKE Pod Snapshot primitives arrive for RL workloads, the Go SDK reaches provisioning parity with Python, and the sandbox-router deployment became a Kustomization with hardened credentials.
**The v1.0.0 tag is not API stability: the API is `v1beta1`, v1alpha1 was removed in the same release, and upgrades from older versions require a documented four-step migration.**
v1.0.9 followed on 2026-10-29: native gRPC proxying in the sandbox-router (including sandboxd's ProcessService), a Helm chart for the router, WebSockets through the router working again (broken since v1.0.7), directory watching in sandboxd, warm-pool adoption and suspend fixes, and streaming command execution in the Python SDK, with an action-required NetworkPolicy change that opens router egress on TCP 9090 across every namespace under the default allow-all authorizer.
v1.0.10 followed on 2026-11-06: gRPC-Web transcoding in the router for browser clients (same-origin by default, an origin allowlist flag for CORS), sandboxd unary execution limits (`ExecuteWithLimits` with time and output caps enforced once the new daemon flags are set), expanded file operations (directory creation, recursive listing, create-only writes, move, copy, and tar extraction), `ConnectivityRouterPortForward` for Kata and gVisor in the Go SDK, fixed `SandboxClaim` mirroring and warm-pool replica accounting, and new examples for Hyperlight micro-VMs, GKE L4 GPU snapshots, OpenCode, and multi-tenant RL, plus breaking changes: the router's `Options.ProbeAddr` removed for Go users, OLM bundles requiring upstream OLM v0.32.0 or later, and another action-required NetworkPolicy rework.
v1.0.11 followed on 2026-11-12: browser path-prefix routing in the sandbox router for applications like JupyterLab (with automatic `Set-Cookie` and redirect `Location` rewriting under the prefix by default, an opt-out flag for legacy pass-through), sandboxd authentication through a header token that survives proxies stripping `Authorization`, symlink-safe file deletion and named-pipe rejection in the file endpoints, request-body preservation on dial retries, router-tunnel connection config in the Python SDK, `mkdir`, `move`, `copy`, `append`, and `create_only` file operations across the Python, Go, and TypeScript SDKs, a controller fix that stops terminating pods reporting `Ready=True`, and new examples for AWS Nitro Enclaves on EKS and a scoped-token MCP server, with three breaking changes (the response rewriting, a 5-second Python SDK signal timeout raising `TimeoutError`, and an `operating_mode` label that splits the `agent_sandboxes` metric series for raw PromQL).

## Strengths

- Warm pools and claims built for latency, with Google claiming sub-second allocation on GKE and the roadmap marking 300 sandboxes per second as done.
- Vendor-neutral isolation: pick gVisor or Kata per workload instead of marrying one sandbox technology.
- Real SDKs and a documented threat model, unusual rigor for a project this young.
- The Kubernetes-native path for agent fleets shared across teams and tenants, with RBAC and NetworkPolicy inherited.

## Cautions

- Hard Kubernetes requirement: this does not exist outside a cluster you operate.
- It isolates nothing by itself, and the default router authorizer is AllowAll, which the threat model admits; v1.0.10's router NetworkPolicy restricts sandbox egress to pods carrying the sandbox-name-hash label but opens API-server ports 443 and 6443 plus DNS to any destination, so under AllowAll a sandbox can still reach API-server endpoints unless operators set `networkPolicy.apiServerCIDRs`.
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

## Changes

- 2026-08-30 - Created in the Sandboxing category seed with the isolates-nothing-by-itself threat model.
- 2026-09-18 - v1.0.3 released 2026-09-17 (configurable TLS controls, sandboxd process-group cleanup, execution-scoped credentials and egress-policy blueprints), the release count moving from twenty-two to twenty-three and commits from 987 to 997, with growth refreshed (3,936 stars, 206 open issues and PRs).
- 2026-09-25 - v1.0.4 released 2026-09-24, the release count moving to twenty-four and commits to 1,029, with growth refreshed (4,021 stars, 200 open issues and PRs).
- 2026-09-27 - Growth refreshed (4,037 stars, 528 forks, 202 open issues and PRs, pushed 2026-09-25); v1.0.4 remains the latest release.
- 2026-10-02 - Recorded v1.0.5 (2026-10-01, runtime connectivity for the TypeScript SDK, in-cluster sandboxd transport, streaming file transfers, OpenAI Agents integration), the release count moving to twenty-five and commits to 1,069, with growth refreshed (4,118 stars, 539 forks).
- 2026-10-07 - Added the kubernetes-sigs/agent-sandbox star history chart to the Status section.
- 2026-10-09 - Recorded v1.0.6 (2026-10-08, the first part of a multi-cluster warm-pool fleet planner, interactive TypeScript SDK processes, Go and Python SDK parity, and the name-length CEL admission rule with its pre-existing-object caveat), the release count moving to twenty-six and commits to 1,125, with growth refreshed (4,198 stars, 548 forks, pushed 2026-10-09).
- 2026-10-16 - Recorded v1.0.7 (2026-10-15, sandboxd bearer-token authentication, streaming Go SDK execution, deeper Python and TypeScript SDK parity, warm pools holding scheduling-gated members, and the signal-exit-code and Python-logging behavior changes), the release count moving to twenty-seven and commits to 1,167, with growth refreshed (4,268 stars, 564 forks, pushed 2026-10-15).
- 2026-10-23 - Recorded v1.0.8 (2026-10-22, MCP command output bounded at a 30,000-character default with new required truncation fields and breaking effect for strict schema validators, opt-in recovery from failed Pods, GKE Pod Snapshot primitives for RL, Go SDK provisioning parity, and the sandbox-router Kustomization move with hardened credentials), the release count moving to twenty-eight.
- 2026-11-01 - Rotation re-verification: every cited URL re-fetched and alive (repository, the v1.0.0 release page, the threat model, the Google announcement, and the E2B and Modal comparison docs); recorded v1.0.9 (2026-10-29, native gRPC proxying in the sandbox-router with a router Helm chart, WebSockets through the router working again after the v1.0.7 break, sandboxd directory watching, warm-pool adoption and suspend fixes, streaming Python SDK execution, and the action-required NetworkPolicy opening router egress on TCP 9090 in every namespace), the release count moving to twenty-nine and the repository pushed 2026-10-31.
- 2026-11-07 - Recorded v1.0.10 (2026-11-06, gRPC-Web transcoding in the router for browser clients, sandboxd unary execution limits with time and output caps, expanded file operations, ConnectivityRouterPortForward for Kata and gVisor in the Go SDK, claim-mirroring and warm-pool accounting fixes, and new Hyperlight, GKE L4 GPU snapshot, OpenCode, and multi-tenant RL examples; breaking removal of the router's Options.ProbeAddr, OLM bundles requiring upstream OLM v0.32.0 or later, and a NetworkPolicy rework that scopes sandbox egress but opens API-server ports to any destination), the release count moving to thirty and the Cautions bullet updated to the v1.0.10 posture, with the repository pushed 2026-11-07.
- 2026-11-13 - Recorded v1.0.11 (2026-11-12, browser path-prefix routing in the sandbox router with automatic Set-Cookie and redirect-Location rewriting, sandboxd header-token authentication that survives Authorization-stripping proxies, symlink-safe deletion and named-pipe rejection, SDK file-operation expansion with router-tunnel connections, the PodTerminating readiness fix, and AWS Nitro Enclaves and scoped-token MCP server examples, with the response-rewrite, signal-timeout, and metric-label breaking changes), the release count moving to thirty-one, with the repository pushed 2026-11-12.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [OpenShell](../openshell/index.md) - the workstation-layer counterpart
- [Executions Feature Matrix](../../executions/executions-feature-matrix/index.md) - the runs these sandboxes would host
- [agent-skills-open-standard](../../skills/agent-skills-open-standard/index.md) - no relation, but the other infrastructure-flavored standard in the section

## References

- https://github.com/kubernetes-sigs/agent-sandbox - repository, CRDs, SIG Apps scope, SDKs
- https://github.com/kubernetes-sigs/agent-sandbox/releases/tag/v1.0.0 - the release, migration requirements, and integration news
- https://raw.githubusercontent.com/kubernetes-sigs/agent-sandbox/HEAD/docs/security/threat_model.md - the project's own security gaps, the critical source
- https://cloud.google.com/blog/products/containers-kubernetes/agentic-ai-on-kubernetes-and-gke - the Google announcement and gVisor foundation
- https://docs.e2b.dev/ - the hosted-sandbox comparison
- https://modal.com/docs/guide/sandboxes - the Modal sandbox comparison
