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

> **User:** We want to produce a new classification model and the associated infrastructure to serve real-time predictions. What should our next steps be?

> **ChatGPT:** There are several steps you can take to produce a new classification model and associated infrastructure for serving real-time predictions:
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

> **User:** I want to be able to classify whether a person prefers one brand over another.
> I might know about the age of that person, the country where they live, how much time they use a given app per day, how many friends they have on this app.
> As output, I want to classify whether they would prefer brand A or brand B.

> **ChatGPT:** Great! Here's an overview of the steps you could take to create a classification model to predict whether a person prefers brand A or brand B based on their age, country, app usage, and number of friends:
>
> Data collection: Collect data from a representative sample of people that includes their age, country, app usage, number of friends, and which brand they prefer (A or B).
>
> Data preprocessing: Clean and preprocess the data by removing any duplicates, filling in missing values, and converting categorical variables (like country) into numerical features.
>
> Feature engineering: Create additional features from the data that might help improve the model's performance. For example, you could create features like "average app usage per friend" or "age group" based on ranges of ages.
>
> Split the data: Split the data into training and testing sets. This is important so that you can evaluate the model's performance on data that it hasn't seen before.
>
> Choose a classification algorithm: Choose an appropriate algorithm for your data. Some popular choices include logistic regression, decision trees, and random forests.
>
> Train the model: Train the classification model on the training data. Use the testing data to evaluate the model's performance and adjust the model's hyperparameters to improve its accuracy.
>
> Deploy the model: Once the model is trained and performs well on the testing data, deploy it and set up an API to receive input data and provide predictions in real-time.
>
> Monitor and update the model: Continuously monitor the model's performance and update it as needed. As new data becomes available, retrain the model to improve its accuracy over time.
>
> Remember to keep in mind the ethical considerations of using personal data for classification purposes, and ensure that you comply with all relevant data protection laws and regulations.


> **User:** Help me Collect data from a representative sample of people that includes their age, country, app usage, number of friends, and which brand they prefer (A or B).

> **ChatGPT:** Collecting data from a representative sample of people can be done in several ways, depending on the resources and time available. Here are some possible methods:
>
> Online surveys: Conduct an online survey using a platform like Google Forms or SurveyMonkey. You can create a questionnaire that includes questions about age, country, app usage, number of friends, and which brand they prefer (A or B). You can then distribute the survey to a representative sample of people using social media or email lists.
>
> In-person interviews: Conduct in-person interviews with people in public places such as malls or parks. Ask them questions about their age, country, app usage, number of friends, and which brand they prefer (A or B).
>
> Online panels: Join an online panel service such as Toluna or YouGov. These services have a pool of people who have agreed to participate in surveys or other research studies. You can create a questionnaire that includes questions about age, country, app usage, number of friends, and which brand they prefer (A or B) and distribute it to a representative sample of people.
>
> Social media groups: Join relevant social media groups or communities and ask members to participate in a survey or provide data about their preferences. You can create a questionnaire that includes questions about age, country, app usage, number of friends, and which brand they prefer (A or B) and post it in the group or community.
>
> When collecting data, it's important to ensure that the sample is representative of the population you are interested in. This can be achieved by using random sampling or stratified sampling techniques. Additionally, it's important to ensure that participants provide informed consent and that their privacy is protected.


> **User:**  Conduct an online survey using a platform like Google Forms or SurveyMonkey. You can create a questionnaire that includes questions about age, country, app usage, number of friends, and which brand they prefer (A or B). You can then distribute the survey to a representative sample of people using social media or email lists.

> **ChatGPT:** Here's an example of how you can create an online survey using Google Forms:
>
> Go to Google Forms and log in to your Google account.
> Click on the "Blank" template to create a new survey.
> Add a title to your survey and include a brief introduction that explains the purpose of the survey and how the data will be used.
> Add questions about age, country, app usage, number of friends, and brand preference (A or B). You can use a variety of question types, such as multiple choice, dropdown, or text input fields.
> Customize the appearance of your survey by choosing a theme or adding images.
> Preview your survey to ensure that it looks the way you want it to.
> Set up distribution options, such as a link to the survey or embedding it on a website. You can also send the survey via email or social media.
> Test your survey to ensure that it is working properly.
> Monitor responses as they come in and analyze the data once you have a sufficient sample size.
> When distributing your survey, it's important to ensure that you reach a representative sample of people. You can use social media, email lists, or targeted advertising to reach your desired audience. It's also important to provide participants with informed consent and ensure that their privacy is protected.


> **User:** Go to Google Forms and log in to your Google account.

> **ChatGPT:** I'm sorry, as an AI language model, I don't have the ability to log in to your Google account. However, you can follow these steps to log in to your Google account and access Google Forms:

> Go to the Google homepage (www.google.com) on your web browser.
> Click on the "Sign in" button located on the top right corner of the page.
> Enter your Google account email address and password in the provided fields.
> Click on the "Next" button to proceed.
> If prompted, enter the verification code sent to your registered phone number or email address to verify your identity.
> Once you have successfully signed in, click on the "Apps" icon (represented by 9 small squares) located on the top right corner of the page.
> Click on the "Forms" icon to access Google Forms.
> You can now create a new form or edit an existing one.

# Notes

# See also

# References
