---
title: Claude Code hooks
created: 2026-08-24
updated: 2026-10-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, executions, claude-code, hooks]
readability: 3
audience_notes: >
  Engineers already running Claude Code who want deterministic control over what the agent does between prompts.
  Assumes you know the JSON settings files and can write a small shell script.
---

Claude Code hooks are user-defined shell commands, HTTP endpoints, or LLM prompts that Claude Code runs automatically at specific points in its lifecycle, turning the harness itself into an event-driven system.

**Hooks are the only mechanism in Claude Code that gives you deterministic control, and I consider them mandatory before pointing the harness at anything you care about.**

## What it is

Hooks live in JSON settings files at four scopes (user, project, local, and organization-managed policy) plus plugin manifests, skill frontmatter, and subagent frontmatter, and plugins can also register hooks as JavaScript functions in their own process (the docs' mods surface).
**The event surface has grown to 33 lifecycle points**: session start and end, prompt submit, before and after every tool call, permission requests, compaction, subagent start and stop, file changes on disk, and config changes.
Handlers come in five types: shell commands, HTTP POSTs, MCP tool calls, single-turn prompt evaluations, and experimental multi-turn agent hooks.
The same hook events fire in the terminal, IDE extensions, the desktop app, and Claude Code on the web, and they also fire inside subagents.

## Status

**Active and heavily invested in.**
The feature ships in the proprietary CLI tracked by the `anthropics/claude-code` repository (about 150.7k stars as of 2026-10-13, roughly 16.1k open issues as of 2026-10-30).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=anthropics/claude-code&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=anthropics/claude-code&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=anthropics/claude-code&type=date&legend=top-left" />
</picture>

A third-party ecosystem exists: an HN search surfaces several hundred stories mentioning Claude Code hooks as of 2026-10-25, including dedicated tooling like Graft, whose August 2026 launch thread drew 44 comments.
Anthropic's own security-guidance plugin is built entirely on hooks (SessionStart, UserPromptSubmit, PostToolUse, Stop), which signals production commitment.

## Strengths

- **Determinism where the model cannot be trusted to behave**: formatting after edits, blocking destructive commands, re-injecting context after compaction, and desktop notifications all run whether or not the model remembers.
- Handler diversity (command, HTTP, MCP tool, prompt, agent) covers both deterministic rules and judgment calls in one config system.
- Enterprise controls exist: `allowManagedHooksOnly` restricts hooks to managed policy, and HTTP hooks require URL allowlists with env-var interpolation limits.
- Async and `asyncRewake` hooks run in the background and can wake Claude when a long check fails, so guardrails do not block the loop.

## Cautions

- **The `if` filter fails open**: the docs say plainly that because it is best-effort, you should use the permission system, not a hook, to enforce a hard allow or deny.
- Matcher semantics are version-gated and event-specific (FileChanged and StopFailure accept only pipe separators while every other event also accepts commas, StopFailure's `cloud_credential_error` matcher needs v2.1.267 or later, and the `onFailure` block-on-failure field v2.1.295), so a config can silently change meaning across client versions, and agent hooks are experimental.
- Cloud sessions do not read `~/.claude/settings.json`, so your personal hooks quietly disappear on the web.
- Prompt and agent handlers add model calls: Anthropic's own plugin docs estimate roughly one review call per turn that changes files plus a deeper review per commit.

## Pricing

Included with Claude Code, so the pricing is the harness's (Pro, Max, or API billing), but prompt and agent hooks consume usage like any other request.
There is no separate hooks tier.

## Compared to

- GitHub Copilot hooks: the same lifecycle-trigger idea in Copilot cloud agent and CLI, but bound to GitHub's ecosystem rather than your local shell.
- [Claude Code routines](../claude-code-routines/index.md): scheduled execution in Claude's cloud; hooks are event-triggered inside a session, routines are cron outside it.
- [OpenChamber](../../surfaces/openchamber/index.md): schedules prompts on cron across sessions, but does not intercept the tool loop itself.

## Bottom line

**Recommended for every team running Claude Code on real repositories; policy enforced in hooks and permission rules is the only enforcement that survives an indifferent model.**
Not for one-off interactive use, where the config overhead buys little.
I would go further: a team that relies on prompt instructions instead of PreToolUse hooks has not yet adopted agentic coding safely, and readers who think prompts are enough may disagree.

## Changes

- 2026-08-24 - Created in the Executions category seed.
- 2026-08-30 - Corrected the open-issue count from 5k+ to about 15k after it proved materially wrong.
- 2026-09-18 - Refreshed the repository counters (about 145.2k to about 146k stars, roughly 12.4k to roughly 12.5k open issues).
- 2026-09-29 - Refreshed the repository counters (about 148.5k stars, roughly 13.6k open issues) and re-dated the reference.
- 2026-10-06 - Refreshed the event count to 33 per the current reference table, re-grounded the matcher version-gating caution on the current docs after the older version claims left the page, and linked the new Claude Code routines note.
- 2026-10-07 - Added the anthropics/claude-code star history chart to the Status section.
- 2026-10-11 - Refreshed the repository counters (about 150.0k to about 150.1k stars) and corrected the HN story count from roughly 500 to roughly 450 against the current search; the 33-event count and all doc claims re-verified unchanged.
- 2026-10-18 - Replaced the churning HN story count with "several hundred" (the same query moved between about 450 and about 500 within the month) and refreshed the open-issue count to roughly 15.2k; the 33-event surface and the five handler types re-verified against the live reference after the 2026-10-17 push.
- 2026-10-25 - Fully re-verified in rotation with every cited URL re-fetched: the 33-event surface, the five handler types, the four scopes plus skill and subagent frontmatter, the fail-open `if` filter, the FileChanged/StopFailure pipe-only matcher rule, and the security-guidance hook map all re-confirmed against the live docs; replaced the stale v2.1.214 `if` directory-pattern example, which left the current page, with the version gates the page now carries (StopFailure's `cloud_credential_error` matcher at v2.1.267, `onFailure` at v2.1.295), added the plugin mods function-hook surface, and re-dated the counters and HN footprint (517 stories, several hundred).

## See also

- [Claude Code](../../harnesses/claude-code/index.md) - the harness these triggers live inside
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - where the harness sits in the four-layer map
- [OpenChamber](../../surfaces/openchamber/index.md) - the cron-style counterpart for scheduled runs outside the session
- [Claude Code routines](../claude-code-routines/index.md) - the hosted scheduler that fires whole sessions where hooks fire inside one

## References

- https://code.claude.com/docs/en/hooks - event reference, handler types, matcher semantics, fail-open caution (re-fetched 2026-10-30; the 33-event table, the five handler types, and the v2.1.267 and v2.1.295 matcher and `onFailure` gates all still present)
- https://code.claude.com/docs/en/hooks-guide - quickstart, deterministic-control framing, usage costs of model-backed hooks
- https://code.claude.com/docs/en/security-guidance - the official plugin built entirely on hooks
- https://github.com/anthropics/claude-code - repository scale, as of 2026-10-30
- https://news.ycombinator.com/item?id=49299985 - third-party hooks tooling (Graft) and community scrutiny of its benchmark claims
