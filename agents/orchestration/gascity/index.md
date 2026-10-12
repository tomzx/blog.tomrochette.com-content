---
title: Gas City
created: 2026-10-12
updated: 2026-10-12
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, sdk, multi-agent, formulas, worktrees]
readability: 3
audience_notes: >
  Engineers who followed Gas Town and want to know what survived it, or who want to build a fleet orchestrator
  from primitives instead of adopting a product. Assumes you know git worktrees and what a merge queue is.
---

Gas City is the MIT orchestration-builder SDK extracted from Gas Town: six composable primitives (agents, beads, formulas, rigs, packs, events) that turn a written-once job description into a fleet of coding agents running outside your session, with zero roles hardcoded into the binary.

**Its bet is the opposite of its predecessor's: where Gas Town shipped a town with fixed roles, Gas City ships infrastructure, and every orchestration built on it, Gas Town included, inherits the improvements.**

## What it is

A Go binary (`gc`) plus the beads CLI that runs a declarative `city.toml`: rigs register projects, agents are configuration with prompt templates, and formulas compile into bead graphs the controller/supervisor loop reconciles to running state (README and docs, fetched 2026-10-12).
Runtime providers cover tmux, subprocess, exec, ACP, Kubernetes, and herdr, so a city can drive local terminals or a cluster.
The v1 model runs single-agent, in-session formulas; the v2 model decomposes a job into beads, fans ready work out in parallel across agents, gates each step on dependencies, and retries failures to completion.
It is maintained by the gastownhall org, the same lineage as Steve Yegge's Gas Town, with docs on Mintlify and Blacksmith as the visible sponsor.

## Status

**Active, and the only living branch of the Gas Town lineage.**
1,362 stars, 445 forks, 1,492 open issues, created 2026-02-22, pushed 2026-10-12, as of 2026-10-12 (GitHub API).
Yegge announced the direction in the May 2026 "Welcome to Gas City" essay, and the 33-point Hacker News thread on it (2026-05-04) is the project's main independent record.
Development continued after Gas Town itself was shut down in September 2026, and the migration doc maps every Town role, mechanism, and command onto City primitives.
The release list is toolchain and edge tags rather than a semver application line, so there is no stable-release marker yet.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=gastownhall/gascity&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=gastownhall/gascity&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=gastownhall/gascity&type=date&theme=dark&legend=top-left" />
</picture>

## Strengths

- **The fleet-orchestration loop is the most complete workflow engine in this category**: decomposition, parallel fan-out, dependency gating, retries, and crash-safe bead units that survive a downed agent.
- The extraction is verifiable, not a rebrand: the mayor, deacon, witness, refinery, polecat, crew, and dog all became configuration, and the docs carry the full mapping tables.
- Providers include two category members, tmux and herdr, so the SDK can orchestrate over infrastructure you may already run.
- Packs make orchestration shareable: a city imports reusable behavior, and a feature added to the platform lifts every city built on it.

## Cautions

- **The lineage carries its own cautionary record**: Gas Town was shut down nine months in, with its author saying he never successfully built anything with it, and Gas City is the same org's second attempt at the same problem.
- 1,492 open issues against 445 forks is the highest fork-to-star ratio in this batch and a lot of open work for an SDK with no stable release line.
- The v2 formula model is young and the docs say host-enabled defaults are still settling, so expect churn in the core abstraction.
- The docs position Gas City as "the platform for building software factories", which makes it adjacent to the software-factory products tracked separately in this section; the SDK-versus-product difference is the reason it profiles here.

## Pricing

Pricing does not apply: the SDK is free and MIT-licensed, with Blacksmith sponsorship as the visible funding surface.
The costs are your agents' model tokens and whatever machines run the city.

## Compared to

- [Gas Town](../gastown/index.md): the shut-down town this was extracted from; choose Gas City if you want the coordination as composable infrastructure, and read both notes before investing.
- [Bernstein](../bernstein/index.md): the deterministic scheduler and policy layer; Bernstein owns governance and audit, Gas City owns decomposition and fan-out.
- [Archon](../archon/index.md): the YAML workflow engine over coding-agent SDKs; Archon is a product with triggers, Gas City is a toolkit you assemble a product from.

## Bottom line

**Recommended for engineers who want Gas Town's coordination as primitives, can carry a pre-stable SDK, and will read the migration doc before porting any Town habit.**
Not for teams that need a maintained product with a stable release line today, or anyone unwilling to inherit a lineage whose first product its own author abandoned.

## Changes

- 2026-10-12 - Created from the 2026-10-12 candidate scan, with the lineage risk and the fork-and-issue load recorded as the critical angle.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Gas Town](../gastown/index.md) - the shut-down predecessor whose mechanisms this extracts
- [Bernstein](../bernstein/index.md) - the governance-first counterpoint in the same workflow-runner seat
- [Archon](../archon/index.md) - the product-shaped workflow engine over the coding-agent SDKs

## References

- https://github.com/gastownhall/gascity - repository, 1,362 stars, forks, issues, dates, MIT license, and the provider list, as of 2026-10-12 (fetched through the GitHub API)
- https://github.com/gastownhall/gascity/blob/main/README.md - the extraction framing, city.toml model, dependency list, and the coming-from-Gas-Town pointer
- https://docs.gascityhall.com - the six primitives (Agent, Bead, Formula, Rig, Pack, Event) and the software-factory positioning
- https://docs.gascity.com/getting-started/coming-from-gastown - the role, mechanism, and command mapping tables grounding the extraction claims
- https://news.ycombinator.com/item?id=48015146 - the 33-point May 2026 thread on Yegge's "Welcome to Gas City" essay, the main independent record
- https://hn.algolia.com/api/v1/search?query=%22Welcome%20to%20Gas%20City%22&tags=story - the thread search confirming points and dates (2026-10-12); the Yegge Medium essay itself returned 403 to automated fetch this run
