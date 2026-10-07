---
title: "ctx"
created: 2026-09-05
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, search, cli]
readability: 3
audience_notes: >
  Engineers who want their coding agents to recall what previous sessions actually did, without a lossy memory layer in between.
  Assumes you know what a session transcript, git blame, and token cost are.
---

**ctx is local search over the sessions your coding agents already recorded, and its blame capability turns git blame around: from any line of code back to the transcript that produced it.**

## What it is

An Apache-2.0 CLI (ctxrs/ctx, installable with one curl) that indexes past coding-agent sessions on your machine and searches messages and tool calls across agents and sessions, jumping from a result to the exact event or the full transcript.
It models the relationships between parent sessions, subagents, and forks, so an agent can recover a whole chain of work, and it positions itself explicitly against agent memory: no compaction step, just the real record.
The blame capability, "git blame, but for agent sessions", maps a line, file, commit, or PR back to the session that produced the code with citations to the transcript and tool calls, and it states plainly that it cannot prove attribution for sessions not on your machine.
Through the v2.0 release of 2026-09-24, search, blame, a new local code graph, and a tool-output compaction command ship in one executable, where blame had previously been the paid pro add-on.
Search is BM25 by default with an opt-in semantic mode that embeds locally (the built-in model needs no API key), present in the CLI since the 1.2.x line of late August 2026, and the v2.2.0 release of 2026-09-30 added opt-in history backup plus beta sharing through a self-hosted server with collection permissions and revocable access.

## Status

Active: created 2026-02-23, about 1.1k stars (1,149) and 76 forks, pushed 2026-10-05, latest release v2.2.8 on 2026-10-05 (incremental-import and blame-worker fixes), after the v2.2.7 line of 2026-10-02 (incremental-import fixes, a day after v2.2.6 added `ctx import --all --incremental` for one-pass catch-up imports), after the v2.2.0 line of 2026-09-30 (opt-in history backup plus beta sharing through a self-hosted ctx server, with installer-recovery, history-import, and telemetry fixes through v2.2.5 on 2026-10-01), the v2.1.3 and v2.1.4 patches of 2026-09-29 and 2026-09-30, and the v2.1.0 line of 2026-09-28 (paged blame indexing that scales past 16,384 sources), as of 2026-10-06.

