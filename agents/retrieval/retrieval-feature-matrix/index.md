---
title: "Retrieval Feature Matrix"
created: 2026-08-24
updated: 2026-10-06
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, comparison, retrieval, rag, code-retrieval, llm=glm-5.3-flash]
readability: 3
audience_notes: >
  Engineers choosing between retrieval frameworks, shipped semantic search, and chunking strategies for agentic coding.
  Assumes you know what embeddings, vector stores, and RAG mean; each column links to a full note with sources.
---

This matrix compares the nine retrieval entries profiled in this section, two frameworks, two patterns, one chunking library, two document-parsing pipelines, one self-hosted code-index engine, and one embeddable search-engine library, feature by feature, so the shortlisting step does not require reading nine notes.

**Both frameworks are pivoting away from retrieval as their business, both patterns are being demoted by the tools that ship them, and the chunking library that won the niche has outlived its own maker's attention, which I read as evidence that the agent loop, not the index, is now the retrieval layer, while the Knowhere column bets against that demotion by selling structure-preserving parsing as a hosted service, the open-codebase-index column bets the same way from the self-hosted side, and neither bet has independent validation yet.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [Chonkie](../chonkie/index.md) | [Docling](../docling/index.md) | [Knowhere](../knowhere/index.md) | [LangChain](../langchain/index.md) | [LlamaIndex](../llamaindex/index.md) | [open-codebase-index](../open-codebase-index/index.md) | [Orama](../orama/index.md) | [Semantic code search](../semantic-code-search/index.md) | [Tree-sitter chunking](../tree-sitter-chunking/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | chunking library | document parsing library (PDF, Office, audio, video to structured output) | hosted document-parsing pipeline plus OSS engine | agent framework | retrieval framework | self-hosted code-index engine (MCP and plugin) | embeddable search-engine and RAG library (full-text, vector, hybrid) | shipped capability | parsing technique |
| Open source license | ✓ MIT | ✓ MIT | ~ Apache-2.0 engine and self-hosted stack, hosted API proprietary | ✓ MIT | ✓ MIT | ✓ MIT | ✓ Apache-2.0 text, GitHub detects NOASSERTION | ~ tool-dependent | ✓ MIT parsers |
| Primary language | Python, TypeScript port | Python | Python | Python | Python | TypeScript plus Rust native module | TypeScript | ~ varies by tool | C11 core |
| Code-specific focus | ~ general text, one code chunker | ✗ documents, not code | ✗ documents (PDFs, decks, spreadsheets), not code | ~ generic text RAG | ~ general data, code capable | ✓ code only | ✗ general text, not code | ✓ code only | ✓ code only |
| AST-aware code splitting | ✓ CodeChunker | ✗ document layout models, not AST | ✗ document hierarchy, not AST | ✗ separators only | ✓ CodeSplitter | ✓ tree-sitter chunking built in | ✗ schema-and-tokenizer indexing | ? chunkers undisclosed | ✓ the technique |
| Hosted or commercial arm | ✗ hosted API dead, OSS only | ~ Docling for IBM watsonx managed path, no published prices | ✓ the hosted per-page API is the funnel | ✓ LangSmith SaaS | ✓ LlamaParse SaaS | ✗ fully local, bring your own embedding provider | ✗ OSS only, no paid tiers surfaced | ~ plan-gated indexes | ✗ was Chonkie Cloud, now dead |
| Positioning drift in the notes | ~ maker moved to Feyn Labs, OSS continues | ✗ new entrant (2026-09 scan), no drift yet | ✗ new entrant (2026-09), no drift yet | ~ climb to agent platform | ~ pivot to document OCR | ✗ new entrant (2026-10 scan), no drift yet | ✗ new entrant (2026-10-06 scan), no drift yet | ~ demoted to optional | ~ outsourced to Chonkie |
| Maintenance status | ✓ active, 4.78k stars, 1.24M downloads/month | ✓ active, 68.4k stars, 2.83M downloads/month, PyPI 2.133.0 | ✓ active, 3.66k stars, v1.2.22 (2026-10-05) | ✓ active, 147.5k stars | ✓ active, 52.4k stars | ✓ active, 215 stars, 6.3k downloads/month, npm 0.35.2 (2026-10-05) | ~ slowing, 10.57k stars, 1.51M downloads/week, v3.1.18 (2025-12-19), last main commit 2026-07-03 | ~ active but demoted | ✓ mature, pervasive |
| Displacement signal in the notes | ~ founder pivoted away, niche commoditized | ~ none yet; the heavyweight torch dependency is the standing complaint | ~ stars ran ahead of any discussion, two Show HNs, 2 points combined | ~ retrieval commoditized | ~ agentic search eats indexed RAG | ~ zero discussion so far, installs lead stars | ~ installs far outrun discussion, 1-point 2023 HN story, stale unscoped npm name | ✓ pioneers shipped grep loops, Cursor's docs dropped embeddings | ~ ranked below truncation |
| What it replaces in a coding-agent stack | framework text splitters | hand-rolled PDF and Office extraction | hand-rolled OCR plus vector-store parsing | hand-rolled agent loops | hand-rolled retrievers | hand-rolled code RAG pipelines | a hosted search dependency or hand-rolled inverted index in JS/TS apps | grep-only lookups | line-count chunking |

