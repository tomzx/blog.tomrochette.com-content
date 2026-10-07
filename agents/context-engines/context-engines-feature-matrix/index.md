---
title: "Context Engines Feature Matrix"
created: 2026-08-24
updated: 2026-10-07
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, context-engines, code-retrieval, developer-tools]
readability: 3
audience_notes: >
  Engineers shortlisting context engines for coding agents who need the capability deltas at a glance.
  Assumes you know what MCP, code intelligence, and token budgets mean; each column links to a full note with sources.
---

This matrix compares the fourteen context tools profiled in this section, feature by feature, so the shortlisting step does not require reading fourteen notes.

**The interesting question is not which engine is best but whether a repository needs one at all: most codebases sit below the only published payback threshold in the category, and I claim most buyers of these engines are paying for an index their own vendors' data cannot justify.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [Augment Code](../augment-code/index.md) | [CodeAlive](../codealive/index.md) | [Context7](../context7/index.md) | [Graft](../graft/index.md) | [Graphify](../graphify/index.md) | [Headroom](../headroom/index.md) | [Jevgrep](../jevgrep/index.md) | [qmd](../qmd/index.md) | [Repomix](../repomix/index.md) | [rtk](../rtk/index.md) | [Semble](../semble/index.md) | [Serena](../serena/index.md) | [Sourcegraph code context platform](../sourcegraph-code-context/index.md) | [TOON](../toon-format/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | coding platform | hosted context-engine API | hosted docs-injection service | local context-graph CLI | local knowledge-graph CLI | local compression layer (library, proxy, agent wrap, MCP) | per-query code-search CLI | local search engine | local CLI | CLI output proxy | local search index | MCP semantic-code toolkit | search platform | serialization convention (spec plus implementations) |
| Deployment | cloud SaaS | cloud SaaS; demo-gated self-hosted (Docker Compose or Kubernetes/Helm, BYO-LLM); Docker MCP for the cloud product | cloud SaaS; self-hosted on Enterprise; hosted MCP endpoint plus local CLI and skill installs | local CLI, MCP, and repo files; Trail Brain is the hosted upsell | local CLI, hosted plans or self-host | local only (library, proxy on localhost, wrap around 14 agents, MCP server) | local CLI plus installed agent skill; queries run against a model provider under your key | local CLI plus daemon | local CLI | local binary | local CLI, MCP, or library | local MCP server (stdio or HTTP), paid JetBrains plugin backend | single-tenant cloud or self-host | in-process library (TypeScript reference plus community ports), no service |
| Open source | ~ harness forks OSS Pi | ✗ closed core; self-hostable MCP server only | ~ CLI and MCP server MIT, the platform closed | ✓ MIT | ✓ Apache-2.0 | ✓ Apache-2.0 | ✓ MIT | ✓ MIT | ✓ MIT | ✓ Apache-2.0 | ✓ MIT | ~ application GPL-3.0-or-later, SolidLSP MIT | ~ SCIP only | ✓ MIT spec and reference implementation |
| Free tier | ✗ none | ✓ free tier with MCP access (25 MB repos, 100 chats/month) | ✓ 1,000 API calls/month on public repos, plus 20 bonus calls a day while blocked | ✓ entirely | ✓ CLI entirely | ✓ entirely | ✓ CLI entirely; queries bill provider tokens | ✓ entirely | ✓ entirely | ✓ CLI entirely | ✓ entirely | ✓ core entirely; JetBrains backend paid | ~ public search only | ✓ entirely |
| Index model | real-time semantic index | server-side code graph plus hybrid semantic, lexical, and graph-traversal retrieval | none of yours, a hosted index of the world's library documentation, version-parsed, trust-scored, and injection-screened | tree-sitter wiring graph plus optional LLM-written markdown nodes, no vectors | deterministic AST knowledge graph, no vectors | none, per-message statistical and BERT-class compression with an optional AST mode; a Compress-Cache-Retrieve store keeps originals | none, per-query relevance judged by Jev over the working tree | SQLite FTS5 plus vectors, markdown chunks | none, whole-repo pack | none, per-command output filtering | static embeddings plus BM25 fused, tree-sitter chunks | none, live language-server parse (40+ languages); optional JetBrains analysis | indexed search plus SCIP intel | none, a deterministic re-encoding of the JSON data model (indentation plus tabular rows) |
| Index freshness | real-time | refreshed on every push | refreshed from upstream docs by the service, version-specific | structural re-sync per query, background rebuild after edits | snapshot at build time | live per call, with a deduplicating cross-agent memory store | live per query, no index | indexed, refreshed on update | snapshot at pack time | live per command | cached index, auto-invalidated on change | live parse of the working tree, no index | index-dependent | deterministic per document, nothing indexed |
| Delivery to agents | own harness only | hosted MCP endpoint, Docker MCP, REST API, npx installer | hosted MCP endpoint, npx MCP server, `ctx7` CLI plus agent skill (no MCP mode) | instruction files in 9 agents, 6-tool MCP server, Claude Code hooks and statusline | skill in 17 assistants (vendor count), MCP, CLI | Python/TypeScript library, `headroom proxy`, `headroom wrap` for 14 coding agents, MCP server | CLI, agent skill installer for Claude Code, Codex, OpenCode, and others | CLI, MCP server, SDK, plugin | CLI pack, ~ MCP | hooks rewriting commands in 16 tools | MCP, CLI, AGENTS.md instructions, sub-agent installer | MCP server (stdio or HTTP) | MCP server | any (encode at the prompt boundary in code; media type and file extension defined) |
| Scale where it pays | large private repos | multi-repo exploration on a metered budget; published tiers cap repos at 25-500 MB | any project on fast-moving third-party libraries whose training-data knowledge has gone stale | large repos where agents re-explore, no published threshold | repo-scale Q&A and path tracing | token bills dominated by tool output, logs, and RAG noise | unfamiliar repos where nobody maintains an index | personal docs and knowledge bases | under a few hundred K tokens | long interactive sessions with noisy commands | repos where grep-and-read burns tokens | large polyglot repos, reference hunts and refactors | 400K+ LOC | prompts embedding large uniform arrays (tables, record lists) |
| Writes code | ✓ agents and factory | ~ review agent comments on PRs | ✗ delivers docs only | ✗ maps, queries, blast radius | ✗ graphs and queries | ✗ compresses input only | ✗ finds and excerpts only | ✗ searches only | ✗ packs only | ✗ filters output | ✗ searches only | ✓ symbol-level edits and renames | ~ migrations, beta | ✗ |
| Pricing model | $20/$100 flat tiers plus usage | free tier, $15/$50/from-$100 monthly usage balances, per-action rates ($0.02 search to $0.50 review) | free tier, Pro $10/seat/month (2,000 calls included, then $5 per 1,000; private-repo parsing $5 per 1M tokens), Enterprise custom | free, MIT; Trail Brain from $20k/yr is the upsell | free core, Pro $10/mo yearly or $15 monthly, Teams $20/seat/mo yearly or $29 monthly, Enterprise early access | free, Apache-2.0 | free, MIT; queries bill your provider's Jev usage | free, MIT | free, MIT | free CLI, Pro unpriced | free, MIT | free core; paid JetBrains plugin, price unpublished | from $16K/year | free, MIT |
| Enterprise orientation | ✓ SOC 2, ISO 42001 | ~ self-hosted option, DPA, no-training claims; tiny vendor, no SOC 2 yet | ✓ SOC 2, SSO, and self-hosted on Enterprise | ~ Trail Brain: SOC 2 Type II all plans, HIPAA BAA on Large | ~ hosted Teams/Enterprise plans | ✗ | ✗ | ✗ | ✗ | ~ Pro tier, on-prem option | ✗ | ~ paid JetBrains backend, no enterprise plan | ✓ SOC 2, ISO 27001 | ✗ |

