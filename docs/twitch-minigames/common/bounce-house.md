---
description: Bounce House is a common minigame added in version v0.3 Alpha. It's based on the YouTuve version of the same name.
---

{{ game.yt_version("common/bounce-house/") }}

# Bounce House

{{ game.info(
  slots_guaranteed = "8",
  slots_raffle     = "8",
  added            = "v0.3 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/bounce-house.png"
) }}

**Bounce House** is a common minigame added in version v0.3 Alpha. It is based on the YouTube version's [tile of the same name](../../youtube-minigames/common/bounce-house.md).

## Gameplay

The tile consists of a 1 point block and an elimination bowl rotating around it's center and 2 moving structures with a 5 points gap between them. Just under the pipe, there's a small, rotating rectangle.

The participating players' marbles are dropped and begin to fly around the tile, launched by the moving structures. If a marble touches the point block, the given number of points is added to it's balance and the block's value is increased by 1. If a marble falls through the gap, 5 points are added to it's balance, it appears back in the game through the pipe at the top and the gap's value is increased by 5. If a marble gets into the rotating bowl, it is eliminated from the game and 2 points are transfered to the king's balance.

When there's one marble left, the game ends and the players are ranked by their elimination order. The longest surviving player wins.

{{ game.history({
  'v0.3 Alpha': [
    'Minigame Added'
  ],
  'v0.9 Alpha': [
    'Changed values. Spinning block is now 1 point, spinning bucket -2 points and gap is 10 points.',
    'Spinning block increases value by 1 every time it gets hit. Gap increases value by 5 every time a marble passes through.'
  ]
}) }}