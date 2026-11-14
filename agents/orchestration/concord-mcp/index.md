---
title: Concord MCP
created: 2026-11-06
updated: 2026-11-14
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, coordination, mcp, messaging, multi-agent]
readability: 3
audience_notes: >
  Engineers running two or more coding agents against the same repository who
  want the agents to coordinate instead of colliding, and who will evaluate an
  advisory claim system and a pre-1.0 dependency. Assumes familiarity with
  MCP-aware harnesses such as Claude Code and Codex.
---

Concord MCP is an MIT-licensed MCP server and CLI that gives coding agents sharing one repository a common work-state layer: presence, file and task claims, live agent-to-agent messaging, ownership handoffs, and review packets.

## What it is

**Concord coordinates the agents you already run instead of adding another runtime.**
Concord AI's TypeScript MCP server installs from npm as `@concord-ai/concord-mcp` and keeps its state in a local SQLite database under `.concord/` at the repository root, beside human-readable `HANDOFF.md` and `REVIEW_PACKET.md` artifacts.
Agents coordinate through five MCP tools: `start_work` registers presence, claims a task, and reports scope overlaps before editing, `inspect_work` reads workspace and task state, inboxes, and durable prompt/reply threads, `update_work` records context or sends live messages, `transfer_work` handles assignment, acceptance, handoffs, and reassignment, and `finish_work` records evidence and marks tasks review-ready, complete, or closed.
Humans inspect the same workspace through a `concord` CLI with `status`, `dashboard` (a live TUI), `tasks`, `handoff`, and `review-packet` commands.
`concord setup` registers the server and merges instructions into Claude Code, Codex, Cursor, Gemini CLI, Grok Build, Goose, GitHub Copilot CLI, and Antigravity configs.
A hosted cloud tier in early access syncs the same work-state across machines.
The project states explicitly that it is not an orchestrator, code reviewer, hosted sync service, or autonomous agent.

## Status

**Active and fast-moving, pre-1.0.**
The repository was created 2026-07-14 and surfaced on Show HN on 2026-08-27, where it stood at 9 points and 4 comments as of 2026-11-06.
It reached 978 stars as of 2026-11-06.
The latest release, v0.22.0, shipped 2026-11-11, after v0.21.0 (2026-11-09) and v0.21.1 (2026-11-11), and FollowAgents counted thirteen releases between its review snapshot of 2026-10-04 and its writing.
The npm package (@concord-ai/concord-mcp, 35 published versions, latest 0.22.0) drew 4,131 downloads in the trailing month (2026-10-14 to 2026-11-13), down from the 5,184 the 2026-11-06 verification recorded and up from the 3,618 of the prior window.
Independent coverage exists: Hlido's public-surface review scored it 70/100 on 2026-09-11 and FollowAgents' source review scored it 67/100 on 2026-10-04.
The hosted cloud tier Hlido recorded as unshipped in September reached early access by 2026-11-06.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Get-Concord-AI/concord-mcp&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Get-Concord-AI/concord-mcp&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Get-Concord-AI/concord-mcp&type=date&legend=top-left" />
</picture>

## Strengths

- Claim-before-edit overlap detection surfaces collisions at task start, not merge time.
- Agent-native deployment: one MCP server works with the harnesses teams already run, no new runtime to adopt.
- Writes carry optimistic concurrency (`expected_version`) and every ownership change lands in an append-only audit history.
- Handoffs and review packets carry scope, tests, risks, and provenance to the human reviewer.
- Local-first: state stays in `.concord/` (gitignored by default), so task content never leaves the machine on the open-source path.

## Cautions

- Telemetry to getconcord.ai is on by default, and the server-side IP and country-code fields it stores have no automatic expiry; disable it with `CONCORD_TELEMETRY_DISABLED=1` or `DO_NOT_TRACK=1` before use.
- Pre-1.0 churn: FollowAgents found the README's tool names drifting from the project's own test suite, and security fixes target only the latest version.
- `concord setup` merges instructions and registers servers across many client config files at once.
- Claims are advisory: the system depends on agents following their instructions, and agent-owned claims must never override CODEOWNERS, tests, or human review.
- The coordination value needs two or more agents in one shared checkout; the open-source package does nothing for a single agent or across repositories.
- There is no at-scale evidence of coordination outcomes, and the vendor itself says its demo measures dual-writer exposure, not merge-conflict reduction.

## Pricing

The local open-source server is free under MIT on one machine.
The cloud free tier is $0 in early access and adds multi-machine state, a dashboard, and Claude and ChatGPT apps.
The Team tier is $15 per seat per month, where a seat is a human member and agents are not seats; the site's own example prices four members at $60 per month for 12 agents.
As of 2026-11-06.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-11-06 | Team | Baseline at $15 per seat per month, local open-source and cloud free tiers at $0 | https://getconcord.ai/pricing |

## Compared to

**hcom** coordinates agents through terminal mailboxes with watching and spawning, a broader ad-hoc team fabric but without a claim ledger, review packets, or a task-memory contract.
**Foremerge** attacks the same collision problem with a publish-before-change protocol, signaling plan collisions without messaging, task state, or handoffs.
Choose Concord when the bottleneck is two or more agents claiming and handing off work inside one checkout, hcom when agents need to message and spawn each other across terminals, and Foremerge when the only need is catching colliding plans before edits land.

## Bottom line

Recommended for teams already running two or more coding agents against one repository and relaying context between windows by hand, who want explicit claims, handoffs, and review packets.
Not for single-agent workflows, for teams needing enforced isolation rather than advisory claims, or for hosted multi-repo coordination beyond the early-access cloud tier.

## Changes

- 2026-11-06 - Created.
- 2026-11-14 - Rotation re-verification: every cited URL re-fetched and live; v0.22.0 stands as the latest release, the npm trailing-month downloads refreshed to 4,131 (2026-10-14 to 2026-11-13).

## See also

- [hcom](../hcom/index.md) - the terminal messaging fabric alternative, agents coordinating over CLI mailboxes instead of a claim ledger.
- [Foremerge](../foremerge/index.md) - the publish-before-change protocol that catches the same plan collisions earlier in the loop.
- [Model Context Protocol (MCP)](../../protocols/mcp/index.md) - the protocol Concord ships on, grounding what an MCP-server coordination layer plugs into.
- [Managing many LLM agent sessions](../../../managing-many-llm-agent-sessions/index.md) - the corpus piece on the multi-session practices Concord's claim ledger formalizes.

## References

- https://github.com/Get-Concord-AI/concord-mcp - repository, README with the five tools, MIT license, 978 stars as of 2026-11-06, release v0.20.0 (2026-11-05).
- https://getconcord.ai/ - product surface, deployment model, and the not-an-orchestrator self-description.
- https://getconcord.ai/pricing - the free local and cloud tiers, Team at $15 per seat per month as of 2026-11-06.
- https://api.npmjs.org/downloads/point/2026-10-14:2026-11-13/@concord-ai/concord-mcp - 4,131 downloads in the trailing month (2026-11-14 fetch).
- https://registry.npmjs.org/@concord-ai/concord-mcp - the npm package's 35 published versions and latest 0.22.0.
- https://news.ycombinator.com/item?id=49464704 - the Show HN thread of 2026-08-27, 9 points and 4 comments.
- https://followagents.com/en/agents/concord-mcp - critical source review (67/100, telemetry-on-by-default, tool-name drift, pre-1.0 cautions).
- https://hlido.eu/reviews/get-concord-ai-concord-mcp/ - critical public-surface review (70/100 on 2026-09-11, cloud tier then unshipped, no at-scale evidence).
