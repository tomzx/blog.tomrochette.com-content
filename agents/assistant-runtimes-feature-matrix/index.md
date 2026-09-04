---
title: "Assistant Runtimes Feature Matrix"
created: 2026-08-27
updated: 2026-09-04
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, assistant-runtimes, personal-assistants]
readability: 3
audience_notes: >
  Engineers choosing a self-hosted assistant runtime, chat-channel or desktop, and deciding how much machine they are willing to trust.
  Assumes you know what a container and a cross-compiled binary are; each column links to a full note.
---

This matrix compares the nine assistant runtimes profiled in this section: the OpenClaw root, the three variants named after shrinking it, the learning-loop challenger, the readable Python core, the two Cowork-style desktops, and the channel-matrix newcomer.
Everything below was verified against live sources on 2026-08-30 and re-verified on 2026-09-02 and 2026-09-04.

**The family ladder is a trust ladder: OpenClaw is an ecosystem, NanoClaw an auditable codebase, ZeroClaw a static binary, PicoClaw a firmware image, Hermes a memory that grows, and the 2026 columns stretch the ladder again, Nanobot bets on readable Python, QwenPaw on channels and security defaults, and OpenWork and Eigent carry the category onto the desktop as Cowork alternatives.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Eigent](../eigent/index.md) | [Hermes](../hermes/index.md) | [Nanobot](../nanobot/index.md) | [NanoClaw](../nanoclaw/index.md) | [OpenClaw](../openclaw/index.md) | [OpenWork](../openwork/index.md) | [PicoClaw](../picoclaw/index.md) | [QwenPaw](../qwenpaw/index.md) | [ZeroClaw](../zeroclaw/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Runtime | TypeScript Electron over Python (CAMEL) | Python (uv), single gateway | Python 3.11+ single core | TypeScript on Node | TypeScript on Node | TypeScript Electron over OpenCode | single Go binary | Python on AgentScope 2.0 | single Rust binary |
| License | ✓ Apache-2.0 | ✓ MIT | ✓ MIT | ✓ MIT | ✓ MIT | ~ MIT core, EE source-available | ✓ MIT | ✓ Apache-2.0 | ✓ MIT OR Apache-2.0 |
| Born | 2025-07-29 | 2025-07-22 | 2026-02-01 | 2026-01-31 | 2025-11-24 | 2026-01-14 | 2026-02-04 | 2026-02-24 | 2026-02-13 |
| Stars | about 15.2k | about 241k | about 47.7k | about 30.7k | about 389k | about 23.3k | about 29.9k | about 34.9k | about 32.7k |
| Footprint | Electron plus local backend | single gateway, seven backends | small readable core, WebUI in wheel | one process, containerized | large, 70+ dependencies per the NanoClaw audit | Electron app wrapping OpenCode | one binary, 10-20MB RAM | full stack, local models included | one binary, any machine |
| Isolation model | ~ host by default, cloud sandbox optional | ✓ isolated subagents, sandboxed backends | ~ localhost-first, config-driven | ✓ per-agent Linux containers | app-level, sandboxing optional | ✗ host access by design | ~ v0.2.6 isolation support | ✓ five security layers, kernel sandbox | ~ own machine, tool grants |
| Channels | ~ desktop UI, no chat apps | Telegram, Discord, Slack, WhatsApp, Signal, CLI | 8+ incl. Telegram, Discord, Slack, WeChat | 13+ installed as skills | dozens incl. Signal, iMessage | ~ desktop app, web alpha | many incl. WeCom, WeChat, IRC | 7 incl. DingTalk, WeChat, QQ, iMessage | 30+ incl. voice, webhooks |
| Providers | BYOK, local Ollama/vLLM, cloud credits | any, Nous Portal, one-command switch | any OpenAI-compatible, Ollama, vLLM | Claude SDK plus codex, opencode, ollama skills | hosted plus local | any OpenCode provider (50+) | many incl. Kimi, MiMo, Bedrock | DashScope, major clouds, own small models offline | about 20 incl. Ollama |
| Edge and mobile | ✗ desktop only | ~ $5 VPS, serverless idle on Modal, Daytona | ~ server deploys (Render) | ✗ Docker host only | companion apps | ✗ desktop only | ✓ Android APK, $10 RISC-V boards | ~ beta Tauri desktop | ~ Android port, Raspberry Pi |
| Credentials | your keys or cloud credits | per-provider keys or Nous Portal | your keys on host | ✓ OneCLI Agent Vault | your keys on host | your keys BYO | your keys in workspace | your keys, or none offline | your keys in workspace |
| Security record | GAIA claim corrected, astroturf flag | edited plagiarism-claim issue, 39.3k open issues | clean so far, category-skepticism thread | clean so far | provider saga plus a 514-point vuln report | HN boundary questions unresolved | pre-1.0 banner, scam-token notice | telemetry auto-accept default | clean so far, thin coverage |
| Status | active, v1.0.3 | active, v2026.8.31, 39.3k open issues | active, PyPI alpha | active, 1k open issues | active, 2.0 shipped 2026-08-30, 6.3k open issues | active, weekly signed releases | active, 44 open issues, pre-1.0 | active, post-rewrite churn | active, 800 open issues |

## Reading the matrix

**The isolation and credentials rows are the ones that bite: only NanoClaw containers the agent and vaults the keys by default, QwenPaw ships the strongest default posture (five security layers including a kernel sandbox), while OpenWork and Eigent run on your host by design, the trade for being desktop apps.**
PicoClaw's isolation is a recent feature flag rather than an architecture, and ZeroClaw's answer is that the binary itself is small enough to trust.

**The providers row hides the family's politics: the root endured Google and Anthropic restricting subscriptions for it in 2026, so check your provider's current stance toward this family before standardizing.**
QwenPaw is the only column with a real offline path through its own trained small models.

**The desktop split is the new category line: OpenWork and Eigent do not do chat channels at all, which is why their cells go tilde there, and choosing between them and the messaging runtimes is really choosing between an assistant that lives in your chats and one that lives on your desktop.**

**The status row's issue counts are inversely proportional to age, not quality: the root carries 6,303 open issues at scale, and the pre-1.0 PicoClaw carries 44, so read the column against its birthday.**

**Hermes is the column that breaks the -claw pattern: it competes on the learning loop rather than the trust ladder, and its 241k stars against a 39.3k-issue backlog is the trade in one row pair.**

## Choosing from the matrix

- Want the ecosystem, channels, and companion apps and accept the weight: OpenClaw.
- Want the assistant to compound (skills, memory, user model) and will supervise it: Hermes.
- Want to read every line and cage the agent: NanoClaw.
- Want to stop needing to read it, or run on a Pi: ZeroClaw.
- Want it on a microcontroller or salvage hardware, pre-1.0 accepted: PicoClaw.
- Want a readable Python core you can extend: Nanobot, binding to localhost and owning the security surface.
- Want the deepest chat-channel matrix including Chinese apps, or a real offline assistant: QwenPaw.
- Want a Cowork-style desktop on OpenCode with skills that port via MCP: OpenWork.
- Want a Cowork-style desktop with multi-agent workforces under Apache-2.0: Eigent.

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the layer that manages these as employees
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the coding-agent cousins
- [Read the Commits, Not the Manual](../../learnings-from-openclaw/index.md) - maintaining the root at scale
- [Managing Many Concurrent LLM Agent Sessions](../../managing-many-llm-agent-sessions/index.md) - the supervision context

## References

- https://github.com/openclaw/openclaw - Gateway model, channels, security posture
- https://github.com/NousResearch/hermes-agent - learning loop, backends, providers for the Hermes column
- https://github.com/nanocoai/nanoclaw - container isolation, vault, skill-based channels
- https://github.com/zeroclaw-labs/zeroclaw - runtime model, provider and channel counts
- https://github.com/sipeed/picoclaw - footprint, architectures, security banners
- https://github.com/HKUDS/nanobot - stars, alpha status, and surfaces for the Nanobot column
- https://github.com/different-ai/openwork - the OpenWork column: OpenCode base, split license, adoption
- https://github.com/eigent-ai/eigent - the Eigent column: CAMEL workforce, Apache-2.0, maturity
- https://github.com/agentscope-ai/QwenPaw - the QwenPaw column: channels, security layers, offline models
