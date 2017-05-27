---
title: J.R. Quinlan - Induction of Decision Trees (1986)
created: 2017-04-13
taxonomy:
  category: [Machine Learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
## 2. The TDIDT family of learning systems
* Three principal dimensions along which machine learning systems can be classified
	* The underlying strategies used
	* The representation of knowledge acquired by the system
	* The application domain of the system
* The applications addressed in this paper involve classification
* The underlying strategy is non-incremental learning from examples
* The systems are presented with a set of cases relevant to a classification task and develop a decision tree from the top down, guided by frequency information in the examples but not by the particular order in which the examples are given
* Concept Learning System (CLS) constructs a decision tree that attempts to minimize the cost of classifying an object
* This cost has components of two types:
	* The measurement cost of determining the value of property A exhibited by the object
	* The misclassification cost of deciding that the object belongs to class J when its real class is K
* CLS uses a lookahead strategy similar to minimax

## 3. The induction task
* The basis is a universe of objects that are described in terms of a collection of attributes
* Each attribute measures some important feature of an object and will be limited to taking a (usually small) set of discrete, mutually exclusive values
* The induction task is to develop a classification rule that can determine the class of any object from its values of the attributes
* If the training set contains two objects that have identical values for each attribute and yet belong to different classes, it is clearly impossible to differentiate between these objects with reference only to the given attributes
	* In such a case attributes will be termed inadequate for the training set and hence for the induction task
* The essence of induction is to move beyond the training set, i.e. to construct a decision tree that correctly classifies not only objects from the training set but other (unseen) objects as well
* In order to do this, the decision tree must capture some meaningful relationship between an object's class and its values of the attributes
* Given a choice between two decision trees, each of which is correct over the training set, it seems sensible to prefer the simpler one on the grounds that it is more likely to capture structure inherent in the problem

## 4. ID3
* One approach to the induction task would be to generate all possible decision trees that correctly classify the training set and to select the simplest of them
* ID3 has generally been found to construct simple decision trees, but the approach it uses cannot guarantee that better trees have not been overlooked
* The basic structure of ID3 is iterative
* A subset of the training set called the window is chosen at random and a decision tree formed from it; this tree correctly classifies all objects in the window
* All objects in the training set are then classified using the tree
* If the tree gives the correct answer for all these objects then it is correct for the entire training set and the process terminates
* If not, a selection of the incorrectly classified objects is added to the window and the process continues

## 5. Noise
* Errors in the training set may cause the attributes to become inadequate
* Errors in the training set may lead to decision trees of spurious complexity
* Two modifications are required if the tree-building algorithm is to be able to operate with a noise-affected training set
	* The algorithm must be able to work with inadequate attributes, because noise can cause even the most comprehensive set of attributes to appear inadequate
	* The algorithm must be able to decide that testing further attributes will not improve the predictive accuracy of the decision tree
* Let C be a collection of objects containing representatives of both classes, and let A be an attribute with random values that produces subsets $\{C_1, C_2, \dots, C_v\}$
* Unless the proportion of class P objects in each of the $C_i$ is exactly the same as the proportion of class P objects in C itself, branching on attribute A will give an apparent information gain
* It will therefore appear that testing attribute A is a sensible step, even though the values of A are random and so cannot help to classify the objects in C
* Using the chi-square test for stochastic independence has been found to be a successful method to screen out irrelevant attributes

## 6. Unknown attribute values
* What should be done when the set of information for the training set is incomplete?
* One way around the problem attempts to fill in an unknown value by utilizing information provided by context
	* Use Bayesian formalism to determine the probability that the object has value $A_i$ of A by examining the values of A in C as a function of their class
	* Use a decision-tree approach to determine the unknown values of an attribute
	* Use the most common value (naive)
* Treating "unknown" as a separate value is not a solution to the problem (could appear to give higher information gain)

## 7. The selection criterion
* Bratko's group encountered a medical induction problem in which the attribute selected by the gain criterion was judged by specialists to be less relevant than other attributes. This situation was also noted on other tasks, prompting Kononenko et al. to suggest that the gain criterion tends to favor attributes with many values
* ASSISTANT solves this problem by requiring that all tests have only two outcomes
	* Either the value is in a subset S of the values of the attribute A, or it is not
* The side-effects of this solution are
	* It can lead to decision trees that are even more unintelligible to human experts than is ordinarily the case, with unrelated attribute values being grouped together and with multiple tests on the same attribute
	* The subset criterion can require a large increase in computation
		* There are $2^{v-1} - 1$ different ways of specifying the distinguished subsets of attribute values
* When all attributes are binary, the gain ratio criterion has been found to give considerably smaller decision trees
* When the task includes attributes with large numbers of values, the subset criterion gives smaller decision trees that also have better predictive performance, but can require much more computation
* When these many-valued attributes are augmented by redundant attributes which contain the same information at a lower level of detail, the gain ratio gives decision trees with the greatest predictive accuracy

## 8. Conclusion
* While decision trees are fast to execute and can be very accurate, they leave much to be desired as representations of knowledge
* Experts who are shown such trees for classification tasks in their own domain often can identify little familiar material
* Work by Shapiro (1983) offers a possible solution to this problem. In his approach, called Structured Induction, a rule-formation task is tackled in the same style as structured programming. The task is solved in terms of a collection of notational super-attributes, after which the subtasks of inducing classification rules to find the values of the super-attributes are approached in the same top-down fashion

# See also

# References
* Quinlan, J. Ross. "Induction of decision trees." Machine learning 1.1 (1986): 81-106.
* http://cgis.cs.umd.edu/class/fall2009/cmsc828r/PAPERS/fulltext_Quilan_Ashwin_Kumar.pdf