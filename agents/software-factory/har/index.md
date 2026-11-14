---
title: "HAR"
created: 2026-08-29
updated: 2026-11-14
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=big-pickle, llm=glm-5.3-flash, software-factory, harness, multi-agent, worktrees]
readability: 3
audience_notes: >
  Engineers who run fleets of coding agents on one repo and want deterministic verification and proof of what ran.
  Assumes you know what a worktree, a harness, and an MCP server are.
---

HAR, the open agent harness from os-factory, is a CLI and MCP server that turns a repository into isolated per-agent worktrees with deterministic launch, verify, and teardown stages, so a fleet of coding agents can work concurrently and reviewers trust the output.

## What it is

An Apache-2.0 TypeScript tool, installed via `npm install -g @osfactory/har`, that scaffolds a machine-readable `.har/` contract into any repo naming its stack, scripts, and checks.
Each task gets an isolated slot: its own worktree, branch, ports, and database.
A deterministic verify stage runs the project's real checks and records evidence, logs, artifacts, and a validated tree hash per commit, and Mission Control is the bundled local dashboard.
It is harness-agnostic and works with Claude Code, Cursor, Codex, or any MCP-capable agent.

## Status

Active and shipping: 122 stars and 14 forks since creation on 2026-06-28, v1.25.1 released 2026-11-13 (v1.0.0 landed 2026-08-28, ten releases in the first week of September alone), and the last main push on 2026-11-13 per the GitHub API as of 2026-11-14.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=os-factory/har&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=os-factory/har&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=os-factory/har&type=date&legend=top-left" />
</picture>

v1.16.0 adds a Cypress plugin, the first release since v1.15.1 on 2026-09-28.
v1.16.1 (2026-11-03) pins Playwright at 1.64.1 for browser tests, a one-fix patch that ended the four-week release gap.
**The v1.16.2-through-v1.25.1 burst of 2026-11-09 to 2026-11-13 shipped twelve releases in five days, and its theme is slot-level telemetry and HQ integration: Claude usage is harvested per slot through Mission Control attribution (v1.20.0), cost comes from Claude Code's native metrics via hook spans (v1.21.0), LLM usage is attributed to slots per request through an evidence timeline (v1.22.0, ADR 0003), and that attribution then flows to the portal, with one org connection held at a time (v1.23.0), the evidence-timeline attribution shared with the portal (v1.24.0), Mission Control's attributed usage shipped to the portal (v1.25.0), and v1.25.1 claiming slot evidence that arrives before its slot while pricing Claude Opus 5.5 through genai-prices 0.2.3; beside it, agents get guidance for triaging occupied slots (v1.17.0), the harness reads AGENTS.md directly instead of scaffolding CLAUDE.md (v1.19.0), and the HQ portal moves onto Kerno's portal endpoints (v1.16.2, v1.18.0).**
It carries a code of conduct, security policy, and a sponsor (Kerno, a runtime code tester for coding agents), which is a steadier footprint than the category's usual single-commit repo.

## Strengths

- **One repo contract replaces the scattered run knowledge**: a README, CLAUDE.md, Cursor rules, and CI yaml become one `.har/` that any agent reads the same way.
- **Real concurrency**: each slot gets its own worktree, ports, and database, so agents no longer collide on shared dev servers or git state.
- **Proof, not self-report**: every task runs the same deterministic verify and leaves an evidence trail, because verification passes are tied to the exact code that was checked.
- **Portable away from vendor lock-in**: because the contract lives in the repo as an open standard, switching coding agents does not mean rebuilding the verification setup.

## Cautions

- **It runs alongside a coding agent rather than replacing it**: HAR coordinates and verifies a fleet, but the agents themselves are the harnesses you already pay for, so it is a layer, not a factory that owns the whole loop like Fluent.
- **Young at about 120 stars**, though releases through v1.16.0 signal momentum, not abandonment.
- **The deterministic verify is only as strong as your contract**: a `.har/` that ships placeholder checks is theater, the same trap as the placeholder gates elsewhere in this category.
- **It depends on the ecosystem staying open**: its value rests on a portable contract and MCP support holding across vendors in a landscape that keeps consolidating.

## Pricing

