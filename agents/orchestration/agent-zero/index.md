---
title: Agent Zero
created: 2026-11-24
updated: 2026-11-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.4, orchestration, multi-agent, autonomous-agents, sandboxing, security]
readability: 3
audience_notes: >
  Engineers comparing open-source multi-agent and autonomous-agent frameworks who already run model APIs
  or a local model server and understand what a Docker container does and does not isolate. Assumes you
  can read a CVE title and know what an approval prompt is for.
---

Agent Zero is an MIT-licensed, self-hosted general-purpose agent from Jan Tomášek's Agent Zero, s.r.o. that works inside its own Linux sandbox over a terminal, a browser, and desktop apps, and delegates by spawning subordinate agents that can spawn their own.

**It is the framework tier's run-time delegation entry: where CrewAI and MetaGPT script roles into a workflow, Agent Zero's agent decides while running which subtasks to hand to fresh copies of itself, and the price of that freedom is an agent that acts without an approval step and carries a third-party-reported security record.**

## What it is

You run it as one Docker container on your machine or a server, reached through a Web UI, with an A0 Launcher desktop app for Windows, macOS, and Linux, an `a0` CLI connector that extends it onto files, commands, and a browser on your own computer, and a Telegram integration.
The agent has its own Linux workspace with a terminal, a built-in browser with an annotate mode, an XFCE desktop with LibreOffice, and Time Travel snapshots of the workspace that it can roll back.
Its multi-agent model is delegation by spawning: the agent hands parts of a task to other agents, each with its own instructions and conversation, and the Linux Foundation's research report describes the design as agents summoning sub-agents recursively, each acting as a quasi-atomic primitive.
Agent Profiles give a chat a repeatable role (developer, researcher, reviewer, writer), and the repository ships bundled profiles for a developer, a hacker, and a researcher.
Projects isolate workspaces, instructions, memory, secrets, knowledge, and model presets, skills load on demand, and LiteLLM routes any provider, a ChatGPT account, or a local model.
Outside tools and agents come in through MCP, a Plugin Hub of community plugins, and A2A, which the architecture page describes as communication for multi-agent orchestration.
The stack is Python 3.12 or later with Flask, Alpine.js, LiteLLM, and Socket.IO, and the license file is MIT text headed with the company's name, which is why GitHub reports NOASSERTION.

## Status

Active: v2.16 on 2026-11-17 (A0Cleaner weekly cleanup, scheduled-task catch-up after downtime, Time Travel snapshot expiry on by default, OAuth proxy and A2A credential hardening) after v2.15 (2026-11-01, bundled tools promoted to plugins and per-action tool permissions), v2.14 (2026-10-13), and v2.13 (2026-09-23), the eighth release since v2.9 on 2026-08-12, with the default branch pushed 2026-11-23 (GitHub API, as of 2026-11-24).
The repository was created 2024-06-10 as `frdel/agent-zero` and stands at 19,966 stars with 3,901 forks and 187 open issues as of 2026-11-24; the old path still resolves to it.
Two accounts carry the work, at 1,395 and 1,051 commits against 139 for the third (GitHub API, as of 2026-11-24).
**Almost none of that adoption shows up in discussion: Hacker News carries five stories about it since 2024, every one between 1 and 3 points with no comments.**
The independent coverage that exists is critical: a Linux Foundation Research profile, a 2025 security write-up, a 2026 user report of credentials in logs, and a third-party review that grades it D.
A third major version that moves agent-run code into disposable gVisor sandboxes was announced as a sneak peek on 2026-08-17, not as a release.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=agent0ai/agent-zero&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=agent0ai/agent-zero&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=agent0ai/agent-zero&type=date&legend=top-left" />
</picture>

## Strengths

- **Delegation is decided by the agent, not scripted by you**, so one prompt can fan a task out to sub-agents that each hold their own context and instructions.
- The agent gets a whole Linux machine and writes and runs its own code, which is why the project's own use cases run from office documents to penetration testing.
- Almost nothing is hidden: prompts are Markdown files, tools are plugins, and a second model can audit tool calls through the Infection Check plugin.
- Time Travel snapshots give the workspace an undo that Git does not cover for files an agent creates and edits on the fly.

