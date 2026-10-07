---
title: "Sandboxing Feature Matrix"
created: 2026-08-30
updated: 2026-10-07
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, sandboxing, isolation, security]
readability: 3
audience_notes: >
  Engineers deciding where agent isolation should live: the workstation, the cluster, the wrapper, the framework, the hosted API, or the provisioning layer.
  Assumes you know what a container, seccomp, and FUSE are; each column links to a full note with sources.
---

This matrix compares the sixteen members of the Sandboxing category: two orchestrators (the Kubernetes fleet orchestrator and NVIDIA's OpenShell reference stack), the provisioning driver, the framework with sandbox tiers, the general-purpose sandbox platform, the hosted sandbox API that defines the category's compatibility baseline, and ten further isolation boundaries spanning kernel wrappers, namespace sandboxes, and microVMs from workstation to fleet scale.
The Kind row is what keeps this category legible: twelve columns are isolation boundaries (nine workstation-scale, three platform-scale services), two orchestrate boundaries (Agent Sandbox for fleets, NemoClaw for NVIDIA's reference assistants), one is a framework that consumes boundaries, and one feeds repositories into all of them.

**Isolation is cheap to claim and expensive to enforce, so the deciding rows are the mechanism and the maturity: a kernel boundary nobody has audited loses to a container boundary a vendor stands behind.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Agent Sandbox](../agent-sandbox/index.md) | [aigate](../aigate/index.md) | [ArtifactFS](../artifact-fs/index.md) | [Brig](../brig/index.md) | [Clawk](../clawk/index.md) | [CubeSandbox](../cubesandbox/index.md) | [Drop](../drop/index.md) | [E2B](../e2b/index.md) | [Fence](../fence/index.md) | [Flue](../flue/index.md) | [Microsandbox](../microsandbox/index.md) | [NemoClaw](../nemoclaw/index.md) | [nono](../nono/index.md) | [NVX](../nvx/index.md) | [OpenSandbox](../opensandbox/index.md) | [OpenShell](../openshell/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | K8s sandbox orchestrator | kernel-enforced CLI wrapper | workspace provisioning driver | microVM workstation sandbox | disposable per-agent Linux VM | self-hosted E2B-compatible microVM sandbox service | rootless namespace sandbox wrapper | hosted Firecracker-microVM sandbox API | OS-native command sandbox CLI | framework with sandbox tiers | local-first embeddable microVM runtime | OpenShell reference stack: guided onboarding, managed inference, network policy, and lifecycle ops | kernel capability sandbox with per-tool broker | research-grade microVM sandbox | general-purpose sandbox platform | sandboxed agent runtime |
| Isolation boundary | ~ delegates to gVisor or Kata via RuntimeClass | ✓ ACLs plus namespaces plus Seatbelt | ✗ not an isolation boundary | ✓ microVM per agent (hull hvi, vz, or Linux urunc), runc optional and flagged weaker | ✓ VM boundary, host mounts only what you share | ✓ dedicated-kernel KVM MicroVM per sandbox, eBPF network isolation | ✓ six namespace types, capabilities dropped, optional gVisor | ✓ Firecracker microVM per session, nftables egress firewall | ✓ sandbox-exec on macOS, bubblewrap plus Landlock and seccomp on Linux, host kernel shared | ✗ adapters to external sandboxes | ✓ microVM per sandbox via libkrun, own kernel | ~ none of its own; applies OpenShell's boundary (seccomp, Landlock, privilege drop, namespaces) plus a stricter blueprint policy | ✓ kernel primitives, session sandbox plus per-command sandboxes | ✓ OpenVMM microVM, own kernel, Linux guests | ~ default runc container, opt-in gVisor, Kata, or Firecracker | ✓ container or MicroVM, Landlock, seccomp, L7 proxy |
| Backing | Google Cloud via Kubernetes SIG Apps, Apache-2.0 | anonymous two-person org, MIT | Cloudflare, Apache-2.0 | NOFire AI (team behind CNCF's urunc), Apache-2.0 | small independent team, Apache-2.0 | Tencent, Apache-2.0 with listed third-party exceptions | solo author (Jan Wrobel), Apache-2.0 | E2B (Insight Partners-backed, $32M raised), Apache-2.0 SDKs and runtime | Tusk (AI testing-agents company), Apache-2.0 | Astro/Cloudflare team, Apache-2.0 | superradcompany (YC-backed badge), Apache-2.0 | NVIDIA, Apache-2.0 | nolabs-ai (the Sigstore team), Apache-2.0 | Microsoft (MSR and Azure Research), MIT | opensandbox-group, Alibaba-origin, Apache-2.0 | NVIDIA, Apache-2.0 |
| Platform | any Kubernetes cluster | Linux first, macOS partial | macOS (macFUSE), Linux (fuse3) | Apple Silicon macOS 15+ (14 with fallbacks), Linux x86-64/arm64 | macOS, Linux experimental | x86_64 Linux with KVM, ARM64 supported, K8s deploy preview | Linux only (amd64, arm64), host distro reused | hosted cloud (US, EU, APAC), BYOC; Embed self-hosts on one x86-64 KVM Linux node | macOS and Linux, container-free | any Node 22+ host, deploys anywhere | Linux, macOS, and Windows hosts | Linux, macOS, and WSL hosts with Docker; DGX Spark and DGX Station express profiles | Linux and macOS, brew/Nix/curl install | Linux/KVM, Linux/MSHV, Windows/WHP | Docker locally, Kubernetes runtime at scale | Linux, macOS, WSL2 experimental |
| Agent integration | none specific, bring your own | tool-agnostic wrapper | any sandbox that mounts FUSE | 8 built-in profiles (Claude Code, Codex, Gemini, Grok, OpenCode, Cursor, Claude Desktop, shell) | wraps Claude Code, Codex, pi, or a shell | E2B SDK drop-in, base-URL swap | tool-agnostic wrapper, docs tour uses Claude Code | SDK-first (Python, JavaScript), framework adapters target it | tool-agnostic wrapper, wiring docs for Claude Code, Codex, Amp, Gemini CLI, Copilot, OpenCode, Droid | hooks, useSandbox API | agent-created sandboxes via shipped skills and an MCP server, embeddable library | OpenClaw default, Hermes, LangChain Deep Agents Code, Pi release candidate; onboarding wizard and per-agent aliases | tool-agnostic CLI plus Go/TypeScript/Python SDKs | none shipped, agent architecture in design docs | 5 SDK languages, osb CLI, MCP server | 4 first-class, BYOC |
| Policy model | K8s RBAC plus RuntimeClass | per-project YAML deny rules | ✗ n/a, provisioning only | network posture isolated by default on hvi and Linux, egress policies enforced on hvi and Linux | network allow-list, forge pre-allowed | eBPF inter-sandbox isolation plus L7 per-domain egress policy | TOML config, shared base plus per-environment overrides | per-sandbox nftables egress, SNI/Host-inspecting domain allow and deny lists | one fence.json, network deny-by-default with allow templates, command deny rules, write restrictions | tier choice plus env allowlist | ~ container-style flags, no declarative policy layer | Balanced, Restricted, or Open presets over OpenShell YAML, managed network policies, hardened blueprint image | per-tool profiles with chained policies, L7 credential proxy scoping API methods and paths | ~ snapshot and lifecycle ABI, no policy engine yet | ingress gateway plus per-sandbox egress controls | declarative YAML, auditable |
| Credential handling | your K8s secrets | egress allowlist, stdout masking | ✗ n/a | ✓ host credential sources unread on the run path, keychain-backed store, profile-named forwarding | secrets stay on host, ssh-agent forwarded | ✓ credential vault, keys injected at egress gateway | original home hidden, selected host files read-only | ✓ secrets vault injected at egress proxy | ✗ not a credential broker, policy files only | env allowlist per tier | ~ project states secret keys never enter the VM (self-reported) | ✓ keys stay at OpenShell's inference proxy, host env vars filtered from the build, digest-pinned credential helper | ✓ per-tool credentials via proxy, tokens scoped to selected methods and paths | ✗ not yet addressed | ✓ credential vault for outbound requests | ✓ keys stay at inference proxy |
| Maturity | v1.0.5 tag, v1beta1 API, breaking migrations | v1.0.0, 14 stars, no audit | 1.0.0-rc, no releases, beta | pre-1.0 (v0.4.0), new sandboxes isolated by default on hvi and Linux, no audit | pre-1.0 (v0.4.0), own breaking-changes banner | pre-1.0 (v0.7.2), five months old | pre-1.0 (v0.3.0), solo maintainer | SOC 2 Type II cloud, 2.53.x SDK train, runtime newly open source | pre-1.0 (v0.1.67), org renamed to fencesandbox, no audit | first stable v2.0 after rewrite | pre-1.0 (v0.7.7), weekly releases, no audit | prerelease only (one ci-native-podman-e2e tag, 2026-10-01), self-declared alpha | pre-1.0 (v0.79.0), 1.0 approaching, no audit | research preview, daily v0.1.0-dev prereleases, no stable release | first stable 1.1.0 umbrella release | stable 0.1.x line at v0.1.2, self-declared alpha dropped |
| Community signal | 4.2k stars, Google-backed | 14 stars, 0 issues, footprint is the signal | 1.2k stars, 217-point HN launch | 211 stars, 9-point launch, eight weeks old | 1.0k stars, 226-point HN launch, quiet since August | 12.8k stars, best HN thread 7 points | 377 stars, 193-point HN launch | 14.2k stars (SDK repo), 2-point launch, enterprise claims | 986 stars, 78-point HN launch | 8.4k stars, single dominant author | 8.6k stars, 402-point HN launch (2025) | 22.7k stars, 385-point HN launch | 4.4k stars, best HN thread 4 points | 338 stars, 3-point HN thread | 15.7k stars, no HN launch of its own, Trendshift-driven | 15.2k stars, ~128 contributors |
| Pricing | free, cluster costs | free | free, Artifacts service metered | free | free | free, self-hosted fleet | free | usage-based, Hobby free, Pro $150/mo | free | free, provider costs | free, self-hosted | free, host and token costs | free | free | free, self-hosted | free |

## Reading the matrix

**The backing row is doing more work than the license row: all sixteen are permissively licensed, and what differs is who you sue, so to speak, when the boundary breaks.**
Google Cloud, NVIDIA (which now stands behind two columns, OpenShell and NemoClaw), Alibaba's opensandbox-group, Tencent, NOFire AI (the team behind CNCF's urunc), the venture-backed E2B company, Microsoft, nolabs-ai (the Sigstore team), Tusk, and YC-backed superradcompany stand behind eleven columns between them; the rest belong to two Cloudflare team projects, a small independent team, a solo author, and an anonymous org.

**The isolation-boundary row separates boundaries from plumbing**: OpenShell, aigate, Brig, Clawk, Drop, CubeSandbox, E2B, Fence, Microsandbox, nono, and NVX enforce at the kernel, container, or VM level, OpenSandbox ships a container boundary with stronger runtimes behind opt-in configuration, Agent Sandbox explicitly delegates, NemoClaw inherits OpenShell's enforcement and layers a stricter blueprint on top, Flue explicitly refuses, and ArtifactFS is upstream plumbing that gets repos into any of them fast.
A matrix that pretended all sixteen were equivalent would be lying by layout.

**The credential row now has five architectural answers**: OpenShell, CubeSandbox, OpenSandbox, E2B, and NemoClaw (which creates the providers at onboarding, filters key-bearing host env vars out of the build, and rides OpenShell's inference proxy) keep keys out of the sandbox via a proxy or vault, nono goes finer and scopes each tool's token to selected API methods and paths through its own broker, Drop's answer is the filesystem itself, an empty home with selected paths mounted read-only, aigate masks and allowlists at the edges, Brig reads no host credential source and forwards only what its profiles name, Microsandbox states keys never enter the VM without publishing an external review of the mechanism, and the rest delegate to you, so the differentiator moves from whether it is done to where the proxy runs and who operates it.

**Audit status is the caution no cell can carry**: OpenShell reached its stable 0.1.x line (now at v0.1.2) without an announced audit, aigate has no security process at all, Clawk publishes its own limits (the allow-list trusts the forge, so anything the agent reads could be published) while quieting down since August, Fence's maintainer stated reads are allow-by-default on launch day, nono advertises an immutable audit chain and an OpenSSF badge while awaiting an external audit, Microsandbox's boot and secret claims are self-reported, NVX answers with a limits page that rules out production needs by name, NemoClaw pins its credential helper and form by SHA-256 digest and publishes hardening docs while declaring itself alpha with no external audit, the newer platforms announce no independent audit either, OpenSandbox leaning on cosign-signed images and OpenSSF badges, CubeSandbox on its own benchmarks, Drop on a candid docs overview, Brig publishing measured reachability results and trust assumptions while awaiting an external audit, and E2B answering with SOC 2 Type II on process while the boundary itself stays un-audited in public, so the maturity row is a security row in disguise.

## Choosing from the matrix

- Need multiple agents sandboxed on workstations with egress and key policy: OpenShell, pre-1.0 risk priced in.
- Want OpenClaw, Hermes, or Deep Agents operated for you inside OpenShell with NVIDIA's defaults: NemoClaw, alpha attached.
- Want to stop approving every command on a macOS workstation and accept pre-1.0 churn: Clawk.
- Need cluster-scale, multi-tenant sandbox fleets on Kubernetes you operate: Agent Sandbox, with gVisor or Kata actually configured.
- Want uniform cross-tool restriction for personal use on Linux and will read the source first: aigate.
- Want a coding agent fenced in on Linux without leaving your installed environment: Drop, with gVisor enabled for untrusted work.
- Want a maintained microVM around an agent on your own Apple Silicon or Linux box, and will read its security docs first: Brig, pre-1.0.
- Want one policy file around semi-trusted commands and agents on macOS or Linux, accepting allow-by-default reads: Fence, 0.x.
- Want each delegated tool fenced separately with per-endpoint credential scoping: nono, pre-1.0.
- Want VMs with container workflows on your own machine, including agents that spawn their own sandboxes: Microsandbox, self-reported claims attached.
- Need Windows-hypervisor isolation research, or want to watch where Microsoft is taking microVMs: NVX, a research preview.
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
- 2026-10-07 - Extended to fifteen columns with Fence (the OS-native command sandbox CLI), Microsandbox (the libkrun local-first microVM runtime), nono (the per-command capability broker), and NVX (Microsoft's research-grade microVM sandbox), inserted alphabetically, with the boundary, backing, credential, and audit prose updated for fifteen members.
- 2026-10-07 - Cell refreshes: Brig maturity to v0.4.0 with the new default-isolated network posture and Linux egress enforcement, Brig community to 211 stars, Drop to 377, and OpenShell to 15.2k stars as the platform push continued.
- 2026-10-07 - Extended to sixteen columns with NemoClaw (NVIDIA's OpenShell reference stack for OpenClaw, Hermes, and Deep Agents), inserted alphabetically between Microsandbox and nono, with the intro, orchestrator count, backing, boundary, credential, and audit prose updated.

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
- https://github.com/fencesandbox/fence - the Fence column: OS-native primitives, tool-agnostic policy, docs security model
- https://github.com/superradcompany/microsandbox - the Microsandbox column: libkrun runtime, agent skills, self-reported claims
- https://github.com/nolabs-ai/nono - the nono column: per-tool broker, credential proxy, audit chain
- https://github.com/microsoft/nvx - the NVX column: OpenVMM research sandbox, limits page, benchmark discipline
- https://github.com/opensandbox-group/OpenSandbox - the OpenSandbox column: platform scope, SDKs, cosign signing, opt-in secure runtimes
- https://code.claude.com/docs/en/sandboxing - the built-in sandboxing baseline the category is measured against
