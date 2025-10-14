---
title: My client-side only AI web application template
created: 2025-10-13
taxonomy:
  type: post
  tag: [templates, ai, web, javascript]
  status: draft
---

Over the past month I've started building client-side only AI web applications (e.g., [ai-text-editor](https://github.com/TomzxCode/ai-text-editor), a private ai-language-assistant to teach myself Chinese Mandarin).
I've gone with this approach because it lends itself very well to vibe coding with [vibe-kanban](https://www.vibekanban.com/).
I've configured the `Dev Server Script` option to open the `index.html` file in my browser and it works immediately, no need to build assets or start a backend server.
This speeds up iteration cycle considerably.

# The template

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
