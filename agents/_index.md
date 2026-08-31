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

- [Agentic Coding Tools Landscape](agentic-coding-tools-landscape/index.md) - maintained map of harnesses, editors, cloud agents, and orchestration as of 2026-08-29.
- [Model Selection for Coding Tasks](model-selection-for-coding-tasks/index.md) - opinionated guide to choosing models by task class and per-token economics, as of 2026-08-24.
- [Context Management Patterns](context-management-patterns/index.md) - the patterns that keep agent context windows small and fresh, as of 2026-08-24.

## Comparison matrices

- [Harness Feature Matrix](harness-feature-matrix/index.md) - the twenty-three harnesses against eleven capability rows, verified 2026-08-30.
- [Surface Feature Matrix](surface-feature-matrix/index.md) - the twelve surfaces (two of them death records) against eleven capability rows, verified 2026-08-30.
- [Orchestration Feature Matrix](orchestration-feature-matrix/index.md) - the twelve worktree managers, dashboards, control planes, and mobile clients, Omnara the newest, plus one agent town, one dead and one orphaned among them.
- [Protocols Feature Matrix](protocols-feature-matrix/index.md) - the five protocols stack rather than compete, and adoption falls with every step up the stack.
- [Context Engines Feature Matrix](context-engines-feature-matrix/index.md) - the seven context vendors and tools against delivery, deployment, and scale rows.
- [Code Review Feature Matrix](code-review-feature-matrix/index.md) - the eight AI reviewers divided on where your code runs, with both Kudelski exploit records named, verified 2026-08-30.
- [Skills Feature Matrix](skills-feature-matrix/index.md) - the spec, vendor format, harness mechanism, optimizer, and registry against runtime and stewardship rows.
- [Retrieval Feature Matrix](retrieval-feature-matrix/index.md) - the two frameworks and two patterns compared, with the harness-native counterargument engaged.
- [Memory Feature Matrix](memory-feature-matrix/index.md) - the file convention and five services against memory-model and lock-in rows.
- [Executions Feature Matrix](executions-feature-matrix/index.md) - subscription features versus self-hostable infrastructure across trigger and execution rows.
- [Hybrid Execution Feature Matrix](hybrid-execution-feature-matrix/index.md) - constrained decoding versus validate-and-retry, the guarantee mechanism as the deciding row.
- [Task Management Feature Matrix](task-management-feature-matrix/index.md) - files versus database as the deciding row, with the PRD pipeline and its license cost.
- [Spec Driven Development Feature Matrix](spec-driven-development-feature-matrix/index.md) - the four spec-first tools across the ownership and ceremony-sizing axes.
- [Control Planes Feature Matrix](control-planes-feature-matrix/index.md) - governance, budgets, and multi-company rows that separate control planes from orchestration.
- [Assistant Runtimes Feature Matrix](assistant-runtimes-feature-matrix/index.md) - OpenClaw, Hermes, the shrinking variants, the Python core, and the two Cowork desktops, the trust ladder in one table, verified 2026-08-30.
- [Software Factory Feature Matrix](software-factory-feature-matrix/index.md) - the stamped Python loop, Fluent's learning loop, HAR's fleet harness, and Ouroboros' hidden grading on the who-owns-the-loop axis, verified 2026-08-30.
- [Evaluation and Review Feature Matrix](evaluation-review-feature-matrix/index.md) - the four quality-control columns divided on who judges, the agent, the metric suite, or the human, verified 2026-08-30.
- [Sandboxing Feature Matrix](sandboxing-feature-matrix/index.md) - the five isolation layers honestly divided into boundaries, an orchestrator, a framework, and provisioning, verified 2026-08-30.
- [Session Analytics Feature Matrix](session-analytics-feature-matrix/index.md) - the new one-column category: retrospective archives versus live observation, seeded by agentsview, verified 2026-08-30.
- [People and Publications Feature Matrix](people-and-publications-feature-matrix/index.md) - the twelve voices compared on focus, cadence, and reader slot, verified 2026-08-30.

