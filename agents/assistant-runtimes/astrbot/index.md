---
title: AstrBot
created: 2026-10-06
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, assistant-runtimes, python, chat-channels, plugins, open-source]
readability: 3
audience_notes: >
  Engineers choosing a self-hosted assistant that must live in IM platforms, especially the Chinese
  messaging ecosystems, and weighing the plugin-marketplace platform bet against AGPL licensing and
  a thin English-language scrutiny record.
---

AstrBot is an AGPL-3.0 Python agent-chatbot platform, started by Soulter in 2022 and now under the AstrBotDevs org, that turns QQ, WeChat, WeCom, Lark, DingTalk, Telegram, Slack, Discord, LINE, and a dozen more IM platforms into agent surfaces with a 1,000-plus-plugin marketplace, MCP and skills support, an agent sandbox, and a WebUI.

**AstrBot is the category's veteran: it predates the -claw wave by three years and won the Chinese IM ecosystem first, which is why it has OpenClaw-scale adoption (41.5k stars) with almost no Hacker News footprint, and why its repo description now markets it as an "openclaw alternative".**

## What it is

A Python 3.12+ asynchronous platform deployable as a `uv tool install astrbot` one-liner, Docker or Docker Compose, a desktop app (AstrBot-desktop), a Windows launcher, NAS panels (CasaOS, 1Panel, BT-Panel), or RainYun one-click cloud.
Official adapters cover QQ, OneBot v11, Telegram, WeCom and its AI bot, WeChat Official Accounts, Feishu (Lark), DingTalk, Slack, Discord, LINE, Satori, KOOK, Misskey, and Mattermost, with Matrix, Rocket.Chat, and VoceChat as community plugins and WhatsApp marked coming soon.
Model providers span OpenAI-compatible endpoints, Anthropic, Gemini, Moonshot, Zhipu, DeepSeek, Ollama, and LM Studio, plus a long table of Chinese API gateways, and the platform also bridges to the Dify, Alibaba Bailian, and Coze agent platforms; STT and TTS are built in.
The agent layer has sub-agents, tool calls, workflow orchestration, context compression, a knowledge base, native MCP and skills, and an Agent Sandbox for isolated code and shell execution, all managed through a visual WebUI and a web ChatUI.

## Status

Active and long-lived: 41,466 stars, 3,023 forks, and 1,612 open issues and pull requests as of 2026-10-06, created 2022-12-08, pushed 2026-10-06, AGPL-3.0.
The cadence is steady: v4.28.1 (2026-09-14), v4.28.2 (2026-09-27), and a v4.29.0-beta.1 prerelease (2026-10-01).
The community runs through 15-plus QQ groups, a Discord server, HelloGitHub, and Trendshift, not through HN or the Western blogosphere, and that shows in the record: an Algolia story search for AstrBot returns only astroturfing threads it typo-matches, no AstrBot story at all.
**The missing independent footprint is the signal to weigh before trusting it: adoption this size with zero English-language technical scrutiny means the vetting has happened in QQ groups you are probably not reading.**

## Strengths

- The deepest official channel matrix in this category, 14-plus platforms, including the LINE, KOOK, and Misskey surfaces nothing else here touches.
- A plugin marketplace with 1,000-plus plugins, the category's largest extension economy after OpenClaw's.
- The Agent Sandbox makes isolated code and shell execution a first-class feature rather than a configuration afterthought.
- Deployment breadth from a single uv command to NAS app stores, rare for runtimes in this weight class.

## Cautions

- AGPL-3.0 is the category's only strong copyleft license: hosting it for others as a service triggers source obligations the MIT and Apache members do not carry.
- The repo's provider table mixes documentation with referral links (CompShare, 302.AI, PPIO carry affiliate codes), so treat the recommended gateways as sponsor relationships, not neutral picks.
- Silent-drop adapter bugs are the recorded failure class: the QQ official adapter dropped all non-@ group messages until a fix merged in June 2026 (issue 8131), and the docs are Chinese-first with English translations lagging.
- China-ecosystem gravity is structural: QQ-group support, Afdian sponsorship, and RainYun deployment assume infrastructure and norms that travel poorly.

## Pricing

N/A, free and open source under AGPL-3.0, self-hosted.
Your costs are model keys and the hosting you choose; the project is sponsored through Afdian, and the RainYun one-click path is a third-party paid host.

## Compared to

- [QwenPaw](../qwenpaw/index.md): the closest overlap, the other China-channel-matrix runtime; choose AstrBot for the wider platform table and plugin marketplace, QwenPaw for the offline path through its own trained small models and the five-layer security stack.
- [OpenClaw](../openclaw/index.md): the ecosystem root; choose OpenClaw for Western channels, companion apps, and the skills economy, AstrBot for QQ and WeChat first.
- [Nanobot](../nanobot/index.md): the readable-Python-minimalism pick; choose Nanobot to own a small core, AstrBot to inherit a platform.

## Bottom line

**Recommended for engineers whose assistant must live in QQ, WeChat, WeCom, Lark, or DingTalk, and for anyone who wants a plugin-marketplace platform instead of a minimal core.**
Not for anyone who needs permissive licensing for a hosted offering, or who cannot vet a runtime whose technical scrutiny lives in QQ groups.

## Changes

- 2026-10-06 - Created from the entrant scan as the category's fourteenth member.

## See also

- [QwenPaw](../qwenpaw/index.md) - the nearest rival on the channel matrix, with the offline-model counterbet
- [OpenClaw](../openclaw/index.md) - the root runtime whose repo description now names AstrBot as an alternative
- [Nanobot](../nanobot/index.md) - the other lightweight Python path, minimalism against platform
- [Assistant Runtimes Feature Matrix](../assistant-runtimes-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/AstrBotDevs/AstrBot - repository, description, license, adoption numbers as of 2026-10-06 (via the API)
- https://raw.githubusercontent.com/AstrBotDevs/AstrBot/HEAD/README.md - features, platform and provider tables, deployment paths, community surfaces
- https://api.github.com/repos/AstrBotDevs/AstrBot - stars, forks, issues, license, and dates as of 2026-10-06
- https://api.github.com/repos/AstrBotDevs/AstrBot/releases?per_page=3 - v4.28.1 (2026-09-14), v4.28.2 (2026-09-27), v4.29.0-beta.1 (2026-10-01)
- https://astrbot.app/ - the product landing, a thin page whose body renders client-side (the "Agentic AI 助手" tagline and the docs, blog, roadmap, and plugin portals serve in the HTML)
- https://docs.astrbot.app/en/ - the English documentation entry
- https://github.com/AstrBotDevs/AstrBot/issues/8131 - the QQ official adapter's silent drop of non-@ group messages, fixed by PR 8838 in June 2026, the critical source (via the API)
- https://hn.algolia.com/api/v1/search?query=AstrBot&tags=story&hitsPerPage=10 - the HN footprint search returning only astroturfing typo-matches, the zero-footprint evidence
