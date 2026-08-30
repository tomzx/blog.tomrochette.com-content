---
title: "Sandboxing Feature Matrix"
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, sandboxing, isolation, security]
readability: 3
audience_notes: >
  Engineers deciding where agent isolation should live: the workstation, the cluster, the wrapper, the framework, or the provisioning layer.
  Assumes you know what a container, seccomp, and FUSE are; each column links to a full note with sources.
---

This matrix compares the five members of the Sandboxing category: the vendor-backed runtime, the Kubernetes orchestrator, the kernel-enforced wrapper, the framework with sandbox tiers, and the provisioning driver.
The Kind row is what keeps this category legible: only two columns are isolation boundaries, one is an orchestrator around boundaries, one is a framework that consumes boundaries, and one feeds repositories into all of them.
Everything below was verified against live sources on 2026-08-30.

**Isolation is cheap to claim and expensive to enforce, so the deciding rows are the mechanism and the maturity: a kernel boundary nobody has audited loses to a container boundary a vendor stands behind.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [OpenShell](../openshell/index.md) | [Agent Sandbox](../agent-sandbox/index.md) | [aigate](../aigate/index.md) | [Flue](../flue/index.md) | [ArtifactFS](../artifact-fs/index.md) |
| --- | --- | --- | --- | --- | --- |
| Kind | sandboxed agent runtime | K8s sandbox orchestrator | kernel-enforced CLI wrapper | framework with sandbox tiers | workspace provisioning driver |
| Isolation boundary | ✓ container or MicroVM, Landlock, seccomp, L7 proxy | ~ delegates to gVisor or Kata via RuntimeClass | ✓ ACLs plus namespaces plus Seatbelt | ✗ adapters to external sandboxes | ✗ not an isolation boundary |
| Backing | NVIDIA, Apache-2.0 | Google Cloud via Kubernetes SIG Apps, Apache-2.0 | anonymous two-person org, MIT | Astro/Cloudflare team, Apache-2.0 | Cloudflare, Apache-2.0 |
| Platform | Linux, macOS, WSL2 experimental | any Kubernetes cluster | Linux first, macOS partial | any Node 22+ host, deploys anywhere | macOS (macFUSE), Linux (fuse3) |
| Agent integration | 4 first-class, BYOC | none specific, bring your own | tool-agnostic wrapper | hooks, useSandbox API | any sandbox that mounts FUSE |
| Policy model | declarative YAML, auditable | K8s RBAC plus RuntimeClass | per-project YAML deny rules | tier choice plus env allowlist | ✗ n/a, provisioning only |
| Credential handling | ✓ keys stay at inference proxy | your K8s secrets | egress allowlist, stdout masking | env allowlist per tier | ✗ n/a |
| Maturity | alpha, v0.0.x | v1.0.0 tag, v1beta1 API, breaking migrations | v1.0.0, 14 stars, no audit | first stable v2.0 after rewrite | 1.0.0-rc, no releases, beta |
| Community signal | 8.4k stars, ~110 contributors | 3.7k stars, Google-backed | 14 stars, 0 issues, footprint is the signal | 8.1k stars, single dominant author | 1.1k stars, 217-point HN launch |
| Pricing | free | free, cluster costs | free | free, provider costs | free, Artifacts service metered |

## Reading the matrix

**The backing row is doing more work than the license row: all five are permissively licensed, and what differs is who you sue, so to speak, when the boundary breaks.**
NVIDIA and Google Cloud stand behind two columns; an anonymous org and two single-dominant-author projects stand behind the others.

**The isolation-boundary row separates real boundaries from plumbing**: OpenShell and aigate enforce at the kernel or container level, Agent Sandbox explicitly delegates, Flue explicitly refuses, and ArtifactFS is upstream plumbing that gets repos into any of them fast.
A matrix that pretended all five were equivalent would be lying by layout.

**The credential row is OpenShell's lead**: keys that never enter the sandbox is the only architectural answer to exfiltration here; aigate masks and allowlists at the edges, and the rest delegate to you.

**Audit status is the caution no cell can carry**: OpenShell is alpha without an announced audit, aigate has no security process at all, and both sell the same promise, so the maturity row is a security row in disguise.

## Choosing from the matrix

- Need multiple agents sandboxed on workstations with egress and key policy: OpenShell, alpha risk priced in.
- Need cluster-scale, multi-tenant sandbox fleets on Kubernetes you operate: Agent Sandbox, with gVisor or Kata actually configured.
- Want uniform cross-tool restriction for personal use on Linux and will read the source first: aigate.
- Building TypeScript agents and want sandbox semantics as framework features: Flue, with the boundary chosen deliberately.
- Agent sandboxes burning minutes cloning big repos: ArtifactFS, on hosts where FUSE is allowed.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the agents these layers wrap, some with built-in sandboxing
- [Codex](../codex/index.md) - the built-in kernel sandboxing baseline
- [Executions Feature Matrix](../executions-feature-matrix/index.md) - the unattended runs isolation exists to protect
- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - governance above the sandboxes

## References

- https://github.com/NVIDIA/OpenShell - the OpenShell column: protection layers, agents, alpha status
- https://github.com/kubernetes-sigs/agent-sandbox - the Agent Sandbox column: CRDs, threat model, maturity
- https://github.com/AxeForging/aigate - the aigate column: mechanism and its own caveats
- https://github.com/withastro/flue - the Flue column: three-tier sandbox model
- https://github.com/cloudflare/artifact-fs - the ArtifactFS column: FUSE architecture, limitations
- https://docs.claude.com/en/docs/claude-code/sandboxing - the built-in sandboxing baseline the category is measured against
