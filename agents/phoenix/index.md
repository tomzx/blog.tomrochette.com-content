---
title: Phoenix
created: 2026-08-30
updated: 2026-09-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation, observability, opentelemetry, tracing]
readability: 3
audience_notes: >
  Engineers who need to see and evaluate what their LLM applications and agents did in production-like detail.
  Assumes you know what OpenTelemetry tracing and a span are.
---

Phoenix is Arize AI's open-source AI observability and evaluation platform: OpenTelemetry-native tracing, LLM and code evals, versioned datasets and experiments, a prompt playground, and a built-in AI engineering agent, self-hostable or running on the Arize AX cloud.
Facts below verified as of 2026-09-05.

**Phoenix is the observability column of this category, and its defining trade is the ELv2 license: everything is inspectable and self-hostable, but you cannot offer Phoenix itself as a service, and Arize keeps the production-grade monitoring surface in the paid platform.**

## What it is

A Python platform (`pip install arize-phoenix`, web UI on localhost:6006) built on OpenTelemetry with instrumentation from the companion OpenInference project: dozens of auto-instrumentors for OpenAI, Anthropic, LangChain, LlamaIndex, CrewAI, the Vercel AI SDK, and MCP.
Traces flow over OTLP, evals attach to spans (LLM judges, code evaluators, human annotations, with documented interop for Ragas and deepeval), datasets and experiments version prompts, and span replay re-runs a captured step.
A remote MCP server lets coding agents query the traces, and the PXI agent works inside the UI.
Docker, Helm, and one-click deploys cover laptop through Kubernetes; TypeScript client packages ship alongside.
Core platform under Elastic License 2.0 with the client and OTel packages Apache-2.0; made by Arize AI ($70M Series C, February 2025).

## Status

Mature and busy: 11,333 stars, 1,106 forks, 973 open issues and PRs as of 2026-09-05.
Created 2022-11-09, pushed the day of verification, platform release arize-phoenix 20.8.0 on 2026-09-04, about 1.8 million PyPI downloads a month as of 2026-09-04.
**Four years in, it is the oldest and most production-proven column in this category, with near-daily commits and weekly releases.**

## Strengths

- OTel-native end to end: the same OTLP traces feed Phoenix and Arize AX, and OpenLIT and OpenLLMetry data convert in.
- Covers the full loop, tracing, evals, datasets, experiments, prompt versioning, replay, not just trace storage.
- Runs anywhere data must stay, from laptop to air-gapped clusters.
- Modern DX including one-command coding-agent instrumentation and an MCP endpoint.

## Cautions

- Not truly open source: ELv2 bars offering Phoenix as a managed service, and a community issue calls the license overly restrictive for OSS compatibility.
- Production monitoring (dashboards, alerting, issue grouping) lives in Arize AX, not the OSS project.
- The Azure quick-deploy template serves plain HTTP and the Google Cloud button builds from source, per the README's own notes.
- 967 open issues and PRs is a large queue even for a project this size.

## Pricing

Phoenix OSS is free and self-hosted with no paywalled features inside the product.
Arize AX: Free (25k spans/month), Pro $50/month, Enterprise custom with SSO, SOC 2, HIPAA, SLAs, and self-hosting.

## Compared to

- [deepeval](../deepeval/index.md): eval-first, pytest-style, no trace store; choose deepeval to gate CI, Phoenix when traces and a UI matter, and note they interoperate.
- Langfuse: the closest feature peer with a permissive MIT core; choose Langfuse when license terms dominate, Phoenix for OpenInference breadth and the AX upgrade path.
- Plain OTel backends (Jaeger, Tempo, Datadog): excellent generic span storage with no LLM semantics; choose Phoenix when AI-specific observability is the point.

## Bottom line

**Recommended for teams that need production-grade AI tracing and evaluation under their own infrastructure, accepting ELv2 and the AX upsell gravity.**
Not for anyone resampling hosted observability on top of it, or strictly open-source shops whose policy excludes Elastic-licensed cores.

## See also

- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins
- [deepeval](../deepeval/index.md) - the eval-first alternative that interops with Phoenix
- [Workshop](../workshop/index.md) - the local debugger in the same category
- [agentsview](../agentsview/index.md) - session analytics for coding agents, the local-first cousin

## References

- https://github.com/Arize-ai/phoenix - repository, README, license, adoption numbers
- https://arize.com/docs/phoenix - the OTel and OpenInference basis, features
- https://arize.com/docs/phoenix/resources/frequently-asked-questions/what-is-the-difference-between-phoenix-and-arize - the Phoenix versus AX split
- https://arize.com/pricing/ - the AX tiers for the pricing rows
- https://pypi.org/project/arize-phoenix/ - current version and license as published
- https://github.com/Arize-ai/phoenix/issues/9890 - the community pushback on ELv2, the critical source
