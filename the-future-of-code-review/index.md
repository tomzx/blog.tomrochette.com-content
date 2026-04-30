---
title: "The Future of Code Review: How AI Makes Human Review Obsolete"
created: 2026-04-18
type: post
status: finished
tags: [ai, software-engineering, code-review, llm, fully-ai-generated, llm=glm-5.1]
readability: 3
---

The traditional code review is dying.
Not because it's unnecessary, but because it's becoming unnecessary.

For decades, code review has been a cornerstone of software engineering.
Pull requests, peer reviews, endless rounds of comments - this is how we've maintained code quality.
But AI is fundamentally changing this equation.
The question isn't whether AI will replace human code review, but how quickly.

## The Problem With Human Code Review

Human code review suffers from three fatal flaws:

1. **It doesn't scale**.
As teams grow, review backlogs grow.
Developers wait days or weeks for feedback, blocking progress.

2. **It's inconsistent**.
Reviews vary wildly based on who's reviewing, when they're reviewing, and how much coffee they've had.

3. **It's expensive**.
Senior engineers spend significant time reviewing code instead of building features.
In high-cost engineering organizations, this is millions of dollars annually.

The alternative - no reviews - isn't viable either.
Shipping unreviewed code is a recipe for security vulnerabilities, bugs, and technical debt.

## The AI Solution: Software Factories

A new paradigm is emerging: the Software Factory.
Instead of humans reviewing code, AI systems verify, test, and heal code autonomously.
This isn't theoretical, it's already running in production.

Consider StrongDM's Software Factory, which launched in July 2025.
A team of three people (CTO, senior manager, and a new hire) built a system that autonomously clones core products like Okta, Jira, and Slack.
Their target: $1,000 per day per engineer in tokens.
Sounds expensive until you realize what they're shipping.

## How It Works

The Software Factory approach replaces human review with six verification layers:

### 1. Competitive Generation

Instead of one AI writing code, run three in parallel.
Like a slot machine with three reels spinning, all generating different implementations.
An automated evaluator selects the best output based on passing tests, minimal diffs, and fewer dependencies.
The cost of running three models is trivial compared to the quality gain.

### 2. Iterative Refinement (Trycycle)

Define the problem, write a plan, ask "is it perfect?"
If not, try again.
Implement, then ask "is it perfect?"
If not, try again.
This loop can run autonomously for hours.

### 3. Scenario-Based Validation

Treat scenarios like machine learning holdout sets.
Store acceptance scenarios outside the codebase, then have an LLM judge whether the implementation satisfies them.
Instead of a binary "tests pass," you get a probabilistic satisfaction score measuring trajectory toward success.

### 4. Observability and Healing

Every interaction in the system gets logged to an execution database (CXDB).
A Healer agent monitors this database, clusters similar problems, and writes prescriptions.
No human bug reports.
No human triage.
Just autonomous detection and fixing.

### 5. Digital Twin Testing

Clone critical external dependencies - Google Sheets, Slack, Jira, authentication providers.
Build replicas that AI agents cannot distinguish from production.
Test in the most realistic environment possible without touching actual production systems.

### 6. Adversarial Verification

Separate the coding agent from the verification agent.
Have a third agent actively try to break what was built.
Enforce that verification criteria are authored before code, not after.
This prevents the common anti-pattern of writing tests to match implementation rather than specify behavior.

## The Economic Case

This approach isn't just about quality, it's about economics.

StrongDM's team reports seeing 21% more tasks completed and 98% more pull requests shipped.
One case study: Nubank migrated an eight-year ETL monolith (six million lines, one thousand engineers) from an 18-month timeline to weeks.
That's an 8-12x efficiency improvement with 20x cost savings.

The breakeven point is 50-70 pull requests per month.
Above that threshold, the AI factory costs less than human review while delivering higher velocity.

## The Five-Level Evolution

