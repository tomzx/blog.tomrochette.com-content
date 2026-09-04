---
title: Semantic code search in coding tools
created: 2026-08-24
updated: 2026-08-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, code-retrieval, embeddings, rag]
readability: 3
audience_notes: >
  Engineers building or evaluating codebase retrieval inside AI coding tools.
  Assumes familiarity with embeddings, vector indexes, and agentic tool loops.

---

Semantic code search is retrieval over a codebase by meaning (vector similarity over embedded chunks) rather than literal match, shipped inside coding tools as an automatically built workspace index.
Facts below verified as of 2026-09-04.

**Built-in embeddings indexes are retreating from coding tools: the pioneers are replacing them with agentic grep loops, and the tools keeping semantic search are moving the index to the platform or making it optional.**

## What it is

Each shipping implementation differs in where the index lives.
Cursor embeds code chunks server-side with encrypted chunks and client-side decryption, but its retrieval docs now lead with Instant Grep (a custom engine claimed to outperform ripgrep) and an Explore subagent that runs parallel searches in its own context window.
VS Code Copilot exposes `#codebase` semantic search backed by an index built either remotely by GitHub (per repository, shared) or locally, while the same agent also runs grep, text search, file search, and usages tools.
Continue's legacy `@Codebase` provider computed embeddings locally with transformers.js, hybrid keyword search, and LLM reranking (25 retrieved, 5 final) into a local sqlite index.
Devin Desktop (the former Windsurf) documents a RAG context engine that indexes the local codebase and, for Teams and Enterprise, remote repositories, using M-Query retrieval.

## Status

**Active as a capability, demoted as a default.**
Continue deprecated `@Codebase` in favor of agent file-exploration tools, rules files, and MCP servers, keeping code RAG only as an advanced build-your-own path.
VS Code states that when no semantic index is ready, the other tools "still provide great results".
Aider never shipped embeddings at all, ranking tree-sitter symbols by graph references instead.

## Strengths

- **Concept queries work without knowing identifiers**: "where is authentication handled" finds code grep cannot name.
- Privacy-preserving designs exist and are documented: fully local embeddings (Continue's legacy path) or encrypted chunks decrypted client-side (Cursor).
- A shared index amortizes cost: GitHub builds one index per repository, and Cursor shares team indexes for similar codebases.

## Cautions

- **Freshness**: an index lags the working tree, while grep and usages are always current, which matters most exactly when agents edit code.
- Vendors themselves hedge: Continue deprecated its provider, and VS Code positions the index as an accelerator with a no-index fallback.
- Chunk quality bounds recall; embeddings of code capture names and comments more than behavior.
- Index limits are plan-gated (Devin ties larger indexes and remote repositories to Pro, Teams, and Enterprise tiers), so retrieval quality becomes a billing variable.
- The skeptical case here is built entirely from vendor retreat; no independent benchmark defending codebase embeddings had surfaced as of 2026-08-24, which is itself a signal about where the evidence lives.

## Pricing

Not applicable as a standalone product.
In practice: bundled into tool subscriptions (Cursor, VS Code Copilot, Devin) with plan-gated index limits, or self-built at embedding-API cost, as in Continue's guide recommending voyage-code-3 plus LanceDB.
**The index is either someone else's cloud cost buried in a seat price, or your API bill.**

## Compared to

- Agentic grep loops (Cursor's Instant Grep, subagents): always current, cheap, inspectable; weaker on concept-only queries.
- Graph-ranked repo maps (aider): deterministic, symbol-level, no embeddings or index maintenance.
- Platform-side indexing (VS Code via GitHub): zero setup and shared, but bound to GitHub-hosted repositories and its rollout policies.

## Bottom line

**Recommended as one signal among several, never as the single retriever; if your tool ships semantic search, use it, but do not design your workflow around the index existing.**
My disagreeable claim: local embeddings indexes will keep disappearing from major coding tools because agentic search wins on freshness and cost, and in 2026 a team building its own code RAG should treat the index as an optional accelerator behind a grep-first agent.
The Devin and VS Code platform bets are the counterargument, and they may well win on the enterprise side.

## See also

- [Cursor](../cursor/index.md) - the tool most visibly shifting from index to grep plus subagents
- [VS Code Copilot](../vscode-copilot/index.md) - semantic indexing moved to the GitHub platform
- [Windsurf](../windsurf/index.md) - the editor whose docs now double down on RAG context as Devin Desktop
- [Aider](../aider/index.md) - the no-embeddings counterexample via graph-ranked repo maps
- [LlamaIndex](../llamaindex/index.md) - framework-grade machinery if you build indexing yourself

## References

- https://cursor.com/docs/context/codebase-indexing - Instant Grep, Explore subagent, and the encrypted-embeddings privacy model
- https://code.visualstudio.com/docs/agents/reference/workspace-context - Copilot's search tool set, semantic index sources, and no-index fallback
- https://docs.continue.dev/reference/deprecated-codebase - the deprecated local embeddings pipeline (transformers.js, hybrid retrieval, LLM reranking)
- https://docs.continue.dev/guides/codebase-documentation-awareness - the replacement model: agent tools, rules, and MCP servers
- https://docs.devin.ai/desktop/context-awareness/windsurf-overview - the RAG context engine and plan-gated indexing in Devin Desktop
- https://aider.chat/docs/repomap.html - graph-ranked repo maps as retrieval without embeddings
