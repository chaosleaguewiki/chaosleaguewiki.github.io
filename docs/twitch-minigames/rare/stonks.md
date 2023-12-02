---
description: Stonks is a rare minigame added in version v0.6 Alpha.
---

# Stonks

{{ game.info(
  rarity           = "rare",
  slots_guaranteed = "5",
  slots_raffle     = "4",
  added            = "v0.6 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/stonks.png"
) }}

**Stonks** is a rare minigame added in version v0.6 Alpha.

## Gameplay

The tile consists of a row of small rotating squares, below which there is a series of gaps. Above and below it there are 2 closed gaps moving diagonally.

The participating players' marbles are dropped and begin to collect points by falling through the gaps. After passing through the gap, it's point value is increased by it's initial value. If a marble falls to the bottom of the tile, it appears back in the game through the pipe at the top. If a marble falls into a closed gap, it is eliminated from the game and the given number of points is transfered to the king's balance. The negative value of closed gaps in the bottom-right corner is increased by it's initial value after a marble falls into one of them.

When there's one marble left, the game ends and the players are ranked by their elimination order. The longest surviving player wins.

{{ game.history({
  'v0.6 Alpha': [
    'Minigame added'
  ]
}) }}