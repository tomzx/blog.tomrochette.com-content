---

title: "A Monorepo Doesn't Make You a Single Team"
created: 2026-06-23
type: post
status: draft
tags: [software-engineering, monorepo, teams, org-design, architecture, conways-law, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes familiarity with version control, monorepos, and how engineering teams coordinate work.
agent_sessions:
  - ses_10adb5dc6ffe9Vsc0i1na9wDpM
---

A monorepo is a tooling decision that teams routinely mistake for an organizational one.
Putting everyone's code in the same repository does not put everyone on the same team.
It is Conway's Law in disguise: a system's structure follows the structure of the organization that builds it, and editing the repository does not edit the org chart ([Conway, "How Do Committees Invent?"](https://www.melconway.com/Home/Conways_Law.html)).
**The repository boundary is a property of your version control; the team boundary is a property of how people coordinate, and the two move on completely independent axes.**

When organizations conflate them, they adopt a monorepo expecting it to dissolve team boundaries, and then discover that those boundaries reappear a few months later, only now they are encoded as directory permissions and review rules instead of repository URLs.

## The Quiet Assumption Behind the Choice

Most arguments for adopting a monorepo are upfront about the tooling wins.
Atomic cross-cutting changes, unified build and CI, shared visibility, and easier code sharing are real benefits, and they follow from one property: at every commit the whole codebase is consistent ([Dan Luu, "Advantages of monorepos"](https://danluu.com/monorepo/)).

The problem starts when the argument quietly slides from "this is a better way to version our code" to "this will make us work like one team."
Teams under pressure to collaborate more reach for the monorepo as if it were an org-chart intervention that happened to ship as a git layout.
It is not.
**A shared repository makes code reachable; it does nothing to make people aligned.**

The giveaway is the language people use when justifying the move.
"We want to break down silos." "We want everyone to feel ownership of the whole system." "We want a single engineering culture."
These are goals about people, and none of them are achieved by a folder structure.

## A Repo Is a Versioning Boundary, Not a Team Boundary

Strip the wishful thinking away and a monorepo is, precisely, a single unit of versioning history.
That is a powerful thing, but it answers the question "what commits together?", not "who works together?" ([Bird et al., "Why Google Stores Billions of Lines of Code in a Single Repository"](https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/)).

**Team-ness is a coordination property.**
A group is one team when they share goals, share accountability for outcomes, coordinate their work continuously, and can reach a decision without crossing an organizational negotiation.
None of that is created by colocating files.

You can have one team spread across many repositories, when their domain genuinely has independent release and trust boundaries.
You can have many teams sharing one repository, when the code is tightly coupled but the people are not.
And you can have the failure case that motivates this article: one repository full of teams who are not, in any operational sense, one team, pretending that shared history has done the work of shared purpose.

The two dimensions are orthogonal, and any combination of them is possible.

## Conway's Law Has Not Been Repealed

Melvin Conway observed that any system designed by an organization will mirror that organization's communication structure ([Conway, "How Do Committees Invent?"](https://www.melconway.com/Home/Conways_Law.html)).
This is usually cited as a warning about architecture, but it applies just as cleanly to repository layout.

When you merge five teams' code into one repo, Conway's Law does not shrug and retire.
The real communication boundaries reassert themselves, only now they have to be expressed as something other than repository URLs, because you took that signal away.
They come back as directory boundaries.
They come back as `CODEOWNERS` rules that require the payments team to approve anything under `payments/`.
They come back as "don't touch the billing code without tagging Sarah" whispered over chat.
They come back as review bottlenecks at the few people who understand the core libraries.

The boundaries were never really gone.
The monorepo just hid them, and hiding a boundary is not the same as removing it.
**Conway's Law guarantees that the team structure will win eventually; the only question is whether it wins through explicit ownership rules or through invisible friction.**

The healthier move is the inverse one: decide the team and communication structure you want first, then let the architecture and the repository follow ([ThoughtWorks, "Inverse Conway Maneuver"](https://www.thoughtworks.com/radar/techniques/inverse-conway-maneuver)).
Trying to run that maneuver in reverse, by editing the repo and hoping the org reorganizes itself to match, is causality pointed the wrong way.

## Shared Code Without Shared Ownership Spoils

The most predictable failure mode of the "we are all one team now" monorepo is the tragedy of the commons ([Wikipedia, "Tragedy of the commons"](https://en.wikipedia.org/wiki/Tragedy_of_the_commons)).

**When code belongs to everyone, it belongs to no one.**
A shared utility library that anyone can edit, and that no specific team is accountable for, accumulates half-finished abstractions, contradictory conventions, and bugs that survive because every team assumes another team will fix them.
Ownership that was crisp at the repository boundary becomes diffuse at the directory boundary, and diffuse ownership is how once-clean codebases rot.

This is why every mature large monorepo reinvents ownership internally.
The very organizations held up as proof that monorepos scale, Google prominent among them, lean on per-directory ownership files and review policies to recreate inside one repository the accountability that separate repositories gave them for free.
The ownership boundary was always going to exist; the choice is whether to design it deliberately or to rediscover it after a few outages.

The discipline that prevents the commons from spoiling is the same one Domain-Driven Design calls a bounded context: a region of the system with its own model, its own owners, and explicit contracts at its edges ([Fowler, "BoundedContext"](https://martinfowler.com/bliki/BoundedContext.html)).
Bounded contexts are a team concept expressed in code, and they work inside a monorepo exactly as well as across repositories, provided someone has the honesty to draw the lines.

## What Actually Makes People One Team

If you want the symptoms of single-team-ness, a repository is the wrong lever.
The real indicators are organizational, and every one of them has to be built on purpose.

A shared roadmap, where the people in question are optimizing for the same outcomes rather than negotiating for them.
Shared on-call and shared accountability for production, so that the cost of a bad change lands on the same people who profit from the feature.
Shared goals that are measured together, so that one group cannot succeed while the other fails on the same metric.
Psychological safety strong enough that a member of one sub-team can challenge a decision in another without it becoming an incident.
A single backlog of work that anyone can pull from, rather than two backlogs coordinated by a meeting.

**None of these come from `git clone`.**
They come from how performance is evaluated, how incidents are run, how planning is done, and how decisions are made.
A monorepo can be a useful substrate for those practices, the way a shared office can help a team gel, but it is a substrate, not a cause.

Team Topologies makes the point cleanly: team cognitive load is the real constraint on what a team can own, and team interaction modes, collaboration, x-as-a-service, facilitating, are the real ways teams relate ([Skelton and Pais, "Team Topologies"](https://teamtopologies.com/)).
A repository is not on that list, because a repository is not an interaction mode.

## The Inverse Is Also True

The mistake cuts in both directions, and the other half is worth saying plainly.

Multiple teams can share a monorepo and be perfectly healthy, as long as they are clear that they are multiple teams.
Clear ownership rules, explicit contracts at team boundaries, and review policies that respect those boundaries turn a shared repository into a convenient shared workspace rather than a false promise of unity.
The companies that run giant monorepos productively do exactly this; they did not become one giant team, they became many teams that share one version-control decision.

Similarly, one team can live across several repositories without being fractured, when those repositories follow real release or trust boundaries.
**The team is defined by the people coordinating, not by the number of remotes they push to.**

Once the two axes are separated, the design questions get easier.
Decide the team boundaries first, based on cognitive load, ownership, and coordination cost.
Then decide whether those teams' code lives together or apart, based on whether the code genuinely ships and evolves together.

## Conclusion

A monorepo is an excellent answer to the question of how to version code that moves together.
It is a non-answer to the question of how to make people work together.

If your teams are misaligned, a shared repository will not align them; it will give misaligned people more ways to step on each other, faster.
If your teams are aligned, the repository layout is a downstream optimization, and either model can be made to work.

**Repository structure should follow the coordination and trust structure, never lead it.**
When you find yourself reaching for a monorepo to fix a collaboration problem, that is a signal that you have a collaboration problem worth fixing directly, and that you are hoping a tool will save you the conversation.

It will not.
You will still have to have it.

## See also

- [Is the Monorepo the Ultimate Way to Version Your Code?](../monorepo-vs-multi-repo/index.md) - the companion piece on what a monorepo actually buys you, technically
- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) - how team size and friction interact with coordination cost, the true determinant of team boundaries
- [When Engineers Disagree on Best Practices](../when-engineers-disagree-on-best-practices/index.md) - resolving the kind of cross-team disputes that shared code tends to surface

## References

- [Conway, "How Do Committees Invent?"](https://www.melconway.com/Home/Conways_Law.html) - the original statement of Conway's Law, that systems mirror communication structure
- [ThoughtWorks, "Inverse Conway Maneuver"](https://www.thoughtworks.com/radar/techniques/inverse-conway-maneuver) - organizing teams to produce the desired architecture, rather than the reverse
- [Fowler, "BoundedContext"](https://martinfowler.com/bliki/BoundedContext.html) - the DDD idea of explicit ownership and model boundaries inside a codebase
- [Skelton and Pais, "Team Topologies"](https://teamtopologies.com/) - team cognitive load and team interaction modes as the real unit of org design
- [Wikipedia, "Tragedy of the commons"](https://en.wikipedia.org/wiki/Tragedy_of_the_commons) - the dynamic by which shared, unowned resources degrade
- [Bird et al., "Why Google Stores Billions of Lines of Code in a Single Repository"](https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/) - how ownership and review are recreated inside a giant monorepo
- [Dan Luu, "Advantages of monorepos"](https://danluu.com/monorepo/) - the technical case for monorepos, which this article takes as given
