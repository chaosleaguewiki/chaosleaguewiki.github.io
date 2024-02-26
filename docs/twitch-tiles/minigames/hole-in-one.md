---
description: Hole In One is a minigame added in version v0.1 Alpha. It is based on the YouTube version of the same name.
---

# Hole In One

{{ game.info(
  rarity           = ["legendary"],
  slots_guaranteed = "8",
  slots_raffle     = "8",
  added            = "v0.1 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/legendary/hole-in-one.png"
) }}

**Hole In One** is a minigame added in version v0.1 Alpha. It is based on the YouTube version's tile of the same name.

## Gameplay

The tile consists of 2 rows of small rotating squares, below which there is one row of gaps.

The participating players' marbles are dropped. Points can only be obtained by falling in the middle gap, which adds 10000 points to the player's balance. The two gaps neighboring the middle one, as well as the outside gaps, are closed. If a marble falls into either of them, it is eliminated from the game, and the 100 or 200 points are transferred to the king's balance. There are 2 gaps that have no effect on the marble. If a marble falls through one of them or through the middle gap, it appears back in the game through the pipe at the top.

When there's one marble left, the game ends, and the players are ranked by their elimination order. The longest surviving player wins.

## Point multiplier and Death Ball

A point multiplier is located in the top-left corner of the tile, displaying a `x2` text. Every 15 seconds, purple text displaying `x2` fly towards the buckets at the bottom, multiplying their value by a factor of 2.

Starting with the 6th multiplication, a [Death Ball](../../mechanics/death-ball.md) is spawned with every subsequent multiplication.

## Images

### Tile rarities

![legendary](../../assets/images/minigames/twitch/legendary/hole-in-one.png "Legendary rarity version"){ loading="lazy" style="max-width: 20%;" }

{{ game.history({
  'v0.1 Alpha': [
    'Minigame added'
  ],
  'v0.6 Alpha': [
    'Closed outside gaps and made them remove 100 points'
  ],
  'v0.20 Alpha': [
    'Buffed point distribution'
  ]
}) }}