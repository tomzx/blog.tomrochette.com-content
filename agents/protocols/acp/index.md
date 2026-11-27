---
title: Agent Client Protocol (ACP)
created: 2026-08-24
updated: 2026-11-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, llm=glm-5.4, protocols, interoperability, editor-integration]
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
The current stable protocol version is 1, with v2 now in Preview (moved from Draft on 2026-11-20, after 17 alpha releases of the v2 schema and a beta.1 schema tag), a migration guide already published, and official Kotlin, Java, Python, Rust, and TypeScript SDKs: both flagship SDKs crossed 1.0.0 in June 2026 and have kept moving, with the Rust crate at 5.6.0 and the TypeScript package at 2.12.0 (both 2026-11-24, the Rust release adopting schema 1.22.0 and the TypeScript train taking schema v1.35.0 and v2.0.0-beta.4) as of 2026-11-25; the Rust 5.0.0 major (2026-11-02) adopted schema 1.15, split its API into v1 and v2 surfaces, and dropped JSON-RPC batch support.

## Status

**Active and compounding.**
The repository shows about 4.4k stars as of 2026-10-13, with roughly 2,400 commits.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=agentclientprotocol/agent-client-protocol&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=agentclientprotocol/agent-client-protocol&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=agentclientprotocol/agent-client-protocol&type=date&legend=top-left" />
</picture>

