---
title: Claude Code routines
created: 2026-10-06
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, executions, claude-code, scheduling]
readability: 3
audience_notes: >
  Teams on Claude subscriptions who want Claude Code sessions to start themselves on schedules, API calls, or GitHub events, without a machine left awake.
  Assumes you know what a Claude Code session is and how GitHub branch protections work.
---

Claude Code routines are saved prompt, repository, and connector configurations that run as unattended Claude Code cloud sessions on a schedule, on an API call, or on GitHub events.

**Routines complete Claude Code's execution story with the scheduled half, and their default posture (full autonomy, every connector attached, green status on mere infrastructure success) makes them the highest-blast-radius unattended agent in this category.**

## What it is

A routine packages a prompt, one or more GitHub repositories, and a set of MCP connectors, then runs as a full Claude Code session on Anthropic-managed cloud infrastructure (or a routed self-hosted environment), so nothing depends on your laptop being open.
One routine can combine three trigger types: a schedule (hourly minimum, presets, custom cron, and one-offs), an API endpoint that fires on an authenticated POST, and GitHub repository events (pull request and release events, with author, label, branch, draft, and regex filters).
It shipped in research preview on 2026-04-14, is available on Pro, Max, Team, and Enterprise plans, and is managed at claude.ai/code/routines or conversationally from the CLI with `/schedule`.

## Status

**Active and invested, in research preview.**
The April 2026 launch drew a 720-point Hacker News thread, and the docs record steady churn since (the CLI's `/schedule` arrived in v2.1.225, run-history inspection in v2.1.227, and the stored-prompt trust model changed in v2.1.213).
The `/fire` endpoint is still flagged experimental, though the dated beta header is now optional.
Anthropic published free routine templates around it and third parties already sell hardened routine packs, which is community traction of a kind.

## Strengths

- **One routine, three trigger kinds**: the same definition can run nightly, fire from a deploy script, and react to new pull requests.
- GitHub filters go deep: author, title, body, base and head branch, labels, draft, and merged state, with regex on any field.
- The API trigger wraps caller-supplied text in an untrusted-data block, so a leaked token delivers labeled context rather than instructions.
- Runs are full sessions you can open, read, and continue by hand, and the org-level kill switch is server-side, so an owner can actually stop them.

## Cautions

- **There is no permission-mode picker**: a routine runs shell commands and calls every tool of every included connector without approval, and all of your account's connectors are included by default, write scopes included.
- A run is creator-private, like Copilot automations: routines belong to the individual claude.ai account, teammates cannot see them, and admins get only the on/off toggle.
- Green run status means the session started and exited without an infrastructure error, not that the task succeeded, and independent practitioners document silent-failure modes (unreadable sources rendered as empty results, delayed fires, dropped GitHub events at the caps).
- Caps are hard: 100 scheduled runs per account-hour, 30 fires per routine-hour shared with Run now, GitHub events beyond the caps dropped until the window resets, and no overage without usage credits.
- Scheduled intervals bottom out at one hour, and an exactly-on-the-hour start can slip several minutes late (Anthropic suggests 9:07 over 9:00).

## Pricing

Included with Claude Pro, Max, Team, and Enterprise plans; there is no separate routines tier.
Runs draw down subscription usage like interactive sessions, and organizations with usage credits enabled can keep running on metered overage past the subscription limit.

## Compared to

- [GitHub Copilot automations](../copilot-automations/index.md): the same hosted, creator-private pattern on GitHub's side, metered in Actions minutes and AI credits instead of subscription usage.
- [Claude Code hooks](../claude-code-hooks/index.md): event triggers inside a live session; routines start whole sessions from outside any session.
- [GitHub Agentic Workflows](../github-agentic-workflows/index.md): the in-repo, versioned alternative when the automation logic itself should be reviewed like code.

## Bottom line

**Recommended for Claude-subscribed teams that need nightly maintenance or PR-event sessions and will contain writes with branch protections and pruned connectors.**
Not for anyone who needs automations a team can audit, or who cannot tolerate research-preview churn in the trust model.
My disagreeable claim: shipping every account connector into an unattended run by default, with no per-run approval gate, is Anthropic optimizing for a magic demo over safe defaults, and the fire-payload wrapping shows the team knows unattended input is hostile territory.

## Changes

- 2026-10-06 - Created.

## See also

- [GitHub Copilot automations](../copilot-automations/index.md) - the GitHub-side hosted sibling with the same creator-private governance hole
- [Claude Code hooks](../claude-code-hooks/index.md) - the in-session event surface these out-of-session triggers complement
- [GitHub Agentic Workflows](../github-agentic-workflows/index.md) - the in-repo, versioned route to the same chores
- [Claude Code](../../harnesses/claude-code/index.md) - the harness every routine run instantiates
- [OpenChamber](../../surfaces/openchamber/index.md) - self-hosted cron scheduling on your own machine, outside any subscription

## References

- https://code.claude.com/docs/en/routines - triggers, autonomy model, limits, plan availability, as of 2026-10-06
- https://claude.com/blog/introducing-routines-in-claude-code - the April 2026 announcement and launch limits
- https://news.ycombinator.com/item?id=47768133 - the 720-point launch discussion
- https://platform.claude.com/docs/en/api/claude-code/routines-fire - the /fire endpoint contract, token scoping, and rate limits
- https://runbook.scosovan.com/claude-code-routine-reported-success-did-nothing/ - independent post-mortem on silent failures and the connector default (critical source)
