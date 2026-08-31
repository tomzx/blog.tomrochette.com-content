---
title: "My Feature Planning Method: Iterate in Parallel, Then Pass Forward"
created: 2026-08-31
type: post
status: finished
tags: [ai, software-engineering, sdlc, planning, workflow, llm, ai-agents, partially-ai-generated, llm=glm-5.3-flash]
readability: 3
audience_notes: >
  Assumes the reader runs coding agents against a structured development process and is comfortable with SDLC vocabulary (requirements, specification, plan). No introduction to what an LLM is.
---

Planning a feature splits into two jobs: finding out what the questions are, and answering them in an order that lets each answer build on the one before it.
The two jobs reward opposite working modes, which is why running them as one activity fails.
When I planned linearly, writing the requirements first and the specification next, the questions surfaced late, after the artifacts they invalidated were already written.
**The method I use now runs the two jobs as two distinct phases: I iterate on every artifact of a feature in parallel until the big questions surface, then I make one ordered forward pass that settles each file in the sequence the SDLC defines.**

## The directory is the feature

Everything I plan lives in a `.sdlc/features/N-feature/` directory, one per feature.
A feature starts as a problem statement in its own file, because a feature whose problem cannot be written down is not ready to be designed.
Around that seed the directory grows into the full artifact set the [SDLC skill](https://github.com/tomzx/agents/tree/main/skills/sdlc) defines: needs assessment, feasibility, requirements, specification, tests, and the rest.

A mature feature directory carries the full artifact set the [SDLC templates](https://github.com/tomzx/agents/tree/main/skills/sdlc/templates) define, needs assessment, requirements, existing solutions, codebase analysis, feasibility, specification, plan, tasks, tests, and a review findings file paired with each, one purpose per file.
On top of that standard set sit the files of my own that hold the directory together.
`README.md` is the overview of the feature and the guide to how the other files should be consumed, which makes it the entry point an agent reads first.
`files-flow.md` records which files depend on which in terms of content, and it matters enough to get its own section below.

## files-flow.md turns consistency into a graph

Many files drift.
A decision that changes in the requirements silently invalidates everything downstream of it, and my memory is not a mechanism I trust to find all of it.
So every feature directory carries `files-flow.md`, a [mermaid](https://mermaid.js.org/) graph of how the files depend on each other in terms of content.
An edge from X to Y means Y's content is derived from X's content, and the rule the graph encodes is mechanical: when file X changes, every Y that depends on X gets re-verified against the new X.
**The graph is documentation for me and a worklist for the agent at the same time, which is the only way a consistency rule survives contact with ten interlocking artifacts.**

## Phase one: iterate in parallel

The first pass over a new feature directory is deliberately chaotic.
I write the problem statement, then jump into the requirements, the specification, and the component plans all at once, in whatever order the thinking wants to happen.
Writing a specification forces questions the requirements never answered, and writing a component plan forces questions the specification never answered, so working the files together is the fastest way to find the holes.
**Iterating in parallel is a question-finding machine: the point is not to finish any file, it is to make every file betray what I do not know while the cheapest possible response is still to write the question down.**
Within a few passes I have the list of risks and open questions that would otherwise have surfaced at implementation time, when each one costs an order of magnitude more to fix.

## Phase two: the forward pass

Once the large questions have answers, I switch modes.
The iteration stops and the forward pass starts: problem statement, then requirements, then specification, then the plans and tests, in the sequence the SDLC skill defines.
A colleague of mine pictures the sequence as a funnel that expands as clarity about what we are building accumulates.
The problem statement is the narrow end, and each artifact downstream widens it, requirements expanding the problem, the specification expanding the requirements, plans expanding the specification.
Walking the funnel in order works because each file gets finished before the next one begins, so every downstream file is written against an upstream that is stable rather than half-moved.
By the time the pass reaches the component plans, most of the content is transcription, because the hard decisions were made during the parallel phase.
**The forward pass is cheap precisely because the parallel phase paid for it.**

## Why two phases instead of one

Linear planning discovers questions at the worst possible time, after the artifacts they invalidate exist.
Parallel-only iteration has the opposite failure: it keeps re-litigating every file and never converges.
The two-phase split gives each mode the job it is good at, and the switch between them is a deliberate decision, not a drift.
My rule for switching is simple: when another pass over the files stops producing new questions, the questions are found, and it is time to answer them in order.
None of this makes the order sacred, and an unknown piece of functionality is where I stay most open about how to work.
The instinct is to proceed methodically, but when an LLM can explore a design space in minutes, the smarter sequence is usually reversed: use the model first to identify the risks, surface the questions, and lay out the options, and only then backtrack and write the relevant documents in order.
Exploration is nearly free, so the failure mode to avoid is premature documentation, not wasted exploration.

## What to Do Next

If you plan features as a pile of SDLC artifacts:

- Start every feature directory with a problem statement file and a files-flow.md, before the requirements exist.
- During discovery, write all the artifacts roughly and simultaneously instead of finishing them one at a time.
- Treat "a full pass produces no new questions" as the signal to stop iterating and start the forward pass.
- When any file changes, follow the files-flow edges and re-verify every dependent file before calling the change done.

## See also

- [Three Gaps My SDLC Pipeline Hit on a Machine Learning Platform](../three-gaps-my-sdlc-pipeline-hit-on-a-machine-learning-platform/index.md) - the stress test that produced files-flow.md and the propagation rule it encodes
- [Every Decision You Change Pays Once Per File](../every-decision-you-change-pays-once-per-file/index.md) - the cost model behind writing the dependency edges down instead of recalling them
- [Defects Flow Downstream](../defects-flow-downstream/index.md) - why a question found during parallel iteration is cheaper than the same question found at implementation
- [My AI Workflow: The Skills Are the Part That Compounds](../my-ai-workflow/index.md) - the skills pipeline these feature directories feed
- [When a Closed Decision Reopens](../when-a-closed-decision-reopens/index.md) - why every decision lives in a file, and what happens to decisions that live only in conversation

## References

- [SDLC skill](https://github.com/tomzx/agents/tree/main/skills/sdlc) - the pipeline whose artifact sequence the forward pass follows
- [Mermaid](https://mermaid.js.org/) - the diagram syntax files-flow.md uses, readable by both humans and agents
