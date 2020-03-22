---
title: Greg Linden - Amazon.com Recommendations - Item-to-Item Collaborative Filtering (2003)
created: 2017-12-09
taxonomy:
  category: [Machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
* There are three common approaches to solving the recommendation problem:
	* traditional collaborative filtering
	* cluster models
	* search-based methods
* Our algorithm's online computation scales independently of the number of customers and number of items in the product catalog

## Recommendation Algorithms
* Most recommendation algorithms start by finding a set of customers whose purchased and rated items overlap the user's purchased and rated items. The algorithm aggregates items from these similar customers, eliminates items the user has already purchased or rated, and recommends the remaining items to the user

### Traditional Collaborative Filtering
* Represents a customer as an N-dimensional vector of items, where $N$ is the number of distinct catalog items
* The components of the vector are positive for purchased or positively rated items and negative for negatively rated items
* To compensate for best-selling items, the algorithm typically multiples the vector components by the inverse frequency, making less well-known items much more relevant
* Using collaborative filtering to generate recommendations is computationally expensive. It is $O(MN)$ in the worst case, where $M$ is the number of customers and $N$ is the number of product catalog items
* Because the average customer vector is extremely sparse, the algorithm's performance tends to be closer to $O(M + N)$
* It is possible to partially address these scaling issues by reducing the data size. We can reduce $M$ by randomly sampling the customers or discarding customers with fewer purchases, and reduce $N$ by discarding very popular or unpopular items
* Unfortunately, all these methods also reduce recommendation quality in several ways
	* If the algorithm examines only a small customer sample, the selected customers will be less similar to the user
	* Item-space partitioning restricts recommendations to a specific product or subject area
	* If the algorithm discards the most popular or unpopular items, they will never appear as recommendations, and customers who have purchased only those items will not get recommendations

### Cluster Models
* Clustering models divide the customer base into many segments and treat the task as a classification problem
* The algorithm's goal is to assign the user to the segment containing the most similar customers
* Using a similarity metric, a clustering algorithm groups the most similar customers together to form clusters or segments
* Because optimal clustering over large data sets is impractical, most applications use various forms of greedy clustering generation
* Clustering models have better online scalability and performance than collaborative filtering because they compare the user to a controlled number of segments rather than the entire customer base
	* However, recommendation quality is low

### Search-Based Methods
* Given the user's purchased and rated items, the algorithm constructs a search query to find other popular items by the same author, artist, or director, or with similar keywords or subjects
* For users with thousands of purchases, it's impractical to base a query on all the items
	* The algorithm must use a subset or summary of the data, reducing quality
* In all cases, recommendation quality is relatively poor

## Item-to-Item Collaborative Filtering
### How It Works
* Rather than matching the user to similar customers, item-to-item collaborative filtering matches each of the user's purchased and rated items to similar items, then combines those similar items into a recommendation list
* To determine the most-similar match for a given item, the algorithm builds a similar-items table by finding items that customers tend to purchase together
* This offline computation of the similar-items table is extremely time intensive, with $O(N^2M)$ as worst case. In practice, however, it's closer to $O(NM)$, as most customers have very few purchases

### Scalability: A Comparison
* For very large data sets, a scalable recommendation algorithm must perform the most expensive calculations offline

# See also

# References
* Linden, Greg, Brent Smith, and Jeremy York. "Amazon. com recommendations: Item-to-item collaborative filtering." IEEE Internet computing 7.1 (2003): 76-80.
