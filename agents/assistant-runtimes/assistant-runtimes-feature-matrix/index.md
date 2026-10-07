---
title: "Assistant Runtimes Feature Matrix"
created: 2026-08-27
updated: 2026-10-07
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, assistant-runtimes, personal-assistants]
readability: 3
audience_notes: >
  Engineers choosing a self-hosted assistant runtime, chat-channel or desktop, and deciding how much machine they are willing to trust.
  Assumes you know what a container and a cross-compiled binary are; each column links to a full note.
---

This matrix compares the fifteen assistant runtimes profiled in this section: the OpenClaw root, the three variants named after shrinking it, the learning-loop challenger, the readable Python core, the three Cowork-style desktops, the three channel-matrix platforms (AstrBot, Octop, and QwenPaw), and the three local-first platforms (AnythingLLM, Open WebUI, PrivateGPT).

**The family ladder is a trust ladder: OpenClaw is an ecosystem, NanoClaw an auditable codebase, ZeroClaw a static binary, PicoClaw a firmware image, Hermes a memory that grows, and the 2026 columns stretch the ladder again, Nanobot bets on readable Python, QwenPaw on channels and security defaults, OpenWork, Eigent, and OpenWorker carry the category onto the desktop as Cowork alternatives, OpenWorker the governed security-first newcomer, while AstrBot, the oldest member, is the IM-platform bet that predates the wave and outlives it, and Octop is the incumbent-vendor answer that joins that IM bet with multi-user household accounts.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [AnythingLLM](../anything-llm/index.md) | [AstrBot](../astrbot/index.md) | [Eigent](../eigent/index.md) | [Hermes](../hermes/index.md) | [Nanobot](../nanobot/index.md) | [NanoClaw](../nanoclaw/index.md) | [Octop](../octop/index.md) | [Open WebUI](../open-webui/index.md) | [OpenClaw](../openclaw/index.md) | [OpenWork](../openwork/index.md) | [OpenWorker](../openworker/index.md) | [PicoClaw](../picoclaw/index.md) | [PrivateGPT](../private-gpt/index.md) | [QwenPaw](../qwenpaw/index.md) | [ZeroClaw](../zeroclaw/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Runtime | Electron desktop plus multi-user Docker, Node | Python 3.12+ async platform, WebUI plus ChatUI | TypeScript Electron over Python (CAMEL) | Python (uv), single gateway | Python 3.11+ single core | TypeScript on Node | Python 3.12+ FastAPI, single process | Python, Docker-first web UI | TypeScript on Node | TypeScript Electron over OpenCode | Python agent server (aisuite) under a native desktop shell | single Go binary | Python API server | Python on AgentScope 2.0 | single Rust binary |
| License | ✓ MIT | ~ AGPL-3.0, strong copyleft | ✓ Apache-2.0 | ✓ MIT | ✓ MIT | ✓ MIT | ✓ MIT | ~ custom Open WebUI License (branding clause; BSD-3 through v0.6.5) | ✓ MIT | ~ MIT core, EE source-available | ✓ MIT | ✓ MIT | ✓ Apache-2.0 | ✓ Apache-2.0 | ✓ MIT OR Apache-2.0 |
| Born | 2023 (Show HN 2024-09-05) | 2022-12-08 | 2025-07-29 | 2025-07-22 | 2026-02-01 | 2026-01-31 | 2026-07-08 | 2023 (license change 2025-04-19) | 2025-11-24 | 2026-01-14 | 2026-07-20 | 2026-02-04 | 2023 (1.0 on 2026-06-03) | 2026-02-24 | 2026-02-13 |
| Stars | about 66.8k | about 41.5k | about 15.5k | about 252k | about 49k | about 31k | about 7.6k | about 154k | about 391k | about 23.9k | about 18.5k | about 30k | about 57.6k | about 35k | about 33k |
| Footprint | desktop app, Docker, Cloud, Android | self-hosted server platform, Docker, desktop app, NAS panels | Electron plus local backend | single gateway, seven backends | small readable core, WebUI in wheel | one process, containerized | single process, web dashboard, CLI, desktop clients | self-hosted Docker deployment, web UI | large, 70+ dependencies per the NanoClaw audit | Electron app wrapping OpenCode | desktop app with a local agent server and 25+ connectors | one binary, 10-20MB RAM | API server plus demo UI | full stack, local models included | one binary, any machine |
| Isolation model | ✗ desktop app on the host | ~ Agent Sandbox for code and shell, host-connected adapters | ~ host by default, cloud sandbox optional | ✓ isolated subagents, sandboxed backends | ~ localhost-first, config-driven | ✓ per-agent Linux containers | ~ workspace backends incl. Docker sandbox, tool approval, shell guardrails | ~ your server, your infra | app-level, sandboxing optional | ✗ host access by design | ~ host by default, NVIDIA OpenShell sandbox for commands | ~ v0.2.6 isolation support | ~ self-hosted, local models | ✓ five security layers, kernel sandbox | ~ own machine, tool grants |
| Channels | ~ desktop and web UI, Docker multi-user | 14+ official incl. QQ, WeCom, DingTalk, LINE, KOOK | ~ desktop UI, no chat apps | Telegram, Discord, Slack, WhatsApp, Signal, CLI | 8+ incl. Telegram, Discord, Slack, WeChat | 13+ installed as skills | 8 incl. Feishu, DingTalk, QQ, WeChat, WeCom | ~ web UI, multi-user | dozens incl. Signal, iMessage | ~ desktop app, web alpha | ~ desktop app and standing automations, no chat apps | many incl. WeCom, WeChat, IRC | ~ API-first, the UI is a demonstrator | 7 incl. DingTalk, WeChat, QQ, iMessage | 30+ incl. voice, webhooks |
| Providers | any major provider, local Ollama and LM Studio | OpenAI-compatible, Anthropic, Gemini, Ollama, Chinese gateways, Dify and Coze | BYOK, local Ollama/vLLM, cloud credits | any, Nous Portal, one-command switch | any OpenAI-compatible, Ollama, vLLM | Claude SDK plus codex, opencode, ollama skills | OpenAI-compatible, DashScope (Qwen), Ollama | Ollama and OpenAI-compatible backends | hosted plus local | any OpenCode provider (50+) | BYOK OpenAI, Anthropic, Google, or open weights, or local Ollama | many incl. Kimi, MiMo, Bedrock | Ollama, llama.cpp, vLLM, OpenAI-compatible | DashScope, major clouds, own small models offline | about 20 incl. Ollama |
| Edge and mobile | ✓ Android app | ✗ server and desktop only | ✗ desktop only | ~ $5 VPS, serverless idle on Modal, Daytona | ~ server deploys (Render) | ✗ Docker host only | ✗ desktop clients, mobile in closed beta | ~ responsive web and PWA | companion apps | ✗ desktop only | ✗ macOS and Windows desktop only | ✓ Android APK, $10 RISC-V boards | ✗ server only | ~ beta Tauri desktop | ~ Raspberry Pi |
| Credentials | your keys | your keys, providers set in the panel | your keys or cloud credits | per-provider keys or Nous Portal | your keys on host | ✓ OneCLI Agent Vault | your keys, per-expert providers | your keys | your keys on host | your keys BYO | your keys | your keys in workspace | your keys, local by default | your keys, or none offline | your keys in workspace |
| Security record | clean so far | silent-drop adapter bug fixed 2026-06, thin English-language scrutiny | GAIA claim corrected, astroturf flag | edited plagiarism-claim issue, 48k open issues | clean so far, category-skepticism thread | clean so far | clean so far, zero English-language scrutiny | clean so far, license controversy | provider saga, 514-point vuln report, Trail of Bits audit completed (23 confirmed vulnerabilities, all fixed) | HN boundary questions unresolved | open beta, macOS builds signed and notarized while Windows builds are unsigned, thin independent footprint | pre-1.0 banner, scam-token notice, picoclaw.io cert renewed after its 2026-09-10 expiry | clean so far | telemetry auto-accept default | clean so far, thin coverage |
| Status | active, v1.17.0 | active, v4.28.2 with a v4.29.0 beta, 1.6k open issues and PRs | active, v1.0.5 | active, 48k open issues | active, PyPI alpha | active, 2026.10.0 in release candidates, 1.0k open issues | active, v1.0.2b6 beta line, 736 open issues | active, v0.11.4 | active, v2026.9.8 stable plus an October-line beta, 9.4k open issues | active, v0.18.57 | active, v0.3.1, open beta | active, 51 open issues, pre-1.0 | active, v1.0.1, pushed 2026-10-07 | active, v2.2.1, post-rewrite churn | active, v0.8.5, 949 open issues |

## Reading the matrix

**The isolation and credentials rows are the ones that bite: only NanoClaw containers the agent and vaults the keys by default, QwenPaw ships the strongest default posture (five security layers including a kernel sandbox), while OpenWork and Eigent run on your host by design, the trade for being desktop apps.**
PicoClaw's isolation is a recent feature flag rather than an architecture, and ZeroClaw's answer is that the binary itself is small enough to trust.

**The providers row hides the family's politics: the root endured Google and Anthropic restricting subscriptions for it in 2026, so check your provider's current stance toward this family before standardizing.**
QwenPaw is the only column with a real offline path through its own trained small models.

**The desktop split is the new category line: OpenWork, Eigent, and OpenWorker do not do chat channels at all, which is why their cells go tilde there, and choosing between them and the messaging runtimes is really choosing between an assistant that lives in your chats and one that lives on your desktop.**

**The status row's issue counts are inversely proportional to age, not quality: the root carries 9.4k open issues at scale, and the pre-1.0 PicoClaw carries 51, so read the column against its birthday.**

**Hermes is the column that breaks the -claw pattern: it competes on the learning loop rather than the trust ladder, and its about 252k stars against a 48k-issue backlog is the trade in one row pair.**

## Choosing from the matrix

- Want the ecosystem, channels, and companion apps and accept the weight: OpenClaw.
- Want the assistant to compound (skills, memory, user model) and will supervise it: Hermes.
- Want to read every line and cage the agent: NanoClaw.
- Want to stop needing to read it, or run on a Pi: ZeroClaw.
- Want it on a microcontroller or salvage hardware, pre-1.0 accepted: PicoClaw.
- Want a readable Python core you can extend: Nanobot, binding to localhost and owning the security surface.
- Want the deepest chat-channel matrix including Chinese IM platforms, plus a 1,000-plugin marketplace: AstrBot.
- Want the Chinese channel matrix with an offline path through its own trained small models: QwenPaw.
- Want a Cowork-style desktop on OpenCode with skills that port via MCP: OpenWork.
- Want a governed, security-first desktop coworker that finishes tasks on your own keys: OpenWorker.
- Want a Cowork-style desktop with multi-agent workforces under Apache-2.0: Eigent.

## Changes

- 2026-08-27 - Created with four columns and twelve rows and the trust-ladder thesis.
- 2026-08-27 - Extended to five columns with Hermes inserted, and the reading section gained the learning-loop-versus-trust-ladder line.
- 2026-08-30 - Nanobot, OpenWork, Eigent, and QwenPaw columns added, matrix at nine columns, with desktop-split prose added.
- 2026-09-13 - Removed the archived Android port from ZeroClaw's edge and mobile cell and corrected its open-issue count to 824.
- 2026-09-20 - Re-verification: moved the OpenClaw status cell to v2026.9.5 with 8.1k open issues, dropped the note-ungrounded v2026.9.14 from the Hermes status cell, moved the PicoClaw status cell to 40 open issues, and recorded picoclaw.io's expired TLS certificate in its security-record cell.
- 2026-09-21 - Re-verification: refreshed drifted cells (Hermes 43k open issues, OpenClaw 8.2k, PicoClaw 38, ZeroClaw 762, OpenWork stars to about 23.7k).
- 2026-09-22 - Re-verification: recorded OpenClaw's completed Trail of Bits audit (23 confirmed vulnerabilities, all fixed) in its security-record cell and refreshed drifted cells (Eigent about 15.4k stars, Hermes about 248k stars and 44k open issues, OpenClaw 8.3k, PicoClaw 33, ZeroClaw 740).
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-24 - Re-verification: refreshed drifted cells (Hermes 43k open issues, OpenClaw v2026.9.6 with 8.6k open issues, PicoClaw 38, ZeroClaw 757).
- 2026-09-27 - Re-verification: refreshed drifted cells (Eigent v1.0.5, Hermes about 249k stars and 44k open issues, OpenClaw 8.7k, PicoClaw 40, ZeroClaw 763) and corrected the opening sentence's stale nine-runtime count to twelve.
- 2026-09-29 - Re-verification: refreshed drifted cells (Hermes about 250k stars and 45k open issues, OpenClaw 8.9k, PicoClaw 51 with its picoclaw.io certificate renewed, ZeroClaw 701, OpenWork about 23.8k stars).
- 2026-10-02 - Re-verification: moved cells (OpenClaw status to v2026.9.7 with 9.2k open issues and stars about 391k, AnythingLLM status to v1.17.0 and stars about 66.7k, Open WebUI stars about 153.8k, Hermes 48k open issues, PicoClaw 59, ZeroClaw 848, PrivateGPT pushed 2026-09-29, Eigent stars about 15.5k, Nanobot stars about 49k) and matching prose counts.
- 2026-10-03 - OpenWorker column added (the Andrew Ng team's governed MIT desktop beta, the category's thirteenth member), re-sorted alphabetically, with volatile cells refreshed (OpenClaw status to v2026.9.8 with 9,157 open issues, ZeroClaw 902 open issues, PrivateGPT pushed 2026-10-02) and matching prose counts.
- 2026-10-06 - AstrBot column added (the AGPL-3.0 IM-platform veteran from 2022, the category's fourteenth member), re-sorted alphabetically, with drifted cells refreshed (Open WebUI stars about 154k, OpenClaw status to a stable-plus-October-beta split with 9.4k open issues, OpenWorker status to v0.3.1, NanoClaw status to the 2026.10.0 release candidates, ZeroClaw status to v0.8.5, PicoClaw 51 open issues, PrivateGPT pushed 2026-10-06) and matching prose counts.
- 2026-10-07 - Octop column added (Tencent Cloud's multi-user, IM-first assistant platform, the category's fifteenth member), re-sorted alphabetically, with drifted cells refreshed (stars row to 2026-10-07 counts, OpenWork status to v0.18.57, ZeroClaw to 949 open issues, PrivateGPT pushed 2026-10-07) and matching prose counts.

## See also

- [Control Planes Feature Matrix](../../control-planes/control-planes-feature-matrix/index.md) - the layer that manages these as employees
- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - the coding-agent cousins
- [Read the Commits, Not the Manual](../../../learnings-from-openclaw/index.md) - maintaining the root at scale
- [Managing Many Concurrent LLM Agent Sessions](../../../managing-many-llm-agent-sessions/index.md) - the supervision context

## References

- https://github.com/openclaw/openclaw - Gateway model, channels, security posture
- https://github.com/NousResearch/hermes-agent - learning loop, backends, providers for the Hermes column
- https://github.com/nanocoai/nanoclaw - container isolation, vault, skill-based channels
- https://github.com/zeroclaw-labs/zeroclaw - runtime model, provider and channel counts
- https://github.com/sipeed/picoclaw - footprint, architectures, security banners
- https://github.com/HKUDS/nanobot - stars, alpha status, and surfaces for the Nanobot column
- https://github.com/different-ai/openwork - the OpenWork column: OpenCode base, split license, adoption
- https://github.com/eigent-ai/eigent - the Eigent column: CAMEL workforce, Apache-2.0, maturity
- https://github.com/AstrBotDevs/AstrBot - the AstrBot column: the IM-platform veteran's channels, plugin marketplace, and Agent Sandbox
- https://github.com/agentscope-ai/QwenPaw - the QwenPaw column: channels, security layers, offline models
- https://github.com/andrewyng/openworker - the OpenWorker column: the governed desktop beta, MIT license, OpenShell sandbox integration
