---
title: "Orchestration Feature Matrix"
created: 2026-08-24
updated: 2026-09-04
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, orchestration, git-worktrees, parallel-agents]
readability: 3
audience_notes: >
  Engineers shortlisting a parallel-agent orchestrator, dashboard or terminal multiplexer or board, who need the capability deltas at a glance.
  Assumes you know what a git worktree is and already run at least one CLI coding agent; each column links to a full note.
---

This matrix compares the twelve orchestration tools profiled in this section, the parallel-agent dashboards, worktree managers, control planes, and the one agent town, feature by feature, so the shortlisting step does not require reading twelve notes.
Everything below was verified against live sources on 2026-08-30, a full re-verification that added the Omnara column on that date, and re-verified on 2026-09-02, 2026-09-03, and 2026-09-04.

**Parallelism is already the free commodity in this category: the only things anyone pays for are review ergonomics and remote execution, and I expect more of these twelve to die or pivot before any of them becomes durable infrastructure.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Claude Squad](../claude-squad/index.md) | [cmux](../cmux/index.md) | [Conductor](../conductor/index.md) | [Crystal](../crystal/index.md) | [dmux](../dmux/index.md) | [Emdash](../emdash/index.md) | [Gas Town](../gastown/index.md) | [Omnara](../omnara/index.md) | [Paseo](../paseo/index.md) | [Superset](../superset/index.md) | [Vibe Kanban](../vibe-kanban/index.md) | [Worktrunk](../worktrunk/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | terminal TUI | native macOS terminal | native Mac app | Electron app | terminal TUI | Electron app | tmux town, workspace manager | Go control plane, web, CLI, API, mobile, Slack | daemon plus desktop, web, mobile clients | Electron agentic IDE | web UI, Rust backend | CLI worktree manager |
| Platforms | macOS, Linux (tmux, no Windows) | macOS only | macOS only (local) | macOS first, Linux later | macOS, Linux (tmux) | macOS, Windows, Linux | macOS, Linux, Windows, Docker | web, iOS, Android, Slack; self-host or Omnara Cloud | macOS, Windows, Linux, iOS, Android, web, Docker | macOS, Linux experimental | any OS with Node | macOS, Linux, Windows |
| Open source | ✓ AGPL-3.0 | ~ GPL-3.0, open core | ✗ closed | ✓ MIT | ✓ MIT | ✓ Apache-2.0 | ✓ MIT | ✓ Apache-2.0 | ✓ Apache-2.0 | ~ Elastic License 2.0 | ✓ Apache-2.0 | ✓ MIT OR Apache-2.0 |
| Price model | free, no tier | free, Pro $40/mo | free local, Pro $50/mo | free (Nimbalyst sells teams) | free | free core, cloud contact-sales | free, BYOK runtime | free self-host, cloud unpriced | free, Hub hosted €15/seat/mo | free local, Pro $15-20/user/mo | free (subs terminated) | free |
| Per-task worktree isolation | ✓ | ? | ✓ own branch | ✓ | ✓ AI-named branch | ✓ | ✓ worktree hooks | ? | ✓ | ✓ | ✓ own branch | ✓ core purpose |
| Harnesses it can drive | any CLI via profiles | any CLI agent | 4 (Claude Code, Codex, Cursor, OpenCode) | 2 (Claude Code, Codex) | 11 CLIs | 25+ CLIs, auto-detected | 5 runtimes, Claude Code default | ? agent underneath unspecified | 4 native + ~36 via ACP | any CLI, 14+ presets | 10+ agents | any CLI via -x, one program name since v0.76 |
| Remote or SSH execution | ? | ~ SSH sessions | ? | ? | ✗ local only | ✓ SSH-first | ~ Docker compose | ✓ machine pools | ✓ encrypted relay, self-host | ~ remote workspaces beta | ~ Docker self-host | ✗ local git |
| Built-in review tooling | ~ diff preview tab | ? | ✓ diffs, checks, PR, review | ~ diff viewer, rebase, squash | ~ merge and PR menu | ✓ diffs, PRs, CI checks | ✓ Refinery merge queue | ~ approvals, questions, events, artifacts | ~ agent output and diffs | ✓ diffs, browser previews | ✓ diffs, comments, PR | ~ status table and merge pipeline |
| Cloud execution option | ✗ no hosting | ✓ Pro, up to 50 cloud VMs | ✓ Vercel sandboxes | ? | ✗ | ~ contact-sales | ✗ self-host, Wasteland federation | ✓ Omnara Cloud, or self-host | ~ self-host anywhere, no vendor cloud | ~ remote workspaces beta | ✗ services removed | ✗ |
| Current status | active, slow burn | active, fast | active, $22M raised | deprecated Feb 2026 | active | active, YC W26 | active, 17.9k stars | active, YC S25, 2,814 stars | active, v0.7, solo maintainer | active, YC P26, $11M raised | orphaned, no push since 2026-04-24 | active, pre-1.0 fast |

## Reading the matrix

**The platform rows tell you who these tools are for: Mac-first GUI shops and unix terminal people, with Emdash alone covering all three desktop OSes and the tmux pair unable to follow anyone to Windows.**
cmux and Conductor are macOS only, and Crystal was macOS first with Linux later.
Vibe Kanban's web UI goes anywhere Node goes, which is the one structural advantage of the board design.

**Worktree isolation is the entry ticket, not the differentiator: every tool here except cmux gives each task its own worktree and branch, so the real spread is harness breadth, from Crystal's two to Emdash's 25+.**
cmux's "?" is structural rather than a gap: it is a terminal built for attention routing, not a session manager, and its note records no worktree feature.
The wrapping pattern dominates (Emdash auto-detects installed CLIs, Claude Squad launches anything through profiles, dmux lists eleven), which means new harness features arrive without waiting for the orchestrator to reimplement them.

**Where your code lives is the quiet differentiator, and Emdash is alone in treating it as a design decision with SSH-first execution and credentials in the OS keychain.**
Cloud execution exists only where a subscription needs it, cmux Pro and Conductor Cloud; dmux is explicitly local-only, Claude Squad ships no hosting at all, and Vibe Kanban's remote services were removed thirty days after its shutdown announcement.

**The status row is the most instructive one in the matrix: of twelve tools, one is deprecated, one lost its vendor, and the counterexamples run on venture rounds and a very loud founder.**
Crystal was deprecated in February 2026 in favor of Nimbalyst, the clearest signal yet that a pure worktree-session manager can be a feature rather than a product.
Bloop shut down in April 2026 and Vibe Kanban is orphaned, local workspaces intact but no push since 2026-04-24 and nobody paid to fix bugs.
Conductor staying a pure session manager and raising money is what keeps the feature-versus-product question contested instead of settled.
**The three 2026 columns sharpen the funding split: Superset raised $11M, Paseo is a solo maintainer with a planned business, and Worktrunk is a single author with no company at all, which is the whole sustainability spectrum in one row.**
**Omnara is the twelfth column and the only one that wants to own execution and state:** agents become YAML configs in your repo, machine pools separate where code runs from who can invoke it, and supervision reaches you from a dashboard, phone, CLI, REST API, or Slack, the open-source counterpoint to Claude Managed Agents.

**Review is the bottleneck this category actually sells, and delivery tracks funding: Conductor has the deepest review surface (diffs, checks, PR page, code review), Emdash and Vibe Kanban carry full PR flows, and the terminal tools stop at diff tabs and merge menus.**
Claude Squad's preview tab and dmux's pane-menu PR cover the dispatch, wait, review, merge loop, but nobody should expect checks or inline comments there.
**Gas Town is the exception that proves the row: its Refinery is a Bors-style merge queue with verification gates, review as infrastructure rather than review as a pane.**

## Choosing from the matrix

- Want the deepest GUI review flow on a Mac and accept a closed client: Conductor.
- Want an auditable client, Windows or Linux support, or agents running next to remote code: Emdash.
- Live in the terminal: Claude Squad for the smallest footprint, dmux for multi-agent fan-out and resumable panes.
- On macOS and drowning in sessions that need attention: cmux's notification rings and unread panel.
- Want planning-first and vendor-less: Vibe Kanban, accepting that it is orphaned, with no push since April 2026.
- Want to supervise agents from your phone over an encrypted relay, self-hosted and FOSS: Paseo.
- Want a control plane that owns agent execution and state behind one API, on your own hardware: Omnara.
- Want a macOS agentic IDE around your existing subscriptions, five or more parallel sessions: Superset, accepting the ELv2 license and beta Linux.
- Want the worktree lifecycle automated inside your own shell with no app at all: Worktrunk.
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
- https://cmux.com/pricing - tiers, the 50-VM cloud cap, CodeRouter removal for the cmux column
- https://conductor.build/pricing/ - tiers, sandbox specs, local versus cloud privacy for the Conductor column
- https://github.com/stravu/crystal - deprecation notice and feature history for the Crystal column
- https://github.com/standardagents/dmux - supported agent list, hooks, local-only scope for the dmux column
- https://emdash.com/ - agent support, SSH model, downloads for the Emdash column
- https://github.com/BloopAI/vibe-kanban - sunset banner and feature list for the Vibe Kanban column
- https://github.com/gastownhall/gastown - architecture, runtimes, Refinery, Docker setup for the Gas Town column
- https://maggieappleton.com/gastown - the field analysis grounding the Gas Town status and cost cells
- https://github.com/omnara-ai/omnara - control plane, license, and stars for the Omnara column
- https://www.vibekanban.com/blog/shutdown - shutdown date, service removal, refunds for the status row
- https://github.com/getpaseo/paseo - platforms, agent catalog, relay, and license for the Paseo column
- https://github.com/superset-sh/superset - worktree model, presets, ELv2 license, and funding for the Superset column
- https://github.com/max-sixty/worktrunk - commands, hooks, license, and release cadence for the Worktrunk column
