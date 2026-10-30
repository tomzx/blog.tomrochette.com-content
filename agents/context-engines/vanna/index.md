---
title: Vanna
created: 2026-10-11
updated: 2026-10-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, text-to-sql, rag]
readability: 3
audience_notes: >
  Engineers evaluating text-to-SQL context engines or inheriting a Vanna deployment who need the archive status and what it implies.
  Assumes you know what RAG and a semantic layer are; read with the WrenAI note, the live successor in this category.
---

Vanna is the MIT text-to-SQL framework that retrieves your schema, documentation, and past question-SQL pairs into the prompt so an LLM can answer data questions, the most-starred RAG ancestor of this category's data-semantics engines.

**The status is the story: the 23.8k-star open-source core was archived by its owner on 2026-03-29, seven weeks after the 2.0 rewrite shipped, and the repository is read-only while the company keeps selling Cloud and Enterprise, so the repo most tutorials link is no longer where anything happens.**

## What it is

A Python framework (pip, MIT) by the Vanna AI company, rebuilt in 2.0 as a user-aware agent framework: tools that run SQL and draw charts, user resolvers, row-level security, audit logs, rate limiting through lifecycle hooks, FastAPI routes, and an embeddable `<vanna-chat>` web component.
The context mechanism is Tool Memory: every successful interaction is saved, and similar questions retrieve and adapt the past SQL and tool-usage patterns, so the agent "learns your database schema, business logic, and query patterns without manual training", in the docs' words; 0.x did the same job by training DDL, documentation, and SQL examples into a vector store, and Context Enrichers still take RAG, memory, or documentation.

## Status

Archived upstream, alive commercially: the repository banner reads "This repository was archived by the owner on Mar 29, 2026. It is now read-only", and the API reports archived true with 23,823 stars as of 2026-10-13, 2,549 forks and 289 open issues as of 2026-10-30, last pushed 2026-02-02.
The last PyPI release is 2.0.2 on 2026-02-02 (2.0.0 shipped 2025-11-20; 78 releases total), and issues and discussions are frozen, so bug reports route through the docs and support channels.
The company side is active: vanna.ai, the docs portal, and a three-tier pricing page all fetched unchanged again on 2026-10-30, selling hosted admin features (access control, hosted vector memory, observability, audit logs) on top of the frozen core.
The community footprint is dated but large: a 547-point launch thread on 2024-01-14 and 232 comments made it the reference text-to-SQL-RAG project, and nothing since.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=vanna-ai/vanna&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=vanna-ai/vanna&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=vanna-ai/vanna&type=date&legend=top-left" />
</picture>

## Strengths

- The founding retrieval design is the pattern this category's data columns descend from: DDL, documentation, and question-SQL pairs assembled per query, before "context engine" was the word for it.
- 2.0's Tool Memory is a working context loop, the same retrieve-past-successes mechanism WrenAI ships as worked examples, proven across a 23.8k-star user base.
- The enterprise wiring is named and mechanical (user resolvers, row-level security, audit logs, per-user quotas), which is what data access through an LLM actually requires.
- MIT and self-hostable, so the frozen core still runs and forks remain legal and cheap.

## Cautions

- Archived read-only: no patches, no public issue tracker, and the changelog moved into docs, so the public patch history a security audit needs stops at 2026-02-02.
- CVE-2024-5565 (June 2024): prompt injection through the Plotly chart-generation path reached Python `exec` for remote code execution, and the vendor's answer was a hardening guide, so a deployment inheriting that path inherits the audit.
- Every accuracy claim is vendor-run: the 2023 accuracy study on the company blog is Vanna's own, and no independent benchmark of the Tool Memory loop exists.
- The 2.0 delivery is app-first: end users meet Vanna through its own chat component and your FastAPI routes, with no MCP surface, so as a context engine for agents you already run it is narrower than WrenAI.

## Pricing

