---
title: PandaCode
created: 2026-11-07
updated: 2026-11-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, coding-agents, desktop-app, tauri, model-routing]
readability: 3
audience_notes: >
  Engineers comparing desktop command centers for parallel coding agents who
  know what Claude Code, Codex, ACP, and git worktrees are, and who need to
  weigh a fast-growing three-week-old project's breadth against its missing
  independent evidence.
---

PandaCode is a free, open-source Tauri 2 desktop workspace that runs nineteen coding-agent CLIs side by side in one native window with projects, Git, a terminal, a browser, a task board, and architect-and-worker agent teams.

## What it is

**PandaCode wraps the agents you already subscribe to instead of selling a runtime, a model, or an account.**
AICodeKing, a solo creator who runs a YouTube channel covering AI coding tools, built it on Tauri 2, Rust, SQLite, and plain TypeScript, rendering through the operating system's webview with no bundled Chromium and no resident Node server.
It drives nineteen engines over six integration paths: Claude Code, Codex, Kimi Code, and OpenCode natively, GLM Coding Plan and Xiaomi MiMo through Claude Code, nine harnesses including GitHub Copilot CLI, Antigravity, Grok Build, DeepSeek, Command Code, Cline, Kilo Code, Devin CLI, and Hermes Agent through ACP, ZCode through its app-server protocol, Pi and its fork omp through Pi's RPC mode, and Meta's Muse Code through MSP.
Per-task worktrees come with a guarded one-click Merge into main that refuses uncommitted changes, and the architect-and-workers team mode adds a local model router that picks each worker's model in about 10 to 25 ms without sending the task anywhere.
Data stays local in SQLite, provider keys live in a user-readable 0600 file rather than the macOS Keychain, and the README enumerates every automatic outbound call in a privacy table.

## Status

**Active and very young: three weeks old, shipping daily, growing fast, and carrying no independent measurement yet.**
The repository was created 2026-10-18 and stood at 1,109 stars with 204 forks and 85 open issues as of 2026-11-07, up from the 400 stars the cnblogs walkthrough counted on 2026-10-22, four days in.
The release train runs daily: ten releases between v0.3.91 (2026-11-02) and v0.3.101 (2026-11-07), the npm installer has published 80 versions since 2026-10-22, and the default branch was pushed the day of this writing.
The owner accounts for 460 of the top ten contributors' commits against 38 for the next contributor, and Hacker News carries no story on the project at all.
The coverage footprint is two third-party writeups plus directory listings: MindStudio's editorial review of 2026-10-21 and wflynn's technical cnblogs walkthrough of 2026-10-22, an EveryDev.ai tools listing, and the creator's own launch video, with Chinese GitHub-trending coverage in the cnblogs piece's own series.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=aicodeking/pandacode&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=aicodeking/pandacode&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=aicodeking/pandacode&type=date&legend=top-left" />
</picture>

## Strengths

- The widest harness fan-in available in a lightweight native shell, at a startup cost the creator measures in fractions of a second.
- Per-task worktrees with a guarded merge, per-turn diffs, turn checks that queue an editable fix message when the project's tests fail, an approvals bar, and prompt rewind that forks the thread before a bad turn.
- Local model routing for agent teams picks each worker's model from a SHA-256-verified ONNX profiler in 10 to 25 ms, pauses models that keep failing, and escalates failed workers to a stronger model.
- Account pools fail tasks over between accounts of the same harness when a usage limit hits, mid-conversation.
- The privacy posture is explicit and checkable: no telemetry, no accounts, and a table of every automatic outbound request with its frequency.

## Cautions

