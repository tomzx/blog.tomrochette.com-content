---
title: "Session Analytics Feature Matrix"
created: 2026-08-30
updated: 2026-09-20
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, session-analytics, observability, token-usage]
readability: 3
audience_notes: >
  Engineers choosing how to observe and audit their coding-agent sessions across tools.
  Assumes you know what a session transcript and token accounting are; each column links to a full note with sources.
---

This matrix compares the four members of the Session analytics category: tools that turn what your coding agents record (or are recording right now) into live views, searchable history, cost reports, and audits.
The category now covers both halves of the job: agents-observe, the live hook-fed dashboard, agentsview, the broad retrospective archive, ctx, the search-and-attribution CLI, and Memex, the search-and-resume TUI.
Everything below was verified against live sources on 2026-09-21.

**The category's founding question, retrospective archive versus live observation, now has both answers plus a closing move: agentsview indexes what every agent already did and cost across 60-plus formats, ctx answers where did this line of code come from, agents-observe answers what is my agent doing right now (though only for Claude Code and Codex), and Memex answers where did I already do this, then drops you back into the session that did it.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [agents-observe](../agents-observe/index.md) | [agentsview](../agentsview/index.md) | [ctx](../ctx/index.md) | [Memex](../memex/index.md) |
| --- | --- | --- | --- | --- |
| Kind | real-time observability dashboard for live and replayed sessions | local session indexer, web UI + CLI + desktop | local session search CLI with a paid blame-attribution add-on | local session search CLI and TUI with resume-in-place and an MCP server |
| Deployment | Claude Code plugin, hooks feeding a Dockerized local API server, dashboard on localhost:4981 | local daemon, Docker, optional PostgreSQL push for teams | single-binary CLI install, agent-callable skill | single-binary CLI install (brew, AUR, Nix, cargo-binstall), TUI, local web UI, native desktop apps, MCP server |
| Open source | ✓ MIT | ✓ MIT | ✓ Apache-2.0 core, pro add-on paid | ✓ MIT |
| Agents covered | ~ Claude Code and Codex, with the plugin install Claude Code-native | 60+ formats auto-discovered (Claude Code, Codex, Gemini CLI, Copilot, Cursor, Zed, OpenCode, and more) | ~ about 40 agent harnesses documented (Claude Code, Codex, Cursor, Pi, OpenCode, and more) | ~ 15 engines graded per capability (Claude Code, Codex, Cursor, OpenCode, Pi, GitHub Copilot CLI, Grok, Antigravity, and more), support uneven |
| Token cost reporting | ✓ per-session token usage and cost breakdowns (since v0.9.7) | ✓ per-model pricing catalog, seconds over months of sessions | ✗ | ~ per-engine token usage, off by default |
| Search | ✓ filtering and search across live and stored events | ✓ FTS5 full text, semantic search opt-in | ✓ cross-agent message and tool-call search, subagent and fork aware | ✓ BM25 default, optional local embeddings for semantic and hybrid queries, saved memories searchable, SSH federation |
| Provenance | ✗ | ✗ | ✓ ctx pro maps a line, file, commit, or PR to the session that produced it | ✗ |
| Live observation | ✓ hook events stream to the dashboard over websockets as agents run | ✗ retrospective only, parses files already written | ✗ retrospective only | ✗ retrospective only |
| Team features | ✗ single-user local setup | ✓ PostgreSQL push, machine-labeled sync, S3 roots, versioned exports | a "For Teams" offering exists, details unpublished | ✗ single-user, SSH federation to your own machines, object-storage sync announced |
| Privacy posture | local-first, events stay in a local SQLite store behind a local Docker server | local-first, one anonymous ping by default, disableable | local-first, attribution refuses data not on the machine | local-first, no cloud service in the default path, embeddings run locally |
| Pricing | free, MIT, no paid tiers published | free, MIT, no accounts | free core, ctx pro paid at $20 USD/month, 14-day trial | free, MIT, no paid tier published |

## Reading the matrix

**The live-observation row is the row this matrix existed to name, and agents-observe now fills it**: hook events stream into its dashboard while the agents run, which neither retrospective tool can do, though the cell covers only Claude Code and Codex today, so the remaining empty cells belong to the harnesses it does not hook.
The second row worth reading is provenance: ctx pro's blame attribution is the only cell in the category that answers "which session wrote this", which agentsview deliberately leaves to cost and history questions.

