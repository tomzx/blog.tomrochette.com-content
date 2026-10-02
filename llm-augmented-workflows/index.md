---

title: "llm-augmented-workflows - A config-driven automation engine for GitHub, powered by opencode"
created: 2026-07-02
type: post
status: finished
tags: [python, github, github-actions, llm, ai-agents, automation, workflows, skills, opencode, fully-ai-generated, llm=glm-5.2, llm=glm-5.3, llm=deepseek-v4.1-flash]
readability: 4
audience_notes: >
  Assumes the reader maintains a GitHub repository, has written a GitHub Actions workflow, and has at least seen an LLM coding agent (opencode, Claude Code, Cursor). No introduction to LLMs or CI.
agent_sessions:
  - ses_0de396603ffe8J70aOu42KwDtq
  - ses_0c555d9bfffeUL6dpThyPWb5n0
---

GitHub already provides a working event bus.
Issues get opened, labeled, and closed; PRs get reviewed and merged; comments land on lines and threads.
Every one of those events is a chance for an LLM agent to do useful work, triage the issue, draft a plan, reproduce a bug, post a review.
The gap is not the events and it is not the agents.
The gap is the code that connects them.

Today that connecting code is per-flow YAML.
Every workflow you want to automate gets its own `triage.yml`, `plan.yml`, `implement.yml`, each with its own copy of the agent invocation boilerplate, its own trigger, its own label math, and its own drift.
Add a fourth flow and you copy the file again.
Change how the agent is called and you edit all of them.
The workflows describe the same agent doing different things, but they share nothing.