The archived MIT core is free and self-hosts without limits.
Hosted admin features are sold per month with question quotas: Explorer $50 (20 questions per day, admin features on OSS or Cloud), Team $500 (300 questions per day, setup and live support), Enterprise custom (unlimited questions, on-prem deployment support, SAML SSO, admin API); annual billing takes 20% off.
All as of 2026-10-30, the three tiers re-verified unchanged against the live pricing page.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-11 | Explorer | Recorded at $50/month, 20 questions per day | https://vanna.ai/pricing |
| 2026-10-11 | Team | Recorded at $500/month, 300 questions per day | https://vanna.ai/pricing |
| 2026-10-11 | Enterprise | Recorded at custom pricing, unlimited questions, SAML SSO, on-prem support | https://vanna.ai/pricing |

## Compared to

- [WrenAI](../wrenai/index.md): the live successor in this category; Wren's semantic model is versioned YAML you review and delivery is MCP-first, Vanna's learned context lives in a vector store and delivery is its own chat app. Choose WrenAI for new builds.
- [Context7](../context7/index.md): the other retrieve-into-the-prompt engine, but over the world's library documentation; Vanna retrieves your schema and your past questions.
- [qmd](../qmd/index.md): local hybrid retrieval over your own documents, the same RAG approach with no SQL semantics; what Vanna does for warehouses, qmd does for notes.

## Bottom line

**Recommended for teams inheriting a Vanna deployment, who should know the core is frozen and budget for a fork or a migration to the governed alternative; not for new builds choosing a data-semantics engine today.**
The archive is the information: the framework that defined text-to-SQL RAG is now a snapshot with a price list.

## Changes

- 2026-10-11 - Created from the retrieval scan's context-engines flag, admitted as the archived RAG ancestor of the data-semantics column; the scan's active-at-18k-stars premise corrected to archived-at-23.8k on the repository's own banner.
- 2026-10-22 - Rotation re-verification: every cited URL re-fetched, the star-history picture block corrected (its light-theme source and fallback carried the dark theme), and the README reference re-described after Vanna slimmed its README to a marketing page that no longer mentions Tool Memory or the agent architecture (the docs still carry both); pricing tiers re-verified unchanged, forks and open issues refreshed.
- 2026-10-30 - Rotation re-verification: every cited URL re-fetched and intact (the archive banner still on the repository page, the slimmed README, PyPI at 2.0.2 across 78 releases, the docs portal and commercial site, the three pricing tiers unchanged, the 547-point launch thread, the CVE-2024-5565 coverage); forks refreshed; no claim changed.

## See also

- [WrenAI](../wrenai/index.md) - the live governed-semantics engine that inherited this job
- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins as the second data column
- [Context7](../context7/index.md) - the outside-knowledge sibling on the same retrieve-into-the-prompt axis
- [qmd](../qmd/index.md) - the local-RAG contrast for documents

## References

- https://github.com/vanna-ai/vanna - the archive banner, "archived by the owner on Mar 29, 2026", on the repository page
- https://api.github.com/repos/vanna-ai/vanna - forks, issues, archived flag, and last push as of 2026-10-30 (stars kept at the 2026-10-13 baseline)
- https://raw.githubusercontent.com/vanna-ai/vanna/main/README.md - the Vanna 2.0 README as re-fetched 2026-10-22: the slimmed marketing page (user-aware permissions, vanna-chat, enterprise security, MIT); Tool Memory and the agent architecture now live only in the docs
- https://pypi.org/pypi/vanna/json - 78 releases with 2.0.2 on 2026-02-02 the last
- https://vanna.ai/docs/ - the live docs: the Tool Memory mechanism and the 0.x migration path
- https://vanna.ai - the commercial site: Cloud and self-host, hosted admin features
- https://vanna.ai/pricing - Explorer $50, Team $500, Enterprise custom, re-verified unchanged 2026-10-30
- https://hn.algolia.com/api/v1/items/38992601 - the 547-point launch thread of 2024-01-14, the community footprint's peak
- https://www.scmagazine.com/news/vanna-ai-prompt-injection-vulnerability-enables-rce - CVE-2024-5565 prompt-injection RCE coverage, the record's critical source
