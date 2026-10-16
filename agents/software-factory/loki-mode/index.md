---
title: Loki Mode
created: 2026-10-07
updated: 2026-10-16
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
It installs from npm, Bun, Homebrew, or Docker and runs on your machine with your own keys against Claude by default, with Cline, Codex, Aider, and OpenCode supported as experimental providers; a bundled MCP server exposes 39 tools including run, status, and verify for background runs.
Before a build counts as done, a review council selects reviewers from a scored specialist pool, and if the contract cannot be derived the run blocks and asks one question instead of guessing.
Autonomi publishes it under BUSL-1.1, and the README documents outcomes and exit codes, a workspace command, and a doctor that names setup blockers.

## Status

Active and shipping fast: 1,093 stars and 206 forks since creation on 2025-12-26 (as of 2026-10-13), 179,996 Docker pulls as of 2026-10-16, per GitHub and Docker Hub.
Pushed 2026-10-16, and the npm train moved from 11.3.9 (2026-10-09) to v11.15.0 (2026-10-16), published under the `next` tag while `latest` holds 11.10.1, per the GitHub API and the npm registry as of 2026-10-16.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=asklokesh/loki-mode&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=asklokesh/loki-mode&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=asklokesh/loki-mode&type=date&legend=top-left" />
</picture>

**Its Hacker News footprint is self-submitted threads in the single digits, and the 99.67 percent SWE-Bench claim in one of them is self-reported, so no independent evaluation exists as of 2026-10-07.**
The version line moves faster still: eight published releases in the two days to 2026-10-09, after the five that closed 2026-10-08, with v11.3.3 never published because its release run failed.
The 11.4-to-11.15 burst added a publish pattern the release notes state plainly: most tagged versions in the run (v11.4.0 through v11.14.0) failed required CI and reached npm only through fix-forward patches, and v11.6.0 was a consolidation release that merged or deleted every duplicate module under an "extend existing code, never duplicate" rule.
v11.3.1 shipped the 11.3 program's ten v1 features (cost preview, mutation proof, intent card, reviewer brief, scored worktree attempts, memory with proof, overnight queue, before/after proof, provider failover, and a supply-chain guard), the router escalation chain and plan-time routing from v11.3.0 stay off by default, and the v11.3.4 through v11.3.9 security arc hardened credential reach, with the release notes now stating plainly that this is default-path hardening, not a sandbox.

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

Free as a source-available CLI: the BUSL-1.1 grant covers personal, internal, academic, and non-commercial use, converts the code to Apache-2.0 on 2030-03-19, and names founder@autonomi.dev for other arrangements.
You bring your own model keys, and Autonomi's site describes a live control plane without published prices as of 2026-10-09, a page this run could not re-fetch (empty on both 2026-10-11 attempts).
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
- 2026-10-09 - Recorded the train to 11.3.9 (eight published releases since 11.3.0, v11.3.3 never published after a failed release run), the v11.3.1 ship of the 11.3 program's ten v1 features, the v11.3.4-v11.3.9 credential-hardening arc with its "hardening, not a sandbox" wording, the provider roster's Cline and Aider additions as experimental, and refreshed counts.
- 2026-10-11 - Added the BUSL-1.1 use grant and its 2030-03-19 Apache-2.0 conversion date to Pricing, recorded the autonomi.dev fetch failure (empty on two attempts), and refreshed counts.
- 2026-10-16 - Recorded the train from 11.3.9 to v11.15.0 (2026-10-16, `next` tag while `latest` holds 11.10.1), the fix-forward publish pattern where CI-failed tags reached npm only through patches, and the v11.6.0 consolidation release.

## See also

- [Ouroboros](../ouroboros/index.md) - the other verification-first member, hidden grading versus signed receipts
- [Super Simple Software Factory](../super-simple-software-factory/index.md) - the MIT stamped-loop alternative
- [SuperPlane](../superplane/index.md) - the platform factory alternative
- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - where the receipt column sits among the factories

## References

- https://github.com/asklokesh/loki-mode - repository, delivery contract, review council, MCP server, and install methods
- https://www.autonomi.dev - Autonomi's site and the issue-to-PR-with-signed-receipt positioning
- https://www.npmjs.com/package/loki-mode - the npm package, 11.3.9 latest as of 2026-10-09
- https://github.com/asklokesh/loki-mode/releases/tag/v11.3.1 - the v11.3.1 release notes, the 11.3 program's ten v1 features including scored attempts and memory with proof
- https://github.com/asklokesh/loki-mode/releases/tag/v11.3.9 - the v11.3.9 release notes, credential-isolation follow-ups and backstop-triggered promotion
- https://hub.docker.com/r/asklokesh/loki-mode - the Docker image and its pull count
- https://github.com/asklokesh/loki-mode/blob/main/LICENSE - Business Source License 1.1
- https://news.ycombinator.com/item?id=46393705 - the Show HN thread, 4 points
- https://news.ycombinator.com/item?id=46528155 - the self-reported 99.67 percent SWE-Bench thread, 2 points
