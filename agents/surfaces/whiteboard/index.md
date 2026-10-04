---
title: Whiteboard
created: 2026-10-04
updated: 2026-10-04
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, surface, review, open-source]
readability: 3
audience_notes: >
  Engineers whose agents ship work faster than they can review it and who want
  a visual surface for understanding what an agent did. Assumes you run Claude
  Code, Codex, or a similar harness daily.
---

Whiteboard is an MIT-licensed desktop app (YC W26) where a coding agent draws its work on a shared canvas, giving humans a review surface made of diagrams, traces, and diffs instead of terminal scrollback.

## What it is

Whiteboard by /dev/fast is a beta desktop app for macOS, Windows, and Linux that plugs into the harnesses you already run (Claude Code and Codex named first) and hands the agent an SDK to draw on an in-app canvas as it works.
The canvas holds Whiteboard-specific objects: Commits, Diffs, Traces, and a source tree, plus copy-for-agent selection that turns any highlighted region into a prompt-ready snippet.
The public site documents an open API proposal (diff search: parse, hydrate, postprocess) that pins agent-found evidence to exact Git blobs, so a diagram claim can be checked against source.
It shipped v0.2.0 on 2026-10-02 after three releases in its first public week, and the repo shows 2,668 stars and 123 forks as of 2026-10-04.

## Status

New with real traction: the Show HN launch on 2026-09-24 drew 424 points, and the repository, created 2026-08-18, was pushed 2026-10-03.
The team is four (Sid, Alex, Ketan, and Milan), YC W26-backed, and built the app for themselves first.
Distribution is free, open source, and local-only in beta; the founders say a hosted plan is being considered but not decided, so there is no revenue model yet.
The category question is unresolved even in its own launch thread, where commenters reached for orchestrator, control plane, and agent multiplexer before the authors placed it as deliberately not opinionated about where your agent runs.

## Strengths

- **Review is a separate product slot from orchestration, and Whiteboard is the first entrant in it with distribution.**
- The evidence-pinning design (agent claims hydrated against exact Git blobs) attacks the real problem with agent diagrams, which is whether the picture still matches the code.
- Local-first and MIT: the canvas, the agent SDK, and the review artifacts stay on your machine.
- The agent-draws-while-it-works interaction is genuinely new as a shipped product, not a demo.

## Cautions

- The launch thread's own debate (is it an IDE, an orchestrator, a control plane?) reflects a real risk: a review surface nobody can categorize is hard to adopt into a workflow.
- A skeptical comment called the animated hand-drawn diagrams a technique heading everywhere, which cuts both ways: the medium may age faster than the function.
- No hosted plan and no pricing: the business is a stated maybe, and beta desktop apps churn.
- Fifty open issues against six weeks of life, with every major OS build user-reported rather than vendor-certified.

## Pricing

Free and open source under MIT in beta; the founders say a hosted offering is under consideration but undecided.
Without stated prices there is no price history to track.

## Compared to

- Zed ships agent review inside a production editor with its Delta multiplayer environment; choose Zed when review should live where you edit, Whiteboard when you want a dedicated canvas.
- Delta replaces pull requests with in-thread review on DeltaDB; Whiteboard stays harness-agnostic and draws rather than hosts.
- OpenChamber is the session cockpit for running many agents; Whiteboard is for understanding the work one agent did.

## Bottom line

Recommended for engineers whose agent output outpaces their diff-reading capacity and who accept beta churn on a six-week-old app.
Not for teams that need a supported, priced, categorized tool, and not for anyone whose review loop already lives happily in their editor.

## Changes

- 2026-10-04 - Created.

## See also

- [Zed](../zed/index.md) - the editor-anchored contrast, whose Delta environment puts review inside the IDE instead of a canvas.
- [Delta](../delta/index.md) - the PR-replacing review experiment closest to Whiteboard's ambition, hosted rather than harness-agnostic.
- [OpenChamber](../openchamber/index.md) - the running-side cockpit that complements rather than overlaps the review surface.
- [Cursor](../cursor/index.md) - the platform-scale alternative where review, editing, and agents share one vendor surface.

## References

- https://github.com/devdotfast/whiteboard - repository, MIT license, 2,668 stars, 123 forks, release cadence through v0.2.0 (2026-10-02), and the 2026-10-03 push, fetched 2026-10-04.
- https://whiteboard.dev.fast/ - product surface: canvas objects (Commits, Diff, Trace, source tree), the diff-search API proposal with Git-blob hydration, copy-for-agent selection, and downloads for three OSes, fetched 2026-10-04.
- https://news.ycombinator.com/item?id=49833867 - the 424-point Show HN launch (2026-09-24) with the team, the harness integrations, the free-local-only answer, and the categorization debate, fetched via the Algolia items API this run.
- https://github.com/devdotfast/whiteboard/releases - the v0.1.3, v0.1.5, and v0.2.0 release train across the launch week, fetched 2026-10-04.
- https://hn.algolia.com/api/v1/items/49833867 - the thread text and comment tree grounding the skeptical and categorical commentary, fetched 2026-10-04.
