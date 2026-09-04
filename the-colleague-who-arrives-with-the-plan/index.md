---

title: "The Colleague Who Arrives With the Plan"
created: 2026-08-20
type: post
status: draft
tags: [software-engineering, team-management, collaboration, decision-making, ownership, communication, fully-ai-generated, llm=glm-5.3]
readability: 4
audience_notes: >
  Assumes the reader is a software engineer on a team where one colleague ends up steering every project, and has watched their own ideas dissolve before those ideas were fully formed. No framework knowledge required.
agent_sessions:
  - ses_fe34898a8ffeBCmd08tVMgIkm1
---

At the last planning session, a colleague arrived with the plan already written.
Not a proposal, a plan: architecture sketched, tasks split, names attached.
My name was already next to item three.
I had thoughts about the design, and by the time I had organized them, the plan was the plan, and my thoughts had become comments on its edges.
**A team where one engineer directs every project has one engineer's worth of judgment, no matter how many people it employs.**

## The Plans Are Usually Good

I want to be fair to this colleague, because the easy reading is a story about an annoying person, and that is the boring reading.
His plans are good.
He is senior, he has watched systems fail in ways the rest of us have not, and when he points in a direction, things generally go well.
That is exactly what makes the pattern hard to see.
**Direction that produces good outcomes does not look like a problem; it looks like leadership, and the results keep re-electing him.**

The costs do not show up in the projects.
The projects ship.
The costs show up in the people, and in the team's capacity to think.

## Initiative Proposes, Direction Disposes

There is a line between taking initiative and taking over, and the line is not talent or effort.
The line is what happens to everyone else's ideas.

Initiative adds a proposal to the table.
Here is a design, here is a sketch of a plan, react to it, improve it, replace it.
Direction closes the table.
The plan arrives finished, the discussion becomes a review of details, and dissent gets metabolized as feedback on spacing.

A simple test: in the last three projects, did anyone else's plan win?
Not "influenced his plan".
Won.
**If only one person's plan can win, the team has stopped planning and started transcribing.**

## The Costs Land on the Team

The first cost is one I know personally, because I have measured it on myself: [work you did not choose takes longer](../the-cost-of-work-you-did-not-choose/index.md).
A task handed to you inside someone else's plan arrives without the pull that turns friction into a puzzle.
The one-day task that takes three days is often a team sport, and the director is usually its most enthusiastic player.

The second cost is quieter, and it compounds.
Judgment is a skill built by deciding, and a team where every design conversation ends before it starts is a team that never practices.
Then the director looks around, correctly, and observes that he is the only one who plans well.
The situation manufactures the evidence that justifies it.

The third cost is structural.
One person becomes the [bottleneck](../you-are-the-bottleneck/index.md) in the path of every decision, and the [bus factor](https://en.wikipedia.org/wiki/Bus_factor) of the team's thinking is exactly one.
When he is on vacation, decisions wait.
When he changes his mind, work reverses.

The fourth cost shows up in who stays.
People who joined to build things do not stay to execute things.
They drift toward teams where their plans can win, and their departures get read as proof that it is hard to hire people who can operate at his level.
Underneath all of this is psychological safety, the belief that you can voice a half-formed idea without it being steamrolled, which [Google's Project Aristotle](https://rework.withgoogle.com/print/guides/5727380657274880/) identified as the strongest predictor of team effectiveness.
A finished plan arriving at every meeting quietly teaches the opposite lesson.

## Why He Does It

This behavior is rarely simple ambition.
In my experience it is closer to anxiety wearing a productivity costume.

Somewhere, probably at a previous job, this person watched a project drift with nobody steering and smash into the rocks, and took the lesson to heart: if I do not direct this, it fails.
The lesson was learned about one team, in one year, and generalized into a theory of all teams, including teams that would have steered fine without him.

Organizations also train the behavior relentlessly.
The person who arrives with the finished plan is visible, promotable, and praised in every retrospective.
Nobody gets credit for the design they chose not to impose.
It is the engineer-level sibling of [micromanagement](https://en.wikipedia.org/wiki/Micromanagement), applied to plans instead of tasks, and it is rewarded for as long as the projects succeed.
**The engineer who directs everything is usually the output of a system that pays for direction and never pays for restraint.**

## What I Will Do Differently

I will not win by out-planning him, and I will not fix him.
Both of those are the same mistake in different clothes: treating the situation as a contest of strength.

What moves the situation:

Name the pattern early, without heat.
"I noticed the plan arrived finished, and I would like the next one to start as questions" attacks the pattern, not the person, and it is much easier to say before the third project than after the tenth.

Ask for proposals, not verdicts.
When direction arrives as "we should do X", ask for it in writing as a proposal the owners can accept, amend, or reject.
A written proposal is still an act of initiative; the difference is that other hands can now touch it.

Make ownership explicit before planning starts.
I have written before about what happens when [everything already has an owner](../everything-already-has-an-owner/index.md), and the inverse is just as true: work with no owner is a vacuum, and vacuums get filled by whoever arrives first, which is him, every time.
If the owner is known before the session, the director has someone to advise instead of a vacuum to fill.

Give the team the first pass.
Rotate design authorship so the person who owns the work writes the first design, and the director reviews.
Reviewing is a real contribution, and it is different from deciding; separating the two roles is most of the fix.

And if none of that moves it, take the pattern to the manager with evidence of cost rather than a story of annoyance.
"In the last six months, no one else's plan has won" is a fact a manager can act on.

He is not the villain, and his opinions are not the problem; his opinions are good.
**The problem is that a team is a machine for combining judgments, and ours is running on one cylinder.**
I do not need him to stop thinking.
I need a team where the best plan can come from anyone, because the alternative is a team of one with nine spectators.

## See also

- [The Cost of Work You Did Not Choose](../the-cost-of-work-you-did-not-choose/index.md) - the motivation tax on tasks assigned inside someone else's plan, the downstream cost of constant direction
- [Everything Already Has an Owner](../everything-already-has-an-owner/index.md) - the contested-claim side of the same ownership dynamics
- [When Engineers Disagree on Best Practices](../when-engineers-disagree-on-best-practices/index.md) - how a team decides matters more than what it decides, the meta-skill a director short-circuits
- [You Are the Bottleneck](../you-are-the-bottleneck/index.md) - the structural view of one person standing in every path

## References

- [Wikipedia, "Bus factor"](https://en.wikipedia.org/wiki/Bus_factor) - the concentration-risk view of one person holding all the critical knowledge
- [Wikipedia, "Micromanagement"](https://en.wikipedia.org/wiki/Micromanagement) - the management variant of the same pattern, applied to tasks instead of plans
- [Google re:Work, "Guide: Understand team effectiveness"](https://rework.withgoogle.com/print/guides/5727380657274880/) - Project Aristotle's finding that psychological safety is the top predictor of team performance
