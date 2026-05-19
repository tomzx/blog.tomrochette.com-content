---
title: The case for static priorities
created: 2026-05-18
type: post
status: finished
tags: [priority, prioritization, planning, software-engineering, fully-ai-generated, llm=glm-5.1]
readability: 3
---

Most teams that adopt a P0-P5 priority scale make the same mistake: they treat priority as a ranking, not a classification.
The moment all P0s are resolved, someone suggests "promoting" P1s to P0.
This feels logical.
It is wrong.

## Priority is a property of the work, not its position in the queue

P0 means something specific: the production database is corrupted, customers cannot check out, a security vulnerability is being actively exploited.
P0 work has an operational definition.
It describes the *nature* and *consequence* of the task.

A P1 task is important work that should be done this quarter: a feature the largest customer has been requesting, a refactor that will unblock two teams, a performance optimization that will cut infrastructure costs by 30%.
Completing your P0s does not transform a P1 into an existential crisis.
The task has not changed.
Its urgency has not changed.
Calling it P0 adds no information and removes the ability to distinguish it from actual emergencies.

## If everything becomes P0, nothing is P0

Priority inflation is the fastest way to destroy a prioritization system.
Once your team learns that P0 simply means "next thing we're working on," the label stops meaning anything.
When a real P0 arrives, the database is on fire, you need everyone to drop what they are doing, the word no longer carries weight because it has been diluted by promotion.

Consider what happens when you tell a team "this is P0" in a healthy system: people stop what they are doing, context-switch, and focus on the emergency.
That response depends on P0 being rare and meaningfully different from everything else.
If your backlog contains forty items that were "promoted" to P0, the next real emergency gets the same response as a feature request.

## A static system is a shared vocabulary

The value of a priority scale is communication.
When an engineer files a bug as P1, a product manager should immediately understand the rough timeframe and severity without reading the full description.
When a support rep escalates a ticket to P0, the on-call engineer should know to wake up.

This shared understanding requires stable definitions.
If P0 means "site is down" on Monday but "most important remaining backlog item" on Wednesday, the label communicates nothing about the work itself, only about where it sits relative to other work.
That is what a sorted list already tells you.
The priority label should add something a list cannot: the *kind* of impact the task has.

## Why not use importance × urgency?

The Eisenhower Matrix (important/urgent, important/not urgent, not important/urgent, not important/not urgent) is the most common alternative to a priority scale.
It is appealing because it is simple: two dimensions, four quadrants, done.
But it breaks down in practice for several reasons.

**Everything your team is asked to do is important.**
If a task were truly unimportant, it would not be in the backlog.
This means most tasks cluster in the "important" row, and the entire burden of differentiation falls on the urgency axis.
You have effectively collapsed back to a single dimension, but with less granularity than P0-P5.

**Four buckets are too coarse.**
Within "important and not urgent" sits everything from "refactor the authentication system this quarter" to "update the README someday."
The quadrant gives you no way to distinguish these.
P0-P5 gives you six levels, each with an attached timeframe and commitment level.
The matrix tells you "schedule it."
The priority scale tells you "schedule it this quarter."

**Urgency is ambiguous at the boundaries.**
Is a customer feature request urgent because the customer is asking today, or not urgent because there is no deadline?
Is a tech debt refactor urgent because it slows down every sprint, or not urgent because nothing is currently broken?
These edge cases generate the same kind of debate that multi-dimensional systems create, but the matrix offers only two positions: urgent or not.
P0-P5 lets you express degrees of time sensitivity without a separate axis.

**The matrix is a decision framework, not a communication protocol.**
"Important and urgent" describes a reasoning process.
P0 describes a shared organizational response: drop everything, wake people up, ship a fix today.
The priority label carries both classification and implied action.
The matrix carries only classification, leaving the action unspecified.

The Eisenhower Matrix is a good tool for personal time management.
For team-scale prioritization of a shared backlog, a single priority scale with pre-agreed definitions communicates faster and differentiates better.

## Why not decompose into impact, urgency, and risk?

A related objection: instead of a single P0-P5 label, why not rate each task on multiple dimensions?
If each dimension only has two or three values, assessment is quick.

Assessment is indeed quick.
The problem is the decision rule.
Once you have `impact × urgency × risk`, you need a policy for how they combine: does high impact + medium urgency + low risk come before medium impact + high urgency + low risk?
Every disagreement becomes a debate about weights instead of a quick "this is P1" call.

