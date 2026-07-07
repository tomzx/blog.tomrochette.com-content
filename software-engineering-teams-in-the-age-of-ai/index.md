---
title: "Software Engineering Teams in the Age of AI: Smaller, Sharper, Intentionally Imperfect"
created: 2026-05-18
type: post
status: finished
tags: [ai, software-engineering, llm, team-management, productivity, fully-ai-generated, llm=glm-5.1]
readability: 4
---

LLM-powered coding assistants have changed what an individual engineer can produce in a day.
The harder question is what this means for how teams should be organized, how they should work together, and which of their existing processes still earn their keep.
The answer is counterintuitive: the teams that thrive will not be the ones that adopt AI fastest or eliminate the most process.
They will be the ones that correctly distinguish between friction that wastes time and friction that prevents mistakes.

## What Actually Changed

AI-assisted development compresses the time from idea to working code.
An engineer with a capable LLM can prototype a feature in hours that used to take days.
Boilerplate, tests, documentation scaffolding, and CRUD endpoints all move closer to free.

But the things that remain expensive have not changed at all.
Deciding whether to build a feature, choosing the right abstraction, understanding the domain deeply, and aligning technical work with business goals are as hard as they ever were.
In many ways they are harder now, because the temptation to just generate and ship is stronger.

This creates a specific tension for teams.
When individuals can produce more code, the bottleneck shifts from production to coordination and judgment.
Team design has to account for this shift, not ignore it.

## Team Size: Follow the Problem Boundary

There is a persistent urge to declare an ideal team size.
Amazon popularized the "two-pizza team" heuristic.
Agile methodology settled on 3 to 9.
Various management frameworks have their own magic numbers.

AI does not provide a new magic number, but it does tilt the calculus toward smaller teams.

Here is why.
Communication overhead scales quadratically with team size.
A team of 4 has 6 communication channels.
A team of 8 has 28.
When each individual ships faster because of AI assistance, the team hits the coordination ceiling sooner.
The marginal output of the fifth or sixth engineer starts getting eaten by the cost of keeping everyone aligned.

Smaller teams also benefit from clearer ownership.
When three people own a service, there is no ambiguity about who is responsible for it.
When ten people own it, everyone assumes someone else is handling the monitoring, the tests, the deployment pipeline.

But smaller is not always better, and this is where the nuance matters.

A team that is too small for its domain will fragment its attention across too many concerns.
Three engineers trying to own a payments system, a notification platform, and a data pipeline will do none of them well.
They will produce code quickly with AI assistance, but they will produce the wrong code, in the wrong abstractions, because no one has the mental space to think deeply about any one domain.

The right heuristic is not a fixed number.
It is the smallest team that can own a coherent domain end-to-end.
In practice this often lands between 3 and 5 people, but the number should follow the problem boundary, not the other way around.

A team of 3 that owns a single well-bounded service is better than a team of 8 that owns six loosely related ones.
But a team of 6 that owns a genuinely integrated platform is better than splitting that platform across two teams of 3 that now have to coordinate across a boundary that should not exist.

## Friction: Some of It Is Load-Bearing

The instinct when a new efficiency tool arrives is to use it to remove every source of friction.
AI makes code review faster, so why not automate it?
AI can summarize meetings, so why not eliminate them? AI can write documentation, so why not stop requiring it?

This instinct is partially right.
A lot of process friction is genuine waste.
Waiting three days for a manager to approve a deployment that could be automated.
Holding a 30-minute standup where eleven people say "yesterday I worked on tickets, today I will work on tickets."
Filing a Jira ticket for a one-line config change.

But some friction serves a purpose, and removing it silently degrades the team's output quality over time.

Code review is the clearest example.
Before AI, code review served multiple functions: catching bugs, enforcing style, sharing knowledge, and forcing the author to think about their code one more time before it shipped.
AI can handle the style and formatting portion completely.
It can catch obvious bugs.
What it cannot do is evaluate whether the code solves the right problem, whether the abstraction will survive the next feature request, or whether the approach is consistent with how the rest of the system works.

In fact, code review becomes more important with AI-generated code, not less.
When a human writes every line, you can assume they thought about each line at some level, even if imperfectly.
When an LLM generates code, the author may not have read every line carefully.
The reviewer can no longer rely on the author's intent as a safety net.
They have to verify both correctness and intent independently.

This is harder work than traditional code review.
It means reviews should be slower, not faster.
The process should have more friction, not less.
What should change is what the friction is applied to: less time on style, more time on substance.

