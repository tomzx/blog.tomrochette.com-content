---
title: PrivateGPT
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, assistant-runtimes, self-hosting, api-first, rag]
readability: 3
audience_notes: >
  Developers building private AI applications on local models, who need a backend layer above
  an inference server, and anyone tracking how a company can fund an open-source project after a quiet period.
---

PrivateGPT is the Apache-2.0 API layer from Zylon that sits above any OpenAI-compatible local inference server and exposes Claude-style application primitives: messages, file ingestion, retrieval with citations, tools, MCP, database and CSV access, and embeddings.

**PrivateGPT's 57k stars measure the 2023 "chat with your documents" demo, but the project is no longer that app: 1.0 (June 2026) rebuilt it as developer infrastructure, and the open question is whether infrastructure can inherit a demo's audience.**

## What it is

PrivateGPT does not run models; it connects to Ollama, llama.cpp, vLLM, or any server implementing the OpenAI chat endpoints, installable via a Homebrew tap or a uv tool install.
The API is the product: standard messages with streaming and async, token counting, artifact ingestion, agentic RAG with citations, built-in web search, web fetch, and code execution tools, custom tools, MCP connectors, and structured database and CSV access.
Integration guides cover Claude Code, Claude Desktop and Cowork, Claude for Microsoft 365, and OpenCode, with n8n, OpenClaw, and Hermes Agent named as API consumers.
A workbench UI ships at /ui, but the docs are explicit that it is a demonstrator and the API is the actual product.
The compatibility table against the Claude API is candid: skills are basic, prompt caching and OAuth are missing, and structured outputs are inference-dependent.
Commercially, Zylon builds the enterprise platform on top: an on-premise, air-gapped AI infrastructure for regulated industries with fixed pricing, connectors, and governance.

## Status

Alive again after a long quiet stretch: 57,556 stars, 7,621 forks, and 15 open issues as of 2026-10-06, created 2023-05-02, pushed 2026-10-06.

<a href="https://www.star-history.com/?repos=zylon-ai%2Fprivate-gpt&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=zylon-ai/private-gpt&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=zylon-ai/private-gpt&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=zylon-ai/private-gpt&type=date&legend=top-left" />
 </picture>
</a>

The project went viral in May 2023 with a 520-point Hacker News thread as the original offline document chat.
**Then came the fork gap: the v1.0.0 release notes state the release merges two years of work from a private fork, which is a direct admission that the public repo lagged while Zylon built commercially.**
v1.0.0 shipped 2026-06-03 with a breaking API change, v1.0.1 followed on 2026-06-18, and no release has shipped since, though main is active.
Fifteen open issues on a project this size is unusually low, which I read as issue hygiene rather than an absence of bugs.
The same notes say Zylon closed its private fork and now develops against the open repository, which is the commitment to watch.

## Strengths

- The only project in this wing that treats a local AI backend as an API contract rather than an app, which is what builders actually need.
- Apache-2.0 with no branding strings, the cleanest license of the three local-first platforms.
- Model-server agnosticism means your inference choice stays yours.
- Company-funded development now flows publicly, and the Claude API compatibility matrix gives a concrete mental model.

## Cautions

- Two years of private-fork history means the community should verify, not assume, that public development stays first-class.
- The 1.0 breaking change orphans the 2023-era tutorials that most of the star history was built on.
- The workbench UI is deliberately not a finished product, so anyone wanting an app today should look elsewhere in this category.
- The project's own launch-thread comments are a reminder of the ceiling: local models of that era were far behind cloud quality, and retrieval quality depends heavily on document preparation.
- Zylon's marketing claims about use by Google, Meta, and J.P. Morgan are unaudited.

## Pricing

Free and open source under Apache-2.0, self-hosted against your own inference server.
Zylon, the commercial platform built on it, is sold through demos and contact sales with no public price.

## Compared to

- [Open WebUI](../open-webui/index.md): app-first chat and administration versus API-first building blocks, a distinction PrivateGPT's own docs draw; choose Open WebUI to give people an interface, PrivateGPT to give developers a backend.
- Ollama and friends: the inference layer below it; they answer how to run a model, PrivateGPT answers how to build on one, and you use them together.
- [AnythingLLM](../anything-llm/index.md): a finished workspace versus a raw API; choose AnythingLLM for out-of-the-box use, PrivateGPT when the product is yours to write.

## Bottom line

**Recommended for developers building their own private AI application surface on local models who are comfortable wiring an API.**
Not for anyone who wants a finished chat UI today.
The disagreeable claim I will defend: the star count is a museum of the 2023 demo, and I would trade most of those stars for 5,000 active users of the 1.0 API, because the mismatch between an audience and a product direction nearly killed this project once already.

## Changes

- 2026-09-27 - Created when the owner's GitHub-stars scan surfaced it.
- 2026-10-07 - Added the zylon-ai/private-gpt star history chart to the Status section.

## See also

- [OpenClaw](../openclaw/index.md) - the messaging-first assistant PrivateGPT lists as an integration target
- [Hermes](../hermes/index.md) - the other agent runtime PrivateGPT's README names as a consumer of the API
- [Open WebUI](../open-webui/index.md) - the app-first counterpart its docs position against
- [LangChain](../../retrieval/langchain/index.md) - the framework-style building blocks PrivateGPT productizes into an API

## References

- https://github.com/zylon-ai/private-gpt - README: architecture, Claude API compatibility, Zylon relationship, history
- https://api.github.com/repos/zylon-ai/private-gpt - stars, forks, issues, license, and dates as of 2026-10-06
- https://api.github.com/repos/zylon-ai/private-gpt/releases?per_page=4 - v1.0.0 notes (two-year private-fork merge, breaking change, Zylon developing in the open) and v1.0.1
- https://docs.privategpt.dev/ - the API-first positioning and the Claude API compatibility table
- https://www.zylon.ai/ - the company, on-premise positioning, and lineage claims, fetched 2026-09-27
- https://news.ycombinator.com/item?id=36024503 - the 2023 viral thread (520 points), the critical source on the local-quality gap, fetched via the Algolia items API
