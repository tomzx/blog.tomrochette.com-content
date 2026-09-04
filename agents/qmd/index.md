---
title: qmd
created: 2026-08-30
updated: 2026-09-02
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, retrieval, local-search, open-source]
readability: 3
audience_notes: >
  Engineers who want their agents to search notes, docs, and knowledge bases locally without shipping data to a cloud.
  Assumes you know what BM25, embeddings, and an MCP server are.
---

qmd is a local-first CLI search engine by Tobias Lütke that indexes your markdown notes, docs, and knowledge bases and searches them with a hybrid BM25 plus vector plus LLM-reranked pipeline, designed for humans and agents alike.
Facts below verified as of 2026-09-04.

**qmd is the argument that a single maintainer can ship production-grade local retrieval in one binary-plus-SQLite, and that most agent RAG does not need a framework, a server, or a cloud.**

## What it is

A TypeScript CLI (`@tobilu/qmd`, Node 22+ or Bun) with three modes: `search` for BM25 keyword, `vsearch` for semantic vectors, and `query` for the full hybrid stack.
The stack is real retrieval engineering running entirely on-device: SQLite FTS5, sqlite-vec with a 300M embedding model, LLM query expansion with typed sub-queries, reciprocal rank fusion, and a 0.6B cross-encoder reranker, about 2 GB of GGUF models downloaded on first use.
Markdown-aware chunking around 900 tokens with optional tree-sitter chunking for code; storage is one SQLite file in your cache directory.
Agent surfaces include `--json` output, doc-id and line-range retrieval, an MCP server (stdio and HTTP), an SDK, and a Claude Code plugin.
MIT, by Tobias Lütke (Shopify CEO), who authored about three quarters of the commits and confirmed the design intent on Hacker News.

## Status

Young with unusual traction: 29,441 stars, 1,839 forks, 131 open issues and PRs as of 2026-09-02, created 2025-12-08.
Latest release v2.8.3 on 2026-08-16, pushed 2026-08-18.
**The maintainer concentration is the story: one high-profile author shipping v1 through v2.8 in nine months, with community PRs around the edge.**

## Strengths

- The hybrid pipeline is the same architecture pattern production search uses, running locally with small models instead of an API.
- Agent-first surface area: JSON output, precise line-range retrieval, MCP, and an SDK, so results drop straight into a context window.
- Disciplined maintenance: a `qmd bench` command for measuring precision, recall, and MRR per backend, plus prompt-security fixes documented in the changelog.
- Fully local, so notes and knowledge bases never leave the machine.

## Cautions

- The footprint is not light: Node 22+, roughly 2 GB of models, Homebrew SQLite on macOS, and documented Windows and Metal rough edges.
- The v2.8.3 security notes disclose three past vulnerabilities, including arbitrary command execution from a cloned repo's index config and DNS rebinding against the HTTP MCP server, all fixed, all indicative of an agentic tool's attack surface.
- Quality claims come from the project's own fixtures, with no independent evaluation, and an open bug reports the reranker wedging the MCP daemon on large documents.
- Single-maintainer risk with repeated behavior changes across the v2 line.

## Pricing

Free and open source under MIT, fully local, no cloud component.
The costs are disk and local compute.

## Compared to

- Plain grep and ripgrep: instant and exact when you know the tokens; qmd wins when the answer does not contain your query words and agents need ranked, scored snippets.
- [LangChain](../langchain/index.md) and [LlamaIndex](../llamaindex/index.md): frameworks for building custom retrieval products; qmd is a finished zero-code product, and the right choice when local files are the whole corpus.
- [Semantic code search](../semantic-code-search/index.md): the workspace-index pattern for codebases; qmd targets prose and notes, and the two compose rather than compete.

## Bottom line

**Recommended for engineers whose agents need to find things in personal docs, meeting notes, and knowledge bases without sending them anywhere, and who can afford 2 GB of models.**
Not for code-symbol search (use grep-class tools), constrained machines, or teams needing vendor support.

## See also

- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins
- [Retrieval Feature Matrix](../retrieval-feature-matrix/index.md) - where the RAG patterns sit
- [Semantic code search](../semantic-code-search/index.md) - the codebase-side counterpart
- [LlamaIndex](../llamaindex/index.md) - the framework alternative

## References

- https://github.com/tobi/qmd - repository, description, license
- https://raw.githubusercontent.com/tobi/qmd/HEAD/README.md - architecture, install, models, MCP and SDK surfaces
- https://raw.githubusercontent.com/tobi/qmd/HEAD/CHANGELOG.md - release cadence, security fixes, platform issues
- https://api.github.com/repos/tobi/qmd - exact stars, forks, and dates as of 2026-09-02
- https://news.ycombinator.com/item?id=46689289 - the author on design intent and local-first trade-offs
