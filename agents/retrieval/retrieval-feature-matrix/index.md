---
title: "Retrieval Feature Matrix"
created: 2026-08-24
updated: 2026-09-21
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, comparison, retrieval, rag, code-retrieval, llm=glm-5.3-flash]
readability: 3
audience_notes: >
  Engineers choosing between retrieval frameworks, shipped semantic search, and chunking strategies for agentic coding.
  Assumes you know what embeddings, vector stores, and RAG mean; each column links to a full note with sources.
---

This matrix compares the six retrieval entries profiled in this section, two frameworks, two patterns, one chunking library, and one hosted document-parsing pipeline, feature by feature, so the shortlisting step does not require reading six notes.
Everything below was re-verified against the refreshed member notes and live sources on 2026-09-22.

**Both frameworks are pivoting away from retrieval as their business, both patterns are being demoted by the tools that ship them, and the chunking library that won the niche has outlived its own maker's attention, which I read as evidence that the agent loop, not the index, is now the retrieval layer, while the newest column bets against that demotion by selling structure-preserving parsing as a hosted service, with a star count that no independent discussion yet backs.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [Chonkie](../chonkie/index.md) | [Knowhere](../knowhere/index.md) | [LangChain](../langchain/index.md) | [LlamaIndex](../llamaindex/index.md) | [Semantic code search](../semantic-code-search/index.md) | [Tree-sitter chunking](../tree-sitter-chunking/index.md) |
| --- | --- | --- | --- | --- | --- | --- |
| Kind | chunking library | hosted document-parsing pipeline plus OSS engine | agent framework | retrieval framework | shipped capability | parsing technique |
| Open source license | ✓ MIT | ~ Apache-2.0 engine and self-hosted stack, hosted API proprietary | ✓ MIT | ✓ MIT | ~ tool-dependent | ✓ MIT parsers |
| Primary language | Python, TypeScript port | Python | Python | Python | ~ varies by tool | C11 core |
| Code-specific focus | ~ general text, one code chunker | ✗ documents (PDFs, decks, spreadsheets), not code | ~ generic text RAG | ~ general data, code capable | ✓ code only | ✓ code only |
| AST-aware code splitting | ✓ CodeChunker | ✗ document hierarchy, not AST | ✗ separators only | ✓ CodeSplitter | ? chunkers undisclosed | ✓ the technique |
| Hosted or commercial arm | ✗ hosted API dead, OSS only | ✓ the hosted per-page API is the funnel | ✓ LangSmith SaaS | ✓ LlamaParse SaaS | ~ plan-gated indexes | ✗ was Chonkie Cloud, now dead |
| Positioning drift in the notes | ~ maker moved to Feyn Labs, OSS continues | ✗ new entrant (2026-09), no drift yet | ~ climb to agent platform | ~ pivot to document OCR | ~ demoted to optional | ~ outsourced to Chonkie |
| Maintenance status | ✓ active, 4.76k stars, 1.02M downloads/month | ✓ active, 3.46k stars, v1.2.16 (2026-09-21) | ✓ active, 146.9k stars | ✓ active, 52.3k stars | ~ active but demoted | ✓ mature, pervasive |
| Displacement signal in the notes | ~ founder pivoted away, niche commoditized | ~ stars ran ahead of any discussion, two Show HNs, 2 points combined | ~ retrieval commoditized | ~ agentic search eats indexed RAG | ✓ pioneers shipped grep loops | ~ ranked below truncation |
| What it replaces in a coding-agent stack | framework text splitters | hand-rolled OCR plus vector-store parsing | hand-rolled agent loops | hand-rolled retrievers | grep-only lookups | line-count chunking |

## Reading the matrix

**The two frameworks are the healthiest entries and the least committed to retrieval: the giants of the category are both diversifying away from the job you would hire them for.**
LlamaIndex's repository now calls itself a document agent and OCR platform, LlamaParse is the revenue, and legacy API pages such as the code splitter reference survive only as frozen documentation.
LangChain repositioned as an agent engineering platform with its own terminal coding agent, and my own call in its note is to stop picking it purely for RAG.
Chonkie completes the pattern from the other side: the library the frameworks outsource chunking to is still maintained and pulling over a million downloads a month, but its maker's domain now redirects to the founder's next venture and the paid API is dead.

**Knowhere is the column betting against the demotion pattern: where every drift row above demotes local indexes, it sells parsing and structuring as a hosted, per-page service and hands the structured result to agents through MCP, which makes it the enterprise-bet side of the thesis made concrete.**
Its own note carries the counter-signal, 3.46k stars behind two Show HNs with two combined points and a marketing benchmark that is entirely self-reported, so I would pilot it on your worst documents before believing any number on its site.

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

## See also

- [Context Management Patterns](../../context-management-patterns/index.md) - the size-threshold argument this matrix leans on
- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - the terminal agents that consume all of this retrieval
- [Surface Feature Matrix](../../surfaces/surface-feature-matrix/index.md) - the editors shipping or dropping these indexes
- [Aider](../../harnesses/aider/index.md) - the no-embeddings counterexample via graph-ranked repo maps

## References

- https://github.com/chonkie-inc/chonkie - repository facts (4,764 stars, MIT, pushed 2026-09-18) for the Chonkie column (GitHub API, as of 2026-09-21)
- https://github.com/Ontos-AI/knowhere - repository, tracks, and MCP server for the Knowhere column (3,413 stars, Python, Apache-2.0, pushed 2026-09-21, as of 2026-09-21)
- https://docs.knowhereto.ai/pricing - the per-page pricing behind the Knowhere commercial-arm cell
- https://docs.knowhereto.ai/mcp - the parse, list, outline, grep, and retrieval tools behind the Knowhere column's agent-facing surface
- https://hn.algolia.com/api/v1/items/49738595 - the September 2026 Show HN grounding the Knowhere missing-discussion cell
- https://raw.githubusercontent.com/chonkie-inc/chonkie/main/README.md - chunker table (CodeChunker, FastChunker) and the self-hosted API server for the Chonkie column
- https://pypistats.org/api/packages/chonkie/recent - 1,020,031 downloads last month for the maintenance row, as of 2026-09-21
- https://usefeyn.com - the Feyn Labs founder letter behind the chonkie.ai redirect, grounding the maker-moved-on cells
- https://github.com/run-llama/llama_index - repository scale, MIT license, and the document-agent and OCR pivot wording for the LlamaIndex column
- https://www.llamaindex.ai/pricing - LlamaParse tiers grounding the commercial-arm row
- https://github.com/langchain-ai/langchain - repository scale, MIT license, and agent-platform positioning for the LangChain column
- https://python.langchain.com/api_reference/text_splitters/text_splitters/code_splitter.html - separator-based code splitting only, grounding the AST row
- https://cursor.com/docs/context/codebase-indexing - Instant Grep first and encrypted chunks for the semantic search column
- https://docs.continue.dev/reference/deprecated-codebase - the deprecated local embeddings pipeline for the displacement row
- https://docs.continue.dev/guides/custom-code-rag - the chunking strategy ranking (truncate, fixed-length, AST) for the tree-sitter column
- https://tree-sitter.github.io/tree-sitter/ - parser properties (incremental, error-robust, C11) for the technique column
