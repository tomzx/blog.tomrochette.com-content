---
title: Eigent
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, assistant-runtimes, cowork, multi-agent, open-source]
readability: 3
audience_notes: >
  Engineers choosing a desktop app for visually supervised multi-agent work with permissive licensing.
  Assumes you know what MCP tools and a BYOK model are.
---

Eigent is an Apache-2.0, Electron-based desktop app for building and running AI agent workforces, specialized worker agents executing tasks in parallel on the CAMEL-AI framework, with a large built-in MCP integration catalog, browser and terminal toolkits, human-in-the-loop escalation, and automations, positioned as the free and local alternative to Claude Cowork.
Facts below verified as of 2026-08-30.

**Eigent is the only Cowork-style desktop in this category with a permissive license and a real multi-agent architecture, and its history includes a corrected benchmark claim that should calibrate how much of the pitch you take on faith.**

## What it is

A TypeScript Electron frontend over a Python FastAPI backend, organized as Space, Session, Task, with two modes: a single-agent harness and a multi-agent Workforce where specialized workers execute in parallel (built on the founder's CAMEL-AI framework).
Tools include an extensive MCP integration catalog, a skills system, browser and terminal toolkits, and human-in-the-loop escalation; automations cover scheduled, event, and app triggers.
Model-agnostic: BYOK cloud APIs, Eigent Cloud credits, or local models via Ollama, vLLM, LM Studio, and SGLang; full self-hosting with a local backend is documented.
macOS (Intel and Apple Silicon), Windows, and Linux.
By Eigent AI (EIGENT UK LTD), founded by Guohao Li, who also founded CAMEL-AI; funding undisclosed.

## Status

Active and maturing: 15,160 stars, 1,801 forks, 213 open issues as of 2026-08-30, created 2025-07-29, pushed 2026-08-28, v1.0.3 released that day.
**The smallest community of the Cowork trio, and the launch thread matters: the "ranked top 1 on GAIA benchmark" claim referred to the predecessor project OWL, the founder acknowledged it, and 1-karma accounts posted praise.**

## Strengths

- Apache-2.0 with a documented full self-hosting path, cleaner than the custom licenses around it.
- The CAMEL-based Workforce is a genuine multi-agent architecture, not a single harness with a spinner.
- Model and deployment freedom: BYOK, an extensive MCP tool catalog, local inference, no subscription required to use it.
- Cross-platform with an enterprise tier already offered.

## Cautions

- The marketing-claim history above, plus self-reported revenue figures and undisclosed funding.
- "Local and free" needs qualification: the quick-start path connects to Eigent cloud and requires an account; fully local is a separate, more involved setup.
- Heavy stack (Electron plus Python) and a smaller community than its direct rivals.
- Teams tier still marked coming soon.

## Pricing

Free: BYOK and local models, 1,000 registration credits.
Plus $19.99/month (2,000 task credits), Pro $99.99/month (10,000 credits), Teams coming soon, Enterprise custom with local deployment.
Ten percent of subscriptions is pledged to CAMEL-AI.org.

## Compared to

- [OpenWork](../openwork/index.md): the larger, OpenCode-based Cowork alternative with an MCP portability story; choose Eigent for true multi-agent workforces and the permissive license, OpenWork for ecosystem and skills portability.
- [OpenClaw](../openclaw/index.md): the messaging-first always-on assistant; choose OpenClaw for phone-driven personal assistance, Eigent for desktop-supervised work on files and tasks.
- Claude Cowork: polished, sandboxed, subscription-tied; choose Cowork for turnkey security management, Eigent for model freedom, local deployment, and parallel agent teams.

## Bottom line

**Recommended for engineers who want to visually run parallel specialist agents on their own hardware under a permissive license.**
Not for buyers who need vendor accountability history, and not for the quick-start path if local-only is the requirement, because that path phones home.

## See also

- [Assistant Runtimes Feature Matrix](../assistant-runtimes-feature-matrix/index.md) - the category comparison this note joins
- [OpenWork](../openwork/index.md) - the OpenCode-based rival
- [OpenClaw](../openclaw/index.md) - the messaging-first root of the category
- [Hermes](../hermes/index.md) - the learning-loop runtime

## References

- https://github.com/eigent-ai/eigent - repository, stack, license, adoption numbers
- https://raw.githubusercontent.com/eigent-ai/eigent/HEAD/README.md - features and deployment paths
- https://www.eigent.ai/pricing - the tiers and credits for the pricing rows
- https://www.eigent.ai/about - the company and CAMEL-AI relationship
- https://news.ycombinator.com/item?id=44736010 - the corrected GAIA claim and astroturfing flag, the critical source
- https://claude.com/blog/cowork-research-preview - the Cowork comparison baseline
