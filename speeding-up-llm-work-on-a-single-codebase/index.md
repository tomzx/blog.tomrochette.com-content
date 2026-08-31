---
title: "Speeding Up LLM Work on a Single Codebase"
created: 2026-08-31
type: post
status: finished
tags: [llm, ai-agents, git, parallelism, productivity, software-engineering, partially-ai-generated, llm=glm-5.3-flash]
readability: 3
audience_notes: >
  Assumes the reader is a software engineer who already runs LLM coding agents (Claude Code, opencode, or similar) against a real repository and knows git branching. Git worktrees are explained from first principles, but no agent-internals knowledge is assumed.
---

When I work with a coding agent, most of the wall clock time goes to waiting.
The agent thinks and edits, I watch the spinner, then review the result, then queue the next task, and the whole loop runs serially all day.
**The biggest speedup available in agentic coding is not a smarter model, it is running more of the work at the same time.**
Almost every real codebase carries more independent work than one session can absorb: the bug in the parser, the new endpoint, the dependency upgrade, the flaky test.
The hard part is not spawning extra sessions, it is keeping them from stepping on each other, and that is a git and workflow problem before it is an AI problem.

## Why One Session Is the Slow Configuration

A single session is not literally a queue of length one, most harnesses let you queue or steer messages that the agent consumes at its own pace.
But a queued message is not parallel work: the session still executes its queue one item at a time, so task two waits while task one runs, and the agent waits while you review.
The model inside the session is not the constraint, the serialization is.
The progression I use goes from one branch with one task, to one branch with several non-colliding tasks, to one worktree per task, and finally to a pool of worktrees fed with more tasks than there are worktrees.
Shared branches are the cheap first step, [git worktrees](https://git-scm.com/docs/git-worktree) are the mechanism that makes concurrency safe once tasks start colliding, and an orchestrator is what you add when coordination itself outgrows your attention.

## Share a Branch When Tasks Cannot Collide

The configuration you already run is one branch with one task and one session.
When your tasks provably cannot collide, the cheapest upgrade is to keep that single branch and add sessions to it, each working on separate files at the same time.
Nothing to merge, no duplicated environments, and the moment a session finishes, its work is already on the branch.
The failure modes are just as real: two agents editing the same file silently overwrite each other on disk, an agent's context goes stale as files change under it, and simultaneous commits race on the git index.
Last writer wins, and nobody notices until tests fail for reasons neither change explains on its own.

**Sharing a branch moves the isolation problem from the filesystem into your head, so only use it when the tasks provably do not touch the same files.**
The rules that make it work:

- Partition by module before spawning, and state each session's file scope in its prompt.
- Prefer additive tasks: new files, new endpoints, new tests rarely collide.
- Have each session commit early and often, scoped to its own paths, and stagger commits so index operations do not race.
- If two tasks genuinely need the same file, stop pretending and serialize them.

The decision rule I use has three tiers.
If two tasks share no file and no interface, they are trivially parallel, put them anywhere.
If they share an interface but not files, define the interface first, then parallelize.
If they share a file, serialize.
Most of the bad experiences people report with parallel agents are tier violations, not tool failures.

## Isolate with Git Worktrees

Sooner or later a shared-branch batch produces its first silent collision, and that is the signal to graduate to worktrees.
A git worktree gives you several working directories that share one repository.
Each worktree is a full checkout on its own branch, so two agents can edit, build, and run tests without ever seeing each other's half-finished changes.
The command line story is short:

```
git worktree add ../myrepo-auth-fix -b auth-fix
git worktree add ../myrepo-api -b api-endpoint
```

Point session one at `../myrepo-auth-fix`, session two at `../myrepo-api`, and they are fully isolated at the filesystem level.
`git worktree list` shows what is checked out where, and `git worktree remove` cleans up when a task lands.
Because all worktrees share the same object store, branches created in one are immediately visible in the others, and git only adds a little per-worktree metadata under `.git/worktrees`.

**Worktrees are the default answer because isolation is what lets you stop thinking about collisions.**
You stop rationing attention across "which files is the other agent touching" and spend it on the work instead.
Worktrees also outlive their first task: keep a pool of them and route the next task into whichever one just freed up, and you are running the final configuration, more tasks than worktrees.
The cost is environment duplication: each worktree needs its own `node_modules` or virtualenv, its own build artifacts, and its own port for a dev server.
I pay that cost by keeping environment setup scripted and boring, so a new worktree is ready in a minute, and by assigning port offsets per worktree.
If your setup takes an hour instead of a minute, fix that first, because a slow setup will kill the parallelism on its own.
The second cost arrives at integration: parallel work postpones conflicts instead of eliminating them, so keep the tasks on disjoint modules or the merge becomes the new bottleneck.

## Add an Orchestrator When Coordination Becomes the Job

With two or three sessions, you can be the coordinator.
Past that, coordination starts eating the day you were trying to save, which is [Amdahl's law](https://en.wikipedia.org/wiki/Amdahl%27s_law) applied to your own attention: the serial fraction (decomposing, assigning, integrating, deciding) eventually caps the speedup no matter how many workers you spawn.
The fix is to promote coordination into a role, the orchestrator, and let it own four jobs.
It decomposes the goal into a task graph and marks what can run in parallel.
It assigns subtasks to worker sessions, each in its own worktree.
It enforces contracts between workers, and it integrates, merging finished branches in dependency order and resolving conflicts itself.

**An orchestrator earns its place not by typing faster than the workers but by owning the contracts that make parallel work safe.**
The contract step is the one people skip, and it is the one that matters.
Before any worker starts, the orchestrator writes down the interfaces the workers will build against: the API schema, the shared types, the module boundaries, the test contract.
Workers then develop against a fixed interface instead of against each other's moving output, and integration becomes mechanical instead of investigative.
Pair this with critical-path thinking ([the critical path method](https://en.wikipedia.org/wiki/Critical_path_method) is the old, good version): start the longest task first, because parallelism cannot shorten the chain of dependent work.

You can be the orchestrator, run a dedicated session for it, or delegate it to a planning agent that fans out work and collects results, in the pattern I described in [Scaling the LLM Agent Company](../scaling-the-llm-agent-company/index.md).
I still orchestrate small batches myself, because writing the task graph is where the actual judgment lives, and judgment is the one input the cheaper workers around it cannot supply.
The failure mode to watch for is an orchestrator that decomposes badly: workers then block on each other, and you pay coordination cost for serial work.

## More Ways to Buy Speed

Worktrees and orchestration are the structural moves, but several smaller changes compound with them.

**Shorten the feedback loop first.**
An agent iterates at the speed of your test suite, so a ten-minute suite turns every edit-test cycle into ten minutes, and no amount of parallelism fixes a slow loop.
Keep a fast test subset that agents run by default, parallelize the full suite, and make lint and typecheck instant.
Speed of iteration is a multiplier on every session you run.

**Tell agents when to verify, not just how.**
An instruction file that lists the lint, typecheck, and test commands is table stakes, and one that says when to run them is worth more.
Left unsupervised, a diligent agent runs the whole suite after every small edit, and on a large project that habit converts hours of work into waiting.
The instruction that pays is something like "make all your edits first, then run the full check suite once before you commit, and use targeted tests only while debugging a specific failure".
**Verification is a batch job at commit time, not a reflex after every change.**
This is a pure instruction-file change: same commands, same rigor, a fraction of the wall clock time.

**Write the context down once.**
Every session that has to rediscover your conventions burns time you did not budget for.
A good `AGENTS.md` or equivalent, covering layout, conventions, commands, and the "never do this" list, turns that rediscovery into a file read, and better context also means fewer wrong turns per task ([The Importance of Context When Interacting with LLMs](../the-importance-of-context-when-interacting-with-llms/index.md)).

**Warm the environments.**
Prebuild dependencies so a fresh worktree is functional in seconds: cached package installs, a devcontainer, or a declarative environment.
The parallel workflow dies quietly when every new checkout costs an hour of setup.

**Route models by task.**
Use the cheap, fast model for exploration, searching, and summarizing, and the strong model for design and edits.
An explorer session answering questions alongside a writer session doing edits is cheap parallelism that pays immediately.

**Plan before you fan out.**
Run a planning pass that produces the task graph before spawning workers.
A graph written up front is what makes fan-out fast and integration boring, and it is the artifact you review when something goes wrong.

**Supervise asynchronously.**
Do not watch every session.
Let them run to a blocker, checkpoint their state, and batch your decisions at fixed intervals, the pattern from [Managing Many Concurrent LLM Agent Sessions](../managing-many-llm-agent-sessions/index.md).
Synchronous supervision caps you at one session no matter what git says is possible.

**Watch the review gate.**
Parallel agents outproduce your review capacity fast, and then review and integration become the wall ([You Are the Bottleneck](../you-are-the-bottleneck/index.md)).
Budget for it: batch your reviews, review outcomes (tests, recordings, benchmarks) before diffs, and treat rising integration time as the signal that your task boundaries are too coarse.

**Profile where the time actually goes.**
Agent sessions write detailed logs by default, so the raw material for a time audit is already on your disk.
A tool like [AgentsView](https://github.com/kenn-io/agentsview) indexes those session files from every harness into one local archive with usage, cost, and history analytics (my [research note on agentsview](../agents/agentsview/index.md) covers the details).
Read the report the way you would read a profiler output: find the phases that consume the most wall clock time, then ask what instruction, script, or boundary would shrink the biggest one.
Long working phases point at slow test loops or oversized tasks, heavy token spend on easy work points at wrong model routing, and sessions that stall waiting for you point at supervision that should be more asynchronous.
**Treat your agent workflow like a hot path in code: profile it, find the biggest cost, and cut that first.**
The workflow improves the same way code does, by measuring before optimizing.

## Advanced Strategies

The techniques above are the baseline for a parallel workflow.
The ones below are bigger investments, and they pay off once the basics are routine and the profiling data tells you where the remaining time goes.

**Race N attempts and keep the winner.**
For tasks that are small but hard, run two or three attempts in parallel worktrees and keep the one that passes tests or benchmarks best, discarding the rest.
The losers cost tokens, the winner saves a debugging session.
A cheaper variant is session forking: at a real design decision, fork the session and try both options from the same context, then keep the branch with the better result.

**Close the loop from CI back to the agent.**
When a check fails after the agent commits, route the failure straight back to the authoring session, or to a fresh session seeded with the failure context, instead of queuing it for a human.
Batch the day's failures into one repair pass so the full suite runs once for all of them.
The goal is a pipeline where a human only looks at changes that already pass everything.

**Cascade models instead of routing them statically.**
Start each task on the cheapest model that could plausibly succeed, and escalate to a stronger one only when a signal says it failed: tests red, low confidence, or a critic flag.
Static routing pays strong-model prices on every task, a cascade pays them only on the hard tail.

**Make the codebase legible to agents.**
Every convention an agent discovers by exploration is paid again by every session, so move conventions from documentation into mechanics: lint rules instead of style guides, generators instead of templates to copy, strict types instead of tribal knowledge.
Design module seams deliberately so that future parallel tasks touch disjoint files by construction.
**A codebase machines can navigate without asking is the multiplier that applies to every session you will ever run.**

**Turn frequent operations into tools.**
If every session hand-rolls the same shell commands to query the schema, run a migration, or deploy a preview, encode those operations once as CLI commands checked into the repo.
Prefer a plain CLI over agent-specific tool protocols: every harness already speaks shell, so a command written once works in every session, every worktree, and your own terminal too.

**Share one code index across sessions.**
A prebuilt index ([LSP](https://microsoft.github.io/language-server-protocol/), [ctags](https://github.com/universal-ctags/ctags), or embeddings) lets sessions query the codebase instead of crawling it, and the index is built once and reused by every parallel session.
Exploration is often the largest single phase in an agent session, and a shared index attacks it directly.

**Run a critic alongside every writer.**
A reviewer agent that reads the writer's diff as it lands catches most defects before the human gate, and you review its verdicts instead of every diff.
This is how you shrink the review wall without lowering the bar: the critic applies the checklist, the human applies judgment.

**Eval your workflow like you eval models.**
Keep a set of golden tasks for your repo, fix this bug, add this endpoint, with known-good outcomes, and score candidate models, prompts, and tools against them before adopting anything.
Adopting on vibes imports regressions silently, evals catch them before they cost you weeks.

**Move the runtime off your machine.**
Local parallelism caps out at your cores, your disk, and your patience, so run sessions in ephemeral cloud environments that can be snapshotted and restored, one warmed environment per session.
This buys isolation you cannot get locally: a session restored from a clean snapshot cannot be poisoned by another session's half-installed dependencies.

**Speculate on what comes next.**
While work runs, an idle agent prefetches for the likely-next tasks: summarizing the module a task will touch, pre-building the target, drafting the context file.
When the task starts, its context is already warm, and the startup cost drops to near zero.

## The Expiry Date on This Advice

**Everything above optimizes the machine side of the loop, and the machine side is the side getting cheaper fastest.**
While models are slow and expensive, parallelizing them safely pays, which is what most of this article is for.
Follow the trajectory, though, and the serial fraction of the loop stops being the agent and becomes you.
The agent finishes a task in minutes, turns around, and waits, not for compute but for you to decide what it should do next.
Once that is the failure mode, worktrees, orchestrators, and cascades stop buying wall clock time, because the queue the agents pull from is your capacity to specify and decide, the exact shift [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) describes.
I treat the playbook above as advice for the current regime, and the part that survives is the part the machines cannot accelerate: knowing what is worth building and saying it precisely.

## What to Do Next

This week, pick three genuinely independent tasks on your codebase and run them concurrently, on your existing branch if they share no files, or one worktree per task if they do.
Time two things: the environment setup per worktree, and the integration at the end.
If setup dominates, script it until it does not.
If integration conflicts dominate, your tasks were not independent, and the fix is in how you draw task boundaries, not in the tools.
Once three concurrent sessions feel routine, write your first explicit contract before spawning workers on shared interfaces, and add an orchestrator only when coordinating them takes more of your day than deciding what they should build.
In my experience two to four concurrent sessions is the sweet spot for one person, and the binding constraint past that is never the model.
Adopt the advanced strategies one at a time, and only when your profiling data says the basics have stopped moving your wall clock number.

## See also

- [Managing Many Concurrent LLM Agent Sessions](../managing-many-llm-agent-sessions/index.md) - the human-side supervision problem once parallel sessions exist, and the batching patterns that keep it survivable
- [Scaling the LLM Agent Company](../scaling-the-llm-agent-company/index.md) - the organizational version of the orchestrator pattern, where the orchestration layer replaces human management
- [Who Resolves the Merge Conflict?](../who-resolves-the-merge-conflict/index.md) - where the cost of parallel agent work surfaces, at integration time
- [The Importance of Context When Interacting with LLMs](../the-importance-of-context-when-interacting-with-llms/index.md) - why written context cuts iterations per task, the per-session complement to per-workflow parallelism
- [You Are the Bottleneck](../you-are-the-bottleneck/index.md) - the review capacity wall that parallel agents run into downstream
- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - why the constraint keeps moving up the decision chain, and where this advice expires once models get fast enough
- [The Agentic Development Environment Landscape](../the-agentic-development-environment-landscape/index.md) - the tooling layer that hosts and coordinates these sessions
- [Scaling Yourself Horizontally](../scaling-yourself-horizontally/index.md) - the leverage framing for why replication beats working longer

## References

- [git-worktree Documentation](https://git-scm.com/docs/git-worktree) - the git mechanism behind isolated parallel checkouts
- [Claude Code: Common workflows](https://code.claude.com/docs/en/common-workflows) - documents the parallel-sessions-with-worktrees practice as a mainstream workflow
- [Trunk Based Development](https://trunkbaseddevelopment.com/) - the integration discipline that shared-branch and frequent-merge workflows sit on
- [Amdahl's law](https://en.wikipedia.org/wiki/Amdahl%27s_law) - why the serial fraction (decomposition, integration, decisions) caps the speedup from adding agents
- [Critical path method](https://en.wikipedia.org/wiki/Critical_path_method) - why the longest dependency chain, not the task count, sets the minimum wall clock time
