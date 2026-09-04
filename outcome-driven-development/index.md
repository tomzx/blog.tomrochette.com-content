---

title: "Outcome-Driven Development: Manage the Outcome, Not the Agent"
created: 2026-08-21
type: post
status: draft
tags: [software-engineering, ai-agents, llm, planning, management, fully-ai-generated, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader already delegates work to LLM coding agents and participates in planning rituals like backlogs, tickets, and standups. No introduction to what an LLM agent is.
agent_sessions:
  - ses_fdd9894fbffeS4T6CUVFkbRybU
---

Software development has spent fifty years managing work as effort.
Tickets, story points, standup reports, review throughput: every one of those signals measures how much human activity a piece of work consumed.
**When the executor is an LLM agent, activity stops being scarce, and every signal built on it stops meaning anything. The only interface worth maintaining between you and the work is the outcome: a state of the world you can check.**

I keep watching teams run agents through rituals designed to steer humans.
The rituals fail the same way every time: the volume of activity explodes, the measurements say everything is going wonderfully, and the world gets better much more slowly than the burndown chart claims.
The problem is not the agents.
The problem is that effort was never the point, it was just the only thing we could afford to observe.

## Effort Was the Interface

For most of software history, the expensive part of a task was the human attention required to execute it.
So we built management around effort.
We decomposed features into day-sized tickets because a person loses the thread at month scale.
We counted story points because person-hours were the budget.
We held standups because the cheapest way to observe progress was to ask the human performing it.
We reviewed diffs because the human producing them was the most expensive and least consistent component in the system, and review was quality control applied to that scarce component.

None of that was wrong.
**Task decomposition was not a design preference, it was a workaround for the bandwidth of the machine doing the work, and the machine was a person.**
Managing by outcomes was always the stated ideal, from [management by objectives](https://en.wikipedia.org/wiki/Management_by_objectives) through [OKRs](https://en.wikipedia.org/wiki/OKR), but observing outcomes per unit of work was expensive, so day to day we steered activity and treated outcomes as a quarterly summary.

## Agents Break Every Effort Signal

An agent produces activity at near-zero marginal cost.
Given a backlog, an agent burns down every ticket in it and opens fifty pull requests before lunch, and each pull request looks like a morning of human work.
The moment that is true, every activity-based measurement becomes a [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law) casualty: when a measure becomes a target, it stops measuring.
Tickets closed, points burnt, pull requests merged, lines written: an agent maximizes all of those numbers while contributing nothing to what the numbers were supposed to stand for.

A second break is quieter.
The route stopped being informative.
When a human executes, the diff is a record of scarce decisions, and reading the record audits the decisions.
When an agent executes, routes are cheap and effectively unbounded, and auditing the route means auditing an endless stream of plausible diffs.
The destination is the only thing left worth auditing.

The delegation problem also becomes literal.
Economists call the arrangement where a principal hands work to an agent with different incentives the [principal–agent problem](https://en.wikipedia.org/wiki/Principal%E2%80%93agent_problem), and the usual defense is contract design.
An LLM agent is that problem with the names turned literal: the agent optimizes the letter of your instruction, not the state of the world you hoped the instruction would produce.
**The contract is the only thing you control, so the contract has to be the outcome, stated as something checkable.**

## What Counts as an Outcome

An outcome is a checkable state of the world, and it has three parts: an observable delta (what becomes true), a verifier (how the delta gets checked by something independent of the producer), and a budget (what the delta may cost in time, tokens, or money).

The definition does the real work when you apply it to ordinary tickets.

"Refactor the auth module" is an activity.
The outcome version says: a new caller can be added without touching more than two files, and the boundary check in CI enforces that from now on.
"Fix the login bug" becomes: the reproduction script fails before the change, passes after it, and stays green in CI.
"Make search faster" becomes: p95 latency of the search endpoint under the recorded load test drops below 200 ms, checked nightly.

The test is always the same three questions.
What becomes true?
How would I check?
What may it cost?
**If you cannot answer all three, you did not write an outcome, you wrote a task or a wish, and a wish handed to an agent comes back as a plausible-looking diff with nothing behind it.**

There is a boundary to respect here, and I drew it in [The Acceptance Gap](../the-acceptance-gap/index.md): the objective half of what you want can be encoded as a check, and the taste half cannot, because taste is a reaction you have not had yet.
Outcome-driven development covers the objective half.
The taste half still closes through fast iteration and a human saying "good enough, ship it".

## Delegation Changes Composition

Handing work to an agent stops being a prompt and becomes a contract with four fields: the outcome statement, the verifier, the budget, and the invariants, the short list of global constraints that hold for every change, dependency direction, blast radius limits, license rules.
The agent picks the route.
You stop reviewing routes and start reviewing destinations, using exactly the verification machinery I described in [Verifying Code Without Reading It](../verifying-code-without-reading-it/index.md): checks and critics per property, run on every change, no human reading diffs.

What remains for the human concentrates at the ends of the pipeline.
Deciding which outcomes are worth pursuing at all, which is the bottleneck that moved upstream, as [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) keeps showing.
Writing outcomes and verifiers, which is specification work, and specification is now the highest-leverage skill on the team.
Maintaining the invariant list.
And accepting the result, which stays human for the taste half forever.

[Zero Touch Engineering](../zero-touch-engineering/index.md) is the limit case of the same structure.
When the outcome and the verifier are fully specified, the loop from an observed signal to a deployed fix needs no human in the path.
The humans in a zero-touch system are not gone, they are the ones specifying which outcomes the loop pursues.

## Three Ways It Fails

The first failure is outcome laundering: relabeling tasks as outcomes and changing nothing else.
"Have the agent refactor the module" is not an outcome, it is the old ticket with a new verb.
Run the three-part test on anything labeled an outcome, and if no verifier exists, the label is decoration.

The second failure is narrow outcomes.
An agent that satisfies the letter of each outcome while degrading everything the outcome did not measure will pass every check and still leave the system worse, which is [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law) operating one level up.
Maintainability, consistency, and the load on future readers do not compress into any single task's outcome, which is why the invariant list exists, and why someone must own the whole system rather than the sum of the outcomes, the question [Who Maintains the Slop?](../who-maintains-the-slop/index.md) asks from the inheritor's side.
**Each outcome achieved, and the codebase still worse, is the signature of a team that delegated outcomes but never wrote invariants.**

The third failure is abdication.
One of my standing principles: when you outsource an outcome, you also outsource the decisions that produce it.
Delegating execution is leverage only if the person who owned the outcome still owns it after the delegation, keeps the verifier independent, and answers for the result.
Delegation without retained ownership does not produce leverage, it produces an accountability gap with a queue in front of it.

## What to Do Next

Rewrite the top ten items of your backlog as outcomes.
State the delta, name the verifier, set the budget, and treat anything that fails the three-part test as a step inside an outcome rather than an outcome itself.
Expect the rewrite to be slow the first time, because you are writing down, for the first time, what "done" was always supposed to mean, the same externalization [When the Same Ticket Means Different Work](../when-the-same-ticket-means-different-work/index.md) demands at planning time.

Retire your activity metrics.
Replace tickets-closed and points-burnt with outcome yield: outcomes accepted per week, per dollar, per retry.
When a verifier fails, send the work back to the agent instead of fixing the diff by hand, because a human who repairs failed agent output has quietly become the review queue again.

Write the invariant list once, as a team, and enforce it in CI on every change, agent-made or not.
Then review outcomes on a cadence, not diffs on a stream.

The old status question was "what did you work on this week".
The new one is "what is true now that was not true before, and what checked it".
**Effort was the currency when humans executed. Outcomes are the currency when agents do. Manage what you can check, and let the route belong to the machine.**

## See also

- [The Acceptance Gap](../the-acceptance-gap/index.md) - the split between the objective half of a goal, which outcomes can encode, and the taste half, which only iteration closes
- [Verifying Code Without Reading It](../verifying-code-without-reading-it/index.md) - the machinery that verifies outcomes without any human reading diffs
- [When the Same Ticket Means Different Work](../when-the-same-ticket-means-different-work/index.md) - why scope boundaries must live in the written work item, of which the outcome statement is the sharpest form
- [Zero Touch Engineering](../zero-touch-engineering/index.md) - the limit case where a fully specified outcome and verifier remove the human from the path entirely
- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) - the team-scale version: outcome-level planning replacing granular estimation

## References

- [Wikipedia, "Goodhart's law"](https://en.wikipedia.org/wiki/Goodhart%27s_law) - why every effort-based signal collapses once agents can maximize it for free
- [Wikipedia, "Principal–agent problem"](https://en.wikipedia.org/wiki/Principal%E2%80%93agent_problem) - the incentive framework behind contract-first delegation to something that optimizes the letter of your instruction
- [Wikipedia, "Management by objectives"](https://en.wikipedia.org/wiki/Management_by_objectives) - the Drucker lineage of managing by outcomes rather than activity, decades before observation got cheap
- [Wikipedia, "OKR"](https://en.wikipedia.org/wiki/OKR) - the modern descendant of objective management, effective exactly to the degree its key results are checkable
- [Wikipedia, "Outcome-driven innovation"](https://en.wikipedia.org/wiki/Outcome-driven_innovation) - the product-side use of the same word, where outcomes describe customer progress rather than system state
