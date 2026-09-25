---
title: Langfuse
created: 2026-09-16
updated: 2026-09-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation, observability, llm-as-judge]
readability: 3
audience_notes: >
  Engineers who need production-grade tracing and evaluation for LLM applications and agents under a license their employer will accept.
  Assumes you know what a trace, an LLM-as-judge eval, and open core mean.
---

Langfuse is an open-source (MIT core) observability and evaluation platform for LLM applications and agents, covering tracing, LLM-as-judge and human evaluation, prompt management, and datasets and experiments, self-hostable or consumed as Langfuse Cloud, and part of ClickHouse since January 2026.
Facts below verified as of 2026-09-25.

**Langfuse is the MIT-licensed observability and evaluation column the category lacked, and its open-core boundary is drawn in the filesystem: MIT outside the `ee/` directories, proprietary inside them.**

## What it is

A self-hostable web platform (Docker Compose locally, Kubernetes templates for production) or Langfuse Cloud, instrumented through Python and JS SDKs, OpenTelemetry, an LLM gateway such as LiteLLM, or the docs' 100-plus library and framework integrations.
Traces, sessions, users, and costs land in a UI where agents render as graphs; evaluation attaches to the same data through managed LLM-as-judge evaluators, custom code evaluators, user feedback, manual annotation queues, and custom score APIs.
Prompt management versions and deploys prompts with server and client caching, a playground iterates on them, and datasets and experiments run pre-deployment evaluations against them.
Made by Langfuse (YC W23), acquired by ClickHouse in January 2026, with the root LICENSE copyright now reading ClickHouse, Inc.

## Status

Mature and busy: 35,022 stars, 3,843 forks, created 2023-05-18, pushed 2026-09-24, v4.45.2 released 2026-09-24 as of 2026-09-25.
Announced ClickHouse acquisition landed on Hacker News on 2026-01-17 with 220 points, and the README says the team doubled in the six months before it.
**Three years old, the largest community in this category, and now owned by a database vendor whose observability stack it slots into.**

## Strengths

- The most permissive core license in the observability tier: MIT lets you self-host, modify, and even sell what ELv2-licensed rivals reserve.
- The full loop in one platform: tracing, evaluation, prompt management, datasets, and experiments, natively integrated rather than bolted together.
- OpenTelemetry-based ingestion keeps exit costs visible, and an agent skill, CLI, and MCP server let coding agents work with it directly.
- Real production pull: the pricing page names Canva, Twilio, Ramp, and Khan Academy, and the docs ship an interactive demo project.

## Cautions

- The `ee/` split is structural: SSO, RBAC depth, and other enterprise features live in proprietary modules, so "MIT" describes the core, not the edges.
- Ownership changed hands, and the acquisition thread carries the standard open-core worries ("fine as long as all these open source projects stay open source") alongside consolidation takes about data vendors absorbing observability.
- Cloud billing counts every trace, observation, and score as a unit, then charges $8 per 100k beyond the plan allowance, so high-volume tracing bills creep.
- It observes applications you instrument, not coding sessions a harness already wrote, so it does not answer this blog's session-analytics questions.

## Pricing

Self-hosted: free, MIT core, with the `ee/` directories under their separate license.
Langfuse Cloud as of 2026-09-25: Hobby free (50k units/month, 30-day retention), Core $29/month, Pro $199/month (Teams add-on $300/month), Enterprise $2,499/month, plus graduated overage from $8 down to $6 per 100k units.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-18 | Langfuse Cloud | Baseline: Hobby free (50k units/mo, 30-day retention), Core $29/mo, Pro $199/mo (Teams add-on $300/mo), Enterprise $2,499/mo, graduated overage from $8 down to $6 per 100k units; self-hosted core free (MIT). Re-verified unchanged 2026-09-25. | [langfuse.com/pricing](https://langfuse.com/pricing) |

## Compared to

- [Phoenix](../phoenix/index.md): the closest feature peer; choose Langfuse when the MIT core matters and you want prompt management built in, Phoenix for OpenInference instrumentation breadth and the Arize AX upgrade path, remembering Phoenix's core is ELv2.
- [deepeval](../deepeval/index.md): a pytest-style framework that gates CI on eval failures; choose it when the eval suite must block merges, Langfuse when production traces need evaluating and the team lives in a dashboard.
- LangSmith: the commercial incumbent; a Launch HN commenter described rejecting it over coupling concerns with the vendor's framework, which is the independence argument Langfuse runs on.

## Bottom line

**Recommended for teams that want production tracing, evaluation, and prompt management in one self-hostable platform under a permissive license, accepting open-core edges and ClickHouse ownership.**
Not for pytest-style CI gating (use deepeval) or for observing coding-agent sessions a harness already wrote on disk (that is the session-analytics category's job).

## Changes

- 2026-09-16 - Created.
- 2026-09-18 - Recorded the v4.38.0 release and refreshed repository counts.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-25 - Recorded the v4.45.2 release and refreshed repository counts; cloud pricing re-verified unchanged.

## See also

- [Phoenix](../phoenix/index.md) - the closest peer and the license contrast that decides between them
- [deepeval](../deepeval/index.md) - the eval-framework alternative when the gate is CI
- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins
- [Hamel Husain](../../people-and-publications/hamel-husain/index.md) - the eval-driven methodology these platforms implement

## References

- https://github.com/langfuse/langfuse - repository, description, stars and forks, pushed date as of 2026-09-18
- https://raw.githubusercontent.com/langfuse/langfuse/main/LICENSE - MIT core, the `ee/` carve-out, and the ClickHouse, Inc. copyright
- https://raw.githubusercontent.com/langfuse/langfuse/main/README.md - feature set, self-hosting, integrations, and the January 2026 ClickHouse note
- https://langfuse.com/docs - platform overview, OTel basis, evaluation methods, agent skill, CLI, and MCP server
- https://langfuse.com/pricing - cloud tiers, billable units, graduated overage, self-host FAQ, named customers
- https://github.com/langfuse/langfuse/releases - v4.36.1 release date
- https://news.ycombinator.com/item?id=46656552 - the acquisition thread, 220 points, with the open-core and consolidation concerns
- https://news.ycombinator.com/item?id=42441258 - the 2024 Launch HN thread, 215 points, including the LangSmith comparison
- https://news.ycombinator.com/item?id=37310070 - the 2023 Show HN thread, 143 points
