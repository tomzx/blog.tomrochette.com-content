---
title: Local Deep Research
created: 2026-10-07
updated: 2026-11-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, open-source, deep-research, local-first]
readability: 3
audience_notes: >
  Engineers who want a Deep Research-class literature loop they can self-host, and researchers comparing local-first agent stacks.
  Assumes you know what a search agent and a local LLM runtime are.
---

Local Deep Research (LDR) is an MIT-licensed, local-first research agent that runs an agentic search loop across web, academic, and private-document sources and returns cited reports, entirely on hardware and models you control.

**LDR is the self-hostable counterpart this category's product tier never had: the same search-and-synthesize loop as OpenAI Deep Research, but the engines, the models, and the encrypted index all stay on your side of the network, and its headline benchmark claim ships with the contamination caveats printed next to it.**

## What it is

A Python web application with a REST API, an MCP server, and a Docker image, built by LearningCircuit and its community contributors, installable from PyPI or Docker Hub.
The loop works in two modes: quick pipeline strategies for fast answers, and a LangGraph agent strategy where the LLM decides what to search, which engines to use (arXiv, PubMed, Semantic Scholar, Wikipedia, SearXNG, GitHub, the Wayback Machine, The Guardian, Wikinews), and when to synthesize.
Premium engines (Tavily, Google via SerpAPI, Brave) plug in with your own API keys, and local documents or any LangChain retriever join the same search surface.
Every session's sources can be downloaded into a SQLCipher-encrypted local library, where they are extracted, indexed, and searchable, so later runs combine your own corpus with the live web.
Around the loop sit a journal-quality system scoring 212K-plus indexed sources with predatory-journal detection (OpenAlex and DOAJ data), scheduled research digests, and PDF or Markdown export.

## Status

