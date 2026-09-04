---
title: "Session Analytics Feature Matrix"
created: 2026-08-30
updated: 2026-09-02
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, session-analytics, observability, token-usage]
readability: 3
audience_notes: >
  Engineers choosing how to observe and audit their coding-agent sessions across tools.
  Assumes you know what a session transcript and token accounting are; each column links to a full note with sources.
---

This matrix compares the members of the Session analytics category: tools that turn what your coding agents already record into searchable history, cost reports, and audits.
The category is seeded with a single member, agentsview, so the matrix is one column and the scaffold the next member extends; the obvious candidates for the empty cells are live-session observers (hook-based dashboards such as agents-observe) and harness-native usage views, and the gaps are named in prose below until a note earns them a column.
Everything below was verified against live sources on 2026-09-04.

**The category question is retrospective archive versus live observation: agentsview answers what did my agents do and cost across every tool I run, and nobody in it yet answers what is my agent doing right now.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [agentsview](../agentsview/index.md) |
| --- | --- |
| Kind | local session indexer, web UI + CLI + desktop |
| Deployment | local daemon, Docker, optional PostgreSQL push for teams |
| Open source | ✓ MIT |
| Agents covered | ~55 sources auto-discovered (Claude Code, Codex, Gemini CLI, Copilot, Cursor, Zed, OpenCode, and more) |
| Token cost reporting | ✓ per-model pricing catalog, seconds over months of sessions |
| Search | ✓ FTS5 full text, semantic search opt-in |
| Live observation | ✗ retrospective only, parses files already written |
| Team features | ✓ PostgreSQL push, machine-labeled sync, S3 roots, versioned exports |
| Privacy posture | local-first, one anonymous ping by default, disableable |
| Pricing | free, MIT, no accounts |

## Reading the matrix

**The empty cells are the thesis: the live-observation row is where the category is incomplete, because hook-based dashboards exist but have not yet earned notes under the citation standard.**
agentsview deliberately refuses live observation, which keeps it a passive reader of files your agents already wrote and keeps its privacy posture clean.

**Token cost reporting is the row that pays for the tool**: harness-native cost views reset and see only their own sessions, while a pre-indexed store answers multi-tool, multi-month questions in seconds.
The project's own benchmark claims 84 to 223 times faster reports than ad-hoc parsing, with the docs calling that an upper bound, so treat it as directional.

**Breadth of coverage is the moat**: roughly 55 supported sources against a field of single-agent tools, which matters because most practitioners now run two or three harnesses at once.

## Choosing from the matrix

- Running three or more different coding agents and wanting one private history and cost view: agentsview.
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
- https://code.claude.com/docs/en/costs - the harness-native cost views that define the category's baseline