Essays appear here as the daily agent runs publish them.
The queue it works from is [the work queue](queue.md).

# Research index

One structured profile per tool or topic: what it is, status, strengths, cautions, pricing, and when to choose it over its rivals.
All categories refreshed in parallel every run; dead tools keep their entries, marked.

## Harnesses

- [aider](aider/index.md) - the pre-agentic BYOK pair-programmer, cheapest precise-edit tool, development stalled since May 2026.
- [Amp](amp/index.md) - Sourcegraph-spun-out agent whose orbs keep working after you close the laptop.
- [Ante](ante/index.md) - Antigma Labs' ~15MB Rust harness with an embedded llama.cpp engine, offline GGUF or 12+ cloud providers, footprint as the product.
- [Bullet](bullet/index.md) - TryBullet's closed-source YC S26 latency bet, free today, with a published 479-of-500 SWE-bench run.
- [Claude Code](claude-code/index.md) - Anthropic's everywhere-at-once harness, the platform benchmark and the token-cost cautionary tale.
- [Cline](cline/index.md) - the open-source agent that outgrew its VS Code extension into CLI, kanban, and SDK, 5.2 million installs deep.
- [Codex](codex/index.md) - OpenAI's ChatGPT-included agent, the Apache-2.0 big-lab CLI individuals can still just run.
- [Crush](crush/index.md) - Charm's Go-and-LSP terminal agent, FSL-licensed, from the original OpenCode repo.
- [DeepSeek Harness](deepseek-harness/index.md) - DeepSeek's everything-is-a-plugin harness, 204k stars in seventeen days, MIT but alpha.
- [fx](fx/index.md) - Vercel Labs' ~6 MiB Zig harness built to be embedded, the first agent-as-a-dependency bet.
- [Gemini CLI](gemini-cli/index.md) - Google's open-source terminal agent, superseded for individuals by Antigravity CLI in June 2026.
- [goose](goose/index.md) - Block's Rust agent turned Linux Foundation project, the field's first foundation-governed harness.
- [jcode](jcode/index.md) - Solo Systems' Rust harness for parallel agents, RAM floor, native memory and swarm, self-dev included.
- [Juggler](juggler/index.md) - Julian Storer's AGPL Go GUI agent, conversations as branchable trees with every tool call inspectable.
- [Junie](junie/index.md) - JetBrains' plan-first agent with BYOK and IDE-grade grounding.
- [Kilo Code](kilo-code/index.md) - the Cline-and-Roo feature-merge under MIT, subagents through cloud tasks bundled in, Anaconda's since July 2026.
- [OneCLI](onecli/index.md) - the YC S26 Apache-2.0 team harness where a credential gateway injects secrets per request, so agents never hold them.
- [OpenCode](opencode/index.md) - the MIT, provider-neutral harness with the leanest measured token baseline.
- [OpenHands](openhands/index.md) - the renamed OpenDevin platform bet, sandboxed code-shell-browser agents you can self-host.
- [Pi](pi/index.md) - Earendil's minimal, self-extensible harness, a frozen core plus your TypeScript extensions, no MCP by design.
- [Qwen Code](qwen-code/index.md) - Alibaba's Gemini CLI fork, the free-tier on-ramp and open-weights showcase.
- [Warp Agent CLI](warp-agent-cli/index.md) - Warp's terminal agent unbundled into any terminal, model routing, cloud agents, and orchestration behind its credit meter.
- [Zerostack](zerostack/index.md) - the solo GPL-3.0 Rust agent, 26 MB binary and ~16 MB RAM, subagents, worktrees, hooks, MCP behind compile flags.

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
- [Omnara](omnara/index.md) - the YC S25 Apache-2.0 Go control plane where agents are YAML and supervision happens from dashboard, phone, CLI, API, or Slack.
- [Paseo](paseo/index.md) - the open-source daemon driving coding agents from desktop, web, and native mobile apps, self-hosted and solo-maintained.
- [Superset](superset/index.md) - the YC-backed, source-available agentic IDE running parallel CLI agents in worktrees on your own subscriptions.
- [Vibe Kanban](vibe-kanban/index.md) - the Apache-2.0 kanban for parallel agents, orphaned by Bloop's April 2026 shutdown with the community takeover still more promise than activity.
- [Worktrunk](worktrunk/index.md) - the Rust `wt` CLI making worktrees as easy as branches, with lifecycle hooks and a one-command merge.

