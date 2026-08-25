---
title: OpenChamber
created: 2026-08-24
updated: 2026-08-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, surfaces, agentic-development-environments, opencode, open-source]
readability: 3
audience_notes: >
  Engineers running several coding-agent sessions in parallel who want one surface to steer them.
  Assumes you already run OpenCode or a similar harness and know what a git worktree is.
---

OpenChamber is a free, MIT-licensed agentic development environment built around the OpenCode SDK: desktop, browser, mobile, and a VS Code extension for steering parallel agent sessions.
Facts below verified as of 2026-08-25.

**OpenChamber is the open-source answer to "where do I run my many OpenCode sessions", and its differentiator is not polish but the fact that the whole surface, worktrees, chat, terminals, scheduling, is code you can read and fix.**

## What it is

**A session cockpit, not an editor**: parallel sessions each get their own worktree and branch, with chat, files, and terminals in one window.
Session Goals let an agent keep working toward a finish line with the app closed; Multi-run and Fusion send one task across up to five models and keep or fuse the best results; scheduled work runs prompts on cron; and sessions start from GitHub issues or PRs and merge without leaving the app.
Remote access works through a password-gated browser UI, Cloudflare tunnels, or an end-to-end-encrypted Private Relay pairing with no open ports.
It runs on the OpenCode SDK today and is an independent project, not affiliated with the OpenCode team.

## Status

**Very active.**
About 9.2k stars and 964 forks as of 2026-08-25, with v1.20.0 (August 22, 2026) still the latest release and commits landing the morning of this verification.
A 190-point Hacker News thread in August 2026 marks its arrival in general awareness.

## Strengths

- **Parallel sessions with automatic worktree management is the core loop**, and the feature set around it (goals, multi-model fusion, cron scheduling) is built for exactly that workload.
- Privacy is inspectable: nothing collected, code stays local, and the policy is visible in the source rather than a document.
- Free and MIT with donation funding; no subscription cliff anywhere.
- Every device surface (desktop, browser, phone, VS Code) drives the same sessions.

## Cautions

- **It is one harness deep**: OpenCode SDK today, so your harness choice is made for you.
- The built-in editor is serviceable, not good; heavy users keep a real editor open for diff review.
- The reliability record has rough chapters documented in detail in the corpus: chat blocking during worktree creation, terminal sessions closing on their own, and a weak `@` file matcher.
- A young project moving fast; expect regressions between releases.

## Pricing

Free, open source, MIT.
Donations via PayPal fund development; there is no paid tier, as of 2026-08-25.

## Compared to

- [Antigravity](../antigravity/index.md): Google's free multi-agent command center; closed client versus open code.
- [Cursor](../cursor/index.md): the editor-first platform; OpenChamber is sessions-first and harness-agnostic only in the OpenCode direction.
- [VS Code + Copilot](../vscode-copilot/index.md): the default surface; OpenChamber is for people whose problem is parallelism, not editing.

## Bottom line

**Recommended for engineers juggling multiple OpenCode sessions against shared repositories who want to own their surface.**
Not for anyone who wants a polished IDE experience or harness choice beyond OpenCode.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the surface layer this note belongs to
- [Six Months with OpenChamber](../../six-months-with-openchamber/index.md) - the owner's deep usage retrospective, including every friction named above
- [Managing Many Concurrent LLM Agent Sessions](../../managing-many-llm-agent-sessions/index.md) - the supervision problem OpenChamber exists for
- [OpenCode](../opencode/index.md) - the harness underneath

## References

- https://openchamber.dev/ - features, surfaces, privacy model, FAQ
- https://github.com/openchamber/openchamber - source, repository scale, as of 2026-08-25
- https://github.com/openchamber/openchamber/releases/tag/v1.20.0 - the August 22, 2026 release
- https://docs.openchamber.dev/ - install and configuration documentation
- https://news.ycombinator.com/item?id=49233448 - the August 2026 launch discussion
