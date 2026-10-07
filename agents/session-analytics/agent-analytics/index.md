---
title: Agent Analytics
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, session-analytics, analytics, mcp, open-source]
readability: 3
audience_notes: >
  Builders shipping products with agent assistance who want web analytics their coding agent can read and act on.
  Assumes you know what a tracker script, a funnel, and an MCP server are.
---

Agent Analytics is an agent-readable web analytics platform: one tracker script stores your product's events in your own Cloudflare D1 or SQLite database (or its hosted cloud), and your coding agent queries the data through a skill, MCP server, CLI, or HTTP API instead of a human dashboard.

**Agent Analytics is not session observability, it is product analytics with the human dashboard moved out of the loop, which puts it at the edge of this category while sharing the category's founding premise that the data already exists and an agent should be able to read it directly.**

## What it is

The open-source server accepts a single `tracker.js` tag that captures page views, paths, referrers, UTM sources, sessions, device and browser, country, and first-touch attribution, with optional custom events, consent mode, click tracking, errors, performance, vitals, SPA tracking, and opt-in session replay.
Analytics are exposed to agents rather than humans: an operating skill and an autoresearch skill, an MCP server, an official CLI, and an HTTP API, backed by an OpenAPI 3.1 spec and LLM-readable `llms.txt` and `llms-full.txt` exports.
The self-hosted server runs on Cloudflare Workers plus D1, on Docker or Kubernetes with SQLite, or as a plain Node process you point the CLI at.
Documented integrations cover Claude Code, Claude Desktop and Cowork, Codex, Cursor, OpenClaw, Paperclip, Hermes, Instinct, and OpenWork.
Made by Agent Analytics, the same maintainer behind the Awesome Multi-Agent Orchestrators directory.
The README claims MIT, but I could not find a LICENSE file on the default branch.

## Status

The hosted product has moved faster than the open-source server: the main repository has 17 stars and was created 2026-02-06 and last pushed 2026-05-06, while the CLI is a published npm package and sibling repos in the org were pushed through September 2026, as of 2026-09-27.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Agent-Analytics/agent-analytics&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Agent-Analytics/agent-analytics&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Agent-Analytics/agent-analytics&type=date&legend=top-left" />
</picture>

Community signal is thin and concentrated in the org's own plugins, the most prominent being the Hermes dashboard plugin at 27 stars and the Paperclip live analytics plugin at 14 stars, as of 2026-09-27; I found no Hacker News thread for the site.
The README claims MIT and links a LICENSE file that is absent from the default branch, which returned 404 when I fetched it.
**A young hosted product whose open-source server already looks quieter than its cloud, with the open-source claim itself unfinished at the repository level.**

## Strengths

- The agent-first stance is carried all the way through: skill, MCP, CLI, and HTTP, plus an OpenAPI 3.1 spec and LLM-readable docs exports, instead of a dashboard a human has to relay.
- There is a genuine self-host path on free infrastructure: Cloudflare Workers plus D1 with almost no server management, or Docker and Node with SQLite you own.
- The free cloud tier is real usage rather than a demo: 100k events per month, two projects, and multi-agent access.
- Session replay on the paid tier is opt-in and masks recognizable PII, and the docs state the trade-off rather than burying it.
- Integrations cover the tooling this audience already runs, including Claude Code, Codex, Cursor, OpenClaw, and Paperclip.

## Cautions

- Category fit is loose: this measures your product's web traffic, not your coding agents' sessions or token cost, so it answers how the product is doing rather than what the agents did.
- The open-source server repository has been quieter than the hosted cloud since May 2026, and the MIT LICENSE file the README links is missing from the default branch, so self-hosters rely on a claim the repository does not yet substantiate.
- Hosted use moves event data, and optionally session replay, onto the vendor's infrastructure; only the self-hosted route keeps it on yours.
- Per-event metering means a bot-heavy or high-traffic site can consume the free allowance faster than a 90-day retention window suggests.
- The identity-stitching and portfolio model is more product machinery than most small teams need, and the agent-native API is the part that earns its keep.

## Pricing

Free cloud plan at $0 per month: 2 projects, multi-agent access, 100k events per month, 500 analytics reads per month, 90-day retention, and 2 full website scans per month.
Paid cloud plan at $1 per 10k events: unlimited projects, multi-agent access, unlimited analytics reads, unlimited experiments, session replay, 12-month retention, and 100 full website scans per month.
Self-hosting the open-source server on your own Cloudflare, Docker, or Node infrastructure is free apart from your own infrastructure costs.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-27 | Cloud | Free plan introduced at $0/month with 100k events and 2 projects, and a metered plan at $1 per 10k events; self-host free and open source | https://agentanalytics.sh/ |

## Compared to

- [agentsview](../agentsview/index.md): the local session and cost archive for your coding agents; Agent Analytics measures your product's users, so the two answer different questions.
- [agents-observe](../agents-observe/index.md): the live dashboard for coding-agent sessions; Agent Analytics instead watches the product surface those agents help build.
- [Paperclip](../../control-planes/paperclip/index.md): the control plane whose live analytics plugin consumes Agent Analytics, which is the clearest example of this tool's agent-native purpose.

## Bottom line

**Recommended for builders shipping agent-built products who want a self-hostable, agent-queryable web analytics layer instead of a human dashboard.**
Not for observing coding-agent sessions, token cost, or provenance, despite living in this category.

## Changes

- 2026-09-27 - Created.
- 2026-10-07 - Added the Agent-Analytics/agent-analytics star history chart to the Status section.

## See also

- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins at the category's edge
- [agentsview](../agentsview/index.md) - the local session archive that answers the agent-history question this tool does not
- [agents-observe](../agents-observe/index.md) - the live coding-agent dashboard it parallels only in its real-time surface
- [Paperclip](../../control-planes/paperclip/index.md) - the control plane with a live analytics plugin that consumes this product

## References

- https://agentanalytics.sh/ - the pricing tiers, the free and metered cloud plans, and the agent-first pitch
- https://github.com/Agent-Analytics/agent-analytics - the open-source server repository, its activity, and the missing license file
- https://raw.githubusercontent.com/Agent-Analytics/agent-analytics/main/README.md - the capability list, self-host routes, and CLI usage
- https://docs.agentanalytics.sh/ - the docs home, the product-system model, and the list of access surfaces and integrations
- https://docs.agentanalytics.sh/openapi.yaml - the OpenAPI 3.1 spec and the agent-session and API-key auth model
- https://raw.githubusercontent.com/Agent-Analytics/agent-analytics-cli/main/README.md - the CLI command surface for analytics, funnels, and experiments
- https://api.github.com/repos/Agent-Analytics/agent-analytics - stars, creation and last-push dates, and the absent license as of 2026-09-27
- https://hn.algolia.com/api/v1/search?query=agentanalytics.sh - the empty Hacker News footprint behind the thin-community claim