## Cautions

- **It acts without asking**: shell commands, file changes, browser and desktop actions, and scheduled tasks run with no approval step, Tool Access defaults to allow, and the Infection Check audit ships disabled (third-party review, evidence checked 2026-11-04).
- The security record is long and third-party-reported: a keyword search of the National Vulnerability Database returns ten CVE records for Agent Zero since April 2025 (path traversal, server-side request forgery, stored cross-site scripting, insecure permissions), all assigned by VulDB, MITRE, or VulnCheck, and the same review found no vendor advisory for them.
- A 2025-06-27 write-up found the Web UI had no login by default and a cross-site request forgery path that uploaded files into the container as root; the README's Docker command now binds to localhost, and the install guide says never to expose the instance without authentication.
- A user reported in issue #1474 (opened 2026-04-08, closed 2026-07-08) that clear-text passwords reached the logs and persisted chat histories on v1.7.
- The README's own safety model says to keep it in Docker and never mount your whole home directory, and the A0 CLI connector is a deliberate bridge onto your machine, read-only or read-write.
- The same review records an update check, on by default, that posts the version and a hashed install id to the project's API, with an off switch.
- A token, A0T on Base, sponsors the project and carries its governance, and access to Venice.ai models through the project's API proxy is unlocked by staking it, where the Linux Foundation profile had recorded no commercial plans.
- Minor releases carry breaking changes (v2.15 promoted bundled tools to plugins), and two accounts write nearly all the code.

## Pricing

The software is free under MIT, and you bring your own model access: provider keys, a ChatGPT account, or a local model server.
There is no paid tier and no vendor compute cloud.
The project's LLM API proxy, which serves Venice.ai models, is unlocked by staking A0T tokens rather than by a subscription (token and API pages, as of 2026-11-24).

## Compared to

**[AutoGPT](../autogpt/index.md)** is the precedent that admitted autonomous general agents to this tier; AutoGPT rebuilt itself as a block-based workflow platform with a hosted tier, where Agent Zero stayed a single self-hosted agent that writes and runs code in its own Linux machine.
**[Hive](../hive/index.md)** shares the agents-spawn-agents design; Hive's Queen clones workers around one persistent ledger for business processes, while Agent Zero's sub-agents are task-scoped copies that report back.
**[OpenClaw](../../assistant-runtimes/openclaw/index.md)** is the personal-assistant runtime it resembles from the outside (self-hosted, Telegram, memory); OpenClaw leads with its Gateway and messaging channels, Agent Zero with its sandboxed Linux workspace and sub-agent delegation.
Choose Agent Zero for a general-purpose agent you extend by editing prompts and spawning sub-agents, AutoGPT for a builder and marketplace, and Hive for a persistent worker colony.

## Bottom line

Recommended for engineers who want a general-purpose, prompt-editable agent with its own computer, will run it isolated with the audit plugin switched on, and accept that its adoption is undiscussed and its security record is third-party-reported.
Not for unattended use on anything you care about, for exposure to the internet, or for anyone who needs an approval gate before an agent runs a command.

## Changes

- 2026-11-24 - Created, resolving the candidate the assistant-runtimes scan flagged as never resolved in any category, admitted on the AutoGPT autonomous-agent precedent and above the 2026-10-28 below-tier line.

## See also

- [AutoGPT](../autogpt/index.md) - the autonomous-agent precedent in this tier, since rebuilt as a workflow platform
- [Hive](../hive/index.md) - the other runtime whose agents spawn agents, around a persistent ledger instead of task-scoped copies
- [ChatDev](../chatdev/index.md) - the other high-star framework with a thin discussion record, the scale-and-activity exception this tier set
- [OpenClaw](../../assistant-runtimes/openclaw/index.md) - the personal-assistant runtime with the same self-hosted, channel-driven outline
- [OpenWorker](../../assistant-runtimes/openworker/index.md) - the governed desktop coworker, the approvals-and-sandboxing counterpoint to an agent that acts without asking
- [Cloudroom](../cloudroom/index.md) - the cloud-agent app whose adapters run Agent Zero's `a0` bridge in a cloud thread

