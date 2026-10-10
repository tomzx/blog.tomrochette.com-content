---
title: Brig
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, microvm, isolation, macos, linux, open-source]
readability: 3
audience_notes: >
  Engineers who want a maintained microVM around coding agents on their own Apple Silicon or Linux workstation.
  Assumes you know what a microVM, Hypervisor.framework, and cosign image verification are.
---

Brig is NOFire AI's Apache-2.0 Go tooling that runs coding agents such as Claude Code, Codex, Gemini CLI, OpenCode, or Grok inside a per-agent microVM on your own machine, with the project directory mounted read-write, no host credential reach, and cosign-verified guest images.

**Brig is the maintained successor to the workstation-VM slot Clawk went quiet in, and its distinguishing artifact is documentation: a security page that states every boundary, every measured limit, and every trust assumption in public.**

## What it is

A Go CLI (brig) plus an optional session daemon (brigd) that drive a microVM runtime: on Apple Silicon, hull's hvi backend drives Hypervisor.framework directly (six of eight built-in profiles), with Virtualization.framework and Linux nerdctl plus the urunc shim as the other paths, and host-kernel-sharing runc or crun shims refused outright since v0.4.0 rather than merely discouraged.
The agent gets its own kernel and home directory, the named project mounts read-write at /work/<name>, and nothing else on the host is reachable, with `brig doctor` checking the host and `brig info` printing the exact isolation envelope before a boot.
Credentials never enter by default: runs read no host credential source, secrets live in a store backed by the macOS keychain or a Linux Secret Service keyring, and profiles name exactly what crosses, delivered as files on a tmpfs mount or as environment variables.
Built by NOFire AI, the team behind urunc, a CNCF Sandbox project; images, boot assets, and release binaries are cosign keyless-verified against pinned GitHub workflows, and the macOS binaries are Apple notarized.

## Status

Young but professionally built: 218 stars, 21 forks as of 2026-10-09, created 2026-08-12, pushed 2026-10-08, Apache-2.0.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=brig-sh/brig&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=brig-sh/brig&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=brig-sh/brig&type=date&legend=top-left" />
</picture>

v0.2.0 shipped 2026-09-15, v0.3.0 on 2026-09-26, and v0.4.0 on 2026-10-06, with channel-main prereleases cutting almost daily in between and since (0.4.1 builds from 2026-10-08).
The Show HN launch on 2026-09-22 drew 9 points, and the maintainer's introduction is most of the thread's substance, so the community footprint is thin and the documentation is where the evidence lives.
**A nine-point launch against 218 stars in eight weeks reads as quiet, deliberate adoption rather than a wave, and no independent audit or benchmark exists yet, while v0.4.0's breaking changes show the security defaults are still moving: new sandboxes now get isolated networks by default on hvi and Linux, and the runtime refuses shims that share the host kernel.**

## Strengths

- A microVM boundary by default on both Apple Silicon and Linux, with the isolation envelope printed per run instead of assumed.
- The most candid security documentation in the category: the docs publish measured sandbox-to-sandbox reachability results with dates, admit the shared-network answer changed between measurements, and list the trust assumptions no vendor can engineer away.
- Supply-chain verification beyond every peer here: guest images, kernels, initrds, and release binaries are cosign-verified against workflow-anchored identities, with a `require` mode that refuses what it cannot verify.
- Explicit backend behavior: egress policies are refused, not silently ignored, on backends that cannot enforce them.

## Cautions

- Pre-1.0 (v0.4.0) with daily prerelease churn and no independent audit.
- Egress policies enforce on hull's hvi backend and, since v0.4.0, on Linux through nftables on the sandbox's own bridge, while the vz, qemu, and docker backends have no policy enforcement, and the default with no policy attached is open internet access.
- Two sandboxes on a shared network can reach each other by the project's own measurements, and v0.4.0 made isolated networks the default for new sandboxes on hvi and Linux (vz, qemu, and the claude-desktop profile stay shared), while the docs warn the shared-network answer is not a stable property.
- The credential model has stated sharp edges: Brig's stored copy of a Claude refresh token is less protected than the original keychain item, and `files:` bindings bypass the denylist by design.
- Intel Macs are unsupported, and macOS 14 needs fallback variables.

## Pricing

Free and open source under Apache-2.0; the costs are local compute and image pulls.
No hosted tier or pricing page exists as of 2026-10-06.

## Compared to

- [Clawk](../clawk/index.md): the earlier disposable-VM workstation tool, macOS-only and quiet since August 2026; choose Brig for active maintenance, Linux support, and verification, Clawk for its conversation-resume workflow.
- [Drop](../drop/index.md): the namespace wrapper that keeps your host distro with no VM; Drop is lighter, Brig's boundary is stronger (its own kernel) and crosses platforms.
- [OpenShell](../openshell/index.md): NVIDIA's runtime adds declarative L7 egress policy and proxy-held keys; choose OpenShell for organizational policy, Brig for a personal, per-project microVM.

## Bottom line

**Recommended for engineers on Apple Silicon or Linux who want a coding agent fenced by a microVM on their own machine and will read the unusually detailed security docs.**
Not for Intel Macs, for anyone needing enforced egress policy on Linux today, or for teams that require an audited boundary.

## Changes

- 2026-10-06 - Created from the entrant-resolution run, profiling the actively maintained microVM workstation sandbox with the category's most detailed published security claims.
- 2026-10-07 - Added the brig-sh/brig star history chart to the Status section.
- 2026-10-07 - Recorded v0.4.0 (2026-10-06) with its breaking changes (new sandboxes isolated by default on hvi and Linux, host-kernel shims refused, exit 7 for unenforceable properties), corrected the Linux egress-enforcement caution against the current security docs (enforced in nftables), and refreshed counts (211 stars).

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [Clawk](../clawk/index.md) - the macOS-only VM predecessor in the same slot
- [Drop](../drop/index.md) - the lighter namespace-only alternative on Linux
- [OpenShell](../openshell/index.md) - the policy-engine runtime above the workstation

## References

- https://github.com/brig-sh/brig - repository, README, platform table, install, verification defaults
- https://github.com/brig-sh/brig/releases - the v0.2.0, v0.3.0, and channel-main release record
- https://brig.sh/docs/quickstart/ - the doctor/run/stop workflow, the execution envelope, host support
- https://brig.sh/docs/security/ - the boundary claims, measured shared-network results, credential limits, and trust assumptions
- https://hn.algolia.com/api/v1/items/49802729 - the 9-point Show HN launch by NOFire AI's founder
