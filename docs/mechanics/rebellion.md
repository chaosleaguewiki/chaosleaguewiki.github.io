---
description: Rebellion is a game mechanic where people can give bits to start a multiplier that increases points earned amongst other effects.
---

# Rebellion

{{ image.right(
    url     = "../../assets/images/rebellion-animation.webp",
    title   = "Rebellion",
    caption = "The animation played when someone starts a rebellion."
) }}

Rebellion is a game mechanic where people can give bits to start a multiplier that increases points earned amongst other effects.

## How it works

Players can cheer 200 or more bits to start a rebellion. When a rebellion is started will a circle appear around the marble of the player who started it. This circle will have certain effects on tiles and other mechanics tied to the multiplier value displayed. See the [Effects section](#effects) for details.

The default multiplier starts at 2, but increases by one with every addition 100 bits added. In addition is the duration of the rebellion also increased.  
The duration is 40 seconds per dollar worth of bits spent.

## Effects

{{ image.right(
    url = "../../assets/images/rebellion-effect.png",
    caption = "The rebellion circle affecting the gaps in its radius, changing their value"
) }}

The circle around the rebellion starter has specific effects on players, tiles and other mechanics, depending on the situation. Players need to be inside the circle to receive the effects.

### Bidding spawn tickets

When a player bids spawn tickets to participate while in the effect area of the rebellion leader will the tickets they spent be multiplied. This will also affect the prize a player can win on a tile.

Should the rebellion leader not be king and also not be in a tile's guaranteed slots will their effect area be located at the bottom of the queue, applying the multiplier to any tickets a player bids for this tile while not already being in the guaranteed slots (Outside the effect radius).

### Point gaps

Gaps giving or taking points have their values multiplied while in the effect area of the rebellion leader.

Skull gaps in [Zero or Hero] also turn into Angel gaps. These gaps do not take away any points from the player while still eliminating them.

{{ game.history({
    'v0.15 Alpha': [
        'Gameplay mechanic added'
    ],
    'v0.18 Alpha': [
        'Duration buffed to 40 sec/dollar'
    ]
}) }}