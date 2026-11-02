---
artifact: article-plan
audience: One developer who already runs a coding agent and tracks work in GitHub issues or a project tracker.
status: draft
---

# Article Plan: Agentic: a work tracker for coding agents

## Core insight

For a developer who delegates work to agents, the missing tool is not a better agent interface but a tracker that holds the context of each task and treats agents as first-class users, and Agentic is that tool.

## Audience and calibration

Software engineers who already run OpenCode, Claude Code, pi, or a similar agent, and who manage several pieces of work at once.
They know what an issue, a worktree, a pull request, and a CLI are.
Tone: peer-to-peer and direct.
Depth: the design decisions and their trade-offs, not a feature tour.
No introduction to LLMs or to git.

## Format and length

Long-form product essay, about 1,200 words, with one diagram and one screenshot.

## Section outline

### The work is scattered, and the agent does not fix that

- Claim: an agent speeds up one turn but does not remember the work across sessions, so the developer spends the saved time rebuilding context.
- Evidence: first-hand description of the workflow, plus the October status post that describes consolidating one-off tools (https://blog.tomrochette.com/what-ive-built-and-what-i-need/2026-10/).
- Visualization: none.

### A task is the unit, and everything attaches to it

- Claim: putting sources, people, repositories, worktrees, and runs on one task turns resuming into a read.
- Evidence: the project README and docs (https://github.com/TomzxCode/agentic, https://tomzxcode.github.io/agentic/).
- Visualization: a diagram of sources, task, and execution.

### The agent maintains its own context

- Claim: because the CLI is a complete client over the same API, an agent can read and write the tracker, and a context run keeps the summary and next steps current.
- Evidence: the CLI reference and the concepts page (https://tomzxcode.github.io/agentic/reference/cli/, https://tomzxcode.github.io/agentic/explanation/concepts/).
- Visualization: a screenshot of a task page.

### Any harness, one durable queue

- Claim: ACP gives one interface to any harness, and a separate worker with a durable queue means a long agent turn survives an API restart.
- Evidence: ACP (https://agentclientprotocol.com/), the wiring explanation (https://tomzxcode.github.io/agentic/explanation/how-agents-are-wired/), and SAQ (https://github.com/tobymao/saq).
- Visualization: none.

### Measure how much the agents did alone

- Claim: recording a change lifecycle turns delegation into two numbers, autonomy rate and yield, instead of a feeling.
- Evidence: the track-changes guide (https://tomzxcode.github.io/agentic/how-to/track-changes-and-metrics/) and the metrics view (https://tomzxcode.github.io/agentic/views/metrics/).
- Visualization: none.

### Local-first, with the cost stated

- Claim: running on the developer's machine removes OAuth, sync, and tenancy work, and the price is no authentication and no teams.
- Evidence: the local-first explanation (https://tomzxcode.github.io/agentic/explanation/local-first/).
- Visualization: none.

### Try it

- Claim: the setup is short and the first useful loop is one task, one worktree, one run.
- Evidence: the getting-started tutorial (https://tomzxcode.github.io/agentic/tutorials/getting-started/).
- Visualization: none.

## Opening and takeaway

- Hook: the slow part of delegation is rebuilding context, not waiting for the agent.
- Takeaway: if you delegate to agents across several repositories, track the work where the agent can read and write it, not only where you can.

## Non-goals

- No full feature inventory, no changelog, and no roadmap.
- No comparison table of competitor products.
- No setup troubleshooting or API reference.
- No claim that the tool is ready for teams.
