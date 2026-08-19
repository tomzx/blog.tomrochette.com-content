---
title: "You Are the Bottleneck: What to Do When Your Coworker's LLMs Outproduce Your Review"
created: 2026-08-19
type: post
status: finished
tags: [ai, software-engineering, code-review, llm, pull-request, productivity, fully-ai-generated, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader works on a team where a colleague generates LLM-assisted pull requests faster than anyone can review them, and knows how pull requests and CI work. No introduction to LLMs.
---

Your coworker opens pull requests faster than you can read them.
Every morning the queue is longer than when you left.
Their work piles up behind your name, and everyone can see whose approval is missing.
**You are not the bottleneck.**
**The process that routes every change through one human reader is the bottleneck, and no amount of reading faster will fix it.**

The setup is now ordinary.
More than one in five code reviews on GitHub already [involve an agent](https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/), and a developer driving an LLM can open ten plausible pull requests in the time it takes you to properly review two.
The gap between arrival and departure is not a temporary spike.
The gap is the new steady state, and it needs a structural answer from both sides of the queue.

## The Math Ends Badly on Its Own

Review is a queue.
Changes arrive at your coworker's production rate and leave at your review rate.
When arrival exceeds service, the queue grows without bound, which is the whole story of your inbox.

The instinctive response is to raise your service rate: read faster, review longer hours, take fewer breaks.
Queueing theory says why that response fails even when it works.
[Kingman's formula](https://en.wikipedia.org/wiki/Kingman%27s_formula) says that waiting time grows with variability divided by spare capacity, so as your utilization approaches one hundred percent, waits explode nonlinearly.
A reviewer at eighty percent capacity has a manageable queue.
The same reviewer at ninety-seven percent, which is what "keeping up" actually demands, has waits measured in days.
**A process that only functions when you are never tired, never in a meeting, and never sick is not a process; it is a countdown.**

There is a second failure hiding behind the first.
An overloaded reviewer does not stop reviewing, the reviewer degrades first.
You skim.
You approve what the tests already cover.
You rubber-stamp the fourth pull request of the evening.
**The queue does not just grow, it silently stops protecting anything, because code merged by a rubber stamp feels reviewed without being reviewed.**
Rubber-stamped merges are worse than a visible backlog: the backlog at least admits the work is not being checked.

## The Reframe

The useful lens here is the [theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints).
A system's throughput is set by its constraint, and the prescribed moves are to exploit the constraint (spend constraint time only on work only the constraint can do), elevate the constraint (add capacity or automation), and subordinate everything else to the constraint (upstream steps keep the constraint fed with work worth its time).

Read that list again with names attached.
The constraint is you.
Exploiting the constraint means your reading time goes only to changes that genuinely need human judgment.
Elevating the constraint means automated gates absorb what does not need your eyes.
Subordinating to the constraint means your coworker's job changes: keep the queue full of cheap-to-judge, high-value changes instead of merely full.

Guilt is the wrong response to being the constraint, and so is heroics.
**Bottleneck is a role in a system, not a verdict on a person, and roles can be redesigned.**
The question stops being "how do I review faster" and becomes "what should be allowed to arrive at this queue at all, and how should the queue drain".

## What Your Coworker Should Do

When generation is cheap, producing more changes is trivial and producing mergeable changes is the actual work.
**Your coworker's job is no longer to produce changes; the job is to produce changes that are cheap to say yes to.**

Measure time-to-merge, not pull requests opened.
A pull request that sits for a week is not output, it is inventory, and inventory that waits long enough rots into rebase conflicts and stale specs.

Concretely, every pull request should arrive with four things.

**A specification written before the code.**
Acceptance criteria that existed before generation started, not a description reverse-engineered from the diff afterward.
Reviewing a plan takes minutes; reviewing an unexplained implementation takes an hour, and the plan is where your disagreement is cheap.

**Evidence that the change works.**
A failing test turned green by the fix, a before-and-after recording, a benchmark.
A fix is not fixed until something independent of the model says so, which is the acceptance gap in miniature.
Evidence converts your review from "verify by hand" to "check the verification", and those tasks differ by an order of magnitude in cost.

**An annotation of the risk.**
A self-review pass that flags the dangerous hunks, states the blast radius, and says which parts the coworker is unsure about.
The risk annotation is the single highest-leverage habit of the four, because it tells you where your scarce attention belongs and proves a human actually read the output before demanding that you do.

**A summary that enables a thirty-second judgment.**
What changed, why, what could break, how to roll it back.

Beyond per-PR discipline, two structural commitments matter more.

**Respect a work-in-progress limit.**
At most two or three open pull requests at a time.
When the cap is reached, the surplus capacity goes to writing tests, improving gates, and sharpening the next spec, not to opening a fourth PR that will age out in the queue.
**The most productive use of a fast producer's spare time is reducing the review burden itself: gates, encoded conventions, and tooling that make every future change cheaper to judge, not just the producer's own.**

**Stay attached after merge.**
Bugs in generated code route back to the generator for a window of time, because the person who captured the benefit of fast production should carry the first round of the cost.

## What You Should Do

Your side of the contract is to stop being a per-diff reader and become the designer of how the queue drains.

**Classify instead of read.**
A README typo and a schema migration are both pull requests and do not need the same gate.
Compute blast radius and reversibility per change, auto-merge the low-risk class on green, and hold only the risky minority for human eyes.
The majority of a flood is routine, and routine work is what machines are for.

**Encode your recurring comments.**
Every review comment you have written more than twice is a gate you have not built yet.
Complexity limits, dead code detection, coverage thresholds, forbidden dependency classes.
Each encoded check is a category of attention you never spend again, and a category of queue pressure that disappears permanently.

**Move your attention upstream.**
Review the spec before the code is generated, not the diff after.
Ten minutes on a plan prevents an hour on a wrong implementation, and your disagreement lands while it still costs a conversation instead of a rework.

**Match your coworker's tools.**
Your coworker generates with a model; you triage with one.
Running a first-pass review that flags anomalies, summarizes each diff, and ranks the queue by risk is not cheating, it is symmetrical.
A pipeline where one side is machine-accelerated and the other is capped at human reading speed is broken by construction, whether the asymmetry is malicious or accidental.

**Batch reviews into fixed windows.**
Two scheduled review blocks a day, instead of interrupt-driven approval sessions.
Predictable service beats heroic bursts because Kingman's formula punishes variability itself, and every interruption you remove shrinks the waits more than the raw time saved suggests.

**Make the queue visible.**
Arrival rate versus service rate, time-to-merge, queue depth, on a dashboard both of you see.
Numbers turn a feels-bad conversation ("you are slow", "you flood me") into an engineering conversation ("our arrival rate is triple our service rate, so we change one of them").

## What You Agree On Together

The fix is a contract, not a truce.

Define merge-ready: the checklist a pull request satisfies before it even enters your queue.
Set the WIP limit at your sustainable service rate, and treat the limit as the throttle that keeps arrival below service.
Agree on the escalation path for the small set of changes, the irreversible ones, the trust-boundary ones, that deserve synchronous human attention while your coworker waits.
Agree on where surplus producer capacity goes when the queue is full, because idle generation capacity pointed at more PRs is how the problem restarts.

Then change what you both measure.
**The unit of team output is merged changes, not opened pull requests**, and every metric that rewards opening over merging rebuilds the queue you just dismantled.

## What to Do Next

Tomorrow, your coworker attaches the four things, spec, evidence, risk annotation, summary, to every new pull request, and you classify the existing backlog into auto-merge-gate versus needs-my-eyes, resolving nothing yet, just sorting.

This week, set the WIP limit and move your two most-repeated review comments into CI.

This month, make spec review the meeting that replaced diff review, and put time-to-merge on the dashboard next to queue depth.

The queue was never a verdict on how fast you read.
The queue is a design decision your team made without noticing, and a decision made by accident can be made on purpose.

## See also

- [You Cannot Out-Review a Machine by Hand](../you-cannot-out-review-a-machine-by-hand/index.md) - the same queue math in its adversarial form, where the tooling asymmetry is deliberate rather than accidental
- [The Merge Gate](../the-merge-gate/index.md) - how to classify changes by blast radius so only the risky minority needs a human approval
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - the case that judgment belongs upstream in specifications and gates rather than downstream in diffs
- [The Acceptance Gap](../the-acceptance-gap/index.md) - what counts as independent evidence that a change works, the evidence your coworker should attach to every pull request
- [Who Maintains the Slop?](../who-maintains-the-slop/index.md) - why the generator must stay attached to the code after it merges, the ownership window this article's contract requires

## References

- [Kingman's formula](https://en.wikipedia.org/wiki/Kingman%27s_formula) - the queueing result that explains why waits explode as utilization approaches one hundred percent
- [Theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints) - the exploit, elevate, subordinate framework applied to the reviewer as the constraint
- [Queueing theory](https://en.wikipedia.org/wiki/Queueing_theory) - the general study of arrival and service rates, the model underneath the review queue
- [GitHub Blog, "Agent pull requests are everywhere"](https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/) - the data showing agent-generated pull requests are already a large fraction of reviews
