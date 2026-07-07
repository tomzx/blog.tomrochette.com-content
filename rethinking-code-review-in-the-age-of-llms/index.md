---
title: "Rethinking Code Review in the Age of LLMs"
created: 2026-06-12
type: post
status: finished
tags: [ai, software-engineering, code-review, llm, productivity, fully-ai-generated, llm=glm-5.1, llm=glm-5.2]
readability: 3
---

Code review is a bottleneck.
**I am no longer convinced it is a useful one.**

This is not a conclusion I arrived at lightly.
Code review has been one of the most reliable quality gates in software engineering for decades.
But the assumption underlying code review, that a human reading code before it ships catches meaningful problems, is worth re-examining when most of that code was written by an LLM.

## What Code Review Was Supposed to Do

Code review served several purposes simultaneously.

It caught bugs before they reached production.
It enforced consistency across a codebase.
It spread knowledge between team members.
It forced the author to organize their thoughts before presenting them to a peer.

Each of these purposes assumed something important: that the person who wrote the code and the person reviewing it were both human, that the author had thought carefully about each line, and that the reviewer could rely on the author's intent as context.

**When an LLM writes the code, these assumptions break.**

The LLM did not think carefully about each line.
The LLM does not have intent in the way a human does.
The reviewer cannot ask the author "what were you trying to do here?" and get a meaningful answer, because the author is a statistical model that generated the most probable next token.

This changes the nature of the review fundamentally, and not in the direction most people assume.

## Why Reviewing LLM Code Is Different

When a human writes code, code review is a conversation between two people who share a mental model.
The reviewer can trust that the author made deliberate choices, even imperfect ones.
Differences between what the reviewer expects and what the code does are interesting signals, because they represent a gap between two human understandings of the same problem.

**When an LLM writes code, there is no shared mental model.**
The code is the output of a pattern-matching process.
Sometimes it is correct.
Sometimes it is subtly wrong in ways that look correct.
Sometimes it is obviously wrong.

The reviewer's job shifts from "does this match the author's intent?" to "does this do what I want?"
This sounds like the same question, but it is not.
The first question allows the reviewer to leverage the author's reasoning.
The second question requires the reviewer to independently verify every assumption the code makes.

**This is harder, more tedious, and less effective than reviewing human-written code.**
The reviewer is not building on the author's thinking.
They are reconstructing it from scratch, line by line.

## The Bottleneck Argument

Here is the practical problem.

LLMs can generate code orders of magnitude faster than humans can review it.
A developer who used to spend six hours implementing a feature might now spend thirty minutes prompting an LLM and one hour reviewing the output.

**The ratio of review time to implementation time has inverted.**
Where review used to be a small fraction of the development cycle, it is now the dominant fraction.

And the quality of that review is worse, not better, because reviewing code you did not write is cognitively different from reviewing code you understand deeply.

This creates a specific kind of bottleneck: one where the throughput-limiting step is also the lowest-quality step.
**You are spending most of your time on the part of the process where you add the least value.**

## What I Would Rather Be Doing

If I am going to spend my limited cognitive budget, I want to spend it on the decisions that matter most.

Deciding which problems to solve.
Understanding whether a feature should exist at all.
Designing the boundary between components.
Choosing the right abstraction for the domain.
Thinking about how users will actually interact with what we build.

These are high-leverage activities.
They determine whether the code that gets written is useful, not just correct.

Reviewing LLM-generated code for style, naming conventions, and obvious bugs is low-leverage work.
An automated tool can do it faster and more consistently than I can.
A linter does not get tired.
An automated test suite does not lose focus after the third function.

**The hours I spend reviewing code that an LLM wrote are hours I am not spending on the problems that only a human can solve.**
That trade-off did not used to exist, because writing code and reviewing code were both human activities and the time allocation was roughly balanced.
Now the balance is broken, and the opportunity cost of review is much higher.

## Why Automatic Review and Approval Make Sense

I have no objection to automated code review.
I have no objection to automated PR approval.

**The instinct to keep a human in the loop for every change is driven by fear, not by a rational assessment of what the human actually contributes at that point in the process.**

