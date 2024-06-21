---
template: blog
body_classes: fullwidth

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
    title: tomrochette.com
    description: What's up with my life
    limit: 1000

pagination: true
---
