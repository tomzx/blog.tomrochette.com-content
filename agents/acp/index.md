---
title: Agent Client Protocol (ACP)
created: 2026-08-24
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, protocols, interoperability, editor-integration]
readability: 3
audience_notes: >
  Engineers who want to run any coding agent inside any editor instead of committing to one vendor's pair.
  Assumes you know what LSP did for language intelligence and what a stdio subprocess is.

---

ACP is an open protocol that standardizes communication between code editors and coding agents.
Facts below verified as of 2026-09-05.

**It is pulling the same trick LSP pulled a decade ago, and it is working: editors are becoming interchangeable hosts for agents rather than agent vendors.**

## What it is

Agents run as editor subprocesses speaking JSON-RPC over stdio, with message types for the coding UX that matters (session lifecycle, permission requests, diffs).
The protocol reuses MCP's JSON representations where it can and keeps user-readable text in Markdown.
**Zed originated it, JetBrains co-developed it after merging its own internal Junie protocol effort, and the repository now lives under the vendor-neutral `agentclientprotocol` organization, Apache-2.0.**
The current stable protocol version is 1, with a v2 draft and a migration guide already published, and official Kotlin, Java, Python, Rust, and TypeScript SDKs.

## Status

**Active and compounding.**
The repository shows about 4.2k stars and 2,200 commits as of 2026-09-05.
The official agents list has grown to roughly 40 entries and now includes Codex CLI (via Zed's adapter), the Claude agent (also via Zed's SDK adapter), Gemini CLI, Cursor, OpenCode, Goose, Junie, Kiro CLI, Factory Droid, Cline, Kimi CLI, Qwen Code, and GitHub Copilot in public preview since 2026-01-28.
Clients include Zed, JetBrains IDEs (beta in the 25.3 release candidates, December 2025), Neovim and Emacs plugins, VS Code extensions, and Devin Desktop.
In this index, [OpenCode](../opencode/index.md) ships `opencode acp`, and [JetBrains](../jetbrains/index.md), [Zed](../zed/index.md), [Junie](../junie/index.md), and [Windsurf's Devin Desktop](../windsurf/index.md) all host agents through it.
Remote, cloud-hosted agents are explicitly still work in progress.

## Strengths

- **One integration per agent reaches every ACP editor, collapsing the editor-agent marriage problem.**
- JSON-RPC over stdio is small enough that hobbyists ship clients and agents in a weekend, and JetBrains calls the protocol easy to implement.
- Vendor-neutral stewardship with two editor incumbents (Zed, JetBrains) driving it.
- Complements rather than competes with MCP: an ACP-hosted agent can still call MCP servers.

## Cautions

- **Standards flatten UX**: JetBrains itself admits trading tailor-made features for protocol compliance while it works to push some of them back into the protocol.
- Remote agents are unfinished, so cloud harnesses remain second-class citizens.
- The launch HN thread (281 points) pushed back on protocol proliferation (why not LSP, why not MCP, what about AG-UI) and on the name collision with IBM's Agent Communication Protocol, which has since merged into A2A.
- Unsaved-file synchronization and diff rendering come up repeatedly as rough edges in practice discussions.

## Pricing

**Free and open source, Apache-2.0, no CLA required.**
There is nothing to buy; the only cost is integration time.

## Compared to

- **MCP: agent-to-tool, while ACP is editor-to-agent; the two compose rather than compete.**
- Vendor IDE integrations (Claude Code's extensions, Cursor's built-in agent): deeper tailor-made UX, zero portability.
- AG-UI: streams agent events to web frontends; overlapping goals but web-native rather than editor-native.

## Bottom line

**Recommended for anyone who wants to choose a harness and an editor independently; it is the cheapest portability insurance in the coding-agent stack today.**
The disagreeable part: I think ACP matters more than any single agent or editor in this index, because it dissolves the vendor-marriage question the whole market is built on.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the four-layer map that names ACP the LSP moment of this cycle
- [Zed](../zed/index.md) - the originating editor and its external-agents story
- [OpenCode](../opencode/index.md) - the harness that made ACP its editor strategy
- [JetBrains](../jetbrains/index.md) - the co-creator that brought ACP to the largest IDE installed base
- [Junie](../junie/index.md) - JetBrains's own agent, whose internal protocol became part of ACP

## References

- https://agentclientprotocol.com - official introduction: stdio model, MCP type reuse, protocol version 1
- https://agentclientprotocol.com/overview/agents - the agent list (Codex CLI, Claude agent, Gemini CLI, Cursor, OpenCode, Copilot preview)
- https://agentclientprotocol.com/overview/clients - the client list (Zed, JetBrains, Neovim, Emacs, VS Code, Devin Desktop)
- https://github.com/agentclientprotocol/agent-client-protocol - Apache-2.0 repository, SDKs, stars and commits as of 2026-09-05
- https://blog.jetbrains.com/ai/2025/12/bring-your-own-ai-agent-to-jetbrains-ides/ - co-creation story, 25.3 beta, the UX trade-off admission
- https://news.ycombinator.com/item?id=45074147 - launch thread criticism (LSP and MCP comparisons, protocol proliferation, name collision)