Consider what a good code reviewer does today.
They check that tests pass.
They look for obvious bugs.
They verify naming conventions.
They ensure the change aligns with the stated goal.

**Every one of these checks can be automated.**
Tests pass or they do not.
Static analysis tools catch bugs more reliably than tired humans scanning diffs.
Linters enforce style more consistently than any reviewer.
Alignment with the stated goal can be checked by having an LLM compare the PR description with the actual changes.

## The Wrong Stage to Catch Subtle Issues

The remaining argument for human review is that humans catch subtle issues that automated tools miss: architectural problems, subtle security vulnerabilities, misunderstandings of the domain.

These are real concerns, but they are not best addressed at the PR level.
They are best addressed at the specification level.
If you write a precise specification, automated verification can confirm the implementation matches it.
If the specification is vague, no amount of human review will save you from building the wrong thing.

Some would argue that catching these issues during review is better than not catching them at all.
This is hard to disagree with in isolation.
Of course a subtle bug caught at review is better than the same bug reaching production.

But this framing hides the real trade-off.
The question is not whether review catches some problems.
It is whether review is the best place to catch them, and whether the time spent reviewing could catch more problems if spent elsewhere.

When you catch an architectural flaw at review time, the code is already written.
Fixing it means rework, rebase, re-test, re-review.
Catching the same flaw during specification costs a conversation.
The later you catch it, the more expensive it is, and code review is one of the latest stages in the pipeline.

More importantly, relying on review to catch subtle issues is unreliable by design.
A human reviewer catches what they happen to notice, when they happen to be alert, on the changes they happen to read carefully.
Some issues get caught.
Many do not.
**You are depending on luck and attention, not on a system.**

The alternative is to build the catching into the system itself.
A precise specification catches architectural misunderstandings before code exists.
A comprehensive test suite catches behavioral bugs on every run, not just when a reviewer is paying attention.
Static analysis catches security patterns deterministically.
Each of these catches issues systematically, on every change, forever.

Review catches issues once, for the reviewer who happens to be in front of the diff.
A good test catches the same class of issue every time it runs, for as long as the codebase exists.
If you find the same kind of subtle issue during review more than once, the answer is not to keep reviewing harder.
**The answer is to encode that check into your automated gates so it never depends on a human noticing again.**

"Catching it late is better than not catching it" is true.
**It is also an argument for accepting a process that catches too little, too late, at the highest possible cost.**

**The review should happen before the code is written, not after.**
Spend the human effort on the spec.
Let the machines verify compliance.

## The Quality Maximization Myth

Some would argue that this misses the point.
The goal of code review is not just to check gates, it is to make the code the best it can be.
A good reviewer suggests a cleaner abstraction, spots a performance issue the author missed, proposes a name that communicates intent better.
Review is quality maximization, not just verification.

This sounds right until you press on what "the best it can be" actually means.

It is subjective.
It is unbounded.
There is always a cleaner abstraction, a faster algorithm, a better name.
The pursuit has no natural stopping point, which is why code reviews so often devolve into bikeshedding over style preferences that do not measurably improve the outcome.

When the code was written by a human, a second perspective genuinely improved the implementation.
Two brains could find a better approach than one.
**But when the code is generated by an LLM, the reviewer is the only brain in the loop, and their suggestions compete with the option of simply regenerating the code against a better specification.**

If the code is not good enough, the answer is not to have a human improve it line by line during review.
The answer is to improve the specification, the test suite, or the generation prompt, and let the machine produce a better version.
That scales.
Human suggestions on a diff do not.

**The quality of the code is bounded by the quality of the specification that produced it.**
If you want better code, write a better spec.
**Reviewing the output is the most expensive, least scalable way to improve it.**

## The Reallocation

Here is what I am proposing.

**Instead of spending 30% of development time on code review, spend 5% on automated verification and reallocate the saved hours to specification, problem selection, and domain understanding.**

The quality of the software will not decrease.
The tests still run.
The linters still lint.
The static analysis still analyzes.
What changes is where the human attention goes.