## Reading the matrix

**The two frameworks are the healthiest entries and the least committed to retrieval: the giants of the category are both diversifying away from the job you would hire them for.**
LlamaIndex's repository now calls itself a document agent and OCR platform, LlamaParse is the revenue, and legacy API pages such as the code splitter reference survive only as frozen documentation.
LangChain repositioned as an agent engineering platform with its own terminal coding agent, and my own call in its note is to stop picking it purely for RAG.
Chonkie completes the pattern from the other side: the library the frameworks outsource chunking to is still maintained and pulling over a million downloads a month, but its maker's domain now redirects to the founder's next venture and the paid API is dead.

**Knowhere is the column betting against the demotion pattern: where every drift row above demotes local indexes, it sells parsing and structuring as a hosted, per-page service and hands the structured result to agents through MCP, which makes it the enterprise-bet side of the thesis made concrete.**
Its own note carries the counter-signal, 3.66k stars behind two Show HNs with two combined points and a marketing benchmark that is entirely self-reported, so I would pilot it on your worst documents before believing any number on its site.

**open-codebase-index makes the same bet from the self-hosted side, and it is the counterexample that keeps the thesis arguable: a local embeddings-plus-BM25-plus-call-graph index served over MCP while Cursor strips embeddings from its own docs.**
Its counter-signal is a 215-star repo with zero independent discussion behind 6,252 monthly npm installs as of 2026-10-05, so the capability is being used even though nobody is arguing about it in public.

**Orama is the in-process counterfactual to the whole demotion story: search that never leaves your JavaScript process, installed 1.51M times a week, and quietly losing its maintainers anyway.**
Its cells say two things at once, 10.57k stars and a stalled release train (v3.1.18 of 2025-12-19), and its name collision with an unrelated 2018 React-charts npm package means half the people who search for it install the wrong thing.

**The pattern columns carry the shipped verdict: semantic indexes are being demoted inside the tools that pioneered them, and the chunking strategy called most exact is ranked last by the practitioners who documented their pipeline.**
Cursor's retrieval docs lead with Instant Grep and an Explore subagent, Continue deprecated its `@Codebase` embeddings provider, and VS Code ships a no-index fallback.
Continue's custom code RAG guide ranks truncation and fixed-length chunking above AST chunking because a 16k-token embedding model fits most whole files.

**The context-management-patterns essay argues that harness-native features beat bespoke RAG below a few hundred thousand lines of code, and this matrix is that claim's evidence table.**
Every drift row points the same direction, and the essay's Sourcegraph data (a negative reward delta below 400K LOC from the vendor's own benchmark) sets the threshold.
The live counterargument sits in the commercial-arm row: Devin Desktop doubles down on a RAG context engine and VS Code moved its index to the GitHub platform, so indexed retrieval may survive as an enterprise service even as local indexes disappear.

