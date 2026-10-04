---
title: "Surface Feature Matrix"
created: 2026-08-24
updated: 2026-10-04
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, comparison, surfaces, ai-editors]
readability: 3
audience_notes: >
  Engineers choosing an editor or environment for agentic coding who need the capability deltas at a glance.
  Assumes you know what MCP, AGENTS.md, cloud agents, and BYOK mean; each column links to a full note.
---

This matrix compares the fourteen surfaces profiled in this section, feature by feature, from editors to agent platforms to session cockpits.

**The surfaces differ less in whether they have an agent and more in what they are: an editor with an agent inside, a platform that treats the editor as one client, or a cockpit for many agents, and the row that matters most is the one nobody advertises, who runs where.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [Continue](../continue/index.md) | [Cursor](../cursor/index.md) | [Delta](../delta/index.md) | [Google Antigravity](../antigravity/index.md) | [JetBrains IDEs](../jetbrains/index.md) | [Kiro](../kiro/index.md) | [OpenChamber](../openchamber/index.md) | [Roo Code](../roo-code/index.md) | [Trae](../trae/index.md) | [Void](../void/index.md) | [VS Code + Copilot](../vscode-copilot/index.md) | [Whiteboard](../whiteboard/index.md) | [Windsurf](../windsurf/index.md) | [Zed](../zed/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | platform, IDE, CLI, SDK | extensions and CLI | multiplayer agent environment over DeltaDB | VS Code fork | IDE suite | closed IDE | local session app | VS Code extension | VS Code fork | VS Code fork | editor plus extensions | desktop canvas app where agents draw and humans review | VS Code fork | Rust editor |
| Open source | ✗ | ✓ Apache-2.0 | ✗ | ✗ | ~ Community IDEs | ✗ | ✓ MIT | ✓ Apache-2.0 | ✗ | ✓ Apache-2.0 | ~ MIT editor | ✓ MIT app and SDK | ✗ | ~ mixed licenses |
| Free tier | ✓ unlimited completions | ✓ Hobby | ✓ beta free | ✓ Individuals $0 | ✓ 5 credits | ✓ 50 credits | ✓ | ✓ BYOK extension | ✓ | ✓ | ✓ Copilot Free | ✓ free and local-only in beta | ✓ Devin account | ✓ |
| BYOK | ✗ | ✓ | ✓ | ✓ | ✓ Junie | ✗ | ✓ via OpenCode | ✓ | ? | ✓ | ✓ | ✓ brings your own harness (Claude Code, Codex) | ✗ Devin key only | ✓ |
| Local models | ✗ | ✓ Ollama | ~ via external agents | ? | ✓ Junie | ✗ | ✓ via OpenCode | ✓ | ? | ? | ✓ | ✓ local-only today | ? | ✓ |
| MCP | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ? not verified | ✓ | ✓ |
| AGENTS.md | ? | ✗ own rules | ? | ✓ | ✗ guidelines.md | ✓ | ✓ | ✓ if enabled | ✓ | ? | ✓ | ? not verified | ✓ | ✓ |
| Cloud agents | ~ remote control | ✗ | ~ web and cloud runners | ✓ | ~ | ✓ web and Crew | ✗ local machine only | ~ Cloud sunset 2026-05 | ✓ TraeWork | ✗ | ✓ Copilot agent | ✗ review surface, not a host | ✓ Devin | ✗ |
| Parallel agent management | ✓ command center | ✗ | ✓ threads | ✓ fleets | ? | ✓ Crew | ✓ core loop | ~ orchestrator mode | ✓ concurrent tasks | ✗ | ✓ Agents window | ✗ none advertised | ✓ Command Center | ~ agent panel |
| Scheduled work | ✓ scheduled messages | ✗ | ? | ✓ automations | ? | ✓ hooks | ✓ cron | ? | ? | ✗ | ~ via GitHub | ✗ none advertised | ? | ✗ |
| Mobile surface | ✓ remote control | ✗ | ✓ mobile browser | ✓ | ✓ | ✓ | ✓ beta | ? | ? | ✗ | ✓ Copilot app | ✗ desktop app only | ? | ✗ |

## Reading the matrix

I weight the cloud-agents and BYOK rows heaviest, because they decide where your work actually executes.
**The free-tier row is the story of 2026: every surface now has one, and the differences are rate limits and credit counts rather than feature walls.**
Antigravity and OpenChamber are the extremes, a closed platform giving the most capability away and an open app with no paid tier to gate anything.

**MCP support is table stakes and effectively universal**, which moves the differentiation to AGENTS.md, where JetBrains (guidelines.md) is now the lone vendor-convention holdout after Kiro added AGENTS.md support.

**The cloud-agents row separates three philosophies:** platforms with their own cloud (Cursor, Delta, Kiro, Trae, Windsurf under Devin, VS Code via GitHub), tools that only reach your own machine (OpenChamber, Zed, Void), and Antigravity's remote-control middle path.

**Delta is the only column that is not an editor or a host at all: it is a thread with its own worktree, recorded in a version-control layer that keeps the conversation beside the code, which is why its review row is strongest where every other column leans on a forge.**

**BYOK plus local models is the sovereignty column pair, and only JetBrains (via Junie), OpenChamber (via OpenCode), VS Code, and Zed fill both cells today.**

**Two of the thirteen columns are death records, Continue acquired by Cursor in June 2026 and Roo Code sunset by its own team in May 2026, so their cells read as as-they-were snapshots; both exits point at [Cline](../../harnesses/cline/index.md), which tells you where the extension generation's value consolidated.**

## Choosing from the matrix

- Want the editor to stay dumb and own the agents: OpenChamber, Zed, or VS Code with an ACP harness.
- Want the surface to also be the cloud: Cursor, Kiro, or Windsurf under Devin.
- Want review fused into the work instead of filed afterward, and can accept hosted history: Delta, free while in beta, betting your team will read threads.
- Want zero budget: Antigravity's free tier or Void, accepting the incident record or the stall respectively.
- Must keep code on-device: OpenChamber, Void, or Zed with BYOK.

## Changes

- 2026-08-24 - Created in the owner-requested matrix run, ten surfaces by eleven feature rows.
- 2026-08-26 - Added a first-person reading line per the writing rules.
- 2026-08-26 - Extended from ten to twelve columns with Continue and Roo Code, adding the death-records paragraph.
- 2026-09-04 - Updated the Continue cell after its final release was corrected to 2.1.0-vscode.
- 2026-09-13 - Replaced the dead docs.windsurf.com reference (now 404) with docs.devin.ai, which now serves the Devin Desktop docs alone.
- 2026-09-16 - Corrected the docs.devin.ai reference after docs.windsurf.com resumed redirecting into it instead of returning 404; no matrix cells moved.
- 2026-09-24 - Renamed the JetBrains column to its listing title, JetBrains IDEs; no cells moved.
- 2026-10-04 - Extended from thirteen to fourteen columns with Whiteboard, the MIT agent-drawing review canvas, inserted in sorted position with every cell traced to the new note.
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-27 - Renamed the Antigravity column to its member title, Google Antigravity, and re-sorted the columns by member title (it now sorts under G); no cell content moved.
- 2026-10-04 - Corrected the Free tier row, where the Cursor column carried Continue's final-release marker and the Antigravity column carried Cursor's Hobby tier name, a misalignment dating to the original ten-column row being one cell short; Cursor now reads Hobby and Antigravity reads Individuals $0, per the member notes.
- 2026-10-04 - Extended from twelve to thirteen columns with Delta, Zed Industries' multiplayer agent environment over DeltaDB (public beta 2026-09-16), inserted alphabetically between Cursor and Google Antigravity, and updated the intro, reading, and choosing sections.

## See also

- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - the same treatment for terminal agents
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map these columns come from
- [ACP](../../protocols/acp/index.md) - the protocol that keeps the editor choice replaceable
- [AGENTS.md](../../protocols/agents-md/index.md) - the convention behind the AGENTS.md row
- [Six Months with OpenChamber](../../../six-months-with-openchamber/index.md) - a longitudinal account of one column

## References

- https://antigravity.google/pricing - free tier scope for the Antigravity column
- https://cursor.com/docs/rules - AGENTS.md support for the Cursor column (formerly /docs/context/rules, moved)
- https://code.visualstudio.com/docs/agent-customization/custom-instructions - AGENTS.md support for the VS Code column
- https://zed.dev/docs/ai/agents - agent and AGENTS.md support for the Zed column
- https://docs.trae.ai/ide/agent-rules - AGENTS.md support for the Trae column (currently redirects through a Trae promo page mid-site-restructure)
- https://docs.continue.dev/customize/rules - rules system for the Continue column
- https://roocodeinc.github.io/Roo-Code/features/custom-instructions - AGENTS.md and .roorules for the Roo Code column
- https://roocodeinc.github.io/Roo-Code/features/mcp/overview - MCP for the Roo Code column
- https://docs.devin.ai/desktop/getting-started - product direction and MCP for the Windsurf column, also the redirect target of docs.windsurf.com (308 through /windsurf/getting-started) since September 16, 2026
- https://zed.dev/blog/delta-public-beta - the public beta announcement, PR replacement, and free-during-beta status behind the Delta column
- https://delta.dev/pricing - Personal and Pro tiers, BYOK, and the Zed-shared account behind the Delta column's free-tier and BYOK cells
