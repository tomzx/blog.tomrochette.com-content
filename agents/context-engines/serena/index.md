---
title: Serena
created: 2026-10-04
updated: 2026-10-04
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, code-search, lsp, mcp, open-source]
readability: 3
audience_notes: >
  Engineers wiring coding agents to large codebases who are deciding between an
  LSP-backed symbol toolkit and embedding or graph indexes.
  Assumes you know what the language server protocol and MCP are.
---

Serena is an open-source MCP toolkit that gives coding agents IDE-grade semantic abilities, symbol-level retrieval, referencing, and editing, on top of language servers, plus a paid JetBrains backend, built by Oraios Software in Munich.

**Serena is the largest bet that agents want the IDE's forty-year-old answer to code search (language servers) rather than a new embedding index, and at about 30k stars it is the biggest tool in the context-engine category the section had not yet profiled.**

## What it is

A Python application (`uv tool install serena-agent`) that runs as an MCP server (stdio or HTTP) and exposes symbol-level tools: `find_symbol`, symbol overview, `find_referencing_symbols`, rename, and symbolic edits (replace body, insert before or after) that are token-cheap because they target definitions instead of line ranges.
The default backend is language servers implementing the LSP, free and covering more than 40 languages; a paid Serena JetBrains plugin backend swaps in the IDE's deeper analysis (type hierarchy, move and inline refactorings, interactive debugging).
It carries a per-project memory system (markdown memories the agent writes and reads across sessions), YAML configuration at global, project, and per-client levels, and it deliberately disables its basic file and shell tools inside harnesses like Claude Code that already ship them.
Distributed as `serena-agent` on PyPI; the application is GPL-3.0-or-later and the SolidLSP component MIT, with a contributor license agreement required.

## Status

**Active and very large.**
About 30.0k stars and 2,041 forks as of 2026-10-04, created 2025-03-23, pushed 2026-09-30, latest release v1.7.0 on 2026-08-09 (GitHub API), with the PyPI package at 1.7.0 across 15 releases and 148,555 downloads in the trailing month (as of 2026-10-04).
The JetBrains plugin shows about 19.5k installs on the JetBrains marketplace.
There was no big launch moment: the tool accumulated stars through practitioner word of mouth, and its Hacker News presence is comment-level, not story-level, with users naming it the indexing layer in OpenCode and Cursor-exit setups.

## Strengths

- **Symbol tools return exactly what an edit needs**: a referenced definition, a rename across files, a body replacement, without the agent reading whole files or splitting on line counts.
- Freshness is architectural: language servers parse the working tree live, so there is no index to go stale mid-edit, the exact failure mode that demoted embeddings indexes.
- Zero marginal cost on the default path: free LSP backends, no API keys, everything local.
- The per-project memory system is a quiet bonus: markdown memories scoped per repository, composable with AGENTS.md conventions instead of replacing them.

## Cautions

- **The flagship evidence is the vendor's own prompt**: the README's "what our end users say" section is a self-run evaluation where the company asks agents to rate Serena's tools, which is testimonial, not benchmark.
- No independent performance evaluation exists as of 2026-10-04; I found praise in practitioner threads but no third-party measurement of token savings or task success.
- The application is GPL-3.0-or-later and contributions require a CLA, which some commercial embedders will treat as a stop sign.
- LSP setup is per-language machinery: some languages need extra servers, and the JetBrains backend's deeper features (debugging, move refactoring) sit behind a paid plugin whose price the marketplace does not publish.
- The README itself warns that marketplace installs are outdated, an unusual distribution-hygiene smell for a tool this popular.

## Pricing

The core is free and open source (GPL-3.0-or-later application, MIT SolidLSP) with the free LSP backend.
The Serena JetBrains plugin is paid with a 7-day free trial; the JetBrains marketplace API exposes the product and trial but no public per-seat price, so I could not verify a number and record none.

## Compared to

- [Sourcegraph code context platform](../sourcegraph-code-context/index.md): both sell precise symbol intelligence to agents; Sourcegraph indexes across a whole organization at $16K a year, Serena runs free against one local workspace with no index.
- [Semble](../semble/index.md): static-embedding plus BM25 search that answers where-is-code-like-X; Serena answers what-references-this-symbol and edits it, and the two compose (Semble to find the area, Serena to work on it).
- [Graft](../graft/index.md): prebuilt readable maps of a codebase; Serena gives the agent the tools to build its own understanding on demand, which costs more tokens per session but never goes stale.

## Bottom line

**Recommended for anyone running agents on large polyglot codebases who wants IDE-grade navigation and editing for free, locally, with no index to maintain.**
Not for teams that need a permissive license to embed the engine in a product, and not as a replacement for the harness's own grep on small repos where symbol tools are ceremony.
My disagreeable claim: Serena's growth proves the embedding-index era of code context was a detour, because the oldest tool in software (the compiler-adjacent language server) beats it on every axis agents care about except vague concept queries.

## Changes

- 2026-10-04 - Created from the 2026-10-04 entrant scan, the largest uncovered tool in the category at about 30k stars, with seven fetched sources.

## See also

- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins
- [Semble](../semble/index.md) - the embedding-based neighbor that answers different queries
- [Sourcegraph code context platform](../sourcegraph-code-context/index.md) - the enterprise version of the symbol-precision bet
- [Tree-sitter code chunking](../../retrieval/tree-sitter-chunking/index.md) - the cheaper syntax-aware alternative without LSP machinery
- [MCP](../../protocols/mcp/index.md) - the protocol this toolkit rides into every harness

## References

- https://github.com/oraios/serena - repository, 30.0k stars and activity as of 2026-10-04, architecture, backend choice, installer warning
- https://raw.githubusercontent.com/oraios/serena/main/README.md - tool tables, language support count, memory system, the self-run agent evaluation, licensing overview
- https://raw.githubusercontent.com/oraios/serena/main/LICENSE - the per-component licensing: SolidLSP MIT, application GPL-3.0-or-later, distributions GPL as a whole
- https://oraios.github.io/serena/ - official documentation hub (tools, clients, configuration, evaluation pages)
- https://plugins.jetbrains.com/api/plugins/28946 - the JetBrains plugin: Oraios Software (Munich), about 19.5k installs, 7-day trial, no published price, fetched 2026-10-04
- https://pypi.org/pypi/serena-agent/json - the distribution, version 1.7.0, 15 releases
- https://pypistats.org/api/packages/serena-agent/recent - 148,555 downloads in the trailing month as of 2026-10-04
- https://hn.algolia.com/api/v1/search?query=serena+mcp&tags=comment - the comment-level HN footprint: OpenCode indexing setups and the symbolic-search recommendation
