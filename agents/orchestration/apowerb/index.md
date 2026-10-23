---
title: apowerb
created: 2026-10-21
updated: 2026-10-22
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, agents, self-hosted, open-core]
readability: 3
audience_notes: >
  Teams that want unattended business agents (inbox triage, reports, CRM updates) running on
  their own infrastructure, with quotas and audit trails. Assumes you are comfortable with
  Docker Compose or Helm and bring your own model keys.
---

apowerb is an Apache-2.0, self-hosted Python platform for building and running production AI agents: agents defined in a web UI or REST API, stored in Postgres, executed on Google's ADK with any model through LiteLLM, orchestrated in base, parallel, sequential, or loop patterns with hierarchical sub-agents, and triggered on demand, on a schedule, by email, or by webhook.

**apowerb's bet is that orchestration is the easy part and the plumbing is the product: business tools, triggers, audit, and quotas in one Docker Compose stack.**

## What it is

A Python stack from thaink² (its founder posted the HN threads): a FastAPI server, a Typer CLI, a REST API, and a companion Next.js interface, deployable with Docker Compose or Helm.
Agents are defined in the database and materialized as Python modules at startup, then executed through Google ADK, with LiteLLM in front of Anthropic, OpenAI, Mistral, Gemini, Azure AI Foundry, OVHcloud, and other providers, so model choice never touches agent code.
The toolset is the pitch: 24-plus tool modules covering Google Workspace, Microsoft 365, GitHub, HubSpot, Pipedrive, Odoo, SQL databases, Oracle, MongoDB, S3, web search, OCR, speech, and sandboxed Python, plus built-in RAG over files, URLs, query results, and S3 buckets, and Text-to-SQL against your own schema.
Orchestration covers the four execution patterns plus hierarchical sub-agents, and runs start from a chat, a schedule, a new Gmail or Outlook message, or a webhook, each leaving an auditable session trace.
It is an open core by declaration: the published package is a complete generic server, while billing, identity-provider sign-in, MFA, token accounting and quotas, B2B prospecting, agent evaluation, and the administration panel are commercial bricks that are absent from the open-source build, not flag-gated.

## Status

Young and shipping fast: 149 stars and 22 forks as of 2026-10-21, repository created 2026-07-29, default-branch push 2026-10-22, PyPI at 0.2.95 with 140 releases in under three months, three of them on 2026-10-20 alone (GitHub API and PyPI, as of 2026-10-22).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=apowerb/apowerb&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=apowerb/apowerb&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=apowerb/apowerb&type=date&theme=dark&legend=top-left" />
</picture>

The independent footprint is the founder's own HN threads, a four-point Show HN with one reply and a five-point Helm-chart post, with no third-party coverage found as of 2026-10-21.
**Three months, 135 releases, and no outside voice yet: the velocity is documented, the corroboration is not.**

## Strengths

- The business-systems toolset is the deepest in its cohort: two office suites, two CRMs, an ERP, and four database families as built-in modules rather than a plugin hunt.
- Unattended by design: schedules, email triggers, and webhooks start agents without anyone in the chat, and every run leaves a session trace.
- The open-core line is drawn in public: commercial features are absent from the build rather than crippled behind a flag, per the editions page's own framing.
- LiteLLM plus ADK keeps agent code independent of model vendor, and agents stay scriptable, reviewable, and reproducible in Postgres rather than trapped in a canvas.
- Helm support puts a Kubernetes path next to the Docker Compose default.

## Cautions

- Three months old with a 135-release train: expect churn, and pin versions.
- The README claims per-user token quotas as an open-source production control, but the editions page lists token accounting and quotas among the commercial bricks absent from the open-source build; verify against the release you run (as of 2026-10-21).
- Agent evaluation left the core in 0.2.0, so the judge logic is now a paid brick.
- No coding-agent story: this orchestrates business agents, not worktrees or pull requests.
- Adoption is thin: 149 stars and self-posted threads only, so production references do not exist yet.

## Pricing

Open core: the published package is Apache-2.0 and complete for its scope, and you pay your own model and hosting bills.
thaink² sells the commercial bricks (billing, identity-provider sign-in, MFA, token accounting and quotas, B2B prospecting, agent evaluation, the administration panel) separately, with no public price list as of 2026-10-21.

## Compared to

- [Agno](../agno/index.md): also a Python agent platform with a paid control plane, but agent-framework-first rather than business-integration-first; choose apowerb when the tools you need are Outlook and Odoo, not agent primitives.
- [Dify](../dify/index.md): the visual-canvas incumbent with the larger ecosystem; apowerb defines agents in a UI or API over Postgres and competes on the built-in business toolset.
- [AutoGPT](../autogpt/index.md): the hosted-plus-self-host workflow platform with a marketplace; apowerb is narrower and more operational, aimed at unattended back-office runs with quotas and audit.

## Bottom line

Recommended for teams automating business back-offices (inbox triage, scheduled reports, CRM updates) with unattended agents on their own infrastructure.
Not for coding-agent orchestration, and not without pinning versions and verifying the quota claim against your build.

## Changes

- 2026-10-21 - Created.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Agno](../agno/index.md) - the closest framework-plus-control-plane sibling
- [Dify](../dify/index.md) - the visual-canvas incumbent in the same wing
- [AutoGPT](../autogpt/index.md) - the hosted workflow platform chasing the same unattended runs

## References

- https://api.github.com/repos/apowerb/apowerb - repository, license, counts, and dates (as of 2026-10-21)
- https://raw.githubusercontent.com/apowerb/apowerb/main/README.md - capabilities, the ADK/LiteLLM stack, and the quota claim
- https://docs.apowerb.com/ - architecture, capability summary, and the orchestration patterns
- https://docs.apowerb.com/concepts/editions - the open-core boundary and the absent commercial bricks
- https://pypi.org/pypi/apowerb/json - version 0.2.93 and the 135-release train (as of 2026-10-21)
- https://api.github.com/repos/apowerb/apowerb/releases - the release cadence, three releases on 2026-10-20
- https://hn.algolia.com/api/v1/items/49739951 - the founder's four-point HN thread and its single reply
