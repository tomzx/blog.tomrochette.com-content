---
title: claude-devtools
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, observability, claude-code, open-source]
readability: 3
audience_notes: >
  Engineers who want to see everything a Claude Code session actually did, from token sources to tool payloads, after the fact.
  Assumes you know what ~/.claude stores and what a context window is.
---

claude-devtools is an MIT-licensed desktop app that reads the Claude Code session logs already on your machine and reconstructs what the terminal hid: full tool payloads, per-turn token attribution, subagent trees, and compaction history.

**claude-devtools exists because Claude Code v2.1.20 replaced detailed terminal output with summaries, and it is this category's deepest single-harness answer: where agentsview indexes many agents shallowly, claude-devtools reconstructs one agent completely.**

## What it is

A desktop application (macOS, Linux, and Windows; Homebrew, direct download, or Docker on localhost:3456) that parses the session transcripts under ~/.claude in place, with zero configuration and no API keys.
Its headline feature is context reconstruction: per-turn token attribution across seven categories (CLAUDE.md at global, project, and directory levels, skills, @-mentioned files, tool input and output, thinking, team overhead, and user text) with compaction visualization.
Every tool call expands to a specialized viewer (syntax-highlighted Reads, inline Edit diffs, Bash output), subagent activity renders as full execution trees with tokens, duration, and cost, and sessions export to Markdown, JSON, or plain text.
A command palette gives cross-session search with multi-pane side-by-side sessions, SSH support inspects sessions on remote machines, and notification triggers watch for .env access, tool errors, or high token use.
Made by matt1398, MIT-licensed, with docs at claude-dev.tools.

## Status

Young: 3,960 stars, 305 forks, 53 open issues, created 2026-02-07, pushed 2026-09-26, as of 2026-10-06.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=matt1398/claude-devtools&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=matt1398/claude-devtools&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=matt1398/claude-devtools&type=date&legend=top-left" />
</picture>

Its Show HN reached 69 points on 2026-02-13, two days after the 1,085-point "Claude Code is being dumbed down?" thread that motivated it.
The release line has been quiet since v0.5.0 on 2026-05-13 while the default branch kept receiving commits, so read the commit log rather than the releases page for current state.
**The deepest tool in the category for one harness, born from a specific grievance, and still pre-1.0 with a stalled release cadence.**

## Strengths

- The per-turn seven-category token attribution is unique here: it answers what is in the context window and why, not just how many tokens a session burned.
- Full tool-payload reconstruction is the same transparency promise agents-observe makes live, delivered retrospectively with no hooks, no server, and no install in the agent's path.
- Subagent trees with per-agent tokens, duration, and cost make multi-agent runs legible in one harness.
- It works against sessions you already have, including server-side logs through the Docker deployment.

## Cautions

- Claude Code only: every other retrospective member of this category parses several formats, and if your sessions live in Codex or OpenCode this tool cannot see them.
- Releases stopped at v0.5.0 in May 2026 while development continued on the default branch, so packaged builds lag the code you would actually run.
- Token attribution is the tool's own reconstruction from transcripts, so it inherits every gap in what Claude Code wrote (the same undercount class agentsview documents).
- The grievance it was built against, summarized terminal output, is harness behavior that can change in any release, so its core value tracks Claude Code's interface decisions.

## Pricing

Free and open source under MIT; the website's own structured data lists the offer at $0.
No paid tiers are published.

## Compared to

- [agents-observe](../agents-observe/index.md): the live half of the same promise for Claude Code, via hooks and a dashboard; claude-devtools is retrospective with deeper reconstruction.
- [AgentTrace](../agenttrace/index.md): the multi-harness TUI audit of cost, latency, and health; claude-devtools goes deeper on one harness.
- [agentsview](../agentsview/index.md): the breadth play, indexing 60-plus formats for history and cost; the deep view feeds the archive.

## Bottom line

**Recommended for Claude Code users who want to audit what a session actually did, token source by token source, after the fact.**
Not for multi-harness coverage, live observation, or anyone who needs a maintained release channel.

## Changes

- 2026-10-06 - Created from the 2026-10-06 entrant scan: the deepest single-harness session inspector in the category, born from the v2.1.20 dumbing-down backlash, with seven fetched sources.
- 2026-10-07 - Added the matt1398/claude-devtools star history chart to the Status section.

## See also

- [agents-observe](../agents-observe/index.md) - the live counterpart for the same harness
- [AgentTrace](../agenttrace/index.md) - the multi-harness audit sibling
- [agentsview](../agentsview/index.md) - the breadth alternative for history and cost
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins
- [Claude Code](../../harnesses/claude-code/index.md) - the harness whose logs it reconstructs

## References

- https://github.com/matt1398/claude-devtools - repository, 3,960 stars and 305 forks as of 2026-10-06, MIT license, created 2026-02-07
- https://raw.githubusercontent.com/matt1398/claude-devtools/main/README.md - the feature set, install paths, and the v2.1.20 grievance framing
- https://claude-dev.tools - the docs site, whose structured data lists a $0 offer
- https://api.github.com/repos/matt1398/claude-devtools/releases - v0.5.0 (2026-05-13) as the newest tagged release, the quiet release line
- https://hn.algolia.com/api/v1/items/47004712 - the 69-point Show HN of 2026-02-13
- https://hn.algolia.com/api/v1/items/46978710 - the 1,085-point "Claude Code is being dumbed down?" thread the tool answers
- https://symmetrybreak.ing/blog/claude-code-is-being-dumbed-down/ - the blog post that started the backlash
