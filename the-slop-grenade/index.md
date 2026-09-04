---

title: "The Slop Grenade: Code Ownership in the Age of the Team of One"
created: 2026-08-21
type: post
status: draft
tags: [software-engineering, team-management, ownership, ai, llm, code-quality, fully-ai-generated, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader is an engineer, tech lead, or engineering manager at a company large enough that code ownership is written down in files, and has used LLM coding tools. No management background required.
agent_sessions:
  - ses_fdd9a1c34ffeYL9aE0Q4fK3Zgw
---

A large company writes code ownership down.
A `CODEOWNERS` file says whose approval a change needs, a service catalog says which team gets paged, an on-call rotation says who answers at 3 a.m.
The map exists because strangers share a codebase, and strangers cannot rebuild trust from scratch for every pull request.
The map stayed true as long as one assumption held: the amount of code a person can produce stays roughly proportional to the amount of code the people around them can absorb and answer for.
**LLMs broke that assumption, and companies are now accumulating code that outgrew the person who generated it while the ownership map pretends nothing changed.**

That outgrown code is what I call a slop grenade.
It works, it demos well, and it sits quietly, sometimes for years, until something breaks and it detonates on whoever holds the directory it landed in.

## What Ownership Means at a Large Company

At ten people, ownership is trust between people who sit within shouting distance.
At a few thousand, it has to be a file.
GitHub's [code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) mechanism is the canonical form: rules that route every change to named reviewers by path, so that a stranger proposing an edit to payments code automatically meets the people who answer for payments.

The file is not the ownership, though.
Ownership is not property; nobody owns code at a company the way they own a laptop.
**Ownership is a promise to answer for a region of the codebase: review the changes, fix the failures, take the page.**
`CODEOWNERS` rules, review gates, service catalogs, and on-call rotations are just the promise written in a form strangers can read.

The map also encodes a limit that nobody states out loud.
[Team Topologies](https://teamtopologies.com/) names it team cognitive load: a team can only own what fits in its collective head, so territory is handed out in proportion to absorption capacity.
You give a team a service because six people can hold that service in mind, and you do not give it three more services, because then it holds none of them.

For most of software history, the calibration ran by itself.
Writing code by hand was slow, so a person's footprint grew at the pace a team grows anyway, one reviewed change at a time.
Code review was the metering valve, and the valve opened at exactly the rate the people downstream could understand what was coming through it.

## The Coupling That Broke

Generation is nearly free now, and understanding is not.
This asymmetry is the one [Who Maintains the Slop?](../who-maintains-the-slop/index.md) works through at the level of one handoff: producing code collapsed in cost while absorbing it stayed expensive, because absorption is dominated by understanding.

At company scale, the asymmetry breaks a ratio the org chart depends on.
A team absorbs new code at a roughly fixed rate, set by review hours, onboarding, and how much context fits in heads.
A person driving a fleet of agents produces at a rate that no longer has any ceiling tied to headcount.
The last metering valve was review, and review is failing exactly as queue math predicts: changes arrive faster than they leave, the queue grows, the pressure to approve builds, and the approvals degrade ([You Are the Bottleneck](../you-are-the-bottleneck/index.md)).

What comes out the other end is code that exists in a quantity the map never planned for.
**The amount of code a company can actually own is bounded by the understanding of the people named in its ownership files, and by nothing else; generation now exceeds that bound routinely.**

## The Team of One

Somewhere in your company right now there is a team of one: a single engineer plus a fleet of agents, producing an entire subsystem.
The internal tool, the migration harness, the new service, the prototype that quietly became production.
The org chart says a team owns the domain, and the map still routes approvals through that team, but production has moved to one person, and the team's ownership has become ceremonial.

This is not the deliberate arrangement I wrote about in [Solo Is a Team Size](../solo-is-a-team-size/index.md), where a solo operator consciously imports team practices, from specifications and gates to decision records, to stay solvent.
The large-company team of one is rarely deliberate org design.
It is an emergent side effect of velocity plus one willing person, and it is usually celebrated while it lasts, because the demos are impressive and the metrics move.

The person at the center is rational, not villainous.
The company rewards shipping and does not charge for maintenance, so shipping at machine speed is the behavior that gets rewarded ([Who Maintains the Slop?](../who-maintains-the-slop/index.md)).
And the person pays a price that the celebration never mentions: a [bus factor](https://en.wikipedia.org/wiki/Bus_factor) of one, an on-call burden for a system nobody else can explain, and a growing dread that walking away converts a career highlight into a reputation.
**The team of one ends up choosing between becoming the permanent bottleneck and becoming the person who left the grenade, and neither option is what the promotion was for.**

## What a Slop Grenade Actually Is

It is worth being precise, because slop usually connotes bad output, and quality is not the axis here.
Plenty of grenades pass their tests and follow the style guide.
A grenade is defined by a ratio: the maintenance the code will demand versus the answering capacity behind it.
Generated code can be competent and still be a grenade, if there is enough of it and almost no one who can explain why it is the way it is.

Three properties mark one.

It works well enough to become depended upon, because code that fails gets deleted and code that demos gets integrated.
Its recoverable intent is thin relative to its size, the condition [The Code You Will Never Read](../the-code-you-will-never-read/index.md) describes from the reader's side and [Who Maintains the Slop?](../who-maintains-the-slop/index.md) calls archaeology without the civilization.
And the name in the ownership file cannot cover it: either one person who cannot hold it, or a team that never consented to it.

The detonation mechanics are organizational, not technical.
Directory-based ownership means the team whose path matches inherits the code, consent or not, which is assignment by proximity at company scale ([Accountability Is Not Blame](../accountability-is-not-blame/index.md)).
If the code landed somewhere unowned, it drifts to whoever is downstream or whoever still cares.
Nobody volunteers to inherit it, for the reason [The Cost of Work You Did Not Choose](../the-cost-of-work-you-did-not-choose/index.md) documents: work you did not choose carries a tax, and this work carries the heaviest one available.

The grenades also arrive in volleys, not only as single large subsystems.
Forty mid-size ones, each too small to escalate, together exceed what the surrounding teams can absorb, and no single one looks like the problem.

Then the generator leaves, eventually, and the company discovers the map was wrong.
Not wrong about the paths; the rules all matched.
Wrong about the promise underneath them: the name was still in the file, and the answering was gone.

## What to Do Next

If you run engineering at a company where this is starting to happen, three moves cover most of it.

**Treat footprint growth as an ownership decision, not a code decision.**
A change that adds thirty thousand lines is not a review, it is an org-design event.
Require a named owner and an absorption plan before generation starts, not after the pull request opens; no owner, no merge, applied at company scale, kills the worst cases outright.

**Budget absorption explicitly.**
Review capacity is the metering valve, so make it a number.
A team accepting five thousand lines of someone else's generated code this quarter is making a decision that deserves to be seen as one, and slow-walking generated changes is not bureaucracy, it is the valve doing its job.

**Give every team of one a graduation path.**
When the code outgrows the person, either it earns a team, staffed deliberately with the intent handed over as specifications and decision records, or it shrinks.
Deleting generated code is cheap relative to maintaining it, and code that can be regenerated from its specification should be: keep the spec, delete the code.

If you are the engineer sitting on a grenade, or about to build one, two moves.

**Apply the explain test.**
Could you answer why-questions about the system, why this boundary, why this retry policy, why this data model, without asking the model?
If not, you generated the code and did not build it, and the gap is what someone else will inherit.
Close it the only way that works: write the specification, the decision records, and the handoff paragraph that [Solo Is a Team Size](../solo-is-a-team-size/index.md) describes as the closest thing solo work has to succession.

**Surface the mismatch early.**
The moment your output outpaces your team's absorption, say so, loudly, in writing.
The alternative is discovering the trap from the inside, at the exact moment the code has become too central to walk away from and too large to hold.

The question of how fast code can be produced is answered; the machines answered it.
The live question at a large company is how much code it can still answer for, and whether the map that tracks the answering matches where the code actually is.
**A company does not own the code its name appears on in an ownership file; it owns the code someone is still able and willing to answer for. Everything else is unexploded.**

## See also

- [Who Maintains the Slop?](../who-maintains-the-slop/index.md) - the handoff-level economics of cheap generation, which this article scales up to the company ownership map
- [Solo Is a Team Size](../solo-is-a-team-size/index.md) - the deliberate, well-run version of the team of one, and the succession practices that make it survivable
- [Accountability Is Not Blame](../accountability-is-not-blame/index.md) - assignment by proximity, the mechanism that decides who a grenade detonates on when no owner holds it
- [A Monorepo Doesn't Make You a Single Team](../a-monorepo-doesnt-make-you-a-single-team/index.md) - how large shared codebases recreate ownership boundaries internally, the map this article depends on
- [The Cost of Work You Did Not Choose](../the-cost-of-work-you-did-not-choose/index.md) - the motivation tax that makes inherited grenades slower and heavier than their difficulty alone predicts

## References

- [GitHub docs, "About code owners"](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) - the path-based ownership mechanism most large repositories use to write the promise down
- [Skelton and Pais, "Team Topologies"](https://teamtopologies.com/) - team cognitive load as the limit on how much a team can own, the absorption capacity this article budgets
- [Wikipedia, "Bus factor"](https://en.wikipedia.org/wiki/Bus_factor) - the concentration-of-knowledge risk that a team of one maximizes by construction
- [Wikipedia, "DevOps"](https://en.wikipedia.org/wiki/DevOps) - the "you build it, you run it" alignment of authorship with ownership that machine-speed generation unaligns
- [Wikipedia, "InnerSource"](https://en.wikipedia.org/wiki/InnerSource) - open-source contribution norms applied inside a company, the etiquette strangers sharing a codebase rely on
