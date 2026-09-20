---
title: Graphify
created: 2026-08-30
updated: 2026-09-20
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, knowledge-graphs, code-intelligence, open-source]
readability: 3
audience_notes: >
  Engineers deciding how their coding agent should learn a large codebase, who are weighing graph indexing against packing or embeddings.
  Assumes you know what an AST, a vector store, and an MCP server are.
---

Graphify is an open-source Python CLI that turns a codebase, plus its docs, SQL schemas, and PDFs, into a queryable knowledge graph exposed as a `/graphify` skill and MCP server for coding assistants, built on local deterministic tree-sitter parsing with no vector store.
Facts below verified as of 2026-09-20.

**Graphify's bet is that structure beats similarity: an agent that can traverse exact calls-and-imports edges with file:line citations needs less context than one searching embeddings, and the code path runs entirely on your machine.**
The bet is young, self-benchmarked, and wrapped in a YC company's funnel.

## What it is

One command builds `graphify-out/`: an interactive `graph.html`, a `GRAPH_REPORT.md` with god nodes and communities, and `graph.json` with the full graph, which you then query through `graphify query`, `path`, and `explain` instead of grepping.
Code is parsed with tree-sitter across 36 code languages (the project site's count as of 2026-09-18), resolving calls, imports, and inheritance edges deterministically with no LLM; docs, PDFs, and images go through a semantic pass using your assistant's model or a configured API key.
Every edge is tagged EXTRACTED, INFERRED, or AMBIGUOUS, so readable facts are distinguishable from guessed ones, and queries return subgraphs with file:line citations.
A skill installer targets Claude Code, Cursor, Codex, Gemini CLI, OpenCode, and 20+ other platforms, plus an MCP server and exports to Neo4j and Obsidian.
Made by Graphify Labs, a YC Summer 2026 company of two people in London, Apache-2.0, with the PyPI package named `graphifyy`.

## Status

Growing absurdly fast for its age: 119,720 stars and 1,843 commits in about five months since 2026-04-03, latest release v0.9.64 on 2026-09-18, all as of 2026-09-20, with 253 contributors as of 2026-09-18.
The YC page claims 5M+ downloads and named production users, all self-reported.
The ecosystem is growing too: a third-party C# port, graphify-csharp, launched September 11, 2026 with a 46-point Show HN and 21 comments as of 2026-09-16, the largest discussion any Graphify-linked project has drawn.
**The star count still outruns the discussion footprint: Hacker News stories linking the main repo drew two or three points with no comments, a mismatch I treat as a flag, not a slam dunk.**

## Strengths

- The code-only path is fully local and key-free, so the default workflow leaks nothing.
- Edge-level provenance (EXTRACTED versus INFERRED with file:line) is a real answer to the trust problem in generated context.
- One graph covers code and its non-code artifacts, and the skill installs across most harnesses your team already runs.
- Shipping velocity is exceptional, with another release (v0.9.64) landing two days before this re-verification and a published benchmark methodology.

## Cautions

- The benchmarks are self-published, and on the headline QA-accuracy metric graphify trails supermemory while winning on cost and recall, per its own BENCHMARKS.md.
- Only code is local: docs, PDFs, and images are sent to whatever LLM backend is configured.
- Pre-1.0 with 1,425 open issues and PRs as of 2026-09-20, a nonstandard default branch, and acknowledged PyPI name-squatting on `graphify*` packages.
- The free CLI is the top of an open-core funnel into a hosted product whose plans only recently gained public prices, so expect the monetization posture to keep moving.

## Pricing

The core CLI is free, Apache-2.0, no account.
The hosted side now publishes four plans (as of 2026-09-18): Free ($0, one developer, no card, with node, build, and review allowances), Pro ($10/month billed yearly or $15 billed monthly, one developer, uncapped graphs), Teams ($20 per seat/month billed yearly or $29 billed monthly, minimum 2 seats, rising to $28 yearly and $40 monthly after the first 100 teams), and Enterprise (early access, self-hosted, licensed per seat, with the price scoped on a call instead of published), plus free access for qualified MIT and Apache licensed OSS projects.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-18 | Hosted plans | First published ladder: Free $0 (one developer), Pro $10/mo billed yearly or $15 monthly, Teams $20/seat/mo yearly or $29 monthly (min 2 seats), Enterprise scoped on a call; core CLI free (Apache-2.0). | [graphify.com/pricing](https://graphify.com/pricing) |

## Compared to

- [Repomix](../repomix/index.md): flattens a whole repo into one file for a single prompt; choose Graphify for repeated agentic Q&A over a codebase, Repomix for one-shot context sharing.
- [Sourcegraph code context platform](../sourcegraph-code-context/index.md): org-wide search across many repositories; choose Graphify for deep structural reasoning about one codebase inside an agent.
- [Semantic code search](../../retrieval/semantic-code-search/index.md): embeddings find similar chunks for vague queries; Graphify returns exact connection paths with citations when you need to know how things connect.

## Bottom line

**Recommended for teams whose agents burn tokens re-discovering how a large codebase connects, who can tolerate pre-1.0 churn and verify the benchmarks on their own repo.**
Not for small repos where grep and packing are enough, or for buyers who need independent evidence before adoption.

## Changes

- 2026-08-30 - Created as a Context engines note covering the local AST knowledge graph, with the self-benchmarked caveat recorded.
- 2026-09-12 - Recorded the newly published hosted plans (Free, Pro $10, Teams $20 per seat, Enterprise) and folded the graphify-csharp port in as ecosystem evidence.
- 2026-09-16 - Re-verified: release v0.9.62, 118,127 stars, 266 contributors, and the hosted plans gained monthly billing options (Pro $15/month, Teams $29/seat/month) while annual prices held; Enterprise is now early access, per seat, priced on a call.
- 2026-09-18 - Re-verified: release v0.9.63, 119,153 stars, 1,810 commits, 253 contributors, 1,394 open issues and PRs; the edge provenance model now documents a third tag, AMBIGUOUS, alongside EXTRACTED and INFERRED; hosted plans unchanged; the C# port reached 67 stars.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-20 - Recorded release v0.9.64 (2026-09-18) and refreshed the volatile numbers (119,720 stars, 1,843 commits, 1,425 open issues and PRs); hosted plans unchanged.

## See also

- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins
- [Repomix](../repomix/index.md) - the packing counterargument
- [Sourcegraph code context platform](../sourcegraph-code-context/index.md) - the enterprise-scale alternative
- [MCP](../../protocols/mcp/index.md) - one of the two delivery surfaces

## References

- https://github.com/Graphify-Labs/graphify - repository, README, architecture, license, adoption numbers
- https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/BENCHMARKS.md - the self-published benchmarks, including the supermemory trade-off
- https://graphify.com/ - positioning and the no-embeddings claim
- https://graphify.com/pricing - the four hosted plans above the free core
- https://graphify.com/llms-full.txt - the full plan table grounding the pricing section (monthly and annual billing), fetched 2026-09-18
- https://pypi.org/project/graphifyy/ - the distribution and current version
- https://www.ycombinator.com/companies/graphify-labs - the maker, batch, and self-reported adoption claims
- https://github.com/zachsaw/graphify-csharp - the third-party C# port, 67 stars as of 2026-09-18
- https://news.ycombinator.com/item?id=49667188 - the port's Show HN thread, 46 points and 21 comments, verified via the Algolia API
