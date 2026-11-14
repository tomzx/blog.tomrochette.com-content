---
title: Agent Substrate
created: 2026-11-14
updated: 2026-11-14
readability: 3
audience_notes: >
  Platform engineers deciding how to run many concurrent, mostly idle agent sessions on Kubernetes with strong isolation.
  Assumes you know what a Kubernetes Pod, a sandbox, and a microVM are.
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, kubernetes, agent-execution, zero-trust, open-source]
---

Agent Substrate is a Google-founded, Apache-2.0 agent execution runtime under the agent-substrate GitHub organization, accepted into the CNCF Sandbox in October 2026, that maps stateful agent sessions (Actors) onto a warm pool of sandboxed Kubernetes Workers and suspends idle sessions to full-state snapshots that resume in under 500 milliseconds.

## What it is

**Agent Substrate proposes a new unit of compute for agent sessions: an Actor that carries memory, files, and identity between warm Workers, so a session pays for compute only while it acts.**
An Actor is an ordinary OCI container image holding an agent session's filesystem, environment, memory state, and network rules, and a Worker is a pre-warmed Kubernetes Pod drawn from a WorkerPool.
When a request arrives for a suspended Actor, the atenet-router holds it in memory (request parking), the controller claims a warm Worker, and the Actor's memory and disk restore from tiered storage onto any available Worker in under 500 milliseconds.
Isolation is gVisor or Cloud Hypervisor microVMs per Actor, one lifecycle for both, and plain containers are unsupported by design.
The zero-trust model gives each Actor a short-lived SPIFFE X.509 identity, launches it credential-free with no inbound or outbound network by default, and injects API keys and tokens out-of-band at the egress gateway from pluggable secret stores.
It runs on any Kubernetes 1.37+ cluster as open source, with a managed surface as Agent Substrate on GKE, and a `kubectl ate` CLI for the actor lifecycle.
Google created it and remains its steward; Solo.io co-maintains it and ships its kagent 1.0 platform layer on top, and NVIDIA contributes upstream around Dynamo, KAI Scheduler, and DSX OS interoperability.

## Status

