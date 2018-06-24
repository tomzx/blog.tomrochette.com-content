---
template: blog
body_classes: header-image fullwidth

sitemap:
    changefreq: monthly
    priority: 1.03

content:
    items: #@self.children
        @taxonomy:
            type: post
    order:
        by: header.created
        dir: desc
    limit: 5
    pagination: true

feed:
    description: An open book into a software engineer's mind.
    limit: 10

pagination: true
---

# tomrochette.com
## An open book into a software engineer's mind.
