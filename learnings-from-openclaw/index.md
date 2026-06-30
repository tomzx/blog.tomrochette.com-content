---
title: "Read the Commits, Not the Manual: What OpenClaw's Git History Reveals About Scaling a Project"
created: 2026-06-30
type: post
status: finished
tags: [open-source, software-engineering, git, llm, ai, code-review, agents, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader has run `git log` on a project they did not build, has participated in a multi-maintainer open source project, and understands pull requests, conventional commits, and what an LLM coding agent is. No explanation of version control basics.
---

The most honest document a software project writes is not its `README`, its `CONTRIBUTING.md`, or its architecture diagram.
It is its commit history, because the commit history is the one artifact the project cannot rewrite after the fact.
**A process doc describes the project the maintainers wish they were running, and the commit log describes the project they are actually running, and the gap between the two is where every real lesson lives.**

I spent time inside the git history of [OpenClaw](https://github.com/openclaw/openclaw), a self-hosted personal AI assistant that talks to you across roughly two dozen messaging channels.
It is an extreme specimen, and extreme specimens are the most legible ones.
In about seven months it accumulated over sixty-two thousand commits from more than three thousand contributors, which is somewhere close to two hundred and ninety commits a day, every day, since its first commit.
That is a throughput at which most projects would have collapsed into an unreadable knot, and it did not.
The interesting question is why, and the commit history answers it more clearly than any roadmap could.

This article is a reading of that history, and the throughline is a single observation that the data makes impossible to miss.
A project's real architecture is not the dependency graph of its packages.
It is the role structure of the people who land commits on it, and OpenClaw reveals that role structure with unusual clarity because it is large enough that the patterns survive any individual's bad week.

## The First Thing the Commits Show: Two Kinds of Maintainer

Run a contributor breakdown on any mature project and you will find that the top commit counts are dominated by one or two names.
OpenClaw is no different.
The founding maintainer, Peter Steinberger, is listed in `CONTRIBUTING.md` as "Benevolent Dictator," and he accounts for well over half of all commits in the repository, roughly three times the next contributor.
The second name down is Vincent Koc, listed as owning "Agents, Telemetry, Hooks, Security."

You can read their titles and learn nothing, or you can read their commits and learn everything.
**The commit prefix and the merge behavior are the two signals that tell you what a maintainer actually does all day, and at OpenClaw they tell two completely different stories.**

Roughly ninety-five percent of Peter Steinberger's recent commits land straight on `main` with no pull request at all.
His work spans every conventional-commit prefix in roughly equal measure: `test:`, `fix:`, `docs:`, `ci:`, `refactor:`, `perf:`.
His scopes are the product itself, the agents, the gateway, the release machinery, the high-traffic channels.
Read his last two hundred commits and you are watching someone build outward, exploring whatever he finds interesting that week, shipping releases, writing the docs for features he just invented, and rarely pausing to open a pull request against his own work.

Vincent Koc's history is the mirror image.
His recent work is almost sixty percent `fix` commits, and his scopes are a completely different surface: end-to-end tests, the QA lab, scripts, CI, and a scope that appears nowhere near the top of Peter's list, `deadcode`.
He opens pull requests.
He uses the review process.
Where Peter's commits read as exploration, Vincent's read as consolidation.

This is the observation that triggered this article, and the temptation is to read it as a process failure on Peter's part, the founder cutting corners, ignoring the queue, doing whatever he wants.
That reading is wrong, and it misses the point.
**The two patterns are not the same job done at different levels of discipline.
They are two different jobs, and a project of this size needs both of them to survive.**

## The Benevolent Dictator and the Steward

Strip the moral framing away and what you are looking at is a role separation so fundamental that every healthy long-lived project eventually rediscovers it, whether it documents the split or not.

One role is the visionary, the person whose job is to push the frontier outward.
They build features that no user has asked for yet, because no user knows to ask for them.
They write docs in the same commit as the code, because to them the doc is part of the feature.
They commit straight to `main` because the bottleneck they are optimizing for is their own momentum, and stopping to open a pull request against themselves would be pure ceremony.
This person does not read the issue tracker for direction.
They read it, when they read it at all, for confirmation that the thing they already wanted to build has some demand.
Their commits are the product roadmap, written in real time.

The other role is the steward, the person whose job is to keep the frontier from collapsing behind the visionary.
They fix the bugs the new features introduced.
They write the end-to-end tests that prove the feature actually works under load.
They remove the dead code the visionary left behind when they pivoted.
They route pull requests from the long tail of contributors through review, because someone has to, and the visionary will not.
Their commits are almost entirely `fix`, `test`, `refactor`, `chore`, and they open pull requests not out of greater virtue but because their work touches shared, load-bearing surface where a mistake costs everyone.

**The visionary produces the entropy that makes the project grow, and the steward does the work that keeps the entropy from being fatal, and neither role is superior to the other.**
A project with only visionaries ships exciting broken things that no one can depend on.
A project with only stewards stays clean and slowly dies, because no one is building the thing anyone wants to use next.
OpenClaw has both, in volume, and that is the first and most important reason it has not collapsed under its own commit rate.

The practical lesson, if you run a project, is to name this split out loud instead of letting it generate resentment in silence.
The most common failure mode is a steward who slowly concludes that the visionary is careless, and a visionary who slowly concludes that the steward is a brake on progress, when in fact each is doing exactly the job the other cannot.
Peter's direct-to-`main` habit is not a defect Vincent is tolerating.
It is the signature of a role, and recognizing it as a role is what stops it from becoming a feud.

## The Specialist Roles That Only Appear at Scale

Past the two primary roles, the commit history surfaces two more contributors whose work is so specialized it would be invisible in a smaller project, and whose existence is itself a signal of size.
**A project small enough for everyone to do a bit of everything has no specialists, and the appearance of specialists is the commit-history fingerprint of a project that has grown past the point where generalists can cover the surface.**

The third most prolific contributor, going by Shakker, has roughly four thousand commits, and about two thirds of them are `test:`.
There is almost no feature work in the history.
This is a person whose entire contribution is the safety net, the test fixtures, the regression coverage that lets everyone else move fast without the product silently breaking.
A visionary cannot do this work, because it requires the patience to write the hundredth test for a path the fortieth test already almost covered, and a steward is usually too busy putting out active fires to write tests prophylactically.
The test author is a third role, and it is the role that converts the steward's fixes from one-off patches into guarantees that do not have to be re-earned.

Further down the list, Tak Hoffman has a thousand-plus commits, and he owns a scope that appears in almost nobody else's history: `(regression)`.
Of the hundred-plus commits in the repository tagged `fix(regression):`, almost all of them are his.
This is a regression hunter, someone whose beat is not bugs in general but bugs in things that used to work, the specific class of defect that erodes user trust faster than any missing feature can build it.
Regression hunting is a discipline of its own, because it requires holding a mental model of how the system used to behave and noticing when a change has quietly violated it, and it is the kind of work that only gets staffed deliberately once a project is large enough that the founding maintainer can no longer hold the whole behavior graph in their head.

The lesson is that the visionary-and-steward split is a starting frame, not a complete one.
As a project grows, the roles keep subdividing, and each subdivision is a person whose commits tell you, by their narrowness, exactly what the project is now too large to handle with generalists.
Read the contributors with unusual scope concentrations and you read the project's growing pains written out in advance.

## The Second Thing the Commits Show: The Real Architecture Is the Ownership Table

Three thousand contributors is a number at which coordination by conversation breaks down completely.
You cannot have a meeting with three thousand people.
You cannot maintain a shared mental model with three thousand people.
The only way a project absorbs that many contributors without descending into a pull-request traffic jam is to partition the work so thoroughly that most contributors never need to talk to each other at all.

OpenClaw does this with an explicit ownership table, and it is the most underrated document in the repository.
`CONTRIBUTING.md` lists roughly thirty maintainers, each with a named specialty: one owns Telegram, one owns the iOS app, one owns Memory, one owns the Discord subsystem, one owns Chinese channels and nothing else.
The instruction to contributors is blunt: "Do not guess who to tag," route through the ownership list, the label automation, and `CODEOWNERS` instead.

**When the surface area of a project exceeds what any one person can hold in their head, the only scalable architecture is a partition, and the partition has to live in a file, not in tribal knowledge.**
The plugin layout reinforces this from the code side.
There are around a hundred and forty-five extensions and only twenty-one core packages, and the project's own vision document states the principle outright: core stays lean, capabilities ship as plugins, and the bar for adding an optional capability to core is "intentionally high."

This is the same insight as the role split, applied at the level of the codebase rather than the people.
You cannot hold one hundred and forty-five channel adapters in your head, but you do not have to, because each one is owned by one person who only has to hold one in theirs.
The partition is the architecture, and the ownership table is the partition made durable.
A project that grows past a few active contributors without writing this table down is a project that will discover, painfully, that the absence of an ownership map is itself an architecture, an architecture in which the loudest reviewer owns everything by default.

## The Third Thing the Commits Show: Every Rule Is a Scar on Reviewer Time

The contribution rules in OpenClaw are unusually specific, and a first-time reader will find some of them almost hostile.
There is a hard cap of twenty open pull requests per author, enforced automatically, past which your pull requests are labeled and closed.
Refactor-only pull requests are refused outright.
Test-only or CI-only pull requests that chase a known `main` failure are refused outright.
Pull requests over roughly five thousand changed lines are reviewed "only in exceptional circumstances."
One pull request must equal one issue or topic.

Read in isolation these read as pettiness.
Read as a group they are the scars of a specific, recurring wound, and the wound is always the same.
**Every one of these rules is a response to something that once drained reviewer attention without producing proportional value, because reviewer attention is the single scarcest, least-elastic resource a project at this scale has.**

The visionary can always produce more commits.
The contributor pool can always produce more pull requests.
Neither of those can produce more maintainer-hours for review, and so the entire rule set is engineered to protect that one bottleneck.
The twenty-pull-request cap exists because batch-opened pull requests impose review cost in proportion to their number, not their value.
The ban on refactor-only work exists because a refactor that changes no behavior consumes review to confirm it changes no behavior, which is review spent proving a negative.
The line limit exists because a five-thousand-line diff cannot actually be reviewed by a human, it can only be rubber-stamped, and rubber-stamping is the failure mode the gate is supposed to prevent.

This is the theory of constraints applied to a volunteer workforce.
When you cannot add capacity at the bottleneck, the only lever left is to choke the demand arriving at it, and you choke demand by making rules that reject the classes of work that waste the bottleneck's time.
A rule that reads as harsh to a contributor is almost always a rule that reads as triage to a maintainer who has been doing the job long enough to know which inputs are waste.

## The Fourth Thing the Commits Show: They Dogfood the Future of Development

OpenClaw builds an AI agent, and it builds it with AI agents, and the commit history makes the second fact as visible as the first.

Bot accounts appear throughout the contributor list.
The contribution guide treats AI-authored pull requests as first-class citizens, requiring only that they be marked, with a checklist that asks for the model, the prompt or session log, and a human confirmation that the code is understood.
Codex review is not an experiment, it is described as the "current highest standard of AI review," expected to run on every pull request and to be addressed by the author before a human reviewer is ever bothered.

The reason this matters is not that it is futuristic.
It is that it is a live, working answer to the question every team is now fumbling with, which is how to integrate generated code without being flooded by it.
**The OpenClaw answer is not to ban generated contributions and not to blindly trust them, but to treat their provenance as a required signal and to route that signal into both the review and the reviewer.**

This is exactly the provenance argument I made, from the maintainer's side, in [Triaging Open Source Pull Requests](../triaging-open-source-pull-requests/index.md): the one piece of information a reviewer most needs about a modern pull request is which model produced it and what prompt produced it, because that is the information that tells you which blind spots to check for.
OpenClaw asks for exactly that, up front, in the template, and it pairs the request with an automated review pass that can be calibrated against the disclosed model.
That pairing, disclosure plus targeted automated review, is the most credible workflow I have seen for accepting generated code at volume, and it is sitting right there in a `CONTRIBUTING.md` that most projects have not yet caught up to.

## How to Read a Project This Way Yourself

The method that produced these observations is generalizable, and it costs you nothing but a terminal.
You do not need access to a project's Slack, its planning board, or its maintainers' intentions.
You need its git history and three commands.

Start with the contributor breakdown, `git shortlog -sne`, and look at the ratio between the top name and everyone else.
A project whose top contributor dwarfs the rest is a project whose direction is set by one person, and everything else is execution.
A project whose top contributors are close in volume is a project run by committee, and its commits will read as negotiation rather than vision.

Then take the top two or three names and compare their conventional-commit prefixes, `git log --author=... --format=%s`, grouped by prefix.
The ratio of `fix` to `feat`, the presence or absence of `docs` and `test`, the dominance of `refactor` or `chore`, these tell you who builds and who maintains, and they tell you in five minutes what would take a month of standups to learn.
A maintainer whose commits are sixty percent `fix` is a steward.
A maintainer whose commits span every prefix evenly is a visionary.
**The prefix distribution is a fingerprint of a role, and reading it is faster and more honest than reading anyone's job title.**

Finally, count how many of each top contributor's commits reference a pull request versus landing straight on `main`.
This is the governance signal.
A project where even the founder routes through pull requests is a project run by process.
A project where one person lands on `main` freely and the rest use pull requests is a project that has, whether it admits it or not, a benevolent dictator and a steward, and the rest of the contribution rules will make sense once you see the split.

Run this on your own project before you run it on anyone else's.
You may find that the role structure you assume you are running is not the one your commits describe, and the gap is the first thing worth fixing.

## What to Do on Monday

If you maintain a project, take an hour and read your own commit history the way this article reads OpenClaw's.
Find your visionary and your steward, and if you do not have both, that is the single most important hiring or delegation decision in front of you.
A project with no steward is slowly dying behind a pile of un-merged fixes and unread pull requests, and no amount of feature velocity will save it.

Write down your ownership table, explicitly, in a file, even if it is just three names today.
The day you have thirty contributors is too late to invent the partition, because by then the loudest reviewer will have quietly become the owner of everything, and unwinding that is a political problem rather than a documentation one.
The partition is cheap to write early and expensive to write late.

Audit your contribution rules as a set, not individually.
Every rule that reads as harsh to a contributor should correspond to a specific class of work that once wasted your review time.
Any rule you cannot trace back to such a wound is a rule that is probably driving contributors away without earning its cost, and it is a candidate for deletion.

## See also

- [The Codebase Gardener](../the-codebase-gardener/index.md) - the team-codebase argument that standards must be encoded where work passes through them, which is the lens this article uses to read OpenClaw's rules as reviewer-time conservation
- [Triaging Open Source Pull Requests](../triaging-open-source-pull-requests/index.md) - the provenance argument this article extends: when the reviewer knows which model wrote a pull request, they know which blind spots to check, and OpenClaw's disclosure template is a working implementation of it
- [The Merge Gate](../the-merge-gate/index.md) - the case for gating on the blast radius of a change rather than the existence of a pull request, which is the principle behind OpenClaw's line limits and its refusal of refactor-only work
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - why a machine-checked constraint outperforms a tired human scan, the premise behind treating Codex review as the default standard
- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) - which friction is load-bearing and which is waste, the distinction that explains why OpenClaw's harsh rules are the former and not the latter

## References

- [OpenClaw on GitHub](https://github.com/openclaw/openclaw) - the repository whose commit history, CONTRIBUTING.md, and VISION.md are the primary sources for every observation in this article
- [Wikipedia, "Theory of Constraints"](https://en.wikipedia.org/wiki/Theory_of_constraints) - Goldratt's framing for why you protect the bottleneck rather than adding effort elsewhere, the basis for reading OpenClaw's rules as reviewer-time conservation
- [Wikipedia, "Benevolent dictator for life"](https://en.wikipedia.org/wiki/Benevolent_dictator_for_life) - the canonical name for the role OpenClaw's commit history reveals in its top contributor, independent of any title
