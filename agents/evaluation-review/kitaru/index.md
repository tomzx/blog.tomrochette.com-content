---
title: Kitaru
created: 2026-10-14
updated: 2026-10-31
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation-review, replay-evals, regression-testing]
readability: 3
audience_notes: >
  Engineers running an AI agent in front of users who need to know whether the next prompt, model, or code change regresses production behavior before it ships.
  Assumes you know what a trace store (Langfuse, Phoenix) and a regression test are.
---

Kitaru is ZenML's Apache-2.0 replay-based eval platform: it turns recorded or imported production agent runs into sessions it can re-execute against your next change, so you learn what improved and what broke before shipping.

**Its bet is that production traffic is already the eval set, and the missing piece is a runtime that can re-run it safely; its discipline is that an unchanged replay must reproduce the original before any forked replay can be trusted.**

## What it is

A self-hosted platform from ZenML GmbH, the ML-pipelines company: one FastAPI + Postgres server you run in Docker or Helm, plus workers that execute replays inside your own environment, with Python and TypeScript SDKs, a CLI, and an MCP server and agent skills so a coding assistant drives the loop.
Sessions arrive two ways: recording adapters that wrap your agent once (PydanticAI, LangGraph, OpenAI Agents SDK, Claude Agent SDK, Mastra, Vercel AI SDK), or importers for the traces you already collect from Langfuse, LangSmith, Braintrust, Logfire, Arize Phoenix, and MLflow.
Replays answer tool calls from the recording under per-tool policies (history, static, or passthrough), so the re-run issues no second refund and touches no live system.
Evaluations start from you: an investigation has your coding assistant interview you over the sessions that matter and pin your verdicts to exact trace locations, and those judgments calibrate the evaluators that later gate changes.

## Status

Active and vendor-backed: 308 stars, 26 forks as of 2026-10-14, last push 2026-10-30, with the repository created 2026-03-05.
The release train is fast and coordinated: PyPI 0.27.3 and TypeScript SDK 0.7.0 shipped together on 2026-10-30, with the adapter packages versioned in step, and roughly 9,900 PyPI downloads in the last month (pypistats, as of 2026-10-31), the one adoption receipt here that is not self-reported.
It has already pivoted once: launched March 2026 as open-source infrastructure for async agents, carried a durable-runtime framing through July, and relaunched on 2026-08-18 around replay-based evals with Workers replacing the old Stacks concept, and parts of the docs still describe the older flows-and-checkpoints framing.
The standalone kitaru.ai site folded into zenml.io in October 2026: the pricing page is now a Kitaru workspace tab on zenml.io/pricing, the relaunch post moved to the ZenML blog, and the pricing FAQ says one subscription covers both products on one bill.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=zenml-io/kitaru&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=zenml-io/kitaru&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=zenml-io/kitaru&type=date&legend=top-left" />
</picture>

**The footprint is thin: three HN submissions (2026-03-25, 2026-04-22, 2026-07-06) hold 2-3 points and one comment between them, I found no third-party writeup, and no outside contributor has more than nine commits against the lead maintainer's 721.**
The docs are candid about the fit in both directions, naming prototype teams as the wrong audience, which is the self-skepticism this category rarely volunteers.

## Strengths

- Replay re-executes your actual agent code against the recorded world instead of re-scoring outputs, the distinction its own docs draw against every eval platform here.
- Human judgment is the seed, and evaluators must agree with your pinned verdicts before they gate anything, so the gate inherits a checked calibration rather than a vibe.
- The cohort that caught a production failure becomes the CI regression gate, closing the trace-to-test-suite loop the other columns leave open.
- Imports from six trace stores mean nothing in your production path changes; your observability stack stays the system of record.
- A funded vendor with a track record (ZenML, SOC 2 and ISO 27001) and a sustained multi-package release cadence behind it.

## Cautions

- Near-zero independent reception: the HN record never moved, no third-party coverage exists, and the companion skills repository holds 6 stars.
- Mid-pivot documentation: pages describing the old durable-runtime framing (flows, checkpoints, stacks) sit beside the new eval framing under the same name, a trap for anyone following older links.
- Replay fidelity is conditional: the OpenAI Agents adapter cannot use a history default, the default tool policy passes calls through to live tools (the docs warn a replayed refund call refunds again), and an unrecorded tool call fails the replay.
- Cloud caps bite at scale: one AI agent and 100 pipeline runs a month on the $39 Starter plan push growing teams toward Enterprise.
- The calibration check is only as good as the reviewed sample; a gate calibrated on a handful of pinned judgments inherits their blind spots.

