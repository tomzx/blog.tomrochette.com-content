---
title: Ruflo
created: 2026-10-06
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, meta-harness, claude-code, codex, swarms, agent-memory, federation]
readability: 3
audience_notes: >
  Engineers evaluating meta-harnesses and multi-agent layers over Claude Code and Codex, who can read a GitHub repository critically.
  Assumes you know what a CLI coding harness is and why a star count can mislead.
---

Ruflo is an MIT-licensed, npm-installed meta-harness that wraps Claude Code and Codex with 100+ prebuilt specialized agents, coordinated swarms, persistent self-learning memory, and cross-machine federation.

**Ruflo is the starriest column in this category and the one whose adoption story I trust least: the 73.9k stars measure the renamed Claude Flow repository, the download badges link to proof files committed inside the project's own repo, and the entire independent footprint I can find is a three-point Show HN thread.**

## What it is

A layer around Claude Code and Codex from rUv Cohen's Cognitum.One: one `npx ruflo init` installs 100+ agents, swarm coordination, a learning loop, vector RAG, and security guardrails on top of the CLIs you already run.
The README's own framing is "Agent = Model + Harness", with Ruflo as the harness: an execution layer that routes work from CLI and MCP surfaces through a router into swarms, memory, and model providers.
Federation lets installations on different machines talk to each other without leaking data, a claim no other column in this category's matrix makes at the agent level.
It ships under MIT, installs from npm, and drives the Claude Code and Codex accounts you already have.

## Status

Active and shipping almost daily: v3.53.0 released 2026-10-06 (a version bump plus catalog entry, with the console, ruflo-protector, and mods plugins moving through the git marketplace), v3.52.1 and v3.52.0 the day before, with 40 contributors and an npm release feed that still carries claude-flow-named packages.
73,951 stars, 8,795 forks, and 1,113 open issues as of 2026-10-06.
npm `ruflo` served 60,190 downloads in the week ending 2026-10-04.
**Those stars are inherited: `github.com/ruvnet/claude-flow` returns a 301 redirect to `ruvnet/ruflo`, and the README's star badge still points at the claude-flow shields URL, so the number measures the repository's history under the Claude Flow name plus a rename, not adoption of Ruflo the product.**
The independent evidence for that product is thin: a Show HN from July 2026 at 3 points and an April 2026 "Is any one using ruflo?" post at 1 point.
The "8.1M+ ecosystem downloads" and "106k git clones in 14 days" badges link to JSON proof files committed inside the repository, which is self-measurement, not third-party measurement.

## Strengths

- Breadth per install: agents, swarms, memory, RAG, hooks, and federation in one `npx ruflo init`, where most columns here do one of those.
- Shipping cadence: multiple releases in the first days of October 2026, and 60k weekly npm installs even after discounting the self-reported badges.
- Cross-machine federation is a capability claim no other column in the matrix makes at the agent level.
- MIT and provider-agnostic at the model layer: it drives the Claude Code and Codex subscriptions you already pay for.

## Cautions

- The provenance problem: the project built its reputation as Claude Flow, renamed to Ruflo, and kept the number, while the README badge still points at the old URL and old write-ups describe a different scope.
- Every adoption number that matters is self-reported: the badges cite in-repo proof JSONs, the fourteen-chapter guide is written by the founder, and it is a republished LinkedIn post.
- The community footprint contradicts the star count: 3 points and 1 point on Hacker News against 73.9k stars is the widest gap I have measured in this category.
- 1,113 open issues as of 2026-10-06 suggests support load that has outrun the maintainers.
- The scope is enormous (memory, RAG, swarms, federation, guardrails) for a project past major version 52, which is churn risk by definition.

## Pricing

Free and open source under MIT.
No hosted tier and no Ruflo bill: agents run on your existing Claude Code and Codex accounts, so inference is billed by those providers.

## Compared to

- [OpenRig](../openrig/index.md): the other local meta-harness over your existing Claude Code and Codex installs; choose OpenRig for named, snapshot-restorable teams of terminal sessions, Ruflo for in-process swarms with memory and federation.
- [oh-my-codex](../oh-my-codex/index.md): the workflow layer for Codex CLI alone; choose it if Codex is your only CLI, Ruflo if you run Claude Code and Codex and want agents, memory, and federation around both.
- [CrewAI](../crewai/index.md): the Python framework where you assemble the crew yourself; choose CrewAI when you must own the orchestration code, Ruflo when you want the crew prebuilt.

## Bottom line

**Recommended for Claude Code and Codex users who want a maximal prebuilt agent layer and will verify claims against their own usage rather than the repository's badges.**
Not for teams that need an independently verified adoption history, a stable API surface, or a scope that fits in one afternoon.

## Changes

- 2026-10-06 - Created.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [OpenRig](../openrig/index.md) - the other local meta-harness over your existing installs
- [oh-my-codex](../oh-my-codex/index.md) - the single-CLI version of the same instinct
- [CrewAI](../crewai/index.md) - the build-it-yourself alternative to prebuilt swarms
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this category extends

## References

- https://api.github.com/repos/ruvnet/ruflo - stars, forks, open issues, MIT license, and push date as of 2026-10-06
- https://raw.githubusercontent.com/ruvnet/ruflo/main/README.md - the meta-harness definition, the 100+ agents claim, the claude-flow badge URLs, and the in-repo proof badges
- https://api.github.com/repos/ruvnet/ruflo/releases - v3.52.1 (2026-10-06), the daily cadence, and the claude-flow-named npm packages
- https://raw.githubusercontent.com/ruvnet/ruflo/main/docs/ruflo-explained.md - the fourteen-chapter guide and its Cognitum.One authorship
- https://api.npmjs.org/downloads/point/last-week/ruflo - 60,190 downloads in the week ending 2026-10-04
- https://github.com/ruvnet/claude-flow - the 301 redirect to ruvnet/ruflo behind the inherited star count
- https://cognitum.one/agentic-engineering - the company page the README banner promotes
- https://hn.algolia.com/api/v1/search?query=ruflo&tags=story - the thin Hacker News footprint, both threads and their point counts
- https://news.ycombinator.com/item?id=49051072 - the Show HN thread at 3 points, July 2026
- https://news.ycombinator.com/item?id=47943679 - "Is any one using ruflo?" at 1 point, April 2026
