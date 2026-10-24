---
title: Claude Code Action
created: 2026-10-11
updated: 2026-10-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, executions, github-actions, claude-code, scheduling]
readability: 3
audience_notes: >
  Maintainers who already use Claude Code and want it answering issues and reviewing pull requests unattended.
  Assumes you know GitHub Actions workflows, secrets, and what installing a GitHub App grants.
---

Claude Code Action is Anthropic's official GitHub Action that runs Claude Code inside your repository's workflows, answering @claude mentions, working issues, and turning them into pull requests without a person starting each run.

**It is the reference event-triggered coding agent on GitHub: official, the largest in its class by stars, and the path Claude's own docs recommend, and its guardrails are opt-in workflow flags rather than a compiled gate, so the security posture is exactly what the workflow author configures.**

## What it is

One action (`anthropics/claude-code-action`) you wire into `.github/workflows`, installed against a GitHub App whose setup is a single `/install-github-app` command from Claude Code.
Interactive mode fires on the trigger phrase (@claude by default, customizable) in issues, pull requests, and comments, plus optional label and assignment triggers; automation mode takes an explicit `prompt` input and runs on whatever event you attach, including cron schedules.
It executes entirely on your own Actions runners and authenticates to Claude through an Anthropic API key, a Claude subscription, or one of the cloud providers (Amazon Bedrock, Google Vertex AI, Microsoft Foundry).
It is MIT-licensed, built by Anthropic, and versioned through a dense v1.0.x release train (v1.0.261 on 2026-10-23), with a documented migration path from the 2025 beta; the GitHub Latest badge still sits on the v1.0 announcement release of 2025-08-26.

## Status

**Active, official, and large.**
9,497 stars as of 2026-10-13, 2,213 forks and 835 open issues and pull requests as of 2026-10-24 (GitHub API), created 2025-05-19 and pushed 2026-10-24.
The release train is the opposite of stalled: the repo publishes a v1.0.x release per merge (v1.0.261 on 2026-10-23, three days after v1.0.258), while the Latest badge stays pinned to the v1.0 announcement release of 2025-08-26, so a `/releases/latest` check reads this action as frozen when it ships almost daily.
Hacker News has no dedicated launch thread; the most substantive coverage is a July 2025 post describing an accidental prompt injection through the action (8 points, zero comments), which is the representative failure mode for every mention-triggered agent.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=anthropics/claude-code-action&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=anthropics/claude-code-action&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=anthropics/claude-code-action&type=date&theme=dark&legend=top-left" />
</picture>

## Strengths

- **The trigger surface is the smoothest in the category**: one command installs the app, workflow, and secret, and @claude then works in issues, pull requests, and comments, with the phrase, labels, and assignments all configurable.
- Interactive and automation modes are the same action, so a mention bot and a scheduled maintenance task share one setup.
- The docs' solutions guide ships ready-made workflows for scheduled maintenance, issue triage and labeling, path-scoped reviews, and external-contributor handling.
- Runs land on your own runners with four provider paths, so inference follows whichever Claude channel your team already pays for.

## Cautions

- **The security docs flag their own sharp edges in capitals**: `allowed_non_write_users` is marked RISKY, and `allowed_bots: '*'` on a public repository lets any external GitHub App trigger the action with a prompt it controls.
- Prompt injection through untrusted issue and comment content stays the documented residual risk; secret scrubbing and optional bubblewrap PID-namespace isolation "reduces but does not eliminate" it, in the docs' own words, so workflow permissions must be minimized by hand.
- Claude Code only: no engine choice and no safe-outputs compilation, which is the gap GitHub Agentic Workflows sells against.
- 835 open issues and pull requests is a heavy backlog for an official action at this scale (as of 2026-10-24).

## Pricing

The action is free and MIT-licensed.
Runs cost GitHub Actions minutes plus Claude usage billed to whichever channel you configure: an Anthropic API key, a Claude subscription, or Bedrock, Vertex AI, and Foundry equivalents.

