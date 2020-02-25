---
title: IMDb ratings importer
created: 2020-02-23
taxonomy:
  type: post
  category: [Problems, PHP]
  status: finished
---

# Problem
I have movie ratings that I would like to import into IMDb. I also happen to know PHP. How can I do that?

# Solution
In 2013 I wrote [IMDb ratings importer](https://github.com/tomzx/imdb-importer) for the purpose of importing ratings I had created in another system (Rotten Tomatoes). I wanted to import my ratings into IMDb so that I could use their statistics reporting tools, which let you see your distribution of ratings and the distribution of the release year of the movies you've seen. A friend of mine also had his bot send a message to our discussion channel whenever one of us would update their ratings after watching a movie.

The library is pretty straightforward. It expects you to provide it with a string that uniquely identifies your cookie on the server side.

# References
* https://github.com/tomzx/imdb-importer
