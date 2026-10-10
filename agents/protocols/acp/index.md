---
title: Agent Client Protocol (ACP)
created: 2026-08-24
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, protocols, interoperability, editor-integration]
readability: 3
audience_notes: >
  Engineers who want to run any coding agent inside any editor instead of committing to one vendor's pair.
  Assumes you know what LSP did for language intelligence and what a stdio subprocess is.

---

ACP is an open protocol that standardizes communication between code editors and coding agents.

**It is pulling the same trick LSP pulled a decade ago, and it is working: editors are becoming interchangeable hosts for agents rather than agent vendors.**

## What it is

Agents run as editor subprocesses speaking JSON-RPC over stdio, with message types for the coding UX that matters (session lifecycle, permission requests, diffs).
The protocol reuses MCP's JSON representations where it can and keeps user-readable text in Markdown.
**Zed originated it, JetBrains co-developed it after merging its own internal Junie protocol effort, and the repository now lives under the vendor-neutral `agentclientprotocol` organization, Apache-2.0.**
The current stable protocol version is 1, with a v2 draft and a migration guide already published, and official Kotlin, Java, Python, Rust, and TypeScript SDKs: both flagship SDKs crossed 1.0.0 in June 2026 and have kept moving, with the Rust crate at 3.2.0 (2026-10-08) and the TypeScript package at 1.7.0 (2026-10-02) as of 2026-10-09.

## Status

**Active and compounding.**
The repository shows about 4.4k stars as of 2026-10-09, with roughly 2,300 commits.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=agentclientprotocol/agent-client-protocol&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=agentclientprotocol/agent-client-protocol&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=agentclientprotocol/agent-client-protocol&type=date&legend=top-left" />
</picture>

The official agents list has grown to 41 entries (re-counted 2026-10-09) and now includes Codex CLI (via the protocol project's adapter), the Claude agent (via Zed's SDK adapter), Gemini CLI, Cursor, OpenCode, Goose, Junie, Kiro CLI, Factory Droid, Cline, Kimi CLI, Qwen Code, and GitHub Copilot in public preview since 2026-01-28.
Clients include Zed, JetBrains IDEs (beta in the 25.3 release candidates, December 2025), Neovim and Emacs plugins, VS Code extensions, and Devin Desktop.
In this index, [OpenCode](../../harnesses/opencode/index.md) ships `opencode acp`, and [JetBrains](../../surfaces/jetbrains/index.md), [Zed](../../surfaces/zed/index.md), [Junie](../../harnesses/junie/index.md), and [Windsurf's Devin Desktop](../../surfaces/windsurf/index.md) all host agents through it.
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
- [AG-UI](../ag-ui/index.md): streams agent events to web frontends; overlapping goals but web-native rather than editor-native.

## Bottom line

**Recommended for anyone who wants to choose a harness and an editor independently; it is the cheapest portability insurance in the coding-agent stack today.**
The disagreeable part: I think ACP matters more than any single agent or editor in this index, because it dissolves the vendor-marriage question the whole market is built on.

## Changes

- 2026-08-24 - Created in the Protocols category seed.
- 2026-09-16 - Linked the Compared-to AG-UI mention to the new AG-UI note.
- 2026-10-06 - Recorded the Rust and TypeScript SDKs reaching 1.0.0 (June 2026) and re-counted the official agents list at 41 entries.
- 2026-10-07 - Recorded the SDK train moving past 1.0.0 while the stable protocol stays at version 1 with the v2 draft open: the Rust crate reached 3.0.0 on 2026-10-06 and the TypeScript package 1.7.0 on 2026-10-02; agents list re-counted at 41.
- 2026-10-07 - Added the agentclientprotocol/agent-client-protocol star history chart to the Status section.
- 2026-10-08 - The Rust SDK train moved to 3.1.0 (2026-10-07) while the stable protocol stays at version 1 and the v2 draft stays open; agents list re-counted at 41 as of 2026-10-08.
- 2026-10-09 - The Rust SDK train moved to 3.2.0 (2026-10-08) while the stable protocol stays at version 1 and the v2 draft stays open; agents list re-counted at 41 as of 2026-10-09.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the four-layer map that names ACP the LSP moment of this cycle
- [Zed](../../surfaces/zed/index.md) - the originating editor and its external-agents story
- [OpenCode](../../harnesses/opencode/index.md) - the harness that made ACP its editor strategy
- [JetBrains](../../surfaces/jetbrains/index.md) - the co-creator that brought ACP to the largest IDE installed base
- [Junie](../../harnesses/junie/index.md) - JetBrains's own agent, whose internal protocol became part of ACP

## References

- https://agentclientprotocol.com - official introduction: stdio model, MCP type reuse, protocol version 1
- https://agentclientprotocol.com/get-started/agents - the agent list (41 entries: Codex CLI, Claude agent, Gemini CLI, Cursor, OpenCode, Copilot preview)
- https://agentclientprotocol.com/overview/clients - the client list (Zed, JetBrains, Neovim, Emacs, VS Code, Devin Desktop)
- https://github.com/agentclientprotocol/agent-client-protocol - Apache-2.0 repository, SDKs, stars as of 2026-10-08
- https://agentclientprotocol.com/announcements/sdk-1-0-releases - the Rust and TypeScript SDKs at 1.0.0 (June 2026), fetched via the site's markdown mirror
- https://crates.io/api/v1/crates/agent-client-protocol - the Rust SDK: latest 3.2.0, published 2026-10-08, as of 2026-10-09
- https://registry.npmjs.org/@agentclientprotocol/sdk - the TypeScript SDK: latest 1.7.0, published 2026-10-02, as of 2026-10-09
- https://blog.jetbrains.com/ai/2025/12/bring-your-own-ai-agent-to-jetbrains-ides/ - co-creation story, 25.3 beta, the UX trade-off admission
- https://news.ycombinator.com/item?id=45074147 - launch thread criticism (LSP and MCP comparisons, protocol proliferation, name collision)