Apache-2.0, free, installable from npm with no license cost.
You bring the coding agents and their subscriptions, and Mission Control runs locally on your machine.
HAR HQ, the hosted team layer, published its first pricing (as of 2026-09-18, re-verified 2026-11-14): Team at $400 per month for up to 50 users with $100 in monthly cloud credits included, and Enterprise custom with self-hosted or VPC deployment, SSO, SAML, SCIM, and SLAs.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-18 | HAR HQ Team | First published pricing: Team $400/mo for up to 50 users with $100 monthly cloud credits, Enterprise custom; the core stays Apache-2.0 free. | [harhq.com](https://harhq.com) |

## Compared to

- [Super Simple Software Factory](../super-simple-software-factory/index.md) stamps a Python loop into the repo and owns phases and gates in code; HAR is harness-side, isolating and verifying a fleet around a repo contract rather than stamping a single loop.
- [Fluent](../fluent/index.md) adds a deterministic final Tester and a self-improvement learning loop on top of worktree isolation; HAR provides the isolation and verification but delegates the reviewing and learning to its agents.
- [Harnesses](../../harnesses/harness-feature-matrix/index.md) are the single coding agents (Claude Code, Codex) that HAR coordinates; this category is the fleet-and-factory layer above them.

## Bottom line

Recommended for teams running several coding agents on one repository who want concurrent work, deterministic verification, and an evidence trail without rewriting their agent setup.
Not for a solo developer doing one agent at a time, where the harness alone is simpler than the fleet machinery.

## Changes

- 2026-08-29 - Created in the software factory alternatives scan as the harness-style member.
- 2026-09-12 - Recorded HAR HQ, a hosted team layer with no published pricing, replacing the earlier no-cloud claim.
- 2026-09-13 - Recorded HAR HQ's first published pricing (Team $400 per month up to 50 users, Enterprise custom), replacing the no-pricing note.
- 2026-09-16 - Recorded the v1.14.2 release (2026-09-14) and re-verified HAR HQ pricing unchanged.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-25 - Recorded the v1.14.3 release (2026-09-24) and re-verified HAR HQ pricing unchanged.
- 2026-09-27 - Recorded the v1.15.0 release (2026-09-26) and re-verified HAR HQ pricing unchanged.
- 2026-09-29 - Recorded the v1.15.1 release (2026-09-28) and refreshed counts (96 stars, pushed 2026-09-28); HAR HQ pricing re-verified unchanged.
- 2026-10-07 - Added the os-factory/har star history chart to the Status section.
- 2026-10-07 - Recorded the v1.16.0 release (2026-10-07, Cypress plugin); HAR HQ pricing re-verified unchanged.
- 2026-10-17 - Rotation re-verification: repository, releases (v1.16.0 still newest, no push since 2026-10-07), the docs site (plugin marketplace and iOS profile now advertised), the Kerno sponsorship (Kerno v1 live), the demo video, and HAR HQ pricing (Team $400 unchanged) all re-fetched; no material change.
- 2026-10-23 - Rotation re-verification: repository, releases (v1.16.0 still newest, no push since 2026-10-07), the docs site (marketplace now listing seven plugins), the demo video, the Kerno sponsorship (Kerno v1), and HAR HQ pricing (Team $400 with $100 monthly cloud credits, Enterprise custom, unchanged) all re-fetched; no material change.
- 2026-10-28 - Rotation re-verification: repository, releases (v1.16.0 still newest, no push since 2026-10-07), the docs site (marketplace still listing seven plugins), the demo video, the Kerno sponsorship (Kerno v1 live), and HAR HQ pricing (Team $400 with $100 monthly cloud credits, Enterprise custom, unchanged) all re-fetched; no material change.
- 2026-11-07 - Recorded the v1.16.1 release (2026-11-03, Playwright pinned at 1.64.1 for browser tests) and the rotation re-verification: repository, releases, the docs site (marketplace still listing seven plugins), the demo video, the Kerno sponsorship, and HAR HQ pricing (Team $400 with $100 monthly cloud credits, Enterprise custom, unchanged) all re-fetched; no other material change.
- 2026-11-13 - Recorded the v1.16.2-through-v1.22.0 burst (eight releases, 2026-11-09 to 2026-11-13): per-slot Claude usage and cost telemetry through Mission Control attribution, native-metric hook spans, and a per-request evidence timeline (v1.20.0 to v1.22.0, ADR 0003), occupied-slot triage guidance (v1.17.0), AGENTS.md read directly instead of scaffolding CLAUDE.md (v1.19.0), and the HQ portal's move onto Kerno's endpoints (v1.16.2, v1.18.0); HAR HQ pricing re-verified unchanged.
- 2026-11-14 - Recorded the burst reaching v1.25.1 (twelve releases, 2026-11-09 to 2026-11-13): the attribution line extended to the portal, with one org connection at a time (v1.23.0), evidence-timeline attribution shared with the portal (v1.24.0), Mission Control's attributed usage shipped to the portal (v1.25.0), and the out-of-order slot-evidence claim fix plus Claude Opus 5.5 pricing through genai-prices 0.2.3 (v1.25.1); HAR HQ pricing re-verified unchanged.

## See also

- [Super Simple Software Factory](../super-simple-software-factory/index.md) - the founding member this harness-style factory is read against
- [Fluent](../fluent/index.md) - the self-improving factory that also owns the full loop
- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - the category matrix HAR now fills a column in
- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - the single coding agents a HAR fleet coordinates
- [Code Factories: Wow](../../../code-factories-wow/index.md) - the corpus metaphor this category scales toward

## References

- https://github.com/os-factory/har - the repo, the `.har/` contract, and the verify-and-evidence model
- https://harproject.dev - the documentation covering concepts, verification, MCP tools, and Mission Control
- https://youtu.be/XKl4ZzWy7mQ - the introductory demo of the harness
- https://github.com/os-factory/har/releases - the release cadence, v1.0.0 through v1.25.1
- https://kerno.io - the sponsor that tests runtime code for coding agents, grounding the verification emphasis
- https://harhq.com - the HAR HQ site, grounding the Team $400 per month and Enterprise custom tiers as of 2026-09-18
