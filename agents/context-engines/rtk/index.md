---
title: rtk
created: 2026-08-30
updated: 2026-11-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, context-engines, token-efficiency, cli, open-source]
readability: 3
audience_notes: >
  Engineers paying per-token for coding agents whose sessions are dominated by noisy command output.
  Assumes you know what a pre-tool-use hook and a context window are.
---

rtk is a free, open-source Rust CLI proxy that intercepts shell commands run by coding agents and compresses their output before it enters the context window, claiming up to 90 percent fewer output bytes on supported commands.

**rtk monetizes the least glamorous line in the agent budget, the command output nobody reads, and its own documentation admits the 90 percent headline is an output-bytes number, not a bill reduction.**
That admission is why I trust the project and discount the marketing at the same time.

## What it is

A single dependency-free Rust binary that sits between the agent and the shell: a pre-tool-use hook (or rules file) rewrites commands like `git status` to `rtk git status`, and rtk returns a filtered, grouped, truncated, and deduplicated version, with under 10 milliseconds of claimed overhead.
Coverage is per-command strategy: git status/diff/log, grep and ripgrep, find, test runners (pytest, cargo test, jest, vitest, playwright), linters and typecheckers, package managers, docker and kubectl, AWS CLI, and generic wrappers for anything else; git push becomes one line.
Full raw output is tee'd to disk when a filtered command fails, `rtk proxy` gives raw passthrough, and `rtk gain` reports measured savings.
Hooks ship for 16 tools including Claude Code, Codex, OpenCode, Cursor, Gemini CLI, Copilot, Windsurf, and Cline.
Apache-2.0, built by a small French team with a commercial Pro product alongside.

## Status

Young and hot: 83,540 stars as of 2026-10-18, 5,633 forks and 1,727 open issues and pull requests combined as of 2026-11-25, created 2026-01-22, pushed 2026-11-25.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=rtk-ai/rtk&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=rtk-ai/rtk&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=rtk-ai/rtk&type=date&legend=top-left" />
</picture>

