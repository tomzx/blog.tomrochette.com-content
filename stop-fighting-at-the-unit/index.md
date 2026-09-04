---

title: "Stop Fighting at the Unit: Encode Your Judgment Instead"
created: 2026-06-24
type: post
status: finished
tags: [software-engineering, ai, productivity, judgment, decision-making, attention, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader is a technical practitioner who has felt the gap between how fast work arrives and how fast they can personally attend to it. Synthesizes several earlier articles; no single one is prerequisite.
agent_sessions:
  - ses_005ec6e29ffeREI2bLD97m5Tfn
---

When I look back at the things that have frustrated me recently, they all have the same structure.

The codebase that drifts faster than I can review it ([The Codebase Gardener](../the-codebase-gardener/index.md)).
The scope decision that reopens every time a new person enters the chain ([When a Closed Decision Reopens](../when-a-closed-decision-reopens/index.md)).
The model releases that pile up faster than I can read them ([Keeping Up With AI Is a Losing Strategy](../keeping-up-with-ai/index.md)).
The convention I keep defending in pull request comments that nobody reads next week ([When Engineers Disagree on Best Practices](../when-engineers-disagree-on-best-practices/index.md)).
The team that adopted a monorepo and stayed just as misaligned ([A Monorepo Doesn't Make You a Single Team](../a-monorepo-doesnt-make-you-a-single-team/index.md)).
The two camps arguing whether to delegate everything to AI or nothing, both quietly hollowing themselves out ([AI-Maxxing and Resistance Are the Same Mistake](../ai-maxxing-vs-fighting-against-it/index.md)).

Different domains.
Same structure.
**Each is a fight at the unit, the diff, the meeting, the paper, the comment, the repo, and each is being lost for the same reason: per-unit human effort scales linearly with my hours, while the thing I am fighting scales with something else entirely.**

This article is the throughline I kept bumping into.
It is not a new idea so much as a single idea that every one of those pieces was reaching for from its own angle.
Stop fighting at the unit.
Start fighting at the layer everything is forced to pass through.

## The Asymmetry That Connects Every One of Them

The reason these problems feel unrelated is that they live in different parts of the work.
Code review.
Scope.
Learning.
Tooling.
Team design.

Strip the domain away and they share one structure.
On one side of the ratio is something that grows exponentially or fragments multiplicatively: pull requests from agents, papers from arXiv, new hires joining the communication chain, teammates each driving their own conventions.
On the other side is a human reading, arguing, deciding, or noticing at a rate that has not meaningfully changed in a generation.

A human reads at a few hundred words per minute.
A human holds a handful of items in working memory.
A human can be in one meeting at a time, make a bounded number of careful decisions a day, and review a bounded number of diffs before the quality of attention collapses.
None of those numbers is moving.

Meanwhile, the production side of every one of these cycles is compounding.
**The ratio is moving against you in every domain at once, and the instinctive response, to read faster, review harder, argue better, attend more meetings, is the response that the ratio has already defeated.**

## "Fight Harder" Is the Trap

The trap is that fighting harder feels virtuous while you do it.

Catching a misnamed variable in review feels like defending the standard.
It is not.
It is fighting a single ember while the forest is on fire.
Re-arguing a scope decision in the meeting where it resurfaced feels like refusing to back down on a technical truth.
It is not.
It is paying the same tax a third time because the decision was never written down.
Reading one more newsletter feels like staying informed.
It is not.
It is optimizing for the producer's schedule at the cost of your own.

In every case the per-unit effort is real, the per-unit payoff is real, and the aggregate position is deteriorating.
**Per-unit effort cannot match entropy that is being produced faster than you can process it.**
This is not a discipline problem.
It is structural.
No amount of rigor at the unit closes a gap that the unit's own arithmetic keeps widening.

## Tools Do Not Fix People Problems

The first place the trap shows up is the tool decision.

Adopt a monorepo, expecting it to dissolve team boundaries.
It does not.
The boundaries reappear as `CODEOWNERS` rules and review bottlenecks, because a repository is a versioning boundary, not a coordination boundary ([Conway's Law](https://www.melconway.com/Home/Conways_Law.html) guarantees the team structure wins eventually).
Adopt an LLM agent, expecting it to dissolve the code-quality problem.
It does not.
It produces code faster than you can read it, and the bottleneck moves to review, then to specification, then to taste ([The Shifting Bottleneck](../the-shifting-bottleneck/index.md)).
Adopt a sprint framework, expecting it to dissolve the prioritization problem.
It does not.
It just gives the same misalignment a more impressive calendar.

The common error is reaching for a structural change in the substrate, the repository, the tool, the framework, and expecting it to do the work of a structural change in the people.
**Tooling follows coordination. It does not create it.**
If your teams are misaligned, a shared repository gives misaligned people more ways to step on each other, faster.
If your team has no shared decision-making process, the best framework in the world will be renegotiated every sprint.

The inverse maneuver is the one that actually works: decide the team and communication structure you want first, then let the tooling follow ([ThoughtWorks, "Inverse Conway Maneuver"](https://www.thoughtworks.com/radar/techniques/inverse-conway-maneuver)).
The repository is a downstream optimization.
The agent is a downstream amplifier.
Neither is a substitute for the conversation you were hoping to skip.

## The Bottleneck Moves, It Does Not Disappear

The second place the trap shows up is the belief that automating a layer removes the layer.

It does not.
It moves the constraint to whatever was upstream of the layer you automated, and that upstream layer is almost always more judgment-heavy, not less.
Automate code production, and review becomes the bottleneck.
Automate review with gates and paved roads, and specification becomes the bottleneck.
Automate triage with an agent, and deciding what to care about becomes the bottleneck.
Automate that too, and the only thing left is the taste that decides whether any of it was worth doing.

This is the same pattern at every scale, and the practical consequence is uncomfortable.
**The layer you automate away is never the layer that was actually constraining the outcome for long.**
The outcome was always being constrained by judgment, and automation just makes the judgment legible by removing the easier work that was hiding it.

The AI-maxxer's error is mistaking the move for a disappearance, and concluding there is no bottleneck left worth staffing ([AI-Maxxing and Resistance Are the Same Mistake](../ai-maxxing-vs-fighting-against-it/index.md)).
The resistor's error is treating the disappearing layer as worth preserving in the name of craft.
Both miss that the leverage has simply moved up, and that the moved-to layer is where the durable work now lives.

## Durable Versus Ephemeral, Compounding Versus Depreciating

Once you accept that the bottleneck moves up, the next question is which of your activities are even worth protecting.

Most of what feels urgent in any of these cycles is ephemeral.
A specific model's benchmark numbers, a specific launch event, this week's leaderboard: these date within weeks.
A specific pull request's style debate, a specific meeting's scope argument, a specific newsletter's hot take: these stop mattering the moment they are resolved, and sometimes before.

A surprising amount is durable.
The mechanics of attention.
The basics of context and prompting.
The theory of constraints in a pipeline.
The discipline of writing decisions down.
The difference between a reversible choice and an irreversible one.
The taste that decides whether something should exist at all.
These barely move across model generations, and they compound.

The right posture falls out of this distinction immediately.
**Overweight the durable. Underweight the ephemeral.**
The ephemeral items are not worthless, but they should be consumed on demand, when a specific decision requires them, not on a schedule driven by fear that you are missing something.
And the durable layer is where the time you reclaim from the ephemeral should land, because the durable layer is the only thing in the cycle that actually compounds ([Keeping Up With AI Is a Losing Strategy](../keeping-up-with-ai/index.md)).

The test that settles it, for any activity on your plate, is the two-year test.
If I let the model do this for the next two years, will the me that emerges be more valuable, or less, than the me that kept doing it by hand?
If less, delegate it ruthlessly, even if it feels like craft.
If more, protect it ferociously, even if a model offers to do it for free.

## Encode Judgment in What Outlives You

So far this is diagnosis.
The prescription is one move, repeated until it is reflexive.

**Stop defending your judgment at the unit, and start encoding it in the layer everything passes through.**

A standard that lives only in your review comments executes only when you are awake, looking, and willing to argue about it.
A standard that lives in a lint rule, a CI gate, a scaffold template, or a skill file executes on every change, forever, without you being present.
That is the whole difference between a standard and an opinion.
A standard runs whether or not anyone agrees with it.
An opinion dies the moment you go on vacation.

The same move applies to every domain where per-unit effort is losing.

For scope decisions, the encoding is the written decision record, with the north star, the milestone, the priced options, and the date.
A decision that lives only in the heads of the people who were in the room has a half-life equal to the time it takes one new person to enter the chain.
A decision that lives in a file says the same thing to the new manager on their first day as it said to the principal on the day it was written ([When a Closed Decision Reopens](../when-a-closed-decision-reopens/index.md)).

For conventions, the encoding is the invariant, machine-checked, that converts an arguable preference into a property the system will enforce.
Every preference you promote to an invariant is one fewer conversation you have to win, and one fewer place the codebase can drift while you are not looking ([The Codebase Gardener](../the-codebase-gardener/index.md)).

For triggers and cadences, the encoding is the loop file, versioned alongside the skill it schedules, so that "what does this do" and "when does this run" evolve in the same pull request ([Loops as Files](../loops-as-files/index.md)).
A trigger that lives in a crontab nobody reads is a policy nobody reviewed.

For team norms, the encoding is the decision record plus the disagree-and-commit process that produced it, because the meta-process for handling the next disagreement is worth more than the specific answer to this one ([When Engineers Disagree on Best Practices](../when-engineers-disagree-on-best-practices/index.md)).

In every case the pattern is the same.
The judgment does not go away.
It stops being something you exert in real time and starts being something the system exerts on your behalf.
**Your leverage stops scaling with your hours and starts scaling with the surface area of what you have encoded.**

## Incentives Are Not Aligned, and Urgency Is a Hypothesis

There is a reason the per-unit fight feels so relentless, and it is not only that there is a lot to do.

Almost everyone producing AI content, framework advocacy, scope pressure, or convention evangelism benefits from your feeling underinformed or under-committed.
Newsletters need opens.
Model labs need adoption.
Benchmark authors need citations.
Thought leaders need attention.
A new manager needs to demonstrate value to the senior leader, and an enthusiastic "we can do more" lands better in that first meeting than a cautious "we already agreed to less."

This does not make any of them wrong.
It means the default framing, "you need to know this now," "we should be building this," "this is the right way," is a sales pitch aimed at a reader or a colleague who has no time to verify it ([Keeping Up With AI Is a Losing Strategy](../keeping-up-with-ai/index.md)).

The defense is not to become suspicious of everything.
It is to treat the urgency of any single item as a hypothesis from someone with an incentive to inflate it, not as a fact about the world.
Real shifts are rare, and they usually surface through your durable layer, your pull-based learning, and your colleagues whether or not you chased them directly.
**The asymmetry favors the tighter filter.**
Optimize for not being drowned, not for not being surprised.

## Silent Failure Is the Dangerous Kind

The encoding strategy has one failure mode that deserves to be named explicitly, because it is the same failure mode that makes per-unit effort feel safe in the first place.

A filter that worked at the last model generation will be miscalibrated for this one, and you will not notice, because the failure is silent: you simply stop seeing the things it threw away.
A gate that passed a year ago will let a new class of problem through, and you will not notice, because everything is still green.
A loop that ran reliably for a quarter will silently stop running when the event it triggers on changes form, and the first sign of trouble will be the damage.
A decision record that settled a question will quietly stop reflecting reality as the constraints that produced it drift.

The encoding does not eliminate the need for attention.
It changes where the attention goes.
Instead of attending to every unit, you attend to the calibration of the encodings: re-auditing the filter, re-running the trigger in dry-run, re-checking the invariant against the failure modes that have emerged since it was written, re-reviewing the decision record against the current state of the world.

**A filter is not something you build once; it is something you maintain, and most people never re-audit theirs.**
The encoded layer decays too.
It just decays on a timescale you can schedule around, instead of a timescale that schedules around you.

## The Last Job Is Articulating Taste

Follow the move to its end and the bottleneck lands somewhere specific.

Once execution is delegated, review is gated, triage is automated, and even the filter is run by an agent, the scarce skill is no longer any of those things.
It is specifying, precisely and candidly, what you actually care about: what counts as signal for your specific work, which trade-offs you accept when you tune the threshold tighter or looser, which decisions are one-way doors, which conventions are structural, which scope is the milestone and which is the north star.

That skill does not delegate.
It cannot delegate, because using the delegation well already presupposes it.
**The last human job in this chain is articulating taste, and nobody can write that prompt for you.**

This is the uncomfortable core of the whole pattern.
The work that survives every layer of automation is the work of deciding what the automation is for.
It is judgment-heavy, it is hard to outsource, and it compounds, which is the strongest case I can make for spending attention on it now, before the per-unit work you are still doing eats the time you would have used to build it.

## What to Do Next

You do not need permission, and you do not need a migration.

Pick the single per-unit fight that is consuming the most of your attention, the review comment you keep writing, the scope argument you keep relitigating, the standard you keep defending verbally, the cadence you keep running by hand.
Ask the one question that matters: what would have to be true for this fight to not need me next week?

Then write the thing that makes it true.
A lint rule.
A CI gate.
A decision record.
A loop file.
A priced option list instead of an "impossible."
A skill file the agent loads instead of an opinion you bring to the standup.

Run it on every change, including the ones you do not personally touch.
Then do it again next week, with the next most expensive fight.
**Each encoding is a piece of vigilance that stops being yours and starts being the system's.**

Over a quarter, the surface you have to defend manually shrinks to the small set of genuinely judgment-laden calls: taste, architectural direction, whether a feature should exist at all, whether this is still the codebase you want to be responsible for.
Everything else is being caught upstream of you, by machinery that does not tire, by files that do not go on vacation, by records that say the same thing to the new manager as they said to the principal.

You will still miss things.
So will the person who fights every diff, attends every meeting, and reads every paper, and they will also have missed the chance to build anything durable with the time they spent.
**The ratio is moving against per-unit effort in every domain at once. The only durable defense is judgment encoded in artifacts that outlive your attention.**

Stop fighting at the unit.
Start fighting at the layer.

## See also

- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - the upstream pattern this article generalizes: every layer automated reveals a more judgment-heavy layer upstream
- [The Codebase Gardener](../the-codebase-gardener/index.md) - the same encoding move applied to code quality, where the layer everything passes through is CI, lint, and skill files
- [When a Closed Decision Reopens](../when-a-closed-decision-reopens/index.md) - the same encoding move applied to scope, where the layer everything passes through is the written decision record
- [Keeping Up With AI Is a Losing Strategy](../keeping-up-with-ai/index.md) - the same encoding move applied to information consumption, where the layer everything passes through is your filter
- [When Engineers Disagree on Best Practices](../when-engineers-disagree-on-best-practices/index.md) - the meta-process for resolving disagreements being worth more than any specific resolution
- [AI-Maxxing and Resistance Are the Same Mistake](../ai-maxxing-vs-fighting-against-it/index.md) - the durable-versus-depreciating distinction that decides what to encode versus what to delegate
- [A Monorepo Doesn't Make You a Single Team](../a-monorepo-doesnt-make-you-a-single-team/index.md) - the canonical case of a tool decision failing to substitute for a people decision
- [Loops as Files](../loops-as-files/index.md) - extending the encoding move from skills to the triggers that schedule them

## References

- [Theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints) - Goldratt's framing for why improving one station exposes the next bottleneck, the mechanism behind every "automate the layer, the bottleneck moves up" claim in this article
- [Conway's Law](https://www.melconway.com/Home/Conways_Law.html) - why systems mirror communication structure, the reason tool decisions cannot substitute for coordination decisions
- [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law) - why a measure, once it becomes a target, stops measuring what you meant, the reason encoded filters and invariants must be re-audited
- [Architecture Decision Records](https://adr.github.io/) - the lightweight written record that turns a verbal decision into something that travels to rooms you are not in
- [Disagree and commit](https://en.wikipedia.org/wiki/Disagree_and_commit) - the one-way versus two-way door distinction that decides which fights are worth your scarce attention
- [Paved road](https://en.wikipedia.org/wiki/Paved_road) - making the compliant path the easiest path, the highest-leverage encoding available to a solo defender
