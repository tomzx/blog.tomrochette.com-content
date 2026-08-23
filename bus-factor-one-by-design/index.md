---
title: "Bus Factor One by Design"
created: 2026-08-22
type: post
status: finished
tags: [ai, software-engineering, llm, agents, team-management, ownership, fully-ai-generated, llm=ox-alpha, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader works in or leads a software organization, knows the term bus factor, and has felt the pull of one-person ownership in the agent era. No management theory background required.
---

Picture a company where every system belongs to exactly one person.
No colleague reviews their changes, no meeting syncs anyone on what they built, and no second person carries the context needed to touch it.
A few years ago that description would have read as negligence.
Today it reads like an efficiency proposal, because agents have absorbed most of what colleagues used to contribute during implementation.
**The model can work, but only for companies that answer one question before adopting it: what happens when the owner goes on vacation, or quits?**

## Why Single-Owner Systems Are Coming

The economics of coordination flipped before the model did.
[Brooks counted it in 1975](https://en.wikipedia.org/wiki/The_Mythical_Man-Month): n people create n(n-1)/2 communication channels, and every channel taxes alignment.
When implementation was expensive, that tax bought reliability, because colleagues caught each other's mistakes while catching up on context.
Now agents produce the code and verification pipelines judge it, so [human review of generated changes](../rethinking-code-review-in-the-age-of-llms/index.md) has become the lowest-leverage gate in the loop, and the specification replaces the meeting as the unit of coordination.
What remains of the channel tax is mostly cost.

Against that cost, a single owner buys three things teams struggle to produce at any price.
Coherence, because one taste decides every abstraction instead of a committee averaging its members.
Speed, because nothing waits on sync.
Accountability, because when something breaks there is exactly one person who answers for it.

This is not hypothetical.
[A study of the Truck Factor](https://arxiv.org/abs/1512.05230), the minimum number of developers who must disappear before a project stalls, found many popular open source projects already sit at one.
Critical infrastructure runs on bus factor one more often than any company would admit to running production that way.
The difference is that companies now have an economic reason to stop pretending otherwise and a toolset for surviving it.

## The Question Hides an Assumption

"What if nobody else knows the system?" assumes knowledge lives in heads.
For most of software history it did, because writing it down served nobody's daily work.
Documentation rotted because the only people able to maintain it were busy maintaining the system.

Agents change the cost of the alternative.
Decision records, runbooks, architecture maps, and executable specifications can now be produced and refreshed continuously as a byproduct of the work itself.
The fleet that builds the system keeps its own paper trail current, the same way CI keeps tests green.

**The metric stops being how many heads know the system and becomes how fast a competent outsider plus their agents can re-acquire it from artifacts alone.**
Call it re-acquisition time.
Bus factor measured the redundancy of memory.
Re-acquisition time measures the recoverability of understanding.

That inversion is why the model deserves a fair hearing.
**A team of five who never write anything down can be harder to take over than a single owner whose repository documents itself, because five heads of unspoken context is just bus factor five with better manners.**

## How a Company Runs on Owners of One

The mechanisms are organizational, not technical.

**Ownership is conditional on legibility.**
An owner keeps the system as long as it stays handover-ready without them.
Definition of done includes the artifacts: tests that read like specifications, decision records with alternatives considered, runbooks, an architecture map that reflects reality.
Agents draft and refresh these continuously, so legibility stops being a chore and becomes a property of the pipeline.
Think of it as [source code escrow](https://en.wikipedia.org/wiki/Source_code_escrow) applied to understanding rather than code: the company holds the knowledge outside the person who operates it.

**Vacations are load tests.**
Every owner takes a mandatory uninterrupted absence each year.
During it, another engineer plus their agents must handle incidents and ship one scoped change using only the artifacts, with the owner unreachable.
Score the takeover and publish the time it took.
The drill is chaos engineering applied to the org chart: you inject failure into the ownership layer while the stakes are a minor feature, not a resignation letter.

**Redundancy spend follows blast radius.**
Not every internal script deserves a second person.
Classify systems by blast radius and cap how much revenue-critical surface may exceed a re-acquisition threshold, say two weeks.
This is portfolio management: concentrate risk where you choose, hedge where loss would be unrecoverable, and know which is which.

**Succession is scheduled, not emergent.**
Rotate owners on a cadence so every handover gets exercised while both parties still work there.
For the few systems whose takeover would hurt most, name a shadow owner who runs the vacation drill against them quarterly.
The handoff paragraph from [Solo Is a Team Size](../solo-is-a-team-size/index.md) (what the system is, why it exists, who inherits it) becomes a required field in the service registry rather than advice for solo operators.

**Incentives reward survivable systems.**
Promotion criteria should include "your system passed your absence", and managers should treat "only I can touch this" as a liability, not leverage.
The irreplaceable engineer is not an asset the company enjoys; it is concentrated risk the company funds.
Pay people to make themselves unnecessary and indispensability stops being a career strategy.

## What Still Does Not Transfer

Some knowledge refuses to become artifacts.
Taste, the reasons the roadmap bends where it does, the history of a negotiation with a key customer: deliberation leaves traces but rarely conclusions.

Two habits keep more of it from escaping.
Record rationale at decision time, while the alternatives are still alive, because a decision record written six months later is fiction.
Occasionally have the owner defend direction to a peer: not the code, the choices, so judgment gets exercised against a counterparty instead of echoing inside one skull.

Then accept what remains.
Some re-acquisition friction is irreducible, the same way some latency is.
Budget it like depreciation rather than promising zero, and nobody gets surprised when a departure costs three weeks instead of none.

## What to Do Next

Pick your most critical system and measure its re-acquisition time this month.
Hand it to another competent engineer plus their agents with a scoped feature request and no access to the owner.
Whatever number comes back is your real exposure, and it is almost certainly larger than management believes.

Set thresholds by blast radius and drill vacations against everything above them.
Change one line of promotion criteria to reward owners whose systems survive their absence.
And when someone next argues a system needs a second head, ask whether they mean memory redundancy, which agents and artifacts now supply cheaply, or judgment redundancy, which only a second person supplies.
**The first is solved; budget for the second only where the stakes are directional.**

A company can run on owners of one indefinitely.
What it cannot survive is letting knowledge live in only one place.
**People operate the systems, the artifacts are the asset, and the company's job is to keep the asset independent of any operator, including the ones it wishes it could keep forever.**

## See also

- [Solo Is a Team Size](../solo-is-a-team-size/index.md) - the solo-operator limit case of this model, and the source of the handoff paragraph turned registry field here
- [You Are the Bottleneck](../you-are-the-bottleneck/index.md) - the acceptance-evidence contract that makes a fast single producer trustworthy enough to own a system alone
- [Who Maintains the Slop?](../who-maintains-the-slop/index.md) - who stays attached to agent-generated code once its author moves on, the maintenance half of the ownership question
- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) - the team-based counterpart, covering which processes stay worth their friction when colleagues remain in the loop

## References

- [Guido Avelino et al., "A novel approach for estimating Truck Factor"](https://arxiv.org/abs/1512.05230) - the empirical finding that many widely used projects already run at truck factor one
- [Bus factor (Wikipedia)](https://en.wikipedia.org/wiki/Bus_factor) - the classic formulation of the risk this model deliberately accepts
- [Source code escrow (Wikipedia)](https://en.wikipedia.org/wiki/Source_code_escrow) - the established practice of holding operational knowledge outside the operating party
- [Frederick Brooks, "The Mythical Man-Month" (Wikipedia)](https://en.wikipedia.org/wiki/The_Mythical_Man-Month) - the communication-channel math that made coordination expensive and single ownership attractive
