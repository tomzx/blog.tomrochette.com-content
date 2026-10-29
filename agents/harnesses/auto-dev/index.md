---
title: AutoDev
created: 2026-10-13
updated: 2026-10-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, harness, ide-plugin, jetbrains, vscode, kotlin]
readability: 3
audience_notes: >
  Engineers evaluating IDE-embedded coding agents, especially on the JetBrains side, who want to know what one maintainer's multiplatform platform bet delivers today.
  Assumes you know what an IDE plugin, MCP, and AGENTS.md are.
---

AutoDev is Phodal's MPL-2.0 multi-agent coding development platform written on Kotlin Multiplatform: one agent engine compiled to IntelliJ IDEA, VS Code, CLI, web, desktop, Android, iOS, and JS/WASM targets, shipping today as the alpha AutoDev 3.0 "Xiuper" beside the stable AutoDev 2.0 Sketch plugin line.

**It is the category's widest-surface IDE bet and its narrowest bus: five top-level agents and nine subagents across every device class, carried by one maintainer who wrote about 98 percent of the code.**

## What it is

A Kotlin Multiplatform codebase whose shared mpp-core module holds the agent engine, tools, MCP integration, and AGENTS.md loading, with mpp-idea and mpp-vscode as IDE frontends and CLI, web, and desktop shells around them.
Xiuper's top-level agents are Document, Coding, Review, ChatDB, and Artifact, backed by nine specialized subagents (analysis, error recovery, NanoDSL UI, charts, codebase investigation, domain dictionary, SQL revision, E2E testing, and web).
The tool surface includes file system, grep/glob, shell, web fetch, and MCP, with Claude-format skill loading, SpecKit command integration, A2A agent commands, and tree-sitter parsing for seven languages.
AutoDev 2.0, the stable predecessor on the autodev2 branch, is the Sketch IDE-canvas line (code, diff, terminal, and diagram sketches) with the DevIns agent language.

## Status

Established but slowing: 4,557 stars, 500 forks, and 4 open issues as of 2026-10-13, pushed 2026-09-25, created April 2023.
The commit record shows a June 2026 train (IDEA plugin 0.4.2 on 2026-06-19) and a single commit on 2026-09-25, and Xiuper's releases are alpha-only (compose-v3.0.0-alpha5, February 2026).
Distribution traction is small: the Xiuper JetBrains plugin shows 671 downloads and the stable Sketch plugin 4,548 as of 2026-10-29, and the VS Code extension about 5,543 installs (last updated December 2025, as of 2026-10-29).
The repository moved from the unit-mesh organization to the author's personal account (the old path redirects), and the docs site still links the old location.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=phodal/auto-dev&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=phodal/auto-dev&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=phodal/auto-dev&type=date&legend=top-left" />
</picture>

## Strengths

- The multiplatform architecture is genuinely one codebase: the same agent engine targets eight surface classes, which no other member of this category attempts.
- The agent roster covers the full development loop, requirements research through review and data query, not just code generation.
- AGENTS.md handling is first-class: automatic discovery and prompt injection from the project hierarchy.
- The ecosystem plumbing is current: MCP tools, Claude-format skills, SpecKit commands, and A2A agent commands all load today.
- Four years of continuous solo development with bilingual (Chinese/English) documentation and a stable 2.0 line users can stay on.

## Cautions

- The name collides with Microsoft Research Asia's AutoDev agent framework paper, which dominates search results and every HN thread on the term; the project itself has no Hacker News footprint at all.
- Bus factor is effectively one: the founder accounts for about 98 percent of contributions, and the org-to-personal-account move concentrates it further.
- Xiuper is alpha-only with no stable release of the 3.0 platform, and the VS Code extension has not been updated since December 2025.
- Marketplace installs are three orders of magnitude below the category's mass members (Cline claims 5.5 million installs), so the platform thesis is untested at scale.
- The docs site's promised research-paper link is empty, and the only "AutoDev" arXiv paper is Microsoft's, not this project's.

## Pricing

