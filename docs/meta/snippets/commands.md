---
description: The commands.md Snippet contains links to all the commands available in Chaos League.
---

# Commands

/// info | Automatically included
This Snippet is automatically included in all files and does not need to be added manually.
///

The `commands.md` Snippet contains links to all the commands available in Chaos League.

## Content

The below list is pulled automatically from the snippet file itself.

```markdown
{% set file = read_file(".snippets/commands.md") %}
{% for line in file -%}
  {{ line }}
{%- endfor %}
```