**Code-specific machinery is thinnest exactly where you would buy it: the biggest framework offers separator-based splitting only, and the deepest AST chunking route runs through a library whose commercial arm just died.**
LangChain's text splitters catalog has no AST chunker at all.
LlamaIndex's newer Chunker node parser wraps Chonkie rather than reimplementing chunking, which tells you where maintainers think the effort should live, and with Chonkie Cloud dead that route is now open source or nothing.

## Choosing from the matrix

- Ingestion-heavy document RAG across many formats: LlamaIndex, pricing LlamaParse only if you want the maintained parsing.
- Multi-provider agent systems that also need retrieval: LangChain plus LangSmith, accepting generic text splitters.
- Want concept lookup in an editor today: use the shipped semantic search where present, but keep a grep-first workflow; do not design around the index existing.
- Building your own code RAG: start with truncation and fixed-length chunking, and adopt tree-sitter chunking only when measurements on your corpus earn the complexity.
- Need a chunker beyond truncation for document RAG: Chonkie, free and maintained, accepting that its hosted API is gone and roadmap risk comes from a pivoted maker.
- RAG over dirty PDFs and decks with no parsing team to maintain: Knowhere, paying per page and spending the free credit on your worst documents first, while treating its self-reported benchmark as marketing until an independent run exists.
- Want semantic code search without trusting a vendor index: open-codebase-index behind your harness's MCP or plugin config, pinning a version and accepting that nothing independent validates its retrieval yet.
- Need full-text or hybrid search inside a JS/TS app or edge function with no server: Orama, accepting the stalled release train and the npm name collision.
- Repo below a few hundred thousand lines: skip the category and learn compaction, subagents, and memory files first.
- Past that threshold: build on framework machinery or a dedicated chunker, and deliver the index to your harness via MCP.

## Changes

- 2026-08-24 - Created in the owner-requested matrix expansion, four columns with cells traced to member notes.
- 2026-08-26 - Fixed a self-contradiction about the legacy LangChain code-splitter docs, reworded as frozen documentation.
- 2026-08-30 - Re-sorted columns alphabetically with LangChain first per the new owner rule, and repaired the tags-line YAML the sort broke.
- 2026-09-16 - Extended from four to five columns with Chonkie, corrected the tree-sitter hosted-arm cell now that Chonkie Cloud is dead, and updated the thesis, reading, and choosing prose for the library column.
- 2026-09-18 - Refreshed the maintenance row numbers for the 2026-09-18 re-verification: Chonkie 4.76k stars and 1.08M downloads/month, LangChain 146.6k stars, LlamaIndex 52.2k stars.
- 2026-09-20 - Extended from five to six columns with Knowhere, refreshed the Chonkie downloads and LangChain stars cells, and extended the thesis, reading, and choosing prose for the hosted-parsing column.
- 2026-09-21 - Refreshed the maintenance row: Knowhere to 3.41k stars and release v1.2.15, Chonkie downloads to 1.02M, LangChain stars to 146.8k, and LlamaIndex stars to 52.3k.
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-25 - Refreshed the maintenance row: Chonkie 4.77k stars and 1.14M downloads/month, Knowhere 3.49k stars and release v1.2.17 (2026-09-23), LangChain 147.0k stars.
- 2026-09-27 - Refreshed the maintenance row: Knowhere to 3.53k stars, with release v1.2.17 unchanged, and aligned the reading prose to the same figure.
- 2026-09-27 - Repaired the intro and thesis prose left stale by the 2026-09-27 Docling column: the count now reads seven entries and the hosted-parsing bet is attributed to Knowhere by name rather than as the newest column.
- 2026-10-02 - Refreshed the maintenance row: Chonkie 4.78k stars, Docling 68.3k stars and PyPI 2.132.0, Knowhere 3.61k stars and release v1.2.20 (2026-09-30), LangChain 147.4k stars, LlamaIndex 52.4k stars.
- 2026-10-05 - Extended from seven to eight columns with open-codebase-index, sorted between LlamaIndex and Semantic code search; the maintenance row refreshed (Docling 68.4k stars and 2.83M downloads/month, Knowhere 3.66k stars and v1.2.22 of 2026-10-05, LangChain 147.5k stars), and the Cursor reference corrected, that page no longer documenting the encrypted-embeddings index.
- 2026-10-06 - Extended from eight to nine columns with Orama, sorted between open-codebase-index and Semantic code search, with its license-detection quirk, stalled release train, and npm name collision folded into the cells and the reading prose.

