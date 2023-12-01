---
description: The games.md Snippet contains links to all the games available in Chaos League.
---

# Games

/// info | Automatically included
This Snippet is automatically included in all files and does not need to be added manually.
///

The `games.md` Snippet contains links to all the games available in Chaos League.

## Content

The below list is pulled automatically from the snippet file itself.

```markdown
{% set file = read_file(".snippets/games.md") %}
{% for line in file -%}
  {{ line }}
{%- endfor %}
```