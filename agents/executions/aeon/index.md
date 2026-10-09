---
title: Aeon
created: 2026-10-08
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, executions, github-actions, scheduling, autonomous-agents]
readability: 3
audience_notes: >
  Engineers who want an always-on personal agent running on their own GitHub Actions minutes and can accept a single-maintainer, token-adjacent project.
  Assumes you know Actions workflows and cron.
---

Aeon is an MIT-licensed framework that turns a GitHub repository plus Actions into an unattended agent, firing Markdown-file skills on cron, reactive triggers, or chains through any of nine coding-agent harnesses.

**Aeon has the deepest third-party unattended-agent trigger surface I have found, and the least governance: the project's own pitch, "no approval loops", is the caution.**

## What it is

An instance is a template copy of the aeon repo: skills (one SKILL.md prompt file each, 85 bundled), memory as committed Markdown, and an aeon.yml holding cron schedules.
A scheduler workflow ticks every five minutes and dispatches due skills to GitHub Actions, where they run through a harness adapter (Claude Code by default, plus Grok, Codex, Pi, Vibe, Kimi, fx, Cursor, and Hermes) against ten model gateways including a Claude subscription token.
Every run gets a Haiku quality score, failures file structured issues in the repo, and three consecutive failures auto-open a repair PR, which is the self-healing loop.
It is built by Aaron Elijah Mars (Aeon Inc), and deployment is a fork or template copy, so your repo is the runtime and your secrets stay in your repo's encrypted store.

## Status

**Active and single-maintainer.**
767 stars, 278 forks, and 1,427 commits as of 2026-10-08, created 2026-03-04 and pushed the day of this check.
The maintainer wrote about 88% of tracked contributor commits, and there is exactly one tagged release (v0.1.0, 2026-07-09), so development is trunk-based on main.
A Hacker News search returned no coverage as of 2026-10-08, and the fork count is inflated as an adoption signal because every deployed instance is a fork by design.
The project's proof-of-work page self-reports 141 vulnerability findings across 105 repositories (4.8M stars secured, counts as of 2026-09-28) with a link per fix, substantial evidence that is curated by the project itself.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=aeonfun/aeon&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=aeonfun/aeon&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=aeonfun/aeon&type=date&legend=top-left" />
</picture>

## Strengths

- **The trigger surface is the category's deepest outside the vendors**: five-minute cron, reactive triggers on run metrics (consecutive failures, success rate, last status), skill chains with parallel steps and score-gated routing, and Telegram inbound with slash commands plus an instant webhook mode.
- Git is the database: memory, run state, config, and the failure tracker are committed files, so the whole agent is inspectable and revertible with git alone.
- Nine harnesses behind one run contract and ten gateways mean a skill written once fires on any CLI, with a Claude subscription token as one of the credential options.
- The self-healing loop (score every run, file issues, auto-repair after three failures) is the most complete automated-maintenance story in this category.

## Cautions

- **The project is entangled with a crypto token**: the README links a $aeon token page and a wallet address, bundled skills move onchain funds (distribute-tokens) and deploy Uniswap v4 hooks that carry a mandatory 10 bps AeonFee, and several of the ten gateways are crypto-billed.
- Bus factor: one maintainer, one tagged release, and no third-party documentation.
- "No approval loops" is the design stance: auto-merge merges green PRs up to three per run, and cross-repo skills want a classic PAT with repo and workflow scopes.
- Skill blast radius is a self-declared frontmatter hint, not a sandbox; the docs say so, and nothing technical stops a mislabeled skill.
- No independent coverage or benchmarking exists as of 2026-10-08, so every quality claim traces back to the project's own pages.

## Pricing

Free and MIT-licensed; there is no Aeon tier.
Your costs are GitHub Actions minutes (free on public repos, metered on private) plus model inference on whichever gateway you connect, and the hosted Aeon Connect dashboard is free and stores no keys.

## Compared to

- [GitHub Agentic Workflows](../github-agentic-workflows/index.md): the vendor-built Actions layer compiles guarded workflows with cost caps and a firewall; Aeon is broader (chat inbound, run-metric triggers, self-healing, any harness) but swaps guardrails for self-declared capability hints.
- [Claude Code routines](../claude-code-routines/index.md): hosted scheduled sessions inside a Claude subscription with no repo artifacts; Aeon is repo-native, runs on your minutes, and keeps state in git.
- [n8n](../n8n/index.md): the SaaS-webhook canvas with an agents preview; Aeon is CLI-and-repo-native with skills instead of nodes and no hosted execution path.

## Bottom line

**Recommended for solo operators who want an always-on agent on their own Actions minutes, will read every SKILL.md before enabling it, and accept a single-maintainer token-adjacent project.**
Not for teams that need a governed execution layer (gh-aw is the answer there) or anyone unwilling to take a self-reported track record on faith.

## Changes

- 2026-10-08 - Created.

## See also

- [GitHub Agentic Workflows](../github-agentic-workflows/index.md) - the guardrail-first way to run agents on the same Actions runners
- [Claude Code routines](../claude-code-routines/index.md) - the hosted scheduler for Claude-subscribed teams
- [n8n](../n8n/index.md) - webhook-first automation with a preview agents layer
- [Claude Code](../../harnesses/claude-code/index.md) - the default harness every Aeon run drives

## References

- https://github.com/aeonfun/aeon - repository scale, template deployment model, MIT license, single release, founder line, as of 2026-10-08
- https://www.aeon.fun/docs - architecture, the 85-skill catalog, five-minute scheduler, reactive triggers, chains, harnesses, and gateways
- https://www.aeon.fun/security - the self-reported vulnerability-disclosure record (141 findings, 105 repositories, counts as of 2026-09-28)
- https://aaronjmars.com - the founder's own description of Aeon, MiroShark, and Hyperstitions
- https://hn.algolia.com/api/v1/search?query=aeonfun&tags=story - the coverage search that returned no hits, as of 2026-10-08
- https://api.github.com/repos/aeonfun/aeon - exact counters (created 2026-03-04, 767 stars, 278 forks, pushed 2026-10-08) and the single v0.1.0 release
