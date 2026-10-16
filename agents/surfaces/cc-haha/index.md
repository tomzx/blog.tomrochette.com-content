---
title: cc-haha
created: 2026-10-11
updated: 2026-10-16
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, surfaces, ai-editors, open-source, claude-code]
readability: 3
audience_notes: >
  Engineers who live in Claude Code and want the whole agent surface, sessions, approvals, MCP, subagents, and skills, in one desktop GUI.
  Assumes you know what Claude Code, MCP, and a git worktree are.
---

cc-haha is an MIT-licensed open-source desktop workbench for Claude Code and other agents, packing sessions, worktree launches, diff review, MCP and subagent management, a skills marketplace, and scheduled tasks into one macOS, Windows, and Linux app.

**cc-haha is the broadest Claude Code GUI in this category, and its 8,609 forks against 15,023 stars say its audience lives in an ecosystem this section's other evidence channels barely reach.**

## What it is

A local-first workbench that wraps Claude Code in a GUI: multi-session management with global search, branch and worktree launches, diff review, a built-in browser preview, graphical permission approvals, and model selection across Claude, ChatGPT, Grok, presets, and local endpoints.
The agent layer is managed visually too: MCP servers and subagents get their own management screens, Agent Teams gives multi-agent collaboration a workbench, and dynamic workflow orchestration sits above the sessions.
The long tail is unusually wide: model request tracing, image generation, a skills marketplace, Computer Use (on macOS it drives other apps without occupying your mouse and keyboard), desktop pets, H5 remote access, IM access over WeChat, Feishu, DingTalk, Telegram, and WhatsApp, and scheduled tasks.
It is built by NanmiCoder in TypeScript, documented first in Chinese with an English README, and distributed as desktop builds through its releases.

## Status

**Active and growing fast outside the English-language channels.**
The repository was created 2026-03-31 and shows 15,023 stars and 8,609 forks as of 2026-10-16, with commits landing the same week.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=NanmiCoder/cc-haha&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=NanmiCoder/cc-haha&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=NanmiCoder/cc-haha&type=date&legend=top-left" />
</picture>

The release train runs roughly weekly: v0.6.6 (September 22), v0.6.7 (September 27), v0.6.8 (October 1), v0.7.0 (October 8), v0.7.1 (October 11), and v0.7.2 with v0.7.3 (both October 15, DeepSeek account sign-in without an API key, a session-tab count limit, and an urgent fix for a Windows bug that popped black terminal windows on open or resume) as the latest.
An Algolia search of Hacker News returned zero stories for the project as of 2026-10-11, and this run's search found no third-party coverage in English.

## Strengths

- **It is the only member that puts the whole Claude Code control plane in a GUI: permission approvals, MCP servers, subagents, and skills all get visual management instead of config files.**
- The IM integrations turn WeChat, Feishu, DingTalk, Telegram, or WhatsApp into remote controls for local agents, a wider channel list than any other member documents.
- Computer Use that operates other applications without taking over the mouse and keyboard is a capability no other member ships.
- Local endpoints sit beside the hosted models in the model picker, so on-device or self-hosted models are a documented path.

## Cautions

- **The missing independent footprint is the caution: zero Hacker News stories and no English third-party coverage found this run, so every capability claim rests on the project's own README.**
- The project is pre-1.0 (v0.7.0), and a client this broad, Computer Use and IM control included, has a blast radius that a young codebase has not had time to prove safe.
- The documentation is Chinese-first; the English README exists but the deeper guides are not translated, which narrows the audience this section writes for.
- The marketing site (cchaha.ai) rendered only its title to this run's fetch, so the docs site grounds nothing by itself.

## Pricing

Free and open source under MIT; no paid tier exists.

## Compared to

- [OpenChamber](../openchamber/index.md): the session cockpit around OpenCode; OpenChamber is code you can audit for harness work, cc-haha is the wider but Claude-centric GUI.
- [Cate](../cate/index.md): the canvas workspace for many agent CLIs; Cate supervises in space, cc-haha supervises in panels and IM channels.
- [Vibeyard](../vibeyard/index.md): the other single-maintainer desktop wrapping agent CLIs; Vibeyard's kanban spawns sessions, cc-haha's teams and workflows coordinate them.

## Bottom line

**Recommended for Claude Code-centric engineers who read Chinese documentation and want the entire agent control plane in one GUI.**
Not for teams that need an English-first project, a 1.0 stability guarantee, or third-party validation of the security surface.

## Changes

- 2026-10-11 - Created from the category entrant scan, admitted on its differentiated whole-control-plane GUI and IM remote access, with the zero-footprint caution recorded.
- 2026-10-11 - Added the star history chart.
- 2026-10-12 - Recorded v0.7.1 (October 11, ChatGPT OAuth Fast mode, a regular-subagent concurrency cap, a voice-dictation shortcut, and CSV/TSV preview) as the new latest release; counts refreshed.
- 2026-10-16 - Recorded v0.7.2 and v0.7.3 (October 15, DeepSeek account sign-in without an API key, a session-tab count limit, and the Windows black-terminal-popup fix) as the new latest releases; counts refreshed.

## See also

- [OpenChamber](../openchamber/index.md) - the open session cockpit this note joins as the Claude-centric workbench
- [Cate](../cate/index.md) - the canvas answer to the same supervision problem
- [Vibeyard](../vibeyard/index.md) - the CLI-wrapping desktop with the task board
- [Claude Code](../../harnesses/claude-code/index.md) - the harness whose control plane this workbench renders

## References

- https://github.com/NanmiCoder/cc-haha - repository, README feature list (sessions, worktrees, diff review, MCP and subagent management, Agent Teams, Computer Use, skills marketplace, IM access, scheduled tasks), MIT license, 15,023 stars and 8,609 forks as of 2026-10-16
- https://api.github.com/repos/NanmiCoder/cc-haha - creation date 2026-03-31, language TypeScript, push date 2026-10-15, stars and forks as of 2026-10-16
- https://github.com/NanmiCoder/cc-haha/releases - v0.7.3 (2026-10-15) as the latest release, after v0.7.2 (October 15), v0.7.1 (October 11), v0.7.0 (October 8), and v0.6.8 (October 1)
- https://cchaha.ai - the docs-site domain, which rendered only its title to this run's fetch (client-rendered shell)
- https://hn.algolia.com/api/v1/search?query=cc-haha&tags=story - the exhaustive search that returned zero stories, the missing-footprint evidence, fetched 2026-10-11
