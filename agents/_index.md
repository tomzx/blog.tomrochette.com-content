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

- [Agentic Coding Tools Landscape](agentic-coding-tools-landscape/index.md) - maintained map of harnesses, editors, cloud agents, and orchestration as of 2026-08-24.
- [Model Selection for Coding Tasks](model-selection-for-coding-tasks/index.md) - opinionated guide to choosing models by task class and per-token economics, as of 2026-08-24.
- [Context Management Patterns](context-management-patterns/index.md) - the patterns that keep agent context windows small and fresh, as of 2026-08-24.

## Comparison matrices

- [Harness Feature Matrix](harness-feature-matrix/index.md) - the eleven harnesses against eleven capability rows, verified 2026-08-25.
- [Surface Feature Matrix](surface-feature-matrix/index.md) - the twelve surfaces (two of them death records) against eleven capability rows, verified 2026-08-26.
- [Orchestration Feature Matrix](orchestration-feature-matrix/index.md) - the eight worktree managers, dashboards, and one agent town compared, one dead and one orphaned among them.
- [Protocols Feature Matrix](protocols-feature-matrix/index.md) - the four protocols stack rather than compete, and adoption falls with every step up the stack.
- [Context Engines Feature Matrix](context-engines-feature-matrix/index.md) - the four context vendors and tools against delivery, deployment, and scale rows.
- [Skills Feature Matrix](skills-feature-matrix/index.md) - the spec, vendor format, harness mechanism, and registry against runtime and stewardship rows.
- [Retrieval Feature Matrix](retrieval-feature-matrix/index.md) - the two frameworks and two patterns compared, with the harness-native counterargument engaged.
- [Memory Feature Matrix](memory-feature-matrix/index.md) - the file convention and four services against memory-model and lock-in rows.
- [Executions Feature Matrix](executions-feature-matrix/index.md) - subscription features versus self-hostable infrastructure across trigger and execution rows.
- [Hybrid Execution Feature Matrix](hybrid-execution-feature-matrix/index.md) - constrained decoding versus validate-and-retry, the guarantee mechanism as the deciding row.
- [Task Management Feature Matrix](task-management-feature-matrix/index.md) - files versus database as the deciding row, with the PRD pipeline and its license cost.
- [Spec Driven Development Feature Matrix](spec-driven-development-feature-matrix/index.md) - the four spec-first tools across the ownership and ceremony-sizing axes.
- [Control Planes Feature Matrix](control-planes-feature-matrix/index.md) - governance, budgets, and multi-company rows that separate control planes from orchestration.
- [Assistant Runtimes Feature Matrix](assistant-runtimes-feature-matrix/index.md) - OpenClaw and the three variants named after shrinking it, the trust ladder in one table.

Essays appear here as the daily agent runs publish them.
The queue it works from is [the work queue](queue.md).

# Research index

One structured profile per tool or topic: what it is, status, strengths, cautions, pricing, and when to choose it over its rivals.
Refreshed one category at a time, stalest first; dead tools keep their entries, marked.

## Harnesses

- [aider](aider/index.md) - the pre-agentic BYOK pair-programmer, cheapest precise-edit tool, development stalled since May 2026.
- [Amp](amp/index.md) - Sourcegraph-spun-out agent whose orbs keep working after you close the laptop.
- [Claude Code](claude-code/index.md) - Anthropic's everywhere-at-once harness, the platform benchmark and the token-cost cautionary tale.
- [Cline](cline/index.md) - the open-source agent that outgrew its VS Code extension into CLI, kanban, and SDK, 5.1 million installs deep.
- [Codex](codex/index.md) - OpenAI's ChatGPT-included agent, the Apache-2.0 big-lab CLI individuals can still just run.
- [Crush](crush/index.md) - Charm's Go-and-LSP terminal agent, FSL-licensed, from the original OpenCode repo.
- [Gemini CLI](gemini-cli/index.md) - Google's open-source terminal agent, superseded for individuals by Antigravity CLI in June 2026.
- [goose](goose/index.md) - Block's Rust agent turned Linux Foundation project, the field's first foundation-governed harness.
- [Junie](junie/index.md) - JetBrains' plan-first agent with BYOK and IDE-grade grounding.
- [OpenCode](opencode/index.md) - the MIT, provider-neutral harness with the leanest measured token baseline.
- [Qwen Code](qwen-code/index.md) - Alibaba's Gemini CLI fork, the free-tier on-ramp and open-weights showcase.

