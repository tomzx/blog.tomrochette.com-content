---
title: Trigger.dev
created: 2026-10-10
updated: 2026-10-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, executions, scheduling, durable-execution, workflow-automation]
readability: 3
audience_notes: >
  Product engineers who need scheduled or event-triggered agent and workflow runs inside an application,
  deciding between Trigger.dev's cloud, self-hosting it, or one of this category's other execution layers.
  Assumes comfort with TypeScript, cron, and usage-based pricing.
---

Trigger.dev is an Apache-2.0 developer platform where you write agent and workflow tasks in TypeScript and run them on durable managed infrastructure triggered by cron schedules, SDK calls, and batches.

**Trigger.dev is the code-first execution layer this category was missing, and its one big catch is that the headline durability does not survive self-hosting: the checkpoint-resume machinery is a cloud-only feature by the vendor's own comparison table.**

## What it is

You write tasks in a `trigger` folder of your codebase, deploy them with the CLI, and Trigger.dev runs them with no timeouts, automatic retries, queues, and per-run observability.
Triggering comes from your backend code (`tasks.trigger()`), from other tasks (`triggerAndWait`), from batches of up to 1,000 runs, from durable cron schedules with IANA timezones, and, since 2026-10-26, from inbound webhooks in public beta.
The agents story is code, not canvas: documented guides cover the Vercel AI SDK and the Claude Agent SDK, and chat agents stream to your frontend with human-in-the-loop tool approvals.
It is built by API Hero Ltd (YC W23), deploys to Trigger.dev Cloud or self-hosted containers (a webapp plus a worker), and the current version is v4.8.2 (October 29).

## Status

**Active and mature, on its fourth major version.**
16,532 stars as of 2026-10-13 and 1,522 forks as of 2026-10-30, pushed 2026-10-29, with the repository created 2022-11-30.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=triggerdotdev/trigger.dev&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=triggerdotdev/trigger.dev&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=triggerdotdev/trigger.dev&type=date&legend=top-left" />
</picture>

The Hacker News record spans three launches: the v1 Show HN drew 745 points in February 2023, the V2 relaunch 172 points in October 2023, and the September 2025 Launch HN (162 points) confirmed the YC W23 backing and the CRIU checkpoint approach, with adoption there driven, in the CTO's account, by agents and workflows.
The v3-to-v4 transition shows the churn risk: v3 is end of life, 4.5.0 is the last release that runs v3 tasks, and 4.5.1 and later reject v3 triggers and deploys outright.

## Strengths

- **The trigger surface is the deepest code-first one in this category**: durable cron with timezones and load-spreading windows, thousands of per-user schedules on one task, delays, TTLs, idempotency keys, debounce, batch triggers of up to 1,000 runs, and, in beta since 2026-10-26, signature-verified inbound webhooks that route each event to up to 25 agents.
- Durability is the product: runs checkpoint via CRIU and resume on other machines, so waits and human-in-the-loop pauses burn no compute and survive redeploys.
- Everything is code in your repo: typed payloads, version control, deploy rollback, and preview branches, so the automation logic is reviewable like any other code.
- Observability ships with the platform: per-run tracing, LLM observability, replays, and alerts to email, Slack, or webhooks.

## Cautions

- **Self-hosting gives you the scheduler without the durability**: the vendor's own feature table marks checkpoints, warm starts, and auto-scaling as cloud-only, so a self-hosted wait blocks a worker instead of snapshotting it.
- Inbound webhooks are the youngest trigger surface in the category: the public beta landed 2026-10-26, and the 40-provider launch list, the Standard Webhooks and Svix support, and the 25-agent routing cap are all launch-day vendor claims (as of 2026-10-30).
- The free plan is a trial in practice: $5 of monthly credits and tasks stop when they run out, and free-plan schedules are capped at one run per hour with a forced 60-minute window.
- Usage pricing stacks two meters (per-second compute plus $0.000025 per run invocation), so chatty agent runs are hard to cost-predict without the billing alerts the dashboard offers.
- Major versions break: v3 reached end of life with 4.5.1 and later rejecting v3 deploys, an upgrade cliff every user, self-hosted or not, had to cross.

## Pricing

