---
title: Great or acceptable software solution
created: 2020-02-06
taxonomy:
  type: post
  tag: [questions, software development]
  status: finished
---

# Question
Is it better to spend a lot of time designing a great software solution or to implement an acceptable one?

# Answer
In software development, the further you go down the development pipeline, the more expensive it is to change things. Once a solution is established and is being used by other parts of the code, replacing it becomes more expensive. Thus it would make sense to spend as much time as possible planning what you're going to develop before you develop it. Sometimes you however do not have enough information to make an informed design decision upfront and you actually need to implement something to explore and understand what will be needed to solve the problem. The exploratory implementation you do may end up being satisfactory enough that you do not see the need to redesign your solution.

When you implement a solution you generally have an idea of the use cases you need to support, but sometimes certain use cases are less common and require a lot more effort to support. As such, you have the choice between implementing a solution that would support both common and uncommon use cases but would require more time, or you could implement a solution that covers the common cases. Depending on the field you are in, you will have to choose between this tradeoff.

In the domains I've worked (game development, web development, machine learning), it has been more valuable to implement an acceptable solution that could be shown as providing value to the client vs designing a great solution until it was proven to be necessary.

Always make wise use of your time and assess whether quality or quantity is needed for your software project.
