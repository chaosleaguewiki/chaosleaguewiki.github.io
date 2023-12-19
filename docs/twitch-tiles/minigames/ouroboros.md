---
description: Ouroboros is a minigame added in version v0.18 Alpha. It's based on the YouTube version of the same name.
---

# Ouroboros

{{ game.info(
  slots_guaranteed = "8",
  slots_raffle     = "8",
  added            = "v0.18 Alpha",
  
  img_url = "../../../assets/images/minigames/twitch/common/ouroboros.png"
) }}

**Ouroboros** is a minigame added in version v0.18 Alpha. It's based on the YouTube version of the same name.

## Gameplay

The tile contains a circle made up of gaps and pillars rotating counter-clockwise. In the center is a closed gap slowly rotating clockwise. At the bottom is a row of gaps, some of which are closed.

The circle has gaps with the initial point values 1, 2, 3, 5, 6, 7, 8, 10 and 25. Only gaps with 1, 5 and 50 points exist twice in the circle, facing each other.  
The bottom row of gaps has 2 point gaps with -1, -2 and -4 gaps put in-between from left to right.

Only the 25 points gap will change its value whenever a player passes through it, which is indicated by the colored line of it cycling through different colors. The value it increases by is random.

{{ game.history({
  'v0.18 Alpha': [
    'Minigame Added'
  ],
  'v0.19 Alpha': [
    'Increased death rate',
    'Nerfed point earnings'
  ],
  'v0.22 Alpha': [
    'Minigame can now appear in any rarity',
    'Minigame buffed'
  ],
  'v0.24 Alpha': [
    'Added sudden death doubler'
  ]
}) }}