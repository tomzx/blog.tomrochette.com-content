---
title: Codeg
created: 2026-10-11
updated: 2026-11-14
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, surfaces, agentic-development-environments, open-source]
readability: 3
audience_notes: >
  Engineers running several coding-agent CLIs who want one workspace that keeps every session, searchable and resumable, regardless of which agent produced it.
  Assumes you know what ACP is and what an agent's local session history is.
---

Codeg is an Apache-2.0 multi-agent coding workspace, in Rust, that aggregates sessions from nineteen built-in agents plus any ACP agent into one searchable conversation layer, with a desktop app, a self-hosted server or Docker deployment, and native iOS and Android clients.

**Codeg's bet is that the session history your agents already write to disk is the durable asset, and that any surface which can import, search, resume, and hand those sessions between agents owns the workflow.**

## What it is

A workspace that renders every supported agent as the same structured conversation instead of a terminal: Claude Code, Codex, OpenCode, Pi, Grok Build, and fourteen more built in (nineteen total as of 2026-10-18), plus any ACP-speaking agent.
The session layer is the differentiator: Codeg imports, searches, and resumes the history each agent keeps on disk, and hands a session to a different agent to continue.
On top of that sit a main-agent delegation model (Claude Code calling Codex or Gemini as its own subagent session), Project Boot scaffolding, chat channels over Telegram, Lark (Feishu), and iLink (Weixin), office document work through a bundled officecli, research skills, and cron automations.
It is written in Rust, licensed Apache-2.0, and deployed as a desktop app, a self-hosted server, or Docker.

## Status

**Active on a fast release train.**
The repository was created 2026-02-09 and shows 3,980 stars and 517 forks as of 2026-10-16, with commits landing the same day.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=spacering-net/codeg&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=spacering-net/codeg&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=spacering-net/codeg&type=date&legend=top-left" />
</picture>