- The PandaCode License is MIT plus a fork-attribution clause, so GitHub's API reads it as NOASSERTION: any fork used commercially or released publicly must state "This is a fork of PandaCode" with a link, a non-OSI condition for anyone building a product on it.
- Release builds carry no code signature: macOS builds are ad-hoc signed and not notarized (Gatekeeper needs an `xattr` workaround or the `npx pandacode` local-signing path), and Windows trips SmartScreen.
- Windows and Linux builds trail macOS: the iOS Simulator tools are macOS-only, Intel and x86_64 builds fall back to a simpler keyword-based model router, and closing the window on Linux quits the app instead of backgrounding it.
- Three weeks of history at 1,109 stars with one dominant author and zero Hacker News footprint leaves the growth curve uncorroborated by any independent measurement.
- The performance claims (roughly a third of a second to open, 130 to 160 MB idle, against T3 Code's about 3 seconds and 700 MB) are the creator's own, and MindStudio's review says so.
- Third-party writeups already lag the build: both describe the team mode's early caps (three workers, a twenty-round ceiling) that the current README has removed.
- Provenance breadcrumbs are worth reading: the creator published k3code, an opinionated T3 Code fork, on 2026-10-09, nine days before calling PandaCode "not a fork" at launch, and the app's SQLite file keeps the legacy name kingcode.sqlite3.

## Pricing

Free and open source under the PandaCode License, with no account, license key, or paid tier.
It adds no markup: you bring the coding CLIs and their subscriptions, and cloud-agent runs execute on machines in your own cloud accounts.

## Compared to

**Emdash** shares the wrap-the-installed-CLIs model across all three desktop OSes and goes SSH-first for remote code, where PandaCode keeps execution local or in your own cloud sandboxes and carries the wider engine list.
**Agent Orchestrator** pairs its Electron kanban with per-worker PR, CI, and review state routed back into the same worker, the integration PandaCode approximates with turn checks and a GitHub view instead.
**T3 Code** is the multi-client control surface the creator benchmarked against and forked first, and it ships phone clients as products where PandaCode's mobile app must be built from source.
Choose PandaCode for the widest engine list and local model routing in the lightest window, Agent Orchestrator for CI-and-review state per worker, and T3 Code for polished native client reach.

## Bottom line

Recommended for developers who already pay for two or more coding-agent subscriptions and want them supervised in one fast native window with worktrees, teams, and local model routing, and who can tolerate unsigned installers and 0.x churn.
Not for teams that need an OSI license to build a derivative product, a signed and notarized install path, or independently measured performance claims.

## Changes

- 2026-11-07 - Created.

## See also

- [Emdash](../emdash/index.md) - the cross-platform ADE sharing the wrap-installed-CLIs model, SSH-first where PandaCode is local-first.
- [Agent Orchestrator](../agent-orchestrator/index.md) - the closest structural peer, a kanban workspace with per-worker PR and CI state.
- [T3 Code](../t3code/index.md) - the control surface PandaCode benchmarked against, and the project the creator forked first.
- [OpenHarness](../openharness/index.md) - the other native command center linking machines over an encrypted relay, PandaCode Connect's nearest peer.

## References

- https://api.github.com/repos/aicodeking/pandacode - repository metadata: created 2026-10-18, Rust, 1,109 stars, 204 forks, 85 open issues, license detected NOASSERTION, as of 2026-11-07.
- https://raw.githubusercontent.com/aicodeking/pandacode/main/README.md - the nineteen-engine list, worktree merge guard, team model routing, privacy table, unsigned-install instructions, and the kingcode.sqlite3 legacy name.
- https://raw.githubusercontent.com/aicodeking/pandacode/main/LICENSE - the PandaCode License terms, MIT plus the fork-attribution clause.
- https://api.github.com/repos/aicodeking/pandacode/releases?per_page=10 - the release feed, v0.3.101 (2026-11-07) and the daily train from 2026-11-02.
- https://www.mindstudio.ai/blog/panda-code-desktop-ai-coding-agent-gui - MindStudio's 2026-10-21 review, the creator-benchmark caveat, the unsigned-build friction, and the early team caps.
- https://www.cnblogs.com/wflynn/p/23397823 - wflynn's 2026-10-22 walkthrough, 400 stars four days in, the module architecture, and the approval-gap, docs-gap, and cap cautions.
- https://www.youtube.com/watch?v=cCFAIrbt_s8 - the creator's launch video, "I built the fastest & lightest AI coding agent GUI", verified through its oEmbed metadata.
- https://www.everydev.ai/tools/pandacode - the EveryDev.ai directory listing, confirmed through search results because the site serves a Vercel bot-check wall to unauthenticated fetches.
- https://api.github.com/users/aicodeking/repos - the creator's repositories, including k3code (T3 Code fork, 2026-10-09), the PandaOrchestrator router, and the homebrew tap.
- https://api.github.com/repos/aicodeking/pandacode/contributors - the single-dominant-author split (460 commits against 38 for the next contributor).
- https://registry.npmjs.org/pandacode - the npx installer, 80 versions since 2026-10-22, latest 0.3.101.
- https://hn.algolia.com/api/v1/search?query=PandaCode&hitsPerPage=10 - the empty Hacker News footprint (fuzzy matches only).
