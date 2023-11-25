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

### `!tomato [amount] @user` { #tomato }

Lets you throw `[amount]` of tomatos towards the mentioned user. This command costs you points, but the hit player will also lose points.

### `!givepoints [amount] @user` { #givepoints }

Gives the mentioned user `[amount]` of your pooints.

### `!givegold [amount] @user` { #givegold }

Gives the mentioned user `[amount]` of your gold.

### `!defend [amount]` { #defend }

Spend `[amount]` of your points to spread across 10 obsidian defense bricks.

### `!stats @user` { #stats }

Get statistics of the mentioned user.

### `!playlist`

Gives a link to the [Spotify Playlist][song-playlist] used for the music playing in the game.

### `!lava [bits]` { #lava }

Adds `[bits]` amount of bits to the lava progress bar. Once full will a bucket of lava be released. Players killed by the lava will lose half their points.

### `!water [bits]` { #water }

Adds `[bits]` amount of bits to the water progress bar. Once full will a bucket of water be released. It will extinguish existing lava previously spread through the [`!lava` command](#lava).

### `!cancelbid`

Cancels the current bid tickets or bits and removes the player from the queue. The invested tickets or bits won't be refunded.

### `!wiki`

Gives a link to this wiki you're currently reading.

## Throne Commands

Only executable by the current king on the throne.

### `!song [Artist - Song]` { #song }

Plays a song available on [this playlist][song-playlist]

### `!nextsong`

Skip to a new random song from [the playlist][song-playlist]

### `!toll [amount]` { #toll }

Set a point fee that each player has to pay when entering gameplay on a tile.  
`[amount]` can be a number between 0 and 15.

## Tile commands

Only executable by players participating in a tile, or by the king while a certain tile is being played.

### `!buy<number>` { #buy }

Usable in the minigame [Trail Shop] to buy one of three available Trails using Gold you've earned.

`buy1` buys the cheapest, `buy2` the second cheapest and `buy3` the most expensive trail.

### `!left`

Usable in the minigame [Royal Execution] by the current king.

Moves the spikes at the top of the tile to the left side.

### `!right`

Usable in the minigame [Royal Execution] by the current king.

Moves the spikes at the top of the tile to the right side.

### `!pull @user` { #pull }

Usable in the minigame [Danger Zone].

Pulls the mentioned player marble towards your own. Only players in the game can be pulled.

[song-playlist]: https://open.spotify.com/playlist/5gdz9X9y9hpBOCjYo6TI31
