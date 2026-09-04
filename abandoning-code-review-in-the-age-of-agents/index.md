---

title: "Abandoning Code Review in the Age of Agents"
created: 2026-09-01
type: post
status: draft
tags: [ai, software-engineering, code-review, agents, llm, fully-ai-generated, llm=glm-5.3-flash]
readability: 3
audience_notes: >
  Assumes the reader is a software engineer or engineering lead who runs pull request review and has used LLM coding agents. No introduction to agents or CI required.
agent_sessions:
  - ses_fa3913c42ffeTa1ZCuv6Nb7Ifv
---

Code review is the last human-speed step in a pipeline that now runs at machine speed.
**I have gathered every reason I can find to abandon it in the age of agentic software development, and together they are stronger than any argument for keeping it.**

I have argued pieces of this case before, in [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) and [The Future of Code Review](../the-future-of-code-review/index.md).
This article puts every reason in one place, grouped by where it comes from: throughput, cognition, reliability, sociology, and safety, plus the reasons no reform can rescue the practice.

## What changed

A coding agent is not autocomplete.
Autocomplete typed faster, and the human still wrote the code.
An agent takes a ticket, plans, edits across files, runs the tests, and opens a pull request, and it can do that several times a day, in parallel with other agents doing the same.
**When generation becomes a machine-rate activity, every human-rate step downstream becomes the constraint, and per-diff human approval is that step.**
Nothing else in the pipeline caps throughput the way review does.
The queue is the tell: once you supervise enough agents, review items arrive faster than you can clear them, and the surplus waits on you.

## The throughput reasons

**1. Agents parallelized generation, and review is still serial.**
An agent fleet works across worktrees at the same time.
Human review funnels all of that output through one reader at a time.
**The step agents made parallel, review re-serializes.**

**2. The queue math guarantees collapse.**
Review is a queue with an arrival rate and a service rate.
Agent output raises the arrival rate, and a human cannot raise the service rate by trying harder.
When arrivals exceed service, the queue grows without bound, and no amount of discipline fixes it ([You Cannot Out-Review a Machine by Hand](../you-cannot-out-review-a-machine-by-hand/index.md)).

**3. Review latency destroys the value of agent speed.**
An agent that finishes in twenty minutes and waits a day for approval delivers in a day and twenty minutes.
The machine idles at the one station that cannot speed up.
**Buying speed at the generation stage and giving it back at the approval stage is paying twice for nothing.**

**4. Review cost scales with output, and gate cost does not.**
Every human review is rent, paid again on every pull request, forever.
A check in CI is built once, maintained occasionally, and runs on every change in between.
**The more the agents produce, the more the rent costs, and the more a gate saves.**

**5. Mandatory review converts machine failure into human exhaustion.**
A misconfigured agent can open hundreds of pull requests in an afternoon.
If every pull request needs a human, the agent's failure mode becomes your week.
**Rate-limit the pipeline, not the people reading it.**

**6. Human-in-the-loop approval is the worst of both worlds.**
All-human development had balanced rates: slow generation, slow approval.
Fully autonomous development is fast end to end.
Mandatory human review pays for machine-rate generation and human-rate approval at the same time, which is the most expensive combination available.

## The cognitive reasons

**7. Reviewing agent code is verification, not review.**
Review works when reviewer and author share a mental model, so the reviewer can build on the author's reasoning and ask what they meant.
An agent has no intent to consult, so the reviewer reconstructs meaning line by line, alone.
**That is not review; that is re-deriving the code from scratch with extra steps.**

**8. Attention collapses exactly where agents guarantee volume.**
Studies of real review practice put the useful band of a diff around two to four hundred changed lines, and effectiveness falls off sharply beyond it ([SmartBear, "Best Kept Secrets of Peer Code Review"](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/)).
Agents produce volume, and volume guarantees you live beyond the cliff.
The conditions that make review worth doing are the conditions agents make impossible.

**9. The diff is the wrong unit of correctness.**
Review inspects a slice of code.
Correctness is a property of the whole system: how the change behaves under load, against real data, alongside the other changes landing the same hour.
Staging and load tests approximate a few of those properties; production is where all of them show up at once.

