---
title: Langfuse
created: 2026-09-16
updated: 2026-11-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, evaluation, observability, llm-as-judge]
readability: 3
audience_notes: >
  Engineers who need production-grade tracing and evaluation for LLM applications and agents under a license their employer will accept.
  Assumes you know what a trace, an LLM-as-judge eval, and open core mean.
---

Langfuse is an open-source (MIT core) observability and evaluation platform for LLM applications and agents, covering tracing, LLM-as-judge and human evaluation, prompt management, and datasets and experiments, self-hostable or consumed as Langfuse Cloud, and part of ClickHouse since January 2026.

**Langfuse is the MIT-licensed observability and evaluation column the category lacked, and its open-core boundary is drawn in the filesystem: MIT outside the `ee/` directories, proprietary inside them.**

## What it is

A self-hostable web platform (Docker Compose locally, Kubernetes templates for production) or Langfuse Cloud, instrumented through Python and JS SDKs, OpenTelemetry, an LLM gateway such as LiteLLM, or the docs' 100-plus library and framework integrations.
Traces, sessions, users, and costs land in a UI where agents render as graphs; evaluation attaches to the same data through managed LLM-as-judge evaluators, custom code evaluators, user feedback, manual annotation queues, and custom score APIs.
Prompt management versions and deploys prompts with server and client caching, a playground iterates on them, and datasets and experiments run pre-deployment evaluations against them.
Made by Langfuse (YC W23), acquired by ClickHouse in January 2026, with the root LICENSE copyright now reading ClickHouse, Inc.

## Status

