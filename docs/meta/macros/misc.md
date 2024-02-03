---
description: Miscellaneous macros that aren't part of a specific category.
---

# Miscellaneous

Miscellaneous macros that aren't part of a specific category.

## Available variants

There currently exist 2 variants.

{% raw %}
- [`{{ read_json_file(path) }}`](#read_json_file)
- [`{{ read_file(path) }}`](#read_file)
{% endraw %}

{% raw %}
## `{{ read_json_file(path) }}` { #read_json_file }
{% endraw %}

This macro reads the content of a JSON file located at the provided path (Relative to the root folder of the project) and allows you to use it through the jinja2 templating system.

### Options { #read_json_file-options }

| Option      | Required | Default | Description                                               |
|-------------|----------|---------|-----------------------------------------------------------|
| `file_path` | Yes      | (Empty) | Location of the file relative to the root of the project. |

### Example { #read_json_file-example }

/// tab | Raw
{% raw %}
```
{% set json = read_json_file("docs/assets/quip_battle_prompts.json") %}
{% if json -%}
  <ul>
  {% for entry in json %}
    <li>{{ entry }}</li>
  {% endfor %}
  </ul>
{%- endif %}
```
{% endraw %}
///

/// tab | Result
{% set json = read_json_file("docs/assets/quip_battle_prompts.json") %}
{% if json -%}
  <ul>
  {% for entry in json %}
    <li>{{ entry }}</li>
  {% endfor %}
  </ul>
{%- endif %}
///

----

{% raw %}
## `{{ read_file(path) }}` { #read_file }
{% endraw %}

This macro reads the content of a file located at the provided path (Relative to the root folder of the project) and allows you to use it through the jinja2 templating system.

### Options { #read_file-options }

| Option      | Required | Default | Description                                               |
|-------------|----------|---------|-----------------------------------------------------------|
| `file_path` | Yes      | (Empty) | Location of the file relative to the root of the project. |

### Example { #read_file-example }

/// tab | Raw
{% raw %}
````
{% set file = read_file(".snippets/games.md") %}
{% if file %}
```markdown
{% for line in file -%}
  {{ line }}
{%- endfor %}
```
{% endif %}
````
{% endraw %}
///

/// tab | Result
{% set file = read_file(".snippets/games.md") %}
{% if file %}
```markdown
{% for line in file -%}
  {{ line }}
{%- endfor %}
```
{% endif %}
///
