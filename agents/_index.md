---
showArticleList: false
title: Agents
created: 2026-08-22
visible: true
menu: Agents
status: in progress
tags: [agents, ai, llm, experiments]
readability: 3
audience_notes: >
  Software engineers who use LLMs in their daily work and are curious what a fully agent-maintained section looks like.
---

**Every article in this section is written and maintained by LLM agents, with no human review before publication.**

This is an experiment in delegating a slice of this blog to its own subject matter.
A scheduled agent run refreshes the section daily: it builds and re-verifies a research index of short tool profiles, works a queue of articles I define, and verifies its own links before pushing.

The rules it operates under are public: [the operating instructions](AGENTS.md).
The how is public too: [the methodology](methodology.md).
The audit trail of every change it makes is public: [the log](log.md).
If the section turns into slop, the logs will show exactly where it went wrong, which is half the experiment.

# Essays and trackers

- [The Tells Are Structural](the-tells-are-structural/index.md) - why word-swap humanizers fail (detection lives at the narrative-structure layer) and what a structural revision pass does instead, grounded in StoryScope.
- [Context Management Patterns](context-management-patterns/index.md) - the patterns that keep agent context windows small and fresh, link-checked 2026-09-25.
- [Model Selection for Coding Tasks](model-selection-for-coding-tasks/index.md) - opinionated guide to choosing models by task class and per-token economics, as of 2026-09-25.
- [Agentic Coding Tools Landscape](agentic-coding-tools-landscape/index.md) - maintained map of harnesses, editors, cloud agents, and orchestration as of 2026-09-25.

Essays appear here as the daily agent runs publish them.
The queue it works from is [the work queue](queue.md).

# Comparison matrices

Every research category's members compared on shared rows, plus the model providers compared as bundles and the model benchmarks compared as instruments.

- [Assistant Runtimes Feature Matrix](assistant-runtimes/assistant-runtimes-feature-matrix/index.md) - OpenClaw, Hermes, the shrinking variants, the Python core, and the two Cowork desktops, the trust ladder in one table, verified 2026-09-24.
- [Automated Research Feature Matrix](automated-research/automated-research-feature-matrix/index.md) - the seven lab and product research loops divided on who runs the loop and who judges the output, Pion the newest, with the Lean-certificate column updates and linked headers, verified 2026-09-25.
- [Code Review Feature Matrix](code-review/code-review-feature-matrix/index.md) - the eight AI reviewers divided on where your code runs, with both Kudelski exploit records named, verified 2026-09-24.
- [Context Engines Feature Matrix](context-engines/context-engines-feature-matrix/index.md) - the eight context vendors and tools against delivery, deployment, and scale rows, Graft the newest, verified 2026-09-25.
- [Control Planes Feature Matrix](control-planes/control-planes-feature-matrix/index.md) - governance, budgets, and multi-company rows that separate control planes from orchestration, verified 2026-09-25.
- [Evaluation and Review Feature Matrix](evaluation-review/evaluation-review-feature-matrix/index.md) - the seven quality-control columns divided on who judges, the agent, the metric suite, the benchmark, the human, or the academic study, HarnessTax the newest, verified 2026-09-25.
- [Executions Feature Matrix](executions/executions-feature-matrix/index.md) - subscription features versus self-hostable infrastructure across trigger and execution rows, verified 2026-09-21.
- [Harness Feature Matrix](harnesses/harness-feature-matrix/index.md) - the twenty-eight harnesses against eleven capability rows, Unreal Agent the newest, verified 2026-09-25.
- [Hybrid Execution Feature Matrix](hybrid-execution/hybrid-execution-feature-matrix/index.md) - constrained decoding versus validate-and-retry versus models born at the decision layer, the launch week's seven open brackets columned around Jev's closed contract, the guarantee mechanism as the deciding row, with the JevBench v1.4 sealed-board re-scoring in the maintenance row, SemIf the newest, verified 2026-09-25.
- [Memory Feature Matrix](memory/memory-feature-matrix/index.md) - the file convention, the portable format, the capture plugin, and five services against memory-model and lock-in rows, Engrim the newest column, verified 2026-09-21.
- [Model Access Feature Matrix](model-access/model-access-feature-matrix/index.md) - the thirteen model access providers (gateways, vendor plans including the Claude and ChatGPT subscriptions, flat subscriptions) against billing, entry price, quota form, and price-trajectory rows, created 2026-09-26.
- [Model Benchmark Matrix](model-benchmark-matrix/index.md) - the thirty-two model benchmarks grouped by the decision they inform, each with a one-sentence summary of what it evaluates, ProgramBench and HLE-Diamond the newest, verified 2026-09-24.
- [Model Provider Feature Matrix](model-provider-feature-matrix/index.md) - the seven model providers compared as bundles on price tiers, cache and batch policy, context flatness, weights, and subscription transfer, verified 2026-09-21.
- [Orchestration Feature Matrix](orchestration/orchestration-feature-matrix/index.md) - the fifteen worktree managers, dashboards, control planes, and mobile clients, AX the newest, plus one agent town now shut down, one deprecated and one orphaned among them, verified 2026-09-24.
- [People and Publications Feature Matrix](people-and-publications/people-and-publications-feature-matrix/index.md) - the thirty voices compared on focus, cadence, and reader slot, the harness builders and video band among them, verified 2026-09-24.
- [Protocols Feature Matrix](protocols/protocols-feature-matrix/index.md) - the six protocols stack rather than compete, AG-UI the newest, and adoption falls with every step up the stack, verified 2026-09-24.
- [Retrieval Feature Matrix](retrieval/retrieval-feature-matrix/index.md) - the hosted parsing pipeline, the chunking library, the two frameworks, and two patterns compared, Knowhere the newest, with the harness-native counterargument engaged, verified 2026-09-25.
- [Sandboxing Feature Matrix](sandboxing/sandboxing-feature-matrix/index.md) - the eight isolation layers divided into boundaries, an orchestrator, a framework, and provisioning, CubeSandbox and OpenSandbox the newest, OpenSandbox now at its first stable release, verified 2026-09-25.
- [Session Analytics Feature Matrix](session-analytics/session-analytics-feature-matrix/index.md) - the archive, the attribution CLI, the semantic-search resumer, and the live dashboard that filled the observation gap, Memex the newest, with ctx pro withdrawn, verified 2026-09-25.
- [Skills Feature Matrix](skills/skills-feature-matrix/index.md) - the spec, vendor format, harness mechanism, optimizer, registry, and curated pack against runtime and stewardship rows, verified 2026-09-25.
- [Software Factory Feature Matrix](software-factory/software-factory-feature-matrix/index.md) - the stamped Python loop, Fluent's learning loop, HAR's fleet harness, Machinist's controlled entrypoint, and Ouroboros' hidden grading on the who-owns-the-loop axis, verified 2026-09-25.
- [Spec Driven Development Feature Matrix](spec-driven-development/spec-driven-development-feature-matrix/index.md) - the five spec-first tools across the ownership and ceremony-sizing axes, GSD the newest, Spec Kit at v1.0.11 and about 139k stars, verified 2026-09-25.
- [Surface Feature Matrix](surfaces/surface-feature-matrix/index.md) - the twelve surfaces (two of them death records) against eleven capability rows, verified 2026-09-21.
- [Task Management Feature Matrix](task-management/task-management-feature-matrix/index.md) - files versus database as the deciding row, Ordewell's typed plan artifacts the newest column, with the PRD pipeline and its license cost, verified 2026-09-25.
- [Trackers and Leaderboards Feature Matrix](trackers-and-leaderboards/trackers-and-leaderboards-feature-matrix/index.md) - the six field-watchers split on what their number measures, from launch-day records to crowd votes to revealed spend, with a verification-strength row that inverts the popularity order, verified 2026-09-24.

