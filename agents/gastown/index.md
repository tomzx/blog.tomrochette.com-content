---
title: Gas Town
created: 2026-08-27
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, orchestration, multi-agent, git-worktrees, open-source, tmux]
readability: 3
audience_notes: >
  Engineers running many coding agents who are deciding whether a supervision hierarchy beats a dashboard, and anyone following the Gas Town phenomenon.
  Assumes you know tmux, git worktrees, and what a merge queue is.
---

Gas Town is Steve Yegge's MIT-licensed multi-agent workspace manager (`gt`): a tmux-driven town where a Mayor agent coordinates 20-30 worker agents (polecats) across project rigs, with git-worktree hooks for persistence, a Bors-style merge queue, and beads as the work ledger.
Facts below verified as of 2026-09-05.

**Gas Town is the first orchestration tool that treats agent supervision as a hierarchy of agents rather than a dashboard of panes, and its deliberately chaotic rollout is the experiment: whether a self-governing town of agents is governable at all.**

## What it is

Install with `brew install gastown`, run `gt install ~/gt`, and you get a Town: per-project rigs wrapping git repositories, a Crew Member workspace for hands-on work, and polecats, worker agents with persistent identity but ephemeral sessions, spawned per task.
**Persistence is the design core: work state survives crashes and restarts because it lives in git-worktree hooks and the beads ledger, not in session memory.**
The supervision stack is deep: a Witness per rig detects stuck agents, a Deacon runs background patrol cycles dispatching Dogs for maintenance, convoys bundle beads into work units with autonomous stall detection, the Refinery batches merges through a bisecting verification queue, `gt escalate` routes blockers by severity, a scheduler governs dispatch to avoid rate-limit exhaustion, and Seance lets a new session interview its predecessor's logs.
Claude Code is the default runtime with Codex, Copilot, Gemini, and Cursor configurable, and Wasteland federates towns through DoltHub with reputation stamps.

## Status

Active, famous, and contested.
As of 2026-09-03: 17,909 stars, 1,650 forks, 442 open issues, created 2025-12-16, pushed 2026-09-02, latest release v1.2.1 on 2026-06-06.
**Its HN footprint dwarfs every tool in this section: the announcement thread (354 points), Maggie Appleton's field analysis (403 points), the v1.0 post (113 points), and the governance controversy (253 points).**
That controversy, [issue #3649](https://github.com/gastownhall/gastown/issues/3649), asked whether the town improves itself using agents running on users' LLM credits, and Appleton's account records the texture: entirely vibecoded, thousands of dollars a month in API burn, and a $GAS meme coin the project did not authorize.

## Strengths

- The Mayor-Witness-Deacon hierarchy supervises agents with agents, which is the only approach that scales past a screenful of panes.
- Persistent identity with ephemeral sessions is the right lifecycle: roles accumulate history, sessions stay cheap.
- The Refinery merge queue with verification gates is review infrastructure, the actual bottleneck, not just plumbing.
- The beads integration makes the task ledger and the execution layer one system, which no dashboard in this category does.

## Cautions

- Cost: a populated town burns real money monthly, and by its author's own account the thing was hastily built.
- Governance is an open question, the credits issue being the canonical thread, and federated reputation (Wasteland) is young.
- The dependency surface is heavy: Go, Dolt, bd, tmux, ICU headers, or Docker to contain it all.
- Vocabulary as interface (Mayor, polecats, convoys, molecules, seance) is charming and a hiring-and-onboarding tax at once.

## Pricing

Free and open source under MIT.
No paid tier; the runtime cost is your own agent credits, which is the controversy's denominator.

## Compared to

- [Conductor](../conductor/index.md) and [Emdash](../emdash/index.md): polished GUI dashboards for a handful of agents; choose them under 10 sessions, Gas Town when the town is the unit.
- [Vibe Kanban](../vibe-kanban/index.md): the kanban pattern without supervision hierarchy; a ghost town next to this.
- [OpenChamber](../openchamber/index.md): the session cockpit at calmer scale; choose it when you want visibility, not a civil service.

## Bottom line

**Recommended for agent-heavy engineers with budget and tolerance for churn who want to supervise 20+ agents with a hierarchy instead of a wall of terminals.**
Not for anyone with one agent, thin credits, or a compliance department.
The disagreeable claim I will defend: strip the metaphors away and what remains is the first working answer to supervision at scale, and the GUI dashboards will either grow a Deacon of their own or become furniture.

## See also

- [beads](../beads/index.md) - the ledger Gas Town runs on, same org
- [Conductor](../conductor/index.md) - the funded GUI counterpoint
- [Vibe Kanban](../vibe-kanban/index.md) - the orphaned kanban predecessor pattern
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where orchestration sits in the map

## References

- https://github.com/gastownhall/gastown - README: architecture, concepts, installation, prerequisites
- https://api.github.com/repos/gastownhall/gastown - stars, forks, issues, push dates as of 2026-09-03
- https://maggieappleton.com/gastown - the 403-point field analysis: patterns, bottlenecks, costs, the meme coin
- https://news.ycombinator.com/item?id=46458936 - the 354-point announcement thread (Welcome to Gas Town)
- https://github.com/gastownhall/gastown/issues/3649 - the credits-governance issue, 253-point HN discussion
- https://api.github.com/repos/gastownhall/gastown/releases - v1.2.1, 2026-06-06