## Surfaces

- [Antigravity](antigravity/index.md) - Google's free multi-agent platform (2.0, IDE, CLI, SDK), generous tier, incident-heavy first year.
- [Continue](continue/index.md) - the open-source Copilot alternative across VS Code, JetBrains, and CLI, acquired by Cursor in June 2026, now read-only.
- [Cursor](cursor/index.md) - Anysphere's AI-native editor platform, acquired by SpaceX in August 2026.
- [JetBrains IDEs](jetbrains/index.md) - the analysis-heavy IDEs whose AI layer, AI Assistant plus Junie, is removable and provider-agnostic.
- [Kiro](kiro/index.md) - AWS's spec-driven agentic IDE, credits-metered, from a 50-credit free tier to $200/month.
- [OpenChamber](openchamber/index.md) - the MIT open-source session cockpit around OpenCode, worktrees and multi-model fusion included.
- [Roo Code](roo-code/index.md) - the Cline-fork VS Code extension that sunset itself in May 2026 to chase cloud agents.
- [Trae](trae/index.md) - ByteDance's budget AI IDE, SOLO mode and cloud tasks from $3/month, telemetry questions attached.
- [Void](void/index.md) - the Apache-2.0 open-source Cursor alternative, demand proven, releases stalled since April 2025.
- [VS Code + Copilot](vscode-copilot/index.md) - the neutral default, hosting Copilot, Claude Code, and Codex as swappable harnesses.
- [Windsurf](windsurf/index.md) - the agentic IDE rescued by Cognition in 2025, now rebranding into Devin Desktop.
- [Zed](zed/index.md) - the Rust performance editor where AI is optional and BYOK is unlimited.

## Orchestration

- [Claude Squad](claude-squad/index.md) - free AGPL terminal app running multiple coding agents in tmux, each in its own worktree.
- [cmux](cmux/index.md) - Manaflow's libghostty macOS terminal for parallel agents, notification rings free, cloud execution paid.
- [Conductor](conductor/index.md) - the macOS app for parallel Claude Code, Codex, Cursor, and OpenCode sessions with diff review and PR flow.
- [Crystal](crystal/index.md) - Stravu's worktree manager, deprecated February 2026 for Nimbalyst, kept here as a death record.
- [dmux](dmux/index.md) - the MIT tmux TUI where every task pane gets its own worktree and branch.
- [Emdash](emdash/index.md) - the Apache-2.0 agentic development environment from General Action (YC W26), local or over SSH.
- [Gas Town](gastown/index.md) - Steve Yegge's tmux town of 20-30 supervised agents with a merge queue, beads as the ledger, and the field's loudest controversies.
- [Vibe Kanban](vibe-kanban/index.md) - the Apache-2.0 kanban for parallel agents, orphaned by Bloop's April 2026 shutdown with the community takeover still more promise than activity.

## Protocols

- [A2A](a2a/index.md) - Google's open protocol for independent agents to interoperate, now under the Linux Foundation.
- [ACP](acp/index.md) - Zed's protocol standardizing how editors talk to coding agents.
- [AGENTS.md](agents-md/index.md) - the open convention for repo-level agent instruction files.
- [MCP](mcp/index.md) - the open protocol standardizing how AI applications connect to tools and data.

## Context engines

- [Augment Code](augment-code/index.md) - the coding platform whose core is a real-time semantic Context Engine feeding Auggie and Cosmos.
- [Greptile](greptile/index.md) - AI code review running a swarm of agents over a graph index of your repositories.
- [Repomix](repomix/index.md) - the MIT CLI that packs a whole repo into one AI-friendly file, retrieval-free by design.
- [Sourcegraph code context platform](sourcegraph-code-context/index.md) - code search repositioned as the retrieval layer for agents, with value showing up above roughly 400K lines.

## Skills

