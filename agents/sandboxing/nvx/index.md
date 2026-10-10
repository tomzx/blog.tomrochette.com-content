---
title: NVX
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, microvm, isolation, microsoft, research, open-source]
readability: 3
audience_notes: >
  Platform engineers tracking where Microsoft research is taking microVM isolation for agentic workloads, especially on Windows hypervisors.
  Assumes you know what a microVM, OpenVMM, and a snapshot ABI are.
---

NVX is Microsoft's MIT-licensed microVM sandbox for agentic workloads, built on OpenVMM by the MSR Systems Research Group and Azure Research with a guest derived from the Nanvix research system, running Linux guests on Linux/KVM, Linux/MSHV, and Windows/WHP behind a Python harness.

**NVX is this category's first native-Windows boundary and its most self-limited project: the design docs carry a current-limits page that enumerates, in detail, everything the ABI deliberately does not do, which is the opposite of the usual sandbox marketing.**

## What it is

An ultra-light microVM whose repository ships version pins, patches, guest sources, build tooling, and benchmarks: `scripts/nvx.py download && scripts/nvx.py run` boots an Alpine guest (Ubuntu selectable) and opens a root shell, on KVM, Microsoft's MSHV, or the Windows Hypervisor Platform.
The design documentation covers a machine and device ABI, time ABI, snapshot and restore, snapshot sharing, a sandbox filesystem and agent architecture, concurrency and trust boundaries, validation, and a Copilot-driven adversarial-testing program, with sections explicitly marked as not yet implemented.
A benchmark coordinator runs a 21-metric microVM workload suite plus lifecycle metrics, gates p50 results in CI across one, two, four, and eight vCPUs, and versions its history by ABI so regressions compare against the right baseline.
This is a research artifact with a release train of daily `v0.1.0-dev` prereleases and no stable release.

## Status

Young, institutional, and quiet in public: 369 stars, pushed 2026-10-09 as of 2026-10-09, created 2026-08-27.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=microsoft/nvx&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=microsoft/nvx&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=microsoft/nvx&type=date&theme=dark&legend=top-left" />
</picture>

Daily dev prereleases have cut continuously since late September 2026, with the repository pushed the day of this refresh.
**The single Hacker News thread drew 3 points on 2026-10-03, so this is a Microsoft research release being watched by almost nobody yet, and its substance lives in the design and limits documents rather than community debate.**

## Strengths

- The only member of this category with native Windows (WHP) and MSHV paths; every workstation peer is macOS or Linux first.
- Documentation rigor at research grade: an explicit limits page, ABI-versioned benchmark history, and adversarial testing with Copilot as the fuzzer.
- Snapshot and restore with sharing, the provisioning primitive the hosted platforms charge for, exposed as a research CLI.
- Institutional backing from MSR and Azure Research, with the Nanvix lineage documented rather than implied.

## Cautions

- No stable release and an ABI family that rules out, by its own limits page, live migration, CPU and memory hotplug, non-x86 guests, firmware boot, nested virtualization, and a production control RPC.
- No agent profiles, no policy engine, no credential story yet: the agent-workload positioning is in the description and the design docs, not in shipped integrations.
- The community footprint is one 3-point HN thread; there is no independent evaluation of the isolation claims.
- A research project at a large company can be reorganized into, or out of, existence without notice.

## Pricing

Free and open source under MIT, no paid tiers or hosted offering.
Costs are the KVM, MSHV, or WHP-capable host you run it on.

## Compared to

- [Brig](../brig/index.md): the polished workstation microVM with agent profiles, cosign verification, and shipped egress policy; NVX is the instrumented research frontier, Brig the tool to actually run agents in.
- [Microsandbox](../microsandbox/index.md): the libkrun runtime that made local microVMs feel like containers; NVX trades ergonomics for measurement discipline and Windows coverage.
- [Agent Sandbox](../agent-sandbox/index.md): the Kubernetes orchestrator that could one day schedule NVX-class VMs as a RuntimeClass, the way it delegates to gVisor and Kata today.

## Bottom line

**Recommended as a watch: the project to read if you need to know where Microsoft thinks microVM sandboxes for agents are going, or if you specifically need Windows-hypervisor isolation research.**
Not for running agents today, which is what Brig, OpenShell, or the hosted APIs are for.

## Changes

- 2026-10-07 - Created from the entrant-resolution run, profiling Microsoft's OpenVMM-based research sandbox with its current-limits honesty and Windows-only-in-category coverage.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [Brig](../brig/index.md) - the workstation microVM that is production-leaning where NVX is research
- [Microsandbox](../microsandbox/index.md) - the local-first libkrun counterpart
- [Agent Sandbox](../agent-sandbox/index.md) - the Kubernetes layer that delegates to isolation runtimes

## References

- https://github.com/microsoft/nvx - repository, README, institutional provenance, platform paths
- https://raw.githubusercontent.com/microsoft/nvx/dev/doc/benchmarks.md - the benchmark methodology and CI gating
- https://raw.githubusercontent.com/microsoft/nvx/dev/doc/design/current-limits.md - the ABI's own limits, the critical source
- https://raw.githubusercontent.com/microsoft/nvx/dev/doc/design.md - the design index including the agent architecture and adversarial testing
- https://api.github.com/repos/microsoft/nvx - stars, creation and push dates, license as of 2026-10-07
- https://api.github.com/repos/microsoft/nvx/releases - the daily v0.1.0-dev prerelease train
- https://hn.algolia.com/api/v1/items/49941250 - the 3-point HN submission of 2026-10-03
