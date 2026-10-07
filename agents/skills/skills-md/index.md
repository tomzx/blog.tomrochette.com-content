---
title: skills.md
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, skills, registries, marketplaces, hosted-execution]
readability: 3
audience_notes: >
  Engineers deciding whether to buy hosted skill execution for their agents, and authors weighing a paid marketplace against the free registries.
  Assumes familiarity with SKILL.md packaging and MCP configuration.
---

skills.md is Hasna's hosted-execution skills marketplace: an agent finds a skill through its CLI and MCP server, the skill runs on skills.md's servers, and the finished artifacts come back to the project.

**It is this category's first paid column, and the model it sells differs from every free registry here: execution as a service, where the skill's compute happens on the vendor's machines and each run is quoted in credits before you approve it.**

## What it is

The client is an open-source Apache-2.0 CLI and SDK (`@hasna/skills` on npm, latest 0.10.46 with 168 published versions since 2026-02-14) that signs in through a browser flow and registers a stdio MCP server with the agent, documented for claude, codex, cursor, opencode, pi, and windsurf, with any MCP host supported by manual registration.
The catalog is curated rather than crawled: the marketplace page lists 250 entries (the homepage says 300 plus curated skills) across generation-style tasks like logo design, brand kits, pitch decks, and market research reports, each returning downloadable artifacts.
Authors publish with `skills push`, where every push is a version, and companies can self-host, since the CLI, SDK, MCP server, and service code are public in the hasna/skills repository, made public on 2026-09-26.

## Status

**Active product, near-zero community footprint.**
The npm package has shipped 168 versions in roughly eight months, but the GitHub repository showed 0 stars and 0 forks as of 2026-10-07, eleven days after it went public.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=hasna/skills&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=hasna/skills&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=hasna/skills&type=date&legend=top-left" />
</picture>

No Hacker News story covers the marketplace (my search returned only 4-point items about the SKILL.md filename in general), and I found no independent review, so the adoption evidence is the release cadence, not a community.
The site is candid in ways that help evaluation: its marketplace labels every hosting status unverified pending a live check, and its demo session is labeled illustrative.

## Strengths

- **Hosted execution moves the risky half off your machine: generation workloads run on the vendor's infrastructure, with only artifacts and a quoted price crossing back.**
- The credit model prices per run with an approval prompt and a per-run credit limit, so cost is a decision made before execution, not a bill after it.
- Publishing is versioned (`skills push`, `skills versions`) and self-hosting is documented, under an Apache-2.0 client.
- It rides MCP, so any host can register it rather than only the six documented CLIs.

## Cautions

- **The community footprint is a warning in both directions: zero GitHub stars on a ten-day-old repo and no independent coverage mean nobody has audited the hosted execution path, which is exactly the surface that receives your prompts and briefs.**
- Skills execute server-side, so everything in a skill's prompt and your brief leaves your environment; that is the product, but it is a nonstarter for private codebases and regulated content.
- The catalog numbers disagree with each other (300 plus on the homepage, 250 on the marketplace page), small enough to be sync lag and worth rechecking.
- Credits expire after 365 days and the CLI runs on the vendor's sign-in flow, so workflows accumulate dependency on a hosted account.

## Pricing

Freemium with metered execution.
Free: $0, public skills on all agents, trial credits for new accounts.
Pro: $10 per month, billed monthly, cancel any time.
Credits: pay per run, packs of $1, $5, $20, $50, or $100, purchased credits expire after 365 days, and hosted runs are quoted first with a per-run credit limit you approve.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-06 | Free, Pro, credits | First recorded: Free $0, Pro $10 per month, credit packs $1-$100 with 365-day expiry | https://skills.md/ |

## Compared to

- skills.sh: the free telemetry-ranked registry, where skills are files you run yourself; skills.md trades the file model for hosted execution and a bill.
- SkillMD: the free verification-first index; neither grades what skills.md actually executes, and skills.md's curation is a list, not a verdict.
- Anthropic Agent Skills: the format skills.md's hosted skills imitate; there the folder runs in your harness, here it runs on Hasna's servers.

## Bottom line

**Recommended for generation-style tasks (logos, decks, brand kits) where sending a brief to a hosted runner is harmless and the credit quote keeps cost visible.**
Not for anything touching private code, secrets, or compliance boundaries, and not as a general skills registry, because the catalog is curated and small.
My disagreeable claim: this is the first skills product that could actually sustain a business, because it charges for the scarce things (compute and curation) while the free registries rank files nobody pays for, which also explains why the repo went public only once the marketplace was ready.

## Changes

- 2026-10-06 - Created in the daily refresh's skills entrant scan.
- 2026-10-07 - Added the hasna/skills star history chart to the Status section.

## See also

- [skills.sh](../skills-sh/index.md) - the free registry incumbent this monetizes against
- [SkillMD](../skillmd/index.md) - the other registry in the category, verification-first where this is execution-first
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the format its hosted skills follow
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map this marketplace sits in

## References

- https://skills.md/ - the product surface: CLI and MCP flows, the plans (Free, Pro $10 per month, credit packs $1-$100), 300-plus curated skills, Apache-2.0, Hasna, Inc. (fetched 2026-10-06)
- https://skills.md/marketplace - the catalog page: 250 of 250 entries, category filters, and every hosting status labeled unverified pending a live check (fetched 2026-10-06)
- https://registry.npmjs.org/@hasna/skills - the CLI package: created 2026-02-14, latest 0.10.46, 168 versions (fetched 2026-10-07)
- https://api.github.com/repos/hasna/skills - the Apache-2.0 CLI, SDK, MCP, and service repo: made public 2026-09-26, 0 stars, pushed 2026-10-07 (GitHub API, as of 2026-10-07)
- https://hn.algolia.com/api/v1/search?query=%22skills.md%22&tags=story - the footprint scan: no marketplace coverage, the nearest hits are 4-point items about the filename convention (fetched 2026-10-06)
