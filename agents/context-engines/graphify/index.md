---
title: Graphify
created: 2026-08-30
updated: 2026-11-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, context-engines, knowledge-graphs, code-intelligence, open-source]
readability: 3
audience_notes: >
  Engineers deciding how their coding agent should learn a large codebase, who are weighing graph indexing against packing or embeddings.
  Assumes you know what an AST, a vector store, and an MCP server are.
---

Graphify is an open-source Python CLI that turns a codebase, plus its docs, SQL schemas, and PDFs, into a queryable knowledge graph exposed as a `/graphify` skill and MCP server for coding assistants, built on local deterministic tree-sitter parsing with no vector store.

**Graphify's bet is that structure beats similarity: an agent that can traverse exact calls-and-imports edges with file:line citations needs less context than one searching embeddings, and the code path runs entirely on your machine.**
The bet is young, self-benchmarked, and wrapped in a YC company's funnel.

## What it is

One command builds `graphify-out/`: an interactive `graph.html`, a `GRAPH_REPORT.md` with god nodes and communities, and `graph.json` with the full graph, which you then query through `graphify query`, `path`, and `explain` instead of grepping.
Code is parsed with tree-sitter across 36 code languages (the project site's count as of 2026-09-18), resolving calls, imports, and inheritance edges deterministically with no LLM; docs, PDFs, and images go through a semantic pass using your assistant's model or a configured API key.
Every edge is tagged EXTRACTED, INFERRED, or AMBIGUOUS, so readable facts are distinguishable from guessed ones, and queries return subgraphs with file:line citations.
A skill installer targets the 17 coding assistants the vendor documents (Claude Code, Cursor, Codex, Gemini CLI, OpenCode, and 12 more), plus an MCP server and exports to Neo4j and Obsidian.
Made by Graphify Labs, a YC Summer 2026 company of two people in London, Apache-2.0, with the PyPI package named `graphifyy`.

## Status

Growing absurdly fast for its age: 126,981 stars as of 2026-10-16, latest release v0.9.119 on 2026-11-24, 3,223 commits in under eight months since 2026-04-03 (as of 2026-11-25), and 14,721 forks and 1,742 open issues and pull requests as of 2026-11-25 (432 contributors as of 2026-11-24).
Releases v0.9.110 and v0.9.111 (both 2026-11-15) fixed Python aliased-import call linking (`from mod import foo as bar; bar()` now links from method bodies and decorated definitions) and shipped a maintenance-and-security release raising the minimum Python to 3.11, pulling in patched optional and transitive dependencies after 3.10's October 2026 end of life.
Release v0.9.112 (2026-11-17) shipped the Delphi/Pascal cluster (a form linked to the unit that implements it, calls resolved through global object variables, base classes resolved to their declarations, and units the grammar cannot parse recovered end to end) alongside Java overloaded methods keyed by arity and erased signature, Go bare-receiver resolution to its own package's type, Rust `crate::` imports resolving inside their own crate, C directory-qualified angle includes, a dedup fix keeping prefix-derived words apart from their base words, and an install fix where `graphify claude install` writes its section to the file Claude Code actually reads (an existing CLAUDE.md wins over AGENTS.md), with uninstall symmetric.
Release v0.9.113 (2026-11-19) raised the packaging floor again: the minimum Python is now 3.11.5 with soupsieve pinned to 4.1.1, clearing the ReDoS advisories reachable through beautifulsoup4 in the optional `svg`/`all`/`pdf` extras (installs on Python 3.11.0 to 3.11.4 keep resolving to 0.9.112), and it kept underscore/case member twins apart in node ids across Ruby, Lua, Scala, and Elixir while a Rust fix reads a prelude trait's generic argument as a reference instead of a wrong `implements`/`inherits` edge.
Releases v0.9.114 and v0.9.115 (2026-11-20 and 11-21) followed: v0.9.114 is a performance release across the extract, build, update, watch, cluster, and analyze paths (byte-identical output on the perf entries) with a batch of extractor and build fixes (Java Lombok getters synthesized, Kotlin typed-receiver member calls bound across files and through interfaces, PL/pgSQL ERROR-recovery routine bodies gaining their reads_from edges, EXTRACTED edges kept over tied semantic copies, T-SQL misread procedure headers yielding single nodes, VB.NET methods after multi-line string literals reparsed with a placeholder, C++ `std::`-qualified types kept off project symbols, Python `sys.path` script-dir imports bound, cross-repo `calls` edges kept through the serve relation filter), and v0.9.115 fixes the GHSA-g6c9-j4vm-mwq4 forced-SMB-authentication issue on Windows (a `.sh` source line or a `.git` UNC gitdir pointer could coerce outbound SMB auth leaking a NetNTLMv2 response; probes now bounded to the scan root with UNC paths refused before resolution) alongside resolution and watch fixes, the two releases sharing the AST cache schema bumps to 50 and 51 so warm caches re-extract the affected languages.
Releases v0.9.116 through v0.9.118 were consolidated into one GitHub release: v0.9.118 (2026-11-23) carries the changelogs written for 0.9.116 and 0.9.117 alongside its own, fourteen community pull requests of extractor, resolution, serve, export, clustering, and reporting fixes (Objective-C methods whose names collide inside one interface getting their own salted node ids, C struct function-pointer calls no longer fabricating a `calls` edge to a same-named free function, C# contextual keywords rewritten to their verbatim `@name` form before parsing, Go struct fields bound to their own package, Svelte `export *` barrel imports resolving to the defining module, the `get_section` retry getting its own graph caches instead of raising `KeyError` on stale ids, the MCP server loading `graph.json` off the event loop so a reload stops blocking concurrent requests, a deleted clustered `GRAPH_REPORT.md` regenerated, image nodes demoted in query seed scoring, export filenames honoring the filesystem's `NAME_MAX`, directed wiki exports including incoming edges, `.graphifyrc` parsing `demote_docs` and `query_demote_docs`, and community-overlap counting made linear), with the AST cache schema raised from 51 to 53 so the first build after upgrading re-extracts Objective-C, C, and C#; main's 2026-11-23 commit after the release is a test-suite speedup (tmpfs plus xdist), not a code change.
Release v0.9.119 (2026-11-24) fixed a core-install regression in 0.9.118, where the serve graph commands (`query`, `path`, `explain`, `affected`, and `benchmark`) raised ModuleNotFoundError on a core install without the `[mcp]` extra because 0.9.118 imported `anyio` at the top of `graphify/serve.py`, and shipped ten community pull requests of resolution, extractor, export, and performance fixes (lambda-parameter and function-parameter shadows in Python no longer bound to module-level definitions, Go locals that shadow an imported package and same-named sibling packages resolved, a COBOL `GO TO` emitting a `calls` edge to its paragraph, wiki cross-references linked by node id, the undirected `affected` traversal walking incident edges, query terms absent from the corpus skipped, and file-label disambiguation made near-linear), with the AST cache schema raised from 53 to 55 so Python, Go, and COBOL re-extract after upgrading; main's only commit after it is a CI change.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Graphify-Labs/graphify&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Graphify-Labs/graphify&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Graphify-Labs/graphify&type=date&legend=top-left" />
</picture>

The YC page claims 5M+ downloads and named production users, all self-reported.
**The Enterprise early-access tier now ships differential formal verification**: a solver ladder (Z3, CrossHair, CBMC, JBMC) that proves a changed function behavior-preserving or returns a concrete input that breaks it, alongside graph-aware PR review, per the vendor's full index (fetched 2026-09-26).
The ecosystem is growing too: a third-party C# port, graphify-csharp, launched September 11, 2026 with a 46-point Show HN and 21 comments as of 2026-09-16, the largest discussion any Graphify-linked project has drawn.
**The star count still outruns the discussion footprint: Hacker News stories linking the main repo drew two or three points with no comments, a mismatch I treat as a flag, not a slam dunk.**

## Strengths

- The code-only path is fully local and key-free, so the default workflow leaks nothing.
- Edge-level provenance (EXTRACTED versus INFERRED with file:line) is a real answer to the trust problem in generated context.
- One graph covers code and its non-code artifacts, and the skill installs across most harnesses your team already runs.
- Shipping velocity is exceptional, with releases landing near-daily (v0.9.68, a watcher shell-quoting security fix, on 2026-09-25) and a published benchmark methodology.

## Cautions

- The benchmarks are self-published, and on the headline QA-accuracy metric graphify trails supermemory while winning on cost and recall, per its own BENCHMARKS.md.
- Only code is local: docs, PDFs, and images are sent to whatever LLM backend is configured.
- Pre-1.0 with 1,639 open issues and PRs as of 2026-11-13, a nonstandard default branch, and acknowledged PyPI name-squatting on `graphify*` packages.
- The free CLI is the top of an open-core funnel into a hosted product whose plans only recently gained public prices, so expect the monetization strategy to keep moving.

## Pricing

The core CLI is free, Apache-2.0, no account.
The hosted side publishes four plans (page updated 2026-11-23, fetched 2026-11-24): Free ($0, one developer, no card, with node, build, and review allowances), Pro ($10/month billed yearly, $12/month billed quarterly at $36 a quarter, or $15 billed monthly, one developer, uncapped graphs), Teams ($20 per seat/month billed yearly, $24 billed quarterly, or $29 billed monthly, minimum 2 seats, rising to $28, $32, and $40 after the first 100 teams), and Enterprise (custom, self-hosted on your infrastructure, with the price scoped on a call instead of published), each paid plan carrying a two-week card-required trial, plus free access for qualified MIT and Apache licensed OSS projects; the early-access label now sits on the Jira, Confluence, Sentry AI SRE, Google Drive, and Vercel connectors rolling out to paid workspaces.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-18 | Hosted plans | First published ladder: Free $0 (one developer), Pro $10/mo billed yearly or $15 monthly, Teams $20/seat/mo yearly or $29 monthly (min 2 seats), Enterprise scoped on a call; core CLI free (Apache-2.0). | [graphify.com/pricing](https://graphify.com/pricing) |
| 2026-11-23 | Pro, Teams | Quarterly billing added between monthly and annual: Pro $36/quarter ($12/month), Teams $72/developer/quarter ($24/developer/month) for the first 100 teams, then $96/quarter ($32/month); monthly and annual prices unchanged. Observed 2026-11-24 on the page marked updated 2026-11-23. | [graphify.com/pricing](https://graphify.com/pricing) |

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
- 2026-09-22 - Recorded release v0.9.66 (2026-09-22) and refreshed the volatile numbers (120,654 stars, 1,888 commits, 273 contributors, 1,445 open issues and PRs); hosted plans unchanged.
- 2026-09-25 - Recorded release v0.9.67 (2026-09-23), refreshed the volatile numbers (121,216 stars, 1,908 commits, 260 contributors, 1,464 open issues and PRs), corrected the installer surface to the vendor's documented 17 assistants, and added the Enterprise early-access differential formal verification and graph-aware PR review; hosted plans unchanged.
- 2026-09-26 - Recorded release v0.9.68 (2026-09-25, a watcher shell-quoting security fix) and refreshed the volatile numbers (121,495 stars, 1,933 commits, 263 contributors, 1,478 open issues and PRs); hosted plans unchanged.
- 2026-09-27 - Recorded release v0.9.69 (2026-09-26) and refreshed the volatile numbers (121,718 stars, 1,961 commits, 264 contributors, 1,483 open issues and PRs); hosted plans unchanged.
- 2026-09-29 - Recorded release v0.9.71 (2026-09-28) and refreshed the volatile numbers (122,219 stars, 1,984 commits, 267 contributors, 1,501 open issues and PRs); hosted plans unchanged.
- 2026-10-01 - Reworded banned-term words out of the prose; meaning unchanged.
- 2026-10-02 - Recorded release v0.9.73 (2026-09-30, with v0.9.72 on 2026-09-29) and refreshed the volatile numbers (123,085 stars, 2,023 commits, 277 contributors, 1,516 open issues and PRs); hosted plans re-verified unchanged.
- 2026-10-03 - Recorded release v0.9.74 (2026-10-02) and refreshed the volatile numbers (123,390 stars, 2,043 commits, 280 contributors, 1,531 open issues and PRs); hosted plans re-verified unchanged.
- 2026-10-04 - Recorded release v0.9.75 (2026-10-04) and refreshed the volatile numbers (123,562 stars, 2,080 commits, 1,503 open issues and PRs); hosted plans re-verified unchanged.
- 2026-10-05 - Recorded release v0.9.76 (2026-10-04) and refreshed the volatile numbers (123,872 stars, 2,105 commits, 287 contributors, 1,522 open issues and PRs); hosted plans re-verified unchanged against the live pricing page.
- 2026-10-06 - Recorded release v0.9.77 (2026-10-05) and refreshed the volatile numbers (124,118 stars, 2,132 commits, 294 contributors, 1,506 open issues and PRs); hosted plans re-verified unchanged against the live pricing page and the full plan index.
- 2026-10-07 - Added the Graphify-Labs/graphify star history chart to the Status section.
- 2026-10-07 - Recorded releases v0.9.78 and v0.9.79 (both 2026-10-06) and refreshed the volatile numbers (124,473 stars, 2,148 commits, 1,517 open issues and PRs); hosted plans re-verified unchanged against the live pricing page and the full plan index.
- 2026-10-08 - Recorded release v0.9.80 (2026-10-07) and refreshed the volatile numbers (124,751 stars, 2,168 commits, 311 contributors, 1,550 open issues and PRs); hosted plans re-verified unchanged against the live pricing page.
- 2026-10-09 - Recorded releases v0.9.81 and v0.9.82 (October 8 and 9) and refreshed the volatile numbers (124,825 stars, 2,188 commits, 314 contributors, 1,552 open issues and PRs); hosted plans re-verified unchanged against the live pricing page and the full plan index.
- 2026-10-10 - Recorded releases v0.9.83 and v0.9.84 (October 9 and 10) and refreshed the volatile numbers (125,102 stars, 2,210 commits, 317 contributors, 1,537 open issues and PRs); hosted plans re-verified unchanged against the live pricing page.
- 2026-10-11 - Recorded release v0.9.85 (October 10) and refreshed the volatile numbers (125,367 stars, 1,542 open issues and PRs); hosted plans re-verified unchanged against the live pricing page and the full plan index.
- 2026-10-12 - Recorded release v0.9.86 (October 11) and refreshed the volatile numbers (125,646 stars); hosted plans re-verified unchanged against the live pricing page.
- 2026-10-13 - Recorded releases v0.9.87 and v0.9.88 (both October 12) and refreshed the volatile numbers (125,962 stars, 2,324 commits, 1,493 open issues and PRs); hosted plans re-verified unchanged against the live pricing page.
- 2026-10-17 - Recorded release v0.9.92 (2026-10-16, twenty-three community pull requests across call-resolution and skill fixes, with the AST cache schema bumped so the first build after upgrading re-extracts); hosted plans unchanged.
- 2026-10-22 - Recorded release v0.9.93 (2026-10-20, twenty-two community pull requests of extraction fixes with a credential-redaction pass on rationale labels, the AST cache schema bumped so the first build after upgrading re-extracts) and refreshed the volatile numbers (2,464 commits, 332 contributors, 1,615 open issues and PRs); hosted plans re-verified unchanged against the live pricing page.
- 2026-10-24 - Recorded releases v0.9.94 (2026-10-22) and v0.9.95 (2026-10-23), a two-release security pass (ingestion rejecting malformed hosts, ports, and embedded credentials and no longer following dangling symlinks; skill installs writing through randomly named temp files so a pre-planted symlink cannot redirect them, plus type-alias extraction in four languages) and refreshed the volatile numbers (2,539 commits, 342 contributors, 1,606 open issues and PRs); hosted plans re-verified unchanged against the live pricing page and the full plan index.
- 2026-10-27 - Recorded release v0.9.96 (2026-10-26: a dependency security pass raising the Pillow floor to 13.0.0+ on Python 3.11+ and pypdf to 6.19.0+ to clear the bulk of the open Dependabot advisories, plus an 18-PR backlog batch of extraction and watch fixes) and refreshed the volatile numbers (2,584 commits, 350 contributors, 1,652 open issues and PRs); hosted plans re-verified unchanged against the live pricing page.
- 2026-10-31 - Recorded releases v0.9.98 and v0.9.99 (both 2026-10-30: collapsed duplicate edges keep their weaker provenance in an `also_seen` list instead of discarding it, and equal-length paths now resolve to the most conservative route, whose summary names its weakest hop, with `confidence_score` printed in path, explain, and neighbors output) and refreshed the volatile numbers (2,675 commits, 357 contributors, 1,644 open issues and PRs); hosted plans re-verified unchanged against the live pricing page.
- 2026-11-05 - Recorded the v0.9.100 to v0.9.102 train (2026-11-01 to 2026-11-03: node-id collisions fixed for names differing only in case, a resolution-accuracy and cache-correctness pass across C++, Rust, Python, and Go, and a large correctness and performance release spanning call resolution, the query layer, incremental update, hooks, and the skill runbook) and refreshed the volatile numbers (2,831 commits, 369 contributors, 1,629 open issues and PRs); hosted plans re-verified unchanged against the live pricing page.
- 2026-11-06 - Recorded release v0.9.103 (2026-11-05: a broad correctness, performance and robustness pass, C# preprocessor-directive blanking before parsing, Solidity library-call and YAML merge-key extractor fixes, hooks fixes for stale-by-mtime flags and the strict orientation gate, `query` reading budget and depth from `.graphifyrc` plus a `--depth` flag, the Pi project skill written to `.pi/skills`, and the AST cache schema bumped to 39 so warm caches re-run the affected extractions); hosted plans re-verified unchanged against the live pricing page.
- 2026-11-08 - Recorded release v0.9.104 (2026-11-08: a security fix stopping the `/graphify` skill runbook from substituting the agent-supplied scan path into generated Python code, the resolved root now read from the trusted `graphify-out/.graphify_root` sidecar so a directory name carrying a quote or `$(...)` cannot execute, plus a Solidity receiver-call resolution fix) and refreshed the volatile numbers (2,907 commits, 379 contributors, 1,630 open issues and PRs); hosted plans re-verified unchanged against the live pricing page.
- 2026-11-11 - Recorded the v0.9.105 and v0.9.106 pair (2026-11-09 and 11-10: a watch-tree fix pruning ignored directories so large projects stop exhausting inotify watches, C++ member-call resolution through field-typed receivers, type aliases, and forward declarations, TS/JS barrel and ESM-namespace import resolution, a uv/pip Python-version cap so fresh installs stop failing on interpreter builds, a query fix making BFS order hash-independent so edge-line output stops varying with `PYTHONHASHSEED`, a `--no-doc-demotion` query flag for docs-first corpora, and the AST cache schema bumped to 43 so warm caches re-run the affected Python and C++ extractions) and refreshed the volatile numbers (2,988 commits, 13,963 forks, 1,629 open issues and PRs); PyPI tracks 0.9.106, hosted plans re-verified unchanged against the live pricing page.
- 2026-11-13 - Recorded the v0.9.107 and v0.9.108 pair (2026-11-11 and 11-12: v0.9.107 kept case-only and underscore-prefixed member twins apart in node ids across Java, PHP, and module-level declarations, stopped the PHP route-path scan at the closure's own argument, kept LLM slice timeouts partial so failed docs re-queue, and sized the AST worker pool by uncached work while the read path stopped loading every language extractor, and v0.9.108 fixed the graph-reload single-flight race so a reload stops stalling every MCP request, accepted Oracle `[NON]EDITIONABLE` in routine and trigger recovery, let `context_filter` reach heritage edges without a context, fixed unparsed derived-table aliases and comma joins and dblink suffixes in SQL routine bodies, typed Java calls through class-qualified static fields, bound C# calls on keyword-typed receivers, and shipped a local Gemini CLI extension from the repo root) and refreshed the volatile numbers (3,027 commits, 389 contributors, 14,089 forks, 1,639 open issues and PRs); PyPI tracks 0.9.108, hosted plans re-verified unchanged against the live pricing page.
- 2026-11-15 - Recorded release v0.9.109 (2026-11-14: node-id collision fixes keeping `_name`/`name` and case-only member twins apart across C++, Swift, Kotlin, and Dart, C# explicit interface implementations kept out of overload binding with leftover overloads paired against ordinary members and non-UTF-8 files decoded before directive blanking, LLM graph-fragment validation rejecting ambiguous fragments before caching while accepting a single-element array wrapper, last good AST records preserved on source failure, and the `/graphify` skill's B3.5 coverage step reading the scan root from `.graphify_root`) and refreshed the volatile numbers (3,048 commits, 391 contributors, 14,191 forks, 1,633 open issues and PRs); PyPI tracks 0.9.109, hosted plans re-verified unchanged against the live pricing page.
- 2026-11-16 - Recorded the v0.9.110 and v0.9.111 pair (both 2026-11-15: Python aliased-import call linking from method bodies and decorated definitions, and a maintenance-and-security release raising the minimum Python from 3.10 to 3.11 for the patched dependency line) and refreshed the volatile numbers (3,065 commits, 420 contributors, 14,260 forks, 1,638 open issues and PRs); PyPI tracks 0.9.111.
- 2026-11-19 - Recorded release v0.9.112 (2026-11-17: the Delphi/Pascal cluster, Java overload nodes keyed by arity and erased signature, Go bare-receiver and Rust crate-scoped resolution, the prefix-word dedup fix, and the claude-install CLAUDE.md-precedence fix) and refreshed the volatile numbers (3,098 commits, 425 contributors, 14,454 forks, 1,686 open issues and PRs); PyPI tracks 0.9.112.
- 2026-11-20 - Recorded release v0.9.113 (2026-11-19: the Python floor raised to 3.11.5 with soupsieve pinned at 4.1.1 to clear the transitive ReDoS advisories, node-id twin fixes across Ruby, Lua, Scala, and Elixir, and a Rust prelude-generics fix) and refreshed the volatile numbers (3,128 commits, 426 contributors, 14,508 forks, 1,679 open issues and PRs); PyPI tracks 0.9.113.
- 2026-11-22 - Recorded releases v0.9.114 and v0.9.115 (2026-11-20 and 11-21: the extract/build/update performance release with the Java Lombok, Kotlin typed-receiver, PL/pgSQL, T-SQL, VB.NET, C++, and Python sys.path extractor fixes, then the GHSA-g6c9-j4vm-mwq4 forced-SMB-authentication security fix on Windows with probes bounded to the scan root); PyPI tracks 0.9.115; volatile numbers refreshed (14,578 forks, 1,692 open issues and PRs, pushed 2026-11-21).
- 2026-11-24 - Recorded release v0.9.118 (2026-11-23: the 0.9.116 and 0.9.117 changelogs folded into one release of fourteen community pull requests covering extractor, resolution, serve, export, clustering, and reporting fixes, with the AST cache schema raised 51 to 53); PyPI tracks 0.9.118; volatile numbers refreshed (14,662 forks, 1,701 open issues and pull requests, 3,202 commits, 432 contributors, pushed 2026-11-23).
- 2026-11-24 - Recorded the hosted plans gaining quarterly billing between monthly and annual (Pro $36 a quarter or $12 a month, Teams $72 a developer a quarter or $24 a month for the first 100 teams, then $96 or $32), with monthly and annual prices unchanged, the Enterprise plan now reading custom and self-hosted rather than early access and licensed per seat, a two-week card-required trial on Pro and Teams, and the early-access label moved to the rolling-out connectors (pricing page updated 2026-11-23); appended the Price history row.
- 2026-11-25 - Full rotation re-verification: every cited URL re-fetched and intact (the repository, the benchmarks, the project and pricing pages still marked updated 2026-11-23 with quarterly billing, PyPI, the v0.9.118 release, the YC page, the C# port, and the Show HN thread); recorded release v0.9.119 (2026-11-24: the core-install fix that lets the serve graph commands run without the `[mcp]` extra, plus ten community pull requests of resolution, extractor, export, and performance fixes, with the AST cache schema raised 53 to 55); PyPI tracks 0.9.119; volatile numbers refreshed (14,721 forks, 1,742 open issues and pull requests, 3,223 commits, pushed 2026-11-24).

## See also

- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins
- [Repomix](../repomix/index.md) - the packing counterargument
- [Sourcegraph code context platform](../sourcegraph-code-context/index.md) - the enterprise-scale alternative
- [MCP](../../protocols/mcp/index.md) - one of the two delivery surfaces

## References

- https://github.com/Graphify-Labs/graphify - repository, README, architecture, license, adoption numbers
- https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/BENCHMARKS.md - the self-published benchmarks, including the supermemory trade-off
- https://graphify.com/ - positioning and the no-embeddings claim
- https://graphify.com/pricing - the four hosted plans above the free core: monthly, quarterly, and annual prices, the OSS and startup discounts, and the trial terms (re-verified unchanged 2026-10-07, 2026-11-13, and 2026-11-15; quarterly billing recorded 2026-11-24 on the page marked updated 2026-11-23)
- https://graphify.com/llms-full.txt - the full plan table grounding the pricing section (monthly and annual billing), fetched 2026-10-07
- https://pypi.org/project/graphifyy/ - the distribution and current version (0.9.119, re-fetched 2026-11-25)
- https://api.github.com/repos/Graphify-Labs/graphify/releases/tags/v0.9.118 - the v0.9.118 release notes: the fourteen-pull-request batch, the consolidated 0.9.116 and 0.9.117 changelogs, and the AST cache schema bump from 51 to 53 (fetched 2026-11-24)
- https://api.github.com/repos/Graphify-Labs/graphify/releases/tags/v0.9.119 - the v0.9.119 release notes: the core-install regression fix and the ten-pull-request batch, with the AST cache schema bump from 53 to 55 (fetched 2026-11-25)
- https://www.ycombinator.com/companies/graphify-labs - the maker, batch, and self-reported adoption claims
- https://github.com/zachsaw/graphify-csharp - the third-party C# port, 73 stars as of 2026-10-10
- https://news.ycombinator.com/item?id=49667188 - the port's Show HN thread, 46 points and 21 comments, verified via the Algolia API
