---
title: ChatGPT limitations
created: 2023-04-22
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview
* It does not execute actions, but it can generate text explaining what actions to take. While this is a current limitation that is addressed by plugins, the next logical step is to have ChatGPT execute actions. As an example of a machine learning engineer working on a project, while ChatGPT can help with devising a plan, it cannot execute the plan. If I already have infrastructure and I want help testing different models and hyperparameters, I still need to write the necessary prompts for ChatGPT, verify the code implements my desired intent, copy the generated code, execute it, and then analyze the results. Furthermore, any execution of machine learning code can take from minutes to hours to execute. In other words, while it helps me reduce the amount of time spent on certain tasks such as reflecting, generating a plan, writing code, because it does not execute those, I am still left with doing them myself.


Let us walk through a scenario and use ChatGPT.

> User: We want to produce a new classification model and the associated infrastructure to serve real-time predictions. What should our next steps be?

> ChatGPT: There are several steps you can take to produce a new classification model and associated infrastructure for serving real-time predictions:
>
> Define the problem: Define the problem you want to solve with your classification model. What are the inputs to your model, and what are the outputs you want to predict? For example, you may want to classify images into different categories, or classify text into different sentiment categories.
>
> Collect and preprocess data: Collect data that is representative of the problem you want to solve. Preprocess the data by cleaning and transforming it so that it is in a format that can be used for training the model.
>
> Select a machine learning algorithm: Select a machine learning algorithm that is appropriate for your problem. For example, you may want to use a decision tree, random forest, or support vector machine.
>
> Train the model: Train the model using the preprocessed data and the selected machine learning algorithm. Split the data into training and testing sets, and use cross-validation to evaluate the model's performance.
>
> Tune hyperparameters: Tune the hyperparameters of the machine learning algorithm to improve the performance of the model. Hyperparameters are parameters that are set before training the model, such as the learning rate or the number of hidden layers in a neural network.
>
> Evaluate the model: Evaluate the model's performance on a holdout dataset. Use metrics such as accuracy, precision, recall, and F1-score to evaluate the model's performance.
>
> Deploy the model: Deploy the model and associated infrastructure to serve real-time predictions. This may involve setting up a server, creating an API, and integrating the model into your application.
>
> Monitor and update the model: Monitor the model's performance in real-time, and update the model as needed to improve its performance. This may involve retraining the model with new data or tweaking the hyperparameters.

# Notes

# See also

# References
