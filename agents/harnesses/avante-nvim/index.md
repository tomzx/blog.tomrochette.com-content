---
title: Avante.nvim
created: 2026-10-13
updated: 2026-10-18
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, harness, neovim, editor-agent]
readability: 3
audience_notes: >
  Neovim users who want a Cursor-style agentic coder inside their editor instead of a separate CLI or fork.
  Assumes you live in Neovim and know what bring-your-own-key means.
---

Avante.nvim is an Apache-2.0 Neovim plugin that reproduces the Cursor AI IDE experience inside Neovim: an agentic coding panel with tool use, diff application, and bring-your-own providers, originally by yetone and now under the avante-corp organization.

**Its claim to the harnesses category is the editor-embedded loop: like Cline, it runs its own agent loop against your files, but it lives where Neovim users already are, which makes it the default answer for the one editor family the CLI harness wave skipped.**

## What it is

A Lua plugin with Rust helpers requiring Neovim 0.12+, distributed through the Neovim plugin ecosystem and tracked by community plugin directories.
It provides AI-driven code suggestions, an agent mode that plans and edits across files, a tool-use surface, and diff-based application of changes, with provider configuration for commercial APIs and local backends.
Development is active with CI on both Lua and Rust, a Discord community, and rapid iteration the README itself flags.

## Status

Established and maintained: 18,183 stars, 858 forks, and 53 open issues as of 2026-10-13, with the default branch pushed 2026-10-17 (GitHub API, re-checked 2026-10-18) and the newest tagged release v0.4.0 (2026-09-26), plugin installs generally tracking the branch.
**Its adoption is the oldest story in this wave: a 300-point Hacker News launch thread in August 2024, sustained directory and community coverage since, which makes it one of the few editor-extension harnesses with a proven multi-year footprint.**
The repository moved from the author's personal account to the avante-corp organization, the ordinary sign of a project outgrowing one maintainer.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=avante-corp/avante.nvim&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=avante-corp/avante.nvim&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=avante-corp/avante.nvim&type=date&legend=top-left" />
</picture>

## Strengths

- The editor is the harness: suggestions, agent planning, and diff application happen in the buffer, with no context switch to a terminal.
- Bring-your-own providers including local backends, so the plugin outlives any single vendor relationship.
- Two years of public history (August 2024 launch, 300-point thread) with continuous maintenance and a 2026 organization transfer.
- Engineering hygiene on the record: CI on both languages, pre-commit checks, and a versioned release line.
- The category's standing answer for Neovim, which no CLI harness replaces.

## Cautions

- Neovim 0.12+ is a hard floor, so conservative configurations must upgrade their editor to upgrade the agent.
- Rapid iteration is the project's own description of itself, which means configuration surfaces move under you.
- The editor boundary is a capability boundary: no cloud execution, no scheduled runs, and several harness features (subagents, hooks) are not documented at the depth CLI harnesses offer.
- As a plugin it inherits Neovim's single-user, single-machine model; team-level governance does not exist here.
- Tagged releases lag the branch, so pinning versions is on you.

## Pricing

Free and open source under Apache-2.0.
No hosted tier; model cost is whatever your configured providers charge, including free local backends.

## Compared to

- [Cline](../cline/index.md): the VS Code counterpart with the same editor-embedded-loop idea and a larger ecosystem; Cline if you live in VS Code, Avante.nvim if you live in Neovim.
- [Claude Code](../claude-code/index.md): the terminal harness with subagents, hooks, and cloud options; use it when you want harness depth, Avante.nvim when you want the editor native.
- [OpenCode](../opencode/index.md): the vendor-neutral terminal harness; pairs with any editor, while Avante.nvim is the in-editor experience for one.

## Bottom line

**Recommended for Neovim users who want the agentic loop in their editor with their own keys and local models.**
Not for team governance needs, scheduled or cloud execution, or anyone unwilling to track a fast-moving plugin branch.

## Changes

- 2026-10-13 - Created.
- 2026-10-13 - Corrected the star-history chart markup: the light source and fallback image dropped the dark-theme parameter to match the canonical chart block.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the category comparison this note joins
- [Cline](../cline/index.md) - the VS Code counterpart with the same editor-embedded loop
- [Claude Code](../claude-code/index.md) - the terminal harness with the deeper operations surface
- [OpenCode](../opencode/index.md) - the vendor-neutral terminal alternative
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this section extends

## References

- https://github.com/avante-corp/avante.nvim - repository, Apache-2.0 license, stars, push activity, requirements, and the Cursor-emulation scope as of 2026-10-13
- https://github.com/avante-corp/avante.nvim/blob/main/README.md - the feature description, provider configuration, and tool-use surface
- https://github.com/yetone/avante.nvim - the original personal-account location, kept as the rename evidence
- https://news.ycombinator.com/item?id=41353835 - the August 2024 launch thread (300 points), the project's independent footprint
- https://dotfyle.com/plugins/yetone/avante.nvim - the Neovim plugin directory listing tracking community installs
