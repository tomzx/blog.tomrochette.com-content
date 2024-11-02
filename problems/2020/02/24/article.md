---
title: Rotten Tomatoes ratings exporter
created: 2020-02-24
taxonomy:
  type: post
  tag: [Problems, PHP]
  status: finished
---

# Problem
I have rated a lot of movies on Rotten Tomatoes and I'd like to export them to a text format. I also know PHP. How can I do that?

# Solution
In 2013 I wrote [Rotten Tomatoes ratings exporter](https://github.com/tomzx/rotten-tomatoes-exporter) for the purpose of exporting the movies I had rated into a format I could read and also store.

To automate the process of acquiring the ratings, I wrote a small class which needs information available in the site's cookies once you are logged in. With this information in hand, it is then possible to fetch the ratings from the website and store them in any desired format, given that the data returned to you is a plain PHP array.

# References
* https://github.com/tomzx/rotten-tomatoes-exporter
