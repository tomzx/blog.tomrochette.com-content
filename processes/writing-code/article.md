---
title: Writing code
created: 2019-05-25
taxonomy:
  type: post
  tag: [software-development, processes]
  status: draft
  readability: 5
---

# LLM-assisted flow
* Use the task background + acceptance criteria as plan prompt (manual)
* Use the planning feature of the agent and let it generate a plan (LLM)
* Review the plan and adjust as necessary (manual)
  * Ensure the presence of tests
* Let the agent implement the code based on the plan (LLM)
* Review the code implemented by the agent (manual)
  * Ensure it meets the acceptance criteria
  * Ensure code quality and standards
* Manually verify that functionality is working as expected (manual)
* Commit code on a branch (manual)
* Push to the central repository (manual)
* Verify that CI passes
* Create pull request (manual + LLM generated description)

# Pre-LLMs flow
* Make sure you understand what you have to implement
* Make it work
* Write a test for what you implemented
* Refactor the code for reusability/code standard
* Verify that your code passes linting and tests
* Commit your code on a branch
* Push to the central repository
* Verify that CI passes
* Create pull request
* Annotate code to explain intent of changes
