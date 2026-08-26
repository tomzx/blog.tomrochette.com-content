---
title: n8n
created: 2026-08-24
updated: 2026-08-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, executions, webhooks, workflow-automation]
readability: 3
audience_notes: >
  Engineers evaluating a self-hostable platform for webhook- and schedule-driven AI agents outside the repository.
  Assumes comfort with Docker, API keys, and reading a license.
---

n8n is a fair-code workflow automation platform with native AI capabilities, where webhook triggers, cron schedules, and chat channels start workflows and agents built on a visual canvas with code nodes.
Facts below verified as of 2026-08-24.

**n8n is the most credible webhook-triggered agent substrate with real engineering uptake, as long as you accept that it is not open source and your use of it is bounded by its license.**

## What it is

Workflows are directed graphs of nodes (1,500+ integrations per the README) that trigger on webhooks, schedules, chat messages, or app events, mixing JavaScript and Python code with visual steps.
The agents feature (in preview) adds first-class agents with a model, instructions, tools, skills, memory, sub-agents, and channels (Slack, Telegram, Linear), runnable on schedules from hourly to custom cron.
Deployment is self-hosted (free Community Edition) or n8n Cloud; the Webhook node exposes test and production URLs with basic, header, or JWT auth, IP allowlists, and streaming responses for AI agents.

## Status

**Very active and heavily funded.**
About 202k stars and 60.3k forks on GitHub as of 2026-08-24, with 23,000+ commits.
A $180M Series C (October 2025, led by Accel, with NVIDIA's NVentures) brought total funding to $240M at a $2.5B valuation.
Caveat on maturity: the agents layer is in preview, not yet supported on self-hosted Enterprise, and queue mode does not work with agents.

## Strengths

- **Webhook-to-agent is a one-node path**: an HTTP POST becomes an agent turn with authentication, allowlists, and response modes (immediate, final-node, or streaming) configured on the trigger itself.
- Model flexibility with no lock-in: any provider, bring your own keys, swap models without rebuilding.
- Publishing is snapshot-based: edits go to a draft while the published version keeps serving channels and schedules, and every publish is versioned and revertible.
- The community is large and real (a forum with tens of thousands of members, and HN launch threads from 728 points in 2019 to 235 points for the Series C).

## Cautions

- **The Sustainable Use License is not an open source license**: use is restricted to internal business purposes, and hosting n8n for others for money or white-labeling it is prohibited without a commercial agreement.
- The contributor agreement gives n8n the right to relicense contributed code, so forks cannot count on today's terms.
- Webhook conditionals fail open: if the `Only Run If` expression errors, n8n logs a warning and lets the request through, so treat it as routing, not enforcement.
- Preview-status rough edges: agents ignore queue mode (breaking scale-out), channels need a public `WEBHOOK_URL`, and one turn equals one billed execution, so chatty agents are hard to cost-predict.

## Pricing

Cloud plans bill per full workflow execution with unlimited users and steps: Starter at 20 EUR/month annually for 2,500 executions, Pro at 50 EUR for 10,000, Business at 667 EUR for 40,000, Enterprise by quote (as of 2026-08-24).
Self-hosting the Community Edition is free; Business-and-up self-hosted licenses ping n8n's license server daily and count your executions.

## Compared to

- [GitHub Agentic Workflows](../github-agentic-workflows/index.md): repository-centric execution with safe-output gates; n8n is integration-centric with the whole SaaS world as its toolbox.
- Zapier and Make: closed SaaS automation with per-step or per-operation billing; n8n gives you the source, self-hosting, and per-execution pricing.
- [OpenChamber](../openchamber/index.md): schedules coding-agent prompts on your machine; n8n schedules general agents against APIs, not repos.

## Bottom line

**Recommended for engineers who need external events (webhooks, chat, schedules) to drive agents with tools across dozens of services, and who will self-host.**
Not for anyone building a product whose value derives substantially from n8n itself, or who needs the agents layer hardened today.
My disagreeable claim: for scheduled and webhook-triggered coding-adjacent work, n8n plus a coding agent beats writing your own queue-and-cron service for most teams, and calling it "open source" (as much of the community does) is factually wrong and matters.

## See also

- [GitHub Agentic Workflows](../github-agentic-workflows/index.md) - the repo-centric execution substrate
- [Copilot automations](../copilot-automations/index.md) - hosted scheduling inside GitHub
- [Claude Code](../claude-code/index.md) - an MCP client that can build and manage n8n agents
- [OpenChamber](../openchamber/index.md) - local, self-hosted scheduling for coding sessions

## References

- https://github.com/n8n-io/n8n - repository scale and fair-code licensing, as of 2026-08-24
- https://docs.n8n.io/build/build-and-manage-agents.md - agents feature: channels, schedules, sub-agents, preview limits
- https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/ - webhook trigger semantics, auth, fail-open conditional
- https://n8n.io/pricing/ - plan tiers and execution-based billing, as of 2026-08-24
- https://docs.n8n.io/privacy-and-security/sustainable-use-license.md - license terms and the not-open-source statement
- https://blog.n8n.io/series-c/ - $180M Series C, $2.5B valuation, October 2025
- https://news.ycombinator.com/item?id=21191676 - the 2019 launch thread (728 points)
- https://news.ycombinator.com/item?id=45525336 - the Series C announcement thread (235 points)
