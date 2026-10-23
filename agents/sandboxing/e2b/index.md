---
title: E2B
created: 2026-10-06
updated: 2026-10-23
readability: 3
audience_notes: >
  Engineers choosing where agent code execution runs, comparing the hosted sandbox API against the self-hosted platforms.
  Assumes you know what Firecracker, per-second billing, and a base-URL-compatible SDK are.
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, microvm, firecracker, hosted-api, isolation, security]
---

E2B is the hosted sandbox API that gives each agent session an isolated Firecracker microVM with its own kernel, created through Python or JavaScript SDK calls and billed per second, and it is the interface the self-hosted members of this category advertise compatibility with.

**E2B is this category's compatibility baseline rather than a competitor on mechanism, and its 2026 move, open-sourcing the runtime behind its cloud, turns the hosted-versus-self-hosted comparison into a choice of whose operator you run.**

## What it is

A cloud service plus SDKs where `Sandbox.create()` returns a full Linux machine: shell, filesystem, network, ports exposed as HTTPS sandbox URLs, and an optional desktop, usable from any model provider or agent framework.
Every sandbox is a hardware-isolated Firecracker microVM booted by resuming a pre-booted snapshot, with memory pages served lazily through userfaultfd, so fresh creates, resumes, and forks of up to 100 copies take the same fast path.
Egress is governed per sandbox through nftables with SNI/Host-inspecting domain allow and deny lists, and secrets stay in a vault that injects them at the egress proxy, so values never enter the sandbox filesystem.
The cloud is SOC 2 Type II compliant with US, EU, and APAC regions; enterprise teams get BYOC on AWS, GCP, or Azure, a private-cloud control plane is in development, and E2B Embed is an Apache-2.0 single-node package (Docker Compose, Terraform, Kubernetes) that runs the whole stack on one x86-64 KVM Linux machine.

## Status

Active and well funded: the SDK repo stands at 14,378 stars and the runtime repo at 1,725 stars as of 2026-10-16, the SDK repo created 2023-03-04 and pushed 2026-10-19 (the runtime repo pushed 2026-10-18), with the e2b package on PyPI at 2.59.0 (as of 2026-10-23) after the 2.56.0 release of 2026-10-13 opened the next train.
The 2.56.0 cut is a breaking one for JavaScript users: Node.js 22 is now the minimum, the SDK depends on undici 8 only, and the SDK-level in-flight request caps and their environment variables are removed in favor of undici's connection pools.
2.57.0 and 2.58.0 followed on 2026-10-20 (a tls option for the egress proxy connection, and streaming stdin and PTY input handles), and 2.59.0 on 2026-10-22 added per-sandbox DNS server allowlists inside the egress firewall while deprecating the apiUrl and sandboxUrl connection options and their environment variables ahead of removal in the next major.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=e2b-dev/E2B&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=e2b-dev/E2B&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=e2b-dev/E2B&type=date&legend=top-left" />
</picture>

A $21M Series A led by Insight Partners was announced 2025-07-28, $32M total, with company claims of 88 percent of the Fortune 100 signed up, hundreds of millions of sandbox sessions since October 2024, and named users including Hugging Face, LMArena, Perplexity, Groq, and Manus.
**Hacker News never embraced it: the 2024 launch thread drew 2 points, the category's HN energy went to self-hosted challengers such as CubeSandbox's 7-point launch pitching itself as the open-source E2B, and every traction number above is the company's own.**

## Strengths

- Hardware isolation by default on the hosted path, one Firecracker microVM per sandbox, where most self-hosted platforms make you opt into the hard boundary.
- The snapshot-resume design is the fastest provisioning story in the category and the thing every compatibility claim tests against.
- The credential vault at the egress proxy is the same design OpenShell and CubeSandbox advertise, operated for you instead of by you.
- Broadest framework reach: it is the sandbox adapters target and the API self-hosted platforms reimplement, so examples and skills transfer.

## Cautions

- Per-second usage billing scales with agent appetite, the default sandbox is 2 vCPU and 4 GiB, and concurrency caps arrive fast: Hobby 20, Pro 100 before the $650 and $1,150 add-on tiers.
- CPU-only, no GPU sandboxes, so RL and eval workloads needing GPUs go elsewhere.
- The hosted tier is a dependency on one vendor's uptime and regions, and Enterprise starts at a $3,000 monthly minimum.
- No independent audit of the boundary itself exists; SOC 2 covers process, and the runtime's operational record outside E2B's own fleet is short.

