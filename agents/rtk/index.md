---
title: rtk
created: 2026-08-30
updated: 2026-09-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, token-efficiency, cli, open-source]
readability: 3
audience_notes: >
  Engineers paying per-token for coding agents whose sessions are dominated by noisy command output.
  Assumes you know what a pre-tool-use hook and a context window are.
---

rtk is a free, open-source Rust CLI proxy that intercepts shell commands run by coding agents and compresses their output before it enters the context window, claiming up to 90 percent fewer output bytes on supported commands.
Facts below verified as of 2026-09-05.

**rtk monetizes the least glamorous line in the agent budget, the command output nobody reads, and its own documentation admits the 90 percent headline is an output-bytes number, not a bill reduction.**
That admission is why I trust the project and discount the marketing at the same time.

## What it is

A single dependency-free Rust binary that sits between the agent and the shell: a pre-tool-use hook (or rules file) rewrites commands like `git status` to `rtk git status`, and rtk returns a filtered, grouped, truncated, and deduplicated version, with under 10 milliseconds of claimed overhead.
Coverage is per-command strategy: git status/diff/log, grep and ripgrep, find, test runners (pytest, cargo test, jest, vitest, playwright), linters and typecheckers, package managers, docker and kubectl, AWS CLI, and generic wrappers for anything else; git push becomes one line.
Full raw output is tee'd to disk when a filtered command fails, `rtk proxy` gives raw passthrough, and `rtk gain` reports measured savings.
Hooks ship for 16 tools including Claude Code, Codex, OpenCode, Cursor, Gemini CLI, Copilot, Windsurf, and Cline.
Apache-2.0, built by a small French team with a commercial Pro product alongside.

## Status

Young and hot: 78,619 stars, 4,966 forks, 1,053 open issues and 1,035 open PRs as of 2026-09-05, created 2026-01-22, pushed the day of verification.
Latest stable is v0.48.0 (2026-09-04) with near-daily release candidates; the project is pre-1.0.
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
- A crates.io name collision is documented in its own README, and the combined open issues and PRs total around 2,100 as of 2026-09-05.

## Pricing

The CLI is free, Apache-2.0, no accounts.
RTK Pro adds secret detection, org policies, observability, and sandboxed environments as a dedicated-tenant SaaS, self-hosted Helm chart, or on-prem deployment, with a 7-day trial; public per-seat prices are not published.

## Compared to

- [Repomix](../repomix/index.md): statically packs a whole repo for one prompt; rtk dynamically filters output during a live session, and the two are complementary.
- Plain CLI with no proxy: perfect fidelity and zero dependencies; choose it when exact output matters or your agent's built-in tools dominate, rtk when long sessions are dominated by noisy commands on metered APIs.
- [qmd](../qmd/index.md): compresses which context enters the window from your documents; rtk compresses what the shell sends back, so they compose.

## Bottom line

**Recommended for teams on metered APIs whose agent sessions are dominated by test, git, and search output, with `rtk gain` run for a week before believing any savings number.**
Not for sessions driven by built-in Read/Grep tools, or anyone whose agents cannot tolerate condensed failure output.

## See also

- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins
- [Repomix](../repomix/index.md) - the static-packing complement
- [Context Management Patterns](../context-management-patterns/index.md) - the manual practices rtk automates
- [Model Selection for Coding Tasks](../model-selection-for-coding-tasks/index.md) - the per-token economics rtk attacks

## References

- https://github.com/rtk-ai/rtk - repository, supported commands, agent integrations, license
- https://raw.githubusercontent.com/rtk-ai/rtk/HEAD/README.md - the four filter strategies, 16 integrations, and the name-collision warning
- https://raw.githubusercontent.com/rtk-ai/rtk/develop/docs/guide/resources/savings-explained.md - the project's own methodology and the bytes-versus-bill caveat
- https://github.com/rtk-ai/rtk/releases - release cadence and the filter-correctness bug history
- https://www.rtk-ai.app - the marketing claims this note discounts
- https://pro.rtk-ai.app - the Pro product surface and deployment models
- https://news.ycombinator.com/item?id=47189599 - the thread with naming criticism and early user-posted gain stats