Cloud plans bill a monthly base plus usage: Free at $0 with $5 monthly credits, 20 concurrent runs, and 10 schedules; Hobby at $10/month with $10 credits and 50 concurrent runs; Pro at $50/month with $50 credits, 200+ concurrent runs, and 1,000+ schedules; Enterprise custom (as of 2026-10-20).
Usage bills per second of compute by machine size (Micro at $0.0000169 per second to Large 2x at $0.00068) plus $0.000025 per run invocation, and checkpointed waits do not count toward compute.
Self-hosting the Apache-2.0 platform is free but unsupported and, per the caution above, without checkpoints.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-10 | Cloud plans | Baseline: Free $0 ($5 monthly credits, 20 concurrent runs, 10 schedules), Hobby $10/mo ($10 credits, 50 concurrent), Pro $50/mo ($50 credits, 200+ concurrent, 1,000+ schedules), Enterprise custom; compute $0.0000169 to $0.00068 per second by machine plus $0.000025 per run. | [trigger.dev/pricing](https://trigger.dev/pricing) |

## Compared to

- [n8n](../n8n/index.md): the visual canvas with 1,500+ integrations under a fair-code license; Trigger.dev is code-first TypeScript under Apache-2.0, choose it when the automation logic belongs in your codebase.
- [GitHub Agentic Workflows](../github-agentic-workflows/index.md): repository chores compiled to guarded Actions runs; Trigger.dev runs application workloads, not repository maintenance.
- [Claude Code routines](../claude-code-routines/index.md): hosted scheduled sessions inside one vendor's subscription; Trigger.dev runs any code against any provider on infrastructure you can also self-host.

## Bottom line

**Recommended for product engineers who need scheduled or event-triggered agent workloads inside an application, in TypeScript, and will pay for cloud durability or accept the self-hosted feature gap.**
Not for repository chores (gh-aw is the fit) or visual integration glue (n8n).
My disagreeable claim: calling Trigger.dev open source and self-hostable is only half the story, because the checkpointing that makes runs durable is exactly what you give up when you leave their cloud, and most buyers will not notice until a long-running wait eats their workers.

## Changes

- 2026-10-10 - Created.
- 2026-10-11 - Refreshed the repository counters (16,510 to 16,516 stars, 1,486 to 1,489 forks) and re-confirmed v4.7.3 current and the pricing tiers unchanged.
- 2026-10-16 - Recorded the v4.7.4 release (2026-10-14); the pricing tiers re-verified unchanged against the pricing page.
- 2026-10-22 - Recorded the v4.7.5 and v4.7.6 releases (both 2026-10-20), moving the current-version claim from v4.7.4 (October 14), and refreshed the repository counters (1,508 forks, pushed 2026-10-22).
- 2026-10-24 - Recorded the v4.8.0 and v4.8.1 releases (both 2026-10-23), moving the current-version claim from v4.7.6 (October 20); the repository counters re-verified around them (1,508 forks, pushed 2026-10-24).
- 2026-10-30 - Fully re-verified in rotation with every cited URL re-fetched: recorded the v4.8.2 release (2026-10-29) and the public-beta inbound-webhooks launch (2026-10-26, 40+ named providers including GitHub, Slack, and Stripe, Standard Webhooks and Svix support, signature verification, dedup, and routing to up to 25 agents per event), with the webhooks changelog added as a reference; the pricing tiers (Free $0, Hobby $10, Pro $50, Enterprise custom, per-second compute plus $0.000025 per run), the self-hosted cloud-only feature table, the v3 end-of-life cliff, the cron timezone and window behavior with the free-plan hourly floor, and the three HN launch threads (162, 745, and 172 points) all re-confirmed; the counters refreshed (1,522 forks, pushed 2026-10-29).

## See also

- [n8n](../n8n/index.md) - the visual-canvas execution platform
- [GitHub Agentic Workflows](../github-agentic-workflows/index.md) - the repo-automation counterpart on Actions
- [Claude Code routines](../claude-code-routines/index.md) - the hosted scheduler inside Claude subscriptions
- [Claude Code](../../harnesses/claude-code/index.md) - the harness behind the Claude Agent SDK guide

## References

- https://github.com/triggerdotdev/trigger.dev - repository scale, Apache-2.0 license, deployment model, as of 2026-10-13 (counters verified via the GitHub API the same run)
- https://api.github.com/repos/triggerdotdev/trigger.dev - exact counters (16,532 stars pinned at their 2026-10-13 fetch, 1,522 forks, pushed 2026-10-29, created 2022-11-30; re-verified 2026-10-30) and the Apache-2.0 license
- https://api.github.com/repos/triggerdotdev/trigger.dev/releases?per_page=5 - the v4.8.2 release (2026-10-29, re-fetched 2026-10-30) following v4.8.0 and v4.8.1 (both 2026-10-23)
- https://trigger.dev/ - product surface, the agents pitch, the Apache-2.0 and self-hosting statements, and the Webhooks beta changelog banner (re-fetched 2026-10-30; the API Hero Ltd company footer last confirmed 2026-10-11)
- https://trigger.dev/pricing - plan tiers, per-second machine rates, and the per-run invocation fee, as of 2026-10-11 (tiers re-verified unchanged 2026-10-30)
- https://trigger.dev/docs/triggering - trigger functions, batches, delays, TTLs, idempotency keys, and debounce (re-fetched 2026-10-30)
- https://trigger.dev/docs/tasks/scheduled - cron schedules, IANA timezones, load-spreading windows, and the free-plan hourly floor (re-fetched 2026-10-30)
- https://trigger.dev/docs/self-hosting/overview - the self-hosted feature gap (no checkpoints, warm starts, or auto-scaling) and v3 end of life, the vendor's own table (critical source, re-fetched 2026-10-30)
- https://trigger.dev/changelog/webhooks-beta - the public-beta inbound-webhooks launch (2026-10-26): 40+ named providers, Standard Webhooks and Svix support, signature verification, dedup, and routing to up to 25 agents per event
- https://news.ycombinator.com/item?id=45250720 - the September 2025 Launch HN (162 points): YC W23, CRIU checkpointing, cloud-first direction
- https://news.ycombinator.com/item?id=34610686 - the February 2023 v1 Show HN (745 points)
- https://news.ycombinator.com/item?id=37750763 - the October 2023 V2 relaunch as a Temporal alternative (172 points)
