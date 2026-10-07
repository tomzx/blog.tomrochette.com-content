---
title: Yao
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, agent-workspaces, self-hosted]
readability: 3
audience_notes: >
  Engineers evaluating a self-hosted agent workspace that spans their own devices, who want the eight-thousand-star count put in context before shortlisting.
  Assumes you know what a task board and a coding-agent harness are.
---

Yao (now marketed as Yao Agents) is a self-hosted, cross-device agent workspace from Infinite Wisdom Software, built on the Yao Engine single binary, where agents work in workspaces spread across your own desktops, phones, and servers and surface their output on a task board.

**The 8.1k stars are five years old, not agent-era: most were accumulated as a 2021 low-code engine, so the pivot is much younger and far less proven than the count suggests.**

## What it is

A product family on one engine: Yao Agents (the workspace, where a conversation turns into a board task and workspaces accumulate into a document knowledge base), Tai Link (the device connector), and Yao Engine (a Go single-binary runtime).
Surfaces are desktop, Android (beta), browser, and an Open API with SSE and WebSocket, all self-hosted, and agents run on the machines you register rather than on a vendor cloud.
The agent-era integrations are recent and first-party: DeepSeek Harness (announced 2026-08-18) and Jev, TypeSafe AI's typed-decision model, through Tao (2026-09-24).
The license is a modified Apache-2.0 that GitHub reports as NOASSERTION.

## Status

Active on the product side and old on the clock: the repository was created 2021-09-06 and shows 8,079 stars and 721 forks as of 2026-10-06, pushed 2026-10-05.

<a href="https://www.star-history.com/?repos=YaoApp%2Fyao&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=YaoApp/yao&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=YaoApp/yao&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=YaoApp/yao&type=date&legend=top-left" />
 </picture>
</a>

The release line sits at v1.0.0-rc26 (2026-10-05), moving roughly weekly since summer 2026, which means five years without a stable 1.0.
The only HN story remains the 2-point, zero-comment 2022 launch of the low-code era, and I found no independent coverage of the agent pivot this run, which is the adoption signal to weigh against the star count.

## Strengths

- The cross-device spread (desktop, Android, browser, API) is rare in a category that is mostly one desktop app or one terminal TUI.
- Self-hosted and local-first by design: agents run on machines you control, with your data.
- First-party model-side integration: DeepSeek Harness and Jev ship inside the product rather than as configuration you wire up.

## Cautions

- The star count measures the 2021-2022 low-code engine, not the agent workspace.
- The modified license requires preserving the logo and the certificate-verification logic, and it requires a commercial license for organizations with 50 or more employees or over $1M annual revenue, so this is not plain open source.
- Five years of releases still short of 1.0, plus a rebrand from yaoapps.com to yaoagents.com, is pivot churn to price in.
- The repository ships a "Guide for AI Agents" issue instructing AI assistants how to research and describe it, which I read as marketing aimed at the agent-research channel rather than at developers.

## Pricing

Free to self-host under the modified Apache-2.0 terms.
The commercial license required at enterprise scale is quote-based with no public price (as of 2026-10-06).

## Compared to

- [Omnara](../omnara/index.md): the other control plane that wants phone-and-dashboard supervision, but Omnara wraps the CLI agents you already run while Yao wants its own workspace products on your devices.
- [LobeHub](../lobehub/index.md): the other platform born as something else (a chat UI) that pivoted into agent operations and sells a hosted tier; Yao's console exists, but hosted agent execution is unverified.
- [Emdash](../emdash/index.md): the desktop-workspace rival that wraps 25-plus existing CLIs locally; Yao's agents are its own, running on the devices you register.

## Bottom line

**Recommended for self-hosters who want agents working across their own machines under one board, and who accept the license strings.**
Not for anyone reading the 8k stars as agent-era adoption, and not for pure open-source procurement lists.

## Changes

- 2026-10-06 - Created.
- 2026-10-07 - Added the YaoApp/yao star history chart to the Status section.

## See also

- [DeepSeek Harness](../../harnesses/deepseek-harness/index.md) - the harness Yao integrates first-party
- [Omnara](../omnara/index.md) - the open-source cross-device control plane counterpart
- [LobeHub](../lobehub/index.md) - the other pivoted platform in the category
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the comparison this note joins

## References

- https://api.github.com/repos/YaoApp/yao - repository metadata, counts, and topics as of 2026-10-06
- https://api.github.com/repos/YaoApp/yao/readme - the Yao Agents product surface: workspaces, task board, Open API, and the DeepSeek Harness and Jev announcements
- https://api.github.com/repos/YaoApp/yao/license - the modified Apache-2.0 terms, including the 50-employee and $1M commercial-license conditions
- https://api.github.com/repos/YaoApp/yao/releases - the v1.0.0-rc26 release line and cadence
- https://yaoagents.com - the product family (Yao Agents, Tai Link, Yao Engine) and self-hosting positioning
- https://yaoagents.com/blog/en-us/2026/release/deepseek-harness - the DeepSeek Harness integration, dated 2026-08-18
- https://yaoagents.com/blog/en-us/2026/release/jev - the Jev typed-decision integration through Tao, dated 2026-09-24
- https://hn.algolia.com/api/v1/items/30699919 - the 2022 low-code launch thread, 2 points and zero comments, cited as the thin-footprint signal
