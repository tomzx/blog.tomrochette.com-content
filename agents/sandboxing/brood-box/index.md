---
title: Brood Box
created: 2026-10-12
updated: 2026-10-23
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, microvm, isolation, kvm, open-source]
readability: 3
audience_notes: >
  Engineers who want a coding agent fenced by a hardware boundary and a mandatory
  per-file diff review before anything lands on their workspace.
  Assumes you know what a microVM, KVM, and copy-on-write snapshots are.
---

Brood Box is Stacklok's experimental Apache-2.0 Go CLI that runs coding agents inside libkrun microVMs against a copy-on-write snapshot of your workspace, then flushes changes back only after you approve a per-file diff.

**Its distinguishing feature is the review gate: the VM stops before review begins, and a SHA-256 differ with flush-time hash re-verification stands between everything the agent did and your actual files.**

## What it is

A self-contained `bbox` binary (pure Go, no CGO) that boots a libkrun microVM per run: KVM on Linux, Hypervisor.framework on Apple Silicon macOS, with the libkrunfw firmware downloaded at first run and cached.
The default workspace mode copies your project into a snapshot (FICLONE on Linux, clonefile(2) on macOS), mounts it through virtio-fs, and never writes to your files without passing the diff engine; a direct mode writes through unreviewed but requires an explicit operator flag with --yes, and per-workspace config cannot enable it.
Five agent commands ship built in (Claude Code, Codex, OpenCode, Hermes, Gemini CLI), custom agents take an OCI image and command in config, and `bbox run-image` runs an arbitrary image one-shot with safer-than-custom defaults.
A DNS-aware egress firewall offers three profiles (permissive, standard, locked) plus per-host allowlist entries, and a ToolHive proxy forwards MCP servers into the VM.
Built by Stacklok, the supply-chain security company behind ToolHive and Minder; the README carries an experimental warning badge.

## Status

Small and steady: 78 stars, 8 contributors including its dependency bot, as of 2026-10-16, created 2026-02-13, pushed 2026-10-22, Apache-2.0.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=stacklok/brood-box&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=stacklok/brood-box&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=stacklok/brood-box&type=date&legend=top-left" />
</picture>

The release train ran from v0.0.18 (2026-05-04) through v0.0.25 (2026-09-14), roughly monthly, with commits resuming 2026-10-13 after a month quiet (dependency bumps and, on 2026-10-16, a contributor PR adding `.claude.json` to Claude Code's retained credential paths), and the dependency-bump train continuing through 2026-10-21.
I found no Hacker News thread for the project (the Algolia query for "brood box" returns zero stories), so the 78 stars arrived without any launch moment.
**A vendor-owned project with six months of monthly releases is the reliable kind of small, but the footprint is too thin for community security review, the boundary is self-described, and no audit exists.**

## Strengths

- The review gate is structural: the VM stops before the diff renders, so the agent cannot modify files while you review, and flush-time re-hashing guards the window between diff and write.
- Tighten-only workspace config: a repo cannot widen egress, disable review, switch to direct mode, or negate the always-excluded secret patterns (.env, *.pem, .ssh/, .aws/).
- The egress firewall is DNS-aware with a locked profile that reaches the LLM provider only, plus --allow-host entries by hostname.
- Vendor depth: Stacklok maintains ToolHive, and MCP servers proxy into the VM through it rather than being installed inside.

## Cautions

- Pre-1.0 (v0.0.25) with a self-declared experimental badge and no independent audit.
- The isolation mechanism is libkrun, the same runtime family as Microsandbox; the novelty is the workflow, not a new boundary primitive.
- Apple Silicon only on macOS, KVM required on Linux, and the firmware download path is a runtime dependency (disableable with --no-firmware-download).
- No public discussion footprint: 78 stars and zero HN threads mean nobody has stress-tested the claims in public.

## Pricing

Free and open source under Apache-2.0; the costs are your VM host resources and image pulls.
No hosted tier or pricing page exists as of 2026-10-12.

## Compared to

- [Microsandbox](../microsandbox/index.md): the same libkrun family as an embeddable runtime where agents spawn their own sandboxes; choose Brood Box when a mandatory human diff gate is the point.
- [Brig](../brig/index.md): the other vendor-backed workstation microVM, with broader platform coverage and measured security docs; Brig targets parallel per-agent VMs, Brood Box one reviewed session at a time.
- [Yolobox](../yolobox/index.md): the container-grade shortcut with sudo inside; Brood Box costs a VM boot but gives the agent its own kernel.

## Bottom line

**Recommended for engineers on Apple Silicon or KVM Linux who want a hardware boundary plus a mandatory human diff gate before agent changes touch the workspace.**
Not for Windows or Intel Macs, for parallel multi-agent fleets (the job Brig does), or for anyone requiring an audited or community-reviewed boundary.

## Changes

- 2026-10-12 - Created from the 2026-10-12 awesome-claude-code scan, profiling Stacklok's review-gated microVM runner with the review gate recorded as the distinguishing mechanism.
- 2026-10-13 - Recorded commits resuming 2026-10-13 after a month quiet (a ToolHive v0.52.0 dependency bump); v0.0.25 remains the latest release and counts are unchanged.
- 2026-10-23 - Rotation re-verification: every cited URL re-fetched (repository, release train, ToolHive, the HN story search), all alive; the push advanced to 2026-10-22 on dependency bumps alone, v0.0.25 remains the latest release, the experimental README stands unchanged, and the HN story search still returns zero hits.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [Microsandbox](../microsandbox/index.md) - the libkrun neighbor with an embeddable runtime instead of a review gate
- [Brig](../brig/index.md) - the other vendor-backed workstation microVM sandbox
- [Yolobox](../yolobox/index.md) - the container-grade alternative when a VM is more than you need

## References

- https://github.com/stacklok/brood-box - repository, README (mechanism, workspace modes, egress firewall, security model), 78 stars, dates, license, as of 2026-10-16
- https://api.github.com/repos/stacklok/brood-box/releases - the v0.0.18 through v0.0.25 release train
- https://github.com/stacklok/toolhive - the ToolHive MCP platform the VM proxy integrates, Stacklok's other product
- https://hn.algolia.com/api/v1/search?query=%22brood%20box%22&tags=story - zero story hits (2026-10-12), the missing-launch-footprint record
