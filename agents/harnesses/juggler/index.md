---
title: Juggler
created: 2026-08-30
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agents, harnesses, gui, go]
readability: 3
audience_notes: >
  Engineers who want a graphical, inspectable surface for a coding agent instead of a
  terminal TUI, and who care about branching conversations and session durability.
  Assumes you know what a harness, BYOK, and AGPL mean.
---

Juggler is a free, open-source desktop GUI coding agent built by the developer behind JUCE, giving you a visual workbench where conversations branch into trees and every tool call and raw context message is inspectable.

**Juggler is the strongest argument that the terminal is the wrong native surface for agent work: its whole bet is that reading diffs, editing multi-line prompts, and absorbing tool output are GUI problems.**

## What it is

A single Go binary with a native desktop app (Wails, no Electron or Node) that runs its own agent loop against the usual providers: Claude Code CLI or API, OpenAI/Codex, GitHub Copilot, Gemini, Mistral, Z.ai, Ollama, OpenRouter, DeepSeek, with your subscription or API keys.
Conversations are trees, not log files: any point can branch into a sub-thread recursively, with undo/redo, duplication, and backtracking.
Everything is inspectable, including tool calls, approvals, item properties, and the raw context JSON.
Sessions live in a database rather than memory, so they survive quits, crashes, and reconnects, and multiple clients (desktop plus browsers, local or remote headless) can view the same live session.
Made by Julian Storer (JUCE, Tracktion, Cmajor), distributed as signed installers for macOS, Windows, and Linux.

## Status

**Young, active, and single-maintainer, with a strong launch.**
The public Show HN on July 12, 2026 drew 280 points and 119 comments ([HN](https://news.ycombinator.com/item?id=48883305)).
751 stars and 51 forks as of 2026-10-04 on a repo created June 19, 2026 (GitHub API); it had crossed 732 by October 3, over a hundred stars more than the day before, and stood at 768 stars and 52 forks as of 2026-10-06.

<a href="https://www.star-history.com/?repos=juggler-ai%2Fjuggler&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=juggler-ai/juggler&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=juggler-ai/juggler&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=juggler-ai/juggler&type=date&legend=top-left" />
 </picture>
</a>

Shipping is steady: v0.7.4 published October 2, 2026, adding per-provider toggles for Codex and Copilot subscriptions, thinking levels for Ollama models, a file viewer that plays video and audio and opens more image formats, and a fix for slow-starting WSL sessions on Windows; v0.7.3 (September 30) added a "Group" workspace type that organizes conversations without a worktree or copy, usage meters that redden by pace against the window rather than by quota consumed, touch-device fixes, and an LM Studio provider that reads each model's loaded context window.
One person builds it, which is both the reason it ships fast and the project's single point of failure.

## Strengths

- **Conversation-as-tree is a real interaction model, not a gimmick**: branching sub-threads let you backtrack a decision without losing the rest of the session, which terminal scrollback cannot do.
- Session durability across devices: a paused approval survives a crash and reopens on another machine, which makes long agent runs practical.
- Extensible without lock-in: the extension SDK and bundled extensions are Apache-2.0, so closed-source extensions are allowed, while the app itself is AGPL-3.0.
- Runs locally or headless-remote with the same UI, no signup, no telemetry gate.

## Cautions

- **One maintainer**: bus factor of one, no company, no funding announced as of 2026-09-12.
- The app code is AGPL-3.0, which matters if you want to embed or host it inside a closed product (commercial licensing is offered by the author).
- Young v0.6.x software from a first-time-agent author; expect churn in session formats and extension APIs.
- GUI-first means terminal-centric habits (SSH workflows, CI scripting, pipes) are not the target; remote use works but through Juggler's own client model.

## Pricing

Free and open-source, no signup: download the binary and run it.
You pay your own model costs through your existing subscriptions or API keys.
The AGPL app code with a paid commercial-licensing option for closed use is the only monetization path stated as of 2026-09-12.

## Compared to

- [Claude Code](../claude-code/index.md): the terminal incumbent with the deepest ecosystem; pick Claude Code for hooks/skills infrastructure, Juggler when you want to see and steer every step graphically.
- [OpenCode](../opencode/index.md): the other open-source community magnet, terminal-first; Juggler is the GUI counterpart with comparable provider breadth.
- [Zed](../../surfaces/zed/index.md): editor-native agent UX for people who live in an editor; Juggler is a standalone workbench for people who want agent sessions as first-class documents.

## Bottom line

**Recommended for developers whose agent work is long interactive sessions they need to inspect, branch, and resume across devices; not for teams wanting a vendor-backed product or terminal/CI automation.**
I think the harnesses that win the GUI layer will be the ones that treat conversations as editable trees, and I would bet on Juggler's model over Electron dashboards bolted onto a terminal agent.

## Changes

- 2026-08-30 - Created in the Harnesses category as one of six entrants accepted in the same run.
- 2026-09-16 - Recorded the v0.6.4 release (September 14) and refreshed counters (596 stars, 45 forks).
- 2026-09-24 - Recorded the v0.7.0 release (September 24), which added workspaces (git worktrees, scratch copies, or subfolders), and refreshed counters.
- 2026-09-29 - Recorded the v0.7.1 (September 27, side-by-side diffs, workspace polish, OpenRouter presets) and v0.7.2 (September 28, first-launch provider setup, folder drop-to-open, welcome panel) releases and refreshed counters.
- 2026-10-02 - Recorded the v0.7.3 release (September 30), which added a Group workspace type, pace-based usage meters, touch fixes, and an LM Studio provider reading each model's context window, and refreshed counters.
- 2026-10-03 - Recorded the v0.7.4 release (October 2), which added per-provider Codex and Copilot subscription toggles, Ollama thinking levels, media playback in the file viewer, and a Windows WSL fix, and refreshed counters (732 stars, 51 forks), over a hundred new stars in a day.
- 2026-10-07 - Added the juggler-ai/juggler star history chart to the Status section.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - where a GUI-native harness sits in the surface layer
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the terminal incumbents Juggler diverges from
- [OpenCode](../opencode/index.md) - the open terminal harness with a comparable community-driven ethos
- [Conductor](../../orchestration/conductor/index.md) - the other GUI bet, but as a multi-session Mac manager around existing agents

## References

- https://github.com/juggler-ai/juggler - repository, AGPL-3.0 app code with Apache-2.0 extensions, 768 stars as of 2026-10-06
- https://juggler.studio/ - product claims, provider list, session model
- https://raw.githubusercontent.com/juggler-ai/juggler/main/README.md - architecture, licensing map, build model
- https://news.ycombinator.com/item?id=48883305 - the July 12, 2026 launch thread, 280 points (verified via Algolia API)
- https://github.com/juggler-ai/juggler/releases - v0.7.4, published 2026-10-02 (verified via GitHub API)
