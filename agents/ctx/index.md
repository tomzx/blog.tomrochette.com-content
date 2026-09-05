---
title: "ctx"
created: 2026-09-05
updated: 2026-09-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, search, cli]
readability: 3
audience_notes: >
  Engineers who want their coding agents to recall what previous sessions actually did, without a lossy memory layer in between.
  Assumes you know what a session transcript, git blame, and token cost are.
---

**ctx is local search over the sessions your coding agents already recorded, and its pro add-on turns git blame around: from any line of code back to the transcript that produced it.**
Facts below verified as of 2026-09-05.

## What it is

An Apache-2.0 CLI (ctxrs/ctx, installable with one curl) that indexes past coding-agent sessions on your machine and searches messages and tool calls across agents and sessions, jumping from a result to the exact event or the full transcript.
It models the relationships between parent sessions, subagents, and forks, so an agent can recover a whole chain of work, and it positions itself explicitly against agent memory: no compaction step, just the real record.
The paid add-on, ctx pro, is "git blame, but for agent sessions": from a line, file, commit, or PR it surfaces the session that produced the code with citations back to the transcript and tool calls, and it states plainly that it cannot prove attribution for sessions not on your machine.

## Status

Active: created 2026-02-23, 1,077 stars and 69 forks, pushed the day of verification.
The docs site at ctx.rs is complete (concepts, supported agents including Claude Code, Codex, Cursor, Pi, OpenCode, and more, storage, comparisons, a changelog), and a `/ctx` skill lets agents call it directly.
**The community footprint is nearly empty, a 5-point, one-comment Show HN on 2026-09-03, which I read as the product being discovered through agents rather than through forums, and as thin independent verification.**

## Strengths

- The blame attribution is a genuinely new capability in this category: agentsview tells you what happened across sessions, ctx pro tells you which session is responsible for this line.
- The no-compaction stance is a real design difference from the Memory category: summaries go stale, transcripts do not.
- Cross-agent and cross-session search with subagent and fork awareness matches how people actually run two or three harnesses at once.

## Cautions

- The 50x token-efficiency claim is self-reported (917 versus 45,734 tokens in its own example), with no independent benchmark as of 2026-09-05.
- ctx pro's price is not published on the pages fetched this run, and the free/pro split means the headline capability is partially gated.
- It reads whatever the agents wrote: transcripts are only as complete as the harnesses' logs, and deleted local history is gone.

## Pricing

The core CLI is free and open source under Apache-2.0.
ctx pro is a paid add-on whose pricing was not extractable from ctx.rs as of 2026-09-05; a "For Teams" offering also exists.

## Compared to

- [agentsview](../agentsview/index.md): the category's first member, stronger on token-cost reporting and breadth of supported agents; ctx is stronger on attribution and agent-facing retrieval.
- [claude-mem](../claude-mem/index.md): the compress-and-reinject approach, which ctx explicitly frames itself against.
- [file-based-agent-memory](../file-based-agent-memory/index.md): memory as human-written markdown, the deliberate opposite of search over raw transcripts.

## Bottom line

Recommended for engineers running multiple agents who want past sessions as a queryable corpus and are willing to verify the efficiency claims on their own workload.
Not for anyone needing audited cost reporting (agentsview's job) or provenance guarantees beyond the local machine.

## See also

- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category this note extends to two columns
- [agentsview](../agentsview/index.md) - the retrospective archive ctx most directly complements
- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the compaction-based alternatives ctx argues against
- [Context Management Patterns](../context-management-patterns/index.md) - the token economics the efficiency claim targets

## References

- https://github.com/ctxrs/ctx - repository, license, install, and the no-compaction positioning
- https://ctx.rs - documentation: concepts, supported agents, storage, comparisons
- https://ctx.rs/pro - the blame-attribution add-on and its citation model
- https://hn.algolia.com/api/v1/items/49550141 - the Show HN launch thread, cited as the thin-footprint signal
- https://ctx.rs/comparisons - the project's own framing against agent memory and grep-based search
