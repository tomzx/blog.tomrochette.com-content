---
title: Atomic Agents
created: 2026-10-07
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, python-framework]
readability: 3
audience_notes: >
  Python engineers building agent pipelines on typed components, and anyone comparing the validate-and-retry family.
  Assumes you know Pydantic and have used Instructor or an equivalent.
---

Atomic Agents is the MIT Python framework that assembles agents, tools, and context providers as small schema-validated components, built directly on Instructor and Pydantic so every component's input and output is a declared schema with retry when validation fails.

**Atomic Agents is the framework-layer member of the validate-and-retry family: Instructor gives one call a typed contract, and Atomic Agents gives the whole pipeline one, which makes it the closest thing this category has to an opinionated reference architecture for the post-hoc side of the guarantee spectrum.**

## What it is

A pip-installable Python framework by Kenny Vaneetvelde and Eigenwise, MIT licensed, with Sphinx documentation, a cookbook, and an Atomic Assembler CLI that downloads community tools (6,283 stars as of 2026-10-15, pushed 2026-10-20).
Components are single-purpose and composable: an `AtomicAgent` is generic over its input and output schemas, chat history and context providers are injected, and providers arrive through Instructor's integrations (OpenAI, Anthropic, Groq, Gemini, Ollama for local models).
All control flow is plain Python, deliberately: no graphs, no runtime DSL, the framework's stated bet being that familiar software-engineering practice beats orchestration frameworks for most pipelines.
Example projects ship for RAG chatbots, web search, deep research, orchestration agents, and MCP, and a Reddit community (r/AtomicAgents) has grown around the framework.

## Status

Active: created 2024-06-03, 6,283 stars as of 2026-10-15, three releases on 2026-10-19 (v2.12.1, v2.13.0, and v2.13.1) followed by v2.14.0 on 2026-10-20 and v2.15.0 on 2026-10-21, PyPI at 2.15.0, pushed 2026-10-24 (generic-schema resolution and Instructor-callback fixes without a release), as of 2026-10-25.
The 2.11.0 release added an optional OpenInference instrumentor (`atomic-agents[observability]`) that emits AGENT and TOOL spans for Arize Phoenix, and 2.12.0 hardened the MCP surface (tool pagination, schema-reference resolution, error-result propagation) alongside new Firecrawl Search and FXMacroData tools.
The 2026-10-19 train then un-pinned the foundation: 2.12.1 capped `mcp` below 2.0 so fresh installs can import the connector, 2.13.0 replaced the exact Instructor pin with `instructor>=1.17.0,<2` while documenting Instructor 1.17's changed `max_retries` counting (a value of 3 now permits three retries after the first attempt, so older budgets shrink by one), and 2.13.1 made two agent-config fields type-checker-friendly under Pyright and Pylance.
The 2026-10-20/21 train rebuilt the observability layer: v2.14.0 activates the framework through the standard `opentelemetry-instrument` launcher with both OpenTelemetry and Phoenix discovery entry points, and v2.15.0 moved tracing onto `opentelemetry-api` alone, emitting OpenTelemetry GenAI semantic-convention spans that any OTLP backend reads (a plain collector, Grafana Tempo, Sentry, Datadog, Honeycomb, PostHog, Jaeger, Arize Phoenix, Langfuse), so Phoenix and the OpenInference packages are no longer required, with one `chat {model}` CLIENT span per Instructor attempt carrying per-attempt and total token usage, the responding model, attempt count, and validation errors as events.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Eigenwise/atomic-agents&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Eigenwise/atomic-agents&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Eigenwise/atomic-agents&type=date&legend=top-left" />
</picture>

Development is steady rather than explosive: a maintained 2.x line, documentation current with releases, and a maintainer-visible community.
Its Hacker News footprint is negligible, so adoption evidence is the star and PyPI record, not forum debate.

## Strengths

- Inherits Instructor's provider breadth and reask mechanics, so the typed contract works across 15-plus providers including local Ollama.
- The atomic-component discipline (single-purpose, schema-bounded, composable) is a maintainability argument the one-call libraries never make.
- Plain-Python control flow keeps the whole pipeline debuggable with ordinary tooling, and the docs treat that as the design center, not a limitation.
- Complete free tier: MIT, no service, no metering.

## Cautions

