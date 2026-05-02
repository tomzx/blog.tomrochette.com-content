---
title: task-stack - A persistent task stack that lives in your system tray
created: 2026-05-02
type: post
status: finished
tags: [python, productivity, developer-tools, desktop-app, fully-ai-generated, llm=glm-5.1]
readability: 4
---

I've been using the [workstack](/workstack) concept for years to track what I'm working on and where I got interrupted.
task-stack is the natural evolution: a small system tray app that keeps a persistent, reorderable stack of tasks always one hotkey away.

The top of the stack is your current task.
Everything below it is queued.
Press **Ctrl+Shift+T** from anywhere and a compact window appears where you can add, reorder, promote, and remove tasks.
Close the window and it's out of your way.
The tray icon always shows the current task as its tooltip.

[Repository and source code](https://github.com/TomzxCode/task-stack)

## Why a stack, not a list

Todo lists are flat.
Kanban boards are heavy.
When you're deep in flow and get interrupted, you don't want to prioritize a backlog — you want to push something on top of what you're doing and pop it off when you're done.

A stack models this naturally:
- **Push**: a new urgent task goes on top, becomes the current task.
- **Pop**: mark done, the next task surfaces automatically.
- **Reorder**: something can wait? move it down. Something urgent? promote it to the top.

No projects, no tags, no due dates.
Just a stack of things to do, in order.

## Features

- **System tray icon** with the current task as tooltip and a "Mark Done (pop)" action.
- **Global hotkey** (default: Ctrl+Shift+T, configurable) to bring the stack window forward from any application.
- **Keyboard-driven editing**: add tasks with Enter, reorder with arrow keys, promote with `/`, remove with Backspace.
Full shortcut table in the README.
- **Persistent state** in `~/.task-stack.yaml`.
Easy to inspect, back up, or version control.
- **Soft deletes**: removed tasks stay in the YAML file with a `deleted_at` timestamp, so you keep a full history.
- **Timestamps**: each task tracks `created_at`, `started_at` (first time it became current), and `last_current`.
- **Cross-platform**: works on macOS, Linux, and Windows.

## Quick start

```bash
git clone https://github.com/TomzxCode/task-stack.git
cd task-stack/python
uv sync
uv run task-stack
```

The app starts in the system tray.
Press the hotkey or pick "Open Stack" from the tray menu.

## Data format

Tasks are stored in `~/.task-stack.yaml` as a simple YAML list:

```yaml
- text: Write blog post about task-stack
  created_at: '2026-05-02T10:00:00+00:00'
  started_at: '2026-05-02T10:00:00+00:00'
  last_current: '2026-05-02T10:30:00+00:00'
- text: Review pull requests
  created_at: '2026-05-02T09:00:00+00:00'
  deleted_at: '2026-05-02T09:45:00+00:00'
```

Active tasks come first in stack order.
Soft-deleted tasks are appended at the end with a `deleted_at` timestamp.
Settings (window geometry, hotkey) live in `~/.task-stack.settings.yaml`.

## Configure the hotkey

Edit `~/.task-stack.settings.yaml`:

```yaml
hotkey: ctrl+shift+t
# hotkey: alt+space
# hotkey: cmd+shift+space
```

Restart the app to apply.
The current hotkey is shown in the tray menu.

## When this is useful

- **Developers context-switching** between code reviews, bug fixes, and feature work.
Push the interruption on the stack, pop it when done, resume what you were doing.
- **Anyone who works with interruptions** and wants a lightweight way to track what's pending without opening a full project management tool.
- **Time tracking enthusiasts** who want `started_at` / `last_current` timestamps to reconstruct what they worked on during the day.

## Related

- [Workstack](/workstack) — the original note-taking concept that inspired task-stack.
