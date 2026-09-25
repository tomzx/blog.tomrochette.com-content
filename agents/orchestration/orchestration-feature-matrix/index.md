---
title: "Orchestration Feature Matrix"
created: 2026-08-24
updated: 2026-09-24
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, orchestration, git-worktrees, parallel-agents]
readability: 3
audience_notes: >
  Engineers shortlisting a parallel-agent orchestrator, dashboard or terminal multiplexer or board, who need the capability deltas at a glance.
  Assumes you know what a git worktree is and already run at least one CLI coding agent; each column links to a full note.
---

This matrix compares the sixteen orchestration tools profiled in this section, the parallel-agent dashboards, worktree managers, control planes, mobile clients, a coordination protocol, a cluster-scale agent fleet orchestrator, JetBrains' standalone agent environment, and the one agent town, feature by feature, so the shortlisting step does not require reading sixteen notes.

**Parallelism is already the free commodity in this category: the only things anyone pays for are review ergonomics and remote execution, and I expect more of these sixteen to die or pivot before any of them becomes durable infrastructure.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [AX](../ax/index.md) | [Claude Squad](../claude-squad/index.md) | [cmux](../cmux/index.md) | [Conductor](../conductor/index.md) | [Crystal](../crystal/index.md) | [dmux](../dmux/index.md) | [Emdash](../emdash/index.md) | [Foremerge](../foremerge/index.md) | [Gas Town](../gastown/index.md) | [Happy Coder](../happy-coder/index.md) | [JetBrains Air](../jetbrains-air/index.md) | [Omnara](../omnara/index.md) | [Paseo](../paseo/index.md) | [Superset](../superset/index.md) | [Vibe Kanban](../vibe-kanban/index.md) | [Worktrunk](../worktrunk/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | Kubernetes agent-fleet orchestrator | terminal TUI | native macOS terminal | native Mac app | Electron app | terminal TUI | Electron app | coordination protocol above Git, CLI plus MCP server | tmux town, workspace manager | native mobile and macOS client, wraps the agent CLI | standalone agent environment, desktop app plus org web | Go control plane, web, CLI, API, mobile, Slack | daemon plus desktop, web, mobile clients | Electron agentic IDE | web UI, Rust backend | CLI worktree manager |
| Platforms | Kubernetes clusters; Linux or macOS CLI (Go) | macOS, Linux (tmux, no Windows) | macOS only | macOS only (local) | macOS first, Linux later | macOS, Linux (tmux) | macOS, Windows, Linux | macOS, Linux, Windows binaries; local, single machine | macOS, Linux, Windows, Docker | iOS, Android, macOS, web | macOS, Windows, Linux desktop; org-only web | web, iOS, Android, Slack; self-host or Omnara Cloud | macOS, Windows, Linux, iOS, Android, web, Docker | macOS, Linux experimental | any OS with Node | macOS, Linux, Windows |
| Open source | ✓ Apache-2.0 | ✓ AGPL-3.0 | ~ GPL-3.0, open core | ✗ closed | ✓ MIT | ✓ MIT | ✓ Apache-2.0 | ✓ Apache-2.0 | ✓ MIT | ✓ MIT | ✗ closed | ✓ Apache-2.0 | ✓ Apache-2.0 | ~ Elastic License 2.0 | ✓ Apache-2.0 | ✓ MIT OR Apache-2.0 |
| Price model | free, open source | free, no tier | free, Pro $50/mo, Max $200/mo | free local, Pro $50/mo | free (Nimbalyst sells teams) | free | free core, cloud contact-sales | free, open source | free, BYOK runtime | free, donations | included with JetBrains AI Pro/Ultimate, BYOK supported | free self-host, cloud usage-priced | free, Hub hosted €15/seat/mo | free local, Pro $15-20/user/mo | free (subs terminated) | free |
| Per-task worktree isolation | ~ sandboxed tasks with pre-wired git workspaces, not worktrees | ✓ | ? | ✓ own branch | ✓ | ✓ AI-named branch | ✓ | ~ assumes the worktrees you already run | ✓ worktree hooks | ✗ existing paths only | ✓ worktree, Docker, or cloud per task | ? | ✓ | ✓ own branch | ✓ own branch | ✓ core purpose |
| Harnesses it can drive | any agent container, bring-your-own runner image | any CLI via profiles | any CLI agent | 4 (Claude Code, Codex, Cursor, OpenCode) | 2 (Claude Code, Codex) | 11 CLIs | 25+ CLIs, auto-detected | any MCP client plus CLI and JSON API; setup auto-wires Claude Code, Codex, Cursor | 5 runtimes, Claude Code default | 2 (Claude Code, Codex) | 4 built-in (Claude Agent, Codex, Gemini CLI, Junie) + any ACP agent | ? agent underneath unspecified | 4 native + ~36 via ACP | any CLI, 21 presets | 10+ agents | any CLI via -x, one program name since v0.76 |
| Remote or SSH execution | ✓ cluster-native, ax ssh into sandboxes | ? | ~ SSH sessions | ? | ? | ✗ local only | ✓ SSH-first | ✗ local, single machine | ~ Docker compose | ✓ E2E-encrypted relay | ✓ JetBrains cloud, org web | ✓ machine pools | ✓ encrypted relay, self-host | ~ remote workspaces beta | ~ Docker self-host | ✗ local git |
| Built-in review tooling | ~ watch, logs, and ssh, no review surface | ~ diff preview tab | ? | ✓ diffs, checks, PR, review | ~ diff viewer, rebase, squash | ~ merge and PR menu | ✓ diffs, PRs, CI checks | ~ advisory conflict findings, verification-gated ChangeSets, no diff surface | ✓ Refinery merge queue | ~ diffs and terminals beside conversations | ✓ language-aware diffs, Agent Review (agent reviews agent) | ~ approvals, questions, events, artifacts | ~ agent output and diffs | ✓ diffs, browser previews | ✓ diffs, comments, PR | ~ status table and merge pipeline |
| Cloud execution option | ✓ is the cloud execution layer | ✗ no hosting | ✓ Pro, up to 50 cloud VMs | ✓ Vercel sandboxes | ? | ✗ | ~ contact-sales | ✗ local only | ✗ self-host, Wasteland federation | ✗ your machine only | ✓ JetBrains-managed cloud environments | ✓ Omnara Cloud, or self-host | ~ self-host anywhere, no vendor cloud | ~ remote workspaces beta | ✗ services removed | ✗ |
| Current status | active, Google team, v0.3.0, pre-stable | active, slow burn | active, fast | active, $22M raised | deprecated Feb 2026 | active | active, YC W26 | active, 505 stars, pre-1.0, v0.5.0 | shut down Sept 2026, repo kept as death record | active, 23.9k stars, community team | active, public preview, v262.834.41 | active, YC S25, 2,863 stars | active, v0.9.2, solo maintainer | active, YC P26, $11M raised | orphaned, community commits resumed 2026-09-16, v0.1.45 prerelease on GitHub, npm still 0.1.44 | active, pre-1.0 fast |

## Reading the matrix

**The platform rows tell you who these tools are for: Mac-first GUI shops and unix terminal people, with Emdash the only GUI covering all three desktop OSes and the tmux pair unable to follow anyone to Windows.**
cmux and Conductor are macOS only, and Crystal was macOS first with Linux later.
Vibe Kanban's web UI goes anywhere Node goes, which is the one structural advantage of the board design.

**Worktree isolation is the entry ticket, not the differentiator: every tool here except cmux and Foremerge gives each task its own worktree and branch, so the real spread is harness breadth, from Crystal's two to Emdash's 25+.**
cmux's "?" is structural rather than a gap: it is a terminal built for attention routing, not a session manager, and its note records no worktree feature.
Foremerge's tilde is the opposite of a gap: it assumes the worktrees you already run and coordinates plans across them, the one column whose unit of work is the intent rather than the task.
The wrapping pattern dominates (Emdash auto-detects installed CLIs, Claude Squad launches anything through profiles, dmux lists eleven), which means new harness features arrive without waiting for the orchestrator to reimplement them.

**Where your code lives is the quiet differentiator, and Emdash is alone in treating it as a design decision with SSH-first execution and credentials in the OS keychain.**
Cloud execution exists only where a subscription or usage bill is attached, cmux Pro, Conductor Cloud, Omnara Cloud, and JetBrains-managed cloud tasks; dmux is explicitly local-only, Claude Squad ships no hosting at all, and Vibe Kanban's remote services were removed thirty days after its shutdown announcement.

**The status row is the most instructive one in the matrix: of sixteen tools, one is deprecated, one lost its vendor, one is a cluster-scale platform entrant, one new column attacks the failure worktrees cannot see, and the counterexamples run on venture rounds and a very loud founder.**
Crystal was deprecated in February 2026 in favor of Nimbalyst, the clearest signal yet that a pure worktree-session manager can be a feature rather than a product.
Bloop shut down in April 2026 and Vibe Kanban is orphaned, local workspaces intact, ten commits on the default branch since the shutdown (the first a 2026-09-15 version bump by a former Bloop maintainer, nine more with substantive fixes through 2026-09-19), a v0.1.45 prerelease published on GitHub on 2026-09-19 with npm still serving 0.1.44 as latest, and nobody paid to fix bugs.
Conductor staying a pure session manager and raising money is what keeps the feature-versus-product question contested instead of settled.
**The three 2026 columns sharpen the funding split: Superset raised $11M, Paseo is a solo maintainer with a planned business, and Worktrunk is a single author with no company at all, which is the whole sustainability spectrum in one row.**
**Omnara is the tenth column and the only one that wants to own execution and state:** agents become YAML configs in your repo, machine pools separate where code runs from who can invoke it, and supervision reaches you from a dashboard, phone, CLI, REST API, or Slack, the open-source counterpoint to Claude Managed Agents.
**Happy Coder is the purest thin client in the table:** two harnesses, no worktrees, no hosting, yet 23.8k stars, second only to cmux among maintained tools, because phone access to the sessions you already run is what people actually install.
**JetBrains Air is the vendor entry, and it is the only column whose price model is a bundle:** no standalone fee, four agent families unlocked by a JetBrains AI Pro or Ultimate subscription, with the deepest isolation menu in the table (worktree, Docker, or cloud per task) and org governance behind it, which makes it the strongest evidence yet that this layer is a feature incumbents will attach to existing subscriptions.
**AX is the scale outlier at the front of the table:** Google's Kubernetes-based fleet orchestrator treats agents as a datacenter workload class with sandboxing, network fencing, and checkpoint-resume, which makes every other column here look like what it is, a desktop tool.
**Foremerge is the newest column and the only one that coordinates plans instead of hosting sessions:** agents publish intents with semantic scopes before they edit, and a deterministic detector flags destructive-versus-additive collisions that git merges cleanly, which names the residue every worktree column here leaves behind.

**Review is the bottleneck this category actually sells, and delivery tracks funding: Conductor has the deepest review surface (diffs, checks, PR page, code review), Emdash and Vibe Kanban carry full PR flows, and the terminal tools stop at diff tabs and merge menus.**
Claude Squad's preview tab and dmux's pane-menu PR cover the dispatch, wait, review, merge loop, but nobody should expect checks or inline comments there.
**Gas Town is the exception that proves the row: its Refinery is a Bors-style merge queue with verification gates, review as infrastructure rather than review as a pane.**

## Choosing from the matrix

- Want the deepest GUI review flow on a Mac and accept a closed client: Conductor.
- Want an auditable client, Windows or Linux support, or agents running next to remote code: Emdash.
- Live in the terminal: Claude Squad for the smallest footprint, dmux for multi-agent fan-out and resumable panes.
- On macOS and drowning in sessions that need attention: cmux's notification rings and unread panel.
- Want planning-first and vendor-less: Vibe Kanban, accepting that it is orphaned, with community commits resumed but no stable release since April 2026.
- Want to supervise agents from your phone over an encrypted relay, self-hosted and FOSS: Paseo.
- Want your existing Claude Code or Codex sessions on a phone, end-to-end encrypted, and nothing more: Happy Coder.
- Want a control plane that owns agent execution and state behind one API, on your own hardware: Omnara.
- Want declarative fleet-scale orchestration on Kubernetes instead of a desktop app: AX, accepting pre-stable churn and cluster operations.
- Want a macOS agentic IDE around your existing subscriptions, five or more parallel sessions: Superset, accepting the ELv2 license and beta Linux.
- Already pay for JetBrains AI Pro or Ultimate and want isolation choice plus org governance around four agent families: JetBrains Air, accepting the preview status and credits-only cloud.
- Want the worktree lifecycle automated inside your own shell with no app at all: Worktrunk.
- Run several agents in parallel worktrees on one repo and fear clean merges that break the design: Foremerge, advisory and local-first.
- Supervising 20 or more agents with agent watchers and a merge queue, credits and churn accepted: Gas Town.
- Do not adopt Crystal today; if its idea appeals, evaluate Nimbalyst on its own merits.

## Changes

- 2026-08-24 - Created with seven tools and the death and orphan stories carried into the reading section.
- 2026-08-27 - Extended from seven to eight columns with Gas Town and canonicalized the emdash reference.
- 2026-08-30 - Added Paseo, Superset, and Worktrunk columns, reaching eleven, with a funding-spectrum sentence.
- 2026-09-06 - Extended from twelve to thirteen columns with Happy Coder.
- 2026-09-13 - Corrected the Happy Coder and JetBrains Air columns, whose body cells had been transposed since the Air column was added on 2026-09-12.
- 2026-09-13 - Reframed Gas Town's status to active but cooling (no default-branch commit since 2026-07-23, no release since v1.2.1 in June).
- 2026-09-20 - Moved Gas Town's status cell to shut down (September 2026, Yegge's admission per Dan Luu via AINews), matching the note's death record.
- 2026-09-13 - Corrected the Vibe Kanban orphan wording to no default-branch commit since 2026-04-24, named Omnara Cloud and JetBrains cloud tasks in the cloud-execution prose, and qualified Happy Coder's star ranking as second among maintained tools.
- 2026-09-16 - Re-verification: recorded Vibe Kanban's first post-shutdown default-branch commit (2026-09-15), refreshed the Omnara star count to 2,851, and updated the JetBrains Air release to 262.834.41.
- 2026-09-18 - Re-verification: recorded Vibe Kanban's community commits resuming (eight on the default branch since 2026-09-15, still no release), moved the cmux price cell to the new monthly-only Pro $50 and Max $200 tiers, refreshed the Omnara star count to 2,857, and corrected the stale Air changelog version in the references.
- 2026-09-20 - Re-verification: moved the Vibe Kanban status cell to the community's 0.1.45 tag, which npm and the release list do not publish yet, and refreshed the Omnara star count to 2,861.
- 2026-09-21 - Extended from fourteen to fifteen columns with AX (Google's cluster-scale agent fleet orchestrator, added sorted into the first position), refreshed the Happy Coder star count to 23.9k, and moved the Paseo status cell to v0.8 with 0.9 betas.
- 2026-09-22 - Extended from fifteen to sixteen columns with Foremerge (Nick Woodhead's coordination protocol for parallel agents, added sorted after Emdash), moved the Paseo status cell to v0.9.1, and refreshed the Omnara star count to 2,863.
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-24 - Refreshed the Vibe Kanban status cell to the GitHub v0.1.45 prerelease (npm still 0.1.44), moved Paseo's status cell to v0.9.2, and refreshed Foremerge's star count to 505.

## See also

- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - the same treatment for the harness layer these tools drive
- [Surface Feature Matrix](../../surfaces/surface-feature-matrix/index.md) - the same treatment for editors and environments
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map these columns come from
- [Managing Many Concurrent LLM Agent Sessions](../../../managing-many-llm-agent-sessions/index.md) - the supervision problem the whole category answers
- [OpenChamber](../../surfaces/openchamber/index.md) - scheduled sessions, the non-interactive complement to parallel dispatch

## References

- https://github.com/smtg-ai/claude-squad - profiles, worktrees, packaging for the Claude Squad column
- https://github.com/google/ax - repository, primitives, license, and status for the AX column
- https://agentexecutor.io - the Task, Workspace, Gateway, and Model model for the AX column
- https://cmux.com/pricing - tiers, the 50-VM cloud cap, CodeRouter removal for the cmux column
- https://conductor.build/pricing/ - tiers, sandbox specs, local versus cloud privacy for the Conductor column
- https://github.com/stravu/crystal - deprecation notice and feature history for the Crystal column
- https://github.com/standardagents/dmux - supported agent list, hooks, local-only scope for the dmux column
- https://emdash.com/ - agent support, SSH model, downloads for the Emdash column
- https://github.com/BloopAI/vibe-kanban - sunset banner and feature list for the Vibe Kanban column
- https://github.com/gastownhall/gastown - architecture, runtimes, Refinery, Docker setup for the Gas Town column
- https://github.com/slopus/happy - repository, stars, license, and monorepo layout for the Happy Coder column
- https://paseo.sh/alternatives/happy-coder - the provider, worktree, and platform limits for the Happy Coder column
- https://news.ycombinator.com/item?id=44904039 - launch thread and donation-IAP context for the Happy Coder pricing cell
- https://maggieappleton.com/gastown - the field analysis grounding the Gas Town status and cost cells
- https://github.com/omnara-ai/omnara - control plane, license, and stars for the Omnara column
- https://www.vibekanban.com/blog/shutdown - shutdown date, service removal, refunds for the status row
- https://github.com/getpaseo/paseo - platforms, agent catalog, relay, and license for the Paseo column
- https://github.com/superset-sh/superset - worktree model, presets, ELv2 license, and funding for the Superset column
- https://github.com/max-sixty/worktrunk - commands, hooks, license, and release cadence for the Worktrunk column
- https://air.dev/ - supported agents, isolation options, and pricing FAQ for the JetBrains Air column
- https://air.dev/changelog - current version 262.834.41 and platform dates for the JetBrains Air status cell
- https://www.jetbrains.com/help/air/execution-environments.html - the worktree, Docker, and cloud isolation model for the JetBrains Air isolation cells
- https://www.jetbrains.com/help/air/cloud-tasks.html - the JetBrains-managed cloud environments for the JetBrains Air cloud cell
