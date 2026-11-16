---
title: "Exo"
created: 2026-09-05
updated: 2026-11-16
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agent, self-improvement, agent-hosting, rust]
readability: 3
audience_notes: >
  Engineers curious about self-modifying agent harnesses and the recursive self-improvement idea, and cost-sensitive practitioners looking at the cheapest measured harness.
  Assumes you know what an agent harness, Docker, and an API key are.
---

**Exo is an open-source (MIT) runtime that hosts markdown-defined agents behind an API on the coding harness you pick, Codex, Claude Code, and Pi included; its first-year product, a self-modifying agent harness, is archived as Earlier Exo.**

**Exo traded its original bet for an infrastructure one: the recursive self-improvement harness this note first profiled now lives in the repository's archive, and the live project positions itself as the open, self-hostable alternative to Claude Managed Agents and OpenAI's Agents API.**

## What it is

A Rust-and-TypeScript runtime from Exo Labs (exoharness.ai, MIT) where an agent is a markdown file (`harness:` front matter picks Codex, Claude Code, or Pi, plus model and credential) and `exo run` hosts it behind an API with durable conversations, resumable tasks, per-user credential vaults, Firecracker sandboxes, and network egress policies.
Slack and custom adapters reach the hosted agents, and the architecture doc's stated bet is harness agnosticism: the harness's semantics stay with the harness you chose, while Exo owns the infrastructure layer, so you can switch harnesses or models without rewriting the application.
The first-year product, the self-modifying harness with an append-only event log as its brake, is preserved under `examples/self-improving-agent/` with its RSI.md design document, and the docs' "Earlier Exo" archive section names it as a previous iteration.

## Status

**Pivoted: the self-modifying harness the note first profiled is archived as "Earlier Exo", and the active project is a harness-agnostic agent hosting runtime.**
The docs' archive section records the self-evolution harness as a previous iteration, and the commit stream since the pivot is infrastructure work: Firecracker snapshot budgets and the 1.18.0 bump, typed sandbox failures, opt-in egress redirect policies, a configurable process-bridge stdin, and shared OAuth refresh for provider vaults (GitHub API, as of 2026-11-16, on a repo created 2026-05-20, pushed 2026-11-13, with 1,505 stars at the 2026-10-15 baseline and 132 forks).
Still no tagged releases as of 2026-11-16.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=exoharness/exo&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=exoharness/exo&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=exoharness/exo&type=date&legend=top-left" />
</picture>

**The independent FrontierHarness Eval measured the archived self-modification harness near the bottom of nine harnesses on pass rate but first on cost: 53.3 percent pass at a $1.05 median cost per task, against Claude Code's $18.34 on the same model and tasks; the board's v1.1 layout re-read unchanged on 2026-11-16 (the August 22 run, scored on Kimi K3).**
The community footprint is thin, a 3-point and a 2-point Hacker News thread, so the eval and the repository are nearly the whole evidence base as of 2026-10-04.

## Strengths

- The hosting runtime is the pragmatic product: markdown agent definitions, durable conversations, per-user credential vaults, and egress policies wrapped around harnesses you already run.
- The dropped self-modification bet is preserved rather than erased: RSI.md and the examples tree document the architecture, which is rare for a retired thesis.
- Harness substitution without application rewrites is the specific gap it fills against Claude Managed Agents and OpenAI's Agents API.
- MIT licensed with CI and integration-test badges visible in the repository.

## Cautions

- **The pivot retires the thesis the note was written for**: the self-rewriting harness no longer has a maintainer's ambition behind it, and its safety question ended unanswered.
- No tagged releases as of 2026-11-16, so adoption means pinning commits, and the docs carry an under-construction banner with installation instructions still being written.
- The runtime holds credentials (vaults) and enforces network policy, a security reviewer's problem of its own.
- Docker or Firecracker and a toolchain bootstrap keep the footprint heavier than a single-binary CLI agent.

## Pricing

Free and open source under MIT.
You pay model tokens to the provider behind whichever harness an agent runs on; the FrontierHarness run measured the archived harness at the lowest median token cost per completed task in the field on Kimi K3 pricing (the figure lives in Status above, where the benchmark that produced it is cited).

## Compared to

