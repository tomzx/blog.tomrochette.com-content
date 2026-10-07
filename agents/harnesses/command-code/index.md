---
title: Command Code
created: 2026-10-05
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agents, harnesses, open-models, personalization, closed-source]
readability: 3
audience_notes: >
  Engineers choosing a terminal coding agent for open-weight models on a budget, and anyone evaluating whether a
  personalization layer can carry a closed client. Assumes you know what BYOK, MCP, and prompt-cache hit rates mean.
---

Command Code is a closed-source terminal (plus desktop) coding agent from CommandCodeAI, the company formerly operating as Langbase, pitched as the best harness for open-weight models and differentiated by taste-1, a personalization model that learns your coding conventions from every accept, reject, and edit.

**Command Code is the first harness whose product is a learned model of you rather than a better loop, and the bet stands or falls on whether a large install base converts into trust in a closed client from a five-month-old pivot.**

## What it is

An npm-distributed CLI (`command-code`) plus a desktop app for macOS, Linux, and Windows, running interactive, headless (`-p`, `--yolo`), and background-sandbox sessions.
The signature mechanism is taste-1: interaction signals distill into project-level skills and personal memory, stored as human-readable markdown under `.commandcode/taste/`, and shareable across a team with `npx taste push` and `pull`.
The surface is complete for a young tool: `/skills`, `/commands`, `/mcp` servers, custom `/agents`, persistent `/memory`, plugins, session sharing, and ACP support so Zed-class editors can host it (`cmd acp`, shipped in v1.74.0).
Model access is the actual pitch: a vendor roster spanning Anthropic, OpenAI, Google, xAI, DeepSeek, Qwen, Kimi, GLM, and MiniMax, sold through credit bundles with per-model allowances and deal multipliers, with free stealth-preview models on every plan.
The company raised a $5 million seed led by Tom Preston-Werner, with Amjad Masad and Luca Maestri among the angels, and previously ran Langbase, which Tech Stackups reports processed about 1.2 billion agent runs per month.

## Status

**Active and fast-growing in distribution, with an evidence base that is mostly the vendor's own.**
The npm package's latest build is 1.74.3 (published October 5, 2026), the site's changelog counts 390 releases, and the package did 219,535 downloads in the last month (the API window covering September 5 to October 4, as of 2026-10-06).
The `CommandCodeAI/command-code` repository has 4,097 stars as of 2026-10-06 (GitHub API) but hosts issues only: no source, no license, the client is closed.

<a href="https://www.star-history.com/?repos=CommandCodeAI%2Fcommand-code&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=CommandCodeAI/command-code&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=CommandCodeAI/command-code&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=CommandCodeAI/command-code&type=date&legend=top-left" />
 </picture>
</a>

The first public release dates to about May 2026 (a 3-point Show HN on May 6), and the GOAT plan announcement drew 6 points in August; the site claims 100,000-plus developers and 40,000-plus paying customers, numbers I cannot verify from anywhere independent.
I treat the install count as the one solid signal and the discussion vacuum as a warning: a genuinely adopted tool usually leaves more community trace than this.

## Strengths

- **Open-model focus backed by harness engineering claims**: tool-call validation and repair on every model (about 1 million repairs per trillion tokens, it says), claimed 99-percent-plus cache hit rates, and free stealth-preview models (Space Bunny Alpha, Laguna S 2.1, the Ling 3.x line) on every plan.
- taste-1 is a genuinely different mechanism: conventions become learned, inspectable markdown files you can version and share, not rules files you maintain by hand.
- Aggressive pricing: $1/month entry with $10 of credits, and $70 of credits for $10 on the GOAT plan across roughly 50 models.
- BYOK breadth including local models, per the Tech Stackups model-flexibility table.

## Cautions

- **The client is closed and the trust model is the vendor's word**: no source repository, no license file, a privacy page, and a personalization layer that watches how you code.
- First-release quality was rough: Tech Stackups recorded 25 open issues filed within 48 hours of the May launch, all paste, crash, and integration failures.
- The efficiency claims are self-published: the token-efficiency and cache-rate benchmarks it leads are its own.
- A near-zero Hacker News footprint against the claimed install base, so treat the vendor's adoption numbers as marketing until independently confirmed.
- The price structure is genuinely complex: per-model allowances, effective-usage multipliers of up to 2x to 5x on deal models, a processing fee on every plan, and free models whose credits cost nothing only while capacity lasts.

