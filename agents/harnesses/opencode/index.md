---
title: OpenCode
created: 2026-08-22
updated: 2026-11-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, llm=glm-5.4, coding-agents, harnesses, open-source, developer-tools]
readability: 3
audience_notes: >
  Engineers who pay for their own tokens or switch providers often, evaluating the main vendor-neutral harness.
  Assumes familiarity with AGENTS.md, MCP, and what a prompt-cache prefix is.

---

OpenCode is the open-source (MIT), provider-neutral coding agent from Anomaly: a TUI, desktop app, IDE extension, and web view built off one codebase, running against any provider's API keys.

**OpenCode is what a harness should cost in tokens, roughly a fifth of Claude Code's measured baseline, and its 2026 security and legal history is a working lesson in why agent clients need audits too.**

## What it is

The `opencode` TUI ships build and plan agents (Tab to switch), a general subagent, `/init` generating an AGENTS.md, `/undo` and `/redo` of agent changes, and shareable conversation links.
**One codebase also produces a desktop app, a VS Code extension, a web view, an SDK, a server, and `opencode acp`, which hosts the agent inside ACP-speaking editors (Zed, JetBrains, Neovim) unchanged.**
Providers are configured by API key; OpenCode Zen is the team's curated, tested model gateway.

## Status

**Very active.**
The repository moved from `sst` to `anomalyco/opencode` and shows about 213.6k stars and 28.7k forks under MIT as of 2026-10-15.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=anomalyco/opencode&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=anomalyco/opencode&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=anomalyco/opencode&type=date&legend=top-left" />
</picture>

It originated in the 2025 opencode-ai/Charm split that also produced Crush.
OpenCode is the continuation that kept the name, the domain, and the community.

## Strengths

