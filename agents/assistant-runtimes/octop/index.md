---
title: Octop
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, assistant-runtimes, personal-assistants, python, self-hosted, open-source]
readability: 3
audience_notes: >
  Engineers choosing a self-hosted assistant for a household or small team that lives in Chinese
  enterprise IM platforms, and anyone tracking what incumbent cloud vendors build when they enter
  the assistant-runtime wave.
  Assumes you know what a chat channel integration and a multi-user web app are.
---

Octop is Tencent Cloud's MIT-licensed, self-hosted AI assistant platform: one Python process serves a web dashboard, a CLI, native desktop clients, and eight-plus IM channels for a multi-user household or team, and each member gets their own team of specialized "experts".

**Octop is what the assistant-runtime wave looks like when an incumbent vendor builds it: multi-user by default, Tencent-enterprise-IM first, and composed from four small sub-repos (harness, gateway, memory, browser) instead of one monolith, at 7.6k stars within three months of launch.**

## What it is

A Python 3.12+ FastAPI application that runs as a single restart-safe process: state lives in a control-plane database under `~/.octop/` (SQLite by default, PostgreSQL optional), and every surface (web dashboard, IM, cron) routes through one in-process HarnessProcessor.
Users get "experts", per-user agent profiles with their own workspace, providers, channels, and cron, plus 16 MBTI persona templates, an expert market for sharing configurations, and an AgentTeams beta where a coordinator schedules multiple experts on multi-step work.
The IM bridge (octop-gateway) normalizes Feishu, DingTalk, QQ, WeChat, WeCom, Telegram, and Discord into one processing pipeline, and ACP works in both directions: `octop acp` serves your Octop agent to Zed or OpenCode, and outbound runners delegate to OpenCode, Claude Code, CodeBuddy, or Codex with permission gates.
Providers are OpenAI-compatible APIs, DashScope (Qwen), Ollama, and other presets configured per agent, with a RAG knowledge base, CDP-based browser automation, remote desktop, and plugins rounding out the surface.
It is published under the TencentCloud GitHub org and built from four focused sub-repos: octop-harness (the agent runtime), octop-gateway, octop-memory, and octop-browser.

## Status

Fast out of the gate and young: 7,555 stars and 916 forks in its first three months as of 2026-10-07 (created 2026-07-08, pushed 2026-10-06), 736 open issues, MIT.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=TencentCloud/Octop&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=TencentCloud/Octop&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=TencentCloud/Octop&type=date&legend=top-left" />
</picture>

GitHub releases run a beta line (v1.0.2b4 on 2026-09-27 through v1.0.2b6 on 2026-10-04) while PyPI's stable `octop` package sits at 1.0.1, and the README carries a Trendshift trending badge.
**The adoption curve is the fastest first quarter in this category after the 2026 wave, and the scrutiny record is the exact AstrBot profile at a third of the age: one 1-point Hacker News thread, zero English-language technical coverage, so the vetting so far has happened in Chinese-language channels you are probably not reading.**

## Strengths

- Multi-user from day one: household and team accounts with JWT isolation, expert sharing, and a shared skill pool, which every other runtime in this category treats as an afterthought or omits.
- The Tencent enterprise IM matrix (Feishu, DingTalk, WeCom, QQ, WeChat) through a normalizing gateway, alongside Telegram and Discord.
- ACP in both directions, serving your agent to IDEs and delegating out to coding agents, a symmetry no other member offers.
- The composable sub-repo architecture (harness, gateway, memory, browser) keeps the pieces independently evaluable.

## Cautions

- Zero English-language technical scrutiny: the only independent trace this run found is a 1-point Hacker News thread from 2026-10-06.
- The release line is beta-tagged (v1.0.2b6) and PyPI lags GitHub, so pin versions deliberately.
- The one-line installer pulls its script from a Tencent Cloud COS bucket, and the docs, community, and channel gravity are China-first like AstrBot and QwenPaw.
- The runtime sub-repo (octop-harness) stands at 39 stars, which says the ecosystem is the org's own code rather than a community.

## Pricing

N/A, free and open source under MIT, self-hosted.
Your costs are model keys and the machine you run it on; a managed-agents cloud option is on the roadmap, not shipped.

## Compared to

- [AstrBot](../astrbot/index.md): the older IM-platform veteran with the wider platform table and the 1,000-plugin marketplace; choose AstrBot for platform breadth and community, Octop for multi-user expert teams and the Tencent-suite connectors.
- [QwenPaw](../qwenpaw/index.md): the other China-channel runtime; choose QwenPaw for the offline path through its own trained small models and the five-layer security stack, Octop for multi-user accounts and ACP.
- [OpenClaw](../openclaw/index.md): the single-operator ecosystem root; choose OpenClaw for channel and companion depth, Octop when the assistant must serve a household or team with separate accounts.

## Bottom line

**Recommended for households and small teams whose assistant must live in Feishu, DingTalk, QQ, or WeChat, and who want per-user expert isolation under an MIT license.**
Not for anyone who needs independent security scrutiny before adopting, or a Western-IM-first deployment.
The disagreeable claim I will defend: multi-user is the assistant category's next battleground, and an incumbent vendor shipped it first while every community favorite still assumes one operator.

## Changes

- 2026-10-07 - Created from the entrant scan as the category's fifteenth member.

## See also

- [AstrBot](../astrbot/index.md) - the IM-platform veteran it most overlaps with
- [QwenPaw](../qwenpaw/index.md) - the other China-channel matrix, with the offline counterbet
- [OpenClaw](../openclaw/index.md) - the single-operator root of the category
- [Assistant Runtimes Feature Matrix](../assistant-runtimes-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/TencentCloud/Octop - repository, license, and adoption numbers as of 2026-10-07
- https://raw.githubusercontent.com/TencentCloud/Octop/main/README.md - architecture, experts, channels, ACP, roadmap, install paths
- https://api.github.com/repos/TencentCloud/Octop/releases?per_page=3 - the v1.0.2b4 through v1.0.2b6 beta line (2026-09-27 through 2026-10-04)
- https://pypi.org/pypi/octop/json - the PyPI stable channel at 1.0.1 while GitHub runs v1.0.2b6
- https://github.com/TencentCloud/octop-harness - the agent-runtime sub-repo and its 39-star footprint
- https://hn.algolia.com/api/v1/items/49976872 - the single 1-point Hacker News thread (2026-10-06), the zero-scrutiny evidence
- https://trendshift.io/repositories/95504 - the Trendshift trending badge the README carries
