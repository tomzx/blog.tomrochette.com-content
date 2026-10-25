---
title: OpenChamber
created: 2026-08-24
updated: 2026-10-25
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
About 11,669 stars (11,668) and 1,305 forks as of 2026-10-16, with v2.5.1 (October 23, Git hosts Gitea, Forgejo, and Gerrit joining GitHub and GitLab with Codeberg ready, stacked pull requests, usage-limit fallback that switches accounts or models when a provider caps out, GitHub Enterprise support, and Tailscale Serve and Funnel as external tunnels) above v2.5.0 (October 19, find in changes across the whole changeset in the Changes and Walkthrough panels, page annotation in the chat and for HTML files in Files, settings that keep sessions warm 30 minutes to 3 hours after a reply, an Issues and PRs board that lists every repository in a multi-repo project, sidebar session sorting by time across projects, pasted images saved as linked files, and browser-panel sign-ins that survive a restart) above v2.4.0 (October 17, an integrations catalog of more than 160 services with one-click MCP installs plus skills or plugins and visible sign-in status, find in files with a regex switch above the sidebar file tree, agent choice pages answered in the same turn, a connection diagnostics timeline exportable as a `.log`, and web search through plugin providers like SearXNG, Brave, and Kagi) above v2.3.3 (October 14, 2026, agent-rendered charts, tables, diagrams, and interface mockups above the answer, end-to-end-encrypted mobile push that names what happened, and review threads on the issues board) above v2.3.2 (October 14, 2026, project knowledge the agents read and change with their own tool, issue and pull-request links opening on the issues board, and Linux .deb and .rpm packages) above v2.3.1 (October 13, 2026, starting a session from iOS Shortcuts and Siri, an Antigravity usage card beside the Google card, a view-repository-on-GitHub-or-GitLab action, and mobile fixes ending the connect, drop, reconnect loop on slow servers) above v2.3.0 (October 12, 2026, panels that move around the chat so a terminal and a diff can share the screen, calmer streaming replies, Arabic and Hebrew with right-to-left mirroring, and a sidebar split into Tree and List views) above v2.2.0 (October 8, 2026,an Issues and PRs board listing a project's GitHub, GitLab, or Linear issues and pull requests with comment, review, merge, and session-start actions from the preview, environment variables per project or loaded from direnv, devenv, or a Nix shell, Azure and Bedrock provider connections, and a cache-preserving routing default) after v2.1.1 (October 4, 2026, GitLab support end to end with merge requests in the Git panel and sidebar, one composer picker for GitHub issues, pull requests, and Linear items, per-repository git identities, and automatic cleanup of worktrees whose pull request merged) after v2.1.0 (October 1, cross-conversation message search over every session with the index kept on-machine, background commands and subagents that stay visible with live logs while they run, and a rebuilt file editor with changed-line markers, folding, multi-cursor, and a symbol outline) after v2.0.4 (September 28, enterprise mode for teams that an administrator turns on with a policy file or `OPENCHAMBER_ENTERPRISE_MODE=1`, keeping conversations with the configured providers, locking provider management to config, and restricting extensions to administrator-approved repositories, plus goal checking, an Excalidraw extension, a Dutch interface, and Jev off by default), the v2.0.3 to v2.0.4 pair of September 28 (per-session permission modes of ask, safety net, or accept all, an In work session section, multi-run from the composer, a token-stats page, and provider cards), the v2.0.0 GA of the app on OpenCode 2 (September 23), the v1.24 line just below it (v1.24.2 of September 18 ending it), and commits landing October 20, 2026.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=openchamber/openchamber&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=openchamber/openchamber&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=openchamber/openchamber&type=date&legend=top-left" />
</picture>

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
- 2026-10-05 - Recorded v2.1.1 (October 4, GitLab integration, unified references picker, per-repository git identities, merged-worktree cleanup) as the new latest release and refreshed stars to 11,126 and forks to 1,226.
- 2026-10-07 - Added the openchamber/openchamber star history chart to the Status section.
- 2026-10-09 - Recorded v2.2.0 (October 8, the Issues and PRs board across GitHub, GitLab, and Linear, per-project environment variables with direnv, devenv, and Nix loading, Azure and Bedrock provider connections, and cache-preserving routing) as the new latest release and refreshed stars to 11,308 and forks to 1,250.
- 2026-10-13 - Recorded v2.3.0 (October 12, movable panels around the chat, calmer streaming replies, Arabic and Hebrew with right-to-left mirroring, the Tree and List sidebar) and v2.3.1 (October 13, iOS Shortcuts and Siri session starts, an Antigravity usage card, and the mobile reconnect-loop fix) as the new latest releases; stars refreshed to 11,503 and forks to 1,277.
- 2026-10-16 - Recorded v2.3.2 (October 14, project knowledge agents read and change with their own tool, issue and PR links opening on the issues board, Linux .deb and .rpm packages) and v2.3.3 (October 14, agent-rendered charts and mockups above the answer, end-to-end-encrypted mobile push with content, review threads on the issues board) as the new latest releases; stars refreshed to 11,668 and forks to 1,305.
- 2026-10-17 - Recorded v2.4.0 (October 17, the integrations catalog with one-click MCP installs, find in files, agent choice pages, the downloadable connection diagnostics timeline, and web search plugin providers) as the new latest release.
- 2026-10-20 - Recorded v2.5.0 (October 19, find in changes, page annotation, warm sessions from 30 minutes to 3 hours, the multi-repository Issues and PRs board, cross-project session sorting, saved pasted images, and persistent browser-panel sign-ins) as the new latest release.
- 2026-10-25 - Recorded v2.5.1 (October 23, the Gitea, Forgejo, and Gerrit git hosts with Codeberg ready, stacked pull requests, usage-limit account and model fallback, GitHub Enterprise support, and Tailscale Serve and Funnel tunnels) as the new latest release.

## See also

- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the landscape piece whose OpenCode-native section is this tool
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the surface layer this note belongs to
- [Six Months with OpenChamber](../../../six-months-with-openchamber/index.md) - the owner's deep usage retrospective, including every friction named above
- [Managing Many Concurrent LLM Agent Sessions](../../../managing-many-llm-agent-sessions/index.md) - the supervision problem OpenChamber exists for
- [OpenCode](../../harnesses/opencode/index.md) - the harness underneath

## References

- https://openchamber.dev/ - features, surfaces, privacy model, FAQ
- https://github.com/openchamber/openchamber - source, repository scale, as of 2026-10-16
- https://github.com/openchamber/openchamber/releases/tag/v2.5.1 - the October 23, 2026 release: the new git hosts, stacked pull requests, the usage-limit fallback, GitHub Enterprise, the Tailscale tunnels, and the Electron 44.9.3 and bundled-OpenCode-2.1.3 updates, fetched 2026-10-25
- https://api.github.com/repos/openchamber/openchamber/releases/tags/v2.5.0 - the October 19 release notes: find in changes, page annotation, warm sessions, the multi-repository issues and PRs board, and the browser-panel improvements, fetched 2026-10-20
- https://github.com/openchamber/openchamber/releases/tag/v2.3.3 - the October 14, 2026 release (agent-rendered charts and mockups, encrypted mobile push with content, review threads on the issues board); v2.3.2 of October 14 and v2.3.1 of October 13 sit just below it
- https://github.com/openchamber/openchamber/releases/tag/v2.3.2 - the October 14, 2026 release (project knowledge tool for agents, issue and PR links on the issues board, Linux .deb and .rpm packages); v2.3.1 of October 13 and v2.3.0 of October 12 sit just below it
- https://api.github.com/repos/openchamber/openchamber/releases/tags/v2.4.0 - the October 17 release notes: the integrations catalog, find in files, agent choice pages, connection diagnostics, and web search providers, fetched 2026-10-17
- https://github.com/openchamber/openchamber/releases/tag/v2.2.0 - the October 8, 2026 release (the Issues and PRs board, environment variables, Azure and Bedrock connections, cache-preserving routing); v2.1.1 of October 4 sits just below it
- https://github.com/openchamber/openchamber/releases/tag/v2.1.1 - the October 4, 2026 release (GitLab support, references picker, git identities, worktree cleanup)
- https://docs.openchamber.dev/ - install and configuration documentation
- https://news.ycombinator.com/item?id=49233448 - the August 2026 launch discussion
