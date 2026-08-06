---
title: "Who Maintains the Slop?"
created: 2026-08-05
type: post
status: finished
tags: [ai, software-engineering, llm, code-quality, team-management, productivity, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader is an engineer, tech lead, or manager who has inherited AI-generated code they did not author, choose, or agree to. No specific tooling or framework knowledge required.
---

A coworker ships a feature this week.
The demo goes well, the metric moves, the credit lands on them.
Six months later the feature breaks, and the ticket is assigned to you.
You did not write it, you did not ask for it, and the person whose name is on the commits cannot explain it to you, because they did not write it either.
**They prompted it, you inherit it, and that asymmetry is the whole problem.**

This is not the ordinary handoff, where someone moves on and leaves their code behind.
It is a new and worse kind, because the thing being handed off carries less recoverable intent than human code ever did, and the person handing it off has less of that intent to offer than the author of human code ever had.
The slop producer walks away with the reward.
The maintainer is left with the cost, and was never asked whether they wanted to absorb it.

## Generation Is Cheap. Understanding Is Not.

The economics of AI-assisted code are lopsided in a way most teams have not priced in.
Generating code is now nearly free, a prompt and a few seconds.
Maintaining code has gotten cheaper too, because you can now ask a model to explain the code to you, but it has not gotten cheaper by nearly as much.
Maintenance is dominated by understanding, and understanding, even with help, is still time-consuming in a way generation is not.

When the cost of producing something collapses while the cost of owning it stays fixed, you get a predictable result.
People produce a great deal more of it than they are willing to maintain.
This is the same dynamic economists call a [negative externality](https://en.wikipedia.org/wiki/Externality): the producer captures the benefit and passes the cost to someone else who never agreed to pay it.
**In software, the river the cost gets dumped into is the codebase, and the people downstream are the maintainers.**

The old discipline that held this in check was effort.
Writing a feature by hand cost days, and that cost forced a conversation about whether the feature was worth building and whether the author was ready to live with it.
Remove that cost, and the conversation disappears with it, because the friction that produced it is gone.
The feature still costs days to maintain.
It just costs someone else, later, in a currency the original author never had to spend.

## The Author Is No Longer the Cheapest Maintainer

For a long time, software engineering ran on a principle that aligned incentive and responsibility cleanly.
Amazon stated it as [you build it, you run it](https://en.wikipedia.org/wiki/DevOps): the team that creates a service operates it, because they understand it best, and making them own the consequences makes them answerable for what they ship.

That principle worked for a specific reason.
The person who wrote the code was also the cheapest person to maintain it, because the act of writing it left a durable model in their head.
You build it, you run it was efficient as well as just.
The accountability aligned with the economics.

**AI slop severs that alignment.**
The person who generated the code did not build a model of it in their head, because they did not build it.
They saw the output, checked that it ran, verified that it did what they desired, and moved on.
They are not the cheapest maintainer anymore.
Often nobody is.
The maintainer who inherits the code knows neither the original intent nor the code itself, and the author who might remember the intent has nothing to say about the implementation that would help.

So the natural loop closes wrong.
Instead of the builder owning what they built, the code drifts to whoever is left, whoever is downstream, whoever still cares about the codebase staying healthy.
**Maintenance becomes a tax on the people who care, levied by the people who do not.**

## The Defining Feature of Slop Is Missing Intent

It is worth being precise about what makes slop slop.
It is not only that the code is bad, because sometimes the code runs fine and passes its tests.
It is that the code carries no intent anyone can recover.

Human code, even messy human code, is full of traces of the mind that wrote it.
Variable names that betray a mental model, comments that record a half-thought, a function split in a way that reflects how the author decomposed the problem.
These are imperfect signals, and they are often misleading, but they are signals.
When you inherit human code, you are an archaeologist working through strata left by a civilization that existed.
This is what [The Code You Will Never Read](../the-code-you-will-never-read/index.md) describes from the maintainer's side: a growing body of code whose internals are opaque by construction.

AI slop is archaeology without the civilization.
The patterns in it were not chosen by a mind that held the problem; they were chosen by a model selecting the most probable next token.
The names are plausible, the structure is conventional, and none of it is evidence of a decision you can reconstruct, because no decision was made in the way a human makes one.
**You cannot ask the code what it meant, and increasingly you cannot ask the author either, because the author's answer is the same guess you would make yourself.**

This is what makes AI slop harder to maintain than the human mess it resembles.
The mess is not the hard part.
The hard part is that the mess came with nobody attached to it.

## The Missing Ingredient Is Consent

The sting in the slop handoff is not only that the work is hard.
It is that the maintainer had no say in any of the decisions that produced it.

They did not choose to build the feature.
They did not choose its scope, its boundaries, its dependencies, its tradeoffs.
They did not choose the abstractions it imposes on the codebase, or the patterns it will invite the next generator to copy.
All of those choices were made by a person and a model who will not be present when the consequences arrive, and they were made without the person who will carry the consequences in the room.
**The maintainer inherits a set of decisions they were never party to, and is asked to own outcomes they could not influence.**

This is the part that goes beyond "the task is annoying," and it is why slop handoffs corrode teams faster than ordinary ones.
I wrote about the motivation tax on unchosen work in [The Cost of Work You Did Not Choose](../the-cost-of-work-you-did-not-choose/index.md).
The slop version of that tax is heavier, because the work is harder to understand and the handoff is more frequent.
When being handed other people's AI output becomes the norm, the people who maintain the codebase start to feel like janitors in a building they did not design and are not allowed to redesign, and that feeling is a leading indicator of people leaving.

## The Generator Is Rational, Not Villainous

It is tempting to tell this story with a villain, the lazy coworker dumping their slop on the team.
That story is satisfying and it is mostly wrong, and believing it will stop you from fixing the actual problem.

The generator is responding rationally to the incentives the team has set.
The team rewards shipping.
It does not charge for maintenance.
It does not require ownership to persist after a feature lands.
It does not ask whether the maintainer consents to absorb the code before it merges.
Given those incentives, generating fast, shipping fast, and moving on is the behavior that gets rewarded, so it is the behavior that happens.
**You do not fix an incentive problem by asking people to be better. You fix it by changing the prices.**

The mistake is to moralize what is structural.
The slop producer is not failing at professionalism.
They are succeeding at exactly what the system measures, and the system measures velocity, not the maintenance debt that velocity leaves behind.
Until the system charges for that debt, the generator who slows down to own their output is not virtuous; they are slower than the colleague who does not, and they lose.

## What to Do

The fix is to move the price back to where the benefit was captured.
A few concrete moves, each of which closes a gap the current default leaves open.

**Make intent travel with the code.**
The maintainer should inherit a specification, acceptance criteria, and the decisions that matter, not just a diff.
When a feature lands, it lands with a written account of what it was for, what it was not for, and where the hard choices were made.
The code is downstream of the spec, as [Defects Flow Downstream, Fixes Must Flow Upstream](../defects-flow-downstream/index.md) argues, and the spec is the part that lets a future maintainer fix the source instead of patching the symptom.
If the generator cannot produce that account, that is the signal that the generator did not understand what they shipped, and the merge should wait until someone does.

**Make the generator sticky.**
The person who generates the code owns it for a window after it ships, the same way a human author would under you build it, you run it.
You prompt it, you run it.
Bugs in that module route back to the generator for a quarter, not to whoever happens to be nearby.
This restores the alignment that cheap generation removed: the person who captured the benefit now carries at least the first round of the cost, which is the cheapest place to charge it.

**Require the maintainer's consent.**
No AI-generated change lands on a surface someone else owns without their sign-off.
This is the one that feels heavy and is the most important, because it is the only move that gives the maintainer a say in the decisions that will become their problem.
The owner of the affected code reviews the intent and the boundaries, not the diff.
If they would not have chosen to absorb this, they should not be forced to, and forcing them is what produces the slop handoff in the first place.
This is the same intent-source question that decides who is qualified to act on a change in [Who Resolves the Merge Conflict?](../who-resolves-the-merge-conflict/index.md): the person who can back the decision with intent they actually hold.

**Price the handoff.**
If a slop producer does hand work to someone else, they owe that person context, tests, and time, not a working diff.
The handoff is not complete when the code runs.
It is complete when the receiver could explain the code to a third person without the original author in the room.
Charge the handoff in the currency the generator tried to skip, which is understanding, and watch how much less slop gets produced when understanding is the cost of walking away.

**Gate generation on ownership.**
Before AI code can merge, there must be a named owner who will maintain it.
No owner, no merge.
This is a trivial rule and it eliminates the worst cases outright, the drive-by generation that lands in a shared module and becomes everyone's problem and no one's responsibility.

## The Real Failure Is Upstream

The pattern underneath all of this is the one [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) reaches from a different direction: real responsibility lives upstream, in the decisions that guided the work, not in the person left holding the diff at the end.

The slop handoff is what happens when responsibility is allowed to drift downstream and settle on whoever is standing there when the code breaks.
The generator made the decision to generate.
The model made the decisions inside the code.
The maintainer made no decision at all, and gets to own every one of them.

That is not a sustainable arrangement, and the people who notice it first are the maintainers, because they are the ones paying the tax.
They will not keep paying it quietly.
They will either push the price back upstream, where it belongs, or they will leave for a codebase where someone else has already done it.

**AI did not invent the handoff. It made generation so cheap that handing the result off became the path of least resistance. The slop producer is not a villain; they are a rational actor in a system that prices generation at zero and maintenance at full cost. The fix is not to scold them. It is to put the price back where it was captured, in the currency that was skipped, which is understanding.**

## See also

- [The Cost of Work You Did Not Choose](../the-cost-of-work-you-did-not-choose/index.md) - the motivation tax on work handed to you by declaration, which the slop handoff makes heavier and more frequent
- [The Code You Will Never Read](../the-code-you-will-never-read/index.md) - maintaining code whose internals are opaque, the condition that makes AI slop harder to inherit than the human mess it resembles
- [Defects Flow Downstream, Fixes Must Flow Upstream](../defects-flow-downstream/index.md) - the rule that the durable fix is upstream, which is why the spec must travel with the code so the maintainer inherits the source and not just the symptom
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - the argument that real responsibility lives in the decisions that guided the work, not in the person scanning the diff at the end
- [Who Resolves the Merge Conflict?](../who-resolves-the-merge-conflict/index.md) - the intent-source test for who is qualified to act on a change, which is the same test that decides who should own the slop

## References

- [Wikipedia, "Slop (artificial intelligence)"](https://en.wikipedia.org/wiki/Slop_(artificial_intelligence)) - the term for low-effort, mass-produced AI content, extended here to code that ships without recoverable intent
- [Wikipedia, "Externality"](https://en.wikipedia.org/wiki/Externality) - the economic frame for a cost imposed on a third party who did not consent, the model for slop as pollution of the codebase
- [Wikipedia, "Tragedy of the commons"](https://en.wikipedia.org/wiki/Tragedy_of_the_commons) - why a shared resource degrades when individuals capture the benefit and socialize the cost, the codebase as commons
- [Wikipedia, "Technical debt"](https://en.wikipedia.org/wiki/Technical_debt) - the accumulated maintenance cost deferred by fast generation, the debt the slop producer leaves behind
- [Wikipedia, "DevOps"](https://en.wikipedia.org/wiki/DevOps) - the "you build it, you run it" principle that aligned authorship with ownership, which cheap generation unaligns
- [Wikipedia, "Free rider problem"](https://en.wikipedia.org/wiki/Free_rider_problem) - the dynamic by which those who benefit without paying overwhelm those who carry the cost, the maintainer's trap
- [Wikipedia, "Principal-agent problem"](https://en.wikipedia.org/wiki/Principal%E2%80%93agent_problem) - the mismatch between the person deciding what gets built and the person bearing the consequences, the structure of the slop handoff