[![Star History Chart](https://api.star-history.com/chart?repos=ctxrs/ctx&type=date&legend=top-left)](https://www.star-history.com/?repos=ctxrs%2Fctx&type=date&legend=top-left)

The docs site at ctx.rs is complete (concepts, about 40 supported agent harnesses including Claude Code, Codex, Cursor, Pi, and OpenCode, storage, comparisons, a changelog), and a `/ctx` skill lets agents call it directly.
**The community footprint is nearly empty, a 5-point, one-comment Show HN on 2026-09-03 plus a 3-point re-launch on 2026-09-16, which I read as the product being discovered through agents rather than through forums, and as thin independent verification.**

## Strengths

- The blame attribution is a genuinely new capability in this category: agentsview tells you what happened across sessions, ctx tells you which session is responsible for this line.
- The no-compaction stance is a real design difference from the Memory category: summaries go stale, transcripts do not.
- Cross-agent and cross-session search with subagent and fork awareness matches how people actually run two or three harnesses at once.

## Cautions

- The 50x token-efficiency claim is self-reported (917 versus 45,734 tokens in its own example, still shown on the site's home page as of 2026-09-27), with no independent benchmark.
- The pro subscription that once gated blame disappeared from the site with 2.0, so the business model behind a formerly paid capability is now unstated.
- It reads whatever the agents wrote: transcripts are only as complete as the harnesses' logs, and deleted local history is gone.

## Pricing

The core CLI is free and open source under Apache-2.0.
ctx pro, the $20 USD per month add-on with a two-week trial recorded here through 2026-09-21, no longer appears anywhere on the site as of 2026-09-25: the docs now ship blame inside the single open-source executable, with no pricing page, trial, or "For Teams" listing remaining.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-18 | ctx pro | Baseline: core CLI free (Apache-2.0), pro add-on $20 USD/month with a two-week trial; a Teams offering also exists. | [ctx.rs/pro](https://ctx.rs/pro) |
| 2026-09-25 | ctx pro | Withdrawn: no pricing page or $20/month listing remains after v2.0.0 shipped Blame inside the single open-source executable; the site lists no paid tier. | [ctx.rs](https://ctx.rs), [v2.0.0 release notes](https://github.com/ctxrs/ctx/releases/tag/v2.0.0) |

## Compared to

- [agentsview](../agentsview/index.md): the category's first member, stronger on token-cost reporting and breadth of supported agents; ctx is stronger on attribution and agent-facing retrieval.
- [claude-mem](../../memory/claude-mem/index.md): the compress-and-reinject approach, which ctx explicitly frames itself against.
- [file-based-agent-memory](../../memory/file-based-agent-memory/index.md): memory as human-written markdown, the deliberate opposite of search over raw transcripts.

## Bottom line

Recommended for engineers running multiple agents who want past sessions as a queryable corpus and are willing to verify the efficiency claims on their own workload.
Not for anyone needing audited cost reporting (agentsview's job) or provenance guarantees beyond the local machine.

## Changes

- 2026-09-05 - Created from the entrant-resolution run, filling the session-analytics matrix's second column.
- 2026-09-06 - Recorded new pro pricing at $20/month with a 14-day trial.
- 2026-09-07 - Comparisons link replaced with the per-topic path after the old path began returning 404s.
- 2026-09-09 - Caution updated after comparison numbers moved from the comparisons page to the home page.
- 2026-09-12 - Recorded the new paid referral program.
- 2026-09-18 - Recorded the v1.4.10 release line (three releases on 2026-09-16), the 3-point re-launch thread of 2026-09-16, and the docs now listing about 40 supported agent harnesses.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-21 - Release line moved to v1.4.12 (two releases shipped 2026-09-20); pro pricing re-verified unchanged.
- 2026-09-25 - Release line moved to v2.0.1 (2026-09-24), which unified search, blame, a new code graph, and tool-output compaction in one executable, and the site stopped listing the ctx pro subscription entirely, so the Pricing section, its caution, and the Price history were revised.
- 2026-09-27 - Release line moved to v2.0.4 (2026-09-27, memory-use and active-session fixes), with v2.0.2 (2026-09-25) and a v1.6.4 maintenance release (2026-09-26) between; repository counts refreshed (1,132 to 1,135 stars) and the home-page efficiency claim re-verified unchanged.
- 2026-09-29 - Release line moved to v2.1.2: v2.1.0 (2026-09-28) added paged blame indexing beyond 16,384 sources, and v2.1.1 and v2.1.2 (2026-09-29) fixed sift-hook execution and history-index maintenance; repository counts refreshed (1,135 to 1,141 stars).
- 2026-10-02 - Release line moved to v2.2.5 (2026-10-01): v2.2.0 (2026-09-30) added opt-in history backup plus beta sharing through a self-hosted ctx server with collection permissions and revocable access, and v2.2.1 through v2.2.5 fixed installer recovery, history imports, and telemetry before restoring the skill's search-first guidance; repository counts refreshed (1,141 to 1,145 stars, 71 to 72 forks).
- 2026-10-03 - Release line moved to v2.2.7 (2026-10-02): v2.2.6 added `ctx import --all --incremental` for one-pass catch-up imports and v2.2.7 fixed incremental Codex-rollout imports and Sift output-hook telemetry; repository counts refreshed (1,145 to 1,147 stars).
- 2026-10-06 - Release line moved to v2.2.8 (2026-10-05, incremental-import and blame-worker fixes); repository counts refreshed (1,148 to 1,149 stars, 74 to 76 forks).
- 2026-10-07 - Added the ctxrs/ctx star history chart to the Status section.

## See also

- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category this note extends to two columns
- [agentsview](../agentsview/index.md) - the retrospective archive ctx most directly complements
- [Memory Feature Matrix](../../memory/memory-feature-matrix/index.md) - the compaction-based alternatives ctx argues against
- [Context Management Patterns](../../context-management-patterns/index.md) - the token economics the efficiency claim targets

## References

- https://github.com/ctxrs/ctx - repository, license, install, and the no-compaction positioning
- https://ctx.rs - documentation: concepts, supported agents, storage, comparisons, and the home page carrying the efficiency claim (no pricing listed as of 2026-09-25)
- https://ctx.rs/pro - now the blame documentation page; the former pro-pricing URL redirects into the docs
- https://hn.algolia.com/api/v1/items/49550141 - the Show HN launch thread, cited as the thin-footprint signal
- https://ctx.rs/comparisons/agent-memory - the project's own framing against agent memory, from the comparisons section that now splits per topic
- https://api.github.com/repos/ctxrs/ctx/releases - v2.2.8 published 2026-10-05, with v2.2.7 (2026-10-02), v2.2.6 (2026-10-02), the v2.2.5 release (2026-10-01), the v2.2.0 line (2026-09-30), and the v2.1.x patches between
- https://news.ycombinator.com/item?id=49727859 - the 3-point Show HN re-launch on 2026-09-16
