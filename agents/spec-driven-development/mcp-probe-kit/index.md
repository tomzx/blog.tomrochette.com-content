---
title: MCP Probe Kit
created: 2026-11-01
updated: 2026-11-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, spec-driven-development, mcp, workflow, open-source]
readability: 3
audience_notes: >
  Engineers who want a spec-driven delivery loop enforced through MCP tools rather than slash commands or a CLI.
  Assumes you know what an MCP server and a review gate are.
---

MCP Probe Kit is a solo-maintained, MIT-licensed MCP server that runs a spec-driven delivery loop (requirements, spec, implementation, test, review) as 29 model-visible tools, with a convergence gate that blocks closure until that evidence chain is complete.

**Its bet is protocol-native enforcement: where this category's other members ship slash commands, skills, or CLIs that the harness interprets, MCP Probe Kit makes the workflow itself a set of MCP tools the agent calls, and the converge tool refuses to close a feature until the spec, test, and review evidence exists.**

## What it is

An npm package (`npx mcp-probe-kit@latest`, first published 2025-10-25, at v4.1.1 after 82 versions) that any MCP client can mount: Cursor, Claude Desktop, Cline, Continue, and others, speaking both the legacy MCP protocol and the 2026-07-28 revision, on Node.js 20 or newer.
The tool surface splits into plan persistence and convergence (`plan_heartbeat`, `resume_plan`, `converge`), workflow orchestration (`start_feature`, `start_bugfix`, `start_onboard`, `start_ui`, `start_product`, `start_ralph`), and project and specification tools (`init_project`, `init_project_context`, `check_spec`, `estimate`), beside code, test, git, and structured-interview utilities, with a 39-tool compatibility surface behind an opt-in flag.
Five native MCP Apps render the workflow: a Memory Center, Feature, Bug, and Product Workbenches, and the Convergence Gate itself.
State is local: delegated plans persist progress through `plan_heartbeat` and resume across sessions with `resume_plan`, chat handoff archives losslessly under `docs/history-session/` without a vector database, and the optional memory layer needs a self-hosted Qdrant plus an embedding endpoint.

## Status

Active and shipping, thinly adopted: 41 stars, 5 forks, created 2025-10-25, pushed 2026-11-05, as of 2026-11-07 (GitHub API), MIT, solo steward (mybolide).
The npm package has 82 published versions in its first year, v4.1.1 (2026-10-13) the newest stable, and 1,096 downloads last month (the 2026-10-08 to 2026-11-06 window, re-read 2026-11-07).
The v4 line (2026-08 through 10) shipped native MCP Apps, resumable plans, evidence convergence, parent-child specs, and a managed GitNexus sidecar.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=mybolide/mcp-probe-kit&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=mybolide/mcp-probe-kit&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=mybolide/mcp-probe-kit&type=date&legend=top-left" />
</picture>

**The independent footprint is empty, and that is this note's critical angle: a Hacker News search returns nothing, and the only third-party badge is the MseeP listing the README itself carries, so the claims rest on the steward's own README, homepage, and demo animations.**

## Strengths

- The convergence gate is protocol-native: `converge` refuses closure when requirements, spec, implementation, test, or review evidence is incomplete, the category's convergence idea enforced as a tool call instead of a convention.
- Plans survive sessions: `plan_heartbeat` persists actual progress and `resume_plan` restores the next executable step, so delegated agent work does not restart from zero.
- One mount covers any MCP client with no per-harness packaging, and both the legacy and 2026-07-28 protocol revisions are supported.
- The surface is explicit about its own breadth: the compact 29-tool default hides the rest, and the full 39-tool compatibility set is opt-in rather than forced.

## Cautions

- Zero independent coverage and a solo steward: 41 stars and about 1,100 npm downloads a month after a year is thin validation for a 29-tool surface.
- The breadth invites drift: workflow orchestration, memory, GitNexus sidecar management, UI utilities, and commit generation in one server, with 82 npm versions in a year signaling churn.
- The memory layer's defaults need self-hosted infrastructure (Qdrant, an embedding endpoint), so the out-of-box experience is the no-memory subset.
- Enforcement is still the agent choosing to call `converge`: a harness or prompt that skips tool calls bypasses the gate the same way a yolo-configured agent skips any convention.

## Pricing

Does not apply: MIT, free, no paid tier found as of 2026-11-01.

## Compared to

- [GitHub Spec Kit](../spec-kit/index.md): the movement root scaffolds markdown conventions the harness drives through slash commands; MCP Probe Kit exposes the loop as protocol tools any MCP client can call.
- [Spec Kitty](../spec-kitty/index.md): the other gated-pipeline member; Spec Kitty keeps review state in your repository and runs work packages in worktrees, MCP Probe Kit keeps evidence state in tool results and runs wherever the client does.
- [Archcore](../archcore/index.md): the other convergence-first member; Archcore reviews typed documents in git and names the side that is wrong, MCP Probe Kit gates closure on recorded evidence without a document layer.

## Bottom line

**Recommended for engineers already running an MCP client who want the spec loop delivered as tools, with delegated plans that resume across sessions and a convergence gate, and who accept an unvalidated, fast-churning surface.**
Not for anyone who needs independent validation, a stable tool API, or a workflow whose state lives in the repository rather than in a server process.

## Changes

- 2026-11-01 - Created from the Engineering4AI awesome-list entrant scan (the MCP Servers entry merged 2026-11-01), resolving mybolide/mcp-probe-kit as the protocol-native workflow column with the zero-coverage record as the critical angle.

## See also

- [GitHub Spec Kit](../spec-kit/index.md) - the movement root whose workflow MCP Probe Kit re-delivers as tools
- [Spec Kitty](../spec-kitty/index.md) - the other evidence-gated pipeline, repo-side state where MCP Probe Kit is protocol-side
- [Archcore](../archcore/index.md) - the convergence-first neighbor with a document layer
- [Spec Driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/mybolide/mcp-probe-kit - repository: counts, dates, license (41 stars as of 2026-11-01)
- https://raw.githubusercontent.com/mybolide/mcp-probe-kit/main/README.md - the tool surface, convergence gate, plan persistence, history session, and MCP Apps
- https://registry.npmjs.org/mcp-probe-kit - the npm package: v4.1.1 latest, 82 versions, MIT, first published 2025-10-25
- https://api.npmjs.org/downloads/point/last-month/mcp-probe-kit - 1,096 downloads last month (2026-10-08 to 2026-11-06 window), fetched 2026-11-07
- https://api.github.com/repos/mybolide/mcp-probe-kit/releases - the release train through v4.1.1 (2026-10-13), fetched 2026-11-07
- https://mcp-probe-kit.bytezonex.com/ - the project site: the v4 framing and the workbench surfaces
- https://hn.algolia.com/api/v1/search?query=mcp-probe-kit&hitsPerPage=5 - the footprint check: zero hits, the missing-coverage signal
