---
title: Agent-Causality
created: 2026-10-28
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, run-recording, replay, causal-analysis, open-source]
readability: 3
audience_notes: >
  Engineers debugging branching multi-agent failures who want the causal structure captured while the run happens, not guessed afterward.
  Assumes you know what an event graph, a SQLite file, and counterfactual replay are.
---

Agent-Causality is an AGPL-3.0 Python SDK and CLI that records OpenCode and LangGraph agent runs as causal event graphs with declared parents, slices a failing event to the recorded events it structurally depends on, and replays registered decisions with changed inputs to test which ones flip the outcome.

**Agent-Causality's bet is that causality belongs in the capture, not the post-mortem: every event carries the parents its recorder declared, so slices, provenance, and counterfactual replay are queries over facts the run wrote down, and the project's own benchmark reports where that stops working.**

## What it is

Two packages are required, and the README says so plainly: `agent-causality` on PyPI (the SDK, CLI, an ingest receiver for OpenCode events, and the Visual DAG Explorer web UI) and `@psionic-labs/opencode-agent-causality` on npm (an OpenCode plugin, telemetry capture only, forwarding the global event stream plus tool, permission, and message hooks).
Events persist to one SQLite file per run, with secrets redacted before persistence; capture is fail-open and never interrupts the agent.
LangGraph runs record through a callback handler that converts parent_run_id containment into explicit causal edges, dropping unknown parents rather than inventing them.
The Explorer renders the causal graph and a per-agent timeline and ships analysis tabs (chain, provenance, interaction, evidence, metrics), no API key needed; an optional explain extra adds LLM-grounded analysis through OpenRouter, kept in its own labeled block.
Made by Vasant Kumar Mogia (Psionics) under AGPL-3.0, with an in-repository research paper on declared dependency tracing and counterfactual sensitivity analysis.

## Status

Young and active but essentially unadopted: 6 stars, 2 forks, 3 open issues, created 2026-08-15, pushed 2026-10-28, releases through v0.2.1 on 2026-10-22, as of 2026-10-28.
The registries confirm the thinness: PyPI serves 0.2.1 (the README names 0.3.0) and the OpenCode plugin 0.1.6, with 154 PyPI downloads in the week to 2026-10-28 and 243 npm downloads in the month to 2026-10-26.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Psionic-labs/Agent-Causality&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Psionic-labs/Agent-Causality&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Psionic-labs/Agent-Causality&type=date&legend=top-left" />
</picture>

The critical source is the project's own benchmark, and it is unusually frank: live OpenCode runs captured at micro/macro-average 1.0, but a cause recall of 0.3 over explicit-evidence edges and a joint ancestry of 0.0, with the README conceding that genuine causal interaction is unsupported from live traces.
I found no independent discussion: the Hacker News story search returns zero hits, and the README's evidence is its own benchmark results.
**A solo research-grade tool with a paper, frankly negative self-benchmarks, and no community verdict yet, so read the benchmark results before believing the causal claims.**

## Strengths

- Declared, not inferred, causal edges: every parent link is recorded at capture time by the recorder that saw the dependency happen.
- The self-benchmark names its failures (cause recall 0.3, joint ancestry 0.0 on live traces), which is more falsifiable than the category's usual claims.
- Both surfaces a debugging session needs are included: a queryable SQLite graph and a no-key Explorer with graph, timeline, and metrics views.
- Counterfactual replay re-runs registered merge decisions with changed inputs and reports which flips change the outcome.
- Capture never blocks the agent, and secrets are redacted before anything persists.

## Cautions

- 6 stars, 2 forks, and zero independent coverage: every claim here is the project's own evidence.
- The tool's own live-trace results limit it to structural slices over explicit edges, not true causal interaction, which is the whole promise.
- AGPL-3.0 complicates embedding in commercial tooling, and the two-package install means either half alone is incomplete.
- Version drift: the README names agent-causality 0.3.0 while PyPI serves 0.2.1, an early-project smell to watch.
- One maintainer, pre-1.0, and a schema surface (SQLite event graphs) with no compatibility guarantees yet.

## Pricing

Free and open source under AGPL-3.0; no paid tier is published, and everything runs locally.

## Compared to

- [NovaFabric](../novafabric/index.md): the replay-and-evidence sibling from the same source list; NovaFabric preserves and diffs whole runs for audit, Agent-Causality slices recorded runs for cause.
- [agentsview](../agentsview/index.md): the archive that answers history and cost questions; Agent-Causality answers only why this run failed, from a capture it had to be present for.
- [ClawTrace](../clawtrace/index.md): the hosted tracing platform with an AI analyst; ClawTrace sees live OpenClaw payloads in the cloud, Agent-Causality keeps declared causal graphs in a local SQLite file.

## Bottom line

**Recommended for engineers running branching LangGraph or OpenCode systems who want failure diagnosis grounded in capture-time facts, and who will read the benchmark before trusting the slice.**
Not for cost reporting, transcript search, live dashboards, or anyone who needs an independently verified dependency.

## Changes

- 2026-10-28 - Created from the coordinator's entrant handoff, admitted on the declared-causal-parent capture mechanism, the self-critical live-trace benchmark with its named negative results, and nine fetched sources.

## See also

- [NovaFabric](../novafabric/index.md) - the run-recording and evidence sibling this note joined with
- [agentsview](../agentsview/index.md) - the retrospective archive for everything except why a run failed
- [ClawTrace](../clawtrace/index.md) - the hosted tracing alternative with full payloads
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins

## References

- https://api.github.com/repos/Psionic-labs/Agent-Causality - 6 stars, 2 forks, AGPL-3.0, created 2026-08-15, pushed 2026-10-28, as of 2026-10-28
- https://raw.githubusercontent.com/Psionic-labs/Agent-Causality/main/README.md - the two-package contract, capture hooks, SQLite storage, Explorer views, benchmark summary, and the paper link
- https://api.github.com/repos/Psionic-labs/Agent-Causality/releases - v0.2.1 (2026-10-22), v0.2.0 (2026-10-18), v0.1.4 (2026-10-14)
- https://pypi.org/pypi/agent-causality/json - PyPI package, version 0.2.1, Python 3.11 or newer
- https://registry.npmjs.org/@psionic-labs/opencode-agent-causality - the OpenCode plugin, latest 0.1.6 (2026-10-22)
- https://pypistats.org/api/packages/agent-causality/recent - 154 downloads in the week to 2026-10-28, behind the adoption claim
- https://api.npmjs.org/downloads/point/last-month/@psionic-labs/opencode-agent-causality - 243 downloads in the month to 2026-10-26
- https://psionic-labs.github.io/Agent-Causality/opencode.html - the OpenCode integration guide
- https://raw.githubusercontent.com/Psionic-labs/Agent-Causality/main/docs/benchmarks.md - the full benchmark results behind the negative-results claim
- https://hn.algolia.com/api/v1/search?query=Agent-Causality&tags=story - zero stories, the empty independent footprint this note states