## Reading the matrix

**This is not one market: a platform, a hosted context-engine API, a docs-injection service, a code-map CLI, a graph CLI, a compression layer, a per-question search CLI, a search engine, a packer CLI, an output proxy, an on-demand search index, an LSP symbol toolkit, a search platform, and a serialization convention share a category label but sell fourteen different jobs.**
Augment sells the author-review-verify loop around its engine; CodeAlive sells metered access to a hosted multi-repo index to whatever agent you already run; Context7 sells fresh third-party documentation injected at prompt time; Graft sells a readable map the agent opens like any other file; Graphify sells structural reasoning about one codebase; Headroom sells a smaller token bill for everything the agent reads, with the originals one retrieve away; Jevgrep sells the first files of an answer, judged per query with no index to maintain; qmd sells local retrieval over your documents; Repomix sells one deterministic file; rtk sells cheaper command output; Semble sells instant query-time snippets with no standing service; Serena sells the IDE's own symbol tools to whatever agent you already run; Sourcegraph sells retrieval to whatever agent you already run; TOON sells the same data for fewer tokens at the prompt boundary.
The review service that used to sit in this table, Greptile, moved to the Code review category, because what it sells is judgment on the PR stream, not retrieval.
The Writes code row makes the split visible: Augment ships authoring agents, Sourcegraph's Agentic Batch Changes stays in the migration lane, Serena edits at the symbol level when the task asks, CodeAlive's review agent only comments on PRs, and the other 2026 columns refuse the code-writing job entirely.

