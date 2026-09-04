---

title: "Three Gaps My SDLC Pipeline Hit on a Machine Learning Platform"
created: 2026-08-23
type: post
status: draft
tags: [ai, software-engineering, sdlc, llm, ai-agents, workflow, partially-ai-generated, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader runs coding agents against a structured development process and is comfortable with SDLC vocabulary (requirements, specification, plan). No introduction to what an LLM is.
agent_sessions:
  - ses_fd2f78383ffe3VcpPx2zprr1Vk
---

I have been building a machine learning platform with my SDLC skills driving the agents, from needs assessment through specification to implementation.
The pipeline itself held up better than I expected.
**What broke were three assumptions the pipeline makes about how I work: that I work on one thing at a time, that one change touches one place, and that I stay in the loop for every step.**
A real platform, with many commands and many interlocking parts, violated all three assumptions within weeks.

## The setup

The platform is [TomzxCode/ml-platform](https://github.com/TomzxCode/ml-platform), a set of commands, the usual suspects for machine learning work: training, evaluating, promoting models, and so on.
Following the [SDLC pipeline](https://github.com/tomzx/agents/tree/main/skills/sdlc), each command got its own feature directory holding its needs assessment, requirements, specification, and plan.
A skill per phase walks an agent through the artifacts, and I review at the boundaries.
On a small project this flow feels complete.
On the platform, the number of features and the connections between them exposed the three gaps below.

## Ideas do not wait for the current task

The first gap showed up immediately.
While designing one command, I would notice what another command should be, or what a shared piece needed, and the new idea would start competing with the work in front of me.
The mechanical answer is to fork: capture the idea in a new session, point the agent at a fresh feature directory, and return to the original task.
[OpenChamber](https://github.com/btriapitsyn/openchamber) makes forking cheap because sessions are branchable.

But forking surfaced the deeper problem.
**A forked session inherits a snapshot of the artifact tree, while the sessions around it keep changing the tree underneath it.**
The forked agent works from requirements that are already stale, and neither session knows the other exists.
My SDLC skills treat the `.sdlc/` directory as fixed input, read once at session start.
What the skills need instead is awareness that the tree is moving: record the point each session forked from, and have every phase skill re-read what changed in the relevant artifacts since that point before acting.
Sibling work should arrive as an input, not as a surprise at review time.

## One change means several files must change

The second gap is about the artifacts themselves.
Changing one part of the platform meant files in other parts had to change too: a revision to one command's specification forces updates in the requirements and plans of the commands that consume what the first command produces.

My skills already have two mechanisms adjacent to the problem, and neither one is the missing piece.
[backpropagate-sdlc](https://github.com/tomzx/agents/tree/main/skills/backpropagate-sdlc) walks the artifact chain in reverse, from code back to the requirement that motivated it, which verifies consistency after the fact.
[sync-sdlc](https://github.com/tomzx/agents/tree/main/skills/sync-sdlc) regenerates artifacts wholesale when the code drifts from them.
**What is missing is forward propagation: when an artifact changes, the artifacts that depend on the changed artifact should update as part of the same motion, not be discovered stale later.**

The fix I am converging on is a dependency diagram that the files themselves carry.
Each artifact declares what the artifact depends on, in a small [mermaid](https://mermaid.js.org/) block that renders in review and stays readable for agents, the same pattern I described in [Agent Skills That Render](../agent-skills-that-render/index.md).
A propagation skill then follows the edges and updates the affected files, or raises a question where the update needs a decision.
The diagram is documentation for me and a worklist for the agent at the same time.

## The features outnumber my attention

The third gap is the one I feel the most.
Creating a feature directory per command was cheap; I seeded each one with everything known so far and moved on.
The expensive part came next: the pipeline needed me to walk each feature, one by one, through its design iterations, and there are more features than I have hours.
**The bottleneck stopped being the work and started being my personal traversal of the work.**

What I want instead is ownership.
An agent, or a set of agents, that takes each feature directory as the directory stands and starts iterating: refine the requirements, draft the specification, surface the open questions, and come back only at the gates that need a human decision.
The unit of delegation moves from the task ("write the requirements for X") to the feature ("take X as far as you can").
Each owning agent still passes through the same phase skills and the same gates, so autonomy is capped at the decision points rather than removed.
This is the [self-evolving repository](../the-self-evolving-repository/index.md) idea scaled down to one feature at a time, with the gates kept in place.

## Three symptoms of one problem

The gaps look separate, but the gaps share a root.
The pipeline is serial and human-paced: one session, one artifact at a time, one human reviewing each step.
The platform is parallel: sessions multiply, artifacts depend on each other, and the feature count exceeds my throughput.
**The fix in all three cases is to make the artifact tree the coordination medium, so agents synchronize through the files and the dependency graph instead of through me.**
Fork awareness is agents reading each other's changes; propagation is agents updating each other's files; ownership is agents driving each other's features.
I move from being the scheduler to being the reviewer at the gates.

## What to Do Next

If you run a similar pipeline against a project with many features:

- Record where each session forks from, and make the phase skills diff the artifact tree since that point before the skills act.
- Add a dependency declaration to each artifact, and a propagation step that follows the edges when an artifact changes.
- Pick one feature directory as the template, dispatch an owning agent per remaining feature, and let each agent run to the next human gate.
- Measure how far each feature gets before the feature needs you; the distance tells you where the real gates are.

## See also

- [My AI Workflow](../my-ai-workflow/index.md) - the workflow this stress test ran on, and where the human time was supposed to go
- [Managing Many Concurrent LLM Agent Sessions](../managing-many-llm-agent-sessions/index.md) - the supervision problem that session forking amplifies
- [Agent Skills That Render](../agent-skills-that-render/index.md) - mermaid in SDLC artifacts, the carrier the dependency diagram would ride on
- [The Self-Evolving Repository](../the-self-evolving-repository/index.md) - the end state when feature ownership runs without a human in the loop
- [I Specify Open Source Projects I Don't Maintain](../i-specify-open-source-projects-i-dont-maintain/index.md) - the workspace where sync-sdlc keeps artifacts current, the precedent for propagation

## References

- [TomzxCode/ml-platform](https://github.com/TomzxCode/ml-platform) - the machine learning platform whose feature tree exposed the three gaps
- [SDLC skill](https://github.com/tomzx/agents/tree/main/skills/sdlc) - the pipeline that produced the artifacts this article is about
- [backpropagate-sdlc](https://github.com/tomzx/agents/tree/main/skills/backpropagate-sdlc) - the reverse consistency walk that forward propagation would complement
- [sync-sdlc](https://github.com/tomzx/agents/tree/main/skills/sync-sdlc) - the drift-detection pass that regenerates artifacts wholesale
- [OpenChamber](https://github.com/btriapitsyn/openchamber) - the branchable session surface that makes forking cheap
- [Mermaid](https://mermaid.js.org/) - the diagram syntax the dependency declarations would use
