---
title: "Surface Feature Matrix"
created: 2026-08-24
updated: 2026-10-17
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, comparison, surfaces, ai-editors]
readability: 3
audience_notes: >
  Engineers choosing an editor or environment for agentic coding who need the capability deltas at a glance.
  Assumes you know what MCP, AGENTS.md, cloud agents, and BYOK mean; each column links to a full note.
---

This matrix compares the twenty-three surfaces profiled in this section, feature by feature, from editors to agent platforms to session cockpits to the review-first browser console.

**The surfaces differ less in whether they have an agent and more in what they are: an editor with an agent inside, a platform that treats the editor as one client, or a cockpit for many agents, and the row that matters most is the one nobody advertises, who runs where.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [bb](../bb/index.md) | [Cate](../cate/index.md) | [cc-haha](../cc-haha/index.md) | [Codeg](../codeg/index.md) | [CodeNomad](../codenomad/index.md) | [Continue](../continue/index.md) | [Cursor](../cursor/index.md) | [Delta](../delta/index.md) | [Google Antigravity](../antigravity/index.md) | [JetBrains IDEs](../jetbrains/index.md) | [Kiro](../kiro/index.md) | [Nimbalyst](../nimbalyst/index.md) | [OpenChamber](../openchamber/index.md) | [px0](../px0/index.md) | [Roo Code](../roo-code/index.md) | [Trae](../trae/index.md) | [Vibeyard](../vibeyard/index.md) | [Visual Studio 2026](../visual-studio-2026/index.md) | [Void](../void/index.md) | [VS Code + Copilot](../vscode-copilot/index.md) | [Whiteboard](../whiteboard/index.md) | [Windsurf](../windsurf/index.md) | [Zed](../zed/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | self-building agent IDE over desktop, web, CLI, and HTTP API | infinite-canvas desktop workspace | Claude Code desktop workbench with Agent Teams and IM remote access | multi-agent coding workspace aggregating sessions over desktop, server, and Docker | OpenCode cockpit over desktop (Electron and Tauri) and browser, with a self-host server mode | platform, IDE, CLI, SDK | extensions and CLI | multiplayer agent environment over DeltaDB | VS Code fork | IDE suite | closed IDE | visual workspace where humans and agents co-edit files with per-block diffs | local session app | browser IDE for reviewing AI-generated code, one static Go binary served over HTTP, read-first with harness handoff | VS Code extension | VS Code fork | Electron desktop IDE wrapping agent CLIs with a project dashboard, kanban, and session grid | Windows IDE | VS Code fork | editor plus extensions | desktop canvas app where agents draw and humans review | VS Code fork | Rust editor |
| Open source | ✓ MIT | ✓ MIT | ✓ MIT | ✓ Apache-2.0 | ✓ MIT | ✗ | ✓ Apache-2.0 | ✗ | ✗ | ~ Community IDEs | ✗ | ✓ MIT apps, AGPL server | ✓ MIT | ✓ MIT | ✓ Apache-2.0 | ✗ | ✓ MIT | ✗ | ✓ Apache-2.0 | ~ MIT editor | ✓ MIT app and SDK | ✗ | ~ mixed licenses |
| Free tier | ✓ free and open source | ✓ free and open source | ✓ free and open source | ✓ free and open source | ✓ free and open source | ✓ unlimited completions | ✓ Free (X-fused ladder, 2026-10-13) | ✓ beta free | ✓ Individuals $0 | ✓ free to start (Junie Lite) | ✓ 50 credits | ✓ free for individuals, Teams free in beta | ✓ | ✓ free and open source | ✓ BYOK extension | ✓ | ✓ free and open source | ✓ Community | ✓ | ✓ Copilot Free | ✓ free and local-only in beta | ✓ Devin account | ✓ |
| BYOK | ✓ drives the provider CLIs you authenticated | ✓ via your agent CLIs and keys | ✓ model picker with custom and local endpoints | ✓ drives the agents you already run | ✓ via OpenCode's configured providers | ✗ | ✓ | ✓ | ~ SDK local servers only, no BYOK in plans | ✓ Junie | ✗ | ✓ your Claude Code or Codex subscription or key | ✓ via OpenCode | ✓ via the harnesses it dispatches to (Claude Code, Cursor Agent, Antigravity, OpenCode), no model access of its own | ✓ | ? | ✓ through the CLIs it hosts (multiple isolated Claude profiles) | ✓ preview (Foundry, OpenAI, Anthropic, Ollama) | ✓ | ✓ | ✓ brings your own harness (Claude Code, Codex) | ✗ Devin key only | ✓ |
| Local models | ? not verified | ~ via your agent CLIs | ✓ local endpoints documented | ? not verified | ✓ via OpenCode | ✗ | ✗ not documented | ~ via external agents | ~ via the SDK (LiteRT or Ollama) | ✓ Junie | ✗ | ~ via hosted agents (OpenCode in alpha) | ✓ via OpenCode | ~ via the harnesses it dispatches to | ✓ | ? | ~ via the wrapped CLIs | ✓ Ollama in BYOK preview | ? | ✓ | ~ via the harnesses it hosts, local or SSH remote hosts | ? | ✓ |
| MCP | ? not verified | ? not verified | ✓ visual management | ✓ | ✓ connection and plugin management | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ client and servers, results as widgets | ✓ | ? not verified | ✓ | ✓ | ? not verified | ✓ in agent mode | ? | ✓ | ? not verified | ✓ | ✓ |
| AGENTS.md | ? not verified | ? not verified | ? not verified | ? not verified | ? not verified | ? | ✓ plus own rules | ? | ✓ | ✗ guidelines.md | ✓ | ? not verified | ✓ | ? not verified | ✓ if enabled | ✓ | ? not verified | ✗ copilot-instructions.md | ? | ✓ | ? not verified | ✓ | ✓ |
| Cloud agents | ✗ threads run on your machine | ✗ local and SSH only | ✗ local, remote over IM and H5 | ~ your own server or Docker | ~ your machines only (desktop, your own server, the OpenTunnel relay), no vendor cloud | ~ remote control | ✓ cloud agents | ~ web and cloud runners | ✓ | ~ | ✓ web and Crew | ✗ agents run on your machine | ✗ local machine only | ✗ your own machines only, remote-first over HTTP | ~ Cloud sunset 2026-05 | ✓ TraeWork | ✗ local sessions only | ✓ Copilot cloud since 18.1 | ✗ | ✓ Copilot agent | ~ your own hosts over experimental SSH, no vendor cloud | ✓ Devin | ✗ |
| Parallel agent management | ✓ threads, agents spawn agents | ✓ core loop | ✓ sessions plus Agent Teams | ✓ main-agent delegation to typed sub-agents | ✓ projects, nested sessions, worktrees, background tasks and child sessions | ✓ command center | ~ cloud agents | ✓ threads | ✓ fleets | ? | ✓ Crew | ✓ session kanban with worktree isolation | ✓ core loop | ~ multi-turn agent threads with batch inline edits, not a session grid | ~ orchestrator mode | ✓ concurrent tasks | ✓ core loop (swarm grid) | ✗ none documented | ✗ | ✓ Agents window | ✗ none advertised | ✓ Command Center | ~ agent panel |
| Scheduled work | ✓ scheduled-jobs plugin | ✗ none documented | ✓ scheduled tasks | ✓ cron automations | ✗ none documented | ✓ scheduled messages | ✓ automations | ? | ✓ automations | ? | ✓ hooks | ~ automations documented | ✓ cron | ✗ none documented | ? | ? | ✗ none documented | ✗ none documented | ✗ | ~ via GitHub | ✗ none advertised | ? | ✗ |
| Mobile surface | ~ web app and remote-access plugins | ✗ none documented | ~ H5 and IM channels, no native app | ✓ native iOS and Android | ~ browser remote control through the OpenTunnel relay, no native app | ✓ remote control | ✓ iOS app | ✓ mobile browser | ✓ | ✓ | ✓ | ✓ iOS companion, Android in development | ✓ beta | ~ any-browser UI (the site claims tablet and mobile), no native app | ? | ? | ✗ none documented | ✗ | ✗ | ✓ Copilot app | ✗ desktop app only | ? | ✗ |

## Reading the matrix

I weight the cloud-agents and BYOK rows heaviest, because they decide where your work actually executes.
**The free-tier row is the story of 2026: every surface now has one, and the differences are rate limits and credit counts rather than feature walls.**
Antigravity and OpenChamber are the extremes, a closed platform giving the most capability away and an open app with no paid tier to gate anything.

**MCP support is table stakes and effectively universal**, which moves the differentiation to AGENTS.md, where JetBrains (guidelines.md) is now the lone vendor-convention holdout after Kiro added AGENTS.md support.

**The cloud-agents row separates three philosophies:** platforms with their own cloud (Cursor, Delta, Kiro, Trae, Windsurf under Devin, VS Code via GitHub), tools that only reach your own machines (OpenChamber, Zed, Void, Cate, Vibeyard, bb, cc-haha, Nimbalyst, CodeNomad, px0, Whiteboard over its experimental SSH hosts, and Codeg on your own server), and Antigravity's remote-control middle path.

**Delta and Whiteboard are the columns that are neither editors nor hosts: Delta is a thread with its own worktree, recorded in a version-control layer that keeps the conversation beside the code, and Whiteboard is a canvas the agent draws onto while your own harness does the running, which is why both review rows work without the pull request every other column ends at.**

**BYOK plus local models is the sovereignty column pair, and JetBrains (via Junie), OpenChamber (via OpenCode), Cate (via your agent CLIs), cc-haha (via its local endpoints), VS Code, Zed, Whiteboard (its own harnesses, local or on SSH hosts), Visual Studio 2026 (Ollama through the BYOK preview), and the departed Roo Code fill both cells today.**

**Two of the twenty-three columns are death records, Continue acquired by Cursor in June 2026 and Roo Code sunset by its own team in May 2026, so their cells read as as-they-were snapshots; both exits point at [Cline](../../harnesses/cline/index.md), which tells you where the extension generation's value consolidated.**

## Choosing from the matrix

- Want the editor to stay dumb and own the agents: OpenChamber, Cate, Zed, or VS Code with an ACP harness.
- Want the agents to build the editor itself, and can live on Apple Silicon: bb, whose plugins and features are written with its own agents.
- Want every agent's history in one searchable place you can hand between agents: Codeg.
- Want a native desktop cockpit for OpenCode with phone remote control, and can accept one-harness commitment: CodeNomad.
- Want the whole Claude Code control plane in one GUI, and can read Chinese-first documentation: cc-haha.
- Want to co-edit documents and code with the agent under per-block diff review: Nimbalyst.
- Want a review console instead of an editor, and can live on self-run benchmarks: px0, one Go binary over PR diffs and instant search, handing fixes to your own harness.
- Want a task board that spawns and closes agent sessions off the board, and can accept a single maintainer who has been quiet since September 2026: Vibeyard.
- Want the surface to also be the cloud: Cursor, Kiro, or Windsurf under Devin.
- Want review fused into the work instead of filed afterward, and can accept hosted history: Delta, free while in beta, betting your team will read threads.
- Want zero budget: Antigravity's free tier or Void, accepting the incident record or the stall respectively.
- Live in .NET or C++ on Windows: Visual Studio 2026, whose agents meet the debugger and profiler instead of an editor plugin, if the per-seat subscription reads as fair to you.
- Must keep code on-device: OpenChamber, Void, or Zed with BYOK.

## Changes

- 2026-08-24 - Created in the owner-requested matrix run, ten surfaces by eleven feature rows.
- 2026-08-26 - Added a first-person reading line per the writing rules.
- 2026-08-26 - Extended from ten to twelve columns with Continue and Roo Code, adding the death-records paragraph.
- 2026-09-04 - Updated the Continue cell after its final release was corrected to 2.1.0-vscode.
- 2026-09-13 - Replaced the dead docs.windsurf.com reference (now 404) with docs.devin.ai, which now serves the Devin Desktop docs alone.
- 2026-09-16 - Corrected the docs.devin.ai reference after docs.windsurf.com resumed redirecting into it instead of returning 404; no matrix cells moved.
- 2026-09-24 - Renamed the JetBrains column to its listing title, JetBrains IDEs; no cells moved.
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-27 - Renamed the Antigravity column to its member title, Google Antigravity, and re-sorted the columns by member title (it now sorts under G); no cell content moved.
- 2026-10-04 - Corrected the Free tier row, where the Cursor column carried Continue's final-release marker and the Antigravity column carried Cursor's Hobby tier name, a misalignment dating to the original ten-column row being one cell short; Cursor now reads Hobby and Antigravity reads Individuals $0, per the member notes.
- 2026-10-04 - Extended from twelve to thirteen columns with Delta, Zed Industries' multiplayer agent environment over DeltaDB (public beta 2026-09-16), inserted alphabetically between Cursor and Google Antigravity, and updated the intro, reading, and choosing sections.
- 2026-10-04 - Extended from thirteen to fourteen columns with Whiteboard, the MIT agent-drawing review canvas, inserted in sorted position with every cell traced to the new note.
- 2026-10-05 - Corrected six Cursor cells against the vendor's live docs and pricing page: AGENTS.md is supported alongside Cursor's own rules, cloud agents, automations, the iOS app, and parallel cloud agents are shipped, and local models are not documented (the old Ollama claim traced to nothing current); also fixed the death-records count, which still said thirteen after Delta and Whiteboard brought the matrix to fourteen columns, extended the neither-editor-nor-host reading to Whiteboard, and corrected the sovereignty pair's column list, which missed Roo Code's as-they-were cells and Whiteboard's harness-plus-local pair.
- 2026-10-06 - Extended from fourteen to fifteen columns with Visual Studio 2026, Microsoft's Windows IDE whose Copilot stack (agent mode with MCP, cloud agents since 18.1, the 18.10 BYOK preview) ships inside the incumbent, inserted in sorted position between Trae and Void; updated the intro, reading, and choosing sections.
- 2026-10-07 - Corrected the Google Antigravity cells against the vendor's docs: the SDK runs agents on local models through LiteRT or OpenAI-compatible local servers, where the cell read unverified, and BYOK moves to a partial because the plans page states BYOK and bring-your-own-endpoint are unsupported; no other cells moved.
- 2026-10-08 - Extended from fifteen to sixteen columns with Cate, the MIT infinite-canvas desktop workspace whose agent-aware terminals report working, waiting, or finished, inserted in sorted position at the head of the row; updated the intro, reading, and choosing sections.
- 2026-10-09 - Corrected the JetBrains IDEs free-tier cell against the vendor's redesigned plans page: the free start is now described as Junie Lite, a free model always on in every JetBrains account, where the cell carried the earlier 5-credit allotment; the two paid figures are exposed again on the same page ($8.33 and $25.00 per user/month, unchanged).
- 2026-10-10 - Extended from sixteen to seventeen columns with Vibeyard, the MIT desktop IDE wrapping Claude Code, Codex CLI, and Gemini CLI (kanban cards that spawn and close sessions, isolated Claude profiles, WebRTC session sharing), inserted in sorted position between Trae and Visual Studio 2026; updated the intro, reading, and choosing sections, and corrected the death-records line's stale column count (it still said fifteen after Cate joined).
- 2026-10-11 - Extended from seventeen to twenty-one columns with bb (the self-building agent IDE, at the head of the sorted row), cc-haha (the Claude Code desktop workbench) and Codeg (the session-aggregating workspace with native mobile clients) between Cate and Continue, and Nimbalyst (the human-and-agent co-editing workspace) between Kiro and OpenChamber; updated the intro, reading, and choosing sections.
- 2026-10-11 - Extended from twenty-one to twenty-two columns with CodeNomad (the MIT desktop-and-browser OpenCode cockpit with a self-host server mode and OpenTunnel phone pairing), inserted alphabetically between Codeg and Continue, every row gaining a cell traced to the new note; updated the intro, the cloud-agents reading, and the choosing section, and added its references.
- 2026-10-11 - Extended from twenty-two to twenty-three columns with px0 (the MIT browser IDE for reviewing AI-generated code, one static Go binary with PR review and harness handoff), inserted in case-insensitive sorted position between OpenChamber and Roo Code and traced to the new note; the intro, the cloud-agents reading, the death-records count, and the choosing section updated, and the px0 references added.
- 2026-10-13 - Corrected the Cursor free-tier cell after the vendor's pricing restructure: the Hobby tier name is gone and the page now sells Free, Plus, Premium, Super, and Ultra under X Subscription Corp, so the cell reads Free with the date; returned the two misplaced 2026-10-11 extension bullets to date order while appending this one.
- 2026-10-17 - Moved the Whiteboard cells after the v0.3.0 SSH-remote-hosts release: cloud agents reads your own hosts over experimental SSH with no vendor cloud, and local models reads via the harnesses it hosts, local or SSH remote hosts; the cloud-agents and sovereignty readings updated to match.

## See also

- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - the same treatment for terminal agents
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map these columns come from
- [ACP](../../protocols/acp/index.md) - the protocol that keeps the editor choice replaceable
- [AGENTS.md](../../protocols/agents-md/index.md) - the convention behind the AGENTS.md row
- [Six Months with OpenChamber](../../../six-months-with-openchamber/index.md) - a longitudinal account of one column

## References

- https://antigravity.google/pricing - free tier scope for the Antigravity column
- https://cursor.com/docs/rules - the rules system and AGENTS.md support for the Cursor column (formerly /docs/context/rules, moved)
- https://cursor.com/docs/models-and-pricing - cloud agents, Automations, Cursor for iOS, and the Teams Premium price for the Cursor column, as of 2026-10-05
- https://cursor.com/pricing - plan features and tiers for the Cursor column, re-verified 2026-10-05
- https://code.visualstudio.com/docs/agent-customization/custom-instructions - AGENTS.md support for the VS Code column
- https://zed.dev/docs/ai/agents - agent and AGENTS.md support for the Zed column
- https://docs.trae.ai/ide/agent-rules - AGENTS.md support for the Trae column (currently redirects through a Trae promo page mid-site-restructure)
- https://docs.continue.dev/customize/rules - rules system for the Continue column
- https://roocodeinc.github.io/Roo-Code/features/custom-instructions - AGENTS.md and .roorules for the Roo Code column
- https://roocodeinc.github.io/Roo-Code/features/mcp/overview - MCP for the Roo Code column
- https://docs.devin.ai/desktop/getting-started - product direction and MCP for the Windsurf column, also the redirect target of docs.windsurf.com (308 through /windsurf/getting-started) since September 16, 2026
- https://zed.dev/blog/delta-public-beta - the public beta announcement, PR replacement, and free-during-beta status behind the Delta column
- https://github.com/NeuralNomadsAI/CodeNomad - the CodeNomad column: repository, MIT license, stars, and activity (GitHub API, as of 2026-10-11)
- https://raw.githubusercontent.com/NeuralNomadsAI/CodeNomad/main/README.md - the cockpit features, OpenCode V2 version contract, SideCars, and remote control for the CodeNomad column
- https://raw.githubusercontent.com/NeuralNomadsAI/CodeNomad/main/packages/server/README.md - the server mode, authentication, and remote-access model behind the CodeNomad column's cloud-agents and mobile cells
- https://delta.dev/pricing - Personal and Pro tiers, BYOK, and the Zed-shared account behind the Delta column's free-tier and BYOK cells
- https://github.com/px0-ai/px0 - the px0 column: repository, MIT, Go, stars, and dates (GitHub API, as of 2026-10-11)
- https://raw.githubusercontent.com/px0-ai/px0/HEAD/README.md - the px0 column: PR review, harness handoff list, virtual rendering, remote mode, and sandboxing
- https://px0.ai/ - the px0 column: the performance claims, the four-harness headline, the logo wall, and the design-partner program
- https://hn.algolia.com/api/v1/items/49683668 - the px0 column: the 7-point, zero-comment Show HN, the footprint record
