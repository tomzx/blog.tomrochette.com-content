---
title: Semble
created: 2026-08-30
updated: 2026-09-02
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, code-search, context-engines, local-first, developer-tools]
readability: 3
audience_notes: >
  Engineers deciding whether agents should retrieve code by search instead of grep-and-read,
  and what a static-embedding index can and cannot promise. Assumes familiarity with BM25,
  embeddings, and MCP.
---

Semble is a MIT-licensed local code search tool built for coding agents: it chunks a repository along syntax boundaries, indexes it with static Model2Vec embeddings plus BM25, and answers natural-language queries with only the relevant snippets.
Facts below verified as of 2026-09-02.

**Semble's bet is that a code-specialized index small enough to run in under a second on any CPU can replace the most expensive thing an agent does, which is grep-failing its way through full-file reads.**

## What it is

**One Python tool, three delivery surfaces, zero setup.**
`semble install` detects installed agents (Claude Code, Codex, OpenCode, Pi, and others) and wires any combination of an MCP server, CLI usage instructions in AGENTS.md or CLAUDE.md, and a dedicated `semble-search` sub-agent; `semble uninstall` reverses it.
The engine splits files into tree-sitter chunks, scores queries with static potion-code-16M-v2 embeddings and BM25 in parallel, fuses the rankings with reciprocal rank fusion, then reranks with code-aware signals; everything runs on CPU with no API keys or external services.
It ships as a CLI (`semble search`, `find-related`, a docs/config/all content switch), a two-tool MCP server (`search`, `find_related`), and a Python library, with gitignore-aware filtering, local path or git-URL inputs, and cached indexes invalidated on file change.
It is built by MinishLab, the two-person team (Stephan and Thomas, per the launch post) behind the Model2Vec static-embedding project.

## Status

**Young, active, and unusually well received for a search tool.**
5,981 stars and 259 forks since the repo appeared on 2026-04-06, with the last push 2026-08-26 and v0.5.5 released 2026-08-12 (GitHub API, as of 2026-09-02).
120,156 PyPI downloads in the month ending 2026-09-01 (PyPIstats).
The launch Show HN (May 17, 2026) drew 445 points and 151 comments, on top of two quiet warm-up threads in April; a third-party VS Code extension appeared in August, which is the usual early-ecosystem signal.

## Strengths

- **The speed numbers, if they replicate, change the deployment model**: about 500 ms to index an average repo and about 1 ms per query on CPU means per-session on-demand indexing, with no standing service and no stale-index failure mode.
- The retrieval stack is a real hybrid design, static embeddings for meaning plus BM25 for identifiers, not one trick, and the pipeline and ablations are published.
- Token-efficiency framing is measurable at the margins that matter: the benchmark reports 97 percent recall at 2k retrieved tokens where grep-plus-read needs a 100k window for 85 percent.
- Grounded, self-measured savings: `semble savings` records actual calls and estimated avoided tokens per machine, so a team can audit the claim on its own traffic instead of trusting the vendor.

## Cautions

- **Every published number is self-run, and the founders say so**: in the launch thread they state they do not claim end-to-end agent improvements because they have not measured them, so the 99-percent token reduction is a retrieval-layer figure, not a work-quality one.
- The benchmark bar is modest: parity is claimed against CodeRankEmbed, a 137M-parameter model, and the static-embedding design caps how much semantic depth is available at any price.
- The "fewer tokens than grep" baseline has been challenged on its own terms: grep spends zero tokens, the cost is the agent's read strategy afterward, and commenters asked whether the comparison is 100k-to-2k or 1k-to-20, a question the benchmark answers only in aggregate.
- Two maintainers, a five-month-old project, and a pre-1.0 (0.5.x) API are the usual early-adoption risks.

## Pricing

**Free and MIT-licensed; there is nothing to buy.**
No cloud tier or paid plan exists as of 2026-09-02, so the cost model is entirely the compute you already have and the model tokens the snippets displace.

## Compared to

- [Repomix](../repomix/index.md): the inclusion-first alternative, one deterministic file for the whole repo; Repomix wins for small repos and one-shot questions, Semble wins once the pack would eat the window.
- [Graphify](../graphify/index.md): the structure-first alternative, a deterministic AST knowledge graph with citations; choose Graphify for how-the-codebase-connects questions, Semble for where-is-the-code-that-does-X.
- [qmd](../qmd/index.md): the same hybrid static-embedding plus BM25 plus rerank architecture, aimed at personal notes and docs rather than codebases; the two are complements, one per corpus.

## Bottom line

**Recommended for agent users on repos big enough that grep-plus-read burns real tokens, who want a local, key-free index and will measure savings with `semble savings` rather than take the benchmark on faith.**
Not for small repos where a Repomix pack or plain grep is already enough, and not for anyone needing vendor support or an agent-level quality guarantee, because neither exists yet.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where the context-engine layer sits in the four-layer map
- [Semantic code search](../semantic-code-search/index.md) - the pattern note this tool instantiates
- [Tree-sitter chunking](../tree-sitter-chunking/index.md) - the parsing layer under Semble's chunker
- [rtk](../rtk/index.md) - the neighboring token-reduction bet, filtering output instead of selecting input

## References

- https://github.com/MinishLab/semble - repo, README (architecture, installer, CLI, MCP, savings counter), stars and activity as of 2026-09-02
- https://news.ycombinator.com/item?id=48169874 - the 445-point launch thread, including the founders' no-agent-level-claim statement and the baseline criticisms (verified via the Algolia items API)
- https://pypi.org/project/semble/ - the package surface
- https://pypistats.org/api/packages/semble/recent - 120,156 downloads in the month ending 2026-09-01
- https://huggingface.co/minishlab/potion-code-16M-v2 - the embedding model the index runs on
- https://github.com/MinishLab/semble/blob/main/benchmarks/README.md - benchmark methodology, NDCG@10, and the token-efficiency setup
