---
title: "Session Analytics Feature Matrix"
created: 2026-08-30
updated: 2026-09-05
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, session-analytics, observability, token-usage]
readability: 3
audience_notes: >
  Engineers choosing how to observe and audit their coding-agent sessions across tools.
  Assumes you know what a session transcript and token accounting are; each column links to a full note with sources.
---

This matrix compares the members of the Session analytics category: tools that turn what your coding agents already record into searchable history, cost reports, and audits.
The category now has two members: agentsview, the broad retrospective archive, and ctx, the search-and-attribution CLI; the live-observation cells remain empty, and the gap is named in prose below until a note earns them a column.
Everything below was verified against live sources on 2026-09-05.

**The category question is still retrospective archive versus live observation: agentsview answers what did my agents do and cost across every tool I run, ctx answers where did this line of code come from, and nobody in the category yet answers what is my agent doing right now.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [agentsview](../agentsview/index.md) | [ctx](../ctx/index.md) |
| --- | --- | --- |
| Kind | local session indexer, web UI + CLI + desktop | local session search CLI with a paid blame-attribution add-on |
| Deployment | local daemon, Docker, optional PostgreSQL push for teams | single-binary CLI install, agent-callable skill |
| Open source | ✓ MIT | ✓ Apache-2.0 core, pro add-on paid |
| Agents covered | ~60 sources auto-discovered (Claude Code, Codex, Gemini CLI, Copilot, Cursor, Zed, OpenCode, and more) | ~ major agents documented (Claude Code, Codex, Cursor, Pi, OpenCode, and more), full count unstated |
| Token cost reporting | ✓ per-model pricing catalog, seconds over months of sessions | ✗ |
| Search | ✓ FTS5 full text, semantic search opt-in | ✓ cross-agent message and tool-call search, subagent and fork aware |
| Provenance | ✗ | ✓ ctx pro maps a line, file, commit, or PR to the session that produced it |
| Live observation | ✗ retrospective only, parses files already written | ✗ retrospective only |
| Team features | ✓ PostgreSQL push, machine-labeled sync, S3 roots, versioned exports | a "For Teams" offering exists, details unpublished |
| Privacy posture | local-first, one anonymous ping by default, disableable | local-first, attribution refuses data not on the machine |
| Pricing | free, MIT, no accounts | free core, ctx pro paid, price unpublished as of 2026-09-05 |

## Reading the matrix

**The live-observation row is still where the category is incomplete**: both members are retrospective readers of files agents already wrote, and the hook-based dashboards that would fill the empty cells have not yet earned notes under the citation standard.
The second row worth reading is provenance: ctx pro's blame attribution is the only cell in the category that answers "which session wrote this", which agentsview deliberately leaves to cost and history questions.

**Token cost reporting is the row that pays for the tool**: harness-native cost views reset and see only their own sessions, while a pre-indexed store answers multi-tool, multi-month questions in seconds.
The project's own benchmark claims 84 to 223 times faster reports than ad-hoc parsing, with the docs calling that an upper bound, so treat it as directional.

**Breadth of coverage is agentsview's moat**: roughly 60 supported sources against a field of single-agent tools, which matters because most practitioners now run two or three harnesses at once.
ctx's moat is different: agent-facing retrieval, where the consumer of the search is your next session rather than you.

## Choosing from the matrix

- Running three or more different coding agents and wanting one private history and cost view: agentsview.
- Wanting your agents to recall why code exists, from the session that wrote it: ctx, with its pro gating and self-reported numbers accepted.
- Needing to see what an agent is doing right now: not this category yet; use a harness-native view or watch for a live-observation note.
- Single-agent users: your harness's built-in usage views are probably enough.

## See also

- [Executions Feature Matrix](../executions-feature-matrix/index.md) - the trigger-and-run layer whose runs these tools observe
- [Model Selection for Coding Tasks](../model-selection-for-coding-tasks/index.md) - the per-token economics these reports feed
- [Context Management Patterns](../context-management-patterns/index.md) - the context costs the token reports make visible

## References

- https://github.com/kenn-io/agentsview - the repository, supported agents, architecture, and license for the agentsview column
- https://agentsview.io/token-usage/ - the cost computation, benchmark caveats, and undercount disclosures
- https://agentsview.io - the deployment surfaces and team features
- https://github.com/ctxrs/ctx - the ctx column: repository, license, and no-compaction positioning
- https://ctx.rs/pro - the ctx column: blame attribution and its citation model
- https://code.claude.com/docs/en/costs - the harness-native cost views that define the category's baseline