**Token cost reporting is the row that pays for the tool**: harness-native cost views reset and see only their own sessions, while a pre-indexed store answers multi-tool, multi-month questions in seconds.
An earlier version of the agentsview docs benchmarked its reports at 84 to 223 times faster than ad-hoc parsing (calling that an upper bound); the current docs have dropped that benchmark entirely, so the row should be read as "fast because pre-indexed", with no vendor number left to lean on.
The docs' usage JSON contract and the session-export schema both sit at schema version 6, so scripts consuming those reports should expect breaking churn.

**Memex adds the closing move the other archive tools lack: resume-in-place, where finding a session and re-entering it are one action in the TUI, plus the category's only local semantic search (BM25 by default, optional local embeddings, so the headline requires opt-in setup).**
Its 15-engine support table is graded per capability and unevenly at that (some engines have no resume at all, token counting is missing for at least one), and its launch footprint is as thin as ctx's was, so read the column as promising and unproven.

**Breadth of coverage is agentsview's moat**: roughly 60 supported sources against ctx's 40, Memex's 15, and agents-observe's two, which matters because most practitioners now run two or three harnesses at once.
ctx's moat is different: agent-facing retrieval, where the consumer of the search is your next session rather than you.

## Choosing from the matrix

- Running three or more different coding agents and wanting one private history and cost view: agentsview.
- Wanting your agents to recall why code exists, from the session that wrote it: ctx, with its pro gating and self-reported numbers accepted.
- Living in the terminal and wanting semantic recall plus one action back into the session: Memex, accepting 222 stars and thin verification.
- Needing to see what an agent is doing right now: agents-observe, if your agents are Claude Code or Codex; otherwise a harness-native view is still the fallback.
- Single-agent users: your harness's built-in usage views are probably enough.

## Changes

- 2026-08-30 - Created as the Session analytics category's companion matrix, a single-column scaffold with the live-observation gap named in prose.
- 2026-09-05 - Extended from one to two columns with ctx.
- 2026-09-06 - Updated the ctx cell for its published pro pricing.
- 2026-09-08 - Dropped the agentsview benchmark claim from the prose after the tool's docs removed it entirely.
- 2026-09-13 - Added the agentsview usage-output schema version 6 churn note to the reading prose.
- 2026-09-16 - Extended to three columns with agents-observe, filling the live-observation gap the prose used to name.
- 2026-09-18 - ctx agents-covered cell updated after the docs began listing about 40 supported agent harnesses.
- 2026-09-20 - Extended from three to four columns with Memex, inserted last alphabetically, every row gaining a cell traced to the new note, with the reading and choosing prose extended.
- 2026-09-20 - Corrected the schema caution in the reading prose: the docs' usage JSON contract is at schema version 5, version 6 is the session-export schema.

## See also

- [Executions Feature Matrix](../../executions/executions-feature-matrix/index.md) - the trigger-and-run layer whose runs these tools observe
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - the per-token economics these reports feed
- [Context Management Patterns](../../context-management-patterns/index.md) - the context costs the token reports make visible

## References

- https://github.com/kenn-io/agentsview - the repository, supported agents, architecture, and license for the agentsview column
- https://www.agentsview.io/docs/token-usage/ - the cost computation, benchmark caveats, and undercount disclosures
- https://www.agentsview.io - the deployment surfaces and team features
- https://github.com/ctxrs/ctx - the ctx column: repository, license, and no-compaction positioning
- https://ctx.rs/pro - the ctx column: blame attribution and its citation model
- https://code.claude.com/docs/en/costs - the harness-native cost views that define the category's baseline
- https://github.com/simple10/agents-observe - the agents-observe column: repository, license, and adoption numbers
- https://raw.githubusercontent.com/simple10/agents-observe/main/README.md - the agents-observe column: plugin install, Docker server, websockets dashboard, and token and cost breakdowns
- https://news.ycombinator.com/item?id=47602986 - the agents-observe launch thread behind the live-observation claim's community context
- https://github.com/nicosuave/memex - the Memex column: repository, surfaces, engine support table, and license
- https://raw.githubusercontent.com/nicosuave/memex/main/README.md - the Memex column: BM25 and local-embedding search, resume-in-place, MCP server, and install paths
