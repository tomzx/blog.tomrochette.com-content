---
title: "When Engineers Disagree on Best Practices: Surviving the Forming Stage"
created: 2026-06-17
type: post
status: finished
tags: [software-engineering, team-management, decision-making, conflict-resolution, fully-ai-generated, llm=glm-5.2]
readability: 3
---

A new team's first disagreement about best practices is not a warning sign.
It is the moment the team actually starts becoming a team.
What separates teams that survive this phase from those that stall is not which practices they adopt, but how they resolve the disagreement.

## Why the Forming Stage Produces Disagreement

Every engineer arrives carrying a backpack full of practices that worked somewhere else.
The testing strategy that saved your last team from weekly regressions.
The code review checklist that caught the security bug before it shipped.
The branching model that kept releases sane.
These are not random preferences.
They are scar tissue from real failures, and the engineer who brings them believes, correctly, that they matter.

The problem is that every other engineer on the new team arrives with their own backpack, full of different scar tissue, formed by different failures.
When these backpacks collide, you get the pattern Bruce Tuckman described in his 1965 study of small-group development: [forming, storming, norming, performing](https://en.wikipedia.org/wiki/Tuckman%27s_stages_of_group_development).
Teams do not skip from forming straight to performing.
They pass through storming, the phase where members test each other, surface conflicting assumptions, and negotiate how work should be done.

The forming stage is uniquely prone to practice disagreements for three reasons.

First, there is no shared history.
On an established team, conventions are settled and invisible.
The team just does things a certain way because that is how it has always been done.
A new team has no "always," so everything is up for debate at once.

Second, there is no established trust.
Disagreeing about code style feels low-stakes on a team where everyone has shipped together for a year, because everyone knows the argument is about the style, not about competence.
On a new team, the same disagreement can feel like a referendum on someone's expertise, because no one has yet proven anything to anyone else.

Third, there is no shared vocabulary for resolving conflict.
An established team has accumulated meta-norms: how they make decisions, who decides what, when to escalate, when to let something go.
A new team has none of this.
So every disagreement is also, simultaneously, a negotiation about how disagreements get resolved.

## Most "Best Practice" Debates Are Preference Debates

The first thing to recognize is that the phrase "best practice" is doing a lot of misleading work.
A best practice is a practice that is demonstrably better than its alternatives across most contexts.
Very few software engineering practices clear that bar.

Consider the debates that consume the most oxygen on a new team.
Tabs versus spaces.
Git Flow versus trunk-based development.
Story points versus no estimates.
Unit tests versus integration tests as the primary signal.
Commit message conventions.
These are not best practices.
They are conventions, and a convention's value comes almost entirely from being shared, not from being optimal.
**The team that uses the second-best testing framework consistently will outperform the team that uses the best one inconsistently.**

This does not mean all practices are equal.
Some debates involve genuine principles where the choice has lasting consequences: whether to build or buy a critical dependency, how much to invest in observability before shipping, whether a monolith or services is the right starting architecture.
These deserve real deliberation.
The skill is in telling the convention debate from the principle debate, because they require completely different resolution mechanisms.

## Reversible Versus Irreversible Decisions

A useful [distinction](https://en.wikipedia.org/wiki/Disagree_and_commit) maps directly onto this problem.
Some decisions are one-way doors.
Once you walk through, you cannot come back.
Choosing a primary database, committing to a cloud provider, or picking a framework that will permeate your codebase are one-way door decisions.
These deserve heavy deliberation, because the cost of being wrong is high and the cost of reversing is higher.

Most practice debates on a new team are two-way doors.
You can adopt trunk-based development, try it for six weeks, and switch back if it is not working.
You can pick a linter configuration, discover it fights your codebase, and change it.
**Two-way door decisions should be made quickly, because the fastest path to knowing is often to try.**

A new team that treats every practice debate as a one-way door will spend its first two months in meetings and produce nothing.
A team that treats a genuine one-way door as reversible will make a choice it regrets for years.
The discipline is in classifying the decision before debating it.

## The Experiment Mindset

The single most effective frame for resolving practice disagreement during forming is to treat practices as hypotheses, not as identities.

When two engineers disagree about whether to require code review before merge, the unproductive version of that conversation is an argument about whether code review is good.
Both people dig in, cite their favorite blog posts, and the discussion becomes about winning.

The productive version converts the disagreement into an experiment.
You require code review for the next month, track how many defects it catches in review versus in production, and look at the data together at the end.
Now the two engineers are not opponents.
They are co-investigators running the same experiment.

This works because it removes the requirement that someone be wrong.
An engineer who advocated for mandatory review does not lose face if the experiment shows it adds little value, because they ran the test in good faith.
An engineer who opposed it does not lose face if the experiment shows it catches real bugs, because they agreed to look at the evidence.

A few rules make experiments work.

Time-box them.
An open-ended experiment is just a delayed argument.
Four to six weeks is usually enough to see signal without exhausting the team's patience.

Define success criteria before you start.
If you wait until the experiment is over to decide what would count as success, you will re-litigate the original disagreement with data instead of opinions, which is only marginally better.

Keep the cost of reversal low.
If switching back after the experiment is expensive, the experiment is really a one-way door in disguise.

Write down the result.
A one-paragraph note recording what you tried, what you observed, and what you decided turns a single resolution into institutional memory that saves the next new team member from re-fighting the same battle.

## How You Decide Matters More Than What You Decide

Here is the point that is easy to miss when you are in the middle of a heated debate about, say, whether to use feature branches or trunk-based development.

The specific answer matters less than you think.
**What matters enormously, especially during the forming stage, is that the team builds a repeatable process for reaching decisions together.**

A team that resolves its first disagreement well, with a clear process, shared evidence, and a decision everyone can live with, has just created something more valuable than the practice it chose.
It has created the template for the next disagreement, and the one after that.
Each resolved disagreement makes the next one easier, because the meta-process is now familiar.

A team that resolves its first disagreement badly, by letting the loudest person win, or by avoiding the conflict until it festers, or by escalating to a manager who picks a winner, has also created a template.
That template will repeat.
**The first disagreement a new team faces is really a dress rehearsal for every disagreement that follows.**

This is why the forming stage deserves deliberate attention rather than the hope that things will sort themselves out.
The norms a team establishes in its first weeks are sticky.
They become "how we do things here," and once that identity forms, it is far harder to change than to set well in the first place.

## A Playbook for the First Disagreement

Concretely, when the first real practice disagreement surfaces on a new team, the following sequence works.

Name it.
Say out loud that this is a disagreement about practice, that disagreements are expected, and that the goal is to find a resolution the team can commit to, not to identify who is right.

Classify it.
Ask whether this is a convention debate, where value comes from consistency, or a principle debate, where the choice has lasting consequences.
Ask whether it is a one-way door or a two-way door.

For conventions and two-way doors, decide fast.
Default to whoever has to live with the consequence most directly, or to the option that is easiest to change, or to the existing convention if one already exists.
Time-box the decision to one conversation, not three.

For principles and one-way doors, slow down.
Write a short decision record capturing the options, the trade-offs, and the reasoning.
Get the right people in the room, which usually means the people who will own the consequences, not necessarily the people with the strongest opinions.

Either way, record the outcome.
A one-page architecture decision record or a paragraph in the team handbook turns a fragile verbal agreement into something a new hire can read six months later.

And then commit.
The principle of "disagree and commit" applies here.
Once the team has decided, even those who argued otherwise support the decision fully.
A practice executed with full commitment and an imperfect choice beats a better practice executed with resentment and inconsistency.

## When Someone Refuses to Commit

There is a failure mode worth naming.

Occasionally an engineer treats a practice debate as a hill to die on, refuses to accept the team's decision, and continues working the old way.
This is no longer a disagreement about practice.
It is a disagreement about whether the team's decision-making process has legitimacy.

This must be addressed directly, and early.
A team that tolerates a member who overrides collective decisions after they are made has no process at all.
It has a veto by the most stubborn person.
The conversation is no longer about the practice.
It is about participation in a shared system.

In a healthy forming team, this conversation is rare, because the process itself was fair enough that losing a debate does not feel like losing status.
When it does happen, resolving it cleanly, with empathy but without accommodation, is one of the most important trust-building acts the team will undertake.
Underneath that trust is psychological safety, the shared belief that you can speak up, dissent, and even be wrong without being humiliated, which [Google's Project Aristotle](https://rework.withgoogle.com/print/guides/5727380657274880/) identified as the single strongest predictor of team effectiveness.
A team cannot storm productively without it.

## The Payoff

A team that navigates its forming-stage disagreements well emerges with two assets.

The first is a set of shared conventions, probably imperfect, that let the team move fast without relitigating every choice.
The second, and more important, is a shared process for handling the next thing they do not yet agree on.

New disagreements never stop.
The codebase grows, the team grows, the technology landscape shifts, and yesterday's settled practice becomes tomorrow's debate.
The teams that handle this well are not the ones that picked the best practices on day one.
They are the ones that learned, during forming, how to disagree productively, decide efficiently, and commit fully.

That skill compounds for the life of the team.

## See also

- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) - team composition and which processes earn their keep under pressure
- [Principles](../principles/index.md) -- decision-making principles, including separating load-bearing friction from waste

## References

- [Wikipedia, "Tuckman's stages of group development"](https://en.wikipedia.org/wiki/Tuckman%27s_stages_of_group_development) - the forming-storming-norming-performing model that explains why early friction is structural, not pathological
- [Wikipedia, "Disagree and commit"](https://en.wikipedia.org/wiki/Disagree_and_commit) - documents the one-way/two-way door distinction and the disagree-and-commit principle for group decision-making
- [Google re:Work, "Guide: Understand team effectiveness"](https://rework.withgoogle.com/print/guides/5727380657274880/) - Project Aristotle's finding that psychological safety is the top predictor of team performance
