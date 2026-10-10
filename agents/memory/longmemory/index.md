---
title: LongMemory
created: 2026-10-08
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, temporal, sqlite, self-hosted, mcp]
readability: 3
audience_notes: >
  Engineers choosing a self-hostable memory engine who care about temporal truth and
  governance, profiled against the hosted temporal service and the thinner local options.
  Assumes you know what provenance and point-in-time queries mean.
---

LongMemory is an Apache-2.0 local-first memory engine: a TypeScript library, CLI, HTTP server, and MCP server over SQLite that keeps immutable, provenance-carrying memories with separate recorded and valid time, governed scopes, and four recall modes.

**Its bet is that memory needs the database properties agents never get (immutability, temporal truth, governance, explanation), and it is the first local option in this category to build all four into the open engine.**

## What it is

A project by CaviraOSS, renamed from OpenMemory (the old openmemory-js and openmemory-py packages remain as forwarding bridges; the official distribution is `longmemory` on npm, at 1.3.3).
The Hydrograph engine keeps immutable nodes, typed executable edges, worlds, entities, and traces, persisted to SQLite.
Recall comes in four modes: strict (temporal, contradiction, confidence, and grounding gates), historical (point-in-time queries with a supplied valid time), associative (semantic, lexical, entity, and graph signals), and world-grounded (requires current external evidence).
Governance is structural: tenant, organization, project, user, team, role, agent, task, and framework scopes, with MCP tool arguments unable to override server-bound identity.
Surfaces include the npm library, a CLI, an HTTP API on port 7331, an MCP server with 13 governed tools, a Next.js dashboard, a VS Code extension, a session porter that imports Claude Code, Codex, OpenCode, Gemini CLI, Copilot, and Cline logs, an n8n community node, and one-click templates for Docker, Heroku, Railway, and Render.

## Status

**Young but shipping, with a strong independent launch record for its size.**
4,524 stars with the repository pushed 2026-09-20, created 2025-10-19, as of 2026-10-09 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=CaviraOSS/LongMemory&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=CaviraOSS/LongMemory&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=CaviraOSS/LongMemory&type=date&theme=dark&legend=top-left" />
</picture>

The Show HN thread (December 2025, as OpenMemory) drew 48 points and 16 comments, and the README lists 36 contributors.
Its benchmark harness publishes manifests and fails closed on incomplete datasets or embedding fallback, covering LongMemEval, LoCoMo, and BEAM, though the published results are still the project's own runs.
Two verification gaps carried into this run: the PyPI distribution the README instructs you to install (`longmemory-sdk`) returned 404 again on 2026-10-09 (as on 2026-10-08), and the repository has not pushed since September 20.

## Strengths

- **Temporal truth in the open engine**: recorded time and valid time are separate, with supersession and point-in-time recall, territory every other local option here leaves to Zep's paid tier.
- Immutable storage with hashes and provenance, so recall and decay cannot rewrite history.
- Deterministic governance with server-bound identity, the strongest multi-scope story among the self-hostable members.
- The benchmark harness's fail-closed manifests refuse to publish incomplete runs, an unusually careful design for a self-run scoreboard.

## Cautions

- **Young and quiet**: no push since September 20, an npm train at 1.3.3, and a core team small enough that bus factor is a fair question.
- The Python SDK distribution 404'd on both the JSON API and the simple index this run, so the multi-language story is uneven in practice.
- The rich engine wants operations: embeddings need provider keys, and the server, dashboard, and extension paths add surface the in-process library hides.
- All published benchmark results are self-run; no independent replication exists yet.

## Pricing

Pricing does not apply: Apache-2.0 (the n8n node MIT by that registry's rules), self-hosted, no hosted tier, as of 2026-10-08.

## Compared to

- [Zep](../zep/index.md): the hosted temporal-graph service; LongMemory is the first open engine here with point-in-time truth, though unproven at Zep's production scale.
- [Cognee](../cognee/index.md): the other self-hostable graph option; Cognee builds graphs from documents in pipelines, LongMemory keeps a governed temporal store agents read and write.
- [Engrim](../engrim/index.md): the other local cross-agent store; Engrim is a thin curated SQLite scratchpad, LongMemory is a full engine with governance and temporal queries.

## Bottom line

**Recommended for teams that need temporal, governed memory they can self-host and will accept a young dependency.**
Not for anyone needing a hosted tier, a proven-at-scale engine, or a Python SDK that installs today.

## Changes

- 2026-10-08 - Created from the 2026-10-08 awesome-list entrant scan, with six fetched sources; the unresolvable PyPI SDK distribution recorded as the run's verification gap.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [Zep](../zep/index.md) - the hosted temporal service this engine's temporal model answers
- [Cognee](../cognee/index.md) - the pipeline-style self-hosted graph alternative
- [Engrim](../engrim/index.md) - the thin local store at the opposite end of the complexity spectrum

## References

- https://github.com/CaviraOSS/LongMemory - repository, 4,524 stars, activity, Apache-2.0, the OpenMemory rename, as of 2026-10-09
- https://raw.githubusercontent.com/CaviraOSS/LongMemory/main/README.md - the Hydrograph memory model, recall modes, governance scopes, surfaces, and migration paths
- https://raw.githubusercontent.com/CaviraOSS/LongMemory/main/LICENSE - the Apache-2.0 license text
- https://registry.npmjs.org/longmemory - the official npm distribution at 1.3.3
- https://pypi.org/simple/longmemory-sdk/ - the PyPI distribution returning 404 at fetch time (2026-10-08 and again 2026-10-09), the verification gap
- https://news.ycombinator.com/item?id=46262294 - the Show HN thread (48 points, 16 comments, 2025-12-14), the launch record
