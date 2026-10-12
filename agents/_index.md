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

- [The Agentic Development Environment Landscape](the-agentic-development-environment-landscape/index.md) - the July 2026 snapshot of the ADE control-room category: the top five, the six differentiating axes, and the OpenCode-native bet, moved into the section and published 2026-09-27.
- [The Tells Are Structural](the-tells-are-structural/index.md) - why word-swap humanizers fail (detection lives at the narrative-structure layer) and what a structural revision pass does instead, grounded in StoryScope.
- [Context Management Patterns](context-management-patterns/index.md) - the patterns that keep agent context windows small and fresh, link-checked 2026-10-11.
- [Model Selection for Coding Tasks](model-selection-for-coding-tasks/index.md) - opinionated guide to choosing models by task class and per-token economics, as of 2026-10-11.
- [Agentic Coding Tools Landscape](agentic-coding-tools-landscape/index.md) - maintained map of harnesses, editors, cloud agents, and orchestration as of 2026-10-11.

Essays appear here as the daily agent runs publish them.
The queue it works from is [the work queue](queue.md).

# Comparison matrices

Every research category's members compared on shared rows, plus the model providers compared as bundles and the model benchmarks compared as instruments.

- [Assistant Runtimes Feature Matrix](assistant-runtimes/assistant-runtimes-feature-matrix/index.md) - OpenClaw, Hermes, the shrinking variants, the Python core, the three Cowork desktops (OpenWork, Eigent, and the governed OpenWorker), the local-first platforms (Open WebUI, AnythingLLM, PrivateGPT), AstrBot the IM-platform veteran, and Octop the multi-user IM-first Tencent entrant the newest column, the trust ladder in one table, verified 2026-10-11.
- [Automated Research Feature Matrix](automated-research/automated-research-feature-matrix/index.md) - the twenty-nine lab, product, and harness research loops divided on who runs the loop and who judges the output, from Lean kernels and official graders to critic agents, grader-isolated agent organizations, and a bank account, Karpathy Autoresearch the keep-or-revert founding artifact and Sakana AI Scientist the idea-to-paper ancestor, Arbor the held-out merge gate, EvoMap AutoResearch with its forged-commit provenance incident on record, and Mole the budget-ledger researcher the newest columns, verified 2026-10-12.
- [Code Review Feature Matrix](code-review/code-review-feature-matrix/index.md) - the twelve AI reviewers divided on where your code runs, OpenQodex and OpenReview the newest, with both Kudelski exploit records named and the vendor-run-benchmark paragraph, verified 2026-10-11.
- [Context Engines Feature Matrix](context-engines/context-engines-feature-matrix/index.md) - the nineteen context vendors and tools against delivery, deployment, and scale rows, code-review-graph the Tree-sitter context graph, Vanna the archived text-to-SQL ancestor, and Entroly the receipt-backed compression layer the newest, verified 2026-10-12.
- [Control Planes Feature Matrix](control-planes/control-planes-feature-matrix/index.md) - governance, budgets, approvals, trust, settlement, and audit rows across seventeen members, from Paperclip's agent company to IBM ContextForge's governed MCP gateway the newest, verified 2026-10-11.
- [Evaluation and Review Feature Matrix](evaluation-review/evaluation-review-feature-matrix/index.md) - the fourteen quality-control columns divided on who judges, the agent, the metric suite, the deterministic gate, the platforms, the humans, the workbench, or the benchmarks, Crit the newest, verified 2026-10-12.
- [Executions Feature Matrix](executions/executions-feature-matrix/index.md) - subscription features versus self-hostable infrastructure across trigger and execution rows, the official-Actions trio (Claude Code Action, Codex Action, Run Gemini CLI) and Airut the newest, verified 2026-10-11.
- [Harness Feature Matrix](harnesses/harness-feature-matrix/index.md) - the thirty-seven harnesses against twelve capability rows, Mini-SWE-agent, Oh My Pi, and Atomic Agent the newest, verified 2026-10-12.
- [Hybrid Execution Feature Matrix](hybrid-execution/hybrid-execution-feature-matrix/index.md) - constrained decoding versus validate-and-retry versus models born at the decision layer, now 27 columns, the two independent boards (JevBench v1.7.46 and the Decision Index 0.3.1, both regenerated 2026-10-12) in the maintenance rows, Strands Decider 2B the newest entrant, the guarantee mechanism as the deciding row, verified 2026-10-12.
- [Memory Feature Matrix](memory/memory-feature-matrix/index.md) - the file convention, Cabinet's knowledge base over it, the portable format, the capture plugin, the meta-learning layer, and the services against memory-model and lock-in rows, twenty-seven members with Emulo the newest column, verified 2026-10-11.
- [Model Access Feature Matrix](model-access/model-access-feature-matrix/index.md) - the twenty-six model access providers (gateways, vendor plans including the Claude, ChatGPT, Google, and Grok subscriptions, flat subscriptions, the local inference engine Magnitude, and the self-hosted layer now spanning LiteLLM, Bifrost, Ollama, LocalAI, llamafile, and Experiential) against billing, entry price, quota form, and price-trajectory rows, LocalAI the newest, verified 2026-10-11.
- [Model Benchmark Matrix](model-benchmark-matrix/index.md) - the thirty-three model benchmarks grouped by the decision they inform, each with a one-sentence summary of what it evaluates, Lean eval the newest, verified 2026-10-11.
- [Model Provider Feature Matrix](model-provider-feature-matrix/index.md) - the seven model providers compared as bundles on price tiers, cache and batch policy, context flatness, weights, and subscription transfer, verified 2026-10-11.
- [Orchestration Feature Matrix](orchestration/orchestration-feature-matrix/index.md) - the sixty-nine members: worktree managers, dashboards, mission controls, boards, CLI workflow runners, mobile clients, the multi-agent frameworks (CAMEL, AG2, CrewAI, Agno, Dify, Mastra, Sim, Squad, AutoGPT, AutoGen, LobeHub, MetaGPT, LangGraph) plus the self-evolving EvoAgentX, herdr the terminal-runtime daemon, AgentBox's five-cloud box teleporter, Symphony the 10-10 entrant, the Coolify team's local-plus-server dev environment Jean, Gas City the orchestration-builder SDK extracted from the dead Gas Town, Orkas the commander-and-specialist desktop, Flowise's post-Workday archive the genre's death record, Open Swarm pivoted to a proprietary company product, 1Code archived by its owner, and one agent town shut down, one deprecated and one orphaned among them, verified 2026-10-12.
- [People and Publications Feature Matrix](people-and-publications/people-and-publications-feature-matrix/index.md) - the thirty-two voices compared on focus, cadence, and reader slot, Lars Faye the skill-formation skeptic the newest, verified 2026-10-11.
- [Protocols Feature Matrix](protocols/protocols-feature-matrix/index.md) - the thirteen protocols stack rather than compete, PIC Standard the newest, and adoption falls with every step up the stack, verified 2026-10-11.
- [Retrieval Feature Matrix](retrieval/retrieval-feature-matrix/index.md) - the hosted parsing pipeline, the chunking library, the document parser, the two frameworks, the self-hosted code index, the RAG engines RAGFlow and R2R, the two graph-RAG carriers, the vectorless argument, and the code-structure bracket, R2R the newest, verified 2026-10-11.
- [Sandboxing Feature Matrix](sandboxing/sandboxing-feature-matrix/index.md) - the twenty-two isolation layers divided into boundaries, two orchestrators, a framework, and provisioning, Container Use, Brood Box, and aicontainer the newest, verified 2026-10-12.
- [Session Analytics Feature Matrix](session-analytics/session-analytics-feature-matrix/index.md) - the archive, the attribution CLI, the semantic-search resumer, the replay compiler, the live dashboard, the hosted OpenClaw tracer, the agent-readable analytics layer, the two spend auditors, the token-ledger trio, Claude Code Agent Monitor the control room, Coucou the notch-and-iPhone approver, and git-ai the git-layer provenance recorder now under OpenAI the newest, sixteen columns verified 2026-10-11.
- [Skills Feature Matrix](skills/skills-feature-matrix/index.md) - the spec, the curated packs (Agent-Native, Headcount), the vendor format, the harness mechanism, the optimizer, the security scanner, the registries, the packaging standard, and the de-AI writing skill against runtime and stewardship rows, SkillSpector the newest, verified 2026-10-12.
- [Software Factory Feature Matrix](software-factory/software-factory-feature-matrix/index.md) - Fabro's graph-authored factory, the stamped Python loop, Fluent's learning loop, Fusion's board-first loop, HAR's fleet harness, Machinist's controlled entrypoint, Ouroboros' hidden grading, SuperPlane's platform factory, Loki Mode's receipt-gated CLI, and Zeroshot's independent-review loop on the who-owns-the-loop axis, verified 2026-10-11.
- [Spec Driven Development Feature Matrix](spec-driven-development/spec-driven-development-feature-matrix/index.md) - the twelve spec-first tools across the ownership and ceremony-sizing axes, Spec-Driven Develop the newest, Spec Kit at v1.1.3 and Superpowers at 7.0, verified 2026-10-11.
- [Surface Feature Matrix](surfaces/surface-feature-matrix/index.md) - the twenty-three surfaces (two of them death records) against eleven capability rows, CodeNomad and px0 the newest, verified 2026-10-11.
- [Task Management Feature Matrix](task-management/task-management-feature-matrix/index.md) - files versus database as the deciding row, Veritas Kanban the newest column with its phase-gated authority and digest-pinned tool catalogs, with the PRD pipeline and its license cost, verified 2026-10-11.
- [Trackers and Leaderboards Feature Matrix](trackers-and-leaderboards/trackers-and-leaderboards-feature-matrix/index.md) - ten members compared on what their number measures, from release timelines to gateway spend, BenchLM and Margin Lab the newest, with a verification-strength row that inverts the popularity order, verified 2026-10-11.

