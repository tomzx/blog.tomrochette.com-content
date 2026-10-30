---
title: Crush
created: 2026-08-22
updated: 2026-10-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, coding-agents, harnesses, terminal, go]
readability: 3
audience_notes: >
  Terminal-heavy engineers evaluating Charm's LSP-enhanced coding agent.
  Assumes you know what a language server does and what FSL licensing means.

---

Crush is Charm's terminal coding agent: a single Go binary that pulls context from language servers, runs any provider including local models, and carries the [FSL-1.1-MIT](https://fsl.software/) license.

**Crush is the best-looking and most portable harness in the field, and a license plus an origin story that community has not forgotten will keep it the second choice for teams that audit provenance.**

## What it is

**An LSP-enhanced TUI: language servers feed it context the way they would an IDE, on top of multi-model chat with mid-session model switching.**
It speaks MCP (stdio, http, sse, with OAuth), supports the Agent Skills standard including Claude-format skill directories, and initializes projects with an AGENTS.md (plus CRUSH.md for Crush-specific rules).
Configuration is a `crushrc`, which is literally Bash, and its model catalog auto-updates from [Catwalk](https://github.com/charmbracelet/catwalk), a community database.
It runs on macOS, Linux, Windows, Android, and the BSDs.

## Status

**Active.**
About 28.6k stars and 2.3k forks as of 2026-10-17, and 4,390 commits as of 2026-10-30, launched July 30, 2025, with v0.99.0 (October 29, 2026) the latest release, the Catwalk v3 rework: the provider `type` now names the API format a provider speaks (`completions`, `responses`, or `messages`) with config migrated automatically on load, hooks follow the whole run (sessions, turns, permissions, and more) validated against a known-events list, a client/server mode arrived, `--can-reason` became `--thinking always|never|toggleable`, and `--max-attachments` plus friendly reasoning-level names in the picker landed, after v0.98.2 (October 23, 2026) added the built-in `keanu` theme and OpenRouter sticky-routing headers, re-signed-in every OAuth provider on a rejected credential, and fixed a crash when parallel tool calls finish together, after v0.98.1 (October 9) routed newer Copilot models through the Responses API and v0.98.0 the day before.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=charmbracelet/crush&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=charmbracelet/crush&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=charmbracelet/crush&type=date&legend=top-left" />
</picture>

It is the continuation of the original opencode-ai repository: creator Kujtim Hoxha joined Charm, and the repo moved with him.
After the dispute that split the community, Charm renamed it Crush while the other developers kept the OpenCode name.
Charm's own telling is ["Crush, come home"](https://charm.land/blog/crush-comes-home/); the other side's version lives in [the launch thread](https://news.ycombinator.com/item?id=44736176).

## Strengths

- **The LSP integration is the differentiator**: definitions and diagnostics as context, not just grep.
- A Go binary with no runtime dependency chain, on more platforms than anyone else bothers to support.
- Reads AGENTS.md, CLAUDE.md conventions via global config, and even Cursor and Claude skill directories.
- FSL-1.1-MIT converts every version to real MIT two years after release.

## Cautions

- **Not open source by OSI definitions**: FSL restricts competing use for two years per version; some teams will fail policy on it.
- The 2025 fork fight (repository move, history edits alleged, name split) still colors trust, and you should read both accounts before standardizing on it.
- Launch-era reviews reported weaker planning, more tokens, and rough edges versus OpenCode; verify against current releases before relying on those impressions either way.
- No subscription login: providers need API keys, including Anthropic.
- `crushrc` is arbitrary shell code; the [README](https://github.com/charmbracelet/crush) itself warns not to launch Crush in an unreviewed directory.

## Pricing

The tool is free under FSL-1.1-MIT.
**BYOK means your providers bill you directly**; Charm sells Hyper, its own subscription provider with a free tier and zero data retention, pitched as the optimized default.
No stable public pricing page existed at verification time, per the README.

## Compared to

- [OpenCode](../opencode/index.md): same ancestor, MIT, bigger community; the safer institutional pick.
- [aider](../aider/index.md): also BYOK, REPL-feel; choose aider when you want no frills.
- [Claude Code](../claude-code/index.md): subscription platform; the comparison is polish versus portability.

## Bottom line

**Recommended for engineers who want the best-looking terminal, LSP lovers, and local-model users.**
Not for license-restricted organizations or communities that relitigate 2025.

## Changes

- 2026-08-22 - Created in the Harnesses category seed.
- 2026-08-22 - Removed type: post per the section-wide owner rules change.
- 2026-08-23 - Style conformance pass: sources hyperlinked, per-section insights bolded, sentences split, showy wording replaced.
- 2026-09-16 - Refreshed repository scale to about 28.1k stars and 4,181 commits.
- 2026-10-07 - Added the charmbracelet/crush star history chart to the Status section.
- 2026-10-17 - Recorded the v0.98.0 and v0.98.1 releases (October 8 and 9, the latter routing newer Copilot models through the Responses API), refreshed the commit count, and re-fetched every cited reference in the rotation pass.
- 2026-10-24 - Recorded the v0.98.2 release (October 23): the built-in `keanu` theme, OpenRouter app-attribution and sticky-routing headers, OAuth sign-in and credential-refresh fixes, and a crash fix for parallel tool calls finishing together.
- 2026-10-29 - Rotation re-verification, re-fetching every cited reference (all live) and refreshing the commit count to 4,375, with v0.98.2 still the newest release.
- 2026-10-30 - Recorded the v0.99.0 release (October 29): the Catwalk v3 provider-model rework with automatic config migration, run-wide hooks validated against a known-events list, a client/server mode, and `--thinking` replacing `--can-reason`; commits refreshed to 4,390.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - Crush in the independent tail of the harness layer
- [Iterating on Agent Skills](../../../iterating-on-agent-skills/index.md) - the skill format Crush adopted
- [The Shifting Bottleneck](../../../the-shifting-bottleneck/index.md) - why context quality (LSP) matters more than generation
- [OpenCode](../opencode/index.md) - the sibling it split from

## References

- https://github.com/charmbracelet/crush - features, license, provider matrix, as of 2026-10-17
- https://news.ycombinator.com/item?id=44736176 - launch thread with the full origin story and early comparisons
- https://fsl.software/ - what FSL-1.1-MIT permits and when it converts
- https://charm.land/blog/crush-comes-home/ - Charm's account of the project joining the company
- https://github.com/charmbracelet/catwalk - the community model database behind provider auto-update
