---
title: Fabro
created: 2026-10-10
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, software-factory, workflow-graphs, rust]
readability: 3
audience_notes: >
  Expert teams that want their agent process version-controlled as a graph they author.
  Assumes you know what a workflow node, a human gate, and a model router are.
---

Fabro is an MIT-licensed Rust server that runs software work as version-controlled Graphviz graphs: nodes are agents, shell commands, or human approval gates, and the server owns sequencing, branching, loops, and verification.

## What it is

**The process is a diffable file: workflows are Graphviz DOT checked into version control, with a CSS-like stylesheet routing each node to a model.**
Bryan Helmkamp's (QLty) project installs as a single zero-dependency binary via Homebrew, an install script, or Docker, and runs as a server with a React web UI and a REST API with SSE events.
Verification layers combine test suites, linters, type checkers, and LLM-as-judge, and failures trigger fix loops automatically.
Execution runs on your laptop or in Daytona cloud sandboxes with SSH and preview links, every stage commits code and metadata to git branches, and the durable event stream is queryable with SQL via DuckDB.

## Status

Active: 1,702 stars since creation on 2026-03-13 (as of 2026-10-13), pushed 2026-10-25, per the GitHub API.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=fabro-sh/fabro&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=fabro-sh/fabro&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=fabro-sh/fabro&type=date&theme=dark&legend=top-left" />
</picture>

**Every tagged release is a nightly prerelease (v0.396.0-nightly.0 of 2026-10-24 the newest), the Homebrew tap serves fabro-nightly, and no stable release exists.**
The independent footprint is two self-submitted Show HN threads at 7 and 6 points, where the author names Stripe's Minions and Factory.ai Droids as the analogs and positions Fabro as the open, own-your-toolchain alternative.

## Strengths

- **The workflow is a reviewable artifact**: DOT graphs are diffable, version-controlled, and reusable across a team, the clearest process-as-code statement in the category.
- Stylesheets route each node to a model with fallback chains, so planning runs cheap models and coding runs frontier ones.
- Human gates are graph nodes rather than afterthoughts, and steering reaches running agents mid-turn.
- Verification failures trigger fix loops automatically, and git checkpointing makes runs resumable and revertible.

## Cautions

- **Nightly-only distribution**: no stable tag exists, so production users track a moving prerelease train.
- Thin independent footprint: two self-submitted single-digit threads and no third-party evaluation.
- Cloud isolation means a Daytona dependency, and local runs give it up.
- The DOT dialect is Fabro-specific, so a team's accumulated graph library is process lock-in.

## Pricing

MIT, free, and self-hosted, with a one-click Railway deploy of the same Docker image.
There is no hosted tier and no published prices.

## Compared to

- [Zeroshot](../zeroshot/index.md) ships the review loop built in; Fabro makes you author the graph, and anything can be a node, including shell commands and human gates.
- [SuperPlane](../superplane/index.md) owns the intake-to-PR line as a platform; Fabro is a workflow server you point at the process you define.
- [Fluent](../fluent/index.md) is a fixed factory loop with a deterministic final gate; Fabro provides the graph primitives to build your own loop.

## Bottom line

**Recommended for expert teams that want their agent process version-controlled and diffable, with human judgment encoded as gates in the graph.**
Not for anyone needing stable tagged releases, proven scale, or a factory that arrives with its process already decided.

## Changes

- 2026-10-10 - Created from the awesome-software-factories scan as the workflow-graph member.
- 2026-10-19 - Rotation re-verification: every cited URL re-fetched (repository, why-fabro docs, the launch thread, the releases API, the HN search, and the awesome-software-factories list) and all claims confirmed, including the nightly-only train (v0.389.0-nightly.0 still the newest tag) and the pushed date; no material change.
- 2026-10-23 - Corrected the star-history chart's light source, which wrongly carried the dark-theme parameter, and refreshed the volatile lines (pushed 2026-10-22, nightly train at v0.393.0-nightly.1); no material change.
- 2026-10-25 - Refreshed the volatile lines (pushed 2026-10-25, nightly train at v0.396.0-nightly.0); no material change.

## See also

- [Zeroshot](../zeroshot/index.md) - the built-in-review-loop alternative
- [Fluent](../fluent/index.md) - the opinionated fixed-loop comparison
- [SuperPlane](../superplane/index.md) - the platform factory alternative
- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - where the workflow-graph column sits among the factories

## References

- https://github.com/fabro-sh/fabro - repository, feature table, example workflow, install methods, and license
- https://docs.fabro.sh/getting-started/why-fabro - the problem framing, the DOT-graph model, and the verification layers
- https://news.ycombinator.com/item?id=47652404 - the author's launch thread, analogs, and positioning
- https://api.github.com/repos/fabro-sh/fabro/releases - the nightly-only release train, v0.396.0-nightly.0 newest as of 2026-10-25
- https://hn.algolia.com/api/v1/search?query=fabro&tags=story - the thin independent-discussion footprint this note records
- https://github.com/varun1505/awesome-software-factories - the third-party curated list that surfaced this note
