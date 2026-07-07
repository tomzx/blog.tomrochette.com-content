---
title: "The Concept Car Problem: Demoing a Vision Without Promising a Product"
created: 2026-07-07
type: post
status: finished
tags: [software-engineering, team-management, communication, expectations, requirements, demos, fully-ai-generated, llm=claude]
readability: 3
audience_notes: >
  Assumes the reader is an engineer, tech lead, or principal caught between a senior leader's vague ask and the limits of today's tools, particularly after a vision demo raised expectations. No specific framework knowledge required.
---

Senior leadership asked for a feature and was vague about what they actually wanted.
Your team did the diligent thing: you built a demo of the north star, the version of the feature you would build if today's tools could support it, and you used that demo to negotiate a concrete, feasible scope with your principal.
Then a new manager had their first meeting with the senior leader, the topic resurfaced, and the expectations you thought were settled came loose again.
Now you are bracing for another round of explaining what is and is not possible today.

The instinct is to treat this as a communication failure to be corrected once, harder.
It is not.
**You are experiencing the predictable physics of three forces: vague intent invites reinterpretation, vivid demos anchor expectations above feasibility, and alignment decays every time a new person enters the conversation.**
Each force is manageable.
What is not manageable is pretending the cycle is an anomaly that the next great meeting will end for good.

## Vague Intent Is Not a Defect. It Is the Format Leadership Speaks In.