## Pricing

Hobby: free, one-time $100 usage credits, 20 concurrent sandboxes, 1-hour sessions, 10 GiB storage included.
Pro: $150 per month plus usage, 100 concurrent, 24-hour sessions, 20 GiB storage; Pro+ and Pro++ add-ons at $650 and $1,150 per month raise concurrency to 600 and 1,100.
Enterprise: custom, with a $3,000 monthly minimum and BYOC.
Published usage rates as of 2026-10-11: $0.000014 per vCPU-second and $0.0000045 per GiB-second, storage included free; sandboxes configure 1 to 8 vCPU and 1 to 8 GiB, CPU-only.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-06 | Hobby / Pro / Pro+ / Pro++ / Enterprise | Baseline: Hobby free with $100 one-time credits; Pro $150 per month plus usage at $0.000014 per vCPU-second and $0.0000045 per GiB-second; Pro+ $650 and Pro++ $1,150 concurrency add-ons; Enterprise $3,000 monthly minimum. | [E2B pricing](https://e2b.dev/pricing) |

## Compared to

- [CubeSandbox](../cubesandbox/index.md): the self-hosted E2B-compatible microVM service; choose it when data residency or sustained volume beats operating a KVM fleet, E2B when zero operations matters.
- [Agent Sandbox](../agent-sandbox/index.md): the Kubernetes orchestrator for the fleet you would otherwise rent; complementary, since agent-sandbox still needs you to run the cluster.
- Modal sandboxes and other hosted APIs: E2B's difference is the agent-native surface (desktop sandboxes, pause and fork, sandbox URLs) and being the API others target for compatibility.

## Bottom line

**Recommended for teams that want hardware-isolated agent execution with no infrastructure and can absorb usage-based billing; it remains the interface the rest of the category codes against.**
Not for GPU workloads, for $0-marginal-cost fleet scale, or for anyone unwilling to let a vendor operate the execution floor.

## Changes

- 2026-10-06 - Created, resolving the standing queue question after E2B served as the comparison baseline in four member notes without a note of its own; prices and counts as of 2026-10-06.
- 2026-10-07 - Added the e2b-dev/E2B star history chart to the Status section.
- 2026-10-10 - Recorded the SDK train moving to 2.55.x (e2b@2.55.0 and @e2b/python-sdk@2.55.1 on 2026-10-09, PyPI now 2.55.1), and refreshed counts (SDK repo 14,265 stars, runtime repo 1,702 stars).
- 2026-10-13 - Recorded the 2.56.0 release of 2026-10-13 opening the next SDK train (Node.js 22 minimum, undici 8 only, the in-flight request caps and their env vars removed), with PyPI at 2.56.0 and counts refreshed (SDK repo 14,324 stars, runtime repo 1,712 stars).
- 2026-10-23 - Recorded the train advancing to 2.59.0 (2.57.0 and 2.58.0 on 2026-10-20: a tls egress-proxy option and streaming stdin/PTY input handles; 2.59.0 on 2026-10-22: per-sandbox DNS server allowlists in the egress firewall, the apiUrl and sandboxUrl options and their env vars deprecated ahead of next-major removal, and unified sandbox domain endpoints), with PyPI at 2.59.0.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [CubeSandbox](../cubesandbox/index.md) - the self-hosted drop-in for exactly this API
- [OpenShell](../openshell/index.md) - the workstation runtime with the same vault-at-proxy design
- [agent-sandbox](../agent-sandbox/index.md) - the Kubernetes path to the same fleet you would rent

## References

- https://e2b.dev - product model, deployment options, SOC 2, regions, Embed
- https://docs.e2b.dev/ - SDK surface, sandbox lifecycle, persistence semantics
- https://e2b.dev/pricing - plans, concurrency tiers, published usage rates as of 2026-10-06
- https://github.com/e2b-dev/E2B - SDK repository, growth, license
- https://github.com/e2b-dev/runtime - the open-source runtime and the Embed single-node package
- https://pypi.org/pypi/e2b/json - the e2b package's current version, 2.59.0 as of 2026-10-23
- https://e2b.dev/blog/series-a - the $21M Series A and the enterprise traction claims
- https://hn.algolia.com/api/v1/items/41860413 - the 2-point 2024 launch thread
- https://hn.algolia.com/api/v1/items/47863430 - CubeSandbox's open-source-alternative launch, the competitive counterpoint
