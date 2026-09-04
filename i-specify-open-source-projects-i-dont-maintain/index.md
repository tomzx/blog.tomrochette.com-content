---

title: "I Specify Open Source Projects I Don't Maintain"
created: 2026-08-06
type: post
status: draft
tags: [ai, software-engineering, sdlc, specification, open-source, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader is an engineer or architect who builds on top of open-source AI tooling and has felt the cost of depending on code nobody has ever written a specification for. Comfortable with SDLC vocabulary (requirements, specification, plan).
agent_sessions:
  - ses_02ac6f0deffeJM9zGSgxYb57qd
---

I keep a public repository called [TomzxCode/sdlc](https://github.com/TomzxCode/sdlc) that holds no application code.
It holds specifications, requirements, plans, decisions, and learnings for open-source projects I depend on but do not maintain, projects like [OpenCode](https://github.com/anomalyco/opencode), [OpenChamber](https://github.com/openchamber/openchamber), [Paperclip](https://github.com/paperclipai/paperclip), and [Pi](https://github.com/earendil-works/pi).
**The reason is simple: if nobody has written the specification for the code I build on, I have my agents write it, in a workspace I control.**

This looks like extra work, but the writing is not mine to do anymore.
Pointing an agent at an unfamiliar repository and asking it to produce the specification is cheap, and it is the cheapest leverage I have found for depending on software I did not write.

## What the workspace actually is

The repository is organized by GitHub path.
Every tracked project lives under `{organization}/{repository}/`, and each one holds a `.sdlc/` tree of markdown artifacts: needs assessments, requirements, specifications, plans, tests, decisions, assumptions, and learnings.
There is no source code in it, because the source code already lives upstream where it belongs.
**What lives here is the durable planning and design knowledge that precedes and guides implementation, the layer that upstream projects rarely maintain in public.**

The workspace is consumed by the [SDLC skill pipeline](https://github.com/tomzx/agents/tree/main/skills/sdlc), which produces these artifacts and keeps them consistent.
[sync-sdlc](https://github.com/tomzx/agents/tree/main/skills/sync-sdlc) runs weekly in CI, where it re-checks out each upstream project, regenerates the `.sdlc/` artifacts to match the current code, and commits the diff, so when upstream changes, the specification does not silently rot.
A build script in the workspace renders the state of every project into a static status dashboard published at [tomzxcode.github.io/sdlc](https://tomzxcode.github.io/sdlc/), which gives me a single page to see where each project stands across the whole lifecycle.

## Why specifications live outside the code

The default place for documentation is inside the repository it describes.
That default is wrong for specifications, and it gets worse as the generation step automates.

When the spec sits next to the code, three things go wrong at once.
It is written by whoever happens to be implementing, which makes it an afterthought rather than an input.
It drifts the moment the code changes and nobody updates it, because the cost of updating is paid by the author and the benefit is collected by the next reader.
And it cannot be compared across projects, because each one reinvents its own format and keeps its own conventions in its own corner of the internet.
**A specification that cannot be read alongside the specifications of its peers is a specification that cannot be cross-referenced, and a specification that drifts silently is worse than no specification at all, because it makes decisions with the authority of one.**

Pulling the specs into a workspace I own inverts all three.
My agents write them before I build on the code, so they are an input.
The drift check runs on a schedule against a workspace I control, so updating is part of the pipeline rather than a favor I ask of upstream.
And every project shares one format, one directory structure, and one set of conventions, which is what makes cross-referencing possible at all.

## Why specify projects you do not own

This is the part that sounds strange until you need it.
Most teams never write a specification for someone else's software.
You read the README, you read the code, you form a mental model, and you build.
The mental model stays in your head, it is lossy, and the next person redoes the whole reconstruction from scratch.

I depend on a handful of fast-moving AI tools, and I depend on them at a level where a wrong assumption about their architecture costs me real time.
The cheapest way I have found to depend on them well is to have an agent write down what the code does, at a specification level, and then let the drift check tell me when that write-up has gone stale.
**Having the agent write the spec is how I learn the system, and keeping the spec is how I notice when my understanding has drifted from the code.**

There is a second payoff that only shows up when several projects share one workspace.
Once OpenCode, OpenChamber, Paperclip, and Pi are specified in the same format, in the same place, their architectures become comparable.
I can see where they overlap, where they assume different things about the same problem, and where a decision recorded for one project is the decision I should reuse for another.
That comparison is impossible when each spec is buried in its own repository behind its own conventions, and it is the reason a shared workspace beats a folder per upstream repo.

## What becomes possible once the specs are centralized

A few things only work because the specifications live together and are machine-checked.

Drift turns into a signal instead of a silent rot.
When upstream ships a change that contradicts a recorded requirement, the weekly [sync-sdlc](https://github.com/tomzx/agents/tree/main/skills/sync-sdlc) pass catches it and regenerates the artifact to match, so the contradiction shows up as a committed diff I can review before it costs me a debugging session downstream.
The specification stops being a document and starts being a contract that gets verified.

Traceability runs in both directions.
[backpropagate-sdlc](https://github.com/tomzx/agents/tree/main/skills/backpropagate-sdlc) walks the artifact chain in reverse, from code back to the requirement that motivated it, which is how I tell whether a change I am about to build on top of is actually backed by a recorded decision or is just something that happened to ship.

And the whole workspace reads as a status page.
Because every project reports through the same [sdlc-status](https://github.com/tomzx/agents/tree/main/skills/sdlc-status) format, one page tells me which projects have open questions, which have decisions pending, and which have drifted since last week.
**The point of centralizing the specifications is not tidiness; it is that consistency across projects is a thing you can only buy once, by putting them in the same place under the same rules.**

## What to do next

If you depend on open-source software at a depth where assumptions hurt, try the pattern on one project.
Clone [TomzxCode/sdlc](https://github.com/TomzxCode/sdlc) as a reference for the layout, pick one upstream repository you build on, and write its specification in a `.sdlc/` tree you control.
Run the [SDLC skills](https://github.com/tomzx/agents/tree/main/skills/sdlc) against it if you use a compatible agent, or just keep the tree by hand; the value is in the artifact and the format, not in the tooling.

**Treat the specification as the input to everything you build on top, not as documentation of what was built.**
When upstream changes and your spec drifts, treat the drift as a finding about your own understanding, because that is exactly what it is.
And once you have two or three projects specified in the same place, read them side by side, because the comparisons that fall out of a shared workspace are the part you cannot get any other way.

## See also

- [Defects Flow Downstream, Fixes Must Flow Upstream](../defects-flow-downstream/index.md) - why the specification is the highest-leverage artifact to get right and to fix when it is wrong, the argument this workspace is built to act on
- [The Foundation Predicts the House of Cards](../the-foundation-predicts-the-house-of-cards/index.md) - the upstream artifacts as the foundation whose quality decides whether the code built on top stands up, which is the case for specifying your dependencies
- [My AI Workflow: The Skills Are the Part That Compounds](../my-ai-workflow/index.md) - the skills library that produces and maintains these specifications, the engine behind the workspace
- [The Self-Evolving Repository](../the-self-evolving-repository/index.md) - the end state when drift detection and scheduled syncs keep a specification workspace current without manual upkeep
- [The Codebase Gardener](../the-codebase-gardener/index.md) - why the layer every project passes through is where you fight for cross-project consistency, which is the point of centralizing specifications
- [Verifying Code Without Reading It](../verifying-code-without-reading-it/index.md) - the shift from reading diffs to checking artifacts, the same relocation that makes a drift-checked specification more valuable than a code review

## References

- [TomzxCode/sdlc](https://github.com/TomzxCode/sdlc) - the workspace this article describes, holding specifications for several open-source AI projects under a shared `.sdlc/` layout
- [SDLC status pages](https://tomzxcode.github.io/sdlc/) - the rendered static-HTML view of every tracked project's lifecycle state
- [tomzx/agents, SDLC skill](https://github.com/tomzx/agents/tree/main/skills/sdlc) - the pipeline that produces the artifacts the workspace holds