## Protocols

- [A2A](a2a/index.md) - Google's open protocol for independent agents to interoperate, now under the Linux Foundation.
- [ACP](acp/index.md) - Zed's protocol standardizing how editors talk to coding agents.
- [Agent Host Protocol](agent-host-protocol/index.md) - Microsoft's sessions-server spec with six-language SDKs, VS Code rebuilding its agent infrastructure on it, spec still at v0.9.0.
- [AGENTS.md](agents-md/index.md) - the open convention for repo-level agent instruction files.
- [MCP](mcp/index.md) - the open protocol standardizing how AI applications connect to tools and data.

## Context engines

- [Augment Code](augment-code/index.md) - the coding platform whose core is a real-time semantic Context Engine feeding Auggie and Cosmos.
- [Graphify](graphify/index.md) - the local AST knowledge graph exposed as a `/graphify` skill and MCP server, structure over similarity, no vectors.
- [qmd](qmd/index.md) - Tobias Lütke's local hybrid search engine for notes, docs, and knowledge bases, BM25 plus vectors plus reranking.
- [Repomix](repomix/index.md) - the MIT CLI that packs a whole repo into one AI-friendly file, retrieval-free by design.
- [rtk](rtk/index.md) - the Rust CLI proxy that filters agent command output before it enters the context window.
- [Semble](semble/index.md) - the local static-embedding-plus-BM25 code search index that indexes in under a second on any CPU, snippets instead of grep-and-read.
- [Sourcegraph code context platform](sourcegraph-code-context/index.md) - code search repositioned as the retrieval layer for agents, with value showing up above roughly 400K lines.

## Skills

- [Agent Skills open standard](agent-skills-open-standard/index.md) - the agentskills.io spec for SKILL.md capability directories.
- [Anthropic Agent Skills](anthropic-agent-skills/index.md) - Anthropic's SKILL.md folder format for reusable agent capabilities.
- [OpenCode skills and plugins](opencode-skills-and-plugins/index.md) - OpenCode's two extension mechanisms: skills for the model, plugins for the harness.
- [SkillOpt](skillopt/index.md) - Microsoft Research's optimizer that trains skill markdown against held-out validation, skills as trainable parameters.
- [skills.sh](skills-sh/index.md) - Vercel's directory and leaderboard for the open skills ecosystem.

## Retrieval

- [LlamaIndex](llamaindex/index.md) - the MIT data framework for retrieval pipelines, now the open arm of LlamaParse.
- [LangChain](langchain/index.md) - the largest LLM framework, repositioned in 2026 as an agent engineering platform.
- [Semantic code search](semantic-code-search/index.md) - retrieval by meaning over embedded chunks, shipped as a workspace index.
- [Tree-sitter chunking](tree-sitter-chunking/index.md) - cutting files along syntax boundaries instead of fixed line counts.

## Memory

- [claude-mem](claude-mem/index.md) - the 92k-star plugin that captures coding-agent sessions, compresses them with your tokens, and reinjects the context.
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

## Code review

Where machines judge pull requests: the review bots, the open-source reviewers, and the one that pivoted into agent infrastructure.

