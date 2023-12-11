---
description: The game macro allows the insertion of game-page relevant content such as info boxes and history.
---

# Game

The game macro allows the insertion of game-page relevant content such as [info boxes](#game.info) and [history](#game.history).

## Available variants

There currently exist 4 variants.

{% raw %}
- [`{{ game.info(title, rarity, inputs, timer, rounds, slots_guaranteed, slots_raffle, added, img_url, img_alt, img_caption) }}`](#game.info)
- [`{{ game.history(versions) }}`](#game.history)
- [`{{ game.yt_version(path) }}`](#game.yt_version)
- [`{{ game.twitch_version(path) }}`](#game.twitch_version)
{% endraw %}

----

{% raw %}
## `{{ game.info(title, rarity, inputs, timer, rounds, slots_guaranteed, slots_raffle, added, img_url, img_alt, img_caption) }}` { #game.info }
{% endraw %}

The `game.info` macro adds a info box to the right of the page containing common info such as the rarity, required inputs, timer, etc.

### Options { #game.info-options }

| Option             | Required | Default      | Description                                                       |
|--------------------|----------|--------------|-------------------------------------------------------------------|
| `title`            | No       | (Page title) | The title to display at the top of the info box.                  |
| `rarity`           | No       | `Unknown`    | List of rarities this game can have.                              |
| `inputs`           | No       | `None`       | Any required inputs the game has.                                 |
| `timer`            | No       | `None`       | Time limit the game has.                                          |
| `rounds`           | No       | `None`       | Number of rounds the game has.                                    |
| `slots_guaranteed` | No       | `N/A`        | Number of slots where players are guaranteed to join the game.    |
| `slots_raffle`     | No       | `N/A`        | Number of slots that players have a chance to join the game with. |
| `added`            | No       | `Unknown`    | Version in which this game has been added.                        |
| `img_url`          | No       | `None`       | URL to an image to display. Can be a relative or absolute URL.    |
| `img_alt`          | No       | (Page title) | Alt text to set for the image.                                    |
| `img_caption`      | No       | (Empty)      | Caption to display below the image.                               |

### Example { #game.info-example }

/// tab | Default
//// tab | Raw
{% raw %}
```
{{ game.info() }}

Lorem Ipsum Dolor sit amet
```
{% endraw %}
////

//// tab | Result
{{ game.info() }}

Lorem Ipsum Dolor sit amet
////
///

/// tab | Changed Title
//// tab | Raw
{% raw %}
```
{{ game.info(
    title = "Title"
) }}

Lorem Ipsum Dolor sit amet
```
{% endraw %}
////

//// tab | Result
{{ game.info(
    title = "Title"
) }}

Lorem Ipsum Dolor sit amet
////
///

/// tab | Changed info
//// tab | Raw
{% raw %}
```
{{ game.info(
    rarity           = ["Epic"],
    inputs           = "!command",
    timer            = "30 Seconds",
    rounds           = "3",
    slots_guaranteed = "8",
    slots_raffle     = "2",
    added            = "v0.1 Alpha"
) }}

Lorem Ipsum Dolor sit amet
```
{% endraw %}
////

//// tab | Result
{{ game.info(
    rarity           = ["Epic"],
    inputs           = "!command",
    timer            = "30 Seconds",
    rounds           = "3",
    slots_guaranteed = "8",
    slots_raffle     = "2",
    added            = "v0.1 Alpha"
) }}

Lorem Ipsum Dolor sit amet
////
///

/// tab | Added Image
//// tab | Raw
{% raw %}
```
{{ game.info(
    img_url     = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–",
    img_alt     = "image",
    img_caption = "Image Caption"
) }}

Lorem Ipsum Dolor sit amet
```
{% endraw %}
////

//// tab | Result
{{ game.info(
    img_url     = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–",
    img_alt     = "image",
    img_caption = "Image Caption"
) }}

Lorem Ipsum Dolor sit amet
////
///

----

{% raw %}
## `{{ game.history(versions) }}` { #game.history }
{% endraw %}

The `game.history` macro adds a Info block containing the version history of a game.  
Do note that the `versions` option can/should be treated like JSON with each string holding an array of entries. See the [Example](#game.history-example) for how it may look.

### Options { #game.history-options }

| Option     | Required | Default      | Description                                                  |
|------------|----------|--------------|--------------------------------------------------------------|
| `versions` | Yes      | (Empty list) | List of version Strings containing entries of their changes. |

### Example { #game.history-example }

/// tab | Raw
{% raw %}
```
{{ game.history({
    'v0.1 Alpha': [
        'Minigame added'
    ],
    'v0.2 Alpha': [
        'Fixed a bug',
        'Added something'
    ]
}) }}
```
{% endraw %}
///

/// tab | Result
{{ game.history({
    'v0.1 Alpha': [
        'Minigame added'
    ],
    'v0.2 Alpha': [
        'Fixed a bug',
        'Added something'
    ]
}) }}
///

----

{% raw %}
## `{{ game.yt_version(path) }}` { #game.yt_version }
{% endraw %}

The `game.yt_version` macro adds a banner to the page, informing the reader about this page being about the Twitch version and that a page about the YouTube version exists.

### Options { #game.yt_version-options }

| Option | Required | Default | Description                                                                                                    |
|--------|----------|---------|----------------------------------------------------------------------------------------------------------------|
| `path` | Yes      | (Empty) | The path to link. This is relative to `/youtube-minigames/` and should not start with a `/` nor end with `.md` |

### Examples { #game.yt_version-examples }

/// tab | Raw
{% raw %}
```
{{ game.yt_version("common/bounce-house/") }}
```
{% endraw %}
///

/// tab | Result
{{ game.yt_version("common/bounce-house/") }}
///

----

{% raw %}
## `{{ game.twitch_version(path) }}` { #game.twitch_version }
{% endraw %}

The `game.twitch_version` macro adds a banner to the page, informing the reader about this page being about the YouTube version and that a page about the Twitch version exists.

### Options { #game.twitch_version-options }

| Option | Required | Default | Description                                                                                               |
|--------|----------|---------|-----------------------------------------------------------------------------------------------------------|
| `path` | Yes      | (Empty) | The path to link. This is relative to `/twitch-tiles/` and should not start with a `/` nor end with `.md` |

### Examples { #game.twitch_version-examples }

/// tab | Raw
{% raw %}
```
{{ game.twitch_version("minigames/bounce-house/") }}
```
{% endraw %}
///

/// tab | Result
{{ game.twitch_version("minigames/bounce-house/") }}
///