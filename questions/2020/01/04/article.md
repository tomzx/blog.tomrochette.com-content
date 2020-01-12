---
title: How to prioritize numerous tasks
created: 2020-01-04
routes:
  aliases:
    - /questions/2020-01-04
taxonomy:
  type: post
  category: [Questions, Task management]
  status: finished
---

# Question
How do you prioritize things when there are so many of them competing against one another?

# Answer
My approach to task prioritization, assuming that you have a list of tasks with no other information, involves adding information that will help you prioritize them.

## Important/Urgent
Assuming you are using a issue tracking system like Redmine, Notion.so or JIRA, I would add two new properties to each task: important and urgent. This approach is based on the [Eisenhower method](https://en.wikipedia.org/wiki/Time_management#The_Eisenhower_Method) of time management. You will want to go through all the tasks and determine whether they are important and whether they are urgent.

With this first pass of information added to your tasks, you should be able to prioritize them in the following order:
1. Important/Urgent
2. Important/Not urgent
3. Not important/Urgent
4. Not important/Not urgent

You should avoid as much as possible spending your time on tasks that are not important.

This is the first step to prioritizing your task. It is a lightweight approach to prioritization which will also allow you to consider whether a task has any importance, something that is sometimes not considered and leads people to work on low priority tasks.

## Return on investment (ROI)
At this point, we now assume that you have a lot of tasks that are not urgent but important. So many in fact that it is hard to decide which ones to do. It may feel like you're back to square one, but now the important/urgent properties are not a way to order your tasks anymore. This is where the return on investment (ROI) metric is useful.

Similar to the important/urgent properties, we will add two new properties: estimated value (in dollars) and estimated effort (in hours). A third field, the ROI, is automatically derived from the previous two by computing estimated value divided by estimated effort.

For each task you will want to estimate to the best of your knowledge how much effort would be required to complete the task, as well as how much value you expect it to bring. Once you have those numbers for all your tasks, you should be able to order them by descending ROI. This will provide you with the list of tasks you should work on in order, as they are the one likely to provide you with the highest amount of ROI.

If at this point you still have many tasks which have the same ROI, you can first try to tackle the ones with the least amount of effort to get them out of the way and have quick wins. If you're still left with many tasks at this point, my current approach does not deal with this situation. It becomes a question of defining a higher level roadmap, determining which collection of feature may have more impact than others. It may also be possible to look into additional properties of the task, such as how long since they've been created and left incomplete.

# References
* [Task management](../../../../../processes/task-management)