I built [llm-augmented-workflows](https://github.com/TomzxCode/llm-augmented-workflows) to reduce all of that duplication to one file.
**You describe every flow as event-matched rules in a single `.github/llmaw/flows.yml`, and the dispatcher routes GitHub events to the right agent skill, with token-free label and shell steps for the transitions that do not need a model.**

## The problem

The moment you try to automate more than one agent-driven flow, the per-file pattern breaks down.

Each flow duplicates three things that it should not duplicate.
First, the wiring: trigger on this label, run the agent, relabel, wait for the next event.
Second, the agent invocation: which model, which skills repo, which timeout, which working directory.
Third, the outcome handling: what to do when the agent says *approved*, *rejected*, or *needs changes*.

That duplication has a cost.
Workflows drift from each other.
The agent invocation that worked yesterday is copy-pasted into the new flow with the old model id.
A label rename in one file does not propagate to the others.
And the parts of the flow that do not even need an LLM, relabeling an issue, posting a fixed comment, closing a linked issue on merge, still incur a model call because the file is built around one.

**What you want is to describe the *flow* once, and let the engine handle the wiring.**

## How it works

The engine is a small stateless dispatcher with one reusable GitHub Actions workflow.
**State is stored entirely in GitHub, in labels, issues, and PRs.**
The engine reads an event, matches it against `flows.yml`, runs the matched rule's pipeline, and exits.

```
GitHub event (issue labeled, PR merged, comment, ...)
   |
   v
dispatch.yml  reads flows.yml  ->  route matches rule(s)
   |
   v
for each matched rule, run-rule runs its whole `run` in one pass:
   labels/shell (pre) -> skill (opencode) -> labels/shell (post) -> on_outcome
   |
   v
the agent acts on GitHub (relabel, comment, open PR, close) -> emits new events
```

The pipeline is the unit of work.
A rule's `run` is an ordered list of steps, and the engine runs them in one pass: token-free label and shell steps can run before and after the agent, the agent step calls an opencode skill, and `on_outcome` maps the agent's verdict to labels, a close, or a comment.
Because relabeling emits a new event, the next phase of the flow is just another rule that matches the new label.
Terminal outcomes need no special handling: an agent closes an issue (won't fix), or a PR merges and an `on-merge` rule closes the linked issue.

## One config file, not one workflow per flow

Every flow is defined in `.github/llmaw/flows.yml`.
A flow is a list of rules, and a rule is a `when` (the event match) plus a `run` (the ordered pipeline).

```yaml
defaults:
  model: opencode/deepseek-v4-flash-free
  agents_repository: tomzx/agents
  timeout_minutes: 30
flows:
  plan:
    rules:
      - id: generate-plan
        when: { event: issues, action: labeled, label: plan-needed }
        run: [ { skill: generate-plan } ]
      - id: on-plan-merged
        when: { event: pull_request, action: closed, merged: true, branch_prefix: plan/ }
        run: [ { labels: { add: [plan-approved], target: linked-issue } } ]
      - id: implement
        when: { event: issues, action: labeled, label: plan-approved }
        run: [ { skill: implement-plan } ]
```

Read the file top to bottom and you have the whole flow.
An issue gets `plan-needed`, the `generate-plan` skill runs and opens a `plan/...` PR.
When that PR merges, `on-plan-merged` adds `plan-approved` to the linked issue, no model involved.
When the issue is labeled `plan-approved`, the `implement-plan` skill runs and implements it.
**Three rules, one file, one copy of the wiring.**

## Token-free transitions

Token-free transitions are the feature that justifies the whole design.

Relabeling an issue does not require an LLM, and neither does closing a linked issue on merge or posting a deterministic comment.
In llm-augmented-workflows, `labels` and `shell` steps run without calling the model at all.
The `on-plan-merged` rule above is a single label step: when the plan PR merges, add `plan-approved` to the linked issue.
Zero tokens, zero model latency, one GitHub API call.

**That means the agent only runs where the agent is actually needed, and the transitions between phases use no tokens, run fast, and are deterministic.**
A flow that used to cost three model calls (triage, plan, implement) plus the steps between them now costs two, because the step between them is a label.

## Two execution modes

Each matched rule's pipeline runs in one job.
What happens *after* the pipeline is controlled by the execution mode:

- **event-driven** (default): the rule runs once and the job ends.
  The relabel emits a new event that re-triggers the dispatcher for the next phase.
  One job per phase, each one independently observable in the Actions log.
- **continuous**: the same job keeps advancing to the next rule based on the labels each rule adds, until `llmaw:needs-human` appears or the chain reaches a resting state.
  One job per pipeline, the whole end-to-end run in one log.

Set it under `defaults.execution` or per flow, force it per dispatch via the `execution` input or the `LLMAW_EXECUTION` repo variable.
Event-driven is easier to debug; continuous is easier to watch flow end to end.
The same `flows.yml` works in either mode, because the mode is about how the engine chains rules, not how the rules are defined.

## Skills come from your agents repository

The `skill` step does not run an inline prompt.
It runs an opencode skill sourced from a configurable agents repository, `tomzx/agents` by default, overridable with `AGENTS_REPOSITORY`.

That separation is important.
The flow definition says *what* should happen and *when*.
**The skill definition says *how* the agent should do it.**
When you improve the `generate-plan` skill, every flow that references it gets the improvement, without touching `flows.yml`.
When you add a new flow, you reference an existing skill instead of inlining a prompt that will fall out of date.

## The default flow runs on the free model

The default model is `opencode/deepseek-v4-flash-free`, and it needs only the auto-provided `GITHUB_TOKEN`.
**You can adopt the engine on a throwaway repo without provisioning a single secret.**
Override per repo or per org with `OPENCODE_MODEL`, point `AGENTS_REPOSITORY` at your own skills, raise `LLMAW_MAX_ITERATIONS` for long continuous runs, and you are done.

## Getting started

Three steps.

1. Add one wrapper workflow to your repo, pinning the dispatcher by ref.

   `.github/workflows/llm-workflows.yml`

   ```yaml
   name: LLM Workflows
   on:
     issues: { types: [opened, labeled, reopened, closed] }
     pull_request: { types: [closed, labeled, ready_for_review] }
     issue_comment: { types: [created] }
     pull_request_review_comment: { types: [created] }
   permissions:
     contents: write
     pull-requests: write
     issues: write
   jobs:
     dispatch:
       uses: TomzxCode/llm-augmented-workflows/.github/workflows/dispatch.yml@v1
       secrets: inherit
   ```

2. Add `.github/llmaw/flows.yml` describing your flows.
   Start from the example above or the [`docs/flows.md`](https://github.com/TomzxCode/llm-augmented-workflows/blob/main/docs/flows.md) recipes for triage, close-on-merge, and per-step overrides.

3. Run the **Setup Labels** workflow to create the labels declared under `labels:`, or let your flows add them as needed.

Pin `@v1` for the latest within a major tag, `@main` if you want to track the tip, or `@<full-sha>` for an immutable production pin.

Consumers never copy the engine.
The dispatcher checks this repository out into `.llmaw/` on the worker and runs `uv run --project .llmaw llmaw ...`, pinning the version via the wrapper's `uses:` ref.

## What it does not do yet

The engine's unit of work is one issue per workflow execution.
A matched rule runs, the agent acts, the job ends (or chains within continuous mode until `needs-human`), and the next event is the next run.
That model fits small, well-scoped work well: triage this issue, plan this feature, reproduce this bug, implement this task.

**It does not fit a large epic.**
A change that spans many tasks, many PRs, and many days cannot be implemented by a single issue's pipeline, because the engine has no concept of an epic as a first-class object that owns child issues and tracks their aggregate progress.
To implement a large change today, you have to break the epic into per-task issues yourself, outside the engine, and let each of those issues run its own one-issue pipeline.
The decomposition step, deciding how to split the work and how the pieces depend on each other, is not automated.

Closing that gap is the next phase of the problem, and it is where the `needs-human` checkpoint currently does the most work.
Until the engine can take an epic, decompose it into ordered tasks, and drive each task through its own run while tracking the whole, large changes stay a manual decomposition followed by automated execution.

## Why this structure

I have been writing about the pieces of this for a while.
[Loops as Files](../loops-as-files/index.md) argued that the trigger layer deserves the same treatment as the prompt layer, versioned, reviewable, owned next to the behavior it schedules.
[The Self-Evolving Repository](../the-self-evolving-repository/index.md) pushed the question of how far you can take a GitHub project where every maintainer function is replaced by an automated loop.
**llm-augmented-workflows is the engine for both: the flows file is the schedule, the skills are the behavior, and the state stays in GitHub.**

If you already use [ghx](../ghx/index.md) for agentic code reviews or [github-board](../github-board/index.md) to visualize your issues, llm-augmented-workflows is the layer that keeps the issues moving.

## See also

- [Loops as Files](../loops-as-files/index.md) - the scheduling layer that `flows.yml` makes concrete per repository
- [The Self-Evolving Repository](../the-self-evolving-repository/index.md) - the end state this engine is built toward
- [ghx](../ghx/index.md) - the CLI the review skills use for inline PR comments the `gh` CLI does not expose
- [github-board](../github-board/index.md) - a kanban view over the same GitHub state these flows mutate
- [The Merge Gate](../the-merge-gate/index.md) - why the human checkpoint (`llmaw:needs-human`) stays in the loop
