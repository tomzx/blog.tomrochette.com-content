---
title: CC Safety Net
created: 2026-10-07
updated: 2026-11-14
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, control-planes, policy-enforcement, guardrails, security, open-source]
readability: 3
audience_notes: >
  Engineers who run AI coding agents on their own machine and want destructive commands and secret reads blocked before they execute.
  Assumes you know what a PreToolUse hook is and the difference between a policy gate and a sandbox.
---

CC Safety Net (Coding CLI Safety Net) is an MIT pre-execution guard that parses each command or file access an AI coding agent is about to make and blocks destructive git and filesystem operations plus secret-file reads before the tool call runs.

**Its design point is parse-then-decide: it reads what a command would actually do, so wrapping it or reordering flags does not sneak past, and it fails open on its own breakage (a broken config never blocks anything), the opposite trade from the sandboxes it explicitly says it is not.**

## What it is

A TypeScript CLI installed with `npx cc-safety-net install` into the hook surface of sixteen coding-agent CLIs, including Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot CLI, OpenCode, OpenClaw, Hermes Agent, Kimi Code, Pi, DeepSeek Harness, Amp Code, Antigravity CLI, Devin CLI, Factory Droid, and Grok Build, on Windows, macOS, and Linux.
Blocked by default are destructive commands (`git reset --hard`, `git push --force`, `rm -rf` on dangerous targets, including inside `bash -c` or `python -c`) and secret access (SSH keys, `.env` files, `~/.aws`, coding-CLI credentials) from both the shell and the agent's file tools.
Policy is tuned through a GUI (`npx cc-safety-net gui`) across Standard, Strict, and Paranoid presets, extended through official rulebooks (Terraform, AWS, gcloud, Azure) or your own JSON, and shared by committing the `.cc-safety-net/` directory so clones and cloud sessions inherit the same rules; a `checkCommand` library API embeds the engine in other tools.
It states plainly that it is not a sandbox: it contains no processes, sets no filesystem permissions, and watches no network egress.
MIT, single-repo open source, with full documentation at ccsafetynet.com.

## Status

Actively maintained with no Hacker News help: 1,615 stars, 84 forks, and 11 open issues and pull requests as of 2026-11-14, created 2025-12-25, pushed 2026-11-14 with the default branch's latest commit on 2026-11-12.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=kenryu42/cc-safety-net&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=kenryu42/cc-safety-net&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=kenryu42/cc-safety-net&type=date&legend=top-left" />
</picture>

The npm package (`cc-safety-net`) is at 2.7.12 as of 2026-11-13, first published 2026-01-03 and last published 2026-11-12, so the release cadence is measured in days.
**A Hacker News search returns zero threads as of 2026-10-07, so ten months of growth came through npm and GitHub alone, and the missing community footprint means the security claims have no public adversarial review I could find.**

## Strengths

- Command parsing rather than pattern matching: reordering flags or hiding the payload in `bash -c` or `python -c` does not evade the check.
- Sixteen harness surfaces behind one install command, with policy distributable through the repo itself, which fits how teams already sync tool config.
- The GUI preset ladder (Standard, Strict, Paranoid) and rulebook packs make the policy approachable without reading YAML.
- The fail-open stance is stated up front, which is more candor than most guards offer about their own failure mode.

## Cautions

- It decides before execution and contains nothing after, so it complements rather than replaces an isolation boundary, and the README says so itself.
- Fail-open cuts both ways: a crashed or bypassed guard stops protecting silently, which is the wrong default for a threat model where the agent is adversarial rather than merely error-prone.
- Zero Hacker News footprint and no independent audit; the claims about parsing resistance are the project's own.
- The npm path has its own wrinkle the README warns about: a bare `cc-safety-net` spec can resolve a stale copy from the npx cache, so the `@latest` qualifier matters.

## Pricing

Free and open source under MIT, no paid tiers or hosted offering found as of 2026-10-07.

## Compared to

- [Veto](../veto/index.md): the same enforcement point (before the tool handler runs) with a different scope and audit depth, since Veto adds an allow/warn/require-approval ladder, approval routing, and offline-verifiable receipts for money-and-data actions, while CC Safety Net guards a workstation's git and secrets with none of that machinery.
- [OpenAPPA](../openappa/index.md): information-flow policy over what an agent reads, in-process or as a sidecar; CC Safety Net is a command-surface hook with secret-path denial, not a labeling engine.
- [Microsoft Agent Governance Toolkit](../microsoft-agent-governance-toolkit/index.md): the heavier multi-language program with policy engines, identity, and compliance; choose it for org-scale governance, CC Safety Net for a same-hour personal guardrail.

## Bottom line

**Recommended for developers who want destructive-command and secret-access guardrails across many agent CLIs on their own machine, installed in one command, accepting that the guard is a hook and not a boundary.**
Not for org-scale governance, audited enforcement, or anything where a silently crashed guard is unacceptable.

## Changes