- [Omnigent](../omnigent/index.md): the docs' own nearest analog, the same harness-agnostic hosting bet with policies and sandboxes behind one API; Exo is the smaller, self-hostable counterpart.
- [Pi](../pi/index.md): Pi keeps a minimal core you extend with human-written TypeScript packages, while Exo delegates the whole loop to a harness you bring.
- [Hermes](../../assistant-runtimes/hermes/index.md): the self-improvement incumbent by scale; Hermes learns within a fixed harness, a conservative version of the bet Exo dropped.

## Bottom line

Recommended for engineers who want to self-host agents on the harness they already trust, with credentials and network policy handled by the runtime.
Not for anyone chasing the recursive self-improvement thesis, which the project itself has archived, or for production use without pinning a commit.
I read the pivot as the market's verdict on self-modifying harnesses: the infrastructure around the harness sold, the harness that rewrote itself did not.

## Changes

- 2026-09-05 - Created in the Harnesses category during the six-entrant resolution run.
- 2026-09-06 - Rewrote the FrontierHarness sentence, correcting a mathematically wrong pass-rate claim while keeping the $1.05-per-task cost figure.
- 2026-09-08 - Reverted a sub-run error that had claimed twelve FrontierHarness harnesses instead of nine.
- 2026-09-16 - Refreshed repository scale to 1,413 stars and 106 forks; the FrontierHarness cost and pass-rate figures are unchanged.
- 2026-10-06 - Refreshed repository counters (1,486 stars) and corrected the stale harness count in the See-also matrix line.
- 2026-10-06 - Moved the FrontierHarness dollar figure out of the Pricing section, leaving it in Status where the benchmark is cited, so the note conforms to the price-history rule.
- 2026-10-07 - Added the exoharness/exo star history chart to the Status section.
- 2026-10-17 - Repaired the RSI.md reference in the rotation pass: the repository restructure moved the document from docs/ to examples/self-improving-agent/docs/ (the old URL 404s), and refreshed the push date.
- 2026-10-25 - Rotation re-verification, every cited reference live (RSI.md at its post-restructure path), and the push date refreshed to 2026-10-23; no releases and no new independent evaluation, so the FrontierHarness figures stand as cited.
- 2026-10-31 - Rotation re-verification, every cited reference live: pushed date refreshed to 2026-10-31, and the FrontierHarness figures re-read unchanged ($1.05 median, 53.3 percent pass) from the live site.
- 2026-11-08 - Rotation re-verification, every cited reference live: the push date refreshed to 2026-11-08, still no tagged releases, and the FrontierHarness figures re-read unchanged ($1.05 median, 53.3 percent pass, Claude Code at $18.34) from the live site.
- 2026-11-16 - Rotation re-verification surfaced the pivot: the docs now archive the self-modifying harness as "Earlier Exo" and pitch Exo as a harness-agnostic agent hosting runtime (markdown-defined agents, durable conversations, Firecracker sandboxes, vaults, and egress policies over Codex, Claude Code, and Pi); rewrote the definition, What it is, Status, Strengths, Cautions, Compared to, and Bottom line to the pivoted product, reframed the FrontierHarness figures as measuring the archived iteration (re-read unchanged on the v1.1 board), and refreshed the push date to 2026-11-13.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - where the self-modification bet sits among the category's members
- [Pi](../pi/index.md) - the human-directed counterpart to agent-directed extension
- [Software Factory Feature Matrix](../../software-factory/software-factory-feature-matrix/index.md) - deterministic loop owners versus a harness that lets the agent own its own loop
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map this harness sits in

## References

- https://github.com/exoharness/exo - repository, license, architecture, and setup requirements
- https://exoharness.ai/docs - the docs pitching the hosting runtime, the markdown agent model, the Omnigent comparison, and the "Earlier Exo" archive section naming the self-evolution harness a previous iteration (fetched 2026-11-16)
- https://github.com/exoharness/exo/blob/main/examples/self-improving-agent/docs/RSI.md - the recursive self improvement design document of the archived iteration (moved from docs/ in the repository restructure)
- https://frontierharness.org - the independent cost and pass-rate measurements
- https://frontierharness.org/leaderboard/eval-data.json - the v1.1 board data re-read 2026-11-16: exo at 53.3 percent pass and $1.05 effective cost per pass, first of the field, against Claude Code's $18.34 (the 2026-08-22 run, Kimi K3, nine harnesses)
- https://hn.algolia.com/api/v1/items/49430143 - the larger of the two HN threads, cited as the thin-footprint signal
