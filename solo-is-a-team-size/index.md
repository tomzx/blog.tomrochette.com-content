---
title: "Solo Is a Team Size: When Humans Still Earn a Seat in the Agentic Era"
created: 2026-08-20
type: post
status: finished
tags: [ai, software-engineering, llm, agents, team-management, collaboration, fully-ai-generated, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader is an engineer or founder who can already delegate most implementation to LLM agents and has wondered whether colleagues are now more cost than benefit. No management background required.
---

One person directing a fleet of agents now produces more working software in a week than a small team produced a decade ago.
Every alignment meeting, every argument about conventions, every wait for a review starts to look like pure overhead.
The question I ask myself is whether working in a team still makes sense at all.
The question assumes that going solo means leaving teams behind.
It does not.
A solo operator running a fleet of agents is already working in a team, one human and N machines, with assignments, reviews, conventions, and all the coordination that implies.
The real question is not team or no team.
**The real question is when a seat at that table should be filled by a human.**

## Your Fleet Is Already a Team

What would I actually do all day if I went solo?
I would write specifications, which are prompts, and delegate them, which is task assignment.
I would review what comes back, request changes, and resolve conflicts between agents working on the same files.
I would maintain conventions that every agent must follow and correct the ones that drift.
That is not a person quietly coding alone.
**That is a team lead doing team lead work for a team that happens to be made of agents.**

Now audit which functions this team already covers, and which have no seat assigned.

Execution is fully covered.
Agents turn a specification into working changes, at any hour, at any scale.
Give the fleet my worst idea and it returns that idea implemented fluently, with tests, in minutes.
**That is the fleet doing its job well; reviewing the idea was never its job.**
Direction would have a single seat, mine, and execution would treat whatever leaves that seat as settled, which is exactly what execution should do.
The same property appears in prose, as [What the Author Brings When the Model Writes](../what-the-author-brings-when-the-model-writes/index.md) observes: the model can produce anything, which is why the deciding is separate from the producing.

The reasons behind past decisions would live in one head, mine.
The agents would hold exactly the conventions I encode, and the why would survive only if I wrote it down, which would make the whole operation one node until the records make it more.
The node does not need to fail dramatically.
The node just needs to take a vacation.

And the review of my own direction would run through the same head that chose it.
My errors would pass my own review at a rate that should terrify anyone who has reread their own writing a day later.

The overhead I would escape by going solo is the delivery mechanism for direction review, shared memory, and second eyes.
It would not disappear; it would convert into gaps that surface later and cost more.

## Encode the Practices Before Adding Headcount

The first move is not to hire.
The first move is to import the team practices that make any team function, because applied to a fleet they are what make solo work at scale.

Write the specification before the code, because the prompt is the source code, and the fleet executes the specification it is given, no more and no less.
Encode conventions as gates and skill files that execute on every change instead of review comments that depend on someone remembering to say them, the move [The Codebase Gardener](../the-codebase-gardener/index.md) argues for and [Bringing Everyone to the Same Level](../bringing-everyone-to-the-same-level/index.md) describes as institutional memory that runs itself.
Demand evidence with every delivery, a failing test turned green, a recording, a benchmark, so that acceptance stops being a matter of opinion and starts being a check, the contract [You Are the Bottleneck](../you-are-the-bottleneck/index.md) asks of any fast producer.
Write decisions down, one paragraph each, so the why survives outside your head.

A fleet with specs, gates, evidence, and records is a team with a functioning culture.
**Most of what made teams feel like overhead was the delivery cost of these four things, and agents let you pay that cost once, in code, instead of forever, in meetings.**

## When It Makes Sense to Be a Human Team

Now the original question can be asked precisely: when does a seat need a human?

[Brooks made the accounting fifty years ago](https://en.wikipedia.org/wiki/The_Mythical_Man-Month): n people create n(n-1)/2 communication channels, and every channel taxes alignment.
The economics changed.
An agent seat executes without needing alignment and pays no channel tax; a human seat pays the full tax and must contribute enough direction, memory, and accountability to cover it.
**A human seat has to earn its place against near-free, and it earns it in the three roles the fleet does not perform.**

Three conditions cover most of the cases.

**The work has no oracle.**
An agent can verify against a check: tests that pass, a spec that matches, a conflict with a mechanical resolution.
When correctness is machine-checkable, fill the seat with an agent and sleep well.
When the work is direction, intent, or taste, when the question is whether the thing should exist, there is no oracle, only judgment.
An agent executes the plan it is given; a human can question the plan itself.
[Who Resolves the Merge Conflict?](../who-resolves-the-merge-conflict/index.md) draws the same line inside a single pull request: mechanical conflicts go to the bot, semantic ones need someone who holds intent.

**The context exceeds one head.**
A real product accumulates more surface than any single person holds, and past some size the single node becomes the constraint no matter how fast the fleet executes.
A second head is replication: another copy of the why, the failure modes, and the customer reality, which is why the node can finally take a vacation.
Below that size, the second head mostly duplicates what you already know, and the channel tax buys little.

**The stakes need a counterparty.**
Some decisions are irreversible or expensive enough that one confident brain, machine-amplified, should not make them alone.
A name beside yours on the decision is not ceremony; it is a second signature on the one-way doors, and it is also what accountability requires when something eventually breaks.
Accountability is a role agents do not hold: an agent executes, and a person answers for what was decided.

**Ownership has no seat.**
Add the three conditions together and the sum is ownership: deciding what the work is, remembering why it exists, and answering for it.
In a company, ownership survives the owner: when someone is away or leaves, the work is reassigned, and someone else takes responsibility for keeping it functioning.
The company is the container that keeps ownership continuous; individuals are stewards who hold it for a while and pass it on.
A solo setup has no container.
The owner and the person are the same thing, so absence does not reassign the work; it orphans it.
The fleet keeps executing, patches, deploys, alerts handled, but execution is not ownership.
**A system can keep running and still be abandoned, because ownership means someone answers for it, and no agent holds that role.**

The partial answers are all transfer artifacts.
Decision records, runbooks, and specifications make the why inheritable, so a successor can pick the work up without the owner's head.
Opening the source turns the community into a container of last resort.
Naming an inheritor, even informally, converts the orphan case into a handoff waiting to happen.
None of these fully solves it.
**Ownership continuity for the solo operator is still an open problem, and pretending the fleet solves it is how systems get abandoned while they are still green.**

Notice what this does to hiring logic.
Teams used to add humans for hands, and hands are now near-free, so the remaining reasons to add a human are direction, memory, and accountability.
[Google's Project Aristotle](https://rework.withgoogle.com/print/guides/5727380657274880/) found that the strongest predictor of human team effectiveness is psychological safety, which is precisely the capacity for dissent to occur.
The finding reads as a warning here: a human seat without safety produces agreement instead of judgment, and agreement is a contribution the fleet already supplies.
And the solo fleet is the limiting case, [groupthink](https://en.wikipedia.org/wiki/Groupthink) with an n of one, a team where dissent holds no seat at all.

The human team that remains is therefore small, three to five people owning a domain end to end as [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) argues, but the staffing question inverts.
Do not ask how much the candidate can produce.
Ask where the candidate will disagree with you, and whether that disagreement will be right often enough to pay its channel tax.

## What to Do Next

If you run a fleet, or are weighing one, audit it as a team this week.
Trace the path your worst current idea would take through it, station by station, and count the places where the plan itself can be challenged.
If the count is zero, you have found the gap, and it is in the design, not in the agents.

Then decide deliberately where judgment enters.
If your work has an oracle, is reversible, and fits in one head, stay solo and stop feeling guilty about it; the fleet plus encoded process is a real team.
If any of the three conditions bites, no oracle, context overflow, one-way doors, buy a human seat in whatever dose makes sense: a paid reviewer for the consequential changes, a community that will tell you the idea is bad while it is still cheap to kill, a co-founder for the direction itself.

For everything you own, write the handoff paragraph: what it is, why it exists, who inherits it.
The paragraph converts ownership from a property of your presence into an artifact, the same move as every other practice in this piece, and it is the closest thing solo work currently has to succession.

And if you build a team, staff it for the disagreements.
**You were never choosing between working alone and working with people; you were deciding, seat by seat, what each kind of worker is for.**
Agents are for the work.
Humans are for the judgment that decides what the work is for.

## See also

- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) - the design of the small human team that remains once seats are filled for dissent instead of hands
- [The Prompt Is the Source Code](../the-prompt-is-the-source-code/index.md) - the specification as the management artifact of an agent fleet, the first practice a solo operator imports
- [You Are the Bottleneck](../you-are-the-bottleneck/index.md) - the review contract that turns acceptance from opinion into check, and the queue math once generation is cheap
- [Who Resolves the Merge Conflict?](../who-resolves-the-merge-conflict/index.md) - the oracle versus no-oracle split inside a single pull request, the same line that decides human versus agent seats
- [Who Maintains the Slop?](../who-maintains-the-slop/index.md) - the ownership question for generated code: who stays attached after the fleet produces it

## References

- [Fred Brooks, "The Mythical Man-Month" (Wikipedia)](https://en.wikipedia.org/wiki/The_Mythical_Man-Month) - the channel-counting math that human seats must now pay for against agent seats that coordinate at near-zero cost
- [Google re:Work, "Guide: Understand team effectiveness"](https://rework.withgoogle.com/print/guides/5727380657274880/) - Project Aristotle's finding that psychological safety, the capacity for dissent, is the top predictor of team performance
- [Groupthink (Wikipedia)](https://en.wikipedia.org/wiki/Groupthink) - what absent dissent does to group decisions, the dynamic a solo fleet embodies when no seat is assigned to it
