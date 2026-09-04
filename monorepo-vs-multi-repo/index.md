---

title: "Is the Monorepo the Ultimate Way to Version Your Code?"
created: 2026-06-23
type: post
status: draft
tags: [software-engineering, version-control, monorepo, architecture, multi-repo, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes familiarity with version control, CI/CD, and basic software architecture concepts.
agent_sessions:
  - ses_10ae5636dffeCiXCFf5NeEIXLp
---

Every few years the same argument restarts.
Should an organization keep its code in one repository or many?
People point at Google and Meta, who put billions of lines of code in a single repository, and then point at the open-source world, which lives across millions of small ones, and ask which model is right.

The candid answer is that "right" is the wrong question.
The right question is what each model actually buys you, and where the boundary of that purchase runs out.

## The Main Value Proposition, Stated Plainly

The monorepo's central value proposition is a single property, and almost every benefit people list is a consequence of it.

**At every commit, the entire codebase is in a consistent, working state, and a change that spans many projects can be made atomically.**

That is the whole pitch.
One version of everything.
One source of truth.
A change to a shared library and the fix to every one of its callers can land in the same commit, because they live in the same history.

Everything else people love about monorepos, the shared tooling, the easy code sharing, the visibility, the unified dependency graph, is downstream of that one fact.
If you understand the atomic cross-cutting change, you understand why Google stores billions of lines in one repository and why engineers there call it a competitive advantage ([Bird et al., "Why Google Stores Billions of Lines of Code in a Single Repository"](https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/)).

## The Multi-Repo Coordination Tax

To see why atomicity matters, watch what happens when you do not have it.

You have a shared library used by twelve services, each in its own repository.
You want to change the library's API.
The library is well designed, so this is a legitimate, healthy change.

In a multi-repo world the change becomes a dance.
You edit the library, cut a new version, publish it.
Then you visit each of the twelve consumers, bump the dependency, fix the breakage the new API caused, and release each service in some safe order.
**If one consumer is owned by a team that is busy, the library is now stuck supporting two APIs, and "temporary" becomes permanent.**
The coordination is manual, sequential, and fragile.

In a monorepo you change the library and all twelve callers in one commit.
Either the whole thing builds and tests pass, or none of it lands.
There is no version to bump because there is only one version.
There is no publish step because there is no package boundary to cross.
The change is one unit of work, reviewed as one unit, reverted as one unit if it goes wrong.

This is the property people are reaching for when they say monorepos "scale."
Dan Luu puts the same point more bluntly: monorepos solve the atomic cross-project commit problem in exactly the way git and Mercurial solved the atomic cross-file commit problem a generation ago ([Dan Luu, "Advantages of monorepos"](https://danluu.com/monorepo/)).
Nobody argues anymore whether cross-file atomic commits are worth having.
The cross-project version of the same idea is harder to see because it is newer, but it is the same kind of win.

## One Identifier for the Whole System

There is a consequence of atomicity that is easy to state and hard to overvalue.

In a monorepo, a single commit hash names the entire state of the codebase at a point in time.
Every service, every library, every configuration, pinned by one identifier.
That hash is the answer to "what was running when this bug appeared," to "reproduce last Tuesday's build," and to "roll the system back to a known-good state."
It is also the snapshot an agent can hold as the world it is reasoning about, and re-check against after it acts.

A polyrepo setup can only approximate this, and the approximation is a second-class property.
You can keep a manifest or lockfile that pins each repository to a specific commit, and git submodules are the native form of the idea.
But the identifier is now a tuple of hashes, or a commit in yet another repo pointing at the rest, not a single intrinsic pointer.
The manifest is assembled after the fact, so it can drift from what each repo actually contains, and nothing guarantees the pinned combination even builds together until somebody runs the full matrix, which is expensive and so gets skipped until something breaks.

The difference is between a guarantee and a claim.
**A monorepo commit is a guarantee: at this identifier, the entire system was in a verified working state.**
A polyrepo manifest is a claim: we believe these versions went together, and we last checked at some point.

## Why That Single Property Keeps Paying Off

Atomicity is the seed.
The tree that grows from it is large.

**Code sharing becomes nearly free.**
In a multi-repo setup, sharing code between services means standing up a package, a registry, a publishing pipeline, a versioning policy, and a deprecation strategy.
That overhead is real, so teams do the rational thing: they copy the code instead.
Duplication multiplies, and a bug fixed in one copy stays alive in nine others.
In a monorepo, sharing a new library is creating a folder.
There is no publishing step and no version to reconcile, so the cost that discouraged sharing disappears.

**Tooling is unified by default.**
When all code lives under one root, one build system, one linter, one CI configuration, and one set of conventions apply everywhere ([Bazel](https://bazel.build/), the build system that grew out of Google's monorepo, exists precisely to make this true at scale).
Code search, static analysis, and refactoring tools operate across project boundaries without extra plumbing, because there are no boundaries to bridge.

**Engineers can move.**
A developer can navigate from the frontend to the backend to the shared libraries with the same `cd` they use inside a single project.
Onboarding, debugging across services, and understanding the full path of a request all get cheaper when the whole system is one checkout.

**Visibility replaces documentation.**
You do not need a wiki describing the API of another team's service when you can read the implementation.
As more of that implementation is read by machines rather than humans, this property matters more, not less.

## Why AI Agents Tilt the Scales Toward a Monorepo

There is a reason the monorepo debate is heating up again, and it is not nostalgia.

An AI coding agent is bounded by one thing above all: the context it can reach.
The quality of what an agent produces is roughly proportional to how much of the relevant code it can actually read and run against.
Inside a single repository that is a solved problem.
Across many repositories, it is the problem.

Take the same shared-library refactor from earlier, but hand it to an agent.
In a monorepo, one agent session can change the library, walk every caller, fix each breakage, run the full affected test suite, and open one coherent pull request, because every caller lives in the same graph it is already reasoning over ([monorepo.tools, "Monorepos Amplify AI Agents"](https://monorepo.tools/)).
The agent does not need anyone to tell it what the other services expect; it reads the implementation.

In a multi-repo setup that same task falls apart.
The agent can change the library, but then it hits the repository wall.
It cannot see the callers, so it cannot fix them, and it cannot run their tests to know whether its change broke anything.
Each consumer becomes a separate session with no shared state, and the human becomes the bridge that ferries context between them: this is the API surface, this is what the other service expects, here is the published type definition that may already be stale.

Repo boundaries are a coordination tax that humans pay with meetings and chat messages.
**Agents have no cheap way to pay that tax, so the same boundary that mildly annoys a human stops an agent entirely.**

The deepest asymmetry is in the feedback loop.
In a monorepo, a backend change that breaks the frontend surfaces instantly, in the same session, against the real tests, with the agent knowing it made the change.
In a multi-repo world the failure surfaces much later, in a different session, after a publish and a dependency bump, when the agent that caused it is long gone and the context is lost.
Agents are good at fixing things they just broke and can see.
They are bad at fixing things that break elsewhere, later, for reasons they cannot observe.

There is also the matter of proof.
A monorepo gives an agent a single place to demonstrate that a change is complete: the affected tests pass, the type checker is green, the lint is clean, across every consumer at once.
"Does everything still work together" is a question a monorepo can answer from one vantage point, and a polyrepo world fundamentally cannot.

None of this makes the monorepo automatically correct.
It does mean the coordination cost a monorepo eliminates is the exact cost AI agents are worst at paying, and as more of the work of writing and maintaining software shifts to agents, that alignment compounds.

## The Real Costs

A monorepo is not free, and pretending otherwise is how organizations adopt one and then suffer.

**It demands tooling investment that scales with size.**
A ten-person company can put everything in one git repository and never feel pain.
A ten-thousand-person company cannot.
Plain git starts to strain at hundreds of thousands of commits and millions of files, and the companies that run giant monorepos have patched their version control to cope ([Meta, "Scaling Mercurial at Facebook"](https://code.fb.com/core-data/scaling-mercurial-at-facebook/)).
If you do not have, or do not build, the build caching, the affected-change detection, and the remote execution that makes a large monorepo tractable, you inherit Google-scale problems on a startup budget.

**Access control is coarser.**
In a multi-repo world, the repository boundary is a natural permission boundary: the payments team owns its repo, the marketing site owns theirs.
A monorepo has to recreate those boundaries with tooling, through path-level ownership rules and code review policies, and that layer is never quite as clean as a separate repository.

**The blast radius of a bad change is larger.**
Atomic cross-cutting commits are a feature until someone lands a bad one.
A single commit that touches shared code can break every consumer at once, so the safety nets (tests, canaries, rollback paths) have to be proportionally stronger.

**Not everything belongs together.**
Open-source libraries, vendored third-party code, and genuinely independent products have their own release cadences, their own contributors, and their own trust boundaries.
Forcing them into one repository fights their nature.

## The Decision, Without the Religion

**Strip the tribal identity out of it and the choice reduces to one variable: where does your coordination cost live?**

If your projects are tightly coupled, ship together, and share code constantly, the coordination cost of keeping them separate is high and the monorepo eliminates most of it.
A product company building one application, with a frontend, a backend, and shared libraries that move together, is the textbook case where a monorepo is the right default ([ThoughtWorks Technology Radar, "Monorepo"](https://www.thoughtworks.com/radar/techniques/monorepo)).

If your projects are independent, have different owners and release cadences, or are distributed to the outside world, the coordination cost of keeping them together is higher than the cost of keeping them apart.
An open-source ecosystem, a platform with many independent consumers, or a holding company of unrelated products all fit the multi-repo model better, because the trust and release boundaries genuinely do not line up.

**The repository boundary should match the coordination and trust boundary.**
When those boundaries align, the choice makes itself.

## So, Is It Ultimate?

If "ultimate" means universally superior, then no.
There are real organizations for whom many small repositories are the correct answer, and the properties that make a monorepo great become liabilities when the things inside it do not actually belong together.

But if "ultimate" means the model with the single most valuable property in code versioning, the monorepo has a strong claim.
**Atomic, cross-cutting change against a single source of truth is the property every other good thing follows from**, and it is the property the alternatives spend the most effort recreating badly through versioning, publishing, and orchestration tooling.

The frontier of where a monorepo pays off is also moving.
Remote caching, affected-change detection, distributed execution, and even "synthetic" monorepos that build one dependency graph across many physical repositories are pushing the practical boundary outward, so the set of organizations for which a monorepo is the right answer is larger today than it was five years ago, and larger still for any organization leaning hard on AI agents.

The monorepo is not the end of history for code versioning.
But its core proposition is the one most worth optimizing for, and the burden of proof now sits more heavily on the case for splitting up.

## See also

- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) - how AI shifts engineering bottlenecks toward coordination, the cost a monorepo eliminates
- [The Self-Evolving Repository](../the-self-evolving-repository/index.md) - automating a whole GitHub project, which leans on repository structure being tractable for agents
- [The Merge Gate](../the-merge-gate/index.md) - how code lands safely, complementary to the question of where code lives

## References

- [Bird et al., "Why Google Stores Billions of Lines of Code in a Single Repository"](https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/) - the canonical study of a giant monorepo and why Google keeps it
- [Dan Luu, "Advantages of monorepos"](https://danluu.com/monorepo/) - the clearest case that atomic cross-project changes are the core win
- [monorepo.tools, "Monorepos Amplify AI Agents"](https://monorepo.tools/) - framing of repo boundaries as walls for AI agents
- [Meta, "Scaling Mercurial at Facebook"](https://code.fb.com/core-data/scaling-mercurial-at-facebook/) - the tooling investment required to run a monorepo at scale
- [Bazel](https://bazel.build/) - the build system that grew out of Google's monorepo
- [ThoughtWorks Technology Radar, "Monorepo"](https://www.thoughtworks.com/radar/techniques/monorepo) - a neutral adopt/trial framing of when it fits
