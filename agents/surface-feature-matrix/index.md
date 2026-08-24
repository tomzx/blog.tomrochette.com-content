---
title: "Surface Feature Matrix"
created: 2026-08-24
updated: 2026-08-24
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, comparison, surfaces, ai-editors]
readability: 3
audience_notes: >
  Engineers choosing an editor or environment for agentic coding who need the capability deltas at a glance.
  Assumes you know what MCP, AGENTS.md, cloud agents, and BYOK mean; each column links to a full note.
---

This matrix compares the ten surfaces profiled in this section, feature by feature, from editors to agent platforms to session cockpits.
Everything below was verified against live sources on 2026-08-24.

**The surfaces differ less in whether they have an agent and more in what they are: an editor with an agent inside, a platform that treats the editor as one client, or a cockpit for many agents, and the row that matters most is the one nobody advertises, who runs where.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [Antigravity](../antigravity/index.md) | [Cursor](../cursor/index.md) | [JetBrains](../jetbrains/index.md) | [Kiro](../kiro/index.md) | [OpenChamber](../openchamber/index.md) | [Trae](../trae/index.md) | [Void](../void/index.md) | [VS Code + Copilot](../vscode-copilot/index.md) | [Windsurf](../windsurf/index.md) | [Zed](../zed/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | platform, IDE, CLI, SDK | VS Code fork | IDE suite | closed IDE | local session app | VS Code fork | VS Code fork | editor plus extensions | VS Code fork | Rust editor |
| Open source | ✗ | ✗ | ~ Community IDEs | ✗ | ✓ MIT | ✗ | ✓ Apache-2.0 | ~ MIT editor | ✗ | ~ mixed licenses |
| Free tier | ✓ unlimited completions | ✓ Hobby | ✓ 5 credits | ✓ 50 credits | ✓ | ✓ | ✓ | ✓ Copilot Free | ✓ Devin account | ✓ |
| BYOK | ✗ | ✓ | ✓ Junie | ✗ | ✓ via OpenCode | ? | ✓ | ✓ | ✗ Devin key only | ✓ |
| Local models | ✗ | ? | ✓ Junie | ✗ | ✓ via OpenCode | ? | ? | ✓ | ? | ✓ |
| MCP | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ✓ | ✓ | ✓ |
| AGENTS.md | ? | ✓ | ✗ guidelines.md | ~ spec files instead | ✓ | ✓ | ? | ✓ | ✓ | ✓ |
| Cloud agents | ~ remote control | ✓ | ~ | ✓ web and Crew | ✗ local machine only | ✓ TraeWork | ✗ | ✓ Copilot agent | ✓ Devin | ✗ |
| Parallel agent management | ✓ command center | ✓ fleets | ? | ✓ Crew | ✓ core loop | ✓ concurrent tasks | ✗ | ✓ Agents window | ✓ Command Center | ~ agent panel |
| Scheduled work | ✓ scheduled messages | ✓ automations | ? | ✓ hooks | ✓ cron | ? | ✗ | ~ via GitHub | ? | ✗ |
| Mobile surface | ✓ remote control | ✓ | ✓ | ✓ | ✓ beta | ? | ✗ | ✓ Copilot app | ? | ✗ |

## Reading the matrix

**The free-tier row is the story of 2026: every surface now has one, and the differences are rate limits and credit counts rather than feature walls.**
Antigravity and OpenChamber are the extremes, a closed platform giving the most capability away and an open app with no paid tier to gate anything.

**MCP support is table stakes and effectively universal**, which moves the differentiation to AGENTS.md, where the vendor-convention holdouts (JetBrains with guidelines.md, Kiro with spec files) are now the outliers.

**The cloud-agents row separates three philosophies:** platforms with their own cloud (Cursor, Kiro, Trae, Windsurf under Devin, VS Code via GitHub), tools that only reach your own machine (OpenChamber, Zed, Void), and Antigravity's remote-control middle path.

**BYOK plus local models is the sovereignty column pair, and only JetBrains (via Junie), OpenChamber (via OpenCode), VS Code, and Zed fill both cells today.**

## Choosing from the matrix

- Want the editor to stay dumb and own the agents: OpenChamber, Zed, or VS Code with an ACP harness.
- Want the surface to also be the cloud: Cursor, Kiro, or Windsurf under Devin.
- Want zero budget: Antigravity's free tier or Void, accepting the incident record or the stall respectively.
- Must keep code on-device: OpenChamber, Void, or Zed with BYOK.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the same treatment for terminal agents
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the map these columns come from
- [ACP](../acp/index.md) - the protocol that keeps the editor choice replaceable
- [AGENTS.md](../agents-md/index.md) - the convention behind the AGENTS.md row
- [Six Months with OpenChamber](../../six-months-with-openchamber/index.md) - a longitudinal account of one column

## References

- https://antigravity.google/pricing - free tier scope for the Antigravity column
- https://cursor.com/docs/context/rules - AGENTS.md support for the Cursor column
- https://code.visualstudio.com/docs/agent-customization/custom-instructions - AGENTS.md support for the VS Code column
- https://zed.dev/docs/ai/agents - agent and AGENTS.md support for the Zed column
- https://docs.trae.ai/ide/agent-rules - AGENTS.md support for the Trae column
- https://docs.windsurf.com/ - product direction and MCP for the Windsurf column
