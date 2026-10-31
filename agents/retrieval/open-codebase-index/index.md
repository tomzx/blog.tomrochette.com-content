---
title: open-codebase-index
created: 2026-10-05
updated: 2026-10-31
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
221 stars and 38 forks as of 2026-10-13, pushed 2026-10-30 (GitHub API, as of 2026-10-31).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Helweg/open-codebase-index&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Helweg/open-codebase-index&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Helweg/open-codebase-index&type=date&legend=top-left" />
</picture>

npm shows 38 versions since 2026-07-30, latest 0.38.2 published 2026-10-26, and 5,569 downloads in the trailing month to 2026-10-30 (nine zero days inside the window, so the level reads approximate), against 5,365 to 2026-10-27, 5,662 to 2026-10-22, 6,785 to 2026-10-18, and 7,613 to 2026-10-12, so the three-month decline pauses roughly flat in this note's tracking.
A search for its name on Hacker News returned zero hits as of 2026-10-11, so like graft and Knowhere in this section, adoption is quiet and distribution runs from README to install, not from launches.

## Strengths

- **The evidence-pack design (bounded `codebase_context` and `codebase_peek` before full-source `codebase_search`) matches how harnesses spend context, which grep-only loops pay for on every broad question.**
- Genuinely host-neutral: one MCP core across Codex, Claude Code, Cursor, Windsurf, and OpenCode, instead of one fork per harness.
- The call-graph tools (`call_graph`, `call_graph_path`, `pr_impact`) go past retrieval into blast-radius questions no embeddings index answers.
- Branch-aware incremental indexing with content-hash reuse keeps the index current where agents edit, the freshness failure mode that demoted tool-built indexes.

## Cautions

- **Zero independent discussion (no HN thread, no third-party benchmark found as of 2026-10-05) means the only quality evidence is the repo's own `benchmarks/` directory.**
- Releases landing inside single days (0.36.x, 0.37.x, now 0.38.x) are churn, and the package has already renamed once (`opencode-codebase-index` remains a supported alias), splitting the install base its download counts measure.
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
My disagreeable claim: a 5,600-installs-a-month npm package with zero discussion is a better adoption signal than a trending repository, because installs mean someone wired it into their agent and kept it.

## Changes

- 2026-10-05 - Created in the daily refresh's retrieval entrant scan.
- 2026-10-07 - Added the Helweg/open-codebase-index star history chart to the Status section.
- 2026-10-07 - Recorded npm release 0.35.3 (published 2026-10-06, 28 versions total) and refreshed the repository numbers to 216 stars as of 2026-10-07; downloads and the zero-HN-footprint claim unchanged.
- 2026-10-08 - Recorded the npm train moving to 0.36.0 (2026-10-07) and 0.36.1 (2026-10-08), 30 versions total, and refreshed the repository numbers to 217 stars pushed 2026-10-08; downloads and the zero-HN-footprint claim unchanged.
- 2026-10-09 - Recorded the npm train moving to 0.36.2 (2026-10-08) and 0.36.3 (2026-10-09), 32 versions total, refreshed downloads to 6,807 for the month of 2026-09-08 to 2026-10-07, and the repository numbers to 216 stars pushed 2026-10-09; the zero-HN-footprint claim unchanged.
- 2026-10-13 - Refreshed the repository numbers (221 stars, pushed 2026-10-13), the npm figures (7,613 downloads for the month to 2026-10-12, the train paused at 0.36.3), and corrected the version count to 32 against the registry, where the Status line had drifted to 33.
- 2026-10-20 - Recorded the npm train resuming at 0.37.0 (2026-10-19, 33 versions total, the first release after the ten-day 0.36.3 pause) and refreshed the repository activity (pushed 2026-10-20) and monthly downloads (6,785, window to 2026-10-18).
- 2026-10-22 - Recorded the npm train at 0.37.1 (2026-10-20) and 0.37.2 (2026-10-21, 35 versions total) and refreshed the repository activity (pushed 2026-10-22); monthly downloads unchanged.
- 2026-10-24 - Recorded the npm train moving to 0.38.0 (2026-10-23, 36 versions total), refreshed the repository activity (pushed 2026-10-23), and recorded the trailing-month download trend falling again (7,613 to 2026-10-12, 6,785 to 2026-10-18, now 5,662 to 2026-10-22), with the Cautions churn line and the Bottom-line install figure aligned.
- 2026-10-26 - Recorded the npm train reaching 0.38.1 (2026-10-25, 37 versions total) and refreshed the repository activity (pushed 2026-10-26); trailing-month downloads unchanged.
- 2026-10-27 - Recorded the npm train reaching 0.38.2 (2026-10-26, 38 versions total) and the trailing-month install trend falling again (5,662 to 2026-10-22, now 5,365 to 2026-10-27, ten zero days inside the window), a third consecutive decline, with the Bottom-line install figure aligned; the repository push date is unchanged at 2026-10-26.
- 2026-10-31 - Refreshed the repository activity (pushed 2026-10-30) and re-read the trailing-month installs at 5,569 to 2026-10-30 (nine zero days), roughly flat against the prior 5,365 reading, pausing the three-decline string; PyPI/npm latest remains 0.38.2.

## See also

- [Semantic code search in coding tools](../semantic-code-search/index.md) - the shipped-capability pattern this tool lets you self-host
- [Tree-sitter code chunking](../tree-sitter-chunking/index.md) - the parsing layer it builds on
- [Aider](../../harnesses/aider/index.md) - the graph-ranked, no-embeddings counterexample
- [OpenCode](../../harnesses/opencode/index.md) - the harness with the deepest documented plugin integration here

## References

- https://github.com/Helweg/open-codebase-index - repository: 221 stars (as of 2026-10-13), 38 forks, MIT, created 2026-01-13, pushed 2026-10-30 (GitHub API, as of 2026-10-31)
- https://raw.githubusercontent.com/Helweg/open-codebase-index/main/README.md - hosts, highlights, pipeline, embedding providers, legacy package aliases (fetched 2026-10-05, re-verified unchanged 2026-10-11)
- https://raw.githubusercontent.com/Helweg/open-codebase-index/main/docs/tools.md - the host surface matrix: 16 portable tools, 3 knowledge-base tools, 5 MCP prompts (fetched 2026-10-05)
- https://registry.npmjs.org/open-codebase-index - latest 0.38.2 published 2026-10-26, 38 versions since 2026-07-30 (fetched 2026-10-31)
- https://api.npmjs.org/downloads/range/2026-10-01:2026-10-30/open-codebase-index - 5,569 downloads across the window, nine zero days inside it (fetched 2026-10-31; npm's point endpoints can serve stale windows, so the figure comes from the explicit range call)
- https://hn.algolia.com/api/v1/search?query=%22open-codebase-index%22&tags=story - the zero-hit footprint scan (fetched 2026-10-05, re-verified zero hits 2026-10-11)
