---
title: Paperclip
created: 2026-08-27
updated: 2026-09-02
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, control-planes, agent-operations, multi-agent, open-source, governance]
readability: 3
audience_notes: >
  Engineers or solo operators running several AI agents toward business goals who are deciding between a control plane and a pile of terminals.
  Assumes you already run at least one agent (OpenClaw, Claude Code, Codex, Cursor) and know what a cron schedule is.
---

Paperclip (paperclipai/paperclip) is an MIT-licensed, self-hostable control plane for a company of AI agents: a Node.js server and React UI where agents check work out of a ticket board via scheduled heartbeats, wrapped in org charts, budgets, approvals, skills, and an audit log.
Facts below verified as of 2026-09-04.

**The name is the thesis: an agent-company platform named after the paperclip maximizer is selling governance as the product (budgets that pause agents, approvals, chain of command, immutable audit trails), and about 79k stars in its first six months say the market wants exactly that.**

## What it is

Install with a checksummed script from [paperclip.ing](https://paperclip.ing) or `npx paperclipai onboard`; one Node.js process runs the API, a React UI (with a phone-served variant), and an embedded PostgreSQL, no account required.
**The unit of work is the ticket agents check out from, with real conflict semantics (a checkout owned by another agent returns 409), and the unit of life is the heartbeat: agents wake on schedules and events (assignment, comments, @-mentions), act, and exit, rather than running continuously.**
The README's four pillars are the task manager, an org chart for mixed human and agent roles, employee training (Skill Studio, evals, agent performance reviews), and an agentic OS layer with sandboxed cloud execution (e2b, Cloudflare, Daytona, Modal, Novita, self-hosted Kubernetes) plus SSO, RBAC, and cost controls.
Any agent that can receive a heartbeat is hirable, OpenClaw, Claude Code, Codex, Cursor, plain HTTP, and one deployment can run multiple companies with data isolation.

## Status

Active at extreme velocity.
As of 2026-09-02: 79,854 stars and 14,654 forks since creation on 2026-03-02, 5,336 open issues, pushed the day of verification, latest release v2026.831.1 on 2026-09-02 (date-versioned), cloud deployments in waitlist with multi-tenant isolation already shipped per the roadmap.
**Its Hacker News footprint is nearly empty: the April 2026 Show HN got 3 points, so the growth ran through X and Discord instead, which tells you who the audience is.**
The roadmap is public about what does not exist yet: memory and knowledge, work queues, self-organization, CEO chat, and one item called MAXIMIZER MODE, the joke made explicit.

## Strengths

- The company abstraction fits agent work better than the session abstraction: goals trace to a mission, budgets cap spend per agent, and approvals gate real decisions.
- Agent-agnostic by contract, so your OpenClaw or Claude Code investment carries over unchanged.
- Self-hosted with an embedded database and no vendor account; the quickstart is genuinely one command.
- Audit-first: run ids on every mutating call, immutable activity log, artifacts and work products attached to issues.

## Cautions

- The quickstart defaults to a trusted local loopback mode, and the README itself tells you to pick an authenticated bind preset for anything beyond the first run; read before you expose.
- 5,336 open issues at six months old is a support surface growing as fast as the star count.
- Date-versioned near-daily releases mean you are always upgrading; pin deliberately.
- The pitch says autonomous businesses while the memory, work-queue, and self-organization pillars are still roadmap items, so expect to supervise more than the landing page implies.
- Name collisions: desktop Clippy-style tools also call themselves paperclip (agent-paperclip, clippyai-desktop); search carefully.

## Pricing

Open source under MIT, self-hosted, no account.
A hosted cloud is in waitlist with no published pricing as of 2026-09-02.

## Compared to

- [OpenClaw](../openclaw/index.md) (388,571 stars as of 2026-09-02): the employee, not the company; Paperclip's own line is "if OpenClaw is an employee, Paperclip is the company", and it manages OpenClaw instances among others.
- [Gas Town](../gastown/index.md): supervision for many coding agents inside one workspace; choose Gas Town for repo work, Paperclip when the goal is a business, not a codebase.
- [beads](../beads/index.md) with a plain harness: the ledger-plus-heartbeat pattern you can assemble yourself when a whole company is overkill.

## Bottom line

**Recommended for operators running multiple agents toward business goals who want budgets, approvals, and audit trails instead of a wall of terminals.**
Not for single-agent coding workflows, where a harness plus a task tracker is sufficient machinery.
The disagreeable claim I will defend: "manage business goals, not pull requests" is the correct split in this whole section, the worktree orchestrators and the goal control plane are different products, and Paperclip is the first open-source tool to get the second abstraction right.

## See also

- [Gas Town](../gastown/index.md) - the repo-scale counterpart to the company-scale control plane
- [Executions Feature Matrix](../executions-feature-matrix/index.md) - the smaller scheduled-trigger layer Paperclip generalizes
- [Managing Many Concurrent LLM Agent Sessions](../../managing-many-llm-agent-sessions/index.md) - the supervision problem the heartbeat model answers
- [Read the Commits, Not the Manual](../../learnings-from-openclaw/index.md) - how the biggest employee-side project sustains its own scale

## References

- https://github.com/paperclipai/paperclip - README: pillars, quickstart defaults, FAQ, roadmap
- https://api.github.com/repos/paperclipai/paperclip - stars, forks, issues, push dates as of 2026-09-02
- https://paperclip.ing - homepage, release line, testimonials
- https://docs.paperclip.ing - official documentation
- https://api.github.com/repos/paperclipai/paperclip/releases - v2026.831.1, 2026-09-02
- https://news.ycombinator.com/item?id=47903549 - the 3-point Show HN, the thin-footprint signal
- https://api.github.com/repos/openclaw/openclaw - OpenClaw scale for the comparison
