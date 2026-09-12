---
title: "Context Engines Feature Matrix"
created: 2026-08-24
updated: 2026-09-12
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, context-engines, code-retrieval, developer-tools]
readability: 3
audience_notes: >
  Engineers shortlisting context engines for coding agents who need the capability deltas at a glance.
  Assumes you know what MCP, code intelligence, and token budgets mean; each column links to a full note with sources.
---

This matrix compares the eight context tools profiled in this section, feature by feature, so the shortlisting step does not require reading eight notes.
Everything below was re-verified against live sources on 2026-09-12, with the Greptile column removed on 2026-08-30 when the note moved to the Code review category.

**The interesting question is not which engine is best but whether a repository needs one at all: most codebases sit below the only published payback threshold in the category, and I claim most buyers of these engines are paying for an index their own vendors' data cannot justify.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [Augment Code](../augment-code/index.md) | [Graft](../graft/index.md) | [Graphify](../graphify/index.md) | [qmd](../qmd/index.md) | [Repomix](../repomix/index.md) | [rtk](../rtk/index.md) | [Semble](../semble/index.md) | [Sourcegraph](../sourcegraph-code-context/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | coding platform | local context-graph CLI | local knowledge-graph CLI | local search engine | local CLI | CLI output proxy | local search index | search platform |
| Deployment | cloud SaaS | local CLI, MCP, and repo files; Trail Brain is the hosted upsell | local CLI, hosted plans or self-host | local CLI plus daemon | local CLI | local binary | local CLI, MCP, or library | single-tenant cloud or self-host |
| Open source | ~ harness forks OSS Pi | ✓ MIT | ✓ Apache-2.0 | ✓ MIT | ✓ MIT | ✓ Apache-2.0 | ✓ MIT | ~ SCIP only |
| Free tier | ✗ none | ✓ entirely | ✓ CLI entirely | ✓ entirely | ✓ entirely | ✓ CLI entirely | ✓ entirely | ~ public search only |
| Index model | real-time semantic index | tree-sitter wiring graph plus optional LLM-written markdown nodes, no vectors | deterministic AST knowledge graph, no vectors | SQLite FTS5 plus vectors, markdown chunks | none, whole-repo pack | none, per-command output filtering | static embeddings plus BM25 fused, tree-sitter chunks | indexed search plus SCIP intel |
| Index freshness | real-time | structural re-sync per query, background rebuild after edits | snapshot at build time | indexed, refreshed on update | snapshot at pack time | live per command | cached index, auto-invalidated on change | index-dependent |
| Delivery to agents | own harness only | instruction files in 9 agents, 6-tool MCP server, Claude Code hooks and statusline | skill in 20+ agents, MCP, CLI | CLI, MCP server, SDK, plugin | CLI pack, ~ MCP | hooks rewriting commands in 16 tools | MCP, CLI, AGENTS.md instructions, sub-agent installer | MCP server |
| Scale where it pays | large private repos | large repos where agents re-explore, no published threshold | repo-scale Q&A and path tracing | personal docs and knowledge bases | under a few hundred K tokens | long interactive sessions with noisy commands | repos where grep-and-read burns tokens | 400K+ LOC |
| Writes code | ✓ agents and factory | ✗ maps, queries, blast radius | ✗ graphs and queries | ✗ searches only | ✗ packs only | ✗ filters output | ✗ searches only | ~ migrations, beta |
| Pricing model | $20/$100 flat tiers plus usage | free, MIT; Trail Brain from $20k/yr is the upsell | free core, $10/mo Pro, $20/seat/mo Teams, custom Enterprise | free, MIT | free, MIT | free CLI, Pro unpriced | free, MIT | from $16K/year |
| Enterprise orientation | ✓ SOC 2, ISO 42001 | ~ Trail Brain: SOC 2 Type II all plans, HIPAA BAA on Large | ~ hosted Teams/Enterprise plans | ✗ | ✗ | ~ Pro tier, on-prem option | ✗ | ✓ SOC 2, ISO 27001 |

## Reading the matrix

**This is not one market: a platform, a code-map CLI, a graph CLI, a search engine, a packer CLI, an output proxy, an on-demand search index, and a search platform share a category label but sell eight different jobs.**
Augment sells the author-review-verify loop around its engine; Graft sells a readable map the agent opens like any other file; Graphify sells structural reasoning about one codebase; qmd sells local retrieval over your documents; Repomix sells one deterministic file; rtk sells cheaper command output; Semble sells instant query-time snippets with no standing service; Sourcegraph sells retrieval to whatever agent you already run.
The review service that used to sit in this table, Greptile, moved to the Code review category, because what it sells is judgment on the PR stream, not retrieval.
The Writes code row makes the split visible: only Augment ships authoring agents, while Sourcegraph's Agentic Batch Changes stays in the migration lane, and the 2026 columns refuse the code-writing job entirely.

