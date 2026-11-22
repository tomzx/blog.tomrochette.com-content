---
title: Code-Graph-RAG
created: 2026-10-07
updated: 2026-11-22
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, retrieval, code-retrieval, knowledge-graph, rag]
readability: 3
audience_notes: >
  Engineers wiring codebase retrieval into an agent loop who want structural, graph-backed
  answers instead of embedding similarity.
  Assumes familiarity with tree-sitter, graph databases, and Cypher.
---

Code-Graph-RAG is an MIT-licensed Python system that parses a multi-language codebase with tree-sitter plus compiler-grade frontends into a knowledge graph stored in an embedded SQLite database by default (Memgraph and Neo4j are opt-in backends) and answers natural-language questions and edit requests through an agent that writes Cypher.

**It pushes code retrieval past similarity search entirely: functions, classes, calls, and imports live in a graph, so the questions it answers well are structural ones (what calls this, what breaks if this changes) that embeddings index cannot address at all.**

## What it is

A `cgr` CLI (PyPI `code-graph-rag`) with two components.
The parser layer reads every source file with tree-sitter, sharpens facts with compiler frontends where a toolchain exists (libclang for C and C++, go/types for Go, opt-in Roslyn, javac, and Jedi for C#, Java, and Python), and can overlay runtime behavior by tracing a test run or pulling production eBPF profiles into the graph.
The RAG layer turns natural language into Cypher over the graph backend, retrieves the matching code, and drives AST-based surgical patching with a diff preview.
The graph is an embedded SQLite file by default (no server, no Docker), with Memgraph and Neo4j available as opt-in backends over the same Cypher.
Python, TypeScript, JavaScript, Rust, Go, Java, C, C++, C#, PHP, Lua, Dart, and Julia are fully supported, with structural support for Ruby, Kotlin, Swift, Elixir, Haskell, Solidity, Bash, and Nix on a pluggable ast-grep tier, under one language-agnostic schema across a monorepo.
Made by an independent developer, with an enterprise support and services badge on the README.

## Status

**Actively shipping and early: 5.2k stars in sixteen months with almost no independent discussion.**
5,252 stars and 702 forks as of 2026-10-14, pushed 2026-11-22 with the default branch's latest commit a reexport-caller-check PR merge (dated 2026-11-22), with 306 open issues (GitHub API, as of 2026-11-22).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=vitali87/code-graph-rag&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=vitali87/code-graph-rag&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=vitali87/code-graph-rag&type=date&legend=top-left" />
</picture>

PyPI shows version 0.6.62 released 2026-11-15 across 41 releases: 0.2.0 (2026-10-15) was the first release past the 0.1 line that carried all 27 of the preceding ones, ten point releases landed in the three days after it, the 0.2 line ran to 0.2.24 by 2026-10-23, the 0.3 line opened the next day and reached 0.3.13 by 2026-10-25, the 0.4 line opened 2026-10-30 at 0.4.5, whose notes gate a repository's `.cgr.md` out of the agent's system prompt until its content is approved, ran to 0.4.19 by 2026-11-02, and the 0.5 line opened 2026-11-03 at 0.5.0, whose NEWS headlines are JavaScript signature reading and writing for change signatures plus the Rust toolchain bump; PyPI never saw a 0.5.x publish past 0.5.0 even as the main branch's version bumps ran to 0.5.14, and the 0.6 line opened 2026-11-08 at 0.6.0 and jumped straight to 0.6.30 by 2026-11-09 (the main branch meanwhile bumped on to 0.6.39), whose NEWS headlines are Python and TypeScript type handling for walrus operators and match binding targets, Go rename refinement, and ES-module resolution fixes; the four NEWS entries that had grown past the 0.6.30 headlines (pprof profile naming, a raised Anthropic output budget, dead-code roots for IPython rich-display methods, and incremental refresh updating callers when dispatch targets change) rendered into the 0.6.62 publish together with five new headlines (CommonJS renamed-property import resolution, incremental syncs that retain class field types, receiver-scoped Python property reads, rejected cross-language internal import targets, and constructor attribute-field initializer handling in TS/JS, Java, and C#), and the README documents the cadence, PyPI and GitHub Releases carrying every 50th version plus security fixes, breaking changes, and release-now merges, so this 32-version jump caught the installable release up to the main branch's version bump on its release day, and the 0.7 line opened 2026-11-17 at 0.7.1 with no 0.7.0 published, then jumped straight to 0.7.79 on 2026-11-21 (43 releases total), the catch-up pattern again: the NEWS entries grown past the 0.7.1 headlines rendered into the publish together with two new headlines, refined code analysis (how query captures are read, how calls are judged, and how dead code is identified) and a surface-definition mechanism that records and enforces a codebase's public surface with CI failures for deviations.
Two Show HNs (February and March 2026) drew 1 point each, so the star count ran far ahead of any independent technical debate, the same pattern Knowhere and open-codebase-index in this section show.

## Strengths

- **Blast-radius questions are its home turf: call graphs, reference walks, and dead-code discovery from entry points are native graph queries, not retrieval approximations.**
- The layered parser is the right architecture: tree-sitter for coverage, compiler frontends for precision where available, runtime traces for the dispatch static analysis cannot see.
- One unified graph schema across a polyglot monorepo is the case where per-repo embeddings pipelines degrade worst.

## Cautions

- **Zero independent discussion and roughly 450 open issues against 5.2k stars means the only quality evidence is the project's own demos and CI.**
- The install pitch now says no database server, because the graph defaults to an embedded SQLite file; picking the Memgraph or Neo4j backend brings a separate dependency with its own licensing and operational cost back.
- The 0.2 line landed ten point releases in its first three days, after 27 releases on the 0.1 line, ran to 0.2.24 before a 0.3 line opened on 2026-10-24, and jumped to 0.4.5 on 2026-10-30, which means churn, and the Cypher-generation quality depends on the model you attach, which no benchmark here measures.
- Indexing is per-repo work (`cgr start --update-graph`), so freshness after agent edits needs the incremental update path to actually hold.

## Pricing

Free and open source under MIT, with enterprise support and services quoted by the developer.
Your costs are the Memgraph deployment and your own LLM bills for query answering, so no prices belong in this note and no price history table applies.

## Compared to

- [open-codebase-index](../open-codebase-index/index.md): the embeddings-plus-BM25 sibling over MCP, host-neutral and lighter; choose it for concept lookup, Code-Graph-RAG for structural and blast-radius questions.
- Aider's graph-ranked repo map ([Aider](../../harnesses/aider/index.md)): the no-store middle ground, ranking tree-sitter symbols by references without a database; choose it when even an embedded graph store is more than you want to run.
- [Tree-sitter code chunking](../tree-sitter-chunking/index.md): the parsing layer alone, feeding a vector store; Code-Graph-RAG keeps the parse and swaps the vector store for a queryable graph.

## Bottom line

**Recommended for monorepo teams whose retrieval questions are structural, who will operate Memgraph, and who will validate answer quality on their own repo before trusting it.**
Not for concept-level search, not as a dependency-free tool, and not for anyone needing independent evidence first, because none exists.
My disagreeable claim: this is the version of code retrieval the embeddings era skipped, and its near-zero discussion footprint says more about how few teams measure retrieval structurally than about the tool.

## Changes

- 2026-10-07 - Created in the daily refresh's retrieval entrant scan from the awesome-rag-production source.
- 2026-10-13 - Refreshed the volatile numbers (5,252 stars, pushed 2026-10-14) and recorded the open-issue count falling from 739 to 591 in two days, with the Cautions line aligned.
- 2026-10-16 - Recorded the PyPI train moving to 0.2.0 (2026-10-15, 29 releases total, the first release past the 0.1 line) and refreshed the repository activity (pushed 2026-10-15, 589 open issues).
- 2026-10-19 - Recorded the PyPI train reaching 0.2.10 (2026-10-18, 30 releases total, ten point releases in three days) and refreshed the repository activity (pushed 2026-10-19, 589 open issues).
- 2026-10-22 - Refreshed the repository activity (pushed 2026-10-22) and recorded the open-issue count falling from 590 to 543, with the Cautions line aligned; PyPI 0.2.10 remains latest.
- 2026-10-24 - Recorded the PyPI train reaching 0.3.2 (2026-10-24, 34 releases total; the 0.2 line ran to 0.2.24 by 2026-10-23 before the 0.3 line opened) and refreshed the repository activity (pushed 2026-10-24, 538 open issues), with the Cautions churn line extended.
- 2026-10-25 - Refreshed the repository activity (pushed 2026-10-25, 526 open issues); PyPI 0.3.2 remains latest.
- 2026-10-26 - Fixed the star-history chart markup (the light source carried theme=dark), refreshed the repository activity (pushed 2026-10-26, 547 open issues), and recorded the PyPI train reaching 0.3.13 (2026-10-25, 35 releases total).
- 2026-10-27 - Refreshed the repository activity (pushed 2026-10-27, 543 open issues); PyPI 0.3.13 remains latest.
- 2026-10-31 - Refreshed the repository activity (pushed 2026-10-31, 516 open issues); PyPI 0.3.13 remains latest.
- 2026-11-01 - Recorded the PyPI train reaching 0.4.5 (2026-10-30, 36 releases; the 0.4 line's headline change gates a repository's `.cgr.md` out of the agent's system prompt until approved) and refreshed the repository activity (pushed 2026-11-01, 541 open issues).
- 2026-11-03 - Recorded the PyPI train reaching 0.5.0 (2026-11-03, 38 releases; the NEWS headlines are JavaScript signature reading and writing for change signatures plus the Rust toolchain bump) and refreshed the repository activity (pushed 2026-11-03, 522 open issues).
- 2026-11-06 - Refreshed the repository activity (pushed 2026-11-05, 521 open issues); PyPI 0.5.0 remains latest across 38 releases.
- 2026-11-07 - Refreshed the repository activity (pushed 2026-11-07 with the main branch's version bump to 0.5.7, 520 open issues), re-fetched PyPI (0.5.0 still latest across 38 releases, the 0.4 line corrected to its true endpoint 0.4.19 of 2026-11-02), and aligned the Status PyPI sentence, whose lead still read 0.4.5 across 36 releases.
- 2026-11-08 - Refreshed the repository activity (pushed 2026-11-08 with the main branch's version bump to 0.5.14, 509 open issues); PyPI 0.5.0 remains latest across 38 releases.
- 2026-11-12 - Recorded the PyPI train jumping to 0.6.30 (2026-11-09, 40 releases; the 0.5 line never published past 0.5.0 and the 0.6 line went 0.6.0 on 2026-11-08 then straight to 0.6.30, with the main branch's version bumps running ahead at 0.6.39 by 2026-11-12) and refreshed the repository activity (pushed 2026-11-12, 456 open issues).
- 2026-11-15 - Rotation re-verification re-fetched every cited URL live (repository API, README, NEWS.md, PyPI, and the footprint scan all fetched) and corrected the storage description the README had moved: the graph defaults to an embedded SQLite file with no server and no Docker, Memgraph and Neo4j becoming opt-in backends, with the definition, What-it-is, Cautions, and Compared-to lines aligned; recorded Julia joining the fully-supported list with eight structural-support languages named on the ast-grep tier, recorded the README's release-cadence note (PyPI carries every 50th version plus security fixes, breaking changes, and release-now merges, so main tags run ahead by tens of patch versions), recorded the 0.6-line NEWS block growing four entries past the 0.6.30 headlines with PyPI 0.6.30 still latest across 40 releases, and refreshed the repository activity (pushed 2026-11-14 with the main branch's version bump to 0.6.45, 445 open issues).
- 2026-11-16 - Recorded the PyPI train publishing 0.6.62 (2026-11-15, 41 releases; the 32-version jump rendered the four grown NEWS entries together with five new headlines, catching the installable release up to the main branch's bump train on release day) and refreshed the repository activity (pushed 2026-11-16 at the repository level with the default branch's latest commit the 0.6.62 bump, 440 open issues).
- 2026-11-17 - Refreshed the repository activity (pushed 2026-11-17 with the main branch's version bump train running on to 0.6.81, 424 open issues); PyPI 0.6.62 remains latest across 41 releases.
- 2026-11-19 - Recorded the PyPI train opening the 0.7 line at 0.7.1 (2026-11-17, 42 releases total, no 0.7.0 published) and refreshed the repository activity (pushed 2026-11-19 with the default branch's latest commit a prompt-audit PR merge, 370 open issues).
- 2026-11-21 - Refreshed the repository activity (pushed 2026-11-21 with the default branch's latest commit a C++ lambda-creation-reference PR merge, 304 open issues); PyPI 0.7.1 remains latest across 42 releases.
- 2026-11-22 - Recorded the PyPI train jumping to 0.7.79 (2026-11-21, 43 releases; the 0.7 line's first catch-up publish after 0.7.1, rendering the grown NEWS entries together with the refined-code-analysis and public-surface-enforcement headlines) and refreshed the repository activity (pushed 2026-11-22 with the default branch's latest commit a reexport-caller-check PR merge, 306 open issues).

## See also

- [open-codebase-index](../open-codebase-index/index.md) - the self-hosted embeddings-based code index it contrasts with
- [Tree-sitter code chunking](../tree-sitter-chunking/index.md) - the parser layer it builds on without the vector store
- [Aider](../../harnesses/aider/index.md) - the graph-ranked repo map, the no-database variant of the same idea
- [Semantic code search in coding tools](../semantic-code-search/index.md) - the shipped-tool pattern it replaces for structural questions

## References

- https://api.github.com/repos/vitali87/code-graph-rag - 5,252 stars (as of 2026-10-14), 702 forks, MIT, created 2025-06-16, pushed 2026-11-22, 306 open issues (GitHub API, as of 2026-11-22)
- https://raw.githubusercontent.com/vitali87/code-graph-rag/main/README.md - the two-component architecture, compiler frontends, runtime tracing, language support, the embedded SQLite default with Memgraph and Neo4j opt-in, the release-cadence table, and the enterprise services section (re-fetched 2026-11-15)
- https://raw.githubusercontent.com/vitali87/code-graph-rag/main/NEWS.md - the feature-news ledger behind the active-maintenance claim; the four grown entries rendered into the 0.6.62 publish together with five new headlines (CommonJS renamed-property import resolution, class-field-type-retaining incremental syncs, receiver-scoped Python property reads, rejected cross-language internal import targets, and constructor attribute-field initializer handling), re-fetched 2026-11-16; the entries grown past the 0.7.1 headlines rendered into the 0.7.79 publish together with the refined-code-analysis and surface-definition headlines, re-fetched 2026-11-22
- https://pypi.org/pypi/code-graph-rag/json - version 0.7.79 (2026-11-21), 43 releases (fetched 2026-11-22, latest; the 0.7 line opened 2026-11-17 at 0.7.1 with no 0.7.0 published, the 0.6 line ended at 0.6.62 (2026-11-15) with no 0.7.0 published, and the 0.5 line never published past 0.5.0 of 2026-11-03)
- https://hn.algolia.com/api/v1/search?query=Code-Graph-RAG%20knowledge%20graph&tags=story - the footprint scan: the cited Show HNs at 1 point each (re-fetched 2026-11-15, the query still returns the March 2026 Code-Graph-RAG Show HN at 1 point)
