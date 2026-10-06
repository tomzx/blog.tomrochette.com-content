---
title: "Sandboxing Feature Matrix"
created: 2026-08-30
updated: 2026-10-06
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, sandboxing, isolation, security]
readability: 3
audience_notes: >
  Engineers deciding where agent isolation should live: the workstation, the cluster, the wrapper, the framework, the hosted API, or the provisioning layer.
  Assumes you know what a container, seccomp, and FUSE are; each column links to a full note with sources.
---

This matrix compares the eleven members of the Sandboxing category: the Kubernetes orchestrator, the kernel-enforced wrapper, the provisioning driver, the microVM workstation sandbox, the disposable-VM workstation tool, the rootless namespace wrapper, the self-hosted E2B-compatible microVM service, the hosted sandbox API that defines the category's compatibility baseline, the framework with sandbox tiers, the general-purpose sandbox platform, and the policy runtime.
The Kind row is what keeps this category legible: eight columns are isolation boundaries (five workstation-scale, three platform-scale services), one is an orchestrator around boundaries, one is a framework that consumes boundaries, and one feeds repositories into all of them.

**Isolation is cheap to claim and expensive to enforce, so the deciding rows are the mechanism and the maturity: a kernel boundary nobody has audited loses to a container boundary a vendor stands behind.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Agent Sandbox](../agent-sandbox/index.md) | [aigate](../aigate/index.md) | [ArtifactFS](../artifact-fs/index.md) | [Brig](../brig/index.md) | [Clawk](../clawk/index.md) | [CubeSandbox](../cubesandbox/index.md) | [Drop](../drop/index.md) | [E2B](../e2b/index.md) | [Flue](../flue/index.md) | [OpenSandbox](../opensandbox/index.md) | [OpenShell](../openshell/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | K8s sandbox orchestrator | kernel-enforced CLI wrapper | workspace provisioning driver | microVM workstation sandbox | disposable per-agent Linux VM | self-hosted E2B-compatible microVM sandbox service | rootless namespace sandbox wrapper | hosted Firecracker-microVM sandbox API | framework with sandbox tiers | general-purpose sandbox platform | sandboxed agent runtime |
| Isolation boundary | ~ delegates to gVisor or Kata via RuntimeClass | ✓ ACLs plus namespaces plus Seatbelt | ✗ not an isolation boundary | ✓ microVM per agent (hull hvi, vz, or Linux urunc), runc optional and flagged weaker | ✓ VM boundary, host mounts only what you share | ✓ dedicated-kernel KVM MicroVM per sandbox, eBPF network isolation | ✓ six namespace types, capabilities dropped, optional gVisor | ✓ Firecracker microVM per session, nftables egress firewall | ✗ adapters to external sandboxes | ~ default runc container, opt-in gVisor, Kata, or Firecracker | ✓ container or MicroVM, Landlock, seccomp, L7 proxy |
| Backing | Google Cloud via Kubernetes SIG Apps, Apache-2.0 | anonymous two-person org, MIT | Cloudflare, Apache-2.0 | NOFire AI (team behind CNCF's urunc), Apache-2.0 | small independent team, Apache-2.0 | Tencent, Apache-2.0 with listed third-party exceptions | solo author (Jan Wrobel), Apache-2.0 | E2B (Insight Partners-backed, $32M raised), Apache-2.0 SDKs and runtime | Astro/Cloudflare team, Apache-2.0 | opensandbox-group, Alibaba-origin, Apache-2.0 | NVIDIA, Apache-2.0 |
| Platform | any Kubernetes cluster | Linux first, macOS partial | macOS (macFUSE), Linux (fuse3) | Apple Silicon macOS 15+ (14 with fallbacks), Linux x86-64/arm64 | macOS, Linux experimental | x86_64 Linux with KVM, ARM64 supported, K8s deploy preview | Linux only (amd64, arm64), host distro reused | hosted cloud (US, EU, APAC), BYOC; Embed self-hosts on one x86-64 KVM Linux node | any Node 22+ host, deploys anywhere | Docker locally, Kubernetes runtime at scale | Linux, macOS, WSL2 experimental |
| Agent integration | none specific, bring your own | tool-agnostic wrapper | any sandbox that mounts FUSE | 8 built-in profiles (Claude Code, Codex, Gemini, Grok, OpenCode, Cursor, Claude Desktop, shell) | wraps Claude Code, Codex, pi, or a shell | E2B SDK drop-in, base-URL swap | tool-agnostic wrapper, docs tour uses Claude Code | SDK-first (Python, JavaScript), framework adapters target it | hooks, useSandbox API | 5 SDK languages, osb CLI, MCP server | 4 first-class, BYOC |
| Policy model | K8s RBAC plus RuntimeClass | per-project YAML deny rules | ✗ n/a, provisioning only | isolated or shared networks, egress policies enforced on hvi only | network allow-list, forge pre-allowed | eBPF inter-sandbox isolation plus L7 per-domain egress policy | TOML config, shared base plus per-environment overrides | per-sandbox nftables egress, SNI/Host-inspecting domain allow and deny lists | tier choice plus env allowlist | ingress gateway plus per-sandbox egress controls | declarative YAML, auditable |
| Credential handling | your K8s secrets | egress allowlist, stdout masking | ✗ n/a | ✓ host credential sources unread on the run path, keychain-backed store, profile-named forwarding | secrets stay on host, ssh-agent forwarded | ✓ credential vault, keys injected at egress gateway | original home hidden, selected host files read-only | ✓ secrets vault injected at egress proxy | env allowlist per tier | ✓ credential vault for outbound requests | ✓ keys stay at inference proxy |
| Maturity | v1.0.5 tag, v1beta1 API, breaking migrations | v1.0.0, 14 stars, no audit | 1.0.0-rc, no releases, beta | pre-1.0 (v0.3.0), daily channel prereleases, no audit | pre-1.0 (v0.4.0), own breaking-changes banner | pre-1.0 (v0.7.2), five months old | pre-1.0 (v0.3.0), solo maintainer | SOC 2 Type II cloud, 2.52.x SDK train, runtime newly open source | first stable v2.0 after rewrite | first stable 1.1.0 umbrella release | stable 0.1.x line at v0.1.2, self-declared alpha dropped |
| Community signal | 4.2k stars, Google-backed | 14 stars, 0 issues, footprint is the signal | 1.2k stars, 217-point HN launch | 207 stars, 9-point launch, eight weeks old | 1.0k stars, 226-point HN launch, quiet since August | 12.8k stars, best HN thread 7 points | 375 stars, 193-point HN launch | 14.2k stars (SDK repo), 2-point launch, enterprise claims | 8.4k stars, single dominant author | 15.7k stars, no HN launch of its own, Trendshift-driven | 15.0k stars, ~128 contributors |
| Pricing | free, cluster costs | free | free, Artifacts service metered | free | free | free, self-hosted fleet | free | usage-based, Hobby free, Pro $150/mo | free, provider costs | free, self-hosted | free |

## Reading the matrix

**The backing row is doing more work than the license row: all eleven are permissively licensed, and what differs is who you sue, so to speak, when the boundary breaks.**
Google Cloud, NVIDIA, Alibaba's opensandbox-group, Tencent, NOFire AI (the team behind CNCF's urunc), and the venture-backed E2B company stand behind six columns between them; the rest belong to a Cloudflare team project, a small independent team, a solo author, and an anonymous org.

**The isolation-boundary row separates boundaries from plumbing**: OpenShell, aigate, Brig, Clawk, Drop, CubeSandbox, and E2B enforce at the kernel, container, or VM level, OpenSandbox ships a container boundary with stronger runtimes behind opt-in configuration, Agent Sandbox explicitly delegates, Flue explicitly refuses, and ArtifactFS is upstream plumbing that gets repos into any of them fast.
A matrix that pretended all eleven were equivalent would be lying by layout.

**The credential row now has four architectural answers**: OpenShell, CubeSandbox, OpenSandbox, and E2B all keep keys out of the sandbox via a proxy or vault, Drop's answer is the filesystem itself, an empty home with selected paths mounted read-only, aigate masks and allowlists at the edges, Brig reads no host credential source and forwards only what its profiles name, and the rest delegate to you, so the differentiator moves from whether it is done to where the proxy runs and who operates it.

**Audit status is the caution no cell can carry**: OpenShell reached its stable 0.1.x line (now at v0.1.2) without an announced audit, aigate has no security process at all, Clawk publishes its own limits (the allow-list trusts the forge, so anything the agent reads could be published) while quieting down since August, and the newer platforms announce no independent audit either, OpenSandbox leaning on cosign-signed images and OpenSSF badges, CubeSandbox on its own benchmarks, Drop on a candid docs overview, Brig publishing measured reachability results and trust assumptions while awaiting an external audit, and E2B answering with SOC 2 Type II on process while the boundary itself stays un-audited in public, so the maturity row is a security row in disguise.

## Choosing from the matrix

- Need multiple agents sandboxed on workstations with egress and key policy: OpenShell, pre-1.0 risk priced in.
- Want to stop approving every command on a macOS workstation and accept pre-1.0 churn: Clawk.
- Need cluster-scale, multi-tenant sandbox fleets on Kubernetes you operate: Agent Sandbox, with gVisor or Kata actually configured.
- Want uniform cross-tool restriction for personal use on Linux and will read the source first: aigate.
- Want a coding agent fenced in on Linux without leaving your installed environment: Drop, with gVisor enabled for untrusted work.
- Want a maintained microVM around an agent on your own Apple Silicon or Linux box, and will read its security docs first: Brig, pre-1.0.
- Building TypeScript agents and want sandbox semantics as framework features: Flue, with the boundary chosen deliberately.
- Agent sandboxes burning minutes cloning big repos: ArtifactFS, on hosts where FUSE is allowed.
- Need a drop-in self-hosted replacement for the E2B API with hardware isolation: CubeSandbox, on a KVM-capable Linux fleet.
- Want zero-ops hardware-isolated execution behind an API and can pay per second: E2B, the hosted path.
- Want one self-hosted platform for coding agents, GUI agents, and evals across Docker and Kubernetes: OpenSandbox, with a secure runtime configured deliberately.

## Changes

- 2026-08-30 - Created with the Sandboxing category seed, five columns with a kind row separating boundaries from plumbing.
- 2026-08-30 - Re-sorted columns alphabetically, dropping kind-order, per the new owner rule.
- 2026-09-05 - Extended from five to six columns with Clawk, making three boundary columns.
- 2026-09-16 - Extended from six to eight columns (CubeSandbox, OpenSandbox), re-sorted alphabetically, with the boundary, backing, credential, and audit prose updated for eight members.
- 2026-09-18 - Agent Sandbox maturity cell updated to the v1.0.3 tag (released 2026-09-17); every other cell re-verified against the refreshed notes and unchanged.
- 2026-09-21 - Refreshed the community-signal cells for CubeSandbox (12.6k), Flue (8.3k), OpenSandbox (15.4k), and OpenShell (8.7k stars, ~120 contributors); all other cells re-verified unchanged.
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-25 - Maturity cells refreshed: Agent Sandbox v1.0.4, CubeSandbox v0.7.2, OpenSandbox at its first stable 1.1.0 umbrella release; community-signal cells refreshed (Agent Sandbox 4.0k, CubeSandbox 12.7k, Flue 8.4k, OpenSandbox 15.5k, OpenShell 8.8k stars and about 123 contributors).
- 2026-09-27 - OpenShell maturity cell moved to its first stable v0.1.1 release (v0.1.0 on 2026-09-25, alpha badge dropped), and the audit prose updated to match.
- 2026-09-29 - Extended to nine columns with Drop (rootless namespace wrapper), inserted alphabetically, with the backing, boundary, credential, and audit prose updated for nine members.
- 2026-09-29 - Cell refreshes: OpenShell maturity to the stable 0.1.x line at v0.1.2 and community to 9.7k stars with about 124 contributors, OpenSandbox community to 15.6k stars, and the OpenShell choosing bullet reworded from alpha to pre-1.0 risk after the stable graduation.
- 2026-10-02 - Cell refreshes: Agent Sandbox maturity to v1.0.5 and community to 4.1k stars, Drop maturity to v0.3.0 and community to 350 stars, ArtifactFS community to 1.2k stars, CubeSandbox community to 12.8k stars, and OpenShell community to 14.0k stars with about 126 contributors after the Open Agent Safety Platform push.
- 2026-10-06 - Extended to eleven columns with Brig (the actively maintained microVM workstation sandbox) and E2B (the hosted sandbox API the category cites as its compatibility baseline), inserted alphabetically, with the boundary, backing, credential, and audit prose updated for eleven members.
- 2026-10-06 - Cell refreshes: Agent Sandbox community to 4.2k stars, Drop to 375, OpenSandbox to 15.7k, and OpenShell to 15.0k stars with about 128 contributors.

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
- https://github.com/wrr/drop - the Drop column: rootless namespaces, gVisor option, TOML config
- https://github.com/brig-sh/brig - the Brig column: microVM boundary, cosign verification, security-model candor
- https://github.com/e2b-dev/E2B - the E2B column: the SDK repo behind the community cell
- https://e2b.dev - the E2B column: hosted Firecracker sandboxes, deployment options, pricing
- https://github.com/opensandbox-group/OpenSandbox - the OpenSandbox column: platform scope, SDKs, cosign signing, opt-in secure runtimes
- https://code.claude.com/docs/en/sandboxing - the built-in sandboxing baseline the category is measured against