## Pricing

Individual plans as of 2026-10-06 (re-verified unchanged): Go $1/month ($10 of credits, open models), GOAT $10/month ($70 of credits, roughly 50 models including GPT-5.6 Sol), Pro $20/month ($80 of credits, premium models), Max 10x $100/month ($150 of credits), and Max 20x $200/month ($300 of credits), each plus a processing fee.
The Provider plan at $15/month is an OpenAI- and Anthropic-compatible API with zero markup; Teams is $40/month with pooled credits; Enterprise is custom.
Top-up credits are bought at model cost, roll over, and never expire; free stealth-preview models consume no credits while they last.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-05 | Individual plans | Baseline: Go $1/mo ($10 credits), GOAT $10/mo ($70 credits), Pro $20/mo ($80 credits), Max 10x $100/mo ($150 credits), Max 20x $200/mo ($300 credits), processing fee on each. | [commandcode.ai/pricing](https://commandcode.ai/pricing) |
| 2026-10-05 | Provider | Baseline: $15/mo API plan, OpenAI- and Anthropic-compatible endpoints, zero markup, rollover top-ups. | [commandcode.ai/pricing](https://commandcode.ai/pricing) |
| 2026-10-05 | Teams | Baseline: $40/mo with pooled credits and central admin. | [commandcode.ai/pricing](https://commandcode.ai/pricing) |

## Compared to

- [Kimi Code](../kimi-code/index.md): the other challenger-model harness; Kimi Code is open source and tuned by its own model vendor, Command Code is closed and vendor-neutral across open models.
- [MiMo Code](../mimo-code/index.md): the other cheap-token open-weights play; MiMo Code is MIT and auditable, Command Code is closed with a personalization layer as the differentiator.
- [Claude Code](../claude-code/index.md): the premium closed rival; Command Code undercuts its entry price by an order of magnitude and bets open models plus harness repair close the gap.

## Bottom line

**Recommended for token-payers who want open-weight models in a polished harness and will accept a closed client plus self-reported benchmarks to get them.**
Not for open-client mandates, and not for anyone who needs independent evaluation before trusting an agent with their repository.

## Changes

- 2026-10-05 - Created from the same-day entrant scan, with the site, pricing page, npm registry, repository, third-party review, and Hacker News record fetched.
- 2026-10-07 - Added the CommandCodeAI/command-code star history chart to the Status section.

## See also

- [Kimi Code](../kimi-code/index.md) - the open-source challenger-model harness it competes with on price
- [MiMo Code](../mimo-code/index.md) - the auditable cheap-tokens alternative
- [Claude Code](../claude-code/index.md) - the premium closed incumbent it undercuts
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the capability rows this column joins

## References

- https://commandcode.ai/ - product surface, taste-1 claims, company positioning, and the $5M seed line (fetched 2026-10-05)
- https://commandcode.ai/pricing - plan ladder, credits, Provider API plan, and Teams pricing, as of 2026-10-06 (re-verified unchanged)
- https://registry.npmjs.org/command-code - latest build 1.74.3 published 2026-10-05, package created 2025-08-07 (verified via the registry API)
- https://api.npmjs.org/downloads/point/last-month/command-code - 219,535 downloads, window September 5 to October 4, as of 2026-10-06
- https://github.com/CommandCodeAI/command-code - issues-only repository, 4,097 stars, no source or license, as of 2026-10-06 (verified via the GitHub API)
- https://techstackups.com/comparisons/coding-agent-harness-comparison-2026/ - the critical source: closed-source classification, funding details, ex-Langbase history, and the 48-hour launch-issue record (fetched 2026-10-05)
- https://hn.algolia.com/api/v1/items/48031887 - the May 6, 2026 Show HN, 3 points (verified via the Algolia API)
- https://hn.algolia.com/api/v1/items/49188656 - the August 5, 2026 GOAT-plan Show HN, 6 points
