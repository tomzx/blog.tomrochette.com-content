---
title: "Assistant Runtimes Feature Matrix"
created: 2026-08-27
updated: 2026-08-27
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, comparison, assistant-runtimes, personal-assistants]
readability: 3
audience_notes: >
  Engineers choosing a self-hosted chat-channel assistant runtime and deciding how much machine they are willing to trust.
  Assumes you know what a container and a cross-compiled binary are; each column links to a full note.
---

This matrix compares the four assistant runtimes profiled in this section, the OpenClaw root and the three variants named after shrinking it, feature by feature.
Everything below was verified against live sources on 2026-08-27.

**The family ladder is a trust ladder: OpenClaw is an ecosystem, NanoClaw an auditable codebase, ZeroClaw a static binary, PicoClaw a firmware image, and the real choice is how much machine and code you are willing to trust with your messages.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [OpenClaw](../openclaw/index.md) | [NanoClaw](../nanoclaw/index.md) | [ZeroClaw](../zeroclaw/index.md) | [PicoClaw](../picoclaw/index.md) |
| --- | --- | --- | --- | --- |
| Runtime | TypeScript on Node | TypeScript on Node | single Rust binary | single Go binary |
| License | ✓ MIT | ✓ MIT | ✓ MIT OR Apache-2.0 | ✓ MIT |
| Born | 2025-11-24 | 2026-01-31 | 2026-02-13 | 2026-02-04 |
| Stars | about 388k | about 30.6k | about 32.7k | about 29.9k |
| Footprint | large, 70+ dependencies per the NanoClaw audit | one process, containerized | one binary, any machine | one binary, 10-20MB RAM |
| Isolation model | app-level, sandboxing optional | ✓ per-agent Linux containers | ~ own machine, tool grants | ~ v0.2.6 isolation support |
| Channels | dozens incl. Signal, iMessage | 13+ installed as skills | 30+ incl. voice, webhooks | many incl. WeCom, WeChat, IRC |
| Providers | hosted plus local | Claude SDK plus codex, opencode, ollama skills | about 20 incl. Ollama | many incl. Kimi, MiMo, Bedrock |
| Edge and mobile | companion apps | ✗ Docker host only | ~ Android port, Raspberry Pi | ✓ Android APK, $10 RISC-V boards |
| Credentials | your keys on host | ✓ OneCLI Agent Vault | your keys in workspace | your keys in workspace |
| Security record | provider saga plus a 514-point vuln report | clean so far | clean so far, thin coverage | pre-1.0 banner, scam-token notice |
| Status | active, 5.6k open issues | active, 1k open issues | active, 804 open issues | active, 38 open issues, pre-1.0 |

## Reading the matrix

**The isolation and credentials rows are the ones that bite: only NanoClaw containers the agent and vaults the keys by default, while the root runs tools on your host unless you configure otherwise.**
PicoClaw's isolation is a recent feature flag rather than an architecture, and ZeroClaw's answer is that the binary itself is small enough to trust.

**The providers row hides the family's politics: the root endured Google and Anthropic restricting subscriptions for it in 2026, so check your provider's current stance toward this family before standardizing.**

**The status row's issue counts are inversely proportional to age, not quality: the root carries 5,617 open issues at scale, and the pre-1.0 PicoClaw carries 38, so read the column against its birthday.**

## Choosing from the matrix

- Want the ecosystem, channels, and companion apps and accept the weight: OpenClaw.
- Want to read every line and cage the agent: NanoClaw.
- Want to stop needing to read it, or run on a Pi: ZeroClaw.
- Want it on a microcontroller or salvage hardware, pre-1.0 accepted: PicoClaw.

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the layer that manages these as employees
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the coding-agent cousins
- [Read the Commits, Not the Manual](../../learnings-from-openclaw/index.md) - maintaining the root at scale
- [Managing Many Concurrent LLM Agent Sessions](../../managing-many-llm-agent-sessions/index.md) - the supervision context

## References

- https://github.com/openclaw/openclaw - Gateway model, channels, security posture
- https://github.com/nanocoai/nanoclaw - container isolation, vault, skill-based channels
- https://github.com/zeroclaw-labs/zeroclaw - runtime model, provider and channel counts
- https://github.com/sipeed/picoclaw - footprint, architectures, security banners
- https://api.github.com/repos/openclaw/openclaw - scale figures as of 2026-08-27
