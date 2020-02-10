---
title: When to abandon pull requests
created: 2020-02-09
taxonomy:
  type: post
  category: [Questions, Software development]
  status: finished
---

# Question
When is it appropriate to abandon a pull request?

# Answer
Assuming that this is in a business context, you should abandon working on a pull request if getting the pull request merged is taking away too much time from others and it requires a lot of additional changes, creating a lot of back and forth between the creator and the reviewers.

You should abandon it if the feature/bug it fixes is not important enough compared to other more important ones. One should always work on the most important task rather than to work on tasks of lower importance. Furthermore, working on low importance pull requests will also "force" your coworkers to review those low importance pull request, reducing the overall productivity. As such, always think of the impact you will have on others.

Many developers often think that bugs are of the utmost importance and should be fixed as soon as possible. However, implementing a good fix might require a lot of effort on the part of the person that will fix the issue, as well as a good amount of effort on the part of the reviewers which could have spent their time on features or bugs that are more important. Like anything else, bugs should be prioritized based on how important they are, not just that they are a bug.
