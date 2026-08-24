---
title: LangChain
created: 2026-08-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, rag, agents, frameworks]
readability: 3
audience_notes: >
  Engineers selecting an agent or RAG framework, assumed to have shipped at least one LLM application and to know the 2024 abstraction criticism.

---

LangChain is the largest open source LLM application framework, repositioned in 2026 as an "agent engineering platform" spanning the create_agent harness, LangGraph orchestration, Deep Agents, and a terminal coding agent called dcode.
Facts below verified as of 2026-08-24.

**The coding-agent angle is now real and first-party: LangChain ships its own terminal coding agent, which moves it from "tooling you might build on" to "competitor in your harness choice".**

## What it is

The MIT-licensed OSS stack has three layers: LangChain's `create_agent` (a minimal model plus tools plus middleware harness), LangGraph (low-level durable agent workflows), and Deep Agents (batteries-included planning, subagents, virtual filesystem, context compression).
**Deep Agents Code (`dcode`) is an open source terminal coding agent with persistent memory, skills, subagents, remote sandboxes, and approval gates, installable independently of any LangChain service.**
The commercial side is LangSmith: tracing, evaluation, deployment, sandboxes, and the no-code Fleet agents.

## Status

Active and dominant by footprint.
The `langchain-ai/langchain` repository shows 144.9k stars, 24.1k forks, and 16,656 commits as of 2026-08-24.
**The telling history: after the 2024 "death by abstraction" wave, the company publicly moved to lower-level primitives (LangGraph, then create_agent), and is now climbing back up with Deep Agents, dcode, and OpenWiki, a CLI that writes agent wikis for coding agents.**

## Strengths

- **The most portable model interface in the field**: one API across OpenAI, Anthropic, Google, Bedrock, Ollama, and dozens more, which is the layer that actually resists churn.
- Retrieval docs now teach agentic RAG (2-step, agentic, hybrid) instead of pushing one big retrieval chain.
- dcode inherits Deep Agents' context compression and subagents, and runs with any provider key you own.
- LangSmith evaluation and tracing remain the most mature observability pair for agents built this way.

## Cautions

- **Trust debt is the core risk**: the Octomind post (480 points, 297 comments) documents teams abandoning the framework for leaky abstractions, and while the CEO responded by moving investment lower-level, every new layer (Deep Agents, dcode) asks users to be burned twice.
- Ecosystem sprawl: choosing between LangChain, LangGraph, and Deep Agents is genuine design work, and the docs themselves need a decision tree for it.
- The retrieval stack is generic text RAG: the current text splitters catalog offers separator-based code splitting only, with no AST chunker.
- The polished experience assumes LangSmith, a paid SaaS, for tracing and evaluation.

## Pricing

OSS (LangChain, LangGraph, Deep Agents, dcode): free, MIT.
LangSmith as of 2026-08-24: Developer $0 with 5k base traces/month, Plus $39/seat/month with 10k base traces, Enterprise custom, plus metered units (LCU at $1.50, LSU at $1.00) for deployments, sandboxes, Engine, and Fleet.
**The framework is free forever; the operations layer around it is where the bill lives.**

## Compared to

- [LlamaIndex](../llamaindex/index.md): deeper retrieval modules, thinner agent platform; pair them or split by primary need.
- Established terminal harnesses (Claude Code, Codex, OpenCode): dcode is a credible new entrant but the incumbents have years of editor, CI, and workflow integration.
- Hand-rolled agent loops: for a single provider and a stable tool set, direct SDK plus a loop avoids the abstraction tax the HN thread documents.

## Bottom line

**Recommended for teams building multi-provider agent systems who will also adopt LangSmith, and for anyone wanting an ownable coding agent they can fork rather than subscribe to.**
I would not pick LangChain in 2026 purely for RAG, its original job: retrieval has commoditized into provider APIs and agentic search, and the differentiating value has moved to the harness and evaluation layers.
Disagree if you like; the retrieval-first framing is my call, not the docs'.

## See also

- [LlamaIndex](../llamaindex/index.md) - the retrieval-first counterpart, pivoting to documents
- [Claude Code](../claude-code/index.md) - the harness incumbent that dcode enters against
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where framework vendors now collide with harness vendors
- [The Importance of Context When Interacting with LLMs](../../the-importance-of-context-when-interacting-with-llms/index.md) - the underlying reason retrieval and context beat raw model choice

## References

- https://github.com/langchain-ai/langchain - repository scale (144.9k stars), MIT license, platform positioning, as of 2026-08-24
- https://docs.langchain.com/oss/deepagents/code/overview.md - dcode, the terminal coding agent built on Deep Agents
- https://docs.langchain.com/oss/python/langchain/retrieval.md - RAG architectures: 2-step, agentic, hybrid, and the agentic-RAG-first framing
- https://www.langchain.com/pricing - LangSmith tiers and LCU/LSU metering, as of 2026-08-24
- https://news.ycombinator.com/item?id=40739982 - the Octomind critique thread with the CEO's response acknowledging over-abstraction
- https://python.langchain.com/api_reference/text_splitters/text_splitters/code_splitter.html - current text splitters catalog, showing separator-based code splitting only
