---
description: Chat commands available for the Twitch version of Chaos League.
---

# Twitch Commands

## Global Commands

### `!attack`

/// note | Command cannot be used while spawned in
///

Starts an attack against the current king by spawning you at the red pipe with the `!attack` text on it (bottom-center of the screen).  
You will then move up and start your attack.

You can read more about attacking the king on the [game mechanics page](../mechanics/index.md).

### `!recruit`

Gives you a link to share. Every player that joins using your link will earn you 50% of the points they earn.

[Learn more about recruiting](../mechanics/recruiting.md).

### `!tomato [amount] @user` { #tomato }

Lets you throw `[amount]` of tomatos towards the mentioned user. This command costs you points, but the hit player will also lose points.

### `!givepoints [amount] @user` { #givepoints }

{{ utils.removed(version="v0.24 Alpha", type="Command") }}

Gives the mentioned user `[amount]` of your points.

### `!givegold [amount] @user` { #givegold }

Gives the mentioned user `[amount]` of your gold.

### `!defend [amount]` { #defend }

Takes `[amount]` from your own points and spreads it evenly across the obsidian blocks in the defense wall of the king.

### `!stats @user` / `!mystats` { #stats }

Get statistics of the mentioned user. `!stats` without a mention or `!mystats` returns your statistics.

### `!playlist`

Gives a link to the [Spotify Playlist][song-playlist] used for the music playing in the game.

### `!lava [bits]` { #lava }

Adds `[bits]` amount of bits to the lava progress bar. Once full, a bucket of lava will be released. Players killed by the lava will lose half their points.  
`[bits]` needs to be a twitch cheer.

[Learn more about Lava and Water Bucket](../mechanics/water-and-lava-bucket.md).

### `!water [bits]` { #water }

Adds `[bits]` amount of bits to the water progress bar. Once full, a bucket of water will be released. It will extinguish existing lava previously spread through the [`!lava` command](#lava).  
`[bits]` needs to be a twitch cheer.

[Learn more about Lava and Water Bucket](../mechanics/water-and-lava-bucket.md).

### `!cancelbid` / `!unbid` { #cancelbid }

Cancels the current bid tickets or bits and removes the player from the queue. The invested tickets or bits won't be refunded.

### `!wiki`

Gives a link to this wiki you're currently reading.

### `!patreon`

Gives a link to DoodleChaos' Patreon page.

### `!discord`

Gives a link to DoodleChaos' Discord server.

### `!flipcoin`

Flips a coin for you, giving heads or tails at random.

## Throne Commands

Only executable by the current king on the throne.

### `!song [Artist - Song]` { #song }

Plays a song available on [this playlist][song-playlist].

### `!nextsong`

Skips to a new random song from [the playlist][song-playlist].

### `!toll [amount]` { #toll }

Sets a point fee that each player has to pay when going through the pipe on a tile.  
`[amount]` can be a number between 0 and 15.

## Tile commands

Only executable by players participating in a tile, or by the king while a certain tile is being played.

### `!buy<number>` { #buy }

Can only be used in [Shop Tiles](../twitch-tiles/index.md#available-shop-tiles).

Allows you to buy one of the displayed items at the displayed gold price. `!buy1` buys the cheapest, `!buy2` the middle and `!buy3` the most expensive item in the Shop Tile.

### `!left`

Usable in the minigame [Royal Execution] by the current king.

Moves the spikes at the top of the tile to the left side.

### `!right`

Usable in the minigame [Royal Execution] by the current king.

Moves the spikes at the top of the tile to the right side.

### `!pull @user` { #pull }

{{ utils.removed(version="v0.20 Alpha", type="Command") }}

Usable in the minigame [Danger Zone].

Pulls the mentioned player marble towards your own. Only players in the game can be pulled.

[song-playlist]: https://open.spotify.com/playlist/4P2LPOHaCPmSAyoTYEHuKA
