---
title: LangChain
created: 2026-08-24
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, rag, agents, frameworks]
readability: 3
audience_notes: >
  Engineers selecting an agent or RAG framework, assumed to have shipped at least one LLM application and to know the 2024 abstraction criticism.

---

LangChain is the largest open source LLM application framework, repositioned in 2026 as an "agent engineering platform" spanning the create_agent harness, LangGraph orchestration, Deep Agents, and a terminal coding agent called dcode.

**The coding-agent angle is now concrete and first-party: LangChain ships its own terminal coding agent, which moves it from "tooling you might build on" to "competitor in your harness choice".**

## What it is

The MIT-licensed OSS stack has three layers: LangChain's `create_agent` (a minimal model plus tools plus middleware harness), LangGraph (low-level durable agent workflows), and Deep Agents (batteries-included planning, subagents, virtual filesystem, context compression).
**Deep Agents Code (`dcode`) is an open source terminal coding agent with persistent memory, skills, subagents, remote sandboxes, and approval gates, installable independently of any LangChain service.**
The commercial side is LangSmith: tracing, evaluation, deployment, sandboxes, and the no-code Fleet agents.

## Status

Active and dominant by footprint.
The `langchain-ai/langchain` repository shows 147.8k stars (147,789) and 24.8k forks as of 2026-10-13, extending the recovery above the 147.4k recorded 2026-10-09, with 17,067 commits and a push on 2026-10-25 (GitHub, as of 2026-10-25).
The next-day recovery supports the reading that the dip was GitHub's periodic removal of bulk-created accounts, not an adoption signal.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=langchain-ai/langchain&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=langchain-ai/langchain&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=langchain-ai/langchain&type=date&legend=top-left" />
</picture>

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
LangSmith as of 2026-10-19: Developer $0 with 5k base traces/month, Plus $39/seat/month with 10k base traces, Enterprise custom, with usage metered in LangChain Standard Units at $1.00 per LSU across Deployment, Sandboxes, Engine, and Fleet.
**The framework is free forever; the operations layer around it is where the bill lives.**

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-18 | LangSmith | Baseline: OSS free (MIT); LangSmith Developer $0 (5k traces/mo), Plus $39/seat/mo (10k traces), Enterprise custom, metered units LCU $1.50 and LSU $1.00. | [langchain.com/pricing](https://www.langchain.com/pricing) |
| 2026-10-02 | LangSmith | The LCU ($1.50) line item no longer appears on the pricing page; usage metering is consolidated in LSUs at $1.00, plan prices unchanged. | [langchain.com/pricing](https://www.langchain.com/pricing) |

## Compared to

- [LlamaIndex](../llamaindex/index.md): deeper retrieval modules, thinner agent platform; pair them or split by primary need.
- Established terminal harnesses (Claude Code, Codex, OpenCode): dcode is a credible new entrant but the incumbents have years of editor, CI, and workflow integration.
- Hand-rolled agent loops: for a single provider and a stable tool set, direct SDK plus a loop avoids the abstraction tax the HN thread documents.

## Bottom line

**Recommended for teams building multi-provider agent systems who will also adopt LangSmith, and for anyone wanting an ownable coding agent they can fork rather than subscribe to.**
I would not pick LangChain in 2026 purely for RAG, its original job: retrieval has commoditized into provider APIs and agentic search, and the differentiating value has moved to the harness and evaluation layers.
Disagree if you like; the retrieval-first framing is my call, not the docs'.

## Changes

- 2026-08-24 - Created among the seed notes of the Retrieval category.
- 2026-09-18 - Refreshed volatile facts for the 2026-09-18 verification: 146.6k stars, 24.5k forks, 16,782 commits, LangSmith pricing re-confirmed unchanged.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-25 - Refreshed volatile facts: 147.0k stars, 24.6k forks, 16,852 commits as of 2026-09-25; LangSmith pricing re-confirmed unchanged.
- 2026-10-02 - Recorded the LangSmith pricing page consolidating metering in LSUs at $1.00 with the LCU ($1.50) line item gone, appended the price history row, and refreshed the repository numbers (147.4k stars, 24.7k forks, 16,908 commits).
- 2026-10-07 - Added the langchain-ai/langchain star history chart to the Status section.
- 2026-10-09 - Recorded the first star-count decline in the note's tracking, 147.4k (147,424) as of 2026-10-09 against 147.5k recorded 2026-10-07, and re-verified LangSmith pricing unchanged.
- 2026-10-10 - Recorded the star count recovering to 147.5k (147,536) one day after the first recorded decline, supporting the bulk-account-removal reading, with commits refreshed to 16,965.
- 2026-10-11 - Reworded a banned-term word out of the thesis and refreshed the volatile numbers (147.6k stars, 147,579, as of 2026-10-11); LangSmith pricing re-verified unchanged.
- 2026-10-22 - Rotation re-verification re-fetched every cited URL live (the dcode docs, the retrieval architectures page, the Octomind thread, and LangSmith pricing all unchanged), refreshed the repository activity (17,048 commits, pushed 2026-10-22), and re-confirmed the text-splitters catalog still has no AST chunker.
- 2026-10-24 - Refreshed the repository activity (17,059 commits, pushed 2026-10-24); pricing and docs claims untouched since the 2026-10-22 rotation.
- 2026-10-25 - Refreshed the repository activity (17,067 commits, pushed 2026-10-25).

## See also

- [LlamaIndex](../llamaindex/index.md) - the retrieval-first counterpart, pivoting to documents
- [Claude Code](../../harnesses/claude-code/index.md) - the harness incumbent that dcode enters against
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - where framework vendors now collide with harness vendors
- [The Importance of Context When Interacting with LLMs](../../../the-importance-of-context-when-interacting-with-llms/index.md) - the underlying reason retrieval and context beat raw model choice

## References

- https://github.com/langchain-ai/langchain - repository scale (147.8k stars as of 2026-10-13), MIT license, platform positioning, pushed 2026-10-25, 17,067 commits (fetched 2026-10-25)
- https://docs.langchain.com/oss/deepagents/code/overview.md - dcode, the terminal coding agent built on Deep Agents (re-verified unchanged 2026-10-22)
- https://docs.langchain.com/oss/python/langchain/retrieval.md - RAG architectures: 2-step, agentic, hybrid, and the agentic-RAG-first framing (re-verified unchanged 2026-10-22)
- https://www.langchain.com/pricing - LangSmith tiers and LSU metering, as of 2026-10-22 (re-verified unchanged; previously recorded 2026-10-07, 2026-10-09, 2026-10-11, 2026-10-13, and 2026-10-19)
- https://news.ycombinator.com/item?id=40739982 - the Octomind critique thread with the CEO's response acknowledging over-abstraction (re-verified 2026-10-22, 480 points)
- https://python.langchain.com/api_reference/text_splitters/text_splitters/code_splitter.html - the text-splitters package catalog, separator-based code splitting only and no AST chunker class (re-verified 2026-10-22; the page now serves the package class index)
