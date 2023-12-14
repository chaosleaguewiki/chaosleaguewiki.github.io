---
description: Stonks is a minigame added in version v0.6 Alpha.
---

# Stonks

{{ game.info(
  rarity           = ["common", "rare", "epic", "legendary"],
  slots_guaranteed = "5",
  slots_raffle     = "4",
  added            = "v0.6 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/common/stonks.png"
) }}

**Stonks** is a minigame added in version v0.6 Alpha.

## Gameplay

The tile consists of a row of small rotating pins, below which there is a series of gaps. Above and below it there are 2 slowly moving gaps.

The players are droped at the top from the pipe into the tile after which they make their way through the row of rotating pins.  
Should they end up at the right will they fall down into one of the two buckets, eliminating them while also transferring the displayed point value from them to the king.

Falling through any other gap will give the player the displayed point value. Falling to any gap not having a grey line at the top will make it increase its value by a certain factor based on its line color.

After falling through any gap will they fall to the bottom of the tile after which they reappear at the top at the location of the pipe.

## Point multiplier

A point multiplier is located at the top left of the tile, displaying a x2.  
Every 10 seconds will it increase the point values of the gaps and buckets by a factor of 2. Every 3rd multiplication will a death ball be spawned underneath the multiplier, eliminating every player that touches its spikes when exposed.

{{ game.history({
  'v0.6 Alpha': [
    'Minigame added'
  ],
  'v0.22 Alpha': [
    'Minigame can now appear in any rarity'
  ],
  'v0.24 Alpha': [
    'Added sudden death doubler'
  ]
}) }}