---
title: My client-side only AI web application template
created: 2025-10-13
taxonomy:
  type: post
  tag: [templates, ai, web, javascript]
  status: draft
---

Over the past month I've started building a client-side only AI web application.
I've gone with this approach because it lends itself very well to vibe coding with vibe-kanban

* Use an `importmap` and javascript modules
* Imports
	* [llm.js](https://github.com/themaximalist/llm.js) to do LLM calls directly from the browser

```javascript
<script type="importmap">
{
    "imports": {
        "llm.js": "https://esm.sh/@themaximalist/llm.js@1.0.1?target=node",
    }
}
</script>
<script type="module" src="app.js"></script>
```