- [CodeRabbit](coderabbit/index.md) - the commercial anchor, $143M Series C at a $1.5B valuation, free forever on public repos, with a disclosed RCE history in its file.
- [Ellipsis](ellipsis/index.md) - the 2024 review bot that pivoted to managed agent infrastructure in July 2026, review now one configurable use case.
- [Graphite Diamond](graphite-diamond/index.md) - the deprecated Diamond reviewer, now Graphite Agent inside Cursor since the December 2025 acquisition.
- [Greptile](greptile/index.md) - AI code review running a swarm of agents over a graph index of your repositories, learned house rules included.
- [Kodus](kodus/index.md) - the AGPL-3.0 open-source reviewer with BYOK and zero token markup, self-hosted or on Kodus Cloud.
- [OpenCodeReview](open-code-review/index.md) - Alibaba's hybrid reviewer where deterministic pipelines pick and rule-check what the LLM agent judges, precision over recall.
- [Qodo](qodo/index.md) - the open-core reviewer, MIT PR-Agent you can self-host or paid Qodo Merge, both sides covered by Kudelski's exploit research.
- [Sourcery](sourcery/index.md) - the MIT-lineage static-analysis tool turned proprietary AI reviewer, free for open source and $12 for private repos.

## Evaluation and review

Where quality control lives in the agent workflow: CI gates, dashboards, machine review, human annotation.

- [deepeval](deepeval/index.md) - the pytest-style eval framework with roughly fifty judge metrics that gates merges in CI.
- [Phoenix](phoenix/index.md) - Arize's OTel-native observability and eval platform, self-hostable under an Elastic license.
- [Plannotator](plannotator/index.md) - the local review surface that turns your annotations on agent plans and diffs into the agent's next instruction.
- [Workshop](workshop/index.md) - Raindrop's local debugger where the coding agent reads traces, writes evals, and fixes what fails.

## Sandboxing

Where agent isolation should live: the workstation, the cluster, the wrapper, the framework, or the provisioning layer.

- [Agent Sandbox](agent-sandbox/index.md) - the Kubernetes SIG Apps CRD for declarative sandbox fleets, delegating isolation to gVisor or Kata.
- [aigate](aigate/index.md) - the fourteen-star kernel-enforced wrapper, kept as the reference design for small-scale OS-level agent sandboxing.
- [ArtifactFS](artifact-fs/index.md) - Cloudflare's FUSE driver that mounts big repos in seconds, the provisioning layer sandboxes need before isolation matters.
- [Flue](flue/index.md) - the Astro team's agent framework whose contribution is a three-tier sandbox taxonomy and durable execution.
- [OpenShell](openshell/index.md) - NVIDIA's container-and-MicroVM runtime where declarative policy and inference-proxy keys make the boundary credible.

## Spec-driven development

- [BMad Method](bmad-method/index.md) - the agile method that sizes ceremony to the change, roles and retrospectives included.
- [GitHub Spec Kit](spec-kit/index.md) - the MIT process-plus-CLI layer that made specs-before-agents a movement, agent-neutral, 132k stars in year one.
- [OpenSpec](openspec/index.md) - the brownfield spec toolkit whose delta proposals archive into a living ledger, 1.6M npm downloads a month.
- [Tessl](tessl/index.md) - the $125M platform bet that spec-driven development is infrastructure you rent.

## Task management

- [Backlog.md](backlog-md/index.md) - the markdown-native task manager whose three review gates, spec, plan, code, make it the first line of code review.
- [beads](beads/index.md) - Steve Yegge's Dolt-backed graph issue tracker, dependency-aware with atomic claims, the agent-memory thesis in running code.
- [Task Master](task-master/index.md) - the most-installed PRD-to-tasks pipeline, quiet since April 2026 as it became Hamster's Commons-Clause commercial engine.

## Control planes

- [Paperclip](paperclip/index.md) - the MIT self-hosted control plane for a company of agents, heartbeats, budgets, and governance, 79k stars in six months.
- [TinyAGI](tinyagi/index.md) - the one-person-company orchestrator that stalled in March 2026, kept as the category's first consolidation record.

## Assistant runtimes

