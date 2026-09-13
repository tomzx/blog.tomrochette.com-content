---
title: Grok Build
created: 2026-09-12
updated: 2026-09-12
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, harnesses, coding-agents, terminal, open-source]
readability: 3
audience_notes: >
  Engineers deciding whether xAI's terminal coding agent belongs in their toolkit.
  Assumes you know what a TUI agent, BYOK, MCP, and ACP are.
---

Grok Build (`grok`) is SpaceXAI's (xAI's) open-source Rust terminal coding agent, a full-screen mouse-interactive TUI that understands your codebase, edits files, runs shell commands, searches the web, and manages long-running tasks, interactively, headlessly, or embedded in editors.
Facts below verified as of 2026-09-12.

**No harness in this section iterates faster, and none asks for more trust: the Apache-2.0 client ships through vendor channels that bypass the repository entirely, on a default auth path that a wire-level analysis caught uploading whole repositories to xAI infrastructure.**

## What it is

A roughly 170 MiB Rust binary for macOS, Linux, and Windows, running as an interactive TUI, headlessly via `grok -p` (with `--output-format streaming-json`) for scripts and CI, or inside editors over the Agent Client Protocol.
The GitHub repository is a periodic one-way sync from the SpaceXAI monorepo, with a `SOURCE_REV` file recording the source commit, and it accepts no external contributions.
The feature surface is Claude Code-class: AGENTS.md project rules (plus CLAUDE.md, `.cursor/rules`, and `.claude/rules` compatibility), MCP servers, subagents, hooks that also read Claude Code and Cursor hook files, skills, plugins with marketplaces, plan mode, worktrees, and `/loop` scheduled prompts.
The third-party notices disclose in-tree source ports of openai/codex and sst/opencode tool implementations, which tells you exactly whose agents it was benchmarked against.

## Status

Active and extremely fast-moving: 26,704 stars and 5,030 forks as of 2026-09-12, roughly nine weeks after the repo was created on 2026-07-14, last pushed 2026-09-09.
The changelog lists v1.0.25 as current as of 2026-09-09, with 138 releases logged between May 17 and September 9, roughly one per day.
There are no GitHub releases or tags (both API endpoints return empty arrays), so binaries ship from the install script at x.ai/cli, which pulls versioned binaries from a Cloudflare-fronted URL with a Google Cloud Storage fallback across stable, alpha, and enterprise channels; the docs also document `npm install -g @xai-official/grok` as the alternative that needs neither host.
The HN footprint is heavy for a nine-week-old tool: a 100-point preview thread in May 2026, the wire-level analysis at 539 points on July 12, a 100-point follow-up on July 13 reporting the repo-upload behavior persisted under retest, and the open-source announcement at 590 points and 643 comments on July 15.
I read the open-sourcing as reputational triage: top comments on the launch thread explicitly connect it to the privacy upset three days earlier.

## Strengths

- **The fastest release cadence of any harness in this section**, roughly daily, and it reached 1.0 on 2026-08-07, under a month after the repo appeared.
- Cross-compatibility is a design goal: it reads CLAUDE.md, Claude Code hook files, Cursor hooks, and even Anthropic's `managed-settings.json` policies, making migration in either direction cheap.
- The enterprise story is unusually complete: four auth methods including corporate OIDC, layered managed configuration with fail-closed `requirements.toml` pinning, team-level zero data retention, and a Landlock/Seatbelt sandbox with a `strict` profile for untrusted repositories.
- Real BYOK: any custom model works via `base_url` and `env_key` in `config.toml`, and `grok inspect` shows the resolved config, rules, skills, plugins, hooks, and MCP servers.

## Cautions

- **The wire-level analysis found the CLI uploads every tracked file plus git history, independent of what the agent actually reads**, and the follow-up thread reports the behavior persisted under retesting.
- The default interactive path authenticates through auth.x.ai and sends inference through `cli-chat-proxy.grok.com`, so your code crosses xAI infrastructure; zero data retention is a team-level enterprise setting, not a default.
- Open code, closed process: no external contributions, issues and discussions disabled, and PR creation restricted to collaborators, so forking is possible but upstreaming is not.
- The sandbox that would contain an untrusted-repo incident is off by default.
- A telemetry exporter ships in the client; opt-out exists and can be policy-pinned, but the default posture is set by the vendor, not by you.

