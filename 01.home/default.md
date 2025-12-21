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

pagination: true
---
