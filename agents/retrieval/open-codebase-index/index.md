---
title: open-codebase-index
created: 2026-10-05
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, retrieval, code-retrieval, rag, embeddings, mcp]
readability: 3
audience_notes: >
  Engineers who want agent-grade semantic code search they host themselves, wired into an existing harness through MCP or a plugin.
  Assumes familiarity with embeddings, BM25, and MCP.
---

open-codebase-index is an MIT-licensed local semantic code index (TypeScript plus a Rust native module) that serves embeddings, BM25 keyword search, symbol lookup, and call-graph tools to OpenCode, Claude Code, Codex, Pi, Jcode, and any MCP client, with branch-aware incremental indexing stored in SQLite.

**It is the self-hosted counterexample to the shipped-tool retreat from semantic search: while Cursor's docs stopped documenting an embeddings index and Continue deprecated its index provider, this tool keeps the index on your machine and hands the agent about twenty retrieval tools over MCP.**

## What it is

Install is `npm install open-codebase-index` (or `-g` for the `ocbi` CLI), then a plugin entry for OpenCode or an MCP registration for Codex, Claude Code, Jcode, Cursor, Windsurf, and other clients; a Pi extension and a bundled `codebase-search` skill cover Pi and omp.
The pipeline is git-aware file discovery, tree-sitter parsing and chunking (TypeScript, Python, Rust, Go, Java, C#, Ruby, and more, with text fallback), embedding generation with content-hash reuse (Ollama, OpenAI, Google, or any OpenAI-compatible endpoint), and a SQLite plus usearch plus BM25 store.
The tool surface is 16 portable tools (`codebase_context`, `codebase_search`, `implementation_lookup`, `call_graph`, `call_graph_path`, `pr_impact`, and neighbors) plus 3 knowledge-base tools, hosted at 19 or 20 tools depending on the client, with 5 MCP prompts.
The docs carry a host-surface matrix spelling out which client gets which tools, the kind of integration documentation most tools in this slot never write.

## Status

**Active and shipping constantly, with almost no community footprint.**
215 stars and 34 forks since 2026-01-13, 1,023 commits, pushed 2026-10-06 (GitHub API, as of 2026-10-06).
npm shows 27 versions since 2026-07-30, latest 0.35.2 published 2026-10-05, and 6,674 downloads in the month of 2026-09-05 to 2026-10-04, so installs run well ahead of stars.
A search for its name on Hacker News returned zero hits as of 2026-10-05, so like graft and Knowhere in this section, adoption is quiet and distribution runs from README to install, not from launches.

## Strengths

- **The evidence-pack design (bounded `codebase_context` and `codebase_peek` before full-source `codebase_search`) matches how harnesses spend context, which grep-only loops pay for on every broad question.**
- Genuinely host-neutral: one MCP core across Codex, Claude Code, Cursor, Windsurf, and OpenCode, instead of one fork per harness.
- The call-graph tools (`call_graph`, `call_graph_path`, `pr_impact`) go past retrieval into blast-radius questions no embeddings index answers.
- Branch-aware incremental indexing with content-hash reuse keeps the index current where agents edit, the freshness failure mode that demoted tool-built indexes.

## Cautions

- **Zero independent discussion (no HN thread, no third-party benchmark found as of 2026-10-05) means the only quality evidence is the repo's own `benchmarks/` directory.**
- 0.35.x with releases inside a single day is churn, and the package has already renamed once (`opencode-codebase-index` remains a supported alias), splitting the install base its download counts measure.
- The embedding choice is yours and it matters: local Ollama means GPU or patient CPU time, cloud providers mean your code leaves the machine, which undercuts the local-index pitch.
- The workspace note's thesis cuts here too: an always-current grep loop needs no index at all, so the tool has to earn its keep on concept queries and graph questions specifically.

## Pricing

Free and open source under MIT.
The only costs are your embedding bill (cloud API tokens or local compute) and the disk for the SQLite index.

## Compared to

- Shipped tool indexes (the [semantic code search](../semantic-code-search/index.md) pattern): zero setup, but Cursor's docs no longer document stored embeddings and Continue deprecated its provider, so that capability is retreating from tools.
- Graph-ranked repo maps (aider): deterministic and always current, no embeddings, but no concept-level matching.
- [Tree-sitter code chunking](../tree-sitter-chunking/index.md): the parsing layer this tool builds on; used directly, it is the DIY version of the same parser.

## Bottom line

**Recommended for OpenCode, Pi, or MCP-client users who want semantic search without trusting a vendor index, and who will pin a version and read the tools matrix first.**
Not for anyone needing proven retrieval quality, because nothing independent validates it yet.
My disagreeable claim: a 6,000-installs-a-month npm package with zero discussion is a better adoption signal than a trending repository, because installs mean someone wired it into their agent and kept it.

## Changes

- 2026-10-05 - Created in the daily refresh's retrieval entrant scan.

## See also

- [Semantic code search in coding tools](../semantic-code-search/index.md) - the shipped-capability pattern this tool lets you self-host
- [Tree-sitter code chunking](../tree-sitter-chunking/index.md) - the parsing layer it builds on
- [Aider](../../harnesses/aider/index.md) - the graph-ranked, no-embeddings counterexample
- [OpenCode](../../harnesses/opencode/index.md) - the harness with the deepest documented plugin integration here

## References

- https://github.com/Helweg/open-codebase-index - repository: 215 stars, 34 forks, MIT, created 2026-01-13, pushed 2026-10-06, 1,023 commits (GitHub API, as of 2026-10-06)
- https://raw.githubusercontent.com/Helweg/open-codebase-index/main/README.md - hosts, highlights, pipeline, embedding providers, legacy package aliases (fetched 2026-10-05)
- https://raw.githubusercontent.com/Helweg/open-codebase-index/main/docs/tools.md - the host surface matrix: 16 portable tools, 3 knowledge-base tools, 5 MCP prompts (fetched 2026-10-05)
- https://registry.npmjs.org/open-codebase-index - latest 0.35.2 published 2026-10-05, 27 versions since 2026-07-30, MIT (re-verified unchanged 2026-10-06)
- https://api.npmjs.org/downloads/point/last-month/open-codebase-index - 6,674 downloads, window 2026-09-05 to 2026-10-04 (fetched 2026-10-06)
- https://hn.algolia.com/api/v1/search?query=%22open-codebase-index%22&tags=story - the zero-hit footprint scan (fetched 2026-10-05)
