---
title: Sandstorm
created: 2026-10-31
updated: 2026-10-31
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, microvm, gvisor, firecracker, sandbox-lifecycle]
readability: 3
audience_notes: >
  Engineers running self-hosted fleets of agent sandboxes who are paying for idle machines.
  Assumes you know what a microVM, a container, and a snapshot are.
---

Sandstorm is a self-hosted Rust platform that fits thousands of agent sandboxes onto machines by pausing idle ones, snapshotting them to disk, and restoring them quickly when traffic arrives.

**Sandstorm's bet is that agent sandboxes idle most of the time, so a tiered pause-snapshot-restore lifecycle, not bigger machines, is what makes a sandbox fleet affordable.**

## What it is

One binary, `sandstormd`, serves as the master, the node agent, and the web console, with the master holding desired state in SQLite and placing sandboxes across nodes.
Sandboxes run in one of two backends, gVisor containers or Firecracker microVMs, each sandbox in its own network namespace, and both backends can pool in one fleet.
The lifecycle has four tiers: hot (running), frozen (paused, cold pages in zswap, about 0.1 s back to hot), snapshot (checkpointed to disk, about 0.2 s back), and detached (volume only, cold start).
Nodes join by address and pairing code or dial out from behind NAT, a per-node gateway wakes a sandbox on incoming traffic, and nodes refuse new work under memory pressure so the host stays reachable.
Apache-2.0, by DeepLethe (whose own site, deeplethe.com, is a Chinese-language company page), created 2026-05-11 under the name forkd and since renamed (the old path redirects; a forkd-action repository remains).

## Status

Active and unreleased for five months: 3,270 stars, 293 forks, and 11 open issues and pull requests as of 2026-10-31 (GitHub API), pushed 2026-10-31, while the newest tag is still v0.5.3 from 2026-07-22.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=deeplethe/sandstorm&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=deeplethe/sandstorm&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=deeplethe/sandstorm&type=date&legend=top-left" />
</picture>

Zero independent footprint: a Hacker News search returns no story about this project as of 2026-10-31, and the latency chart on the README is self-published and self-measured.
The name collides with Sandstorm.io, the long-archived self-hosted app platform, which still owns search results for the word.

## Strengths

- **The lifecycle is the feature**: published wake latencies per tier (about 0.1 s frozen, about 0.2 s from snapshot) aim the design at idle memory, the actual cost driver of sandbox fleets.
- Real isolation boundaries, not wrappers around them: gVisor and Firecracker are first-class backends with their own optimization passes, documented with before-and-after measurements in the repo's OPTIMIZATIONS.md.
- Fleet plumbing in one binary: SQLite desired state, NAT-dialing nodes, wake-on-traffic gateway, and self-protecting nodes.

## Cautions

- No release since July 2026 while main pushes daily, so adopters run source builds or pin to a stale tag.
- Every performance number is self-measured, with no third-party benchmark or write-up found anywhere.
- Single-vendor project with a Chinese-language company presence and no English community channel surfaced, so roadmap visibility and support are thin.
- The Sandstorm name fight against Sandstorm.io for search and mindshare is a permanent tax.

## Pricing

Does not apply: the platform is open-source and self-hosted, and no hosted tier is on offer.

## Compared to

- Microsandbox: a local-first embeddable microVM runtime for sandboxes on one machine; choose Sandstorm when the fleet spans machines and idle cost, not sandbox startup, is the problem.
- CubeSandbox: Tencent's self-hosted, E2B-compatible microVM sandbox service; it is API-first where Sandstorm is lifecycle-first with a web console and placement.
- E2B: the hosted Firecracker API that defines the category baseline; choose it for zero ops, and Sandstorm to own the machines underneath.

## Bottom line

Recommended for engineers running self-hosted agent-sandbox fleets on their own machines, who can accept an unreleased main and self-measured numbers. Not for teams wanting a hosted API, a tagged release, or an independently reviewed product.

## Changes

- 2026-10-31 - Created.

## See also

- [Microsandbox](../microsandbox/index.md) - the local-first microVM runtime this note's lifecycle economics answer at fleet scale
- [CubeSandbox](../cubesandbox/index.md) - the self-hosted microVM sandbox service closest in shape
- [E2B](../e2b/index.md) - the hosted baseline every self-hosted entry here is measured against
- [Overalls](../overalls/index.md) - the other self-hosted Firecracker platform in the category

## References

- https://github.com/deeplethe/sandstorm - repository, feature set, backends, and lifecycle claims
- https://raw.githubusercontent.com/deeplethe/sandstorm/HEAD/README.md - tier table, latency chart, key features, and naming
- https://raw.githubusercontent.com/deeplethe/sandstorm/HEAD/docs/OPTIMIZATIONS.md - the per-backend optimization evidence
- https://github.com/deeplethe/sandstorm/releases - the stalled release train (v0.5.3, 2026-07-22)
- https://deeplethe.com - the maker and its Chinese-language company presence
- https://hn.algolia.com/api/v1/search?query=deeplethe%20sandstorm&tags=story - the zero-story Hacker News footprint as of 2026-10-31
