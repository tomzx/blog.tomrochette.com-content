---
title: "Orchestration Feature Matrix"
created: 2026-08-24
updated: 2026-09-27
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, llm=deepseek-v4.1-flash, comparison, orchestration, git-worktrees, parallel-agents]
readability: 3
audience_notes: >
  Engineers shortlisting a parallel-agent orchestrator, dashboard or terminal multiplexer or board, who need the capability deltas at a glance.
  Assumes you know what a git worktree is and already run at least one CLI coding agent; each column links to a full note.
---

This matrix compares the thirty-one orchestration tools profiled in this section, the parallel-agent dashboards, worktree managers, control planes, mobile clients, a coordination protocol, a cluster-scale agent fleet orchestrator, JetBrains' standalone agent environment, two conversational multi-agent frameworks, a dormant role-play framework, hosted agent platforms, the one agent town, and the newer wave of workflow runners, a graph workspace, a sandbox library, a tmux harness, an issue-board platform, a Codex workflow layer, and a mission-control canvas, feature by feature, so the shortlisting step does not require reading thirty-one notes.

**Parallelism is already the free commodity in this category: the only things anyone pays for are review ergonomics and remote execution, and I expect more of these thirty-one to die or pivot before any of them becomes durable infrastructure.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [AutoGen](../autogen/index.md) | [AutoGPT](../autogpt/index.md) | [AX](../ax/index.md) | [Claude Squad](../claude-squad/index.md) | [cmux](../cmux/index.md) | [Conductor](../conductor/index.md) | [Crewplane](../crewplane/index.md) | [Crystal](../crystal/index.md) | [dmux](../dmux/index.md) | [Emdash](../emdash/index.md) | [Foremerge](../foremerge/index.md) | [Gas Town](../gastown/index.md) | [GraphCode](../graphcode/index.md) | [Happy Coder](../happy-coder/index.md) | [Helmor](../helmor/index.md) | [JetBrains Air](../jetbrains-air/index.md) | [Lanes](../lanes/index.md) | [LobeHub](../lobehub/index.md) | [LoopTroop](../looptroop/index.md) | [MetaGPT](../metagpt/index.md) | [Multica](../multica/index.md) | [oh-my-codex](../oh-my-codex/index.md) | [Omnara](../omnara/index.md) | [Open Swarm](../open-swarm/index.md) | [Orca](../orca/index.md) | [Paseo](../paseo/index.md) | [Sandcastle](../sandcastle/index.md) | [Superset](../superset/index.md) | [The Perfect Orchestrator](../the-perfect-orchestrator/index.md) | [Vibe Kanban](../vibe-kanban/index.md) | [Worktrunk](../worktrunk/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | conversational multi-agent framework | agent workflow platform | Kubernetes agent-fleet orchestrator | terminal TUI | native macOS terminal | native Mac app | Python CLI workflow runner | Electron app | terminal TUI | Electron app | coordination protocol above Git, CLI plus MCP server | tmux town, workspace manager | native macOS graph workspace, daemon plus CLI | native mobile and macOS client, wraps the agent CLI | Tauri desktop workbench | standalone agent environment, desktop app plus org web | native macOS workspace, CLI plus self-hostable MCP endpoint | agent hiring and scheduling platform | local GUI web app | SOP multi-agent software-company framework | self-hostable workspace plus daemon | Codex CLI workflow layer, npm package | Go control plane, web, CLI, API, mobile, Slack | Electron desktop app plus FastAPI backend | Electron agentic IDE, desktop plus mobile | daemon plus desktop, web, mobile clients | TypeScript library plus CLI | Electron agentic IDE | bash plus tmux harness, Claude Code plugin | web UI, Rust backend | CLI worktree manager |
| Platforms | Python, any OS | Docker self-host, hosted cloud, web builder | Kubernetes clusters; Linux or macOS CLI (Go) | macOS, Linux (tmux, no Windows) | macOS only | macOS only (local) | Python 3.13+, any OS | macOS first, Linux later | macOS, Linux (tmux) | macOS, Windows, Linux | macOS, Linux, Windows binaries; local, single machine | macOS, Linux, Windows, Docker | macOS 15+ Apple Silicon only | iOS, Android, macOS, web | macOS, Windows x64 (no Linux) | macOS, Windows, Linux desktop; org-only web | macOS Ventura+ (Apple Silicon, Intel); Link on macOS/Linux | desktop app, web, cloud | any OS with Node 24+; requires OpenCode | Python, any OS | web, server (Docker/Helm/binary), desktop (macOS/Windows/Linux), iOS | macOS/Linux primary; native Windows and Codex App unsupported default | web, iOS, Android, Slack; self-host or Omnara Cloud | macOS only (Windows/Linux planned) | macOS, Windows, Linux; iOS and Android companions | macOS, Windows, Linux, iOS, Android, web, Docker | any OS with Node plus Docker, Podman, or Vercel | macOS, Linux experimental | Linux, macOS (tmux 3.0+) | any OS with Node | macOS, Linux, Windows |
| Open source | ✓ MIT packages, repo root detected CC-BY-4.0 | ~ Polyform Shield for the platform, MIT for classic | ✓ Apache-2.0 | ✓ AGPL-3.0 | ~ GPL-3.0, open core | ✗ closed | ✓ Apache-2.0 | ✓ MIT | ✓ MIT | ✓ Apache-2.0 | ✓ Apache-2.0 | ✓ MIT | ~ FSL-1.1-MIT (source-available; app and daemon FSL, integration surfaces MIT) | ✓ MIT | ✓ Apache-2.0 | ✗ closed | ~ app source published, license undeclared; Link Apache-2.0 | ~ community license, Apache 2.0 plus conditions | ✓ MIT | ✓ MIT | ~ custom Multica License (Apache-2.0 plus hosted and commercial conditions, GitHub NOASSERTION) | ✓ MIT | ✓ Apache-2.0 | ✓ AGPL-3.0 (README badge says MIT) | ✓ MIT | ✓ Apache-2.0 | ✓ MIT | ~ Elastic License 2.0 | ✓ MIT | ✓ Apache-2.0 | ✓ MIT OR Apache-2.0 |
| Price model | free, open source | free self-host, hosted Pro $42.50/mo, Max $272/mo billed annually | free, open source | free, no tier | free, Pro $50/mo, Max $200/mo | free local, Pro $50/mo | free, open source | free (Nimbalyst sells teams) | free | free core, cloud contact-sales | free, open source | free, BYOK runtime | free, source-available | free, donations | free, open source | included with JetBrains AI Pro/Ultimate, BYOK supported | free (1 user), Pro $19/mo (10 seats), Enterprise custom; Compute per-second | free self-host, cloud $9.9-$39.9/mo billed yearly | free, open source | free, open source (the MGX hosted sibling is separate) | free to start; hosted cloud paid (no public price table) | free, open source | free self-host, cloud usage-priced | free, open source | free and open source; Enterprise custom | free, Hub hosted €15/seat/mo | free, open source | free local, Pro $15-20/user/mo | free, open source | free (subs terminated) | free |
| Per-task worktree isolation | ✗ in-memory agent conversations, no worktrees | ✗ block-based workflows, not repo tasks | ~ sandboxed tasks with pre-wired git workspaces, not worktrees | ✓ | ? | ✓ own branch | ~ optional Git-backed worktrees and snapshots; default edits the project root | ✓ | ✓ AI-named branch | ✓ | ~ assumes the worktrees you already run | ✓ worktree hooks | ~ per-loop worktree under a project | ✗ existing paths only | ✓ one worktree and branch per workspace | ✓ worktree, Docker, or cloud per task | ✓ one issue, branch, and worktree per task | ✗ chat and scheduled agent tasks, not repo tasks | ✓ isolated OpenCode worktree per bead, fresh worktree per retry | ✗ role conversations, no worktrees | ~ runtime is a machine you connect; per-issue worktree not a documented primitive | ✓ $team workers each get a dedicated git worktree by default | ? | ✓ each agent gets its own worktree and branch | ✓ every task in its own worktree and branch | ✓ | ✓ creates a host worktree and merges the branch back | ✓ own branch | ✗ workers share a workspace; ownership rules and lock-guarded commits instead | ✓ own branch | ✓ core purpose |
| Harnesses it can drive | ~ its own assistant agents, not external CLIs | ~ its own blocks and agents, not external CLIs | any agent container, bring-your-own runner image | any CLI via profiles | any CLI agent | 4 (Claude Code, Codex, Cursor, OpenCode) | any CLI (Claude Code, Codex, Gemini CLI, Copilot CLI, Kilo, Pi, DeepSeek, OpenCode) | 2 (Claude Code, Codex) | 11 CLIs | 25+ CLIs, auto-detected | any MCP client plus CLI and JSON API; setup auto-wires Claude Code, Codex, Cursor | 5 runtimes, Claude Code default | 5 (Claude Code, Copilot CLI, Codex, OpenCode, Pi) | 2 (Claude Code, Codex) | 5 (Claude Code, Codex, Cursor, OpenCode, Kimi Code) | 4 built-in (Claude Agent, Codex, Gemini CLI, Junie) + any ACP agent | any CLI via PTY; Claude Code and Codex first-class | ~ its own agents plus 10,000+ skills and MCP plugins | 1 (OpenCode) | ~ its own role agents, not external CLIs | 26 agent CLIs (Claude Code, Codex, Cursor, Copilot, Kimi, OpenCode, and more) | 1 primary (Codex CLI); mixed-provider teams codex, claude, gemini | ? agent underneath unspecified | ~ its own Claude Agent SDK agents | 27+ CLI agents (Claude Code, Codex, Cursor CLI, Gemini, Copilot, OpenCode, Pi, and more) | 4 native + ~36 via ACP | 6 agent providers (claude-code, codex, pi, cursor, opencode, copilot) | any CLI, 21 presets | 1 (Claude Code) | 10+ agents | any CLI via -x, one program name since v0.76 |
| Remote or SSH execution | ~ distributed actor runtime, self-hosted | ✓ cloud-native by design | ✓ cluster-native, ax ssh into sandboxes | ? | ~ SSH sessions | ? | ✗ local only | ? | ✗ local only | ✓ SSH-first | ✗ local, single machine | ~ Docker compose | ✓ remote repos over SSH | ✓ E2E-encrypted relay | ~ experimental Cloudflare-tunnel mobile companion, no SSH | ✓ JetBrains cloud, org web | ✗ local execution; Link self-hostable | ✓ cloud-native | ✗ local only | ✗ local runs | ✓ daemon runtimes on any connected machine | ✗ local only | ✓ machine pools | ✗ local only | ✓ SSH worktrees, self-hosted server, cloud VMs | ✓ encrypted relay, self-host | ~ Vercel isolated sandboxes, no SSH | ~ remote workspaces beta | ✗ local tmux session | ~ Docker self-host | ✗ local git |
| Built-in review tooling | ✗ no review surface | ~ runs dashboard and logs, no code review | ~ watch, logs, and ssh, no review surface | ~ diff preview tab | ? | ✓ diffs, checks, PR, review | ~ review loops and findings artifacts, no diff surface | ~ diff viewer, rebase, squash | ~ merge and PR menu | ✓ diffs, PRs, CI checks | ~ advisory conflict findings, verification-gated ChangeSets, no diff surface | ✓ Refinery merge queue | ~ attach to any live terminal; no diff or PR review surface | ~ diffs and terminals beside conversations | ✓ diffs, Monaco editor, one-click PR/MR, merge, fix CI, stacked PRs | ✓ language-aware diffs, Agent Review (agent reviews agent) | ✓ diffs, Monaco editor, git client, SQLite browser, GitHub/Linear write-back | ✗ none | ~ per-bead diff review and human approval gate, no PR checks | ✗ none, code lands in the repo | ✓ review gates, execution-log replay, issue comments and diffs | ~ code-review and ultraqa skills, merge tracking via integration-report.md | ~ approvals, questions, events, artifacts | ~ diff viewer for uncommitted changes, no PR flow | ✓ diff viewer, inline annotations back to the agent, GitHub/Linear review | ~ agent output and diffs | ~ logs and per-iteration results, no review UI | ✓ diffs, browser previews | ~ adversarial cross-verification of findings, no diff or PR surface | ✓ diffs, comments, PR | ~ status table and merge pipeline |
| Cloud execution option | ✗ none first-party | ✓ the hosted platform is the product | ✓ is the cloud execution layer | ✗ no hosting | ✓ Pro, up to 50 cloud VMs | ✓ Vercel sandboxes | ✗ none | ? | ✗ | ~ contact-sales | ✗ local only | ✗ self-host, Wasteland federation | ~ your own SSH hosts, no vendor cloud | ✗ your machine only | ✗ local-first | ✓ JetBrains-managed cloud environments | ✗ local-first; Compute is GPU rental, not agent hosting | ✓ LobeHub Cloud | ✗ local execution (Docker possible) | ~ the MGX hosted sibling | ✓ Multica Cloud or self-host | ✗ none | ✓ Omnara Cloud, or self-host | ✗ local only | ✓ self-hosted servers or your own cloud VMs | ~ self-host anywhere, no vendor cloud | ✓ Vercel Firecracker sandboxes | ~ remote workspaces beta | ✗ none (run on your own VPS) | ✗ services removed | ✗ |
| Current status | maintenance mode, successor Microsoft Agent Framework at 13.8k stars | active, platform beta v0.8.1, 187.6k stars | active, Google team, v0.3.1, pre-stable | active, slow burn | active, fast | active, $22M raised | active, early, 41 stars as of 2026-09-27, v0.3.5 | deprecated Feb 2026 | active | active, YC W26 | active, 507 stars, pre-1.0, v0.5.0 | shut down Sept 2026, repo kept as death record | active, v0.1.76-beta2 (2026-09-27), 129 stars as of 2026-09-27, created 2026-07-26 | active, 23.9k stars, community team | active but cooling, v0.46.0 (2026-07-24), last commit 2026-08-22, 1.3k stars | active, public preview, v262.834.41 | active, v0.49 (2026-09-08), 271 stars on lanes-sh/app as of 2026-09-27 | active, daily canary releases, 82.8k stars | active, early alpha, v0.5.9 (2026-08-26), 154 stars as of 2026-09-27 | quiet since v0.8.2 (2025-03), org energy moved to OpenManus | active, v0.5.3 (2026-09-24), 51.5k stars as of 2026-09-27, star count caveated | active, v0.21.6 (2026-09-21), 33.4k stars as of 2026-09-27 | active, YC S25, 2,871 stars | active, experimental release line, v1.8.0-exp.2 (2026-09-23), 820 stars as of 2026-09-27 | active, v1.4.215 (2026-09-27), 79.4k stars as of 2026-09-27 | active, v0.9.2, solo maintainer | appears dormant, v0.12.0 (2026-06-29), no push since, 8.2k stars as of 2026-09-27 | active, YC P26, $11M raised | quiet, v0.2.0 (2026-06-06), last commit 2026-06-30, 1 star as of 2026-09-27 | orphaned, community commits resumed 2026-09-16, v0.1.45 prerelease on GitHub, npm still 0.1.44 | active, pre-1.0 fast |

## Reading the matrix

**The platform rows tell you who these tools are for: Mac-first GUI shops and unix terminal people, with Emdash the only GUI covering all three desktop OSes and the tmux pair unable to follow anyone to Windows.**
cmux and Conductor are macOS only, and Crystal was macOS first with Linux later.
Vibe Kanban's web UI goes anywhere Node goes, which is the one structural advantage of the board design.

**Worktree isolation is the entry ticket, not the differentiator: every session-oriented tool here except cmux, Foremerge, and The Perfect Orchestrator gives each task its own worktree and branch, so the real spread is harness breadth, from LoopTroop's one and Crystal's two to Emdash's 25+.**
cmux's "?" is structural rather than a gap: it is a terminal built for attention routing, not a session manager, and its note records no worktree feature.
Foremerge's tilde is the opposite of a gap: it assumes the worktrees you already run and coordinates plans across them, the one column whose unit of work is the intent rather than the task.
The wrapping pattern dominates (Emdash auto-detects installed CLIs, Claude Squad launches anything through profiles, dmux lists eleven), which means new harness features arrive without waiting for the orchestrator to reimplement them.

**Where your code lives is the quiet differentiator, and Emdash is alone in treating it as a design decision with SSH-first execution and credentials in the OS keychain.**
Cloud execution exists only where a subscription or usage bill is attached, cmux Pro, Conductor Cloud, Omnara Cloud, and JetBrains-managed cloud tasks; dmux is explicitly local-only, Claude Squad ships no hosting at all, and Vibe Kanban's remote services were removed thirty days after its shutdown announcement.

**The status row is the most instructive one in the matrix: of thirty-one tools, one is deprecated, one lost its vendor, one is a cluster-scale platform entrant, one new column attacks the failure worktrees cannot see, and the counterexamples run on venture rounds and a very loud founder.**
Crystal was deprecated in February 2026 in favor of Nimbalyst, the clearest signal yet that a pure worktree-session manager can be a feature rather than a product.
Bloop shut down in April 2026 and Vibe Kanban is orphaned, local workspaces intact, ten commits on the default branch since the shutdown (the first a 2026-09-15 version bump by a former Bloop maintainer, nine more with substantive fixes through 2026-09-19), a v0.1.45 prerelease published on GitHub on 2026-09-19 with npm still serving 0.1.44 as latest, and nobody paid to fix bugs.
Conductor staying a pure session manager and raising money is what keeps the feature-versus-product question contested instead of settled.
**The three 2026 columns sharpen the funding split: Superset raised $11M, Paseo is a solo maintainer with a planned business, and Worktrunk is a single author with no company at all, which is the whole sustainability spectrum in one row.**
**Omnara is the tenth column and the only one that wants to own execution and state:** agents become YAML configs in your repo, machine pools separate where code runs from who can invoke it, and supervision reaches you from a dashboard, phone, CLI, REST API, or Slack, the open-source counterpoint to Claude Managed Agents.
**Happy Coder is the purest thin client in the table:** two harnesses, no worktrees, no hosting, yet 23.8k stars, second only to cmux among maintained tools, because phone access to the sessions you already run is what people actually install.
**JetBrains Air is the vendor entry, and it is the only column whose price model is a bundle:** no standalone fee, four agent families unlocked by a JetBrains AI Pro or Ultimate subscription, with the deepest isolation menu in the table (worktree, Docker, or cloud per task) and org governance behind it, which makes it the strongest evidence yet that this layer is a feature incumbents will attach to existing subscriptions.
**AX is the scale outlier at the front of the table:** Google's Kubernetes-based fleet orchestrator treats agents as a datacenter workload class with sandboxing, network fencing, and checkpoint-resume, which makes every other column here look like what it is, a desktop tool.
**Foremerge is the newest column and the only one that coordinates plans instead of hosting sessions:** agents publish intents with semantic scopes before they edit, and a deterministic detector flags destructive-versus-additive collisions that git merges cleanly, which names the residue every worktree column here leaves behind.
**The four framework columns are this category's museum wing and its adjacent business park:** AutoGen is in maintenance mode and MetaGPT dormant while AutoGPT and LobeHub run active hosted platforms, which is why I weight the parallel-agent columns as where the daily engineering work is.

**The eleven new columns split into three families, and the split says more than any single feature cell.**
Four are process engines that own a workflow rather than a session: Crewplane sequences a Markdown DAG across CLIs and keeps the run record on disk, Sandcastle exposes the same instinct as a TypeScript library over Docker, Podman, or Vercel sandboxes, LoopTroop wraps OpenCode in council planning and fresh-context recovery, and oh-my-codex adds skills, memory, and worktree teams to Codex CLI.
Three are visual surfaces: GraphCode arranges live sessions into a graph whose hand-off, message, and spawn edges fire on shell predicates, Helmor is a local-first workbench that carries a task through review, test, merge, and one-click PR, and Open Swarm is a mission-control canvas with unified tool approvals and per-session cost tracking.
Four are platforms or boards: Lanes puts parallel PTY sessions on a macOS issue board and pairs it with a self-hostable agent-access endpoint, Orca is the MIT, cross-platform ADE with a mobile companion and 27+ agents, Multica assigns issues to agents as teammates on a self-hostable board, and The Perfect Orchestrator is a one-star tmux harness whose adversarial verification of workers is the most interesting idea of the batch.

**The new entrants sharpen the category's two fault lines: openness and maintenance.**
Orca, Helmor, Lanes, and Open Swarm stay free or freemium on venture or solo funding, while Multica's 51.5k stars and custom, non-OSI license are exactly the caveated popularity signal this matrix exists to flag.
Sandcastle and The Perfect Orchestrator last committed in June 2026, GraphCode is two months old with one maintainer, and LoopTroop and Crewplane are early with tiny star counts, so the feature-versus-product question the earlier columns raised now has a shorter runway.
**The one new capability claim worth taking seriously is adversarial verification:** The Perfect Orchestrator will not count a finding until a different worker fails to refute it, which is a sharper answer to worker overconfidence than any review surface in the table.

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
- Want your agent process versioned as Markdown with resumable, inspectable runs across several CLIs: Crewplane.
- Want to script sandboxed agents from TypeScript and own the pipeline: Sandcastle, accepting a repository quiet since June 2026.
- Want one lead to brief and adversarially verify workers over tmux, no daemons: The Perfect Orchestrator, a one-star template rather than a maintained tool.
- On Apple Silicon and want connected, unattended loops you can still attach to: GraphCode, accepting the FSL license and 0.1.x beta.
- Want an open, local-first workbench that finishes the loop through review, test, and one-click PR: Helmor, on macOS or Windows.
- Want parallel PTY sessions organized as issues on a macOS board, with a self-hosted agent-access layer: Lanes.
- Want the broadest, most open ADE, across all three desktop OSes plus phone and remote: Orca.
- Want to assign issues to agents as teammates on a board you can self-host: Multica, accepting the custom license and the star-count caveat.
- Want one local canvas to launch, approve, and cost-track several Claude agents: Open Swarm.
- Want planning-first, high-correctness runs over OpenCode with human approval at every merge: LoopTroop.
- Want Codex CLI to behave like a team with worktrees, memory, and skills: oh-my-codex.
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
- 2026-09-27 - Extended from sixteen to twenty columns with AutoGen, AutoGPT, LobeHub, and MetaGPT, the multi-agent frameworks and hosted platforms, and updated the prose counts and the reading section to match.
- 2026-09-27 - Extended from twenty to thirty-one columns with Crewplane, GraphCode, Helmor, Lanes, LoopTroop, Multica, oh-my-codex, Open Swarm, Orca, Sandcastle, and The Perfect Orchestrator (a batch of workflow runners, a graph workspace, a sandbox library, a tmux harness, an issue-board platform, a Codex workflow layer, and a mission-control canvas), re-sorted all columns, and added the three-family reading section and the new choosing entries.

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
- https://github.com/stablyai/orca - repository, worktrees, 27-agent list, MIT license, and stars for the Orca column
- https://www.onorca.dev/docs - worktrees, review, remote, and the "not a model" scope for the Orca cells
- https://github.com/mattpocock/sandcastle - sandbox providers, branch strategy, hooks, and license for the Sandcastle column
- https://registry.npmjs.org/@ai-hero%2Fsandcastle - Sandcastle package version and license
- https://lanes.sh/pricing - tiers, seats, and Compute billing for the Lanes price cell
- https://github.com/lanes-sh/app - board, sessions, worktrees, and the undeclared license for the Lanes column
- https://github.com/crewplaneai/crewplane - Markdown workflows, resumable runs, and license for the Crewplane column
- https://helmor.ai/ - local-first workbench, agents, and ship actions for the Helmor column
- https://github.com/dohooo/helmor - worktrees, one-click PR and merge, CLI and MCP, and the cooling commit cadence for Helmor
- https://github.com/openswarm-ai/openswarm - canvas, approvals, worktrees, and the AGPL-3.0 LICENSE for the Open Swarm column
- https://www.looptroop.ovh/docs/ - council planning, beads, Ralph loops, and alpha status for the LoopTroop column
- https://graphcode.app/ - loop types, graph edges, and the FSL license for the GraphCode column
- https://github.com/daman8271/the-perfect-orchestrator - lead-and-worker harness, adversarial verification, and license for the column
- https://github.com/multica-ai/multica - issue assignment, runtimes, license metadata, and stars for the Multica column
- https://www.promptquorum.com/power-local-llm/multica-review - the star-count caveat and the custom-license analysis for the Multica cells
- https://github.com/Yeachan-Heo/oh-my-codex - skills, worktree teams, MCP servers, and license for the oh-my-codex column
