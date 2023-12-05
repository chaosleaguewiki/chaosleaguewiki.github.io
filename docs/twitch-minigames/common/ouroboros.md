---
description: Ouroboros is a common minigame added in version v0.18 Alpha. It's based on the YouTube version of the same name.
---

# Ouroboros

{{ game.info(
  slots_guaranteed = "8",
  slots_raffle     = "8",
  added            = "v0.18 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/ouroboros.png"
) }}

**Ouroboros** is a common minigame added in version v0.18 Alpha. It's based on the YouTube version of the same name.

## Gameplay

the tile contains a circle made up of gaps and pillars rotating counter clockwise. At the bottom is a row of gaps, some of which are closed.

The circle has gaps with point values 1, 2, 3, 5, 6, 7, 8, 10 and 50. Only the 1, 5 and 50 tiles exist twice, facing each other.  
The bottom row of gaps has the values 5, -2, 5, -4, 5, -8 and 5 from left to right.

All tiles with the exception of the 50 tile won't change their value. Said tile will change their value based on the color it has while a player passes through it, meaning it can increase by any possible value.

{{ game.history({
  'v0.18 Alpha': [
    'Minigame Added'
  ],
  'v0.19 Alpha': [
    'Increased death rate',
    'Nerfed point earnings'
  ]
}) }}