The P0-P5 scale is that policy pre-baked.
Someone already decided the mapping.
The team classifies and moves on.

That said, if a team consistently disagrees on priority labels, that disagreement itself is useful.
It surfaces the underlying dimensions naturally.
The debate about impact, urgency, and risk is the conversation you have *when the single label fails*, not the default workflow.
A single priority label is the fast path.
Decomposed dimensions are the escalation path.

## Working on P1s does not require calling them P0

Here is the practical concern: after P0s are done, what do you work on?
P1s, obviously.
You do not need to rename them to start working on them.

A static priority system separates two decisions:
1. **What is this task?** (classification: P0 through P5)
2. **What should we work on next?** (scheduling: pick the highest-priority task that is unblocked and aligned with current goals)

Dynamic systems conflate these two decisions.
By making priority a function of the backlog state, you lose the ability to classify independently of schedule.
This means you cannot look at a task's priority and know what kind of work it represents.
You can only know where it ranked at the time it was labeled.

## Re-labeling has a real cost

Every time you promote items after completing higher-priority work, you pay a coordination cost.
Someone has to decide which P1s become P0s.
That decision requires a meeting, or at least a Slack thread, or a product manager's judgment call.
The larger the team, the more expensive this becomes.

In a static system, this cost is zero.
You finish P0s, you pick up the next highest-priority task, and you keep building.
No ceremony, no relabeling, no debate about whether this P1 has "earned" its promotion.

## Static priorities enable proportional allocation

Healthy teams do not just work on the highest-priority item.
They allocate capacity across priority levels: 10% on P0 (emergencies, when they arise), 60% on P1 (core roadmap), 20% on P2 (improvements), 10% on P3-P5 (maintenance, tech debt, experiments).

This kind of planning is only possible with stable definitions.
If P1s keep becoming P0s, you cannot reason about where your time is going.
Your velocity metrics become meaningless because the definition of each bucket shifts under you.

## Honest labeling forces honest conversations

A static system forces the team to be honest about what they are not doing.

In a dynamic system, everything important eventually becomes P0, so nothing is ever explicitly deprioritized.
A stakeholder asks "when will you do X?" and the answer is "it's P1, we'll get to it after the current P0s."
This is honest but uncomfortable.
The discomfort is the point.

When a P2 feature stays P2 for three quarters, the organization has a clear signal: this work is not important enough to displace P1 work.
That signal triggers a useful conversation: should we increase staffing, should we drop the feature, or should we accept that it will not happen soon?

In a dynamic system, that feature would have been promoted to P1, then P0, and done without anyone confronting the question of whether it was worth doing at all.

## When priorities *should* change

A static system does not mean priorities are frozen forever.
Priorities should change when the *task itself* changes, not when the backlog above it empties.

A P2 performance issue becomes P1 when a major customer threatens to churn over it.
The task's context changed.
A P3 experiment becomes P1 when early results show it could replace a critical dependency.
New information arrived.
A P1 feature becomes P0 when a competitor launches it and your sales team starts losing deals.
The market shifted.

These are legitimate priority changes because the nature and consequence of the work actually changed.
They are not promotions based on queue position.

## The scale

For reference, a well-defined static scale looks something like this:

- **P0**: Critical. Production is down, data is at risk, or customers are blocked. Drop everything.
- **P1**: High. Important work with clear business impact. Should be done this quarter.
- **P2**: Medium. Valuable but not time-sensitive. Should be done within the next two quarters.
- **P3**: Low. Nice to have. Will do if capacity allows.
- **P4**: Minimal. Logged for consideration. No commitment to do.
- **P5**: Rejected or deferred indefinitely. Kept for historical reference.

Each level describes a timeframe, a level of commitment, and a resource allocation.
None of these definitions reference other tasks in the backlog.

## What to do instead of promoting

When you finish your P0s and start working through P1s, do not relabel.
Instead:

1. **Sort P1s by dependencies and impact.** Within a priority level, use a secondary criterion to decide order.
2. **Pick the top P1 and start.** No ceremony needed.
3. **If you run out of P1s, start on P2s.** The system is working as intended.

The priority label told you this was important-but-not-critical work.
It still is.
The fact that nothing more urgent remains does not change its nature.

## The one-sentence version

Priority describes what a task *is*, not when you will get to it.
Keep the label stable, sort within levels, and let the schedule be the schedule.