**I read the delivery row as the lock-in axis the marketing never names.**
Sourcegraph speaks MCP (plus API and CLI surfaces) to any agent; Repomix hands a plain file to anything that reads; Semble installs itself into whatever agents it finds, MCP, AGENTS.md instructions, or a sub-agent; Graft goes furthest, committing hooks, a statusline, and MCP config into the repo so the wiring travels with the code; Augment's Context Engine only drives Augment's own surfaces, so its documented token savings are purchasable only inside its own harness.

**The scale row is where the budget decision lives, and the only published threshold belongs to Sourcegraph.**
Its own CodeScaleBench reports a +0.259 reward delta with agents 30% cheaper and 38% faster in the 400K-2M LOC range, and a slightly negative -0.080 below 400K LOC.
Repomix inverts that curve: it pays off under a few hundred thousand tokens, then whole-window packing degrades linearly.
Augment and Graft claim the large-private-repo end but publish no size threshold.

**Freshness splits real-time from snapshot, and it bites exactly when an agent is mid-edit.**
Augment indexes in real time; Repomix is a snapshot invalidated by every edit; Sourcegraph depends on index lag it inherits from its architecture.

**Every efficiency number in this matrix is vendor-run, and the pricing floors span free to $150K.**
Augment's 33% token savings, Sourcegraph's cost deltas, Semble's 99%-fewer-tokens benchmark, and Graft's 42% token savings and 54%-to-66% SWE-bench jump all come from the vendors themselves; Augment, Semble, and Graft at least publish methodology alongside the numbers, which is the category's best practice even if no third party has replicated any of it, and Semble's founders explicitly decline to claim end-to-end agent improvements.

## Choosing from the matrix

- Multi-repo organization past 400K LOC with agents thrashing on local search and an enterprise budget: Sourcegraph.
- Token-heavy team on one large private repo wanting a single vendor for authoring and review: Augment, after re-running its benchmark on your own repo first.
- AI review of pull requests rather than retrieval: the Code review category, compared in its own [feature matrix](../code-review-feature-matrix/index.md).
- Agents re-discovering how one large codebase connects, with structure and citations preferred: Graphify, after verifying its self-published benchmarks on your repo.
- Agents starting every session blind on a large repo, and a team that wants the map committed as wiring and regenerated per machine: Graft, keeping the free structural layer and re-running its vendor benchmarks on your repo first.
- Local search over personal docs, notes, and knowledge bases for humans and agents: qmd, it is free and local.
- Small or mid repo, one-shot whole-repo questions, onboarding packs, or a CI guard on context budget: Repomix, it is free.
- Repo too big to pack, agents burning tokens on grep-and-read, no appetite for a standing service: Semble, measuring with `semble savings` before believing the benchmark.
- Metered-API sessions dominated by noisy test, git, and search output: rtk, measuring with `rtk gain` before believing the savings.
- Code must stay on-device: Graphify, Repomix, and Graft's structural layer locally, qmd and rtk entirely, or Sourcegraph self-hosted; Augment's engine stays in its cloud.

## See also

- [Context Management Patterns](../context-management-patterns/index.md) - the manual practices this category productizes
- [Code Review Feature Matrix](../code-review-feature-matrix/index.md) - the category Greptile moved to, judgment on the PR stream
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the agents that consume what these engines deliver
- [MCP](../mcp/index.md) - the protocol behind the delivery row
- [Semantic code search in coding tools](../semantic-code-search/index.md) - whether indexed retrieval survives inside editors at all

## References

- https://www.augmentcode.com/context-engine - Context Engine mechanics and efficiency claims for the Augment column
- https://www.augmentcode.com/pricing - flat Business plan and the 40% service fee for the Augment column
- https://github.com/yamadashy/repomix - CLI surface, output formats, token budgets, and MCP mode for the Repomix column
- https://sourcegraph.com/pricing - enterprise entry price and credits model for the Sourcegraph column
- https://sourcegraph.com/blog/why-coding-agents-fail-large-codebases - the 400K LOC threshold and the cost/speed deltas
- https://github.com/Graphify-Labs/graphify - the AST knowledge-graph architecture and license for the Graphify column
- https://github.com/tobi/qmd - the hybrid local search stack for the qmd column
- https://github.com/rtk-ai/rtk - the output-filtering strategies and agent integrations for the rtk column
- https://github.com/MinishLab/semble - the hybrid static-embedding stack and installer surfaces for the Semble column
- https://news.ycombinator.com/item?id=48169874 - the launch thread grounding the Semble column's self-published-benchmark caveat
- https://github.com/NanoNets/Graft - repository, README architecture and claims, license, and adoption stats for the Graft column
- https://graft.nanonets.ai - the product site and Trail attribution for the Graft column
- https://raw.githubusercontent.com/NanoNets/context-graph-engine/main/TELEMETRY.md - the telemetry posture for the Graft column
- https://trailhq.com/pricing - Trail Brain plan pricing for the Graft column's pricing cell
- https://hn.algolia.com/api/v1/items/49299985 - the launch thread grounding the Graft column's vendor-run-benchmark caveat