- **The leanest measured harness of the majors**: about 7k baseline tokens versus about 33k for Claude Code, byte-stable cache prefixes, and about 3.7x cheaper on a matched pass/fail benchmark ([July 2026 proxy study](https://systima.ai/blog/claude-code-vs-opencode-token-overhead)).
- Truly provider-neutral, reading both AGENTS.md and CLAUDE.md.
- ACP support makes your editor choice irrelevant while keeping one harness.
- Undo/redo and share are small features that match how people actually work.

## Cautions

- **[CVE-2026-22812](https://cy.md/opencode-rce/)**: before v1.0.216 any website could execute code on your machine via the auto-started server; before v1.1.10 the server started silently; since v1.1.10 the server is off by default but still unauthenticated when enabled, with some vectors unfixed at disclosure.
- **[GHSA-632h-h47v-g4x4](https://securitylabs.datadoghq.com/articles/opencode-upgrade-remote-code-execution/)**: Datadog's September 24, 2026 disclosure of a second upgrade-path RCE, a content-type confusion in the `/global/upgrade` endpoint of the web interface exploitable cross-origin, fixed in 1.18.22; Anomaly declined to request a CVE, saying GitHub Security Advisories already cover the ground.
- Pin your version and read the config.
- In March 2026 [Anthropic legal requests](https://github.com/anomalyco/opencode/pull/18186) removed the Claude Pro/Max OAuth login and Anthropic-branded defaults, so your Claude subscription will not drive OpenCode; use API keys or Zen.
- Fast-moving config surface; the docs carry 'versions older than 0.1.x' style of breaking-change warnings.
- The docs site now defaults to V2, marked latest, with a V1 switcher and a Migrate from V1 page that says V1 plugins do not run in V2 and the V2 curl installer replaces the V1 binary (as of 2026-11-24); the v2-tagged-release gap closed on 2026-10-27 with v2.2.0: experimental desktop plugins (create, install, and share), a refreshed desktop app, experimental image and decision generation APIs in the plugins and SDK, keyed session-instruction entries that extend the prompt without busting the cache or starting an extra turn, and configurable prompt-cache TTLs per provider or model, with breaking changes moving the `@opencode/ai` package root to the Promise API (the Effect API now lives at `@opencode/ai/effect`), removing the OpenCode GitHub Action, and requiring OpenTUI 0.7 for TUI plugins; the v1.x train continues beside it, reaching v1.19.6 (2026-11-17: the desktop app offers the OpenCode 2.0 upgrade in place, keeping sessions, projects, and settings while v1 plugins need an update, history images past 25 MiB become placeholders, and an oversized-request provider error starts compaction and a retry instead of failing the turn), while the v2 train ran on through v2.4.0 and v2.4.1 (both November 23), v2.4.0 adding a built-in desktop browser with imported sign-ins and extensions, automations that run a prompt, a script, or a shell command on a timer, a cron schedule, or an MCP event through `/automation`, video generation through connected providers, a new default TUI look, and Windows taskbar status, with upgrade notes renaming the image tool to `generate_image`, auto-updating versioned plugins, moving Copilot to `COPILOT_GITHUB_TOKEN` instead of `GITHUB_TOKEN`, negotiating the newest MCP protocol first, and requiring OpenTUI 0.9.4 for TUI plugins, and v2.4.1 fixing assistant messages failing to save on macOS 12, compaction keeping more history than `keep.tokens`, and `/models` hiding config-only providers' models, after v2.3.2 (November 18, GPT-6.2 prompt caching fixed by sending the system prompt as a leading developer message on every Responses route so Copilot's gpt-6.2-sol uncached input per step fell from about 14,000 tokens to 3, and webfetch structured output no longer echoing its url and format), after v2.3.1 (also November 18, timed-out shell commands moving to the background instead of being killed, compaction summaries written in the background as a session nears the limit, GPT 6.2 Sol and Astra in the picker on ChatGPT sign-in, plugin updates from Settings, and selection comment tooling), after v2.3.0 (November 13, background subagents by default: subagents return immediately, continue in the background, and report back whenever they become idle so the parent session keeps working, quieter transcripts by default with each run of tool calls and thoughts summarized into one collapsible activity row until Verbosity is set to medium or high, and desktop jump-to-message through the command palette or Cmd+Alt+G), after v2.2.7 (November 10, GitHub Copilot Auto: pick Auto in the model picker when the Copilot account has an Auto pool and Copilot's router chooses each session's model at the Auto discount, falling back to the account's default chat model when routing fails, plus side-panel tab shortcuts), after v2.2.6 (November 6, shared MCP connection pooling, GUI plugin color themes, code-block action slots, and native settings and menu components) and v2.2.5 (October 30, desktop worktree and shell-mode shortcuts and comment-popup quote sends among the additions), after v1.19.4 (2026-10-22) bumped the bundled Bun to 1.4.4 for runtime security and v1.19.3 made configurable model reasoning options generate reasoning variants while preserving configured overrides.
- Windows works best under WSL.

## Pricing

The software is free and MIT.
**You pay providers directly for tokens**, or route through OpenCode Zen with its own billing.
There is no bundled subscription usage, which is the point.

## Compared to

- [Claude Code](../claude-code/index.md): the platform-in-a-subscription; costs more per token by design.
- [Crush](../crush/index.md): same ancestor, Go and FSL-licensed, prettier; pick OpenCode for MIT and the larger community.
- [aider](../aider/index.md): also BYOK, but pair-programming style rather than an autonomous loop.

## Bottom line

**Recommended as the default for token-paying, provider-switching engineers.**
Not for teams that need subscription billing simplicity or cannot audit a fast-moving open codebase.

## Changes

- 2026-08-22 - Created in the Harnesses category seed, recording CVE-2026-22812 and the Anthropic legal-request OAuth removal.
- 2026-08-23 - Style pass: bolded each section's key insight, hyperlinked in-body sources, and clarified referents.
- 2026-09-26 - Linked the new Model access notes for Zen and Go, where the gateway's billing and the token pack now have their own profiles.
- 2026-10-04 - Added the GHSA-632h-h47v-g4x4 upgrade-path RCE from Datadog's September 24 disclosure (fixed in 1.18.22, no CVE requested) and the v2-banner-versus-v1.18.x-releases versioning fact.
- 2026-10-07 - Added the anomalyco/opencode star history chart to the Status section.
- 2026-10-17 - Recorded the v1.x train reaching v1.19.3 (October 16), which made model reasoning options configurable into generated reasoning variants while preserving configured overrides, keeping the v2-tagged-release gap open.
- 2026-10-26 - Recorded the v1.x train reaching v1.19.4 (October 22), a runtime-security bump of the bundled Bun to 1.4.4, keeping the v2-tagged-release gap open; every cited URL re-fetched in the rotation pass.
- 2026-10-28 - Recorded the v2-tagged release gap closing: v2.2.0 (October 27) shipped experimental desktop plugins, a refreshed desktop app, image and decision generation APIs, cache-preserving session-instruction entries, and prompt-cache TTLs, with breaking SDK packaging changes and the OpenCode GitHub Action removed, and the v1.x train continued at v1.19.5 (October 28).
- 2026-11-01 - Recorded the v2 train reaching v2.2.5 (October 30, five stable releases in three days after v2.2.0): desktop worktree and shell-mode shortcuts, comment-popup quote sends, and further desktop-app polish, with the v1.x train parked at v1.19.5 and the default branch pushed 2026-11-01.
- 2026-11-07 - Recorded the v2 train reaching v2.2.6 (published November 6): shared MCP connections, pooling one connection across projects with the same setup so fewer processes run and starts are faster, plus GUI plugin color themes, code-block action slots, and native settings and menu components, with a process-daemon component train alongside (v0.4.0 October 29, v0.5.0 November 5) and the v1.x train still parked at v1.19.5.
- 2026-11-14 - Recorded the v2 train reaching v2.3.0 (published November 13): background subagents by default, returning immediately and reporting back when idle so the parent session keeps working, transcripts summarizing each run of tool calls and thoughts into one collapsible activity row until Verbosity is raised, and desktop jump-to-message, after the v2.2.7 Copilot Auto release (November 10) the Status prose already carried, and the default branch pushed 2026-11-14.
- 2026-11-17 - Recorded the v1.x train reaching v1.19.6 (published November 17): the desktop offering the OpenCode 2.0 upgrade in place with sessions and settings kept (v1 plugins need an update), history images past 25 MiB replaced with placeholders, and oversized-request provider errors starting compaction plus a retry, alongside the process-daemon component's v0.6.0 (November 16); the default branch pushed 2026-11-17.
- 2026-11-19 - Recorded the v2 train reaching v2.3.1 and v2.3.2 (both published November 18): background shell timeouts that keep running, background compaction summaries, GPT 6.2 models on ChatGPT sign-in, Settings plugin updates, then the GPT-6.2 prompt-caching fix sending the system prompt as a leading developer message on every Responses route (Copilot gpt-6.2-sol uncached input per step from about 14,000 tokens to 3).
- 2026-11-24 - Rotation re-verification, re-fetching every cited reference (all live): recorded the v2 train reaching v2.4.0 and v2.4.1 (both published November 23): a built-in desktop browser, automations on a timer, cron schedule, or MCP event through `/automation`, video generation, the new default TUI look, and Windows taskbar status, with upgrade notes renaming the image tool to `generate_image`, auto-updating versioned plugins, moving Copilot to `COPILOT_GITHUB_TOKEN`, and requiring OpenTUI 0.9.4 for TUI plugins, then the macOS 12 message-save fix; the v1.x train stays at v1.19.6 and the default branch was pushed 2026-11-24, against the repository's releases feed (the releases/latest endpoint keys the v1 train, so the work list carried no release flag).
- 2026-11-24 - Replaced the stale docs fact (a v2 banner) with the docs site defaulting to V2, marked latest, with a V1 switcher and a Migrate from V1 page, and moved the matrix scheduled-runs cell from host apps to the built-in automations.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the vendor-neutral slot in the harness layer
- [OpenCode Go](../../model-access/opencode-go/index.md) - the team's $10/month token pack, the subscription this harness's pricing note says it does not bundle
- [OpenCode Zen](../../model-access/opencode-zen/index.md) - the billing and pricing detail behind the curated gateway this note names
- [The Shifting Bottleneck](../../../the-shifting-bottleneck/index.md) - why lean harnesses matter as generation gets cheaper
- [Managing Many Concurrent LLM Agent Sessions](../../../managing-many-llm-agent-sessions/index.md) - what running several OpenCode sessions looks like
- [Claude Code](../claude-code/index.md) - the measured token-overhead comparison

## References

- https://opencode.ai/docs/ - the V2 (latest) docs: install through opencode.ai/v2/install or the `@opencode/cli` npm package, the built-in build and plan agents, commands, providers (the V1 docs sit behind the site's V1 switcher, as of 2026-11-24)
- https://opencode.ai/docs/migrate-v1/ - the V1 to V2 migration page: V1 plugins do not run in V2, and the V2 curl installer replaces the V1 binary
- https://api.github.com/repos/anomalyco/opencode/releases - the v1 and v2 release trains, v2.4.1 newest and v1.19.6 the v1 head (both fetched 2026-11-24)
- https://github.com/anomalyco/opencode - repository scale, MIT license, desktop builds, as of 2026-10-12
- https://github.com/anomalyco/opencode/pull/18186 - the March 2026 Anthropic legal-request removals
- https://cy.md/opencode-rce/ - CVE-2026-22812 disclosure with versions and mitigations
- https://securitylabs.datadoghq.com/articles/opencode-upgrade-remote-code-execution/ - the GHSA-632h-h47v-g4x4 disclosure (2026-09-24): attack flow, the 1.18.22 fix, and Anomaly's no-CVE reasoning, fetched 2026-10-04
- https://systima.ai/blog/claude-code-vs-opencode-token-overhead - the measured baseline and cache comparison
