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

The participating players' marbles are dropped. Points can only be obtained by falling in the middle gap, which adds 10000 of them to player's balance. The two gaps neighboring the middle one, as well as the outside gaps, are closed. If a marble falls into either of them, it is eliminated from the game, and the 100 or 200 points are transfered to the king's balance. There are 2 gaps that have no effect on the marble. If a marble falls through one of them or through the middle gap, it appears back in the game through the pipe at the top.

When there's one marble left, the game ends, and the players are ranked by their elimination order. The longest surviving player wins.

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