- 2026-10-07 - Created from the daily-refresh entrant resolution, profiling the parse-then-decide pre-execution guard and its zero-HN footprint.
- 2026-10-10 - Recorded the npm train at 2.6.7 (published 2026-10-10) and the open-issue count falling from 9 to 1; scale refreshed (1,582 stars, pushed 2026-10-10).
- 2026-10-11 - npm train moved to 2.6.8 (published 2026-10-11); scale refreshed (1,583 stars, pushed 2026-10-11).
- 2026-10-13 - npm train moved to 2.6.10 (published 2026-10-12); scale refreshed (1,606 stars, pushed 2026-10-13).
- 2026-10-16 - npm train moved to 2.6.12 (published 2026-10-15).
- 2026-10-17 - npm train moved to 2.6.13 (published 2026-10-17).
- 2026-10-18 - npm train moved to 2.6.14 (published 2026-10-18).
- 2026-10-19 - npm train moved to 2.6.15 (published 2026-10-19).
- 2026-10-23 - npm train moved to 2.6.18 (published 2026-10-23), after 2.6.16 (2026-10-19) and 2.6.17 (2026-10-22).
- 2026-10-25 - npm train moved to 2.6.19 (published 2026-10-24), closing a gap that let recursive deletes of the root or home directory written as Python, Perl, Node, or Ruby interpreter code through unchecked.
- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-26 - Corrected the star-history chart light-source markup (the light source carried the dark-theme parameter; it now points at the default chart, matching the fallback fix of 2026-10-25).
- 2026-10-28 - npm train moved to 2.7.0 (published 2026-10-27, release v2.7.0): cloud-metadata credential reads, remote data uploads, and `unshare` user-namespace root escalations now blocked, commands that run a shell script from disk get the script analyzed, and the minimum Node.js version rose to 22, a breaking change for Node 18 and 20.
- 2026-11-01 - npm train moved to 2.7.1 (published 2026-10-30, release v2.7.1): remotely fetched programs handed to an interpreter or PowerShell (`curl | python3`, `irm | iex`, `curl -o` then `bash`) now stop as unverifiable shell execution sources, and a host tool's working-directory argument can no longer move the boundary the recursive-delete rules protect.
- 2026-11-05 - npm train moved to 2.7.2 (published 2026-11-02) then 2.7.3 (published 2026-11-04): 2.7.2 extends secret protection behind `env`, `sudo`, and `command` wrapper options and fixes an `allow_paths` entry ignored for a sensitive file named in an environment assignment, and 2.7.3 moves remote `curl`/`wget` uploads from the default Standard level to Strict and Paranoid only while recursive deletes with a variable or wildcard target from the home directory now block at Standard.
- 2026-11-07 - npm train moved to 2.7.4 (published 2026-11-06): PowerShell here-strings with CR line breaks and expansions now parse instead of passing through, and the counters refreshed (pushed 2026-11-06).
- 2026-11-08 - npm train moved to 2.7.5 (published 2026-11-08, release v2.7.5): shell tools that run their commands on another machine (an adb-shell or ssh-backed plugin tool) can be declared with `--no-cwd-arg` or `cwd: false`, so their commands are analyzed instead of passing unchecked.
- 2026-11-11 - npm train moved through 2.7.6 (2026-11-08, user and project policy files readable and writable again on Windows across affected Node.js versions), 2.7.7 and 2.7.8 (2026-11-09, standard mode stopped treating an `ssh`, `scp`, or `sftp -i` identity file as a secret read), and 2.7.9 (2026-11-10, Windows backslash paths and colon-attached PowerShell parameters such as `Get-Content -Path:C:\\proj\\.env` now parse, closing unblocked secret reads), to 2.7.10 (2026-11-11, a `.startswith(".env")` literal counts as data instead of secret access, a false-positive fix); the counters refreshed (3 open issues, pushed 2026-11-11).
- 2026-11-13 - npm train moved to 2.7.11 (2026-11-11, a quoted heredoc passed to a data sink is no longer scanned as shell text when a wrapper or environment assignment precedes the sink, with `CC_SAFETY_NET_PROJECT_TIGHTEN_ONLY` now honoring only wrappers declared in the user's own policy) and 2.7.12 (2026-11-12, PowerShell recursive `Remove-Item` deletes outside the working directory are now judged on `-Recurse` alone instead of requiring `-Force` alongside it); the counters refreshed (5 open issues, pushed 2026-11-12).

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category comparison this note joins
- [Veto](../veto/index.md) - the same enforcement point with approval workflow and receipts
- [OpenAPPA](../openappa/index.md) - the information-flow alternative over what agents read
- [Sandboxing Feature Matrix](../../sandboxing/sandboxing-feature-matrix/index.md) - the boundaries this guard explicitly is not

## References

- https://github.com/kenryu42/cc-safety-net - repository: mechanism, supported CLIs, features, license
- https://raw.githubusercontent.com/kenryu42/cc-safety-net/main/README.md - the README whose mechanism and feature claims this note traces to
- https://ccsafetynet.com/docs - the documentation site (a client-rendered shell to fetchers, so linked rather than quoted)
- https://api.github.com/repos/kenryu42/cc-safety-net - stars, issues, creation and push dates as of 2026-10-11
- https://registry.npmjs.org/cc-safety-net - the 2.6.8 latest tag, first-publish and last-publish dates as of 2026-10-11
- https://hn.algolia.com/api/v1/search?query=%22cc-safety-net%22&tags=story - the zero-thread footprint check as of 2026-10-07
