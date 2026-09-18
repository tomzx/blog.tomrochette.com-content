---
title: "Sandboxing Feature Matrix"
created: 2026-08-30
updated: 2026-09-18
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, sandboxing, isolation, security]
readability: 3
audience_notes: >
  Engineers deciding where agent isolation should live: the workstation, the cluster, the wrapper, the framework, or the provisioning layer.
  Assumes you know what a container, seccomp, and FUSE are; each column links to a full note with sources.
---

This matrix compares the eight members of the Sandboxing category: the Kubernetes orchestrator, the kernel-enforced wrapper, the provisioning driver, the disposable-VM workstation tool, the E2B-compatible microVM service, the framework with sandbox tiers, the general-purpose sandbox platform, and the policy runtime.
The Kind row is what keeps this category legible: five columns are isolation boundaries (three workstation-scale, two platform-scale services), one is an orchestrator around boundaries, one is a framework that consumes boundaries, and one feeds repositories into all of them.
Everything below was re-verified against live sources on 2026-09-18.

**Isolation is cheap to claim and expensive to enforce, so the deciding rows are the mechanism and the maturity: a kernel boundary nobody has audited loses to a container boundary a vendor stands behind.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Agent Sandbox](../agent-sandbox/index.md) | [aigate](../aigate/index.md) | [ArtifactFS](../artifact-fs/index.md) | [Clawk](../clawk/index.md) | [CubeSandbox](../cubesandbox/index.md) | [Flue](../flue/index.md) | [OpenSandbox](../opensandbox/index.md) | [OpenShell](../openshell/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | K8s sandbox orchestrator | kernel-enforced CLI wrapper | workspace provisioning driver | disposable per-agent Linux VM | self-hosted E2B-compatible microVM sandbox service | framework with sandbox tiers | general-purpose sandbox platform | sandboxed agent runtime |
| Isolation boundary | ~ delegates to gVisor or Kata via RuntimeClass | ✓ ACLs plus namespaces plus Seatbelt | ✗ not an isolation boundary | ✓ VM boundary, host mounts only what you share | ✓ dedicated-kernel KVM MicroVM per sandbox, eBPF network isolation | ✗ adapters to external sandboxes | ~ default runc container, opt-in gVisor, Kata, or Firecracker | ✓ container or MicroVM, Landlock, seccomp, L7 proxy |
| Backing | Google Cloud via Kubernetes SIG Apps, Apache-2.0 | anonymous two-person org, MIT | Cloudflare, Apache-2.0 | small independent team, Apache-2.0 | Tencent, Apache-2.0 with listed third-party exceptions | Astro/Cloudflare team, Apache-2.0 | opensandbox-group, Alibaba-origin, Apache-2.0 | NVIDIA, Apache-2.0 |
| Platform | any Kubernetes cluster | Linux first, macOS partial | macOS (macFUSE), Linux (fuse3) | macOS, Linux experimental | x86_64 Linux with KVM, ARM64 supported, K8s deploy preview | any Node 22+ host, deploys anywhere | Docker locally, Kubernetes runtime at scale | Linux, macOS, WSL2 experimental |
| Agent integration | none specific, bring your own | tool-agnostic wrapper | any sandbox that mounts FUSE | wraps Claude Code, Codex, pi, or a shell | E2B SDK drop-in, base-URL swap | hooks, useSandbox API | 5 SDK languages, osb CLI, MCP server | 4 first-class, BYOC |
| Policy model | K8s RBAC plus RuntimeClass | per-project YAML deny rules | ✗ n/a, provisioning only | network allow-list, forge pre-allowed | eBPF inter-sandbox isolation plus L7 per-domain egress policy | tier choice plus env allowlist | ingress gateway plus per-sandbox egress controls | declarative YAML, auditable |
| Credential handling | your K8s secrets | egress allowlist, stdout masking | ✗ n/a | secrets stay on host, ssh-agent forwarded | ✓ credential vault, keys injected at egress gateway | env allowlist per tier | ✓ credential vault for outbound requests | ✓ keys stay at inference proxy |
| Maturity | v1.0.3 tag, v1beta1 API, breaking migrations | v1.0.0, 14 stars, no audit | 1.0.0-rc, no releases, beta | pre-1.0 (v0.4.0), own breaking-changes banner | pre-1.0 (v0.7.1), five months old | first stable v2.0 after rewrite | pre-1.0 (server/v0.2.3), component versioning | alpha, v0.0.x |
| Community signal | 3.9k stars, Google-backed | 14 stars, 0 issues, footprint is the signal | 1.1k stars, 217-point HN launch | 1.0k stars, 226-point HN launch, quiet since August | 12.5k stars, best HN thread 7 points | 8.2k stars, single dominant author | 15.3k stars, no real HN launch, Trendshift-driven | 8.6k stars, ~118 contributors |
| Pricing | free, cluster costs | free | free, Artifacts service metered | free | free, self-hosted fleet | free, provider costs | free, self-hosted | free |

## Reading the matrix

**The backing row is doing more work than the license row: all eight are permissively licensed, and what differs is who you sue, so to speak, when the boundary breaks.**
Google Cloud, NVIDIA, Alibaba's opensandbox-group, and Tencent stand behind four columns between them; the others belong to a Cloudflare team project, a small independent team, and an anonymous org.

**The isolation-boundary row separates real boundaries from plumbing**: OpenShell, aigate, Clawk, and CubeSandbox enforce at the kernel, container, or VM level, OpenSandbox ships a container boundary with stronger runtimes behind opt-in configuration, Agent Sandbox explicitly delegates, Flue explicitly refuses, and ArtifactFS is upstream plumbing that gets repos into any of them fast.
A matrix that pretended all eight were equivalent would be lying by layout.

**The credential row now has three architectural answers**: OpenShell, CubeSandbox, and OpenSandbox all keep keys out of the sandbox via a proxy or vault, aigate masks and allowlists at the edges, and the rest delegate to you, so the differentiator moves from whether it is done to where the proxy runs and who operates it.

**Audit status is the caution no cell can carry**: OpenShell is alpha without an announced audit, aigate has no security process at all, Clawk publishes its own limits (the allow-list trusts the forge, so anything the agent reads could be published) while quieting down since August, and the two new platforms announce no independent audit either, OpenSandbox leaning on cosign-signed images and OpenSSF badges, CubeSandbox on its own benchmarks, so the maturity row is a security row in disguise.

## Choosing from the matrix

- Need multiple agents sandboxed on workstations with egress and key policy: OpenShell, alpha risk priced in.
- Want to stop approving every command on a macOS workstation and accept pre-1.0 churn: Clawk.
- Need cluster-scale, multi-tenant sandbox fleets on Kubernetes you operate: Agent Sandbox, with gVisor or Kata actually configured.
- Want uniform cross-tool restriction for personal use on Linux and will read the source first: aigate.
- Building TypeScript agents and want sandbox semantics as framework features: Flue, with the boundary chosen deliberately.
- Agent sandboxes burning minutes cloning big repos: ArtifactFS, on hosts where FUSE is allowed.
- Need a drop-in self-hosted replacement for the E2B API with hardware isolation: CubeSandbox, on a KVM-capable Linux fleet.
- Want one self-hosted platform for coding agents, GUI agents, and evals across Docker and Kubernetes: OpenSandbox, with a secure runtime configured deliberately.

## Changes

- 2026-08-30 - Created with the Sandboxing category seed, five columns with a kind row separating boundaries from plumbing.
- 2026-08-30 - Re-sorted columns alphabetically, dropping kind-order, per the new owner rule.
- 2026-09-05 - Extended from five to six columns with Clawk, making three boundary columns.
- 2026-09-16 - Extended from six to eight columns (CubeSandbox, OpenSandbox), re-sorted alphabetically, with the boundary, backing, credential, and audit prose updated for eight members.
- 2026-09-18 - Agent Sandbox maturity cell updated to the v1.0.3 tag (released 2026-09-17); every other cell re-verified against the refreshed notes and unchanged.

## See also

- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - the agents these layers wrap, some with built-in sandboxing
- [Codex](../../harnesses/codex/index.md) - the built-in kernel sandboxing baseline
- [Executions Feature Matrix](../../executions/executions-feature-matrix/index.md) - the unattended runs isolation exists to protect
- [Control Planes Feature Matrix](../../control-planes/control-planes-feature-matrix/index.md) - governance above the sandboxes

## References

- https://github.com/NVIDIA/OpenShell - the OpenShell column: protection layers, agents, alpha status
- https://github.com/kubernetes-sigs/agent-sandbox - the Agent Sandbox column: CRDs, threat model, maturity
- https://github.com/AxeForging/aigate - the aigate column: mechanism and its own caveats
- https://github.com/withastro/flue - the Flue column: three-tier sandbox model
- https://github.com/cloudflare/artifact-fs - the ArtifactFS column: FUSE architecture, limitations
- https://github.com/clawkwork/clawk - the Clawk column: VM model, security limits, and release state
- https://github.com/TencentCloud/CubeSandbox - the CubeSandbox column: microVM architecture, E2B compatibility, self-reported benchmarks
- https://github.com/opensandbox-group/OpenSandbox - the OpenSandbox column: platform scope, SDKs, cosign signing, opt-in secure runtimes
- https://code.claude.com/docs/en/sandboxing - the built-in sandboxing baseline the category is measured against
