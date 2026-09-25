---
title: "ctx"
created: 2026-09-05
updated: 2026-09-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, search, cli]
readability: 3
audience_notes: >
  Engineers who want their coding agents to recall what previous sessions actually did, without a lossy memory layer in between.
  Assumes you know what a session transcript, git blame, and token cost are.
---

**ctx is local search over the sessions your coding agents already recorded, and its blame capability turns git blame around: from any line of code back to the transcript that produced it.**
Facts below verified as of 2026-09-25.

## What it is

An Apache-2.0 CLI (ctxrs/ctx, installable with one curl) that indexes past coding-agent sessions on your machine and searches messages and tool calls across agents and sessions, jumping from a result to the exact event or the full transcript.
It models the relationships between parent sessions, subagents, and forks, so an agent can recover a whole chain of work, and it positions itself explicitly against agent memory: no compaction step, just the real record.
The blame capability, "git blame, but for agent sessions", maps a line, file, commit, or PR back to the session that produced the code with citations to the transcript and tool calls, and it states plainly that it cannot prove attribution for sessions not on your machine.
Through the v2.0 release of 2026-09-24, search, blame, a new local code graph, and a tool-output compaction command ship in one executable, where blame had previously been the paid pro add-on.

## Status

Active: created 2026-02-23, about 1.1k stars (1,132) and 71 forks, latest release v2.0.1 on 2026-09-24, after v2.0.0 the same day and a v1.6.x line on 2026-09-22, as of 2026-09-25.
The docs site at ctx.rs is complete (concepts, about 40 supported agent harnesses including Claude Code, Codex, Cursor, Pi, and OpenCode, storage, comparisons, a changelog), and a `/ctx` skill lets agents call it directly.
**The community footprint is nearly empty, a 5-point, one-comment Show HN on 2026-09-03 plus a 3-point re-launch on 2026-09-16, which I read as the product being discovered through agents rather than through forums, and as thin independent verification.**

## Strengths

- The blame attribution is a genuinely new capability in this category: agentsview tells you what happened across sessions, ctx tells you which session is responsible for this line.
- The no-compaction stance is a real design difference from the Memory category: summaries go stale, transcripts do not.
- Cross-agent and cross-session search with subagent and fork awareness matches how people actually run two or three harnesses at once.

## Cautions

- The 50x token-efficiency claim is self-reported (917 versus 45,734 tokens in its own example, still shown on the site's home page as of 2026-09-25), with no independent benchmark.
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
- https://api.github.com/repos/ctxrs/ctx/releases - v2.0.1 published 2026-09-24, with v2.0.0 and the v1.6.x line the days before
- https://news.ycombinator.com/item?id=49727859 - the 3-point Show HN re-launch on 2026-09-16