Mature and busy: 35,785 stars, 3,984 forks as of 2026-10-13 (captured once at note level; the chart is the live signal), created 2023-05-18, pushed 2026-11-27 (the default branch's latest commit, 2026-11-27, an evals gallery score-chip fix after 2026-11-26 commits adding response guardrails for JSON and SSE outputs in the AI gateway and JWT authentication for ClickHouse Cloud), with v4.88.0 (2026-11-26, organizations and instances able to disable public trace and session sharing, a redact guardrail action in the AI gateway, MCP spans recording client capabilities and extensions, and the onboarding API key created as a named Developer key) and v4.87.0 (2026-11-26, the evaluated observation marked in the sample trace view, AI-gateway requests blocked or logged when their last turn matches a guardrail, a reset-budget action for users and API keys, and Topics summary rate-limit backoff) after v4.86.0 (2026-11-24, charts rendered inline as an MCP App, tool calls read from OpenAI Responses output items in the native path, and a tool-column ingestion normalization fix) and v4.85.0 (2026-11-24, Stripe metering from the billable units ledger, a self-serve enterprise trial redeemed by coupon code, trace evaluator testing and trace rule management on the server, and Topics and events dispatch on self-hosted instances) after v4.84.0 (2026-11-23, organization-wide spend budgets in the AI gateway, the billable-events ledger shipped as a ClickHouse migration, the member role hierarchy replaced by an ownership rule, opt-in native OpenTelemetry direct processing, organization-scoped model definitions, and a batchCreateAnnotationQueueItems MCP tool) and v4.83.0 (2026-11-19, a Topics scatter view replacing the list, per-key spend limits and per-user budgets in the AI gateway, IAM role auth for Bedrock connections, and the MCP server moving to the 2026-07-28 protocol revision with a batchCreateScores tool) and v4.82.0 (2026-11-17, audit logs read from ClickHouse, API-key presets renamed, an SSRF fix in GitHub Enterprise SSO, and evals pausing an LLM connection on provider 429s instead of retrying in-call) and v4.81.0 (2026-11-16, Google Vertex AI added as an AI-gateway provider, Gemini decision models in evaluators, dataset items filterable by status, and Topics snapshots with on-demand map refresh) after v4.80.0 (2026-11-13) and v4.79.0 (2026-11-12) and v4.78.0 (2026-11-10) and v4.77.0 (2026-11-09) after v4.76.0 (2026-11-05), v4.75.0 (2026-11-04), v4.74.0 and v4.73.0 (both 2026-11-03), and v4.72.0 (2026-10-29), as of 2026-11-27.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=langfuse/langfuse&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=langfuse/langfuse&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=langfuse/langfuse&type=date&legend=top-left" />
</picture>

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
- OTel-ingested cost aggregates had a cache-accounting bug: the generic GenAI usage extractor missed the official `gen_ai.usage.cache_write.input_tokens` alias, so cache-write tokens were double-counted into input sums and priced at zero; the fix merged on 2026-09-07 (PR 17129) and first shipped in v4.34.0 (2026-09-11), the issue itself closed 2026-09-14, so only builds older than v4.34.0, and traces backfilled across that window, carry the skew.
- It observes applications you instrument, not coding sessions a harness already wrote, so it does not answer this blog's session-analytics questions.

## Pricing

Self-hosted: free, MIT core, with the `ee/` directories under their separate license.
Langfuse Cloud as of 2026-10-11: Hobby free (50k units/month, 30-day retention), Core $29/month, Pro $199/month (Teams add-on $300/month), Enterprise $2,499/month, plus graduated overage from $8 down to $6 per 100k units.

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
- 2026-10-03 - Recorded the v4.50.0 release (2026-10-02) and refreshed repository counts.
- 2026-10-06 - Recorded the v4.51.0 release (2026-10-05) and refreshed repository counts.
- 2026-10-07 - Added the langfuse/langfuse star history chart to the Status section.
- 2026-10-07 - Recorded the v4.52.0 and v4.53.0 releases (both 2026-10-06) and refreshed repository counts.
- 2026-10-08 - Recorded the v4.54.0 release (2026-10-07) and refreshed repository counts.
- 2026-10-09 - Recorded the v4.55.0 release (2026-10-08) and refreshed repository counts.
- 2026-10-10 - Recorded the v4.56.0 release (2026-10-09) and refreshed repository counts; cloud pricing re-verified unchanged.
- 2026-10-13 - Recorded the v4.57.0 release (2026-10-12) and refreshed repository counts.
- 2026-10-13 - Recorded the v4.58.0 release (2026-10-13) and refreshed repository counts.
- 2026-10-16 - Recorded the v4.59.0 (2026-10-14) and v4.60.0 (2026-10-15) releases and refreshed the activity line.
- 2026-10-17 - Recorded the v4.61.0, v4.62.0, and v4.63.0 releases (all 2026-10-16), and added the OTel cache-write accounting caution from the flagged issue 17117 (reported 2026-09-07, closed by the fix 2026-09-14).
- 2026-10-18 - Sharpened the cache-accounting caution with the fix's landing: merged 2026-09-07 (PR 17129), first shipped in v4.34.0 (2026-09-11), issue closed 2026-09-14, so the caution now names the exact safe build.
- 2026-10-21 - Recorded the v4.64.0 (2026-10-19) and v4.65.0 and v4.66.0 (both 2026-10-20) releases and refreshed the activity line.
- 2026-10-23 - Recorded the v4.67.0 (2026-10-21) and v4.68.0 (2026-10-22) releases and refreshed the activity line.
- 2026-10-25 - Recorded the v4.69.0 (2026-10-23) and v4.70.0 (2026-10-24) releases and refreshed the activity line.
- 2026-10-27 - Recorded the v4.70.1 release (2026-10-26) and refreshed the activity line.
- 2026-10-28 - Recorded the v4.71.0 release (2026-10-27) and refreshed the activity line.
- 2026-10-30 - Recorded the v4.72.0 release (2026-10-29) and refreshed the activity line.
- 2026-11-05 - Recorded the v4.73.0 and v4.74.0 releases (both 2026-11-03) and the v4.75.0 release (2026-11-04) and refreshed the activity line.
- 2026-11-07 - Recorded the v4.76.0 release (2026-11-05) and refreshed the activity line.
- 2026-11-11 - Recorded the v4.77.0 (2026-11-09) and v4.78.0 (2026-11-10) releases and refreshed the activity line.
- 2026-11-13 - Recorded the v4.79.0 release (2026-11-12) and refreshed the activity line.
- 2026-11-14 - Recorded the v4.80.0 release (2026-11-13, ClickHouse query parameters sent in the request body by default and Google AI Studio added as an AI-gateway provider) and refreshed the activity line (the default branch moved 2026-11-13 with Topics snapshots and on-demand map refresh, the repository-level 2026-11-14 push being side-branch activity).
- 2026-11-18 - Recorded the v4.81.0 (2026-11-16, Google Vertex AI as an AI-gateway provider, Gemini decision models in evaluators, dataset-item status filters, Topics snapshots and on-demand refresh) and v4.82.0 (2026-11-17, audit logs read from ClickHouse, the API-key preset rename, an SSRF fix in GitHub Enterprise SSO configuration, and evals pausing a connection on provider 429 instead of retrying in-call) releases and refreshed the activity line.
- 2026-11-20 - Recorded the v4.83.0 release (2026-11-19, a Topics scatter view replacing the list, per-key spend limits and per-user budgets in the AI gateway, IAM role auth for Bedrock connections, and the MCP server moving to the 2026-07-28 protocol revision with a batchCreateScores tool) and refreshed the activity line (the default branch's latest commit 2026-11-20).
- 2026-11-21 - Rotation re-verification: every cited URL re-fetched and live (repository, LICENSE, README, docs, pricing page with every tier and the graduated overage unchanged, release line, the cache-accounting issue and fix, the v4.34.0 tag, and the three HN threads), pushed date moved to 2026-11-21, v4.83.0 still the newest release.
- 2026-11-22 - Refreshed the activity line: pushed date moved to 2026-11-22 with the billable-units work landing on the default branch (an org endpoint exposing billable units per project, the org usage breakdown reading from the ledger, and tRPC sign-in 401s logged at debug level on 2026-11-21, then continued-topic naming on 2026-11-22); v4.83.0 still the newest release.
- 2026-11-24 - Recorded the v4.84.0 release (2026-11-23, organization-wide spend budgets in the AI gateway, the billable-events ledger shipped as a ClickHouse migration, the member role hierarchy replaced by an ownership rule, opt-in native OpenTelemetry direct processing, organization-scoped model definitions, and a batchCreateAnnotationQueueItems MCP tool) and refreshed the activity line (the default branch's latest commit 2026-11-23); cloud pricing re-verified unchanged.
- 2026-11-25 - Recorded the v4.85.0 and v4.86.0 releases (both 2026-11-24: Stripe metering from the billable units ledger, a self-serve enterprise trial by coupon code, trace evaluator testing and trace rule management, and Topics on self-hosted instances; then inline charts as an MCP App, OpenAI Responses tool-call reading in the native path, and a tool-column ingestion fix) and refreshed the activity line (the default branch's latest commit 2026-11-24).
- 2026-11-27 - Recorded the v4.87.0 and v4.88.0 releases (both 2026-11-26: the evaluated observation marked in the sample trace view, AI-gateway last-turn guardrail blocking, and a reset-budget action; then organization-level disabling of public trace and session sharing, a redact guardrail action, MCP client capabilities on MCP spans, and a named Developer onboarding key) and refreshed the activity line (the default branch's latest commit 2026-11-27).

## See also

- [Phoenix](../phoenix/index.md) - the closest peer and the license contrast that decides between them
- [deepeval](../deepeval/index.md) - the eval-framework alternative when the gate is CI
- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins
- [Hamel Husain](../../people-and-publications/hamel-husain/index.md) - the eval-driven methodology these platforms implement

## References

- https://github.com/langfuse/langfuse - repository, description, stars and forks, pushed date as of 2026-10-13
- https://raw.githubusercontent.com/langfuse/langfuse/main/LICENSE - MIT core, the `ee/` carve-out, and the ClickHouse, Inc. copyright
- https://raw.githubusercontent.com/langfuse/langfuse/main/README.md - feature set, self-hosting, integrations, and the January 2026 ClickHouse note
- https://langfuse.com/docs - platform overview, OTel basis, evaluation methods, agent skill, CLI, and MCP server
- https://langfuse.com/pricing - cloud tiers, billable units, graduated overage, self-host FAQ, named customers
- https://github.com/langfuse/langfuse/releases - release cadence evidence (v4.51.0 through v4.56.0)
- https://github.com/langfuse/langfuse/issues/17117 - the OTel cache-write token accounting bug (reported 2026-09-07, closed 2026-09-14) behind the caution
- https://github.com/langfuse/langfuse/pull/17129 - the cache-write normalization fix (merged 2026-09-07)
- https://github.com/langfuse/langfuse/releases/tag/v4.34.0 - the first release carrying the fix (2026-09-11), confirmed by tag containment
- https://news.ycombinator.com/item?id=46656552 - the acquisition thread, 220 points, with the open-core and consolidation concerns
- https://news.ycombinator.com/item?id=42441258 - the 2024 Launch HN thread, 215 points, including the LangSmith comparison
- https://news.ycombinator.com/item?id=37310070 - the 2023 Show HN thread, 143 points
