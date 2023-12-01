---
description: Information about the wiki itself such as templates, snippets, etc.
---

# Meta

Pages under this section cover parts of the Chaos League Wiki itself and not the actual game or parts of it.  
The main goal is to help people understand how the wiki's mechanics work so that they can contribute more easily to it.

## Macros

Macros are used to inject customizable content into the page or for other things that a tool like [Snippets](#snippets) cannot solve.

- [Image](macros/image.md)
    - [`image.left`](macros/image.md#image.left)
    - [`image.right`](macros/image.md#image.right)
    - [`image.img`](macros/image.md#image.img)
- [Game](macros/game.md)
    - [`game.info`](macros/game.md#game.info)
    - [`game.history`](macros/game.md#game.history)
    - [`game.yt_version`](macros/game.md#game.yt_version)
    - [`game.twitch_version`](macros/game.md#game.twitch_version)
- [Miscellaneous](macros/misc.md)
    - [`read_json_file`](macros/misc.md#read_json_file)
    - [`read_file`](macros/misc.md#read_file)

## Snippets

Snippets are text files which are inserted using the `--8<-- "<filename>.<extension>"` format.  
Unlike [Macros](#macros) can you not define any options for the snippet to include.

### Automatically added

These Snippets are added automatically to all pages of the wiki.

- [Commands](snippets/commands.md)
- [Games](snippets/games.md)
- [Game Terminology](snippets/game-terminology.md)

### Other Snippets

These Snippets are not automatically added to pages and therefore need to manually be added.

- [Unreleased](snippets/unreleased.md)