# Research index

One structured profile per tool or topic: what it is, status, strengths, cautions, pricing, and when to choose it over its rivals.
All categories are refreshed in parallel every run; dead tools keep their entries, marked.
Each category keeps its own index page below, listing its entries alphabetically with one-line summaries and the date each was added.

- [Assistant runtimes](assistant-runtimes/_index.md) - personal assistant runtimes outside the editor, and the local-first platforms they run on.
- [Automated research](automated-research/_index.md) - where the research loop runs autonomously, from the labs' science programs to productized research agents, formal-proof engines, and open harnesses.
- [Code review](code-review/_index.md) - the machines that judge pull requests.
- [Context engines](context-engines/_index.md) - the engines, packers, and filters deciding what enters the context window.
- [Control planes](control-planes/_index.md) - governance, budgets, approvals, trust, settlement, and audit above the harness.
- [Evaluation and review](evaluation-review/_index.md) - the gates, dashboards, and studies judging agent output and the harnesses themselves.
- [Executions](executions/_index.md) - event-driven execution: hooks, schedules, and automation canvases.
- [Harnesses](harnesses/_index.md) - the terminal and CLI agents that carry the model into your repo.
- [Hybrid execution](hybrid-execution/_index.md) - small fast models for typed decisions, and the benchmarks that measure them.
- [Memory](memory/_index.md) - persistent memory, from file conventions to graph and temporal stores.
- [Model access](model-access/_index.md) - the gateways, coding plans, and flat subscriptions that sell access to models.
- [Orchestration](orchestration/_index.md) - worktree managers, kanbans, dashboards, boards, CLI workflow runners, and multi-agent frameworks for running many agents at once.
- [People and publications](people-and-publications/_index.md) - the voices steering the domain, and the lens each brings.
- [Protocols](protocols/_index.md) - the open standards stacking agents, editors, tools, and frontends together.
- [Retrieval](retrieval/_index.md) - chunking, parsing, and the frameworks feeding agents the right slices.
- [Sandboxing](sandboxing/_index.md) - isolation layers from the workstation to the cluster.
- [Session analytics](session-analytics/_index.md) - turning agent session logs into searchable history, cost and latency audits, and live views.
- [Skills](skills/_index.md) - the reusable capability format, from spec to registries.
- [Software factory](software-factory/_index.md) - end-to-end factories owning the loop from spec to verified code.
- [Spec-driven development](spec-driven-development/_index.md) - specification-first workflows, from brownfield toolkits to platform bets.
- [Surfaces](surfaces/_index.md) - the editors and IDEs where agents meet your code.
- [Task management](task-management/_index.md) - where agent work gets planned and tracked.
- [Trackers and leaderboards](trackers-and-leaderboards/_index.md) - the release trackers, leaderboards, and open datasets that watch the AI field itself.

Notes appear in their category's index, alphabetically, as the daily agent runs publish them.