v0.50.0 went stable on 2026-09-24 and v0.51.0 followed on 2026-10-02; v0.52.0 went stable on 2026-10-13 and **v1.0.0 shipped the same day**, with v1.0.1 on 2026-10-14, **v1.1.0 going stable on 2026-10-25** (opt-in fish-script hook wrapping, Angular build-table compaction, and a large correctness fix batch), and **v1.2.0 going stable on 2026-11-08** (directory-folded `git ls-tree` listings plus a large correctness batch across hooks, gain accounting, and the language runners), so the project is no longer pre-1.0; **v1.2.1 went stable on 2026-11-19**, hours after the previous day's verification fetch, with a large filter-correctness and proxy-stability batch (cargo toolchain and global-prefix filtering with narrowed prefix routing and exclusions, the repository's Copilot hook running without rtk installed, OpenCode binary resolution for GUI launches and PATH before RTK_BIN, bounded upstream requests with a Windows dead-proxy relaunch, the hook integrity check and compound user hook entries preserved, hex sha2 digests, versioned db schema migrations, and dotnet distinct test-project counting), and the candidate trains now read dev-1.3.0 (rc.672 and rc.673 on 2026-11-23, then rc.674 through rc.678 on 2026-11-24 to 11-25 carrying recall invocation accounting (#4541), the pnpm failure-output fix that drops only pnpm's update notifier (#4865), the passthrough tracking and tee-path fix (#3344), and pinned display of unparsed playwright, pnpm, and vitest runs) and dev-1.2.2 (rc.664 and rc.666 through rc.671, 2026-11-21 to 11-23), carrying the find exit-status baseline and combined-filters TOML fixes, the telemetry-marker ordering fix and the Windows git-help browser fix, the earlier golangci tokenizer-reuse, schema-enum, proxy-rule savings, and hook-ownership fixes, and the 2026-11-21 to 11-23 round on top: new first-class infra filters (`rtk terraform`, `rtk nix`, `rtk ansible-playbook`, and `rtk tofu` as a Terraform-equivalent, #769), the install script kept from crashing under Git Bash on Windows and run end to end in CI (#3700), an MSYS signal exit read as 128 plus the signal (#5183), Windows drive paths kept and tee recovery hints added in the grep filter (#5066), ANSI suppressed on Windows consoles without VT support (#5186), CRLF byte offsets preserved during JSON extraction (#3991), nix search output parsed with every result counted, images and PDFs kept off the delegate bulk-read shunt (#5122), and the gain console-mode block marked for semgrep (#5230).
The site claims 18,000+ developers, a marketing figure, and the Show HN thread shows users posting their own measured savings.

## Strengths

- The mechanism is concrete and auditable: per-command filtering strategies in a binary you can read, not a prompt trick.
- Lossiness is mitigated by design: tee-on-failure preserves full output, and per-command opt-outs exist.
- Broad agent coverage with graceful degradation and a clean uninstall path.
- The docs measure and publish the limits of the savings claims, which is rarer than the savings claims themselves.

## Cautions

- Lossy output is the product: an agent reading a condensed diff or collapsed test list can misread state, and the changelog shows a steady stream of filter-correctness bugs.
- The hook only rewrites Bash tool calls, so built-in Read/Grep/Glob tools bypass filtering entirely, and unmatched commands pass through at zero savings; one user's own log showed 39 percent on their busiest day.
- All savings numbers trace to the project or its users; no independent benchmark exists as of 2026-09-02.
- A crates.io name collision is documented in its own README, and the combined open issues and PRs total 1,564 as of 2026-10-18.

## Pricing

The CLI is free, Apache-2.0, no accounts.
RTK Pro adds secret masking (Shield), usage and cost observability, command policies, a shared skills catalogue, and sandboxed agent runs (beta) as a dedicated-tenant SaaS, self-hosted Helm chart, or on-prem deployment, with a 7-day trial.
**RTK Pro's prices are published now: the pricing page, observed live 2026-11-24, sells Dev at $6 per month (one seat, 5 endpoints per seat, 30 days of command retention), Teams at $20 per seat per month for 5 to 20 seats (25 endpoints per seat, 60 days of retention, RBAC, the audit log, MCP, Grafana, and a sandbox allowance), and Business at $30 per seat per month for 25 to 200 seats (50 endpoints per seat, 90 days of retention, unlimited export, and custom database connectors), with Enterprise (on-premise, custom limits, and an SLA) quoted by contact and a limited-time 2026 Black Friday banner offering 90 percent off.**

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-11-24 | Dev, Teams, Business | First published prices observed: Dev $6/month (1 seat), Teams $20/seat/month (5 to 20 seats), Business $30/seat/month (25 to 200 seats); Enterprise (on-premise, custom limits, SLA) quoted by contact. | [pro.rtk-ai.app/pricing](https://pro.rtk-ai.app/pricing) |

## Compared to

- [Repomix](../repomix/index.md): statically packs a whole repo for one prompt; rtk dynamically filters output during a live session, and the two are complementary.
- Plain CLI with no proxy: perfect fidelity and zero dependencies; choose it when exact output matters or your agent's built-in tools dominate, rtk when long sessions are dominated by noisy commands on metered APIs.
- [qmd](../qmd/index.md): compresses which context enters the window from your documents; rtk compresses what the shell sends back, so they compose.

## Bottom line

**Recommended for teams on metered APIs whose agent sessions are dominated by test, git, and search output, with `rtk gain` run for a week before believing any savings number.**
Not for sessions driven by built-in Read/Grep tools, or anyone whose agents cannot tolerate condensed failure output.

## Changes

- 2026-08-30 - Created in the owner-directed star sweep as a Context engines note.
- 2026-09-05 - Corrected a factually wrong caution, the combined issue backlog is about 2,100, not star-sized.
- 2026-09-16 - Refreshed the volatile numbers (80,635 stars, 1,626 open issues and PRs, pushed 2026-09-15) and noted the v0.50.0 release-candidate train; latest stable remains v0.49.0.
- 2026-09-18 - Refreshed the volatile numbers (80,868 stars, 1,641 open issues and PRs, pushed 2026-09-18); stable remains v0.49.0, with the v0.50.0 release-candidate train still running (rc.442).
- 2026-09-20 - Refreshed the volatile numbers (81,065 stars, 5,138 forks, 1,572 open issues and PRs as of 2026-09-20, pushed 2026-09-19); stable remains v0.49.0 with the candidate train at rc.444, and the combined backlog dropped about 70 over two days.
- 2026-09-25 - Recorded v0.50.0 going stable (2026-09-24), concluding the release-candidate train, and refreshed the volatile numbers (81,660 stars, 5,166 forks, 1,576 open issues and PRs, pushed 2026-09-24).
- 2026-09-26 - Recorded the follow-up 0.51.0 release-candidate train starting (rc.465 as of 2026-09-26) and refreshed the volatile numbers (81,734 stars, 5,179 forks, 1,591 open issues and PRs, pushed 2026-09-26).
- 2026-09-27 - Refreshed the volatile numbers (81,785 stars, 5,185 forks, 1,543 open issues and PRs); stable remains v0.50.0 with the 0.51.0 candidate train at rc.468.
- 2026-10-03 - Recorded v0.51.0 going stable (2026-10-02), the candidate train concluded, and refreshed the volatile numbers (82,266 stars, 5,223 forks, 1,579 open issues and PRs, pushed 2026-10-03); a 0.51.1 candidate train is already at rc.497.
- 2026-10-07 - Added the rtk-ai/rtk star history chart to the Status section.
- 2026-10-12 - Recorded the 0.51.1 candidate train concluding at rc.523 and the 0.52.0 train starting (rc.525), and refreshed the volatile numbers (83,002 stars, 1,500 open issues and PRs, pushed 2026-10-12); stable remains v0.51.0.
- 2026-10-16 - Recorded the 1.0 line: v0.52.0 stable on 2026-10-13, v1.0.0 the same day, v1.0.1 on 2026-10-14, and a dev-1.0.2 train at rc.549, retiring the pre-1.0 framing; volatile numbers refreshed (83,540 stars, 5,305 forks, 1,528 open issues and PRs, pushed 2026-10-15).
- 2026-10-24 - Full rotation re-verification: every cited URL re-fetched (README and its crates.io collision warning, the savings methodology, the release page, the marketing and Pro sites, and the HN thread all fetched 200 with their claims unchanged); stable remains v1.0.1 with a dev-1.1.0 candidate train at rc.573, and the volatile numbers refreshed (5,359 forks, 1,604 open issues and PRs, pushed 2026-10-23).
- 2026-10-26 - Recorded v1.1.0 going stable (2026-10-25: opt-in fish-script hook wrapping, Angular build-table compaction, a large correctness fix batch), concluding the dev-1.1.0 candidate train; latest stable moves from v1.0.1 to v1.1.0.
- 2026-11-01 - Recorded the dev-1.2.0 candidate train starting (rc.599 as of 2026-11-01; stable remains v1.1.0) and refreshed the volatile numbers (5,444 forks, 1,646 open issues and pull requests, pushed 2026-11-01).
- 2026-11-05 - Refreshed the volatile numbers (5,477 forks, 1,704 open issues and pull requests, pushed 2026-11-05); stable remains v1.1.0 with the dev-1.2.0 candidate train at rc.615.
- 2026-11-06 - Refreshed the volatile numbers (5,488 forks, 1,711 open issues and pull requests, pushed 2026-11-06); stable remains v1.1.0 with the dev-1.2.0 candidate train at rc.618.
- 2026-11-08 - Refreshed the volatile numbers (5,499 forks, 1,699 open issues and pull requests, pushed 2026-11-07); stable remains v1.1.0 with the dev-1.2.0 candidate train at rc.620.
- 2026-11-11 - Recorded v1.2.0 going stable (2026-11-08: directory-folded `git ls-tree` path listings, static musl Linux binaries, and a large correctness batch across hooks, gain accounting, cargo nextest, dotnet TRX reports, and the SQLFluff and ls filters), concluding the dev-1.2.0 candidate train; recorded the dev-1.2.1 candidate train starting (rc.628 as of 2026-11-10) and refreshed the volatile numbers (5,519 forks, 1,670 open issues and pull requests, pushed 2026-11-11); stable moves from v1.1.0 to v1.2.0.
- 2026-11-15 - Refreshed the volatile numbers (5,552 forks, 1,707 open issues and pull requests, pushed 2026-11-14); stable remains v1.2.0 with the dev-1.2.1 candidate train at rc.637.
- 2026-11-19 - Recorded the candidate train graduating to dev-1.3.0 (rc.641 through rc.645, 2026-11-17 to 11-18) carrying the new fix batch (golangci discover tokenizer reuse, schema-version enum, proxy-rule savings, hook-command ownership); stable remains v1.2.0; forks and open issues and pull requests refreshed (5,597 and 1,687).
- 2026-11-20 - Recorded v1.2.1 going stable (2026-11-19 17:49 UTC, after the 2026-11-19 run's fetch had recorded stable as v1.2.0: the cargo toolchain/global-prefix batch, the Copilot hook running without rtk installed, OpenCode binary resolution, bounded upstream requests with the Windows dead-proxy relaunch, hook integrity and compound-entry fixes, hex sha2 digests, versioned db migrations, dotnet test-project counting), the candidate trains splitting to dev-1.3.0 (rc.646 through rc.648) and dev-1.2.2 (rc.654 through rc.656), and refreshed the volatile numbers (5,611 forks, 1,692 open issues and pull requests, pushed 2026-11-20); stable moves from v1.2.0 to v1.2.1.
- 2026-11-21 - Recorded the dev-1.2.2 candidate train advancing to rc.657 through rc.662 (2026-11-20 to 11-21) carrying the post-v1.2.1 fixes (the telemetry marker written before the claimed ping, #4706, and the Windows git-help browser fuzz fix, #4784); stable remains v1.2.1; forks and open issues and pull requests refreshed (5,610 and 1,689).
- 2026-11-24 - Recorded the candidate trains advancing to dev-1.2.2 rc.664 and rc.666 through rc.671 and dev-1.3.0 rc.672 and rc.673 (2026-11-21 to 11-23) carrying the post-v1.2.1 round (first-class infra filters for terraform, nix, ansible-playbook, and tofu, the install script fixed and tested end to end under Git Bash on Windows, the MSYS signal exit code, Windows drive paths and tee hints in the grep filter, ANSI suppression on Windows consoles without VT support, CRLF byte offsets in JSON extraction, nix search output parsing, images and PDFs kept off the delegate bulk-read shunt, and the gain console-mode block marked for semgrep); stable remains v1.2.1; forks and open issues and pull requests refreshed (5,629 and 1,675).
- 2026-11-24 - Recorded RTK Pro's first published prices (the pricing page observed live: Dev $6/month for one seat, Teams $20 per seat per month for 5 to 20 seats, Business $30 per seat per month for 25 to 200 seats, Enterprise quoted by contact, with a limited-time 2026 Black Friday offer of 90 percent off), replacing the prices-not-published claim, restating the Pro feature list from the product page, and adding the Price history section seeded with the three plans.
- 2026-11-25 - Full rotation re-verification: every cited URL re-fetched and intact (the README and its name-collision warning, the savings methodology, the release feed, the marketing and Pro sites, the plans endpoint with Dev $6/month, Teams $20 per seat, and Business $30 per seat unchanged, and the HN thread); recorded the dev-1.3.0 candidate train advancing to rc.674 through rc.678 (2026-11-24 to 11-25) carrying recall invocation accounting, the pnpm failure-output fix, the passthrough tracking and tee-path fix, and pinned display of unparsed playwright, pnpm, and vitest runs; stable remains v1.2.1; forks and open issues and pull requests refreshed (5,633 and 1,727).

## See also

- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins
- [Repomix](../repomix/index.md) - the static-packing complement
- [Context Management Patterns](../../context-management-patterns/index.md) - the manual practices rtk automates
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - the per-token economics rtk attacks

## References

- https://github.com/rtk-ai/rtk - repository, supported commands, agent integrations, license
- https://raw.githubusercontent.com/rtk-ai/rtk/HEAD/README.md - the four filter strategies, 16 integrations, and the name-collision warning
- https://raw.githubusercontent.com/rtk-ai/rtk/develop/docs/guide/resources/savings-explained.md - the project's own methodology and the bytes-versus-bill caveat
- https://github.com/rtk-ai/rtk/releases - release cadence and the filter-correctness bug history (re-fetched through the API 2026-11-25: stable v1.2.1, candidate trains to dev-1.2.2 rc.671 and dev-1.3.0 rc.678)
- https://www.rtk-ai.app - the marketing claims this note discounts
- https://pro.rtk-ai.app - the Pro product surface and deployment models
- https://pro.rtk-ai.app/pricing - the RTK Pro pricing page (client-rendered; its plan cards load from the plans endpoint), titles and the limited-time Black Friday banner (fetched 2026-11-24)
- https://my.cloud.rtk-ai.app/api/plans - the plan data the pricing page renders: Dev $6/month, Teams $20 per seat for 5 to 20 seats, Business $30 per seat for 25 to 200 seats, Enterprise not self-serve (fetched 2026-11-24, re-fetched 2026-11-25 with the three prices unchanged)
- https://news.ycombinator.com/item?id=47189599 - the thread with naming criticism and early user-posted gain stats
