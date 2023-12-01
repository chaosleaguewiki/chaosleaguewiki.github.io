---
description: The image macro allows the inclusion of images with optional alignment and caption.
---

# Image

The `image` macro allows the inclusion of images with optional alignent and caption.

## Available variants

There currently exist 3 variants to use:

{% raw %}
- [`{{ image.left(url, title, alt, caption) }}`](#image.left)
- [`{{ image.right(url, title, alt, caption) }}`](#image.right)
- [`{{ image.img(url, alt, caption) }}`](#image.img)
{% endraw %}

{% raw %}
## `{{ image.left(url, title, alt, caption) }}` { #image.left }
{% endraw %}

The `image.left` macro inserts an image aligned to the left using an info box like the [`game.info` macro](game.md#game.info).

### Options { #image.left-option }

| Option    | Required | Default | Description                                                   |
|-----------|----------|---------|---------------------------------------------------------------|
| `url`     | Yes      | None    | The URL to the image. This can be a relative or absolute URL. |
| `title`   | No       | None    | Title to display above the image itself.                      |
| `alt`     | No       | `image` | The alt text to set for the image.                            |
| `caption` | No       | None    | The caption to display below the image.                       |

### Examples { #image.left-examples }

/// tab | Default
//// tab | Raw
{% raw %}
```
{{ image.left(
    url = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–"
) }}
{% endraw %}

Lorem Ipsum Dolor sit amet
```
////

//// tab | Result
{{ image.left(
    url = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–"
) }}

Lorem Ipsum Dolor site amet
////
///

/// tab | With title
//// tab | Raw
{% raw %}
```
{{ image.left(
    url   = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–",
    title = "Title"
) }}
{% endraw %}

Lorem Ipsum Dolor sit amet
```
////

//// tab | Result
{{ image.left(
    url   = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–",
    title = "Title"
) }}

Lorem Ipsum Dolor site amet
////
///

/// tab | With caption
//// tab | Raw
{% raw %}
```
{{ image.left(
    url     = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–",
    caption = "Caption"
) }}
{% endraw %}

Lorem Ipsum Dolor sit amet
```
////

//// tab | Result
{{ image.left(
    url     = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–",
    caption = "Caption"
) }}

Lorem Ipsum Dolor site amet
////
///

----

{% raw %}
## `{{ image.right(url, title, alt, caption) }}` { #image.right }
{% endraw %}

The `image.right` macro inserts an image aligned to the right using an info box like the [`game.info` macro](game.md#game.info).

### Options { #image.right-option }

| Option    | Required | Default | Description                                                   |
|-----------|----------|---------|---------------------------------------------------------------|
| `url`     | Yes      | None    | The URL to the image. This can be a relative or absolute URL. |
| `title`   | No       | None    | Title to display above the image itself.                      |
| `alt`     | No       | `image` | The alt text to set for the image.                            |
| `caption` | No       | None    | The caption to display below the image.                       |

### Examples { #image.right-examples }

/// tab | Default
//// tab | Raw
{% raw %}
```
{{ image.right(
    url = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–"
) }}
{% endraw %}

Lorem Ipsum Dolor sit amet
```
////

//// tab | Result
{{ image.right(
    url = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–"
) }}

Lorem Ipsum Dolor site amet
////
///

/// tab | With title
//// tab | Raw
{% raw %}
```
{{ image.right(
    url   = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–",
    title = "Title"
) }}
{% endraw %}

Lorem Ipsum Dolor sit amet
```
////

//// tab | Result
{{ image.right(
    url   = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–",
    title = "Title"
) }}

Lorem Ipsum Dolor site amet
////
///

/// tab | With caption
//// tab | Raw
{% raw %}
```
{{ image.right(
    url     = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–",
    caption = "Caption"
) }}
{% endraw %}

Lorem Ipsum Dolor sit amet
```
////

//// tab | Result
{{ image.right(
    url     = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–",
    caption = "Caption"
) }}

Lorem Ipsum Dolor site amet
////
///

----

{% raw %}
## `{{ image.img(url, alt, caption) }}` { #image.img }
{% endraw %}

The `image.img` macro inserts the provided image, optionally with a caption.

### Options { #image.img-option }

| Option    | Required | Default | Description                                                   |
|-----------|----------|---------|---------------------------------------------------------------|
| `url`     | Yes      | None    | The URL to the image. This can be a relative or absolute URL. |
| `alt`     | No       | `image` | The alt text to set for the image.                            |
| `caption` | No       | None    | The caption to display below the image.                       |

### Examples { #image.img-examples }

/// tab | Default
//// tab | Raw
{% raw %}
```
{{ image.img(
    url = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–"
) }}
{% endraw %}

Lorem Ipsum Dolor sit amet
```
////

//// tab | Result
{{ image.img(
    url = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–"
) }}

Lorem Ipsum Dolor site amet
////
///

/// tab | With caption
//// tab | Raw
{% raw %}
```
{{ image.img(
    url     = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–",
    caption = "Caption"
) }}
{% endraw %}

Lorem Ipsum Dolor sit amet
```
////

//// tab | Result
{{ image.img(
    url     = "https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–",
    caption = "Caption"
) }}

Lorem Ipsum Dolor site amet
////
///