- The guarantee is post-hoc: validation catches a bad output after you have paid for it, with reask retries billing full calls, exactly the mechanism native strict mode makes unnecessary on single-vendor stacks.
- It is a thin layer over Instructor and Pydantic, so most of its value is structure and defaults, and a skeptical team can assemble the same structure itself.
- Community scale is modest next to LangChain-class frameworks, which shows in ecosystem tooling and third-party integrations.
- Bus factor concentrates on one lead maintainer.

## Pricing

Free and open source under MIT; there is no paid tier, so pricing does not apply.
Costs are your model tokens, plus full-call retries on validation failures.

## Compared to

- [Instructor](../instructor/index.md): the library underneath, one typed call at a time; add Atomic Agents when many such calls need to compose into one maintainable pipeline.
- [Outlines](../outlines/index.md): the decoding-time alternative that makes invalid output impossible to emit; choose it when the schema must be guaranteed rather than checked.
- [OpenAI Structured Outputs](../openai-structured-outputs/index.md): the native strict mode that makes both libraries unnecessary on a single-vendor stack.

## Bottom line

**Recommended for Python teams standardizing a multi-component agent pipeline on typed schemas across several providers, reading the framework as conventions and glue rather than magic.**
Not for anyone who can stay on one provider's native strict mode, and not for guarantees at sampling time, which this family's mechanism cannot give.

## Changes

- 2026-10-07 - Created.
- 2026-10-17 - Volatile re-verification after the 2026-10-15 pushes: recorded the same-day v2.11.0 (Arize Phoenix / OpenInference tracing, an observability extra with a new docs guide and example) and v2.12.0 (MCP hardening plus Firecrawl Search and FXMacroData tools) releases, PyPI now at 2.12.0, repository pushed 2026-10-15.
- 2026-10-20 - Volatile re-verification after the 2026-10-19/20 pushes: recorded the three same-day 2026-10-19 releases (v2.12.1 capping mcp below 2.0, v2.13.0 relaxing the Instructor pin to 1.17-plus with the max_retries counting change documented, v2.13.1's Pyright and Pylance fixes), PyPI now at 2.13.1, pushed 2026-10-20.
- 2026-10-22 - Volatile re-verification after the v2.14.0 (2026-10-20) and v2.15.0 (2026-10-21) releases: recorded the rebuilt observability layer, `opentelemetry-instrument` launcher activation and OpenTelemetry GenAI semantic-convention spans on `opentelemetry-api` alone readable by any OTLP backend, with Phoenix and the OpenInference packages no longer required and per-attempt usage carried on one CLIENT span per Instructor call; PyPI now at 2.15.0, pushed 2026-10-21.
- 2026-10-25 - Volatile re-verification after the 2026-10-24 pushes (no release since v2.15.0): generic agent subclasses now resolve their schemas (#328), Instructor callbacks pause when agent hooks are disabled (#327), the quickstart defaults to MiniMax M3.1 Flash, and the docs cover generic schema resolution and hook pausing; pushed date moved to 2026-10-24.

## See also

- [Instructor](../instructor/index.md) - the validate-and-retry library this framework is built on
- [Outlines](../outlines/index.md) - the decoding-time counterpart in the same category
- [OpenAI Structured Outputs](../openai-structured-outputs/index.md) - the native feature that shrinks this family's niche
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/Eigenwise/atomic-agents - repository, MIT license, component model, and the Instructor-plus-Pydantic foundation (fetched 2026-10-22, re-fetched 2026-10-25)
- https://api.github.com/repos/Eigenwise/atomic-agents - stars, created date, and push date for the as-of status (fetched 2026-10-22, re-fetched 2026-10-25)
- https://eigenwise.github.io/atomic-agents/ - the framework documentation: schema-bounded components, provider integrations, the Atomic Assembler CLI, and example projects (fetched 200, 2026-10-17)
- https://pypi.org/pypi/atomic-agents/json - the published package version 2.15.0 (fetched 2026-10-22, re-fetched 2026-10-25)
- https://api.github.com/repos/Eigenwise/atomic-agents/releases - the v2.12.1 through v2.15.0 releases of 2026-10-19 to 10-21 and the release cadence (fetched 2026-10-22, re-fetched 2026-10-25 with the train still topping out at v2.15.0)