- [Eigent](eigent/index.md) - the Apache-2.0 Cowork desktop with CAMEL-based multi-agent workforces and a corrected-benchmark history.
- [Hermes](hermes/index.md) - Nous Research's self-improving agent with the learning loop, 238k stars and the channels to match.
- [NanoClaw](nanoclaw/index.md) - the auditable containerized OpenClaw rewrite, one process you can read in an afternoon.
- [Nanobot](nanobot/index.md) - HKUDS' readable Python agent runtime with the WebUI and channels bundled, 47k stars at alpha.
- [OpenClaw](openclaw/index.md) - the self-hosted personal assistant root of the -claw family, 388k stars and the 2026 provider-restriction saga.
- [OpenWork](openwork/index.md) - the MIT-core Cowork alternative built on OpenCode, whose MCP gateway makes skills portable across agents.
- [PicoClaw](picoclaw/index.md) - Sipeed's Go assistant on $10 RISC-V boards in 10-20MB of RAM, the category as a compile target.
- [QwenPaw](qwenpaw/index.md) - the AgentScope team's assistant with the broadest chat-channel matrix and five built-in security layers.
- [ZeroClaw](zeroclaw/index.md) - the single Rust binary runtime, ownership as a compile-time property.

## Software factory

- [Fluent](fluent/index.md) - the self-improving factory with a deterministic final Tester and a learning loop, for teams that accept pre-1.0 ceremony.
- [HAR](har/index.md) - the open harness that isolates a fleet of coding agents in worktrees with deterministic verification and an evidence trail.
- [Ouroboros](ouroboros/index.md) - the Agent OS that freezes a spec from an interview and verifies with the grading hidden from the worker, 13 runtimes.
- [Super Simple Software Factory](super-simple-software-factory/index.md) - a repeatable agents-plus-code pipeline stamped into any repo as a skill, where Python owns the loop and each agent owns one bounded phase.

## Session analytics

Tools that turn what coding agents already record into searchable history, cost reports, and audits.

- [agentsview](agentsview/index.md) - the local-first indexer for roughly 50 agents' session files, retrospective search and token-cost reporting in one SQLite store.

## People and publications

Profiles of the people and websites shaping this domain as it evolves, and the lens each brings: hands-on practice, industry synthesis, or conceptual vocabulary.

- [AI Jason](ai-jason/index.md) - the video practitioner who shows agent workflows and context engineering working end to end.
- [Andrej Karpathy](andrej-karpathy/index.md) - the vocabulary-setter, from vibe coding to Software 3.0 and agentic engineering.
- [Andrew Ng](deeplearning-ai-andrew-ng/index.md) - the educator whose weekly The Batch and courses popularized agentic design patterns.
- [Caleb Writes Code](caleb-writes-code/index.md) - the video explainer that turns model releases and agentic-engineering concepts into same-week, illustrated shorts.
- [Chip Huyen](chip-huyen/index.md) - the systems-design author of the most-read O'Reilly AI book of 2025.
- [Hamel Husain](hamel-husain/index.md) - the eval-driven method for deciding whether an AI product actually works.
- [Latent Space](latent-space/index.md) - the AI engineering newsletter-podcast-conference of record, by swyx and Alessio.
- [Lilian Weng](lilian-weng/index.md) - the reference writer whose agent survey is the canonical map of planning, memory, and tool use.
- [Nathan Lambert](nathan-lambert/index.md) - the inside-the-labs voice on models, post-training, and the open ecosystem.
- [Simon Willison](simon-willison/index.md) - the daily, hands-on chronicler of tools and agents.
- [Steve Yegge](steve-yegge/index.md) - the operative who builds the agent systems he predicts, Gas Town and the brute squad.
- [The Pragmatic Engineer](the-pragmatic-engineer/index.md) - Gergely Orosz's org-and-data view of how engineering teams adopt agents.

Notes appear here, alphabetically, as the daily agent runs publish them.