The train rolled into November with v0.44.0 (November 13, uncommitted task changes joining a task's PR or merge request with an editable commit message, more responsive streaming replies and long execution histories, built-in expert skills updated to Superpowers 7.0.2 and research skills to scientific-agent-skills 2.72.0, bundled-agent updates to CodeBuddy 2.184.0, Kimi Code 2.6.1, Qoder 1.1.88, and Antigravity 1.5.0, and a memory-retention fix for closed conversation tabs) above v0.43.0 (November 12, idle conversations moved between open folders in bulk with history kept, status-bar Web Service control with a local-connections-only option, and PR/MR lists with CI status, counts, and approval reminders) above v0.42.1 (November 6, related issues selected across pages and handled in one task with a single PR or merge request and a choice of which issues it closes, background work keeping running when you leave a conversation, Office preview improvements, and bundled-agent updates including Claude Code 2.1.318 with adapter 0.101.0) above v0.42.0 (November 3, CNB (cnb.cool) joining the supported code-hosting platforms with issue and merge-request management and task delivery through merge requests, global system-instruction editing for Claude Code, Codex, and OpenCode in agent settings, channel and webhook notifications filterable to top-level session completions, tasks awaiting permission or approval prioritizing Respond, and OpenCode's slash menu listing its loaded skills again), above the October train: v0.33.0 (October 2), v0.34.0 (October 7), v0.35.0 (October 10), v0.35.1 (October 11), and v0.35.2 (October 15, PDF files opening in a file tab, the repository panel turning issues and pull requests into to-dos on its own, taskbar and Dock attention flashes, token-cost estimation at API list prices, and bundled-agent version bumps), then v0.36.0 (October 16, Kiro CLI and ZCode as built-in agents, Assistants as ready-made delegation setups with their own agent and standing instructions that you @-mention, PlantUML blocks drawn as diagrams, and the side panel's tabs moved to a reorderable vertical rail), v0.37.0 (October 18, TRAE CLI and Command Code as built-in agents, Remote Control continuing a Claude Code session on your phone, Claude Code suggesting your next prompt, and the side panel gaining Automations, To-dos, and Issues-and-Pull-requests tabs), then v0.38.0 (October 18, codeg-cli, a command that runs agents through codeg from a terminal, a script, or a CI job and prints the reply as text or JSON while each run stays a conversation you can open and carry on in codeg), then v0.39.0 (October 21, agent-written commit messages, a Run on this computer switch that runs a command on your own machine even from a remote folder, codeg-server sign-in through a proxy such as Cloudflare Access, a Recent sidebar, and Windows and Linux AppImage update fixes), and v0.40.0 (October 24, an activity timeline presenting an agent's work step by step with step counts, elapsed time, and failures summarized, tool-permission decisions preserved with the conversation, and inline and side-by-side comparison of file edits inside conversations, with a database migration that stops 0.39.0 from starting on the updated data), then v0.41.1 (October 28, folder-following tabs with split layouts, HTML previews in replies, native MiniMax Code support, and OpenCode 2 integration), v0.41.2 (October 29, smoother streaming replies, collapsible background tasks, and Kimi Code and CodeBuddy reliability fixes), and v0.41.3 (October 30, a Claude Code thinking-summary switch, Codex follow-up prompt suggestions, and larger workspace backgrounds), then v0.41.4 (November 2, inline math rendered more reliably, the duplicated terminal output in remote workspaces fixed, a more readable execution timeline showing resumed delegations as rows, session renames through ZCode's /rename, an OpenCode compaction reserve settable as a share of the context window, and bundled-agent updates including OpenCode 2.2.5 and Kimi Code 2.4.1), and v0.43.0 (November 12, idle conversations not tied to a task moved between open folders individually or in bulk with history kept, status-bar control of the desktop Web Service with a connections-only-from-this-computer option, and PR/MR lists showing CI status with passing and total counts and approval reminders) as the latest.
An Algolia search of Hacker News returned no story about this project as of 2026-10-11, only substring matches on "codegen", so the footprint is GitHub-side.

## Strengths

- **Session portability is the mechanism nobody else ships: your agent history stops being a private format per tool and becomes one searchable, transferable corpus.**
- The surface list is the category's widest: desktop, self-hosted server, Docker, iOS, and Android, with the mobile clients open source alongside the app.
- ACP support means the built-in nineteen never become the ceiling.
- Apache-2.0 and self-hostable, so the aggregation layer stays on machines you control.

## Cautions

- **Zero independent coverage is the caution: no Hacker News story, no third-party review found this run, so the aggregate-and-hand-off claims rest on the project's own documentation.**
- The feature set stretches well past coding (office documents, research skills, chat channels), which is the general-workspace gravity this category keeps resisting, though coding sessions remain the core here.
- v0.x at a two-releases-per-week pace means churn is the maintenance plan.
- MCP appears in the README but has no dedicated documentation this run found, and AGENTS.md support is undocumented.

## Pricing

Free and open source under Apache-2.0; no paid tier exists.

## Compared to

- [OpenChamber](../openchamber/index.md): the OpenCode-only cockpit with fusion and cron; OpenChamber goes deep on one harness, Codeg goes wide across many.
- [Nimbalyst](../nimbalyst/index.md): the visual-editing workspace; Nimbalyst makes you a co-editor of the artifacts, Codeg makes you the operator of the sessions.
- [Cate](../cate/index.md): the canvas supervisor; Cate shows agent state in space, Codeg unifies agent state into one timeline.

## Bottom line

**Recommended for engineers whose agent history is scattered across three or more CLIs and who want it searchable and resumable in one self-hosted place.**
Not for anyone who needs an independently reviewed tool, a 1.0 release, or an editor-first experience.

## Changes

- 2026-10-11 - Created from the category entrant scan, admitted on its differentiated session-aggregation-and-handoff mechanism, with the zero-coverage caution recorded.
- 2026-10-11 - Added the star history chart.
- 2026-10-16 - Recorded v0.35.2 (October 15, in-tab PDFs, issues-and-PRs to-dos from the repository panel, attention flashes, and token-cost estimation) as the new latest release; counts refreshed.
- 2026-10-18 - Recorded v0.36.0 (October 16, Kiro CLI and ZCode built in, @-mentionable Assistants, PlantUML diagrams, the vertical side-panel rail) and v0.37.0 (October 18, TRAE CLI and Command Code built in, phone-side continuation of Claude Code sessions through Remote Control, next-prompt suggestions, and the Automations, To-dos, and Issues-and-PRs tabs) as the new latest releases, and corrected the built-in agent count to nineteen per the README, where the note carried fifteen.
- 2026-10-19 - Recorded v0.38.0 (October 18, codeg-cli running agents through codeg from a terminal, script, or CI job with text or JSON replies, each run staying a conversation openable in codeg) as the new latest release.
- 2026-10-22 - Recorded v0.39.0 (October 21, agent-written commit messages, the run-on-this-computer switch for remote-folder commands, codeg-server proxy sign-in behind Cloudflare Access, the Recent sidebar, and the Windows and AppImage update fixes) as the new latest release.
- 2026-10-25 - Recorded v0.40.0 (October 24, the step-by-step activity timeline with failure summaries, tool-permission decisions preserved with the conversation, and inline and side-by-side file-edit comparison in conversations, plus a one-way database migration against 0.39.0) as the new latest release.
- 2026-10-31 - Recorded the v0.41.1 through v0.41.3 wave (October 28 to 30, folder-following tabs with split layouts and HTML previews, native MiniMax Code support and OpenCode 2 integration, smoother streaming replies, a Claude Code thinking-summary switch, and Codex follow-up prompt suggestions) as the new latest releases.
- 2026-11-03 - Recorded v0.41.4 (November 2, inline math rendering, the duplicated remote-workspace terminal-output fix, the readable execution timeline with resumed delegations as rows, ZCode /rename session titles, the OpenCode compaction reserve as a context-window share, and bundled-agent updates) as the new latest release.
- 2026-11-04 - Recorded v0.42.0 (November 3, CNB (cnb.cool) as a supported code host with issue and merge-request management and task delivery through merge requests, global system-instruction editing for Claude Code, Codex, and OpenCode, notification filtering to top-level completions, and OpenCode's slash menu listing its skills again) as the new latest release.
- 2026-11-07 - Volatile re-verification on the released signal, recorded v0.42.1 (November 6, related issues across pages handled in one task, background work outliving the conversation view, Office preview improvements, and the Claude Code 2.1.318 bump) as the new latest release.
- 2026-11-13 - Volatile re-verification on the released signal, recorded v0.43.0 (November 12, idle conversations moved between open folders in bulk with history kept, status-bar Web Service control with a local-connections-only option, and PR/MR lists with CI status, counts, and approval reminders) as the new latest release.
- 2026-11-14 - Volatile re-verification on the released signal, recorded v0.44.0 (November 13, uncommitted task changes joining task PRs and merge requests, more responsive streaming and long histories, Superpowers 7.0.2 and scientific-agent-skills 2.72.0 skill updates, bundled-agent bumps, and a conversation-tab memory fix) as the new latest release; the Status release chain, which the November 13 pass had left starting at v0.42.1, brought current with v0.43.0's entry.

## See also

- [OpenChamber](../openchamber/index.md) - the single-harness incumbent this note joins as the many-harness aggregator
- [Nimbalyst](../nimbalyst/index.md) - the visual workspace neighbor, editor-first where Codeg is session-first
- [Cate](../cate/index.md) - the canvas supervisor over the same parallel-agent workload
- [ACP](../../protocols/acp/index.md) - the protocol that lets any agent join Codeg's fifteen built in

## References

- https://github.com/spacering-net/codeg - repository, README (fifteen built-in agents, structured conversation rendering, session import and handoff), Apache-2.0 license, 3,980 stars and 517 forks as of 2026-10-16
- https://api.github.com/repos/spacering-net/codeg - creation date 2026-02-09, language Rust, push date 2026-10-16, stars and forks as of 2026-10-16
- https://docs.codeg.app - the feature set: conversation aggregation, multi-agent delegation, project boot, chat channels over Telegram, Lark, and iLink, office documents, research skills, cron automations, and the open-source iOS and Android clients
- https://github.com/spacering-net/codeg/releases - v0.44.0 (2026-11-13, uncommitted task changes joining task PRs and merge requests, more responsive streaming and long histories, the Superpowers 7.0.2 and scientific-agent-skills 2.72.0 skill updates, bundled-agent bumps, and the conversation-tab memory fix) as the latest release, after v0.43.0 (2026-11-12, bulk idle-conversation moves, status-bar Web Service control, PR/MR lists with CI status), v0.42.1 (2026-11-06, related issues in one task, background work outliving the conversation view, Office previews, the Claude Code 2.1.318 bump) as the latest release, after v0.42.0 (2026-11-03, CNB and the global system-instruction editing), v0.41.4 (2026-11-02, inline math rendering, the duplicated remote-workspace terminal-output fix, the readable execution timeline, and bundled-agent updates), after v0.41.3 (2026-10-30, the Claude Code thinking-summary switch and Codex follow-up prompt suggestions), after v0.41.2 (October 29, streaming-reply smoothness) and v0.41.1 (October 28, folder-following tabs, HTML previews, MiniMax Code, OpenCode 2 integration), v0.40.0 (October 24, the activity timeline and the one-way database migration note), v0.39.0 (October 21), v0.38.0 (October 18, codeg-cli) with v0.37.0 (October 18) and v0.36.0 (October 16, Kiro CLI and ZCode, Assistants, the side-panel tabs), re-fetched 2026-11-14
- https://api.github.com/repos/spacering-net/codeg/releases - v0.39.0 (2026-10-21) and v0.38.0 (2026-10-18, codeg-cli) with their release notes, above v0.37.0 (2026-10-18) and v0.36.0 (2026-10-16, Kiro CLI and ZCode, Assistants, the side-panel tabs), re-fetched 2026-10-22
- https://api.github.com/repos/spacering-net/codeg/releases/tags/v0.39.0 - the October 21 release notes: agent-written commit messages, the Run on this computer switch, codeg-server proxy sign-in behind Cloudflare Access, the Recent sidebar, and the Windows and AppImage update fixes, fetched 2026-10-22
- https://api.github.com/repos/spacering-net/codeg/releases/tags/v0.44.0 - the November 13, 2026 release notes: uncommitted task changes included when creating or updating a PR/MR with a file list and editable commit message, more responsive streaming replies and long execution histories, expert skills updated to Superpowers 7.0.2 and research skills to scientific-agent-skills 2.72.0 (paper lookup across 18 sources), bundled-agent updates (CodeBuddy 2.184.0, Kimi Code 2.6.1, Qoder 1.1.88, Antigravity 1.5.0), and the memory-retention and GitLab image-preview fixes, fetched 2026-11-14
- https://api.github.com/repos/spacering-net/codeg/releases/tags/v0.43.0 - the November 12, 2026 release notes: idle conversations moved between open folders individually or in bulk, status-bar Web Service control with the local-connections-only option, and PR/MR lists with CI status, passing and total counts, and approval reminders, fetched 2026-11-13
- https://api.github.com/repos/spacering-net/codeg/releases/tags/v0.42.0 - the November 3, 2026 release notes: CNB (cnb.cool) support with issue and merge-request management, global system-instruction editing, notification filtering to top-level completions, the Respond prioritization, and the OpenCode skills-menu fix, fetched 2026-11-04
- https://raw.githubusercontent.com/spacering-net/codeg/main/README.md - nineteen agents built in with any ACP agent welcome, the sessions-that-travel pitch, and the platform list, fetched 2026-10-18
- https://hn.algolia.com/api/v1/search?query=codeg&tags=story - the search that found no story about this project (only codegen substring noise), the missing-footprint evidence, fetched 2026-10-11
