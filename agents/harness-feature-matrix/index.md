---
title: "Harness Feature Matrix"
created: 2026-08-24
updated: 2026-08-27
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, comparison, harnesses, coding-agents]
readability: 3
audience_notes: >
  Engineers shortlisting coding-agent harnesses who need the capability deltas at a glance.
  Assumes you know what MCP, AGENTS.md, and BYOK mean; each column links to a full note with sources.
---

This matrix compares the thirteen harnesses profiled in this section, feature by feature, so the shortlisting step does not require reading thirteen notes.
Everything below was verified against live sources on 2026-08-27.

**No harness has everything, and the two axes that actually decide the purchase are client openness and who pays for tokens: everything else is converging.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [aider](../aider/index.md) | [Amp](../amp/index.md) | [Claude Code](../claude-code/index.md) | [Cline](../cline/index.md) | [Codex](../codex/index.md) | [Crush](../crush/index.md) | [Gemini CLI](../gemini-cli/index.md) | [goose](../goose/index.md) | [Junie](../junie/index.md) | [Kilo Code](../kilo-code/index.md) | [OpenCode](../opencode/index.md) | [OpenHands](../openhands/index.md) | [Qwen Code](../qwen-code/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Open client | ✓ Apache-2.0 | ✗ | ✗ | ✓ Apache-2.0 | ✓ Apache-2.0 | ~ FSL-1.1-MIT | ✓ Apache-2.0 | ✓ Apache-2.0 | ✗ | ✓ MIT | ✓ MIT | ✓ MIT | ✓ Apache-2.0 |
| BYOK | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ paid keys | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Included subscription usage | ✗ | ✓ | ✓ | ~ via ClinePass | ✓ | ~ via Hyper | ✗ enterprise only | ~ via ACP subs | ✓ | ~ kilo credits | ~ via Zen | ✗ at-cost only | ~ free OAuth tier |
| Local models | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ Ollama and LM Studio | ✓ | ✓ LM Studio, Ollama, vLLM | ✓ |
| MCP | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| AGENTS.md | ✗ | ✓ | ~ reads CLAUDE.md | ✓ plus .clinerules | ✓ | ✓ plus CRUSH.md | ~ GEMINI.md native | ✓ plus .goosehints | ✗ uses guidelines.md | ✓ plus .kilocoderules | ✓ plus CLAUDE.md | ✗ uses .openhands | ~ QWEN.md native |
| Subagents | ✗ | ✓ | ✓ | ✓ teams | ✓ | ? | ✗ | ✓ | ✗ | ✓ custom and built-in | ✓ | ~ delegates via ACP | ✓ teams |
| Hooks, skills, plugins | ~ lint and test only | ✓ plugins gate tools | ✓ hooks and skills | ✓ skills and SDK plugins | ✓ skills and marketplace | ✓ skills | ? | ✓ hooks and plugins | ~ execution allowlists | ✓ skills and hooks | ✓ skills and plugins | ✓ hooks, skills, plugins | ✓ hooks and auto-skills |
| Cloud execution | ✗ | ✓ orbs | ✓ web and teleport | ✗ | ✓ | ✗ | ~ CI GitHub Action | ✗ | ~ remote control | ✓ cloud agents and tasks | ✗ share links only | ✓ OpenHands Cloud | ✗ |
| Scheduled runs | ✗ | ✓ self-set | ✓ routines | ✓ cron | ? | ✗ | ✗ | ✗ | ✗ | ✓ cron builder | ~ via host apps | ✓ automations and webhooks | ~ experimental cron |
| IDE integration | ✗ | ✗ | ✓ extensions | ✓ VS Code and JetBrains | ✓ extension | ✗ terminal only | ~ enterprise Code Assist | ~ experimental VS Code | ✓ | ✓ VS Code and JetBrains | ✓ VS Code and ACP | ✗ browser and terminal | ✓ VS Code, Zed, JetBrains |

## Reading the matrix

I read this table by columns rather than rows: pick the two rows you actually care about, then let the rest fall away.
**The open-client column splits the field into three groups, and each group answers a different buyer.**
aider, Cline, Codex, Gemini CLI, goose, Kilo Code, OpenCode, OpenHands, and Qwen Code hand you auditable code; Crush is source-available with a competing-use restriction that expires per version; Amp, Claude Code, and Junie are binaries you trust.

**Subscription versus keys is the second axis, and it is orthogonal to openness.**
Codex is open and subscription-fed; Amp is closed but takes your Anthropic key on usage billing; aider and Crush are keys-only, period; goose reuses the Claude, ChatGPT, or Gemini subscription you already pay for via ACP.

**Local-model support now cleanly separates the BYOK purists (aider, Cline, Crush, goose, Junie, Kilo Code, OpenCode, OpenHands, Qwen Code) from the platform players** whose value-add assumes their own model routing.

**The feature everyone lacks is a different one, which is the tell that the category is immature in different places:** aider lacks the agent loop, Gemini CLI lacks a consumer future, Crush lacks documented subagents, OpenCode lacks its own cloud execution, and all three 2026 entrants lack cloud execution: Cline and Qwen Code run only where you stand, and goose keeps its IDE story experimental.
**The two newest columns redraw that map again:** Kilo Code bundles subagents, schedules, and cloud tasks into an editor-native open agent, which nothing else in this table does, while OpenHands skips AGENTS.md entirely because its `.openhands` customization replaces repo-instruction files.

## Choosing from the matrix

- Need an auditable client plus a subscription: Codex is alone in that cell.
- Need local models plus MCP: Cline, Crush, goose, Junie, Kilo Code, OpenCode, OpenHands, or Qwen Code.
- Need scheduled autonomous work in the cloud: Amp, Claude Code, Kilo Code, or OpenHands.
- Need editor-embedded agents with deep analysis: Junie or Claude Code.
- Need rules portability across tools: Amp, Cline, Codex, Crush, goose, Kilo Code, and OpenCode read AGENTS.md natively.
- Need an auditable agent platform you can self-host with cloud automation built in: OpenHands.
- Need none of the above, just cheap precise edits on your keys: aider.

## See also

- [Harness Feature Matrix companion: surfaces](../surface-feature-matrix/index.md) - the same treatment for editors and environments
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the map these columns come from
- [Model Selection for Coding Tasks](../model-selection-for-coding-tasks/index.md) - the model side of the same decision
- [MCP](../mcp/index.md) - the protocol behind the MCP row
- [AGENTS.md](../agents-md/index.md) - the convention behind the AGENTS.md row

## References

- https://github.com/Aider-AI/aider - license and feature surface for the aider column
- https://ampcode.com/manual/ - modes, plugins, orbs for the Amp column
- https://code.claude.com/docs/en/overview - surfaces, skills, routines for the Claude Code column
- https://docs.cline.bot/features/cline-rules - rules formats including native AGENTS.md for the Cline column
- https://developers.openai.com/codex/cli - CLI, skills, AGENTS.md for the Codex column
- https://docs.openhands.dev/llms.txt - component map, automations, local LLMs, and .openhands customization for the OpenHands column
- https://kilo.ai/docs/llms.txt - subagents, MCP, AGENTS.md support, schedules, and cloud tasks for the Kilo Code column
- https://www.anaconda.com/blog/anaconda-acquires-kilo-code - ownership context for the Kilo Code column
- https://goose-docs.ai/docs/guides/context-engineering/using-goosehints - AGENTS.md and .goosehints defaults for the goose column
- https://opencode.ai/docs/mcp-servers/ - MCP configuration for the OpenCode column
- https://github.com/JetBrains/junie - distribution model and MCP mentions for the Junie column
- https://qwenlm.github.io/qwen-code-docs/en/users/configuration/settings/ - QWEN.md and experimental cron for the Qwen Code column