## References

- https://api.github.com/repos/agent0ai/agent-zero - repository metadata: created 2024-06-10, pushed 2026-11-23, 19,966 stars, 3,901 forks, 187 open issues, license detected NOASSERTION, as of 2026-11-24.
- https://raw.githubusercontent.com/agent0ai/agent-zero/main/README.md - the Linux-workspace pitch, the install paths, the Multi-Agent Cooperation section, Projects, the A0 CLI connector, the safety model, and the MIT statement.
- https://raw.githubusercontent.com/agent0ai/agent-zero/main/LICENSE - the MIT text headed "Agent Zero, s.r.o.", which GitHub does not classify.
- https://raw.githubusercontent.com/agent0ai/agent-zero/main/AGENTS.md - the stack line (Python 3.12+ framework, Flask, Alpine.js, LiteLLM, Socket.IO).
- https://raw.githubusercontent.com/agent0ai/agent-zero/main/docs/guides/agent-profiles.md - Agent Profiles as repeatable roles for a chat, and the bundled profiles left unchanged under /a0/agents.
- https://api.github.com/repos/agent0ai/agent-zero/releases?per_page=8 - the release feed, v2.16 (2026-11-17) back to v2.9 (2026-08-12), with the v2.15 and v2.16 notes.
- https://api.github.com/repos/agent0ai/agent-zero/contributors?per_page=8 - the two-account commit split (3clyp50 1,395, frdel 1,051, linuztx 139).
- https://api.github.com/repos/frdel/agent-zero - the original repository path, which resolves to agent0ai/agent-zero.
- https://agent-zero.ai/ - the site's framework pitch, the A0T token description, and the Agent Zero, s.r.o. company line.
- https://www.agent-zero.ai/p/architecture/ - the architecture overview, including A2A communication for multi-agent orchestration.
- https://www.agent-zero.ai/p/linux-foundation-article/ - the Linux Foundation Research "Decentralization and AI" profile by Alan Majer: founder Jan Tomášek, agents summoning sub-agents recursively, the "genius engineer" and "foolish child" remark, and the no-commercial-plans statement.
- https://www.linuxfoundation.org/research/decentralized-internet - the report's page at the Linux Foundation.
- https://www.agent-zero.ai/p/articles/agent-zero-v2-16/ - the v2.16 release article of 2026-11-17 with its security and upgrade notes.
- https://www.agent-zero.ai/p/articles/agent-zero-v3-sandboxing-sneak-peek/ - the 2026-08-17 sneak peek at gVisor sandboxes for agent-run code, marked as work in progress.
- https://www.agent-zero.ai/p/articles/agent-zero-kali-linux/ - the 2026-05-20 article on the dedicated Kali Linux environment the agent runs in.
- https://www.agent-zero.ai/p/docs/installation/ - the Docker command bound to localhost and the rule never to expose the instance without Web UI authentication.
- https://www.agent-zero.ai/p/token - the A0T token on Base, sponsorship, and governance.
- https://www.agent-zero.ai/p/community/api-dashboard/about/ - the LLM API proxy: A0T staking unlocks Venice.ai model access.
- https://hn.algolia.com/api/v1/search?query=%22Agent%20Zero%22&tags=story&hitsPerPage=30 - the five Hacker News stories about the project, 1 to 3 points each with no comments.
- https://www.anchorterminal.com/tools/agent-zero - the third-party review grading it D (49.7 of 100): no approval step, Tool Access defaulting to allow, Infection Check disabled, the update check, and third-party CVEs with no vendor advisory, evidence checked 2026-11-04.
- https://julian-b.xyz/posts/agentZeroSecurityWriteup.html - the 2025-06-27 security write-up: no login by default on the Web UI and cross-site request forgery file uploads into the container (fetched in full through a second client after the first returned 403).
- https://api.github.com/repos/agent0ai/agent-zero/issues/1474 - the user report of clear-text credentials in logs and persisted histories on v1.7, opened 2026-04-08 and closed 2026-07-08.
- https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=agent-zero - the National Vulnerability Database keyword search returning ten CVE records, as of 2026-11-24.