Right now, human attention is concentrated at the end of the pipeline, reviewing output.
It should be concentrated at the beginning of the pipeline, defining what the output should be.

This is not a radical idea.
It is the same principle behind test-driven development: define what you want first, then build it.
**The difference is that now the builder is a machine, and the definition is the only place where human judgment is irreplaceable.**

## This Is Not Hypothetical

None of this is a prediction about the future.
I run this approach today.

My development workflow front-loads human effort into specification, requirements, and problem selection.
Before any code is written, there is an issue with acceptance criteria, a requirements document, and a technical specification, each reviewed and approved.
That is where my judgment gets spent.

Code generation happens against that specification.
When a pull request is opened, an automated review pipeline checks it against concrete gates.
Does it introduce security-sensitive changes?
Does it add new dependencies?
Does it change public interfaces?
Is the change reversible?
Do the tests pass?
Does the diff actually satisfy the acceptance criteria from the linked issue?

**If all gates pass, the PR is approved automatically.**
No human reads the diff.
No human clicks approve.

When the gates flag something, the PR is held for manual review.
This is not the same as reviewing every change.
It is reviewing the changes that carry real risk, which is a much smaller set.

The distinction matters.
**I am not advocating for shipping unreviewed code.**
**I am advocating for shipping code that has been verified by systems more reliable than a tired human scanning a diff, and reserving human attention for the small fraction of changes where it actually adds value.**

