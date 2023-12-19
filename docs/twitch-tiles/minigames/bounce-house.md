---
description: Bounce House is a minigame added in version v0.3 Alpha. It's based on the YouTube version of the same name.
---

{{ game.yt_version("common/bounce-house/") }}

# Bounce House

{{ game.info(
  slots_guaranteed = "8",
  slots_raffle     = "8",
  added            = "v0.3 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/common/bounce-house.png"
) }}

**Bounce House** is a minigame added in version v0.3 Alpha. It is based on the YouTube version's [tile of the same name](../../youtube-minigames/common/bounce-house.md).

## Gameplay

The tile consists of a 8 points cube and an elimination bucket of 1 point value rotating counter-clockwise around the center. At the bottom is a 8 point gap with two diagonal components on the side moving up and down. At the top is a spinning plate.

The players are dropped from the pipe at the top falling into the tile where they will be bounced around by the moving components at the bottom. When they touch the rotating cube or fall through the gap at the bottom, the displayed point value will be added to the player. If they touch the rotating bucket, the displayed point value will be removed from them and transferred to the king.

When there's one marble left, the game ends and the players are ranked by their elimination order. The longest surviving player wins.

## Point multiplier

A point multiplier is located at the top left of the tile, displaying x2.  
Every 10 seconds, it will increase the point values of the gap, block and bucket by a factor of 2. Every 3rd multiplication, a death ball will be spawned underneath the multiplier, eliminating every player that touches its spikes when exposed.

{{ game.history({
  'v0.3 Alpha': [
    'Minigame added'
  ],
  'v0.9 Alpha': [
    'Changed values. Spinning block is now 1 point, spinning bucket is -2 points and gap is 10 points.',
    'Spinning block increases value by 1 every time it gets hit. Gap increases value by 5 every time a marble passes through.'
  ],
  'v0.22 Alpha': [
    'Minigame can now appear in any rarity'
  ],
  'v0.24 Alpha': [
    'Added sudden death doubler'
  ]
}) }}