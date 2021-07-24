---
title: Managing your reading
created: 2021-04-21
taxonomy:
  type: post
  category: [General, Processes]
  status: draft
---

The process described below attempts to optimize reading quality books and enjoying the reading experience. As such, it promotes book exploration (discovery of new books) and reading books which have a high rating according to your own taste. Books which receive lower ratings (compared to other books) are moved down the reading priority list and will not be read until books that have higher priority (i.e., rating) either are finished reading or their rating decreases such that other books are now high priority.

* Pick highly read books (use a site like goodreads to identify those books).
* When reading a book, record the page you start and stop reading on, the time you start and stop reading and emit a rating for what you've read.
	* You can decide to optimize whether you want to optimize per page rating or per duration rating, that is, get the most value per page or by time spent reading.
* Add new books to your reading list regularly. Those books are considered as having the highest priority and are then added to the prioritized list of books according to its rating.
* When not reading a new book, read the books in order of priority and by interest at the time of reading.
* From time to time you may look at your list of prioritized books and decide whether the books with the lowest priority should ever be finished. In some cases it is reasonable to decide that certain books will never be read completely.
* As an alternative approach, one can use [multi-armed bandits algorithms](https://en.wikipedia.org/wiki/Multi-armed_bandit) to decide which book to read next. Given that we can convert multi-armed bandits problem into the problem of selecting which book to read next given a sequence of readings and associated rating ("rewards"), the various algorithms (such as Epsilon-greedy or UCB1) will provide us with the next book we should read.
	* Interestingly enough, an algorithm like UCB1 will promote reading books we've never read first over reading books we've already started reading.

# My reading strategy
* Read partially any book for which you haven't given any rating
* Rate what you have read on a 1 to 5 scale, 1 being very bad and 5 being very good (see [book rating](../book-rating/article.md))
* Compute the weighted rating of the book (the sum of rating times # of page associated to the reading divided by the total # of pages read so far for the book)
* Sort books by weighted rating, then average estimated amount of time left to complete

# References
* [How to prioritize which book to read](../../questions/2020/01/06/article.md)
* [Tracking my readings](../../questions/2020/02/18/article.md)
* [Read more books](../../questions/2020/03/01/article.md)
* [Reading fiction books](../../questions/2020/03/17/article.md)
* [Reading technical books](../../questions/2020/03/18/article.md)
* [Why I avoid reading books](../../questions/2020/03/21/article.md)
* [Book rating](../book-rating/article.md)
* [Reading Multiple Books at a Time](https://juvoni.com/reading-multiple-books)
