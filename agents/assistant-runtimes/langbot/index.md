---
title: LangBot
created: 2026-10-30
updated: 2026-10-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, assistant-runtimes, python, chat-channels, plugins, open-source]
readability: 3
audience_notes: >
  Engineers operating LLM bots as a managed service across instant-messaging platforms, especially
  mixed Western-and-Chinese channel fleets, who care about operations guardrails more than personal
  companionship.
  Assumes you know what a chat channel adapter and a plugin marketplace are.
---

LangBot is an Apache-2.0 Python platform for building agentic instant-messaging bots, connecting LLMs to Discord, Telegram, Slack, LINE, QQ, WeChat, WeCom, Lark, DingTalk, KOOK, and Matrix through a multi-pipeline architecture with a web management dashboard, a separate plugin market, and MCP support.

**LangBot is the member that treats the assistant as an operated service rather than a personal companion: access control, rate limiting, sensitive-word filtering, and monitoring are the headline features, and that framing is exactly why an operations team should look at it and a single player probably should not.**

## What it is

A Python 3.11+ platform (the PyPI package classifies itself Production/Stable) launched as `uvx langbot` with a webUI on localhost:5300, deployable also through Docker Compose or the hosted LangBot Cloud.
The multi-pipeline architecture runs different bots for different scenarios in one deployment, each with its own configuration, and a browser dashboard configures and monitors them all without YAML editing.
Plugins are a separate install from the project's plugin market, and the integration list leans on agent platforms: Dify, Coze, n8n, Langflow, Deerflow, and Tencent's Weknora beside native LLM providers.
Created 2022-12-07, one day before AstrBot, and now maintained under the langbot-app org with bilingual documentation and a Chinese-first community alongside a Discord server.

## Status

Active and steady: 18,601 stars and 1,676 forks as of 2026-10-30, created 2022-12-07, 144 open issues with the last push on 2026-10-30, Apache-2.0.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=langbot-app/LangBot&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=langbot-app/LangBot&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=langbot-app/LangBot&type=date&legend=top-left" />
</picture>

The v4.11 line is current: v4.11.0 shipped 2026-10-14 after two release candidates, v4.11.1 and v4.11.2 followed on 2026-10-20 and 2026-10-22, and v4.11.4 landed 2026-10-29 on GitHub and PyPI the same day, with PyPI classifying the package Production/Stable.
**The scrutiny record is the exact AstrBot and Octop profile: an HN search returns only an unrelated 2024 namesake translation demo, so the eighteen thousand stars and the production claims have been vetted in Chinese-language channels and a Discord server you are probably not reading.**

## Strengths

- The production guardrails (access control, rate limiting, sensitive-word filtering, monitoring, exception handling) are first-class features rather than a self-hosting afterthought.
- The multi-pipeline model fits operating several distinct bots for several audiences from one deployment, which the single-operator members in this category deliberately do not do.
- Eleven named IM platforms including Matrix, LINE, and KOOK beside the Chinese trio, the widest single-vendor matrix in the category.
- Apache-2.0, the permissive-license option in the IM-platform wing where AstrBot carries AGPL-3.0.

## Cautions

- Zero English-language technical scrutiny, and the production-readiness claims are the project's own.
- Plugins install separately from the core, so a bare `uvx langbot` deploy is smaller than the platform's capability list suggests.
- The hosted Cloud console is the README's recommended path, and the gravity toward it is the same managed-platform pull Open WebUI's license thread argued about.
- The Chinese-ecosystem gravity (QQ support channels, Chinese-first docs, Weknora integration) assumes infrastructure and norms that travel poorly.

## Pricing

N/A, free and open source under Apache-2.0, self-hosted.
Your costs are model keys and the machine or VPS you run it on.
LangBot Cloud, the managed hosting path, is sold through the cloud console with no public price in the page markup (as of 2026-10-30).

## Compared to

- [AstrBot](../astrbot/index.md): the one-day-younger IM-platform veteran with the 1,000-plus-plugin marketplace and AGPL-3.0; choose AstrBot for the extension economy, LangBot for the production guardrails and the permissive license.
- [Octop](../octop/index.md): the multi-user household platform; choose Octop when separate human accounts with their own experts are the requirement, LangBot when separate bot pipelines are.
- [OpenClaw](../openclaw/index.md): the single-operator personal ecosystem; choose OpenClaw for a personal assistant that lives in your chats, LangBot for bots operated as a service for other people.

## Bottom line

**Recommended for teams operating LLM bots across IM platforms as a managed service under a permissive license.**
Not for a single player who wants a personal assistant, or anyone who needs independent security scrutiny before adopting.

## Changes

- 2026-10-30 - Created from the dedicated-source scan as the category's sixteenth member, recording the Apache-2.0 IM-platform platform with its production-guardrails bet and the zero-English-scrutiny signal.

## See also

- [AstrBot](../astrbot/index.md) - the platform twin it shares its birthday week and community profile with
- [Octop](../octop/index.md) - the other operated multi-actor platform, households against pipelines
- [QwenPaw](../qwenpaw/index.md) - the channel-matrix counterpart with the offline models
- [Assistant Runtimes Feature Matrix](../assistant-runtimes-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/langbot-app/LangBot - repository, positioning, platform and integration lists
- https://raw.githubusercontent.com/langbot-app/LangBot/HEAD/README.md - capabilities, quick-start paths, plugin-market split
- https://api.github.com/repos/langbot-app/LangBot - stars, forks, issues, license, and dates as of 2026-10-30
- https://api.github.com/repos/langbot-app/LangBot/releases?per_page=4 - the v4.11 line from v4.11.0 (2026-10-14) to v4.11.4 (2026-10-29)
- https://pypi.org/pypi/langbot/json - the Production/Stable classification, the Python floor, and the PyPI release dates
- https://langbot.app/docs/en/insight/features - the feature documentation entry
- https://space.langbot.app/cloud - the LangBot Cloud hosted path, no public price in the page markup
- https://hn.algolia.com/api/v1/search?query=LangBot&tags=story&hitsPerPage=6 - the HN footprint search returning only an unrelated 2024 namesake, the zero-scrutiny evidence