**10. Plausibility defeats skimming.**
Agent code is trained on human code, so it looks like code.
It has the conventional structure, the familiar names, the confident test coverage.
A human skim pattern-matches "looks fine" and moves on.
**The better the model gets, the less a skim finds, because skimming works by noticing oddity, and agents are optimized to minimize oddity.**

**11. Review comments no longer land anywhere.**
With human authors, a review comment taught the author, and the lesson compounded over years.
An agent does not carry the lesson out of the pull request.
The loop that actually teaches the system is the specification and the test suite, so the comment is a cost with no memory.

## The reliability reasons

**12. Defect finding was never review's real output.**
When Microsoft studied its own review process, only about fifteen percent of review comments related to defects, and most of those were minor ([Czerwonka, Greiler, and Tilford, "Code Reviews Do Not Find Bugs"](https://dblp.org/rec/conf/icse/CzerwonkaGT15.html)).
The bulk of the value developers reported was code improvement and awareness, not bug catching ([Bacchelli & Bird, "Expectations, Outcomes, and Challenges of Modern Code Review"](https://sback.it/publications/icse2013.pdf)).
**The one thing review is famous for is the thing it does least.**

**13. Review is a sample; a gate is a census.**
A human reads some of the lines, once, on one Tuesday.
A check runs on every line, on every run, for as long as the codebase exists.
When review finds an issue, the fix is one pull request; when a gate catches a class of issue, the fix is permanent.

**14. A verdict that depends on the reviewer is not a verdict.**
The same diff gets approved at 9 a.m. and rejected at 5 p.m., approved by one lead and nitpicked by another.
CI gives the same answer every time.
**Process decisions that matter should not hinge on who had coffee.**

**15. The approve click produces the feeling of safety.**
Most approvals are decided by CI status, author reputation, diff size, and the description, before the code is read ([You Already Review Code Without Reading It](../code-review-without-reading-the-code/index.md)).
The signature certifies that a person was present, not that the code was examined.
**Feeling safe and being checked are different products, and review sells the first one.**

**16. Accountability theater allocates blame instead of preventing harm.**
The approving signature exists so that, after an incident, someone can be pointed at.
In practice nobody blames the reviewer; they blame the author, the tests, or the process.
**A mechanism whose output is blame allocation does not need to sit between your agents and production.**

## The sociology reasons

**17. The social benefits had a human on both ends, and now they do not.**
Mentoring juniors, building trust, sharing context, softening criticism: these justified review's cost when two humans met at the diff.
An agent is not mentored by comments, does not build trust through diffs, and has no feelings to manage.
**The functions that made review worth its cost had a human author as their subject, and the human author is gone.**

**18. Review is where bikeshedding lives.**
Naming debates, brace placement, and abstraction preferences consume senior hours while the change waits.
When output is cheap to regenerate, nitpicking the diff is the wrong loop; improve the spec and regenerate instead.
Gates never argue about tabs.

**19. Approval is a permission slip, and permission is the bottleneck.**
What review actually gates is not quality but permission to merge.
When agents can produce the change in minutes, the scarce resource is the yes.
**Queueing the yes is pure overhead: nothing is learned there, and little is checked that CI could not check.**

**20. Knowledge diffusion is the one real loss, and it has cheaper substitutes.**
Review did spread awareness of the codebase, and I count that as the strongest argument for keeping it.
But the same awareness comes from spec review, design review, ownership docs, and rotation, where people learn decisions instead of skimming one diff.
**Buy knowledge where it is cheap; do not price it in approvals.**

## The safety reasons

**21. Production is the ground truth review pretends to be.**
Google's SRE organization reports that 70% of outages are due to changes in a live system ([Google, "Site Reliability Engineering"](https://sre.google/sre-book/introduction/)).
Most of those are configuration, data, load, and integration effects that no diff-reader can see.
Canary deployments, feature flags, monitoring, and tested rollback observe the real system instead of predicting it.
**A reviewer guesses; a canary measures.**

**22. Reversibility beats pre-approval.**
Making changes hard to make is one way to stay safe; making them cheap to undo is another.
Small, independent, backward-compatible changes with tested rollback paths cap the damage of any single mistake, including mistakes no reviewer would have caught.
An undo button outperforms a gatekeeper.

**23. Skimming misses security; gates do not.**
A tired reviewer scanning a diff will not spot a subtle injection or an import that quietly resolves to a lookalike public package.
Static analysis, dependency policy gates, and a dedicated adversarial agent hunting the change will, on every pull request, at machine speed.

**24. If review is worth doing, delegate it to a system.**
A reviewer agent reads the whole repository, never tires on the fourth diff, and when it finds a class of issue, writes the gate that catches that class forever.
An ad hoc human reviewer catches what they happen to notice, once.
**Machine review at machine speed is the only review that scales with machine generation.**

## Why reform does not rescue it

**25. Every reform keeps the cost and shrinks the benefit.**
Checklists, review SLAs, smaller pull requests, review budgets: each trims waste at the edges and preserves the ritual at the center.
The math is unchanged, because per-diff human attention cannot scale to machine-rate output.
**Reforming review is spending effort to keep the bottleneck comfortable instead of removing the bottleneck.**

**26. The judgment moves upstream, where it always belonged.**
Abandoning review does not mean abandoning scrutiny.
It means scrutinizing specifications, acceptance criteria, gates, and the small set of irreversible, trust-boundary changes that genuinely deserve slow human reading ([The Merge Gate](../the-merge-gate/index.md)).
**Review the intentions and the mechanisms; stop reviewing the output.**

## What to do next

Measure the queue first.
Count agent pull requests arriving per day and the hours you actually spend reviewing.
If arrivals exceed service, you have already abandoned review; you just have not admitted it in policy.

Then make the default explicit.
Low blast radius changes merge on green: CI, gates, and the reviewer agent, no human click.
Reserve deliberate human reading for irreversible changes, security boundaries, and the gating system itself.

Convert every catch.
Each time review or production surfaces an issue, encode it as a check before moving on.
The list of checks is the review process you are actually running; the queue is just where its results used to wait.

**Code review was the right process for software made at human speed.**
**Agents ended that era, and the process should end with it.**

## See also

- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - the full-length argument that reading machine-written diffs is the wrong tool, and what to do with the hours instead.
- [You Already Review Code Without Reading It](../code-review-without-reading-the-code/index.md) - the evidence that approvals are decided by signals rather than reading, which is the premise behind reasons 15 and 16.
- [The Future of Code Review](../the-future-of-code-review/index.md) - the industrial version of this case: verification factories, the five levels, and what teams already run in production.
- [You Cannot Out-Review a Machine by Hand](../you-cannot-out-review-a-machine-by-hand/index.md) - the queue math behind reason 2, applied to any machine-generated workload.
- [Verifying Code Without Reading It](../verifying-code-without-reading-it/index.md) - the replacement system: the checks, critics, and gates that do the work review was supposed to do.
- [Rolling Out the Unread Review](../rolling-out-the-unread-review/index.md) - how to ship that replacement system to a team that does not trust it yet.
- [The Merge Gate](../the-merge-gate/index.md) - where a human gate still earns its place once per-diff review is gone.
- [The Acceptance Gap](../the-acceptance-gap/index.md) - why acceptance, not review, is the gate that matters between an agent and production.

## References

- [Wikipedia, "Code review"](https://en.wikipedia.org/wiki/Code_review) - the origin of formal review in Fagan's inspections, a process designed for human authors.
- [SmartBear, "Best Kept Secrets of Peer Code Review"](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/) - the 200-400 line finding behind reason 8.
- [Czerwonka, Greiler, and Tilford, "Code Reviews Do Not Find Bugs" (ICSE 2015)](https://dblp.org/rec/conf/icse/CzerwonkaGT15.html) - the measurement behind reason 12; only about fifteen percent of Microsoft review comments related to defects.
- [Bacchelli and Bird, "Expectations, Outcomes, and Challenges of Modern Code Review" (ICSE 2013)](https://sback.it/publications/icse2013.pdf) - what developers expect from review versus what it delivers.
- [Google, "Site Reliability Engineering"](https://sre.google/sre-book/introduction/) - the finding that 70% of outages come from changes in a live system, behind reason 21.
- [Latent Space, "Reviews Dead"](https://www.latent.space/p/reviews-dead) - industry reporting on teams already dropping per-diff human review.