**I read the delivery row as the lock-in axis the marketing never names.**
Sourcegraph speaks MCP (plus API and CLI surfaces) to any agent; Repomix hands a plain file to anything that reads; Semble installs itself into whatever agents it finds, MCP, AGENTS.md instructions, or a sub-agent; Graft goes furthest, committing hooks, a statusline, and MCP config into the repo so the wiring travels with the code; Augment's Context Engine only drives Augment's own surfaces, so its documented token savings are purchasable only inside its own harness.
Context7 and Headroom sit at the opposite pole: both are outside services (hosted or local) that any agent can consume, Context7 through one MCP registration or skill and Headroom through one wrap command across fourteen agents, which makes them the cheapest columns to try and the easiest to drop.

**The scale row is where the budget decision lives, and the only published threshold belongs to Sourcegraph.**
Its own CodeScaleBench reports a +0.259 reward delta with agents 30% cheaper and 38% faster in the 400K-2M LOC range, and a slightly negative -0.080 below 400K LOC.
Repomix inverts that curve: it pays off under a few hundred thousand tokens, then whole-window packing degrades linearly.
Augment and Graft claim the large-private-repo end but publish no size threshold.

**Freshness splits real-time from snapshot, and it bites exactly when an agent is mid-edit.**
Augment indexes in real time; Repomix is a snapshot invalidated by every edit; Sourcegraph depends on index lag it inherits from its architecture; Serena sidesteps the axis entirely by parsing the working tree live with no index at all, and Jevgrep dodges it the same way, judging the tree live on every query.
Context7 moves freshness off your repo and onto the world's documentation, refreshed by the service; Headroom and TOON have no index to go stale, one compressing each message as it passes and the other encoding each document deterministically.

**Every efficiency number in this matrix is vendor-run, and the pricing floors span free to $150K.**
Augment's 33% token savings, Sourcegraph's cost deltas, Semble's 99%-fewer-tokens benchmark, Graft's 42% token savings and 54%-to-66% SWE-bench jump, Jevgrep's roughly 29% task-cost cut, and Headroom's 57%-on-a-seeded-incident-dump table all come from the vendors themselves; Augment, Semble, Graft, Jevgrep, and Headroom at least publish methodology alongside the numbers, which is the category's best practice even if no third party has replicated any of it, and Semble's founders explicitly decline to claim end-to-end agent improvements.

## Choosing from the matrix