Active and heavily developed: 9,192 stars as of 2026-10-15, 890 forks, created 2025-02-09, last pushed 2026-11-08 on the same many-commit daily cadence (the November 7-8 post-release batch links research notifications to the results page, rejects active challenge pages before citation extraction, validates and retains FAISS segments through in-flight searches, adds a folder picker for collection uploads, and bumps oauthlib for CVE-2026-49272), following the November 5-6 batch's migration-marker and theme-persistence fixes, the November 2-5 batch's security and cache hardening (the benchmark grader's endpoint key bound to its origin, inbound WebSocket message size capped at the transport, response nonces required for template scripts and styles, the research cache keyed by chunk row identity with FAISS segments verified on every read, a gap-free migration chain enforced by test, and settings-recovery help in the web UI), the October 26-28 batch's DOI resolution to open-access copies before declaring paywall, LaTeX and BibTeX URL userinfo stripping, a shared dark theme default, worker-owned RAG preparation sessions, and stale download-claim recovery, and capped by the v2.0.0 release published the evening of November 7 (PyPI 20:01 UTC, GitHub 20:10 UTC), the October 18 version bump come to publication and the project's first major-version cut: the web layer rebuilt on FastAPI and Uvicorn, security hardening across the app, new search engines, a Stop control that interrupts research mid-generation, 1,010 commits over ten weeks from 40 contributors (31 new to the project), and a breaking database migration the release notes warn about, v1.10.7 unable to open upgraded data, as of 2026-11-08.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=LearningCircuit/local-deep-research&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=LearningCircuit/local-deep-research&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=LearningCircuit/local-deep-research&type=date&legend=top-left" />
</picture>

The March 2025 launch thread reached 190 points and 34 comments on Hacker News.
The project's headline benchmark is self-reported through community channels: about 95.7 percent SimpleQA (287 of 300) and 77 percent xbench-DeepSearch (77 of 100) with Qwen3.6-27B on a single RTX 3090 using the LangGraph agent strategy, published as a Hugging Face community dataset the README calls the first fully local result at that level.

## Strengths

- Privacy-first by construction: local models, an encrypted library, and a stated policy of respecting robots.txt with no anti-detection fetching.
- Model-agnostic and engine-agnostic (Ollama, LM Studio, llama.cpp, or cloud APIs over ten-plus engines), so neither a model vendor nor a search vendor locks the loop in.
- The benchmark dataset is public and community-maintained, with per-model, per-engine, and per-strategy breakdowns anyone can extend.
- The MCP server and REST API make the loop callable from other agents, and the LangGraph strategy is a legible worked example of agentic search routing.
- The README now documents a per-run egress scope system: Private only mode forces local inference and refuses cloud providers, Strict arms a best-effort socket-level guard, and the guarded HTTP layer checks destinations against SSRF rules, a plainly stated account of the boundary the privacy story rides on.

## Cautions

- The headline numbers are self-reported community benchmarks, and the README itself flags small samples, LLM-grader noise, and SimpleQA contamination risk on newer base models.
- No machine judge sits inside the loop: the output is prose with citations, so the human stays the verifier, exactly as with Deep Research.
- 1,385 open issues and pull requests as of 2026-11-07 against a volunteer contributor base signals a project where support lags feature growth.
- Attaching premium engines or cloud models reintroduces the external calls the privacy story avoids, one API key at a time.

## Pricing

Free and open source under MIT; there is no paid tier, so pricing does not apply.
Costs are your own hardware plus any premium search-engine keys or cloud model APIs you attach.

## Compared to

- [OpenAI Deep Research](../openai-deep-research/index.md): the closed product tier; choose LDR for privacy, local models, and your own document index, Deep Research for zero-setup breadth.
- [OpenResearch](../openresearch/index.md): the other loop that runs on your own machine; OpenResearch executes code experiments with git lineage, LDR synthesizes literature with citations.
- [Agon](../agon/index.md): the producer-critic loop toward papers and experiments; LDR is the literature-synthesis tier without the code-execution half.

## Bottom line

**Recommended for engineers who want a Deep Research-class literature loop that never leaves their hardware, and for agent builders who want a working LangGraph search-routing loop to read and copy.**
Not for anyone who needs machine-verified output or turnkey support: the loop ends in prose a human must check, and the benchmark claims rest on the community's own graders, as of 2026-10-07.

## Changes

- 2026-10-07 - Created.
- 2026-10-12 - Refreshed the volatile counts (stars, forks, the October 12 push) and the open-issue count.
- 2026-10-18 - Recorded the main-branch version bump to 2.0.0, the project's first major-version cut, which had not reached GitHub releases or PyPI as of this run.
- 2026-11-07 - Rotation re-verification: all cited URLs re-fetched and live, with the benchmark rows (95.7 percent SimpleQA, 77 percent xbench-DeepSearch), the 190-point launch thread, and the v1.10.7 release and PyPI freeze all confirmed unchanged and 2.0.0 still unreleased; recorded the November 5-6 commits, the README's new egress-scope documentation, and the open-issue count moved to 1,385.
- 2026-11-08 - Recorded the v2.0.0 release, published the evening of November 7 on PyPI and GitHub hours after that morning's verification: the FastAPI and Uvicorn web-layer rebuild, app-wide security hardening, new search engines, mid-generation Stop, 1,010 commits over ten weeks from 40 contributors (31 new), and the breaking database migration that leaves v1.10.7 unable to open upgraded data; the release-freeze line recorded the same morning is closed, and the November 7-8 commits continue post-release fixes.

## See also

- [OpenAI Deep Research](../openai-deep-research/index.md) - the closed product counterpart this note mirrors at the self-hosted tier
- [OpenResearch](../openresearch/index.md) - the other local-first loop on your machine, code experiments instead of literature
- [Agon](../agon/index.md) - the paper-producing loop whose deep-literature stage LDR productizes
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/LearningCircuit/local-deep-research - repository, description, and MIT license (fetched 200, 2026-11-07)
- https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/README.md - the loop, strategies, engines, the egress-scope system, the benchmark table with its own caveats, the journal-quality system, and the MCP server (fetched 200, 2026-11-07)
- https://api.github.com/repos/LearningCircuit/local-deep-research - stars, forks, created and push dates, open-issue count, and license for the as-of status (fetched 200, 2026-11-07)
- https://api.github.com/repos/LearningCircuit/local-deep-research/releases?per_page=3 - v1.10.7 (2026-08-28) the latest published release at the 2026-11-07 re-fetch; superseded the same evening by v2.0.0 (fetched 200, 2026-11-07)
- https://api.github.com/repos/LearningCircuit/local-deep-research/releases/tags/v2.0.0 - the v2.0.0 release notes (published 2026-11-07 20:10 UTC): the FastAPI and Uvicorn rebuild, 1,010 commits from 40 contributors, the upgrade and rollback warnings, and the v1.10.7 incompatibility with upgraded databases (fetched 200, 2026-11-08)
- https://pypi.org/pypi/local-deep-research/json - the published version 1.10.7 at the 2026-11-07 re-fetch and 2.0.0 uploaded 2026-11-07 20:01 UTC, license metadata, and Python requirement (fetched 200, 2026-11-07 and 2026-11-08)
- https://huggingface.co/datasets/local-deep-research/ldr-benchmarks - the community benchmark dataset behind the SimpleQA and xbench-DeepSearch numbers (fetched 200, 2026-11-07)
- https://hn.algolia.com/api/v1/items/43330164 - the 190-point, 34-comment launch thread from March 2025 (fetched 200, 2026-11-07)
