---
title: Loki Mode
created: 2026-10-07
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, software-factory, autonomous-agents, verification]
readability: 3
audience_notes: >
  Engineers who want an autonomous issue-to-pull-request factory that proves what it delivered.
  Assumes you know what an acceptance contract, an MCP server, and a source-available license are.
---

Loki Mode is Autonomi's source-available autonomous software factory: hand it a PRD, a GitHub issue, an OpenAPI doc, or a one-line brief, and it derives a delivery contract, builds against it, and ends with a signed Evidence Receipt stating what was proven and what was not.

## What it is

**A local CLI factory whose acceptance artifact is a receipt you can re-check offline, not an agent's claim of done.**
It installs from npm, Bun, Homebrew, or Docker and runs on your machine with your own keys against Claude, Codex, and OpenCode; a bundled MCP server exposes 39 tools including run, status, and verify for background runs.
Before a build counts as done, a review council selects reviewers from a scored specialist pool, and if the contract cannot be derived the run blocks and asks one question instead of guessing.
Autonomi publishes it under BUSL-1.1, and the README documents outcomes and exit codes, a workspace command, and a doctor that names setup blockers.

## Status

Active and shipping fast: 1,087 stars and 208 forks since creation on 2025-12-26, pushed 2026-10-08, npm at 11.3.0 (2026-10-08), and 174,997 Docker pulls, per GitHub, npm, and Docker Hub as of 2026-10-08.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=asklokesh/loki-mode&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=asklokesh/loki-mode&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=asklokesh/loki-mode&type=date&legend=top-left" />
</picture>

**Its Hacker News footprint is self-submitted threads in the single digits, and the 99.67 percent SWE-Bench claim in one of them is self-reported, so no independent evaluation exists as of 2026-10-07.**
The version line moves fast: five releases landed in the two days to 2026-10-08.
v11.3.0 adds a model router escalation chain and plan-time routing shipped off by default, with the release notes claiming byte-identical behavior when LOKI_ROUTER is unset across a 156-scenario differential.

## Strengths

- **The receipt is the acceptance artifact**: it states what was proven and what was not, and anyone can re-check it offline.
- **It refuses to guess**: an underivable contract blocks the run with one question, a rarer safety move than another retry.
- **The review council is pulled, not prompted**: reviewers are selected from a scored specialist pool per run.
- **Distribution is finished**: npm, Homebrew, and Docker installs, a doctor for setup, and an MCP server for programmatic runs.

## Cautions

- **BUSL-1.1 is source-available, not open source**: the code is readable but not OSI-licensed, and GitHub cannot classify the license.
- **The README's Documentation link dead-ends**: the wiki it points to does not exist, so docs live in scattered repo files.
- **Benchmark claims are self-reported** and the HN threads are self-submitted; treat the SWE-Bench number as marketing until a third party repeats it.
- **Version churn is fast**, with a v10 engine already superseded by an 11.x line.

## Pricing

Free as a source-available CLI; you bring your own model keys, and Autonomi's site describes a live control plane without published prices as of 2026-10-07.
There is no public tier to track yet.

## Compared to

- [Super Simple Software Factory](../super-simple-software-factory/index.md) is the MIT stamped-skill minimalist; Loki Mode is a packaged CLI with a receipt gate under a BUSL license.
- [Ouroboros](../ouroboros/index.md) hides the grading from the worker; Loki Mode signs what was proven and lets you verify the receipt yourself.
- [SuperPlane](../superplane/index.md) runs the intake-to-PR line as a shared platform; Loki Mode runs it locally with your keys.

## Bottom line

**Recommended for engineers who want an autonomous issue-to-PR loop with an offline-checkable receipt and accept a source-available license and self-reported benchmarks.**
Not for teams that require OSI licensing, and not for anyone who needs independent evaluation first.

## Changes

- 2026-10-07 - Created from the category's entrant scan as the receipt-gated member.
- 2026-10-08 - Recorded the npm train's jump from 11.0.3 to 11.3.0 (five releases in the two days to 2026-10-08, led by the router escalation chain shipped off by default) and refreshed counts.

## See also

- [Ouroboros](../ouroboros/index.md) - the other verification-first member, hidden grading versus signed receipts
- [Super Simple Software Factory](../super-simple-software-factory/index.md) - the MIT stamped-loop alternative
- [SuperPlane](../superplane/index.md) - the platform factory alternative
- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - where the receipt column sits among the factories

## References

- https://github.com/asklokesh/loki-mode - repository, delivery contract, review council, MCP server, and install methods
- https://www.autonomi.dev - Autonomi's site and the issue-to-PR-with-signed-receipt positioning
- https://www.npmjs.com/package/loki-mode - the npm package, 11.3.0 latest as of 2026-10-08
- https://github.com/asklokesh/loki-mode/releases/tag/v11.3.0 - the v11.3.0 release notes, router escalation chain off by default and skill-link healing hardening
- https://hub.docker.com/r/asklokesh/loki-mode - the Docker image and its pull count
- https://github.com/asklokesh/loki-mode/blob/main/LICENSE - Business Source License 1.1
- https://news.ycombinator.com/item?id=46393705 - the Show HN thread, 4 points
- https://news.ycombinator.com/item?id=46528155 - the self-reported 99.67 percent SWE-Bench thread, 2 points
