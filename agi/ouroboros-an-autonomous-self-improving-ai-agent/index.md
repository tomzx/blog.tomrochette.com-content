---
title: "Ouroboros: An Autonomous Self-Improving AI Agent"
created: 2026-01-02
status: finished
type: post
tags: [artificial-general-intelligence, ouroboros, open-source, fully-ai-generated, llm=glm-4.7, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader knows what an LLM-based agent is and how git works; no background in self-improving agents is required.
---

## What is Ouroboros?

**[Ouroboros](https://github.com/TomzxCode/ouroboros) is an autonomous AI agent that works on the tasks you give it and continuously improves itself.**
It is named after the ancient symbol of a serpent eating its own tail (representing infinity and cyclic renewal), and it implements a continuous loop of Do → Learn → Improve → Retry.

Unlike traditional AI assistants that wait for commands and forget context between sessions, Ouroboros:

- Runs indefinitely without human intervention
- Maintains persistent memory of everything it has done
- Reflects on its performance regularly
- Modifies its own code to improve over time
- Can incorporate human feedback when provided

Previously I wrote about [GlobaLLM](../globallm-automated-open-source-contribution-at-scale/index.md), an AI agent that autonomously contributes to open source projects.
While GlobaLLM's primary objective is project and task prioritization at scale, Ouroboros focuses on task implementation and self-improvement.
**Ouroboros is thus one component of GlobaLLM's solution.**

## How It Works

### The Core Loop

Ouroboros follows a structured nine-step cycle that repeats continuously:

1. **Read goals**: fetches tasks from `agent/goals/active.md`
2. **Select goal**: picks one to work on, or defaults to self-improvement
3. **Plan**: uses an LLM to create a step-by-step plan
4. **Execute**: carries out the plan using available tools
5. **Journal**: writes results to a daily log
6. **Reflect**: analyzes what happened and identifies improvements, both task-related and self-related
7. **Self-modify**: edits its own source code if improvements are found
8. **Journal again**: records reflection and modification results
9. **Repeat**: starts the cycle anew

**The separation between execution and self-modification is crucial.**
The agent will not modify its code while working on a task; reflections and improvements happen only during dedicated reflection cycles.

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│                      Agent Core                         │
│  (coordinates the loop, handles signals, manages state) │
└─────────────────────────────────────────────────────────┘
         │                    │                    │
         ▼                    ▼                    ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Memory     │    │  LLM Layer   │    │   Tools      │
│              │    │              │    │              │
│ • Working    │    │ • Anthropic  │    │ • run_cmd    │
│ • Journal    │───▶│   Claude     │───▶│ • read_file  │
│ • Goals      │    │ • Token      │    │ • write_file │
│ • Feedback   │    │   tracking   │    │ • search_*   │
└──────────────┘    └──────────────┘    └──────────────┘
```

### Memory System

Ouroboros uses a three-tiered memory architecture:

| Tier | Description | Location |
|------|-------------|----------|
| **Working memory** | Current goals, immediate context | In-process |
| **Short-term** | Daily journals (notes, reflections, feedback) | `agent/journal/YYYY/MM/DD/` |
| **Long-term** | Git history with descriptive commits | Git repository |

Everything is logged in human-readable markdown, which makes it easy to inspect what the agent has been up to.

### Tool Registry

The agent comes with built-in tools for common operations:

- `run_command`: execute shell commands
- `read_file`: read file contents
- `write_file`: write to files
- `search_files`: find files by pattern
- `search_content`: search within files

**Crucially, Ouroboros can create, register, and use new tools that it writes itself.**

Tools are implemented as CLI commands of the `ouroboros` CLI, which the agent can invoke during execution.

## Design Principles

### Safety Through Structure

**The execution/reflection separation prevents runaway self-modification.**
The agent can change code only during a dedicated reflection phase, and all changes are committed to git with descriptive messages that explain the reasoning behind each change.

### Transparency

**Every action is logged.**
Want to know what the agent did?
Check the daily journal:

- `agent/journal/YYYY/MM/DD/notes.md`: what it did
- `agent/journal/YYYY/MM/DD/reflections.md`: what it learned
- `agent/journal/YYYY/MM/DD/user-feedback.md`: human input received

### Autonomy with Optional Guidance

Ouroboros needs no human intervention, but it welcomes it.
It incorporates feedback, adjusts course based on user suggestions, and explains its reasoning when asked.

## What Makes It Interesting

1. **True self-improvement**: the agent can and does modify its own implementation based on reflection
2. **Persistent memory**: git commits serve as a permanent, queryable history of everything tried
3. **Graceful degradation**: failed modifications can be reverted; the agent learns and tries again
4. **Tool extensibility**: new tools can be created dynamically as needs arise
5. **Idle improvement**: when no goals are active, it works on making itself better

## The Vision

Ouroboros represents an experiment in autonomous AI agents.
**Can an agent truly improve itself over time without human intervention, or with only limited intervention?**
By maintaining a detailed journal, reflecting on its actions, and having the freedom to modify its own code, Ouroboros aims to answer this question.

The name is fitting: the serpent eating its tail represents the continuous cycle of doing, learning, and improving that drives the agent forward.
Each reflection builds on the last; each modification makes the agent slightly more capable.

[Ouroboros](https://github.com/TomzxCode/ouroboros) is open source.
Check out the repository to see the code, contribute, or run your own self-improving agent.