## See also

- [Context Management Patterns](../../context-management-patterns/index.md) - the size-threshold argument this matrix leans on
- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - the terminal agents that consume all of this retrieval
- [Surface Feature Matrix](../../surfaces/surface-feature-matrix/index.md) - the editors shipping or dropping these indexes
- [Aider](../../harnesses/aider/index.md) - the no-embeddings counterexample via graph-ranked repo maps

## References

- https://github.com/chonkie-inc/chonkie - repository facts for the Chonkie column (4,783 stars, MIT, pushed 2026-10-03; the canonical home is feyninc/chonkie, this URL redirects) (GitHub API, as of 2026-10-05)
- https://github.com/Ontos-AI/knowhere - repository, tracks, and MCP server for the Knowhere column (3,661 stars, Python, Apache-2.0, pushed 2026-10-05, as of 2026-10-05)
- https://docs.knowhereto.ai/pricing - the per-page pricing behind the Knowhere commercial-arm cell
- https://docs.knowhereto.ai/mcp - the parse, list, outline, grep, and retrieval tools behind the Knowhere column's agent-facing surface
- https://hn.algolia.com/api/v1/items/49738595 - the September 2026 Show HN grounding the Knowhere missing-discussion cell
- https://raw.githubusercontent.com/chonkie-inc/chonkie/main/README.md - chunker table (CodeChunker, FastChunker) and the self-hosted API server for the Chonkie column
- https://pypistats.org/api/packages/chonkie/recent - 1,241,047 downloads last month for the maintenance row, as of 2026-10-04
- https://usefeyn.com - the Feyn Labs founder letter behind the chonkie.ai redirect, grounding the maker-moved-on cells
- https://github.com/run-llama/llama_index - repository scale, MIT license, and the document-agent and OCR pivot wording for the LlamaIndex column
- https://www.llamaindex.ai/pricing - LlamaParse tiers grounding the commercial-arm row
- https://github.com/langchain-ai/langchain - repository scale, MIT license, and agent-platform positioning for the LangChain column
- https://python.langchain.com/api_reference/text_splitters/text_splitters/code_splitter.html - separator-based code splitting only, grounding the AST row
- https://cursor.com/docs/context/codebase-indexing - retitled Search: Instant Grep first, local index, and the statement that no codebase embeddings are stored, for the semantic search column
- https://docs.continue.dev/reference/deprecated-codebase - the deprecated local embeddings pipeline for the displacement row
- https://docs.continue.dev/guides/custom-code-rag - the chunking strategy ranking (truncate, fixed-length, AST) for the tree-sitter column
- https://tree-sitter.github.io/tree-sitter/ - parser properties (incremental, error-robust, C11) for the technique column
- https://github.com/Helweg/open-codebase-index - repository facts for the open-codebase-index column (215 stars, MIT, pushed 2026-10-05, 961 commits) (GitHub API, as of 2026-10-05)
- https://raw.githubusercontent.com/Helweg/open-codebase-index/main/docs/tools.md - the host surface matrix (16 portable tools, 3 knowledge-base tools, 5 prompts) behind the new column
- https://api.npmjs.org/downloads/point/last-month/open-codebase-index - 6,252 downloads last month behind the maintenance cell, window 2026-09-04 to 2026-10-03
