---
title: "K2 new slider option: killing your chances of getting spidered?"
created: 2006-05-25T06:16:50-05:00
taxonomy:
  type: post
  tag: [sites, k2, themes, wordpress, web-crawler]
---

Well, it took me some time until I realise that this cool slider bar option as something negative about it: it hides contains from search engines spiders.

Using AJAX coding, the only one who can trigger the request to the server are the users, a bot wouldn't be able to read any content except the one that's appearing on the front page.

Is this going to kill my chances of getting spidered?
Actually yes. As the top navigation (the ­­Older and Newer links) are also programmed to trigger javascript, the spider cannot go anywhere. When it reads a # link, it just stays on the same page, no new content for the bot to read.

The thing though is that the spider can still view your list of latest post which are static. When they go to theses pages, nothing is in AJAX format, the links are all going to another post so it's fine. The only impact the slider has is it removes a bit of power from your front page.
