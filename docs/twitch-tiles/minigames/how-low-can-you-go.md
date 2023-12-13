---
description: How Low Can You Go is a minigame added in version v0.1 Alpha. It is based on the YouTube version of the same name.
---

{{ game.yt_version("common/how-low-can-you-go/") }}

# How Low Can You Go

{{ game.info(
  rarity           = ["common", "rare", "epic", "legendary"],
  slots_guaranteed = "8",
  slots_raffle     = "4",
  added            = "v0.1 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/how-low-can-you-go.png"
) }}

**How Low Can You Go** is a minigame added in version v0.1 Alpha. It is based on the YouTube version's [tile of the same name](../../youtube-minigames/common/how-low-can-you-go.md).

## Gameplay

The tile consists of 2 circles moving horizantally, below which there are 3 rows with several gaps.

The participating players' marbles are dropped and begin to collect points by falling through the gaps. If a marble falls through the last row, it appears back in the game through the pipe at the top. If a marble falls into a closed gap, it is eliminated from the game and a given number of points is transfered to the king's balance.  
With the exception of closed gaps does every gap increase its point value by one for every marble falling through it.

When there's one marble left, the game ends and the players are ranked by their elimination order. The longest surviving player wins.

{{ game.history({
  'v0.1 Alpha': [
    'Minigame added'
  ],
  'v0.16 Alpha': [
    '(Experimental) Gaps now increase in value every time a player passes through'
  ],
  'v0.17 Alpha': [
    'Nerfed survival Rate'
  ],
  'v0.22 Alpha': [
    'Minigame can now appear in any rarity',
    'Minigame buffed'
  ],
  'v0.24 Alpha': [
    'Added sudden death doubler'
  ]
}) }}