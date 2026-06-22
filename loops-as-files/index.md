---
title: "Loops as Files: The Scheduling Layer Skills Forgot"
created: 2026-06-21
type: post
status: draft
tags: [llm, ai-agents, skills, automation, loops, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader already uses an LLM coding agent with skill or rule files (opencode, Claude Code, Cursor) and has at least seen a GitHub Actions workflow or a cron job. No introduction to LLMs.
---

Skills as files solved one half of the automation problem.
They told the model *how* to do a task, versioned and reviewable, loaded into context on demand.
They did not solve the other half.
They told the model nothing about *when* to run.
**A skill is inert until something invokes it, and in practice that something is almost always a human typing a command.**

That leaves the most experienced agent in your system doing nothing until you remember to ask it.
It also leaves every event in your environment, the issue that was just opened, the Slack thread that just heated up, the dependency that just shipped a security patch, waiting for a human to notice and forward it to the right skill.
The human has become the cron.

The fix is the same shape as the fix for the variance problem in [Bringing Everyone to the Same Level](../bringing-everyone-to-the-same-level/index.md): take the invisible process out of someone's head and make it a file.
Except the process to extract now is not "how do I triage an issue," it is "when do I triage issues, and what triggers that decision."
That belongs in a file too, and that file is a loop.

## The Asymmetry Between How and When

Skills files normalized a useful idea.
The prompt is the asset, the asset is text, text is versioned in git, and versioned text is reviewed, diffed, shared, and reused like code.
The same model that made skills valuable applies cleanly to the trigger layer, but the trigger layer is still being treated as plumbing.
It lives in crontabs nobody reads, in GitHub Action YAMLs that drift away from the skills they invoke, in shell scripts that bake agent invocations into system paths.

The result is that the two halves of an autonomous workflow live in different worlds.
The prompt is curated.
The trigger is improvised.
When the prompt changes, the trigger does not, and when the trigger breaks, nobody who understands the prompt finds out until the agent has been silent for a week.

**The schedule is part of the behavior.
A skill that runs on `/deploy` and the same skill that runs at 02:00 every Tuesday are not the same skill.
They have different blast radius, different cost profile, and different failure modes, and they deserve to be specified, reviewed, and owned together.**

## What a Loop File Is

A loop file is a markdown document with two parts.
The frontmatter declares when it runs and under what constraints.
The body declares what it does, almost always by composing skills that already exist.

In form it is the closest existing analog to a GitHub Actions workflow file, except the unit of work is not a shell command, it is an agent invocation with a loaded skill.

A minimal example:

```markdown
---
name: hourly-issue-triage
description: Triage new issues as they appear, every hour.
on:
  schedule:
    cron: "0 * * * *"
skills: [triage-issue]
budget:
  max-runs-per-day: 24
  max-cost-usd-per-run: 0.50
---

# Hourly Issue Triage

For every issue opened since the last run, invoke `/triage-issue`.
Defer to the skill for all classification logic.
Stop when the budget for this run is exhausted and resume on the next tick.
```

That is the whole artifact.
The skill owns the how.
The loop owns the when, the how-often, the how-much, and the what-to-do-when-it-breaks.
Each concern is in its own file, each file is reviewable, and changes to one do not silently invalidate the other.

## The Frontmatter Is the Contract

The reason the frontmatter matters more than the body is that the frontmatter is the part the runtime actually parses.
It is the contract between the human writing the loop and the system executing it.

A skill with no frontmatter is still useful as a document.
A loop with no frontmatter is a dead file.
So the fields that go in the frontmatter are not cosmetic metadata, they are the trigger specification, and they should be designed the way any interface is designed, with the smallest set of concepts that covers the realistic workload.

The field I want to anchor on is `on`, borrowed deliberately from GitHub Actions because the mental model is already widely understood.
`on` says what causes this loop to fire, and its value can be one or many of three things.

### Time

```yaml
on:
  schedule:
    cron: "0 * * * *"
```

Cron is the obvious first case, and there is no reason to invent a new syntax for it.
Cron is ugly, but it is universally understood, parseable, and already supported by every scheduler the reader is likely to have.
Most loops that need to run on a clock are well expressed as a single cron expression, and loops that need more complex recurrence can compose multiple loop files.

A secondary form worth supporting is an interval, for cases where wall-clock alignment does not matter:

```yaml
on:
  interval:
    every: 15m
```

Interval is easier to read and easier to distribute across a fleet, since N agents with `every: 15m` will naturally desynchronize in a way that `cron` will not.

### Events

Time is the easy case.
The interesting case is event-driven, and the reason the user's framing matters is that "loops" undersells what is going on.
A loop that fires on a schedule is just a cron job with a markdown file on top.
A loop that fires on an event is something genuinely new: a versioned, reviewable handler for things that happen in the world.

```yaml
on:
  events:
    - type: github.issues.opened
      repo: "owner/repo"
      filter: "labels.length == 0"

    - type: slack.mention
      channels: ["#support"]
      filter: "text contains 'sev1'"

    - type: github.pull_request.opened
      repo: "owner/repo"
      filter: "author.trust < 'trusted'"

    - type: file.changed
      paths: ["pyproject.toml", "uv.lock"]

    - type: metric.threshold
      metric: api.error_rate
      window: 5m
      op: ">"
      value: 0.01
```

The shape is the same in every case: a typed event source, an optional scope, and an optional filter expression.
The types themselves are namespaced by source (`github.*`, `slack.*`, `file.*`, `metric.*`) so that adding a new integration is additive rather than a schema change.

A single loop can declare multiple events, and the runtime treats them as a logical OR.
That covers the common case of "I want this skill to fire on a cron *and* when a human pokes it," which is exactly the shape of most operational loops.

### Webhooks

The third trigger is a catch-all for events the runtime cannot subscribe to directly.
A webhook is an event source the runtime exposes rather than consumes.

```yaml
on:
  webhook:
    path: /loops/deploy-staging
    secret: ${DEPLOY_WEBHOOK_SECRET}
```

Anything that can hit an HTTP endpoint, from a monitoring tool to a ChatOps button to a physical device, can now trigger a skill, and the access control lives next to the prompt it gates.

## The Frontmatter That Prevents the Loop From Eating Your Wallet

Time and events say when to start.
The loop also needs to say when to stop, and this is the part that existing skill files do not need and loop files cannot live without.

```yaml
budget:
  max-runs-per-day: 24
  max-cost-usd-per-run: 0.50
  max-concurrent: 1
concurrency: cancel-previous
timeout: 10m
on-failure: alert      # alert | retry | escalate | ignore
escalation:
  skill: notify-on-call
  after: 3 failures
```

I argued in [The Self-Evolving Repository](../the-self-evolving-repository/index.md) that cost runaway is one of the defining failure modes of autonomous systems, and a loop without a budget is one bad `while True` away from being a case study.
Every loop file should be able to answer three questions without ambiguity: how often can this run, how much can each run spend, and what happens when it fails.
If a loop cannot answer those questions, the runtime should refuse to start it.

The `concurrency` field is the other one that earns its keep early.
A loop that runs every five minutes and takes six minutes to finish will, without a concurrency policy, slowly consume every slot the runtime has.
`cancel-previous`, `queue`, and `drop` cover the realistic cases, and the right default is `cancel-previous` for anything stateless.

## Loops Compose Skills, They Do Not Replace Them

There is a temptation, once you have a loop format, to start inlining the prompt into the loop body.
Resist it.
A loop file should read like an orchestrator, not like a skill, because it is one.

The body of a loop is typically a short sequence of skill invocations, with just enough glue logic to express ordering, branching, and handoff.

```markdown
# Nightly Dependency Review

1. `/audit-dependencies` against the current lockfile.
2. If it reports any `severity >= high`, `/create-issue` with the audit output.
3. `/notify-on-call` summarizing counts and the worst offender.
```

Three skills, one paragraph of orchestration, fully readable.
The logic that is hard (what counts as a high-severity vulnerability, how to phrase an issue, who the on-call is) lives in the skills it invokes, where it can be improved independently, tested independently, and reused from other loops.

This also keeps the loop file honest about its job.
A loop file that grows past a screen of text is probably doing the work of a skill and should be split.
The same length discipline that keeps skills effective, which I borrowed from the "lost in the middle" argument in [Bringing Everyone to the Same Level](../bringing-everyone-to-the-same-level/index.md), applies to loops.
If the runtime has to parse a long preamble before it even reaches the trigger, the trigger is no longer the contract.

## Why Loops Have to Be Files

Every argument for skills as files applies, with minor edits, to loops as files, and one new argument applies only to loops.

**Versioning.**
A trigger change is a behavior change.
"Run triage on every new issue" and "run triage on every new issue except those from outside contributors" are different policies with different consequences.
A trigger that lives in a crontab or a GitHub Actions YAML that nobody reviews is a policy that nobody reviewed, and reviewing it matters because the consequences of a trigger bug (silently not running, or silently running too often) are usually larger than the consequences of a prompt bug.

**Reviewability.**
A loop file in git means every change goes through a pull request, which means the blast radius of the change is visible to the people who will be paged when it goes wrong.
This is the same point I made, about code, in [The Codebase Gardener](../the-codebase-gardener/index.md): a standard that lives only in someone's head is a standard that dies when that person goes on vacation.
A loop that lives only in someone's crontab has the same half-life.

**Portability.**
A loop file describes what should happen, not where it runs.
The same file can be executed by a local scheduler during development, by a team-shared runner in production, and by a CI provider that wants to dry-run it on every commit.
That portability is what makes loops shareable across teams the way skills are shareable, and it is what makes a "loop library" a coherent concept in a way that a "crontab library" never was.

**Diffability.**
The single most useful property of a file is that you can `git blame` it.
When the on-call gets paged at 03:00 because the deployment loop has been firing every two minutes for an hour, the first question is "who changed the trigger, when, and why," and the answer should be one `git log` away, not an archaeological dig through a CI settings UI.

The argument that applies only to loops is **co-location with the skill**.
A skill file and the loop that schedules it are describing two facets of the same behavior, and when they live in the same repository, in the same format, in the same review pipeline, they evolve together.
A skill change that should have changed the trigger (say, "this skill is now expensive, run it less often") is a change that can actually be made in the same pull request by the same person who understood the consequence.

## What the Runtime Owes You

A loop format without a runtime is a markdown opinion.
The runtime is what makes loops safe to leave running, and it owes the operator a small, specific set of behaviors that are not optional.

**Idempotency by default.**
A loop will be double-triggered.
The cron will fire twice during a clock skew.
The webhook will be retried.
The runtime must be willing to run the same loop with the same inputs twice and treat the second run as a no-op, which means the skills it invokes must be idempotent, which is a property worth designing into skills whether they are loop-driven or not.

**Per-run state.**
Every run writes a state file, in the same shape I described in [Managing Many Concurrent LLM Agent Sessions](../managing-many-llm-agent-sessions/index.md): what fired, what ran, what it produced, what it cost, what it will do next time.
Without this, debugging a misbehaving loop is reading logs, and reading logs is what we used to do before we had files.

**A kill switch.**
There must be one command, one CLI flag, one environment variable, that stops every running loop and disables every scheduled trigger.
The cost of not having this is the cost of not having a circuit breaker in your electrical panel.

**Observability that is not optional.**
A loop that fails silently is strictly worse than no loop at all, because no loop at least fails loudly when a human expected it.
Every run emits run-started, run-succeeded, run-failed, run-budget-exceeded events, and the runtime ships them to whatever sink the operator already trusts.

**Dry run.**
`--dry-run` evaluates the trigger, selects the skill, expands the inputs, and prints what it would have done, without invoking the model.
This is the cheapest possible way to debug a trigger filter, and it should exist on every loop runner.

## What Goes Wrong

Loops inherit the failure modes of any autonomous system and add two of their own.

**Drift toward the measurable.**
A loop that fires on `github.issues.opened` will, over time, optimize the project for issue-shaped signals, because those are the signals that cause work to happen.
The project stops reacting to anything that does not show up as an event the loop can see.
This is Goodhart's law applied to ops automation, and the defense is the same as in the self-evolving repository: keep a human-edited roadmap, and reserve a small number of loops for periodic "what should we be working on" reflection that is not event-driven.

**Loops stepping on loops.**
Once loops are cheap to write, people write a lot of them.
Two loops that both touch the same issue tracker, both with their own opinions about labels and priorities, will quietly fight each other, and the issue tracker will lose.
The runtime needs loop-level isolation (separate working directories, separate state files, separate rate limits) and a registry that makes it easy to answer "which loops currently fire on this event," the same way a codebase makes it easy to answer "which tests currently exercise this function."

**Trigger rot.**
A loop that worked when it was written will silently stop working when the thing it triggers on changes shape, the GitHub webhook payload gains a field, the Slack channel gets renamed, the metric gets relabeled.
Loops need the same periodic sweep that code needs, and the sweep is mechanical: for each loop, fire its trigger in dry-run, confirm the skill still runs, retire the loops that nobody owns.

**Cost runaway, again.**
Worth saying twice.
An event-driven loop with no budget, attached to a busy event source, is a direct line from "Slack got excited" to "the API bill is four digits."
The budget field in the frontmatter exists for exactly this reason, and the runtime must enforce it hard, not warn softly.

## The Naming Question

I have used "loop" throughout because it captures the simplest mental model: something that runs again and again.
It is worth being honest that "loop" undersells the format.
A loop that fires only on `slack.mention` is not really looping.
It is reacting.

The more accurate name is probably "routine," "trigger," or "automation," and the reason none of those quite land is that each one emphasizes one of the two trigger classes at the expense of the other.
"Loop" emphasizes time.
"Trigger" emphasizes events.
"Routine" emphasizes the work.
The format itself does not care.
The `on:` field is the source of truth, and the file is whatever its trigger says it is.

In practice, teams that adopt this will settle on one word and use it for both, the same way "skill" is now used for files that range from one-line hints to multi-page workflows.
The word matters less than the format, and the format is: markdown, frontmatter, `on`, a budget, a short body.

## What to Do on Monday

You do not need a runtime to start.

Find the one task that you do on a cadence and keep doing manually because it is "too small to automate."
Triage the overnight issue queue.
Summarize the Slack channel at end of day.
Check whether dependencies have shipped patches.
That task is your first loop.

Write it as a loop file, even if the runtime that will execute it does not exist yet.
Write the frontmatter honestly, the trigger you want, the budget you would accept, the skill it should invoke.
If the skill does not exist yet, write its stub too.

You now have two artifacts that describe the behavior you want, in the same repository, in the same format, reviewable in the same pull request.
When a runtime arrives (and several already will, given how cheaply existing coding agents can be wrapped in a scheduler), your loop is ready to drop in.

Then do it again with the next task, and the next.
Each loop file is a piece of operational judgment that stops being a private habit and starts being a shared, owned, versioned standard.
The team that wins in this era is not the one with the most skills.
**It is the one whose skills run, on time and on event, without anyone remembering to ask them to.**

## See also

- [Bringing Everyone to the Same Level](../bringing-everyone-to-the-same-level/index.md) - the case for skills as files; this article is the same argument one layer up, applied to the trigger instead of the prompt
- [The Self-Evolving Repository](../the-self-evolving-repository/index.md) - the autonomous loop at project scale; loop files are how you make that loop inspectable and bounded
- [Managing Many Concurrent LLM Agent Sessions](../managing-many-llm-agent-sessions/index.md) - the per-run state file pattern that loops need to inherit to be debuggable
- [The Codebase Gardener](../the-codebase-gardener/index.md) - the argument that standards only count when they are encoded; triggers are standards
- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - once skills make execution cheap, the leverage moves up, and the trigger layer is one of the places it moves to
- [Scaling the LLM Agent Company](../scaling-the-llm-agent-company/index.md) - the cost and correlated-failure concerns that the budget and concurrency fields in a loop file exist to contain

## References

- [Wikipedia, "Cron"](https://en.wikipedia.org/wiki/Cron) - the time-based job scheduler whose syntax the `on.schedule.cron` field borrows wholesale, because there is no value in inventing a new one
- [GitHub Actions documentation, "Events that trigger workflows"](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows) - the `on:` mental model and event taxonomy this format deliberately mirrors, so readers do not have to learn a new concept
- [Wikipedia, "Idempotence"](https://en.wikipedia.org/wiki/Idempotence) - the mathematical property that makes loops safe to re-trigger, and therefore the property every skill invoked by a loop must be designed to have
- [Wikipedia, "Goodhart's law"](https://en.wikipedia.org/wiki/Goodhart%27s_law) - why an event-driven loop will optimize for whatever its events measure, and why a non-event-driven reflection loop must exist alongside it
- [Wikipedia, "The Checklist Manifesto"](https://en.wikipedia.org/wiki/The_Checklist_Manifesto) - Atul Gawande's case that disciplined, written checklists outperform expert memory, which is the same argument for trigger files as it was for skill files
