---
title: Anki recorder
created: 2020-02-18
taxonomy:
  type: post
  tag: [Problems, Anki]
  status: finished
---

# Problem
I'm learning a language using Anki flash cards and I'd like to record my progress over time. I'd like to be able to hear what I sounded like when I started learning.

# Solution
In 2017 I started learning Chinese. It was quite difficult for me given that I had very little prior experience with Asian languages, other than learning a bit of Japanese through a Rosetta Stone program where I couldn't figure out what they wanted me to learn based on images alone (they were trying to teach me color, but it was not obvious).

I imported the Memrise Mandarin Chinese flashcards level 1, 2 and 3 through the use of an Anki extension (https://github.com/wilddom/memrise2anki-extension) and I started my journey to learn. After practicing for a few weeks, I started being interested to have some form of recording of my progress, so I thought I could simply record my voice when I was asked to recall a word. Anki already had a recorder as part of its features so I simply piggy-backed on it to implement an Anki extension which I called the [Anki recorder](https://github.com/tomzx/anki-recorder).

When a new card is shown to you, the recorder starts right away. As you recall the word, you have to pronounce it. Once you've said the word, you can then check if you were correct or not, at which point the recording is stopped. Each record is timestamped, which allows you to listen to any of the words over time. It's rather funny to listen to yourself when you started learning a language and how you sound a few years later.

With this tool I was able to record over 193k audio samples over 3 years. There's a good chunk of those records that is only silence because it would also be triggered on cards with text only (where you had to remember how to write the word, or what the word meant).

Hopefully this tool can allow you to record your language learning progression and have fun after a few months of practice!

# References
* https://github.com/tomzx/anki-recorder
