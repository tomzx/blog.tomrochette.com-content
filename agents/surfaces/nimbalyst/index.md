---
title: Nimbalyst
created: 2026-10-11
updated: 2026-10-18
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, surfaces, ai-editors, open-source]
readability: 3
audience_notes: >
  Engineers who want to read and edit what their coding agents produce, not just approve terminal diffs, and who work in documents and diagrams as much as code.
  Assumes you know what Claude Code, a worktree, and MCP are.
---

Nimbalyst is an MIT-licensed open-source desktop workspace where you and coding agents (Claude Code, Codex, OpenCode) edit the same markdown, diagrams, mockups, and code, with every agent change arriving as a reviewable red or green diff.

**Nimbalyst's bet is that agent work is mostly documents, and that a workspace where humans and agents co-edit the same files, with per-block diff approval, beats a terminal for anyone whose context lives in specs, diagrams, and trackers.**

## What it is

A visual workspace built around WYSIWYG editors for markdown, CSV, mockups, Monaco code, Excalidraw, data models, Mermaid, mind maps, and an embedded browser, nearly all of them implemented on the product's own extension SDK, and an extension can register an agent provider, which is how Gemini support arrives without a release.
Parallel agent sessions run with one-click worktree isolation, tracked on a session kanban linked to the files each session touched, and integrated task trackers sit in the same workspace for agents to read and update.
MCP servers connect with tool results rendered as widgets rather than raw JSON, content stays in plain files in your git repo, and an iOS companion handles approvals and replies on the go (Android in development).
The desktop and iOS apps are MIT and free for individuals on macOS, Windows, and Linux; the collaboration server is AGPL, with Teams multiplayer free during beta.
It is built by a four-person team and continues the lineage of Crystal, the orchestration member this section tracks as deprecated in Nimbalyst's favor.

## Status

**Active on a fast train, with a small independent footprint.**
The repository was created 2025-10-30 and shows 1,908 stars and 304 forks as of 2026-10-16, with v0.81.7 (October 16, Claude Code sessions suggesting your next prompt with Tab to fill, Claude Agent sessions auto-resuming when a usage limit resets, and new editor blocks: charts, callouts, columns, tabs, a table of contents, transclusions, @ mentions, and link previews) as the latest release after v0.81.6 (October 15, the wiki plugin telling the agent at session start which local wiki pages cover the code and which cover uncommitted changes, plus new wikiDoctor and listMarks tools) and the v0.81.4 and v0.81.5 pair of October 14 (local-wiki fixes and team moves, and interactive HTML pages embedded live in documents as a new wiki page type).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=nimbalyst/nimbalyst&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=nimbalyst/nimbalyst&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=nimbalyst/nimbalyst&type=date&legend=top-left" />
</picture>

The open-source launch was a self-submitted Show HN on 2026-04-30 that drew 8 points and 4 comments; six self-submitted threads going back to November 2025 peak at 29 points, and this run's search found no third-party coverage.

## Strengths

- **Per-block diff review inside the document is the mechanism the terminal cannot give you: you accept, reject, or edit each agent change in the rendered file where it lands.**
- The extension SDK is offered to your agents too: ask for an editor for a file type the product does not ship, and your agent writes, installs, and reloads it live.
- Plain files on disk in open formats, no proprietary store, and the git repo stays the source of truth.
- The iOS companion covers the waiting-on-you loop (approvals, replies, queued tasks) without a vendor cloud.

## Cautions

- **A year of work and six self-submitted threads have produced no third-party coverage, so the visual-workspace thesis is still unvalidated outside its own team.**
- Teams multiplayer is the revenue plan (AGPL server, paid plans promised), and it is free during beta, so the business side is unproven.
- Six releases in three days this week is the v0.x churn rate you are adopting.
- The SOC-2 claim on the teams page is vendor-stated and unaudited from where this section sits.

## Pricing

Free for individuals with no feature limits; Teams multiplayer is free during beta with paid plans planned, and no prices are stated yet.
Without stated prices there is no price history to track.

## Compared to

- [Cate](../cate/index.md): the canvas workspace; Cate is spatial supervision of terminals, Nimbalyst is document co-editing with the agent.
- [Whiteboard](../whiteboard/index.md): the review canvas where a finished agent draws its work; Whiteboard is harness-agnostic and built for reading, Nimbalyst is a full editor where both sides write.
- [Vibeyard](../vibeyard/index.md): the CLI cockpit with the task board; Vibeyard supervises the run, Nimbalyst edits the artifacts.

## Bottom line

**Recommended for engineers whose agent work is document-heavy (specs, diagrams, mockups, trackers) and who want per-block review instead of terminal approval.**
Not for terminal-first developers, and not for teams that need an independently validated collaboration product today.

## Changes

- 2026-10-11 - Created from the category entrant scan, admitted on its differentiated co-editing and per-block diff review, with the empty-footprint caution recorded.
- 2026-10-11 - Added the star history chart.
- 2026-10-13 - Recorded v0.81.1 (October 13, the nimbalyst-wiki plugin for the Codex CLI, wiki attachments, and usage-limit auto-resume for stopped Claude sessions) as the new latest release; counts refreshed.
- 2026-10-16 - Recorded the v0.81.4 and v0.81.5 pair of October 14 (local-wiki fixes, interactive HTML pages as a wiki page type) and v0.81.6 (October 15, wiki coverage context at session start, wikiDoctor and listMarks tools) as the new latest releases; counts refreshed.
- 2026-10-18 - Recorded v0.81.7 (October 16, next-prompt suggestions with Tab to fill, usage-limit auto-resume for Claude Agent sessions, and the new editor blocks from charts and callouts to columns, tabs, and link previews) as the new latest release.

## See also

- [Crystal](../../orchestration/crystal/index.md) - the deprecated predecessor this workspace continues
- [Cate](../cate/index.md) - the canvas neighbor supervising the same parallel sessions
- [Whiteboard](../whiteboard/index.md) - the review-side canvas that shares the visual-review thesis
- [Vibeyard](../vibeyard/index.md) - the board-first cockpit beside this editor-first workspace

## References

- https://github.com/nimbalyst/nimbalyst - repository, README (visual editors, per-block diffs, session kanban with worktree isolation, task tracking, MCP widgets, extension SDK, iOS companion), MIT license, 1,908 stars and 304 forks as of 2026-10-16
- https://api.github.com/repos/nimbalyst/nimbalyst - creation date 2025-10-30, language TypeScript, push date 2026-10-16, stars and forks as of 2026-10-16
- https://nimbalyst.com/ - the product site: the editor list, the extension-system description (agent-registered providers), Teams free during beta, and the platform list
- https://api.github.com/repos/nimbalyst/nimbalyst/releases - v0.81.7 (2026-10-16) as the latest release, after v0.81.6 (October 15), v0.81.5 and v0.81.4 (October 14), and v0.81.3 (October 14), re-fetched 2026-10-18
- https://hn.algolia.com/api/v1/search?query=nimbalyst&tags=story - the six self-submitted threads (best: 29 points December 2025; the 2026-04-30 open-source launch at 8 points), the empty-footprint evidence, fetched 2026-10-11
- https://docs.nimbalyst.com/ - the documentation index: the three modes (Files, Agent, Task), the MCP setup page, agent teams, worktrees, automations, and the Teams collaboration architecture (Cloudflare sync, per-team isolation), fetched 2026-10-11