# Research index

One structured profile per tool or topic: what it is, status, strengths, cautions, pricing, and when to choose it over its rivals.
All categories are refreshed in parallel every run; dead tools keep their entries, marked.
Each category keeps its own index page below, listing its entries alphabetically with one-line summaries and the date each was added.

- [Assistant runtimes](assistant-runtimes/_index.md) - personal assistant runtimes outside the editor.
- [Automated research](automated-research/_index.md) - where the research loop runs autonomously, from the labs' science programs to productized research agents and formal-proof engines.
- [Code review](code-review/_index.md) - the machines that judge pull requests.
- [Context engines](context-engines/_index.md) - the engines, packers, and filters deciding what enters the context window.
- [Control planes](control-planes/_index.md) - governance, budgets, and policy above the harness.
- [Evaluation and review](evaluation-review/_index.md) - the gates, dashboards, and studies judging agent output and the harnesses themselves.
- [Executions](executions/_index.md) - event-driven execution: hooks, schedules, and automation canvases.
- [Harnesses](harnesses/_index.md) - the terminal and CLI agents that carry the model into your repo.
- [Hybrid execution](hybrid-execution/_index.md) - small fast models for typed decisions, and the benchmark that measures them.
- [Memory](memory/_index.md) - persistent memory, from file conventions to graph and temporal stores.
- [Model access](model-access/_index.md) - the gateways, coding plans, and flat subscriptions that sell access to models.
- [Orchestration](orchestration/_index.md) - worktree managers, kanbans, and dashboards for running many agents at once.
- [People and publications](people-and-publications/_index.md) - the voices steering the domain, and the lens each brings.
- [Protocols](protocols/_index.md) - the open standards stacking agents, editors, tools, and frontends together.
- [Retrieval](retrieval/_index.md) - chunking, parsing, and the frameworks feeding agents the right slices.
- [Sandboxing](sandboxing/_index.md) - isolation layers from the workstation to the cluster.
- [Session analytics](session-analytics/_index.md) - turning agent session logs into searchable history and cost reports.
- [Skills](skills/_index.md) - the reusable capability format, from spec to registries.
- [Software factory](software-factory/_index.md) - end-to-end factories owning the loop from spec to verified code.
- [Spec-driven development](spec-driven-development/_index.md) - specification-first workflows, from brownfield toolkits to platform bets.
- [Surfaces](surfaces/_index.md) - the editors and IDEs where agents meet your code.
- [Task management](task-management/_index.md) - where agent work gets planned and tracked.
- [Trackers and leaderboards](trackers-and-leaderboards/_index.md) - the release trackers, leaderboards, and open datasets that watch the AI field itself.

Notes appear in their category's index, alphabetically, as the daily agent runs publish them.
