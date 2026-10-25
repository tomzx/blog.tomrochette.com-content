---
title: Arc Kit
created: 2026-10-13
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, spec-driven-development, governance, enterprise-architecture]
readability: 3
audience_notes: >
  Enterprise and government architects who want lifecycle governance commands inside their coding agent instead of a document template library.
  Assumes you know what a spec-driven workflow is and what an architecture review board expects.
---

Arc Kit is a solo-maintained, MIT-licensed governance harness for enterprise architecture: 76 lifecycle commands packaged as a Claude Code plugin (with Gemini, Copilot, Codex, OpenCode, Mistral, and Kimi Code formats) that turn strategy, requirements, design, delivery, and assurance work into structured, citation-marked drafts.

**Its bet is that governance is a command surface: where this category's other members spec the software, Arc Kit specs the institution around it, from HM Treasury business cases to Wardley Maps to HLD and DLD design reviews.**

## What it is

A command catalog plus templates, scripts, and bundled MCP servers (AWS Knowledge, Microsoft Learn, Google Developer Knowledge, and UK public-sector scrapers), created by a UK-public-sector-background maintainer in October 2025.
Claude Code is the premier platform (autonomous research agents, automation hooks, automatic marketplace updates, with the standalone `arckit-claude` marketplace now the recommended install); the same 76 commands ship as a Gemini CLI extension, Copilot prompt files, a Mistral extension, Kimi Code skills, and Codex and OpenCode formats.
The catalog covers architecture principles, stakeholder analysis, Orange Book risk, Green Book business cases, requirements with ERD and GDPR checks, build-versus-buy research, Wardley Mapping, Mermaid diagrams, vendor RFPs, formal design reviews, ServiceNow design, requirements traceability, and inline citation markers for external documents.
A plugin system composes regional and sector overlays, fourteen community plugins as of 2026-10-25, from the EU, UAE, France, Austria, and Canada to Australia and USA federal packs, NHS clinical safety, UK finance, Australian energy, and TOGAF ADM, and every artifact carries a provenance record of the model and effort level that produced it; the project also ships an Open Badges certification program.

## Status

Active and growing: 2,255 stars, 283 forks, and 23 open issues as of 2026-10-14, created 2025-10-14 with its default branch last committing 2026-10-20 (as of 2026-10-25), effectively solo (95 of the last 100 commits), with release v6.18.2 (2026-10-12) the newest of a train that shipped v6.18.0 and v6.18.1 on October 10 and 12.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=tractorjuice/arc-kit&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=tractorjuice/arc-kit&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=tractorjuice/arc-kit&type=date&legend=top-left" />
</picture>

**The community footprint is silent: zero Hacker News threads under its own name, so the stars ride practitioner word of mouth (the README's UK-government framing) rather than public debate.**
The provenance notes are unusually candid about model behavior, recording exactly which Claude Code versions changed how effort levels execute.

## Strengths

- The command surface is governance-specific and complete: the lifecycle from strategy to assurance exists as invocable commands, not advice documents.
- Provenance and citation discipline: artifacts record the model and effort that produced them, and external documents are cited inline with source quotes.
- Multi-harness distribution that ships: seven agent formats from one catalog, with per-format quirks documented (Copilot's 165 prompt files, Kimi's manifest-loaded skill).
- Human review is structural, not aspirational: the README states artifacts are drafts for qualified people to review, never advice.
- The overlay system composes jurisdictions and sectors without forking the core.

## Cautions

- Effectively one maintainer: 95 of the last 100 commits are the founder, so the bus factor is one person plus the community overlay authors.
- The license is mixed: MIT except the UK G-Cloud supplier overlay, which is public but proprietary and Claude-only, so the full catalog is not open everywhere.
- Deep Claude Code favoritism: the premier experience (research agents, hooks, bundled MCP servers) degrades to plain command files elsewhere.
- Zero independent footprint means no field reports outside the README's own claims, and the governance domain (Orange Book, Green Book, ServiceNow) is exactly where silent errors are expensive.
- The breadth (76 commands across two domains) invites drift between overlays and core; the compatibility marketplace already exists because it happened once.

## Pricing

Free and open source under MIT, with one exception: the `arckit-uk-gcloud` supplier overlay is public but proprietary and distributed only for Claude Code.
No hosted tier and no paid plan anywhere in the project.

## Compared to

- [AI-DLC](../ai-dlc/index.md): AWS's harness-neutral lifecycle engine specs the software build; Arc Kit specs the architecture governance around it, with public-sector documents AI-DLC does not model.
- [Superpowers](../superpowers/index.md): the mandatory-workflow skill suite at 300x the adoption; Superpowers is general engineering discipline, Arc Kit is a governance domain catalog.
- [GitHub Spec Kit](../spec-kit/index.md): the spec-first movement's process layer; pair it with Arc Kit when the specs need business cases and design reviews attached.

## Bottom line

**Recommended for enterprise and public-sector architects who want their governance lifecycle as commands inside Claude Code, with provenance and citations attached to every artifact.**
Not for pure software spec work (Spec Kit and peers are lighter), multi-maintainer shops needing license uniformity, or teams off the Claude Code premiere who need the full research-agent experience.

## Changes

- 2026-10-13 - Created.
- 2026-10-14 - Added the release train (v6.18.0 through v6.18.2, October 10 to 12) and refreshed counts.
- 2026-10-25 - Rotation re-verification of every cited source (all alive, the release train unchanged at v6.18.2): recorded the overlay catalog's growth to fourteen community plugins (France, Netherlands, Austria, Canada, Australia, and USA among the newer jurisdictions), the standalone arckit-claude marketplace as the recommended Claude Code install, and the Open Badges certification program.

## See also

- [Spec Driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the category comparison this note joins
- [AI-DLC](../ai-dlc/index.md) - the lifecycle-engine neighbor on the software side of the category
- [Superpowers](../superpowers/index.md) - the general workflow suite at the category's largest adoption
- [GitHub Spec Kit](../spec-kit/index.md) - the spec-first process layer Arc Kit's artifacts would feed
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this section extends

## References

- https://github.com/tractorjuice/arc-kit - repository, counts, mixed-license note, the 76-command catalog, and provenance notes as of 2026-10-13
- https://arckit.org/ - the project site and governance-workflow framing
- https://github.com/tractorjuice/arc-kit/blob/main/README.md - the install formats (Claude Code, Gemini, Copilot, Mistral, Kimi, Codex, OpenCode), the plugin marketplace composition, and the drafts-for-review disclaimer
- https://github.com/tractorjuice/arc-kit/blob/main/LICENSE - the MIT grant and its carve-out for the proprietary arckit-uk-gcloud overlay
- https://news.ycombinator.com/ - Algolia search for Arc Kit and enterprise architecture returned no threads, the recorded absence of an independent community footprint
