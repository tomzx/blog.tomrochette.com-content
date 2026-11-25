---
title: Microsandbox
created: 2026-10-07
updated: 2026-11-25
readability: 3
audience_notes: >
  Engineers who want hardware-isolated sandboxes with container-style ergonomics on their own machines, including letting agents spawn VMs themselves.
  Assumes you know what a microVM, an OCI image, and libkrun are.
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, sandboxing, microvm, isolation, open-source]
---

Microsandbox is a local-first, Apache-2.0 microVM runtime and library, built on libkrun, that runs untrusted workloads in fast virtual machines with Docker-like workflows, OCI images, fork and snapshot semantics, and support for Linux, macOS, and Windows hosts.

**Microsandbox made VMs behave like containers, and it is the only member of this category built for agents to create their own sandboxes: a shipped Agent Skills package and MCP server let a running agent spawn microVMs as tools.**

## What it is

A runtime binary plus an embeddable library: you pull standard OCI images from Docker Hub, GHCR, or any registry, then run, exec, and attach to them like containers, except each one is a hardware-isolated VM with its own kernel.
The README claims average boot times under 100 milliseconds, a self-reported figure footnoted to guest boot on an M1 machine, and the state model goes beyond containers: pause and resume, snapshots, and forking a live sandbox.
Credentials are advertised as "secret keys that never enter the VM", the project's own unverified claim of unexploitable secret handling.
It embeds in application code (no long-running daemon required), runs sandboxes in detached mode for long-lived sessions, and ships a companion Agent Skills repository and MCP server so agents can create and manage their own sandboxes.
The same SDK and CLI surface can also select a hosted backend, microsandbox cloud, which runs the sandboxes on the company's infrastructure with an API key.
The project carries a Y Combinator badge and has moved organizations more than once since its 2024 launch, landing at superradcompany/microsandbox.

## Status

Large by this category's standards and still shipping weekly: 8,704 stars as of 2026-10-23, 205 open issues and PRs as of 2026-11-25, pushed 2026-11-24, created 2024-10-03.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=superradcompany/microsandbox&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=superradcompany/microsandbox&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=superradcompany/microsandbox&type=date&legend=top-left" />
</picture>

