---
title: "The Codebase Gardener: Keeping a Codebase Sane When Teammates and Their Agents Pull in Every Direction"
created: 2026-06-20
type: post
status: finished
tags: [ai, software-engineering, llm, code-review, tech-debt, productivity, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader is an engineer on a team where LLM coding agents do most of the producing, and that they have at least seen a CI pipeline, a lint config, or a "skill"/"rule" file. No explanation of what an LLM is.
---

You cannot review your way to a sane codebase when the code is being produced faster than you can read it.
This is the new arithmetic of the LLM era, and it is brutal for the one engineer on the team who cares about consistency.
**The strategy that actually works is to stop fighting at the pull request and start fighting at the layer everyone, and every agent, is forced to pass through.**

## The Math Changed Under Us

For most of software history, one careful engineer could hold a codebase together by reviewing most of what landed in it.
The volume was human.
A teammate produced code at roughly the rate you could read it, and a determined reviewer could keep the drift in check.
That equilibrium is gone, and two things killed it.

First, throughput.
A teammate driving an LLM agent now opens in an afternoon the pull requests that used to take a week.
The unit of work did not change; the rate at which units appear did.

Second, plurality.
Each teammate may be driving a different agent, loaded with different skills, different conventions, a different mental picture of what "good" means for this codebase.
The codebase does not converge on a single style through argument anymore.
It fragments into as many dialects as there are agents producing it, and each dialect looks plausible, because plausibility is exactly what an LLM optimizes for.
A function can be internally coherent, consistent with nothing around it, and wrong about the domain all at once.

You, alone, reading diffs, are now the slowest station in a pipeline that was designed to outrun you.
**Per-unit review scales linearly with your hours, and the entropy is being produced exponentially.**
No amount of discipline closes that gap.

## Reviewing Harder Is the Trap

The instinct of the engineer who cares is to review more, longer, more strictly.
This is exactly the wrong move, for reasons I laid out in [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md).
Every hour you spend line-editing someone else's agent output is an hour the next three pull requests go unread.
You become the bottleneck, and bottleneck reviewers do not stay bottleneck reviewers for long.
Teammates start tagging each other for approvals, slicing changes to slip under your threshold, or simply waiting you out until you tire.

You end up exhausted, quietly resented, and still losing ground to the codebase.
The worst part is that the work feels virtuous while you do it.
Catching a misnamed variable in review feels like defending the standard.
It is not.
It is fighting a single ember while the forest is on fire.

**Review is a per-unit activity, and per-unit activity cannot match entropy that is being produced faster than you can read it.**
If your entire strategy is "I will catch the problems at review," the strategy has already lost.
The question is not how to review better.
The question is how to make most of the review unnecessary.

## Move the Leverage From Review to Infrastructure

The way one person defends a codebase against many producers is to stop operating on the units and start operating on the system that produces them.
This is the [theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints) applied to code quality: if you cannot keep up at the review station, do not add more reviewers.
Change the station.

Concretely, it means every standard you care about has to live in the one of the few places work is forced to pass through, rather than in your head or in your review comments.
There are only a handful of such places, and together they are the entire leverage surface available to a single engineer.

The skill and rule files every agent loads at the start of a task.
The CI gates every pull request must clear before it can merge.
The templates and scaffolds every new module begins from.
The default configuration the linters, formatters, and analyzers ship with.
The hooks that run on commit, on push, and on merge.

If your standard is encoded in any of these, it executes on every change, forever, without you being present.
**If it lives only in your review comments, it executes only when you are awake, looking, and willing to argue about it.**
That is the whole difference between a standard and an opinion.
A standard runs whether or not anyone agrees with it.
An opinion dies the moment you go on vacation.

This is the same point made, from the team's perspective, in [Bringing Everyone to the Same Level](../bringing-everyone-to-the-same-level/index.md): the senior engineer's edge was always a process they ran in their head, and a process in a head does not scale.
Here the stakes are higher, because you are not trying to lift the team to your level.
You are trying to hold the line while the team is actively, if innocently, pulling away from it.
The mechanism is the same.
Encode the process, and let the encoding do the defending.

## Make the Right Thing the Path of Least Resistance

Most code in a codebase is the way it is because that was the easiest thing to type at the time.
This is a feature, not a bug, for someone trying to steer a codebase alone.
If the easiest path also happens to be the correct path, conformity is free, and nobody has to be persuaded of anything.

This is the [paved road](https://en.wikipedia.org/wiki/Paved_road) idea, and it is the single highest-leverage intervention available to a solo defender.
You do not get compliance by arguing for it.
You get it by making the compliant thing the thing that happens when nobody is thinking.

Ship a project template that already has the test harness, the lint config, the migration format, and the observability scaffolding wired in, and a teammate who spins up a new service produces conforming code by default, without ever reading your standards document.
Wire the migration linter into CI so that a non-backward-compatible migration fails to merge, and the question of whether backward compatibility is "our standard" stops being a question at all.
**Friction for the wrong thing, zero friction for the right thing.**
That asymmetry does more work than any amount of documentation, because it operates on the path of least resistance rather than against it.

The flip side matters just as much.
Remove friction from the behavior you want.
If you want small, reversible changes, make small changes trivially easy to merge.
If reviewing is expensive, people batch, and batching is exactly what produces the large, entangled, unreviewable pull requests that defeat you.
Tax what you want less of, and subsidize what you want more of, and do both in the tooling rather than in the standup.

## Invariants, Not Preferences

Most review wars never end because most of what people fight over are preferences.
Tabs versus spaces.
Single exit versus early return.
One assertion per test.
Preferences are arguable, and in an LLM-saturated codebase, arguable means unwinnable, because the other engineer's agent was told the exact opposite of what yours was told, with equal confidence.

The move is to convert as many preferences as possible into invariants before they can become arguments.
An invariant is a property the system will enforce whether or not anyone agrees with it.
Database migrations must be backward compatible.
New dependencies require an audit record.
Public API changes require a feature flag.
Cyclomatic complexity above a threshold fails the build.
These are not opinions.
They are [machine-checkable constraints](../rethinking-code-review-in-the-age-of-llms/index.md), and a constraint that a machine checks is a constraint you never have to argue about again.

Every preference you promote to an invariant is one fewer conversation you have to win, and one fewer place the codebase can drift while you are not looking.
Reserve your remaining human attention for the small set of things that genuinely cannot be encoded: taste, architectural direction, whether a feature should exist at all.
Everything else should be a gate or a default, silently doing the work you used to do by hand.

## Garden in Sweeps, Not in Diffs

Per-PR review is not the only way to fight decay, and in this era it is no longer even the best way.
Some drift will always get through, because no gate is perfect and because some of what rots a codebase is not visible in any single diff.
Naming conventions slide.
Duplication accretes.
A module that was clean in isolation becomes a knot once three teammates have each extended it in a different direction.

The answer is to operate the [Boy Scout rule](https://en.wikipedia.org/wiki/Robert_C._Martin) at the codebase level rather than at the commit level: run regular maintenance sweeps instead of trying to catch everything one pull request at a time.
Once a week, run the dead-code analysis.
Run the duplication detector and look at the new clusters.
Pull the complexity trend report and see which functions crossed a threshold this week.
Skim a list of newly added dependencies.

A sweep lets you fix the eighty percent of drift that no individual pull request would have surfaced, and it lets you fix it in a way that does not require winning an argument on each one.
You are not blocking anyone's work.
You are tidying, in batches, on your own time, against objective signals from the tools.
**The gardener does not follow every leaf as it falls.
The gardener rakes.**

This is also the honest acknowledgment that some entropy is the cost of speed, and that the goal is not zero drift.
The goal is a drift rate low enough that your weekly sweep net positive, so that over months the codebase gets cleaner rather than dirtier even as it grows.
A codebase that gets slowly cleaner under load is a codebase you are successfully defending.
A codebase that gets slowly dirtier no matter how hard you review is one you are losing, and the review is not the fix.

## Write the Decisions That Outlast You

One of the cheapest, highest-leverage things a solo defender can do is write things down in a form that survives without them.
[Architecture decision records](https://adr.github.io/), one page each, capturing what was decided, what alternatives were rejected, and why.
A short conventions document that is explicitly the source of truth the lint config is derived from.
A "why this exists" header on the modules most likely to be misunderstood.

The point of writing it down is not to win today's argument.
Today's argument will be re-litigated regardless, because the engineer on the other side, or their agent, has not read it.
The point is to ensure that the same argument does not have to be re-won from scratch every time, by you, in real time.

A decision that lives in a file is a decision the next agent can be pointed at.
A decision that lives only in your head dies the moment you switch teams, or take a week off, or simply get tired of explaining it for the fiftieth time.
When your defenses are encoded as files, the codebase keeps its shape without you holding it together.
When they are encoded only as your vigilance, the codebase is one two-week vacation away from drift you will spend a month undoing.

## Pick the Battles That Are Actually One-Way Doors

You cannot hold every line, and trying to is the fastest route to burnout.
The discipline is to decide, in advance, which fights are worth your scarce attention, and the useful frame is the distinction between one-way and two-way doors, which I wrote about in [When Engineers Disagree on Best Practices](../when-engineers-disagree-on-best-practices/index.md).

A one-way door is a decision that is hard or impossible to reverse.
Choosing a primary database.
Committing to a service boundary that will be expensive to move later.
Adopting a framework that will permeate every file.
Dropping a database column.
These deserve your full attention, and as the defender of the codebase these are where you should spend it.
Block them, slow them, write the decision record, make the team justify the trade-off.

A two-way door is a decision you can undo in an afternoon.
A naming convention.
A helper function in the wrong package.
A test that could have been structured better.
Let these go, or fix them in a sweep later.
**The solo defender who treats every diff as a one-way door exhausts themselves on reversible things and has nothing left for the decisions that actually compound.**

This is also the cure for the resentment that otherwise eats this role alive.
You will see things every day that are not how you would have done them.
Most of them do not matter.
Learn to feel the one-way doors in your stomach and let the rest pass, and you will last long enough to actually defend the things that count.

## The Honest Limit

Sometimes the team will not align, and no amount of infrastructure will fully save you.
A teammate may insist on driving their own agent with their own skills, their own conventions, their own picture of the codebase, and treat your paved road as a suggestion rather than a default.
A manager may value shipping velocity over every standard you have encoded, and quietly override the gates that matter.

At that point your job is no longer to win.
It is to make the cost of the drift visible.
Keep the trend reports.
Keep the complexity numbers.
Keep the record of which decisions were one-way doors that got walked through without the decision being made.
Do this not to build a case against anyone, but because the most powerful thing a defender can produce, when defense fails, is a clear record of what was lost and when, so that the next attempt at sanity starts from evidence rather than from vibes.

And know when to stop defending a particular front.
A codebase is not worth your health, and a team that has decided, collectively, to let the codebase rot will rot it with or without you.
Your leverage is highest at the start of a codebase's life and lowest once the rot is structural.
If you have encoded what you can, written down what you know, and the drift is still winning, the rational move is to spend less energy fighting and more energy deciding whether this is still the codebase you want to be responsible for.

## What to Do on Monday

You do not need permission, and you do not need a migration.
Pick the single standard that is being violated most often, the one that costs you the most review time, and convert it from a review comment into a gate.
A lint rule.
A CI check.
A line in the skill file every agent loads.
Run it on every pull request, including the ones you do not personally review.

Then do it again, next week, with the next most expensive standard.
Each conversion is a piece of vigilance that stops being yours and starts being the system's.
Over a quarter, the surface you have to defend manually shrinks to the small set of genuinely judgment-laden calls, and the volume of entropy you face stops mattering quite so much, because most of it is being caught upstream of you, by machinery that does not tire.

**The solo defender who wins is not the one who reviews the most.**
**The solo defender who wins is the one who has made themselves, slowly and deliberately, the part of the pipeline that is no longer strictly necessary.**

A sane codebase in this era is not one that a heroic reviewer holds together by force of attention.
It is one whose standards have been pushed so far upstream, into the skills and gates and defaults and templates, that the code arrives mostly correct, and the reviewer is left doing the small amount of work that only a human can do.
Build that, one encoded standard at a time, and the direction the rest of the team is pulling in starts to matter a great deal less.

## See also

- [Bringing Everyone to the Same Level](../bringing-everyone-to-the-same-level/index.md) -- the team-level argument for encoding senior engineers' processes into skills; this article is the adversarial, solo version of the same insight
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) -- the case that quality is a property of your constraints, not your reviewers, which is the premise the gardening strategy stands on
- [When Engineers Disagree on Best Practices](../when-engineers-disagree-on-best-practices/index.md) -- the one-way versus two-way door framing this article borrows for deciding which fights a solo defender should pick
- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) -- which friction is load-bearing and which is waste, the distinction that decides what to encode versus what to remove
- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) -- why each layer of automation pushes leverage one step up the decision chain, into specification and infrastructure

## References

- [Wikipedia, "Theory of Constraints"](https://en.wikipedia.org/wiki/Theory_of_constraints) -- Goldratt's framing for why you change the bottleneck station rather than adding effort at it, the basis for moving leverage from review to infrastructure
- [Wikipedia, "Paved road"](https://en.wikipedia.org/wiki/Paved_road) -- the principle of making the compliant path the easiest path, which lets a single engineer steer a codebase without persuading anyone
- [Wikipedia, "Technical debt"](https://en.wikipedia.org/wiki/Technical_debt) -- the metaphor for accumulated drift that a weekly gardening sweep is meant to keep net-negative
- [Wikipedia, "Broken windows theory"](https://en.wikipedia.org/wiki/Broken_windows_theory) -- why visible decay accelerates further decay, and why keeping the drift rate below the sweep rate matters disproportionately
- [tomzx/agents](https://github.com/tomzx/agents) -- a working library of the skill files and review gates that implement the infrastructure-first defense described here
