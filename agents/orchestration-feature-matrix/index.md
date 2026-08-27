---
title: "Orchestration Feature Matrix"
created: 2026-08-24
updated: 2026-08-27
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, comparison, orchestration, git-worktrees, parallel-agents]
readability: 3
audience_notes: >
  Engineers shortlisting a parallel-agent orchestrator, dashboard or terminal multiplexer or board, who need the capability deltas at a glance.
  Assumes you know what a git worktree is and already run at least one CLI coding agent; each column links to a full note.
---

This matrix compares the eight orchestration tools profiled in this section, the parallel-agent dashboards, worktree managers, and the one agent town, feature by feature, so the shortlisting step does not require reading eight notes.
Everything below was verified against live sources on 2026-08-24; the Gas Town column on 2026-08-27.

**Parallelism is already the free commodity in this category: the only things anyone pays for are review ergonomics and remote execution, and I expect more of these eight to die or pivot before any of them becomes durable infrastructure.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Claude Squad](../claude-squad/index.md) | [cmux](../cmux/index.md) | [Conductor](../conductor/index.md) | [Crystal](../crystal/index.md) | [dmux](../dmux/index.md) | [Emdash](../emdash/index.md) | [Gas Town](../gastown/index.md) | [Vibe Kanban](../vibe-kanban/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | terminal TUI | native macOS terminal | native Mac app | Electron app | terminal TUI | Electron app | tmux town, workspace manager | web UI, Rust backend |
| Platforms | macOS, Linux (tmux, no Windows) | macOS only | macOS only (local) | macOS first, Linux later | macOS, Linux (tmux) | macOS, Windows, Linux | macOS, Linux, Windows, Docker | any OS with Node |
| Open source | ✓ AGPL-3.0 | ~ GPL-3.0, open core | ✗ closed | ✓ MIT | ✓ MIT | ✓ Apache-2.0 | ✓ MIT | ✓ Apache-2.0 |
| Price model | free, no tier | free, Pro $24/mo | free local, Pro $50/mo | free (Nimbalyst sells teams) | free | free core, cloud contact-sales | free, BYOK runtime | free (subs terminated) |
| Per-task worktree isolation | ✓ | ? | ✓ own branch | ✓ | ✓ AI-named branch | ✓ | ✓ worktree hooks | ✓ own branch |
| Harnesses it can drive | any CLI via profiles | any CLI agent | 4 (Claude Code, Codex, Cursor, OpenCode) | 2 (Claude Code, Codex) | 11 CLIs | 25+ CLIs, auto-detected | 5 runtimes, Claude Code default | 10+ agents |
| Remote or SSH execution | ? | ~ SSH sessions | ? | ? | ✗ local only | ✓ SSH-first | ~ Docker compose | ~ Docker self-host |
| Built-in review tooling | ~ diff preview tab | ? | ✓ diffs, checks, PR, review | ~ diff viewer, rebase, squash | ~ merge and PR menu | ✓ diffs, PRs, CI checks | ✓ Refinery merge queue | ✓ diffs, comments, PR |
| Cloud execution option | ✗ no hosting | ✓ Pro cloud VMs | ✓ Vercel sandboxes | ? | ✗ | ~ contact-sales | ✗ self-host, Wasteland federation | ✗ services removed |
| Current status | active, slow burn | active, fast | active, $22M raised | deprecated Feb 2026 | active | active, YC W26 | active, 17.8k stars | community-maintained |

## Reading the matrix

**The platform rows tell you who these tools are for: Mac-first GUI shops and unix terminal people, with Emdash alone covering all three desktop OSes and the tmux pair unable to follow anyone to Windows.**
cmux and Conductor are macOS only, and Crystal was macOS first with Linux later.
Vibe Kanban's web UI goes anywhere Node goes, which is the one structural advantage of the board design.

**Worktree isolation is the entry ticket, not the differentiator: every tool here except cmux gives each task its own worktree and branch, so the real spread is harness breadth, from Crystal's two to Emdash's 25+.**
cmux's "?" is structural rather than a gap: it is a terminal built for attention routing, not a session manager, and its note records no worktree feature.
The wrapping pattern dominates (Emdash auto-detects installed CLIs, Claude Squad launches anything through profiles, dmux lists eleven), which means new harness features arrive without waiting for the orchestrator to reimplement them.

**Where your code lives is the quiet differentiator, and Emdash is alone in treating it as a design decision with SSH-first execution and credentials in the OS keychain.**
Cloud execution exists only where a subscription needs it, cmux Pro and Conductor Cloud; dmux is explicitly local-only, Claude Squad ships no hosting at all, and Vibe Kanban's remote services were removed thirty days after its shutdown announcement.

**The status row is the most instructive one in the matrix: of eight tools, one is deprecated, one lost its vendor, and the counterexamples run on a $22M Series A and a very loud founder.**
Crystal was deprecated in February 2026 in favor of Nimbalyst, the clearest signal yet that a pure worktree-session manager can be a feature rather than a product.
Bloop shut down in April 2026 and Vibe Kanban survives community-maintained, local workspaces intact but nobody paid to fix bugs.
Conductor staying a pure session manager and raising money is what keeps the feature-versus-product question contested instead of settled.

**Review is the bottleneck this category actually sells, and delivery tracks funding: Conductor has the deepest review surface (diffs, checks, PR page, code review), Emdash and Vibe Kanban carry full PR flows, and the terminal tools stop at diff tabs and merge menus.**
Claude Squad's preview tab and dmux's pane-menu PR cover the dispatch, wait, review, merge loop, but nobody should expect checks or inline comments there.
**Gas Town is the exception that proves the row: its Refinery is a Bors-style merge queue with verification gates, review as infrastructure rather than review as a pane.**

## Choosing from the matrix

- Want the deepest GUI review flow on a Mac and accept a closed client: Conductor.
- Want an auditable client, Windows or Linux support, or agents running next to remote code: Emdash.
- Live in the terminal: Claude Squad for the smallest footprint, dmux for multi-agent fan-out and resumable panes.
- On macOS and drowning in sessions that need attention: cmux's notification rings and unread panel.
- Want planning-first and vendor-less: Vibe Kanban, accepting community-only maintenance.
- Supervising 20 or more agents with agent watchers and a merge queue, credits and churn accepted: Gas Town.
- Do not adopt Crystal today; if its idea appeals, evaluate Nimbalyst on its own merits.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the same treatment for the harness layer these tools drive
- [Surface Feature Matrix](../surface-feature-matrix/index.md) - the same treatment for editors and environments
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the map these columns come from
- [Managing Many Concurrent LLM Agent Sessions](../../managing-many-llm-agent-sessions/index.md) - the supervision problem the whole category answers
- [OpenChamber](../openchamber/index.md) - scheduled sessions, the non-interactive complement to parallel dispatch

## References

- https://github.com/smtg-ai/claude-squad - profiles, worktrees, packaging for the Claude Squad column
- https://cmux.com/pricing - tiers, cloud VM hours, CodeRouter for the cmux column
- https://conductor.build/pricing/ - tiers, sandbox specs, local versus cloud privacy for the Conductor column
- https://github.com/stravu/crystal - deprecation notice and feature history for the Crystal column
- https://github.com/standardagents/dmux - supported agent list, hooks, local-only scope for the dmux column
- https://emdash.com/ - agent support, SSH model, downloads for the Emdash column
- https://github.com/BloopAI/vibe-kanban - sunset banner and feature list for the Vibe Kanban column
- https://github.com/gastownhall/gastown - architecture, runtimes, Refinery, Docker setup for the Gas Town column
- https://maggieappleton.com/gastown - the field analysis grounding the Gas Town status and cost cells
- https://www.vibekanban.com/blog/shutdown - shutdown date, service removal, refunds for the status row
