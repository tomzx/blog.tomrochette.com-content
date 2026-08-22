---
title: "Agentic Coding Tools Landscape"
created: 2026-08-22
status: finished
tags: [ai, llm, coding-agents, developer-tools, agent-curated, fully-ai-generated, llm=glm-5.3]
readability: 3
audience_notes: >
  Software engineers picking or re-evaluating coding agents and harnesses.
  Assumes you have driven at least one terminal coding agent and now want a current map of the whole field.
---

This page maps the agentic development environment as it exists today: the coding agents, the editors they run in, the clouds they run on, and the tools that watch them in parallel.
Everything here was verified against live sources on 2026-08-22.
I re-verify every link on each refresh, and when the facts move, this page moves with them and the date above changes with them.

**The terminal harness, not the IDE, is the center of the stack, and every other layer has spent the last year rearranging itself around a handful of CLIs.**
That has one practical consequence: **pick your harness first and your editor second**, because the editor is now the replaceable part.

## The map in four layers

The whole field fits in four boxes plus a set of shared conventions.

- Harnesses: terminal agents that run the edit-test-commit loop (Claude Code, Codex, Gemini CLI, OpenCode, and a long independent tail).
- Surfaces: editors and IDEs that host the loop, either by bundling an agent or by speaking a protocol to one.
- Cloud: the same agents running on someone else's machine, against a branch, delivering a pull request.
- Orchestration: control rooms that run many agents in parallel and absorb the review burden.

Underneath all four sit the conventions that make the parts interchangeable: MCP for tools, ACP for editor integration, and AGENTS.md for project instructions.

## Harnesses: the loop lives in the terminal