Start by dropping the expectation that senior leadership will ever hand you requirements.
Executives operate at the altitude of direction, not specification.
The military ran into this problem centuries before software did and formalized the answer as [commander's intent](https://en.wikipedia.org/wiki/Intent_(military)): the leader states the outcome and why it matters, and the units closest to the ground own the translation into concrete action, because they are the only ones who can see the terrain.

This reframing matters because it relocates the ambiguity from "leadership failed to specify" to "specification is our job."
When you accept that the translation is yours to own, two obligations come with it.
First, you must write the translation down, because an unwritten interpretation is indistinguishable from no interpretation.
Second, you must close the loop by presenting the translation back to the person whose intent you interpreted, and get an explicit yes.
**A vague ask that you silently interpret is a debt; the interest is every future meeting where someone else interprets it differently.**

In your situation, the translation happened, but the loop closed with the principal, not with the senior leader.
The person whose vague wish started everything never ratified the concrete scope that came out of it.
That gap is exactly where the new manager's meeting reopened the question: the leader was still holding the original wish, because nobody had ever traded it in for the negotiated version.

## The Demo Anchored Them. That Was Its Job. That Is Also the Problem.

A north star demo is a persuasion instrument, and yours worked.
It compressed an abstract vision into something leadership could see, react to, and get excited about.
But a demo does not come with its own disclaimers.
The viewer walks away holding the most concrete artifact from the meeting, and the most concrete artifact wins.
You showed them a destination; they recorded an ETA.

This is [anchoring](https://en.wikipedia.org/wiki/Anchoring_effect) doing what anchoring does.
The first vivid number, image, or experience a person encounters becomes the reference point that all subsequent adjustments are made from, and the adjustments are reliably insufficient.
Every later conversation about feasible scope is now experienced by the leader as a markdown from the demo, and markdowns feel like losses.
You are not negotiating from zero up to what is possible; you are negotiating from the demo down to it, and down is the emotionally expensive direction.

The automotive industry solved this decades ago with a labeling ritual.
A [concept car](https://en.wikipedia.org/wiki/Concept_car) is shown at auto shows precisely to gauge reaction to a vision, and nobody storms the dealership demanding to buy one, because the entire industry has agreed on what the label "concept" means: this is a direction, not a product, and the production version will be smaller, heavier, and less dramatic.
Software vision demos have no such ritual, so every demo is implicitly a product announcement unless you build the disclaimer into the artifact itself.

Do that literally.
Put the label on the first slide and the last: this is the three-year vision, it is not buildable with today's tools, and here is the specific slice we propose to build now.
Show the vision and the feasible slice in the same meeting, side by side, so the anchor and the commitment enter the leader's memory as a pair.
**A vision demoed without its feasible counterpart is a promise; a vision demoed next to its feasible counterpart is a roadmap.**

## Alignment Is a State That Decays, Not an Event That Concludes

The agreement with your principal felt like the end of the process.
It was actually a snapshot of a state, and the state began decaying immediately.
Alignment lives in individual heads, not in the organization, and the organization keeps swapping heads: a new manager arrives, the senior leader's attention cycles away and returns, priorities shift a quarter later.
Each swap resets some fraction of the shared understanding to zero, and the reset people default back to the most vivid thing they know, which is the vague wish or the shiny demo, not the carefully negotiated scope they were never part of negotiating.

Your new manager is the clearest case.
They walked into a first meeting with a senior leader, almost certainly wanting to demonstrate energy and possibility, holding none of the history that produced the current scope.
Of course the topic reopened.
Sending anyone into that room unbriefed guarantees it, and blaming them for it misreads a systems failure as a personal one.
The mechanics of why decisions must travel as written records rather than memories are covered in [When a Closed Decision Reopens](../when-a-closed-decision-reopens/index.md); the short version is that a decision that lives only in the heads of the people who made it cannot survive contact with anyone who was absent.

The practical consequence: stop treating re-alignment as a failure state and start budgeting for it.
Every new stakeholder gets the briefing before their first exposure to the topic, not after their first misstep.
Every return of the topic gets answered with the same written artifact, not a fresh improvisation.
**You cannot prevent alignment from decaying; you can only make re-alignment cheap, and the way to make it cheap is to make it a document instead of a debate.**

## Move the Argument from "Possible?" to "What Changed?"

The most draining part of the cycle is that every round relitigates feasibility from scratch, as if the question "can this be built today?" had never been answered.
The way out is to change what the recurring conversation is about.

Build a capability ledger: a short, living document that lists each piece of the north star, the specific capability it requires, whether that capability exists today, and what you are watching for.
"Real-time semantic search over the full corpus: requires X; current tools achieve Y; blocked until Z; we re-evaluate quarterly."
This does three things at once.
It converts "impossible," a word leaders hear as reluctance, into named, checkable dependencies.
It gives the vision a standing home, so acknowledging the north star no longer requires re-promising it.
And it transforms the recurring meeting from a feasibility debate into a status review: not "can we or can't we," but "here is what changed since last quarter, and here is what that unlocks."

The distinction between the destination and the current step is old enough to have furniture named after it; the [three horizons framework](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/enduring-ideas-the-three-horizons-of-growth) exists precisely because organizations that discuss horizon-three ambitions and horizon-one commitments in the same breath end up doing neither well.
Give each horizon its own artifact and its own cadence, and they stop fighting.

The quarterly cadence matters more than it looks, especially when the missing capabilities are moving targets, as they are anywhere AI tooling is involved.
A feasibility answer given six months ago is stale in both directions: things that were impossible may now be possible, and leadership knows this, which is part of why they keep re-asking.
**A team that proactively reports "here is what just became possible" earns the standing to be believed when it says "this is not possible yet."**
The re-asking does not stop because you won the argument; it stops because you built the mechanism that answers the question before it is asked.

## The Playbook

When the topic comes back, and it will, run this sequence instead of the debate.

First, brief the new manager now, before their second meeting with the senior leader.
Walk them through the vision, the negotiated scope, and the capability ledger, and invite their objections in private.
A manager who co-owns the record will carry it into the room; a manager who has never seen it will improvise around it.

Second, get the negotiated scope ratified by the senior leader directly, in writing, with the north star acknowledged in the same document.
The agreement with your principal was necessary but not sufficient; the person whose intent started this has to trade the wish for the plan, explicitly, or the wish stays live.

Third, re-label the demo retroactively.
In the next conversation, put the concept-car framing on it: that demo was the destination, this document is the vehicle we can actually build this quarter, and this ledger is the list of parts the destination still needs.

Fourth, install the cadence.
A standing quarterly review of the ledger, on a date you control, turns surprise relitigation into scheduled reassessment.
The cycle you are stuck in is the unscheduled version of a conversation that is genuinely necessary; scheduling it is what makes it stop ambushing you.

You cannot build what today's tools cannot support, and no amount of repeating that will make it land.
What lands is a vision with a label, a scope with a signature, a ledger with dates, and a manager who walks into the room already holding all three.

## See also

- [When a Closed Decision Reopens](../when-a-closed-decision-reopens/index.md) - the companion piece: why the negotiated decision itself failed to survive the new manager's meeting, and the written-record discipline that fixes it
- [Bringing Everyone to the Same Level](../bringing-everyone-to-the-same-level/index.md) - the same problem of knowledge trapped in individual heads, at the level of engineering execution rather than stakeholder alignment

## References

- [Wikipedia, "Intent (military)"](https://en.wikipedia.org/wiki/Intent_(military)) - the doctrine of commander's intent: leaders state outcomes, executing units own the translation into concrete action
- [Wikipedia, "Anchoring effect"](https://en.wikipedia.org/wiki/Anchoring_effect) - why the north star demo became the reference point that every feasible scope is now measured against
- [Wikipedia, "Concept car"](https://en.wikipedia.org/wiki/Concept_car) - the labeling ritual that lets an industry show visions without promising products
- [McKinsey, "Enduring Ideas: The three horizons of growth"](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/enduring-ideas-the-three-horizons-of-growth) - why long-term ambitions and near-term commitments need separate artifacts and separate conversations