## Compared to

- [GitHub Agentic Workflows](../github-agentic-workflows/index.md): the multi-engine compiler with safe outputs, cost caps, and a firewall; choose it when guardrails and engine choice matter more than the mention workflow.
- [Run Gemini CLI](../run-gemini-cli/index.md) and [Codex Action](../codex-action/index.md): the Google and OpenAI parallels, each single-engine like this one.
- [GitHub Copilot automations](../copilot-automations/index.md): the hosted sibling with no workflow files, private repositories only.

## Bottom line

**Recommended for repositories already committed to Claude Code that want issue triage and PR review on mentions, on their own runners.**
Not for multi-engine shops (GitHub Agentic Workflows fits) or anyone unwilling to treat the RISKY flags as untouchable.
My disagreeable claim: the mention workflow is the best default in this category, and it is also the easiest one to configure dangerously, because the flag that lets outsiders trigger Claude is one line long.

## Changes

- 2026-10-11 - Created from the 2026-10-11 official-Actions family admission, with the injection surface recorded as the critical angle.
- 2026-10-17 - Corrected the release story: the action ships a dense v1.0.x train (v1.0.252 on 2026-10-16) rather than holding at the 2025-08-26 v1 tag, whose announcement release merely keeps the Latest badge; found by the volatile pass after new releases landed.
- 2026-10-24 - Fully re-verified in rotation with every cited URL re-fetched: the README, the security docs (the RISKY flags, secret scrubbing, bubblewrap isolation, the bot-allowlist warning, and the new per-actor comment filters), the usage docs, the official GitHub Actions docs, the repo page, the no-dedicated-launch-thread search, and the July 2025 injection report (8 points, zero comments) all re-confirmed; the release train moved to v1.0.261 (2026-10-23) and the counters refreshed (2,213 forks, 835 open issues and pull requests).

## See also

- [GitHub Agentic Workflows](../github-agentic-workflows/index.md) - the multi-engine compiled alternative on the same platform
- [Claude Code](../../harnesses/claude-code/index.md) - the harness this action runs
- [Claude Code routines](../claude-code-routines/index.md) - scheduled Claude sessions without workflow files
- [Claude Code hooks](../claude-code-hooks/index.md) - in-session lifecycle triggers versus repository events

## References

- https://github.com/anthropics/claude-code-action - repository, 9,497 stars, MIT license, as of 2026-10-13
- https://api.github.com/repos/anthropics/claude-code-action - exact counters (9,497 stars pinned at their 2026-10-13 fetch, 2,213 forks, 835 open issues and pull requests, pushed 2026-10-24, created 2025-05-19; re-verified 2026-10-24)
- https://raw.githubusercontent.com/anthropics/claude-code-action/main/README.md - trigger detection, provider paths, v1.0 migration note, solutions catalog
- https://raw.githubusercontent.com/anthropics/claude-code-action/main/docs/security.md - the RISKY flags, secret scrubbing, bubblewrap PID-namespace isolation, and bot-allowlist warnings
- https://raw.githubusercontent.com/anthropics/claude-code-action/main/docs/usage.md - label and phrase triggers, automation prompts, plugin inputs
- https://code.claude.com/docs/en/github-actions - official docs: interactive and automation modes, write-access checks, schedule runs, CLAUDE.md standards
- https://api.github.com/repos/anthropics/claude-code-action/releases?per_page=100 - the v1.0.x release train (v1.0.261 on 2026-10-23, re-fetched 2026-10-24) and the v1.0 announcement release still carrying the Latest badge (2025-08-26, re-fetched 2026-10-24)
- https://hn.algolia.com/api/v1/search?query=claude%20code%20github%20actions&tags=story - the coverage scan finding no dedicated launch thread (2026-10-11, re-checked 2026-10-24)
- https://news.ycombinator.com/item?id=44527916 - the July 2025 accidental prompt-injection report (8 points, zero comments), the critical source