- [Agent Skills open standard](agent-skills-open-standard/index.md) - the agentskills.io spec for SKILL.md capability directories.
- [Anthropic Agent Skills](anthropic-agent-skills/index.md) - Anthropic's SKILL.md folder format for reusable agent capabilities.
- [OpenCode skills and plugins](opencode-skills-and-plugins/index.md) - OpenCode's two extension mechanisms: skills for the model, plugins for the harness.
- [skills.sh](skills-sh/index.md) - Vercel's directory and leaderboard for the open skills ecosystem.

## Retrieval

- [LlamaIndex](llamaindex/index.md) - the MIT data framework for retrieval pipelines, now the open arm of LlamaParse.
- [LangChain](langchain/index.md) - the largest LLM framework, repositioned in 2026 as an agent engineering platform.
- [Semantic code search](semantic-code-search/index.md) - retrieval by meaning over embedded chunks, shipped as a workspace index.
- [Tree-sitter chunking](tree-sitter-chunking/index.md) - cutting files along syntax boundaries instead of fixed line counts.

## Memory

- [Cognee](cognee/index.md) - the Apache-2.0 graph-memory pipeline with the whole engine self-hostable and a flat per-token cloud.
- [File-based agent memory](file-based-agent-memory/index.md) - the CLAUDE.md and AGENTS.md conventions, memory as plain markdown files.
- [Letta](letta/index.md) - the MemGPT creators' memory-first platform, agent plus cloud tier.
- [mem0](mem0/index.md) - the hosted and self-hostable memory layer across vector, graph, and key-value backends.
- [Zep](zep/index.md) - temporal knowledge graphs where contradictions invalidate old facts.

## Executions

- [Claude Code hooks](claude-code-hooks/index.md) - lifecycle triggers that turn the harness into an event-driven system.
- [Copilot automations](copilot-automations/index.md) - GitHub's cloud agent on schedules and repository events.
- [GitHub Agentic Workflows](github-agentic-workflows/index.md) - markdown-defined automation compiled into hardened Actions runs.
- [n8n](n8n/index.md) - the fair-code automation canvas where triggers start workflows and agents.

## Hybrid execution

- [Anthropic structured outputs](anthropic-structured-outputs/index.md) - schema-constrained decoding for Claude responses and tool inputs.
- [Instructor](instructor/index.md) - Pydantic in, validated objects out, with a re-ask when validation fails.
- [OpenAI Structured Outputs](openai-structured-outputs/index.md) - schema-guaranteed responses via constrained decoding.
- [Outlines](outlines/index.md) - logit-masked generation following types, schemas, regexes, or grammars.

## Spec-driven development

- [BMad Method](bmad-method/index.md) - the agile method that sizes ceremony to the change, roles and retrospectives included.
- [GitHub Spec Kit](spec-kit/index.md) - the MIT process-plus-CLI layer that made specs-before-agents a movement, agent-neutral, 131k stars in year one.
- [OpenSpec](openspec/index.md) - the brownfield spec toolkit whose delta proposals archive into a living ledger, 1.6M npm downloads a month.
- [Tessl](tessl/index.md) - the $125M platform bet that spec-driven development is infrastructure you rent.

## Task management

- [Backlog.md](backlog-md/index.md) - the markdown-native task manager whose three review gates, spec, plan, code, make it the first line of code review.
- [beads](beads/index.md) - Steve Yegge's Dolt-backed graph issue tracker, dependency-aware with atomic claims, the agent-memory thesis in running code.
- [Task Master](task-master/index.md) - the most-installed PRD-to-tasks pipeline, quiet since April 2026 as it became Hamster's Commons-Clause commercial engine.

## Control planes

- [Paperclip](paperclip/index.md) - the MIT self-hosted control plane for a company of agents, heartbeats, budgets, and governance, 79k stars in six months.

## Assistant runtimes

- [NanoClaw](nanoclaw/index.md) - the auditable containerized OpenClaw rewrite, one process you can read in an afternoon.
- [OpenClaw](openclaw/index.md) - the self-hosted personal assistant root of the -claw family, 388k stars and the 2026 provider-restriction saga.
- [PicoClaw](picoclaw/index.md) - Sipeed's Go assistant on $10 RISC-V boards in 10-20MB of RAM, the category as a compile target.
- [ZeroClaw](zeroclaw/index.md) - the single Rust binary runtime, ownership as a compile-time property.

Notes appear here, alphabetically, as the daily agent runs publish them.
