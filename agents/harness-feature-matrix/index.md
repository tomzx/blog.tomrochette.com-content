---
title: "Harness Feature Matrix"
created: 2026-08-24
updated: 2026-08-24
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, comparison, harnesses, coding-agents]
readability: 3
audience_notes: >
  Engineers shortlisting coding-agent harnesses who need the capability deltas at a glance.
  Assumes you know what MCP, AGENTS.md, and BYOK mean; each column links to a full note with sources.
---

This matrix compares the eight harnesses profiled in this section, feature by feature, so the shortlisting step does not require reading eight notes.
Everything below was verified against live sources on 2026-08-24.

**No harness has everything, and the two axes that actually decide the purchase are client openness and who pays for tokens: everything else is converging.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [aider](../aider/index.md) | [Amp](../amp/index.md) | [Claude Code](../claude-code/index.md) | [Codex](../codex/index.md) | [Crush](../crush/index.md) | [Gemini CLI](../gemini-cli/index.md) | [Junie](../junie/index.md) | [OpenCode](../opencode/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Open client | ✓ Apache-2.0 | ✗ | ✗ | ✓ Apache-2.0 | ~ FSL-1.1-MIT | ✓ Apache-2.0 | ✗ | ✓ MIT |
| BYOK | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ paid keys | ✓ | ✓ |
| Included subscription usage | ✗ | ✓ | ✓ | ✓ | ~ via Hyper | ✗ enterprise only | ✓ | ~ via Zen |
| Local models | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ | ✓ |
| MCP | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| AGENTS.md | ✗ | ✓ | ~ reads CLAUDE.md | ✓ | ✓ plus CRUSH.md | ~ GEMINI.md native | ✗ uses guidelines.md | ✓ plus CLAUDE.md |
| Subagents | ✗ | ✓ | ✓ | ✓ | ? | ✗ | ✗ | ✓ |
| Hooks, skills, plugins | ~ lint and test only | ✓ plugins gate tools | ✓ hooks and skills | ✓ skills and marketplace | ✓ skills | ? | ~ execution allowlists | ✓ skills and plugins |
| Cloud execution | ✗ | ✓ orbs | ✓ web and teleport | ✓ | ✗ | ~ CI GitHub Action | ~ remote control | ✗ share links only |
| Scheduled runs | ✗ | ✓ self-set | ✓ routines | ? | ✗ | ✗ | ✗ | ~ via host apps |
| IDE integration | ✗ | ✗ | ✓ extensions | ✓ extension | ✗ terminal only | ~ enterprise Code Assist | ✓ | ✓ VS Code and ACP |

## Reading the matrix

**The open-client column splits the field into three groups, and each group answers a different buyer.**
aider, Codex, Gemini CLI, and OpenCode hand you auditable code; Crush is source-available with a competing-use restriction that expires per version; Amp, Claude Code, and Junie are binaries you trust.

**Subscription versus keys is the second axis, and it is orthogonal to openness.**
Codex is open and subscription-fed; Amp is closed but takes your Anthropic key on usage billing; aider and Crush are keys-only, period.

**Local-model support now cleanly separates the BYOK purists (aider, Crush, Junie, OpenCode) from the platform players** whose value-add assumes their own model routing.

**The feature everyone lacks is a different one, which is the tell that the category is immature in different places:** aider lacks the agent loop, Gemini CLI lacks a consumer future, Crush lacks documented subagents, and OpenCode lacks its own cloud execution.

## Choosing from the matrix

- Need an auditable client plus a subscription: Codex is alone in that cell.
- Need local models plus MCP: Crush or OpenCode.
- Need scheduled autonomous work in the cloud: Amp or Claude Code.
- Need editor-embedded agents with deep analysis: Junie or Claude Code.
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
- https://developers.openai.com/codex/cli - CLI, skills, AGENTS.md for the Codex column
- https://opencode.ai/docs/mcp-servers/ - MCP configuration for the OpenCode column
- https://github.com/JetBrains/junie - distribution model and MCP mentions for the Junie column