The infrastructure for this exists.
The gates are concrete.
The approach works because the specification does the heavy lifting that code review used to do poorly.
The skills that implement this workflow are [publicly available](https://github.com/tomzx/agents).

## Who Is Responsible

The first objection is accountability.
If no human reads the code before it ships, who owns the problems it creates?

The real answer is that a human reviewing a pull request for ten minutes was never truly responsible for that code.
They provided a rubber stamp.
They glanced at the diff, checked that the tests passed, and clicked approve.
When that code caused an outage six months later, nobody blamed the reviewer.
They blamed the author, the test suite, the deployment process, or the requirements.

What about the reviewer who spends thirty minutes, or an hour?
They are doing substantive work, not rubber-stamping.
The characterization above does not apply to them.
They genuinely understand the change, question the design, and catch real issues.

But the argument against mandatory review does not depend on reviews being shallow.
It depends on where that hour of expert attention is best spent.

An hour of review catches issues once, for one change, dependably on that reviewer being sharp that day.
An hour spent improving the specification prevents the entire class of issue from reaching implementation.
An hour spent writing a regression test catches the bug on every future run, not just the one time a human happened to read the code.

The thorough review is real work.
It is just not the highest-leverage work that person could be doing with that hour.
And at scale, it is unsustainable: if every PR requires an hour of human review and the LLM produces ten PRs a day, you need ten hours of review to keep up.
That is not a process that scales.

**Code review creates an illusion of accountability without delivering it.**
The signature on the PR is liability theater.

**Real responsibility lives upstream.**
The person who decided this problem was worth solving owns the outcome.
The person who wrote the specification owns whether the implementation matches intent.
The person who designed the deployment pipeline owns how quickly a bad change can be contained.

Removing human review does not remove responsibility.
It forces you to locate responsibility where it actually belongs: in the decisions that guided the work, not in the person who scanned it at the end.

## What About Outages

The second objection is safety.
What if the LLM makes a decision that takes down production?

**This is a real risk, but code review is the wrong tool to mitigate it.**

Most production outages are not caused by bugs that a reviewer would catch.
They are caused by configuration changes, unexpected data formats, load patterns, dependency failures, and integration issues that only surface under real traffic.
A human reading a diff is making a guess about what might happen.
Production behavior is the ground truth.

If you want to prevent outages, invest in the systems that observe and contain actual behavior.

Feature flags so a change can be turned off without a redeploy.
Canary deployments so a bad change reaches 1% of traffic before it reaches 100%.
Monitoring and alerting so a regression is detected in minutes, not hours.
Fast, tested rollback paths so recovery does not depend on someone remembering how the old version worked.

**These tools are more reliable than code review because they operate on reality rather than prediction.**
A reviewer might miss a subtle interaction.
A canary deployment will surface it.

## What About Revertibility

A related concern is that an LLM might produce changes that are hard to undo.
A sprawling refactor, a database migration that is not backward compatible, a change that entangles two previously independent systems.

This is a serious problem, but again, human review is not the safeguard people think it is.

Reviewers focus on forward correctness.
They ask "does this do what it should?"
They rarely ask "can we undo this cleanly?"
Even when they do, revertibility is hard to assess by reading a diff.
It depends on what happens in production after the change lands, on data migrations that have already run, on other changes that build on top of it.

**The solution is to make revertibility a structural property of how changes are made, not a property enforced by review.**

Keep changes small and independent.
Require database migrations to be backward compatible, deployed before the code that depends on them.
Use feature flags so new behavior can be disabled without reverting code.
Treat large, entangling refactors as high-risk changes that warrant extra process, not as the default mode of operation.

These are constraints you encode in your pipeline and your specification process.
They do not require a human to read every line of every PR.
They require discipline at the level where decisions are made.

## What About Code Quality and Maintainability

A third concern is that without human review, LLM-generated code will degrade into slop.
Inconsistent naming, duplicated logic, unnecessary abstractions, dead code, patterns that do not match the rest of the codebase.
Each individual change passes its tests, but the codebase slowly rots.

This is a real risk, and it deserves a real answer.
The answer is not that review prevents it.
The answer is that review catches it inconsistently, after the fact, one PR at a time.

Most of what we call code quality is measurable.
Cyclomatic complexity is a number.
Duplication is detectable.
Dead code is identifiable by static analysis.
Naming conventions are enforceable by linters.
File length, function length, import depth, test coverage gaps, all of these are machine-checkable properties.

If you care about maintainability, encode the constraints that produce it.
Set complexity limits that fail the build.
Run duplication detectors on every PR.
Require test coverage above a threshold.
Lint aggressively.
Block PRs that introduce unused exports or dead code.

These checks run on every change, consistently, without getting tired or distracted.
A human reviewer might flag a function that is too complex.
A complexity gate will flag every function that exceeds the threshold, every time, for as long as the rule exists.

Slop also has an upstream cause.
When the specification is vague about architecture, naming, and patterns, the LLM fills the gap with whatever it has seen most often in its training data.
That output is generic by default.
It will not match your codebase's conventions unless the specification tells it what those conventions are.

This means the fight against slop is won at the specification level, not at the review level.
A specification that includes the patterns to follow, the existing abstractions to reuse, and the naming conventions to respect produces cleaner code than a vague spec plus a human reviewer cleaning up the output.

For what slips through the automated gates, frequent maintenance sweeps catch accumulated decay.
Run a dead code analysis weekly.
Run a duplication detector weekly.
Review complexity trends after every merge.
This is a more systematic approach than hoping each PR's reviewer notices the slow accumulation of mess.

**Code quality is a property of your constraints, not of your reviewers.**

## What I Am Not Saying

I am not saying all code review should be eliminated tomorrow.
Legacy codebases, critical security infrastructure, and domains where correctness is life-or-death may still benefit from human review.

I am not saying code review was never useful.
It was, for decades, one of the best tools we had.
I am saying the tool's value has changed because the context has changed.

I am not saying I trust LLMs to always produce correct code.
I am saying that human code review is not the best way to ensure correctness when the code was machine-generated.
Automated verification, comprehensive test suites, and precise specifications are better tools for that job.

## The Question Worth Asking

The next time you open a pull request full of LLM-generated code and start reviewing it line by line, ask yourself: what am I actually checking?

If you are checking style, a linter does it better.
If you are checking correctness, tests do it better.
If you are checking whether the code solves the right problem, you should have answered that question before the code was written.

**Code review made sense when humans wrote all the code.**
**It makes less sense when humans define the problem and machines implement the solution.**
**The bottleneck has moved.**
**Our processes should move with it.**