The official agents list re-counted at 51 entries (2026-11-19) and now includes Codex CLI (via the protocol project's adapter), the Claude agent (via Zed's SDK adapter), Gemini CLI, Cursor, OpenCode, Goose, Junie, Kiro CLI, Factory Droid, Cline, Kimi CLI, Qwen Code, OpenHands, Poolside, and GitHub Copilot in public preview since 2026-01-28.
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
- 2026-10-10 - Both SDKs moved again on 2026-10-09, the Rust crate to 3.3.0 and the TypeScript package to 1.8.0, while the stable protocol stays at version 1 and the v2 draft stays open; agents list re-counted at 41 as of 2026-10-10.
- 2026-10-13 - The official agents list re-counted at 43 entries, up from 41 on 2026-10-10; the Rust crate (3.3.0), the TypeScript package (1.8.0), the stable protocol at version 1 with the v2 draft open, and the roughly 2,400-commit count re-verified unchanged.
- 2026-10-17 - Both SDKs moved again on 2026-10-16, the Rust crate to 3.4.0 and the TypeScript package to 1.9.0, while the stable protocol stays at version 1 and the v2 alpha train reached schema-v2.0.0-alpha.9 (2026-10-16); agents list re-counted at 43 as of 2026-10-17.
- 2026-10-20 - The TypeScript SDK moved to a breaking 2.0.0 (2026-10-19): the legacy connection classes and connector helper were removed in favor of agent()/client() apps and stable protocol bindings became the default import surface, while the SDK's default protocol stays ACP v1 and both v2 entrypoints stay experimental; the Rust crate (3.4.0), the stable protocol at version 1 with the v1.12.0 / schema-v1.26.0 train of 2026-10-16, and the v2 alpha train at schema-v2.0.0-alpha.9 re-verified unchanged; agents list re-counted at 43 as of 2026-10-20.
- 2026-10-24 - The SDK train moved on without breaking changes, the Rust crate to 3.5.0 (2026-10-22) and the TypeScript package to 2.0.1 (2026-10-22) then 2.0.2 (2026-10-23), both bug-fix releases after the breaking 2.0.0, while the stable protocol stays at version 1 with the v2 draft open; agents list re-counted at 46 as of 2026-10-24.
- 2026-10-25 - The repository pushed 2026-10-25 with the v2 draft's RFD docs moving subagents, system prompt, and MCP-over-ACP to active, while the SDK train stays at Rust 3.5.0 (2026-10-22) and TypeScript 2.0.2 (2026-10-23); agents list re-counted at 46, and the stable protocol stays at version 1 with the v2 draft open.
- 2026-10-27 - The repository pushed 2026-10-26/27 with the v2 unstable train continuing in the schema docs (unknown-variant receiver behavior, exactly one elicitation scope, null request IDs disallowed, a type discriminator on available commands) and no new schema release tag, while the SDK train stays at Rust 3.5.0 and TypeScript 2.0.2; agents list re-counted at 48 (registry additions include Oleafly and Open Walnut on the clients side and a2acode among connectors), and the stable protocol stays at version 1 with the v2 draft open.
- 2026-10-31 - The trains moved on without a protocol change: the stable train to v1.13.0 with schema-v1.27.0 (2026-10-27) and v1.14.0 with schema-v1.28.0 plus the v2 alpha train's schema-v2.0.0-alpha.11 (2026-10-30), the Rust crate to 3.6.0 (2026-10-28) and the TypeScript package to 2.2.0 (2026-10-30), and the agents list re-counted at 49; the stable protocol stays at version 1 with the v2 draft open.
- 2026-11-01 - Re-verification: everything the 2026-10-31 pass recorded stands unchanged, the release trains still end at v1.14.0 with schema-v1.28.0 and schema-v2.0.0-alpha.11 (2026-10-30) with nothing newer tagged, the SDKs stay at Rust 3.6.0 (2026-10-28) and TypeScript 2.2.0 (2026-10-30), and the repository pushed 2026-10-31 with no new tag since.
- 2026-11-03 - The trains moved without touching the stable protocol: the stable train to v1.15.0 with schema-v1.29.0 (2026-11-01), which added unstable session and proxy methods (session/archive, session/unarchive, session/status, session/set_title, auth/status, proxy/initialize, proxy/successor) and moved the client system prompt RFD to preview, then v1.15.1 with schema-v1.29.1 and the v2 alpha train to schema-v2.0.0-alpha.13 (both 2026-11-02, a spec-text reconcile pass); the Rust crate jumped to a breaking 5.0.0 (2026-11-02), adopting schema 1.15, splitting the API into v1 and v2 surfaces, and removing JSON-RPC batch support, and the TypeScript package moved to 2.3.0 (schema updates) then 2.4.0 (cancellable request waits) the same day; the stable protocol stays at version 1 with the v2 draft open, and the agents list re-counted at 49.
- 2026-11-06 - Re-verification: the repository pushed 2026-11-04 on docs-only commits (AionUi and Happier added to the clients list and a Remote ACP Bridge connector added), with no new tag since: the trains stay at v1.15.1 with schema-v1.29.1 and schema-v2.0.0-alpha.13, the SDKs at Rust 5.0.0 and TypeScript 2.4.0, and the stable protocol at version 1 with the v2 draft open; the agents list holds at 49.
- 2026-11-07 - Re-verification: no new tag since (trains stay at v1.15.1 with schema-v1.29.1 and schema-v2.0.0-alpha.13, SDKs still Rust 5.0.0 and TypeScript 2.4.0), with the default branch moving 2026-11-06 to stabilize the client system prompt (#2765), which the 2026-11-03 bullet recorded at preview, unreleased as of this run, and the unstable docs gaining per-item cancels on restricted subagent sessions (#2767); the agents list holds at 49.
- 2026-11-12 - The trains moved and shipped what the last pass recorded unreleased: v1.16.0 with schema-v1.30.0 and schema-v2.0.0-alpha.14 (2026-11-09, stabilizing the client system prompt, #2765), then v1.17.0 with schema-v1.31.0 and schema-v2.0.0-alpha.15 (2026-11-10, unstable additions of session/options with initial config option values, an AuthAccount description, and session tool-call content with one-shot-subagent clarification, plus an unstable-v2 clarification that session/cancel only cancels foreground work); the SDK figures stand (Rust 5.0.0, TypeScript 2.4.0), the stable protocol stays at version 1 with the v2 draft open, the docs added a page comparing ACP to MCP, A2A, and LSP (#2790), and the agents list re-counted at 51.
- 2026-11-14 - Re-verification: no new tag since (the trains stay at v1.17.0 with schema-v1.31.0 and schema-v2.0.0-alpha.15, SDKs at Rust 5.0.0 and TypeScript 2.4.0), with the default branch carrying 2026-11-13 to 11-14 unstable-train work (v2 subagents moving out from behind unstable_subagents, a replay_complete session update, a speed session-config option, markdown plans replacing the file plan type, and RFD docs for v2 idempotency keys and the replay-complete signal) plus client-registry docs commits, and the agents list re-counted at 51.
- 2026-11-15 - The trains moved on 2026-11-14, shipping what the last pass recorded unreleased: v1.18.0 with schema-v1.32.0 (unstable additions of a prompt-suggestions session update and client capability, markdown plans carrying a path in place of the file plan type, the speed session-config option category, and initial config options accepted on session/fork with notification clarifications, plus subagent message-view clarifications) and the v2 alpha train to schema-v2.0.0-alpha.16; the SDK figures stand (Rust 5.0.0, TypeScript 2.4.0), the stable protocol stays at version 1 with the v2 draft open, and the agents list re-counted at 51, unchanged.
- 2026-11-17 - Re-verification: the repository pushed 2026-11-16 on client-registry docs (Varin added to the desktop and web clients, Mobaide added to the mobile clients, Capsule's entry updated for Windows plus a website, and the acp-connector description improved), a session-cursors RFD added to the v2 draft docs, and dependency bumps, with no new tag since: the trains stay at v1.18.0 with schema-v1.32.0 and schema-v2.0.0-alpha.16, the SDKs at Rust 5.0.0 and TypeScript 2.4.0, the stable protocol at version 1 with the v2 draft open, and the agents list holds at 51.
- 2026-11-19 - The trains moved on 2026-11-18: the stable train to v1.19.0 with schema-v1.33.0 (shipping what the last pass recorded unreleased, unstable session cursors with a cursorId on session/fork #2843, plus method-aware payload dispatch #2846) and the v2 alpha train to schema-v2.0.0-alpha.17 (an idempotencyKey on session/prompt #2847, elicitation string properties losing their pattern, a diff required to carry at least one change, and agent cancellation rules); the SDK trains moved with the schemas, the Rust crate through 5.1.0 to 5.4.0 and the TypeScript package through 2.5.0, 2.6.0, and 2.7.0 to 2.8.0 (all non-breaking schema-tracking releases, a train the last two passes had missed), the stable protocol stays at version 1 with the v2 draft open, and the agents list re-counted at 51 as of 2026-11-19; the clients reference moved to the docs page's new get-started address and the SDK references moved with the trains.
- 2026-11-21 - Out-of-rotation re-verification on the release signal: ACP v2 moved from Draft to Preview on 2026-11-20 (announcement 2026-11-20, after 17 alpha schema releases since the July Draft, with the v2 schema train graduating to schema-v2.0.0-beta.1, wire-envelope validation by method and direction, and the docs carrying a full v2 protocol section plus a migration guide), the stable train moved to v1.20.0 with schema-v1.34.0 (stabilizing subagent sessions #2939 and plan operations #2898, the last two of the eight features stabilized in both v1 and v2 since July), the Claude and Codex adapters serve v2 next to v1 per the announcement, and the docs commits moved ACP v2 to Preview and backfilled the stabilization announcements; the stable protocol stays at version 1 with v2 not frozen (remote transports and prompt steering still outside the Preview), the SDK figures stand (Rust 5.4.0, TypeScript 2.8.0), and the agents list re-counted at 51; the What-it-is sentence moved with the Preview promotion.
- 2026-11-22 - The trains moved the afternoon of 2026-11-21, after the last pass's fetch: the stable train to v1.21.0 with schema-v1.34.1 (the Rust SDK re-exporting IndexMap from the schema crate, #2970), then the v1.21.1 and v1.21.2 patches (Rust clippy-exception narrowing with large v2 payloads boxed, #2972, and the unstable-v2 docs naming which description fields may carry Markdown, #2974), and the v2 beta train to schema-v2.0.0-beta.2 (protocol-page reorder and the Cancellation rename, #2964) then schema-v2.0.0-beta.3; both flagship SDKs moved with the train (Rust 5.5.1, TypeScript 2.9.1, both published 2026-11-21); the stable protocol stays at version 1 with v2 in Preview, and the agents list re-counted at 51; the What-it-is SDK figures moved with the train.
- 2026-11-24 - Rotation re-verification on the release signal: the trains moved on 2026-11-23, the stable train to v1.22.0 with schema-v1.35.0 (an unstable attribution of mcp/message requests to a session and tool call #2988, and schema fixes rejecting string payloads for v1 boolean config setters #2981 and a malformed MCP transport instead of launching it as stdio #2982) and the v2 beta train to schema-v2.0.0-beta.4 (the same unstable mcp/message attribution plus a plain-text and Markdown rendering clarification #2978); both flagship SDKs stand (Rust 5.5.1 and TypeScript 2.9.1, both published 2026-11-21, registry re-reads), the default-branch docs added Lucid to the CLI and TUI clients (#2980) and Olympus Coder to the desktop and web clients (#2977), the stable protocol stays at version 1 with v2 in Preview, the agents list re-counted at 51 as of 2026-11-24, and every cited URL re-fetched live with no dead sources.
- 2026-11-25 - Rotation re-verification on the release signal: both flagship SDKs moved on 2026-11-24, after the last pass's registry reads, the Rust crate to 5.6.0 (adopting schema 1.22.0 and exposing the mcp/message attribution, plus MCP servers admitting or rejecting a request by its session, #525 and #526) and the TypeScript package through 2.10.0 (schema v1.35.0 and v2.0.0-beta.4, MCP-over-ACP servers requiring or rejecting a session, #369 and #370), 2.11.0 (the session rejection decided in an admit check, #372), and 2.12.0 (a cancellation signal for the attribution resolver, #374); the tagged protocol trains stand at v1.22.0 with schema-v1.35.0 and schema-v2.0.0-beta.4 (2026-11-23) with no new tag, the default-branch docs changed two registry lines without adding an agent entry (#2990) and added agy-remote-wecom to the Messaging clients (#2991), the stable protocol stays at version 1 with v2 in Preview, the agents list holds at 51, the What-it-is SDK figures moved with the trains, and every cited URL re-fetched live with no dead sources.
- 2026-11-27 - Re-verification: the default branch stabilized the speed config option category on 2026-11-26 (its RFD moved from Preview to Completed and `speed` entered the default v1 and v2 schemas, the category the Claude and Codex adapters tag fast-mode controls with and Zed and Delta use to find them, #2997) with no new tag past v1.22.0 with schema-v1.35.0 and schema-v2.0.0-beta.4, and the client docs added Gerdr, AppuBot, and WittyCode to the desktop and web clients and WrongStack to the agents and CLI clients (#2992 to #2994, #2999); every cited URL re-fetched live with no dead sources.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the four-layer map that names ACP the LSP moment of this cycle
- [Zed](../../surfaces/zed/index.md) - the originating editor and its external-agents story
- [OpenCode](../../harnesses/opencode/index.md) - the harness that made ACP its editor strategy
- [JetBrains](../../surfaces/jetbrains/index.md) - the co-creator that brought ACP to the largest IDE installed base
- [Junie](../../harnesses/junie/index.md) - JetBrains's own agent, whose internal protocol became part of ACP

## References

- https://agentclientprotocol.com - official introduction: stdio model, MCP type reuse, protocol version 1
- https://agentclientprotocol.com/get-started/agents - the agent list (51 entries: Codex CLI, Claude agent, Gemini CLI, Cursor, OpenCode, Copilot preview, OpenHands, Poolside; re-counted 2026-11-24)
- https://agentclientprotocol.com/get-started/clients - the client list (Zed, JetBrains, Neovim, Emacs, VS Code, Devin Desktop; the former overview/clients address redirects here)
- https://github.com/agentclientprotocol/agent-client-protocol - Apache-2.0 repository, SDKs, stars as of 2026-10-13
- https://agentclientprotocol.com/announcements/sdk-1-0-releases - the Rust and TypeScript SDKs at 1.0.0 (June 2026), fetched via the site's markdown mirror
- https://agentclientprotocol.com/announcements/acp-v2-preview.md - the v2 Preview announcement (2026-11-20): Draft to Preview, the 17 alpha releases behind it, background work and subagents in the v2 baseline, the eight features stabilized in both v1 and v2, remote transports still outside, and the Claude and Codex adapters serving v2 next to v1 (fetched 2026-11-21)
- https://crates.io/api/v1/crates/agent-client-protocol - the Rust SDK: latest 5.6.0, published 2026-11-24 (re-fetched 2026-11-25)
- https://registry.npmjs.org/@agentclientprotocol/sdk - the TypeScript SDK: latest 2.12.0, published 2026-11-24 (re-fetched 2026-11-25)
- https://github.com/agentclientprotocol/rust-sdk/releases/tag/v5.0.0 - the Rust SDK 5.0.0 release notes: the schema 1.15 adoption, the v1/v2 API split, and the batch-support removal (fetched 2026-11-03)
- https://raw.githubusercontent.com/agentclientprotocol/typescript-sdk/main/CHANGELOG.md - the TypeScript SDK 2.0.0 changelog: the removed connection classes, the stable-bindings default, and the unchanged v1 default protocol (fetched 2026-10-20)
- https://blog.jetbrains.com/ai/2025/12/bring-your-own-ai-agent-to-jetbrains-ides/ - co-creation story, 25.3 beta, the UX trade-off admission
- https://news.ycombinator.com/item?id=45074147 - launch thread criticism (LSP and MCP comparisons, protocol proliferation, name collision)
