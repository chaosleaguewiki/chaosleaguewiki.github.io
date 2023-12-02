---
description: 
---

# Utils

The utils macro contains different utility macros to create more complex stuff more easily.

## Available variants

There currently exists 1 variant.

{% raw %}
- [`{{ utils.table(entries) }}`](#utils.table)
{% endraw %}

----

{% raw %}
## `{{ utils.table(entries) }}` { #utils.table }
{% endraw %}

The `utils.table` macro adds a table not unlike the [`game.history` table](game.md#game.history), meaning multiple collumns on the right side can belong to the same column on the left side.  
Do note that the `entries` option can/should be treated like JSON with each string holding an array of entries. See the [Example](#utils.table-example) for how it may look.

### Options { #utils.table-options }

| Option    | Required | Default      | Description                                                |
|-----------|----------|--------------|------------------------------------------------------------|
| `entries` | Yes      | (Empty list) | List of Entry Strings containing entries of their changes. |

### Example { #utils.table-example }

/// tab | Raw
{% raw %}
```
{{ utils.table({
    'Added': [
        'Something'
    ],
    'Fixed': [
        'A bug',
        'Something else'
    ]
}) }}
```
{% endraw %}
///

/// tab | Result
{{ utils.table({
    'Added': [
        'Something'
    ],
    'Fixed': [
        'A bug',
        'Something else'
    ]
}) }}
///