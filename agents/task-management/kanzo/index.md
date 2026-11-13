---
title: Kanzo
created: 2026-11-08
updated: 2026-11-12
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, task-management, kanban, mcp, rust, open-source]
readability: 3
audience_notes: >
  Developers who want one tiny local binary where the browser board they watch and the MCP server their agents use read and write the same task store.
  Assumes you know what an MCP server is and what a network-adjacent shared board implies for trust.
---

Kanzo is an AGPL-3.0 single Rust binary that serves a kanban board in your browser and an MCP server for your coding agents over one SQLite file in `~/kanzo`, so humans and agents share one task board with no account, no server, and no setup.

**The board is the shared human-agent surface, not the agent's export format: agents move the same cards you watch, Human-marked tasks and the Backlog column are lanes agents leave alone by data rather than by prompt, and live sharing puts the whole thing on a Raspberry Pi.**

## What it is

One 4.7 MB program (SQLite included) that starts in about 3 milliseconds and holds the whole board in `~/kanzo`: `kanzo.db` for tasks and `config.toml` for port, bind address, and MCP-over-HTTP settings, measured at 5 MB idle and 12 MB with 3,000 tasks on an Apple M4.
You get three doors onto the same store: the browser board at `localhost:4242`, the `kanzo` CLI for terminals and scripts, and MCP for agents, either stdio (`kanzo mcp`, wired up for Claude Code and Codex in the README) or HTTP at `/mcp` on the running board.
The agent surface is deliberately small: ten tools (`list_projects`, `create_project`, `link_repo`, `list_tasks`, `get_task`, `create_task`, `update_task`, `add_comment`, `next_task`, `delete_task`), about 1,000 tokens of schema read once per session, with an agent's project found from the git remote of the repo it works in.
Beyond one machine: `kanzo share on` and `kanzo join` put several computers and their agents on one live board over the network or a VPN with no logins, a private git repo you own syncs the board between machines you use one at a time, and `kanzo export` prints the board as Markdown or JSON.
Emanuele Micheletti (the emanuele-em identity) maintains it, with GitHub-signed release artifacts checkable through `gh attestation verify`, a crates.io package, and installer scripts for macOS, Linux including the Raspberry Pi, and Windows.

## Status

Active and two weeks old at record speed.
As of 2026-11-12: 1,105 stars (fetched 2026-11-08), 95 forks, 9 open issues, created 2026-10-25, pushed 2026-11-11, and v0.4.2 (2026-11-11) the newest of a near-daily release train that began with v0.2.1 on 2026-10-27.
v0.3.0 (2026-11-01) added the live board sharing, a native Windows build, and the Human handoff, where an agent marks a task Human over MCP and leaves it alone; v0.4.0 (2026-11-06) added waits-on dependencies (`next_task` skips a card until its blockers are `done`, a card in `review` still blocks), multi-select and a list view on the board, and a Chinese UI; v0.4.1 (2026-11-07) lets agents switch to a new Kanzo version at their next call without reconnecting and restarts the board on update within seconds.
v0.4.2 (2026-11-11) was the first community-contribution release: three outside contributors fixed the Windows updater always failing, agent tools going silent after an update when a call had been cancelled or the client never sent `initialize` (MCP 2026-07-28 clients), `kanzo export` quietly writing its own old board on a computer joined to another board, and the board shrinking under a browser extension's empty element.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=emanuele-em/kanzo&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=emanuele-em/kanzo&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=emanuele-em/kanzo&type=date&legend=top-left" />
</picture>

An HN search returns zero story hits as of 2026-11-12 (the hits are fuzzy matches on unrelated Kano and Kanboard projects), and the crates.io package shows 241 total downloads, so adoption evidence is the repository curve alone: 1,105 stars in a fortnight is the fastest start this category has recorded, and it is entirely unaudited by independent discussion.

## Strengths

- One process serves the human board and the agent tools over the same SQLite file, so the state you watch is exactly the state the agents mutate, with no sync layer in between.
- The ten-tool MCP list is the cheapest agent surface in this category, about 1,000 tokens read once per session, and replies are plain text measured at 10 to 60 tokens.
- Human tasks and the Backlog column are data-level lanes agents leave alone, not conventions to prompt into every session, and comments record how to resume an agent's session when a card reaches review.
- The self-updating path works end to end: agents pick up new versions at their next call (v0.4.1), release artifacts are GitHub-signed with attestation verification, and the board restarts on update in seconds.

