---
title: "Scaling Yourself Horizontally: Attention Does Not Scale, Leverage Does"
created: 2026-08-25
type: post
status: finished
tags: [ai, software-engineering, llm, agents, productivity, scaling, leverage, fully-ai-generated, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader is a software engineer who already automates some of their own work and has started to wonder where their personal ceiling is. Comfortable with delegating to LLM agents; no introduction to LLMs here.
---

Every engineer I know eventually hits the same wall: the amount of valuable queued work exceeds the hours in a day.
The instinct is to scale vertically, to work longer, read faster, and switch contexts harder.
That direction has a hard ceiling, and the ceiling is low.
**When you cannot scale vertically, you scale horizontally: you build systems that do things for you.**
The resource everyone names as the unscalable one is attention, and I want to push on that claim, because attention is only half the story.

## Scaling Vertically Ends Early

Scaling vertically means adding capacity to the node itself: more hours, more speed, more skill.
The day has twenty-four hours, working memory holds a handful of items at once, and energy refills at a fixed rate.
You can buy maybe two or three times more effective attention by sleeping properly and working in focused blocks, which is real but constant-order.
No amount of discipline buys a tenth of you.
**Vertical scaling tops out around a factor of two; everything past that has to come from replication.**

Scaling horizontally means adding nodes instead of upgrading one.
A node is a system that acts on your behalf while you are absent: a check, a script, a runbook, an agent, a colleague you taught.
The question stops being "how do I do more" and becomes "what can act as me without me".

## A System Is a Decision Made Once

The obvious move is to automate tasks, the repetitive stuff.
That is the low-grade version of scaling horizontally.
**What you are actually doing is building systems that make decisions you would otherwise make by hand, so that each decision gets made once instead of each time.**
A lint rule is a preference of yours, enforced on every change.
A runbook is a decision procedure captured at the moment you understood the system best.
A specification is your intent, written down once and executed against many times.
An agent skill is a whole procedure of yours, replayable at any hour, in any number of instances.
A colleague you coach is the most expensive system of all, the only one that eventually outgrows your judgment.

Andy Grove did the accounting decades ago in [High Output Management](https://en.wikipedia.org/wiki/High_Output_Management): a manager's output is the output of their organization plus the output under their influence.
The same math applies to any engineer with systems.
**Your output is what you produce directly plus what your systems produce in your absence.**

Building systems is an old menu: teach, hire, document, automate.
What changed is the cost of building one.
Teaching a person takes months and produces one system that generalizes.
Writing an agent skill takes an afternoon and produces unlimited instances that never generalize.
Cheap narrow systems for procedures, expensive general ones for judgment, and the current game is knowing which decisions belong in a system and which must stay with you.
The scheduled tasks in my own repositories already work this way: triage, review, and daily curation are systems built out of decisions I once made manually, and they do not sleep.

## The Most Expensive System

One item on that list behaves differently from all the others.
A person you coach is the most expensive system to build and the only one that eventually outgrows your judgment.
**Every other system can only replay decisions you already made, so none of them can tell you that you are wrong.**

The economics push the cheap layers toward machines.
Teaching a machine your preferences takes an afternoon; teaching a person takes months.
The rote layer of teaching, conventions, procedures, mechanics, migrates to machines for the same reason generation did: the cheap system wins on cost.
What cannot migrate is the point of the expensive one.
A person generalizes to situations you never saw, dissents when you are wrong, and eventually holds taste decisions in your stead, and no skill file does any of the three.
**Teaching people does not disappear; it moves up, from transferring procedures to growing judgment.**

The risk runs the other direction.
Judgment grows only through contact with real problems, and apprenticeship was where most people got that contact.
If everyone teaches machines their current preferences and nobody teaches people, the supply of judgment that the next generation of systems is built from depletes.
**Cheap systems consume the very training ground that produces the general ones.**

## So Does Attention Scale or Not?

The claim I keep hearing, including from myself, is that attention is the only resource you cannot really scale.
Three answers, in increasing order of usefulness.

In quantity, no.
The stock is fixed: one serial consciousness, a small working memory, a day that does not extend, and a decision pipe that handles one thing at a time ([Attention Engineering](../attention-engineering/index.md) covers what that means in practice).

In quality, slightly.
Focus, sleep, and single-tasking buy a real multiplier over a frazzled baseline.
That factor of two is worth claiming, and almost nobody has claimed it.
But a constant is not a curve.

In leverage, without bound.
**Attention is the only resource you cannot scale in quantity, and the only one whose yield per unit is unbounded.**
A test attends so that you do not have to; verification substitutes for supervision.
A check written once removes a minute of checking on every future use, forever.
A system built this year raises the return on every hour of attention you will ever spend afterward.
The attention itself does not compound.
The artifacts do, and the artifacts all live outside your head.

What never scales is the deciding itself.
You can multiply what a moment of attention produces, but the moment of judgment, the taste call on whether a thing is good enough, stays serial and stays yours, which is [the acceptance gap](../the-acceptance-gap/index.md) restated as a scaling law.
So the precise version of the claim reads: attention does not scale, and that is exactly why the work is to stop spending attention on anything a system could check.

## Scaling Horizontally Fails in Four Known Ways

Replication looks like a free lunch, and the bill arrives on a delay.

**Systems drift.**
Every system is a snapshot of the decisions you made when you built it, and the world moves on.
The runbook rots, the skill goes stale, the gate blocks a pattern that was bad two years ago and is idiomatic now.
Someone has to tend the systems, and that someone is you, the maintenance burden [The Codebase Gardener](../the-codebase-gardener/index.md) describes.

**Errors correlate.**
A flaw in a system's decisions repeats on every execution, in every instance, at once.
A thousand agents running the same flawed instruction produce a thousand instances of the same mistake, which is why consistently wrong is a worse failure mode than inconsistently right ([Scaling the LLM Agent Company](../scaling-the-llm-agent-company/index.md)).
At that point you are not scaling your throughput; you are scaling your error surface.

**The job converts.**
Scale horizontally far enough and you stop being the producer and become the governor of a system of producers.
Attention moves from doing the work to reviewing outputs, pruning systems, and deciding what to build next.
The constraint did not disappear; it moved up to you, the textbook behavior of a system under the [theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints).
Govern badly and you industrialize your own mistakes at a speed no hand-made error ever reached.

**The source depletes.**
Your judgment is the raw material the systems are built from, and judgment regenerates only through contact with real problems.
Automate away all the doing and you cut off the supply of experience that made your systems worth building, the terminal worry of [The Shifting Bottleneck](../the-shifting-bottleneck/index.md).
**The systems are only as good as the freshest judgment that went into them, so a slice of attention must stay spent on hands-on work even when a system could do it.**

## Review the Result, Not the Change

Code review is where misallocated attention is easiest to see, so let me be specific about it.
When a change arrives, the reflex is to open the diff and read the implementation.
**The question that deserves your attention is not what the change looks like but what it resulted in: the failing test that now passes, the before-and-after recording, the benchmark that moved, the error rate that dropped.**
The implementation is how the result was produced, and the how is increasingly the machine's business.

Concretely, this means review discussions argue about outcomes: what the change does to behavior, to latency, to failure modes, to the rollback path.
Style and implementation details are preferences, and preferences belong in the gates, where they run on every change instead of when a reviewer remembers to mention them ([Verifying Code Without Reading It](../verifying-code-without-reading-it/index.md) builds the full system).
Read the diff itself only when the evidence is missing or the blast radius is large, the classification [The Merge Gate](../the-merge-gate/index.md) argues for.
And when the evidence is missing, treat that absence as the review finding, rather than reconstructing the answer by reading the code.

This is how one serial consciousness survives a fleet of producers.
You audit results and sample implementation, because the day you read every diff is the day the systems outproduce your review capacity ([You Are the Bottleneck](../you-are-the-bottleneck/index.md)).

## What to Do Next

Audit the last two weeks of your work and list every recurring manual action.
Anything done three times or more is a system waiting to be built, and the order matters: gates and skills first, one-off scripts second, docs third, memory last, because the earlier items compound and memory evaporates.

Prefer systems with an oracle.
Automate the checkable, where correctness can be tested mechanically.
The taste decisions, whether a thing is good enough or should exist at all, have no oracle and stay yours, so give them protected time on your calendar instead of letting them be squeezed out by reviewing more output.

Spend the freed attention upstream, on specifications and on deciding what should exist at all, not on reviewing more output faster.
That reallocation is the entire point of scaling horizontally, and [You Are the Bottleneck](../you-are-the-bottleneck/index.md) is what happens when you skip it and let the systems outproduce your review capacity.

Keep a deliberate budget of attention that never gets handed to a system: the taste decisions, plus enough hands-on work to keep your judgment regenerating.
You are protecting the seed stock, not being inefficient.

Then measure yourself in output per unit of attention, not in hours, tasks, or sessions spawned.
The number that defines a scaling engineer is how much ships per hour of focused judgment.

You will never get more of yourself.
**What you can decide is how many systems run without you, how fresh their decisions stay, and what the one serial consciousness behind all of them spends its scarce attention on.**

## See also

- [Attention Engineering](../attention-engineering/index.md) - the tactical layer of this argument: how to allocate the fixed attention across an agent workflow instead of wasting it on generation
- [The Apprentice Problem](../the-apprentice-problem/index.md) - the pipeline consequence of teaching machines instead of people: where new judgment comes from once the junior work is automated
- [You Are the Bottleneck](../you-are-the-bottleneck/index.md) - what happens when generation scales but acceptance does not, and the contract that drains the review queue
- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - the pattern behind source depletion: automating a layer moves the constraint to the layer above
- [Solo Is a Team Size](../solo-is-a-team-size/index.md) - the seat-by-seat version of the same question: which roles need a general copy of judgment (a human) and which need a narrow one
- [Scaling the LLM Agent Company](../scaling-the-llm-agent-company/index.md) - the organizational version of replication and its failure modes, correlated errors first among them
- [The Codebase Gardener](../the-codebase-gardener/index.md) - the maintenance cost of these systems: why they need tending or they rot
- [The Acceptance Gap](../the-acceptance-gap/index.md) - where the taste decision lives and why it stays with you when everything else has been copied

## References

- [Andy Grove, "High Output Management" (Wikipedia)](https://en.wikipedia.org/wiki/High_Output_Management) - the leverage accounting: your output includes everything your organization and your influence produce
- [Theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints) - why elevating a constraint moves it instead of removing it, the mechanism that turns a scaling engineer into a governor
- [Cognitive load](https://en.wikipedia.org/wiki/Cognitive_load) - the research grounding why the quantity of attention is a fixed stock