Free and open source under MPL-2.0.
No hosted tier; model cost is whatever your configured providers (OpenAI, Anthropic, Google, DeepSeek, Ollama) charge.

## Compared to

- [Avante.nvim](../avante-nvim/index.md): the other IDE-plugin harness, Neovim-side with two years of community maintenance and an 18k-star base; choose Avante for Neovim or a maintained plugin, AutoDev for JetBrains and the multi-surface platform.
- [Kilo Code](../kilo-code/index.md): the VS Code and JetBrains open agent with a company behind it; Kilo has the adoption and the vendor, AutoDev the broader device spread and the solo author.
- [Claude Code](../claude-code/index.md): the terminal incumbent with IDE extensions; use it for harness depth and vendor support, AutoDev when the IDE-native agent roster and self-hosted platform matter more.

## Bottom line

**Recommended for JetBrains-centric developers who want an open, self-hosted, multi-agent platform inside the IDE and will pin the stable 2.0 line or accept alpha churn on 3.0.**
Not for anyone needing a large community, vendor accountability, or a non-alpha 3.0 release, and not for VS Code-first users while that extension sits stale.

## Changes

- 2026-10-13 - Created.
- 2026-10-24 - Rotation re-verification, re-fetching every cited reference (all live): refreshed the JetBrains download counters (Xiuper 660, Sketch 4,529) and confirmed the single-2026-09-25 commit cadence and alpha-only release record unchanged.
- 2026-10-29 - Rotation re-verification, re-fetching every cited reference (all live): refreshed the JetBrains download counters (Xiuper 671, Sketch 4,548), the VS Code install count (about 5,543), and confirmed the single-2026-09-25 commit cadence and alpha-only release record unchanged.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the category comparison this note joins
- [Avante.nvim](../avante-nvim/index.md) - the editor-embedded-loop precedent that admitted the IDE-plugin kind
- [Kilo Code](../kilo-code/index.md) - the company-backed IDE-agent contrast at much larger adoption
- [Claude Code](../claude-code/index.md) - the terminal incumbent this platform niche answers
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this section extends

## References

- https://api.github.com/repos/phodal/auto-dev - repository metadata: MPL-2.0 license, 4,557 stars, 500 forks, push and creation dates (as of 2026-10-29, pushed 2026-09-25)
- https://api.github.com/repos/phodal/auto-dev/readme - the README: Xiuper platform scope, module table, agent and subagent roster, AGENTS.md loading, ecosystem integrations, and MPL-2.0 statement
- https://api.github.com/repos/unit-mesh/auto-dev - the former organization path, which resolves to phodal/auto-dev and grounds the repository-move record
- https://api.github.com/repos/phodal/auto-dev/commits?per_page=8 - the June 2026 commit train and the single 2026-09-25 commit behind the cadence reading
- https://api.github.com/repos/phodal/auto-dev/releases?per_page=6 - the alpha-only Xiuper release record (compose-v3.0.0-alpha5, 2026-02-07)
- https://ide.unitmesh.cc/ - the project site: AutoDev positioning, AI-friendly architecture, and Unit Mesh community footer
- https://ide.unitmesh.cc/en/intro - the English docs: supported IDEs, AutoDev 2.0 Sketch, feature overview, and DevIns agent language
- https://plugins.jetbrains.com/api/plugins/29223 - the Xiuper IDEA plugin record: 671 downloads as of 2026-10-29
- https://plugins.jetbrains.com/api/plugins/26988 - the stable Sketch IDEA plugin record: 4,548 downloads as of 2026-10-29
- https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery - the VS Code extension record: about 5,543 installs, last updated 2025-12-14 (as of 2026-10-29)
- https://api.github.com/repos/phodal/auto-dev/contributors?per_page=5 - the contributor table with phodal at 7,505 of roughly 7,620 contributions
- https://hn.algolia.com/api/v1/search?query=%22autodev%22&tags=story&hitsPerPage=10 - the name-collision evidence: every AutoDev HN thread concerns Microsoft's framework, none this project
