---
title: Claude Code hooks
created: 2026-08-24
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, executions, claude-code, hooks]
readability: 3
audience_notes: >
  Engineers already running Claude Code who want deterministic control over what the agent does between prompts.
  Assumes you know the JSON settings files and can write a small shell script.
---

Claude Code hooks are user-defined shell commands, HTTP endpoints, or LLM prompts that Claude Code runs automatically at specific points in its lifecycle, turning the harness itself into an event-driven system.
Facts below verified as of 2026-08-30.

**Hooks are the only mechanism in Claude Code that gives you deterministic control, and I consider them mandatory before pointing the harness at anything you care about.**

## What it is

Hooks live in JSON settings files at four scopes (user, project, local, and organization-managed policy) plus plugin manifests, skill frontmatter, and subagent frontmatter.
**The event surface has grown to roughly 30 lifecycle points**: session start and end, prompt submit, before and after every tool call, permission requests, compaction, subagent start and stop, file changes on disk, and config changes.
Handlers come in five types: shell commands, HTTP POSTs, MCP tool calls, single-turn prompt evaluations, and experimental multi-turn agent hooks.
The same hook events fire in the terminal, IDE extensions, the desktop app, and Claude Code on the web, and they also fire inside subagents.

## Status

**Active and heavily invested in.**
The feature ships in the proprietary CLI tracked by the `anthropics/claude-code` repository (about 143.5k stars and roughly 15k open issues as of 2026-08-30).
A third-party ecosystem exists: an HN search surfaces 467 stories mentioning Claude Code hooks, including dedicated tooling like Graft, whose August 2026 launch thread drew 44 comments.
Anthropic's own security-guidance plugin is built entirely on hooks (SessionStart, UserPromptSubmit, PostToolUse, Stop), which signals production commitment.

## Strengths

- **Determinism where the model cannot be trusted to behave**: formatting after edits, blocking destructive commands, re-injecting context after compaction, and desktop notifications all run whether or not the model remembers.
- Handler diversity (command, HTTP, MCP tool, prompt, agent) covers both deterministic rules and judgment calls in one config system.
- Enterprise controls exist: `allowManagedHooksOnly` restricts hooks to managed policy, and HTTP hooks require URL allowlists with env-var interpolation limits.
- Async and `asyncRewake` hooks run in the background and can wake Claude when a long check fails, so guardrails do not block the loop.

## Cautions

- **The `if` filter fails open**: the docs say plainly that because it is best-effort, you should use the permission system, not a hook, to enforce a hard allow or deny.
- Matcher semantics are version-gated (comma separators need v2.1.191+, hyphens v2.1.195+), so a config can silently change meaning across client versions, and agent hooks are experimental.
- Cloud sessions do not read `~/.claude/settings.json`, so your personal hooks quietly disappear on the web.
- Prompt and agent handlers add model calls: Anthropic's own plugin docs estimate roughly one review call per turn that changes files plus a deeper review per commit.

## Pricing

Included with Claude Code, so the pricing is the harness's (Pro, Max, or API billing), but prompt and agent hooks consume usage like any other request.
There is no separate hooks tier.

## Compared to

- GitHub Copilot hooks: the same lifecycle-trigger idea in Copilot cloud agent and CLI, but bound to GitHub's ecosystem rather than your local shell.
- Claude Code routines: scheduled execution in Claude's cloud; hooks are event-triggered inside a session, routines are cron outside it.
- [OpenChamber](../openchamber/index.md): schedules prompts on cron across sessions, but does not intercept the tool loop itself.

## Bottom line

**Recommended for every team running Claude Code on real repositories; policy enforced in hooks and permission rules is the only enforcement that survives an indifferent model.**
Not for one-off interactive use, where the config overhead buys little.
I would go further: a team that relies on prompt instructions instead of PreToolUse hooks has not yet adopted agentic coding safely, and readers who think prompts are enough may disagree.

## See also

- [Claude Code](../claude-code/index.md) - the harness these triggers live inside
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where the harness sits in the four-layer map
- [OpenChamber](../openchamber/index.md) - the cron-style counterpart for scheduled runs outside the session

## References

- https://code.claude.com/docs/en/hooks - event reference, handler types, matcher semantics, fail-open caution
- https://code.claude.com/docs/en/hooks-guide - quickstart, deterministic-control framing, usage costs of model-backed hooks
- https://code.claude.com/docs/en/security-guidance - the official plugin built entirely on hooks
- https://github.com/anthropics/claude-code - repository scale, as of 2026-08-30
- https://news.ycombinator.com/item?id=49299985 - third-party hooks tooling (Graft) and community scrutiny of its benchmark claims
