---
title: Open WebUI
created: 2026-09-27
updated: 2026-09-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, assistant-runtimes, self-hosting, rag, licensing]
readability: 3
audience_notes: >
  Engineers choosing the front end for a self-hosted Ollama or OpenAI-compatible stack, who need to know
  exactly what the license restricts before the deployment spreads through their organization.
---

Open WebUI is the self-hosted web interface (and now platform) for local and OpenAI-compatible models, created by Timothy Jaeryang Baek, installable via pip, Docker, or Kubernetes, and extensible through plugins, MCP tool servers, and a growing companion ecosystem.

**Open WebUI is the most feature-complete self-hosted AI interface in this category and the one whose license you must read before adopting: since v0.6.6 (2025-04-19) it is not open source by the OSI definition, and it was the project's second license change in five months.**

## What it is

A Python backend with a SvelteKit frontend that connects to Ollama or any OpenAI-compatible API (LM Studio, vLLM, OpenRouter, Groq, and more).
Retrieval is deep: nine vector database options, hybrid BM25 plus vector search with reranking, dozens of web search providers, and OCR-backed document ingestion.
The surface is ChatGPT-like chat plus multi-model conversations, persistent memory, notes, shared channels, calendars, and scheduled automations.
Administration is where it separates from hobbyist UIs: granular RBAC, LDAP, SSO, SCIM provisioning, usage analytics, OpenTelemetry, and Redis-backed horizontal scaling.
Extensibility runs through Filters, Actions, Pipes, Tools, and Skills plugins, MCP via MCPO and OpenAPI tool servers, and agent models that wrap a base model with instructions, knowledge, and tools.
The ecosystem now includes a native desktop app, an Open Terminal sandboxed execution environment, an Open WebUI Computer companion agent, and oikb knowledge base sync.

## Status

Very active and huge for the category: 153,268 stars, 22,427 forks, and 324 open issues as of 2026-09-27, created 2023-10-06, pushed 2026-09-26.
Releases are frequent: v0.11.4 shipped 2026-09-21 (notably a much slimmer Docker image), v0.11.3 and v0.11.2 on 2026-08-31, and v0.11.1 on 2026-08-25.
The README now markets it as "a home for AI" rather than a UI, which matches the expansion into the desktop app, Open Terminal, Computer, and knowledge base sync.
**The license history is the defining fact: MIT until December 2024, BSD-3 until v0.6.5, then the custom Open WebUI License from v0.6.6, which forbids removing or altering the branding unless you stay at or below 50 users in any 30-day window, are a substantive contributor with written permission, or buy an enterprise license, with a CLA required for new contributions.**
The project's own license FAQ concedes the license is not OSI-approved.
Code through v0.6.5 remains BSD-3, and the maintainers point anyone who objects to forking from that tag.
The change drew a 73-point, 59-comment Hacker News thread in May 2025 that remains the best critical record.

## Strengths

- No self-hosted rival matches the end-to-end checklist: RAG, tools, agents, admin, auth, observability, and scaling in one deploy.
- Deployment flexibility from a single pip install to Helm charts, plus a desktop app and PWA.
- The MCP and plugin surface means most integrations are configuration, not forks.
- The enterprise feature set (SCIM, LDAP, audit-friendly auth) is real rather than roadmap.

## Cautions

- Read the license before a company-wide rollout: the branding clause and CLA change what adoption means past 50 users.
- Two license changes in five months is a signal about direction, regardless of how you rate the current terms.
- The Docker images were famously enormous, a complaint visible in the license thread, and the slim image only landed in v0.11.4.
- The moat question from that thread is fair: at bottom it is a web app over provider APIs, and competitors now market themselves explicitly as alternatives to it.

## Pricing

Free to self-host under the Open WebUI License, provided the branding stays visible or you remain within the 50-user window.
Enterprise licenses that permit white-labeling and rebranding are sold through contact sales, with no public price.

## Compared to

- [AnythingLLM](../anything-llm/index.md): MIT, desktop-first, built to hide the machinery from non-engineers; choose it for zero-friction local workspaces, Open WebUI for depth and administration.
- [Eigent](../eigent/index.md): Apache-2.0 Electron desktop for supervised multi-agent work; choose it when agents, not chat, are the product.
- LibreChat: MIT-licensed and named in the license thread as the migration path for teams that cannot accept the branding clause.

## Bottom line

**Recommended as the feature-maximal self-hosted interface for individuals and teams under the 50-user threshold who will keep the branding.**
Not for organizations that need to rebrand, or that treat OSI-approved licenses as procurement policy.
The disagreeable claim I will defend: most of the license outrage is disproportionate to the clause, because for a single engineer the branding requirement changes nothing, and Open WebUI is still the right default for personal self-hosting.

## Changes

- 2026-09-27 - Created when the owner's GitHub-stars scan surfaced it.

## See also

- [Assistant Runtimes Feature Matrix](../assistant-runtimes-feature-matrix/index.md) - the category comparison this note joins
- [AnythingLLM](../anything-llm/index.md) - the MIT desktop-first rival for local workspaces
- [Eigent](../eigent/index.md) - the permissively licensed multi-agent desktop
- [LangChain](../../retrieval/langchain/index.md) - the RAG building blocks Open WebUI packages behind its UI

## References

- https://github.com/open-webui/open-webui - README: features, ecosystem, install paths, license section
- https://api.github.com/repos/open-webui/open-webui - stars, forks, issues, and dates as of 2026-09-27
- https://api.github.com/repos/open-webui/open-webui/releases?per_page=4 - v0.11.4 (2026-09-21) back to v0.11.1 (2026-08-25)
- https://docs.openwebui.com/license/ - the branding clause, the 50-user threshold, the CLA, the fork-from-v0.6.5 path, and the non-OSI admission
- https://news.ycombinator.com/item?id=43901575 - the BSD-3 to Open WebUI License thread (73 points, 59 comments), the critical source
- https://hn.algolia.com/api/v1/search?query=%22Open+WebUI%22&tags=story&hitsPerPage=8 - the thread landscape, including the 101-point "OSS Alternative to Open WebUI" competitor story