**Active and heavily backed, with the strongest institutional adoption story in the category and almost no independent community discussion.**
6,610 stars and 746 forks as of 2026-11-14, repository created 2026-05-13, pushed 2026-11-13, with roughly 129 contributors listed by the GitHub API as of 2026-11-14 (Google and Solo.io both say more than 100 contributors from 40-plus organizations).
The v1.0.0 release ("Fully armed and operational") was published 2026-11-05, the day the donation was announced.
The CNCF Sandbox application (cncf/sandbox#523) was created 2026-09-08 and closed as accepted 2026-10-20; Google announced the donation of Agent Substrate, gVisor, and OpenRL on 2026-11-05 ahead of KubeCon North America in Salt Lake City, and the CNCF counted Agent Substrate among its new Sandbox projects in the 2026-11-10 milestone announcement (portfolio at 231 projects).
The managed surface followed the open-source project: Agent Substrate on GKE was announced 2026-09-15 for non-production use with production support via allowlist, then declared generally available on 2026-11-05 alongside the 1.0 release.
Adoption is vendor and partner grade: kagent 1.0 rebuilt its entire runtime on Agent Substrate and went GA 2026-11-10 with OutSystems and Swissquote in production, Nous Research is building Hermes Enterprise on it, NVIDIA documents Dynamo and KAI Scheduler integrations, and VMware demonstrated a vSphere Kubernetes Service add-on (explicitly unsupported demo artifacts) the same week.
The community footprint is thin for those numbers: I read the 6-point, zero-comment Hacker News thread on the donation (2026-11-06) as the clearest signal that the 6.6k stars and the press wave have not yet produced an independent practitioner discussion, with every other submission about the project sitting at 1 to 3 points.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=agent-substrate/substrate&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=agent-substrate/substrate&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=agent-substrate/substrate&type=date&legend=top-left" />
</picture>

## Strengths

- Density and idle economics are the point: sub-500ms restore, more than 500 suspend and resume activations per second, a claimed 10x density over standard container runtimes, and roughly 250 actors multiplexed onto 8 worker pods in the project's own demo.
- The zero-trust design is architectural rather than bolted on: per-actor SPIFFE identity, credential-free sandboxes, no ingress or egress by default, and gateway-side secret injection, so a prompt-injected agent holds nothing worth stealing.
- Governance-grade institutional adoption in two quarters: CNCF Sandbox acceptance, a managed GKE surface, kagent 1.0 as the platform layer, NVIDIA upstream contributions, and a VMware integration demo.
- The isolation boundary is selectable per Actor, gVisor for container density on any Linux node or Cloud Hypervisor microVMs where hardware virtualization fits, under one lifecycle API.

## Cautions

- **The project is two quarters old with vendor-born momentum: NVIDIA's own integration post states the APIs are still changing and GPU support is being rebuilt on Dynamic Resource Allocation, so the 1.0 tag marks a beginning, not a settled surface.**
- The GKE docs rule out production needs by name: GPU device passthrough into Actor containers is unsupported, gVisor cannot snapshot live CUDA contexts, open network connections (database sessions, MCP connections) do not survive suspend, Autopilot clusters are unsupported, and nodes past roughly 800 concurrent sandboxes need manual kernel tuning.
- No external security audit exists; the trust story rests on architecture documentation and partner adoption.
- Ecosystem churn runs deep even inside the family: kagent 1.0 has no upgrade path from 0.x and requires a fresh install with a new database, and the September GKE positioning (allowlisted production) shifted to GA within two months.
- The skeptical framing is worth holding onto: The New Stack's July coverage pitched Agent Substrate as a bet that agents become Kubernetes' next default workload, and the thread's only comment dismissed it as a lock-in play, while the near-empty Hacker News threads show practitioners have not yet tested that bet in public.

## Pricing

Free, Apache-2.0, self-hosted on any Kubernetes 1.37+ cluster; the costs are the worker pods, snapshot storage, and networking of the cluster you run it on.
The managed surface's pricing is not separately documented from GKE's own: Agent Substrate on GKE deploys onto GKE Standard clusters, uses Cloud Storage buckets for snapshots, and optionally attaches Filestore agent volumes, so pricing rides GKE and Google Cloud infrastructure itself.
No per-seat, per-sandbox, or per-activation fee appears on ate.dev, in the GKE docs, or in the repository as of 2026-11-14.
Solo.io sells enterprise releases of Agent Substrate and kagent with support, tracing, evaluations, and air-gapped installs, without published prices.

## Compared to

- [Agent Sandbox](../agent-sandbox/index.md): the Kubernetes SIG Apps CRD it improves on; the GKE comparison page states Agent Substrate bypasses the standard control-plane bottlenecks that limit Agent Sandbox, running more concurrent agents per machine and starting them faster, at the cost of operating a second control and data plane alongside Kubernetes.
- [E2B](../e2b/index.md): the hosted API path with zero infrastructure and per-second billing; Agent Substrate is the self-hosted or managed-cluster answer for platform teams who need the sessions and identities inside their own governance boundary.
- [Microsandbox](../microsandbox/index.md): the local-first embeddable libkrun runtime for single developer machines; Agent Substrate targets fleet scale on Kubernetes and drops the workstation use case entirely.

## Bottom line

**Recommended for platform teams running many mostly-idle agent sessions on Kubernetes who want zero-trust identity, gateway-held credentials, and idle-compute economics under CNCF governance.**
Not for workstation or single-agent use (Microsandbox's slot), not for teams who want a hosted API instead of operating a cluster (E2B's slot), and not for GPU-dependent agent workloads that need device passthrough or CUDA snapshot restore today, since both isolation modes document that gap on GKE.

## Changes

- 2026-11-14 - Created.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [Agent Sandbox](../agent-sandbox/index.md) - the Kubernetes SIG Apps predecessor the GKE docs position Agent Substrate against
- [E2B](../e2b/index.md) - the hosted API the category's self-hosted members measure themselves against
- [Microsandbox](../microsandbox/index.md) - the workstation-scale microVM counterpart to the cluster-scale actor model
- [OpenShell](../openshell/index.md) - the NVIDIA runtime donated into the CNCF Sandbox in the same KubeCon wave

## References

- https://github.com/agent-substrate/substrate - the repository: description, topics, governance, contributing guide
- https://api.github.com/repos/agent-substrate/substrate - stars, forks, license, creation and push dates as of 2026-11-14
- https://api.github.com/repos/agent-substrate/substrate/releases/latest - the v1.0.0 release record, published 2026-11-05
- https://github.com/cncf/sandbox/issues/523 - the CNCF Sandbox application, created 2026-09-08 and closed 2026-10-20
- https://ate.dev - the project site: actor and worker model, security principles, demos, tutorials, community
- https://opensource.googleblog.com/2026/11/sandboxing-untrusted-ai-agents-at-scale.html - the Google Open Source donation post (2026-11-05): lifecycle of an agent turn, gVisor pairing, KubeCon sessions
- https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf - the Google Cloud announcement (2026-11-05): 1.0, GKE GA, contributor and adoption claims, the CNCF application links
- https://cloud.google.com/blog/products/containers-kubernetes/agent-substrate-available-on-gke - the September GKE announcement (2026-09-15): architectural principles, Nous Research and Hermes Enterprise adoption
- https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate - the GKE concepts page: architecture, Agent Sandbox comparison, limitations and requirements
- https://www.cncf.io/announcements/2026/11/10/cncf-hits-major-milestones-with-global-community-growth-record-industry-investment-and-a-new-generation-of-projects-to-build-ai-systems-in-production/ - the CNCF announcement (2026-11-10): Agent Substrate among new Sandbox projects, the zero-trust description
- https://developer.nvidia.com/blog/agent-substrate-advancing-kubernetes-for-agents-at-scale/ - the NVIDIA technical blog (2026-11-10): upstream contributions, Dynamo integration, the API-churn caution
- https://www.solo.io/blog/announcing-kagent-1-0-ga - the Solo.io kagent 1.0 GA post (2026-11-10): the no-plain-containers statement, gateway security model, production adopters
- https://blogs.vmware.com/cloud-foundation/2026/11/10/running-agent-substrate-on-vmware-vsphere-kubernetes-service/ - the VMware VCF blog (2026-11-10): the VKS add-on demo, resume figures, unsupported-artifacts caveat
- https://hn.algolia.com/api/v1/items/50390509 - the Hacker News thread on the donation (2026-11-06): 6 points, zero comments
- https://hn.algolia.com/api/v1/items/48995603 - the July Hacker News thread on The New Stack's coverage (3 points): the skeptical lock-in comment and the earliest public framing of the project