The same principle applies to other forms of deliberation.

Sprint planning, done well, is the moment when the team asks "are we working on the right things?"
That is productive friction.
Sprint planning, done poorly, is an hour of reading ticket descriptions aloud.
That is waste.

Architecture discussions are productive friction when they prevent the team from building on a flawed foundation.
They are waste when they become philosophical debates that never converge on a decision.

The discipline is in telling the difference.
A useful test: does this process force someone to think about something they would otherwise skip?
If yes, keep it, even if it feels slow.
If no, automate it or remove it.

## Processes Worth Keeping

Beyond code review, a few processes become more valuable in an AI-accelerated environment.

**Architecture decision records (ADRs).**
When code is cheap to produce, the cost of building on the wrong abstraction is disproportionately high.
A one-page document that captures what was decided, why, and what alternatives were considered is worth more than the five minutes it takes to write.
AI can draft these from a conversation, but the team still needs to have the conversation.

**Incident retrospectives.**
These are one of the few processes that compound knowledge over time.
When a production incident occurs, the team that writes down what happened, why, and what they will change gets progressively harder to break.
The team that fixes the bug and moves on repeats the same class of mistake forever.
AI can assist with drafting the timeline from logs and alerts, but the insight about what to change has to come from the people who were in the room.

**Onboarding.**
This is paradoxically harder in AI-heavy teams.
Historically, junior engineers built deep familiarity with a codebase by writing code in it, struggling with its conventions, and learning its quirks through repetition.
When AI handles much of the writing, that struggle disappears, and with it, the learning.
Teams need to be more intentional about how they transfer knowledge.
Structured pairing, documented design decisions, and explicit mentorship become more important, not less.

**Specification before implementation.**
The ability to write a clear specification is now the highest-leverage skill in software engineering.
A precise spec turns an LLM from a mediocre pair programmer into a highly effective one.
A vague spec turns it into a hallucination engine.
Teams that invest in specification quality will outproduce teams that skip straight to prompting.

## Processes Worth Eliminating

Some processes survive on inertia alone.
AI gives permission to rethink them.

**Status meetings that are not decisions.**
If a standup is just a round-robin of activity reports, replace it with an AI-generated summary of yesterday's commits, PRs, and tickets.
Reserve synchronous time for discussions that require back-and-forth.
Most status updates do not.

**Granular task estimation.**
When AI can generate implementation drafts, estimating individual tasks in story points becomes less accurate and less useful.
The time spent decomposing work into one-point, two-point, and three-point tickets is time not spent on the actual work.
Replace granular estimation with outcome-level planning: what do we want to ship this cycle, and are we on track?

**Manual test writing for boilerplate.**
AI handles test scaffolding well.
Engineers should focus on test design (what cases matter, what edge cases exist, what invariants must hold) and let the tooling handle the mechanical work of writing assertions and setup code.
The test plan is the valuable artifact.
The test file is increasingly a commodity.

**Elaborate approval workflows.**
If a change passes CI, passes automated security scanning, and passes peer review, it should not also need approval from a manager who has not read the code.
Every gate that does not add information is pure delay.

## The Structure of a Team That Gets This Right

Bringing these threads together, the team that is well-designed for this era looks something like this.

Four or five people who own a clear domain.
They spend less time writing boilerplate and more time debating trade-offs.
Their code reviews are rigorous about intent and lightweight about style.
They write ADRs for non-obvious decisions and skip them for obvious ones.
They do not hold meetings that could be a paragraph of text.
They write specifications before they prompt.

They treat AI as an amplifier of judgment, not a replacement for it.
The judgment is still the team's job.
The tooling just makes the execution of that judgment faster.

## What Does Not Change

For all the shifts, some things are stubbornly constant.

Trust between team members cannot be generated by a language model.
Psychological safety, the ability to say "I think this approach is wrong" without fear, remains the single strongest predictor of team performance.
A team of mediocre engineers who trust each other will outperform a team of brilliant engineers who do not, with or without AI assistance.

Shared understanding of the problem domain cannot be delegated to tooling.
If no one on the team deeply understands the business context, the code will be technically correct and strategically wrong, faster than ever.

And the discipline to build less, not more, remains the hardest skill.
When implementation is nearly free, the temptation to overbuild is constant.
The teams that thrive will be the ones where someone at the table says "we don't need this," and the rest of the team listens.
