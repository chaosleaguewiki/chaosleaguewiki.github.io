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
  
  img_url = "../../../assets/images/minigames/twitch/common/how-low-can-you-go.png"
) }}

**How Low Can You Go** is a minigame added in version v0.1 Alpha. It is based on the YouTube version's [tile of the same name](../../youtube-minigames/common/how-low-can-you-go.md).

## Gameplay

The tile consists of 2 circles moving horizantally, below which there are 3 rows with several gaps and buckets.

The player marbles are droped from the pipe at the top into the tile after which they will find their way through open gaps or closed buckets with point values displayed.  
Should the player end up in a bucket will the displayed point value get removed from them and transferred to the current king while their marble also gets eliminated. Falling through a gap gives the player the displayed point value.

Each row has one bucket with gaps filling the remaining area. The first row has gaps with an initial point value of 2 and a bucket with an initial point value of 2. The second row has the values of the first row doubled and the 3rd row has its point values be doubled from the 2nd row.

Once the player reaches the bottom of the tile will they reappear at the top at the location of the pipe, repeating the cicle.

## Point multiplier

A point multiplier is located at the top left of the tile, displaying a x2.  
Every 10 seconds will it increase the point values of the gaps and buckets by a factor of 2. Every 3rd multiplication will a death ball be spawned underneath the multiplier, eliminating every player that touches its spikes when exposed.

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