Dan Shapiro at StrongDM describes five levels of AI-assisted development:

**Level 0**: Manual (you write everything)
**Level 1**: Offloading discrete tasks (ChatGPT for regex)
**Level 2**: AI-native tools (90% of "AI" developers today)
**Level 3**: Human-in-the-loop manager (reviewing all code)
**Level 4**: You're now a product manager (spec, argue, craft skills, check tomorrow)
**Level 5**: Dark Factory (black box: specs → software)

Most teams today are stuck at Level 2 or 3.
The future is Levels 4 and 5, where humans specify constraints and AI handles everything else.

## What This Means For Engineers

Your job is not to write code.
Your job is not to read code.
Your job is to solve quality problems so the factory can run.

This requires a philosophical shift.
Instead of "how do I review this code?" ask "why am I doing this?"
If you can describe what's wrong, you can automate it.
If you can describe what quality looks like, you can codify it as a verification rule.

The era of human-centric development is ending.
AI compilers will transform specifications into deployed software.
Teams will consist of AI business analysts, AI DevOps engineers, AI QA specialists, and AI compilers.

## The Implementation Path

This doesn't happen overnight.
A realistic 16-week roadmap:

**Weeks 1-2**: Install Trycycle skill and competitive generation pattern
**Weeks 3-4**: Build execution database and scenario framework
**Weeks 5-6**: Implement Healer agent for autonomous fixes
**Weeks 7-8**: Build digital twins for critical integrations
**Weeks 9-12**: Migrate existing codebase to spec-driven workflow
**Weeks 13-16**: Fine-tuning and compounding learning

The results compound.
Weeks 1-4 might yield 5-10x velocity on simple tasks.
By week 16, teams report 2x monthly speed improvements with compounding gains continuing.

## Open Questions

This isn't a solved problem.
Key research questions remain:

- Is $1,000/day per engineer in tokens realistic or an outlier?
- How do patterns learned in one domain transfer to another?
- When does fine-tuning cost outweigh compounding benefits?
- What specific patterns trigger unavoidable human review?
- How do you validate security without human review of auth logic?

These aren't blockers, they're opportunities for teams to pioneer solutions.

## The End of an Era

The traditional code review served us well.
But like manual testing before automated test suites, its time is passing.
The future isn't humans reviewing AI code.
It's humans designing verification systems that make human review unnecessary.

The question isn't whether your team will adopt this approach.
The question is whether your competitors will adopt it first.

## References

**Primary Sources**

StrongDM Software Factory. Production deployment of autonomous code generation systems.
https://factory.strongdm.ai/

Kilroy. Open-source CLI for running StrongDM-style pipelines locally.
https://github.com/danshapiro/kilroy

Attractor. Provider-agnostic framework for autonomous code generation.
https://github.com/strongdm/attractor

Trycycle. Simple skill for iterative refinement loops.
https://github.com/danshapiro/trycycle

Devin. AI-powered software engineering platform with fine-tuning capabilities.
https://devin.ai/

**Analysis and Commentary**

Willison, Simon. "Software Factory."
https://simonwillison.net/2026/Feb/7/software-factory/

Shapiro, Dan. "The Five Levels."
https://www.danshapiro.com/blog/2026/01/the-five-levels/

Shapiro, Dan. "Dark Factories."
https://www.danshapiro.com/blog/2026/03/dark-factories/

Shapiro, Dan. "You Don't Write the Code."
https://www.danshapiro.com/blog/2026/02/you-dont-write-the-code/

LukePM. "The Software Factory."
https://lukepm.com/blog/the-software-factory/

Latent Space. "Reviews Dead."
https://www.latent.space/p/reviews-dead

**Case Studies**

Nubank ETL Migration. Eight-year monolith migrated in weeks using Devin.
https://devin.ai/

StrongDM Security Software. Autonomous cloning of Okta, Jira, and Slack.
https://factory.strongdm.ai/
