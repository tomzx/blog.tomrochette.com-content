---
title: Graphify
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, knowledge-graphs, code-intelligence, open-source]
readability: 3
audience_notes: >
  Engineers deciding how their coding agent should learn a large codebase, who are weighing graph indexing against packing or embeddings.
  Assumes you know what an AST, a vector store, and an MCP server are.
---

Graphify is an open-source Python CLI that turns a codebase, plus its docs, SQL schemas, and PDFs, into a queryable knowledge graph exposed as a `/graphify` skill and MCP server for coding assistants, built on local deterministic tree-sitter parsing with no vector store.
Facts below verified as of 2026-08-30.

**Graphify's bet is that structure beats similarity: an agent that can traverse exact calls-and-imports edges with file:line citations needs less context than one searching embeddings, and the code path runs entirely on your machine.**
The bet is young, self-benchmarked, and wrapped in a YC company's funnel.

## What it is

One command builds `graphify-out/`: an interactive `graph.html`, a `GRAPH_REPORT.md` with god nodes and communities, and `graph.json` with the full graph, which you then query through `graphify query`, `path`, and `explain` instead of grepping.
Code is parsed with tree-sitter across roughly 40 languages, resolving calls, imports, and inheritance edges deterministically with no LLM; docs, PDFs, and images go through a semantic pass using your assistant's model or a configured API key.
Every edge is tagged EXTRACTED or INFERRED, so readable facts are distinguishable from guessed ones, and queries return subgraphs with file:line citations.
A skill installer targets Claude Code, Cursor, Codex, Gemini CLI, OpenCode, and 20+ other platforms, plus an MCP server and exports to Neo4j and Obsidian.
Made by Graphify Labs, a YC Summer 2026 company of two people in London, Apache-2.0, with the PyPI package named `graphifyy`.

## Status

Growing absurdly fast for its age: 112,374 stars and 1,608 commits in about five months since 2026-04-03, latest release v0.9.52 on 2026-08-29, 225 contributors.
The YC page claims 5M+ downloads and named production users, all self-reported.
**The star count outruns the discussion footprint: Hacker News stories linking the repo drew two or three points with no comments, a mismatch I treat as a flag, not a slam dunk.**

## Strengths

- The code-only path is fully local and key-free, so the default workflow leaks nothing.
- Edge-level provenance (EXTRACTED versus INFERRED with file:line) is a real answer to the trust problem in generated context.
- One graph covers code and its non-code artifacts, and the skill installs across most harnesses your team already runs.
- Shipping velocity is exceptional, with a release the day before verification and a published benchmark methodology.

## Cautions

- The benchmarks are self-published, and on the headline QA-accuracy metric graphify trails supermemory while winning on cost and recall, per its own BENCHMARKS.md.
- Only code is local: docs, PDFs, and images are sent to whatever LLM backend is configured.
- Pre-1.0 with 1,158 open issues and PRs, a nonstandard default branch, and acknowledged PyPI name-squatting on `graphify*` packages.
- The free CLI is the top of an open-core funnel into an early-access enterprise platform, so expect the monetization posture to keep moving.

## Pricing

The core CLI is free, Apache-2.0, no account.
An enterprise platform (merge-gate verification, graph-aware review, self-hosted deployment) is in early access with no public prices.

## Compared to

- [Repomix](../repomix/index.md): flattens a whole repo into one file for a single prompt; choose Graphify for repeated agentic Q&A over a codebase, Repomix for one-shot context sharing.
- [Sourcegraph code context platform](../sourcegraph-code-context/index.md): org-wide search across many repositories; choose Graphify for deep structural reasoning about one codebase inside an agent.
- [Semantic code search](../semantic-code-search/index.md): embeddings find similar chunks for vague queries; Graphify returns exact connection paths with citations when you need to know how things connect.

## Bottom line

**Recommended for teams whose agents burn tokens re-discovering how a large codebase connects, who can tolerate pre-1.0 churn and verify the benchmarks on their own repo.**
Not for small repos where grep and packing are enough, or for buyers who need independent evidence before adoption.

## See also

- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins
- [Repomix](../repomix/index.md) - the packing counterargument
- [Sourcegraph code context platform](../sourcegraph-code-context/index.md) - the enterprise-scale alternative
- [MCP](../mcp/index.md) - one of the two delivery surfaces

## References

- https://github.com/Graphify-Labs/graphify - repository, README, architecture, license, adoption numbers
- https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/BENCHMARKS.md - the self-published benchmarks, including the supermemory trade-off
- https://graphify.com/ - positioning and the no-embeddings claim
- https://graphify.com/pricing - the free-core and early-access-enterprise split
- https://pypi.org/project/graphifyy/ - the distribution and current version
- https://www.ycombinator.com/companies/graphify-labs - the maker, batch, and self-reported adoption claims