## Cautions

- There are no claim records or lease primitives: `next_task` hands out work by moving the card out of `todo` in one step, so two agents do not receive the same card, but nothing stops two agents from updating the same card through `update_task`, and comment authorship defaults to a generic agent unless the client names itself.
- Live sharing has no authentication: the README says to share only on a network you trust, the board binds to `127.0.0.1` until you change it, and sharing opens it to the network.
- AGPL-3.0 carries network copyleft: a changed version offered over a network must share its source, which matters if you wrap the board in a team service.
- One maintainer, v0.x churn on a near-daily train, and zero independent coverage two weeks in; the star curve is the only adoption signal, and it is young enough to reverse.

## Pricing

Free and open source under AGPL-3.0, self-hosted on your own machine or network.
No paid tier, hosted plan, or account exists.

## Compared to

- [kanban-md](../kanban-md/index.md): the files-first neighbor; kanban-md keeps the board as markdown in your repo with expiring claim leases, Kanzo keeps it in one local SQLite file with a browser UI and a smaller, MCP-native agent surface.
- [Agent Kanban](../agent-kanban/index.md): the other browser board for agents; Agent Kanban enforces the review gate but requires the Realmroot and Enbor ecosystem on Cloudflare, Kanzo is one standalone binary with no gate.
- [Kata](../kata/index.md): the local daemon ledger; kata is built for millisecond agent queries with atomic claims, TTL leases, and evidence-based closes, Kanzo is built for the human watching the board while agents work it.

## Bottom line

**Recommended for a solo developer running one to a few agents on one machine, or a small team on one trusted network, who wants to watch the same board the agents work and accepts that coordination stops at the handout.**
Not for teams needing enforced review gates, atomic claims as a boundary, or an audit-grade history, and not anywhere the board must live in git as files.
My disagreeable claim: the shared visual board is the underused primitive here, every other member routes agent work through files or APIs the human never watches live, and Kanzo's bet that watching beats querying is the one worth stealing even if its no-claims coordination is not.

## Changes

- 2026-11-08 - Created, completing the admission the 2026-11-03 cross-category routing resolved for this category (the andyrewlee listing, 921 stars then), with the ten-tool MCP surface, the handout-by-move coordination model, live sharing, and the missing independent footprint recorded.
- 2026-11-12 - Recorded v0.4.2 (2026-11-11: the first community-contribution release, three outside contributors fixing the Windows updater, agent tools silent after cancelled calls or initialize-less MCP 2026-07-28 clients, export on a joined computer, and the board-layout shrink) and refreshed counts (95 forks, 9 open issues, pushed 2026-11-11, 241 crates downloads).

## See also

- [kanban-md](../kanban-md/index.md) - the markdown-files counterpoint with claim leases
- [Agent Kanban](../agent-kanban/index.md) - the ecosystem-bound browser board with the enforced review gate
- [Kata](../kata/index.md) - the local daemon ledger with the claims Kanzo leaves out
- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the category comparison this note joins

## References

- https://raw.githubusercontent.com/emanuele-em/kanzo/main/README.md - the surfaces, sharing and sync models, waits-on rules, performance table, and license (fetched 2026-11-08)
- https://api.github.com/repos/emanuele-em/kanzo - stars, forks, dates, AGPL-3.0 as of 2026-11-12
- https://api.github.com/repos/emanuele-em/kanzo/releases - the v0.2.1 (2026-10-27) through v0.4.1 (2026-11-07) release train, with the v0.3.0 and v0.4.0 feature notes
- https://raw.githubusercontent.com/emanuele-em/kanzo/main/CHANGELOG.md - the v0.4.1 notes: agent self-update, the board restart, markdown tables
- https://raw.githubusercontent.com/emanuele-em/kanzo/main/src/mcp.rs - the ten-tool MCP surface, the next_task handout-by-move, and comment authorship defaults
- https://crates.io/api/v1/crates/kanzo - the cargo package: 241 total downloads, nine versions, created 2026-10-26 as of 2026-11-12
- https://hn.algolia.com/api/v1/search?query=kanzo&tags=story - zero story hits as of 2026-11-12, the missing independent footprint
