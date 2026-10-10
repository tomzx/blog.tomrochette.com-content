---
title: Jevgrep
created: 2026-10-07
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, code-search, cli, open-source]
readability: 3
audience_notes: >
  Engineers choosing how a coding agent should find its starting files in an
  unfamiliar repository, and whether a per-query LLM-judged search beats
  building and maintaining an index. Assumes you know what SWE-bench, agent
  skills, and per-token billing are.
---

Jevgrep is an MIT-licensed CLI (`jg`) that answers a natural-language question about a repository with relevant files, reading leads, and verbatim source excerpts in one stdout response, using Jev to judge relevance across folders, files, and declarations.

**Jevgrep is the no-index counter-bet in this category: instead of building and maintaining an embedding or graph index, every query pays a model to judge relevance on the spot, and the author's own ten-task run prices that trade at roughly 29 percent lower agent cost at equal task success.**

## What it is

**You ask what the code does, and `jg` returns where it lives.**
A query like `jg "How are telemetry events recorded and sent?"` explores the repository hierarchy, selects files using content previews, identifies useful source units, and prints a summary, a compact file list, and source excerpts with line references to stdout.
It uses [Jev](../../hybrid-execution/jev/index.md) to judge relevance with boolean questions over folders, files, and declarations, and requires Node.js 22+ with a key for Vercel AI Gateway, TypeSafe, OpenRouter, OpenCode Zen, or any TypeSafe-compatible endpoint.
Declaration parsing covers Python, TypeScript/JavaScript, Go, and Rust, with a content-preview fallback for other text.
The MIT-licensed CLI ships from David Zhang (dzhng), the engineer behind deep-research, alongside an agent-skill installer (`jg skill`) that wires Claude Code, Codex, OpenCode, and other detected agents to reach for it.

## Status

**Not yet three weeks old and the fastest start in this category, with a thin discussion footprint so far.**
2,482 stars, 180 forks, and 27 open issues and pull requests since the repository appeared on 2026-09-26, pushed 2026-10-02, all as of 2026-10-09 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=dzhng/jevgrep&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=dzhng/jevgrep&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=dzhng/jevgrep&type=date&legend=top-left" />
</picture>

The npm package `@dzhng/jevgrep` sits at v0.8.0 (published 2026-10-01) across 16 releases in its first week, with 6,657 trailing-month downloads (window 2026-09-08 to 2026-10-07).
Its Show HN (2026-09-28) drew 5 points and zero comments, so adoption is running on the author's reputation and the skill distribution rather than discussion.
The earlier run that rejected this repository as a harness candidate recorded it three days into its life; the star count and a proper category fit resolved it as a note this run.

## Strengths

- **No index to build, update, or trust**: the search runs against the working tree, so there is no stale-index failure mode and nothing to wire into CI.
- The agent skill is unusually disciplined: it tells the agent to start behavioral discovery with `jg` but to use grep and direct reads for exact symbols, which is the right division of labor and a discipline few skill descriptions attempt.
- The benchmark reporting is the category's most candid: single-run caveats in its own text, a separate total-cost rerun including the Jev bill (25.8 percent lower), and an explicit statement that the runs establish no statistical equivalence.
- It composes with anything that reads stdout, so it needs no MCP server, no daemon, and no per-agent integration work beyond the skill.

## Cautions

- **Every query sends eligible source content to a model provider**: the docs say default filtering excludes credentials and dependencies but is not a guarantee, so the search root is a privacy decision.
- Every query costs provider tokens, so a team that searches constantly may pay more than an index would charge after its one-time build, and the vendor-run benchmark covers ten tuned Python tasks from one repository.
- Pre-1.0 with a v0.x CLI, one maintainer, and breaking changes already recorded (0.3.0 replaced environment-based credentials with `jg auth`).
- Declaration-aware output is limited to four language families, and queries fall back to content previews elsewhere.
- The star count is under three weeks old; the same velocity that looks like momentum is also the easiest number to fake with a launch push, so the footprint deserves a re-read before this note's framing ages.

## Pricing

**Free and MIT-licensed; the meter is your provider's model bill.**
The CLI has no account and no paid tier, but each query runs Jev judgments under your own key (Vercel AI Gateway, TypeSafe, OpenRouter, OpenCode Zen, or a custom TypeSafe-compatible endpoint), so the running cost is the provider's usage at its published rates.
The author's own total-cost measurement puts the Jev share at roughly a quarter to a third of the savings it produces.

## Compared to

- [Semble](../semble/index.md): the local-index counterpart, free queries after an index build; choose Semble for repeated searching on one machine, Jevgrep when you do not want the index at all or the question is behavioral rather than similarity-based.
- [Sourcegraph code context platform](../sourcegraph-code-context/index.md): indexed cross-repository search at enterprise price; Jevgrep is one repo per query, but starts at zero dollars and zero setup.
- [Repomix](../repomix/index.md): the inclusion-first alternative that packs the whole repo; Jevgrep selects the slice instead, paying per query rather than per token packed.

## Bottom line

**Recommended for agents starting unfamiliar multi-file work in repositories where nobody maintains an index, and for teams already paying metered model bills who will measure savings on their own tasks.**
Not for exact-symbol lookups (grep wins), teams that cannot send source to a model provider, or anyone who needs proven savings beyond one author-run benchmark.
My disagreeable claim: every index in this category is a cache standing in front of model judgment, and Jevgrep's numbers hint that the cache no longer pays for itself in the start-of-task discovery case, which would make the maintained index the legacy option here within a year.

## Changes

- 2026-10-07 - Created from the 2026-10-07 entrant scan (the GitHub created-after search), superseding the 2026-09-29 harnesses-routed rejection after the repository reached 2,355 stars, with the no-index framing and the vendor-run-benchmark caveat recorded.

## See also

- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins as the eleventh column
- [Semble](../semble/index.md) - the local-index counterpart answering the same where-do-I-start question
- [Jev](../../hybrid-execution/jev/index.md) - the model doing the relevance judging under every query
- [Semantic code search in coding tools](../../retrieval/semantic-code-search/index.md) - the indexed-retrieval pattern this tool skips
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - where the context-engine layer sits in the four-layer map

## References

- https://api.github.com/repos/dzhng/jevgrep - repository stats: 2,355 stars, 171 forks, created 2026-09-26, pushed 2026-10-02, as of 2026-10-07
- https://raw.githubusercontent.com/dzhng/jevgrep/main/README.md - architecture, benchmark tables with per-run caveats, privacy and caching notes
- https://raw.githubusercontent.com/dzhng/jevgrep/main/skills/jevgrep/SKILL.md - the agent skill surface and the grep-for-exact-symbols division of labor
- https://raw.githubusercontent.com/dzhng/jevgrep/main/apps/cli/README.md - auth flow, supported providers, `jg doctor`, cache controls
- https://registry.npmjs.org/@dzhng%2Fjevgrep - the package, v0.8.0 latest, 16 versions since 2026-09-26
- https://api.npmjs.org/downloads/point/last-month/@dzhng/jevgrep - 5,869 downloads, window 2026-09-05 to 2026-10-04, fetched 2026-10-07
- https://github.com/dzhng/jevgrep/releases - the release train from v0.4.4 to v0.8.0 (2026-09-28 through 2026-10-01)
- https://news.ycombinator.com/item?id=49880146 - the Show HN: 5 points, zero comments, 2026-09-28 (verified via the Algolia items API)
- https://api.github.com/repos/dzhng/deep-research - the author's track record: 19,764 stars on deep-research as of 2026-10-07
- https://api.github.com/users/dzhng - the author's profile: David Zhang
