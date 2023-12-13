---
description: Markdownify is a filter that allows to parse markdown inside a html text by sending it through the Markdown parser used by MkDocs (Python-Markdown).
---

# Markdownify

**Markdownify** is a filter that allows to parse markdown inside a html text by sending it through the Markdown parser used by MkDocs (Python-Markdown).  
This also includes any markdown extensions added to the Markdown library.

### Example

/// tab | Raw
{% raw %}
```
<p>{{ "Parsing **Markdown** inside some HTML! :thumbsup:" | markdownify }}</p>
```
{% endraw %}
///

/// tab | Result
<p>{{ "Parsing **Markdown** inside some HTML! :thumbsup:" | markdownify }}</p>
///