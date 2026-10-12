---
title: code-review-graph
created: 2026-10-11
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, code-graph, mcp, static-analysis]
readability: 3
audience_notes: >
  Engineers shortlisting code-graph context engines for review-heavy agent workflows on large repositories.
  Assumes you know what Tree-sitter, MCP, and blast-radius analysis are; pairs with Graphify and Serena in this category.
---

code-review-graph is a local-first Python tool that parses a repository into a Tree-sitter knowledge graph and serves it to AI coding tools over MCP and a CLI, so a review reads the blast radius of a change instead of the repository.

**The mechanism is a context engine wearing a review badge: the graph decides what enters the window, the smallest file set a change touches, and the project ships the category's most self-critical benchmarks, stating in its own README that its recall metric is circular and its whole-corpus baseline is one no agent pays.**

## What it is

A pip or pipx CLI (MIT, Python 3.10+) by Tirth (tirth8205), solo maintainer, with an MCP server on stdio or localhost HTTP and one SQLite graph per repository in `.code-review-graph/`.
Tree-sitter parses 30-plus languages and notebooks into nodes (functions, classes, imports) and edges (calls, inheritance, tests); queries return blast radius, risk-scored change detection, hub and bridge detection, community maps, execution flows, dead code, and a generated wiki.
`install` detects up to sixteen AI coding tools (Codex, Claude Code, Cursor, Windsurf, Zed, Continue, OpenCode, and more) and writes each one an MCP entry plus hooks, skills, and rules-file text; `uninstall` removes exactly what it wrote.
A composite GitHub Action posts risk-scored PR comments updated in place, with an optional fail-on-risk merge gate, running the graph on your runner with no source sent anywhere; there is no telemetry, and cloud embeddings are opt-in behind a printed egress warning.

## Status

Active and unusually fast-growing: 32,046 stars, 2,936 forks, and 182 open issues as of 2026-10-11, created 2026-02-26, pushed 2026-10-06, so five figures of stars arrived in under eight months.
PyPI carries 2.3.9 (uploaded 2026-09-18) across 37 releases on a roughly monthly cadence, and the repo runs a documented staging to testing to main promotion flow.
The community footprint is lopsided: a Hacker News search returns three story hits, the largest a 12-point launch thread with two comments (one an install failure), so the star count arrived without front-page discussion, the Trendshift-badge pattern this section has seen before.
Every number below is the author's own; no independent benchmark exists.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=tirth8205/code-review-graph&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=tirth8205/code-review-graph&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=tirth8205/code-review-graph&type=date&theme=dark&legend=top-left" />
</picture>

## Strengths

- The benchmark section is the category's most self-critical: recall 1.0 is labelled circular (the ground truth comes from the same graph the predictor walks), the whole-corpus baseline is called an upper bound no agent pays, the co-change mode is reported not yet usable, and pins, seeds, and a reproduction recipe are published.
- Incremental freshness is mechanical and measured: SHA-diffed re-parses through hooks, watch mode, or a daemon, about 2.5 seconds for a two-file edit on a 3,000-file repository.
- The installer is the widest wiring surface in this category's matrix, one command configuring up to sixteen platforms, with an uninstall documented down to atomic config writes.
- Genuinely local: no telemetry, a SQLite file in the repo, and a stated rule that cloud embedding text is identifiers, signatures, and docstring summaries, never function bodies.

## Cautions

- The headline roughly 63x median reduction is measured against that whole-corpus baseline; the agent-baseline eval that would measure a fairer comparison exists, but no canonical capture of it is published.
- A third-party write-up quotes older claims (6.8x fewer tokens on reviews, up to 49x on daily coding) that it admits it has not verified and that the current README no longer makes, so secondary coverage lags the primary numbers.
- Solo maintainer, eight months old: bus factor one, and the star velocity is ahead of any independent validation.
- Impact analysis is deliberately low-precision (flagging an extra file beats missing a dependency), which costs tokens on large dependency graphs, and the README's own limitations put flow-detection recall at 33%.
- Small repositories and single-file diffs are named by the project itself as cases where graph context costs more than it saves, and the name oversells the review job: the tool judges nothing on the PR stream.

## Pricing

Free, MIT, entirely local.
Pricing does not apply.

## Compared to

- [Graphify](../graphify/index.md): the closest sibling, also a local AST knowledge graph; Graphify aims at repo-scale Q&A and path tracing, this tool is change-and-review-first with blast radius and a CI action.
- [Serena](../serena/index.md): LSP-backed symbol tools that parse live and edit at symbol level, more precise per symbol; this tool wins multi-hop impact questions from a stored graph.
- [Repomix](../repomix/index.md): the one-file whole-repo pack, simplest for one-shot questions on repos that fit a window; no structural queries, and stale the moment you edit.

## Bottom line

**Recommended for review-heavy teams on multi-thousand-file repositories that want the agent to read only the blast radius, after reading the benchmark caveats and ideally re-running the eval on your own repo; not for small repos, single-file diffs, or anyone expecting a tool that judges code.**

## Changes

- 2026-10-11 - Created from the code-review scan's flag, shelved in context-engines over code-review because the graph serves context and judges nothing, with the whole-corpus-baseline and solo-maintainer cautions recorded as the critical angle.

## See also

- [Graphify](../graphify/index.md) - the AST-graph sibling one job over, structure for Q&A instead of change impact
- [Serena](../serena/index.md) - the LSP contrast: live symbol precision against a stored structural graph
- [Repomix](../repomix/index.md) - the pack-everything contrast at the other end of the size curve
- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins
- [Code Review Feature Matrix](../../code-review/code-review-feature-matrix/index.md) - the category the name borrows from, judgment on the PR stream

## References

- https://api.github.com/repos/tirth8205/code-review-graph - stars, forks, issues, license, creation and push dates as of 2026-10-11
- https://raw.githubusercontent.com/tirth8205/code-review-graph/main/README.md - mechanism, installer surfaces, benchmark tables, and the limitations list
- https://raw.githubusercontent.com/tirth8205/code-review-graph/main/docs/FAQ.md - the when-not-to-use size thresholds, the no-telemetry statement, and the Serena and Repomix comparison
- https://pypi.org/pypi/code-review-graph/json - version 2.3.9 and the 37-release train
- https://api.github.com/repos/tirth8205/code-review-graph/releases?per_page=5 - release cadence through v2.3.9 (2026-09-18)
- https://hn.algolia.com/api/v1/items/47314090 - the 12-point launch thread with the install-failure comment
- https://hn.algolia.com/api/v1/search?query=code-review-graph&tags=story&hitsPerPage=10 - the thin Hacker News footprint check as of 2026-10-11
- https://dev.to/stevengonsalvez/code-review-graph-stop-your-agent-reading-the-whole-repo-4272 - the third-party write-up quoting unverified older figures, the record's skeptical source
- https://code-review-graph.com - the website, client-rendered this run (title only fetched), cited through the fetched primaries
