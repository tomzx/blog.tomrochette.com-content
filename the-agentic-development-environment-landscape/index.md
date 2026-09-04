---

title: "The Agentic Development Environment Landscape"
created: 2026-07-04
type: post
status: draft
tags: [ai-agents, coding-agents, ade, landscape, opencode, claude-code, jetbrains, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader has run at least one terminal coding agent (Claude Code, Codex, OpenCode) and understands why steering several at once is hard.
agent_sessions:
  - ses_0d449baf5ffeVU2igHn5OuXedr
---

The terminal coding agent answered the question of whether an AI can edit a real repository.
The next problem is harder: how do you run several of them, watch what they are doing, and keep them from colliding on the same files.
In the space of roughly a year, **a new product category has condensed around exactly that problem**, picked up a name (the Agentic Development Environment, or ADE), earned its own [GitHub topic](https://github.com/topics/ade), and produced a leaderboard anyone evaluating tools should know about.

## What an ADE is, and what it is not

An Agentic Development Environment is a layer that sits above swappable coding agents and below your editor.
**The job is not to be a better model; the job is to be a control room.**
A typical ADE runs several CLI agents (Claude Code, Codex, OpenCode, Gemini CLI, and others) in parallel, isolates each one in its own git worktree or container, gives you a single surface to watch and steer them, and then helps you review and merge the results.
It is defined by what it leaves out: it does not replace your editor, and it does not lock you to one model.

The category is easiest to see by contrast.
The agents themselves (Claude Code, Codex, OpenCode, Gemini CLI, Junie) are the things doing the work, and they live in your terminal.
AI code editors like Cursor and Windsurf bundle their own agent into a fork of VS Code, so the model and the shell are one product.
Terminal UIs like Crystal and Crush give the OpenCode lineage a polished TUI but stay single-agent.
An ADE is the fourth thing: a vendor-neutral shell that treats the agents as plug-replaceable and the parallelism as the core feature.

## Why the category exists now

Three things had to be true at once for the ADE to make sense, and they all became true in the same window.
First, there are now several frontier coding agents worth running, and each is better at different things, so a serious session often wants more than one.
Second, git worktrees made it cheap to give each agent its own isolated checkout, which removed the excuse that parallel agents would step on each other.
Third, and most painfully, the supervision bottleneck moved onto the human: once you can spawn a dozen agents, your working memory and decision budget become the limit, not the model.

That last point is the one that turns a convenience into a category.
Running many agents in parallel is only useful if a person can stay effective while doing it, and that requires externalized state, dashboards, escalation thresholds, and isolation, none of which a bare terminal gives you.
**The ADE is the productized answer to the supervision problem: it is the dashboard, the isolation manager, and the review surface rolled into one.**

A second catalyst arrived in late 2025, when JetBrains and Zed published the [Agent Client Protocol (ACP)](https://blog.jetbrains.com/ai/2025/10/jetbrains-zed-open-interoperability-for-ai-coding-agents-in-your-ide/) and opened it as an interoperability standard for coding agents inside IDEs.
A shared protocol makes the "plug-replaceable agents" premise credibly vendor-neutral instead of a marketing claim, and it gave new entrants a contract to target.

## The leaderboard

The category is unusually concentrated for its age.
As of mid-2026 the top of the field is five products, and the gap between the leader and the sixth is large.

[Superset](https://github.com/superset-sh/superset) is the largest open-source entry by community, billing itself plainly as the code editor for the AI agents era and able to run a fleet of Claude Code, Codex, and similar CLIs on your own machine.
It is an Electron desktop app with a CLI companion, and its positioning is the simplest of the group: bring your own agents, run them in parallel, review the results.

[JetBrains Air](https://air.dev) is the incumbent's answer, and the one most likely to reshape the field by distribution alone.
JetBrains killed Fleet in late 2025 and replaced it with Air, an agentic development environment [launched as a public preview](https://blog.jetbrains.com/air/2026/03/air-launches-as-public-preview-a-new-wave-of-dev-tooling-built-on-26-years-of-experience/) in March 2026 on macOS, with Windows following in June and Linux still pending.
Air is a standalone desktop application, not an IntelliJ plugin, and it supports Codex, Claude Agent, Gemini CLI, and Junie out of the box.
Its distinguishing bet is code intelligence: because it inherits 26 years of IDE work, you can scope a task by referencing a specific class, method, or commit, and review changes against the whole codebase rather than a bare diff.
It is also closed-source and tied to a JetBrains AI subscription or bring-your-own-key, which is the cleanest point of contrast with the open-source entrants.
**Notably, Air does not list OpenCode among its supported agents, which leaves a seam for OpenCode-native tools.**

[Orca](https://github.com/stablyai/orca) is the open-source ADE with the most feature surface and the clearest mobile story.
It runs any CLI agent on macOS, Windows, and Linux, ships an iOS and Android companion app for monitoring agents from your phone, and adds the kind of polish that comes from daily shipping: Ghostty-class terminals, a Design Mode that ships a clicked DOM element straight into an agent prompt, native GitHub and Linear boards, and SSH worktrees for running agents on a remote box.
It is MIT-licensed and YC-backed, and it is the reference implementation most people picture when they hear "ADE."

[Paseo](https://github.com/getpaseo/paseo) takes the privacy-first position to its logical end.
It is AGPL-3.0, ships desktop, mobile, web, and CLI clients against a self-hosted daemon, supports Claude Code, Codex, Copilot, OpenCode, and Pi through one interface, and collects no telemetry.
It also ships skills that turn the orchestrator into an agent capability: handoffs between agents, loops against acceptance criteria, and committees of contrasting agents for second opinions.
For a buyer whose first question is "what is this sending home," Paseo is the answer.

[Emdash](https://github.com/generalaction/emdash) is the open-source ADE with the clearest enterprise intent.
It is a YC W26 company, runs multiple agents in parallel with any provider, and leans into integrations that solo-hacker tools tend to skip: Jira, Linear, and containerization as first-class concerns.
It rounds out a top five that already spans open source (Superset, Orca, Paseo, Emdash) and commercial (Air), which is a healthy mix for such a young category.

## The mid-tier and the long tail

**Below the leaders there is a busy middle, and it is where the next leader is most likely to come from.**
Agent orchestrators built as CLIs and TUIs make up a large share, because the cheapest way to ship an ADE is to not build a GUI at all.
[agent-orchestrator](https://github.com/AgentWrapper/agent-orchestrator) is a Go-based, tmux-driven orchestrator that plans tasks, spawns agents, and autonomously handles CI fixes and merge conflicts, and it has the reach of a leader without the surface area of one.
[Kandev](https://github.com/kdlbs/kandev) frames the same idea as an AI Kanban plus development environment, multi-provider and self-hostable with no telemetry, a framing that maps cleanly onto a team workflow.
[Pane](https://github.com/dcouple/Pane), [agent-os](https://github.com/saadnvd1/agent-os), [lanes](https://github.com/lanes-sh/app), [Frame](https://github.com/kaanozhan/Frame), [genie](https://github.com/automagik-dev/genie), and workstreams each take a slightly different cut of the same problem: terminal-first, mobile-first, spec-driven, or PR-out-the-door.

The long tail is mostly Tauri and Rust experiments (Termote, AKA, codemux, BLXCode), which trade on being lightweight and locally owned, and a handful of IntelliJ-style control surfaces like Athena.
None of these is a leader today, but the category is young enough that any one of them could break out if it found the right wedge, and the two curated lists, [awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators) and awesome-multi-agent-orchestrators, are the best place to watch for movement.

## What actually differentiates an ADE

Once you strip the marketing, the differences collapse onto a small number of axes, and a buyer can score any tool against them in an afternoon.

The first axis is agent-agnostic versus agent-native.
Most leaders are agnostic and treat OpenCode, Claude Code, and Codex as interchangeable inputs, which is the right default if you do not want to bet on a model vendor.
OpenChamber takes the opposite bet: it is the OpenCode-native control room, trading breadth for the deepest possible integration with one agent's server, SDK, and skills catalog.
Both positions are defensible; the mistake is pretending to be both.

The second axis is surface coverage.
Desktop is table stakes; the real arguments are about mobile, web, and remote.
Orca, Paseo, and OpenChamber all treat "start at your desk, check in from your phone" as a first-class story, while Air is desktop-only as of mid-2026 and has said cloud execution is coming.
For anyone who wants to steer agents from outside the office, the mobile and tunnel story is not a nice-to-have; it is the feature.

The third axis is license and pricing, and it splits the field cleanly.
The open-source tools (Superset, Orca, Emdash; Paseo under AGPL; OpenChamber under MIT) cost nothing and run against your own provider keys.
Air is closed-source and either bundles into a JetBrains AI subscription or takes your own API keys, which is fine for an enterprise buyer and a poor fit for a self-hosting one.
**The license is also a proxy for longevity: in a category this young, an MIT or AGPL codebase is the one that survives a company shutting down.**

The fourth axis is the isolation primitive, and it matters more than people credit.
Worktrees are fast and cheap but assume a local repo; containers sandbox the agent but add setup; cloud execution removes the local machine entirely but adds latency and trust questions.
Every ADE picks one or two of these as primary, and the choice constrains everything else about how the tool feels.

The fifth axis is protocol.
ACP is the only credible interop standard, and a tool built on it can claim vendor-neutrality with a straight face; a tool that talks to each agent through its own SDK can be equally capable but has to maintain N integrations and inherits N sets of breakage.
Whether OpenCode gains an ACP adapter is one of the more consequential questions for the OpenCode-native niche.

The sixth axis is code intelligence depth, and it is where Air's IDE lineage shows.
Symbol-aware task scoping (reference a class, not a file path) and whole-codebase review are real productivity gains, and most of the open-source ADEs offer only diff review today.
This is the dimension most likely to be copied next.

## Where OpenChamber sits

**OpenChamber is best understood as the OpenCode-native member of this set, not as an also-ran agnostic ADE.**
It is MIT-licensed, runs across desktop, web, PWA, VS Code, and a mobile story built on tunnels and SSH, and its deepest feature work is exactly where you would expect an OpenCode-native tool to be deepest: branchable chat timelines, worktree sessions, GitHub-native flows, an embedded OpenCode server, and a skills catalog.
Its real weakness is the mirror image of its strength: it does not have an IDE-grade code intelligence layer, so it reviews diffs rather than symbol graphs, and it is one-agent-deep rather than agent-agnostic.

That is a reasonable trade, and probably the right one for a project that wants to be the best control room for one agent rather than an adequate control room for all of them.
The risk is that ACP makes agent-neutrality cheap enough that "agnostic" stops being a differentiator, in which case the agent-native tools have to win on integration depth alone.

## What to watch

Three things will move this category over the next year.
The first is ACP adoption: if OpenCode ships an ACP adapter, the line between agent-native and agent-agnostic blurs fast, and the agnostic tools gain OpenCode support for free.
The second is Air on Linux and mobile: JetBrains closing those gaps removes the surface-coverage argument that the open-source tools currently win on.
The third is whether the mid-tier consolidates or whether one of Kandev, Pane, agent-os, or agent-orchestrator breaks into the top flight, because the category is small enough that a single breakout reshapes the leaderboard.

The safer prediction is the structural one.
The ADE is not a passing fashion; it is the productized answer to a real bottleneck, and once a developer has run five agents in parallel and felt the supervision cost, the control-room tool stops being optional.
**The open question is only which combination of license, surface, and protocol wins, and the answer to that is not yet decided.**

## See also

- [Managing Many Concurrent LLM Agent Sessions](../managing-many-llm-agent-sessions/index.md) - the human-supervision bottleneck that makes ADEs necessary
- [Scaling the LLM Agent Company](../scaling-the-llm-agent-company/index.md) - orchestration as the replacement for human management
- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) - how team structure shifts when agents are first-class workers
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - the review surface ADEs have to rebuild
- [The Codebase Gardener](../the-codebase-gardener/index.md) - the human role when agents do most of the writing

## References

- [stablyai/orca](https://github.com/stablyai/orca) - open-source ADE; any CLI agent, desktop and mobile, the feature reference
- [getpaseo/paseo](https://github.com/getpaseo/paseo) - AGPL self-hosted ADE; multi-provider, zero telemetry
- [superset-sh/superset](https://github.com/superset-sh/superset) - largest open-source ADE by community
- [JetBrains Air](https://air.dev) - the incumbent's commercial ADE
- [JetBrains, "Air Launches as Public Preview"](https://blog.jetbrains.com/air/2026/03/air-launches-as-public-preview-a-new-wave-of-dev-tooling-built-on-26-years-of-experience/) - Air's positioning, supported agents, and roadmap
- [JetBrains + Zed, Agent Client Protocol](https://blog.jetbrains.com/ai/2025/10/jetbrains-zed-open-interoperability-for-ai-coding-agents-in-your-ide/) - the interop standard that makes vendor-neutral ADEs credible
- [generalaction/emdash](https://github.com/generalaction/emdash) - open-source ADE, YC W26, enterprise-integration focus
- [AgentWrapper/agent-orchestrator](https://github.com/AgentWrapper/agent-orchestrator) - tmux-driven CLI orchestrator with autonomous CI and merge handling
- [kdlbs/kandev](https://github.com/kdlbs/kandev) - AI Kanban plus development environment, self-hostable, no telemetry
- [dcouple/Pane](https://github.com/dcouple/Pane) - terminal-first agent manager with remote phone access
- [saadnvd1/agent-os](https://github.com/saadnvd1/agent-os) - mobile-first self-hosted web UI for coding sessions
- [kaanozhan/Frame](https://github.com/kaanozhan/Frame) - spec-driven ADE
- [automagik-dev/genie](https://github.com/automagik-dev/genie) - CLI agent that dispatches parallel worktrees and reviews
- [lanes-sh/app](https://github.com/lanes-sh/app) - mission control for parallel agents
- [andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators) - curated list for tracking the long tail
- [GitHub topic: ade](https://github.com/topics/ade) - the topic page that maps the category
- [GitHub topic: parallel-agents](https://github.com/topics/parallel-agents) - the broader orchestration topic