**The harness, not the model, is the product you actually operate every day, and the big four have become platforms rather than tools.**
[Claude Code](https://code.claude.com/docs/en/overview) runs in the terminal, in VS Code and JetBrains, as a desktop app, and on the web, with sessions that move between surfaces, subagents, skills, hooks, an Agent SDK, and scheduled cloud routines.
[Codex](https://developers.openai.com/codex/) covers the same spread, with a CLI, an IDE extension, desktop, web, and cloud forms, and it configures itself through AGENTS.md; OpenAI now positions it as an open agent harness with open-source components.
[Gemini CLI](https://github.com/google-gemini/gemini-cli) is the open-source outlier from a major lab: Apache-2.0, about 107k GitHub stars, a free tier of 1,000 requests a day, and Gemini 3 models with a 1M-token context window.
[OpenCode](https://opencode.ai/docs/) is the vendor-neutral entry: open source, any provider, with a TUI, an IDE extension, a desktop app, and a web view built off one codebase.

The independent tail matters more than its market share suggests.
[aider](https://aider.chat/) predates the agentic wave and still does one thing well, pair programming against any LLM with a repo map and automatic commits.
[Crush](https://github.com/charmbracelet/crush) (Charm, FSL-1.1-MIT, about 28k stars) pulls context from language servers the way an IDE would, and it reads the same AGENTS.md files as the bigger tools.
[Amp](https://ampcode.com/) bets on remote execution, with "orbs" that keep working after you close the laptop.
[Junie](https://github.com/JetBrains/junie) is JetBrains' agent, LLM-agnostic with bring-your-own-key, shipping from the terminal, the IDE, and CI.

**The split that matters at this layer is subscription versus provider-agnostic, not open versus closed.**
Claude Code and Codex are at their best inside their own vendor's subscription; Gemini CLI, OpenCode, aider, Crush, and Junie run against whatever keys you already own.

## Surfaces: editors stopped bundling, started hosting

[Cursor](https://cursor.com/) began as the AI-native editor and now ships a full stack around it: a CLI, cloud agents that work for hours or days, scheduled automations, a Slack integration, and model pickers spanning OpenAI, Anthropic, Google, xAI, and its own Composer models.
In August 2026 Cursor was [acquired by SpaceX](https://cursor.com/blog/joining-spacex), completing a partnership with SpaceXAI that started in April, which tells you the front of this market is merging with the compute owners.
VS Code and GitHub put one agent in two places: agent mode locally in the editor, and the [Copilot cloud agent](https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent) on GitHub.com, where it gets an ephemeral Actions-powered environment and can be assigned an issue like a teammate.
Windsurf still plays the AI-editor game it helped define.
JetBrains ships Junie and, more consequentially, co-created the [Agent Client Protocol](https://agentclientprotocol.com/) with Zed.

**ACP is quietly dissolving the editor question: an editor that speaks ACP can host any ACP agent as a subprocess, the same trick LSP pulled for language intelligence a decade ago.**
OpenCode already ships [`opencode acp`](https://opencode.ai/docs/acp/), so one harness runs inside Zed, JetBrains IDEs, and Neovim plugins unchanged.
Once your editor hosts your harness, choosing between them stops being a marriage and becomes a preference.

## Cloud: the same agent, somewhere else

Every major harness now has a cloud form, and the differences live in the seams.
Claude Code on the web shares context with the CLI, and `claude --teleport` pulls a web session back into your terminal.
The Copilot cloud agent is GitHub-native and capped at 59 minutes per session, a number that should anchor what you delegate to it.
[Jules](https://jules.google/) clones your repository to a cloud VM, plans, shows a diff, and opens a PR, powered by Gemini 3 Pro with a free tier of 15 tasks a day.
Cursor runs cloud agents as fleets; Amp's orbs are the same idea pointed at your own remote machines.

**Cloud and local are one product with two entry points now, so a tool that offers only one of them is incomplete, and the quotas (59-minute sessions, 15 tasks a day) are the real spec sheet.**
Read the caps before you promise anyone a timeline.

## Orchestration: watching the agents is the job

Run enough agents in parallel and your bottleneck stops being generation and starts being supervision.
The vendors answer inside the harness: subagents in Claude Code and Codex, background agent views, git worktrees everywhere.
A separate category answers from outside: agentic development environments that run any CLI agent in isolated worktrees and give you one surface to steer and review them all.
On the GitHub [ade topic](https://github.com/topics/ade), Orca leads with about 50k stars, ahead of Paseo and Superset, and the curated [awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators) list tracks well over a hundred more across TUIs, desktop apps, swarms, loop runners, and task runners.

**The size of that long tail is the finding: scheduling parallel agents turned out to be easy, so easy that everyone did it, while the scarce skill is deciding what to let through, which is a review problem, not an orchestration problem.**
Most of those hundred tools will not survive that realization.

## The conventions are the moat

Three standards decide how the pieces swap.
[MCP](https://modelcontextprotocol.io/) connects agents to tools and data, and it is spoken by Claude, ChatGPT, VS Code, Cursor, Copilot, Gemini CLI, Crush, and OpenCode alike.
[ACP](https://agentclientprotocol.com/) connects editors to agents.
AGENTS.md carries project instructions, was popularized by Codex, and is now read or written by OpenCode and Crush, against vendor variants like CLAUDE.md and GEMINI.md.

**Switching costs did not disappear, they moved to the convention layer: models are substitutable, your MCP servers, skills, and AGENTS.md files are not, and that is where lock-in now lives.**
A harness that adopts the open conventions is making a promise about your exit; one that only reads its own files is making the opposite promise.

## What to Do Next

- Choose the harness first: a subscription CLI if you live inside one vendor's models, a provider-agnostic one (OpenCode, Crush, Gemini CLI, aider) if you switch or self-host.
- Keep your editor, and if it supports ACP, host your harness inside it instead of migrating IDEs.
- Commit an AGENTS.md to your repositories this week; it is the cheapest portability insurance available right now.
- Route batch work to the cloud form of the harness you already use, and read the session caps before promising a delivery date.
- Graduate to an orchestration tool when reviewing parallel agents, not running them, becomes your actual bottleneck.

## See also

- [Managing Many Concurrent LLM Agent Sessions](../../managing-many-llm-agent-sessions/index.md) - the supervision bottleneck that the orchestration layer exists to absorb
- [Rethinking Code Review in the Age of LLMs](../../rethinking-code-review-in-the-age-of-llms/index.md) - the review surface every layer in this map has to rebuild
- [Scaling the LLM Agent Company](../../scaling-the-llm-agent-company/index.md) - where multi-agent orchestration points once it leaves your laptop
- [The Codebase Gardener](../../the-codebase-gardener/index.md) - the human role that remains when agents do most of the writing

## References

- [Claude Code documentation](https://code.claude.com/docs/en/overview) - the multi-surface harness pattern in one product
- [Codex documentation](https://developers.openai.com/codex/) - surfaces, AGENTS.md configuration, and the open-harness positioning
- [OpenCode documentation](https://opencode.ai/docs/) - the provider-agnostic open-source harness, with [ACP support](https://opencode.ai/docs/acp/) documented separately
- [Agent Client Protocol](https://agentclientprotocol.com/) - the editor-agent interop standard from JetBrains and Zed
- [awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators) - the maintained map of the orchestration long tail