v0.7.5, v0.7.6, and v0.7.7 shipped within a week ending 2026-10-05, a fast pre-1.0 minor-version cadence, v0.7.8 followed on 2026-10-09 (secret substitution scoped to specific header fields, runtime-owned detached jobs, port ranges in published ports, snapshot filesystem-state limits, and a fix that refuses disk restores which would silently drop host mounts), v0.7.9 on 2026-10-22 (adding and removing published ports on running sandboxes, SDK-visible sandbox exit outcomes, JSON network-policy denial output by default, optional exec output backpressure, live label modifications on running sandboxes, restricted-backend configuration, and HTTP CONNECT proxy basic authentication), and v0.7.10 and v0.7.11 inside the same week after it: v0.7.10 on 2026-10-23 (anonymous registry auth in the Go SDK, the project's published smoltcp fork adopted for networking, custom filesystem backends honored, and secret policy writable from the Node and Go SDKs), v0.7.11 on 2026-10-24 (SDK-exposed HTTP CONNECT proxy authentication, a fix for terminal sessions hanging after output, caller config overrides preserved across rebuilds, and recovery of the cleanup left by an interrupted sandbox creation), v0.7.12 closing the week on 2026-10-31 (nested virtualization support, secret modification on cloud sandboxes, and the Windows bind-mount rename and macOS sparse-seek translation fixes), and v0.7.13 following on 2026-11-01 as a Homebrew-repair release for the v0.7.12 install breakage.
That week's post-release train shipped as v0.7.14 on 2026-11-08 (inbound TCP queuing with admission metrics, the stdin, logs, init, image, and port CLI failure repairs, Windows reparse points skipped in directory listings, legacy sandbox storage recovery, ssh failed-command outcomes preserved, cloud SDK cleanup and CLI onboarding repairs, and the libkrunfw 0.1.45 dependency update), and v0.7.15 shipped on 2026-11-12 as the stable cut of the train that followed it (opt-in candidate installs and publishing, and per-file host operations cut on passthrough mounts).
v0.7.16 shipped on 2026-11-18 (Services objects joining the SDKs and CLI, SNI DNS bindings revalidated on reconnect, the libkrun and multigrain firmware updated, every cloud sandbox status decoded by the SDK, and bulk cleanup bursts kept from stopping the guest).
v0.8.1 shipped on 2026-11-23 as the stable cut of the 0.8 line (the v0.8.0 tag carries no published release): the breaking change enforcing snapshot import limits through load options, operator resolvers for multi-tenant DNS, the cloud SDK fixes (a rejected workdir reported as a typed error, a cloud sandbox's own workdir, shell, and command used, env secret references resolved on cloud create, long cloud log follows and downloads preserved), and the v0.8 upgrade guide in the docs.
v0.8.2 followed on 2026-11-24, the newest published release as of 2026-11-25: the SDK switching to the cloud restart route, SDK runtime isolation options, opt-in strict host file opens and bounded patch source staging, opt-in independent file materialization for snapshots, explicit in-band relay connections for the agent surface, a strict hostname policy on UDP egress, isolated authenticated OCI caches with enforced cache-auth provenance, private storage on shared NTFS drives on Windows, a cargo-deny audit beside the locked dependency update, and `--exclude-from` on `msb image prune`; the same day's README update announces microsandbox cloud.
**Its Show HN of 2025-05-30 drew 402 points, the largest community thread of any member of this category, while a June 2026 resubmission drew 3 points, so the launch was a 2025 event and the current proof of life is the release train, not public debate.**

## Strengths

- A hardware boundary with container ergonomics: OCI images, docker-like commands, and sub-second starts remove most of the friction that kept VMs out of agent loops.
- The agent-self-service angle (skills plus MCP) is unique in the category and matches how agents actually operate.
- Fork and snapshot of live VMs enable checkpointing, backtracking, and fan-out patterns containers cannot express as cleanly.
- Cross-platform including Windows, which almost no workstation member here can say.

## Cautions

- Every performance and security claim is self-reported: the sub-100ms boot figure, the unexploitable-secrets claim, none independently audited or benchmarked.
- The hosted backend is metered usage with a credit model (Builder $20 a month including $20 of usage, Teams $200 including $200, as of 2026-11-25), so the cost story beyond self-hosting scales with agent appetite.
- Pre-1.0 with rapid minor-version churn and three organization homes since 2024 (the launch linked microsandbox/microsandbox, later zerocore-ai, now superradcompany), a provenance trail adopters should watch.
- The 402-point launch is a 2025 memory; the 2026 resubmission's 3 points mean the project must be judged on its repo, not its HN history.
- libkrun shares the virtualization story with its upstream: capable, but the isolation claims ride on a dependency this project does not control.

## Pricing

Free and open source under Apache-2.0, self-hosted; the costs are the local or fleet hardware you run it on.
microsandbox cloud, the hosted backend running the same sandboxes through the same SDK and CLI with API-key billing, published prices as of 2026-11-25: Standard compute at $0.048 per vCPU-hour and $0.003 per GiB-hour, Shared-capacity compute at $0.007 and $0.000375, root disk at $0.0000625 per GiB-hour on both, persistent volumes at $0.15 per GiB-month and snapshots at $0.08 per GiB-month, on two plans, Builder at $20 per month including $20 of usage credit and Teams at $200 per month including $200 of usage credit.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-11-25 | microsandbox cloud (Builder / Teams) | Cloud prices first published: Builder $20 per month including $20 of usage credit; Teams $200 per month including $200 of usage credit; Standard compute $0.048 per vCPU-hour and $0.003 per GiB-hour; Shared-capacity compute $0.007 and $0.000375; root disk $0.0000625 per GiB-hour; volumes $0.15 and snapshots $0.08 per GiB-month (no prices published as of 2026-10-17). | [microsandbox cloud pricing](https://docs.microsandbox.dev/cloud/pricing) |

## Compared to

- [CubeSandbox](../cubesandbox/index.md): Tencent's server-fleet E2B-compatible microVM service for many concurrent sandboxes on KVM nodes; Microsandbox is the local-first, embeddable runtime for your own machine.
- [E2B](../e2b/index.md): the hosted baseline with per-second billing; Microsandbox is the buy-nothing path to the same VM boundary.
- [NVX](../nvx/index.md): Microsoft's research-grade microVM sandbox with the Windows-native hypervisor paths; Microsandbox is the productized one, NVX the instrumented one.

## Bottom line

**Recommended for engineers who want VM isolation with container workflows on their own hardware, and for agent-framework authors who want the agent itself to spawn isolated environments.**
Not for anyone needing audited claims or a stable 1.0 API, and not for teams that need a written availability commitment from the hosted tier before adopting it.

## Changes

- 2026-10-07 - Created from the entrant-resolution run, profiling the libkrun-based microVM runtime behind the category's largest HN thread, with its self-reported-claims and provenance cautions.
- 2026-10-10 - Recorded v0.7.8 (2026-10-09, header-scoped secret substitution, detached jobs, port ranges, snapshot limits, and the refuse-unsafe-restore fix), and refreshed counts (8,628 stars, 95 open issues and PRs, pushed 2026-10-10).
- 2026-10-17 - Recorded the microsandbox cloud hosted backend (private beta, API-key billing, no published prices) in What it is, Cautions, Pricing, and the Bottom line, and fixed the star-history picture block (rotation re-verification; every cited URL re-fetched, v0.7.8 still the newest release).
- 2026-10-23 - Recorded v0.7.9 (2026-10-22, live port and label modifications on running sandboxes, SDK-visible exit outcomes, JSON network-policy denial output by default, exec output backpressure, restricted-backend configuration, and HTTP CONNECT proxy basic authentication).
- 2026-10-25 - Recorded v0.7.10 (2026-10-23, anonymous registry auth in the Go SDK, the published smoltcp fork, custom filesystem backends, SDK-writable secret policy) and v0.7.11 (2026-10-24, SDK-exposed HTTP CONNECT proxy authentication, the terminal-hang fix, config overrides preserved across rebuilds, interrupted-creation cleanup recovery), with counts refreshed (123 open issues and PRs, pushed 2026-10-25).
- 2026-11-01 - Recorded v0.7.12 (2026-10-31, nested virtualization support, secret modification on cloud sandboxes, and the Windows bind-mount rename and macOS sparse-seek fixes), with the cloud still private beta, open issues and PRs at 156, and the repository pushed 2026-11-01.
- 2026-11-07 - Recorded v0.7.13 (2026-11-01, the Homebrew repair release for the v0.7.12 install breakage) and the post-release train through 2026-11-07 (the stdin, logs, init, image, and port CLI failure fixes, inbound TCP queuing with admission metrics, disposable Windows WHP integration runners, and Windows reparse points skipped in listings), with the repository pushed 2026-11-07.
- 2026-11-08 - Volatile refresh: the post-release train advanced through 2026-11-08 (legacy sandbox storage recovery, ssh failed-command outcomes preserved, cloud SDK cleanup and CLI onboarding repairs, and the libkrunfw 0.1.45 dependency update), with open issues and PRs at 161 and the repository pushed 2026-11-08.
- 2026-11-12 - Recorded v0.7.14 (2026-11-08, the stable cut of the previously recorded post-release train: inbound TCP queuing with admission metrics, the CLI failure repairs, Windows reparse-point skipping, legacy storage recovery, preserved ssh failed-command outcomes, cloud SDK cleanup, and the libkrunfw 0.1.45 update) and the v0.7.15 bump on main (2026-11-11, unreleased), with the repository pushed 2026-11-11.
- 2026-11-13 - Recorded v0.7.15 (2026-11-12, the stable cut of the opt-in candidate installs and publishing plus the per-file passthrough-mount host-operation cuts), with open issues and PRs at 175 and the repository pushed 2026-11-12.
- 2026-11-14 - Volatile refresh: the post-v0.7.15 train continues on main unreleased, with open issues and PRs moving from 175 to 183 and the repository pushed 2026-11-14.
- 2026-11-15 - Volatile refresh: v0.7.15 still the newest release, main's newest commit staying the 2026-11-12 Ubuntu package-mirror fallback while the repository-level push moved to 2026-11-15 on branch activity, and open issues and PRs moving from 183 to 189.
- 2026-11-18 - Recorded v0.7.16 (2026-11-18, Services objects joining the SDKs and CLI, SNI DNS bindings revalidated on reconnect, the libkrun and multigrain firmware update, full cloud-status decoding in the SDK, and bulk cleanup bursts kept from stopping the guest), with open issues and PRs moving from 189 to 191 and the repository pushed 2026-11-18.
- 2026-11-21 - Volatile refresh: the 0.8 line is cut on main unreleased (the bump commits reaching 0.8.1 on 2026-11-20, with breaking snapshot import limits enforced through load options, multi-tenant DNS resolver isolation, and v0.8 upgrade guidance in the docs), v0.7.16 still the newest published release, open issues and PRs holding at 191, with the repository pushed 2026-11-21.
- 2026-11-22 - Volatile refresh: the 0.8 train advanced on main (the SDK switching to the cloud restart route on 2026-11-21), v0.7.16 still the newest published release, with the repository pushed 2026-11-22.
- 2026-11-25 - Recorded v0.8.1 (2026-11-23, the stable cut of the 0.8 line: breaking snapshot import limits through load options, operator resolvers for multi-tenant DNS, the cloud SDK workdir and secret-reference fixes, the v0.8 upgrade guide) and v0.8.2 (2026-11-24, the newest published release: the cloud restart route in the SDK, SDK runtime isolation options, strict host file opens, a strict hostname policy on UDP egress, isolated authenticated OCI caches, the cargo-deny audit), and the first published microsandbox cloud prices (Builder and Teams plans with Standard and Shared-capacity rates, as of 2026-11-25) with the Price history table seeded; open issues and PRs moving from 191 to 205, with the repository pushed 2026-11-24; rotation re-verification with every cited URL re-fetched.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [CubeSandbox](../cubesandbox/index.md) - the server-fleet counterpart to this local runtime
- [NVX](../nvx/index.md) - the research-grade microVM sandbox from Microsoft
- [E2B](../e2b/index.md) - the hosted API this runtime's skill story parallels

## References

- https://github.com/superradcompany/microsandbox - repository, feature list, libkrun acknowledgement, YC badge, organization moves
- https://api.github.com/repos/superradcompany/microsandbox - stars, open issues, creation and push dates as of 2026-10-07
- https://api.github.com/repos/superradcompany/microsandbox/releases - the v0.7.5 through v0.8.2 release record
- https://docs.microsandbox.dev/ - the documentation site
- https://docs.microsandbox.dev/cloud/overview - the cloud overview: same SDK and CLI surface, billing in the dashboard, links to the pricing and limitations pages
- https://docs.microsandbox.dev/cloud/pricing - the cloud plans and resource rates as of 2026-11-25
- https://hn.algolia.com/api/v1/items/44135977 - the 402-point Show HN of 2025-05-30, including the isolation-tradeoff questions in the thread
