---
description: Players can earn gold, a virtual currency of the game, while being king.
---

# Earning Gold

{{ image.right(
    url = "../../assets/images/earning-gold.png",
    
    title   = "Earning Gold",
    caption = "Image depicting the current king earning gold"
) }}

Players can earn gold, a virtual currency of the game, while being king.  
This earned gold can then be used on [Shop tiles](../twitch-tiles/index.md#available-shop-tiles) to receive cosmetics in return.

## How to obtain Gold

Every 5 minutes will gold be given to the current king. This means to earn gold, a player has to [capture the throne](attacking-the-king.md) and remain king until the 5 minute cooldown runs out.  
Gold is added to the chest for every tile that has been selected, with the gold value added being equal to the tile's initial prize value.

Other ways to earn gold is either by breaking gold ore blocks that are in the defense wall of the king, or receiving gold from another player who used the [`!givegold` command][givegold-command].

{{ game.history({
    'v0.8 Alpha': [
        'Gameplay mechanic added'
    ],
    'v0.25 Alpha': [
        'Travel indicator for gold changed from a number to individual coins'
    ],
    'v0.28 Alpha': [
        'Gold now increases for every selected tile and value increases based on the tile\'s rarity',
        'King now only earns gold every 5 minutes'
    ],
    'v0.30 Alpha': [
        'Gold ore blocks added to the wall, which when broken will give the player who broke it gold'
    ]
}) }}
