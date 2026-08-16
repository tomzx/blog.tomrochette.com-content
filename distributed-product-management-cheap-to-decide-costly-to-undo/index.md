---
title: "Distributed Product Management: Cheap to Decide, Costly to Undo"
created: 2026-08-06
type: post
status: finished
tags: [product-management, software-engineering, ai, llm, decision-making, team-management, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader is an engineer, tech lead, or engineering manager on a team where there is no dedicated product owner and engineers set product direction themselves. No formal product-management background required.
---

Distributed product management is what happens when there is no dedicated product owner, and the people building the product also decide what the product should be.
Each engineer, or each small team, makes product calls inside their own area, and those calls aggregate into the product without anyone coordinating the whole.
**The arrangement removes a real bottleneck, the single product manager, and it removes something less obvious at the same time: the friction that used to force independent decisions to agree with each other.
In the age of LLMs that friction is already gone, which is why a structure that used to be merely risky has become quietly destructive.**

## What Distributed Product Management Actually Is

The dedicated product owner is a specific role: one person who holds the product's direction, decides what gets built and what does not, and is accountable when the result is incoherent.
Distributed product management dissolves that role and spreads its responsibilities across the engineers doing the work.

It shows up in a few familiar forms.
Small teams that never hired a product manager and let the founders or lead engineer set direction.
Open-source projects, where maintainers decide what to accept and what to build, with no owner above them.
"Empowered teams," in the sense [Marty Cagan describes](https://www.svpg.com/books/), where a cross-functional team is given a problem to solve rather than a feature to implement, and the team decides the solution itself.
And, increasingly, engineering cultures where LLM-assisted development has made shipping so cheap that waiting on a product decision feels slower than just making one.

In all of these, the same property holds.
**The person deciding what to build is the person building it, and there is nobody whose job is to keep the pieces coherent.**

## The Case For It

The merits are real, and I do not want to understate them, because they explain why the arrangement is so common.

**It removes a genuine bottleneck.**
A single product manager is a single point of coordination.
When they are slow, blocked, or absent, the whole team waits.
When there is no owner in the path, decisions move at the speed of engineering.

**Decisions sit with the people closest to the problem.**
The engineer implementing the feature usually has more context about the technical reality and the user's actual behavior than a product owner who learned the domain second-hand.
Moving the decision to where the context already lives avoids a translation step, and it avoids the gap between a spec and what the spec was supposed to mean.

**Ownership produces motivation.**
People who decide what they work on care about the work in a way that people handed a task do not, a cost I have felt directly [in finishing work I did not choose](../the-cost-of-work-you-did-not-choose/index.md).
Distributed product management lets engineers keep that investment.

**It scales without growing an organization.**
A dedicated product owner has a finite span of attention.
As a product grows, either the owner becomes a bottleneck or you have to hire and coordinate more of them.
Distributed product management scales with the number of engineers by default.

Each of these is a good argument.
Together they explain why the structure keeps reappearing, and why it often works well for a while.

## The Case Against It

The problems are also real, and they take longer to show up, which is why they are consistently underestimated.

**The product loses coherence.**
A product is a system of decisions that have to agree with each other.
When each decision is made locally and optimally, the result is a [local optimum](https://en.wikipedia.org/wiki/Local_optimum): every piece is reasonable on its own, and the whole is worse than any of its parts.
Two engineers build two ways of doing the same thing.
A new feature uses a pattern that contradicts the one shipped last quarter.
The surface area grows, and nothing ties it together.

**Nobody owns the whole.**
Coherence is not a side effect of good local decisions.
It is a separate concern, the job of noticing the global pattern and sacrificing a local win when it would break that pattern.
Without an owner, that job has no home, which means it does not get done.
This is the [tragedy of the commons](https://en.wikipedia.org/wiki/Tragedy_of_the_commons) applied to a product: the shared surface that everyone uses and nobody maintains.

**Nobody is paid to say no.**
The hardest part of product work is deciding what not to build.
A dedicated owner can kill a feature because they are accountable for focus.
An engineer building in their own area has no incentive to decline their own idea, and no authority to decline anyone else's.
The result is feature accumulation, the same failure mode that turns a [backlog into a dumping ground](../backlog-management-best-practices/index.md), except it ships directly into the product.

**Cross-cutting decisions have no owner.**
Some decisions only make sense globally: the pricing model, the data model, the API conventions, the identity of the product.
These decisions occasionally require one team to accept a worse local outcome so the whole can stay consistent.
Distributed product management has no mechanism for that trade, because no one is authorized to impose a cost on one part to benefit another.

**The strategy drifts, silently.**
When every team optimizes for the metric in front of it, the product as a whole drifts toward whatever those local metrics reward, and that direction is rarely the one the company would have chosen deliberately.
This is [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law) at the level of the product roadmap: each local signal looks reasonable, and the aggregate stops pointing anywhere worth going.

The common thread is that distributed product management is excellent at producing decisions and bad at producing a coherent product.
For a long time, that trade was manageable, because the cost of building kept the decision rate low.

## Why LLMs Make the Trade Worse

Here is the part that has changed.

The friction that used to keep distributed product management tolerable was the cost of implementation.
Building a feature took days or weeks, and that cost forced a conversation before the work started.
An engineer who wanted to ship something had to justify the time, coordinate with the people whose work it touched, and get the change reviewed.
The friction was accidental, but it was doing useful work: it throttled the rate at which independent decisions could accumulate.

LLMs have removed that friction.
An engineer who wants to ship a feature can now spec it, generate it, and open a pull request in an afternoon, without asking anyone whether the feature should exist.
**The cost of making a product decision and the cost of the decision's consequence have been decoupled.
The first one collapsed toward zero.
The second one did not.**

This is what makes distributed product management destructive in the current era rather than merely inefficient.
When decisions were expensive, an incoherent product was a slow problem that you could notice and correct.
When decisions are nearly free, the incoherence arrives faster than any human can track it, and the cost shows up downstream: in a codebase nobody wants to touch, in a feature surface nobody can fully use, in the slow accumulation of a [house of cards](../the-foundation-predicts-the-house-of-cards/index.md) built from locally reasonable additions.

The deeper problem is that cheap decisions change who decides.
When a product decision required a meeting, the decision belonged to whoever ran the meeting.
When it requires only a prompt, the decision belongs to whoever types first.
That is a change in governance disguised as a change in speed, and most teams have not noticed it happened.

It is worth saying what this argument is not claiming.
It is not claiming that engineers are bad at product judgment.
Many are excellent at it, and the [bottleneck has moved toward exactly that judgment](../the-shifting-bottleneck/index.md) as implementation has been automated.
It is claiming that good individual judgment, applied independently and at machine speed, with no coherence layer above it, produces a worse product than the same judgment applied inside a shared frame.

## The Real Question Is Which Decisions to Distribute

The way out is not to bring back the single product manager as a gatekeeper.
That would reintroduce the bottleneck distributed product management was right to remove.
The way out is to notice that "product decisions" is not one category, and that the right structure differs by decision type.

A useful split comes from the [one-way door versus two-way door](https://en.wikipedia.org/wiki/Disagree_and_commit) distinction.
Some decisions are reversible.
If you ship the wrong notification wording, or pick the suboptimal layout for a single screen, you can change it next week with low cost.
These decisions should be distributed, because distributing them removes friction without risking much.

Other decisions are effectively irreversible.
What the product is, which problem it solves, which abstractions it commits to, how the pieces fit together, these set the trajectory of everything built on top of them.
Once a thousand features depend on a data model, the model is no longer negotiable.
These decisions need a single owner, not because the owner is smarter but because coherence requires that someone be able to choose the global over the local.

**The failure mode of distributed product management is not that it distributes decisions.
It is that it distributes the irreversible ones along with the reversible ones.**
Most teams that suffer from "no product owner" are actually suffering from no owner for the small set of trajectory-setting decisions, while the reversible ones are handled fine.
Diagnosing which set is causing the pain is more useful than arguing about whether to have a product manager at all.

## What to Do Next

If your team operates without a dedicated product owner and the product is starting to feel like a patchwork, a few concrete moves help.

**Write the product direction down, in one place, and keep it current.**
This is the single highest-leverage action, and it is the same lesson as [breaking the scope relitigation cycle](../when-a-closed-decision-reopens/index.md): a direction that lives in heads cannot survive contact with the next person or the next quarter.
A short, written north star, the milestones you are committing to now, and the constraints that forced the compromise, gives distributed decisions something to check themselves against.
Without it, every engineer is optimizing for a slightly different product that exists only in their head.

**Separate the two questions explicitly.**
On every non-trivial decision, ask first whether it is reversible or trajectory-setting.
Distribute the first.
Force the second through a single decision-maker and a written record, even if that decision-maker is a rotating engineer rather than a hired product manager.
The role matters less than the fact that someone owns it.

**Encode product-level invariants the way you encode engineering conventions.**
The teams that keep coherence without a full-time owner are the ones that have externalized their standards into a form the work has to satisfy: style guides for the product surface, principles for which features are in scope, a definition of what the product is not.
This is the same mechanism that lets a mature team [scale its conventions into the model](../bringing-everyone-to-the-same-level/index.md).
A convention in a head is advice that gets ignored.
A convention in a written principle is a constraint that gets enforced.

**Keep a thin, intent-level review for product decisions, as a backstop and not a bottleneck.**
The point is not to gate every change.
The point is to catch the small fraction of changes that are individually reasonable and collectively incoherent, the second implementation of an existing feature, the new pattern that contradicts the established one, the locally optimal choice that breaks a global invariant.
This is the product equivalent of the intent check I keep on [LLM-generated code](../rethinking-code-review-in-the-age-of-llms/index.md): light by default, held back for the changes that carry real risk.

**Reallocate the time you saved on implementation into judgment.**
The instinct, once implementation is cheap, is to ship more.
The correct response is to decide more carefully, because the cost of being wrong has not come down even though the cost of acting has.
Time spent on problem selection and direction now buys more than time spent on execution ever did.

## The Dedicated Owner's Real Job Was Coherence

Distributed product management is not wrong.
It removes a real bottleneck, it puts decisions close to the context, and it scales without growing an organization.
The mistake is concluding that because the dedicated owner was unnecessary, the thing the owner was doing is also unnecessary.

It was not.
The owner's real job was coherence: holding the whole product in one head, killing the features that did not fit, and choosing the global over the local when the two disagreed.
Remove the person and you still have to keep the function, or accept that the product will be built faster than anyone can keep it coherent.

**In an era when a product decision costs an afternoon and its consequences last for years, the scarce resource is no longer the ability to decide.
It is the ability to decide in a way that still makes sense next to every other decision the team is making at the same time.**
That is the bottleneck distributed product management has to solve, and LLMs have made it urgent rather than theoretical.

## See also

- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - why the constraint has climbed from implementation to deciding what to build, the exact layer where distributed product management lives
- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) - the team-level view of the same shift, and the case for specification as the highest-leverage skill once execution is cheap
- [Feature Parity Is Not a Moat](../feature-parity-is-not-a-moat/index.md) - the danger of accumulating shallow surface area, which undirected distributed decisions produce on fast-forward
- [When a Closed Decision Reopens](../when-a-closed-decision-reopens/index.md) - the case for writing direction down so it survives the next conversation, the mechanism that lets distributed decisions stay aligned
- [The Foundation Predicts the House of Cards](../the-foundation-predicts-the-house-of-cards/index.md) - why encoded conventions and written judgment outrank tacit ones, applied here to product direction
- [Backlog Management Best Practices](../backlog-management-best-practices/index.md) - the discipline of saying no and keeping focus, the function a coherence owner was quietly performing

## References

- [Marty Cagan, "Inspired: How to Create Tech Products Customers Love"](https://www.svpg.com/books/) - the empowered-team model, the legitimate form of distributed product management, which pairs distributed execution with a strong shared vision
- [Wikipedia, "Local optimum"](https://en.wikipedia.org/wiki/Local_optimum) - the formal version of the coherence problem: locally optimal decisions producing a globally suboptimal product
- [Wikipedia, "Tragedy of the commons"](https://en.wikipedia.org/wiki/Tragedy_of_the_commons) - the dynamic by which a shared product surface, used by everyone and maintained by no one, degrades
- [Wikipedia, "Goodhart's law"](https://en.wikipedia.org/wiki/Goodhart%27s_law) - how optimizing local signals causes the product's aggregate direction to drift away from any deliberately chosen target
- [Wikipedia, "Disagree and commit"](https://en.wikipedia.org/wiki/Disagree_and_commit) - the one-way door versus two-way door distinction that separates decisions which can be distributed from those which need an owner