- Multi-repo organization past 400K LOC with agents thrashing on local search and an enterprise budget: Sourcegraph.
- Token-heavy team on one large private repo wanting a single vendor for authoring and review: Augment, after re-running its benchmark on your own repo first.
- Metered hosted indexing for any MCP agent on a small-team budget: CodeAlive, starting from the free tier and believing none of its numbers until replicated on your repos.
- AI review of pull requests rather than retrieval: the Code review category, compared in its own [feature matrix](../../code-review/code-review-feature-matrix/index.md).
- Agents re-discovering how one large codebase connects, with structure and citations preferred: Graphify, after verifying its self-published benchmarks on your repo.
- Agents starting every session blind on a large repo, and a team that wants the map committed as wiring and regenerated per machine: Graft, keeping the free structural layer and re-running its vendor benchmarks on your repo first.
- An agent starting cold in a repository nobody indexed, paying per question instead of maintaining an index: Jevgrep, after measuring a week of queries against your provider bill.
- Local search over personal docs, notes, and knowledge bases for humans and agents: qmd, it is free and local.
- Small or mid repo, one-shot whole-repo questions, onboarding packs, or a CI guard on context budget: Repomix, it is free.
- Repo too big to pack, agents burning tokens on grep-and-read, no appetite for a standing service: Semble, measuring with `semble savings` before believing the benchmark.
- IDE-grade navigation, reference hunts, and symbol edits on a large polyglot repo, free and local: Serena, keeping grep for the vague concept queries symbol tools cannot answer.
- Metered-API sessions dominated by noisy test, git, and search output: rtk, measuring with `rtk gain` before believing the savings.
- Agents hallucinating APIs from fast-moving libraries: Context7, starting on the free tier and checking injected docs against the versions you pin.
- A token bill dominated by tool output, logs, or RAG noise across many agents: Headroom, starting with the proxy on one workflow and auditing what survives compression.
- Large uniform tables or record lists embedded in prompts: TOON, comparing tokens and accuracy against JSON on your own model before committing.
- Code must stay on-device: Graphify, Repomix, and Graft's structural layer locally, qmd and rtk entirely, Headroom's compression entirely, or Sourcegraph self-hosted; Augment's engine and Context7's platform stay in their clouds.

## Changes

- 2026-08-24 - Created with four columns as one of the remaining categories' companion matrices.
- 2026-08-30 - Graphify, qmd, and rtk columns added, matrix at seven columns, kind-row prose and choosing list extended.
- 2026-08-30 - Extended to eight columns with Semble inserted alphabetically, with reading, choosing, and references sections extended.
- 2026-08-30 - Greptile column removed, back to seven columns, when the note moved to the Code review category.
- 2026-09-16 - Re-dated the re-verification and updated the Graphify pricing cell for the new monthly billing options and the early-access Enterprise tier.
- 2026-09-20 - Repointed the Graft references to the canonical trailhq/Graft repository after the GitHub org rename; no cells moved.
- 2026-09-24 - Renamed the Sourcegraph column to its listing title, Sourcegraph code context platform; no cells moved.
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-25 - Updated the Graphify delivery cell to the vendor's documented 17-assistant installer surface.
- 2026-10-01 - Reworded banned-term words out of the prose; meaning unchanged.
- 2026-10-04 - Extended from eight to nine columns with Serena (the LSP-backed MCP semantic-code toolkit), inserted in sorted position between Semble and Sourcegraph and traced to the new note; the intro, reading, and choosing sections updated for the ninth job and the live-parse freshness column.
- 2026-10-05 - Extended from nine to ten columns with CodeAlive (the hosted agent-agnostic context-engine API), inserted in sorted position after Augment Code and traced to the new note; the intro, reading, and choosing sections updated for the tenth job.
- 2026-10-06 - Moved the CodeAlive deployment and enterprise-orientation cells to record the demo-gated self-hosted deployment (Docker Compose or Kubernetes/Helm, BYO-LLM) with no SOC 2 badge yet; no membership change.
- 2026-10-07 - Extended from ten to eleven columns with Jevgrep (the per-query LLM-judged code-search CLI), inserted in sorted position between Graphify and qmd and traced to the new note; the intro, reading, freshness, efficiency, and choosing sections updated for the eleventh job.
- 2026-10-07 - Extended from eleven to fourteen columns with Context7 (the hosted docs-injection service), Headroom (the local compression layer), and TOON (the serialization convention), inserted in sorted position and traced to the new notes; the intro, delivery, freshness, efficiency, and choosing sections updated for the three new jobs, and the TOON note placed in this category over protocols because it optimizes what enters the window rather than interoperating surfaces.

