---
title: OpenChamber
created: 2026-08-24
updated: 2026-10-03
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, surfaces, agentic-development-environments, opencode, open-source]
readability: 3
audience_notes: >
  Engineers running several coding-agent sessions in parallel who want one surface to steer them.
  Assumes you already run OpenCode or a similar harness and know what a git worktree is.
---

OpenChamber is a free, MIT-licensed agentic development environment built around the OpenCode SDK: desktop, browser, mobile, and a VS Code extension for steering parallel agent sessions.

**OpenChamber is the open-source answer to "where do I run my many OpenCode sessions", and its differentiator is not polish but the fact that the whole surface, worktrees, chat, terminals, scheduling, is code you can read and fix.**

## What it is

**A session cockpit, not an editor**: parallel sessions each get their own worktree and branch, with chat, files, and terminals in one window.
Session Goals let an agent keep working toward a finish line with the app closed; Multi-run and Fusion send one task across several models in parallel (v1.21.1 lifted the five-model cap) and keep or fuse the best results; scheduled work runs prompts on cron; and sessions start from GitHub issues or PRs and merge without leaving the app.
Remote access works through a password-gated browser UI, Cloudflare tunnels, or an end-to-end-encrypted Private Relay pairing with no open ports.
It runs on the OpenCode SDK today and is an independent project, not affiliated with the OpenCode team.

## Status

**Very active.**
About 11,100 stars (11,078) and 1,221 forks as of 2026-10-04, with v2.1.0 (October 1, 2026, cross-conversation message search over every session with the index kept on-machine, background commands and subagents that stay visible with live logs while they run, and a rebuilt file editor with changed-line markers, folding, multi-cursor, and a symbol outline) now the latest release after v2.0.4 (September 28, enterprise mode for teams that an administrator turns on with a policy file or `OPENCHAMBER_ENTERPRISE_MODE=1`, keeping conversations with the configured providers, locking provider management to config, and restricting extensions to administrator-approved repositories, plus goal checking, an Excalidraw extension, a Dutch interface, and Jev off by default), the v2.0.3 to v2.0.4 pair of September 28 (per-session permission modes of ask, safety net, or accept all, an In work session section, multi-run from the composer, a token-stats page, and provider cards), the v2.0.0 GA of the app on OpenCode 2 (September 23), the v1.24 line just below it (v1.24.2 of September 18 ending it), and commits landing October 4, 2026.
A 190-point Hacker News thread in August 2026 marks its arrival in general awareness.

## Strengths

- **Parallel sessions with automatic worktree management is the core loop**, and the feature set around it (goals, multi-model fusion, cron scheduling) is built for exactly that workload.
- Privacy is inspectable: nothing collected, code stays local, and the policy is visible in the source rather than a document.
- Free and MIT with donation funding; no subscription cliff anywhere.
- Every device surface (desktop, browser, phone, VS Code) drives the same sessions.

## Cautions

- **It is one harness deep**: OpenCode SDK today, so your harness choice is made for you.
- The built-in editor was serviceable, not good; v2.1.0's rebuilt editor (changed-line markers, folding, multi-cursor, symbol outline) narrows the gap, but heavy users may still keep a separate editor open for diff review.
- The reliability record has rough chapters documented in detail in the corpus: chat blocking during worktree creation, terminal sessions closing on their own, and a weak `@` file matcher.
- A young project moving fast; expect regressions between releases.

## Pricing

Free, open source, MIT.
Donations via Patreon fund development; there is no paid tier, as of 2026-09-22.

## Compared to

- [Antigravity](../antigravity/index.md): Google's free multi-agent command center; closed client versus open code.
- [Cursor](../cursor/index.md): the editor-first platform; OpenChamber is sessions-first and harness-agnostic only in the OpenCode direction.
- [VS Code + Copilot](../vscode-copilot/index.md): the default surface; OpenChamber is for people whose problem is parallelism, not editing.

## Bottom line

**Recommended for engineers juggling multiple OpenCode sessions against shared repositories who want to own their surface.**
Not for anyone who wants a polished IDE experience or harness choice beyond OpenCode.

## Changes

- 2026-08-24 - Created among the five Surfaces notes after the owner-named OpenChamber verified real and Antimatter did not exist.
- 2026-09-16 - Recorded v1.23.2 (September 14, faster startup and session browsing) as the latest release and refreshed stars to 9,908.
- 2026-09-18 - Recorded v1.24.0 (third-party extensions, themes) and v1.24.1 as the latest releases, stars past 10,000, and the v2-preview test line on OpenCode v2.
- 2026-09-20 - Recorded v1.24.2 (startup and reconnect memory fixes, session waiting indicators) as the latest release and refreshed stars to 10,100.
- 2026-09-24 - Recorded the v2.0 GA: v2.0.0 shipped September 23 ("OpenCode 2 and instant settings", promoting the v2-preview line) and v2.0.1 followed September 24 as the new latest release; stars refreshed to 10,509 and forks to 1,154.
- 2026-09-26 - Recorded v2.0.2 (September 26, cleaner chat timeline rendering plus startup, worktree-config, and mobile relay fixes) as the new latest release and refreshed stars to 10,622.
- 2026-09-27 - Linked the Agentic Development Environment Landscape tracker, whose OpenCode-native section is OpenChamber.
- 2026-09-29 - Recorded v2.0.3 and v2.0.4 (both September 28, per-session permission modes, In work sessions, composer multi-run, and enterprise mode for teams) as the new latest releases and refreshed stars to 10,897.
- 2026-10-02 - Recorded v2.1.0 (October 1, cross-conversation message search, visible background commands and subagents, a rebuilt file editor) as the new latest release and refreshed stars to 11,008.

## See also

- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the landscape piece whose OpenCode-native section is this tool
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the surface layer this note belongs to
- [Six Months with OpenChamber](../../../six-months-with-openchamber/index.md) - the owner's deep usage retrospective, including every friction named above
- [Managing Many Concurrent LLM Agent Sessions](../../../managing-many-llm-agent-sessions/index.md) - the supervision problem OpenChamber exists for
- [OpenCode](../../harnesses/opencode/index.md) - the harness underneath

## References

- https://openchamber.dev/ - features, surfaces, privacy model, FAQ
- https://github.com/openchamber/openchamber - source, repository scale, as of 2026-10-03
- https://github.com/openchamber/openchamber/releases/tag/v2.1.0 - the latest release (October 1, 2026, message search, background commands, rebuilt editor); v2.0.4 of September 28 sits just below it
- https://docs.openchamber.dev/ - install and configuration documentation
- https://news.ycombinator.com/item?id=49233448 - the August 2026 launch discussion
