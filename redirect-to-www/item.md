---
title: Redirect to www
created: 2006-06-04T06:28:16-05:00
taxonomy:
    type: post
    category: Sites
    tag: [apache, .htaccess, rewriterule]
---

<pre><code class="language-apache line-numbers">
Options +FollowSymLinks
RewriteEngine on
RewriteCond %{HTTP_HOST} ^your-domain-here\.com
RewriteRule ^(.*)$ http://www.your-domain-here.com/$1 [R=permanent,L]
</code></pre>

This code placed in your .htaccess will give you the possibility to send any visitor coming to your-domain-here.com to www.your-domain-here.com. This has a great advantage especially with search engines because all your pages will be referenced under the same "subdomain" as if you had both, you'd get www.your-domain-here.com links and your-domain-here.com links which would count as different pages.
