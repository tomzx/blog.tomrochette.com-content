---
title: "My AI Workflow: The Skills Are the Part That Compounds"
created: 2026-07-28
type: post
status: finished
tags: [ai, llm, workflow, skills, opencode, openchamber, cursor, sdlc, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader already uses at least one coding agent (Cursor, Claude Code, OpenCode) and has felt the cost of re-explaining the same workflow to a fresh session. No introduction to what an LLM is.
---

When someone asks what my AI workflow looks like, the real answer is boring on the surface and surprising underneath.
I use a couple of coding tools and a couple of models, and none of them is the thing I would miss.
What I would miss is the body of skills I have been writing, collecting, and refining for the better part of a year.

This is a snapshot of that workflow as it stands today.
The tools come first because they are the visible part, but the real argument is that the tools are the part I expect to replace, and the skills are the part I expect to keep.

I run two coding surfaces and two models, and neither is the interesting part of my setup.
At home I use [GLM 5.2](https://z.ai) from z.ai, and at work I use [GLM 5.2 fast](https://fireworks.ai/blog/glm-5p2-fast) from [Fireworks](https://fireworks.ai).
For editing I use [Cursor](https://www.cursor.com/) at work and [VS Code](https://code.visualstudio.com/) at home, and for anything agentic, multi-step, or long-running I use [OpenChamber](https://github.com/btriapitsyn/openchamber), which is built on [OpenCode](https://opencode.ai).
I never open OpenCode directly; OpenChamber is the surface, OpenCode is the engine underneath.
**The part that actually determines the quality of my work is the library of skills I have been building and sharing in [tomzx/agents](https://github.com/tomzx/agents), and those skills run inside all four of those tools.**
Everything else is interchangeable.

## The setup, in one paragraph

Cursor or VS Code is where I read, navigate, and do small edits.
The moment a task turns into a sequence of steps, create an issue, reproduce a bug, review a PR, open a PR, I move it to OpenChamber, because that is where the work can run to a natural stopping point without me holding the state.
OpenChamber is built on OpenCode and is the control room on top of it: it gives me branchable sessions, worktree isolation, and a single surface to steer several sessions at once.
The skills are not tied to any of these surfaces; because they follow the open Agent Skills format, the same skill runs in Cursor, VS Code, OpenCode, or OpenChamber, so I pick the surface that fits the moment and the workflow does not change.
At home the editor is VS Code and the model is GLM 5.2 on z.ai, at work the editor is Cursor and the model is GLM 5.2 fast on Fireworks, and I switch between them without changing anything else about the workflow.

## The model and the shell are commodities

A year ago I would have had a strong opinion about which model to use.
Now the models are close enough that the choice is mostly about latency and price, which is why I let the environment pick: z.ai at home, Fireworks at work.
**The model stopped being the lever once the models got good enough to follow a well-specified workflow reliably.**

The same is true of the agent shell.
Cursor, VS Code, OpenCode, and Claude Code can all read a repository, edit files, and run commands, and because the skills follow an open format they run in any of them unchanged.
I use several of them because they are good at different things, but I do not expect any one of them to be the source of my advantage.
The shells will keep improving, the models will keep swapping in, and my workflow should not have to move when they do.

## The skills are the workflow

Everything that matters lives in [tomzx/agents](https://github.com/tomzx/agents), a library of composable skills written in the open [Agent Skills](https://agentskills.io) format.
A skill is a self-contained `SKILL.md` with step-by-step instructions for one repeatable task.
A compatible agent discovers skills by name, loads them on demand, and invokes them as slash commands like `/create-pr`, `/review-pr`, or `/end-day`.

The backbone is the SDLC pipeline.
A high-level skill like `/sdlc` orchestrates dozens of focused sub-skills into a full path from issue creation through requirements, specification, plan, implementation, tests, pull request, review, documentation, and learnings.
Each sub-skill is small enough to read in a minute and to improve independently.
**When I improve the `review-pr` skill, every flow that calls it gets the improvement, and I never have to re-explain that step to a session again.**

This is the difference between prompting and engineering a workflow.
A prompt is a one-off conversation.
A skill is the same conversation, written once, versioned, reviewed, and incrementally improved.
The agent performs it the same way every time, and the library gets better as the workflows mature.

## Where the human time goes

The SDLC pipeline is long, but my time is not spread evenly across it.
Almost all of my attention goes to the top: needs, requirements, and specification.
This is where defects fan out the widest and where fixes compound the longest, as [Defects Flow Downstream](../defects-flow-downstream/index.md) lays out, and it is where the work stays irreducibly human, deciding what to build and what "done" means.
A precise specification is the input every downstream skill consumes, and [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) argues it is now the highest-leverage skill in the field.

Everything below the specification, I automate as far as I can.
The plan, the implementation, the tests, the PR description, the review, the deployment, each is a skill the agent runs, and each is a place I would rather spend a token than an hour.
Once judgment is encoded into the layer every change passes through, fighting over each unit of output by hand stops paying for itself.

The downstream hour that used to go into reading diffs goes somewhere else entirely: into building high-fidelity test environments that approximate the production environment as closely as I can get them.
**I would rather spend an hour making the test environment catch the bug than an hour reading a diff hoping to catch it myself, because the test environment runs on every future change and the diff reading runs once.**
This is the trade [Verifying Code Without Reading It](../verifying-code-without-reading-it/index.md) and [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) both argue: review is a one-time signal, verification against a production-like environment is a compounding one.

## The encoding loop

The hardest problem with any workflow is not doing it.
It is remembering to do it, every time, in the right order, without skipping the boring step.

My rule is simple.
**Every time I catch myself remembering to do something, that is a skill that should exist.**
The reminder to check for an existing PR before starting work, the instinct to link an issue to its plan, the habit of running the linter before committing, the reflex to write a learnings note after a painful bug, each of these was once tacit knowledge that lived in my head and showed up only when I was fresh.
Now each one is a skill, and the agent runs it whether I am fresh or not.

The trigger is the remembering itself.
If I had to remember it, the agent should not have to.
Encoding it converts a forgettable step into a reliable one, and a reliable one into an improvable one, because once the step is written down I can see it, review it, and make it better instead of re-deriving it from memory every session.

## What changes when the workflow is versioned

Once the workflow lives in a repository, three things become true at once.

First, it is reliable.
The agent triages the issue, plans the work, reviews the PR, and closes the loop the same way today as it did yesterday, because the steps are written down and not reconstructed from vibes.

Second, it is improvable.
When a step is weak, I edit one file and every session that passes through it gets better.
The compounding is real in a way that prompting never compounds, because the improvement is captured instead of evaporating.

Third, it is shareable.
The skills are public, so anyone on my team or on the internet can run the same workflow against their own repository.
**The workflow became an artifact I can hand to someone else, which is the test for whether you actually have a workflow or just a habit.**

## What I expect to keep

If you asked me which parts of this setup I will still be using in two years, the answer is easy.
Not Cursor, probably not OpenChamber in its current form, and almost certainly not GLM 5.2.
The models and the shells are moving targets, and betting on any specific one is a bet against the field.

The skills are the part I expect to keep, but I do not expect to keep them as they are today.
They will evolve, and the more interesting bet is that they will shrink.
Every skill exists to encode a judgment the model cannot yet make reliably on its own: when to check for a duplicate PR, what a good acceptance criterion looks like, which steps belong in a retrospective.
As the models get smarter, often smarter than me at the specific subtask, those judgments stop being mine to encode and start being the model's to make.
The skill for them becomes redundant and gets deleted.

What persists is the slower-moving part: how I decide what is worth working on, how the phases of a feature connect, where the human checkpoint belongs.
The tactical skills will collapse into the model.
**The skills are not a fixed asset I am accumulating; they are a temporary scaffold for the gap between what the model can do today and what it will do on its own tomorrow, and a good chunk of the work is knowing which scaffold to take down next.**

## See also

- [Defects Flow Downstream](../defects-flow-downstream/index.md) - why the hour at the specification pays back more than the hour at any later stage
- [Verifying Code Without Reading It](../verifying-code-without-reading-it/index.md) - the case for spending review time on a production-like test environment instead of a diff
- [llm-augmented-workflows](../llm-augmented-workflows/index.md) - the engine that runs these skills on GitHub events without a human in the loop
- [The Self-Evolving Repository](../the-self-evolving-repository/index.md) - the end state when every maintainer function is encoded as a loop
- [The Codebase Gardener](../the-codebase-gardener/index.md) - why the layer everyone passes through is where you fight for consistency
- [Managing Many Concurrent LLM Agent Sessions](../managing-many-llm-agent-sessions/index.md) - the supervision problem OpenChamber solves and skills externalize
- [AI tools I have used](../ai-tools-i-have-used/index.md) - the running list of tools, kept up to date

## References

- [Mathieu Larose, "My AI Coding Workflow"](https://mathieularose.com/my-ai-coding-workflow) - the article that prompted me to write this one
- [tomzx/agents](https://github.com/tomzx/agents) - the skills library that is the subject of this article, public and installable
- [Agent Skills format](https://agentskills.io) - the open skill format that makes the library portable across agents
- [OpenCode](https://opencode.ai) - the terminal coding agent the skills target
- [OpenChamber](https://github.com/btriapitsyn/openchamber) - the OpenCode-native control room for parallel sessions
- [Cursor](https://www.cursor.com/) - the editor I use at work for reading and small edits
- [VS Code](https://code.visualstudio.com/) - the editor I use at home for reading and small edits
- [z.ai](https://z.ai) - provider of GLM 5.2, my home model
- [Fireworks](https://fireworks.ai) - provider of GLM 5.2 fast, my work model