## Pricing

Open source and self-hosted free under Apache-2.0.
Cloud is one flat Starter plan at $39 per month (one AI agent, one ML project, unlimited seats, 100 pipeline runs a month), with a 14-day trial needing no credit card.
Enterprise is custom-priced (multi-workspace, on-prem or air-gapped, your own LLM endpoint, SSO/SCIM, audit logs, SLA).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-14 | Cloud | recorded at the $39/month flat launch plan (3 agents, 2 seats, 90-day retention), 14-day full-access trial | https://kitaru.ai/pricing |
| 2026-10-31 | Starter (Cloud) | $39 unchanged, tier reshaped: one AI agent and one ML project with unlimited seats and 100 pipeline runs a month, replacing the 3-agent, 2-seat, 90-day-retention launch terms | https://www.zenml.io/pricing |

## Compared to

- [Langfuse](../langfuse/index.md): the observability platform Kitaru imports from and positions beside; Langfuse tells you what happened, Kitaru re-runs it, and most teams would run both.
- [Phoenix](../phoenix/index.md): the same relationship on the OTel-native side, a second import source that stays the system of record.
- [deepeval](../deepeval/index.md): the pytest-style framework judging outputs you supply; Kitaru sources its cases from production and re-executes them, so choose deepeval for CI-first judging without a trace store.

## Bottom line

**Recommended for teams with an agent in front of users whose regression process today is a few samples and a vibe check, and who want production cases, expert judgment, and replay turning into a CI gate.**
Not for prototypes (its own docs say it will feel like more machinery than you need) and not for anyone who requires an independently validated tool, because the third-party record does not exist yet.

## Changes

- 2026-10-14 - Created.
- 2026-10-21 - Rotation re-verification: recorded the kitaru.ai fold into zenml.io (pricing as a Kitaru workspace tab, one subscription across both products), moved the pricing and relaunch-post references to their new zenml.io URLs, and refreshed the activity line; every cited URL re-fetched and live.
- 2026-10-31 - Rotation re-verification folded into the volatile pass after the coordinated 2026-10-30 releases: PyPI 0.27.3 and TypeScript SDK 0.7.0 recorded, the Starter tier's reshaped terms (one agent, one ML project, unlimited seats, 100 pipeline runs a month) moved into Pricing with a Price history row, and every cited URL re-fetched and live.

## See also

- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins
- [Langfuse](../langfuse/index.md) - the trace store Kitaru treats as the system of record and imports from
- [Phoenix](../phoenix/index.md) - the other import-source observability platform
- [deepeval](../deepeval/index.md) - the CI-gating eval framework judging outputs you supply instead of production replays
- [Kiln](../kiln/index.md) - the other human-judgment-first member: GUI ratings seed judge metrics there, pinned interviews seed replay evaluators here

## References

- https://github.com/zenml-io/kitaru - repository, Apache-2.0, stars, forks, push activity, adapter and importer tables, self-hosting description (as of 2026-10-14, verified through the GitHub API and raw README)
- https://docs.zenml.io/kitaru - the record/replay/improve loop, the five-step method, the who-it-is-for caution, and the workers-in-your-environment architecture
- https://www.zenml.io/blog/introducing-the-new-kitaru - the 2026-08-18 relaunch: cohorts, evaluator calibration against expert verdicts, tool policies, the Stacks-to-Workers pivot, and the positioning against Langfuse, Braintrust, and LangSmith (moved from kitaru.ai in October 2026)
- https://www.zenml.io/pricing - Open Source free, Kitaru Cloud $39/month with 3 agents, 2 seats, and 90-day retention, Enterprise custom (the Kitaru workspace tab; moved from kitaru.ai)
- https://pypi.org/project/kitaru/ - package record: 0.27.3 (2026-10-30), 56 published versions, Python >=3.11 (verified through the PyPI JSON API, the HTML page is client-rendered)
- https://pypistats.org/api/packages/kitaru/recent - roughly 9,900 downloads in the last month as of 2026-10-31
- https://news.ycombinator.com/item?id=48807786 - the July 2026 Show HN under the current positioning, 2 points, no comments, the thin-reception evidence (verified through the HN Algolia item API, with the 2026-03-25 and 2026-04-22 submissions at items 47520115 and 47863502)
- https://github.com/zenml-io/kitaru-skills - companion agent-skills repository, 6 stars, last push 2026-10-30