## See also

- [Context Management Patterns](../../context-management-patterns/index.md) - the manual practices this category productizes
- [Code Review Feature Matrix](../../code-review/code-review-feature-matrix/index.md) - the category Greptile moved to, judgment on the PR stream
- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - the agents that consume what these engines deliver
- [MCP](../../protocols/mcp/index.md) - the protocol behind the delivery row
- [Semantic code search in coding tools](../../retrieval/semantic-code-search/index.md) - whether indexed retrieval survives inside editors at all

## References

- https://www.augmentcode.com/context-engine - Context Engine mechanics and efficiency claims for the Augment column
- https://www.augmentcode.com/pricing - flat Business plan and the 40% service fee for the Augment column
- https://codealive.ai/en - the tier table, per-action rates, and MCP delivery surfaces for the CodeAlive column
- https://docs.codealive.ai/integrations/mcp - the MCP v3 tools and hosted-endpoint deployment behind the CodeAlive column's delivery cell
- https://github.com/yamadashy/repomix - CLI surface, output formats, token budgets, and MCP mode for the Repomix column
- https://sourcegraph.com/pricing - enterprise entry price and credits model for the Sourcegraph code context platform column
- https://sourcegraph.com/blog/why-coding-agents-fail-large-codebases - the 400K LOC threshold and the cost/speed deltas
- https://github.com/Graphify-Labs/graphify - the AST knowledge-graph architecture and license for the Graphify column
- https://github.com/tobi/qmd - the hybrid local search stack for the qmd column
- https://github.com/rtk-ai/rtk - the output-filtering strategies and agent integrations for the rtk column
- https://github.com/MinishLab/semble - the hybrid static-embedding stack and installer surfaces for the Semble column
- https://news.ycombinator.com/item?id=48169874 - the launch thread grounding the Semble column's self-published-benchmark caveat
- https://github.com/trailhq/Graft - canonical repository (NanoNets/Graft redirects here), README architecture and claims, license, and adoption stats for the Graft column
- https://graft.nanonets.ai - the product site and Trail attribution for the Graft column
- https://raw.githubusercontent.com/trailhq/Graft/main/TELEMETRY.md - the telemetry policy for the Graft column
- https://trailhq.com/pricing - Trail Brain plan pricing for the Graft column's pricing cell
- https://hn.algolia.com/api/v1/items/49299985 - the launch thread grounding the Graft column's vendor-run-benchmark caveat
- https://github.com/oraios/serena - the Serena column: tool surface, backends, licensing, adoption (as of 2026-10-04)
- https://raw.githubusercontent.com/oraios/serena/main/LICENSE - the per-component license behind the Serena column's open-source cell
- https://api.github.com/repos/dzhng/jevgrep - the Jevgrep column: repository stats and activity (as of 2026-10-07)
- https://raw.githubusercontent.com/dzhng/jevgrep/main/README.md - the Jevgrep column: architecture, benchmark claims, and provider dependency
- https://github.com/upstash/context7 - the Context7 column: repository, install modes, and delivery surfaces (as of 2026-10-07)
- https://context7.com/plans - the Context7 column: tier table, call quotas, and overage rates
- https://github.com/headroomlabs-ai/headroom - the Headroom column: repository, deployment surfaces, and license (as of 2026-10-07)
- https://docs.headroomlabs.ai/docs - the Headroom column: compression table and seeded benchmark table
- https://github.com/toon-format/toon - the TOON column: repository and design rationale (as of 2026-10-07)
- https://raw.githubusercontent.com/toon-format/spec/HEAD/SPEC.md - the TOON column: spec version 4.3 and conformance requirements
