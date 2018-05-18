---
title: Workstack
created: 2018-05-18
taxonomy:
  type: post
  category: [note taking]
  status: draft
---

The workstack is a very simple idea I had while working. It is based on the concept of a [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) as the name clearly implies. As you work, you, like a computer, process things one at a time and as new things need to be done, you either throw them in a todo list (a queue), or you start doing them right away (you stack them).

The workstack is a way to record notes about what you work on. As you work on something, you can either work on them to completion, or be interrupted by the necessity of working on another task. In the first case, tasks are simply written one after the other with their begin and end time. In the second case, items are also indented, such that it is possible to observe when a task forced you to "switch context".

An example of this note taking format is as follow.

<pre><code class="language-text line-numbers">
Task 1 10:00-10:30
Task 2 10:35-10:50
Task 3 11:00-...
	Task 4 11:05-11:15
	Task 5 11:17-...
		Task 6 11:20
Task 7
</code></pre>

Conceptually, you would want to always complete a stack of operations before moving to a new task. However, it is highly common in programming that one will start going down such stack while working on code and then will not end up climbing back the stack.
