---
description: Chat commands available for the Twitch version of Chaos League.
---

# Twitch Commands

## Global Commands

### `!attack`

Starts an attack against the current king by spawning you at the red pipe with the `!attack` text on it (bottom-center of the screen).  
You will then move up and start your attack.

You can read more about attacking the king on the [game mechanics page](../mechanics/index.md).

/// note
This command cannot be used while you're participating in a minigame.
///

### `!recruit`

Gives you a link to share. Every player that joins using your link will earn you 50% of the points they will earn.

### `!tomato [amount] @user`

Lets you throw `[amount]` of tomatos towards the mentioned user. This command costs you points, but the hit player will also lose points.

### `!givepoints [amount] @user`

Gives the mentioned user `[amount]` of your pooints.  
This command is only available for and usable on players currently alive on the field.

### `!defend [amount]`

Spend `[amount]` of your points to spread across 10 obsidian defense bricks.

### `!stats @user`

Get statistics of the mentioned user.

### `!playlist`

Gives a link to the [Spotify Playlist][song-playlist] used for the music playing in the game.

## Throne Commands

Only executable by the current king on the throne.

### `!song [song name + artist]`

Plays a song available on [this playlist][song-playlist]

### `!nextsong`

Skip to a new random song from [the playlist][song-playlist]

### `!toll [amount]`

Set a point fee that each player has to pay when entering gameplay on a tile.  
`[amount]` can be a number between 0 and 15.

### `!left` and `!right`

These commands can only be executed while the minigame [Royal Execution](../twitch-minigames/epic/royal-execution.md) is playing.  
Lowers a spike wall on the defined side of the tile, eliminating any player Marbles currently in it.

[song-playlist]: https://open.spotify.com/playlist/5gdz9X9y9hpBOCjYo6TI31
