---
title: Rough project size estimation
created: 2020-03-02
taxonomy:
  type: post
  tag: [Questions, Software development]
  status: finished
---

# Question
How do you estimate the size of a project roughly?

# Answer
When I am asked to provide a rough estimate of the required effort on a project with a lot of requirements or user stories, I first want to make sure that my estimate is in the right order of magnitude. That means that I want to estimate a project that takes 1-10 weeks to be in that range, but not estimate less than a week or more than 10 weeks. Similarly, a project that takes one or more years should not estimated as a job of a few weeks.

My orders of magnitude are as follows:
* 1 day
* 1 week (5 days)
* 1 month (20 days)
* 1 quarter (60 days)
* 1 half-year (120/125 days)
* 1 year (250 days)

As such, when estimating a task, I will say that the task will either take 1 day, 1 week or 1 month. In general, any task that is estimated at 1 month long (or above) needs to be broken down into sub-tasks as it indicates that the task is hiding a lot of complexity.

With this kind of approach, one can estimate that a developer can do approximately 250 small tasks (1 day), 50 medium tasks (5 days) or 13 large tasks (20 days) per year.

Start by creating an estimate of the overall project without thinking about any of the underlying tasks. This is done to have a quick idea of the scale of the project.

Then list and estimate the tasks that will need to be accomplished to complete the project. You might be forgetting a few, but it is fine at that moment. Think mostly of the most important tasks and also the riskiest.

If the sum of the efforts you estimated is in the same order of your original project estimate, then you are done. If not, then you need to investigate and explain what led you to either over or under estimate. Did you forget to estimate some tasks? Did you ignore some tasks when you did your initial estimate? What were the assumptions you made that were right/wrong? Once you are satisfied with your explanation, you are done with estimating.