## Pricing

Free and open source under Apache-2.0, with no per-seat fee anywhere in what I fetched.
Usage is billed through an authenticated x.ai account session (the default `grok login` OIDC path) or an `XAI_API_KEY` on pay-as-you-go API pricing.
As of 2026-09-12 the API charges $2.00/$6.00 per 1M tokens for grok-4.6 (under 200k prompt tokens) and lists a cheaper grok-build-0.1 model at $1.00/$2.00 with a 256k context.
The build docs I fetched never state what a consumer Grok subscription includes over the login path, so I treat subscription-included usage as unverified rather than assumed.

## Compared to

- [Codex](../codex/index.md): the other big-lab open terminal agent, and its tool implementations are literally ported inside Grok Build's tree; choose Codex for OpenAI's ecosystem and Grok Build for the TUI, the Grok models, and the deeper config surface.
- [DeepSeek Harness](../deepseek-harness/index.md): the other lab-open-sourced harness; dsh is an alpha plugin kernel with nothing built in, Grok Build is a batteries-included 1.0 product, so the choice is hackability versus polish.
- [Claude Code](../claude-code/index.md): the closed incumbent it openly courts; Grok Build reads CLAUDE.md, its hooks, and its managed settings, which makes it the lowest-friction exit ramp from Anthropic billing.

## Bottom line

**Recommended for engineers who want a Claude Code-class open terminal agent on Grok models, having read the wire-level analysis and accepted the proxy on the default path.**
Not for untrusted repositories without the `strict` sandbox profile and a ZDR agreement, and not for anyone who needs a community-governed client, because upstream takes no outside contributions.
I would not standardize on it while the default data path concentrates your code on xAI infrastructure without per-session guarantees.

## Changes

- 2026-09-12 - Created in the Harnesses category from the same-day entrant resolution.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the capability column this note adds
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where this lands in the harness layer
- [Codex](../codex/index.md) - the other big-lab open terminal agent, and the source of ported tool code
- [When AI Labs Stop Releasing Models](../../when-ai-labs-stop-releasing-models/index.md) - the corpus argument this release stress-tests

## References

- https://github.com/xai-org/grok-build - repository state, Apache-2.0 license, 26,704 stars and 5,030 forks as of 2026-09-12 (verified via the GitHub API)
- https://raw.githubusercontent.com/xai-org/grok-build/main/README.md - monorepo sync with SOURCE_REV, no external contributions, install commands, codex/opencode ports
- https://docs.x.ai/build/overview - TUI, headless mode, ACP, authentication, custom models, grok-4.6 as the powering model
- https://x.ai/cli/install.sh - channel-based binary distribution, GCS fallback, supported platforms, approximate binary size
- https://x.ai/build/changelog - v1.0.25 current as of 2026-09-09 and the roughly-daily release cadence (fetched via a text-extraction proxy because x.ai blocks non-browser agents)
- https://docs.x.ai/build/enterprise - the four auth methods, required network hosts, data lifecycle, ZDR, and telemetry pinning
- https://docs.x.ai/developers/pricing - grok-4.6 and grok-build-0.1 API prices as of 2026-09-12
- https://docs.x.ai/build/features/sandbox - Landlock/Seatbelt profiles and the off-by-default posture
- https://hn.algolia.com/api/v1/items/48877371 - the wire-level analysis thread, 539 points, 2026-07-12
- https://hn.algolia.com/api/v1/items/48896493 - the GCS upload follow-up thread, 100 points, 2026-07-13
- https://hn.algolia.com/api/v1/items/48926590 - the open-source launch thread, 590 points and 643 comments, 2026-07-15
- https://hn.algolia.com/api/v1/items/48139115 - the May 2026 preview thread, 100 points, 2026-05-14
- https://hn.algolia.com/api/v1/items/48656943 - the 0.1 analysis thread, 16 points, 2026-06-24
